# tests/utils/test_ignore_loader.py

"""Tests for Doc Gen's project structure ignore rules."""

from pathlib import Path

from app.doc_gen.utils.ignore_loader import IgnoreLoader
from doc_gen.core.structure.scanner.enums import ProjectType


def test_python_defaults_ignore_named_virtual_environments(tmp_path: Path) -> None:
    """Keep dedicated development and production environments out of scans."""

    loader = IgnoreLoader(root_path=tmp_path, project_type="python")

    assert loader.is_ignored("dev_venv")
    assert loader.is_ignored("prod_venv")
    assert loader.is_ignored("venv_dev")
    assert loader.is_ignored("venv_prod")
    assert loader.is_ignored("publish_venv")
    assert loader.is_ignored("venv_publish")
    assert loader.is_ignored("other_venv")
    assert loader.is_ignored("venv_other")
    assert not loader.is_ignored("custom_venv")


def test_composable_defaults_cover_apps_script_php_and_go(tmp_path: Path) -> None:
    """Detected ecosystems should combine their generated-artifact rules."""

    apps_script = IgnoreLoader(
        root_path=tmp_path,
        project_type=ProjectType.GOOGLE_APPS_SCRIPT,
        project_types=("javascript", "typescript", "google-apps-script"),
    )
    laravel = IgnoreLoader(root_path=tmp_path, project_type=ProjectType.LARAVEL)
    gin = IgnoreLoader(root_path=tmp_path, project_type=ProjectType.GIN)

    assert apps_script.is_ignored("node_modules")
    assert apps_script.is_ignored(".clasp.json")
    assert apps_script.is_ignored(".env.production")
    assert laravel.is_ignored("vendor")
    assert gin.is_ignored("coverage.out")
