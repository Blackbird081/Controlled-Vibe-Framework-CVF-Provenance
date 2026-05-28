# CVF Work Order — LHW11-T3 Memory Context Seed Decay Advisory Connector

Memory class: FULL_RECORD

Status: HOLD_UNTIL_T1_AND_T2_PASS

docType: work_order

Date: 2026-05-28

---

## Purpose

Implement LHW11-T3: a second-order connector spec that maps LHW8-T1
`memorySnapshotAdvisoryType` (6 values) × LHW7-T2 `contaminationRiskAfterSeed`
(`low`/`medium`/`high`) + `signalsStillMissing` × AIF-C
`MemoryGatewayDecision.decision` (6 values) into a named
`memoryContextSeedDecayAdvisoryType` + `promotionGateRecommendation`.

LH1 trigger: `tolaria` (PARTIALLY_ABSORBED — "Reopen for governed memory
snapshot packaging or graph context readout; no reinjection").

Gap: LHW8-T1 gives memory snapshot advisory; LHW7-T2 gives context seed missing
signals and contamination risk after seeding; AIF-C gives gateway policy
outcome. No connector maps these three into an advisory that tells Orchestrator
"has the memory context degraded below promotion threshold?" LHW8-T1 defines
`promotionEligible=false` always — this connector adds the advisory for *why*
and *what to do next* when decay is detected.

## Authority Chain

- LHW11 roadmap: `docs/roadmaps/CVF_LHW11_WORKFLOW_CONNECTOR_WAVE11_ROADMAP_2026-05-28.md`
- LHW11 GC-018: `docs/baselines/CVF_GC018_LHW11_WORKFLOW_CONNECTOR_WAVE11_2026-05-28.md`
- LH1 ledger: `docs/reference/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
  (trigger: `tolaria`)
- LHW8-T1 spec: `docs/reference/CVF_LHW8_T1_MEMORY_EVENT_HOOK_GOVERNANCE_SNAPSHOT_CONNECTOR_SPEC_2026-05-28.md`
- LHW7-T2 spec: `docs/reference/CVF_LHW7_T2_PROJECT_MEMORY_CONTEXT_BUDGET_HANDOFF_CONNECTOR_SPEC_2026-05-28.md`
- AIF-C source: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts`
- **T1 gate: `docs/reviews/CVF_LHW11_T1_SESSION_GOVERNANCE_POSTURE_AGGREGATOR_CONNECTOR_COMPLETION_2026-05-28.md`
  must be CLOSED_PASS_BOUNDED**
- **T2 gate: `docs/reviews/CVF_LHW11_T2_SPEC_CHANGE_GOVERNANCE_DECISION_CONNECTOR_COMPLETION_2026-05-28.md`
  must be CLOSED_PASS_BOUNDED**

## Agent Roles

Implementer writes spec (S1–S5). Reviewer checks: all 6 `memorySnapshotAdvisoryType`
values individually row-verified in S5; all 3 `contaminationRiskAfterSeed`
values individually row-verified; all 6 `MemoryGatewayPolicyDecision` values
individually row-verified; `canReinject=false` preserved; `promotionEligible=false`
not overridden. Auditor confirms `tolaria` LH1 trigger recorded; no memory
reinjection claimed. No self-review.

## Scope

**Allowed:**

- `docs/reference/CVF_LHW11_T3_MEMORY_CONTEXT_SEED_DECAY_ADVISORY_CONNECTOR_SPEC_2026-05-28.md`
  (new)
- `docs/reviews/CVF_LHW11_T3_FAST_LANE_AUDIT_2026-05-28.md` (new)
- `docs/reviews/CVF_LHW11_T3_MEMORY_CONTEXT_SEED_DECAY_ADVISORY_CONNECTOR_COMPLETION_2026-05-28.md`
  (new)
- this work order (status update only)
- session continuity files (including LHW11 roadmap Status update + handoff)

**Forbidden:** `EXTENSIONS/`, `governance/contracts/`, any `.ts`/`.tsx`/`.js`/`.py`
file, receipt envelope schema, public-sync repo.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `docs/reference/CVF_LHW8_T1_MEMORY_EVENT_HOOK_GOVERNANCE_SNAPSHOT_CONNECTOR_SPEC_2026-05-28.md`
   — confirm `memorySnapshotAdvisoryType` values at S2 lines 66–71
4. `docs/reference/CVF_LHW7_T2_PROJECT_MEMORY_CONTEXT_BUDGET_HANDOFF_CONNECTOR_SPEC_2026-05-28.md`
   — confirm `contaminationRiskAfterSeed` values at S3 line 116 (`low`/`medium`/`high`)
   and `signalsStillMissing` at S3 line 114
5. `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts`
   — confirm `MemoryGatewayPolicyDecision` values at lines 15–21;
   confirm `MemoryGatewayDecision.decision` at line 44;
   confirm `canReinject` and `rawMemoryReleased=false` at lines 49–50
6. `docs/reviews/CVF_LHW11_T1_SESSION_GOVERNANCE_POSTURE_AGGREGATOR_CONNECTOR_COMPLETION_2026-05-28.md`
   — confirm T1 CLOSED_PASS_BOUNDED
7. `docs/reviews/CVF_LHW11_T2_SPEC_CHANGE_GOVERNANCE_DECISION_CONNECTOR_COMPLETION_2026-05-28.md`
   — confirm T2 CLOSED_PASS_BOUNDED

## Pre-Dispatch Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| `memorySnapshotAdvisoryType` field | `docs/reference/CVF_LHW8_T1_MEMORY_EVENT_HOOK_GOVERNANCE_SNAPSHOT_CONNECTOR_SPEC_2026-05-28.md` | S3 line 94 | `memorySnapshotAdvisoryType` | LHW8-T1 doc-only field | ACCEPT |
| `snapshot_full_capture` | `docs/reference/CVF_LHW8_T1_MEMORY_EVENT_HOOK_GOVERNANCE_SNAPSHOT_CONNECTOR_SPEC_2026-05-28.md` | S2 line 66 | `memorySnapshotAdvisoryType` value | LHW8-T1 S2 mapping | ACCEPT |
| `snapshot_summary_only` | `docs/reference/CVF_LHW8_T1_MEMORY_EVENT_HOOK_GOVERNANCE_SNAPSHOT_CONNECTOR_SPEC_2026-05-28.md` | S2 line 67 | `memorySnapshotAdvisoryType` value | LHW8-T1 S2 mapping | ACCEPT |
| `snapshot_context_read_only` | `docs/reference/CVF_LHW8_T1_MEMORY_EVENT_HOOK_GOVERNANCE_SNAPSHOT_CONNECTOR_SPEC_2026-05-28.md` | S2 line 68 | `memorySnapshotAdvisoryType` value | LHW8-T1 S2 mapping | ACCEPT |
| `snapshot_redacted_capture` | `docs/reference/CVF_LHW8_T1_MEMORY_EVENT_HOOK_GOVERNANCE_SNAPSHOT_CONNECTOR_SPEC_2026-05-28.md` | S2 line 69 | `memorySnapshotAdvisoryType` value | LHW8-T1 S2 mapping | ACCEPT |
| `snapshot_denied` | `docs/reference/CVF_LHW8_T1_MEMORY_EVENT_HOOK_GOVERNANCE_SNAPSHOT_CONNECTOR_SPEC_2026-05-28.md` | S2 line 70 | `memorySnapshotAdvisoryType` value | LHW8-T1 S2 mapping | ACCEPT |
| `snapshot_approval_pending` | `docs/reference/CVF_LHW8_T1_MEMORY_EVENT_HOOK_GOVERNANCE_SNAPSHOT_CONNECTOR_SPEC_2026-05-28.md` | S2 line 71 | `memorySnapshotAdvisoryType` value | LHW8-T1 S2 mapping | ACCEPT |
| `signalsStillMissing` field | `docs/reference/CVF_LHW7_T2_PROJECT_MEMORY_CONTEXT_BUDGET_HANDOFF_CONNECTOR_SPEC_2026-05-28.md` | S3 line 114 | `signalsStillMissing` | LHW7-T2 doc-only field | ACCEPT |
| `contaminationRiskAfterSeed` field | `docs/reference/CVF_LHW7_T2_PROJECT_MEMORY_CONTEXT_BUDGET_HANDOFF_CONNECTOR_SPEC_2026-05-28.md` | S3 line 116 | `contaminationRiskAfterSeed` | LHW7-T2 doc-only field | ACCEPT |
| `low` (contaminationRiskAfterSeed) | `docs/reference/CVF_LHW7_T2_PROJECT_MEMORY_CONTEXT_BUDGET_HANDOFF_CONNECTOR_SPEC_2026-05-28.md` | S3 line 116 | `contaminationRiskAfterSeed` value | LHW7-T2 doc-only field | ACCEPT |
| `medium` (contaminationRiskAfterSeed) | `docs/reference/CVF_LHW7_T2_PROJECT_MEMORY_CONTEXT_BUDGET_HANDOFF_CONNECTOR_SPEC_2026-05-28.md` | S3 line 116 | `contaminationRiskAfterSeed` value | LHW7-T2 doc-only field | ACCEPT |
| `high` (contaminationRiskAfterSeed) | `docs/reference/CVF_LHW7_T2_PROJECT_MEMORY_CONTEXT_BUDGET_HANDOFF_CONNECTOR_SPEC_2026-05-28.md` | S3 line 116 | `contaminationRiskAfterSeed` value | LHW7-T2 doc-only field | ACCEPT |
| `MemoryGatewayPolicyDecision` type | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts` | line 15 | `export type MemoryGatewayPolicyDecision` | `MemoryGatewayPolicyDecision` | ACCEPT |
| `allow` | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts` | line 16 | `MemoryGatewayPolicyDecision` value | `MemoryGatewayPolicyDecision` | ACCEPT |
| `allow_limited` | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts` | line 17 | `MemoryGatewayPolicyDecision` value | `MemoryGatewayPolicyDecision` | ACCEPT |
| `allow_redacted` | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts` | line 18 | `MemoryGatewayPolicyDecision` value | `MemoryGatewayPolicyDecision` | ACCEPT |
| `allow_summary_only` | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts` | line 19 | `MemoryGatewayPolicyDecision` value | `MemoryGatewayPolicyDecision` | ACCEPT |
| `deny` | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts` | line 20 | `MemoryGatewayPolicyDecision` value | `MemoryGatewayPolicyDecision` | ACCEPT |
| `require_human_approval` | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts` | line 21 | `MemoryGatewayPolicyDecision` value | `MemoryGatewayPolicyDecision` | ACCEPT |
| `MemoryGatewayDecision.decision` | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts` | line 44 | `decision: MemoryGatewayPolicyDecision` | `MemoryGatewayDecision` | ACCEPT |
| `MemoryGatewayDecision.canReinject` | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts` | line 49 | `canReinject: boolean` | `MemoryGatewayDecision` | ACCEPT |
| `MemoryGatewayDecision.rawMemoryReleased` | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts` | line 50 | `rawMemoryReleased` | `MemoryGatewayDecision` | ACCEPT |
| `memoryContextSeedDecayAdvisoryType` (new) | N/A — canonical doc-only field | S3 new fields | doc-only | Memory context seed decay advisory packet | ACCEPT |
| `promotionGateRecommendation` (new) | N/A — canonical doc-only field | S3 new fields | doc-only | Memory context seed decay advisory packet | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification | Status |
| --- | --- | --- | --- | --- |
| T3 spec; `canReinject=false` preserved | S1, S3, Claim Boundary | invariant stated | `rg "canReinject=false"` | OPEN |
| All 6 `memorySnapshotAdvisoryType` values individually row-verified | S5 | 6 rows | No aggregate | OPEN |
| All 3 `contaminationRiskAfterSeed` values individually row-verified | S5 | 3 rows | No aggregate | OPEN |
| All 6 `MemoryGatewayPolicyDecision` values individually row-verified | S5 | 6 rows | No aggregate | OPEN |
| LHW11 wave closure summary in completion review | Closure Checklist | T1+T2+T3 summary table | Reviewer checks | OPEN |
| T1 AND T2 gates confirmed | Authority Chain | both completion reviews | Read both reviews | OPEN |

## Deliverable — Connector Spec

File:
`docs/reference/CVF_LHW11_T3_MEMORY_CONTEXT_SEED_DECAY_ADVISORY_CONNECTOR_SPEC_2026-05-28.md`

S2 design: map `memorySnapshotAdvisoryType` × `contaminationRiskAfterSeed` ×
`MemoryGatewayDecision.decision` → `memoryContextSeedDecayAdvisoryType` +
`promotionGateRecommendation`.

Key rows:
- `snapshot_full_capture` × `low` × `allow` → `memory_context_healthy_eligible_for_review`
  | "Request operator review for promotion. Context healthy and complete."
- `snapshot_summary_only` × `medium` × `allow_summary_only` → `memory_context_partial_promotion_gated`
  | "Promotion blocked: only summary captured. Full capture required."
- `snapshot_redacted_capture` × `high` × `allow_redacted` → `memory_context_contaminated_promotion_blocked`
  | "Promotion blocked: high contamination risk. Redaction audit required."
- `snapshot_denied` × any × `deny` → `memory_context_capture_denied_no_promotion`
  | "No capture; no promotion path. Decay confirmed."
- `snapshot_approval_pending` × any × `require_human_approval` → `memory_context_pending_human_approval`
  | "Promotion suspended pending human approval of capture."
- any × `high` × any → `memory_context_high_contamination_hold`
  | "High contamination risk. Hold all promotion requests."
- `signalsStillMissing` non-empty × any × any → add `missing_signals_present=true` to advisory

Key invariants: `canReinject=false` preserved; `promotionEligible=false` from
LHW8-T1 is not overridden — this connector adds advisory type only, not
promotion authority.

## Pre-Flight

- [ ] Working tree clean
- [ ] T1 AND T2 CLOSED_PASS_BOUNDED confirmed
- [ ] All 6 `memorySnapshotAdvisoryType` values confirmed from LHW8-T1 S2
- [ ] All `MemoryGatewayPolicyDecision` values confirmed from AIF-C source lines 15–21
- [ ] `contaminationRiskAfterSeed` values confirmed from LHW7-T2 S3

## Write Ownership

Implementer owns all new files. No file outside Allowed list may be modified.

## Execution Plan

1. Read all required first reads; confirm T1 and T2 gates.
2. Confirm all input values from source specs and runtime source.
3. Draft spec (S1–S5); verify line count < 250 after S4.
4. Run Fast Lane audit.
5. Run governance gates.
6. Reviewer perspective.
7. Update session continuity; mark LHW11 CLOSED_PASS_BOUNDED.
8. Update LHW11 roadmap: Status → CLOSED_PASS_BOUNDED; replace `<lhw11-commit>`
   in Verification section with actual commit SHA.
9. Commit.
10. Write completion review with LHW11 wave closure summary.

## Evidence Requirements

- Spec < 250 lines
- All 6 `memorySnapshotAdvisoryType` + all 3 `contaminationRiskAfterSeed` +
  all 6 `MemoryGatewayPolicyDecision` values individually row-verified in S5
- `canReinject=false` preserved and explicit in S1 and S3
- `promotionEligible=false` not overridden
- T1 and T2 gates confirmed
- No code file in diff
- LHW11 wave closure summary in completion review

## Acceptance Criteria

- [ ] T1 AND T2 CLOSED_PASS_BOUNDED confirmed before dispatch
- [ ] Spec with all 5 sections; < 250 lines
- [ ] All 6 `memorySnapshotAdvisoryType` values individually row-verified in S5
- [ ] All 3 `contaminationRiskAfterSeed` values individually row-verified in S5
- [ ] All 6 `MemoryGatewayPolicyDecision` values individually row-verified in S5
- [ ] `canReinject=false` explicit; `promotionEligible=false` not overridden
- [ ] `runtimeExecutionAuthorized=false` explicit
- [ ] No code file in diff
- [ ] Session continuity updated; LHW11 CLOSED_PASS_BOUNDED
- [ ] LHW11 roadmap updated with actual commit SHA
- [ ] Completion review with LHW11 wave closure summary

Fail conditions:

- T1 or T2 gate not confirmed
- `canReinject=true` or `promotionEligible=true` anywhere in spec
- Aggregate rows in S5 for multi-value types
- Completion review missing LHW11 wave closure summary

## Review Gate

Before committing: T1+T2 gates confirmed; all 15 individual enum value rows in
S5; `canReinject=false` explicit; `promotionEligible=false` not overridden;
spec < 250 lines; no code file.

## Closure Checklist

- [ ] T1 AND T2 CLOSED_PASS_BOUNDED confirmed
- [ ] Spec with all 5 sections
- [ ] S2 maps `memorySnapshotAdvisoryType` × `contaminationRiskAfterSeed` ×
  `MemoryGatewayDecision.decision` → decay advisory
- [ ] `canReinject=false` and `promotionEligible=false` preserved
- [ ] S5 Source Verification: no aggregate rows
- [ ] No code file in diff
- [ ] Fast Lane audit created
- [ ] Session continuity updated; LHW11 CLOSED_PASS_BOUNDED
- [ ] LHW11 roadmap Status → CLOSED_PASS_BOUNDED; Verification SHA updated
- [ ] Completion review with LHW11 wave closure summary table written

## Return-To-Orchestrator Conditions

Stop if: T1 or T2 gate missing; any token cannot be confirmed; writing requires
memory reinjection or `canReinject=true`; spec exceeds 250 lines before S4.

## LHW11 Wave Closure Gate

This is the final tranche. After T3 is committed, completing agent must:

1. Update `CVF_SESSION/ACTIVE_SESSION_STATE.json`:
   - `lhw11WorkflowConnectorWave11.status = CLOSED_PASS_BOUNDED`
   - `nextAllowedMove` names LHW11 as latest CLOSED_PASS_BOUNDED; states any
     further connector wave requires a fresh roadmap and GC-018
2. Update `CVF_SESSION_MEMORY.md` to reference LHW11 CLOSED_PASS_BOUNDED
3. Update active handoff with full LHW11 wave note

Failure to update all three continuity artifacts blocks the Latest-Closure
Continuity Gate.

## Operator Checkpoint

operator.checkpoint.waiver: Low-risk documentation-only tranche.

## Claim Boundary

LHW11-T3 produces a documentation artifact. It does not claim memory reinjection,
`canReinject=true`, promotion authority, spec mutation, runtime gateway execution,
receipt envelope extension, provider behavior, hosted readiness, production
readiness, or public release readiness.
