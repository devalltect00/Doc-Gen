# AGENTS.md

## Project overview

Doc Gen is a configuration-driven Python CLI that scans repository contents,
prints and analyzes project trees, and generates structured Markdown project
documentation such as `PROJECT_STRUCTURE.md`.

The application is intended for interactive use and repeatable documentation
automation. Preserve deterministic scanning, explicit output paths, safe ignore
rules, readable terminal output, and configuration compatibility.

## Supported user-facing commands

```text
doc-gen init
doc-gen structure generate [target]
doc-gen structure print [target]
doc-gen structure analyze [target]
```

Structure commands support shared profile, smart-mode, depth, file visibility,
directory-collapse, project-type, and verbosity options. Generation additionally
supports an explicit output file. `print` and `analyze` are read-only;
`generate` may write the selected Markdown output.

## Technology and packaging

- Package compatibility: Python 3.9+
- Standard development and container runtime: Python 3.14
- Typer and Rich
- setuptools and setuptools-scm
- Ruff and Black
- Pytest and pytest-cov
- MkDocs Material
- Docker, Docker Compose, and modular Make helpers

The console entry point is defined in `pyproject.toml`. Package resources under
`app/doc_gen/templates/` must remain included in distributions.

## Project structure

```text
app/doc_gen/
├── cli/             CLI commands, arguments, resolution, and presentation
├── config/          Configuration and file loading
├── core/initialize/ Generated configuration scaffolding
├── core/structure/  Discovery, analysis, profiles, rendering, and writing
├── services/        Application-level service composition
├── templates/       Configuration copied by init
├── theme/           Rich theme definitions
├── ui/              Shared terminal presentation
└── utils/           Ignore, parsing, logging, progress, and console helpers

tests/               Unit, CLI, configuration, core, and service tests
docs/                User, architecture, testing, and developer documentation
make/                Modular local, Docker, Compose, and remote Make commands
```

The CLI entry point is `app/doc_gen/cli/main.py`. Keep CLI interaction in
`app/doc_gen/cli/`, reusable structure behavior in `app/doc_gen/core/structure/`,
rendering in renderers, and persistence in writers.

## Generated-output safety contract

- `structure print` and `structure analyze` must remain read-only.
- `structure generate` may write only its resolved output document.
- Resolve the target directory and output path before generation.
- Apply configured and built-in ignore rules consistently.
- Never overwrite unrelated documentation during tests or discovery.
- Use a temporary or dedicated test project for live generation validation.

Do not operate on another repository merely because Doc Gen was invoked from its
source checkout. Make the selected target visible in previews and summaries.

## Dry-run contract

- `init --dry-run` must not create directories or files, overwrite content, or
  prompt for confirmation.
- `structure generate --dry-run` may scan and render in memory but must not
  create its output directory or write the selected Markdown file.
- `structure print` and `structure analyze` are inherently read-only and must
  remain non-mutating when `--dry-run` is supplied.
- Read-only configuration, discovery, validation, and rendering may execute.
- Diagnostic logging may write to its configured destination, but target
  project files must remain unchanged.
- Every mutating command needs regression tests proving its dry-run boundary.

## Configuration and templates

Doc Gen uses `.config/doc_gen/config.toml`. The packaged source template is
`app/doc_gen/templates/config.toml`; generated target configuration is user-owned
after initialization.

When adding or changing a configuration field:

1. Update the packaged template and loader/resolver logic.
2. Preserve compatible defaults where practical.
3. Add tests for CLI/config/default precedence and validation.
4. Update command, configuration, QA, and architecture documentation as needed.

Never silently overwrite user-managed configuration.

## Coding and logging standards

- Follow PEP 8 and existing project conventions.
- Use type hints and useful docstrings.
- Prefer `pathlib` over `os.path`.
- Keep functions focused and responsibilities separated.
- Prefer composition and straightforward code over unnecessary abstraction.
- Do not change public CLI behavior without discussing compatibility.
- Preserve unrelated work and backup files in a dirty worktree.
- Do not use debugging `print()` calls or hardcoded project paths.

Use logging when it improves troubleshooting:

- `CRITICAL`: execution cannot continue safely.
- `ERROR`: generation or analysis failed.
- `WARNING`: a recoverable issue or fallback occurred.
- `INFO`: an important scan or generation state changed.
- `DEBUG`: resolved paths, profiles, detection, or detailed flow.

Never log credentials or sensitive repository content unnecessarily.

## Testing and validation

Use the existing virtual environment when available:

```powershell
.\venv\Scripts\python.exe -m pytest
```

Run focused tests first and then the broader suite. On Windows, use a
repository-local `--basetemp` when the system temporary directory has ACL
problems. Generation changes require tests proving only the selected output is
written; print and analyze tests must remain read-only.

Developer-workflow changes should validate:

- TOML parsing and metadata tests
- `make help` and representative Make dry-runs
- Docker Compose development and production configuration
- production and development CLI `--help` startup

Do not publish packages or images during ordinary validation.

## Documentation

Keep files under `docs/` synchronized with commands, profiles, configuration,
initialization, generation, output paths, Make targets, Docker workflows,
testing, and troubleshooting.

Significant architecture changes require an explanation of responsibilities,
dependencies, data flow, and trade-offs. Update Mermaid diagrams when they
materially improve understanding.

## Development workflow

1. Analyze the active implementation and configuration.
2. Describe affected files, compatibility, risks, and validation.
3. Implement focused changes.
4. Add or update tests and documentation.
5. Run focused and broader validation.

Before executing generation against user documentation, cleanup, publication,
or release operations, explain the target and obtain explicit approval.

## Git and release safeguards

Do not perform commits, tags, pushes, rebases, history rewrites, releases,
package publication, or registry publication unless explicitly requested and
approved. Do not edit `CHANGELOG.md` or bump the project version automatically.

## Completion report

Report:

1. What changed and why
2. Files added, modified, or removed
3. Tests and commands run, including results
4. Documentation changes or remaining work
5. Known limitations and the next recommended step
