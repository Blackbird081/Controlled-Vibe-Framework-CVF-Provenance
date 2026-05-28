# CVF Work Order: W1 Workflow State-Machine Enforcement

Memory class: FULL_RECORD

Status: AUTHORIZED

docType: work_order

Date: 2026-05-24

Tranche: W1

Roadmap: `docs/roadmaps/CVF_WC_WORKFLOW_CHAIN_AND_PAIN_POINT_ROADMAP_2026-05-24.md`

GC-018: `docs/baselines/CVF_GC018_W1_WORKFLOW_STATE_MACHINE_ENFORCEMENT_2026-05-24.md`

---

## Purpose

Close WC-3 Candidate 1 with a thin runtime proof: existing workflow transition
metadata must be replayed as a state machine before route evidence claims a
workflow step completed.

## Agent Roles

| Role | Responsibility |
| --- | --- |
| Orchestrator | Keep W1 bounded to one selected workflow and commit after closure. |
| Legacy Source Extractor | Use CVF Edit and Human System Harness state-machine guidance without importing broad legacy architecture. |
| Implementer | Patch the existing workflow resolver and focused tests. |
| QA | Run focused tests, typecheck, live proof, and release gate. |
| Skeptic/Auditor | Reject overclaims and confirm no forbidden surfaces changed. |
| Safety/Boundary Owner | Confirm deferred reviewer gate cannot be bypassed by state replay. |

## Authority Chain

- Operator instruction: proceed through the WC-3 roadmap in priority order,
  commit after each part, and use live API-key proof where required.
- Roadmap:
  `docs/roadmaps/CVF_WC_WORKFLOW_CHAIN_AND_PAIN_POINT_ROADMAP_2026-05-24.md`
- WC-3 map:
  `docs/reference/CVF_LEGACY_HARVEST_SCAN_MAP_2026-05-24.md`
- WC-4 standard:
  `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`
- GC-018:
  `docs/baselines/CVF_GC018_W1_WORKFLOW_STATE_MACHINE_ENFORCEMENT_2026-05-24.md`

## Scope / Target / Owner Boundary

Allowed files:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/phase-e-workflow-binding.live.spec.ts`
- W1 baseline, work order, completion review
- WC roadmap/session/handoff progress updates

Forbidden files/classes:

- provider adapters and provider router semantics;
- governance evidence receipt envelope types;
- auth/RBAC;
- memory tiers or reinjection semantics;
- public-sync;
- new workflow queue, task runner, or multi-agent orchestration engine.

## Required First Reads

- `docs/reference/CVF_LEGACY_HARVEST_SCAN_MAP_2026-05-24.md`
- `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`
- `docs/baselines/CVF_GC018_W1_WORKFLOW_STATE_MACHINE_ENFORCEMENT_2026-05-24.md`
- `.private_reference/legacy/CVF Edit/CVF_EDIT_ANALYSIS.md`
- `.private_reference/legacy/CVF Edit/De_xuat.md`
- `.private_reference/legacy/CVF Edit/Review CVF.md`
- `.private_reference/legacy/CVF Edit/Review CVF_1.md`
- `.private_reference/legacy/CVF Edit/Review CVF_3.md`
- `.private_reference/legacy/CVF Edit/Review CVF_4.md`
- `.private_reference/legacy/CVF Edit/Review CVF_5.md`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow.product.create_product_brief.v1.json`

## Pre-Flight Checks

- Confirm WC-1/WC-2/WC-3/WC-4 are closed in the WC roadmap.
- Confirm this work order and GC-018 include the Knowledge Absorption
  Blind-Spot Control Block.
- Confirm the selected workflow is `app_builder_complete` /
  `workflow.product.create_product_brief.v1`.
- Confirm no provider adapter, receipt-envelope type, auth/RBAC, or memory
  tier file is required.
- Confirm live proof will follow V3 diagnostics if any run fails, times out,
  or returns empty output.

## Write Ownership

