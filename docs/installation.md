<!-- docs/installation.md -->

# Installation

This guide describes the supported installation methods for DocGen.

## Requirements

- Python 3.14 or later
- pip
- Git (for repository-based installation)

Verify your installation:

```bash
python --version
pip --version
git --version
```

---

## Install from the Private GitLab PyPI Registry

Doc-Gen is not published to the public PyPI index. Use a GitLab deploy token
with `read_package_registry` access and replace the placeholders below:

```bash
python -m pip install \
  --index-url "https://<deploy-token-user>:<deploy-token>@gitlab.com/api/v4/projects/<project-id>/packages/pypi/simple" \
  "doc-gen==1.0.0"
```

Release-candidate tags are normalized to PEP 440. For example,
`v1.0.0-rc.1` is installed as:

```bash
python -m pip install \
  --index-url "https://<deploy-token-user>:<deploy-token>@gitlab.com/api/v4/projects/<project-id>/packages/pypi/simple" \
  "doc-gen==1.0.0rc1"
```

Keep credentials out of committed files and shell history. Disable GitLab
package forwarding for strictly private resolution, and avoid
`--extra-index-url` for private packages.

---

## Install from GitHub

Install the latest version directly from GitHub:

```bash
pip install git+https://github.com/devalltect00/doc-gen.git
```

Install a specific tag:

```bash
pip install git+https://github.com/devalltect00/doc-gen.git@v1.0.0
```

Install from a specific branch:

```bash
pip install git+https://github.com/devalltect00/doc-gen.git@main
```

---

## Install from Release Artifacts

Download release artifacts from GitHub Releases.

Supported formats:

```text
.whl
.tar.gz
```

### Install from Wheel

```bash
pip install doc-gen-x.y.z-py3-none-any.whl
```

### Install from Source Distribution

```bash
pip install doc-gen-x.y.z.tar.gz
```

---

## Install Using Docker

Build the Docker image:

```bash
docker build -t doc-gen .
```

Run the container:

```bash
docker run --rm doc-gen structure generate
```

---

## Install Using Docker Compose

Start the application:

```bash
docker compose up
```

Run in detached mode:

```bash
docker compose up -d
```

Stop containers:

```bash
docker compose down
```

---

## Development Installation

Clone the repository:

```bash
git clone https://github.com/devalltect00/doc-gen.git
```

Enter the project directory:

```bash
cd doc-gen
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install development dependencies:

```bash
pip install -e .[dev]
```

Install documentation dependencies:

```bash
pip install -e .[docs]
```

Install all optional dependencies:

```bash
pip install -e .[dev,docs]
```

---

## Verify Installation

Verify the CLI is available:

```bash
doc-gen --help
```

Expected output:

```text
DocGen CLI
...
```

---

## Troubleshooting

### Command not found

Ensure the virtual environment is activated.

### Git not found

Install Git and ensure it is available on your PATH.

### Permission errors

Consider using a virtual environment rather than a system-wide installation.
