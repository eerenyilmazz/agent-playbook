---
scope: task
when: Mobile testing, choosing minimum OS versions
owner: Eren
status: draft
---
# Device Matrix

## Minimums (set per project from market data)
- iOS: current + previous major.
- Android: cover the large majority of active devices in the target market; check current distribution before deciding.

## Test before release
- Per platform: small phone, large phone; tablet if supported.
- One low-end Android (≤ 4 GB RAM).
- Latest OS and minimum supported OS.

## Check
Largest font/display zoom · dark mode · notch/cutouts and gesture nav · rotation/split-screen (if supported) · slow network · low-power mode · app resume after process death.

## Rules
- Raising minimum OS is breaking for some users: decide with data, announce first.
- Use a device cloud for missing hardware.
