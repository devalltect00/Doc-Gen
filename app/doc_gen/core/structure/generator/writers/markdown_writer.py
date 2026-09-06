# app/doc_gen/core/structure/generator/writers/markdown_writer.py

"""
Markdown file writer.
"""

from pathlib import Path


class MarkdownWriter:
    """
    Write markdown content to disk.
    """

    def write(
        self,
        *,
        output_file: Path,
        content: str,
    ) -> None:
        """
        Write markdown file.

        Parameters
        ----------
        output_file:
            Destination file.

        content:
            Markdown content.
        """

        output_file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        output_file.write_text(
            content,
            encoding="utf-8",
        )
