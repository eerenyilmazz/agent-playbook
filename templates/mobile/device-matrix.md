---
scope: task
template: mobile
owner: Eren
status: draft
---
# Device Matrix

## Default minimums
Set per project in its README, based on target users. Starting point:
- iOS: current major version and the one before it.
- Android: cover the large majority of active devices in the target market; check current distribution data before deciding.

## Test matrix (minimum before release)
- One small-screen phone and one large-screen phone per platform.
- One low-end Android device (limited RAM, slower CPU).
- One tablet if the app supports tablets.
- Latest OS version and the minimum supported OS version.

## Checks
- Layout with largest system font size and display zoom.
- Dark mode.
- Notch/cutout and gesture navigation areas.
- Rotation (if supported) and split-screen.
- Poor network and low battery mode.

## Rules
- Raising the minimum OS version is a breaking change for some users: decide with data and announce it.
- Use a device cloud for devices not physically available.
