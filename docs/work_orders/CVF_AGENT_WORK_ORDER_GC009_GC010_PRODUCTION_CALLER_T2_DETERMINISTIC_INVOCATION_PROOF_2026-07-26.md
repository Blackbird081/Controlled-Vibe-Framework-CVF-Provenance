# CVF Agent Work Order - GC009 GC010 Production Caller T2 Deterministic Invocation Proof

Memory class: governed-worker-dispatch

Status: CLOSED_PASS_BOUNDED_GC009_INVOCATION_PROVEN

Batch ID: GC009-GC010-PCALLER-T2

Dispatch base head: `14434bf58`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: one delegated documentation-and-test worker

Reviewer/closer: Codex

Worker return path: `docs/reviews/CVF_GC009_GC010_PRODUCTION_CALLER_T2_DETERMINISTIC_INVOCATION_PROOF_WORKER_RETURN_2026-07-26.md`

Redispatch R1 original execution base head: `b1c6a0670`

R1 continuation authority: retain the accepted blocked worker return at commit
`08a965226`, repair only the reviewer-owned Worker Return Packet Shape Contract
omission, rerun pre-implementation, create the focused test, refresh the same
worker return, and stop without commit. No runtime or existing-test scope is
added.

Redispatch R2 prior clean execution head: `81951a6ed`

R2 continuation authority: R1 pre-implementation passed 76/77 checks but the
hard-coded historical base made the trace checker compare unrelated committed
packet and continuity paths against the retained worker return. No worker edit
occurred. Run pre-implementation against the clean current execution range
before editing, then perform the same unchanged two-path worker scope.

## Dispatch Prompt Envelope

Role: documentation-and-test worker for `GC009-GC010-PCALLER-T2`.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_GC009_GC010_PRODUCTION_CALLER_T2_DETERMINISTIC_INVOCATION_PROOF_2026-07-26.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: worker must capture the committed dispatch HEAD before edits.

Current-time notes: packet authored on 2026-07-26 after T1 material commit
`29e7d6956` and continuity commit `14434bf58`.

Do-not-misread notes: test-and-evidence work only. Do not change runtime,
existing tests, package metadata, governance, session, roadmap, public,
provider, deployment, or GC-010/T3/T4 surfaces.

Required first actions: read the startup front doors, guard orientation,
literal gotchas, `DESIGN.md`, this packet, its paired GC-018, all required
sources, and applicable checker sources; capture `executionBaseHead`; require
a clean worktree; run pre-implementation before editing.

Return contract: create exactly the focused test and worker return, run all
required proof and worker-return gates, leave changes uncommitted, and return
one terminal disposition.

## Purpose

Prove the T1 GC-009 composition at the real execute-route boundary with a
deterministic positive case and deterministic fail-closed negative case. The
test must exercise the actual POST route, shared gateway, shared engine, route
adapter, audit linkage, and evidence receipt while mocking the provider seam so
no network call occurs.

## Authority Chain

1. `AGENTS.md`;
2. `CVF_SESSION_MEMORY.md`;
3. `CVF_SESSION/ACTIVE_SESSION_STATE.json`;
4. `AGENT_HANDOFF_V52_2026-07-25.md`;
5. `docs/roadmaps/CVF_GC009_GC010_PRODUCTION_CALLER_AND_BOUNDED_E2E_RUNTIME_ROADMAP_2026-07-25.md`;
6. `docs/reviews/CVF_GC009_GC010_PRODUCTION_CALLER_T1_RUNTIME_COMPOSITION_COMPLETION_2026-07-26.md`;
7. `docs/baselines/CVF_GC018_GC009_GC010_PRODUCTION_CALLER_T2_DETERMINISTIC_INVOCATION_PROOF_2026-07-26.md`;
8. this work order.

