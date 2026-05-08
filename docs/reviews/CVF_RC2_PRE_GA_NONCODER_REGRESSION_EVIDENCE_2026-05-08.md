<!-- Memory class: FULL_RECORD -->
# CVF RC2 Pre-GA Non-Coder Regression Evidence

**Date:** 2026-05-08
**Status:** PASS
**Provider lane:** Alibaba

## Summary

- Successful checks: 20
- Required floor: N >= 18
- DeepSeek post-RC2 regression status unknown; this evidence applies to the Alibaba lane only.
- This is a representative Playwright browser-context matrix, not a full W149 40-form UI replay.

## Family Counts

| Family | PASS count |
|---|---:|
| first_value | 2 |
| trusted_form | 2 |
| continuity | 2 |
| intent_routing | 2 |
| clarification | 2 |
| deliverable_pack | 2 |
| metrics | 2 |
| readout | 2 |
| rollout_signal | 2 |
| export_activation | 2 |

## Run Records

| ID | Family | Status | Role | Live receipt | Detail |
|---|---|---|---|---:|---|
| viewer-first-value-receipt | first_value | PASS | viewer | yes | Viewer live execution returned governanceEvidenceReceipt. |
| viewer-trusted-form-receipt | trusted_form | PASS | viewer | yes | Viewer trusted template execution returned receipt. |
| admin-first-value-receipt | first_value | PASS | admin | yes | Admin live execution returned governanceEvidenceReceipt. |
| admin-trusted-form-receipt | trusted_form | PASS | admin | yes | Admin trusted template execution returned receipt. |
| followup-receipt | continuity | PASS | admin | yes | Follow-up execution returned governanceEvidenceReceipt. |
| followup-context | continuity | PASS | admin | yes | Follow-up included previous output context without losing governance receipt. |
| intent-route-email | intent_routing | PASS | admin | yes | routeType=form template=email_template |
| intent-route-competitor | intent_routing | PASS | admin | yes | routeType=form template=competitor_review |
| clarification-state | clarification | PASS | admin | no | Weak input creates bounded clarification state. |
| clarification-answer | clarification | PASS | admin | no | answer recoveryMode=clarify |
| pack-receipt | deliverable_pack | PASS | admin | yes | packType=business_decision |
| pack-actions | deliverable_pack | PASS | admin | yes | Pack includes recommended next actions. |
| metrics-created | metrics | PASS | admin | yes | execution_created event present in representative analytics sample. |
| metrics-exports | metrics | PASS | admin | yes | evidence_exported and deliverable_pack_exported events present in sample. |
| readout-lanes | readout | PASS | admin | yes | lanes=entry_routing:healthy,clarification_recovery:healthy,trusted_form:healthy,followup_continuity:healthy,evidence_export:healthy,deliverable_pack:healthy |
| readout-export-lane | readout | PASS | admin | yes | Evidence export lane exits no_data. |
| rollout-flags-enabled | rollout_signal | PASS | admin | yes | R run sets all three noncoder flags true. |
| rollout-no-block | rollout_signal | PASS | admin | yes | Enabled rollout posture did not block live execution receipts. |
| export-evidence-event | export_activation | PASS | admin | yes | Representative evidence_exported event recorded for W130 lane. |
| export-pack-event | export_activation | PASS | admin | yes | Representative deliverable_pack_exported event recorded for W130 lane. |