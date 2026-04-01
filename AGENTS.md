# AGENTS.md

This repository is for personal use. Keep it simple and clean first; avoid over-designing collaboration, process, or generalized resource systems.

`resources` is a source-and-release repo for public resource payloads, not a CLI repo and not a runtime manager.

## Repo boundary

- `sources/` holds raw resource sources grouped by consumer, currently `sources/oh-my-oc/` and `sources/opencode/`.
- `scripts/` holds tiny packaging helpers only.
- `.github/workflows/release.yml` packages release assets from the sources.

## Maintenance guidance

- Keep source layout obvious and low-maintenance.
- Prefer updating an existing source tree over adding parallel variants.
- Keep packaging scripts tiny and direct.
- Release assets should stay predictable and easy to consume remotely.
- Do not turn this repo into a generic build system.
- Keep generic Opencode templates under `sources/opencode/`; keep `sources/oh-my-oc/` focused on the `oh-my-oc` payload and agent behavior.
- If repo layout or release behavior changes, update this file at the same time.
