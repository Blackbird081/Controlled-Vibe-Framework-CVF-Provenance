# CVF MKG5 Memory Runtime Workflow Chain Roadmap

Memory class: FULL_RECORD

Status: IMPLEMENTATION_REVIEW_READY

docType: roadmap

Date: 2026-06-01

## Purpose

Move the Memory/Knowledge plane from doc-only governance evidence into a real
runtime-system foundation by composing existing Memory owner contracts into one
tested workflow chain.

## Authorization / Decision

Decision: operator requested Memory become a real system after MKG1-MKG4
identified the doc/runtime boundary.

Authority:

- `docs/baselines/CVF_GC018_MKG5_MEMORY_RUNTIME_WORKFLOW_CHAIN_2026-06-01.md`
- `docs/reviews/CVF_MKG1_MEMORY_KNOWLEDGE_GRAPH_OWNER_SURFACE_REVIEW_COMPLETION_2026-06-01.md`
- `docs/reviews/CVF_MKG2_DEFERRED_RUNTIME_CANDIDATE_TRIAGE_REVIEW_2026-06-01.md`
- `docs/reviews/CVF_MKG3_CURRENT_OWNER_NEGATIVE_SEARCH_EVIDENCE_REVIEW_2026-06-01.md`
- `docs/reviews/CVF_MKG4_GATE_EVIDENCE_CONSISTENCY_PROBE_REVIEW_2026-06-01.md`

## Scope

In scope:

- create one Learning Plane Foundation runtime workflow-chain module;
- split the near-threshold LPF root barrel and keep the active entrypoint thin;
- compose existing Memory event, gateway, retrieval, and packaging contracts;
- prove summary-only packaging and fail-closed behavior through focused tests;
- document the route/live boundary for later tranches.

Out of scope:

- web route wiring;
- live/provider proof;
- prompt injection or reinjection;
- raw memory release;
- new memory tier creation;
- graph persistence mutation;
- Legacy source edits under `.private_reference/legacy/**`;
- public-sync, push, or publish.

## Non-Goals

- no public readiness claim;
- no hosted or production readiness claim;
- no `/api/execute` behavior change;
- no autonomous mutation;
- no universal Memory system claim beyond the tested workflow-chain contract.

## Work Plan

| Step | Requirement | Output | Status |
| --- | --- | --- | --- |
| M5.1 | Source-verify existing Memory runtime owners | Source Verification rows | PASS |
| M5.2 | Implement deterministic workflow-chain module | `memory-runtime-workflow-chain.ts` | PASS |
| M5.3 | Add focused unit tests | `memory-runtime-workflow-chain.test.ts` | PASS |
| M5.4 | Run TypeScript and governance gates | verification evidence | PASS |
| M5.5 | File completion review and next-tranche boundary | implementation review packet | PASS |
| M5.6 | Split near-threshold LPF root barrel | `learning-activation.barrel.ts`; `index.ts` 975 -> 885 lines | PASS |

## Acceptance Criteria

| Criterion | Required result |
| --- | --- |
| Runtime chain exists | one module composes event hook, gateway, retrieval, and context packaging |
| Summary-only context | selected memory uses summaries and excludes raw content |
| Fail-closed behavior | policy denial and empty/no-match context do not release raw memory |
| Boundary | no route/live/provider/prompt/public work |
| Verification | focused test and TypeScript check pass |

## Verification / Evidence

Required before closure:

```powershell
npm test -- tests/memory-runtime-workflow-chain.test.ts
npm run check
python governance/compat/check_work_order_dispatch_quality.py --base <baseHead> --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <baseHead> --head HEAD
```

## Roadmap-To-Work-Order Trace

Work order:

`docs/work_orders/CVF_WO_MKG5_MEMORY_RUNTIME_WORKFLOW_CHAIN_2026-06-01.md`

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private runtime-foundation roadmap only. No public-sync remote, public
repository commit, or public artifact path is included.

## Claim Boundary

MKG5-T1 makes Memory a bounded runtime workflow contract. It does not yet claim
route integration, live-provider behavior, prompt reinjection, production
readiness, hosted readiness, public readiness, public-sync, or autonomous
memory mutation.
