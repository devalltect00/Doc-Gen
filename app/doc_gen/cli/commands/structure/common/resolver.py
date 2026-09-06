# app/doc_gen/cli/commands/structure/common/resolver.py

"""
Resolver utilities for structure commands.

This module converts:

    CLI arguments
        +
    configuration values
        +
    defaults

into a strongly typed StructureCommonArgs object.
"""

from pathlib import Path

from doc_gen.cli.constants.enums import ProfileChoices
from doc_gen.core.structure.scanner.enums import (
    ProjectType,
)

from .models import StructureCommonArgs


def resolve_structure_common_args(
    config,
    *,
    target_directory,
    profile,
    smart_mode,
    max_depth,
    show_files,
    collapse_dirs,
    project_type,
    verbose,
    dry_run,
) -> StructureCommonArgs:
    """
    Resolve common structure arguments.

    Priority:
        CLI
        ↓
        config.toml
        ↓
        defaults

    Returns
    -------
    StructureCommonArgs
    """

    collapse_value = config.resolve(
        collapse_dirs,
        ["cli", "structure", "collapse_dirs"],
        None,
    )

    # resolved_collapse_dirs = (
    #     {item.strip() for item in collapse_value.split(",") if item.strip()}
    #     if collapse_value
    #     else set()
    # )

    if isinstance(collapse_value, str):
        resolved_collapse_dirs = {
            item.strip() for item in collapse_value.split(",") if item.strip()
        }
    elif isinstance(collapse_value, list):
        resolved_collapse_dirs = {
            str(item).strip() for item in collapse_value if str(item).strip()
        }
    else:
        resolved_collapse_dirs = set()

    project_type_value = config.resolve(
        project_type,
        ["cli", "structure", "project_type"],
        None,
    )

    resolved_project_type = (
        ProjectType(project_type_value) if project_type_value else None
    )

    return StructureCommonArgs(
        target_directory=Path(
            config.resolve(
                target_directory,
                ["cli", "structure", "target_directory"],
                ".",
            )
        ),
        profile=config.resolve(
            profile,
            ["cli", "structure", "profile"],
            ProfileChoices.DEFAULT,
            # None,
        ),
        smart_mode=config.resolve(
            smart_mode,
            ["cli", "structure", "smart_mode"],
            False,
        ),
        max_depth=config.resolve(
            max_depth,
            ["cli", "structure", "max_depth"],
            3,
        ),
        show_files=config.resolve(
            show_files,
            ["cli", "structure", "show_files"],
            True,
        ),
        collapse_dirs=resolved_collapse_dirs,
        project_type=resolved_project_type,
        verbose=config.resolve(
            verbose,
            ["cli", "structure", "verbose"],
            False,
        ),
        dry_run=config.resolve(
            dry_run,
            ["cli", "execution", "dry_run"],
            False,
        ),
    )
