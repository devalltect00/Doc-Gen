# app/doc_gen/cli/commands/main/options.py

from typing import Annotated, Optional

import typer

from doc_gen.cli.constants.enums import LogLevelChoices
from doc_gen.cli.utils import version_callback

# ---------------------------
# 🧩 APPLICATION OPTIONS
# ---------------------------
NoBannerOption = Annotated[
    bool,
    typer.Option(
        "--no-banner",
        help="""
        Disable banner

        [dim blue]Default:[/dim blue] [red]False[/red]
        """,
    ),
]
HelpOption = Annotated[
    bool,
    typer.Option(
        "--help",
        "-h",
        help="Show help",
    ),
]
VersionOption = Annotated[
    Optional[bool],
    typer.Option(
        "--version",
        "-v",
        help="Get app version",
        callback=version_callback,
    ),
]


# ---------------------------
# 📝 LOGGING OPTIONS
# ---------------------------
DebugOption = Annotated[
    bool,
    typer.Option(
        "--debug/--no-debug",
        "-dbg/-Dbg",
        help="""
        [bold yellow]Debugging mode[/bold yellow]

        [green]Show[/green]/[blue]Hide[/blue] debug message.
        """,
        rich_help_panel="Global • Debug",
    ),
]
LogLevelOption = Annotated[
    LogLevelChoices,
    typer.Option(
        "--log-level",
        "-ll",
        help="""
        [bold]Logging level[/bold]

        Control verbosity of logs

        [bold yellow]•[/bold yellow] [bold]critical[/bold] → only critical errors\n
        [bold yellow]•[/bold yellow] [bold]error[/bold]    → errors only\n
        [bold yellow]•[/bold yellow] [bold]warning[/bold]  → warnings + errors\n
        [bold yellow]•[/bold yellow] [bold]info[/bold]     → general info (default\n
        [bold yellow]•[/bold yellow] [bold]debug[/bold]    → detailed debugging\n

        [dim blue]Default:[/dim blue] info

        [dim yellow]HINT:[/dim yellow] better using config.toml configuration.
        [dim]Variable:[/dim] 'tool.doc-gen.logging.level'
        """,
        rich_help_panel="Global • Debug",
        case_sensitive=False,
    ),
]
