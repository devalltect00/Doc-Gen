# app/doc_gen/core/structure/generator/renderers/repository_structure_renderer.py

"""
Repository structure renderer.
"""

from doc_gen.core.structure.scanner.enums import (
    ProjectType,
)


class RepositoryStructureRenderer:
    """
    Render repository tree section.
    """

    def render(
        self,
        *,
        project_type: ProjectType,
        tree: list[str],
    ) -> str:
        """
        Render repository structure.
        """

        lines = [
            "# Repository Structure",
            "",
            f"(project type: {project_type})",
            "",
            "```text",
        ]

        lines.extend(tree)

        lines.append("```")

        return "\n".join(lines)
