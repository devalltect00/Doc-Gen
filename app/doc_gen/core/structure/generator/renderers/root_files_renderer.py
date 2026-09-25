# app/doc_gen/core/structure/generator/renderers/root_files_renderer.py

"""Recognized repository files renderer."""

from pathlib import Path

from doc_gen.core.structure.metadata.models import MetadataCatalog


class RootFilesRenderer:
    """Render documentation for recognized repository files."""

    def render(
        self,
        *,
        root_directory: Path,
        catalog: MetadataCatalog,
    ) -> str:
        """
        Render recognized file descriptions as formatter-stable Markdown.
        """

        lines = [
            "## Recognized Files",
            "",
        ]

        detected = []

        for filename in catalog.root_files:
            if (root_directory / filename).exists():
                detected.append(filename)

        if not detected:
            lines.append("No recognized repository files detected.")

            return "\n".join(lines)

        for filename in detected:
            lines.append(f"- `{filename}` — {catalog.root_files[filename]}")

        return "\n".join(lines)
