# app/doc_gen/utils/ignore_loader.py

import os
from fnmatch import fnmatch


class IgnoreLoader:
    """Handles ignore rules for project structure scanning."""

    def __init__(self, root_path=".", project_type="generic"):
        self.root_path = root_path
        self.project_type = project_type

        self.patterns = set()
        self._load_default_patterns()
        self._load_projectignore()
        # Optional: enable later
        # self._load_gitignore()

    # ------------------------
    # Default Ignore Patterns
    # ------------------------
    def _load_default_patterns(self):
        common = {
            ".DS_Store",
            "Thumbs.db",
            ".vscode",
            ".idea",
            ".github",
            "__pycache__",
            "mypy_cache",
            ".pytest_cache",
            "*.log",
            "*.pyc",
            "*.pyo",
            "*.pyd",
            "*.egg-info",
        }

        additional = {".git"}

        python = {
            "venv",
            "venv*",
            "dev_venv",
            "prod_venv",
            "venv_dev",
            "venv_prod",
            "publish_venv",
            "venv_publish",
            "other_venv",
            "venv_other",
            ".venv",
            ".venv*",
            "env",
            "env*",
            ".env",
            ".env*",
            ".pdm",
            ".ruff_cache",
            "migrations",
            "alembic/versions",
            "build",
            "dist",
            ".coverage",
            ".tox",
            "db.sqlite3",
            "*.egg-info",
        }

        javascript = {
            "node_modules",
            "dist",
            "build",
            ".next",
            ".turbo",
            ".parcel-cache",
            ".eslintrc",
            ".eslintcache",
            ".prettierrc",
            "yarn.lock",
            "pnpm-lock.yaml",
        }

        common |= additional

        ### Normalize project type for pattern loading
        if self.project_type in {"python", "django", "flask_or_fastapi"}:
            self.project_type = "python"
        if self.project_type in {"reactjs", "nextjs", "nodejs"}:
            self.project_type = "javascript"

        ### Load patterns based on project type
        if self.project_type == "python":
            self.patterns |= common | python
        elif self.project_type == "javascript":
            self.patterns |= common | javascript
        else:
            self.patterns |= common

    # ------------------------
    # .projectignore Support
    # ------------------------
    def _load_projectignore(self):
        path = os.path.join(self.root_path, ".projectignore")

        if not os.path.exists(path):
            return

        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()

                if not line or line.startswith("#"):
                    continue

                self.patterns.add(line)

    # ------------------------
    # (Optional) .gitignore Support
    # ------------------------
    def _load_gitignore(self):
        path = os.path.join(self.root_path, ".gitignore")

        if not os.path.exists(path):
            return

        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()

                if not line or line.startswith("#"):
                    continue

                self.patterns.add(line)

    # ------------------------
    # Check Ignore
    # ------------------------
    def is_ignored(self, name):
        """Check if a file/folder should be ignored."""
        return any(fnmatch(name, pattern) for pattern in self.patterns)

    # ------------------------
    # Debug Helper (Optional)
    # ------------------------
    def get_patterns(self):
        """Return all active ignore patterns."""
        return sorted(self.patterns)
