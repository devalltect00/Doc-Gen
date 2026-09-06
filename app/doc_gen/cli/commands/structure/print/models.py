# app/doc_gen/cli/commands/structure/print/models.py

"""
Models for:

    doc-gen structure print

Contains fully resolved arguments used by the
print command.
"""

from dataclasses import dataclass

from doc_gen.cli.commands.structure.common.models import (
    StructureCommonArgs,
)


@dataclass
class StructurePrintArgs(StructureCommonArgs):
    """
    Fully resolved arguments for:

        doc-gen structure print
    """

    pass
