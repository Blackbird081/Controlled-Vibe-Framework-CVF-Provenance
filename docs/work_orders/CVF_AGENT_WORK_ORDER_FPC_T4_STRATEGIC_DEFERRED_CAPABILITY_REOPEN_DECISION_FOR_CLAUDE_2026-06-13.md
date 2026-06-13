# CVF Agent Work Order: FPC-T4 Strategic Deferred Capability Reopen Decision For Claude - 2026-06-13

Memory class: POINTER_RECORD

Status: DISPATCH_READY_FOR_CLAUDE
Worker: Claude
Orchestrator / reviewer: Codex
Worker commit policy: WORKER_MUST_NOT_COMMIT
Commit mode: WORKER_MUST_NOT_COMMIT
Base head: 7fd250ad
dispatchBaseHead: `7fd250ad`
executionBaseHead: `WORKER_MUST_CAPTURE_BEFORE_EDITS`
closureBaseHead: `WORKER_MUST_NOT_SET`

completionReviewPath:
`docs/reviews/CVF_FPC_T4_STRATEGIC_DEFERRED_CAPABILITY_REOPEN_DECISION_COMPLETION_2026-06-13.md`

reviewerOwnedClosurePaths:

- `docs/baselines/CVF_GC018_FPC_T4_STRATEGIC_DEFERRED_CAPABILITY_REOPEN_DECISION_2026-06-13.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_FPC_T4_STRATEGIC_DEFERRED_CAPABILITY_REOPEN_DECISION_FOR_CLAUDE_2026-06-13.md`
- `docs/reference/CVF_FPC_T4_STRATEGIC_DEFERRED_CAPABILITY_REOPEN_DECISION_MATRIX_2026-06-13.md`
- `docs/reviews/CVF_FPC_T4_STRATEGIC_DEFERRED_CAPABILITY_REOPEN_DECISION_WORKER_RETURN_2026-06-13.md`
- `docs/reviews/CVF_FPC_T4_STRATEGIC_DEFERRED_CAPABILITY_REOPEN_DECISION_COMPLETION_2026-06-13.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION_MEMORY.md`
- `AGENT_HANDOFF_V18_2026-06-12.md`

## Purpose

The purpose is to produce a strategic FPC-T4 decision matrix for deferred CVF
foundation capabilities. The work must decide what remains deferred and what
may become a later bounded tranche; it must not implement the capability.

## Scope

Allowed scope is limited to the two deliverables listed in this work order.
Target surfaces are FPC-T4 planning, source-backed candidate ranking,
anti-overconstraint analysis, and co-work trace supervision boundary.

## Authority Chain

| Authority | Role |
| --- | --- |
| Operator instruction on 2026-06-13 | Authorizes high-value foundation continuation and forbids use-case or narrow-lane drift |
| FPC roadmap FPC-T4 row | Defines deferred capability reopen decision lane |
| GC-018 baseline | Defines dispatch boundary and source anchors |
| This work order | Defines Claude's allowed deliverables and return gates |
| Codex reviewer | Owns closure, commit, and session sync |

## Agent Roles

| Role | Owner | Authority |
| --- | --- | --- |
| Worker | Claude | Draft the two allowed deliverables only |
| Reviewer / committer | Codex | Review, run closure gates, commit if accepted, and update session continuity if needed |
| Operator | Human | Authorize scope expansion only |

## 0. Dispatch Summary

Create the FPC-T4 strategic deferred capability reopen decision matrix.

This is a high-foundation-value planning tranche. It must not implement a
runtime capability, mutate a registry, call a provider, run live proof, enter a
product use case, or drill into a small niche. The purpose is to decide which
large deferred CVF foundation gaps should remain deferred and which should
become future bounded tranches.

## Required First Reads

Read these before drafting:

