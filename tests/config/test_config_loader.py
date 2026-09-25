# tests/config/test_config_loader.py

"""Tests for configuration loading, lookups, and resolution precedence."""

from pathlib import Path

import pytest

from doc_gen.config.config_loader import ConfigError, ConfigLoader
from doc_gen.config.file_loader import load_project_config


def test_config_loader_reads_nested_tool_section(tmp_path: Path) -> None:
    """
    Verify nested `tool.doc-gen` sections are read correctly.

    Args:
        tmp_path: Temporary filesystem path fixture.

    Returns:
        None
    """
    config_file = tmp_path / "config.toml"
    config_file.write_text(
        """
[tool.doc-gen.logging]
level = "DEBUG"
show_level = true
""".strip(),
        encoding="utf-8",
    )

    loader = ConfigLoader(filename=str(config_file))

    assert loader.get("logging", "level") == "DEBUG"
    assert loader.get("logging", "show_level") is True


def test_config_loader_get_and_get_section_defaults(tmp_path: Path) -> None:
    """
    Verify getter methods return defaults for missing sections/keys.

    Args:
        tmp_path: Temporary filesystem path fixture.

    Returns:
        None
    """
    config_file = tmp_path / "empty.toml"
    config_file.write_text("", encoding="utf-8")

    loader = ConfigLoader(filename=str(config_file))

    assert loader.get("missing", default="fallback") == "fallback"
    assert loader.get_section("missing") == {}


def test_config_loader_require_raises_for_missing_key(tmp_path: Path) -> None:
    """
    Verify `require` raises ConfigError when a required key is absent.

    Args:
        tmp_path: Temporary filesystem path fixture.

    Returns:
        None

    Raises:
        ConfigError: Expected for missing required config key.
    """
    config_file = tmp_path / "config.toml"
    config_file.write_text("", encoding="utf-8")
    loader = ConfigLoader(filename=str(config_file))

    with pytest.raises(ConfigError):
        loader.require("cli", "templates", "commit_message")


def test_config_loader_resolve_priority(tmp_path: Path) -> None:
    """
    Verify `resolve` precedence: CLI value > config value > default value.

    Args:
        tmp_path: Temporary filesystem path fixture.

    Returns:
        None
    """
    config_file = tmp_path / "config.toml"
    config_file.write_text(
        """
[tool.doc-gen.cli.templates]
commit_message = "from-config.txt"
""".strip(),
        encoding="utf-8",
    )
    loader = ConfigLoader(filename=str(config_file))

    assert (
        loader.resolve(
            cli_value="from-cli.txt",
            config_keys=["cli", "templates", "commit_message"],
            default="default.txt",
        )
        == "from-cli.txt"
    )

    assert (
        loader.resolve(
            cli_value=None,
            config_keys=["cli", "templates", "commit_message"],
            default="default.txt",
        )
        == "from-config.txt"
    )

    assert (
        loader.resolve(
            cli_value=None,
            config_keys=["cli", "templates", "missing"],
            default="default.txt",
        )
        == "default.txt"
    )


def test_config_loader_invalid_toml_raises_config_error(tmp_path: Path) -> None:
    """
    Verify invalid TOML input raises ConfigError during loader initialization.

    Args:
        tmp_path: Temporary filesystem path fixture.

    Returns:
        None

    Raises:
        ConfigError: Expected for invalid TOML syntax.
    """
    config_file = tmp_path / "bad.toml"
    config_file.write_text("[tool.doc-gen\ninvalid", encoding="utf-8")

    with pytest.raises(ConfigError):
        ConfigLoader(filename=str(config_file))


def test_compatibility_loader_prefers_canonical_namespaced_config(
    tmp_path: Path,
) -> None:
    """The compatibility helper should prefer the maintained config location."""

    canonical = tmp_path / ".config" / "doc_gen" / "config.toml"
    canonical.parent.mkdir(parents=True)
    canonical.write_text(
        "[tool.doc-gen.cli.structure]\nproject_type = 'gin'\n",
        encoding="utf-8",
    )
    (tmp_path / ".projectstructure.toml").write_text(
        "[tool.doc-gen.cli.structure]\nproject_type = 'python'\n",
        encoding="utf-8",
    )

    loaded = load_project_config(str(tmp_path))

    assert loaded["cli"]["structure"]["project_type"] == "gin"


def test_compatibility_loader_keeps_legacy_read_fallback(tmp_path: Path) -> None:
    """Existing callers can still read the retired configuration filename."""

    (tmp_path / ".projectstructure.toml").write_text(
        "[tool.doc-gen.cli.structure]\nmax_depth = 2\n",
        encoding="utf-8",
    )

    loaded = load_project_config(str(tmp_path))

    assert loaded["cli"]["structure"]["max_depth"] == 2
