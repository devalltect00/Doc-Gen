<!-- docs/TODO_tracking_history.md -->

---

# docs/TODO.md

> Current status: see the [2026-09-02 checkpoint update](#checkpoint-3-2026-09-02).
> Older checkboxes, test counts, plans, and decisions are preserved as recorded;
> they are historical context, not proof that every current release gate passed.

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

## 🗑️ Cancelled / Dropped

- [ ] _nothing_

## 🧾 Notes

- TODO.md = short-term execution
- Keep tasks small and actionable

---

<a id="checkpoint-3-2026-09-02"></a>

## 2026-09-02 status update — untagged checkpoint 3

Version scope: **v1.0.0-rc.1**.
The [checkpoint commit message](../.config/custy/templates/commit-message-v1.0.0-development-checkpoint-3.txt)
has **no associated tag or tag message**. Earlier checkpoint files remain unchanged.

### ✅ Current application and developer workflow

- [x] Retain the v0.1.0 baseline: the simple `print_project_structure` project-tree generator.
- [x] Attribute the rename to Doc Gen to v1.0.0-rc.1, with stable v1.0.0 carrying that change forward.
- [x] Keep `init` and `structure generate/print/analyze`, with read-only print/analysis and dry-run preventing generated output.
- [x] Use the `app/doc_gen/` package and `.config/doc_gen/config.toml` with `[tool.doc-gen.cli.structure]` and command-specific sub-tables.
- [x] Keep Python 3.9+ runtime compatibility, Python 3.14 development/containers, and separate test dependencies so the 3.9 validation job does not install incompatible formatting tools.

Earlier references to `.projectstructure.toml`, `app/project_structure`, and
the old project name remain historical. They are not the current setup
instructions. The empty root `TODO.md` adds no tasks to this update.

### ✅ Delivery work carried forward

- [x] Align local, Docker/Compose, Make, pre-commit, and hosted CI validation with the active project rather than the old standalone layout.
- [x] Validate annotated release-tag metadata and package versions; publish exact prerelease/stable image tags and update `latest` only for stable releases.
- [x] Add private GitLab Python package build, artifact checks, clean-install verification, and protected-tag publication using `CI_JOB_TOKEN`.
- [x] Normalize supported release tags to PEP 440 package versions; reject unsupported or ambiguous versions rather than guessing.
- [x] Keep unprotected GitLab tag pipelines validation-only, skipping production-image, package-upload, and provider-release jobs.
- [x] Document installation of an available package version from the selected project registry, independently of cloning source or pulling a container.
- [x] Record the maintainer's report that hosted pipelines passed and the GitLab package registry was populated. This is historical reported validation, not a new pipeline run for this documentation checkpoint.

### ✅ Optional repository metadata helper

- [x] Add `scripts/repository/src/sync_metadata.py` outside the core application and installed CLI.
- [x] Read `[project].description` and independent GitHub/GitLab topics from `pyproject.toml`; do not reinterpret package keywords as repository topics.
- [x] Resolve one repository per provider from ordered remote candidates; the current defaults are GitHub `origin` and GitLab `backup`, using fetch URLs.
- [x] Provide a `--dry-run` path with read-only Git discovery and no provider API calls.
- [x] Document authenticated `gh`/`glab` for live updates, topic replacement and empty-list clearing, no confirmation prompt, and possible partial updates on failure.
- [x] Refresh the README against active commands, configuration, runtime requirements, installation methods, and the helper's actual `src/` path.
- [x] Keep helper details in checkpoint/release commit messages; leave user-facing tag-message templates unchanged for this maintainer-only addition.

### ⏳ Follow-up and release gates

- [ ] Correct the helper docstring examples that omit `src/` and reconcile its GitHub topic-limit constant (currently 50) with the provider maximum of 20.
- [ ] Add isolated mocked coverage for metadata validation, remote selection, dry-run API suppression, topic clearing, and provider failures before treating the helper as fully validated.
- [ ] Review actual targets, credentials, topic lists, and provider permissions before a separately authorized live metadata synchronization; no live synchronization was performed for this checkpoint.
- [ ] Re-run the relevant checks against the exact candidate commit before creating the v1.0.0-rc.1 tag. A passing temporary-tag pipeline is not a formal release.
- [ ] Complete the RC review and approved stable cleanup, then validate the final v1.0.0 commit before its release tag.
- [ ] Review and update pre-commit configuration in a future maintenance task. Existing pre-commit setup is complete; this pending item means a later refresh, not that hooks were never configured.

### Notes and evidence

- [README](../README.md) and [metadata helper](../scripts/repository/src/sync_metadata.py) describe the current setup.
- [GitLab package pipeline](../.gitlab/python-package.yml) defines the validation/publication boundary.
- Earlier test/coverage figures and release-checklist statuses remain attached to their original milestones.
- No existing history, ideas, alternatives, cancelled work, backup snapshots, or earlier checkpoint messages were removed.
