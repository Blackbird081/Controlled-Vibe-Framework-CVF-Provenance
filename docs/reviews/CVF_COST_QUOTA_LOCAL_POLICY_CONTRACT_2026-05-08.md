<!-- Memory class: FULL_RECORD -->
# CVF Cost/Quota Local Policy Contract

**Date:** 2026-05-08
**Status:** IMPLEMENTED
**Track:** CQ1 - Local Budget Policy Contract

## Runtime Contract

Implemented in:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/web-governance-cost-quota.ts`
- integrated into `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/web-governance-jobs.ts`

Active local policy path:

```text
.cvf/config/cost-quota-policy.json
```

The active policy path is local-only by default. Root `.gitignore` now ignores:

```text
.cvf/config/
```

## Default Policy

| Field | Value |
|---|---|
| version | 1 |
| windowMode | rolling_24h |
| globalDailyLiveCallLimit | 120 |
| alibaba dailyLiveCallLimit | 100 |
| deepseek dailyLiveCallLimit | 30 |
| full_live_release_gate per-job cap | 20 |
| provider_check per-job cap | 2 |
| full_live_release_gate cooldown | 300 seconds |
| overrideMode | owner_or_admin |
| auditMode | append_only_jsonl |

## Policy File Protection

- If the policy file contains provider key names with values, token-like
  strings, or high-entropy secret-like values, server preflight blocks with
  `policy_file_contains_secret_like_value`.
- Invalid JSON blocks with `policy_file_invalid_json`.
- The guard falls back to the default policy only for evaluation structure; it
  does not allow jobs when policy validation fails.

## Boundary

- This is a call-count guard, not dollar-price estimation.
- Operator-specific local policy is editable locally and not committed.
