# app/doc_gen/core/structure/generator/renderers/root_files_renderer.py

"""
Root files renderer.
"""

from pathlib import Path

from doc_gen.core.structure.metadata.repository_docs import (
    COMMON_ROOT_FILES,
)


class RootFilesRenderer:
    """
    Render root file documentation.
    """

    def render(
        self,
        *,
        root_directory: Path,
    ) -> str:
        """
        Render root file section.
        """

        lines = [
            "## Root Files",
            "",
        ]

        detected = []

        for filename in COMMON_ROOT_FILES:
            if (root_directory / filename).exists():
                detected.append(filename)

        if not detected:
            lines.append("No common root files detected.")

            return "\n".join(lines)

        lines.extend(
            [
                "| File | Description |",
                "|------|-------------|",
            ]
        )

        for filename in detected:
            lines.append(f"| `{filename}` | {COMMON_ROOT_FILES[filename]} |")

        return "\n".join(lines)
