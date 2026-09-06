# app/doc_gen/core/structure/presenters/analysis_presenter.py

"""
Analysis presentation helpers.
"""

from rich.table import Table

from doc_gen.core.structure.scanner.models import (
    AnalysisResult,
)


class AnalysisPresenter:
    """
    Render analysis results using Rich tables.
    """

    def render(
        self,
        result: AnalysisResult,
    ) -> Table:
        """
        Render repository analysis table.

        Parameters
        ----------
        result:
            Analysis result produced by the scanner.

        Returns
        -------
        Table
            Rich table ready for rendering.
        """

        table = Table(
            title="Repository Analysis",
        )

        table.add_column(
            "Property",
            style="cyan",
        )

        table.add_column(
            "Value",
        )

        table.add_row(
            "Project Type",
            result.project_type.value,
        )

        table.add_row(
            "Project Size",
            str(result.project_size),
        )

        table.add_row(
            "Project Score",
            str(result.project_score),
        )

        table.add_row(
            "Category",
            result.category,
        )

        table.add_row(
            "Smart Mode",
            "Enabled" if result.smart_mode_enabled else "Disabled",
        )

        table.add_row(
            "Max Depth Used",
            str(result.max_depth_used),
        )

        table.add_row(
            "Top Directories",
            # ("\n".join(result.top_directories) if result.top_directories else "-"),
            (", ".join(result.top_directories) if result.top_directories else "-"),
        )

        return table
