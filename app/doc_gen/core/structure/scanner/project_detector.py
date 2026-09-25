# app/doc_gen/core/structure/scanner/project_detector.py

"""
Project type detection.

Responsible only for identifying the project type
based on repository contents.

Detection is deliberately based on safe repository markers. It never reads
credential-bearing files such as ``.clasp.json``.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover - Python 3.9-3.10 compatibility
    import tomli as tomllib

from doc_gen.core.structure.scanner.enums import (
    ProjectType,
)
from doc_gen.core.structure.scanner.models import ProjectFingerprint


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

        return self.detect_fingerprint().primary_type

    def detect_fingerprint(
        self,
        override: ProjectType | None = None,
    ) -> ProjectFingerprint:
        """Detect a project fingerprint while honoring an explicit override.

        Args:
            override: Optional primary type selected by configuration or CLI.

        Returns:
            A composable project fingerprint with stable, sorted signals.
        """

        root_items = {item.name for item in self.root_directory.iterdir()}
        package_dependencies = self._read_package_dependencies()
        python_dependencies = self._read_python_dependencies()
        composer_dependencies = self._read_composer_dependencies()
        go_dependencies = self._read_go_dependencies()

        ecosystems: set[str] = set()
        frameworks: set[str] = set()
        tools: set[str] = set()

        if "package.json" in root_items:
            ecosystems.add("javascript")
        if "tsconfig.json" in root_items or "typescript" in package_dependencies:
            ecosystems.add("typescript")
        if "pnpm-lock.yaml" in root_items or "pnpm-workspace.yaml" in root_items:
            tools.add("pnpm")
        elif "yarn.lock" in root_items:
            tools.add("yarn")
        elif "package-lock.json" in root_items:
            tools.add("npm")

        has_apps_script = bool(
            "@google/clasp" in package_dependencies
            or ".claspignore" in root_items
            or "appsscript.json" in root_items
            or (self.root_directory / "src" / "appsscript.json").is_file()
        )
        if has_apps_script:
            ecosystems.add("javascript")
            frameworks.add("google-apps-script")
            tools.add("clasp")

        has_next = bool(
            "next" in package_dependencies
            or any(
                name in root_items
                for name in (
                    "next.config.js",
                    "next.config.mjs",
                    "next.config.ts",
                )
            )
        )
        has_react = bool(
            "react" in package_dependencies or "react-scripts" in package_dependencies
        )
        if has_next:
            frameworks.add("nextjs")
        elif has_react:
            frameworks.add("reactjs")

        has_python = bool(
            "pyproject.toml" in root_items
            or "requirements.txt" in root_items
            or "setup.py" in root_items
        )
        if has_python:
            ecosystems.add("python")
        if "django" in python_dependencies or "manage.py" in root_items:
            frameworks.add("django")
        if "fastapi" in python_dependencies:
            frameworks.add("fastapi")
        if "flask" in python_dependencies:
            frameworks.add("flask")

        has_php = bool("composer.json" in root_items or composer_dependencies)
        if has_php:
            ecosystems.add("php")
        if "laravel/framework" in composer_dependencies or "artisan" in root_items:
            frameworks.add("laravel")

        has_go = "go.mod" in root_items
        if has_go:
            ecosystems.add("go")
        if "github.com/gin-gonic/gin" in go_dependencies:
            frameworks.add("gin")

        primary_type = override or self._select_primary_type(
            has_apps_script=has_apps_script,
            has_next=has_next,
            has_react=has_react,
            has_python=has_python,
            frameworks=frameworks,
            has_php=has_php,
            has_go=has_go,
            has_node="package.json" in root_items,
        )

        self._add_override_signals(
            primary_type,
            ecosystems=ecosystems,
            frameworks=frameworks,
        )

        return ProjectFingerprint(
            primary_type=primary_type,
            ecosystems=tuple(sorted(ecosystems)),
            frameworks=tuple(sorted(frameworks)),
            tools=tuple(sorted(tools)),
        )

    @staticmethod
    def _select_primary_type(
        *,
        has_apps_script: bool,
        has_next: bool,
        has_react: bool,
        has_python: bool,
        frameworks: set[str],
        has_php: bool,
        has_go: bool,
        has_node: bool,
    ) -> ProjectType:
        """Select the most specific primary type from collected signals."""

        if has_apps_script:
            return ProjectType.GOOGLE_APPS_SCRIPT
        if "laravel" in frameworks:
            return ProjectType.LARAVEL
        if "gin" in frameworks:
            return ProjectType.GIN
        if "django" in frameworks:
            return ProjectType.DJANGO
        if "fastapi" in frameworks:
            return ProjectType.FASTAPI
        if "flask" in frameworks:
            return ProjectType.FLASK
        if has_next:
            return ProjectType.NEXTJS
        if has_react:
            return ProjectType.REACTJS
        if has_python:
            return ProjectType.PYTHON
        if has_php:
            return ProjectType.PHP
        if has_go:
            return ProjectType.GO
        if has_node:
            return ProjectType.NODEJS
        return ProjectType.GENERIC

    @staticmethod
    def _add_override_signals(
        project_type: ProjectType,
        *,
        ecosystems: set[str],
        frameworks: set[str],
    ) -> None:
        """Ensure a manual primary-type override has matching catalog signals."""

        mapping = {
            ProjectType.PYTHON: ("python", None),
            ProjectType.DJANGO: ("python", "django"),
            ProjectType.FLASK: ("python", "flask"),
            ProjectType.FASTAPI: ("python", "fastapi"),
            ProjectType.NODEJS: ("javascript", None),
            ProjectType.REACTJS: ("javascript", "reactjs"),
            ProjectType.NEXTJS: ("javascript", "nextjs"),
            ProjectType.GOOGLE_APPS_SCRIPT: (
                "javascript",
                "google-apps-script",
            ),
            ProjectType.PHP: ("php", None),
            ProjectType.LARAVEL: ("php", "laravel"),
            ProjectType.GO: ("go", None),
            ProjectType.GIN: ("go", "gin"),
        }
        ecosystem, framework = mapping.get(project_type, (None, None))
        if ecosystem:
            ecosystems.add(ecosystem)
        if framework:
            frameworks.add(framework)

    def _read_package_dependencies(
        self,
    ) -> set[str]:
        """
        Read dependencies from package.json.

        Returns
        -------
        set[str]
        """

        data = self._read_json(self.root_directory / "package.json")
        return self._dependency_keys(data, "dependencies", "devDependencies")

    def _read_python_dependencies(self) -> set[str]:
        """Read normalized dependency names from safe Python manifests."""

        dependencies: set[str] = set()
        requirements = self.root_directory / "requirements.txt"
        try:
            for line in requirements.read_text(encoding="utf-8").splitlines():
                name = self._normalize_dependency(line)
                if name:
                    dependencies.add(name)
        except OSError:
            pass

        pyproject = self.root_directory / "pyproject.toml"
        try:
            with pyproject.open("rb") as file:
                data = tomllib.load(file)
        except (OSError, tomllib.TOMLDecodeError, TypeError):
            return dependencies

        project = data.get("project", {})
        if isinstance(project, dict):
            raw_dependencies = project.get("dependencies", [])
            if isinstance(raw_dependencies, list):
                dependencies.update(
                    name
                    for item in raw_dependencies
                    if (name := self._normalize_dependency(str(item)))
                )

            optional = project.get("optional-dependencies", {})
            if isinstance(optional, dict):
                for values in optional.values():
                    if isinstance(values, list):
                        dependencies.update(
                            name
                            for item in values
                            if (name := self._normalize_dependency(str(item)))
                        )

        poetry = data.get("tool", {}).get("poetry", {})
        if isinstance(poetry, dict):
            poetry_dependencies = poetry.get("dependencies", {})
            if isinstance(poetry_dependencies, dict):
                dependencies.update(str(name).lower() for name in poetry_dependencies)

        return dependencies

    def _read_composer_dependencies(self) -> set[str]:
        """Read dependency names from composer.json when available."""

        data = self._read_json(self.root_directory / "composer.json")
        return self._dependency_keys(data, "require", "require-dev")

    def _read_go_dependencies(self) -> set[str]:
        """Read module references from go.mod without executing Go tooling."""

        try:
            content = (self.root_directory / "go.mod").read_text(encoding="utf-8")
        except OSError:
            return set()
        return {
            token
            for token in content.replace("(", " ").replace(")", " ").split()
            if "." in token and "/" in token
        }

    @staticmethod
    def _read_json(path: Path) -> dict[str, Any]:
        """Read an object-valued JSON file, returning an empty object on failure."""

        try:
            with path.open("r", encoding="utf-8") as file:
                data = json.load(file)
        except (OSError, json.JSONDecodeError, TypeError):
            return {}
        return data if isinstance(data, dict) else {}

    @staticmethod
    def _dependency_keys(data: dict[str, Any], *sections: str) -> set[str]:
        """Return normalized dependency keys from object-valued sections."""

        dependencies: set[str] = set()
        for section in sections:
            values = data.get(section, {})
            if isinstance(values, dict):
                dependencies.update(str(name).lower() for name in values)
        return dependencies

    @staticmethod
    def _normalize_dependency(value: str) -> str:
        """Extract a normalized package name from a requirement string."""

        candidate = value.split("#", 1)[0].strip()
        if not candidate or candidate.startswith(("-", "http://", "https://")):
            return ""
        return re.split(r"[\s<>=!~;\[]", candidate, maxsplit=1)[0].lower()
