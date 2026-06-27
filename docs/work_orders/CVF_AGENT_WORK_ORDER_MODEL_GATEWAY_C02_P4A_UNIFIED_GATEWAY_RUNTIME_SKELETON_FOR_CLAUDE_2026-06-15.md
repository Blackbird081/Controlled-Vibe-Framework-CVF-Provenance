# CVF Agent Work Order: Model Gateway C-02 P4A Unified Gateway Runtime Skeleton - 2026-06-15

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Worker: Claude

Orchestrator / reviewer: Codex (or Claude under SINGLE_AGENT_MULTI_ROLE)

Worker commit policy: WORKER_MUST_NOT_COMMIT

Commit mode: WORKER_MUST_NOT_COMMIT

completionReviewPath:
`docs/reviews/CVF_MODEL_GATEWAY_C02_P4A_UNIFIED_GATEWAY_RUNTIME_SKELETON_COMPLETION_2026-06-15.md`

reviewerOwnedClosurePaths:
- `docs/reviews/CVF_MODEL_GATEWAY_C02_P4A_UNIFIED_GATEWAY_RUNTIME_SKELETON_COMPLETION_2026-06-15.md`
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`
- `AGENT_HANDOFF_V18_2026-06-12.md`

dispatchBaseHead: c6c09ae3

executionBaseHead: WORKER_MUST_CAPTURE_AFTER_DISPATCH

closureBaseHead: REVIEWER_CAPTURE_AFTER_WORKER_RETURN

rawMemoryReleased=false

riskCeiling: R1 (additive runtime skeleton + conformance tests; no live
provider; no mutation of existing source beyond barrel)

---

## Authorization Preconditions (BLOCKING)

Both prerequisites are satisfied:

1. Fresh GC-018 baseline:
   `docs/baselines/CVF_GC018_MODEL_GATEWAY_C02_P4A_UNIFIED_GATEWAY_RUNTIME_SKELETON_2026-06-15.md`
2. Operator authorized P4A scope and SINGLE_AGENT_MULTI_ROLE pattern in
   2026-06-15 session instruction.

Dispatch status: `DISPATCHED_UNDER_WORKER_MUST_NOT_COMMIT`.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance runtime skeleton. Public-sync not authorized.

## Claim Boundary

This work order authorizes only the C-02 P4A unified gateway runtime skeleton
inside `EXTENSIONS/CVF_MODEL_GATEWAY/`. It authorizes a local deterministic
skeleton class, barrel edit, and conformance tests. It does NOT authorize live
provider API calls, EPF integration wiring, strategy-layer work, AI Gateway
absorption, public-sync, mutation of any existing source file other than
`index.ts` barrel, governance-kernel changes, or production/public readiness claims.

---

## Purpose

Provide a local deterministic `UnifiedGatewaySkeletonImpl` class that implements
`UnifiedGatewayInterfaceContract` (P3) against existing Model Gateway primitives
(routing, policy, health, quota, receipt), with injectable executor for tests.

This makes the P3 contract machine-verifiable before P4B wires live providers.
The skeleton uses existing `ProviderRegistry`, `ProviderHealthMonitor`,
`QuotaLedger`, `GatewayReceiptBuilder`, `isPolicyAllowed` -- all from existing
source files -- without calling any provider API or network.

---

## Authority Chain

| Authority | Role |
|---|---|
| `docs/baselines/CVF_GC018_MODEL_GATEWAY_C02_P4A_UNIFIED_GATEWAY_RUNTIME_SKELETON_2026-06-15.md` | Implementation authorization for C-02 P4A |
| Operator instruction 2026-06-15 | Approves P4A scope and SINGLE_AGENT_MULTI_ROLE pattern |
| `docs/roadmaps/CVF_MODEL_GATEWAY_C02_P4A_UNIFIED_GATEWAY_RUNTIME_SKELETON_AND_CONFORMANCE_ROADMAP_2026-06-15.md` | P4A roadmap: scope, deliverables, IS spec, acceptance criteria |
| `docs/reference/CVF_MODEL_GATEWAY_C02_PROVIDER_ROUTING_BOUNDARY_REWRITE_PLAN_2026-06-14.md` | Closed C-02 plan; `gatewayUnifiedInterfaceBoundary` disposition (section 9) |
| P3 closure (COMPLETE_PENDING_REVIEW) | `UnifiedGatewayInterfaceContract` is stable P4A implementation target |
| This work order | Worker execution scope |
| Reviewer agent | Closure, commits, allowed repairs, session sync |

---

## Legacy Absorption Coverage Index Disposition

| Field | Evidence |
|---|---|
| Coverage index | `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` |
| Stable row id | `MGW-001` |
| Coverage status | `PARTIAL_RECHECK_REQUIRED` (unchanged) |
| Release basis | P4A implements runtime skeleton for `gatewayUnifiedInterfaceBoundary` advisory |
| Required disposition in worker return | Confirm P4A implements local skeleton only; live provider keys remain deferred for P4B |
| P4A closure coverage note | `MGW-001` stays `PARTIAL_RECHECK_REQUIRED` until P4B also closes |

## Freeze Posture Disposition

| Field | Evidence |
|---|---|
| Active freeze posture | `governance_kernel_freeze_recommended` |
| Freeze rule | `governance/toolkit/05_OPERATION/CVF_GOVERNANCE_KERNEL_FREEZE_RELEASE_RULE.md` |
| Kernel surface check | `CVF_MODEL_GATEWAY` is NOT one of the 12 governance-kernel owner-map surfaces |
| Disposition | Runtime skeleton work permitted under fresh GC-018; no freeze-release packet required |

## Agent Roles

| Role | Owner | Boundary |
|---|---|---|
| Orchestrator / reviewer / committer | Reviewer agent | Review returned class/tests, run gates, author closure artifact, commit, sync session continuity |
| Worker | Worker agent | Author P4A skeleton + conformance tests only; run worker gates; return COMPLETE_PENDING_REVIEW without committing |
| Operator | Human operator | Authorizes scope and assignment; approves any scope change |

## Intake Role Routing Decision

| Field | Decision |
|---|---|
| Intake summary | Operator authorized Model Gateway C-02 P4A runtime skeleton per SINGLE_AGENT_MULTI_ROLE pattern |
| Scope classification | Bounded R1 single-extension Model Gateway runtime skeleton + conformance tests |
| Risk sensitivity | No live provider, no public-sync, no secrets, no production/readiness claim |
| Selected route mode | SINGLE_AGENT_MULTI_ROLE |
| routeMode | SINGLE_AGENT_MULTI_ROLE |
| Role separation basis | Phase gates, separate base heads, worker no-commit boundary, reviewer closure conversion |
| Escalation condition | Stop for scope expansion beyond P4A skeleton boundary, live provider calls, network access, public-sync, secrets, package install, existing-source mutation, governance-kernel mutation |
| Disposition | DISPATCHED_UNDER_WORKER_MUST_NOT_COMMIT |

## Single-Agent Multi-Role Control Block

| Field | Decision |
|---|---|
| Single agent owns implementation and review | YES if operator assigns multi-role, bounded by this block |
| Role separation ledger | Orchestrator owns GC-018 and dispatch; worker owns skeleton/tests and worker return; reviewer owns closure artifact and acceptance; committer owns commits and session sync |
| Evidence basis independent of memory-only claims | GC-018, work order, source verification, conformance tests, diff evidence, governance gates |
| Self-review boundary | Independent review is not claimed; reviewer must inspect real diff and gate evidence before any commit |
| Gate sequence | pre-dispatch by orchestrator, baseline tests by worker, conformance tests by worker, reviewer-fast and pre-closure by reviewer, pre-push only if later authorized |
| Escalation conditions | Stop for forbidden paths, live provider/network, EPF/strategy scope, public-sync, secrets, package install, existing-source mutation, governance-kernel mutation |
| Worker | Assigned worker role |
| Reviewer / committer | Assigned reviewer and committer roles |
| Human escalation checkpoint | Scope expansion only |
| Collusion boundary | Single-agent result is bounded governance evidence, not independent review |

## Reviewer Closure Conversion Block

completionReviewPath:
`docs/reviews/CVF_MODEL_GATEWAY_C02_P4A_UNIFIED_GATEWAY_RUNTIME_SKELETON_COMPLETION_2026-06-15.md`

reviewerOwnedClosurePaths:
- `docs/reviews/CVF_MODEL_GATEWAY_C02_P4A_UNIFIED_GATEWAY_RUNTIME_SKELETON_COMPLETION_2026-06-15.md`
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`
- `AGENT_HANDOFF_V18_2026-06-12.md`

