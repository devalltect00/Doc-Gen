<!-- docs/architecture/workflow.md -->

# Architecture Workflow

This document describes the workflows and execution flows in DocGen.

---

## High-Level Flow

```text
User Command
    │
    ▼
CLI Parser
    │
    ▼
Command Handler
    │
    ▼
Core Service
    │
    ▼
Output (Console / File)
```

---

## Initialization Flow

```text
doc-gen init
    │
    ├── Load configuration
    ├── Resolve args (--mode, --force, --ask)
    ├── Build initialization spec
    │
    └── Write artifacts
        │
        ├── Config files
        └── Template files
```

---

## Structure Generation Flow

```text
doc-gen structure generate
    │
    ├── Read safe repository markers
    ├── Build a composable project fingerprint
    ├── Resolve common + ecosystem + framework metadata
    ├── Build project-aware ignore rules
    ├── Scan target directory
    ├── Build directory tree
    ├── Apply profiles (minimal/default/detailed)
    ├── Apply smart mode (if enabled)
    │
    └── Generate markdown
        │
        ├── Normalize whitespace and line endings
        └── Write the configured output path
            └── docs/project_structure.md by default
```

The Markdown writer owns persistence normalization. Renderers remain focused on
content, while the writer guarantees UTF-8, LF line endings, no trailing
whitespace, no repeated blank lines, and one final newline. Dry-run renders the
same normalized document in memory without creating the output path.

---

## Structure Print Flow

```text
doc-gen structure print
    │
    ├── Scan target directory
    ├── Build directory tree
    ├── Apply profiles
    ├── Apply smart mode (if enabled)
    │
    └── Print to console
        │
        └── Rich-formatted output
```

---

## Analysis Flow

```text
doc-gen structure analyze
    │
    ├── Scan target directory
    ├── Extract metadata
    ├── Calculate statistics
    │
    └── Present analysis
        │
        ├── Metrics
        └── Recommendations
```

---

## Configuration Resolution

```text
CLI Options
    │
    ▼
Environment Variables
    │
    ▼
Config File (.config/doc_gen/config.toml)
    │
    ▼
Default Values
```

---

## Extension Points

The architecture supports extensions through:

1. **Detection signals** - Add safe project markers without changing commands
2. **Metadata catalogs** - Extend ecosystem or framework documentation
3. **Custom profiles** - Extend output-depth behavior
4. **Custom renderers** - Add new output formats
5. **Custom analyzers** - Add new analysis methods

---

## Related Documentation

- [Design Patterns](design-patterns.md)
- [Diagrams](diagrams.md)
