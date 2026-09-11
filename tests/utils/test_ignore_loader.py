# tests/utils/test_ignore_loader.py

"""Tests for Doc Gen's project structure ignore rules."""

from pathlib import Path

from app.doc_gen.utils.ignore_loader import IgnoreLoader


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
