# CVF Work Order — LHW9-T2 Noncoder Friction Advisory Connector

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-05-28

---

## Purpose

Implement LHW9-T2: a connector spec binding CB1
`ProductSkillPackRequestContextReadout` (`missingSignals`, `contaminationFlags`,
`readiness`) × C8 `ProductSkillPackSelectionStatus` (`selected`,
`no_certified_pack_match`) × LHW3-T2 clarification packet types (4 values)
into a noncoder friction advisory packet (`frictionAdvisoryType`,
`antiOverconstraintRecommendation`). Closes the gap where no standard maps
CB1 friction signals + C8 selection failure to a named advisory with an
`antiOverconstraintRecommendation` for non-coder operators.

Documentation-only tranche. `canReinject=false` and `rawMemoryReleased=false`
preserved.

## Authority Chain

- LHW9 roadmap: `docs/roadmaps/CVF_LHW9_WORKFLOW_CONNECTOR_WAVE9_ROADMAP_2026-05-28.md`
- LHW9 GC-018: `docs/baselines/CVF_GC018_LHW9_WORKFLOW_CONNECTOR_WAVE9_2026-05-28.md`
- Fast Lane audit: `docs/reviews/CVF_LHW9_T2_FAST_LANE_AUDIT_2026-05-28.md` → FAST_LANE_READY
- T1 gate: `docs/reviews/CVF_LHW9_T1_MCP_TOOL_APPROVAL_ADVISORY_CONNECTOR_COMPLETION_2026-05-28.md`
  — CLOSED_PASS_BOUNDED
- LH1 ledger: `docs/reference/archive/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
  (triggers: `AI-first vs Human-first`, `Human System Harness`)
- CB1 completion: `docs/reviews/archive/CVF_CB1_CONTEXT_BUDGET_REQUEST_SHAPING_READOUT_COMPLETION_2026-05-25.md`
- C8 completion: `docs/reviews/archive/CVF_C8_PRODUCT_SKILL_PACK_SELECTION_READOUT_COMPLETION_2026-05-25.md`
- LHW3-T2 spec: `docs/reference/CVF_LHW3_REQUEST_CLARIFICATION_RE_INTAKE_LOOP_CONNECTOR_SPEC_2026-05-27.md`

## Agent Roles

Implementer writes spec (S1–S5) using CB1, C8, and LHW3-T2 vocabulary verbatim.
Reviewer checks `ProductSkillPackRequestContextReadiness` values verbatim,
both `ProductSkillPackSelectionStatus` values verbatim, all 4 LHW3-T2
clarification packet types verbatim, `canReinject=false` and
`rawMemoryReleased=false` explicit, boundary table honest, S5 complete.
No self-review.

## Scope

**Allowed:**

- `docs/reference/CVF_LHW9_T2_NONCODER_FRICTION_ADVISORY_CONNECTOR_SPEC_2026-05-28.md`
  (new — primary deliverable)
- this work order (status update only)
- session continuity files

**Forbidden:** `EXTENSIONS/` (any file), `governance/contracts/` (any file),
any `.ts`/`.tsx`/`.js`/`.py` file, receipt envelope schema, public-sync repo.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/product-outcome.runtime.ts`
   — confirm `ProductSkillPackSelectionStatus` at line 45;
   confirm `ProductSkillPackRequestContextReadiness` at lines 48–52;
   confirm `missingSignals` at line 88;
   confirm `contaminationFlags` at line 89
4. `docs/reference/CVF_LHW3_REQUEST_CLARIFICATION_RE_INTAKE_LOOP_CONNECTOR_SPEC_2026-05-27.md`
   — confirm S2 clarification packet types at lines 47–50 (all 4 values)
5. `docs/roadmaps/CVF_LHW9_WORKFLOW_CONNECTOR_WAVE9_ROADMAP_2026-05-28.md`
   — confirm T2 deliverable shape

