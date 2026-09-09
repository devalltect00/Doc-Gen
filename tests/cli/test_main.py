# tests/cli/test_main.py

"""
Tests for Doc-Gen CLI entrypoint.

Focus:
- root command
- help output
- command registration
- banner behavior
"""

from click.utils import strip_ansi
from typer.testing import CliRunner

from doc_gen.cli.main import app
from doc_gen.cli.utils import banner

runner = CliRunner()


def test_main_without_arguments_shows_banner_and_help(monkeypatch):
    """Bare invocation should run the callback before showing successful help."""

    calls = {"count": 0}

    def fake_show():
        calls["count"] += 1

    monkeypatch.setattr(banner, "show", fake_show)

    result = runner.invoke(app, [])

    assert result.exit_code == 0
    assert "Generate and analyze project documentation" in result.output
    assert calls["count"] == 1


def test_main_without_arguments_honors_no_banner(monkeypatch):
    """Bare help should respect the explicit banner suppression flag."""

    calls = {"count": 0}

    def fake_show():
        calls["count"] += 1

    monkeypatch.setattr(banner, "show", fake_show)

    result = runner.invoke(app, ["--no-banner"])

    assert result.exit_code == 0
    assert "Generate and analyze project documentation" in result.output
    assert calls["count"] == 0


def test_main_help_shows_banner_by_default(monkeypatch):
    calls = {"count": 0}

    def fake_show():
        calls["count"] += 1

    monkeypatch.setattr(
        banner,
        "show",
        fake_show,
    )

    result = runner.invoke(
        app,
        ["--help"],
    )

    assert result.exit_code == 0
    assert calls["count"] == 1


def test_main_help_no_banner_flag(monkeypatch):
    calls = {"count": 0}

    def fake_show():
        calls["count"] += 1

    monkeypatch.setattr(
        banner,
        "show",
        fake_show,
    )

    result = runner.invoke(
        app,
        [
            "--no-banner",
            "--help",
        ],
    )

    assert result.exit_code == 0
    assert calls["count"] == 0


def test_init_command_registered():
    result = runner.invoke(
        app,
        [
            "init",
            "--help",
        ],
    )

    assert result.exit_code == 0


def test_structure_command_registered():
    result = runner.invoke(
        app,
        [
            "structure",
            "--help",
        ],
    )

    assert result.exit_code == 0


def test_structure_generate_command_registered():
    result = runner.invoke(
        app,
        [
            "structure",
            "generate",
            "--help",
        ],
    )

    assert result.exit_code == 0


def test_structure_print_command_registered():
    result = runner.invoke(
        app,
        [
            "structure",
            "print",
            "--help",
        ],
    )

    assert result.exit_code == 0


def test_structure_analyze_command_registered():
    result = runner.invoke(
        app,
        [
            "structure",
            "analyze",
            "--help",
        ],
    )

    assert result.exit_code == 0


def test_invalid_command():
    result = runner.invoke(
        app,
        [
            "invalid-command",
        ],
    )

    assert result.exit_code != 0


def test_every_supported_command_exposes_dry_run():
    """Every supported leaf command should advertise explicit dry-run mode."""

    commands = [
        ["init", "--help"],
        ["structure", "generate", "--help"],
        ["structure", "print", "--help"],
        ["structure", "analyze", "--help"],
    ]

    for command in commands:
        result = runner.invoke(
            app,
            command,
            color=False,
            terminal_width=160,
        )
        help_output = strip_ansi(result.output)

        assert result.exit_code == 0
        assert "--dry-run" in help_output
