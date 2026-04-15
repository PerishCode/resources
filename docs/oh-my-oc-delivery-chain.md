# oh-my-oc delivery chain

This note explains how `resources` and `oh-my-oc` fit together so iteration work stays aligned with the actual publish/install/runtime path.

## Source of truth

- `sources/oh-my-oc/` contains the public resource payload that can be packaged for `oh-my-oc`.
- `sources/opencode/` is reserved for generic Opencode resources that are genuinely stable outside the `oh-my-oc` patch chain.

## Release path

- `resources` publishes source payloads.
- The current release workflow is manually dispatched with a version and ref, packages `sources/oh-my-oc/` from the selected commit, publishes `oh-my-oc-<version>.tar.gz` for Unix consumers and `oh-my-oc-<version>.zip` for Windows consumers, and creates the matching `v<version>` release tag during publish.
- The release flow is publish-first: operators choose the version and source ref in the workflow run, the workflow resolves the exact commit snapshot, and the tag is created by the release step instead of being pushed ahead of time.
- Stable releases are gated to `X.Y.Z` versions that must exceed the current latest stable version.
- Normal releases are explicitly marked as the repository `latest` release so consumers do not rely on GitHub auto-selection.
- Content outside `sources/oh-my-oc/` does not automatically become part of the `oh-my-oc` resource release.

## Practical release operations

- Prepare the release commit on `main` first, then run the `Release` workflow instead of creating a local tag.
- Provide the target release version without the `v` prefix, and use the desired git ref if you need to publish from something other than `main`.
- Treat the workflow run as the release authority: if it fails, do not backfill the tag manually.
- After the workflow succeeds, verify the published release assets and resulting `v<version>` tag on GitHub.

## oh-my-oc consumption path

- `oh-my-oc` can use bundled local patch resources or fetch remote resources from `resources`.
- The effective remote patch shape is `sources/oh-my-oc/opencode/{path}`.
- The patch flow only manages `opencode.json` and `agent/*.md` in the target Opencode config directory.

## Runtime implication

- A file being present in the `resources` repo does not make it runtime-visible to Opencode agents.
- Only content that enters the `oh-my-oc` patch chain and is written into the managed Opencode config boundary is reliably runtime-visible.
- If a commander/runtime behavior must always be available, prefer putting it directly in the managed agent/config payload instead of relying on sidecar files or soft references.

## Practical guidance

- Put publishable `oh-my-oc` patch resources under `sources/oh-my-oc/`.
- Put cross-repo explanation, iteration notes, and chain guidance under `docs/`.
- Do not introduce external template or reference files as runtime dependencies unless the install/patch chain gives them a stable runtime location and a native loading mechanism.
