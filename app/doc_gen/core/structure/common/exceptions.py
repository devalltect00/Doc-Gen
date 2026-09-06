# app/doc_gen/core/structure/common/exceptions.py

"""
Exceptions used by structure services.
"""

from doc_gen.core.shared import DocGenError


class StructureError(DocGenError):
    """
    Base structure exception.
    """


class StructureConfigurationError(StructureError):
    """
    Invalid structure configuration.
    """


class StructureScanError(StructureError):
    """
    Structure scanning failure.
    """


class StructureGenerationError(StructureError):
    """
    Structure generation failure.
    """
