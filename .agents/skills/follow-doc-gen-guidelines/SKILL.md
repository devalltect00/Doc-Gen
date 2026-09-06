---
name: follow-doc-gen-guidelines
description: Apply Doc Gen-specific authorization, source layout, generated-output safety, environment, testing, and documentation rules.
---

# Follow Doc Gen Guidelines

## Purpose

Work safely and consistently in the Doc Gen repository. Apply this skill with
the user's latest instruction and the repository's governing files.

## Authorization and governing files

1. Treat the user's latest explicit instruction as the authority for the current
   task and write scope.
2. Read the repository-root `AGENTS.md` before source analysis or implementation.
3. Read `ENGINEERING_EXECUTION_POLICY.md` when architecture, implementation, CLI
   integration, or release readiness is relevant.
4. Use `pyproject.toml`, `Makefile`, configuration templates, and active source as
   executable truth.
5. Preserve unrelated work and obvious backup or temporary files.

Do not perform commits, tags, pushes, releases, package publication, registry
publication, or destructive cleanup without explicit approval.

## Project layout

- `app/doc_gen/cli/**`: commands, options, resolution, and presentation.
- `app/doc_gen/core/structure/**`: scanning, analysis, rendering, and writing.
- `app/doc_gen/config/**`: configuration loading and precedence.
- `app/doc_gen/core/initialize/**`: generated configuration scaffolding.
- `app/doc_gen/ui/**` and `app/doc_gen/theme/**`: terminal presentation.
- `tests/**`: behavior and regression tests.
- `docs/**`: user, architecture, testing, and developer documentation.

Keep filesystem discovery and generation logic out of the CLI layer. Keep
renderers focused on content and writers responsible for persistence.

## Generated-output safety contract

`doc-gen structure print` and `analyze` are read-only. `structure generate` may
write the configured output document, so resolve and display the target and
output path before live validation. Prefer temporary or dedicated test projects
when exercising generation. Never overwrite unrelated project documentation as
an incidental test step.

## Configuration and templates

The active user configuration is `.config/doc_gen/config.toml`; the packaged
default is `app/doc_gen/templates/config.toml`. When changing a field, update the
template, loader/resolver, tests, and relevant documentation together. Do not
unexpectedly overwrite generated user configuration.

## Environment and validation

Use the existing `venv/` when available. The package supports the Python range
declared in `pyproject.toml`; project containers and standard Make setup use
Python 3.14.

Run focused tests first, then broader checks. Use a repository-local
`--basetemp` on Windows when the system temporary directory has ACL problems.
Validate Make syntax, Compose configuration, and CLI `--help` for developer
workflow changes. Do not publish images during validation.

## Implementation and documentation

- Use type hints, useful docstrings, logging, and `pathlib` where practical.
- Keep functions focused and avoid duplicated or hardcoded path logic.
- Do not use debugging `print()` calls.
- Add proportionate tests for changed behavior.
- Update user and developer documentation for CLI, configuration, Make, Docker,
  initialization, generation, or output changes.
- Do not bump versions or edit changelog/release metadata unless requested.

## Completion report

Report what changed, files affected, validation results, documentation changes,
known limitations, anything skipped, and whether files were removed.