The operator released packet authoring with T1 closure commit `29e7d6956`
already recorded. Codex accepted the
source-backed test-only shape and owns dispatch, review, closure conversion,
commit, and continuity updates. The worker owns no commit.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id GC009-GC010-PCALLER-T2 --title "GC009 GC010 Production Caller T2 Deterministic Invocation Proof" --date 2026-07-26 --base 14434bf58 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "T1 bounded closure at material commit 29e7d6956 and continuity commit 14434bf58" --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus `WORKER_MUST_NOT_COMMIT` profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced scaffold fields with exact source facts, test contract, manifests, gates, and closure route |
| checkerReadAheadConfirmation | dispatch-quality, dispatch tables, prompt envelope, handoff boundary, governed file size, worker-return quality, operation trace, and packet authority/encoding checker sources |
| docOnlyNewFields | batch and artifact names only; no runtime field is introduced |
| claimBoundary | packet authoring only; no T2 behavior is claimed |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| T1 independent closure | `docs/reviews/CVF_GC009_GC010_PRODUCTION_CALLER_T1_RUNTIME_COMPOSITION_COMPLETION_2026-07-26.md`; material commit `29e7d6956` | accepted bounded T1 composition and clean proof | PASS |
| continuity checkpoint | `CVF_SESSION/state/entries/gc009Gc010ProductionCallerT1RuntimeCompositionClosure20260726.json`; commit `14434bf58` | next action requires operator selection of T2 | PASS |
| operator selection | explicit operator selection after Codex recommended T2 first | authorization recorded here; no provider-local memory is authority | PASS |
| dispatch base isolation | clean `git status --short` at `14434bf58` before authoring | packet committed before worker execution | PASS |

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intakeSummary | add focused deterministic invocation proof for the closed T1 composition |
| scopeClassification | bounded test and evidence tranche |
| riskSensitivity | R1 |
| selectedRouteMode | MULTI_AGENT_MULTI_ROLE |
| roleSeparationBasis | Codex reviewer/dispatcher, one no-commit worker, Codex reviewer/closer |
| escalationCondition | source contradiction or any need outside the exact two-path worker manifest |

## Agent Roles

| Role | Responsibility |
|---|---|
| Operator | selected T2 packet authoring |
| Codex reviewer/dispatcher | source-verify, gate, commit, and dispatch this packet |
| Worker | create the focused test and worker return; run proof; do not commit |
| Codex reviewer/closer | independently inspect tests and claims, repair allowed closure paths if needed, run closure gates, commit accepted work, and update continuity |

## Scope

### Allowed implementation

Create one new route-level test file that:

1. imports and invokes the real `POST` route;
2. does not mock `cvf-guard-contract`, `route-guard-gateway`,
   `mandatory-gateway-singleton`, or `guard-engine-singleton`;
3. mocks `executeAI` so no network call can occur;
4. mocks existing authentication, enforcement, quota, and durable event
   boundaries only as needed to reach and observe the T1 composition;
5. resets shared engine, shared gateway, rate-limit stores, mocks, and process
   environment for every case;
6. proves a source-backed ALLOW request reaches `executeAI` exactly once;
7. proves a source-backed gateway BLOCK returns 400 and reaches `executeAI`
   zero times;
8. proves each case emits one `MANDATORY_GATEWAY_EVALUATED` event, preserves
   the supplied request ID, links the returned audit ID into the envelope, and
   returns an evidence receipt with the same decision;
9. runs with fake credentials only and performs no live call.

### Explicitly excluded

- edits to runtime/source code;
- edits to `route.test.ts` or any existing test;
- new helpers, fixtures, snapshots, packages, dependencies, or lockfiles;
- browser, provider, network, CLI, MCP, or live governance proof;
- GC-010 `AgentExecutionRuntime`;
- T3-T4, new operator surfaces, session state, public-sync, push, deployment,
  or production-readiness claims;
- governance checker, hook, registry, standard, roadmap, baseline, work-order,
  or completion-review edits by the worker.

## Write Ownership

### Worker-Owned Writable Paths

1. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.mandatory-gateway-invocation.test.ts`
2. `docs/reviews/CVF_GC009_GC010_PRODUCTION_CALLER_T2_DETERMINISTIC_INVOCATION_PROOF_WORKER_RETURN_2026-07-26.md`

### Reviewer-Owned Closure Paths

- `docs/reviews/CVF_GC009_GC010_PRODUCTION_CALLER_T2_DETERMINISTIC_INVOCATION_PROOF_COMPLETION_2026-07-26.md`;
- this work order;
- companion GC-018 baseline;
- companion roadmap;
- applicable system-chain source entry and generated aggregate;
- control matrix and gap README only if T2 acceptance changes their current
  verified semantics;
- active session source fragments, generated state, bootstrap, memory front
  door, and active handoff.

## Required First Reads

| Source | Required action | Reason |
|---|---|---|
| `AGENTS.md` | READ | repository authority and workflow |
| `CVF_SESSION_MEMORY.md` | READ | current continuity front door |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | READ | active state registry |
| `AGENT_HANDOFF_V52_2026-07-25.md` | READ | active handoff |
| `docs/reference/guard_orientation/README.md` | READ | task and role guard orientation |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ | governed artifact literal discipline |
| `DESIGN.md` | READ | Web-surface design boundary, even though T2 changes tests only |
| companion roadmap, GC-018, and this work order | READ | exact authority and scope |
| T1 completion review | READ | predecessor evidence and claim boundary |
| every source path in the Source Verification Block | SOURCE_VERIFIED | current runtime and test contract |
| checker sources in the Checker Source Read-Ahead Block | READ | required literal and gate shapes |

## Pre-Flight Checks

Before editing:

1. capture `executionBaseHead` with `git rev-parse --short HEAD`;
2. require empty `git status --short --untracked-files=all`;
3. confirm this work order and GC-018 are committed and dispatch-ready;
4. for initial execution, confirm the focused test and worker return do not
   exist; for R1, confirm the focused test is absent and the retained worker
   return is the accepted `BLOCKED_SCOPE_EXPANSION_REQUIRED` return committed
   at `08a965226`;
5. confirm `route.ts` remains 955 lines and `route.test.ts` remains 1153 lines;
6. confirm `route.ts` calls `runExecuteRouteMandatoryGateway` before
   `executeAI`;
7. confirm no forbidden gateway/engine mock exists in the new test;
8. set `$executionBaseHead = git rev-parse --short HEAD`, then run
   pre-implementation with `--base $executionBaseHead --head HEAD` while the
   captured current execution worktree is still clean;
9. stop on stale source or unexpected changed path.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| T1 closure releases source-verified T2 packet selection only | VALUE_SET | `docs/reviews/CVF_GC009_GC010_PRODUCTION_CALLER_T1_RUNTIME_COMPOSITION_COMPLETION_2026-07-26.md` | Follow-Up Routing Matrix; Claim Boundary | `SEPARATE_RUNTIME_TRANCHE` | T1 completion review | ACCEPT |
| T2 requires positive provider-seam reach and negative no-reach proof | VALUE_SET | `docs/roadmaps/CVF_GC009_GC010_PRODUCTION_CALLER_AND_BOUNDED_E2E_RUNTIME_ROADMAP_2026-07-25.md` | T2 - Positive And Fail-Closed Negative Invocation Proof | `T2` | roadmap tranche contract | ACCEPT |
| Route calls T1 wrapper before provider routing | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 560-590 | `runExecuteRouteMandatoryGateway` | execute POST route | ACCEPT |
| Existing provider execution seam | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 771-778 | `executeAI` | execute POST route | ACCEPT |
| Wrapper uses the shared mandatory gateway by default | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-guard-gateway.ts` | lines 43-47 | `getSharedMandatoryGateway` | route gateway adapter | ACCEPT |
| Wrapper fails closed with status 400 before returning a guard result | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-guard-gateway.ts` | lines 111-146 | `runExecuteRouteMandatoryGateway` | route gateway adapter | ACCEPT |
| Gateway singleton uses canonical shared engine with no bypass list | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/mandatory-gateway-singleton.ts` | lines 20-33 | `getSharedMandatoryGateway` | cvf-web gateway singleton | ACCEPT |
| Engine singleton exposes a test reset | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/guard-engine-singleton.ts` | full file | `resetSharedGuardEngine` | cvf-web engine singleton | ACCEPT |
| Gateway singleton exposes a test reset | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/mandatory-gateway-singleton.ts` | full file | `resetSharedMandatoryGateway` | cvf-web gateway singleton | ACCEPT |
| Explicit request action is preserved | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-route-guards.ts` | lines 63-80 | `resolveGuardAction` | execute route guard helper | ACCEPT |
| OPERATOR INTAKE allows analysis but not governance deletion | LITERAL_INVARIANT | `EXTENSIONS/CVF_GUARD_CONTRACT/src/guards/authority-gate.guard.ts` | `AUTHORITY_MATRIX`; `AuthorityGateGuard.evaluate` | `OPERATOR` | authority gate | ACCEPT |
| Gateway event includes decision, allowed, bypass, mode, request ID, blocker, and escalation fields | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-guard-gateway.ts` | lines 49-75 | `MANDATORY_GATEWAY_EVALUATED` | route gateway adapter | ACCEPT |
| Existing route suite defines stable environmental isolation | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.test.ts` | lines 1-120 | `beforeEach` | execute route test suite | ACCEPT |

## New Doc-Only Fields

| Proposed item | Meaning | Runtime/source status |
|---|---|---|
| `GC009-GC010-PCALLER-T2` | governed batch identifier | DOC_ONLY_NEW |
| focused test and review filenames | tranche artifact names | DOC_ONLY_NEW |

## Test Contract

### Shared setup

The new suite must:

- follow the existing route suite's fake-environment, authentication,
  enforcement, quota, audit, rate-limit, request-builder, and cleanup patterns;
- set both `CVF_RATE_LIMIT` and `CVF_PROVIDER_QUOTA_PER_MIN` to `10000`;
- reset rate-limit stores, shared mandatory gateway, and shared guard engine
  before each test;
- call `appendAuditEventMock.mockReset().mockResolvedValue(...)`;
- use a unique deterministic audit ID per case when useful;
- use only fake API key text;
- mock `executeAI`, but never mock or inject the T1 gateway, gateway singleton,
  shared engine, or route gateway adapter.

### Positive case

Use an authenticated admin/OPERATOR request with:

- explicit `requestId`;
- default or explicit INTAKE phase;
- R0 risk;
- an analysis action allowed by the OPERATOR INTAKE authority cell;
- an OpenAI provider label and fake key;
- mocked successful `executeAI` output that passes current validation.

Required assertions:

1. response follows the existing successful route shape;
2. `executeAI` is called exactly once;
3. one `MANDATORY_GATEWAY_EVALUATED` event has outcome and
   `gatewayDecision` equal to `ALLOW`;
4. all seven gateway payload keys exist and `gatewayRequestId` equals the
   supplied request ID;
5. returned envelope contains the deterministic audit event ID;
6. evidence receipt decision equals `ALLOW`.

### Fail-Closed Negative Case

Use the same authenticated upstream-permitted request shape, but set explicit
action `delete_governance`. The real authority gate must decide BLOCK.

Required assertions:

1. response status is 400;
2. `executeAI` is called zero times;
3. response `guardResult.finalDecision` equals `BLOCK`;
4. one `MANDATORY_GATEWAY_EVALUATED` event has outcome and
   `gatewayDecision` equal to `BLOCK`;
5. event payload `gatewayAllowed` is false,
   `gatewayRequestId` equals the supplied request ID, and
   `gatewayBlockedBy` identifies `authority_gate`;
6. returned envelope contains the deterministic audit event ID;
7. evidence receipt decision equals `BLOCK`.

### Mock Boundary Negative Scan

The new file must contain zero mock declarations or injected doubles for:

- `route-guard-gateway`;
- `mandatory-gateway-singleton`;
- `guard-engine-singleton`;
- `cvf-guard-contract`;
- `runExecuteRouteMandatoryGateway`;
- `getSharedMandatoryGateway`;
- `getSharedGuardEngine`.

Imports of reset functions are allowed and required.

## Terminal Disposition Enum

Return exactly one:

- `COMPLETE_PENDING_REVIEW`
- `BLOCKED_STALE_EXECUTION_BASE`
- `BLOCKED_SOURCE_DRIFT`
- `BLOCKED_TEST_FAILURE`
- `BLOCKED_SCOPE_EXPANSION_REQUIRED`

Only `COMPLETE_PENDING_REVIEW` may accompany a closure recommendation.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order instruction | Required evidence |
|---|---|---|
| positive deterministic case reaches execution seam | Positive case | actual POST plus `executeAI` count one |
| negative deterministic case fails closed | Negative case | actual POST, 400 response, `executeAI` count zero |
| exercise T1 composition | mock-boundary scan | no gateway, adapter, engine, or contract mocks |
| receipt/evidence | both case contracts | audit payload, linked event ID, response receipt |
| no live provider | shared setup | fake key and mocked `executeAI` |
| smallest changed set | exact two-path worker manifest | git name-status |
| later holds | exclusions and claim boundary | no GC-010 or T3-T4 mutation |

## Design Control Carry-Forward

The worker must not:

- turn this proof into runtime remediation;
- inject a fake gateway or engine decision;
- use upstream enforcement BLOCK as the negative case;
- claim a provider invocation because the mocked provider seam was called;
- touch the existing near-threshold route test;
- weaken assertion depth to status-only proof;
- infer GC-010 or paired-gap closure from GC-009 T2 evidence.

## Worker Autonomy / No-Question Rule

Repair allowed-scope test and worker-return gate failures directly. Return to
the orchestrator only when current source contradicts the packet, a required
proof cannot be achieved without a forbidden path, or the dispatch base is
stale.

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| focused T2 test | create both required route-level cases and all assertions |
| worker return | create from the checker-safe full-gate skeleton and record fresh evidence |

## Required Artifact Manifest

| Artifact class | Path | Owner | Required disposition |
|---|---|---|---|
| deterministic invocation test | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.mandatory-gateway-invocation.test.ts` | worker | new |
| worker return | `docs/reviews/CVF_GC009_GC010_PRODUCTION_CALLER_T2_DETERMINISTIC_INVOCATION_PROOF_WORKER_RETURN_2026-07-26.md` | worker | new |

