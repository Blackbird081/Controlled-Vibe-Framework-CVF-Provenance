# CVF Agent Work Order: Model Gateway C-02 Provider Routing Boundary Rewrite For Claude - 2026-06-14

Memory class: FULL_RECORD

Status: DISPATCHED

Worker: Claude

Orchestrator / reviewer: Codex

Worker commit policy: WORKER_MUST_NOT_COMMIT

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `21f49ec5`

executionBaseHead: WORKER_MUST_CAPTURE_AT_START

closureBaseHead: REVIEWER_CAPTURE_AFTER_WORKER_RETURN

completionReviewPath:
`docs/reviews/CVF_MODEL_GATEWAY_C02_PROVIDER_ROUTING_BOUNDARY_REWRITE_COMPLETION_2026-06-14.md`

reviewerOwnedClosurePaths:

- `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_PROVIDER_ROUTING_BOUNDARY_REWRITE_FOR_CLAUDE_2026-06-14.md`
- `docs/reference/CVF_MODEL_GATEWAY_C02_PROVIDER_ROUTING_BOUNDARY_REWRITE_PLAN_2026-06-14.md`
- `docs/reviews/CVF_MODEL_GATEWAY_C02_PROVIDER_ROUTING_BOUNDARY_REWRITE_WORKER_RETURN_2026-06-14.md`
- `docs/reviews/CVF_MODEL_GATEWAY_C02_PROVIDER_ROUTING_BOUNDARY_REWRITE_COMPLETION_2026-06-14.md`
- session continuity files if Codex accepts and commits closure

rawMemoryReleased=false

## Purpose

Produce the fresh C-02 Model Gateway provider-routing boundary rewrite plan that
replaces the old held C-02 packet. The plan must use the completed Model Gateway
legacy recheck, current Model Gateway source, and Execution Plane Foundation
wrapper anchors to define planning boundaries only.

This is a documentation/planning work order. It does not authorize runtime,
source, test, provider, live-proof, public-sync, registry, or implementation
work.

## Fresh Rewrite Authority

The old held packet must not resume as-is:

`docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_EPF_PROVIDER_ROUTING_BOUNDARY_PLANNING_FOR_CLAUDE_2026-06-13.md`

This fresh rewrite is released by:

- `docs/reference/CVF_MODEL_GATEWAY_LEGACY_ABSORPTION_RECHECK_PLAN_2026-06-13.md`;
- `docs/reviews/CVF_MODEL_GATEWAY_LEGACY_ABSORPTION_COVERAGE_INDEX_COMPLETION_2026-06-13.md`;
- `docs/reviews/CVF_LEGACY_COVERAGE_INDEX_DISPATCH_GUARD_HARDENING_COMPLETION_2026-06-14.md`;
- `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` row `MGW-001`.

Claude must not reopen or continue the old held work order. Use this work order
only.

## Legacy Absorption Coverage Index Disposition

| Field | Evidence |
| --- | --- |
| Coverage index | `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` |
| Stable row id | `MGW-001` |
| Coverage status | `PARTIAL_RECHECK_REQUIRED` |
| Release basis | Bounded recheck closed; C-02 may resume only as `RESUME_WITH_REWRITE` |
| Required disposition in worker plan | The plan must explicitly disposition strategy-layer depth, routing-policy-engine pipeline, dynamic model registry, integration-flow boundary, gateway-interface boundary, and AI Gateway deferral |
| Forbidden shortcut | Do not resume the old current-source-only C-02 packet |

## Reviewer Closure Conversion Block

Codex owns final material closure, completion review, committed-range
pre-closure, and session sync. Claude's writable paths are limited to the two
worker deliverables in this packet.

Claude returns `COMPLETE_PENDING_REVIEW` only after producing the two worker
deliverables and passing the worker pending-return gate.

## Authority Chain

