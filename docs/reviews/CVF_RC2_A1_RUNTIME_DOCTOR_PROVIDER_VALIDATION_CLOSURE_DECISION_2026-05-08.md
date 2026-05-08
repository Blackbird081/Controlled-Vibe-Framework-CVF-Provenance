<!-- Memory class: FULL_RECORD -->
# CVF RC2-A1 Runtime Doctor + Provider Validation Closure Decision

Date: 2026-05-08

Status: CLOSED DELIVERED

## Decision

RC2-A1 is closed. CVF now has secret-safe local diagnostics for clone/runtime
readiness and provider readiness.

## Delivered

- `scripts/cvf_doctor.py`
- `scripts/cvf_provider_check.py`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/.gitignore` now allows
  `.env.example` to be tracked.
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/.env.example` is added as the
  tracked env template referenced by the deploy guide.

## Verification

Commands run:

```bash
python scripts/cvf_doctor.py --json
python scripts/cvf_provider_check.py --provider alibaba --json
python scripts/cvf_provider_check.py --provider deepseek --json
python scripts/cvf_provider_check.py --provider alibaba --json --no-local-env
python scripts/cvf_provider_check.py --provider alibaba --live --json
python scripts/cvf_provider_check.py --provider deepseek --live --json
```

Results:

| Command | Result |
|---|---|
| `cvf_doctor.py --json` | `PASS` on local configured workspace |
| Alibaba provider check without live | `READY_UNVALIDATED` |
| DeepSeek provider check without live | `READY_UNVALIDATED` |
| Alibaba provider check with local env disabled | `MISSING_KEY` |
| Alibaba provider check with live | `LIVE_VALIDATED`, HTTP 200 |
| DeepSeek provider check with live | `LIVE_VALIDATED`, HTTP 200 |

No raw provider key values were printed.

## A0 Blockers Resolved

| A0 Finding | A1 Result |
|---|---|
| Missing tracked `cvf-web/.env.example` | Resolved by `.gitignore` exception and tracked template |
| No one-command doctor | Resolved by `scripts/cvf_doctor.py --json` |
| No provider readiness check | Resolved by `scripts/cvf_provider_check.py --provider ... --json` |

## Remaining Work

Proceed to RC2-A2 only after fresh GC-018 authorization:

- Add guided first-run setup orchestration.
- Use A1 doctor/provider-check as the setup engine.
- Keep Windows as the committed proof platform.

## Boundary

A1 does not provide full guided setup. It does not add Web runtime health UI,
Web operations, or new provider lanes.