## Pre-Dispatch Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| `ProductSkillPackSelectionStatus` type | `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/product-outcome.runtime.ts` | line 45 | `ProductSkillPackSelectionStatus` | `ProductSkillPackSelectionStatus` | ACCEPT |
| `selected` | `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/product-outcome.runtime.ts` | line 45 | `ProductSkillPackSelectionStatus` value | `ProductSkillPackSelectionStatus` | ACCEPT |
| `no_certified_pack_match` | `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/product-outcome.runtime.ts` | line 45 | `ProductSkillPackSelectionStatus` value | `ProductSkillPackSelectionStatus` | ACCEPT |
| `ProductSkillPackRequestContextReadiness` type | `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/product-outcome.runtime.ts` | lines 48–52 | `ProductSkillPackRequestContextReadiness` | `ProductSkillPackRequestContextReadiness` | ACCEPT |
| `ready` | `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/product-outcome.runtime.ts` | line 49 | `ProductSkillPackRequestContextReadiness` value | `ProductSkillPackRequestContextReadiness` | ACCEPT |
| `needs_clarification` | `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/product-outcome.runtime.ts` | line 50 | `ProductSkillPackRequestContextReadiness` value | `ProductSkillPackRequestContextReadiness` | ACCEPT |
| `needs_context_compaction` | `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/product-outcome.runtime.ts` | line 51 | `ProductSkillPackRequestContextReadiness` value | `ProductSkillPackRequestContextReadiness` | ACCEPT |
| `blocked_contaminated_brief` | `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/product-outcome.runtime.ts` | line 52 | `ProductSkillPackRequestContextReadiness` value | `ProductSkillPackRequestContextReadiness` | ACCEPT |
| `ProductSkillPackRequestContextReadout.missingSignals` | `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/product-outcome.runtime.ts` | line 88 | `missingSignals` | `ProductSkillPackRequestContextReadout` | ACCEPT |
| `ProductSkillPackRequestContextReadout.contaminationFlags` | `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/product-outcome.runtime.ts` | line 89 | `contaminationFlags` | `ProductSkillPackRequestContextReadout` | ACCEPT |
| `missing_context_clarification_packet` | `docs/reference/CVF_LHW3_REQUEST_CLARIFICATION_RE_INTAKE_LOOP_CONNECTOR_SPEC_2026-05-27.md` | S2 line 47 | clarification packet type | LHW3-T2 packet | ACCEPT |
| `noisy_context_clarification_packet` | `docs/reference/CVF_LHW3_REQUEST_CLARIFICATION_RE_INTAKE_LOOP_CONNECTOR_SPEC_2026-05-27.md` | S2 line 48 | clarification packet type | LHW3-T2 packet | ACCEPT |
| `ambiguous_outcome_clarification_packet` | `docs/reference/CVF_LHW3_REQUEST_CLARIFICATION_RE_INTAKE_LOOP_CONNECTOR_SPEC_2026-05-27.md` | S2 line 49 | clarification packet type | LHW3-T2 packet | ACCEPT |
| `unmatched_request_clarification_packet` | `docs/reference/CVF_LHW3_REQUEST_CLARIFICATION_RE_INTAKE_LOOP_CONNECTOR_SPEC_2026-05-27.md` | S2 line 50 | clarification packet type | LHW3-T2 packet | ACCEPT |
| New doc-only fields `frictionAdvisoryType`, `antiOverconstraintRecommendation` | N/A — doc-only | S3 new fields | doc-only | Noncoder friction advisory packet | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
| --- | --- | --- | --- | --- |
| T2 spec; CB1/C8/LHW3-T2 field names verbatim | S1–S5 | spec at target path | Reviewer confirms source-verbatim field names | CLOSED |
| `canReinject=false` and `rawMemoryReleased=false` preserved | S1, S3 | invariants stated | Reviewer checks | CLOSED |
| S2 maps CB1 readiness × C8 selection to friction advisory | S2 | rows covering all 4 readiness values | Reviewer checks S2 rows | CLOSED |
| Source Verification Table complete | S5 | Source Verification Table | Reviewer checks no `BLOCKED_SOURCE_NOT_FOUND` | CLOSED |
| No code file modified | Evidence | git diff output | `git diff --name-only` | CLOSED |

## Deliverable — Connector Spec

File:
`docs/reference/CVF_LHW9_T2_NONCODER_FRICTION_ADVISORY_CONNECTOR_SPEC_2026-05-28.md`

## Pre-Flight

- [x] Working tree clean
- [x] All required first reads done
- [x] CB1/C8 fields confirmed from source
- [x] LHW3-T2 packet types confirmed from spec

## Write Ownership

Implementer owns all new files. No file outside the Allowed list may be modified.

## Execution Plan

1. Read all required first reads.
2. Confirm all CB1/C8/LHW3-T2 field names.
3. Draft spec (S1–S5) with Source Verification Table.
4. Confirm no code file staged.
5. Reviewer perspective — record result.
6. Update session continuity.
7. Commit.
8. Write completion review; include T3 gate answer.

Spec size guard: < 250 lines.

## Evidence Requirements

- Spec at target path with all 5 sections present
- S2 covers all 4 `ProductSkillPackRequestContextReadiness` values
- `canReinject=false` and `rawMemoryReleased=false` explicit in S1 and S3
- S4 boundary table present; no doc-only row labeled Runtime
- S5 Source Verification Table complete; no `BLOCKED_SOURCE_NOT_FOUND`
- No code file in diff
- Session continuity updated
- Completion review with T3 gate answer written

## Acceptance Criteria

- [x] Spec with all 5 sections created
- [x] S2 covers all 4 `ProductSkillPackRequestContextReadiness` values
- [x] `canReinject=false` and `rawMemoryReleased=false` explicit
- [x] S4 boundary table honest; no doc-only row labeled Runtime
- [x] S5 Source Verification Table complete
- [x] No code file in diff
- [x] Session continuity updated

Fail conditions:

- Missing LHW9 GC-018 or ACCEPT row citing non-existent file
- Any claim this connector injects memory, sets `canReinject=true`, or
  automates re-intake

## Review Gate

All CB1/C8/LHW3-T2 field names verbatim; `canReinject=false` and
`rawMemoryReleased=false` explicit; S5 complete; no code file in diff.

## Closure Checklist

- [x] Spec created with all 5 sections
- [x] S2 mapping uses CB1/C8/LHW3-T2 vocabulary verbatim
- [x] `canReinject=false` and `rawMemoryReleased=false` explicit
- [x] S5 Source Verification Table complete
- [x] S4 boundary table honest
- [x] No code file in diff
- [x] Session continuity updated
- [x] Completion review with T3 gate answer written

## Return-To-Orchestrator Conditions

Stop if: T1 not CLOSED_PASS; any required read file missing; connector
requires memory injection or lifts `canReinject=false`; spec exceeds 250 lines.

## Operator Checkpoint

operator.checkpoint.waiver: Low-risk documentation-only tranche; T1 gate
confirmed; no operator checkpoint required.

## Claim Boundary

LHW9-T2 produces a documentation artifact. It does not claim CB1/C8/LHW3-T2
runtime extension, memory injection, raw memory release, receipt envelope
extension, provider behavior, hosted readiness, production readiness, or
public release readiness.
