# Project Detection and Metadata

Doc Gen v1.1.0 detects a repository from safe, read-only markers and builds a
composable fingerprint. A fingerprint keeps one primary type for compatibility
while also recording relevant ecosystems, frameworks, and development tools.

## Supported primary types

| Ecosystem | Primary types |
| --- | --- |
| General | `generic` |
| Python | `python`, `django`, `flask`, `fastapi` |
| JavaScript and TypeScript | `nodejs`, `reactjs`, `nextjs` |
| Google Apps Script | `google-apps-script` |
| PHP | `php`, `laravel` |
| Go | `go`, `gin` |

## How composition works

Metadata is merged in this order:

1. Common repository directories and files
2. Detected ecosystem metadata
3. Detected framework metadata

Later, more-specific metadata can refine a common description. Only files and
top-level directories present in the target repository are rendered.

A clasp-based project may therefore be labeled `google-apps-script` while also
using JavaScript, TypeScript, pnpm, and clasp metadata. A Laravel repository may
combine PHP/Laravel backend metadata with separately detected JavaScript tools.

## Detection safety

Detection reads public project manifests such as `package.json`,
`pyproject.toml`, `composer.json`, and `go.mod`. Google Apps Script detection
uses markers such as the `@google/clasp` dependency, `.claspignore`, and
`appsscript.json`.

Doc Gen does not read or document `.clasp.json`, `.clasp.local.json`,
`.clasprc.json`, `.env`, or `.env.*` files. These names are excluded from the
generated tree because they can contain local identifiers or credentials.

## Manual override

Automatic detection is the default. Use a primary override only when necessary:

```bash
doc-gen structure analyze --project-type gin ./service
doc-gen structure generate --project-type laravel ./application
```

The override controls the primary label. Safe signals detected from other
manifests can still enrich metadata and ignore behavior.

## Adding a new ecosystem

Developers can extend support without changing the public command structure:

1. Add a `ProjectType` only when a new primary label is useful.
2. Add safe detection markers to `ProjectDetector`.
3. Add ecosystem or framework metadata to the metadata registry inputs.
4. Add generated-artifact ignores where required.
5. Cover detection, composition, rendering, and safety boundaries with tests.
