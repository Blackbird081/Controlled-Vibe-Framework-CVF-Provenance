# CVF Work Order — LHW2-T2 Workflow Recovery Action Packet Connector

Memory class: FULL_RECORD

Status: OPEN

docType: work_order

Date: 2026-05-27

---

## Purpose

Implement LHW2-T2: a connector spec turning each WR1 transition class into a
concrete MA1-compatible recovery action packet. Closes the gap where WR1 classifies
workflow transitions (escalate, hold, advance, no-transition) but provides no
standard packet template for how those outcomes are communicated to the
Orchestrator or next role agent.

Documentation-only tranche. No source code, runtime module, route, or provider
behavior is changed.

## Authority Chain

- LHW2 roadmap: `docs/roadmaps/CVF_LHW2_WORKFLOW_CONNECTOR_COMPLETION_ROADMAP_2026-05-27.md`
- Fast Lane audit: `docs/reviews/CVF_LHW2_T2_FAST_LANE_AUDIT_2026-05-27.md` → FAST_LANE_READY
- LH1 ledger (`Agent Harnesses` trigger): `docs/reference/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
- WR1: `docs/reviews/CVF_WR1_WORKFLOW_RECOVERY_STATE_PROOF_COMPLETION_2026-05-25.md`
- W1: `docs/reviews/CVF_W1_WORKFLOW_STATE_MACHINE_ENFORCEMENT_COMPLETION_2026-05-24.md`
- LHW1-T2 spec: `docs/reference/CVF_LHW1_WORKFLOW_CHAIN_STATE_CONNECTOR_SPEC_2026-05-27.md`
- MA1 standard: `docs/reference/CVF_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_STANDARD_2026-05-26.md`
  (read full sections 0–9)

## Gate Condition — CHECK FIRST

Confirm T1 is `CLOSED_PASS` by reading:
`docs/reviews/CVF_LHW2_T1_*_COMPLETION_2026-05-27.md`

If T1 is not CLOSED_PASS, stop and report to Orchestrator.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. T1 completion (understand shape T2 must extend)
4. `docs/reviews/CVF_WR1_WORKFLOW_RECOVERY_STATE_PROOF_COMPLETION_2026-05-25.md`
   — confirm the 4 WR1 transition classes, `lastRestorableCheckpoint` logic,
   and `escalate_to_governance` / `hold_for_reviewer_gate` mappings
5. `docs/reference/CVF_LHW1_WORKFLOW_CHAIN_STATE_CONNECTOR_SPEC_2026-05-27.md`
   — S5 recovery state binding; S7 boundary table row for recovery checkpoint
6. `docs/reference/CVF_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_STANDARD_2026-05-26.md`
   — sections 0–9; understand which MA1 sections are relevant for recovery packets
7. `docs/reviews/CVF_W1_WORKFLOW_STATE_MACHINE_ENFORCEMENT_COMPLETION_2026-05-24.md`
   — confirm W1 phase vocabulary used verbatim

## Scope

**Allowed:**

- `docs/reference/CVF_LHW2_WORKFLOW_RECOVERY_ACTION_PACKET_CONNECTOR_SPEC_2026-05-27.md`
  (new — primary deliverable)
- this work order (status update only)
- session continuity files

**Forbidden:** `EXTENSIONS/` (any file), `governance/contracts/` (any file),
`src/lib/workflows/` (any file), any `.ts`/`.tsx`/`.js`/`.py` file, receipt
envelope schema, public-sync repo. Async worker runtime, broad workflow
orchestration, and route-level enforcement remain blocked.

## Deliverable — Connector Spec

File: `docs/reference/CVF_LHW2_WORKFLOW_RECOVERY_ACTION_PACKET_CONNECTOR_SPEC_2026-05-27.md`

Required sections:

### S1 — Purpose and claim boundary

- State what the connector is: a normative doc mapping WR1 transition classes
  to MA1-compatible recovery action packet templates.
- State what it is not: not a WR1 runtime extension; not a new workflow
  orchestration engine; not route-level enforcement.
- Explicit statement: "WR1 `workflowRecoveryReadout` is the runtime authority
  for transition classification; this connector extends that pattern to a
  standard recovery packet shape usable by Orchestrator and role agents."

### S2 — WR1 transition class to recovery packet mapping

One packet template per WR1 transition class. For each class:

- **`no_requested_transition`** — advisory hold packet
  - Packet type, when issued, MA1 sections R/O/N/A, minimum fields
- **`configured_deferred_gate`** — reviewer gate hold packet
  - Packet type, when issued, MA1 sections R/O/N/A, minimum fields,
    which role must respond, `hold_for_reviewer_gate` action binding
- **`valid_from_current_state`** — advance packet
  - Packet type, when issued, MA1 sections R/O/N/A, minimum fields
- **`invalid_from_current_state`** — escalate-to-governance packet
  - Packet type, when issued, MA1 sections R/O/N/A, minimum fields,
    `escalate_to_governance` action binding, stop condition

For MA1 section references, use section numbers from the canonical standard
(## 0 through ## 9). Mark each R (Required), O (Optional), or N/A.

### S3 — lastRestorableCheckpoint to restore packet

Prose description: how `lastRestorableCheckpoint` (the most recently completed
reachable W1 phase) feeds into a recovery packet's `## 4 Input Package` field.

