# Example: Commit Messages

Rules: company/git-and-versioning.md.

**Good**
```
feat(orders): add partial refund endpoint
fix(cart): recalculate tax when shipping country changes
perf(search): add index on products(category_id, created_at)
refactor(payments): extract provider client behind interface (no behavior change)
docs(adr): add 0007 transactional outbox
```

**Breaking**
```
feat(api)!: return amounts in minor units

BREAKING CHANGE: `amount` is now an integer in minor units (kuruş/cents).
Clients must divide by 100. v1 keeps decimals until 2027-01-31.
```

**Bad**
```
fix stuff
WIP
update
refactor + new refund feature + fix login bug
```
