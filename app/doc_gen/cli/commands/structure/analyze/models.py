# app/doc_gen/cli/commands/structure/analyze/models.py

"""
Models for:

    doc-gen structure analyze
"""

from dataclasses import dataclass

from doc_gen.cli.commands.structure.common.models import (
    StructureCommonArgs,
)


@dataclass
class StructureAnalyzeArgs(StructureCommonArgs):
    """
    Fully resolved arguments for:

        doc-gen structure analyze
    """

    pass
