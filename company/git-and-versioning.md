---
scope: always
owner: Eren
status: draft
---
# Git and Versioning

## Branches
- `main` is always releasable. No direct pushes.
- Naming: `feature/short-name`, `fix/short-name`, `hotfix/short-name`.
- Branches are short-lived — a few days at most.

## Commits
- Conventional Commits: `feat:`, `fix:`, `refactor:`, `docs:`, `test:`, `chore:`.
- Breaking change: `feat!:` plus a `BREAKING CHANGE:` note in the body.
- One commit = one logical change.

## Pull requests
- Description covers: what, why, risk level (low/medium/high), how it was tested, rollback path.
- No merge without at least one approval and green CI.
- Prefer squash merge.

## Versioning
- SemVer: MAJOR (breaking), MINOR (feature), PATCH (fix).
- Every release is tagged (`v1.4.2`) and gets a changelog entry.

## Merging to main
- High-risk changes ship behind a feature flag.
- Hotfixes branch from `main` and are tagged right after merge.