| File | Required use |
| --- | --- |
| `AGENTS.md` | active governance instructions, source authority, work-order quality, AOT boundary |
| `CVF_SESSION_MEMORY.md` | front-door state |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | active handoff and current mode |
| `AGENT_HANDOFF_V18_2026-06-12.md` | active handoff context |
| `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | FPC-T4 scope and forbidden boundaries |
| `docs/reference/CVF_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_MATRIX_2026-06-13.md` | deferred capability source matrix |
| `docs/reference/CVF_FPC_T2_SYSTEM_LOOP_INTERLOCK_EXPANSION_DECISION_MATRIX_2026-06-13.md` | FPC-T2-C05 comparator |
| `docs/reference/CVF_FPC_T3_FOUNDATION_CHECKER_TEMPLATE_COVERAGE_PLAN_2026-06-13.md` | FPC-T3-C01 dependency context |
| `docs/reviews/CVF_FPC_T3_C04_C01_EPISTEMIC_WORK_ORDER_AND_PROCESS_PACKET_GUARD_COMPLETION_2026-06-13.md` | latest FPC-T3 closure evidence |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | Model Gateway capability source surface |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | Model Gateway provider registry source surface |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-gate.ts` | Model Gateway method-gate source surface |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` | Model Gateway exported surfaces |
| `EXTENSIONS/CVF_TRUST_SANDBOX/package.json` | Trust Sandbox package boundary |
| `EXTENSIONS/CVF_TRUST_SANDBOX/README.md` | Trust Sandbox coordination boundary |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/runtime-modules.ts` | runtime-module registry boundary |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/sandbox-contract-adapter.ts` | sandbox adapter boundary |
| `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | required work-order and trace sections |
| `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md` | Agent Operation Trace Block requirements |

Provider-specific memory files such as `CLAUDE.md`, Codex memory, Claude
memory, and IDE summaries are not CVF source authority. If read as local
operating guidance, re-verify every source fact against the governed files
above before citing it.

## 2. Allowed Deliverables

Create exactly these uncommitted files:

| Deliverable | Purpose |
| --- | --- |
| `docs/reference/CVF_FPC_T4_STRATEGIC_DEFERRED_CAPABILITY_REOPEN_DECISION_MATRIX_2026-06-13.md` | source-backed ranking matrix, candidate analysis, anti-overconstraint discipline, recommended next tranche |
| `docs/reviews/CVF_FPC_T4_STRATEGIC_DEFERRED_CAPABILITY_REOPEN_DECISION_WORKER_RETURN_2026-06-13.md` | worker return with evidence, gate results, actual changed set, negative search, pending-return gate |

No other file may be created, modified, deleted, renamed, formatted, or staged.

## Pre-Flight Checks

Claude must run and record:

| Check | Required action |
| --- | --- |
| Base HEAD | `git rev-parse --short HEAD` and record as `executionBaseHead` |
| Worktree status | `git status --short` before edits |
| Required reads | Read all files in Required First Reads before drafting |
| Scope collision | Confirm only the two allowed deliverables will be changed |

## Write Ownership

| Path | Owner | Allowed action |
| --- | --- | --- |
| `docs/reference/CVF_FPC_T4_STRATEGIC_DEFERRED_CAPABILITY_REOPEN_DECISION_MATRIX_2026-06-13.md` | Claude | Create only |
| `docs/reviews/CVF_FPC_T4_STRATEGIC_DEFERRED_CAPABILITY_REOPEN_DECISION_WORKER_RETURN_2026-06-13.md` | Claude | Create only |
| Any runtime/source/test/session/public-sync path | None | FORBIDDEN |
| Git index and commits | Codex | Claude must not stage or commit |

