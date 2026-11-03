---
scope: task
when: Building or changing any web UI
owner: Eren
status: draft
---
# Accessibility

Target: WCAG 2.2 AA.

## Must
- Semantic HTML first (`button`, `a`, `label`, landmarks); ARIA only to fill gaps.
- Full keyboard use, logical tab order, visible focus, no focus traps (except modals, which return focus on close).
- `alt` on images (`alt=""` if decorative).
- Every input has a visible label; errors in text, linked via `aria-describedby`, announced.
- Contrast ≥ 4.5:1 text, ≥ 3:1 large text and UI parts.
- Never color alone for meaning.
- One `h1`, ordered headings.
- Works at 200% zoom and 320 px width.
- Touch targets ≥ 24×24 px (aim 44).
- Respect `prefers-reduced-motion`. No auto-playing media with sound.

## Verify
- Automated (axe/Lighthouse) on key pages in CI.
- Manual keyboard pass on main flows; screen reader spot-check before release.

A11y regressions are bugs. Audit procedure: a11y-audit skill.
