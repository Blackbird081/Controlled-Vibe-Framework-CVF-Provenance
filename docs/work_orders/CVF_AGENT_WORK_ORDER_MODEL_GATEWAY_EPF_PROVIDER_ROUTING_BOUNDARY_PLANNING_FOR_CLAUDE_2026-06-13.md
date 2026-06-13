# CVF Agent Work Order: Model Gateway EPF Provider Routing Boundary Planning For Claude - 2026-06-13

Memory class: POINTER_RECORD

Status: DISPATCHED_UNDER_WORKER_MUST_NOT_COMMIT

Worker: Claude

Orchestrator / reviewer: Codex

Worker commit policy: WORKER_MUST_NOT_COMMIT

Commit mode: WORKER_MUST_NOT_COMMIT

Base head: 45b27691

dispatchBaseHead: `45b27691`

executionBaseHead: WORKER_MUST_CAPTURE

closureBaseHead: WORKER_MUST_NOT_SET

completionReviewPath:
`docs/reviews/CVF_MODEL_GATEWAY_EPF_PROVIDER_ROUTING_BOUNDARY_PLANNING_COMPLETION_2026-06-13.md`

reviewerOwnedClosurePaths:

- `docs/baselines/CVF_GC018_MODEL_GATEWAY_EPF_PROVIDER_ROUTING_BOUNDARY_PLANNING_2026-06-13.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_EPF_PROVIDER_ROUTING_BOUNDARY_PLANNING_FOR_CLAUDE_2026-06-13.md`
- `docs/reference/CVF_MODEL_GATEWAY_EPF_PROVIDER_ROUTING_BOUNDARY_PLAN_2026-06-13.md`
- `docs/reviews/CVF_MODEL_GATEWAY_EPF_PROVIDER_ROUTING_BOUNDARY_WORKER_RETURN_2026-06-13.md`
- `docs/reviews/CVF_MODEL_GATEWAY_EPF_PROVIDER_ROUTING_BOUNDARY_PLANNING_COMPLETION_2026-06-13.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION_MEMORY.md`
- `AGENT_HANDOFF_V18_2026-06-12.md`

## Purpose

Produce a source-backed Model Gateway EPF provider-routing boundary plan. The
plan must map current Model Gateway source surfaces, EPF wrapper-anchor
surfaces, provider-method authority, routing-policy evidence, trace/evidence
requirements, and future implementation prerequisites.

The worker must not implement routing, mutate runtime/source/test files, call
providers, add provider/model registry entries, or claim readiness.

## Authority Chain

| Authority | Role |
| --- | --- |
| Operator instruction on 2026-06-13 | Authorized Codex to issue the next Claude work order |
| Active session state | Records FPC-T4 closure and Model Gateway boundary planning as next allowed move |
| FPC-T4 decision matrix | Recommends Model Gateway EPF provider-routing boundary planning first |
| GC-018 baseline | Defines dispatch boundary and source anchors |
| This work order | Defines Claude's allowed deliverables, forbidden paths, and return gates |
| Codex reviewer | Owns closure, commit, allowed repairs, and session sync |

Authority boundary: if any authority artifact conflicts with this work order,
stop and return to Codex before drafting beyond source verification.

## Reviewer Closure Conversion Block

completionReviewPath:
`docs/reviews/CVF_MODEL_GATEWAY_EPF_PROVIDER_ROUTING_BOUNDARY_PLANNING_COMPLETION_2026-06-13.md`

reviewerOwnedClosurePaths:

- `docs/baselines/CVF_GC018_MODEL_GATEWAY_EPF_PROVIDER_ROUTING_BOUNDARY_PLANNING_2026-06-13.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_EPF_PROVIDER_ROUTING_BOUNDARY_PLANNING_FOR_CLAUDE_2026-06-13.md`
- `docs/reference/CVF_MODEL_GATEWAY_EPF_PROVIDER_ROUTING_BOUNDARY_PLAN_2026-06-13.md`
- `docs/reviews/CVF_MODEL_GATEWAY_EPF_PROVIDER_ROUTING_BOUNDARY_WORKER_RETURN_2026-06-13.md`
- `docs/reviews/CVF_MODEL_GATEWAY_EPF_PROVIDER_ROUTING_BOUNDARY_PLANNING_COMPLETION_2026-06-13.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION_MEMORY.md`
- `AGENT_HANDOFF_V18_2026-06-12.md`

