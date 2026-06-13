# CVF GC-018 Model Gateway EPF Provider Routing Boundary Planning - 2026-06-13

Memory class: POINTER_RECORD

Status: DISPATCHED_UNDER_WORKER_MUST_NOT_COMMIT

Owner: Codex Orchestrator

Worker target: Claude

Base head: 45b27691

dispatchBaseHead: `45b27691`

Commit mode: WORKER_MUST_NOT_COMMIT

rawMemoryReleased=false

## Purpose

Open the next high-value CVF foundation tranche selected by FPC-T4: Model
Gateway EPF provider-routing boundary planning.

This baseline authorizes Claude to produce a source-backed boundary plan that
maps the current Model Gateway routing surfaces, the Execution Plane Foundation
gateway wrapper anchor, provider-method authority, trace/evidence needs, and
future implementation prerequisites.

This baseline does not authorize runtime/source implementation, provider/API
calls, live governance proof, registry mutation, public-sync, provider addition,
model addition, cost/quality claims, production readiness, or public readiness.

## Operator Authorization

The operator authorized Codex to issue the next work order for Claude after
FPC-T4 closure. FPC-T4 selected Model Gateway EPF provider-routing boundary
planning as the highest-value CVF foundation move, ahead of AOT breadth,
Sandbox Runtime physical-isolation planning, and the narrower FPC-T2-C05
registry follow-up.

## Scope Classification

| Axis | Disposition |
| --- | --- |
| Work type | Source-backed boundary planning |
| Foundation value | HIGH |
| Use-case dependency | NONE |
| Runtime mutation | FORBIDDEN |
| Provider/live proof | FORBIDDEN |
| Provider/model addition | FORBIDDEN |
| Registry mutation | FORBIDDEN |
| Public-sync | FORBIDDEN |
| Implementation authorization | NONE |
| Worker commit authority | WORKER_MUST_NOT_COMMIT |

## Decision Baseline

The baseline decision is to dispatch a planning-only Model Gateway / Execution
Plane boundary packet. The worker must identify current source surfaces, gaps,
and future implementation prerequisites, then recommend the smallest safe next
tranche. The worker must not convert this plan into code changes.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| EXISTS: FPC-T4 selected Model Gateway EPF provider-routing boundary planning as the highest-value next foundation move | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | line 935 | `acceptedNextMove` | FPC-T4 closure state entry | ACCEPT |
| EXISTS: FPC-T4 matrix recommends Model Gateway EPF provider-routing boundary planning first | `docs/reference/CVF_FPC_T4_STRATEGIC_DEFERRED_CAPABILITY_REOPEN_DECISION_MATRIX_2026-06-13.md` | line 171 | `C-02` | FPC-T4 decision matrix | ACCEPT |
| EXISTS: Model Gateway EPF provider routing is formally deferred | `docs/reference/CVF_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_MATRIX_2026-06-13.md` | line 378 | `Model Gateway (EPF provider routing)` | FPC-T1 deferred capability list | ACCEPT |
| EXISTS: Model Gateway and Sandbox Runtime implementation are forbidden in the FPC foundation roadmap scope | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | line 141 | `Model Gateway or Sandbox Runtime implementation` | FPC roadmap forbidden scope | ACCEPT |
| EXISTS: ProviderRegistry is exported from Model Gateway | `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` | line 67 | `ProviderRegistry` | Model Gateway public exports | ACCEPT |
| EXISTS: PROVIDER_CAPABILITY_REGISTRY is exported from Model Gateway | `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` | line 122 | `PROVIDER_CAPABILITY_REGISTRY` | Model Gateway public exports | ACCEPT |
| EXISTS: Provider method gate helpers are exported from Model Gateway | `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` | lines 129-133 | `assertRegistryProviderMethodSupported`, `getProviderMethodContract`, `listRegistrySupportedMethods` | Model Gateway public exports | ACCEPT |
| EXISTS: Provider capability registry source surface exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | line 42 | `PROVIDER_CAPABILITY_REGISTRY` | Model Gateway provider capability registry | ACCEPT |
| EXISTS: ProviderRegistry class exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | line 30 | `ProviderRegistry` | Model Gateway provider registry | ACCEPT |
| EXISTS: Provider method contract type surface exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-contract.ts` | line 26 | `ProviderMethodContract` | Model Gateway provider method contract | ACCEPT |
| EXISTS: Routing request type exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | line 6 | `RoutingRequest` | Model Gateway routing policy | ACCEPT |
| EXISTS: Routing decision type exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | line 14 | `RoutingDecision` | Model Gateway routing policy | ACCEPT |
| EXISTS: Routing policy contract snapshot builder exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | line 43 | `buildRoutingPolicyContractSnapshot` | Model Gateway routing policy | ACCEPT |
| EXISTS: RoutingPolicyEngine exists and consumes ProviderRegistry | `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | lines 60-62 | `RoutingPolicyEngine`, `ProviderRegistry` | Model Gateway routing policy | ACCEPT |
| EXISTS: RoutingPolicyEngine decides provider selection through policy, health, and quota | `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | lines 64-116 | `decide` | Model Gateway routing policy | ACCEPT |
| EXISTS: Model Gateway README states routing guard-contract boundary | `EXTENSIONS/CVF_MODEL_GATEWAY/README.md` | lines 23-31 | `Guard Contract boundary` | Model Gateway README | ACCEPT |
| EXISTS: EPF preserves CVF_MODEL_GATEWAY as canonical gateway-facing wrapper anchor | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/README.md` | line 10 | `CVF_MODEL_GATEWAY` | Execution Plane Foundation README | ACCEPT |
| EXISTS: EPF shell exposes gateway wrapper alignment without changing source ownership | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/README.md` | lines 41-49 | `Current-cycle wrapper boundary` | Execution Plane Foundation README | ACCEPT |
| EXISTS: EPF source exposes modelGateway coordination anchor | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/index.ts` | line 713 | `modelGateway` | Execution Plane Foundation shell source | ACCEPT |

