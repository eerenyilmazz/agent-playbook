---
scope: task
when: Writing game code or editing scenes/prefabs
owner: Eren
status: draft
---
# Game Developer Rules

Project rules: templates/game/, templates/idle-game/.

## Code
- Gameplay logic separate from engine/presentation where practical → testable.
- Data-driven: stats, balance, content in data files.
- Composition over deep inheritance.
- No allocations or expensive lookups in update loops.
- Decoupled via events, but traceable; no hidden global events.

## Workflow
- Small playable increments; build always runnable.
- Scenes/prefabs: one editor at a time or split to avoid merge conflicts.
- Large assets via Git LFS.
- Build on target platforms regularly.

## Saves
Never break existing saves; versioned format + migrations.

## Tests
Unit tests for rules and economy math; automated smoke test loading each scene; playtest notes per milestone.