## 3. Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| FPC-T4 is the deferred capability reopen decision lane | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | line 276 | `FPC-T4` | FPC roadmap Work Plan | ACCEPT |
| Model Gateway and Sandbox Runtime implementation are forbidden in current FPC dispatch scope | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | line 141 | `Model Gateway or Sandbox Runtime implementation` | FPC roadmap forbidden scope | ACCEPT |
| FPC-T4 requires FPC-T3 closure plus operator decision | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | line 276 | `FPC-T3 closure plus operator decision` | FPC roadmap Work Plan | ACCEPT |
| FPC-T4 remains held until explicit operator decision | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | lines 498, 539 | `FPC-T4` | FPC roadmap next allowed move | ACCEPT |
| FPC closure does not prove provider/live readiness, Model Gateway, or Sandbox completion | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | line 688 | `completed provider/live readiness`, `completed Model Gateway`, `completed Sandbox` | FPC roadmap claim boundary | ACCEPT |
| Model Gateway provider routing is formally deferred and requires separate GC-018 plus operator decision | `docs/reference/CVF_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_MATRIX_2026-06-13.md` | line 378 | `Model Gateway (EPF provider routing)` | FPC-T1 audit matrix | ACCEPT |
| Sandbox Runtime physical isolation is formally deferred and requires separate GC-018 plus operator decision | `docs/reference/CVF_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_MATRIX_2026-06-13.md` | line 379 | `Sandbox Runtime (full physical isolation)` | FPC-T1 audit matrix | ACCEPT |
| Model Gateway has a provider capability registry source surface | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | line 42 | `PROVIDER_CAPABILITY_REGISTRY` | Model Gateway provider capability registry | ACCEPT |
| Model Gateway exposes a provider registry class | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | line 30 | `ProviderRegistry` | Model Gateway provider registry | ACCEPT |
| Model Gateway exposes provider method gate helpers | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-gate.ts` | lines 62, 78, 90 | `getProviderMethodContract`, `assertRegistryProviderMethodSupported`, `listRegistrySupportedMethods` | Model Gateway method gate | ACCEPT |
| Model Gateway public exports include registry and method-gate surfaces | `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` | lines 67, 122, 132-133 | `ProviderRegistry`, `PROVIDER_CAPABILITY_REGISTRY`, `getProviderMethodContract`, `listRegistrySupportedMethods` | Model Gateway public exports | ACCEPT |
| Trust Sandbox package exists as a coordination package | `EXTENSIONS/CVF_TRUST_SANDBOX/package.json` | lines 2, 4 | `cvf-trust-sandbox` | Trust Sandbox package metadata | ACCEPT |
| Trust Sandbox runtime module is recorded as a coordination package until a sandbox action is proven | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/runtime-modules.ts` | lines 152-159 | `trust-sandbox` | runtime module registry | ACCEPT |
| Sandbox adapter states no physical/server-side execution isolation in web API surface | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/sandbox-contract-adapter.ts` | line 11 | `no physical/server-side execution isolation` | sandbox contract adapter | ACCEPT |
| Sandbox adapter exposes simulated execution and audit-log surfaces | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/sandbox-contract-adapter.ts` | lines 113, 139, 214 | `auditLog`, `executeInSandbox`, `getSandboxAuditLog` | sandbox contract adapter | ACCEPT |
| FPC-T2-C05 is viable only after FPC-T3-C01 defines the upstream signal | `docs/reference/CVF_FPC_T2_SYSTEM_LOOP_INTERLOCK_EXPANSION_DECISION_MATRIX_2026-06-13.md` | line 497 | `FPC-T2-C05` | FPC-T2 decision matrix | ACCEPT |

## 4. New Doc-Only Fields

| Field | Purpose | Runtime authority |
| --- | --- | --- |
| `Strategic Reopen Candidate` | Names a deferred capability to rank in FPC-T4 | DOC_ONLY_NEW |
| `Reopen Disposition` | One of `KEEP_DEFERRED`, `REOPEN_AS_PLANNING_TRANCHE`, `REOPEN_AS_IMPLEMENTATION_CANDIDATE_LATER`, `BLOCKED_SOURCE_NOT_FOUND` | DOC_ONLY_NEW |
| `Foundation Value` | Ranks value to CVF core control surfaces, not product use cases | DOC_ONLY_NEW |
| `Anti-Overconstraint / Latency Impact` | Captures whether a proposed guard would slow ordinary CVF work too much | DOC_ONLY_NEW |
| `Co-Work Supervision Value` | Captures how well CVF can supervise Codex/Claude/future cowork surfaces by requiring traces | DOC_ONLY_NEW |

## 5. Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Source | Worker instruction | Status |
| --- | --- | --- | --- |
| FPC-T4 decides deferred capability reopen candidates after FPC-T3 and operator decision | FPC roadmap line 276 | Produce a decision matrix only | SATISFIED_FOR_DISPATCH |
| Model Gateway and Sandbox Runtime implementation stay forbidden | FPC roadmap line 141 | Analyze reopen boundaries but do not implement | SATISFIED_FOR_DISPATCH |
| Deferred Execution Plane capabilities should not preempt foundation audit | FPC roadmap line 635 | Compare readiness and recommend only bounded future tranches | SATISFIED_FOR_DISPATCH |
| Avoid use-case and small-niche drift | Operator instruction | Exclude Policy_Local, Document Translator, corpus ingestion, public product work, and narrow registry-only dispatch as primary lane | SATISFIED_FOR_DISPATCH |

## Reviewer Closure Conversion Block

completionReviewPath:
`docs/reviews/CVF_FPC_T4_STRATEGIC_DEFERRED_CAPABILITY_REOPEN_DECISION_COMPLETION_2026-06-13.md`

reviewerOwnedClosurePaths:

