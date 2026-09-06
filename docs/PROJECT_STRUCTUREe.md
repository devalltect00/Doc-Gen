<!-- docs/PROJECT_STRUCTUREe.md -->

# Project Structure

# Repository Overview

This repository follows a modular structure commonly used in modern projects.

Common directories include:

- `app/` — Main application source code.
- `.config/` — Project configuration files.
- `.github/` — GitHub-related configuration.
- `.vscode/` — Visual Studio Code workspace settings.
- `docs/` — Project documentation and technical references.
- `tests/` — Automated tests.
- `data/` — Input datasets or static data.
- `output/` — Generated outputs from the application.
- `scripts/` — Utility scripts for development or automation.
- `tools/` — Development tools and automation utilities.
- `templates/` — Reusable templates used by the project.

---

# Repository Structure

(project type: ProjectType.PYTHON)

```text
.
├── .config
│   ├── doc_gen
│   └── path_header_scanner
├── .ruff_cache
│   └── 0.15.7
├── app
│   └── doc_gen
├── dist/ ... (collapsed)
├── docs
│   ├── architecture
│   ├── developer-guide
│   ├── diagrams
│   ├── project
│   ├── reads
│   ├── testing
│   └── user-guide
├── logs
├── make_file
├── scripts
│   ├── docker
│   └── docs
├── src
├── tests
│   ├── cli
│   ├── config
│   ├── config_before
│   ├── core
│   ├── services
│   ├── theme
│   ├── unit
│   └── utils
├── venv/ ... (collapsed)
└── venv_3_14
    ├── Include
    ├── Lib
    └── Scripts
```

---

## Root Files

| File | Description |
|------|-------------|
| `README.md` | Project overview and introduction. |
| `CHANGELOG.md` | History of notable changes between releases. |
| `LICENSE` | Project license information. |
| `CONTRIBUTING.md` | Guidelines for contributing to the project. |
| `SECURITY.md` | Security policy and vulnerability reporting instructions. |
| `TODO.md` | Pending tasks and future improvements. |
| `AGENTS.md` | Instructions and guidance for AI agents and automation tools. |
| `DEVELOPMENT_GUIDE.md` | Guide for developers working on the project. |
| `ENGINEERING_EXECUTION_POLICY.md` | Engineering execution standards and policies. |
| `pyproject.toml` | Main Python project configuration file. |
| `requirements.txt` | Python package dependencies. |
| `mkdocs.yml` | MkDocs documentation site configuration. |
| `Makefile` | Defines common development, testing, and build commands. |
| `Dockerfile` | Container image build instructions. |
| `docker-compose.yml` | Default multi-container Docker configuration. |
| `docker-compose.dev.yml` | Development Docker Compose configuration. |
| `docker-compose.prod.yml` | Production Docker Compose configuration. |
| `.gitignore` | Specifies files and directories ignored by Git. |
| `.dockerignore` | Specifies files excluded from Docker build context. |
| `.prettierrc.json` | Prettier code formatting configuration. |
| `.prettierignore` | Files ignored by Prettier. |
| `.pre-commit-config.yaml` | Pre-commit hooks configuration. |
| `.custor.toml` | Custom configuration file used by project tools. |
| `.gitlab-ci.yml` | GitLab CI/CD pipeline configuration. |

---

## Directory Details

### `.config/`
Project configuration files.

Stores reusable configuration files used by the project.
Helps keep the repository root clean and organized.

Common examples:
- .config/tool-config/
- .config/templates/
- .config/settings/

### `app/`
Main application source code.

Contains the core implementation of the project.
May include business logic, services, modules, and utilities.

### `docs/`
Project documentation and technical references.

The documentation folder usually contains structured knowledge about the project.

Common documentation sections:
- docs/architecture        → system design and architecture diagrams
- docs/development         → development guides and workflows
- docs/system              → detailed technical documentation
- docs/reference           → command references and APIs
- docs/user-guide          → instructions for end users
- docs/diagrams            → visual architecture diagrams
- docs/phases              → project phases and planning
- docs/Q&A                 → common questions and explanations

Common files:
- PROJECT_STRUCTURE.md
- DEVELOPMENT_GUIDE.md
- HOW_TO_USE.md
- TODO.md
- CLI_COMMAND.md
- references.md
- badges.md

### `scripts/`
Utility scripts for development or automation.

May include deployment scripts, maintenance tools, or helpers.

### `tests/`
Automated tests.

Contains unit tests and integration tests.
Ensures code reliability and correctness.


---

## Notes

- Temporary files, caches, and environment directories are excluded.
- Structure is generated automatically using DocGen.
