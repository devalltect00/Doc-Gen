"""Generic documentation metadata shared by supported repositories."""

COMMON_DIRECTORIES = {
    "app": {
        "description": "Main application source code.",
        "details": [
            "Contains the core implementation of the project.",
            "May include business logic, services, modules, and utilities.",
        ],
    },
    ".config": {
        "description": "Project configuration files.",
        "details": [
            "Stores reusable configuration files used by the project.",
            "Helps keep the repository root clean and organized.",
            "",
            "Common examples:",
            "",
            "- .config/tool-config/",
            "- .config/templates/",
            "- .config/settings/",
        ],
    },
    "docs": {
        "description": "Project documentation and technical references.",
        "details": [
            "Contains user guides, technical references, and project records.",
            "",
            "Possible sections include:",
            "",
            "- architecture and design decisions",
            "- developer and contributor guides",
            "- user guides and command references",
            "- generated repository documentation",
            "",
            "Doc Gen writes `docs/project_structure.md` by default, but the",
            "destination is configurable.",
        ],
    },
    "tests": {
        "description": "Automated tests.",
        "details": [
            "Contains unit tests and integration tests.",
            "Ensures code reliability and correctness.",
        ],
    },
    "data": {
        "description": "Input datasets or static data.",
        "details": [
            "May contain sample datasets, fixtures, or configuration data.",
        ],
    },
    "output": {
        "description": "Generated outputs from the application.",
        "details": [
            "Logs, reports, generated files, or exported artifacts.",
        ],
    },
    "scripts": {
        "description": "Utility scripts for development or automation.",
        "details": [
            "May include deployment scripts, maintenance tools, or helpers.",
        ],
    },
    "tools": {
        "description": "Development tools and automation utilities.",
        "details": [
            "Contains supporting programs used during development and maintenance.",
            "Tools may generate artifacts, validate the repository, or automate",
            "repeatable engineering tasks.",
        ],
    },
    "templates": {
        "description": "Reusable templates used by the project.",
        "details": [
            "May include document, configuration, message, or source templates.",
            "Templates make generated content repeatable and easier to maintain.",
        ],
    },
}

COMMON_ROOT_FILES = {
    "README.md": "Project overview and introduction.",
    "CHANGELOG.md": "History of notable changes between releases.",
    "LICENSE": "Project license information.",
    "LICENSE.md": "Project license information in Markdown format.",
    "LICENSE.txt": "Project license information in plain-text format.",
    "CONTRIBUTING.md": "Guidelines for contributing to the project.",
    "CODE_OF_CONDUCT.md": "Expected standards for community participation.",
    "SECURITY.md": "Security policy and vulnerability reporting instructions.",
    "SUPPORT.md": "Support channels and help-request guidance.",
    "AUTHORS.md": "Project authors and contributors.",
    "NOTICE": "Required legal notices and attribution information.",
    "ROADMAP.md": "Future plans and development roadmap.",
    "TODO.md": "Pending tasks and future improvements.",
    "ABOUT.md": "General information about the project.",
    "AGENTS.md": "Instructions and guidance for AI agents and automation tools.",
    "DEVELOPMENT_GUIDE.md": "Guide for developers working on the project.",
    "ENGINEERING_EXECUTION_POLICY.md": "Engineering execution standards and policies.",
    "EXECUTION_TRACKER.md": "Tracks execution progress or development stages.",
    "Makefile": "Defines common development, testing, and build commands.",
    "Dockerfile": "Container image build instructions.",
    "Dockerfile.dev": "Development container configuration.",
    "Dockerfile.prod": "Production container configuration.",
    "docker-compose.yml": "Default multi-container Docker configuration.",
    "docker-compose.dev.yml": "Development Docker Compose configuration.",
    "docker-compose.prod.yml": "Production Docker Compose configuration.",
    ".gitignore": "Specifies files and directories ignored by Git.",
    ".dockerignore": "Specifies files excluded from Docker build context.",
    ".editorconfig": "Editor configuration for consistent coding styles.",
    ".prettierrc.json": "Prettier code formatting configuration.",
    ".prettierignore": "Files ignored by Prettier.",
    ".pre-commit-config.yaml": "Pre-commit hooks configuration.",
    ".projectignore": "Ignore rules for project utilities and scanners.",
    ".gitlab-ci.yml": "GitLab CI/CD pipeline configuration.",
    ".env.example": "Example environment variables configuration.",
    ".gitattributes": "Git file handling and line-ending rules.",
}
