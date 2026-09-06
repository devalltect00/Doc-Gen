<!-- docs/TODO_tracking_history_v1.0.0.md -->

---

# Doc Gen TODO Tracking History — v1.0.0

> Cumulative snapshot for **v1.0.0**. Earlier tasks, unfinished work,
> considerations, ideas, cancelled items, and notes are intentionally retained.

---

# 📌 TODO

Tracks short-term development tasks, improvements, tasks and ideas .

---

## 🚧 Now, In Progress

Tasks currently being worked on or requiring immediate attention.

(Use Beta version first )

- [x] add print the structure to cli option by default
- [x] add readme.md
- [x] add license
- [x] add pyproject.toml
- [x] add name of the module/project/repo
- [x] add regenerate requirement.txt
- [x] add handle venv files detector
- [x] add default conf file.
- [x] fixes venv file fetch errors. use start with 'venv'
- [x] Create and update docs

=======

- [x] Change and rename project name from project_structure to doc_gen
- [x] add .github workflow file
  - [x] add ci.yml file
  - [x] add docker-dev.yml file
  - [x] add docker-prod.yml file
  - [x] add release.yml file
- [x] add gitlab-ci.yml
- [x] add ignore files
  - [x] add .gitignore
  - [x] add .dockerignore
  - [x] add .prettierignore
- [x] use logs for external logs
- [x] add .vscode/
  - [x] add .vscode/launch.json // wait if any updates to the app commands if changed
  - [x] add .vscode/settings.json
- [x] add config or meta data
  - [x] add .pre-commit-config.yaml
  - [x] add .prettierrc.json
  - [x] add AGENTS.md
  - [x] add CONTRIBUTING.md
  - [x] add LICENSE
  - [x] add pyproject.toml // remain change command on `doc-gen = "project_structure.cli:main"` part or section
  - [~] add requirements.txt
  - [x] add SECURITY.md
  - [x] add TODO.md
  - [x] add README.md
  - [ ] Add CHANGELOG.md.
- [x] add docker compose files
  - [x] add docker-compose.dev.yml files
  - [x] add docker-compose.prod.yml files
  - [x] add docker-compose.yml files
  - [x] add Dockerfile
- [x] add example_command.txt
- [x] add Makefile
- [x] add Testing
- [x] add mkdocs.yml
- [~] add documentations
  - [x] Add the docs/badges.md
  - [x] Add the docs/configuration.md
  - [x] Add the docs/how-to-use.md
  - [x] Add the docs/index.md
  - [x] Add the docs/infrastructure.md
  - [x] Add the docs/installation.md
  - [x] Add the docs/usage.md
  - [ ] Add the docs/project_structure.md
  - [x] Add the diagrams to docs/diagrams/
- [x] change using doc_gen repo
- [x] change command and file app or project app to DOC GEN
- [x] Using .config/ path instead from tools/ path
- [x] add banner
- [x] path-header-scanner patch
- [x] doc-gen generates docs
- [x] Fix init
- [ ] General project cleanup and consistency pass.
- [x] Update pyproject.toml description
- [x] Update CONTRIBUTING.md description
- [x] Update Makefile
- [x] error exception on CLI when command is missing

---

## 🧠 Planning

### 🚀 v1.0.0 release preparation

- [x] Compare the v0.1.0 four-file standalone utility with the current packaged `app/doc_gen` implementation.
- [x] Establish `v1.0.0-rc.1` as the release candidate for the redesigned CLI and `v1.0.0` as the stable promotion target.
- [x] Prepare separate internal commit messages and public tag/release messages for `v1.0.0-rc.1` and `v1.0.0`.
- [x] Align project metadata, Docker files, Docker Compose files, ignore rules, modular Make workflows, `AGENTS.md`, and documentation with the active application.
- [x] Add explicit dry-run behavior to initialization and every structure command.
- [x] Separate Markdown rendering from persistence so generation dry-run cannot invoke the writer or create output directories.
- [x] Correct local, Docker, Compose, and remote Make option ordering for Typer commands with optional target paths.
- [x] Validate the current baseline with 68 passing tests, 73% coverage, Black, Ruff, and a Docker-based MkDocs build on Python 3.14.
- [ ] Validate `v1.0.0-rc.1` against disposable repositories of different sizes and project types.
- [ ] Complete final cleanup and incorporate release-blocking corrections or documentation clarifications discovered during RC validation.
- [ ] Run final approved test, documentation, packaging, Make, Docker, Compose, and dry-run release checks.
- [ ] Commit, tag, publish, and verify `v1.0.0` only after explicit release approval.

