# CVF GC-018 VI1 W-Series Vertical Execute Chain

Memory class: SUMMARY_RECORD

Status: AUTHORIZED_VI1_W_SERIES_VERTICAL_EXECUTE_CHAIN

docType: gc018_baseline

Date: 2026-05-25

---

## Purpose

Authorize VI1 as a bounded vertical integration tranche for the existing
W-series surfaces already present around `/api/execute`.

The goal is to prove that CVF can run a chained governed execution path, not
only isolated components: one live `/api/execute` response must expose a single
readout joining governance receipt, workflow state, workflow recovery, memory
event hook posture, artifact verification, and operational metrics; the live
proof must include a 2-turn chain.

## Scope / Target / Owner Boundary

Allowed owner files:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/vertical-integration-readout.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/vertical-integration-readout.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.vi1-vertical-chain.alibaba.live.test.ts`
- VI1 completion/session/handoff files

Allowed behavior:

- add a response-level `verticalIntegrationReadout` object;
- link existing surfaces without creating new governance semantics;
- accept an optional client-supplied chain descriptor for 2-turn continuity
  proof;
- run one live Alibaba-compatible `/api/execute` 2-turn proof if a live key is
  available from operator environment or `.env.local`.

Forbidden:

- new receipt envelope schema or replacement receipt contract;
- route-level invalid-transition blocking beyond existing behavior;
- autonomous memory reinjection or raw memory prompt injection;
- new workflow engine, worker queue, planner, MCP/tool/database execution, or
  external skill import;
- provider adapter semantics changes, new provider claims, hosted readiness,
  production readiness, public-sync, or freeze release.

## Source / Predecessor Evidence

Predecessors:

- `docs/reference/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
- `docs/reviews/CVF_W1_WORKFLOW_STATE_MACHINE_ENFORCEMENT_COMPLETION_2026-05-24.md`
- `docs/reviews/CVF_WR1_WORKFLOW_RECOVERY_STATE_PROOF_COMPLETION_2026-05-25.md`
- `docs/reviews/CVF_W2_MEMORY_EVENT_HOOKS_COMPLETION_2026-05-24.md`
- `docs/reviews/CVF_W6_DELIVERABLE_PACK_ARTIFACT_VERIFICATION_COMPLETION_2026-05-24.md`
- existing `/api/execute` receipt, audit memory, Phase 2.C, and Phase 3.E
  route wiring

## Knowledge Absorption Blind-Spot Control Block

- Standard read:
  `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`
- Source inventory:
  - W1 workflow state-machine projection;
  - WR1 workflow recovery readout;
  - W2 memory event hooks;
  - W6 artifact verification;
  - Phase 2.C product brief route slice;
  - Phase 3.E operational metric emission;
  - existing `/api/execute` live governance receipt.
- Prior absorption evidence resolved:
  - W1 and WR1 are already route-visible through workflow projection.
  - W2 is available as a local LPF contract and must remain `canReinject=false`.
  - W6 is already embedded in generated deliverable packs.
  - Phase 3.E metrics already disclose event-model denominators.
  - live run diagnostics standard requires failure classification before
    rerun.
- Detailed source files used:
  - `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts`
  - `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-event-hooks.ts`
  - `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/audit-memory-receipt.ts`
  - `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/phase2c-product-brief-slice.ts`
  - `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/phase3e-operational-emission.ts`
  - `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- Source families skipped:
  - remaining horizontal LH1 sources such as caveman context engine, Workflow
    GoClaw runtime, and agentmemory event capture are deferred unless they can
    wire into this vertical path without a new runtime or semantic expansion.
- File-level accepted value:
  - W1 -> existing state-machine contract version and final state;
  - WR1 -> existing recovery action/checkpoint readout;
  - W2 -> memory event hook posture with no raw release and no reinjection;
  - W6 -> artifact verification summary from generated pack;
  - Phase 3.E -> operational metric IDs and denominator clarity;
  - route receipt -> live receipt IDs, provider/model, decision, and evidence
    mode.
- Owner-surface normalization:
  - implement a route-level integration readout under `cvf-web/src/lib`, not a
    new registry, pack, workflow engine, or receipt schema.
- Accept/defer/reject matrix:
  - ACCEPT_NOW: deterministic vertical readout and 2-turn live proof.
  - DEFER_DEMAND_GATED: caveman context engine, Workflow GoClaw runtime,
    agentmemory event capture wiring, UI chain visualization, broad workflow
    runtime.
  - REJECT_DIRECT: claiming a coherent autonomous agent runtime, memory
    reinjection authority, new provider stability, or production readiness from
    this tranche.
- Adversarial roles completed:
  - Implementer: smallest useful change is one readout helper plus route/test
    wiring.
  - Skeptic/Auditor: response-level aggregation must not alter receipt
    authority or hide partial surfaces.
  - Product/Operator Advocate: one clear readout reduces future time/token
    waste by showing which chain surface failed.
  - Safety/Boundary Owner: W2 remains no-reinjection and live failures require
    diagnostic classification before rerun.
- Thin proof target:
  - one 2-turn live `/api/execute` chain with at least five existing W-series
    surfaces present in the second turn.
- Blind-spot verdict: CLEAR.

## Decision / Baseline / Proposed Tranche

Decision: AUTHORIZE_VI1_W_SERIES_VERTICAL_EXECUTE_CHAIN.

Baseline:

- existing route code already emits several surfaces independently;
- current weakness is clarity and integration proof, not lack of more
  horizontal source material;
- Claude review recommends vertical integration before more absorption.

Proposed tranche:

- add typed `verticalIntegrationReadout`;
- attach it to `/api/execute` responses;
- add focused unit/route tests;
- run a live 2-turn Alibaba-compatible proof with secret-safe diagnostics.

## Acceptance Criteria

- `/api/execute` returns `verticalIntegrationReadout`;
- readout reports receipt, workflow state, workflow recovery, memory hook,
  artifact verification, and operational metrics when present;
- memory hook readout preserves `rawMemoryReleased=false` and
  `canReinject=false`;
- 2-turn chain descriptor links second turn to first receipt without changing
  receipt envelope semantics;
- focused unit/route tests pass;
- live 2-turn proof passes or, if blocked, produces a secret-safe diagnostic
  and does not claim live closure.

## Verification Plan

```bash
cd EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web
npm run test:run -- src/lib/vertical-integration-readout.test.ts src/app/api/execute/route.test.ts
npm run check
npm run test:run -- src/app/api/execute/route.vi1-vertical-chain.alibaba.live.test.ts
cd ../../..
python governance/compat/check_active_session_state.py
python governance/compat/check_agent_handoff_guard_compat.py
```

## Claim Boundary

VI1 may claim only a bounded vertical integration readout and one 2-turn live
proof for existing `/api/execute` surfaces. It does not claim a broad workflow
engine, autonomous agent runtime, memory reinjection, provider stability,
external skill execution, hosted readiness, production readiness, public
release readiness, or freeze release.
