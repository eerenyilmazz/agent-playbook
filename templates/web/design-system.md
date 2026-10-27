---
scope: task
template: web
owner: Eren
status: draft
---
# Design System

## Tokens
- Colors, spacing, typography, radius and shadows are defined once as tokens (CSS variables).
- No hard-coded colors or pixel values in components; use tokens.
- Spacing follows a scale (e.g. 4, 8, 12, 16, 24, 32, 48).
- Light and dark themes are token swaps, not component rewrites.

## Components
- Build from a shared component library; don't create one-off variants.
- Each component documents: purpose, variants, states (default, hover, focus, disabled, loading, error, empty).
- A new variant is added to the library, not copied into a feature.

## Typography
- Maximum 2 font families. A defined type scale; no ad-hoc sizes.
- Body text at least 16 px; comfortable line length (45–75 characters).

## Rules
- Visual changes to shared components are potentially breaking — check every usage.
- Accessibility rules apply to every component (see accessibility.md).
- Component rules for developers: roles/frontend/component-rules.md.