---

## Pre-Flight Checks

Worker must:

1. Capture `executionBaseHead` (`git rev-parse HEAD`).
2. Run `git status --short` and confirm clean worktree (P3 untracked files OK).
3. Confirm fresh GC-018 baseline and operator authorization both exist.
4. Read all Required First Reads.
5. Re-read all source baseline files and re-confirm line ranges.
6. Run baseline test suite for `CVF_MODEL_GATEWAY` to capture green pre-state.

## Write Ownership

Worker may write only:

- `EXTENSIONS/CVF_MODEL_GATEWAY/src/unified-gateway-skeleton.ts` (create)
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` (edit, barrel exports only)
- `EXTENSIONS/CVF_MODEL_GATEWAY/tests/unified-gateway-skeleton.test.ts` (create)
- `docs/reviews/CVF_MODEL_GATEWAY_C02_P4A_UNIFIED_GATEWAY_RUNTIME_SKELETON_WORKER_RETURN_2026-06-15.md` (create)
- GC-051 source entries under `docs/corpus-intelligence/registry/entries/` (create, allowed-scope repair)
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` (regenerate, allowed-scope repair)

Worker must NOT write to any other extension, any session/handoff/registry file,
or any existing source file other than `index.ts` barrel.

## Required First Reads

| File | Required use |
|---|---|
| `AGENTS.md` | Active governance instructions |
| `CVF_SESSION_MEMORY.md` | Current mode and next allowed move |
| `docs/roadmaps/CVF_MODEL_GATEWAY_C02_P4A_UNIFIED_GATEWAY_RUNTIME_SKELETON_AND_CONFORMANCE_ROADMAP_2026-06-15.md` | P4A scope, deliverables, IS spec |
| `docs/baselines/CVF_GC018_MODEL_GATEWAY_C02_P4A_UNIFIED_GATEWAY_RUNTIME_SKELETON_2026-06-15.md` | Implementation authorization |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/unified-gateway-interface-contract.ts` | P3 contract; implementation target |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-policy.ts` | `GatewayPolicyContext`, `isPolicyAllowed` reuse |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-health.ts` | `ProviderHealthMonitor`, `ProviderHealthState` reuse |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | `ProviderRegistry` reuse |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/quota-ledger.ts` | `QuotaLedger` reuse |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-receipt.ts` | `GatewayReceiptBuilder` reuse |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/credential-boundary.ts` | Credential shielding pattern |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/vision-runtime-adapter.ts` | Adapter factory pattern precedent |
| `EXTENSIONS/CVF_MODEL_GATEWAY/tests/model-gateway-runtime.integration.test.ts` | Integration test pattern precedent |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` | Barrel surface; avoid name collisions |
| `governance/toolkit/05_OPERATION/CVF_GOVERNED_FILE_SIZE_GUARD.md` | GC-023 thresholds |

