---
scope: always
owner: Eren
status: draft
---
# Git and Versioning

## Branches
- `main` is protected and always releasable: no direct push, no force push.
- `feature/…`, `fix/…`, `hotfix/…`; short-lived (days). Rebase on `main` before merge.

## Commits
- Conventional Commits: `feat|fix|refactor|perf|docs|test|chore(scope): summary`.
- Breaking: `feat!:` + `BREAKING CHANGE:` footer.
- One logical change per commit (examples/commits.md). No secrets, generated files or large binaries.

## Pull requests
- Body: what, why, risk level, test evidence, rollback path, breaking? (yes/no).
- Merge requires: 1+ approval, green CI, resolved comments. Squash merge.
- Revert first if `main` breaks; fix in a new PR.

## Versioning
- SemVer. Tag every release `vX.Y.Z`; changelog entry per tag.
- Public API/contract deprecations announced one MINOR before removal.

## Hotfix
- Branch from the released tag/`main`, minimal scope, expedited (not skipped) review, tag immediately.
