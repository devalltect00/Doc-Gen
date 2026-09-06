# app/doc_gen/core/structure/generator/renderers/directory_details_renderer.py

"""
Directory details renderer.
"""

from doc_gen.core.structure.metadata.repository_docs import (
    COMMON_DIRECTORIES,
)


class DirectoryDetailsRenderer:
    """
    Render directory details section.
    """

    def render(
        self,
        *,
        directories: list[str],
    ) -> str:
        """
        Render markdown section.
        """

        lines = [
            "## Directory Details",
            "",
        ]

        for directory in directories:
            if directory not in COMMON_DIRECTORIES:
                continue

            info = COMMON_DIRECTORIES[directory]

            lines.append(f"### `{directory}/`")

            lines.append(info["description"])

            lines.append("")

            lines.extend(info["details"])

            lines.append("")

        return "\n".join(lines)
