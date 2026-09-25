"""Project-aware metadata rendering tests."""

from pathlib import Path

from doc_gen.core.structure.common.models import StructureConfig
from doc_gen.core.structure.factory import StructureFactory
from doc_gen.core.structure.generator.markdown_generator import MarkdownGenerator
from doc_gen.core.structure.metadata.registry import MetadataRegistry
from doc_gen.core.structure.scanner.enums import ProjectType
from doc_gen.core.structure.scanner.models import ProjectFingerprint


def test_apps_script_metadata_combines_common_and_framework_entries() -> None:
    """Framework catalogs extend rather than replace common documentation."""

    catalog = MetadataRegistry().resolve(
        ProjectFingerprint(
            primary_type=ProjectType.GOOGLE_APPS_SCRIPT,
            ecosystems=("javascript", "typescript"),
            frameworks=("google-apps-script",),
            tools=("clasp", "pnpm"),
        )
    )

    assert "README.md" in catalog.root_files
    assert "package.json" in catalog.root_files
    assert "src/appsscript.json" in catalog.root_files
    assert "src" in catalog.directories


def test_python_metadata_is_added_only_for_python_projects() -> None:
    """Python tooling should not leak into unrelated repository catalogs."""

    generic_catalog = MetadataRegistry().resolve(
        ProjectFingerprint(primary_type=ProjectType.GENERIC)
    )
    python_catalog = MetadataRegistry().resolve(
        ProjectFingerprint(
            primary_type=ProjectType.PYTHON,
            ecosystems=("python",),
        )
    )

    assert "pyproject.toml" not in generic_catalog.root_files
    assert "pyproject.toml" in python_catalog.root_files
    assert "pytest.ini" in python_catalog.root_files


def test_root_metadata_supports_nested_safe_manifest_paths(tmp_path: Path) -> None:
    """Resolved catalogs can describe safe nested framework manifests."""

    manifest = tmp_path / "src" / "appsscript.json"
    manifest.parent.mkdir()
    manifest.write_text("{}", encoding="utf-8")

    catalog = MetadataRegistry().resolve(
        ProjectFingerprint(
            primary_type=ProjectType.GOOGLE_APPS_SCRIPT,
            ecosystems=("javascript",),
            frameworks=("google-apps-script",),
        )
    )

    detected = [name for name in catalog.root_files if (tmp_path / name).exists()]
    assert detected == ["src/appsscript.json"]


def test_generated_apps_script_document_is_project_aware_and_hides_local_config(
    tmp_path: Path,
) -> None:
    """End-to-end generation should render context without exposing clasp config."""

    (tmp_path / "package.json").write_text(
        '{"devDependencies":{"@google/clasp":"latest","typescript":"latest"}}',
        encoding="utf-8",
    )
    (tmp_path / ".clasp.json").write_text(
        '{"scriptId":"private-test-value"}',
        encoding="utf-8",
    )
    source = tmp_path / "src"
    source.mkdir()
    (source / "appsscript.json").write_text("{}", encoding="utf-8")
    (source / "main.ts").write_text("export {};\n", encoding="utf-8")

    config = StructureConfig(
        target_directory=tmp_path,
        max_depth=4,
        show_files=True,
        collapse_dirs=set(),
        smart_mode=False,
        project_type=None,
    )
    scanner = StructureFactory.create_scanner(config=config)
    content = (
        MarkdownGenerator(
            config=config,
            scanner_service=scanner,
        )
        .generate_document()
        .content
    )

    assert "`google-apps-script`" in content
    assert "`typescript`" in content
    assert "`clasp`" in content
    assert "`src/appsscript.json`" in content
    assert ".clasp.json" not in content
    assert "private-test-value" not in content
    assert "## Recognized Files" in content
    assert "## Root Files" not in content
    assert "### `src/`\n\n" in content
    assert content.endswith("\n")
    assert "\n\n\n" not in content
    assert all(line == line.rstrip(" \t") for line in content.splitlines())
