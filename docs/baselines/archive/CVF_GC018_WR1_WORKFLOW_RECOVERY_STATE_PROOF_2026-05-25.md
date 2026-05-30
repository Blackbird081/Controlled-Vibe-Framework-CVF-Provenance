# CVF GC-018 WR1 Workflow Recovery State Proof

Memory class: SUMMARY_RECORD

Status: AUTHORIZED_WR1_WORKFLOW_RECOVERY_STATE_PROOF

docType: baseline

Date: 2026-05-25

---

## Purpose

Authorize WR1 as a bounded workflow recovery/readout tranche after W1 and CB1.

The goal is to absorb the next LH1 candidate: checkpoint and recovery discipline
from Agent Harnesses, async/boundary lifecycle lessons from deepagents, and CVF
Edit runtime enforceability concerns into one existing Product Brief workflow
projection.

## Scope / Target / Owner Boundary

Owner surface:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.test.ts`

Allowed:

- deterministic workflow recovery/readout helper;
- recovery checkpoint summary from existing state-machine decisions;
- invalid transition classification for one Product Brief workflow;
- tests for checkpoint restore, invalid transition, and configured reviewer
  hold.

Forbidden:

- route-level invalid-transition `BLOCK`;
- broad workflow engine;
- provider/API calls;
- `/api/execute` behavior changes beyond existing projection data flow;
- receipt-envelope changes;
- memory, MCP, database, or tool execution;
- public-sync, hosted readiness, production readiness, or freeze release.

## Source / Predecessor Evidence

- `docs/reference/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
- `docs/reviews/CVF_W1_WORKFLOW_STATE_MACHINE_ENFORCEMENT_COMPLETION_2026-05-24.md`
- `.private_reference/legacy/CVF ADD/Agent Harnesses/CVF_CHECKPOINT_AND_RECOVERY_PROTOCOL.md`
- `.private_reference/legacy/CVF ADD/Agent Harnesses/CVF_EXECUTION_STATE_RESTORE_SPEC.md`
- `.private_reference/legacy/CVF ADD/Agent Harnesses/CVF_SESSION_VALIDATION_GATE_SPEC.md`
- `.private_reference/legacy/CVF ADD/deepagents/CVF_ASYNC_WORK_TICKET_PROTOCOL.md`
- `.private_reference/legacy/CVF ADD/deepagents/CVF_SUBAGENT_EXECUTION_BOUNDARY.md`
- `.private_reference/legacy/CVF Edit/CVF_EDIT_ANALYSIS.md`
- `.private_reference/legacy/CVF Edit/Review CVF_3.md`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts`

## Decision / Baseline / Proposed Tranche

Decision: proceed with WR1 as local deterministic workflow recovery/readout
only.

Baseline:

- W1 emits `cvf.workflowStateMachineProjection.v1` for Product Brief.
- W1 intentionally did not add route-level invalid-transition blocking or
  recovery orchestration.

Proposed output:

- `cvf.workflowRecoveryReadout.wr1.v1`;
- last restorable checkpoint from completed reachable steps;
- invalid requested transition classification;
- recovery action: `resume_from_checkpoint`, `hold_for_reviewer_gate`,
  `escalate_to_governance`, or `request_human_review`;
- tests proving the readout.

## Knowledge Absorption Blind-Spot Control Block

- Standard read:
  `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`
- Source inventory:
  - Agent Harnesses - 11 files, selected 3 recovery/session files
  - deepagents - 8 files, selected 2 lifecycle/boundary files
  - CVF Edit - 10 files, selected 2 runtime enforceability files
- Prior absorption evidence resolved:
  - W1 completion
  - LH1 closeout ledger
  - WC-3 scan map
- Detailed source files used:
  - `CVF_CHECKPOINT_AND_RECOVERY_PROTOCOL.md`
  - `CVF_EXECUTION_STATE_RESTORE_SPEC.md`
  - `CVF_SESSION_VALIDATION_GATE_SPEC.md`
  - `CVF_ASYNC_WORK_TICKET_PROTOCOL.md`
  - `CVF_SUBAGENT_EXECUTION_BOUNDARY.md`
  - `CVF_EDIT_ANALYSIS.md`
  - `Review CVF_3.md`
- Source families skipped:
  - tool/MCP/provider/external skill families; WR1 is workflow-only.
- File-level accepted value:
  - no recovery without checkpoint;
  - no forward progress after failed validation;
  - missing runtime state blocks restoration;
  - invalid transitions require hold/escalation;
  - worker/subagent patterns remain subordinate and non-authorizing.
- Owner-surface normalization:
  - accepted value maps into existing `workflow-resolver.ts` projection/readout,
    not a new runtime engine.
- Accept/defer/reject matrix:
  - ACCEPT_NOW: local recovery readout and invalid-transition classification.
  - DEFER_DEMAND_GATED: route-level blocking, UI recovery, worker tickets,
    async runtime, and global workflow engine.
  - REJECT_DIRECT: autonomous workers, self-authorizing tickets, or policy
    bypass through workflow recovery.
- Adversarial roles completed:
  - Implementer: smallest proof is a resolver helper and tests.
  - Skeptic/Auditor: do not imply route enforcement or recovery orchestration.
  - Product/Operator Advocate: readout should tell future agents why they must
    stop at reviewer gate instead of pushing to receipt/freeze.
  - Safety/Boundary Owner: no execution authority opens.
- Thin proof target:
  - Product Brief projection can report checkpoint, invalid transition, and
    recovery action.
- Blind-spot verdict: CLEAR.

## Evidence / Required Evidence / Verification

Required:

- focused workflow resolver tests PASS;
- cvf-web TypeScript check PASS;
- active state/handoff guards PASS.

Live proof is not required. WR1 does not assert provider, route-level blocking,
or live governance behavior.

## Claim Boundary / Approval Gate

WR1 may claim only deterministic local workflow recovery/readout for one Product
Brief workflow projection. It does not claim route-level invalid-transition
blocking, recovery orchestration, broad workflow engine, provider behavior,
receipt-envelope semantics, hosted readiness, production readiness, public
release readiness, or freeze release.