## New Doc-Only Fields

| Field | Purpose | Runtime authority |
| --- | --- | --- |
| `Provider-Routing Boundary Plan` | Names the planning artifact Claude must produce | DOC_ONLY_NEW |
| `Boundary Disposition` | Records `SOURCE_VISIBLE`, `PLANNING_GAP`, `IMPLEMENTATION_PREREQUISITE`, or `OUT_OF_SCOPE` | DOC_ONLY_NEW |
| `Provider Execution Authority Map` | Maps current routing authority surfaces without changing runtime code | DOC_ONLY_NEW |
| `Future Implementation Candidate` | Names later code work that would require fresh GC-018 | DOC_ONLY_NEW |

## Roadmap-To-Work-Order Trace Matrix

| Source requirement | Source | Dispatch handling | Status |
| --- | --- | --- | --- |
| FPC-T4 selected Model Gateway boundary planning first | FPC-T4 matrix line 171 and active session state line 935 | Dispatch this planning-only GC-018 and work order | SATISFIED_FOR_DISPATCH |
| Model Gateway implementation remains forbidden until later authorization | FPC roadmap line 141 | Work order forbids runtime/source mutation and provider/live proof | SATISFIED_FOR_DISPATCH |
| Avoid use-case and narrow-lane drift | Operator instruction and FPC-T4 closure | Work order excludes Policy_Local, Document Translator, public product work, FPC-T2-C05 registry mutation, and provider addition | SATISFIED_FOR_DISPATCH |
| Keep co-work supervision trace-focused | FPC-T4 matrix co-work supervision section | Work order requires trace/evidence boundary analysis and forbids cowork product development | SATISFIED_FOR_DISPATCH |

## Current Runtime Freshness Verification

| Runtime/source surface | Freshness check | Disposition |
| --- | --- | --- |
| Model Gateway provider registry | `rg -n "ProviderRegistry" EXTENSIONS/CVF_MODEL_GATEWAY/src` returned current source and exports | CURRENT_SOURCE_SURFACE_FOUND |
| Model Gateway provider capability registry | `rg -n "PROVIDER_CAPABILITY_REGISTRY" EXTENSIONS/CVF_MODEL_GATEWAY/src` returned current source and exports | CURRENT_SOURCE_SURFACE_FOUND |
| Model Gateway routing policy | `rg -n "RoutingPolicyEngine|RoutingRequest|RoutingDecision" EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` returned current source | CURRENT_SOURCE_SURFACE_FOUND |
| Execution Plane Foundation gateway wrapper anchor | `rg -n "CVF_MODEL_GATEWAY|createExecutionGatewaySurface|modelGateway" EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION` returned README, source, and tests | CURRENT_SOURCE_SURFACE_FOUND |
| Implementation readiness | No runtime/source/test files are authorized for mutation by this baseline | NOT_RELEASED |