Implementation ownership:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/phase-e-workflow-binding.live.spec.ts`

Documentation ownership:

- W1 GC-018, work order, completion review
- WC roadmap status update
- active session state, front door, and handoff sync

## Knowledge Absorption Blind-Spot Control Block

- Standard read:
  `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`
- Source inventory:
  - `.private_reference/legacy/CVF Edit/` — 10 files
  - `.private_reference/legacy/CVF ADD/Human System Harness/` — 11 files
  - `.private_reference/legacy/CVF ADD/Agent Harnesses/` — 11 files
- Prior absorption evidence resolved:
  - `docs/reference/CVF_LEGACY_HARVEST_SCAN_MAP_2026-05-24.md`
  - `docs/reference/archive/CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md`
  - Phase E workflow-binding closure packets
- Detailed source files used:
  - CVF Edit state-machine review files listed in Required First Reads
  - Human System Harness phase-integrity files cited in GC-018
- Source families skipped:
  - memory, tool/MCP, benchmark, provider, and artifact-renderer candidates are
    deferred to later W-series tranches.
- File-level accepted value:
  - workflow enforcement must validate transitions and reject or defer invalid
    movement rather than relying on prose phases.
- Owner-surface normalization:
  - existing workflow resolver and execute-route workflow projection.
- Accept/defer/reject matrix:
  - ACCEPT_NOW: one selected-flow state replay.
  - DEFER_DEMAND_GATED: full workflow engine, rollback, queue, UI recovery.
  - REJECT_DIRECT: global workflow authority or new kernel law.
- Adversarial roles completed:
  - Implementer: local resolver projection is enough.
  - Skeptic/Auditor: no universal workflow-engine claim.
  - Product/Operator Advocate: prevents misleading completed-step evidence.
  - Safety/Boundary Owner: deferred reviewer gate remains unavailable.
- Thin proof target:
  - live Product Brief call shows step 5 is not completed while review is
    deferred.
- Blind-spot verdict: CLEAR

## Execution Plan

1. Add a state-machine projection to `workflow-resolver`.
2. Replay all configured steps by sequence.
3. Complete only reachable active transitions.
4. Mark configured deferred steps as deferred.
5. Mark active steps after a deferred predecessor as deferred/not completed.
6. Emit receipts only for completed traces with receipt ids.
7. Update route and live tests to assert the truthful projection.
8. Run focused tests, typecheck, live proof, and release gate.
9. File completion review, update roadmap/session/handoff, commit.

## Acceptance Criteria

- [ ] Product Brief workflow projection includes state-machine metadata.
- [ ] Step 4 reviewer gate is deferred and does not advance state.
- [ ] Step 5 receipt-emission is not reported as completed while
      `freeze_ready` is unreachable.
- [ ] Receipt emissions exist only for completed reachable steps.
- [ ] `/api/execute` audit payload includes the state-machine projection.
- [ ] Focused tests PASS.
- [ ] `cvf-web` TypeScript check PASS.
- [ ] Live Phase E workflow-binding proof PASS.
- [ ] Mandatory release gate PASS.
- [ ] Completion review, roadmap, session state, and handoff are updated.

## Evidence Requirements

- Focused workflow resolver and execute route tests PASS.
- `cvf-web` TypeScript check PASS.
- Live Phase E workflow-binding spec PASS with provider API key.
- Mandatory release gate PASS.
- Completion review includes state-machine decisions, receipt-emission count,
  receipt id/trace id when live proof is run, and claim boundary.

## Review Gate

Reject W1 pass if:

- step 5 is still reported `completed` while step 4 is deferred;
- receipt emissions include a step with `receiptId: null`;
- the governance evidence receipt envelope is modified;
- the implementation changes provider behavior;
- live proof is skipped when a governance behavior claim is made.

## Closure Checklist

- [ ] GC-018 and work order committed before runtime implementation.
- [ ] Resolver state-machine projection implemented.
- [ ] Focused unit/route tests updated and PASS.
- [ ] Live proof updated and PASS with secret-safe receipt data.
- [ ] TypeScript check PASS.
- [ ] Mandatory release gate PASS.
- [ ] Markdown/docs/session guards PASS.
- [ ] Completion review filed.
- [ ] WC roadmap/session/handoff updated.
- [ ] Final tranche commit created.

## Return Conditions

Return to orchestrator instead of closing if:

- the selected Product Brief workflow cannot be handled without changing the
  receipt envelope, provider adapters, auth/RBAC, or memory semantics;
- live proof fails and cannot be classified under the V3 diagnostic standard;
- route-level BLOCK is required to close W1 rather than projection-level
  enforcement;
- the implementation would require a new workflow engine or global phase
  authority.

## Operator Checkpoint

No additional operator checkpoint is required for projection-level W1 because
the operator instructed Codex to proceed through the roadmap and check only
after completion. A new checkpoint is required before widening W1 into
route-level invalid-transition blocking, new workflow runtime surfaces,
public-sync, or production claims.

## Claim Boundary

This work order authorizes only a bounded state-machine enforcement proof for
the existing Product Brief workflow binding. It does not authorize broad
workflow orchestration, autonomous execution, public capability claims,
production readiness, or freeze release.
