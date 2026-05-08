<!-- Memory class: FULL_RECORD -->
# CVF Cost/Quota Audit Evidence

**Date:** 2026-05-08
**Job ID:** `91b5c331-884d-49c1-b0ce-137a1a95d559`
**Job status:** succeeded
**Release gate result:** PASS
**Checks passed:** 7/7
**Cost/quota audit path:** `.cvf\runtime\web-governance-cost-quota.jsonl`

## Audit Events For Job

| Event type | Present |
|---|---:|
| estimate_requested | yes |
| estimate_allowed | yes |
| usage_incremented | yes |

## Assertions

- Usage increment recorded: PASS.
- Override used: no.
- Audit fields include role, job ID, provider lane, expected call count, window, caps, and decision reason.
- No raw provider key is included in this artifact.