- What phase name / token is used as the restore point
- What evidence must be present before a restore can begin
- What the Orchestrator must confirm before accepting the packet

### S4 — Dissent and escalation handoff rules

Cover in prose:

- When `invalid_from_current_state` triggers the escalate packet: what the
  receiving Orchestrator must do next (do not advance; log; seek governance).
- When `configured_deferred_gate` triggers the hold packet: which role holds the
  next action token, and how the gate is lifted (Reviewer response via MA1
  `## 9 Return Protocol`).
- Minimum evidence Auditor must confirm before an escalation packet is accepted.

### S5 — Runtime-enforcement boundary table

| Behavior | Current status | Future path |
| --- | --- | --- |
| WR1 transition classification | Runtime (workflow-resolver.ts) | Stable |
| W1 phase state projection | Runtime (workflow-resolver.ts) | Stable |
| Recovery packet structure | Document-only | Future: MA1 packet validator |
| Restore point enforcement | Document-only | Future: route-level checkpoint restore |
| Escalation routing | Document-only | Future: governance escalation queue |
| Reviewer gate lift | Document-only | Future: reviewer gate signal in /api/execute |

Do not label any row "Runtime" unless a closed PASS tranche implements it.

## Pre-Flight

- [ ] T1 CLOSED_PASS confirmed
- [ ] Working tree clean
- [ ] All required first reads done
- [ ] WR1 four transition classes confirmed from WR1 completion review

## Agent Roles

Implementer writes spec (S1–S5) opening with the T1 foundation. Reviewer checks
WR1 transition class names verbatim, MA1 section refs correct, boundary table
honest, no runtime claim added, no `.ts` file touched. Auditor confirms T1 gate
documented, Agent Harnesses LH1 trigger recorded, no async worker or orchestration
runtime claim. No self-review.

## Write Ownership

Implementer owns all new files. No file outside the Allowed list may be modified.

## Execution Plan

1. Confirm T1 gate.
2. Read all required first reads.
3. Draft spec (S1–S5).
4. Confirm no code file staged.
5. Reviewer perspective — record result.
6. Update session continuity (`lhw2_t2_complete`).
7. Commit: `docs(lhw2-t2): add workflow recovery action packet connector spec`.
8. Write completion review; include T3 gate answer (see below).

Spec size guard: < 250 lines. Trim S3/S4 prose if approaching 220 lines.

## Review Gate

Before committing: Reviewer perspective completed; all WR1 class names verbatim;
MA1 section refs correct; boundary table honest; no code file in diff.

## Acceptance Criteria

- [ ] Spec with all 5 sections created
- [ ] All 4 WR1 transition classes mapped to distinct packet templates
- [ ] MA1 sections marked R/O/N/A per packet type
- [ ] `lastRestorableCheckpoint` to restore packet mapping present
- [ ] Dissent and escalation handoff rules documented
- [ ] Runtime boundary table present and honest
- [ ] No code file in diff
- [ ] Session continuity updated

## T3 Gate Output (required in completion review)

Answer explicitly: "Was a concrete tool approval handoff gap identified during
T2 work?"

- YES → describe gap in one sentence; T3 proceeds.
- NO → "No gap found. T3 proceeds per roadmap rationale."
  (T3 proceeds regardless — this output is informational.)

## Evidence Requirements

- Spec at target path with all 5 sections present
- All 4 WR1 transition classes mapped to distinct packet templates in S2
- MA1 sections marked R/O/N/A per packet type using canonical section numbers
- `lastRestorableCheckpoint` to restore packet mapping present in S3
- Dissent and escalation handoff rules documented in S4
- S5 boundary table present; no doc-only row labeled Runtime
- No `.ts`/`.tsx`/`.js`/`.py` file in `git diff --name-only`
- Session continuity updated to `lhw2_t2_complete`
- Completion review written with T3 gate answer

## Closure Checklist

- [ ] T1 gate confirmed documented
- [ ] Spec created with all 5 sections
- [ ] All 4 WR1 transition classes mapped with MA1 sections R/O/N/A
- [ ] `lastRestorableCheckpoint` restore mapping present
- [ ] S5 boundary table honest; no doc-only row labeled Runtime
- [ ] No code file in diff
- [ ] Session continuity updated
- [ ] Completion review with T3 gate answer written

## Return-To-Orchestrator Conditions

Stop and report to Orchestrator if:

- T1 gate is not CLOSED_PASS;
- any required first read file is missing or unreadable;
- writing the connector requires a new WR1 transition class not in the existing
  4-class vocabulary;
- writing the connector requires modifying `workflow-resolver.ts`;
- spec exceeds 250 lines before S4 is complete.

## Operator Checkpoint

operator.checkpoint.waiver: Low-risk documentation-only tranche gated by T1
CLOSED_PASS pre-condition; no operator checkpoint required unless a conflict
with WR1 TypeScript vocabulary is discovered during implementation.

## Claim Boundary

LHW2-T2 produces a documentation artifact. It does not claim WR1/W1 runtime
extension, new workflow orchestration engine, route-level enforcement, async
worker runtime, memory reinjection, receipt envelope extension, provider behavior,
hosted readiness, production readiness, or public release readiness.
