<!-- Memory class: FULL_RECORD -->
# CVF DeepSeek Post-RC2 Confirmation Coverage

**Date:** 2026-05-09
**Status:** PASS
**Provider lane:** DeepSeek
**Model:** `deepseek-chat`
**Claim tier:** bounded post-RC2 regression confirmation

## Cost/Quota Preflight

| Field | Value |
|---|---|
| decision | allowed |
| decisionReason | cost_quota_allowed |
| expectedLiveCallCount | 14 |
| providerLane | deepseek |
| providerUsageBefore | 0 |
| providerLimit | 30 |
| auditPath | D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF\.cvf\runtime\web-governance-cost-quota-ds-confirmation-1778286297115.jsonl |

## Summary

- Successful DeepSeek checks: 14/14
- Families with >=2 PASS records: 7/7
- This satisfies the authorized N>=14 confirmation tier only if all rows below are PASS.

## Family Coverage

| Family | PASS | Total |
|---|---:|---:|
| first_value | 2 | 2 |
| intent_routing | 2 | 2 |
| continuity | 2 | 2 |
| clarification | 2 | 2 |
| deliverable_pack | 2 | 2 |
| trusted_form | 2 | 2 |
| export_readout_metrics | 2 | 2 |

## Records

| ID | Family | Status | HTTP | Receipt | Decision | Output length | Detail |
|---|---|---|---:|---:|---|---:|---|
| ds-first-value-strategy | first_value | PASS | 200 | yes | ALLOW | 4580 | DeepSeek governed response returned receipt. |
| ds-first-value-documentation | first_value | PASS | 200 | yes | ALLOW | 5824 | DeepSeek governed response returned receipt. |
| ds-intent-routing-email | intent_routing | PASS | 200 | yes | ALLOW | 1797 | DeepSeek governed response returned receipt. |
| ds-intent-routing-pricing | intent_routing | PASS | 200 | yes | ALLOW | 5182 | DeepSeek governed response returned receipt. |
| ds-continuity-root | continuity | PASS | 200 | yes | ALLOW | 4481 | DeepSeek governed response returned receipt. |
| ds-continuity-pack | continuity | PASS | 200 | yes | ALLOW | 5786 | DeepSeek governed response returned receipt. |
| ds-clarification-risk | clarification | PASS | 200 | yes | ALLOW | 4154 | DeepSeek governed response returned receipt. |
| ds-clarification-persona | clarification | PASS | 200 | yes | ALLOW | 5699 | DeepSeek governed response returned receipt. |
| ds-deliverable-pack-competitor | deliverable_pack | PASS | 200 | yes | ALLOW | 5098 | DeepSeek governed response returned receipt. |
| ds-deliverable-pack-feature | deliverable_pack | PASS | 200 | yes | ALLOW | 2490 | DeepSeek governed response returned receipt. |
| ds-trusted-form-persona | trusted_form | PASS | 200 | yes | ALLOW | 4382 | DeepSeek governed response returned receipt. |
| ds-trusted-form-risk | trusted_form | PASS | 200 | yes | ALLOW | 3957 | DeepSeek governed response returned receipt. |
| ds-export-readout-feature | export_readout_metrics | PASS | 200 | yes | ALLOW | 3251 | DeepSeek governed response returned receipt. |
| ds-export-readout-pricing | export_readout_metrics | PASS | 200 | yes | ALLOW | 4581 | DeepSeek governed response returned receipt. |

## Boundary

- This is bounded DeepSeek confirmation after Post-RC2 hardening and CQ controls.
- It does not claim full DeepSeek/Alibaba parity.
- It does not claim exact provider-dollar cost control.
- It does not cover Gemini, OpenAI, or Claude; those lanes require separate live keys and evidence.