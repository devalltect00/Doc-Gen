# app/doc_gen/cli/commands/structure/print/resolver.py

"""
Resolver for:

    doc-gen structure print
"""

from doc_gen.cli.commands.structure.common.models import (
    StructureCommonArgs,
)

from .models import StructurePrintArgs


def resolve_structure_print_args(
    *,
    config,
    common_args: StructureCommonArgs,
) -> StructurePrintArgs:
    """
    Resolve print command arguments.

    Returns
    -------
    StructurePrintArgs
    """

    return StructurePrintArgs(
        **common_args.model_dump(),
    )
