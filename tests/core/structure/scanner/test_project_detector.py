"""Project fingerprint detection across supported repository ecosystems."""

import json
from pathlib import Path

import pytest

from doc_gen.core.structure.scanner.enums import ProjectType
from doc_gen.core.structure.scanner.project_detector import ProjectDetector


def write_json(path: Path, data: dict) -> None:
    """Write deterministic JSON test data."""

    path.write_text(json.dumps(data), encoding="utf-8")


def test_detects_google_apps_script_without_reading_local_clasp_config(
    tmp_path: Path,
) -> None:
    """Clasp dependencies and manifests identify Apps Script safely."""

    write_json(
        tmp_path / "package.json",
        {"devDependencies": {"@google/clasp": "latest", "typescript": "latest"}},
    )
    (tmp_path / "pnpm-lock.yaml").write_text("lockfileVersion: 9\n", encoding="utf-8")
    (tmp_path / ".clasp.json").write_text("not-json-and-never-read", encoding="utf-8")
    source = tmp_path / "src"
    source.mkdir()
    write_json(source / "appsscript.json", {"runtimeVersion": "V8"})

    fingerprint = ProjectDetector(tmp_path).detect_fingerprint()

    assert fingerprint.primary_type is ProjectType.GOOGLE_APPS_SCRIPT
    assert fingerprint.ecosystems == ("javascript", "typescript")
    assert "google-apps-script" in fingerprint.frameworks
    assert fingerprint.tools == ("clasp", "pnpm")


@pytest.mark.parametrize(
    ("files", "expected"),
    [
        (
            {
                "composer.json": json.dumps(
                    {"require": {"laravel/framework": "^12.0"}}
                ),
                "artisan": "#!/usr/bin/env php\n",
            },
            ProjectType.LARAVEL,
        ),
        (
            {
                "go.mod": (
                    "module example.test/app\n"
                    "require github.com/gin-gonic/gin v1.10.0\n"
                )
            },
            ProjectType.GIN,
        ),
        (
            {"requirements.txt": "fastapi>=0.115\nuvicorn>=0.34\n"},
            ProjectType.FASTAPI,
        ),
        (
            {"requirements.txt": "Flask>=3.1\n"},
            ProjectType.FLASK,
        ),
    ],
)
def test_detects_supported_frameworks(
    tmp_path: Path,
    files: dict[str, str],
    expected: ProjectType,
) -> None:
    """Framework-specific markers should win over their base ecosystems."""

    for filename, content in files.items():
        (tmp_path / filename).write_text(content, encoding="utf-8")

    assert ProjectDetector(tmp_path).detect() is expected


def test_manual_override_preserves_secondary_safe_signals(tmp_path: Path) -> None:
    """A primary override remains authoritative without discarding tool context."""

    write_json(
        tmp_path / "package.json",
        {"dependencies": {"react": "latest"}, "devDependencies": {}},
    )

    fingerprint = ProjectDetector(tmp_path).detect_fingerprint(ProjectType.NODEJS)

    assert fingerprint.primary_type is ProjectType.NODEJS
    assert "javascript" in fingerprint.ecosystems
    assert "reactjs" in fingerprint.frameworks


def test_pyproject_keywords_do_not_create_false_framework_detection(
    tmp_path: Path,
) -> None:
    """Only dependency fields, not arbitrary TOML text, identify frameworks."""

    (tmp_path / "pyproject.toml").write_text(
        """
[project]
name = "framework-catalog"
dependencies = ["requests>=2"]
keywords = ["flask", "fastapi"]
""".strip(),
        encoding="utf-8",
    )

    assert ProjectDetector(tmp_path).detect() is ProjectType.PYTHON
