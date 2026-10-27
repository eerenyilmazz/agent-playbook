---
scope: task
role: game-developer
owner: Eren
status: draft
---
# Game Developer Rules

Project rules: templates/game/ and templates/idle-game/ where relevant.

## Code
- Gameplay logic separated from engine/presentation code where practical, so it can be tested.
- Data-driven: stats, balance and content in config/data files, not hard-coded.
- Avoid deep inheritance; prefer components/composition.
- No per-frame allocations or expensive lookups in update loops (see performance-and-fps.md).
- Events/messages for decoupling systems, but keep them traceable; no "magic" global events.

## Workflow
- Small, playable increments; the build is always runnable.
- Scenes/prefabs edited by one person at a time, or split to avoid merge conflicts.
- Large assets via Git LFS (see asset-pipeline.md).
- Build for target platforms regularly, not only in the editor.

## Saves and updates
- Never break existing saves; versioned save format with migrations.

## Testing
- Unit tests for game rules and economy math; automated smoke test that loads each scene.
- Playtest notes recorded after each milestone.
