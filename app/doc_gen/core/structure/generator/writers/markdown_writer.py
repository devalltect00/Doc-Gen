# app/doc_gen/core/structure/generator/writers/markdown_writer.py

"""
Markdown file writer.
"""

from pathlib import Path


class MarkdownWriter:
    """
    Write markdown content to disk.
    """

    @staticmethod
    def normalize_content(content: str) -> str:
        """Return stable Markdown text suitable for version control hooks.

        Normalization uses LF line endings, removes trailing spaces and tabs,
        collapses repeated blank lines, and writes exactly one final newline.
        The operation is intentionally conservative and does not invoke an
        ecosystem-specific formatter such as Prettier.
        """

        normalized = content.replace("\r\n", "\n").replace("\r", "\n")
        lines = [line.rstrip(" \t") for line in normalized.split("\n")]

        while lines and not lines[0]:
            lines.pop(0)
        while lines and not lines[-1]:
            lines.pop()

        compacted: list[str] = []
        previous_was_blank = False

        for line in lines:
            is_blank = not line
            if is_blank and previous_was_blank:
                continue
            compacted.append(line)
            previous_was_blank = is_blank

        return "\n".join(compacted) + "\n"

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

        with output_file.open(
            "w",
            encoding="utf-8",
            newline="\n",
        ) as stream:
            stream.write(self.normalize_content(content))