## Source Verification Block

All symbols verified against current source at HEAD `c6c09ae3` on 2026-06-15.
Disposition column uses canonical values only: ACCEPT, REJECT, or BLOCKED-SOURCE-NOT-FOUND
(hyphenated prose; backtick form only in table cells).

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Implementation action | Disposition |
|---|---|---|---|---|---|---|
| Reused: UnifiedGatewayInterfaceContract | `EXTENSIONS/CVF_MODEL_GATEWAY/src/unified-gateway-interface-contract.ts` | line 74 | `UnifiedGatewayInterfaceContract` | unified-gateway-interface-contract | IMPLEMENT_CONTRACT | ACCEPT |
| Reused: GatewayExecuteRequest | `EXTENSIONS/CVF_MODEL_GATEWAY/src/unified-gateway-interface-contract.ts` | line 25 | `GatewayExecuteRequest` | unified-gateway-interface-contract | REUSE_BY_IMPORT | ACCEPT |
| Reused: GatewayErrorEnvelope | `EXTENSIONS/CVF_MODEL_GATEWAY/src/unified-gateway-interface-contract.ts` | line 16 | `GatewayErrorEnvelope` | unified-gateway-interface-contract | REUSE_BY_IMPORT | ACCEPT |
| Reused: GatewayPolicyContext | `EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-policy.ts` | line 2 | `GatewayPolicyContext` | gateway-policy | REUSE_BY_IMPORT | ACCEPT |
| Reused: isPolicyAllowed | `EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-policy.ts` | line 15 | `isPolicyAllowed` | gateway-policy | REUSE_BY_IMPORT | ACCEPT |
| Reused: ProviderHealthMonitor | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-health.ts` | line 17 | `ProviderHealthMonitor` | provider-health | REUSE_BY_IMPORT | ACCEPT |
| Reused: ProviderRegistry | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | line 30 | `ProviderRegistry` | provider-registry | REUSE_BY_IMPORT | ACCEPT |
| Reused: QuotaLedger | `EXTENSIONS/CVF_MODEL_GATEWAY/src/quota-ledger.ts` | line 29 | `QuotaLedger` | quota-ledger | REUSE_BY_IMPORT | ACCEPT |
| Reused: GatewayReceiptBuilder | `EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-receipt.ts` | line 58 | `GatewayReceiptBuilder` | gateway-receipt | REUSE_BY_IMPORT | ACCEPT |
| Reused: index.ts barrel | `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` | lines 1-304 | barrel export blocks | model gateway barrel | EXTEND_BARREL_ONLY | ACCEPT |

Note: worker must re-confirm these at execution time.

## Negative Search And Collision Discipline

| Structured query | Search roots | Expected result | Same-token collision disposition |
|---|---|---|---|
| `rg -l "UnifiedGatewaySkeletonImpl" --hidden --no-ignore .` | All source, tests, docs, JSON | Zero files before authoring | ABSENT; SAFE_TO_ADD |
| `rg -l "unified-gateway-skeleton" --hidden --no-ignore .` | All source, tests, docs, JSON | Zero files before authoring | ABSENT; SAFE_TO_ADD |
| `rg -n "GatewayPolicyContext\|ProviderHealthMonitor\|ProviderRegistry\|QuotaLedger\|GatewayReceiptBuilder\|isPolicyAllowed" EXTENSIONS/CVF_MODEL_GATEWAY/src` | Model Gateway source | Existing symbols in authoritative definition files | COLLISION_IS_AUTHORITATIVE_SOURCE; skeleton must import, not redeclare |

Collision note: all reused types must be imported from their authoritative
definition files. No redeclaration of any existing symbol.

## Current Runtime Freshness Verification

| Surface | Freshness check | Checker-expected line |
|---|---|---|
| `UnifiedGatewayInterfaceContract` | `rg -n "UnifiedGatewayInterfaceContract" EXTENSIONS/CVF_MODEL_GATEWAY/src/unified-gateway-interface-contract.ts` | line 74 |
| `GatewayPolicyContext` | `rg -n "GatewayPolicyContext" EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-policy.ts` | line 2 |
| `isPolicyAllowed` | `rg -n "isPolicyAllowed" EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-policy.ts` | line 15 |
| `ProviderHealthMonitor` | `rg -n "ProviderHealthMonitor" EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-health.ts` | line 17 |
| `ProviderRegistry` | `rg -n "ProviderRegistry" EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | line 30 |
| `QuotaLedger` | `rg -n "QuotaLedger" EXTENSIONS/CVF_MODEL_GATEWAY/src/quota-ledger.ts` | line 29 |
| `GatewayReceiptBuilder` | `rg -n "GatewayReceiptBuilder" EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-receipt.ts` | line 58 |

