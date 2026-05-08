<!-- Memory class: FULL_RECORD -->
# CVF Static CI Gate Design

**Date:** 2026-05-08  
**Track:** RC2 Pre-GA / CI1  
**Status:** DESIGN ACCEPTED FOR CI1 IMPLEMENTATION  

## Design

Add a dedicated static CI lane named `CVF Static CI Gate`.

This lane is intentionally separate from the full release gate. It runs only
checks that do not require provider secrets:

| Check | Command source | Live provider use |
|---|---|---:|
| Web build | `npm run build` in `cvf-web` | No |
| Web TypeScript | `npx tsc --noEmit` in `cvf-web` | No |
| Secrets scan | release-gate secret scanner reused by static runner | No |
| Docs governance | `governance/compat/check_docs_governance_compat.py` | No |
| Static governance tests | targeted Vitest files in `cvf-web` | No |

## Runner

The local runner is:

```bash
python scripts/run_cvf_static_ci_gate.py --json
```

It must not call the default release gate bundle because that bundle includes
mandatory live governance E2E. The static runner may reuse non-live helper
functions such as secret scanning.

## Workflow

The CI workflow is:

```text
.github/workflows/cvf-static-ci.yml
```

It installs only local dependencies and runs the static gate. It does not
require GitHub secrets and does not expose provider keys.

## Claim Boundary

Allowed:

> The repository has a non-secret static CI lane suitable for pre-regression
> baseline protection.

Forbidden:

- Live governance is proven by CI1.
- Release-quality proof is available in PR CI.
- Provider readiness or live E2E has run.
