---
scope: task
role: frontend
owner: Eren
status: draft
---
# Component Rules

## Smart vs presentational
- **Smart (container):** Talks to services/facades, holds feature state, passes data down.
- **Presentational (dumb):** Inputs in, events out. No services, no HTTP, no business logic.

## Rules
- Business logic lives in services/facades, never in templates or components.
- Templates contain no complex expressions; move logic to computed values or pipes.
- One component, one responsibility. Split when a template grows hard to read.
- Use OnPush change detection (or signals) by default.
- Inputs are typed; outputs have clear names (`saved`, `cancelled`).
- Structure: core (singletons), shared (reusable UI), features (feature folders).
- Shared components come from the design system (templates/web/design-system.md); no one-off copies.
- Every component handles loading, empty and error states it can receive.
- Accessibility rules apply (templates/web/accessibility.md).

## Forms
- Reactive forms only; validators in dedicated files.

## Testing
- Presentational components: test inputs/outputs and rendering.
- Smart components and facades: test behavior with mocked services.
