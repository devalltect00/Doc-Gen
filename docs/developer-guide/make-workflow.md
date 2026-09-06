# Make workflow

Doc Gen uses a modular Make system. The root `Makefile` only defines module
loading order; command implementations and help fragments live under
`make/core/`.

## Help groups

```bash
make help
make help-local
make help-docker
make help-compose
make help-remote
```

The grouped help output reports command counts from the same registration data
used by the command modules.

## Local structure workflow

```bash
make setup
make l-generate TARGET=.
make l-generate-smart TARGET=.
make l-print TARGET=.
make l-analyze TARGET=.
```

`print` and `analyze` are read-only. Generation may write the configured Markdown
output, so verify `TARGET` and `DOC_GEN_GENERATE_ARGS` before running it.

Pass explicit dry-run through the command argument variables:

```bash
make l-init DOC_GEN_INIT_ARGS="--dry-run"
make l-generate TARGET=. DOC_GEN_GENERATE_ARGS="--dry-run"
```

Dry-run generation performs discovery and rendering but does not write the
configured Markdown output.

## Docker and Compose

```bash
make d-build-all
make d-print TARGET=.
make c-build-all
make c-analyze TARGET=.
make c-check
```

Direct Docker targets use locally built images. Compose helper services reuse the
development image built by the `app` service.

## Published utility images

Remote targets cover all Devalltect utility images:

```bash
make r-phs-pull
make r-doc-gen-pull
make r-custy-pull
make r-reflow-pull
```

Use `REMOTE_TAG`, `REMOTE_WORKSPACE`, `GHCR_OWNER`, and the corresponding
`REMOTE_*_ARGS` variables to select versions, workspaces, and command options.
Registry push targets are externally visible operations and require explicit
review and authorization.

### Custy credential helpers

The published Custy image supports dedicated GitHub and GitLab credential
helpers:

```bash
make r-custy-credentials-set-github
make r-custy-credentials-set-gitlab
make r-custy-credentials-status
make r-custy-credentials-test CUSTY_CREDENTIALS_REMOTE=origin
```

Provider setup uses a read-write credential mount. Status and remote testing
use a read-only mount, and the test performs only a read-only access check.
`CUSTY_CREDENTIALS_HOST_DIR` selects the external host directory, while
`CUSTY_CREDENTIALS_CONTAINER_DIR` defaults to `/run/secrets/custy`.

Ordinary `r-custy-run*` and `r-custy-workflow` targets preserve their previous
behavior by leaving the directory unmounted. Opt in when a workflow needs the
configured fallback:

```bash
make r-custy-run-push CUSTY_CREDENTIALS_MOUNT=true
```

## Safety

Use print or analyze for read-only checks. Do not run generation, cleanup,
registry push, package publish, or release-related targets without checking their
resolved target and effects.
