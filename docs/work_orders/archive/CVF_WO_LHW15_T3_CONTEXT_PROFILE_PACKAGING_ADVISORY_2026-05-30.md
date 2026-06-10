# CVF Work Order — LHW15-T3 Context Profile Packaging Advisory Connector

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-05-30

---

## Purpose

Create a documentation-only connector spec mapping the `Workflow GoClaw` legacy
family's remaining trigger value (context profile packaging) to a new advisory
type `contextProfilePackagingAdvisoryType` building on VI2's
`requestContextReadout` surface.

Contract version: `cvf.contextProfilePackagingAdvisory.lhw15.t3.v1`

Closes LH1 `Workflow GoClaw` trigger (line 163).

## Authority Chain

- LHW15 roadmap: `docs/roadmaps/CVF_LHW15_WORKFLOW_CONNECTOR_WAVE15_ROADMAP_2026-05-30.md`
- LHW15 GC-018: `docs/baselines/CVF_GC018_LHW15_WORKFLOW_CONNECTOR_WAVE15_2026-05-30.md`
- LH1 source: `docs/reference/archive/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md` line 163
- VI2 owner surface: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-request-context-readout.ts`

## Scope

**Allowed:**
- `docs/reference/CVF_LHW15_T3_CONTEXT_PROFILE_PACKAGING_ADVISORY_CONNECTOR_SPEC_2026-05-30.md` (new)
- `docs/reviews/CVF_LHW15_T3_FAST_LANE_AUDIT_2026-05-30.md` (new)
- `docs/reviews/CVF_LHW15_T3_CONTEXT_PROFILE_PACKAGING_ADVISORY_COMPLETION_2026-05-30.md` (new)
- this work order (status update only)
- session continuity files

**Forbidden:** any code file, EXTENSIONS/ change, receipt envelope, public-sync.

## Pre-Dispatch Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| `Workflow GoClaw` PARTIALLY_ABSORBED | `docs/reference/archive/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md` | line 163 | `Workflow GoClaw` | LH1 Closeout Ledger CVF ADD section | ACCEPT |
| VI2 `requestContextReadout` surface | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-request-context-readout.ts` | file root | `requestContextReadout` | VI2 route context readout | ACCEPT |

New advisory types (doc-only):

| New symbol | Purpose | Runtime claim blocked? |
| --- | --- | --- |
| `contextProfilePackagingAdvisoryType` | 6-value enum for context packaging state | Yes — advisory only |
| `packagingGuidance` | Advisory for context trimming or augmentation before handoff | Yes |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact | Verification | Status |
| --- | --- | --- | --- | --- |
| `contextProfilePackagingAdvisoryType` (6 values) | Spec content | connector spec S2 | values enumerated | PASS |
| `packagingGuidance` field | Spec content | connector spec S3 | field described | PASS |
| VI2 `requestContextReadout` mapping | Spec content | connector spec S4 | mapping to `budgetTier` + `missingSignals` | PASS |
| `runtimeExecutionAuthorized=false` | Invariants | connector spec S5 | explicit | PASS |
| LH1 `Workflow GoClaw` trigger closed | Authority Chain | spec header | LH1 line 163 cited | PASS |
| No code file | Scope | diff | review confirms | PASS |

## Agent Roles

Implementer: write connector spec. Reviewer: verify advisory types, VI2 mapping, boundary. No self-review.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `docs/reference/archive/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md` — confirm `Workflow GoClaw` at line 163

## Write Ownership

Implementer owns all new files listed in Allowed. Only Allowed files may be touched.

## Execution Plan

1. Read required first reads; confirm `Workflow GoClaw` LH1 line 163.
2. Write connector spec with S1–S6 sections per Implementation Design below.
3. Write Fast Lane audit.
4. Write completion review.
5. Run governance gates.
6. Update session continuity; commit.

## Evidence Requirements

- Connector spec with `contextProfilePackagingAdvisoryType` (6 values) and `packagingGuidance`
- VI2 `requestContextReadout` field mapping present (`budgetTier`, `missingSignals`, `noiseFlags`, `contaminationFlags`)
- `runtimeExecutionAuthorized=false` explicit
- LH1 `Workflow GoClaw` trigger cited (line 163)
- No code file in diff

## Acceptance Criteria

- [x] Connector spec complete with all required sections
- [x] `contextProfilePackagingAdvisoryType` with 6 values
- [x] `packagingGuidance` field documented
- [x] VI2 field mapping present
- [x] `runtimeExecutionAuthorized=false` explicit
- [x] LH1 `Workflow GoClaw` trigger cited and closed
- [x] No code file in diff

## Fail Conditions

- Advisory type enum missing or fewer than 6 values
- VI2 mapping absent
- `runtimeExecutionAuthorized` not explicitly `false`

## Review Gate

Connector spec complete; 6-value advisory type; VI2 mapping; `runtimeExecutionAuthorized=false`; no code file.

## Operator Checkpoint

operator.checkpoint.waiver: Operator authorized LHW15 directly 2026-05-30.

## Pre-Flight Checks

- [x] LHW15 GC-018 confirmed
- [x] `Workflow GoClaw` LH1 line 163 disposition confirmed: PARTIALLY_ABSORBED
- [x] VI2 `requestContextReadout` owner surface confirmed
- [x] Working tree clean

## Implementation Design

### Connector Spec Structure

S1 — Purpose and LH1 source citation (Workflow GoClaw line 163, VI2 surface)
S2 — Advisory type enum:
  - `package_ready`: context profile is within budget and has sufficient signals
  - `trim_required`: context exceeds budget tier; noise flags present; must trim before handoff
  - `augment_required`: missing required signals; must enrich before handoff
  - `contamination_flag`: contamination flags detected; must sanitize before handoff
  - `budget_exceeded`: token estimate exceeds ceiling; hard block on handoff
  - `handoff_blocked`: multiple issues; escalate to operator before proceeding
S3 — `packagingGuidance` field: advisory text for context trimming or enrichment
S4 — Mapping to VI2 `requestContextReadout` fields: `budgetTier`, `missingSignals`, `noiseFlags`, `contaminationFlags`
S5 — Boundary: advisory only; no prompt mutation; `runtimeExecutionAuthorized=false`
S6 — Source Verification Table

## Closure Checklist

- [x] Connector spec created with all required sections
- [x] `contextProfilePackagingAdvisoryType` with 6 values
- [x] `packagingGuidance` field documented
- [x] VI2 `requestContextReadout` field mapping present
- [x] `runtimeExecutionAuthorized=false` explicit
- [x] LH1 `Workflow GoClaw` trigger cited and closed
- [x] No code file in diff
- [x] Fast Lane audit PASS
- [x] Session continuity updated

## Return-To-Orchestrator Conditions

Stop if: `Workflow GoClaw` source value cannot be mapped to a doc-only advisory type; VI2 `requestContextReadout` fields cannot be cited without runtime claims; structural completeness gate fails with no clear fix.

## Claim Boundary

Doc-only connector spec. No prompt mutation, no runtime context injection,
no hosted readiness, no public release readiness.
