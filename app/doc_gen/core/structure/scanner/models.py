# app/doc_gen/core/structure/scanner/models.py

"""
Scanner result models.
"""

from dataclasses import dataclass

from doc_gen.core.structure.scanner.enums import (
    ProjectType,
)


@dataclass
class AnalysisResult:
    """
    Repository analysis result.
    """

    project_type: ProjectType

    project_size: int

    project_score: int

    category: str

    top_directories: list[str]

    smart_mode_enabled: bool

    max_depth_used: int
