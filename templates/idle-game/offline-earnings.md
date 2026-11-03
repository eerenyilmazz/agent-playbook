---
scope: task
when: Idle game offline progress and time handling
owner: Eren
status: draft
---
# Offline Earnings

## Calculate
- Offline time = now − last save, from a trusted source (server time when online).
- Analytic formula (rate × time), never tick simulation.
- Cap offline time (design choice; upgradable). Optional efficiency factor < 1.

## Anti-cheat
- Detect clock tampering: compare with server time or monotonic uptime.
- Clamp negative/absurd durations and log them.
- Server computes earnings for anything competitive or tradeable.

## UX
"While you were away" summary (time + amount). Optional bonus (e.g. rewarded ad ×2), never forced.

## Save
Timestamp on every save and on background/quit.
