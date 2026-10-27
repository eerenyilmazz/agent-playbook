---
scope: task
template: idle-game
owner: Eren
status: draft
---
# Economy Balance

Step-by-step tuning procedure: economy-balance skill. This file defines the rules.

## Model
- The whole economy is modeled in a spreadsheet or script before implementation: income per second, costs, time to each milestone.
- Cost growth is exponential (cost = base × rate^level); income growth is slower, creating the "wall" that motivates upgrades and prestige.
- Define target times: first upgrade (seconds), first prestige (e.g. hours), mid-game milestones.

## Rules
- All balance values live in data/config files, never in code. Tune without a new build where possible (remote config).
- Large numbers use a big-number type or library; plan display formatting (K, M, B, scientific) early.
- Prestige resets give a clear, permanent multiplier; the second run must feel noticeably faster.
- Every currency has both sources and sinks; no currency without a sink.
- Log key economy events (purchase, prestige, time to milestone) to verify the model against real players.

## Changes
- Rebalancing that makes existing players weaker is a breaking change; compensate or migrate.
