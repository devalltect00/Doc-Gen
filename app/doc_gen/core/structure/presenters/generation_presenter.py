# app/doc_gen/core/structure/presenters/generation_presenter.py

"""
Generation result presenter.
"""

from rich.table import Table

from doc_gen.core.structure.generator.models import (
    GenerationResult,
)


class GenerationPresenter:
    """
    Render generation results.
    """

    def render(
        self,
        result: GenerationResult,
    ) -> Table:
        """
        Render generation summary.
        """

        title = "Documentation Preview" if result.dry_run else "Documentation Generated"
        table = Table(title=title)

        table.add_column("Property")
        table.add_column("Value")

        table.add_row(
            "Output File",
            str(result.output_file),
        )

        table.add_row(
            "Project Type",
            result.project_type.value,
        )

        table.add_row(
            "Directories",
            str(result.directory_count),
        )

        table.add_row(
            "Tree Lines",
            str(result.tree_line_count),
        )

        table.add_row(
            "Mode",
            "Dry run — not written" if result.dry_run else "Written",
        )

        return table
