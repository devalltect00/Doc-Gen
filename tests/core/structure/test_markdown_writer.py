"""Markdown output normalization regression tests."""

from pathlib import Path

from doc_gen.core.structure.generator.writers.markdown_writer import MarkdownWriter


def test_normalize_content_is_idempotent_and_hook_friendly() -> None:
    """Generated Markdown should have stable whitespace and one final newline."""

    source = "\r\n# Project  \r\n\r\n\r\nContent\t\r\n\r\n"
    expected = "# Project\n\nContent\n"

    normalized = MarkdownWriter.normalize_content(source)

    assert normalized == expected
    assert MarkdownWriter.normalize_content(normalized) == expected


def test_write_uses_utf8_lf_without_trailing_whitespace(tmp_path: Path) -> None:
    """Persistence should match common end-of-file and whitespace hooks."""

    output_file = tmp_path / "custom" / "structure.md"

    MarkdownWriter().write(
        output_file=output_file,
        content="# Project  \r\n\r\nGenerated content\t",
    )

    assert output_file.read_bytes() == b"# Project\n\nGenerated content\n"
