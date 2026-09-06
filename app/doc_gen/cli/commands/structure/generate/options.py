# app/doc_gen/cli/commands/structure/generate/options.py

"""
CLI options specific to:

    doc-gen structure generate
"""

from typing import Annotated

import typer

from doc_gen.cli.constants.completions import (
    completion_output_choices,
)

# =========================================================
# OUTPUT FILE
# =========================================================

OutputFileOption = Annotated[
    str,
    typer.Option(
        "--output",
        "-o",
        help="""
        Output markdown file.

        Example:
            docs/PROJECT_STRUCTURE.md
        """,
        autocompletion=completion_output_choices,
    ),
]
