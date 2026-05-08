<!-- Memory class: FULL_RECORD -->
# CVF RC2-A2 Guided First-Run Setup Closure Decision

Date: 2026-05-08

Status: CLOSED DELIVERED

## Decision

RC2-A2 is closed. CVF now has a guided first-run setup path that stitches
together A1 doctor/provider diagnostics, env template creation, dependency
guidance, Web start guidance, and first governed-run instructions.

## Delivered

- `scripts/cvf_setup.py`
- `docs/guides/CVF_5_MINUTE_RC_SETUP.md`
- README quick-run link to the guided setup path
- `docs/guides/README.md` index link

## Verification

Commands run:

```bash
python scripts/cvf_setup.py --json
python scripts/cvf_setup.py --write-env --provider alibaba --json
python scripts/cvf_setup.py --provider none --json
```

Results:

| Command | Result |
|---|---|
| `cvf_setup.py --json` | `READY` on configured Windows workspace |
| `cvf_setup.py --write-env --provider alibaba --json` | `READY`; `.env.local` already existed |
| `cvf_setup.py --provider none --json` | `READY`; provider validation skipped with clear next action |

## Claim Boundary

Allowed after A2:

> CVF has a guided, low-friction first-run path on Windows from fresh clone to
> first governed run.

Still forbidden:

- zero friction for all environments
- GA-ready
- Web runtime control console
- Web-triggered governance jobs

## Next Track

Track A is complete for RC2 Foundation. Next checkpoint should be RC2-B0 Module
Runtime Classification Audit, with fresh GC-018 authorization.
