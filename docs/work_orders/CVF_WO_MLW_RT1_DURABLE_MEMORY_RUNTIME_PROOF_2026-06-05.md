# CVF Work Order MLW-RT1 Durable Memory Runtime Proof

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-05

executionBaseHead: `acaf9124`

closureBaseHead: `acaf9124`

commitMode: `CODEX_MULTI_ROLE_CLOSEOUT`

## Purpose

Provide a bounded worker packet and closure record for proving existing
durable-memory write/read continuity through the governed `/api/execute` route.

## Objective

Close a bounded runtime-proof tranche showing that the existing governed
`/api/execute` route can write summary-only durable memory and read that stored
summary in a later governed execution request.

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator authorization | 2026-06-05 request to continue and use existing API key if needed | ACCEPT |
| Startup authority | `CVF_SESSION/ACTIVE_SESSION_STATE.json` and active handoff | ACCEPT |
| Live-proof rule | `AGENTS.md` Mandatory Live Governance Proof | ACCEPT |
| Source contract | MLW1/MLW2 runtime contracts and source verification block below | ACCEPT |

## Agent Roles

| Role | Assigned actor | Responsibility |
| --- | --- | --- |
| Orchestrator | Codex | select bounded RT1 tranche and maintain scope boundary |
| Worker | Codex | add focused deterministic and live tests |
| Reviewer | Codex | run tests, classify live diagnostics, and close artifacts |
| Operator | Human | authorize broader backend/public/runtime follow-up only |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Source | Work-order coverage | Disposition |
| --- | --- | --- | --- |
| MLW1 memory operations must be governed | `docs/reference/CVF_MLW1_GOVERNED_MEMORY_OPERATION_RECEIPT_MODEL_2026-06-05.md` | durable write/read receipt invariants tested | ACCEPT |
| MLW2 context must reject raw memory and use governed packaging | `docs/reference/CVF_MLW2_DETERMINISTIC_CONTEXT_BUNDLE_WORKFLOW_2026-06-05.md` | read route prompt block is summary-only and `canReinject=false` | ACCEPT |
| Live governance proof required for runtime behavior claims | `AGENTS.md` live governance proof rule | Alibaba live test added and executed | ACCEPT |
| Backend choice required for new runtime implementation | roadmap operator checkpoint | no new backend selected; existing file-backed store only | ACCEPT_WITH_BOUNDARY |

## Allowed Scope

- Add or update focused tests under
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/`.
- Create MLW-RT1 GC-018, work order, completion review, and continuity updates.
- Run focused deterministic Vitest and one Alibaba live Vitest proof.

## Forbidden Scope

- No durable backend replacement.
- No route behavior rewrite beyond test/proof coverage.
- No package or lockfile edit.
- No public-sync.
- No autonomous memory or learning mutation.
- No MLW7/MLW8 implementation.

## Required First Reads

| Required read | Reason | Status |
| --- | --- | --- |
| `CVF_SESSION_MEMORY.md` | session front door | READ |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | active mode and handoff resolution | READ |
| `AGENT_HANDOFF_V15_2026-05-29.md` | active handoff | READ |
| `docs/reference/CVF_MLW1_GOVERNED_MEMORY_OPERATION_RECEIPT_MODEL_2026-06-05.md` | receipt contract | READ |
| `docs/reference/CVF_MLW2_DETERMINISTIC_CONTEXT_BUNDLE_WORKFLOW_2026-06-05.md` | context boundary | READ |

## Pre-Flight Checks

| Check | Evidence | Status |
| --- | --- | --- |
| Worktree baseline captured | `acaf9124` | PASS |
| Existing runtime source verified | Source Verification Block | PASS |
| Live key availability checked without printing secrets | `resolveAlibabaApiKey` path used | PASS |
| Public/provenance boundary respected | no public-sync action | PASS |

## Write Ownership

Codex owns only the MLW-RT1 test, proof, documentation, registry, roadmap, and
session-continuity edits listed in this work order. Runtime route source,
backend migration, public-sync, and production durability remain outside this
write ownership.

## Execution Plan

1. Add deterministic write-then-read durable-memory route regression.
2. Add one Alibaba live test for the same governed route chain.
3. Run focused deterministic and live tests.
4. Record safe live-run diagnostics for failed attempts.
5. Close baseline, work order, review, registry, roadmap, and session state.

## Evidence Requirements

| Requirement | Evidence |
| --- | --- |
| Deterministic behavior proof | focused Vitest PASS |
| Live governance proof | Alibaba live Vitest PASS |
| Secret safety | no raw key printed; env resolver only |
| Boundary proof | completion claim boundary and public export disposition |
| Continuity proof | session state, front door, and active handoff updated |

## Acceptance Criteria

| Criterion | Status |
| --- | --- |
| Write receipt exists for first governed request | PASS |
| Stored durable memory can be read by later governed request | PASS |
| Read receipt preserves summary-only/no-reinjection boundary | PASS |
| Live Alibaba route proof passes | PASS |
| No backend/public/autonomous-learning claim is made | PASS |

## Review Gate

Reviewer must reject closure if tests fail, live proof is skipped while runtime
behavior is claimed, raw secrets are printed, or the artifact implies
production durability/public readiness.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| File-backed durable memory store exists | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | source file | `createFileBackedDurableMemoryStore` | durable memory store | EXISTS | ACCEPT |
| Durable memory write receipt is exposed | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-final-response.ts` | source file | `durableMemoryWriteReceipt` | final response builder | EXISTS | ACCEPT |
| Durable memory read receipt is exposed | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-final-response.ts` | source file | `durableMemoryRead` | final response builder | EXISTS | ACCEPT |
| Durable memory route reads stored summaries | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/durable-memory-route.ts` | source file | `evaluateDurableMemoryRoute` | durable memory route helper | EXISTS | ACCEPT |
| Durable memory route writes output summaries | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/durable-memory-route.ts` | source file | `evaluateDurableMemoryWrite` | durable memory route helper | EXISTS | ACCEPT |
| Alibaba key aliases are source-backed | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/alibaba-env.ts` | source file | `resolveAlibabaApiKey` | provider env resolver | EXISTS | ACCEPT |