---

## Implementation Specification

### IS-1: UnifiedGatewaySkeletonImpl class

Create `EXTENSIONS/CVF_MODEL_GATEWAY/src/unified-gateway-skeleton.ts`.

The class must implement `UnifiedGatewayInterfaceContract`:

Constructor options interface:
```typescript
export interface UnifiedGatewaySkeletonOptions {
  registry: ProviderRegistry;
  health: ProviderHealthMonitor;
  quota: QuotaLedger;
  receiptBuilder?: GatewayReceiptBuilder;
  localExecuteFn?: (request: GatewayExecuteRequest) => Promise<string>;
}
```

Method contracts:
- `execute(request: GatewayExecuteRequest)`: run `isPolicyAllowed(request.policy)`;
  if denied return `GatewayErrorEnvelope` with `errorClass: "policy_denied"`,
  `credentialShielded: true`, `retryable: false`. If allowed, call
  `localExecuteFn(request)` (or return stub `""` if not injected), return
  `GatewayExecuteResponse` with `traceId`, `text`, and optional `receiptObligation`.
- `stream(request: GatewayStreamRequest)`: if policy denied yield single
  `GatewayErrorEnvelope`. If allowed, yield one `GatewayStreamChunk` with
  `done: true`. Use `AsyncGenerator` or equivalent; no live fetch.