Codex owns final material closure, completion review, committed-range
pre-closure, and session sync. Claude must not mark this work order closed.

## Agent Roles

| Role | Owner | Authority |
| --- | --- | --- |
| Orchestrator / dispatcher | Codex | Files GC-018 and this work order |
| Worker | Claude | Creates exactly the two allowed worker deliverables |
| Reviewer / committer | Codex | Reviews worker return, repairs allowed-scope issues, commits if accepted, and updates session continuity |
| Operator | Human | Authorizes scope expansion only |

Human authorization is required for implementation, runtime/source/test mutation,
provider/live proof, provider/model addition, registry mutation, public-sync,
secrets/quota use, OS/endpoint telemetry, destructive action, or claim-boundary
expansion.

## Scope

Allowed scope:

- Read current governed source and reference artifacts named in Required First Reads.
- Create the provider-routing boundary plan deliverable.
- Create the worker-return packet.
- Run local read-only searches and reviewer/worker gates.
- Record source verification, negative-search collisions, Agent Operation Trace
  evidence, and a recommended future tranche.

Forbidden scope:

- Runtime/source/test edits.
- Model Gateway implementation.
- EPF implementation.
- Provider/API calls or live governance proof.
- Provider/model addition.
- Registry mutation.
- Package install or dependency change.
- Secret inspection.
- Session-state, handoff, or front-door mutation by Claude.
- Public-sync or public catalog claim.
- Policy_Local, Document Translator, corpus ingestion, T12, OS audit,
  endpoint monitoring, file-watcher service, co-work product development,
  raw memory release, memory reinjection, high-risk promotion, or autonomous
  mutation.

Risk ceiling: R1 documentation/planning only.

## Required First Reads

Read before drafting:

| File | Required use |
| --- | --- |
| `AGENTS.md` | active governance instructions and provider-specific memory boundary |
| `CVF_SESSION_MEMORY.md` | current front-door state and next allowed move |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | active closure state and current mode |
| `AGENT_HANDOFF_V18_2026-06-12.md` | active handoff and parked checkpoints |
| `docs/baselines/CVF_GC018_MODEL_GATEWAY_EPF_PROVIDER_ROUTING_BOUNDARY_PLANNING_2026-06-13.md` | dispatch scope and source anchors |
| `docs/reference/CVF_FPC_T4_STRATEGIC_DEFERRED_CAPABILITY_REOPEN_DECISION_MATRIX_2026-06-13.md` | FPC-T4 recommendation and claim boundary |
| `docs/reviews/CVF_FPC_T4_STRATEGIC_DEFERRED_CAPABILITY_REOPEN_DECISION_COMPLETION_2026-06-13.md` | reviewer repair and closure rationale |
| `docs/reference/CVF_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_MATRIX_2026-06-13.md` | deferred Execution Plane capability source |
| `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | FPC roadmap forbidden boundary |
| `EXTENSIONS/CVF_MODEL_GATEWAY/README.md` | Model Gateway guard-contract boundary |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` | exported Model Gateway surfaces |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | provider capability registry |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | provider registry |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-contract.ts` | provider method contract |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-gate.ts` | provider method gate helpers |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | routing request, decision, snapshot, and routing policy engine |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/README.md` | EPF gateway wrapper anchor and shell boundary |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/index.ts` | EPF source anchor for `modelGateway` and gateway wrapper surface |
| `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md` | Agent Operation Trace Block contract |
| `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | work-order and worker-return structure |

Provider-specific memory files such as `CLAUDE.md`, Codex memory, Claude
memory, and IDE summaries are not CVF source authority. If read as local
operating guidance, re-verify every source fact against governed source before
citing it.

## Pre-Flight Checks

Claude must run and record before edits:

```powershell
git rev-parse --short HEAD
git status --short
Test-Path "docs/baselines/CVF_GC018_MODEL_GATEWAY_EPF_PROVIDER_ROUTING_BOUNDARY_PLANNING_2026-06-13.md"
Test-Path "docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_EPF_PROVIDER_ROUTING_BOUNDARY_PLANNING_FOR_CLAUDE_2026-06-13.md"
rg -n "ProviderRegistry|PROVIDER_CAPABILITY_REGISTRY|RoutingPolicyEngine|RoutingRequest|RoutingDecision|buildRoutingPolicyContractSnapshot" EXTENSIONS/CVF_MODEL_GATEWAY/src
rg -n "CVF_MODEL_GATEWAY|Execution Plane|provider routing|Model Gateway" docs/reference docs/roadmaps EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION EXTENSIONS/CVF_MODEL_GATEWAY
```

Expected result:

- HEAD is unchanged from worker start throughout worker execution.
- Required dispatch files exist.
- Runtime/source symbols named by this work order are source-visible.
- Worktree before edits contains no unrelated changes, or any pre-existing
  dirty paths are recorded and ignored.

If a pre-flight check fails, stop and return the failed command and result.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| EXISTS: FPC-T4 selected Model Gateway EPF provider-routing boundary planning as the next foundation move | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | line 935 | `acceptedNextMove` | FPC-T4 closure state entry | ACCEPT |
| EXISTS: FPC-T4 matrix recommends Model Gateway EPF provider-routing boundary planning first | `docs/reference/CVF_FPC_T4_STRATEGIC_DEFERRED_CAPABILITY_REOPEN_DECISION_MATRIX_2026-06-13.md` | line 171 | `C-02` | FPC-T4 decision matrix | ACCEPT |
| EXISTS: Model Gateway EPF provider routing is formally deferred | `docs/reference/CVF_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_MATRIX_2026-06-13.md` | line 378 | `Model Gateway (EPF provider routing)` | FPC-T1 deferred capability list | ACCEPT |
| EXISTS: Model Gateway implementation remains forbidden in current FPC roadmap scope | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | line 141 | `Model Gateway or Sandbox Runtime implementation` | FPC roadmap forbidden scope | ACCEPT |
| EXISTS: ProviderRegistry is exported | `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` | line 67 | `ProviderRegistry` | Model Gateway public exports | ACCEPT |
| EXISTS: PROVIDER_CAPABILITY_REGISTRY is exported | `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` | line 122 | `PROVIDER_CAPABILITY_REGISTRY` | Model Gateway public exports | ACCEPT |
| EXISTS: Provider method gate helpers are exported | `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` | lines 129-133 | `assertRegistryProviderMethodSupported`, `getProviderMethodContract`, `listRegistrySupportedMethods` | Model Gateway public exports | ACCEPT |
| EXISTS: Provider capability registry exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | line 42 | `PROVIDER_CAPABILITY_REGISTRY` | Model Gateway provider capability registry | ACCEPT |
| EXISTS: ProviderRegistry class exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | line 30 | `ProviderRegistry` | Model Gateway provider registry | ACCEPT |
| EXISTS: ProviderMethodContract exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-contract.ts` | line 26 | `ProviderMethodContract` | Model Gateway provider method contract | ACCEPT |
| EXISTS: RoutingRequest exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | line 6 | `RoutingRequest` | Model Gateway routing policy | ACCEPT |
| EXISTS: RoutingDecision exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | line 14 | `RoutingDecision` | Model Gateway routing policy | ACCEPT |
| EXISTS: buildRoutingPolicyContractSnapshot exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | line 43 | `buildRoutingPolicyContractSnapshot` | Model Gateway routing policy | ACCEPT |
| EXISTS: RoutingPolicyEngine consumes ProviderRegistry | `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | lines 60-62 | `RoutingPolicyEngine`, `ProviderRegistry` | Model Gateway routing policy | ACCEPT |
| RUNTIME_BEHAVIOR: RoutingPolicyEngine decides selected, denied, requires_approval, or no_candidate through policy, health, and quota checks | `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | lines 64-116 | `decide` | Model Gateway routing policy | ACCEPT |
| EXISTS: Model Gateway README defines routing guard-contract boundary | `EXTENSIONS/CVF_MODEL_GATEWAY/README.md` | lines 23-31 | `Guard Contract boundary` | Model Gateway README | ACCEPT |
| EXISTS: EPF preserves CVF_MODEL_GATEWAY as gateway-facing wrapper anchor | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/README.md` | line 10 | `CVF_MODEL_GATEWAY` | Execution Plane Foundation README | ACCEPT |
| EXISTS: EPF wrapper boundary states CVF_MODEL_GATEWAY remains the gateway-facing wrapper anchor | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/README.md` | lines 41-49 | `Current-cycle wrapper boundary` | Execution Plane Foundation README | ACCEPT |
| EXISTS: EPF source records modelGateway coordination anchor | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/index.ts` | line 713 | `modelGateway` | Execution Plane Foundation shell source | ACCEPT |

## New Doc-Only Fields

| Field | Purpose | Runtime authority |
| --- | --- | --- |
| `Provider-Routing Boundary Plan` | Names Claude's planning deliverable | DOC_ONLY_NEW |
| `Boundary Disposition` | One of `SOURCE_VISIBLE`, `PLANNING_GAP`, `IMPLEMENTATION_PREREQUISITE`, `OUT_OF_SCOPE` | DOC_ONLY_NEW |
| `Provider Execution Authority Map` | Maps source-visible authority without changing runtime code | DOC_ONLY_NEW |
| `Future Implementation Candidate` | Names later code work requiring fresh GC-018 | DOC_ONLY_NEW |

## Intake Role Routing Decision

| Field | Decision |
| --- | --- |
| Intake item | Model Gateway EPF provider-routing boundary planning |
| Scope classification | source-backed foundation boundary plan only |
| Risk sensitivity | high governance sensitivity; no runtime/provider authority |
| Selected route mode | MULTI_AGENT_MULTI_ROLE |
| Selected role route | Claude worker drafts boundary plan; Codex reviewer/committer closes |
| routeMode | MULTI_AGENT_MULTI_ROLE |
| Routed role | Claude as worker |
| Reviewer | Codex |
| Commit authority | Codex only |
| Runtime/source authority | read-only source inspection only |
| Live/provider authority | NONE |
| Public-sync authority | NONE |
| Escalation condition | Stop for implementation, runtime mutation, provider/live proof, provider/model addition, registry mutation, public-sync, secrets, OS/endpoint telemetry, destructive action, or commit request |
| Disposition | DISPATCHED_UNDER_WORKER_MUST_NOT_COMMIT |

## Roadmap-To-Work-Order Trace Matrix

| Source requirement | Source | Worker instruction | Status |
| --- | --- | --- | --- |
| FPC-T4 selected Model Gateway planning first | FPC-T4 matrix line 171; active state line 935 | Produce Model Gateway EPF boundary plan | SATISFIED_FOR_DISPATCH |
| Model Gateway implementation remains forbidden | FPC roadmap line 141 | Analyze source surfaces only; do not edit runtime | SATISFIED_FOR_DISPATCH |
| Avoid use-case and small-niche drift | Operator instruction and FPC-T4 closure | Exclude Policy_Local, Document Translator, FPC-T2-C05 registry mutation, and public product work | SATISFIED_FOR_DISPATCH |
| Preserve co-work supervision as trace/evidence, not cowork product development | FPC-T4 co-work boundary | Require trace and manifest planning; forbid cowork product work | SATISFIED_FOR_DISPATCH |

## Current Runtime Freshness Verification

| Runtime/source surface | Freshness check | Disposition |
| --- | --- | --- |
| Model Gateway provider registry | `rg -n "ProviderRegistry" EXTENSIONS/CVF_MODEL_GATEWAY/src` returned current source and exports | CURRENT_SOURCE_SURFACE_FOUND |
| Model Gateway provider capability registry | `rg -n "PROVIDER_CAPABILITY_REGISTRY" EXTENSIONS/CVF_MODEL_GATEWAY/src` returned current source and exports | CURRENT_SOURCE_SURFACE_FOUND |
| Model Gateway routing policy | `rg -n "RoutingPolicyEngine|RoutingRequest|RoutingDecision" EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` returned current source | CURRENT_SOURCE_SURFACE_FOUND |
| Execution Plane Foundation gateway wrapper anchor | `rg -n "CVF_MODEL_GATEWAY|createExecutionGatewaySurface|modelGateway" EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION` returned README, source, and tests | CURRENT_SOURCE_SURFACE_FOUND |
| Implementation readiness | No runtime files are authorized for mutation by this work order | NOT_RELEASED |

## Negative Search And Collision Discipline

| Search command or query | Search roots | Result | Disposition |
| --- | --- | --- | --- |
| `rg -n "ProviderRegistry|PROVIDER_CAPABILITY_REGISTRY|RoutingPolicyEngine|RoutingRequest|RoutingDecision|buildRoutingPolicyContractSnapshot" EXTENSIONS/CVF_MODEL_GATEWAY/src` | `EXTENSIONS/CVF_MODEL_GATEWAY/src` | Current source surfaces found | COLLISION_RECORDED_AS_SOURCE_INPUT |
| `rg -n "CVF_MODEL_GATEWAY|Execution Plane|provider routing|Model Gateway" docs/reference docs/roadmaps EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION EXTENSIONS/CVF_MODEL_GATEWAY` | governed docs and source roots | Same-token collisions found in FPC artifacts, Model Gateway source, EPF source, README files, and archives | COLLISION_RECORDED_AS_SOURCE_INPUT_AND_HISTORY_CONTEXT |
| `rg -n "Policy_Local|Document Translator|DT-CVF|public-sync|DASHSCOPE_API_KEY|DEEPSEEK_API_KEY|ALIBABA_API_KEY|T12|rawMemoryReleased|co-work product" docs/reference docs/roadmaps docs/work_orders docs/reviews` | governed docs only | Same-token collisions expected in forbidden-scope and governance artifacts | COLLISION_RECORDED_AS_FORBIDDEN_SCOPE_CONTEXT |
| `rg -n "SOURCE_VISIBLE|PLANNING_GAP|IMPLEMENTATION_PREREQUISITE|Provider-Routing Boundary Plan" docs/baselines docs/reference docs/work_orders docs/reviews` | governed docs | Tokens are new doc-only planning vocabulary in this dispatch packet | COLLISION_RECORDED_AS_DOC_ONLY_NEW |
| `rg -n "COMPLETE_PENDING_REVIEW|BLOCKED_SCOPE_EXPANSION|BLOCKED_SOURCE_NOT_FOUND|HEAD|PASS" docs/reference docs/work_orders docs/reviews` | governed docs | Same-token collisions found in existing work orders, reviews, and governance templates | COLLISION_RECORDED_AS_STATUS_AND_GIT_ANCHOR_VOCABULARY |
| `git status --short` | repo root | Clean worktree before dispatch; pending dispatch files after authoring | MANIFEST_BOUNDARY_RECORDED |
| `git diff --name-status` | repo root | Pending dispatch artifacts only after authoring | TOOL_BOUNDARY_RECORDED |

## Allowed Deliverables

Create exactly these uncommitted files:

| Deliverable | Purpose |
| --- | --- |
| `docs/reference/CVF_MODEL_GATEWAY_EPF_PROVIDER_ROUTING_BOUNDARY_PLAN_2026-06-13.md` | Boundary plan with source authority map, provider execution authority map, trace/evidence requirements, gap map, and recommended next tranche |
| `docs/reviews/CVF_MODEL_GATEWAY_EPF_PROVIDER_ROUTING_BOUNDARY_WORKER_RETURN_2026-06-13.md` | Worker return with source verification summary, gate evidence, Agent Operation Trace Block, and pending-return disposition |

No other file may be created, modified, deleted, renamed, formatted, staged, or
committed by Claude.

## Write Ownership

| Path | Owner | Allowed action |
| --- | --- | --- |
| `docs/reference/CVF_MODEL_GATEWAY_EPF_PROVIDER_ROUTING_BOUNDARY_PLAN_2026-06-13.md` | Claude | Create only |
| `docs/reviews/CVF_MODEL_GATEWAY_EPF_PROVIDER_ROUTING_BOUNDARY_WORKER_RETURN_2026-06-13.md` | Claude | Create only |
| Runtime/source/test paths | None | FORBIDDEN |
| Session/handoff/front-door paths | Codex only | FORBIDDEN to Claude |
| Git index and commits | Codex only | Claude must not stage or commit |

## Forbidden Filesystem State At Dispatch

| Forbidden path | Expected state | Actual state at dispatch | Action if PRESENT |
| --- | --- | --- | --- |
| `docs/reference/CVF_MODEL_GATEWAY_EPF_PROVIDER_ROUTING_BOUNDARY_PLAN_2026-06-13.md` | ABSENT before Claude execution | ABSENT at dispatch authoring | N/A |
| `docs/reviews/CVF_MODEL_GATEWAY_EPF_PROVIDER_ROUTING_BOUNDARY_WORKER_RETURN_2026-06-13.md` | ABSENT before Claude execution | ABSENT at dispatch authoring | N/A |

## Task Instructions

1. Capture `executionBaseHead` with `git rev-parse --short HEAD`.
2. Confirm `git status --short` before edits.
3. Read all required first-read files.
4. Source-verify the current Model Gateway and EPF surfaces named in this work order.
5. Create the boundary plan with these required sections:
   - Purpose
   - Scope Boundary
   - Source Authority Table
   - Source Verification Block
   - Current Provider-Routing Surface Map
   - Provider Execution Authority Map
   - EPF Wrapper Anchor And Integration Gap
   - Trace And Evidence Requirements
   - Boundary Disposition Matrix
   - Anti-Overconstraint / Latency Impact
   - Co-Work Supervision Value
   - Recommended Next Tranche
   - Negative Search And Collision Discipline
   - Finding-To-Governance Learning Disposition
   - Agent Operation Trace Block
   - Public Export Disposition
   - Claim Boundary
6. Create the worker return with:
   - Summary
   - Changed Files
   - Source Verification Summary
   - Worker Pending-Return Gate
   - Agent Operation Trace Block
   - Negative Search And Collision Discipline
   - Gate Results
   - Public Export Disposition
   - Claim Boundary
7. Recommend only a future tranche boundary. Do not authorize implementation.

## Execution Plan

| Step | Input | Action | Output | Stop condition |
| --- | --- | --- | --- | --- |
| 1 | Work order and GC-018 | Capture `executionBaseHead` and initial `git status --short` | Worker-return evidence row | Stop if unrelated dirty files would confuse manifest evidence |
| 2 | Required First Reads | Read governed source and reference files | Source verification notes | Stop if any required file is missing |
| 3 | Current source surfaces | Verify Model Gateway registry, method gate, routing policy, and EPF wrapper anchor | Source Verification Block in boundary plan | Stop on `BLOCKED_SOURCE_NOT_FOUND` |
| 4 | Boundary planning scope | Draft boundary plan and gap map | Boundary plan deliverable | Stop if implementation becomes necessary |
| 5 | Worker-return evidence | Draft worker return with trace and pending-return gate | Worker return deliverable | Stop if trace manifest cannot match |
| 6 | Local gates | Run required gates and diff hygiene | Gate result rows | Stop on out-of-scope failure; otherwise update the allowed deliverables and rerun |

## Evidence Requirements

Evidence must include:

- source citations for every ACCEPT claim;
- negative-search collision rows;
- expected-vs-actual manifest reconciliation;
- `git status --short` before and after edits;
- `git diff --name-status`;
- `git diff --check`;
- `python governance/compat/run_worker_return_fast_gate.py`;
- `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast`;
- explicit N/A-with-reason rows for runtime mutation, provider/live proof,
  registry mutation, public-sync, provider/model addition, and implementation
  readiness.

Base-anchor evidence:

- `dispatchBaseHead`: `45b27691`
- `executionBaseHead`: worker must capture before edits
- `closureBaseHead`: N/A - pending Codex review
- Commit mode: `WORKER_MUST_NOT_COMMIT`

## Acceptance Criteria

| Criterion | Required result |
| --- | --- |
| Exact files | Only the two allowed worker deliverables are changed |
| Source authority | Boundary plan verifies Model Gateway and EPF surfaces against current source |
| No implementation | No runtime/source/test/session/public-sync mutation |
| Provider boundary | No provider/API call, provider/model addition, live proof, cost/quality claim, or readiness claim |
| EPF boundary | Plan distinguishes EPF wrapper anchor from completed provider-routing implementation |
| Anti-overconstraint | Plan phase-places future controls and avoids universal high-latency gates |
| Co-work supervision | Plan frames supervision through trace/evidence requirements, not cowork product development |
| Gates | Worker-return fast gate, reviewer-fast, and diff check pass or record a blocker |

Fail conditions:

- Accepted source claims cite missing paths, wrong symbols, or stale line evidence.
- Boundary plan authorizes implementation or provider/live proof.
- Worker changes any file outside the two allowed deliverables.
- Worker stages or commits.
- Worker inspects secrets or provider credentials.
- Worker introduces public-sync or readiness claims.
- Worker omits Agent Operation Trace Block, Negative Search And Collision
  Discipline, or Public Export Disposition.

Closure is blocked if any fail condition is present.

## Review Gate

Codex will reject or return the packet if any allowed deliverable is missing,
any unauthorized file is changed, source verification contains unsupported
ACCEPT claims, the plan claims implementation readiness, or latency discipline
is absent.

For `WORKER_MUST_NOT_COMMIT` mode, Claude handoff is not closure. Codex owns
review, completion review, material commit, committed-range pre-closure, and
session sync.

## Closure Checklist

| Closure item | Owner | Required disposition |
| --- | --- | --- |
| Boundary plan created | Claude | Required before return |
| Worker return created | Claude | Required before return |
| Exact changed-set manifest | Claude | Required before return |
| Worker-return fast gate | Claude | PASS or blocker recorded |
| Reviewer-fast gate | Claude | PASS or blocker recorded |
| Completion review filed | Codex | Required if material return is accepted |
| Material commit | Codex | Required if accepted |
| Committed-range pre-closure | Codex | Required after material commit |
| Session sync | Codex | Required if mode or next allowed move changes |

## Operator Checkpoint

Operator checkpoint is required only if Claude or Codex needs to expand beyond
planning, mutate runtime/source/test/session/public-sync files, run
provider/live proof, inspect secrets, introduce a provider/model, mutate a registry,
configure OS/endpoint telemetry, perform destructive action, or change the
claim boundary.

## Worker Pending-Return Gate

Claude may return `COMPLETE_PENDING_REVIEW` only when every row is PASS:

| Gate | Required evidence | Status |
| --- | --- | --- |
| Exact deliverables only | `git status --short` shows only the two allowed worker deliverables at return | PASS |
| No implementation | `git diff --name-status` shows no runtime/source/test/session/public-sync mutation | PASS |
| Source verification complete | Source Verification Block has no `BLOCKED_SOURCE_NOT_FOUND` for accepted claims | PASS |
| Provider/live boundary preserved | No provider/API call, live proof, provider/model addition, cost/quality claim, or readiness claim | PASS |
| EPF boundary preserved | Plan distinguishes wrapper anchor from completed implementation | PASS |
| Anti-overconstraint present | Latency discipline section exists and phase-places future controls | PASS |
| Co-work supervision boundary present | CVF supervises through traces/evidence; CVF does not build cowork products | PASS |
| Agent Operation Trace Block complete | Expected and actual manifests match | PASS |
| Public Export Disposition present | `DEFERRED_PRIVATE_ONLY` | PASS |
| Worker did not commit | HEAD unchanged from worker start | PASS |
| `git diff --check` | PASS | PASS |
| `python governance/compat/run_worker_return_fast_gate.py` | PASS | PASS |
| `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast` | PASS | PASS |

## Worker Autonomy / No-Question Rule

Allowed-scope machine-gate failures remain inside Claude's worker scope before
return. Routine source-verification corrections, missing required sections,
trace-block updates, public export disposition updates, and diff hygiene cleanup
must be completed and rerun without escalation.

Claude must stop and return to Codex only when repair would exceed Allowed
scope, change the claim boundary, require forbidden paths, open public-sync,
run live/provider proof, consume secrets/quota, configure OS audit or endpoint
monitoring, perform destructive action, or require a commit.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Codex dispatcher |
| Provider or surface | Codex CLI |
| Session or invocation | dispatchBaseHead `45b27691` |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | `rg`, `Get-Content`, `apply_patch`, governance gates |
| Target paths | `docs/baselines/CVF_GC018_MODEL_GATEWAY_EPF_PROVIDER_ROUTING_BOUNDARY_PLANNING_2026-06-13.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_EPF_PROVIDER_ROUTING_BOUNDARY_PLANNING_FOR_CLAUDE_2026-06-13.md` |
| Allowed scope source | operator instruction 2026-06-13 plus FPC-T4 closure state and decision matrix |
| Before status evidence | `git status --short` clean before dispatch packet creation; base `45b27691` |
| After status evidence | pending dispatch packet files only before material commit |
| Diff evidence | `git diff --name-status` after packet creation |
| Approval boundary | fresh GC-018 and work order for planning-only Model Gateway EPF provider-routing boundary; no implementation |
| Claim boundary | repo-local dispatch trace only; no OS/user attribution, endpoint telemetry, provider-internal log, public readiness, or production readiness claim |
| Agent type | Codex |
| Invocation ID | `dispatchBaseHead=45b27691` |
| Expected manifest | `docs/baselines/CVF_GC018_MODEL_GATEWAY_EPF_PROVIDER_ROUTING_BOUNDARY_PLANNING_2026-06-13.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_EPF_PROVIDER_ROUTING_BOUNDARY_PLANNING_FOR_CLAUDE_2026-06-13.md` |
| Actual changed set | `docs/baselines/CVF_GC018_MODEL_GATEWAY_EPF_PROVIDER_ROUTING_BOUNDARY_PLANNING_2026-06-13.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_EPF_PROVIDER_ROUTING_BOUNDARY_PLANNING_FOR_CLAUDE_2026-06-13.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: dispatch creates new governed packet files and deletes or renames no protected path |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: Source verification will show that Model Gateway
already has provider registry, capability registry, method gate, and routing
policy primitives, while EPF currently preserves `CVF_MODEL_GATEWAY` as a
wrapper anchor rather than proving a full governed provider-routing execution
integration.