- `docs/baselines/CVF_GC018_FPC_T4_STRATEGIC_DEFERRED_CAPABILITY_REOPEN_DECISION_2026-06-13.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_FPC_T4_STRATEGIC_DEFERRED_CAPABILITY_REOPEN_DECISION_FOR_CLAUDE_2026-06-13.md`
- `docs/reference/CVF_FPC_T4_STRATEGIC_DEFERRED_CAPABILITY_REOPEN_DECISION_MATRIX_2026-06-13.md`
- `docs/reviews/CVF_FPC_T4_STRATEGIC_DEFERRED_CAPABILITY_REOPEN_DECISION_WORKER_RETURN_2026-06-13.md`
- `docs/reviews/CVF_FPC_T4_STRATEGIC_DEFERRED_CAPABILITY_REOPEN_DECISION_COMPLETION_2026-06-13.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION_MEMORY.md`
- `AGENT_HANDOFF_V18_2026-06-12.md`

## Intake Role Routing Decision

| Field | Decision |
| --- | --- |
| Intake item | FPC-T4 strategic deferred capability reopen decision |
| Scope classification | source-backed foundation decision matrix only |
| Risk sensitivity | high governance sensitivity; no implementation authority |
| Selected route mode | MULTI_AGENT_MULTI_ROLE |
| Selected role route | Claude worker drafts decision matrix; Codex reviewer/committer closes |
| routeMode | MULTI_AGENT_MULTI_ROLE |
| Routed role | Claude as worker |
| Reviewer | Codex |
| Commit authority | Codex only |
| Runtime/source authority | read-only source inspection only |
| Live/provider authority | NONE |
| Public-sync authority | NONE |
| Escalation condition | Stop for implementation, runtime mutation, provider/live proof, registry mutation, public-sync, secrets, OS/endpoint telemetry, destructive action, or commit request |
| Disposition | DISPATCHED_UNDER_WORKER_MUST_NOT_COMMIT |

## Current Runtime Freshness Verification

| Runtime/source surface | Freshness check | Disposition |
| --- | --- | --- |
| Model Gateway provider capability registry | `rg -n "PROVIDER_CAPABILITY_REGISTRY" EXTENSIONS/CVF_MODEL_GATEWAY` returned current source and tests | CURRENT_SOURCE_SURFACE_FOUND |
| Model Gateway provider registry | `rg -n "ProviderRegistry" EXTENSIONS/CVF_MODEL_GATEWAY` returned current source and tests | CURRENT_SOURCE_SURFACE_FOUND |
| Trust Sandbox module boundary | `rg -n "trust-sandbox|Trust Sandbox" EXTENSIONS docs` returned package and runtime-module entries | CURRENT_SOURCE_SURFACE_FOUND |
| Sandbox adapter boundary | `rg -n "executeInSandbox|auditLog|no physical" EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib` returned adapter evidence | CURRENT_SOURCE_SURFACE_FOUND |
| Implementation readiness | No runtime files are authorized for mutation by this work order | NOT_IMPLEMENTED_BY_THIS_PACKET |

## Negative Search And Collision Discipline

| Search command or query | Search roots | Result | Disposition |
| --- | --- | --- | --- |
| `rg -n "Model Gateway|Sandbox Runtime|trust-sandbox|ProviderRegistry|PROVIDER_CAPABILITY_REGISTRY|executeInSandbox|FPC-T4|FPC-T2-C05" docs EXTENSIONS` | `docs`, `EXTENSIONS` | Same-token collisions found in roadmap, reference plans, runtime source, and tests | COLLISION_RECORDED_AS_SOURCE_INPUT |
| `rg -n "Policy_Local|Document Translator|DT-CVF|public-sync|DASHSCOPE_API_KEY|DEEPSEEK_API_KEY|ALIBABA_API_KEY|Sysmon|endpoint|T12|rawMemoryReleased" docs/reference docs/roadmaps docs/work_orders docs/reviews` | `docs/reference`, `docs/roadmaps`, `docs/work_orders`, `docs/reviews` | Same-token collisions expected because forbidden boundaries and governance standards mention these tokens | COLLISION_RECORDED_AS_FORBIDDEN_SCOPE_CONTEXT |
| `rg -n "COMPLETE_PENDING_REVIEW|BLOCKED_SCOPE_EXPANSION|DOC_ONLY_NEW" docs/reference docs/work_orders docs/reviews` | governed docs | Same-token collisions found in prior work orders and reviews; this work order uses the terms as return statuses and doc-only classifications, not absent-source claims | COLLISION_RECORDED_AS_STATUS_VOCABULARY |
| `rg -n "KEEP_DEFERRED|REOPEN_AS_PLANNING_TRANCHE|REOPEN_AS_IMPLEMENTATION_CANDIDATE_LATER" docs/baselines docs/reference docs/work_orders docs/reviews` | governed docs | Same-token collisions found in this dispatch packet only at authoring time; values are new doc-only disposition vocabulary, not runtime/source claims | COLLISION_RECORDED_AS_DOC_ONLY_DISPOSITION_VOCABULARY |
| `rg -n "\bHEAD\b" docs/reference docs/work_orders docs/reviews` | governed docs | Same-token collisions found in existing work orders and reviews; this work order uses `HEAD` only as git-anchor vocabulary | COLLISION_RECORDED_AS_GIT_ANCHOR_VOCABULARY |
| `git status --short` | repo root | Two new dispatch files only at authoring time | MANIFEST_BOUNDARY_RECORDED |
| `git diff --name-status` | repo root | Untracked files are not shown by raw diff until staged; AOT checker observes changed paths from worktree status | TOOL_BOUNDARY_RECORDED |

