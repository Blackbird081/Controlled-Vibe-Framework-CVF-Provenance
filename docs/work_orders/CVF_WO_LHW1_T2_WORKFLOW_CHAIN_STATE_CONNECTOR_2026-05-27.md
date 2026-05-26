# CVF Work Order — LHW1-T2 Workflow Chain State Connector

Memory class: FULL_RECORD

Status: FAST_LANE_READY

docType: work_order

Date: 2026-05-27

---

## Purpose

Implement LHW1-T2: a state connector binding the CVF five-phase workflow
chain (Intake → Design → Build → Review → Freeze) to role assignments,
evidence receipts, recovery states, and MA1-compatible transfer packet fields.

Documentation-only tranche. No source code, runtime module, route, or
provider behavior is changed.

## Authority Chain

- Operator authorized LHW1 roadmap on 2026-05-27.
- Roadmap: `docs/roadmaps/CVF_LHW1_LEGACY_WORKFLOW_CONNECTOR_ABSORPTION_ROADMAP_2026-05-27.md`
- Fast Lane audit: `docs/reviews/CVF_LHW1_T2_FAST_LANE_AUDIT_2026-05-27.md` → FAST_LANE_READY
- T1 work order: `docs/work_orders/CVF_WO_LHW1_T1_PRODUCT_SKILL_PACK_WORKFLOW_CONNECTOR_2026-05-27.md`
- W1: `docs/reviews/CVF_W1_WORKFLOW_STATE_MACHINE_ENFORCEMENT_COMPLETION_2026-05-24.md`
- WR1: `docs/reviews/CVF_WR1_WORKFLOW_RECOVERY_STATE_PROOF_COMPLETION_2026-05-25.md`
- MA1: `docs/reference/CVF_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_STANDARD_2026-05-26.md`

## Gate Condition — CHECK FIRST

Confirm T1 is `CLOSED_PASS` by reading:
`docs/reviews/CVF_LHW1_T1_PRODUCT_SKILL_PACK_WORKFLOW_CONNECTOR_COMPLETION_2026-05-27.md`

If T1 is not CLOSED_PASS, stop and report to Orchestrator.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. T1 completion + T1 connector spec (understand shape T2 must extend)
4. `docs/reviews/CVF_W1_WORKFLOW_STATE_MACHINE_ENFORCEMENT_COMPLETION_2026-05-24.md`
5. `docs/reviews/CVF_WR1_WORKFLOW_RECOVERY_STATE_PROOF_COMPLETION_2026-05-25.md`
6. `docs/reference/CVF_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_STANDARD_2026-05-26.md`
   (read full sections 0–9)
7. `docs/reference/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
   (CVF Edit / Human System Harness / Agent Harnesses dispositions)

## Scope

**Allowed:** `docs/reference/CVF_LHW1_WORKFLOW_CHAIN_STATE_CONNECTOR_SPEC_2026-05-27.md`
(new); this work order (status update); session continuity files.

**Forbidden:** any file in `EXTENSIONS/`, `governance/contracts/`, any
`.ts`/`.tsx`/`.js`/`.py` file, receipt envelope schema, public-sync repo.

## Deliverable — State connector spec

File: `docs/reference/CVF_LHW1_WORKFLOW_CHAIN_STATE_CONNECTOR_SPEC_2026-05-27.md`

Required sections:

### S1 — Purpose and claim boundary

State what the connector is (normative doc binding phases to roles +
receipts + recovery) and what it is not (not W1/WR1 runtime; not a role
scheduler). Explicit statement: "W1 `workflow-resolver.ts` and WR1
`workflowRecoveryReadout` are the runtime authority; this connector
extends that pattern to a cross-workflow standard."

### S2 — Phase-to-role assignment table

Use W1 vocabulary verbatim. No invented tokens.

| Phase token | Phase name | Primary role | Supporting roles | Evidence to enter |
|---|---|---|---|---|
| `intake_pending` | Intake | Orchestrator | Non-coder submitter | Request present; context profile readiness confirmed |
| `design_ready` | Design | Implementer | Orchestrator | Intake package complete; skill pack selected |
| `build_running` | Build | Implementer | — | Design spec confirmed; execution policy applied |
| `review_pending` | Review | Reviewer | Auditor | Build output present; receipt issued |
| `freeze_ready` | Freeze | Orchestrator + Auditor | Reviewer | Review PASS; all acceptance criteria met |
| `completed` | Completed | (closed) | — | Freeze authorized; receipt final |

### S3 — MA1-compatible role transfer packet fields

Reference MA1 section numbers from the canonical standard — do not
re-define the MA1 structure. For each phase transition, note which
MA1 sections are Required (R), Optional (O), or N/A:

- `## 0 Surface Fidelity Gate`, `## 1 Authority Chain`,
  `## 2 Transfer Objective`, `## 4 Input Package`,
  `## 6 Acceptance Criteria`, `## 8 Stop Conditions`,
  `## 9 Return Protocol`