- `embedding(request: GatewayEmbeddingRequest)`: if policy denied return
  `GatewayErrorEnvelope`. If allowed return `GatewayEmbeddingResponse`
  with `embeddings: [[0, 0, 0]]` and `dimensions: 3`.
- `health(traceId: string)`: call `health.get(providerId)` for each provider
  in registry; set `status` to `"ok"` if all healthy, `"degraded"` if any
  degraded/rate_limited, `"unavailable"` if all unavailable. Return
  `GatewayHealthResponse`.

Credential shielding: no method may include provider API keys, secrets,
or unshielded provider IDs in response payloads. Error envelopes must have
`credentialShielded: true`. Use `providerIdShielded: true` on error
envelopes when provider selection is policy-sensitive.

File-size: must stay under `.ts` advisory threshold (700 lines), hard 1000.

### IS-2: Barrel exports

Add `UnifiedGatewaySkeletonImpl` and `UnifiedGatewaySkeletonOptions` to
`index.ts` using named exports. Do not collide with existing names.

### IS-3: Conformance tests

Create `EXTENSIONS/CVF_MODEL_GATEWAY/tests/unified-gateway-skeleton.test.ts`.

Required test cases (minimum 10):
1. `execute` allowed policy -- returns `GatewayExecuteResponse` shape with `traceId`.
2. `execute` denied policy -- returns `GatewayErrorEnvelope` with `errorClass: "policy_denied"` and `credentialShielded: true`.
3. `execute` with injected `localExecuteFn` -- response `text` matches executor output.
4. `stream` allowed policy -- yields at least one `GatewayStreamChunk` with `done: true`.
5. `stream` denied policy -- yields `GatewayErrorEnvelope` with `credentialShielded: true`.
6. `embedding` allowed policy -- returns `GatewayEmbeddingResponse` with `embeddings` and `dimensions: 3`.
7. `embedding` denied policy -- returns `GatewayErrorEnvelope`.
8. `health` -- returns `GatewayHealthResponse` with valid `status`.
9. Credential shielding -- `JSON.stringify(response)` does not contain any
   injected secret value (e.g. `"sk-test-secret"`).
10. Compile-time check -- `UnifiedGatewaySkeletonImpl` satisfies `UnifiedGatewayInterfaceContract` (type assertion in test).

