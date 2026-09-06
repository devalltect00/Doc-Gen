<!-- docs/configuration.md -->

# Configuration

This document describes how DocGen can be configured.

## Overview

DocGen works out of the box with sensible defaults and typically requires little or no configuration.

Configuration may be provided through:

- Command-line options
- Configuration files
- Environment variables (if supported)
- Future extensions

---

## Default Behavior

By default, DocGen:

- Scans the current directory
- Generates a PROJECT_STRUCTURE.md file
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
```

---

## Environment Variables

Future versions may support environment variables.

Example:

```bash
DOC_GEN_PROFILE=minimal
DOC_GEN_MAX_DEPTH=2
DOC_GEN_SMART=true
```

---

## Configuration Priority

When multiple configuration sources exist, the following priority should apply:

```text
Command Line Arguments
    ↓
Environment Variables
    ↓
Configuration File
    ↓
Built-in Defaults
```

---

## Best Practices

### Use Version Control

Store project configuration files in version control.

Example:

```text
.projectstructure.toml
```

### Keep Configuration Minimal

Only override settings when necessary.

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
