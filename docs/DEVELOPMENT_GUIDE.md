---
# 🧑‍💻 Development Guide
---

This document explains how to develop and extend the project.

---

## ⚙️ Setup

### 1. Clone repository

```bash
git clone <repo-url>
cd doc-gen
```

---

### 2. Install in development mode

```bash
pip install -e .
```

---

## 🚀 Running the CLI

```bash
doc-gen generate
doc-gen print
doc-gen analyze
doc-gen init
```

---

## 🧠 Core Components

### 1. CLI (`cli.py`)

Handles:

- argument parsing
- command routing
- config merging

---

### 2. Config System

```
config/
├── settings.py
├── profiles.py
├── file_loader.py
```

Handles:

- defaults
- profiles
- `.projectstructure.toml`

---

### 3. Scanner

```
core/scanner/structure_scanner.py
```

Handles:

- directory traversal
- ignore rules
- smart mode
- project size detection

---

### 4. Generator

```
core/generator/markdown_generator.py
```

Handles:

- markdown generation
- structure formatting

---

### 5. Utils

```
utils/
├── logging.py
├── console.py
├── progress.py
├── init.py
```

Handles:

- logging
- CLI UI
- progress
- initialization

---

## 🧠 Smart Mode

Smart mode automatically adjusts:

- depth
- file visibility
- collapsing rules

Based on:

- project size
- heuristics

---

## 📄 Config File

```
.projectstructure.toml
```

Used to define project-specific behavior.

---

## 🛠️ Development Workflow

1. Modify code
2. Run CLI locally
3. Validate output
4. Update documentation

---

## 📌 Best Practices

- Keep functions small
- Use type hints
- Use logging (not print)
- Avoid duplication