## Forbidden Path Manifest

| Path or class | Disposition |
|---|---|
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | forbidden |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.test.ts` | forbidden |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-guard-gateway.ts` | forbidden |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/mandatory-gateway-singleton.ts` | forbidden |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/guard-engine-singleton.ts` | forbidden |
| `EXTENSIONS/CVF_GUARD_CONTRACT/` | forbidden |
| package manifests and lockfiles | forbidden |
| `docs/baselines/`, `docs/work_orders/`, `docs/roadmaps/` | forbidden |
| governance, session, active handoff, public-sync, deployment | forbidden |

## Forbidden Filesystem State At Dispatch

| State | Requirement |
|---|---|
| pre-existing tracked changes | none |
| staged changes | none |
| untracked files | none |
| focused test already present | must be absent |
| worker return already present | must be absent |

## Required Proof Manifest

| Proof | Atomic required evidence |
|---|---|
| positive invocation | POST response success; gateway ALLOW event; request ID; envelope event ID; receipt ALLOW; provider mock count one |
| negative fail closed | POST 400; guard BLOCK; gateway BLOCK event; request ID; blocker ID; envelope event ID; receipt BLOCK; provider mock count zero |
| actual T1 chain | zero forbidden gateway/engine mock declarations |
| regression | focused test plus existing 31-test route suite |
| T1 regression bundle | existing mandatory gateway, singleton, and adapter suites |
| type safety | cvf-web TypeScript check |
| maintainability | governed file-size gate |
| changed set | exactly the two worker-owned paths |
| handoff | worker-return fast gate PASS and HEAD unchanged |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | no-commit worker and reviewer/closer | exact test/evidence scope | Vitest and worker return | repository workflow | `TEST_EXECUTION_AUTHORIZED` |
| `EXTERNAL_AGENT_CLI_MCP` | not used | no external invocation or adapter | N/A with reason: local deterministic test only | none | `NOT_APPLICABLE_WITH_REASON` |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | current runtime source verification and deterministic local proof |
| Matching local-view guard | N/A with reason: no outside artifact |
| Owner surface | this work order |
| Disposition | `ABSORBED_AFTER_CVF_PROOF` for bounded local T2 behavior |
| Claim boundary | no external completeness or absorption claim |

