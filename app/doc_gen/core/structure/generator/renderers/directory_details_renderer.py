# app/doc_gen/core/structure/generator/renderers/directory_details_renderer.py

"""
Directory details renderer.
"""

from doc_gen.core.structure.metadata.models import MetadataCatalog


class DirectoryDetailsRenderer:
    """
    Render directory details section.
    """

    def render(
        self,
        *,
        directories: list[str],
        catalog: MetadataCatalog,
    ) -> str:
        """
        Render markdown section.
        """

        lines = [
            "## Directory Details",
            "",
        ]

        for directory in directories:
            if directory not in catalog.directories:
                continue

            info = catalog.directories[directory]

            lines.append(f"### `{directory}/`")

            lines.append("")

            lines.append(info["description"])

            lines.append("")

            lines.extend(info["details"])

            lines.append("")

        return "\n".join(lines)