No live network calls. All external dependencies injected.

File-size: under `.test.ts` advisory (800 lines), hard 1200.

---

## Execution Plan

| Step | Input | Action | Output | Stop condition |
|---|---|---|---|---|
| 1 | Required first reads + GC-018 + operator auth | Capture executionBaseHead; confirm authorizations; re-confirm source baseline line ranges; run baseline tests green | preflight evidence | Stop if GC-018/operator auth missing or baseline red |
| 2 | gateway-policy, provider-health, provider-registry, quota-ledger, gateway-receipt, unified-gateway-interface-contract | Implement IS-1 skeleton class with all four methods | `unified-gateway-skeleton.ts` | Stop if a reused symbol does not exist or a live call would be required |
| 3 | index.ts | Implement IS-2 barrel exports without collision | updated barrel | Stop on export name collision |
| 4 | skeleton + primitives | Implement IS-3 conformance tests | `unified-gateway-skeleton.test.ts` | Stop if a test would require live network or real API key |
| 5 | gates | Run type check, full test suite, reviewer-fast | gate evidence | Stop and repair allowed-scope issues before return |
| 6 | evidence | Author worker return | `COMPLETE_PENDING_REVIEW` | Stop if any gate fails and repair is out of scope |

## Evidence Requirements

Worker must provide source-backed evidence for every claim in the worker return:
- Each reuse claim: cite the imported symbol and its checker-expected line.
- The no-live-call claim: changed file set limited to new skeleton, barrel edit,
  new test, GC-051 entries, and worker return.
- Credential shielding: cite test case 9 result and `credentialShielded: true` literal.
- The no-commit claim: `git rev-parse HEAD` equal to `executionBaseHead`.
- Type-check and test results: actual command output summaries.

## Worker Autonomy / No-Question Rule

Allowed-scope failures (type errors, failing new tests, missing sections, trace
updates, diff hygiene, GC-023 file split, markdown structural sections, ASCII
encoding, GC-051 coverage) must be repaired and rerun without escalation.

Worker must stop and return `BLOCKED_SCOPE_EXPANSION` only when a repair would:
require editing an extension other than `CVF_MODEL_GATEWAY`; require editing any
existing source file other than `index.ts` barrel; require a live provider/API call;
require network access, package install, secret access, public-sync,
registry mutation, session-state mutation, governance-kernel mutation, or any
destructive action.

## Worker Pending-Return Gate

| Gate | Required evidence | Status |
|---|---|---|
| Authorizations present | GC-018 + operator authorization cited | PASS |
| Scope-limited mutation | Changes limited to new skeleton, barrel edit, new tests, GC-051 entries, worker return | PASS |
| Existing sources unchanged | All fragment contracts and existing primitives show zero diff | PASS |
| Implements contract | `UnifiedGatewaySkeletonImpl` satisfies `UnifiedGatewayInterfaceContract` | PASS |
| No live call | No fetch, no network, no provider API key in new files | PASS |
| Conformance tests present | All 10+ required test cases added | PASS |
| Type check | `npm run check` PASS | PASS |
| Test run | `npm test` PASS | PASS |
| GC-023 | No file exceeds hard threshold | PASS |
| Credential shielding | `credentialShielded: true` on all error envelopes; secret not in JSON output | PASS |
| Name collision avoided | `UnifiedGatewaySkeletonImpl` absent from repo before authoring | PASS |
| Agent Operation Trace Block | Expected and actual changed set recorded | PASS |
| Public Export Disposition | `DEFERRED_PRIVATE_ONLY` in worker return | PASS |
| Worker did not commit | HEAD stayed `executionBaseHead` | PASS |
| Diff hygiene | `git diff --check` PASS | PASS |
| Reviewer-fast | `python governance/compat/run_worker_return_fast_gate.py` PASS | PASS |

---

## Acceptance Criteria