## Agent Handoff Contract Control Block

Contract source:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | Codex dispatcher; one worker; Codex reviewer/closer |
| phase | dispatch, no-commit execution, independent review, reviewer commit, session sync |
| baseHeadFor(phase) | dispatchBaseHead=`14434bf58`; executionBaseHead=worker capture; closureBaseHead=reviewer capture |
| changedSetScope(phase) | worker exact two-path manifest; reviewer closure paths separately owned |
| traceScope(phase, actor) | each actor records its own commands, changed set, tests, and claim boundary |
| commitOwner(phase) | worker=`WORKER_MUST_NOT_COMMIT`; reviewer owns accepted material and continuity commits |
| crossBatchIsolation | clean worktree required at worker start; unrelated state blocks execution |
| nextMoveSurfaces | reviewer alone updates roadmap, work order, system-chain surfaces, session state, memory front door, and handoff after acceptance |

## Legacy Absorption Coverage Index Disposition

`NOT_APPLICABLE_WITH_REASON`: this is a focused regression proof for an
already-source-owned runtime edge. It does not intake or reconcile legacy
corpus material.

## Evidence Reuse And Encoding Plan

| Evidence class | Verification mode | Handling |
|---|---|---|
| T1 predecessor commits and completion review | `REUSE_PRIOR_VERIFICATION` | cite exact paths and commits |
| current runtime/test source | `RECOMPUTE_REQUIRED` | read current dispatch HEAD |
| test outcomes | `RECOMPUTE_REQUIRED` | worker runs fresh commands |
| reviewer closure gates | `REVIEWER_RECOMPUTE_ONLY` | worker must not claim closure |
| encoding | ASCII-only | no copied Unicode evidence |

