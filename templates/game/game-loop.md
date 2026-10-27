---
scope: task
template: game
owner: Eren
status: draft
---
# Game Loop

## Core loop first
- Define the core loop in one sentence (e.g. "explore → fight → loot → upgrade").
- Prototype and playtest the core loop before building content around it.
- Every feature must strengthen the core loop or the meta loop; otherwise it waits.

## Technical loop
- Fixed timestep for physics and gameplay logic; rendering may interpolate.
- Game logic is independent of frame rate (use delta time correctly).
- Separate game state from presentation, so logic can be tested without rendering.
- Input is processed once per frame in a single place.

## Game states
- Explicit states: boot, menu, playing, paused, game over. Transitions are defined, not scattered flags.
- Pause truly stops gameplay time; UI keeps working.

## Save data
- Save format is versioned with migrations. Never break existing saves in an update.
- Save regularly and on app background/quit; write atomically to avoid corruption.

## Playtesting
- Playtest every milestone with people who haven't seen the game; record where they get stuck.
