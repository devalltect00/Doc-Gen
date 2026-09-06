# app/doc_gen/core/structure/presenters/tree_presenter.py

"""
Tree presentation helpers.
"""

from rich.panel import Panel


class TreePresenter:
    """
    Render repository trees.
    """

    def render(
        self,
        tree: list[str],
    ) -> Panel:
        """
        Render tree panel.
        """

        return Panel(
            "\n".join(tree),
            title="Project Structure",
        )