### 🧰 Future maintenance

- [ ] Review and update `.pre-commit-config.yaml` so hook versions, Python targets, and validation commands align with the current project. This is planning only; do not update the configuration as part of the v1.0.0 message-preparation work.

### ⏭️ Next

Tasks expected to be addressed soon after current work is finished.

(v1.0.1)

- [ ] Use `custy` custom tools
- [ ] generate changelog
- [ ] Make Github release or Github package
- [ ] installable

---

### 💤 Later

Tasks that are planned but not prioritized yet.

- [x] Improve CLI error handling
- [ ] add diagram
- [ ] Make Github release or Github package
- [ ] installable

---

## ✨ Improvements

Enhancements to existing features or developer experience.

- _nothing_

Examples:

- performance improvements
- better logging
- usability improvements

---

## 🧹 Technical Debt

- Simplify scanner logic
- Standardize error handling

---

## ⚖️ considerations

- Use mkdocs or docusaurus for the docs

---

## 💡 Ideas

Possible future features or experiments that are not yet planned.

- Interactive CLI (wizard mode)
- VSCode extension
- CI integration (auto-generate structure)
- Web visualization UI

---

## ✅ Completed

### `v1.0.0` release scope (stable promotion pending)

#### Summary

- CLI tool implemented
- Modular architecture introduced
- Full documentation system added
- Developer tooling added (Makefile, Docker, CI)
- Config system + smart mode implemented

The implementation scope is complete and is being prepared for RC validation;
the stable Git release remains pending.

#### Core Features

- [x] CLI tool (`generate`, `print`, `analyze`, `init`)
- [x] PROJECT_STRUCTURE.md generator
- [x] Smart mode
- [x] Config file support (`.projectstructure.toml`)
- [x] Profiles (minimal, default, detailed)

---

#### Architecture

- [x] Modular structure (config, scanner, generator, utils)
- [x] Clean package layout (`app/project_structure`)
- [x] Test suite

---

#### Developer Experience

- [x] Makefile
- [x] Docker support
- [x] Pre-commit hooks
- [x] CI pipeline

---

#### Documentation

- [x] README (clean landing page)
- [x] Getting started docs
- [x] User guide
- [x] CLI reference
- [x] Architecture docs

---

#### Improvements & Fixes

- [x] Default CLI print behavior
- [x] Venv detection & handling
- [x] Default config support
- [x] Requirements regeneration
- [x] Project/module naming cleanup

### `v0.1.0`

#### Summary

- Initial PROJECT_STRUCTURE.md generator

#### Core Features

- [x] Simple `PROJECT_STRUCTURE.md` file generator

---

## Since v0.1.0 — `print_project_structure`

- [x] Create a simple `print_project_structure` utility that detects a basic project type and generates a readable directory tree.
- [x] Print the generated project structure in the terminal and optionally save it as a Markdown document.
- [x] Support built-in exclusions and additional ignore patterns from `.projectignore`.
- [x] Publish the original utility under the `print_project_structure` project name throughout the v0.1.0 release.

---

## Since v1.0.0-rc.1

### Version context

| Field | Value |
| --- | --- |
| Version | `v1.0.0-rc.1` |
| Previous version | `v0.1.0` |
| Release type | Major redesign release candidate |
| Version strategy | Semantic Versioning |
| Package compatibility | Python 3.9+ |
| Standard development/runtime | Python 3.14 |

### Project rename and identity

- [x] Rename the project from `print_project_structure` to **Doc Gen** as part of the v1.0.0-rc.1 redesign.
- [x] Introduce `doc-gen` as the installed CLI command for the new v1.0 release line.
- [x] Replace the original single-file identity with the packaged `app/doc_gen` application structure.

### Completed release-candidate scope

#### Structure workflows

- [x] Replace the standalone script with the `doc-gen` console application.
- [x] Add `doc-gen structure generate [target]` for Markdown documentation generation.
- [x] Add read-only `doc-gen structure print [target]` and `doc-gen structure analyze [target]` workflows.
- [x] Add `doc-gen init` for namespaced project configuration.
- [x] Add configurable targets, output paths, depth, file visibility, directory collapse, project type, verbosity, profiles, smart mode, and ignores.
- [x] Add minimal, default, and detailed profiles.
- [x] Detect project characteristics for smart-mode behavior.