| Authority | Role |
| --- | --- |
| Operator instruction on 2026-06-14 | Authorized Codex to issue the next Claude work order |
| `CVF_SESSION_MEMORY.md` and `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Current mode and next allowed move |
| `AGENT_HANDOFF_V18_2026-06-12.md` | Active handoff and parked checkpoints |
| `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` | `MGW-001` coverage status and C-02 rewrite requirement |
| `docs/reference/CVF_MODEL_GATEWAY_LEGACY_ABSORPTION_RECHECK_PLAN_2026-06-13.md` | Accepted/deferred/rejected legacy value map |
| `docs/reviews/CVF_MODEL_GATEWAY_LEGACY_ABSORPTION_COVERAGE_INDEX_COMPLETION_2026-06-13.md` | Codex closure and C-02 resume decision |
| This work order | Fresh Claude execution scope |
| Codex reviewer | Closure, commits, allowed repairs, and session sync |

Provider-specific memory files such as `CLAUDE.md`, Claude memory, Codex
memory, and IDE summaries are not CVF source authority. If read as local
operating guidance, re-verify every source fact against governed source before
citing it.

## Scope

Allowed:

- Read governed front-door, recheck, coverage index, Model Gateway source, and
  EPF wrapper-anchor source listed in Required First Reads.
- Reuse the completed legacy recheck instead of reading all legacy files again.
- Create the two worker deliverables listed in Required Artifact Manifest.
- Map current source surfaces to legacy accepted-value gaps.
- Recommend planning boundaries and later implementation prerequisites.

Forbidden:

- Runtime/source/test edits under `EXTENSIONS/`.
- Model Gateway implementation.
- EPF implementation.
- Provider/API calls, live governance proof, provider/model addition, package
  install, secret inspection, public-sync, or public catalog claim.
- Registry mutation, including the legacy coverage index and corpus registry.
- Session-state, handoff, front-door, or active review queue mutation.
- AI Gateway environment signal absorption, OS audit/control setup, endpoint
  monitoring, Document Translator, Policy_Local, EC activation/retrieval, T12,
  DEP2/Redis/receipt-anchor, raw memory release, co-work product development,
  high-risk promotion, or autonomous mutation.

Risk ceiling: R1 documentation/planning only.

## Agent Roles

| Role | Owner | Boundary |
| --- | --- | --- |
| Orchestrator / reviewer / committer | Codex | Dispatch work order, review returned artifacts, author reviewer closeout, commit accepted artifacts, and sync session continuity |
| Worker | Claude | Produce the two required worker deliverables only, run worker gates, and return `COMPLETE_PENDING_REVIEW` without committing |
| Operator | Human operator | Approves scope changes only when a blocked condition exceeds this work order |

## Pre-Flight Checks

Claude must capture `executionBaseHead`, run `git status --short`, read the
Required First Reads, and confirm the old held C-02 packet is not being resumed.
Stop before writing if unrelated dirty files would be overwritten or if any
Required First Read is missing.

## Write Ownership

Claude may write only:

- `docs/reference/CVF_MODEL_GATEWAY_C02_PROVIDER_ROUTING_BOUNDARY_REWRITE_PLAN_2026-06-14.md`
- `docs/reviews/CVF_MODEL_GATEWAY_C02_PROVIDER_ROUTING_BOUNDARY_REWRITE_WORKER_RETURN_2026-06-14.md`

Codex owns reviewer closure, completion review, commits, and session sync.

## Required First Reads

| File | Required use |
| --- | --- |
| `AGENTS.md` | active governance instructions and provider-specific memory boundary |
| `CVF_SESSION_MEMORY.md` | current mode and next allowed move |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | generated state registry |
| `AGENT_HANDOFF_V18_2026-06-12.md` | active handoff and parked checkpoints |
| `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` | `MGW-001` coverage row |
| `docs/reference/CVF_MODEL_GATEWAY_LEGACY_ABSORPTION_RECHECK_PLAN_2026-06-13.md` | accepted/deferred/rejected legacy value map |
| `docs/reviews/CVF_MODEL_GATEWAY_LEGACY_ABSORPTION_COVERAGE_INDEX_COMPLETION_2026-06-13.md` | Codex reviewer closure and C-02 decision |
| `docs/reviews/CVF_LEGACY_COVERAGE_INDEX_DISPATCH_GUARD_HARDENING_COMPLETION_2026-06-14.md` | guard closure and dispatch requirement |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_EPF_PROVIDER_ROUTING_BOUNDARY_PLANNING_FOR_CLAUDE_2026-06-13.md` | old held packet to avoid reusing |
| `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md` | Agent Operation Trace Block contract |
| `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | worker return and closure structure |
| `EXTENSIONS/CVF_MODEL_GATEWAY/README.md` | Model Gateway guard-contract boundary |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` | exported Model Gateway surfaces |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | current provider capability registry |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | current provider registry |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-contract.ts` | provider method contract |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-gate.ts` | provider method gate helpers |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | current routing request, decision, snapshot, and routing policy engine |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-health.ts` | current provider health monitor |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-policy.ts` | current gateway policy result boundary |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/stream-contract.ts` | current stream contract boundary |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/embedding-contract.ts` | current embedding contract boundary |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/README.md` | EPF gateway wrapper anchor |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/index.ts` | EPF source anchor for `modelGateway` and gateway wrapper surface |

