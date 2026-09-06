# app/doc_gen/cli/commands/structure/generate/models.py

"""
Models for:

    doc-gen structure generate

Contains fully-resolved arguments used by the
generate command.

Shared structure arguments live in:

    structure/common/models.py
"""

from dataclasses import dataclass
from pathlib import Path

from doc_gen.cli.commands.structure.common.models import (
    StructureCommonArgs,
)


@dataclass
class StructureGenerateArgs(StructureCommonArgs):
    """
    Fully resolved arguments for:

        doc-gen structure generate

    Example
    -------
    StructureGenerateArgs(
        target_directory=Path("."),
        profile=ProfileChoices.DEFAULT,
        smart_mode=False,
        max_depth=3,
        show_files=True,
        collapse_dirs={"node_modules", ".venv"},
        project_type=None,
        output_file=Path("docs/PROJECT_STRUCTURE.md"),
        verbose=False,
    )
    """

    output_file: Path
