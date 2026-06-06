# CVF Work Order - MKG5 Memory Runtime Workflow Chain

Memory class: FULL_RECORD

Status: IMPLEMENTATION_REVIEW_READY

docType: work_order

Date: 2026-06-01

## Purpose

Implement the first bounded Memory runtime-system chain by composing existing
Learning Plane Foundation contracts into one deterministic workflow function
with focused tests.

## Authority Chain

| Authority | Path / basis | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-01 request: Memory must become a real system | ACCEPT |
| MKG5 GC-018 | `docs/baselines/CVF_GC018_MKG5_MEMORY_RUNTIME_WORKFLOW_CHAIN_2026-06-01.md` | ACCEPT |
| MKG5 roadmap | `docs/roadmaps/CVF_MKG5_MEMORY_RUNTIME_WORKFLOW_CHAIN_ROADMAP_2026-06-01.md` | ACCEPT |
| MKG1 completion | `docs/reviews/CVF_MKG1_MEMORY_KNOWLEDGE_GRAPH_OWNER_SURFACE_REVIEW_COMPLETION_2026-06-01.md` | ACCEPT |
| MKG4 guard probe | `docs/reviews/CVF_MKG4_GATE_EVIDENCE_CONSISTENCY_PROBE_REVIEW_2026-06-01.md` | ACCEPT |

## Agent Roles

| Role | Responsibility | Boundary |
| --- | --- | --- |
| Orchestrator/implementer | implement bounded runtime chain and tests | no route/live expansion |
| Reviewer | check source verification, tests, and claim boundary | reject route/live overclaim |
| Operator | authorize future route/live tranche | no approval needed for this allowed scope |

## Scope

Allowed scope:

- add `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-runtime-workflow-chain.ts`;
- add `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/memory-runtime-workflow-chain.test.ts`;
- split `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/index.ts` into a thinner
  root barrel plus
  `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/learning-activation.barrel.ts`;
- update this work order, roadmap, GC-018, completion review, and active
  continuity files for MKG5;
- run focused tests, TypeScript check, and governance gates.

Forbidden scope:

- `/api/execute` or web route edits;
- provider/live proof;
- prompt injection or reinjection;
- raw memory release;
- new memory tiers;
- graph persistence mutation;
- Legacy source edits;
- public-sync, push, or publish.

Risk ceiling: R2 bounded runtime contract.

## Required First Reads

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-event-hooks.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-context-packager.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/runtime-memory-hierarchy.ts`
- `docs/reference/CVF_WORK_ORDER_CLOSURE_QUALITY_GATE_STANDARD_2026-05-28.md`

## Pre-Flight Checks

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/check_work_order_dispatch_quality.py --base <baseHead> --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <baseHead> --head HEAD
```

## Source Verification Block

