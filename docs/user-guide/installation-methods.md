<!-- docs/user-guide/installation-methods.md -->

# Installation Methods

This guide describes different ways to install DocGen.

## Method 1: Private GitLab PyPI registry

Doc-Gen is not published to the public PyPI index. Authorized users can install
the immutable release package from its private GitLab project registry with a
deploy token that has `read_package_registry` permission:

```bash
python -m pip install \
  --index-url "https://<deploy-token-user>:<deploy-token>@gitlab.com/api/v4/projects/<project-id>/packages/pypi/simple" \
  "doc-gen==1.0.2"
```

A release-candidate tag such as `v1.0.0-rc.1` is stored as the canonical
PEP 440 version `1.0.0rc1`:

```bash
python -m pip install \
  --index-url "https://<deploy-token-user>:<deploy-token>@gitlab.com/api/v4/projects/<project-id>/packages/pypi/simple" \
  "doc-gen==1.0.0rc1"
```

Do not commit tokens. Disable GitLab package forwarding when resolution must
remain strictly private, and avoid `--extra-index-url` for private package
names.

Verify installation:

```bash
doc-gen --help
```

## Method 2: GitHub

Install directly from the GitHub repository:

```bash
pip install git+https://github.com/devalltect00/doc-gen.git
```

Install a specific version:

```bash
pip install git+https://github.com/devalltect00/doc-gen.git@v1.0.2
```

## Method 3: Docker

Pull the Docker image:

```bash
docker pull doc-gen
```

Run DocGen in a container:

```bash
docker run --rm doc-gen structure generate
```

Mount your project:

```bash
docker run --rm -v $(pwd):/workspace doc-gen structure generate
```

## Method 4: Development Install

Clone and install in development mode:

```bash
git clone https://github.com/devalltect00/doc-gen.git
cd doc-gen
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -e .[dev]
```

## Choosing a Method

| Method              | Best For                    |
| ------------------- | --------------------------- |
| Private GitLab PyPI | Authorized deployments      |
| GitHub              | Latest development version  |
| Docker              | Isolated environment        |
| Development         | Contributing to the project |

## Verification

After installation, verify by running:

```bash
doc-gen structure generate
```

This should create a PROJECT_STRUCTURE.md file.

---

## Related Documentation

- [Quick Start](quickstart.md) - Quick start guide
- [Installation](../installation.md) - Full installation guide
