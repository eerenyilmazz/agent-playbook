---
scope: task
when: Web UI work; choosing browser APIs or CSS features
owner: Eren
status: draft
---
# Browser Support

## Default matrix (override per project from real analytics)
- Chrome, Edge, Firefox, Safari: latest 2 versions.
- iOS Safari, Android Chrome: latest 2 majors.
- No IE.

## Rules
- One source of targets (`browserslist`); tooling handles transpile and prefixes.
- New APIs: check support; provide fallback or progressive enhancement.
- Breakpoints tested: 320 / 768 / 1024 / 1440 px.
- Correct `type`/`inputmode`/`autocomplete` on inputs for mobile keyboards and autofill.
- Safe areas (`env(safe-area-inset-*)`) on mobile.

## Before release
Main flows on Chrome + Safari (desktop and mobile); visual pass on Firefox. Bugs in supported browsers are real bugs.
