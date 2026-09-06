# app/doc_gen/cli/commands/structure/command.py

"""
Parent command group for:

    doc-gen structure

Provides:

    doc-gen structure generate
    doc-gen structure print
    doc-gen structure analyze
"""

import typer

from doc_gen.cli.commands.structure.analyze.command import (
    app as analyze_app,
)
from doc_gen.cli.commands.structure.generate.command import (
    app as generate_app,
)
from doc_gen.cli.commands.structure.print.command import (
    app as print_app,
)

app = typer.Typer(
    help="""
    Structure related commands.

    Examples:

        doc-gen structure generate

        doc-gen structure print

        doc-gen structure analyze
    """,
    rich_help_panel="Project Structure",
)

app.add_typer(
    generate_app,
    name="generate",
)

app.add_typer(
    print_app,
    name="print",
)

app.add_typer(
    analyze_app,
    name="analyze",
)
