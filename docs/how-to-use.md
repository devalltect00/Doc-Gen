<!-- docs/how-to-use.md -->

# How to Use DocGen

This guide provides a quick overview of how to use DocGen for generating project documentation.

## Quick Start

Install Doc-Gen from the private GitLab PyPI registry and generate your first
project structure. Replace the placeholders with a deploy token that has
`read_package_registry` access:

```bash
python -m pip install \
  --index-url "https://<deploy-token-user>:<deploy-token>@gitlab.com/api/v4/projects/<project-id>/packages/pypi/simple" \
  "doc-gen==1.0.2"
doc-gen structure generate
```

This creates a `PROJECT_STRUCTURE.md` file in your current directory.

## Basic Usage

### Generate Project Structure

Create a markdown document showing your project layout:

```bash
doc-gen structure generate
```

Preview generation without creating or replacing the output file:

```bash
doc-gen structure generate --dry-run
```

### Print to Console

Display project structure in the terminal:

```bash
doc-gen structure print
```

### Analyze Project

Get detailed analysis of your project:

```bash
doc-gen structure analyze
```

All commands accept `--dry-run`. For `print` and `analyze`, this makes the
read-only intent explicit; those commands never write project output.

## Common Options

### Profile Selection

Choose how much detail to include:

```bash
doc-gen structure generate --profile minimal
doc-gen structure generate --profile default
doc-gen structure generate --profile detailed
```

### Smart Mode

Let DocGen automatically choose the best settings:

```bash
doc-gen structure generate --smart
```

### Maximum Depth

Control how deep the tree goes:

```bash
doc-gen structure generate --max-depth 3
```

## Configuration File

Create a `.projectstructure.toml` file in your project root:

```toml
[tool.doc-gen]
profile = "default"
max_depth = 3
show_files = true
smart_mode = true
```

## Next Steps

- Read the [Commands Reference](user-guide/commands.md) for full command details
- Check the [Configuration Guide](configuration.md) for all options
- See the [User Guide](user-guide/overview.md) for detailed usage