## Package Skill Productionization Control Block

- SOP source: `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md`
- Current phase: NOT_APPLICABLE_WITH_REASON
- Target lifecycle state: NOT_APPLICABLE_WITH_REASON
- Prior phase evidence: N/A with reason: T2 tests an existing Web runtime edge and does not create an ASSF package skill.
- Next forbidden skip: no skill certification, truth packet, adapter, activation, or live-proof claim may be inferred.
- Runtime/provider proof: provider execution is mocked; no live-provider proof is authorized.
- Claim boundary: package-skill productionization is outside this tranche.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation Storage Layout Block | N/A with reason: T2 creates one focused test and one worker return; it does not split, relocate, refactor, or redesign durable foundation storage |
| Protected storage paths | N/A with reason: no foundation storage topology path is writable |
| Follow-up condition | separate governed work order required before any foundation storage change |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_GC009_GC010_PRODUCTION_CALLER_T2_DETERMINISTIC_INVOCATION_PROOF_COMPLETION_2026-07-26.md` |
| reviewerOwnedClosurePaths | completion review; this work order; baseline; roadmap; source-owned system-chain semantics if applicable; generated aggregate if source changes; session continuity surfaces |
| closureOwner | Codex |
| workerCommitPermission | FORBIDDEN |
| closureRule | worker `COMPLETE_PENDING_REVIEW` is evidence only; Codex independently reruns proof and decides closure |

## Execution Plan

1. Complete preflight and record `executionBaseHead`.
2. Read the worker-return checker and generate a full-gate worker-return
   skeleton at the exact path.
3. Create the focused test file only.
4. Run focused tests during iteration.
5. Run the focused test with the existing route suite.
6. Run the T1 regression bundle and cvf-web typecheck.
7. Run file-size and pre-implementation gates.
8. Complete worker return with fresh outputs.
9. Run worker-return fast gate.
10. Verify exact two-path changed set, clean diff check, no staged files, and
    unchanged HEAD.
11. Return the terminal disposition to Codex.

## Evidence Requirements

Worker return must include:

- `executionBaseHead`;
- exact commands and pass counts;
- positive and negative assertion summary;
- forbidden-mock negative-search command and zero-match result;
- `git diff --name-status`;
- `git status --short`;
- `git diff --cached --name-status`;
- `git diff --check`;
- final line count of the new test;
- no-live statement;
- no-commit statement;
- limitations: GC-010 and T3-T4 remain held.

## Epistemic Process Block

### Expected Result / Prediction

Authorized OPERATOR analysis should reach the mocked provider seam once.
Unauthorized `delete_governance` should be blocked by `authority_gate` and
never reach that seam.

### Evidence Comparison

Compare actual decisions, provider counts, request IDs, audit linkage, and
receipt decisions with the prediction.

### Contradiction Or Gap Disposition

If the real chain cannot produce both results within the two-path manifest,
return the applicable blocked token. Do not change runtime.

### Claim Update

Worker may claim only deterministic local evidence pending independent review.

## Acceptance Criteria

- [x] Worker starts from the committed dispatch HEAD and clean worktree.
- [x] Only the two worker-owned paths change.
- [x] New suite uses actual POST, gateway adapter, gateway singleton, and
  guard engine.
- [x] Positive case proves ALLOW and provider mock count one.
- [x] Negative case proves authority-gate BLOCK and provider mock count zero.
- [x] Both cases prove gateway audit, request-ID preservation, envelope
  linkage, and matching evidence-receipt decision.
- [x] No live provider or network call occurs.
- [x] Focused and regression suites pass.
- [x] cvf-web TypeScript check passes.
- [x] Governed file-size gate passes.
- [x] Worker-return fast gate passes.
- [x] HEAD remains unchanged and nothing is staged.
- [x] GC-010 and T3-T4 remain held.

## Review Gate

Codex must inspect the actual mock graph, independently run both focused cases
and the regression bundle, verify zero forbidden gateway mocks, inspect the
audit and receipt assertions, run closure gates over a real changed range, and
decide whether the evidence proves only bounded GC-009 invocation.

## Successor Authorization Boundary

No additional checkpoint is required for the worker to execute this committed
packet. A fresh operator or roadmap decision remains required before T3,
GC-010, live proof, public-sync, push, or deployment.

## Worker Return Packet Shape Contract

workerReturnPath:
`docs/reviews/CVF_GC009_GC010_PRODUCTION_CALLER_T2_DETERMINISTIC_INVOCATION_PROOF_WORKER_RETURN_2026-07-26.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

