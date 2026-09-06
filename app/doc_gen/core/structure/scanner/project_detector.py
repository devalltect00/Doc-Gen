# app/doc_gen/core/structure/scanner/project_detector.py

"""
Project type detection.

Responsible only for identifying the project type
based on repository contents.

Examples:
    python
    django
    flask
    fastapi
    nodejs
    reactjs
    nextjs
    generic
"""

import json
from pathlib import Path

from doc_gen.core.structure.scanner.enums import (
    ProjectType,
)


class ProjectDetector:
    """
    Detect project type from repository files.
    """

    def __init__(
        self,
        root_directory: Path,
    ) -> None:
        self.root_directory = root_directory

    def detect(self) -> ProjectType:
        """
        Detect project type.

        Returns
        -------
        ProjectType
            Detected project type.
        """

        root_items = {item.name for item in self.root_directory.iterdir()}

        #
        # Node ecosystem
        #
        if "package.json" in root_items:
            if ".next" in root_items or "next.config.js" in root_items:
                return ProjectType.NEXTJS

            dependencies = self._read_package_dependencies()

            if "react-scripts" in dependencies:
                return ProjectType.REACTJS

            return ProjectType.NODEJS

        #
        # Python ecosystem
        #
        if "pyproject.toml" in root_items or "requirements.txt" in root_items:
            if "manage.py" in root_items:
                return ProjectType.DJANGO

            if "main.py" in root_items or "app.py" in root_items:
                return ProjectType.PYTHON

            app_directory = self.root_directory / "app"

            if app_directory.exists():
                app_files = {item.name for item in app_directory.iterdir()}

                if (
                    "main.py" in app_files
                    or "app.py" in app_files
                    or "__init__.py" in app_files
                ):
                    return ProjectType.PYTHON

            return ProjectType.PYTHON

        return ProjectType.GENERIC

    def _read_package_dependencies(
        self,
    ) -> set[ProjectType]:
        """
        Read dependencies from package.json.

        Returns
        -------
        set[ProjectType]
        """

        package_json = self.root_directory / "package.json"

        if not package_json.exists():
            return set()

        try:
            with package_json.open(
                "r",
                encoding="utf-8",
            ) as file:
                data = json.load(file)

            return set(data.get("dependencies", {})) | set(
                data.get("devDependencies", {})
            )

        except Exception:
            return set()
