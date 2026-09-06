# app/doc_gen/cli/commands/structure/generate/resolver.py

"""
Resolver for:

    doc-gen structure generate
"""

from pathlib import Path

from doc_gen.cli.commands.structure.common.models import (
    StructureCommonArgs,
)

from .models import (
    StructureGenerateArgs,
)


def resolve_structure_generate_args(
    config,
    *,
    common_args: StructureCommonArgs,
    output_file,
) -> StructureGenerateArgs:
    """
    Resolve arguments for:

        doc-gen structure generate

    Resolution order:

        1. CLI
        2. Config file
        3. Default value

    Parameters
    ----------
    config:
        Config loader instance.

    common_args:
        Previously resolved shared structure arguments.

    output_file:
        CLI output file value.

    verbose:
        CLI verbose value.

    Returns
    -------
    StructureGenerateArgs
    """

    return StructureGenerateArgs(
        **common_args.model_dump(),
        output_file=Path(
            config.resolve(
                output_file,
                ["cli", "structure", "generate", "output_file"],
                "docs/PROJECT_STRUCTURE.md",
            )
        ),
    )
