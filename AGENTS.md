# AGENTS.md

This repository is for personal use. Keep it simple and clean first; avoid over-designing collaboration, process, or generalized resource systems.

`resources` is a source-and-release repo for public resource payloads, not a CLI repo and not a runtime manager.

## Repo boundary

- `sources/` holds raw resource sources grouped by consumer, currently `sources/oh-my-oc/` and `sources/opencode/`.
- `docs/` holds lightweight repo guidance when a source/release chain needs explanation beyond this file.
- `scripts/` holds tiny packaging helpers only.
- `.github/workflows/release.yml` packages release assets from the sources.

## Maintenance guidance

- Keep source layout obvious and low-maintenance.
- Prefer updating an existing source tree over adding parallel variants.
- Keep packaging scripts tiny and direct.
- Release assets should stay predictable and easy to consume remotely.
- Do not turn this repo into a generic build system.
- Keep source trees factual and low-maintenance; put cross-repo iteration guidance in `docs/` instead of expanding source payload structure.
- Keep the `oh-my-oc` release assets parallel across platforms: `.tar.gz` for Unix consumers and `.zip` for Windows consumers.
- Use `sources/oh-my-oc/` only for content that should enter the `oh-my-oc` release/patch chain.
- If repo layout or release behavior changes, update this file at the same time.