requiredEvidenceTerms: executionBaseHead; git status --short; git diff
--name-status; git diff --cached --name-status; git diff --check; focused
tests; regression tests; typecheck; governed file size; no live provider; no
commit.

requiredSections: Purpose; Scope / Methodology; Findings / Position; Risk / Corrective Action; Claim Boundary; Agent Operation Trace Block; Delta Execution Claim Boundary Control Block; Public Export Disposition; External Knowledge Intake Routing; Rescan Intelligence Hardening; Corpus Completeness And Report Integrity; Finding-To-Governance Learning Disposition; Epistemic Process Block; Machine Closure Package

naInstruction: use `N/A with reason` only when the named evidence class is
genuinely not applicable.

Shape-list rule: list required worker-output section names without heading
prefixes. Use actual heading syntax only for real sections.

## Verification Commands

Run from repository root:

```powershell
$executionBaseHead = git rev-parse --short HEAD
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base $executionBaseHead --head HEAD
Set-Location EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web
npx vitest run src/app/api/execute/route.mandatory-gateway-invocation.test.ts
npx vitest run src/app/api/execute/route.mandatory-gateway-invocation.test.ts src/app/api/execute/route.test.ts
npx vitest run src/lib/route-guard-gateway.test.ts src/lib/mandatory-gateway-singleton.test.ts
npx tsc --noEmit
Set-Location ../../../..
python governance/compat/check_governed_file_size.py --enforce
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git status --short
git diff --cached --name-status
```

The parent command timeout must exceed the combined child test timeout. Split
commands if the execution surface cannot guarantee that ceiling.

## Closure Checklist

- [x] Commit mode and all three base-head lifecycle fields are recorded.
- [x] Worker changed set matches the required artifact manifest.
- [x] Required proof manifest is complete.
- [x] No forbidden path changed.
- [x] Worker return remains pending review and does not claim closure.
- [x] Reviewer independently validates behavior and closure evidence.
- [x] Reviewer converts accepted work into a completion review and commits.
- [x] Reviewer updates roadmap, system-chain semantics if applicable, session
  state, memory front door, and active handoff.

## Return-To-Orchestrator Conditions

Return without scope expansion when:

- dispatch or execution base is stale;
- a required current symbol or path differs from Source Verification;
- actual gateway behavior cannot yield both required cases;
- any required assertion needs runtime or existing-test edits;
- a forbidden path is already dirty;
- live provider, browser, CLI/MCP, session, public, T3-T4, GC-010, push, or
  deployment work is needed;