#### Scanning, rendering, and persistence

- [x] Add deterministic repository discovery models and services.
- [x] Render overview, project tree, root-file, directory-detail, and notes sections.
- [x] Separate Markdown rendering from file persistence through a dedicated writer.
- [x] Collect repository metadata, statistics, and project-type details.
- [x] Apply built-in and configurable ignore rules for repositories, environments, caches, dependencies, and build outputs.
- [x] Keep `PROJECT_STRUCTURE.md` as the conventional default while supporting an explicit output path.

#### CLI, configuration, and safety

- [x] Add a Typer command hierarchy with Rich banners, help, panels, tables, progress, and summaries.
- [x] Add centralized command error boundaries, domain exceptions, concise remediation, and reliable nonzero exits.
- [x] Keep normal-mode output free of raw tracebacks while preserving full debug diagnostics.
- [x] Add `.config/doc_gen/config.toml` with CLI → configuration → default resolution.
- [x] Add initialization builders, models, registries, presenters, and scaffold services.
- [x] Add configurable console and rotating-file logging.

#### Dry-run guarantees

- [x] Add `--dry-run` to initialization and every structure command.
- [x] Prevent dry-run initialization from creating or overwriting files and from prompting.
- [x] Allow generation dry-run to scan and render in memory without creating output directories or files.
- [x] Keep print and analyze read-only when dry-run is supplied.
- [x] Add configuration support and CLI override behavior for dry-run.
- [x] Present generated previews distinctly from persisted results.

#### Architecture and developer workflow

- [x] Separate CLI, configuration, scanner, detector, analyzer, smart mode, profiles, renderers, writer, initialization, UI, and logging responsibilities.
- [x] Replace hardcoded `os`-based traversal and writes with focused services and `pathlib`-oriented models.
- [x] Add shared results, domain exceptions, themes, and utilities.
- [x] Add `AGENTS.md` and engineering guidance for output safety, dry-run, tests, documentation, and releases.
- [x] Add modular Make, Docker, Compose, remote-image, CI/CD, packaging, Ruff, Black, Pytest, MkDocs, and pre-commit workflows.
- [x] Correct Make option ordering for Typer commands with optional target paths.

#### Tests and documentation

- [x] Add CLI, configuration, initialization, scanner, generator, renderer, presenter, service, and utility tests.
- [x] Add coverage for generate, print, analyze, profiles, smart mode, detection, ignores, output rendering, and option resolution.
- [x] Prove dry-run initialization creates no scaffold and dry-run generation never invokes the writer.
- [x] Add pre-commit configuration validation and local/Docker/Compose/Make help checks.
- [x] Record the release baseline as 72 passing tests with 74% measured coverage on Python 3.14.
- [x] Document installation, configuration, commands, profiles, output, safety, architecture, testing, Docker, Compose, Make, and migration.
- [x] Prepare separate internal commit and public release messages for RC.1 and stable 1.0.0.

### Breaking-change checklist

- [x] Document replacement of direct `print_project_structure.py` execution with the `doc-gen` command.
- [x] Document the explicit `structure generate`, `print`, and `analyze` workflows.
- [x] Document migration to `.config/doc_gen/config.toml`.
- [x] Document CLI/configuration-based targets and output paths in place of hardcoded behavior.
- [x] Document the new package layout and scanner/renderer/writer extension boundaries.

### RC validation checklist

- [ ] Install RC.1 in an isolated environment and inspect all command help.
- [ ] Preview initialization and review the proposed configuration.
- [ ] Generate previews for disposable repositories of different sizes and project types.
- [ ] Exercise minimal, default, detailed, and smart-mode behavior.
- [ ] Verify dry-run generation creates neither an output directory nor a Markdown file.
- [ ] Verify print and analyze remain read-only.
- [ ] Review generated output structure, ignores, paths, summaries, and errors.
- [ ] Validate local, Docker, Compose, remote-image, Make, package, and documentation workflows.
- [ ] Commit, tag, publish, and verify `v1.0.0-rc.1` only with explicit release approval.

### Deferred beyond RC.1

- [ ] Complete stable-release cleanup and incorporate release-blocking corrections.
- [ ] Add further project detectors only when their behavior can be deterministic and tested.
- [ ] Consider interactive or visual workflows only after the core CLI contract is stable.
- [ ] Review future pre-commit upgrades intentionally rather than as an unrelated release change.

