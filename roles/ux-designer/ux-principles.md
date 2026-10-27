---
scope: task
role: ux-designer
owner: Eren
status: draft
---
# UX Principles

Related: templates/web/design-system.md, templates/web/accessibility.md.

## Process
- Start from the user's goal and the problem, not the screen.
- Map the main flow before designing screens; keep it as short as possible.
- Design all states: default, loading, empty, error, success, no permission.
- Test with real users (even 3–5 people) before building large features.

## Principles
- Consistency over novelty: reuse existing patterns and components.
- One primary action per screen; make it obvious.
- Clear, plain language; buttons say what they do ("Save changes", not "OK").
- Prevent errors before showing error messages (constraints, defaults, confirmations for destructive actions).
- Feedback for every action within a moment (loading, success, failure).
- Mobile first for anything used on phones.

## Handoff
- Designs use design-system tokens and components; new components are flagged explicitly.
- Specs include states, responsive behavior and accessibility notes.
- UI changes to live products are reversible and announced if they change familiar flows.
