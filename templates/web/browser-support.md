---
scope: task
template: web
owner: Eren
status: draft
---
# Browser Support

## Default support matrix
- Latest 2 versions of Chrome, Edge, Firefox, Safari.
- iOS Safari and Android Chrome: latest 2 major versions.
- No Internet Explorer.

A project may change this matrix in its README, based on its real analytics.

## Rules
- Define targets once (e.g. `browserslist`) and let tooling handle prefixes and transpiling.
- Check feature support before using new APIs; provide a fallback or progressive enhancement.
- Layout is tested at 320, 768, 1024 and 1440 px widths.
- Touch targets at least 44×44 px on mobile.
- Forms tested with mobile keyboards (correct `type` and `inputmode`).

## Testing before release
- Main flows in Chrome and Safari (desktop + mobile) at minimum.
- Visual check in Firefox.
- A bug in a supported browser is a real bug; in an unsupported one, it's documented.
