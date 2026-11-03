---
scope: task
when: Creating or changing UI components, styles, themes
owner: Eren
status: draft
---
# Design System

## Tokens
- Color, spacing, type, radius, shadow, motion defined once as CSS variables.
- No raw hex/px in components. Spacing scale: 4, 8, 12, 16, 24, 32, 48, 64.
- Semantic color tokens (`--color-danger`), not palette names, in components.
- Themes (light/dark) = token swap only.

## Components
- Use the shared library; new variants go into the library, not features.
- Each documents purpose, props, variants and states: default, hover, focus, active, disabled, loading, error, empty.
- Changing a shared component = potentially breaking; check all usages.

## Type
- ≤ 2 families, fixed type scale, body ≥ 16 px, line length 45–75 chars.

Dev rules: roles/frontend/component-rules.md. A11y: accessibility.md.
