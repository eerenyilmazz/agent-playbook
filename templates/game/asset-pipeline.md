---
scope: task
when: Importing, organizing or loading game assets
owner: Eren
status: draft
---
# Asset Pipeline

## Structure
- Folders by feature then type; documented once.
- Names: `type_name_variant` lowercase (`tex_player_idle`, `sfx_coin_pickup`).

## Rules
- Source files (PSD, .blend) stored apart from exported assets.
- Binaries in Git LFS or an asset store.
- Import settings via per-type presets, not per file.
- Budgets per type: texture size, polycount, audio bitrate/length.
- Music streamed/compressed; short frequent SFX decompressed on load.
- Unused assets removed; build size tracked per release.
- Loading by level/area (addressables/bundles), not all at startup.

## Licensing
Every third-party asset has recorded source + license. No unlicensed assets in builds.