| # | Criterion | Verification |
|---|---|---|
| AC1 | `UnifiedGatewaySkeletonImpl` satisfies `UnifiedGatewayInterfaceContract` at compile time | `npm run check` PASS |
| AC2 | All four methods return correct shape on happy path | conformance tests PASS |
| AC3 | All four methods return `GatewayErrorEnvelope` with `credentialShielded: true` when policy denied | conformance tests PASS |
| AC4 | `JSON.stringify(response)` never contains injected secret values | credential shielding test PASS |
| AC5 | No live network call in any test or source file | no `fetch`, no provider URL in new files |
| AC6 | All existing tests continue to PASS | `npm test` PASS |
| AC7 | `rawMemoryReleased=false` on all closure artifacts | front-matter literal |
| AC8 | GC-051 entries added for new source and test files | registry entries present |

---

## Roadmap-To-Work-Order Trace Matrix

| Roadmap deliverable | Roadmap ref | Work order section | Owner |
|---|---|---|---|
| D1 GC-018 baseline | Deliverables D1 | Authorization Preconditions | orchestrator |
| D2 Work order | Deliverables D2 | this document | orchestrator |
| D3 Skeleton class | Deliverables D3 | IS-1, Write Ownership | worker |
| D4 Barrel edit | Deliverables D4 (IS-2) | IS-2 | worker |
| D5 Conformance tests | Deliverables D5 | IS-3, Execution Plan step 4 | worker |
| D6 GC-051 registry entries | Deliverables D6 | Write Ownership | worker |
| D7 Worker return | Deliverables D7 | Write Ownership | worker |
| D8 Completion review | Deliverables D8 | Reviewer Closure Conversion Block | reviewer |
| AC1 implements contract | AC1 | Acceptance Criteria AC1 | worker |
| AC2 happy-path shapes | AC2 | Acceptance Criteria AC2 | worker |
| AC3 error envelope | AC3 | Acceptance Criteria AC3 | worker |
| AC4 credential shielding | AC4 | Acceptance Criteria AC4 | worker |
| AC5 no live call | AC5 | Acceptance Criteria AC5 | worker |
| AC6 existing tests PASS | AC6 | Acceptance Criteria AC6 | worker |
| AC7 rawMemoryReleased | AC7 | Acceptance Criteria AC7 | worker/reviewer |
| AC8 GC-051 entries | AC8 | Acceptance Criteria AC8 | worker |

## Review Gate

The reviewer must verify, on the committed range, before declaring ACCEPT:
- All AC1-AC8 satisfied with cited evidence.
- `UnifiedGatewaySkeletonImpl` implements all four methods of
  `UnifiedGatewayInterfaceContract`.
- No live network call in new source or test files.
- `GatewayErrorEnvelope.credentialShielded` is `true` on all denial paths.
- `npm run check` and `npm test` PASS.
- Pre-closure autorun gate PASSes on material range.

## Closure Checklist

