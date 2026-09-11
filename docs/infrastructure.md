<!-- docs/infrastructure.md -->

# Infrastructure

This document describes the repositories, services, and deployment architecture used by DocGen.

## Overview

```text
Developer
    │
    ▼
GitHub (Primary Repository)
    │
    ├── Source Code
    ├── Issues
    ├── Releases
    ├── Tags
    └── Documentation Source
    │
    ├──────────────► GitHub Releases
    │                 ├── .whl
    │                 └── .tar.gz
    │
    ▼
GitLab Private PyPI Registry
    │
    └── Authenticated Package Distribution
    │
    ▼
Docker Hub / GHCR
    │
    └── Container Images

Docker
    │
    └── Container Runtime

Docker Compose
    │
    └── Local Development
```

---

## Platforms

| Purpose                 | Platform       |
| ----------------------- | -------------- |
| Source Code             | GitHub         |
| Releases                | GitHub         |
| Tags                    | GitHub         |
| Issues                  | GitHub         |
| Discussions             | GitHub         |
| Package Distribution    | GitLab PyPI    |
| Container Registry      | Docker Hub     |
| Container Images        | Docker         |
| Container Orchestration | Docker Compose |

---

## Repository URLs

### GitHub (Primary)

https://github.com/devalltect00/doc-gen

Responsibilities:

- Source of truth
- Pull requests
- Issues
- Releases
- Tags

### GitLab Private PyPI Registry

```text
https://gitlab.com/api/v4/projects/<project-id>/packages/pypi/simple
```

Responsibilities:

- Private wheel and source-distribution storage
- Authenticated package installation
- Immutable package versions produced from protected release tags

---

## Documentation

Documentation is generated using:

- MkDocs
- Material for MkDocs

Published at (if configured):

https://devalltect00.github.io/doc-gen/

---

## Installation & Distribution

DocGen can be installed using several methods.

### Private GitLab PyPI Registry

Install with a deploy token that has `read_package_registry` access:

```bash
python -m pip install \
  --index-url "https://<deploy-token-user>:<deploy-token>@gitlab.com/api/v4/projects/<project-id>/packages/pypi/simple" \
  "doc-gen==1.0.2"
```

The public PyPI index is not a supported Doc-Gen distribution channel.

### GitHub Repository

Install directly from GitHub:

```bash
pip install git+https://github.com/devalltect00/doc-gen.git
```

Specific tag:

```bash
pip install git+https://github.com/devalltect00/doc-gen.git@v1.0.2
```

---

### Release Artifacts

Release artifacts are generated using:

- build
- twine

Artifacts:

```text
dist/
├── *.whl
└── *.tar.gz
```

Install wheel:

```bash
pip install doc_gen-1.0.2-py3-none-any.whl
```

Install source distribution:

```bash
pip install doc_gen-1.0.2.tar.gz
```

---

### Docker

Build locally:

```bash
docker build -t doc-gen .
```

Run container:

```bash
docker run doc-gen structure generate
```

---

### Docker Compose

Run using Docker Compose:

```bash
docker compose up
```

or

```bash
docker compose up -d
```

---

## CI/CD Flow

```text
Push to GitHub
        │
        ▼
GitHub Actions (if configured)
        │
        ├── Test on Python 3.9 and 3.14
        ├── Check Black formatting on Python 3.14
        └── Run Ruff linting on Python 3.14
```

The compatibility test jobs install `.[test]`. The Python 3.14 quality job
installs `.[dev]`. Image and release publication are handled by separate,
guarded workflows described in the CI/CD contract.

---

## Additional Resources

- Makefile commands for local development
- Docker Compose for containerized workflows
- [CI/CD and release contract](ci-cd.md)
