# 📦 Project Structure Generator

<!-- ![Python](https://img.shields.io/pypi/pyversions/doc-gen) -->
<!-- ![License](https://img.shields.io/badge/license-MIT-green) -->

![Python](https://img.shields.io/badge/python-3.14+-blue.svg)
![Versioning](https://img.shields.io/badge/versioning-SemVer-3F4551.svg)
![Tag](https://img.shields.io/github/v/tag/devalltect00/Doc-Gen)
![License](https://img.shields.io/github/license/devalltect00/Doc-Gen)
![Build](https://img.shields.io/badge/CI-GitHub%20Actions-success)
![Coverage](https://img.shields.io/badge/coverage-tracked-success)
![Ruff](https://img.shields.io/badge/lint-ruff-purple.svg)
![Black](https://img.shields.io/badge/code%20style-black-000000.svg)
![Pytest](https://img.shields.io/badge/tested%20with-pytest-0A9EDC.svg)
![Documentation](https://img.shields.io/badge/docs-online-success.svg)
![MkDocs](https://img.shields.io/badge/docs-MkDocs-success.svg)
![Docker](https://img.shields.io/badge/docker-supported-2496ED?logo=docker&logoColor=white)
![Docker Release](https://img.shields.io/badge/docker-release%20images-2496ED?logo=docker&logoColor=white)
![Docker Commit](https://img.shields.io/badge/docker-commit%2Fsha%20images-1D63ED?logo=docker&logoColor=white)
![Release](https://img.shields.io/github/v/release/devalltect00/Path-Header-Scanner)
![Developer Tool](https://img.shields.io/badge/category-developer--tool-orange.svg)

A professional CLI tool to automatically generate a clean and well-documented `PROJECT_STRUCTURE.md` from your repository.

It helps developers quickly understand project layout.

---

## ✨ Features

- 📂 Generate repository tree structure
- 📄 Auto-generate `PROJECT_STRUCTURE.md`
- 🧠 Smart mode (auto-detect project size & optimize output)
- 🎯 Profiles (`minimal`, `default`, `detailed`)
- ⚙️ Config file support (`.projectstructure.toml`)
- 🎨 Colored CLI output (rich UI)
- ⚡ Fast and lightweight
- 🛡️ Explicit dry-run safety for initialization and generated output

---

## 🚀 Quick Start

```bash
pip install doc-gen
doc-gen generate
```

📄 Output:

```text
PROJECT_STRUCTURE.md
```

---

## 🧰 Useful Docs

- 📘 [User Guide Overview](docs/user-guide/overview.md)
- 📖 [CLI Commands Reference](docs\reference\cli-reference.md)
- 📖 [Makefile Commands Reference](docs/developer-guide/make-workflow.md)

---

## 📖 Documentation

### 🚀 Getting Started

- Installation → [`docs/getting-started/installation.md`](docs/getting-started/installation.md)
- Quickstart → [`docs/getting-started/quickstart.md`](docs/getting-started/quickstart.md)

### 📘 User Guide

- Overview → [`docs/user-guide/overview.md`](docs/user-guide/overview.md)
- Commands → [`docs/user-guide/commands.md`](docs/user-guide/commands.md)
- Config → [`docs/user-guide/config.md`](docs/user-guide/config.md)
- Smart Mode → [`docs/user-guide/smart-mode.md`](docs/user-guide/smart-mode.md)
- Examples → [`docs/user-guide/examples.md`](docs/user-guide/examples.md)

### 📚 Reference

- CLI Reference → [`docs/reference/cli-reference.md`](docs/reference/cli-reference.md)

### 🛠 Development

- Setup → [`docs/development/setup.md`](docs/development/setup.md)
- Makefile → [`docs/developer-guide/make-workflow.md`](docs/developer-guide/make-workflow.md)

### 🧱 System

- Architecture → [`docs/system/architecture.md`](docs/system/architecture.md)

---

## 🧑‍💻 Usage

```bash
doc-gen generate
doc-gen print
doc-gen analyze
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

Create `.projectstructure.toml`:

```toml
[tool.doc-gen]

profile = "minimal"
max_depth = 2
show_files = false
smart_mode = true
```

---

## 🧠 Smart Mode

Automatically adjusts:

- depth
- file visibility
- directory collapsing

```bash
doc-gen generate --smart
```

---

## 📁 Project Structure

```text
app/doc_gen/
├── cli.py
├── config/
├── scanner/
├── generator/
├── utils/
```

For the details, see full structure in [`project_structure.md`](docs/project_structure.md).

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

MIT License

Copyright © 2026
This software is **not open source**.
You may not copy, distribute, or modify without permission.

📧 Contact: `rizkypffdev37@gmail.com`

---

_Handcrafted with ❤️ by Devalltect / Rizky Fernandes_
