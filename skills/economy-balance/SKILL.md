---
name: economy-balance
description: Model, tune and verify an idle/incremental game economy — cost curves, income, prestige, offline earnings — with a simulation before and analytics after. Use when designing or rebalancing game progression.
---
# Economy Balance

Rules: templates/idle-game/economy-balance.md, templates/idle-game/offline-earnings.md, templates/idle-game/monetization.md.

## Steps
1. **Targets.** Write target times: first upgrade, first wall, first prestige, each later milestone; session length; days to "end" of content.
2. **Inventory.** List every currency with its sources and sinks. A currency without a sink → fix design first.
3. **Model** in a sheet or script:
   - Generator cost: `base × rate^owned` (start rate 1.07–1.15).
   - Income: `baseIncome × owned × multipliers`.
   - Prestige reward: e.g. `floor(k × lifetimeEarnings^0.5)`; multiplier per prestige point.
   - Offline: `incomePerSec × min(offlineTime, cap) × efficiency`.
4. **Simulate** a player buying the best value-per-cost upgrade each step. Output time to each milestone, active and offline.
5. **Tune** base, rate and multipliers until times match targets. Avoid dead zones (> target wait with nothing to buy).
6. **Check edge cases:** number overflow, display formatting, very long offline, skipping prestige, buying with rewarded boosts.
7. **Move values to config** (remote config if possible). No balance numbers in code.
8. **Ship behind a remote config version;** A/B large changes.
9. **Verify with analytics:** real time-to-milestone, prestige rate, drop-off points, D1/D7 retention vs the model.
10. **Iterate.** Change one lever at a time. Nerfs to existing players: compensate or migrate.

## Output
Model file in repo, target vs simulated table, chosen config values, list of open risks.