### Notes

- The former v0.1.0 implementation was a small standalone utility; 1.0 defines
  a new supported CLI and architecture baseline.
- This file does not claim that external release or publication operations have
  been completed.

---

## Since v1.0.0

### Version context

| Field | Value |
| --- | --- |
| Version | `v1.0.0` |
| Previous version | `v1.0.0-rc.1` |
| Previous stable version | `v0.1.0` |
| Release type | Stable major release |
| Version strategy | Semantic Versioning |
| Promotion rule | Carry forward the validated RC.1 command and output-safety model |

### Stable feature baseline

#### CI/CD and compatibility baseline promoted from RC.1

- [x] Carry forward the Python 3.9 and 3.14 CI matrix and Python 3.9-compatible runtime implementation.
- [x] Carry forward dynamic registry naming, annotated-tag validation, exact prerelease images, and stable-only `latest`.
- [x] Carry forward full tag-message release notes, package artifacts, and root multi-stage Docker builds.
- [ ] Re-run hosted-workflow-equivalent checks after final cleanup and before creating `v1.0.0`.

- [x] Carry forward explicit generate, print, analyze, and initialization workflows.
- [x] Carry forward configurable targets, output paths, profiles, smart mode, depth, visibility, collapse, project type, and ignores.
- [x] Carry forward structured overview, tree, root-file, directory-detail, and notes rendering.
- [x] Carry forward the scanner/renderer/writer separation and writer-level mutation boundary.
- [x] Carry forward read-only print and analyze behavior.
- [x] Carry forward dry-run initialization and generation guarantees.
- [x] Carry forward namespaced `.config/doc_gen/config.toml` configuration.
- [x] Carry forward Rich UI, logging, concise command errors, debug diagnostics, tests, docs, Make, Docker, Compose, packaging, and CI/CD.

### Stable-release finalization

- [ ] Incorporate only release-blocking fixes, migration clarifications, and documentation corrections found during RC validation.
- [ ] Remove temporary development artifacts that are not part of the supported product.
- [ ] Review package metadata, generated configuration, command help, public docs, CI/CD, and container destinations.
- [ ] Confirm generation writes only the resolved output document.
- [ ] Confirm dry-run cannot reach directory creation or the Markdown writer.
- [ ] Preserve completed 1.0 development history and future plans in project tracking documentation.

### Stable validation checklist

- [ ] Run the approved complete test and coverage suite.
- [ ] Run Ruff, Black, pre-commit, packaging, and documentation validation.
- [ ] Validate initialization and every structure command locally and in production containers.
- [ ] Validate minimal, default, detailed, and smart output on disposable repositories.
- [ ] Validate ignore behavior, target resolution, explicit outputs, and command failures.
- [ ] Validate Make, Docker Compose, and remote-image help and dry-run workflows.
- [ ] Commit and create the `v1.0.0` tag only with explicit release approval.
- [ ] Verify distributions, releases, container images, and documentation after publication.

### Stable support boundaries

- [x] `structure print` and `structure analyze` are read-only.
- [x] `structure generate` may write only its selected output file.
- [x] Dry-run may scan and render but may not create the output directory or document.
- [x] Diagnostic logs may be written without changing target-project documentation.
- [x] Generated configuration becomes project-owned after initialization.
- [x] Python 3.9+ remains the package compatibility floor; Python 3.14 is the standard development and container runtime.

### Future work

- [ ] Add new project analysis or detector behavior through focused, tested boundaries.
- [ ] Evaluate interactive workflows, CI generation, or visual structure output as separate future features.
- [ ] Continue improving large-repository performance and progress only with measured evidence.
- [ ] Review and intentionally refresh pre-commit hook versions and Python targets.

### Notes

- Stable 1.0 is intended to promote the reviewed RC.1 foundation rather than
  introduce unvalidated output or mutation behavior.
- Unchecked release operations remain pending explicit authorization.

---

## Additional TODO source review

The repository-root `TODO.md` is currently empty, so it contributes no extra
completed, pending, cancelled, consideration, or idea items to this snapshot.
The historical and version-specific content above remains the authoritative
record until a new root TODO entry is added.

---

## 🗑️ Cancelled / Dropped

- [ ] _nothing_

## 🧾 Notes

- TODO.md = short-term execution
- Keep tasks small and actionable
