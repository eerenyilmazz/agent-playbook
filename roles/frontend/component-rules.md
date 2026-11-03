---
scope: task
when: Writing or reviewing frontend components
owner: Eren
status: draft
---
# Component Rules

## Smart vs presentational
- **Smart:** uses facades, holds feature state, passes data down.
- **Presentational:** inputs in, outputs out. No services, HTTP or business logic.

## Rules
- Business logic in services/facades; templates free of logic (use computed values/pipes).
- One responsibility per component; split when the template gets hard to read.
- `OnPush` (or signals) by default. `trackBy`/`track` on lists; virtual scroll for long lists.
- Typed inputs; outputs named as events (`saved`, `cancelled`).
- Folders: core (singletons) / shared (reusable UI) / features (lazy-loaded).
- UI from the design system (templates/web/design-system.md); accessible (templates/web/accessibility.md).
- Handle loading, empty and error inputs.
- Reactive forms only; validators in dedicated files.

## Tests
Presentational: inputs/outputs/render. Smart + facades: behavior with mocked services.