## Negative Search And Collision Discipline

| Search command or query | Search roots | Result | Disposition |
| --- | --- | --- | --- |
| `rg -n "ProviderRegistry|PROVIDER_CAPABILITY_REGISTRY|RoutingPolicyEngine|RoutingRequest|RoutingDecision|buildRoutingPolicyContractSnapshot" EXTENSIONS/CVF_MODEL_GATEWAY/src` | `EXTENSIONS/CVF_MODEL_GATEWAY/src` | Current source surfaces found | COLLISION_RECORDED_AS_SOURCE_INPUT |
| `rg -n "CVF_MODEL_GATEWAY|Execution Plane|provider routing|Model Gateway" docs/reference docs/roadmaps EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION EXTENSIONS/CVF_MODEL_GATEWAY` | governed docs and source roots | Collisions found in FPC matrix, Model Gateway source, EPF source, archive roadmaps, and README files | COLLISION_RECORDED_AS_SOURCE_INPUT_AND_HISTORY_CONTEXT |
| `rg -n "Policy_Local|Document Translator|DT-CVF|public-sync|DASHSCOPE_API_KEY|DEEPSEEK_API_KEY|ALIBABA_API_KEY|T12|rawMemoryReleased|co-work product" docs/reference docs/roadmaps docs/work_orders docs/reviews` | governed docs only | Same-token collisions expected in forbidden-scope and governance artifacts | COLLISION_RECORDED_AS_FORBIDDEN_SCOPE_CONTEXT |
| `git status --short` | repo root | Clean worktree before dispatch packet creation | MANIFEST_BOUNDARY_RECORDED |
| `git diff --name-status` | repo root | Pending dispatch artifacts only after authoring | TOOL_BOUNDARY_RECORDED |

## Evidence / Verification

Dispatch verification must pass before Codex commits this packet:

| Gate | Command | Expected result |
| --- | --- | --- |
| Dispatch quality | `python governance/compat/check_work_order_dispatch_quality.py --base 45b27691 --head HEAD --enforce` | PASS |
| Pre-dispatch autorun | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 45b27691 --head HEAD` | PASS |
| Reviewer-fast | `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast` | PASS |
| Diff hygiene | `git diff --check` | PASS |

## Allowed Worker Deliverables

Claude may create exactly these uncommitted files:

| Deliverable | Purpose |
| --- | --- |
| `docs/reference/CVF_MODEL_GATEWAY_EPF_PROVIDER_ROUTING_BOUNDARY_PLAN_2026-06-13.md` | Source-backed provider-routing boundary plan, authority map, gap map, implementation prerequisites, and recommended next tranche |
| `docs/reviews/CVF_MODEL_GATEWAY_EPF_PROVIDER_ROUTING_BOUNDARY_WORKER_RETURN_2026-06-13.md` | Worker return with evidence, gate results, trace block, and pending-return disposition |

No other file may be created, modified, deleted, renamed, formatted, staged, or
committed by Claude.

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

Evidence Comparison Requirement: Claude must compare this prediction against
current source evidence and record whether the boundary is confirmed, narrowed,
or contradicted.

Contradiction Handling Requirement: If Claude finds a current implementation
path that already proves full EPF provider-routing integration, it must record
the contradiction and narrow the recommendation. It must not modify runtime
source.

Claim Update Requirement: Worker return must record whether the claim is
confirmed, revised, narrowed, or invalidated.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance foundation planning. Public-sync is not authorized.

## Forbidden Scope

This baseline authorizes no runtime/source/test mutation, no Model Gateway
implementation, no EPF implementation, no provider/API use, no live governance
proof, no provider/model addition, no registry mutation, no package install, no
secret inspection, no infrastructure work, no OS/Sysmon/endpoint monitoring, no
file-watcher service, no public-sync, no public catalog claim, no Document
Translator work, no Policy_Local work, no corpus ingestion, no T12, no raw
memory release, no memory reinjection, no high-risk promotion, no autonomous
mutation, and no co-work product development.

## Claim Boundary

This baseline authorizes only repo-local, source-backed boundary planning for
Model Gateway EPF provider routing. It does not prove or authorize runtime
behavior, provider/live behavior, completed Model Gateway, completed EPF
provider routing, public readiness, production readiness, cost optimization,
output quality, raw memory release, or autonomous mutation.
