---
scope: task
when: Game performance, optimization, target devices
owner: Eren
status: draft
---
# Performance and FPS

## Targets
- 60 FPS on target devices (16.6 ms/frame); stable 30 FPS allowed on low-end mobile if declared.
- Frame-time split budgeted (logic, physics, render, UI) and tracked.
- Frame-time stability > average FPS: no spikes > 2× budget in normal play.
- Memory and build-size budget per platform.

## Rules
- Profile on real target devices, not only in editor.
- Zero allocations in per-frame hot paths; pool frequent objects.
- Reduce draw calls: batching, atlases, shared materials, GPU instancing.
- Platform-compressed textures sized to screen use; mipmaps where needed.
- Simple colliders and a pruned collision matrix.
- Heavy work (pathfinding, loading) spread over frames or off main thread; async scene loading.
- Check for leaks across scene loads.

## Mobile
Test 15+ minute sessions for thermal throttling; quality presets or adaptive quality.

Performance check is part of every milestone.
