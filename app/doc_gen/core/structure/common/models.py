# app/doc_gen/core/structure/common/models.py

"""
Shared backend models for structure operations.

These models are application-layer models.

They are intentionally independent from:

    - Typer
    - CLI arguments
    - TOML configuration
    - Rich output

They represent the resolved structure configuration
used by scanners, analyzers, and generators.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from doc_gen.core.structure.scanner.enums import (
    ProjectType,
)


@dataclass
class StructureConfig:
    """
    Structure generation configuration.

    This model is the primary configuration object
    used by backend services.

    Example
    -------
    StructureConfig(
        target_directory=Path("."),
        max_depth=3,
        show_files=True,
        collapse_dirs={"node_modules"},
        smart_mode=False,
        project_type=None,
    )
    """

    target_directory: Path

    max_depth: int

    show_files: bool

    collapse_dirs: set[str]

    smart_mode: bool

    project_type: ProjectType | None
