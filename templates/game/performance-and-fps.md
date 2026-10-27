---
scope: task
template: game
owner: Eren
status: draft
---
# Performance and FPS

## Targets (default)
- 60 FPS on target devices; 30 FPS stable is acceptable for low-end mobile if declared.
- Frame time budget at 60 FPS: ~16.6 ms total. Split it (e.g. logic, physics, rendering, UI) and track each part.
- Stable frame time matters more than average FPS; avoid spikes.

## Rules
- Profile on real target devices, not only in the editor.
- No allocations in per-frame hot paths; use object pooling for frequent spawns.
- Limit draw calls: batching, atlases, shared materials.
- Textures compressed in platform formats, sized for their on-screen use.
- Physics: simple colliders, sensible layer collision matrix.
- Expensive work (pathfinding, loading) spread across frames or moved off the main thread.
- Memory budget per platform defined; watch for leaks across scene loads.

## Mobile
- Watch thermal throttling in longer sessions (15+ minutes).
- Offer a low-quality setting or adapt automatically.

## Process
- A performance check is part of every milestone, not saved for the end.
