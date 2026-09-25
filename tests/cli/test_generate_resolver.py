"""Generate-command output resolution tests."""

from pathlib import Path

from doc_gen.cli.commands.structure.common.models import StructureCommonArgs
from doc_gen.cli.commands.structure.generate.resolver import (
    resolve_structure_generate_args,
)
from doc_gen.cli.constants.enums import ProfileChoices
from doc_gen.config.config_loader import ConfigLoader


def test_generate_default_uses_canonical_lowercase_output_path(tmp_path: Path) -> None:
    """An uninitialized project should use the same default as the template."""

    config_file = tmp_path / "config.toml"
    config_file.write_text("", encoding="utf-8")
    common = StructureCommonArgs(
        target_directory=tmp_path,
        profile=ProfileChoices.DEFAULT,
        smart_mode=False,
        max_depth=3,
        show_files=True,
        collapse_dirs=set(),
        project_type=None,
        verbose=False,
        dry_run=False,
    )

    args = resolve_structure_generate_args(
        ConfigLoader(filename=config_file),
        common_args=common,
        output_file=None,
    )

    assert args.output_file == Path("docs/project_structure.md")