| Claimed item | Verification class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Memory event hook evaluator exists | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-event-hooks.ts` | exported function | `evaluateMemoryEventHook` | memory event hooks | ACCEPT |
| Controlled memory gateway evaluator exists | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts` | exported function | `evaluateMemoryGatewayRequest` | controlled memory gateway | ACCEPT |
| Memory retrieval evaluator exists | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` | exported function | `evaluateRetrievalRequest` | memory retrieval policy | ACCEPT |
| Memory context packager exists | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-context-packager.ts` | exported function | `packageMemoryContext` | memory context packager | ACCEPT |
| Runtime actor role type exists | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/runtime-memory-hierarchy.ts` | exported type | `RuntimeMemoryActorRole` | runtime memory hierarchy | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
| --- | --- | --- | --- | --- |
| Compose Memory runtime owners | Execution Plan | `runMemoryRuntimeWorkflowChain` | focused unit test | PASS |
| Prove summary-only context | Acceptance Criteria | no raw content in context block | focused unit test | PASS |
| Prove fail-closed behavior | Acceptance Criteria | denied/deferred paths | focused unit test | PASS |
| Preserve route/live boundary | Scope / Claim Boundary | no route/live files touched | `git diff --name-status` | PASS |

## Worker Autonomy / No-Question Rule

The implementer must not ask the operator before performing non-destructive
actions inside this work order's Allowed scope.

If tests or machine gates fail inside Allowed scope, repair and rerun. Ask only
if remediation would exceed scope, require route/live/provider work, public-sync,
secrets/quota, destructive action, or a claim-boundary change.

## Near-Threshold Owner Maintainability Plan

Active owner entrypoint:

`EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/index.ts`

Action: extract context-budget, adaptation, simulation, reputation-routing,
weighting-doctrine, and calibration exports into
`EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/learning-activation.barrel.ts`.

Minimum shrink target: 50 lines

Result: LPF `src/index.ts` reduced from `975` to `885` physical lines.

## Execution Plan

1. Source-verify existing Memory runtime owner modules.
2. Add `runMemoryRuntimeWorkflowChain()` as the deterministic chain owner.
3. Add tests for successful packaging, policy denial, and empty/no-match
   fail-closed behavior.
4. Run focused test and TypeScript check.
5. Run governance gates and file completion review.

## Evidence Requirements

- focused unit test result;
- TypeScript check result;
- `git diff --name-status` changed-file boundary;
- no raw memory release and no reinjection assertions;
- public export disposition.

## Acceptance Criteria

| Criterion | Required result |
| --- | --- |
| Runtime chain | event hook -> gateway -> retrieval -> packager -> context event |
| Secret safety | `rawMemoryReleased=false` across result, receipts, and context block |
| Reinjection boundary | `canReinject=false` across result, receipts, and context block |
| Denial path | policy denial stops before retrieval/context packaging |
| Empty context path | no selected memory fails closed |

## Write Ownership

Owned files:

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-runtime-workflow-chain.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/memory-runtime-workflow-chain.test.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/index.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/learning-activation.barrel.ts`
- `docs/baselines/CVF_GC018_MKG5_MEMORY_RUNTIME_WORKFLOW_CHAIN_2026-06-01.md`
- `docs/roadmaps/CVF_MKG5_MEMORY_RUNTIME_WORKFLOW_CHAIN_ROADMAP_2026-06-01.md`
- `docs/work_orders/CVF_WO_MKG5_MEMORY_RUNTIME_WORKFLOW_CHAIN_2026-06-01.md`
- `docs/reviews/CVF_MKG5_MEMORY_RUNTIME_WORKFLOW_CHAIN_COMPLETION_2026-06-01.md`
- active session continuity files if mode or next allowed move changes.

Forbidden paths:

- `/api/execute` and web route files;
- provider adapter files;
- `.private_reference/legacy/**`;
- public-sync repository files.

Write mode:

- create/modify listed files only.

## Review Gate

Reject closure if this tranche edits web routes, claims live/provider behavior,
authorizes prompt reinjection, releases raw memory, creates a new memory tier,
or omits focused tests.

## Closure Checklist

- [x] Focused unit test passed.
- [x] TypeScript check passed.
- [x] Governance gates passed.
- [x] Changed files stayed inside Write Ownership for MKG5-owned code/docs.
- [x] Implementation review filed with Public Export Disposition.
- [x] No route/live/provider/prompt/public claim added.

## Return Conditions

Return to orchestrator if route wiring, live provider proof, prompt injection,
graph persistence mutation, public-sync, or new memory tier creation becomes
necessary.

## Operator Checkpoint

Operator explicitly requested making Memory a real system. This work order
implements only the first bounded runtime workflow-chain tranche; later route
or live-provider wiring requires a fresh checkpoint or GC-018.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private runtime-foundation work order only. No public-sync remote,
public repository commit, or public artifact path is included.

## Claim Boundary

MKG5-T1 authorizes and implements a bounded runtime workflow-chain contract
only. It does not authorize route integration, live provider proof, public-sync,
prompt reinjection, graph persistence mutation, hosted readiness, production
readiness, public readiness, or autonomous mutation.
