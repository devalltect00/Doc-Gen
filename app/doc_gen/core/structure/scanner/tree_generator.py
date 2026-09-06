# app/doc_gen/core/structure/scanner/tree_generator.py

"""
Repository tree generation.

Responsible only for generating the visual
directory tree representation.
"""

from pathlib import Path


class TreeGenerator:
    """
    Generate repository tree structures.

    Example
    -------
    .

    ├── app
    │   ├── main.py
    │   └── config.py
    └── tests
        └── test_app.py
    """

    def __init__(
        self,
        *,
        root_directory: Path,
        ignore_loader,
        max_depth: int,
        show_files: bool,
        collapse_dirs: set[str],
    ) -> None:
        self.root_directory = root_directory
        self.ignore_loader = ignore_loader

        self.max_depth = max_depth
        self.show_files = show_files
        self.collapse_dirs = collapse_dirs

        self.lines: list[str] = []

    def generate_tree(self) -> list[str]:
        """
        Generate repository tree.

        Returns
        -------
        list[str]
        """

        self.lines = ["."]
        self._collect(
            base_path=self.root_directory,
            prefix="",
            depth=1,
        )

        return self.lines

    def detect_top_directories(
        self,
    ) -> list[str]:
        """
        Detect top-level directories.

        Returns
        -------
        list[str]
        """

        directories: list[str] = []

        for item in self.root_directory.iterdir():
            if item.is_dir() and not self.ignore_loader.is_ignored(item.name):
                directories.append(item.name)

        return sorted(directories)

    def _collect(
        self,
        *,
        base_path: Path,
        prefix: str,
        depth: int,
    ) -> None:
        """
        Recursive tree collector.
        """

        if depth > self.max_depth:
            return

        entries = sorted(
            [
                item
                for item in base_path.iterdir()
                if not self.ignore_loader.is_ignored(item.name)
            ],
            key=lambda item: (
                not item.is_dir(),
                item.name.lower(),
            ),
        )

        if not self.show_files:
            entries = [item for item in entries if item.is_dir()]

        total = len(entries)

        for index, entry in enumerate(entries):
            is_last = index == total - 1

            connector = "└── " if is_last else "├── "

            line = prefix + connector + entry.name

            #
            # Collapsed directories
            #
            if entry.is_dir() and entry.name in self.collapse_dirs:
                line += "/ ... (collapsed)"
                self.lines.append(line)
                continue

            self.lines.append(line)

            if entry.is_dir():
                extension = "    " if is_last else "│   "

                self._collect(
                    base_path=entry,
                    prefix=prefix + extension,
                    depth=depth + 1,
                )
