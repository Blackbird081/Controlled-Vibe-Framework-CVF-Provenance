# CVF Work Order - LHW11 Post-Closure Correction

Memory class: FULL_RECORD

Status: CLOSED_PASS

docType: work_order

Date: 2026-05-29

---

## 1. Mission

Correct LHW11 closure-quality defects exposed by the 2026-05-29 governance
rule hardening without expanding LHW11 runtime scope.

## Purpose

Purpose: make LHW11 evidence truthful and machine-checkable after the new
Allowed-scope, symbol-hygiene, whole-wave range, and line-count gates.

## 2. Authority Chain

- Operator instruction: raise rules first, then fix the findings.
- Rule authority: `docs/reference/CVF_WORK_ORDER_CLOSURE_QUALITY_GATE_STANDARD_2026-05-28.md`
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- Active handoff: `AGENT_HANDOFF_V14_2026-05-27.md`

## 3. Scope

Allowed scope:

- `docs/reference/CVF_LHW11_T1_SESSION_GOVERNANCE_POSTURE_AGGREGATOR_CONNECTOR_SPEC_2026-05-28.md`
- `docs/reference/CVF_LHW11_T1_SESSION_GOVERNANCE_POSTURE_AGGREGATOR_SOURCE_VERIFICATION_2026-05-29.md`
- `docs/reviews/CVF_LHW11_T1_FAST_LANE_AUDIT_2026-05-28.md`
- `docs/reviews/CVF_LHW11_T1_SESSION_GOVERNANCE_POSTURE_AGGREGATOR_CONNECTOR_COMPLETION_2026-05-28.md`
- `docs/work_orders/CVF_WO_LHW11_T3_MEMORY_CONTEXT_SEED_DECAY_ADVISORY_CONNECTOR_2026-05-28.md`
- `docs/reference/CVF_LHW11_T3_MEMORY_CONTEXT_SEED_DECAY_ADVISORY_CONNECTOR_SPEC_2026-05-28.md`
- `docs/reviews/CVF_LHW11_T3_MEMORY_CONTEXT_SEED_DECAY_ADVISORY_CONNECTOR_COMPLETION_2026-05-28.md`
- this correction work order.

Forbidden scope:

- Runtime/code changes.
- Provider, memory, receipt envelope, public-sync, hosted, or production claims.
- Archive cleanup or unrelated baseline movement.
- Live-route proof for `abtop`, `gridex`, or execution-layer families.

Risk ceiling: R1 documentation correction.

## Scope / Target / Owner Boundary

Target: LHW11 documentation evidence only.

Owner boundary: this work order owns only the files listed in Allowed scope.
Anything outside those paths returns to Orchestrator.

## Agent Roles

- Orchestrator: current Codex session.
- Implementer: current Codex session.
- Reviewer: governance machine gates plus operator follow-up review.
- Operator checkpoint: required only if a runtime, public-sync, or live-proof
  claim becomes necessary.

## Required First Reads

- `docs/reference/CVF_WORK_ORDER_CLOSURE_QUALITY_GATE_STANDARD_2026-05-28.md`
- `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`
- `docs/reference/CVF_LHW11_T1_SESSION_GOVERNANCE_POSTURE_AGGREGATOR_CONNECTOR_SPEC_2026-05-28.md`
- `docs/reference/CVF_LHW11_T3_MEMORY_CONTEXT_SEED_DECAY_ADVISORY_CONNECTOR_SPEC_2026-05-28.md`

## Pre-Flight Checks

Required checks:

- `git rev-parse --short HEAD`
- `python governance/compat/check_work_order_dispatch_quality.py --base <baseHead> --head HEAD --enforce`
- `python governance/compat/check_markdown_structural_completeness.py --base <baseHead> --head HEAD --enforce`

## Write Ownership

Write mode: modify-listed plus one new appendix file.

Owned files are exactly the Allowed scope list in Section 3.

## Execution Plan

1. Split T1 row-level source verification into a same-domain appendix.
2. Correct stale T1 audit/completion line-count and changed-file claims.
3. Correct T3 Source Verification symbol cells and `canReinject=false` wording.
4. Run dispatch-quality, structural, line-count, and session gates.

## Evidence Requirements

- Current line counts for T1 primary spec and T3 spec.
- Dispatch-quality pass for changed LHW11 artifacts.
- Structural-completeness pass for this correction work order.
- No runtime/code/public/live-proof diff.

## Acceptance Criteria

- [x] T1 primary spec is below 250 lines.
- [x] T1 source verification remains preserved in a same-domain appendix.
- [x] T3 Source Verification symbol cells contain no value or type syntax.
- [x] T3 `canReinject=false` claim is connector-normalized.
- [x] No runtime/code/public/live-proof claim added.

## Review Gate

Closure requires machine-gate pass for dispatch quality and markdown structural
completeness. Human review may still reopen if a later full-wave LHW11 audit
finds additional defects.

## 4. Required Corrections

| Finding | Correction | Evidence |
| --- | --- | --- |
| T1 spec line-count claim was false | Split row-level S5 evidence into appendix and keep primary spec below 250 lines | Primary spec actual 244 lines |
| T1 completion/audit changed-file claims were incomplete | Add appendix and corrective note for original out-of-scope archive cleanup | Completion review updated |
| T3 Source Verification symbol cells contained type annotations | Use bare symbols `decision` and `canReinject` | Work order updated |
| T3 prose overstated `canReinject=false` as source-preserved | Reword as connector-normalized false | Work order/spec/completion updated |
| T3 completion line-count claim was stale | Recompute current spec line count | Spec actual 158 lines |

## 5. Closure Checklist

- [x] T1 primary spec remains under 250 lines after S5 appendix split.
- [x] T1 source-verification evidence is preserved in a same-domain appendix.
- [x] T1 audit and completion line-count claims are current.
- [x] T3 Source Verification symbol cells use bare field/symbol names.
- [x] T3 `canReinject=false` wording is connector-normalized, not source-preserved.
- [x] No runtime/code/public/live-proof claim added.

## Claim Boundary

This correction only cleans LHW11 documentation evidence and governance
traceability. It does not reopen LHW11 scope, execute live routes, modify
runtime behavior, or prove provider/memory behavior.

## Return Conditions

Return to Orchestrator if any correction requires runtime/code changes, live
route execution, public-sync, or files outside Allowed scope.

## Operator Checkpoint

No operator checkpoint is required for this documentation-only correction after
the listed governance gates pass.
