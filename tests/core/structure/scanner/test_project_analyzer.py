# tests/core/structure/scanner/test_project_analyzer.py

"""Tests for Python 3.9-compatible repository analysis."""

from pathlib import Path

from doc_gen.core.structure.scanner.project_analyzer import ProjectAnalyzer


class FakeIgnoreLoader:
    """Ignore selected names without depending on ignore-file parsing."""

    @staticmethod
    def is_ignored(name: str) -> bool:
        """Return whether a test path name should be excluded."""

        return name in {"ignored", "skip.txt"}


def test_get_project_size_walks_and_filters_directories(tmp_path: Path) -> None:
    """Analysis counts included entries without relying on Path.walk."""

    kept = tmp_path / "kept"
    kept.mkdir()
    (kept / "child.py").write_text("print('kept')\n", encoding="utf-8")
    ignored = tmp_path / "ignored"
    ignored.mkdir()
    (ignored / "hidden.py").write_text("print('ignored')\n", encoding="utf-8")
    (tmp_path / "root.py").write_text("print('root')\n", encoding="utf-8")
    (tmp_path / "skip.txt").write_text("ignored\n", encoding="utf-8")

    analyzer = ProjectAnalyzer(tmp_path, FakeIgnoreLoader())

    assert analyzer.get_project_size(include_folders=True) == 3
    assert analyzer.get_project_size(include_folders=False) == 2