Do not read broad `.private_reference/legacy/` content unless Codex explicitly
re-dispatches a new absorption work order. This C-02 rewrite uses the governed
legacy recheck artifacts as source authority.

## Evidence Reuse And Encoding Plan

verificationMode: REUSE_PRIOR_VERIFICATION

priorVerificationArtifact:
`docs/reference/CVF_MODEL_GATEWAY_LEGACY_ABSORPTION_RECHECK_PLAN_2026-06-13.md`

priorVerificationAnchor:
`MGW-001`; `C-02 Resume Decision`; `Accept/Defer/Reject Matrix`

freshRecomputeRequired: NO

recomputeReason: N/A with reason: bounded legacy recheck already completed and
this work order is a planning rewrite, not a fresh legacy absorption wave.

unicodePathHandling: literal paths with UTF-8-safe readers; do not normalize
legacy paths or filenames.

extractedTextAuthority: N/A with reason

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| EXISTS: Legacy coverage index has `MGW-001` for Model Gateway provider routing | `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` | line 78 | `MGW-001` | legacy coverage index | ACCEPT |
| VALUE_SET: `MGW-001` status is `PARTIAL_RECHECK_REQUIRED` | `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` | line 78 | `PARTIAL_RECHECK_REQUIRED` | legacy coverage index | ACCEPT |
| EXISTS: Model Gateway recheck decision is `RESUME_WITH_REWRITE` | `docs/reference/CVF_MODEL_GATEWAY_LEGACY_ABSORPTION_RECHECK_PLAN_2026-06-13.md` | line 182 | `RESUME_WITH_REWRITE` | C-02 Resume Decision | ACCEPT |
| EXISTS: Recheck requires AI Gateway deferral to be restated | `docs/reference/CVF_MODEL_GATEWAY_LEGACY_ABSORPTION_RECHECK_PLAN_2026-06-13.md` | line 224 | `AI Gateway deferral` | C-02 rewrite requirement | ACCEPT |
| EXISTS: Codex completion requires strategy-layer, routing-policy-engine, dynamic-registry, integration-flow, and gateway-interface dispositions | `docs/reviews/CVF_MODEL_GATEWAY_LEGACY_ABSORPTION_COVERAGE_INDEX_COMPLETION_2026-06-13.md` | lines 139-144 | `C-02 Resume Decision` | completion review | ACCEPT |
| EXISTS: Guard requires legacy coverage-index disposition for legacy-adjacent foundation/workflow-chain work orders | `governance/compat/check_work_order_dispatch_quality.py` | lines 481-508 | `_validate_legacy_coverage_index_disposition` | dispatch-quality checker | ACCEPT |
| EXISTS: Provider capability registry exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | line 42 | `PROVIDER_CAPABILITY_REGISTRY` | Model Gateway provider capability registry | ACCEPT |
| EXISTS: ProviderRegistry exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | line 30 | `ProviderRegistry` | Model Gateway provider registry | ACCEPT |
| EXISTS: ProviderMethodContract exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-contract.ts` | line 26 | `ProviderMethodContract` | provider method contract | ACCEPT |
| EXISTS: RoutingRequest exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | line 6 | `RoutingRequest` | routing policy | ACCEPT |
| EXISTS: RoutingDecision exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | line 14 | `RoutingDecision` | routing policy | ACCEPT |
| EXISTS: RoutingPolicyEngine exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | line 59 | `RoutingPolicyEngine` | routing policy | ACCEPT |
| EXISTS: buildRoutingPolicyContractSnapshot exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | line 43 | `buildRoutingPolicyContractSnapshot` | routing policy | ACCEPT |
| EXISTS: ProviderHealthMonitor exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-health.ts` | line 17 | `ProviderHealthMonitor` | provider health | ACCEPT |
| EXISTS: GatewayPolicyResult exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-policy.ts` | line 1 | `GatewayPolicyResult` | gateway policy | ACCEPT |
| EXISTS: StreamContract exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/stream-contract.ts` | line 7 | `StreamContract` | stream contract | ACCEPT |
| EXISTS: EmbeddingContract exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/embedding-contract.ts` | line 7 | `EmbeddingContract` | embedding contract | ACCEPT |
| EXISTS: EPF preserves `CVF_MODEL_GATEWAY` as gateway-facing wrapper anchor | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/README.md` | line 10 | `CVF_MODEL_GATEWAY` | Execution Plane Foundation README | ACCEPT |
| EXISTS: EPF source records `modelGateway` coordination anchor | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/index.ts` | line 713 | `modelGateway` | Execution Plane Foundation source | ACCEPT |

## New Doc-Only Fields

| Field | Purpose | Runtime authority |
| --- | --- | --- |
| `Boundary Disposition` | Classify each C-02 scope item as `INCLUDE_IN_BOUNDARY`, `DEFER_WITH_REASON`, `OUT_OF_SCOPE`, or `IMPLEMENTATION_PREREQUISITE` | DOC_ONLY_NEW |
| `Accepted Legacy Value Mapping` | Map the 12 accepted value keys from the recheck plan to current owner surfaces or gaps | DOC_ONLY_NEW |
| `C-02 Rewrite Plan` | Claude's planning deliverable | DOC_ONLY_NEW |
| `Future Implementation Candidate` | Names later code work that requires fresh GC-018 | DOC_ONLY_NEW |

## Intake Role Routing Decision

| Field | Decision |
| --- | --- |
| Intake summary | Operator asked Codex to continue by issuing a Claude work order after legacy guard hardening |
| Scope classification | bounded foundation/workflow-chain planning packet |
| Risk sensitivity | legacy-adjacent, provider-routing sensitive, but no runtime/provider/live/public work |
| Selected role route | routeMode=MULTI_AGENT_MULTI_ROLE; Codex orchestrates/reviews, Claude drafts worker deliverables |
| Role separation basis | Claude is worker under `WORKER_MUST_NOT_COMMIT`; Codex is reviewer/committer |
| Escalation condition | Stop for implementation, runtime/source/test changes, provider/live proof, public-sync, secrets, registry mutation, AI Gateway signal absorption, OS/endpoint control, or claim-boundary expansion |
| Disposition | DISPATCHED |

## Roadmap-To-Work-Order Trace Matrix

| Source requirement | Source | Worker instruction | Disposition |
| --- | --- | --- | --- |
| Fresh C-02 rewrite required | `docs/reference/CVF_MODEL_GATEWAY_LEGACY_ABSORPTION_RECHECK_PLAN_2026-06-13.md`; completion review | Produce a new C-02 rewrite plan, not the old held C-02 plan | ACCEPT |
| Coverage-index guard required | `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` row `MGW-001`; guard completion | Include `Legacy Absorption Coverage Index Disposition` | ACCEPT |
| Strategy-layer depth must be dispositioned | recheck plan accepted values | Plan must include/defer Execution Planner, Strategy Taxonomy, Feedback Loop, and Strategy Registry with reasons | ACCEPT |
| Routing-policy-engine pipeline must be dispositioned | recheck plan accepted values | Plan must include/defer PolicyDecision pipeline, merge engine, escalation policy, and constraint conflict resolution | ACCEPT |
| Dynamic model registry must be dispositioned | recheck plan accepted values | Plan must distinguish current provider capability registry from future dynamic model registry | ACCEPT |
| Integration-flow and gateway-interface boundary must be dispositioned | recheck plan accepted values | Plan must include/defer integration flow and unified execute/stream/embedding/health interface boundary | ACCEPT |
| AI Gateway family remains deferred | recheck plan and completion review | Restate privacy/GDPR deferral; do not scope environment signal capture | ACCEPT |

## Current Runtime Freshness Verification

| Runtime/source surface | Freshness check | Disposition |
| --- | --- | --- |
| Model Gateway exported surfaces | `rg -n "ProviderRegistry|PROVIDER_CAPABILITY_REGISTRY|RoutingPolicyEngine|RoutingRequest|RoutingDecision" EXTENSIONS/CVF_MODEL_GATEWAY/src` | CURRENT_SOURCE_SURFACE_FOUND |
| Model Gateway health/policy/stream/embedding contracts | `rg -n "ProviderHealthMonitor|GatewayPolicyResult|StreamContract|EmbeddingContract" EXTENSIONS/CVF_MODEL_GATEWAY/src` | CURRENT_SOURCE_SURFACE_FOUND |
| EPF gateway wrapper anchor | `rg -n "CVF_MODEL_GATEWAY|modelGateway|ExecutionGatewaySurface|createExecutionGatewaySurface" EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION` | CURRENT_SOURCE_SURFACE_FOUND |
| Legacy recheck artifacts | coverage index, recheck plan, completion review | CURRENT_GOVERNED_EVIDENCE_FOUND |

## Negative Search And Collision Discipline

| Search command or query | Search roots | Result | Disposition |
| --- | --- | --- | --- |
| `rg -n "RESUME_WITH_REWRITE|MGW-001|strategy-layer|routing-policy-engine|dynamic model registry|gateway-interface" docs/reference docs/reviews` | governed docs | Current recheck and completion artifacts found | COLLISION_RECORDED_AS_AUTHORITY_INPUT |
| `rg -n "ProviderRegistry|PROVIDER_CAPABILITY_REGISTRY|RoutingPolicyEngine|RoutingRequest|RoutingDecision|buildRoutingPolicyContractSnapshot" EXTENSIONS/CVF_MODEL_GATEWAY/src` | Model Gateway source | Current source surfaces found | COLLISION_RECORDED_AS_SOURCE_INPUT |
| `rg -n "CVF_MODEL_GATEWAY|modelGateway|gateway wrapper" EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION` | EPF source and README | Current wrapper-anchor surfaces found | COLLISION_RECORDED_AS_SOURCE_INPUT |
| `rg -n "Legacy Absorption Coverage Index Disposition|_validate_legacy_coverage_index_disposition" governance/compat/check_work_order_dispatch_quality.py docs/reviews` | guard and review artifacts | Guard marker and completion found | COLLISION_RECORDED_AS_GUARD_INPUT |
| Old held C-02 packet path | `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_EPF_PROVIDER_ROUTING_BOUNDARY_PLANNING_FOR_CLAUDE_2026-06-13.md` | Existing packet remains held | REJECT_AS_EXECUTION_SOURCE |

## Required Artifact Manifest

| Path | Owner | Required at handoff | Purpose |
| --- | --- | --- | --- |
| `docs/reference/CVF_MODEL_GATEWAY_C02_PROVIDER_ROUTING_BOUNDARY_REWRITE_PLAN_2026-06-14.md` | Claude | YES | Fresh C-02 rewrite plan |
| `docs/reviews/CVF_MODEL_GATEWAY_C02_PROVIDER_ROUTING_BOUNDARY_REWRITE_WORKER_RETURN_2026-06-14.md` | Claude | YES | Worker return and gate evidence |
| `docs/reviews/CVF_MODEL_GATEWAY_C02_PROVIDER_ROUTING_BOUNDARY_REWRITE_COMPLETION_2026-06-14.md` | Codex | NO | Reviewer-owned completion review |

## Work-Order Fulfillment Manifest

| Required artifact | Worker action | Reviewer action |
| --- | --- | --- |
| C-02 rewrite plan | Create exactly the required reference plan path | Codex reviews and may repair allowed-scope documentation defects |
| Worker return | Create exactly the required worker return path | Codex verifies gate evidence, trace, and claim boundary |
| Reviewer-owned closeout artifact | Outside Claude write ownership | Codex creates only after accepting worker return |

## Required Proof Manifest

| Required literal | Required at handoff | Evidence location |
| --- | --- | --- |
| `RESUME_WITH_REWRITE` | YES | C-02 rewrite plan and worker return |
| `MGW-001` | YES | C-02 rewrite plan and worker return |
| `WORKER_MUST_NOT_COMMIT` | YES | Worker return |
| `DEFERRED_PRIVATE_ONLY` | YES | Both worker deliverables |

## Evidence Requirements

Claude must provide source-backed evidence for every current-source claim,
legacy-disposition claim, no-runtime/no-provider claim, and no-commit claim.
Evidence may be command output summaries, cited governed file lines/sections,
or explicit N/A with reason where a proof class does not apply.

## Task Instructions

Claude must create a fresh C-02 rewrite plan with these sections:

1. `Source Authority Table`
2. `Legacy Coverage Disposition`
3. `Current Owner Surface Map`
4. `Accepted Legacy Value Mapping`
5. `Boundary Disposition Matrix`
6. `Strategy Layer Scope Decision`
7. `Routing Policy Engine Scope Decision`
8. `Dynamic Model Registry Scope Decision`
9. `Integration Flow And Gateway Interface Scope Decision`
10. `AI Gateway Deferral`
11. `Implementation Prerequisite Map`
12. `Recommended Next Tranche`
13. `Forbidden Scope`
14. `Claim Boundary`
15. `Public Export Disposition`

The plan must not claim implementation readiness. The strongest allowed result
is a planning recommendation such as `NEXT_TRANCHE_WORK_ORDER_READY_AFTER_CODEX_REVIEW`.

## Execution Plan

| Step | Input | Action | Output | Stop condition |
| --- | --- | --- | --- | --- |
| 1 | Required first reads | Capture `executionBaseHead` and dirty worktree state | preflight evidence | Stop if unrelated dirty files would be overwritten |
| 2 | Recheck plan and coverage index | Extract accepted value keys and required C-02 dispositions | legacy value map | Stop if required source file is missing |
| 3 | Current source files | Map current owner surfaces and gaps | owner surface map | Stop if source facts cannot be verified |
| 4 | Boundary decisions | Include/defer each required C-02 area with reason | boundary matrix | Stop if any required gap lacks disposition |
| 5 | Worker deliverables | Write required plan and worker return only | two worker files | Stop for forbidden path changes |
| 6 | Gates | Run required local gates | evidence in worker return | Stop and repair allowed-scope issues before return |

## Worker Pending-Return Gate

Claude must fill this table in the worker return:

| Gate | Required evidence | Status |
| --- | --- | --- |
| Exact deliverables only | `git status --short` shows only the two required worker paths | PENDING |
| No implementation | `git diff --name-status` shows no `EXTENSIONS/` mutation | PENDING |
| Source verification complete | Source facts cite governed files or return a blocking source-missing disposition in the worker return | PENDING |
| Legacy coverage disposition present | Plan cites `MGW-001` and coverage index | PENDING |
| Old held C-02 not reused | Worker return states old packet was not resumed | PENDING |
| AI Gateway deferral preserved | Plan explicitly defers environment signal capture | PENDING |
| Provider/live boundary preserved | No provider/API/live proof, provider/model addition, package install, or secret inspection | PENDING |
| Agent Operation Trace Block complete | Expected and actual changed set recorded or N/A with reason | PENDING |
| Public Export Disposition present | `DEFERRED_PRIVATE_ONLY` in both worker deliverables | PENDING |
| Worker did not commit | HEAD unchanged from `executionBaseHead` | PENDING |
| Diff hygiene | `git diff --check` PASS | PENDING |
| Reviewer-fast | `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast` PASS, or failure is recorded with allowed-scope repair status | PENDING |

## Worker Autonomy / No-Question Rule

Allowed-scope machine-gate failures remain inside Claude's worker scope before
return. Routine source-verification corrections, missing required sections,
trace-block updates, public export disposition updates, and diff hygiene cleanup
must be completed and rerun without escalation.

Claude must stop and return `BLOCKED_SCOPE_EXPANSION` only when repair would
exceed allowed scope, change the claim boundary, require forbidden paths, open
public-sync, run live/provider proof, consume secrets/quota, configure OS audit
or endpoint monitoring, perform destructive action, mutate registries, or
require a commit.

## Acceptance Criteria

| Criterion | Acceptance condition |
| --- | --- |
| Fresh rewrite | Worker plan uses this work order and does not resume the old held C-02 packet |
| Legacy coverage | Worker plan cites `MGW-001` and dispositions every required Model Gateway gap |
| Runtime boundary | No `EXTENSIONS/` source, runtime, or test file is changed |
| Provider boundary | No provider/API/live proof, secret read, provider addition, or model addition occurs |
| Return quality | Worker return includes the pending-return gate with evidence for every row |
| Public boundary | Worker deliverables include `DEFERRED_PRIVATE_ONLY` |

## Review Gate

Codex must run reviewer-fast and dispatch/closure gates before accepting,
committing, or closing the worker return. If a gate fails inside worker-owned
scope, return it to Claude for allowed-scope repair; if the failure is
reviewer-owned, Codex may repair only within reviewer-owned closure scope.

## Closure Checklist

| Item | Closure owner | Status before worker return |
| --- | --- | --- |
| Worker deliverables exist | Claude | PENDING |
| Worker gates recorded | Claude | PENDING |
| Reviewer completion review created | Codex | N/A before worker return |
| Accepted artifacts committed | Codex | N/A before worker return |
| Session continuity synced | Codex | N/A before worker return |

## Return-To-Orchestrator Conditions

Return to Codex with `BLOCKED_SCOPE_EXPANSION` if the work requires forbidden
paths, runtime implementation, provider/live proof, secrets, public-sync,
registry mutation, OS/endpoint monitoring, destructive action, or a commit.

## Operator Checkpoint

No operator checkpoint is required for the bounded planning rewrite. Operator
approval is required only if scope expands beyond documentation/planning or
touches a parked lane.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Codex dispatcher |
| Provider or surface | Codex CLI |
| Session or invocation | dispatchBaseHead `21f49ec5` |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | `rg`, `Get-Content`, `apply_patch`, governance gates |
| Target paths | this work order; worker deliverable paths named in Required Artifact Manifest |
| Allowed scope source | operator instruction 2026-06-14 plus legacy coverage-index guard closure |
| Before status evidence | `git status --short` clean at dispatch start; base `21f49ec5` |
| After status evidence | pending this work order only before material commit |
| Diff evidence | `git diff --name-status` after work-order creation |
| Approval boundary | fresh C-02 planning rewrite for Claude; no implementation |
| Claim boundary | repo-local dispatch trace only; no OS/user attribution, endpoint telemetry, provider-internal log, public readiness, or production readiness claim |
| Agent type | Codex |
| Invocation ID | `dispatchBaseHead=21f49ec5` |
| Expected manifest | `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_PROVIDER_ROUTING_BOUNDARY_REWRITE_FOR_CLAUDE_2026-06-14.md` |
| Actual changed set | `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_PROVIDER_ROUTING_BOUNDARY_REWRITE_FOR_CLAUDE_2026-06-14.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: dispatch creates a new governed work order and deletes or renames no protected path |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: Current source will show provider registry,
capability registry, routing policy, health, stream, and embedding primitives,
but the completed legacy recheck will still require planning dispositions for
strategy layer depth, routing-policy-engine pipeline, dynamic model registry,
integration-flow boundary, and unified gateway-interface boundary.

