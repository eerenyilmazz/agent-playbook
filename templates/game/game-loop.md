---
scope: task
when: Game architecture, gameplay systems, save data
owner: Eren
status: draft
---
# Game Loop

## Design
- Core loop in one sentence (e.g. explore → fight → loot → upgrade). Prototype and playtest it before content.
- A feature must strengthen the core or meta loop, or it waits.

## Technical
- Fixed timestep for gameplay/physics; render interpolates.
- Frame-rate independent logic (correct delta time).
- Game state separate from presentation → testable headless.
- Input read once per frame in one place.
- Seeded randomness so bugs reproduce and tests are deterministic.
- Explicit state machine: boot, menu, playing, paused, game over.
- Pause stops gameplay time; UI still runs.

## Saves
- Versioned format with migrations; updates never break saves.
- Autosave on checkpoints and app background/quit; atomic write (temp file + rename); keep one backup.
- Cloud save conflicts resolved by a defined rule.

## Playtest
Every milestone with fresh players; record where they get stuck or quit.