Evidence Comparison Requirement: The worker return must compare actual source
evidence against this prediction.

Contradiction Handling Requirement: If the worker finds full EPF provider
routing integration is already implemented, the worker must record the
contradiction and narrow the recommendation. It must not modify runtime source.

Claim Update Requirement: The worker return must record whether the prediction
is confirmed, revised, narrowed, or invalidated.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only when both deliverables are complete,
trace blocks are complete, exact changed set matches the allowed manifest,
gates pass, and HEAD remains unchanged.

Return `BLOCKED_SOURCE_NOT_FOUND` if a named runtime/source claim cannot be
verified against governed source.

Return `BLOCKED_SCOPE_EXPANSION` if useful progress requires implementation,
runtime/provider/live work, provider/model addition, public-sync,
session-state mutation, secrets, registry mutation, or any forbidden scope.

Return `BLOCKED_OVERCONSTRAINT_RISK` if the only viable recommendation would
impose broad high-latency controls on ordinary CVF operation.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance foundation-planning dispatch. Public-sync is not
authorized.

## Claim Boundary

This work order authorizes source-backed boundary planning only. It does not
prove provider/live readiness, completed Model Gateway, completed EPF provider
routing, production readiness, public readiness, cost optimization, output
quality, raw memory release, co-work product development, or autonomous
mutation.
