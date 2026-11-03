---
scope: task
when: Idle game currencies, costs, upgrades, prestige
owner: Eren
status: draft
---
# Economy Balance

Tuning procedure: economy-balance skill.

## Model first
- Simulate the economy (sheet or script) before coding: income/s, costs, time to each milestone.
- Costs grow exponentially (`base × rate^level`, rate typically 1.07–1.15); income grows slower → walls that drive upgrades/prestige.
- Target times defined: first upgrade (seconds), first prestige (hours), later milestones.

## Rules
- All values in data/remote config, never code.
- Big-number type from day one; display format (K, M, B… or scientific) decided early.
- Prestige grants a clear permanent multiplier; run 2 noticeably faster than run 1.
- Every currency has sources and sinks.
- Log purchases, prestiges and time-to-milestone; compare with the model.

## Changes
Nerfs to existing players are breaking: compensate or migrate.