## 6. Task Instructions

1. Read all required files and source-verify every runtime/source claim.
2. Create the FPC-T4 decision matrix deliverable.
3. Include at minimum these candidate rows:
   - Model Gateway provider-method/capability registry reopen path.
   - Trust Sandbox / Sandbox Runtime physical-isolation boundary.
   - Co-work trace supervision over agent/provider execution surfaces.
   - FPC-T2-C05 evidence-to-claim registry follow-up as a comparator.
4. Rank candidates by foundation value, source confidence, dependency readiness,
   anti-overconstraint/latency impact, co-work supervision value, and risk.
5. Separate `reopen decision`, `future planning tranche`, and `future
   implementation candidate`. Do not collapse decision planning into
   implementation authorization.
6. Include a recommendation for the next tranche only if it is high-value,
   source-backed, and not a use case or narrow niche.
7. Include a "do not over-tighten" analysis explaining which controls should
   stay lightweight, phase-placed, or deferred to avoid CVF latency.
8. Include a worker-return packet with the required Agent Operation Trace Block,
   Worker Pending-Return Gate, Negative Search And Collision Discipline,
   Public Export Disposition, and Finding-To-Governance Learning Disposition.

## Execution Plan

| Step | Action |
| --- | --- |
| 1 | Capture `executionBaseHead` and clean/dirty worktree state |
| 2 | Complete required reads and source verification |
| 3 | Draft the decision matrix with candidate ranking and claim boundary |
| 4 | Draft the worker return with gate evidence and trace block |
| 5 | Run required negative searches and local gates |
| 6 | Return uncommitted artifacts to Codex |

## Evidence Requirements

Evidence must include source citations, negative-search collision rows,
expected-vs-actual manifest reconciliation, gate command results, and explicit
N/A-with-reason rows for public-sync, live/provider proof, runtime mutation,
registry mutation, and implementation readiness.

## Acceptance Criteria

| Criterion | Required result |
| --- | --- |
| Exact files | Only the two allowed deliverables are changed |
| Foundation value | Candidate ranking addresses strategic CVF foundation gaps |
| No use-case drift | No Policy_Local, Document Translator, corpus ingestion, or public product lane |
| No implementation | No runtime/source/test/session/public-sync mutation |
| Anti-overconstraint | Latency impact is analyzed and broad high-latency guards are avoided |
| Co-work supervision | CVF supervises by trace requirements, not cowork product development |
| Gates | Worker-return fast gate, reviewer-fast, and diff check pass or record blocker |

## Review Gate

Codex will reject the return if any allowed deliverable is missing, any
unauthorized file is changed, source verification contains unsupported ACCEPT
claims, the candidate matrix authorizes implementation, or the latency
discipline is absent.

## Closure Checklist

| Closure item | Owner | Required disposition |
| --- | --- | --- |
| Claude deliverables reviewed | Codex | Required before commit |
| Worker gates checked | Codex | Required before commit |
| Completion review filed | Codex | Required if material return is accepted |
| Pre-closure autorun gate | Codex | Required on committed material range |
| Session state/front door/handoff sync | Codex | Required if mode or next allowed move changes |
| Public catalog disposition | Codex | N/A unless public-sync is separately authorized |