## New Doc-Only Fields

None.

## Implementation Summary

The worker added:

- deterministic regression proving a governed execute write request can create
  summary-only durable memory and a later execute request can read it into the
  governed durable-memory system prompt;
- Alibaba live proof covering the same write-then-read chain with real provider
  execution and real guard authority checks.

## Live Run Diagnostic

Initial live-test attempts failed before provider execution:

| Attempt | Stage | Class | Retryability | User action | Safe message |
| --- | --- | --- | --- | --- | --- |
| 1 | test_harness_precondition | assertion_order_before_route_status | retryable_after_test_fix | none | test read the store before checking the write response |
| 2 | guard_runtime | guard_blocked_ai_commit | retryable_after_metadata_fix | none | modifying write action needed `aiCommit` metadata |
| 3 | guard_runtime | guard_blocked_authority_phase | retryable_after_phase_fix | none | OPERATOR cannot write in INTAKE; write proof moved to BUILD phase |

Final live run: PASS.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | this file | status `CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_MLW_RT1_DURABLE_MEMORY_RUNTIME_PROOF_COMPLETION_2026-06-05.md` | final disposition, changed-file evidence, claim boundary, and gate evidence recorded | PASS |
| Roadmap state | `docs/roadmaps/CVF_CI1_T11_MEMORY_LEARNING_ABSORPTION_CONSOLIDATED_ROADMAP_2026-06-05.md` | MLW-RT1 runtime proof update recorded | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | `mlw-rt1-durable-memory-runtime-proof` registry entry added | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | MLW-RT1 quick lookup row added | PASS |
| External evidence digest | this file, `Live Run Diagnostic` | Alibaba live proof attempts classified with secret-safe fields | PASS |
| System loop interlock | N/A with reason | bounded proof only; no upstream/downstream autonomous loop mutation added | N/A with reason |
| Session continuity | `CVF_SESSION/ACTIVE_SESSION_STATE.json`, `CVF_SESSION_MEMORY.md`, `AGENT_HANDOFF_V15_2026-05-29.md` | active mode and next allowed move updated | PASS |
| Deterministic test | `route.durable-memory.test.ts` | `npm run test:run -- src/app/api/execute/route.durable-memory.test.ts` | PASS |
| Live proof | `route.mlw-rt1-durable-memory.alibaba.live.test.ts` | `npm run test:run -- src/app/api/execute/route.mlw-rt1-durable-memory.alibaba.live.test.ts --reporter=verbose` | PASS |
| Runtime source changes | N/A | N/A with reason - tests/proof only; existing route source unchanged | N/A with reason |
| Public export | N/A | N/A with reason - private provenance proof only | N/A with reason |

## Closure Checklist

- [x] Source verification block complete.
- [x] Deterministic focused test passed.
- [x] Alibaba live proof passed.
- [x] Live-run failures classified before meaningful rerun.
- [x] No raw key printed.
- [x] No backend selection or public claim made.

## Return-To-Orchestrator Conditions

Return to orchestrator if the live key is unavailable, the route source requires
behavioral rewrite, backend selection becomes necessary, public-sync is needed,
or any closure gate fails outside MLW-RT1 allowed scope.

## Operator Checkpoint

Operator checkpoint is required before backend migration, public-safe memory
summary/public-sync, MLW7, MLW8, hosted release proof, or autonomous learning
scope.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Escalation state | Next control action |
| --- | --- | --- | --- | --- |
| Write/read durable memory continuity lacked a single focused route proof | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | TEST_ADDED | retain MLW-RT1 deterministic regression |
| Live write request was initially guard-blocked without `aiCommit` and BUILD phase | PHASE_GATE_PLACEMENT_GAP | GOVERNANCE_CONTROL_PLANE | RULE_REINFORCED | live proof now records required guard metadata |
| Durable backend remains file-backed only | OPERATOR_SCOPE_CLARITY_GAP | GOVERNANCE_CONTROL_PLANE | DEFERRED_WITH_BOUNDARY | backend migration requires separate GC-018 |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance runtime proof. No public README/catalog claim is made.

## Claim Boundary

MLW-RT1 proves bounded existing-route behavior under tests and one live Alibaba
run. It does not claim production durability, distributed storage, hosted
freshness, public readiness, or autonomous learning.
