# app/doc_gen/core/structure/generator/models.py

"""
Generator models.
"""

from dataclasses import dataclass
from pathlib import Path

from doc_gen.core.structure.scanner.enums import (
    ProjectType,
)


@dataclass
class MarkdownDocument:
    """
    Represents generated markdown content.
    """

    content: str


@dataclass
class GenerationResult:
    """
    Result of markdown generation.

    Used by UI presenters to display
    generation summaries.
    """

    output_file: Path

    project_type: ProjectType

    directory_count: int

    tree_line_count: int

    dry_run: bool = False