## Operator Checkpoint

Operator checkpoint is required only if Claude or Codex needs to expand beyond
decision planning, mutate runtime/source/test/session/public-sync files, run
provider/live proof, inspect secrets, configure OS/endpoint telemetry, perform
destructive action, or change the claim boundary.

## 7. Co-Work Supervision Boundary

CVF does not develop `codex_cowork`, `claude_cowork`, or any cowork product.
OpenAI and Anthropic own their agent products and execution platforms.

FPC-T4 may evaluate only how CVF supervises agent/provider work by requiring
repo-local traces, expected manifests, source verification, execution
attribution, and closure evidence. Do not propose agent computer-control
features, endpoint control, hidden telemetry, provider-internal logs, or OS
identity proof.

## 8. Anti-Overconstraint And Latency Discipline

Do not recommend a guard that makes every agent action wait for heavy manual
review. Favor:

| Control need | Preferred CVF placement |
| --- | --- |
| Traceability for governed artifacts | Agent Operation Trace Block plus expected manifest |
| Evidence-backed planning | Source Verification Block and Epistemic Process Block |
| Strategic deferred capability decision | FPC-T4 decision matrix |
| Runtime/provider proof | later explicit implementation tranche only |
| OS/user attribution | out of scope unless separately authorized |

If a candidate would require high-latency universal blocking, rank it lower or
recommend a narrower phase placement.

## 9. Required Deliverable Structure

The decision matrix must include:

- Purpose
- Scope Boundary
- Source Authority Table
- Source Verification Block
- Strategic Reopen Candidate Matrix
- Candidate Ranking
- Dependency Map
- Anti-Overconstraint / Latency Impact
- Co-Work Supervision Value
- Recommended First Tranche
- Rejected Or Kept-Deferred Candidates
- Negative Search And Collision Discipline
- Finding-To-Governance Learning Disposition
- Agent Operation Trace Block
- Public Export Disposition
- Claim Boundary

The worker return must include:

- Summary
- Changed Files
- Source Verification Summary
- Worker Pending-Return Gate
- Agent Operation Trace Block
- Negative Search And Collision Discipline
- Gate Results
- Public Export Disposition
- Claim Boundary

## 10. Required Negative Searches

Run and record safe summaries for searches covering at least:

```powershell
rg -n "Model Gateway|Sandbox Runtime|trust-sandbox|ProviderRegistry|PROVIDER_CAPABILITY_REGISTRY|executeInSandbox|FPC-T4|FPC-T2-C05" docs EXTENSIONS
rg -n "Policy_Local|Document Translator|DT-CVF|public-sync|DASHSCOPE_API_KEY|DEEPSEEK_API_KEY|ALIBABA_API_KEY|Sysmon|endpoint|T12|rawMemoryReleased" docs/reference docs/roadmaps docs/work_orders docs/reviews
git status --short
git diff --name-status
```

Do not print or inspect raw secret values. If an environment file is encountered,
record only that secret inspection is out of scope.

## 11. Worker Pending-Return Gate

Claude may return `COMPLETE_PENDING_REVIEW` only when every row is PASS:

| Gate | Required evidence | Status |
| --- | --- | --- |
| Exact deliverables only | `git status --short` shows only the two allowed deliverables | PENDING |
| No implementation | `git diff --name-status` shows no runtime/source/test/session/public-sync mutation | PENDING |
| Source verification complete | Source Verification Block has no `BLOCKED_SOURCE_NOT_FOUND` for accepted claims | PENDING |
| Decision/implementation separation | Candidate matrix does not authorize implementation | PENDING |
| Anti-overconstraint present | Latency discipline section exists and ranks high-latency controls lower or phase-places them | PENDING |
| Co-work supervision boundary present | CVF supervises through traces; CVF does not build cowork products | PENDING |
| Agent Operation Trace Block complete | Expected and actual manifests match | PENDING |
| Public Export Disposition present | `DEFERRED_PRIVATE_ONLY` | PENDING |
| Worker did not commit | HEAD unchanged from worker start | PENDING |
| `git diff --check` | PASS | PENDING |
| `python governance/compat/run_worker_return_fast_gate.py` | PASS | PENDING |
| `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast` | PASS | PENDING |

## Worker Autonomy / No-Question Rule

