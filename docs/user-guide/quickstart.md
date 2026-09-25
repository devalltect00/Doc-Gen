<!-- docs/user-guide/quickstart.md -->

# Quick Start

Get started with DocGen in 5 minutes.

## Step 1: Install

Install Doc-Gen from the private GitLab PyPI registry with a deploy token that
has `read_package_registry` access:

```bash
python -m pip install \
  --index-url "https://<deploy-token-user>:<deploy-token>@gitlab.com/api/v4/projects/<project-id>/packages/pypi/simple" \
  "doc-gen==1.1.0"
```

## Step 2: Verify Installation

Check that DocGen is installed:

```bash
doc-gen --help
```

You should see the help output.

## Step 3: Generate Structure

Run the generate command:

```bash
doc-gen structure generate
```

This creates `docs/project_structure.md` by default.

## Step 4: View Output

Open the generated file:

```markdown
# docs/project_structure.md
```

You should see your project structure.

## Common Variations

### Print to Console

Instead of saving to a file, print to console:

```bash
doc-gen structure print
```

### Use Smart Mode

Let DocGen optimize automatically:

```bash
doc-gen structure generate --smart
```

### Use a Profile

Choose a detail level:

```bash
# Minimal - just directories
doc-gen structure generate --profile minimal

# Detailed - everything
doc-gen structure generate --profile detailed
```

## Configuration (Optional)

Run `doc-gen init`, then edit `.config/doc_gen/config.toml`:

```toml
[tool.doc-gen.cli.structure]
profile = "default"
max_depth = 3
show_files = true
smart_mode = true
```

## Next Steps

- Read the [Commands](commands.md) for full reference
- Check [Installation Methods](installation-methods.md) for other ways to install
- See configuration options in [Configuration](../configuration.md)
