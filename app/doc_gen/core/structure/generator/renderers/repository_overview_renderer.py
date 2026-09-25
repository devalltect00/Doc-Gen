# app/doc_gen/core/structure/generator/renderers/repository_overview_renderer.py

"""
Repository overview renderer.
"""

from doc_gen.core.structure.metadata.models import MetadataCatalog
from doc_gen.core.structure.scanner.models import ProjectFingerprint


class RepositoryOverviewRenderer:
    """
    Render repository overview section.
    """

    def render(
        self,
        *,
        directories: list[str],
        fingerprint: ProjectFingerprint,
        catalog: MetadataCatalog,
    ) -> str:
        """
        Render markdown section.
        """

        lines = [
            "# Repository Overview",
            "",
            (
                "This repository was analyzed using composable project "
                "and framework metadata."
            ),
            "",
            "Detected technologies: "
            + ", ".join(
                f"`{technology}`" for technology in fingerprint.detected_technologies
            ),
            "",
            "Recognized top-level directories:",
            "",
        ]

        recognized = [name for name in directories if name in catalog.directories]
        if not recognized:
            lines.append("No project-aware top-level directories were detected.")
            return "\n".join(lines)

        for name in recognized:
            info = catalog.directories[name]
            lines.append(f"- `{name}/` — {info['description']}")

        return "\n".join(lines)
