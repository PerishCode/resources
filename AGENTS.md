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

## Standard deployment flow

- The release workflow is triggered manually with a release version and target ref; pushing `main` alone does not publish a release.
- Standard release flow: merge or push the desired commit to `main`, then run the `Release` workflow with the next version (for example `0.1.9`) and the ref to publish from.
- The workflow requires a stable release version in `X.Y.Z` form, rejects versions that do not exceed the current latest release, packages `sources/oh-my-oc/`, publishes two assets, and creates the matching `v<version>` tag from the selected ref as part of the release.
- Normal releases are explicitly published as the repository `latest` release.
- After running the workflow, verify the `Release` GitHub Actions workflow succeeded before considering deployment complete.
- If you changed release behavior, tag rules, or produced assets, update this section and any related docs in the same change.
