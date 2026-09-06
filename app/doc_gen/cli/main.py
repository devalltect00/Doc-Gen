# app/doc_gen/cli/main.py

"""
Main CLI application.

Entrypoint for Doc-Gen.
"""

import typer

from doc_gen.cli.commands import (
    init_command,
    main_command,
    structure_command,
)
from doc_gen.ui.console import console

typer.rich_utils._console = console

app = typer.Typer(
    name="doc-gen",
    help="Generate and analyze project documentation.",
    no_args_is_help=True,
    add_help_option=False,
    add_completion=True,
    rich_markup_mode="rich",
    pretty_exceptions_enable=True,
)

app.callback(invoke_without_command=True)(main_command.main)

app.command()(init_command.init)

#
# Command groups
#

app.add_typer(
    structure_command.app,
    name="structure",
)


def main() -> None:
    """
    CLI entrypoint.
    """
    app()
