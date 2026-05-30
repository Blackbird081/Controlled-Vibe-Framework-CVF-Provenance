# CVF Work Order: WC-1 Workflow Chain Proof

Memory class: FULL_RECORD

Status: AUTHORIZED

docType: work_order

Date: 2026-05-24

Tranche: WC-1

Roadmap: `docs/roadmaps/CVF_WC_WORKFLOW_CHAIN_AND_PAIN_POINT_ROADMAP_2026-05-24.md`

---

## Purpose

Prove the existing CVF workflow chain with live evidence: turn 1 writes
summary-only durable memory after governed execution, and turn 2 reads that
prior memory through the route.

## Scope / Target / Owner Boundary

Allowed:

- WC-1 probe script.
- WC-1 governance docs and roadmap status update.
- Session/handoff updates after closure.

Forbidden:

- `/api/execute` route behavior changes.
- Provider adapter changes.
- Receipt-envelope schema changes.
- New memory tier or `canReinject=true`.
- Hosted/cloud persistence claims.

## Authority Chain

- GC-018:
  `docs/baselines/CVF_GC018_WC1_WORKFLOW_CHAIN_PROOF_2026-05-24.md`
- Roadmap:
  `docs/roadmaps/CVF_WC_WORKFLOW_CHAIN_AND_PAIN_POINT_ROADMAP_2026-05-24.md`

## Agent Roles

| Role | Responsibility |
| --- | --- |
| Orchestrator | Keep WC-1 bounded and sequenced before WC-3. |
| Implementer | Add the live probe script. |
| QA | Run probe, typecheck, and release gate. |
| Governance Reviewer | Confirm receipt-based proof and no overclaim. |
| Release Manager | File closure and update session routing. |

## Required First Reads

- `docs/roadmaps/CVF_WC_WORKFLOW_CHAIN_AND_PAIN_POINT_ROADMAP_2026-05-24.md`
- `docs/reviews/CVF_R2_EXECUTE_ROUTE_DURABLE_MEMORY_WIRING_COMPLETION_2026-05-24.md`
- `docs/reviews/CVF_S1_DURABLE_MEMORY_WRITE_ROUTE_COMPLETION_2026-05-24.md`
- `scripts/run_cvf_r2_durable_memory_route_live_probe.mjs`
- `scripts/run_cvf_s1_durable_memory_write_route_live_probe.mjs`

## Pre-Flight Checks

- Confirm active session gate is clean.
- Confirm WC-2 is closed.
- Confirm live keys are loaded from environment or `.env.local`.
- Confirm proof checks receipts, not only model output.

## Write Ownership

Allowed files:

- `scripts/run_cvf_wc1_workflow_chain_probe.mjs`
- WC-1 baseline, work order, completion review
- WC roadmap/session/handoff status updates

Forbidden files:

- Runtime route files
- Provider adapters
- Receipt-envelope type files
- Public claims beyond bounded evidence summary

## Execution Plan

1. Create the WC-1 live probe script.
2. Start local CVF web with a temporary durable-memory store.
3. Send turn 1 signed `/api/execute` request with durable memory write enabled.
4. Send turn 2 signed `/api/execute` request with durable memory read enabled.
5. Assert the turn 2 read receipt contains the turn 1 memory id.
6. Verify secret hygiene and bounded memory flags.
7. File closure and session updates.

## Evidence Requirements

- Live probe PASS JSON with receipt ids, trace ids, and memory ids.
- `cvf-web` typecheck PASS.
- Mandatory release gate PASS.
- Completion review with Evidence Trace.

## Review Gate

Reviewer must reject WC-1 pass if:

- turn 2 does not include the written memory id in read receipt;
- any durable receipt has `rawMemoryReleased` other than `false`;
- any durable receipt has `canReinject` other than `false`;
- the claim relies only on model output.

## Closure Checklist

- [ ] Probe script added.
- [ ] Live probe PASS.
- [ ] Typecheck PASS.
- [ ] Release gate PASS.
- [ ] Completion review filed.
- [ ] Session/handoff updated.

## Return-To-Orchestrator Conditions

Return blocked if live provider access is unavailable, route execution fails
before provider dispatch, durable write/read receipts are missing, or proving
the chain requires route/provider/runtime changes.

## Operator Checkpoint

No additional checkpoint is required for WC-1 because the operator explicitly
authorized opening implementation. WC-3 still requires separate authorization
after WC-1 closes.

## Acceptance Criteria

- [ ] Turn 1 writes durable memory with receipt evidence.
- [ ] Turn 2 reads the same memory id with receipt evidence.
- [ ] `rawMemoryReleased=false` and `canReinject=false` are preserved.
- [ ] No raw API keys or request headers are printed.

## Claim Boundary

This work order authorizes only the bounded WC-1 live workflow-chain proof. It
does not authorize WC-3, W-series implementation, hosted/cloud persistence,
autonomous memory behavior, provider/runtime changes, production readiness, or
freeze release.
