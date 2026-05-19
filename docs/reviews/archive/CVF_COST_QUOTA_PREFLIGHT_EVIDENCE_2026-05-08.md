<!-- Memory class: FULL_RECORD -->
# CVF Cost/Quota Preflight Evidence

**Date:** 2026-05-08
**Job ID:** `91b5c331-884d-49c1-b0ce-137a1a95d559`
**Job status:** succeeded
**Release gate result:** PASS
**Checks passed:** 7/7
**Cost/quota audit path:** `.cvf\runtime\web-governance-cost-quota.jsonl`

## Result

| Field | Value |
|---|---|
| decision | allowed |
| decisionReason | cost_quota_allowed |
| expectedLiveCallCount | 7 |
| providerLane | alibaba |
| globalUsageBefore | 0 |
| globalLimit | 120 |
| providerUsageBefore | 0 |
| providerLimit | 100 |
| cooldownSeconds | 300 |

## Boundary

- This is a live under-budget allow-path proof for Web `full_live_release_gate`.
- Over-limit, direct API bypass, cooldown, and override paths are covered by no-live targeted tests.
- No raw provider key is included in this artifact.