- a required gate fails outside the exact worker scope.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: `ADIF-0001`, `ADIF-0002`, `ADIF-0014`, `ADIF-0015`,
`ADIF-0020`, `ADIF-0021`, `ADIF-0028`, `ADIF-0029`, `ADIF-0033`,
`ADIF-0044`, `ADIF-0045`, `ADIF-0007`, `ADIF-0016`, `ADIF-0017`,
`ADIF-0024`, `ADIF-0031`, `ADIF-0039`, `ADIF-0043`, `ADIF-0049`,
`ADIF-0006`.

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --json --max-results 50` |
| Returned defect count | 20 |
| Disclosed defectIds | all 20 IDs listed above |
| Dispatch impact | current source verification, exact manifests, no runtime edits, forbidden-mock scan, stable rate-limit isolation, full worker-return gate, and no-commit closure conversion |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_tables.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_agent_packet_authority_and_encoding.py` |
| literalTokensReviewed | `WORKER_MUST_NOT_COMMIT`; exact manifest headings; Source Verification columns; Agent Handoff rows; `completionReviewPath`; `reviewerOwnedClosurePaths`; ASCII-only prose |
| gateRunPurpose | confirm the source-backed worker-executable packet before release |
| claimBoundary | gate compliance does not prove T2 invocation |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex packet author and reviewer/dispatcher |
| Provider or surface | local Codex workspace |
| Session or invocation | GC009-GC010-PCALLER-T2 work-order authoring, 2026-07-26 |
| Working directory | repository root |
| Command or tool surface | governed reads, `rg`, git checks, scaffold helper, ADIF resolver, patch edits, workflow gates |
| Target paths | this work order; paired GC-018; companion roadmap |
| Allowed scope source | explicit operator T2 selection backed by material commit `29e7d6956` |
| Before status evidence | clean worktree at `14434bf58` |
| After status evidence | exact three-path packet-author set |
| Diff evidence | `git status --short`; `git diff --name-status`; `git diff --check` |
| Approval boundary | packet authoring, review, commit, and dispatch only |
| Claim boundary | no worker implementation or T2 behavior yet |
| Agent type | reviewer/dispatcher |
| Invocation ID | `gc009-gc010-production-caller-t2-work-order-2026-07-26` |
| Expected manifest | this work order; paired GC-018; companion roadmap |
| Actual changed set | must match expected manifest before packet commit |
| Manifest delta | none expected |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | deterministic test of the existing T1 GC-009 composition |
| claimDisposition | `BOUNDED_CLAIM_WITH_EVIDENCE`: independent closure accepts local GC-009 invocation |
| receiptEvidence | `CVF_RECEIPT_PRESENT`: ALLOW and BLOCK receipts match gateway decisions |
| actionEvidence | `ACTION_EVIDENCE_PRESENT`: provider seam counts are one and zero |
| invocationBoundary | local Vitest POST calls only; provider adapter mocked |
| interceptionBoundary | no external-agent interception, proxy, wrapper, or arbitrary process control |
| claimLanguage | bounded local GC-009 invocation proven after independent review |
| forbiddenExpansion | no runtime edit, live provider, GC-010, T3-T4, new operator surface, public-sync, push, deployment, or production-readiness claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is a private provenance work order with no matching public-sync
artifact.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this work order | `Status: CLOSED_PASS_BOUNDED_GC009_INVOCATION_PROVEN` | PASS |
| Completion or reviewer artifact | T2 completion review | same closed status | PASS |
| Roadmap state | companion roadmap | T2 pass bounded; T3-T4 held | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | no corpus state change | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | no corpus row required | PASS |
| External evidence digest | N/A with reason: no external evidence consumed | N/A with reason | N/A with reason |
| System loop interlock | paired GC-009/GC-010 gap entry and index | GC-009 accepted; GC-010 remains open | PASS |
| Session continuity | active state, front door, and handoff | separate sync follows material commit | N/A with reason |
| Public export | this work order | `DEFERRED_PRIVATE_ONLY` | PASS |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| positive gateway decision | ALLOW receipt, audit event, and one provider call | PASS |
| negative gateway decision | BLOCK receipt, `authority_gate` event, and zero provider calls | PASS |
| seven-field audit payload | exact key set in both cases | PASS |
| deterministic audit linkage | event ID appears in both response envelopes | PASS |
| live provider receipt | N/A with reason: no live call authorized or made | N/A_WITH_REASON |

## Claim Boundary

This work order is closed with one accepted deterministic route-level test and
one reviewed worker return. It does not authorize runtime remediation,
provider/live proof, GC-010, T3-T4, new surfaces, public export, push,
deployment, production readiness, or paired-gap closure.

## Operator Checkpoint

SATISFIED: the operator explicitly selected T2 after commits `29e7d6956` and
`14434bf58`. This checkpoint releases only the exact worker manifest above.
