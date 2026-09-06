# app/doc_gen/core/structure/scanner/project_analyzer.py

"""
Project size and complexity analysis.
"""

from os import walk
from pathlib import Path


class ProjectAnalyzer:
    """
    Analyze repository size and complexity.
    """

    def __init__(
        self,
        root_directory: Path,
        ignore_loader,
    ) -> None:
        self.root_directory = root_directory
        self.ignore_loader = ignore_loader

    def get_project_size(
        self,
        include_folders: bool = True,
    ) -> int:
        """
        Count repository items.
        """

        total = 0

        for _, dirs, files in walk(self.root_directory):
            dirs[:] = [d for d in dirs if not self.ignore_loader.is_ignored(d)]

            if include_folders:
                total += len(dirs)

            total += sum(1 for file in files if not self.ignore_loader.is_ignored(file))

        return total

    def calculate_project_score(
        self,
        include_folders: bool = True,
    ) -> int:
        """
        Calculate repository complexity score.
        """

        total = self.get_project_size(include_folders=include_folders)

        root_items = {item.name for item in self.root_directory.iterdir()}

        has_node = "package.json" in root_items or "node_modules" in root_items

        has_venv = any(
            name.startswith("venv") or name.startswith(".venv") for name in root_items
        )

        has_dist = "dist" in root_items or "build" in root_items

        score = 0

        if total > 2000:
            score += 3
        elif total > 500:
            score += 2
        else:
            score += 1

        if has_node:
            score += 1

        if has_venv:
            score += 1

        if has_dist:
            score += 1

        return score

    def get_project_category(
        self,
    ) -> str:
        """
        Human-friendly project category.
        """

        score = self.calculate_project_score()

        if score >= 5:
            return "large"

        if score >= 3:
            return "medium"

        return "small"
