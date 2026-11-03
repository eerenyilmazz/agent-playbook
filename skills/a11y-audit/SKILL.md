---
name: a11y-audit
description: Audit a web page or flow against WCAG 2.2 AA with automated and manual checks, and report fixes. Use before releasing UI or on request.
---
# Accessibility Audit

Rules: templates/web/accessibility.md.

## Steps
1. **Scope.** List pages/flows (e.g. sign-up, checkout) and states (error, empty, modal open).
2. **Automated scan** (axe/Lighthouse) per page and state. Note it finds only part of the issues.
3. **Keyboard:** Tab through everything. Check order, visible focus, no traps, Esc closes dialogs, focus returns after close, skip link present.
4. **Screen reader** (NVDA or VoiceOver) on main flow: headings make sense, landmarks, labels read, errors announced, buttons/links named by purpose, dynamic updates announced (`aria-live`).
5. **Visual:** contrast (text, icons, focus ring), 200% zoom, 320 px width, no color-only meaning, text spacing override doesn't break layout.
6. **Forms:** labels, required marked in text, errors linked and specific, autocomplete attributes.
7. **Media and motion:** captions/transcripts, no autoplay with sound, reduced motion respected.
8. **Report** each issue and retest after fixes.

## Finding format
```
[Blocker|Major|Minor] Title — WCAG criterion (e.g. 2.4.7 Focus Visible)
Where: page / component / state
Problem: what a user can't do
Fix: concrete change
```

## Exit
No Blocker or Major open on in-scope flows. Add automated checks for fixed issues to CI.
