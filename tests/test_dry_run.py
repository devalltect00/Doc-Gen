# tests/test_dry_run.py

"""Dry-run regression tests for Doc Gen commands and output boundaries."""

from pathlib import Path
from types import SimpleNamespace

import pytest
from typer.testing import CliRunner

from doc_gen.cli.commands.structure.common.resolver import (
    resolve_structure_common_args,
)
from doc_gen.cli.main import app
from doc_gen.config.config_loader import ConfigLoader
from doc_gen.core.structure.generator.markdown_generator import MarkdownGenerator
from doc_gen.core.structure.generator.models import MarkdownDocument

runner = CliRunner()


@pytest.mark.parametrize(
    ("command", "target"),
    [
        (["structure", "generate", "--dry-run"], "generate"),
        (["structure", "print", "--dry-run"], "print"),
        (["structure", "analyze", "--dry-run"], "analyze"),
    ],
)
def test_structure_commands_accept_dry_run(monkeypatch, command, target) -> None:
    """Every structure command should receive the resolved dry-run flag."""

    captured = {}

    def fake_execute(self, args):
        captured["args"] = args

    class_name = f"Structure{target.title()}Main"
    monkeypatch.setattr(
        f"doc_gen.cli.commands.structure.{target}.command.{class_name}.execute",
        fake_execute,
    )

    result = runner.invoke(app, command)

    assert result.exit_code == 0
    assert captured["args"].dry_run is True


def test_markdown_generator_dry_run_skips_writer(tmp_path: Path) -> None:
    """Generation dry-run may inspect content but must not write output."""

    class FakeScanner:
        project_type = SimpleNamespace(value="python")

        @staticmethod
        def generate_tree():
            return ["."]

        @staticmethod
        def detect_top_directories():
            return []

    generator = MarkdownGenerator(
        config=SimpleNamespace(target_directory=tmp_path),
        scanner_service=FakeScanner(),
    )
    generator.generate_document = lambda: MarkdownDocument(content="# Preview")
    output_file = tmp_path / "PROJECT_STRUCTURE.md"

    result = generator.save(output_file=output_file, dry_run=True)

    assert result.dry_run is True
    assert result.output_file == output_file
    assert not output_file.exists()


def test_generate_command_dry_run_does_not_write_output(tmp_path: Path) -> None:
    """CLI generation dry-run should preserve the requested output path."""

    (tmp_path / "main.py").write_text("print('hello')\n", encoding="utf-8")
    output_file = tmp_path / "docs" / "PROJECT_STRUCTURE.md"

    result = runner.invoke(
        app,
        [
            "structure",
            "generate",
            "--output",
            str(output_file),
            "--dry-run",
            str(tmp_path),
        ],
    )

    assert result.exit_code == 0
    assert not output_file.exists()
    assert not output_file.parent.exists()


def test_configured_dry_run_reaches_structure_commands(tmp_path: Path) -> None:
    """The shared resolver should honor configured dry-run mode."""

    config_file = tmp_path / "config.toml"
    config_file.write_text(
        """
[tool.doc-gen.cli.execution]
dry_run = true
""".strip(),
        encoding="utf-8",
    )
    config = ConfigLoader(filename=config_file)

    args = resolve_structure_common_args(
        config,
        target_directory=".",
        profile=None,
        smart_mode=None,
        max_depth=None,
        show_files=None,
        collapse_dirs=None,
        project_type=None,
        verbose=None,
        dry_run=None,
    )

    assert args.dry_run is True
