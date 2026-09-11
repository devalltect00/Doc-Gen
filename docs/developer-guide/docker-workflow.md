<!-- docs/developer-guide/docker-workflow.md -->

# Docker Workflow

This guide describes how to use Docker and Docker Compose for development with DocGen.

---

## Why Use Docker?

Docker provides:

- Consistent development environment
- Isolation from local system
- Easy to reproduce issues
- Same environment as CI/CD

---

## Docker Images

The project builds multiple Docker images:

Make resolves the reviewed version from `app/doc_gen/__version__.py` before a
local development or production build and supplies it to setuptools-scm as a
Docker build argument. This is required because `.git` is intentionally absent
from the Docker build context. You can override the value for a reviewed build,
for example `make c-build-prod DOC_GEN_BUILD_VERSION=1.0.2`.

| Image                 | Description       |
| --------------------- | ----------------- |
| `doc-gen:latest`      | Base image        |
| `doc-gen-dev:latest`  | Development image |
| `doc-gen-prod:latest` | Production image  |

---

## Building Images

### Build Base Image

```bash
make d-build-base
```

### Build Development Image

```bash
make d-build-dev
```

### Build Production Image

```bash
make d-build-prod
```

### Build All Images

```bash
make d-build-all
```

---

## Running Containers

### Run Tests in Docker

```bash
make d-test
```

### Run Structure Generate in Docker

```bash
make d-generate
make d-generate-smart
```

### Run Structure Print in Docker

```bash
make d-print
make d-print-smart
```

### Run Analysis in Docker

```bash
make d-analyze
```

---

## Docker Compose

### Start Development Environment

```bash
make c-up
```

### Start in Background

```bash
make c-up-detached
```

### Stop Environment

```bash
make c-down
```

### View Logs

```bash
make c-logs
```

---

## Common Compose Commands

### Run Commands via Compose

```bash
# Initialize
make c-init

# Generate
make c-generate

# Print
make c-print

# Analyze
make c-analyze
```

### Quality Assurance

```bash
# Run formatting
make c-format

# Run linter
make c-lint

# Run tests
make c-test

# Run full check
make c-check
```

### Full CI Workflow

```bash
make c-ci
```

---

## Using Makefile

The Makefile provides convenient shortcuts:

```bash
# See all available commands
make help
```

See [`make-workflow.md`](make-workflow.md) for grouped local, Docker, Compose,
and published utility image commands.

---

## Troubleshooting

### Published release tags

Stable production releases publish four coordinated references to the same
image: exact `v1.0.2`, minor `v1.0`, major `v1`, and `latest`. Pin CI and
reproducible automation to the immutable exact tag. The other aliases move only
when a compatible stable release is published. Prereleases such as
`v1.0.0-rc.1` publish only their exact tag.

GitHub and GitLab enforce the same alias and prerelease policy. See the
[CI/CD and release contract](../ci-cd.md) for publication safeguards.

---

### Docker not installed

Install Docker Desktop from https://www.docker.com/products/docker-desktop

### Container not running

Check Docker is running:

```bash
docker info
```

### Build fails

Try rebuilding:

```bash
docker compose build --no-cache
```

---

## Related Documentation

- [Developer Guide](developer-guide.md)
- [Getting Started](getting-started.md)
- [Testing Guide](../testing/testing-guide.md)
- [CI/CD and release contract](../ci-cd.md)
