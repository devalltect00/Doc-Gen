# Dry-run safety

Doc Gen accepts `--dry-run` on all supported commands. Dry-run preserves useful
read-only discovery while blocking project-file mutations.

## Command behavior

| Command | Normal mutation | Dry-run behavior |
| --- | --- | --- |
| `doc-gen init` | Creates or updates `.config/doc_gen/config.toml` | Shows planned directories and files without creating, overwriting, or prompting |
| `doc-gen structure generate` | Writes the configured Markdown output | Scans and renders the preview metadata but does not create the output directory or file |
| `doc-gen structure print` | None | Runs its existing read-only scan and terminal rendering |
| `doc-gen structure analyze` | None | Runs its existing read-only repository analysis |

Examples:

```bash
doc-gen init --dry-run
doc-gen structure generate --dry-run .
doc-gen structure print --dry-run .
doc-gen structure analyze --dry-run .
```

## Configuration

Dry-run can be enabled in `.config/doc_gen/config.toml`:

```toml
[tool.doc-gen.cli.execution]
dry_run = true
```

Resolution order is:

1. command-line option (`--dry-run` or `--no-dry-run`)
2. `[tool.doc-gen.cli.execution].dry_run`
3. built-in default (`false`)

Use `--no-dry-run` only when you intentionally want a command-line override of
configured dry-run mode.

## Guaranteed boundary

During dry-run, Doc Gen may load configuration, scan the selected repository,
detect project type, build a tree, render Markdown in memory, and display
summaries. It does not:

- create or overwrite initialization files;
- create initialization directories;
- prompt for overwrite confirmation;
- create an output directory for generated documentation;
- write or replace the generated Markdown file;
- modify files during print or analyze.

Diagnostic logging may still write to the configured log destination. This is
operational telemetry, not a generated-project mutation.

## Automation through Make

Pass dry-run through the existing command argument variables:

```bash
make l-init DOC_GEN_INIT_ARGS="--dry-run"
make l-generate TARGET=. DOC_GEN_GENERATE_ARGS="--dry-run"
make d-generate TARGET=. DOC_GEN_GENERATE_ARGS="--dry-run"
make c-generate TARGET=. DOC_GEN_GENERATE_ARGS="--dry-run"
```

The application enforces the same boundary for local, Docker, and Compose runs.