Worker-Autonomy / No-Question Rule: any governance gate failure within the
Allowed scope and Write Ownership must be repaired and rerun by Claude before
return. Routine allowed-scope fixes are mandatory.

Claude must stop and return to Codex only when repair would exceed Allowed
scope, change the claim boundary, require forbidden paths, open public-sync,
run live/provider proof, consume secrets/quota, configure OS audit or endpoint
monitoring, perform destructive action, or require a commit.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Codex dispatcher |
| Provider or surface | Codex CLI |
| Session or invocation | dispatchBaseHead `7fd250ad` |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | `rg`, `Test-Path`, `apply_patch`, governance gates |
| Target paths | `docs/baselines/CVF_GC018_FPC_T4_STRATEGIC_DEFERRED_CAPABILITY_REOPEN_DECISION_2026-06-13.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_FPC_T4_STRATEGIC_DEFERRED_CAPABILITY_REOPEN_DECISION_FOR_CLAUDE_2026-06-13.md` |
| Allowed scope source | operator authorization on 2026-06-13 plus FPC roadmap FPC-T4 row |
| Before status evidence | `git status --short` clean before dispatch packet creation |
| After status evidence | pending dispatch packet files in `git status --short` |
| Diff evidence | `git diff --name-status` after packet creation |
| Approval boundary | operator authorized high-value CVF foundation continuation without use cases or narrow lanes |
| Claim boundary | repo-local dispatch trace only; no OS/user attribution, endpoint telemetry, provider-internal log, public readiness, or production readiness claim |
| Agent type | Codex |
| Invocation ID | `dispatchBaseHead=7fd250ad` |
| Expected manifest | `docs/baselines/CVF_GC018_FPC_T4_STRATEGIC_DEFERRED_CAPABILITY_REOPEN_DECISION_2026-06-13.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_FPC_T4_STRATEGIC_DEFERRED_CAPABILITY_REOPEN_DECISION_FOR_CLAUDE_2026-06-13.md` |
| Actual changed set | `docs/baselines/CVF_GC018_FPC_T4_STRATEGIC_DEFERRED_CAPABILITY_REOPEN_DECISION_2026-06-13.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_FPC_T4_STRATEGIC_DEFERRED_CAPABILITY_REOPEN_DECISION_FOR_CLAUDE_2026-06-13.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: dispatch creates new governed packet files and deletes or renames no protected path |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: A strategic FPC-T4 decision matrix will likely
rank the Trust Sandbox / Sandbox Runtime boundary and Model Gateway capability
registry boundary above a narrow FPC-T2-C05 registry-entry follow-up because
they decide larger CVF foundation surfaces while remaining non-implementation.

Observation Plan: Verify current source surfaces, compare candidate foundation
value and dependency readiness, run negative searches, and record whether the
actual evidence confirms or revises the predicted ranking.

Claim Update Requirement: The worker return must record whether this prediction
was confirmed, narrowed, revised, or invalidated. If the ranking changes, cite
the source-backed reason.

## 14. Forbidden Scope

This work order authorizes no runtime source mutation, Model Gateway
implementation, Sandbox Runtime implementation, provider/API use, live
governance proof, infrastructure work, OS/Sysmon/endpoint monitoring,
file-watcher service, public-sync, public catalog claim, Document Translator,
Policy_Local, corpus ingestion, T12, memory release, raw memory reinjection,
autonomous mutation, registry mutation, FPC-T2-C05 registry entry, or cowork
product development.

## 15. Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only when both deliverables are complete,
trace blocks are complete, exact changed set matches the allowed manifest,
gates pass, and HEAD remains unchanged.

Return `BLOCKED_SOURCE_NOT_FOUND` if a named runtime/source claim cannot be
verified against governed source.

Return `BLOCKED_SCOPE_EXPANSION` if useful progress requires implementation,
runtime/provider/live work, public-sync, session-state mutation, secrets,
registry mutation, or any forbidden scope.

Return `BLOCKED_OVERCONSTRAINT_RISK` if the only viable recommendation would
impose broad high-latency controls on ordinary CVF operation.

## 16. Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance foundation-planning dispatch. Public-sync is not
authorized.

## Claim Boundary

This dispatch authorizes source-backed decision planning only. It does not
prove provider/live readiness, completed Model Gateway, completed Sandbox
Runtime, OS/user attribution, endpoint telemetry, production readiness, public
readiness, cost optimization, output quality, raw memory release, or autonomous
mutation.

rawMemoryReleased=false
