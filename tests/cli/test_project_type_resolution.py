"""Project-type CLI and configuration resolution tests."""

from doc_gen.cli.commands.structure.common.resolver import (
    resolve_structure_common_args,
)
from doc_gen.config.config_loader import ConfigLoader
from doc_gen.core.structure.scanner.enums import ProjectType


def resolve(config: ConfigLoader, project_type):
    """Resolve only the project-type field with stable test defaults."""

    return resolve_structure_common_args(
        config,
        target_directory=".",
        profile=None,
        smart_mode=None,
        max_depth=None,
        show_files=None,
        collapse_dirs=None,
        project_type=project_type,
        verbose=None,
        dry_run=None,
    )


def test_auto_project_type_resolves_to_detection(tmp_path) -> None:
    """The public auto choice should not be passed into the core enum."""

    config_file = tmp_path / "config.toml"
    config_file.write_text("", encoding="utf-8")
    args = resolve(ConfigLoader(filename=config_file), "auto")

    assert args.project_type is None


def test_new_project_type_can_be_selected_from_configuration(tmp_path) -> None:
    """New framework values should resolve through the existing config contract."""

    config_file = tmp_path / "config.toml"
    config_file.write_text(
        "[tool.doc-gen.cli.structure]\nproject_type = 'laravel'\n",
        encoding="utf-8",
    )
    args = resolve(ConfigLoader(filename=config_file), None)

    assert args.project_type is ProjectType.LARAVEL
