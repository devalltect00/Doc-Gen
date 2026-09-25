<!-- docs/configuration.md -->

# Configuration

This document describes how Doc Gen can be configured.

## Overview

DocGen works out of the box with sensible defaults and typically requires little or no configuration.

Configuration may be provided through:

- Command-line options
- Configuration files

---

## Default Behavior

By default, DocGen:

- Scans the current directory
- Generates `docs/project_structure.md`
- Uses the "default" profile
- Shows full directory tree
- Does not include hidden files

Example:

```bash
doc-gen structure generate
```

---

## Command-Line Configuration

Most configuration is provided through command-line options.

### Profile Selection

```bash
doc-gen structure generate --profile minimal
doc-gen structure generate --profile default
doc-gen structure generate --profile detailed
```

### Smart Mode

```bash
doc-gen structure generate --smart
```

Smart mode automatically adjusts:

- Maximum depth based on project size
- File visibility based on project complexity
- Directory collapsing

### Maximum Depth

```bash
doc-gen structure generate --max-depth 2
doc-gen structure generate --max-depth 5
```

### Show Files

```bash
doc-gen structure generate --show-files
doc-gen structure generate --hide-files
```

### Dry-run Mode

```bash
doc-gen init --dry-run
doc-gen structure generate --dry-run
```

Dry-run blocks initialization and generated Markdown writes while allowing
read-only scanning and preview rendering.

---

## Configuration File

### File Location

Doc Gen looks for configuration in:

```text
.config/doc_gen/config.toml
```

Priority:

```text
CLI Options
    ↓
Project Configuration (`.config/doc_gen/config.toml`)
    ↓
Default Settings
```

### Example Configuration

Create `.config/doc_gen/config.toml`:

```toml
[tool.doc-gen.cli.execution]
dry_run = false

[tool.doc-gen.cli.structure]

# Profile: minimal, default, or detailed
profile = "default"

# Maximum directory depth
max_depth = 3

# Show individual files
show_files = true

# Enable smart mode
smart_mode = false

# Optional primary-type override. Leave unset for automatic detection.
# project_type = "laravel"
```

### Project detection

Automatic detection combines safe repository markers from multiple ecosystems.
For example, a Google Apps Script repository can contribute JavaScript,
TypeScript, clasp, and Apps Script metadata at the same time. Supported primary
overrides are:

```text
generic, python, django, flask, fastapi,
nodejs, reactjs, nextjs, google-apps-script,
php, laravel, go, gin
```

Use an override from the CLI when automatic detection needs help:

```bash
doc-gen structure generate --project-type google-apps-script
```

The override selects the primary project label. Safe secondary signals may
still extend the metadata and ignore rules. Doc Gen never reads local clasp
credential configuration while detecting Google Apps Script projects.

---

## Configuration Priority

When multiple configuration sources exist, the following priority should apply:

```text
Command Line Arguments
    ↓
Project Configuration (`.config/doc_gen/config.toml`)
    ↓
Built-in Defaults
```

---

## Best Practices

### Use Version Control

Store project configuration files in version control.

The canonical project configuration is `.config/doc_gen/config.toml`.

### Keep Configuration Minimal

Only override settings when necessary.

### Generated Markdown quality

The configured output remains fully project-controlled:

```toml
[tool.doc-gen.cli.structure.generate]
output_file = "docs/project_structure.md"
```

Doc Gen writes the selected Markdown file with UTF-8 encoding, LF line endings,
no trailing spaces or tabs, no repeated blank lines, and exactly one final
newline. This keeps the generated artifact compatible with common
`trailing-whitespace` and `end-of-file-fixer` pre-commit hooks and minimizes
formatter-only changes.

Doc Gen does not execute project-owned formatters or hooks automatically.
Projects with additional Markdown policies should still validate the generated
file with their normal quality workflow.

### Prefer Project-Level Configuration

Avoid machine-specific settings whenever possible.

---

## Related Documentation

- Installation Guide
- Usage Guide
- Project Structure Guide
- Developer Guide
- Dry-run Safety Guide
- Infrastructure Guide
