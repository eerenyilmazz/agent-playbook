# Contributing

All changes go through pull requests. `main` is never pushed to directly.

## Flow
1. Branch from `main`: `docs/<scope>-<short-name>` or `feat/<short-name>`.
2. Edit following README → *Adding or changing a file* (one topic, one file; English; tight bullets).
3. Run `python3 scripts/check.py` and commit the regenerated `INDEX.md`.
4. Open a PR using the template. Title in Conventional Commits form, e.g. `docs(backend): add caching rules`.
5. CI (`check`) must pass. Code owner (@eerenyilmazz) approves. Squash merge.

## What reviewers check
- No duplicated rule — links instead of copies.
- `when:` trigger specific enough for the loader to pick the file.
- Budgets and ArkeLab limits pass (`check.py`).
- `review: expert-required` files: facts have a source in `docs/compliance-sources.md`; `status: approved` only with a named expert.
- Downstream impact: ArkeLab imports this repo — renaming or moving files changes document identities there. Call it out in the PR.

## Releases
Tag `main` as `vX.Y.Z` when ArkeLab should import a new version. Breaking structure changes (folder layout, frontmatter fields) bump MAJOR.
