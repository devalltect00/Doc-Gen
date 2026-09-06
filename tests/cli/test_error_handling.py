# tests/cli/test_error_handling.py

"""Tests for concise Doc Gen command failure reporting."""

from typer.testing import CliRunner

from doc_gen.cli.main import app
from doc_gen.config.config_loader import ConfigError
from doc_gen.core.structure.common.exceptions import StructureGenerationError

runner = CliRunner()


def test_startup_configuration_failure_is_actionable(monkeypatch) -> None:
    """Render known configuration errors without a traceback."""

    def fail():
        raise ConfigError("Invalid Doc Gen configuration.")

    monkeypatch.setattr("doc_gen.cli.commands.main.command.get_config", fail)
    result = runner.invoke(app, ["--no-banner", "structure", "print", "."])

    assert result.exit_code == 1
    assert "Command startup failed" in result.output
    assert "Invalid Doc Gen configuration" in result.output
    assert "Traceback" not in result.output


def test_generate_domain_failure_is_actionable(monkeypatch) -> None:
    """Expose safe generation guidance and preserve a failed exit code."""

    def fail(_self, _args):
        raise StructureGenerationError("Unable to render documentation.")

    monkeypatch.setattr(
        "doc_gen.cli.commands.structure.generate.command.StructureGenerateMain.execute",
        fail,
    )
    result = runner.invoke(
        app, ["--no-banner", "structure", "generate", "--dry-run", "."]
    )

    assert result.exit_code == 1
    assert "Documentation generation failed" in result.output
    assert "Unable to render documentation" in result.output
    assert "Traceback" not in result.output


def test_print_unexpected_failure_hides_internal_details(monkeypatch) -> None:
    """Keep programming details in debug diagnostics only."""

    def fail(_self, _args):
        raise RuntimeError("private print detail")

    monkeypatch.setattr(
        "doc_gen.cli.commands.structure.print.command.StructurePrintMain.execute",
        fail,
    )
    result = runner.invoke(app, ["--no-banner", "structure", "print", "."])

    assert result.exit_code == 1
    assert "Structure printing failed unexpectedly" in result.output
    assert "private print detail" not in result.output
    assert "Traceback" not in result.output


def test_init_unexpected_failure_hides_internal_details(monkeypatch) -> None:
    """Avoid leaking initialization internals in normal output."""

    def fail(_self, _args):
        raise RuntimeError("private initialization detail")

    monkeypatch.setattr("doc_gen.cli.commands.init.command.InitMain.execute", fail)
    result = runner.invoke(app, ["--no-banner", "init"])

    assert result.exit_code == 1
    assert "Initialization failed unexpectedly" in result.output
    assert "private initialization detail" not in result.output
    assert "Traceback" not in result.output
