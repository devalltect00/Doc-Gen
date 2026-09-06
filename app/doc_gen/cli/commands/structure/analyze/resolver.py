# app/doc_gen/cli/commands/structure/analyze/resolver.py

"""
Resolver for:

    doc-gen structure analyze
"""

from doc_gen.cli.commands.structure.common.models import (
    StructureCommonArgs,
)

from .models import StructureAnalyzeArgs


def resolve_structure_analyze_args(
    *,
    config,
    common_args: StructureCommonArgs,
) -> StructureAnalyzeArgs:
    """
    Resolve analyze command arguments.
    """

    return StructureAnalyzeArgs(
        **common_args.model_dump(),
    )
