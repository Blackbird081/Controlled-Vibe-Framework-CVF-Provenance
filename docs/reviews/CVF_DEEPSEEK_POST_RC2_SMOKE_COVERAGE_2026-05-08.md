<!-- Memory class: FULL_RECORD -->
# CVF DeepSeek Post-RC2 Smoke Coverage

**Date:** 2026-05-08
**Status:** PASS
**Provider lane:** DeepSeek
**Claim tier:** smoke/sanity, not regression confirmation

## Cost/Quota Preflight

| Field | Value |
|---|---|
| decision | allowed |
| decisionReason | cost_quota_allowed |
| expectedLiveCallCount | 8 |
| providerLane | deepseek |
| providerUsageBefore | 0 |
| providerLimit | 30 |
| auditPath | D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF\.cvf\runtime\web-governance-cost-quota-ds-smoke-1778259474229.jsonl |

## Summary

- Successful DeepSeek checks: 8/8
- Families covered: 7
- N>=8 is smoke/sanity only. N>=14 is required before using regression confirmation wording.

## Records

| ID | Family | Status | HTTP | Receipt | Output length | Detail |
|---|---|---|---:|---:|---:|---|
| ds-first-value | first_value | PASS | 200 | yes | 4386 | DeepSeek governed response returned receipt. |
| ds-intent-routing | intent_routing | PASS | 200 | yes | 2114 | DeepSeek governed response returned receipt. |
| ds-continuity-root | continuity | PASS | 200 | yes | 4821 | DeepSeek governed response returned receipt. |
| ds-clarification | clarification | PASS | 200 | yes | 3905 | DeepSeek governed response returned receipt. |
| ds-deliverable-pack | deliverable_pack | PASS | 200 | yes | 7368 | DeepSeek governed response returned receipt. |
| ds-trusted-form | trusted_form | PASS | 200 | yes | 5623 | DeepSeek governed response returned receipt. |
| ds-export-readout | export_readout_metrics | PASS | 200 | yes | 2277 | DeepSeek governed response returned receipt. |
| ds-metrics-sanity | export_readout_metrics | PASS | 200 | yes | 5590 | DeepSeek governed response returned receipt. |

## Boundary

- This is bounded DeepSeek smoke/sanity coverage after CQ controls.
- It does not claim full DeepSeek/Alibaba parity.
- It does not replay the full W149 corpus.
- It does not claim DeepSeek regression confirmation.