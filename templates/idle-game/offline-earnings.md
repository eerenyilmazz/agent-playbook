---
scope: task
template: idle-game
owner: Eren
status: draft
---
# Offline Earnings

## Calculation
- Offline time = now − last saved time, using a trusted time source where possible.
- Earnings are calculated analytically (rate × time), not by simulating every tick.
- A cap on offline time (e.g. a few hours) is a design choice; upgrades or purchases may raise it.
- Apply an efficiency factor if offline earnings should be lower than active play.

## Anti-cheat
- Device clock changes (moving time forward) are detected: compare with server time or monotonic clocks when available.
- Negative or absurd durations are clamped and logged.
- If there's a server, the server calculates offline earnings for anything tradeable or competitive.

## UX
- On return, show a clear "while you were away" summary with the amount and time.
- Optional bonus (e.g. watch an ad to double) is offered, never forced.

## Save
- Save timestamp on every save and on app background/quit.