- [x] Fresh GC-018 baseline exists and is cited.
- [x] Operator authorization exists and is cited.
- [x] Worker return records changed files, gate output, and AC evidence.
- [x] Skeleton class implements all four interface methods (AC1, AC2).
- [x] All error envelopes have `credentialShielded: true` (AC3).
- [x] Credential shielding test passes (AC4).
- [x] No live network call (AC5).
- [x] All existing tests PASS (AC6).
- [x] `rawMemoryReleased=false` on all closure artifacts (AC7).
- [x] GC-051 registry entries added (AC8).
- [x] `MGW-001` coverage note recorded: stays `PARTIAL_RECHECK_REQUIRED`.
- [x] Pre-closure autorun gate PASS on the material range.
- [x] Completion review authored with disposition.
- [x] Session continuity synced (front door, state, handoff).

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_MODEL_GATEWAY_C02_P4A_UNIFIED_GATEWAY_RUNTIME_SKELETON_COMPLETION_2026-06-15.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | P4A roadmap | Roadmap remains planning parent; closure recorded here and in completion review | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | GC-051 aggregate drift check PASS | PASS |
| Registry Markdown | N/A with reason: no markdown registry owner exists for this GC-051 entry | BLOCKED with reason | BLOCKED with reason |
| External evidence digest | N/A with reason: repo-local source, tests, and governance gates only | N/A_WITH_REASON | N/A with reason |
| System loop interlock | N/A with reason: no system-loop registry or interlock surface changed | N/A_WITH_REASON | N/A with reason |
| Session continuity | front door, generated state, active handoff | closure sync updates mode, next move, and HEAD pointer | PASS |
| Worker return reviewed | P4A worker return | reviewer-return steward PASS | PASS |
| Runtime/provider/live proof | N/A with reason: no live/provider claim authorized or made | N/A_WITH_REASON | N/A with reason |
| Public-sync | N/A with reason: private provenance only | N/A_WITH_REASON | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Criterion | Required value | Observed value | Status |
|---|---|---|---|
| Existing receipt primitive only | P4A must not add a new receipt acceptance engine | `GatewayReceiptBuilder` remains unmodified; skeleton emits receipt obligations only | PASS |
| Execute receipt obligation | allowed execute response carries a bounded obligation string | `skeleton_execute_receipt_required` | PASS |
| Stream receipt obligation | allowed stream chunk carries a bounded obligation string | `skeleton_stream_receipt_required` | PASS |
| Embedding receipt obligation | allowed embedding response carries a bounded obligation string | `skeleton_embedding_receipt_required` | PASS |
| No new acceptance claim | P4A must not claim receipt acceptance, public readiness, or live proof | completion claim boundary keeps P4A local deterministic only | PASS |

## Operator Checkpoint

The operator must intervene only for:
- Scope expansion beyond the P4A skeleton boundary.
- A decision to authorize live provider calls (P4B requires a separate GC-018).
- Any request to lift a forbidden-scope boundary (live/network, public-sync,
  existing-source mutation, governance-kernel surface).

No operator checkpoint is parked inside the normal worker-to-reviewer flow.

## Verification

Pre-closure autorun gate:

```sh
python governance/compat/run_agent_autorun_workflow_gate.py \
  --phase pre-closure --base c6c09ae3 --head HEAD
```

Must PASS on the material closure commit range before completion review
declares ACCEPT. Pre-commit hook runs automatically at every `git commit`.

---

## Return-To-Orchestrator Conditions

- `COMPLETE_PENDING_REVIEW` -- all deliverables authored, worker gates PASS, no commit.
- `BLOCKED_SCOPE_EXPANSION` -- repair would cross forbidden boundary.
- `BLOCKED_MISSING_AUTHORIZATION` -- GC-018 or operator authorization absent.

Worker must NOT commit, sync session state, or upgrade work-order status.

---

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Claude (orchestrator role -- authoring dispatch package) |
| Provider or surface | Claude Code (VSCode extension) |
| Session or invocation | 2026-06-15 P4A dispatch from HEAD `c6c09ae3` |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | Read (source files, P3 contract, P3 worker return, rewrite plan), Write (roadmap, GC-018, work order) |
| Target paths | roadmap; GC-018 baseline; this work order |
| Allowed scope source | Operator instruction 2026-06-15; P3 COMPLETE_PENDING_REVIEW; nextAllowedMove |
| Before status evidence | `git status --short` shows P3 untracked files; HEAD `c6c09ae3` |
| After status evidence | `git status --short` shows P3 + P4A untracked files (roadmap, GC-018, work order added); HEAD still `c6c09ae3` |
| Diff evidence | `git diff --check` PASS; no staged changes to existing files |
| Approval boundary | Operator authorized; fresh GC-018 exists; work order status DISPATCHED |
| Claim boundary | Repo-local trace only; no OS-level attribution, endpoint telemetry, public readiness, or production readiness claim |
| Agent type | Claude (orchestrator / worker) |
| Invocation ID | Dispatch from HEAD `c6c09ae3` on 2026-06-15 |
| Expected manifest | roadmap; GC-018 baseline; work order |
| Actual changed set | roadmap; GC-018 baseline; work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no protected path deleted or renamed |
