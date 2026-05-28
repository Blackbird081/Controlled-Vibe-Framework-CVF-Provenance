# GC-018: W1 Workflow State-Machine Enforcement

Memory class: FULL_RECORD

Status: AUTHORIZED

docType: baseline

Date: 2026-05-24

Roadmap: `docs/roadmaps/CVF_WC_WORKFLOW_CHAIN_AND_PAIN_POINT_ROADMAP_2026-05-24.md`

Work Order: `docs/work_orders/CVF_WO_W1_WORKFLOW_STATE_MACHINE_ENFORCEMENT_2026-05-24.md`

---

## Purpose

Authorize the first W-series implementation drawn from WC-3 Candidate 1:
turn the existing Product Brief workflow binding into a bounded runtime
state-machine projection so workflow steps cannot be reported as completed when
their predecessor state has not been reached.

## Scope / Target / Owner Boundary

In scope:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.test.ts`
- existing `/api/execute` workflow-binding response and audit payload tests
- existing Phase E workflow-binding live spec
- W1 docs, review, and session handoff updates

Out of scope:

- new workflow engine or queue;
- new provider behavior, provider adapters, or model routing;
- new receipt-envelope fields;
- new role taxonomy, auth/RBAC, planner/worker orchestration, or job system;
- raw memory reinjection, `canReinject=true`, hosted/cloud persistence;
- public-sync or production-readiness claims.

Owner surface: existing `cvf-web` workflow binding and execute-route audit
projection. The tranche may add route response metadata inside the existing
workflow-execution projection, but it must not alter the governance evidence
receipt envelope.

## Depth Audit

Depth score: 9/10.

Rationale:

- WC-3 ranks workflow/state-machine enforcement as the highest-value next
  candidate because it directly addresses the operator's workflow-chain
  diagnosis.
- The current Product Brief binding already contains explicit states,
  transitions, and a deferred reviewer gate, but the resolver still marks the
  later receipt-emission step completed even though `freeze_ready` is not
  reachable while the reviewer gate is deferred.
- A thin implementation can prove runtime transition enforcement on one
  existing workflow without creating a new engine.

## Source / Predecessor Evidence

- WC roadmap:
  `docs/roadmaps/CVF_WC_WORKFLOW_CHAIN_AND_PAIN_POINT_ROADMAP_2026-05-24.md`
- WC-3 map:
  `docs/reference/CVF_LEGACY_HARVEST_SCAN_MAP_2026-05-24.md`
- WC-4 blind-spot standard:
  `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`
- Existing Phase E workflow binding:
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow.product.create_product_brief.v1.json`
- Existing resolver:
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts`
- Legacy state-machine source files listed in the Control Block below.

## Decision / Baseline / Proposed Tranche

Decision: continue with W1 as the first W-series implementation tranche.

Baseline: Product Brief already has transition metadata and route-level workflow
projection evidence, but the current projection can report a later active step
as completed even when the deferred reviewer gate prevents its predecessor
state from being reached.

Proposed tranche: add bounded state-machine replay to the existing workflow
projection and prove it on the Product Brief selected flow.

## Knowledge Absorption Blind-Spot Control Block

- Standard read:
  `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`
- Source inventory:
  - `.private_reference/legacy/CVF Edit/` — 10 files
  - `.private_reference/legacy/CVF ADD/Human System Harness/` — 11 files
  - `.private_reference/legacy/CVF ADD/Agent Harnesses/` — 11 files
  - active runtime files under `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/`
- Prior absorption evidence resolved:
  - `docs/reference/CVF_LEGACY_HARVEST_SCAN_MAP_2026-05-24.md`
  - `docs/reference/archive/CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md`
  - `docs/reviews/archive/CVF_LEGACY_SPEC_ABSORPTION_BLINDSPOT_CODEX_REVIEW_2026-05-23.md`
  - `docs/reviews/archive/CVF_PHASE_E_E3_WORKFLOW_BINDING_COMPLETION_2026-05-18.md`
  - `docs/reviews/archive/CVF_PHASE_E_E4_WORKFLOW_EXECUTE_WIRE_COMPLETION_2026-05-18.md`
- Detailed source files used:
  - `.private_reference/legacy/CVF Edit/CVF_EDIT_ANALYSIS.md`
  - `.private_reference/legacy/CVF Edit/De_xuat.md`
  - `.private_reference/legacy/CVF Edit/Review CVF.md`
  - `.private_reference/legacy/CVF Edit/Review CVF_1.md`
  - `.private_reference/legacy/CVF Edit/Review CVF_3.md`
  - `.private_reference/legacy/CVF Edit/Review CVF_4.md`
  - `.private_reference/legacy/CVF Edit/Review CVF_5.md`
  - `.private_reference/legacy/CVF ADD/Human System Harness/CVF_BRIEF_NORMALIZATION_SPEC.md`
  - `.private_reference/legacy/CVF ADD/Human System Harness/Thong_tin.md`
- Source families skipped:
  - `agentmemory` and `tolaria` — Candidate 2, not W1.
  - `CLI-Anything`, `OpenAgentd`, `pancake-pos-mcp`, `gridex`, `cortex-hub` — Candidate 3, requires later tool-action taxonomy.
  - provider gateway families — Candidate 5, not part of workflow state replay.
- File-level accepted value:
  - CVF Edit reviews -> workflow must be a state machine with transition
    validation and invalid-transition rejection.
  - `De_xuat.md` -> AI/agent must not invent transitions; transitions must be
    deterministic.
  - Human System Harness -> phase integrity must prevent skipped reasoning or
    unsafe transition into later phases.
  - existing Product Brief binding -> one concrete selected workflow with
    transition metadata and a deferred reviewer gate.
- Owner-surface normalization:
  - transition validation -> `workflow-resolver.ts`
  - route evidence -> `/api/execute` workflow execution projection and audit
    payload
  - live proof -> existing Phase E workflow-binding live spec
  - receipt ownership -> existing `receiptBinding`, not a new envelope field
- Accept/defer/reject matrix:
  - ACCEPT_NOW: replay existing workflow transitions and expose a bounded
    state-machine projection for Product Brief.
  - ACCEPT_NOW: stop emitting a step receipt for a step whose predecessor state
    is not reached.
  - DEFER_DEMAND_GATED: full multi-workflow engine, rollback, recovery UI, and
    planner/worker queue.
  - REJECT_DIRECT: adopting legacy state-machine language as a new global
    kernel authority in this tranche.
- Adversarial roles completed:
  - Implementer: smallest proof is in `workflow-resolver`, using existing
    binding metadata and tests.
  - Skeptic/Auditor: main risk is overclaiming a universal workflow engine;
    closure must say one selected workflow only.
  - Product/Operator Advocate: user pain reduced is misleading workflow
    evidence; remaining confusion is that deferred human review still has no
    full UI/runtime review surface.
  - Safety/Boundary Owner: no autonomous execution past a deferred reviewer
    gate and no new authority to execute tools or mutate data.
- Thin proof target:
  - Product Brief route returns a state-machine projection where step 4 is
    deferred, step 5 is not completed, and only reachable steps emit receipts.
- Blind-spot verdict: CLEAR

## Authorized Change

Implement a bounded workflow state-machine projection for
`workflow.product.create_product_brief.v1`:

- replay configured steps in sequence;
- complete only transitions whose `fromState` matches the current state;
- mark deferred reviewer steps as deferred and do not advance state;
- mark later steps waiting on deferred state as deferred/skipped rather than
  completed;
- bind receipts only for steps with completed traces and receipt ids;
- include the projection in existing workflow response/audit metadata.

## Evidence Plan

- `npm run test:run -- src/lib/workflows/workflow-resolver.test.ts src/app/api/execute/route.test.ts`
- `npm run check` in `cvf-web`
- live Phase E workflow-binding spec with provider API key
- mandatory release gate bundle
- markdown/session governance guards

## Acceptance Criteria

- [ ] Product Brief workflow projection includes state-machine metadata.
- [ ] Step 4 reviewer gate is deferred and does not advance state.
- [ ] Step 5 receipt-emission is not reported as completed while
      `freeze_ready` is unreachable.
- [ ] Receipt emissions exist only for completed reachable steps.
- [ ] `/api/execute` audit payload includes the state-machine projection.
- [ ] Focused tests PASS.
- [ ] Live Phase E workflow-binding proof PASS with secret-safe receipts.
- [ ] Mandatory release gate PASS.
- [ ] Closure review filed and session handoff updated.

## Claim Boundary

W1 may claim only bounded workflow state-machine enforcement evidence for the
existing Product Brief workflow binding. It does not claim a general workflow
engine, rollback engine, multi-agent orchestration, hosted readiness, broad
provider stability, production readiness, public capability graduation, or
global freeze lift.