Evidence Comparison Requirement: The worker return must compare the current
source map against the recheck prediction and state whether the prediction was
confirmed, narrowed, or contradicted.

Contradiction Handling Requirement: If Claude finds an existing current source
surface that fully owns a required legacy value, record the source and narrow
the next tranche recommendation. Do not edit runtime source.

Claim Update Requirement: The worker return must record whether C-02 remains
planning-only and whether any implementation candidate is ready only for a
future fresh GC-018.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
| --- | --- | --- | --- | --- |
| Prior C-02 packet was current-source-only and held for missing legacy absorption | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | Fresh rewrite must cite `MGW-001`, recheck plan, and completion review. |
| Future foundation/workflow-chain planning can forget coverage-index evidence | PHASE_GATE_PLACEMENT_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_ADDED | Dispatch-quality guard now requires coverage-index disposition or N/A. |
| Runtime/provider/cost behavior | N/A_WITH_REASON | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | This work order authorizes no runtime/provider/cost behavior. |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance planning dispatch. Public-sync is not authorized.

## Claim Boundary

This work order authorizes only a fresh C-02 documentation/planning rewrite.
It does not implement Model Gateway, EPF provider routing, dynamic model
registry, gateway API, strategy engine, feedback loop, AI Gateway environment
signal capture, provider/API calls, public-sync, production readiness, public
readiness, cost improvement, quality improvement, raw memory release, co-work
product development, or autonomous mutation.
