# resources

Public resource source and release repo.

## Layout

- `sources/` - raw resource sources grouped by consumer
- `scripts/` - tiny packaging helpers
- `.github/workflows/release.yml` - release packaging for tagged versions
- `AGENTS.md` - maintenance guidance for this repo

## Current source

- `sources/oh-my-oc/opencode/` - patch resource source for `oh-my-oc`

## Release

Tagging `v*` builds a tar.gz for `sources/oh-my-oc` and publishes it as a GitHub Release asset.
