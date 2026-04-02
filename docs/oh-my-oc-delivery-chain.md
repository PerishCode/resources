# oh-my-oc delivery chain

This note explains how `resources` and `oh-my-oc` fit together so iteration work stays aligned with the actual publish/install/runtime path.

## Source of truth

- `sources/oh-my-oc/` contains the public resource payload that can be packaged for `oh-my-oc`.
- `sources/opencode/` is reserved for generic Opencode resources that are genuinely stable outside the `oh-my-oc` patch chain.

## Release path

- `resources` publishes source payloads.
- The current release workflow packages `sources/oh-my-oc/` into `oh-my-oc-<version>.tar.gz` for Unix consumers and `oh-my-oc-<version>.zip` for Windows consumers.
- Content outside `sources/oh-my-oc/` does not automatically become part of the `oh-my-oc` resource release.

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
