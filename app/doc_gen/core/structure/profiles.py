# app/doc_gen/core/structure/profiles.py

"""
Structure generation profiles.

Profiles provide predefined structure generation
settings for common repository sizes and use cases.
"""

from dataclasses import dataclass

from doc_gen.cli.constants.enums import ProfileChoices


@dataclass(frozen=True)
class StructureProfile:
    """
    Structure generation profile.
    """

    max_depth: int

    show_files: bool

    collapse_dirs: set[str]


PROFILES: dict[ProfileChoices, StructureProfile] = {
    "minimal": StructureProfile(
        max_depth=2,
        show_files=False,
        collapse_dirs={
            "node_modules",
            "venv",
            ".venv",
            "dist",
            "build",
            ".next",
        },
    ),
    "default": StructureProfile(
        max_depth=3,
        show_files=True,
        collapse_dirs={
            "node_modules",
            "venv",
            ".venv",
        },
    ),
    "detailed": StructureProfile(
        max_depth=5,
        show_files=True,
        collapse_dirs=set(),
    ),
}
