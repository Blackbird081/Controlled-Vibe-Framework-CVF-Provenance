# CVF Work Order — LHW15-T2 Workflow Resume/Recovery Proof Advisory Connector

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-05-30

---

## Purpose

Create a documentation-only connector spec mapping the `Agent Harnesses` legacy
family's remaining trigger value (workflow resume/recovery proof) to a new
advisory type `workflowResumeAdvisoryType` building on WR1's
`lastRestorableCheckpoint` surface.

Contract version: `cvf.workflowResumeRecoveryAdvisory.lhw15.t2.v1`

Closes LH1 `Agent Harnesses` trigger (line 150).

## Authority Chain

- LHW15 roadmap: `docs/roadmaps/CVF_LHW15_WORKFLOW_CONNECTOR_WAVE15_ROADMAP_2026-05-30.md`
- LHW15 GC-018: `docs/baselines/CVF_GC018_LHW15_WORKFLOW_CONNECTOR_WAVE15_2026-05-30.md`
- LH1 source: `docs/reference/archive/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md` line 150
- WR1 owner surface: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts`

## Scope

**Allowed:**
- `docs/reference/CVF_LHW15_T2_WORKFLOW_RESUME_RECOVERY_ADVISORY_CONNECTOR_SPEC_2026-05-30.md` (new)
- `docs/reviews/CVF_LHW15_T2_FAST_LANE_AUDIT_2026-05-30.md` (new)
- `docs/reviews/CVF_LHW15_T2_WORKFLOW_RESUME_RECOVERY_ADVISORY_COMPLETION_2026-05-30.md` (new)
- this work order (status update only)
- session continuity files

**Forbidden:** any code file, EXTENSIONS/ change, receipt envelope, public-sync.

## Pre-Dispatch Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| `Agent Harnesses` PARTIALLY_ABSORBED | `docs/reference/archive/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md` | line 150 | `Agent Harnesses` | LH1 Closeout Ledger CVF ADD section | ACCEPT |
| `lastRestorableCheckpoint` WR1 field | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts` | WR1 surface | `lastRestorableCheckpoint` | workflow recovery readout | ACCEPT |

New advisory types (doc-only):

| New symbol | Purpose | Runtime claim blocked? |
| --- | --- | --- |
| `workflowResumeAdvisoryType` | 6-value enum for resume state | Yes — advisory only |
| `resumptionPath` | Advisory for next safe step and evidence needed | Yes |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact | Verification | Status |
| --- | --- | --- | --- | --- |
| `workflowResumeAdvisoryType` (6 values) | Spec content | connector spec S2 | values enumerated | PASS |
| `resumptionPath` field | Spec content | connector spec S3 | field described | PASS |
| `runtimeExecutionAuthorized=false` | Invariants | connector spec S5 | explicit | PASS |
| LH1 `Agent Harnesses` trigger closed | Authority Chain | spec header | LH1 line 150 cited | PASS |
| No code file | Scope | diff | review confirms | PASS |

## Agent Roles

Implementer: write connector spec. Reviewer: verify advisory types, WR1 mapping, boundary. No self-review.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `docs/reference/archive/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md` — confirm `Agent Harnesses` at line 150

## Write Ownership

Implementer owns all new files listed in Allowed. Only Allowed files may be touched.

## Execution Plan

1. Read required first reads; confirm `Agent Harnesses` LH1 line 150.
2. Write connector spec with S1–S6 sections per Implementation Design below.
3. Write Fast Lane audit.
4. Write completion review.
5. Run governance gates.
6. Update session continuity; commit.

## Evidence Requirements

- Connector spec with `workflowResumeAdvisoryType` (6 values) and `resumptionPath`
- WR1 `lastRestorableCheckpoint` mapping present
- `runtimeExecutionAuthorized=false` explicit
- LH1 `Agent Harnesses` trigger cited (line 150)
- No code file in diff

## Acceptance Criteria

- [x] Connector spec complete with all required sections
- [x] `workflowResumeAdvisoryType` with 6 values
- [x] `resumptionPath` field documented
- [x] WR1 mapping present
- [x] `runtimeExecutionAuthorized=false` explicit
- [x] LH1 `Agent Harnesses` trigger cited and closed
- [x] No code file in diff

## Fail Conditions

- Advisory type enum missing or fewer than 6 values
- WR1 mapping absent
- `runtimeExecutionAuthorized` not explicitly `false`

## Review Gate

Connector spec complete; 6-value advisory type; WR1 mapping; `runtimeExecutionAuthorized=false`; no code file.

## Operator Checkpoint

operator.checkpoint.waiver: Operator authorized LHW15 directly 2026-05-30.

## Pre-Flight Checks

- [x] LHW15 GC-018 confirmed
- [x] `Agent Harnesses` LH1 line 150 disposition confirmed: PARTIALLY_ABSORBED
- [x] WR1 `lastRestorableCheckpoint` owner surface confirmed
- [x] Working tree clean

## Implementation Design

### Connector Spec Structure

S1 — Purpose and LH1 source citation (Agent Harnesses line 150, WR1 surface)
S2 — Advisory type enum:
  - `resume_from_checkpoint`: last restorable checkpoint exists; evidence sufficient
  - `restart_required`: no valid checkpoint; workflow must restart from intake
  - `incomplete_evidence`: checkpoint exists but evidence receipts are missing
  - `approval_gate_pending`: workflow paused at reviewer gate; awaiting approval
  - `escalation_required`: deadlock detected; Orchestrator intervention needed
  - `no_recovery_path`: terminal failure; human intervention required
S3 — `resumptionPath` field: describes next safe step and required evidence
S4 — Mapping to WR1 `lastRestorableCheckpoint` and `recoveryAction` fields
S5 — Boundary: advisory only; no workflow engine; `runtimeExecutionAuthorized=false`
S6 — Source Verification Table

## Closure Checklist

- [x] Connector spec created with all required sections
- [x] `workflowResumeAdvisoryType` with 6 values
- [x] `resumptionPath` field documented
- [x] WR1 `lastRestorableCheckpoint` mapping present
- [x] `runtimeExecutionAuthorized=false` explicit
- [x] LH1 `Agent Harnesses` trigger cited and closed
- [x] No code file in diff
- [x] Fast Lane audit PASS
- [x] Session continuity updated

## Return-To-Orchestrator Conditions

Stop if: `Agent Harnesses` source value cannot be mapped to a doc-only advisory type; WR1 `lastRestorableCheckpoint` cannot be cited without runtime claims; structural completeness gate fails with no clear fix.

## Claim Boundary

Doc-only connector spec. No workflow engine execution, no runtime resume,
no hosted readiness, no public release readiness.
