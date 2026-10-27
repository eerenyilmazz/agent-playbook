---
scope: task
template: game
owner: Eren
status: draft
---
# Asset Pipeline

## Structure and naming
- Folder structure by type and feature, agreed once and documented.
- Naming: `type_name_variant` (e.g. `tex_player_idle`, `sfx_coin_pickup`). Lowercase, no spaces.

## Rules
- Source files (PSD, Blend, etc.) are stored separately from exported game assets.
- Large binaries use Git LFS or a dedicated asset store, not plain git.
- Import settings (compression, size, mip maps) are set by presets per asset type, not per file by hand.
- Every asset has a size budget (texture resolution, polycount, audio length/bitrate).
- Unused assets are removed regularly; build size is tracked per release.
- Audio: compressed formats for music, short uncompressed or lightly compressed for frequent SFX.

## Licensing
- Every third-party asset has a recorded source and license. No unlicensed assets in builds.

## Loading
- Assets are loaded on demand or by level/area (addressables or bundles), not all at startup.
