<!-- docs/user-guide/lifecycle.md -->

# Lifecycle

This guide describes the typical lifecycle of using DocGen.

## Basic Lifecycle

### 1. Install

First, install Doc-Gen from the private GitLab PyPI registry with a deploy
token that has `read_package_registry` access:

```bash
python -m pip install \
  --index-url "https://<deploy-token-user>:<deploy-token>@gitlab.com/api/v4/projects/<project-id>/packages/pypi/simple" \
  "doc-gen==1.0.1"
```

### 2. Generate

Generate the initial structure:

```bash
doc-gen structure generate
```

### 3. Review

Review the generated PROJECT_STRUCTURE.md:

- Open the file
- Check the structure looks correct
- Verify all directories are included

### 4. Adjust

If needed, adjust settings:

```bash
# Try different profile
doc-gen structure generate --profile minimal

# Try smart mode
doc-gen structure generate --smart
```

### 5. Save

Commit the generated file to version control:

```bash
git add PROJECT_STRUCTURE.md
git commit -m "Add project structure documentation"
```

---

## Ongoing Usage

### Regular Updates

Update the structure as your project changes:

```bash
doc-gen structure generate
```

### Different Outputs

Use different commands for different needs:

```bash
# Print to console
doc-gen structure print

# Analyze project
doc-gen structure analyze
```

---

## Automation Ideas

### Pre-commit Hook

Add to your pre-commit workflow:

```bash
# .pre-commit-config.yaml
- repo: https://github.com/devalltect00/doc-gen
  rev: v1.0.1
  hooks:
    - id: generate-structure
```

### CI/CD Integration

Automate in CI/CD:

```yaml
# .gitlab-ci.yml or similar
generate-docs:
  script:
    - python -m pip install --index-url "https://gitlab-ci-token:${CI_JOB_TOKEN}@${CI_SERVER_HOST}/api/v4/projects/${CI_PROJECT_ID}/packages/pypi/simple" "doc-gen==1.0.1"
    - doc-gen structure generate
    - git add PROJECT_STRUCTURE.md
    - git commit -m "Update project structure" || true
```

---

## Cleanup

When no longer needed:

### Uninstall

```bash
pip uninstall doc-gen
```

### Remove Configuration

Delete .projectstructure.toml if created.

---

## Related Documentation

- [Quick Start](quickstart.md) - Quick start guide
- [Commands](commands.md) - Full command reference
- [Overview](overview.md) - User guide overview
