---
scope: task
when: Designing flows, screens, UX changes
owner: Eren
status: draft
---
# UX Principles

Related: templates/web/design-system.md, templates/web/accessibility.md.

## Process
- Start from the user goal and problem; map the flow before screens; shortest path wins.
- Design every state: default, loading, empty, error, success, no permission, offline.
- Test with 3–5 real users before building large features.

## Principles
- Consistency over novelty; reuse patterns and components.
- One primary action per screen.
- Plain language; buttons say the result ("Save changes").
- Prevent errors (constraints, defaults, confirm destructive actions, undo where possible).
- Feedback for every action.
- Mobile first where phones are used.

## Handoff
- Tokens and existing components only; new components flagged.
- Specs include states, responsive behavior, a11y notes, copy.
- Changes to familiar flows in live products are reversible and announced.
