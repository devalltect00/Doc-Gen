<!-- docs/user-guide/overview.md -->

# User Guide Overview

Welcome to the DocGen User Guide. This guide helps you use DocGen effectively.

## What is DocGen?

DocGen is a CLI tool that automatically generates a `PROJECT_STRUCTURE.md` file showing your project layout. It helps developers quickly understand any project.

## Key Features

- **Auto-generate documentation** - Creates PROJECT_STRUCTURE.md automatically
- **Multiple profiles** - Choose detail level (minimal, default, detailed)
- **Smart mode** - Auto-optimizes output based on project size
- **Configurable** - Uses .projectstructure.toml for settings
- **Rich CLI output** - Beautiful colored terminal output

## Quick Example

```bash
# Install
python -m pip install \
  --index-url "https://<deploy-token-user>:<deploy-token>@gitlab.com/api/v4/projects/<project-id>/packages/pypi/simple" \
  "doc-gen==1.0.1"

# Generate documentation
doc-gen structure generate
```

The registry is private and requires a deploy token with
`read_package_registry` access. See the installation methods guide for source,
artifact, and Docker alternatives.

This creates a PROJECT_STRUCTURE.md file.

## Who Should Use DocGen?

- **Developers** - Document your projects quickly
- **Teams** - Keep documentation consistent
- **Open source maintainers** - Help new contributors understand your project

## Documentation Structure

This user guide includes:

1. **Quick Start** - Get started in 5 minutes
2. **Commands** - Detailed command reference
3. **Installation** - Different installation methods
4. **Lifecycle** - Start, run, stop workflows
5. **Configuration** - Customize behavior

## Next Steps

- Read the [Quick Start](quickstart.md) guide
- Check the [Commands](commands.md) reference
- Try [Smart Mode](smart-mode.md) for automatic optimization
