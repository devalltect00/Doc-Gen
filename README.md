# 📦 Doc Gen — Repository Structure Documentation CLI

<!-- ![Python](https://img.shields.io/pypi/pyversions/doc-gen) -->
<!-- ![License](https://img.shields.io/badge/license-MIT-green) -->

[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![Versioning](https://img.shields.io/badge/versioning-SemVer-3F4551.svg)](https://semver.org/)
[![Tag](https://img.shields.io/github/v/tag/devalltect00/Doc-Gen)](https://github.com/devalltect00/Doc-Gen/tags)
[![License](https://img.shields.io/github/license/devalltect00/Doc-Gen)](LICENSE)
[![Build](https://img.shields.io/badge/CI-GitHub%20Actions-success)](https://github.com/devalltect00/Doc-Gen/actions)
![Coverage](https://img.shields.io/badge/coverage-tracked-success)
[![Ruff](https://img.shields.io/badge/lint-ruff-purple.svg)](https://docs.astral.sh/ruff/)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://black.readthedocs.io/)
[![Pytest](https://img.shields.io/badge/tested%20with-pytest-0A9EDC.svg)](https://docs.pytest.org/)
[![Documentation](https://img.shields.io/badge/docs-online-success.svg)](https://devalltect00.github.io/devalltect-docs/docs/doc-gen)
[![MkDocs](https://img.shields.io/badge/docs-MkDocs-success.svg)](https://www.mkdocs.org/)
[![Docker](https://img.shields.io/badge/docker-supported-2496ED?logo=docker&logoColor=white)](docs/developer-guide/docker-workflow.md)
[![Docker Release](https://img.shields.io/badge/docker-release%20images-2496ED?logo=docker&logoColor=white)](https://github.com/devalltect00/Doc-Gen/pkgs/container/doc-gen)
[![Docker Commit](https://img.shields.io/badge/docker-commit%2Fsha%20images-1D63ED?logo=docker&logoColor=white)](https://github.com/devalltect00/Doc-Gen/pkgs/container/doc-gen)
[![Release](https://img.shields.io/github/v/release/devalltect00/Doc-Gen)](https://github.com/devalltect00/Doc-Gen/releases)
[![Developer Tool](https://img.shields.io/badge/category-developer--tool-orange.svg)](https://github.com/devalltect00/Doc-Gen)

Doc Gen generates Markdown project trees, prints directory structures, and
analyzes repository layout. Use profiles, smart mode, and explicit output
paths to tailor the result.

The v0.1.0 project was named `print_project_structure`; the rename to Doc Gen
is part of v1.0.0-rc.1, not a later stable-only change.

---

## ℹ️ Project Metadata

| Property                     | Value                                         |
| ---------------------------- | --------------------------------------------- |
| Project                      | Doc Gen                                       |
| Current version              | `v1.0.1`                                      |
| Python package               | `doc-gen`                                     |
| Package compatibility        | Python 3.9+                                   |
| Standard development runtime | Python 3.14                                   |
| CLI framework                | Typer and Rich                                |
| Version strategy             | SemVer tags and PEP 440 package versions      |
| Distribution                 | Source, private GitLab PyPI, Docker, and GHCR |
| Documentation                | Devalltect Docs and repository documentation  |
| License                      | MIT                                           |
| Maintainer                   | Devalltect / Rizky Fernandes                  |

---

## ✨ Features

- 📂 Generate repository tree structure
- 📄 Generate Markdown at a configured or explicitly selected output path
- 🔎 Separate read-only structure printing and analysis commands
- 🧠 Smart mode (auto-detect project size & optimize output)
- 🎯 Profiles (`minimal`, `default`, `detailed`)
- ⚙️ Namespaced configuration in `.config/doc_gen/config.toml`
- 🎨 Colored CLI output (rich UI)
- ⚡ Fast and lightweight
- 🛡️ Explicit dry-run safety for initialization and generated output

---

## 📦 Installation

Runtime compatibility is Python 3.9+; the standard development and container
runtime is Python 3.14. Contributor formatting tools have their own newer
Python requirements; use Python 3.14 for the complete development environment.

### 🔐 Install a private GitLab package

Choose a version already published in the target project's registry. In an
activated virtual environment, replace the placeholders:

```text
python -m pip install --index-url "https://gitlab.com/api/v4/projects/<project-id>/packages/pypi/simple" "doc-gen==<package-version>"
doc-gen --help
```

Use a deploy token with `read_package_registry`. Supply credentials through
[pip authentication](https://pip.pypa.io/en/stable/topics/authentication/),
not committed files or shared command history. The package version is PEP 440:
`v1.0.0-rc.1` becomes `1.0.0rc1`; `v1.0.0` becomes `1.0.0`.
Use `--index-url`, not `--extra-index-url`; review
[GitLab package forwarding](https://docs.gitlab.com/user/packages/pypi_repository/#package-request-forwarding-security-notice)
if dependencies must stay private.

See [installation and registry guidance](docs/user-guide/installation-methods.md) for authentication,
other installation methods, and registry setup.

### 🧑‍💻 Install from a source checkout

Create and activate a virtual environment, then install from the source root:

```bash
python -m pip install -e .
doc-gen --help
```

## 🚀 Quick Start

Preview initialization, then create the configuration when ready:

```bash
doc-gen init --dry-run
doc-gen init
```

Review `.config/doc_gen/config.toml`. Preview generation before writing output:

```bash
doc-gen structure generate . --output docs/project_structure.md --dry-run
doc-gen structure generate . --output docs/project_structure.md
```

The second command writes `docs/project_structure.md`. Without `--output`,
the selected configuration or internal default determines the path.

---

## 🧰 Useful Docs

- 📘 [User Guide Overview](docs/user-guide/overview.md)
- 📖 [CLI Commands Reference](docs/user-guide/commands.md)
- 📖 [Makefile Commands Reference](docs/developer-guide/make-workflow.md)

---

## 📖 Documentation

### 🚀 Getting Started

- Installation → [`docs/user-guide/installation-methods.md`](docs/user-guide/installation-methods.md)
- Quickstart → [`docs/user-guide/quickstart.md`](docs/user-guide/quickstart.md)

### 📘 User Guide

- Overview → [`docs/user-guide/overview.md`](docs/user-guide/overview.md)
- Commands → [`docs/user-guide/commands.md`](docs/user-guide/commands.md)
- Config → [`docs/configuration.md`](docs/configuration.md)
- Smart Mode → [`docs/user-guide/smart-mode.md`](docs/user-guide/smart-mode.md)
- Examples → [`docs/usage.md`](docs/usage.md)

### 📚 Reference

- CLI Reference → [`docs/user-guide/commands.md`](docs/user-guide/commands.md)

### 🛠 Development

- Setup → [`docs/developer-guide/getting-started.md`](docs/developer-guide/getting-started.md)
- Makefile → [`docs/developer-guide/make-workflow.md`](docs/developer-guide/make-workflow.md)

### 🧱 System

- Architecture → [`docs/architecture/workflow.md`](docs/architecture/workflow.md)

---

## 🧑‍💻 Usage

```bash
doc-gen structure generate
doc-gen structure print
doc-gen structure analyze
doc-gen init
```

Preview any workflow without changing project output:

```bash
doc-gen init --dry-run
doc-gen structure generate --dry-run .
doc-gen structure print --dry-run .
doc-gen structure analyze --dry-run .
```

---

## 📄 Config File Example

After `doc-gen init`, edit `.config/doc_gen/config.toml`:

```toml
[tool.doc-gen.cli.structure]
profile = "custom"
max_depth = 5
show_files = true
smart_mode = false

[tool.doc-gen.cli.structure.generate]
output_file = "docs/project_structure.md"
```

CLI options override configured values. `--dry-run` allows read-only discovery
but prevents persistent generated output; diagnostic logs may still be written.

---

## 🧠 Smart Mode

Automatically adjusts:

- depth
- file visibility
- directory collapsing

```bash
doc-gen structure generate --smart .
```

---

## 📁 Project Structure

```text
app/doc_gen/
├── cli/
├── config/
├── core/
│   ├── initialize/
│   └── structure/
├── services/
├── templates/
├── ui/
└── utils/
```

For the details, see full structure in [`project_structure.md`](docs/project_structure.md).

---

## ⚙️ Repository Metadata Helper (Maintainers)

The optional [metadata sync script](scripts/repository/src/sync_metadata.py)
is source-checkout tooling, not an installed application command. Run it from
this repository's root:

```bash
python scripts/repository/src/sync_metadata.py --dry-run
```

It reads `[project].description` and the separate
`[tool.devalltect.github].topics` / `[tool.devalltect.gitlab].topics` tables
in `pyproject.toml`. Package `keywords` are not repository topics.

Review `GITHUB_REMOTES` and `GITLAB_REMOTES` in the script: the current
defaults are `origin` and `backup`. Each list contains fallback candidates;
the first valid fetch URL selects one repository per provider. Both providers
must resolve. This helper currently targets GitHub.com and GitLab.com.

Dry-run uses Python and read-only Git discovery; it does not call provider
APIs. Live synchronization additionally needs authenticated `gh` and `glab`
with access to update those repositories.

Before removing `--dry-run`, review the targets and metadata carefully:
the live helper does not ask for confirmation, replaces the topic lists, and
clears existing topics when a list is empty or missing. A failure can leave
earlier updates applied; there is no cross-provider rollback.

Known follow-up: the script's docstring still shows the old path, and its
GitHub topic-limit constant is 50 despite
[GitHub's maximum of 20 topics](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics).
Use the path above and keep the GitHub list within 20 until corrected.
These issues and isolated test coverage are tracked in the
[TODO history](docs/TODO_tracking_history.md).

---

## 🤝 Contributing

Contributions, issues, and suggestions are welcome.

Before contributing, review: [`docs/developer-guide/`](docs/developer-guide/)

and: [`docs/architecture/`](docs/architecture/)

For the details, see [`CONTRIBUTING.md`](CONTRIBUTING.md)

---

## 🔐 Security

See [`SECURITY.md`](SECURITY.md)

---

## 📃 Changelog

See [`CHANGELOG.md`](CHANGELOG.md)

---

## 📜 License

See [LICENSE](LICENSE) for the licensing terms.

📧 Contact: `rizkypffdev37@gmail.com`

---

_Handcrafted with ❤️ by Devalltect / Rizky Fernandes_
