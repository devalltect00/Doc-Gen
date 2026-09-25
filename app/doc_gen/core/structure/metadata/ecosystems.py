"""Documentation metadata contributed by supported language ecosystems."""

ECOSYSTEM_DIRECTORIES = {
    "python": {
        "src": {
            "description": "Python source-layout package directory.",
            "details": [
                "Separates importable packages from repository-level tooling and tests.",
            ],
        },
    },
    "javascript": {
        "src": {
            "description": "JavaScript or TypeScript application source code.",
            "details": [
                "Contains runtime modules, entry points, and shared source code.",
            ],
        },
        "public": {
            "description": "Static files copied or served without compilation.",
            "details": ["May contain images, icons, manifests, and other assets."],
        },
    },
    "php": {
        "app": {
            "description": "Primary PHP application source code.",
            "details": ["Contains application services, domain code, and modules."],
        },
        "public": {
            "description": "Public web entry point and static assets.",
            "details": ["Contains files exposed by the web server."],
        },
    },
    "go": {
        "cmd": {
            "description": "Executable entry points for Go applications.",
            "details": ["Each child commonly builds a separate command."],
        },
        "internal": {
            "description": "Private Go packages scoped to this module.",
            "details": ["Go prevents external modules from importing this code."],
        },
        "pkg": {
            "description": "Reusable Go packages intended for broader imports.",
            "details": ["Contains library code shared by commands or consumers."],
        },
    },
}

ECOSYSTEM_ROOT_FILES = {
    "python": {
        "pyproject.toml": "Python project metadata and tool configuration.",
        "requirements.txt": "Python package dependencies.",
        "requirements-dev.txt": "Python development dependencies.",
        "Pipfile": "Pipenv project dependencies and environment configuration.",
        "Pipfile.lock": "Resolved Pipenv dependency versions.",
        "poetry.lock": "Resolved Poetry dependency versions.",
        "uv.lock": "Resolved uv dependency versions.",
        "mkdocs.yml": "MkDocs documentation site configuration.",
        ".python-version": "Python version selected by compatible version managers.",
        "pytest.ini": "Pytest configuration.",
        "ruff.toml": "Ruff linter and formatter configuration.",
        "mypy.ini": "MyPy static type-checking configuration.",
        "tox.ini": "Multi-environment Python test configuration.",
        ".cz.toml": "Commitizen versioning and commit-convention configuration.",
        ".cz_changelog.j2": "Commitizen changelog template.",
        ".custor.toml": "Project automation configuration.",
    },
    "javascript": {
        "package.json": "Node.js package metadata, scripts, and dependencies.",
        "package-lock.json": "npm dependency lock file.",
        "pnpm-lock.yaml": "pnpm dependency lock file.",
        "pnpm-workspace.yaml": "pnpm workspace and package-import configuration.",
        "yarn.lock": "Yarn dependency lock file.",
        "tsconfig.json": "TypeScript compiler configuration.",
        "vite.config.js": "Vite build configuration.",
        "vite.config.ts": "Vite build configuration.",
    },
    "php": {
        "composer.json": "Composer package metadata and PHP dependencies.",
        "composer.lock": "Resolved Composer dependency versions.",
    },
    "go": {
        "go.mod": "Go module identity, language version, and dependencies.",
        "go.sum": "Checksums for resolved Go module dependencies.",
    },
}