### S4 — Dissent and review handoff requirements

Cover in prose:

- Reviewer dissent at `review_pending`: what to record + which MA1
  field captures it + Orchestrator next action.
- Reviewer gate deferred (WR1 pattern): defer to WR1
  `configured_deferred_gate`; do not redefine recovery logic.
- Auditor challenge at `freeze_ready`: minimum evidence Auditor must check.

### S5 — Recovery state binding

Map each WR1 transition class to the phase table:

- `invalid_from_current_state` → `escalate_to_governance` (role must not proceed)
- `lastRestorableCheckpoint` rule: most recently completed reachable
  phase is the restore point.

### S6 — Evidence receipt binding

Minimum receipt fields required at each phase boundary. Reference
existing `GovernanceEvidenceReceipt` field names only (no new envelope
fields). `canReinject: false` restated explicitly.

### S7 — Runtime-enforcement boundary table

| Behavior | Current status | Future path |
|---|---|---|
| Phase state projection | Runtime (W1) | Stable |
| Recovery checkpoint readout | Runtime (WR1) | Stable |
| Role assignment enforcement | Document-only | Future: role-gate in `/api/execute` |
| MA1 packet validation | Document-only | Future: MA1 schema validator |
| Dissent recording | Document-only | Future: dissent field in GovEvidenceReceipt |
| Cross-workflow phase binding | Document-only | Future: multi-workflow state machine |

Do not label any row "Runtime" unless a closed PASS tranche implements it.

## Pre-Flight

- [ ] T1 CLOSED_PASS confirmed
- [ ] working tree clean
- [ ] all required first reads done
- [ ] W1 phase vocabulary confirmed

## Agent Roles

Implementer writes; Reviewer checks phase vocab, MA1 refs, boundary table
honesty, no `.ts` file touched; Auditor confirms T1 gate +
`canReinject: false` + no new runtime claim. No self-review.

## Write Ownership

Implementer owns all new files. Reviewer and Auditor hold read + review
rights only. No file outside the Allowed list in the Scope section may be
modified by any role.

## Execution Plan

1. Confirm T1 gate.
2. Read required files.
3. Draft spec (S1–S7).
4. Confirm no code file staged.
5. Reviewer perspective — record result.
6. Update session continuity (`lhw1_t2_complete`).
7. Commit: `docs(lhw1-t2): add workflow chain state connector spec`.
8. Write completion review; include T3 gate answer (see below).

## Review Gate

Before committing: Reviewer perspective completed; all Acceptance Criteria
checked; `canReinject: false` confirmed present; no code file in diff.

## Evidence Requirements

Spec at target path; all 7 sections present; W1 phase tokens verbatim;
MA1 section refs correct; runtime boundary table honest;
`canReinject: false` explicit; no code file in diff;
completion review includes T3 gate answer.

File size guard: spec < 300 lines. Split at 250 if needed
(sections 1-5 / sections 6-7 + tables).

## Acceptance Criteria

- [ ] Spec with all 7 sections created
- [ ] Phase table uses W1 vocabulary verbatim
- [ ] MA1 fields per phase (R/O/N/A)
- [ ] Dissent + deferred-gate handling documented
- [ ] WR1 recovery vocabulary cross-referenced
- [ ] Runtime boundary table present
- [ ] `canReinject: false` explicit
- [ ] No code file in diff
- [ ] Session continuity updated
- [ ] Completion review with T3 gate answer

## Closure Checklist

- [ ] State connector spec created with all 7 sections
- [ ] Phase table uses W1 vocabulary verbatim
- [ ] `canReinject: false` explicit
- [ ] No code file in diff
- [ ] Session continuity updated
- [ ] Completion review with T3 gate answer written

## Operator Checkpoint

operator.checkpoint.waiver: Low-risk documentation-only tranche gated by
T1 CLOSED_PASS pre-condition; no operator checkpoint required unless a
conflict with W1/WR1 TypeScript is discovered during implementation.

## T3 Gate Output (required in completion review)

Answer explicitly: "Was a concrete context gap identified during T2 work?"

- YES → describe gap in one sentence; T3 may proceed.
- NO → "No gap found. T3 is deferred."

## Return-To-Orchestrator Conditions

- T1 not CLOSED_PASS
- Connector writing requires modifying W1/WR1 TypeScript
- Phase token outside W1 vocabulary needed
- MA1 structure conflicts with T2 role handoff
- Spec exceeds 300 lines before S5 complete

## Claim Boundary

LHW1-T2 is a documentation artifact. It does not claim runtime phase
enforcement, MA1 packet runtime validation, dissent receipt implementation,
multi-workflow state machine runtime, memory reinjection, hosted readiness,
production readiness, or public release readiness.
