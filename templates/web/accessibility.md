---
scope: task
template: web
owner: Eren
status: draft
---
# Accessibility

Target: WCAG 2.2 level AA.

## Must-haves
- Semantic HTML first: `button`, `a`, `nav`, `main`, `label`. ARIA only when HTML can't express it.
- Every interactive element is reachable and usable by keyboard, with a visible focus style.
- Every image has `alt` text; decorative images use `alt=""`.
- Every form field has a visible label; errors are announced and explained in text.
- Text contrast at least 4.5:1 (3:1 for large text and UI components).
- Color is never the only way to convey meaning.
- Page has one `h1` and a logical heading order.
- Content works at 200% zoom and on 320 px width without horizontal scroll.
- Respect `prefers-reduced-motion`.

## Testing
- Automated scan (e.g. axe) on every key page — catches only part of the issues.
- Manual keyboard pass through main flows.
- Quick screen reader check on critical flows before release.

## Rules
- A new component is not done until it passes the checks above.
- Accessibility regressions are treated as bugs, not enhancements.
