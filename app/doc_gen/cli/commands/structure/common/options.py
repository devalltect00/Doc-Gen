# app/doc_gen/cli/commands/structure/common/options.py

"""
Shared CLI options for structure commands.

These options are reused by:

    doc-gen structure generate
    doc-gen structure print
    doc-gen structure analyze
"""

from typing import Annotated, Optional

import typer

from doc_gen.cli.constants.completions import (
    completion_profile_choices,
    completion_target_directory,
)
from doc_gen.cli.constants.enums import (
    ProfileChoices,
    ProjectTypeChoices,
)

# =========================================================
# TARGET DIRECTORY
# =========================================================

TargetDirectoryArgument = Annotated[
    str,
    typer.Argument(
        help="""
        Root directory to scan.

        Examples:
            .
            ./app
            ../my-project
        """,
        autocompletion=completion_target_directory,
    ),
]

# =========================================================
# PROFILE
# =========================================================

ProfileOption = Annotated[
    ProfileChoices,
    typer.Option(
        "--profile",
        help="""
        Structure generation profile.

        Available profiles:
            default
            minimal
            detailed
            custom
        """,
        autocompletion=completion_profile_choices,
        case_sensitive=False,
    ),
]

# =========================================================
# SMART MODE
# =========================================================

SmartModeOption = Annotated[
    bool,
    typer.Option(
        "--smart/--no-smart",
        help="""
        Enable automatic structure optimization.

        Smart mode adjusts:
            - max depth
            - file visibility
            - collapsed directories

        based on repository size.
        """,
    ),
]

# =========================================================
# MAX DEPTH
# =========================================================

MaxDepthOption = Annotated[
    int,
    typer.Option(
        "--max-depth",
        help="""
        Maximum directory depth to display.

        Examples:
            --max-depth 2
            --max-depth 5
        """,
    ),
]

# =========================================================
# SHOW FILES
# =========================================================

ShowFilesOption = Annotated[
    bool,
    typer.Option(
        "--show-files/--hide-files",
        help="""
        Show or hide files.

        Directories are always shown.
        """,
    ),
]

# =========================================================
# COLLAPSE DIRECTORIES
# =========================================================

CollapseDirectoriesOption = Annotated[
    str,
    typer.Option(
        "--collapse",
        help="""
        Comma-separated directory names to collapse.

        Example:
            --collapse node_modules,.venv,dist
        """,
    ),
]

# =========================================================
# PROJECT TYPE
# =========================================================

ProjectTypeOption = Annotated[
    Optional[ProjectTypeChoices],
    typer.Option(
        "--project-type",
        help="""
        Override automatic project detection.

        Examples:
            python
            django
            nodejs
            reactjs
            nextjs
        """,
    ),
]

# =========================================================
# VERBOSE
# =========================================================

VerboseOption = Annotated[
    bool,
    typer.Option(
        "--verbose",
        "-v",
        help="""
        Print generated structure to console.

        Useful for debugging.
        """,
    ),
]

# =========================================================
# DRY RUN
# =========================================================

DryRunOption = Annotated[
    bool,
    typer.Option(
        "--dry-run/--no-dry-run",
        "-dr/-Dr",
        help=(
            "Simulate mutating output. Read-only discovery and analysis may still run."
        ),
    ),
]
