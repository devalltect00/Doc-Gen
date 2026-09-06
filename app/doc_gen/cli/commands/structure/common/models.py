# app/doc_gen/cli/commands/structure/common/models.py

"""
Shared models used by all structure-related commands.

Commands:
    doc-gen structure generate
    doc-gen structure print
    doc-gen structure analyze

This module contains argument models that represent
fully-resolved and validated CLI values.

These models are independent from:

    - Typer
    - argparse
    - TOML configuration
    - backend implementation

The resolver layer is responsible for converting
raw CLI/config values into these models.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from doc_gen.cli.constants.enums import (
    ProfileChoices,
    ProjectTypeChoices,
)


@dataclass
class StructureCommonArgs:
    """
    Shared structure arguments.

    Used by:
        - generate
        - print
        - analyze

    All values must already be resolved.

    Example
    -------
    StructureCommonArgs(
        target_directory=Path("."),
        profile=ProfileChoices.DEFAULT,
        smart_mode=False,
        max_depth=3,
        show_files=True,
        collapse_dirs={"node_modules", ".venv"},
        project_type=None,
        verbose=False,
    )
    """

    target_directory: Path
    profile: ProfileChoices
    smart_mode: bool
    max_depth: int
    show_files: bool
    collapse_dirs: set[str]
    project_type: ProjectTypeChoices | None
    verbose: bool
    dry_run: bool

    def model_dump(self) -> dict:
        """
        Convert common arguments to dictionary.

        Useful when extending StructureCommonArgs
        in command-specific argument models.

        Returns
        -------
        dict
        """

        return {
            "target_directory": self.target_directory,
            "profile": self.profile,
            "smart_mode": self.smart_mode,
            "max_depth": self.max_depth,
            "show_files": self.show_files,
            "collapse_dirs": self.collapse_dirs,
            "project_type": self.project_type,
            "verbose": self.verbose,
            "dry_run": self.dry_run,
        }
