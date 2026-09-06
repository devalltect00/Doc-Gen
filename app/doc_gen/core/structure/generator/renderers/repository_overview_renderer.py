# app/doc_gen/core/structure/generator/renderers/repository_overview_renderer.py

"""
Repository overview renderer.
"""

from doc_gen.core.structure.metadata.repository_docs import (
    COMMON_DIRECTORIES,
)


class RepositoryOverviewRenderer:
    """
    Render repository overview section.
    """

    def render(self) -> str:
        """
        Render markdown section.
        """

        lines = [
            "# Repository Overview",
            "",
            (
                "This repository follows a modular "
                "structure commonly used in modern projects."
            ),
            "",
            "Common directories include:",
            "",
        ]

        for name, info in COMMON_DIRECTORIES.items():
            lines.append(f"- `{name}/` — {info['description']}")

        return "\n".join(lines)
