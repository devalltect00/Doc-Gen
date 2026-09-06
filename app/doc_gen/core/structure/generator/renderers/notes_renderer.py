# app/doc_gen/core/structure/generator/renderers/notes_renderer.py

"""
Notes renderer.
"""


class NotesRenderer:
    """
    Render notes section.
    """

    def render(self) -> str:
        """
        Render markdown section.
        """

        return """
## Notes

- Temporary files, caches, and environment directories are excluded.
- Structure is generated automatically using DocGen.
""".strip()
