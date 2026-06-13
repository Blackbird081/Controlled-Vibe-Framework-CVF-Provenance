# CVF GC-018 FPC-T4 Strategic Deferred Capability Reopen Decision Baseline - 2026-06-13

Memory class: POINTER_RECORD

Status: CLOSED_PASS_BOUNDED
Owner: Codex Orchestrator
Worker target: Claude
Base head: 7fd250ad

## Purpose

Create a source-backed FPC-T4 decision packet for strategic deferred capability
reopen candidates that have high CVF foundation value without entering a use
case, small niche, runtime implementation, provider proof, or public-sync lane.

This baseline authorizes a decision matrix only. It does not authorize Model
Gateway implementation, Sandbox Runtime implementation, provider/API calls,
physical isolation work, OS monitoring, endpoint telemetry, public export,
Policy_Local, Document Translator, corpus ingestion, T12, raw memory release,
or autonomous mutation.

## Operator Authorization

The operator authorized continuation only if the work has high CVF foundation
value and does not enter use cases or narrow niches.

Disposition: FPC-T4 is selected over an immediate FPC-T2-C05 registry-entry
dispatch because FPC-T4 decides whether large deferred foundation capabilities
should remain parked or become future governed tranches. FPC-T2-C05 remains
valid but narrower.

## Scope Classification

| Axis | Disposition |
| --- | --- |
| Work type | Source-backed planning, ranking, and decision matrix |
| Foundation value | HIGH |
| Use-case dependency | NONE |
| Runtime mutation | FORBIDDEN |
| Provider/live proof | FORBIDDEN |
| Public-sync | FORBIDDEN |
| Implementation authorization | NONE |
| Worker commit authority | WORKER_MUST_NOT_COMMIT |

## Decision Baseline

The baseline decision is to dispatch FPC-T4 as a strategic deferred capability
reopen decision packet, not as an implementation packet. The proposed tranche
is a source-backed matrix that ranks foundation capability reopen candidates
and recommends only a future bounded tranche if the evidence supports it.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| FPC-T4 is the deferred capability reopen decision lane | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | line 276 | `FPC-T4` | FPC roadmap Work Plan | ACCEPT |
| Model Gateway and Sandbox Runtime implementation are forbidden in the current FPC dispatch boundary | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | line 141 | `Model Gateway or Sandbox Runtime implementation` | FPC roadmap forbidden scope | ACCEPT |
| FPC-T4 requires FPC-T3 closure plus operator decision | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | line 276 | `FPC-T3 closure plus operator decision` | FPC roadmap Work Plan | ACCEPT |
| Deferred Execution Plane capabilities should not preempt foundation audit | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | line 635 | `FPC-T4 only after T1/T2/T3` | FPC roadmap closure diff gate | ACCEPT |
| Model Gateway provider routing is formally deferred and requires separate GC-018 plus operator decision | `docs/reference/CVF_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_MATRIX_2026-06-13.md` | line 378 | `Model Gateway (EPF provider routing)` | FPC-T1 audit matrix | ACCEPT |
| Sandbox Runtime physical isolation is formally deferred and requires separate GC-018 plus operator decision | `docs/reference/CVF_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_MATRIX_2026-06-13.md` | line 379 | `Sandbox Runtime (full physical isolation)` | FPC-T1 audit matrix | ACCEPT |
| Model Gateway has a provider capability registry source surface | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | line 42 | `PROVIDER_CAPABILITY_REGISTRY` | Model Gateway provider capability registry | ACCEPT |
| Model Gateway exposes provider registry and method gate surfaces | `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` | lines 67, 122, 132-133 | `ProviderRegistry`, `PROVIDER_CAPABILITY_REGISTRY`, `getProviderMethodContract`, `listRegistrySupportedMethods` | Model Gateway public exports | ACCEPT |
| Trust Sandbox is currently represented as a coordination package until a sandbox action is proven | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/runtime-modules.ts` | lines 152-159 | `trust-sandbox` | runtime module registry | ACCEPT |
| Web sandbox adapter records no physical/server-side isolation in the web API surface | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/sandbox-contract-adapter.ts` | line 11 | `no physical/server-side execution isolation` | sandbox contract adapter | ACCEPT |
| Web sandbox adapter exposes a simulated execution entrypoint and audit log | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/sandbox-contract-adapter.ts` | lines 113, 139, 214 | `auditLog`, `executeInSandbox`, `getSandboxAuditLog` | sandbox contract adapter | ACCEPT |
| FPC-T2-C05 is a valid but narrower registry-follow-up candidate after FPC-T3-C01 | `docs/reference/CVF_FPC_T2_SYSTEM_LOOP_INTERLOCK_EXPANSION_DECISION_MATRIX_2026-06-13.md` | line 497 | `FPC-T2-C05` | FPC-T2 decision matrix | ACCEPT |

## New Doc-Only Fields

| Field | Purpose | Runtime authority |
| --- | --- | --- |
| `Strategic Reopen Candidate` | Names a deferred foundation capability for FPC-T4 ranking | DOC_ONLY_NEW |
| `Reopen Disposition` | Records `KEEP_DEFERRED`, `REOPEN_AS_PLANNING_TRANCHE`, `REOPEN_AS_IMPLEMENTATION_CANDIDATE_LATER`, or `BLOCKED_SOURCE_NOT_FOUND` | DOC_ONLY_NEW |
| `Anti-Overconstraint / Latency Impact` | Records whether a proposed control would slow ordinary CVF work too much | DOC_ONLY_NEW |
| `Co-Work Supervision Value` | Records whether a candidate improves traceability for Codex/Claude or future cowork surfaces without building cowork products | DOC_ONLY_NEW |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Source | FPC-T4 dispatch handling | Status |
| --- | --- | --- | --- |
| Deferred capability reopen decision occurs only after FPC-T3 and operator decision | FPC roadmap line 276 | FPC-T3 is closed in current session state; operator authorized high-value foundation continuation | SATISFIED |
| Model Gateway and Sandbox Runtime are not implemented by FPC-T4 | FPC roadmap line 141 | Work order forbids implementation and provider/live proof | SATISFIED |
| Deferred execution-plane capabilities must not preempt foundation audit | FPC roadmap line 635 | FPC-T1/T2/T3 are complete enough for a decision packet; work remains planning only | SATISFIED |
| Avoid use-case and narrow-lane drift | Operator instruction | Work order excludes Policy_Local, Document Translator, corpus ingestion, public product lanes, and niche registry-only dispatch | SATISFIED |

## Current Runtime Freshness Verification

| Runtime/source surface | Freshness check | Disposition |
| --- | --- | --- |
| Model Gateway provider capability registry | `rg -n "PROVIDER_CAPABILITY_REGISTRY" EXTENSIONS/CVF_MODEL_GATEWAY` returned current source and tests | CURRENT_SOURCE_SURFACE_FOUND |
| Model Gateway provider registry | `rg -n "ProviderRegistry" EXTENSIONS/CVF_MODEL_GATEWAY` returned current source and tests | CURRENT_SOURCE_SURFACE_FOUND |
| Trust Sandbox module boundary | `rg -n "trust-sandbox|Trust Sandbox" EXTENSIONS docs` returned package and runtime-module entries | CURRENT_SOURCE_SURFACE_FOUND |
| Sandbox adapter boundary | `rg -n "executeInSandbox|auditLog|no physical" EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib` returned adapter evidence | CURRENT_SOURCE_SURFACE_FOUND |
| Implementation readiness | No runtime files are authorized for mutation by this baseline | NOT_IMPLEMENTED_BY_THIS_PACKET |

## Evidence Verification

This baseline is verified by source citations, negative-search collision
evidence, expected-manifest trace, and pre-dispatch governance gates. Runtime
behavior, provider behavior, physical sandbox isolation, public readiness, and
production readiness are outside the verified claim.

## Negative Search And Collision Discipline

| Search command or query | Search roots | Result | Disposition |
| --- | --- | --- | --- |
| `rg -n "Model Gateway|Sandbox Runtime|trust-sandbox|ProviderRegistry|PROVIDER_CAPABILITY_REGISTRY|executeInSandbox|FPC-T4|FPC-T2-C05" docs EXTENSIONS` | `docs`, `EXTENSIONS` | Same-token collisions found in roadmap, reference plans, runtime source, and tests | COLLISION_RECORDED_AS_SOURCE_INPUT |
| `rg -n "Policy_Local|Document Translator|DT-CVF|public-sync|DASHSCOPE_API_KEY|DEEPSEEK_API_KEY|ALIBABA_API_KEY|Sysmon|endpoint|T12|rawMemoryReleased" docs/reference docs/roadmaps docs/work_orders docs/reviews` | governed docs only | Same-token collisions expected because forbidden boundaries and governance standards mention these tokens | COLLISION_RECORDED_AS_FORBIDDEN_SCOPE_CONTEXT |
| `rg -n "DOC_ONLY_NEW" docs/reference docs/work_orders docs/reviews` | governed docs | Same-token collisions found in existing dispatch packets; this baseline uses `DOC_ONLY_NEW` only as doc-only field classification | COLLISION_RECORDED_AS_DOC_ONLY_VOCABULARY |
| `rg -n "KEEP_DEFERRED|REOPEN_AS_PLANNING_TRANCHE|REOPEN_AS_IMPLEMENTATION_CANDIDATE_LATER" docs/baselines docs/reference docs/work_orders docs/reviews` | governed docs | Same-token collisions found in this dispatch packet only at authoring time; values are new doc-only disposition vocabulary, not runtime/source claims | COLLISION_RECORDED_AS_DOC_ONLY_DISPOSITION_VOCABULARY |
| `git status --short` | repo root | Two new dispatch files only at authoring time | MANIFEST_BOUNDARY_RECORDED |
| `git diff --name-status` | repo root | Untracked files are not shown by raw diff until staged; AOT checker observes changed paths from worktree status | TOOL_BOUNDARY_RECORDED |

## Candidate Set

Claude must evaluate at least these candidates:

| Candidate | Required boundary |
| --- | --- |
| Model Gateway provider-method/capability registry reopen path | Decision only; no provider/API call and no runtime routing implementation |
| Trust Sandbox / Sandbox Runtime physical-isolation boundary | Decision only; distinguish coordination package, simulated adapter, and physical isolation gap |
| Co-work trace supervision over agent/provider execution surfaces | CVF supervises by requiring agent traces; CVF does not build cowork products |
| FPC-T2-C05 evidence-to-claim registry follow-up | Comparator only; valid but likely narrower than FPC-T4 strategic decisions |

## Anti-Overconstraint And Latency Discipline

The FPC-T4 packet must not recommend a broad checkpoint that makes every small
agent action wait on heavy review. Recommended controls should be phase-placed:

| Control type | Preferred placement |
| --- | --- |
| Source-backed decision matrix | planning and pre-dispatch |
| Manifest/trace coverage | reviewer-fast and pre-closure for governed artifacts |
| Runtime/provider/live proof | only in a later explicitly authorized implementation tranche |
| OS or endpoint telemetry | out of CVF source-control scope unless separately authorized |

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

Observation Plan: Claude must verify current source surfaces, negative-search
for collisions and forbidden scope, then compare foundation value, risk,
latency burden, dependency readiness, and co-work trace supervision value.

Claim Update Requirement: The worker return must record whether the prediction
was confirmed, narrowed, revised, or invalidated. If FPC-T2-C05 ranks higher,
the worker must explain why a narrower registry follow-up provides higher
foundation value than strategic deferred-capability decisions.

## Dependency Release And Next-Work-Order Refresh

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| FPC-T3 closure | Current active session state identifies `fpc_t3_c04_c01_epistemic_work_order_and_process_packet_guard_closed_pass_bounded` | RELEASED_FOR_DECISION_PLANNING_ONLY |
| Operator decision for FPC-T4 | Operator authorized continuation only if foundation value is high and no use-case or narrow lane is entered | RELEASED_FOR_DECISION_PLANNING_ONLY |
| Implementation readiness | No implementation tranche is authorized | NOT_RELEASED |
| Provider/live readiness | No provider/live proof is authorized | NOT_RELEASED |

## Forbidden Scope

This baseline authorizes no runtime source mutation, Model Gateway
implementation, Sandbox Runtime implementation, provider/API use, live
governance proof, infrastructure work, OS/Sysmon/endpoint monitoring,
file-watcher service, public-sync, public catalog claim, Document Translator,
Policy_Local, corpus ingestion, T12, memory release, raw memory reinjection,
autonomous mutation, registry mutation, or cowork product development.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance foundation-planning dispatch. Public-sync is not
authorized.

## Claim Boundary

This baseline authorizes only repo-local, source-backed decision planning for
FPC-T4. It does not prove or authorize runtime behavior, provider/live behavior,
physical isolation, public readiness, production readiness, cowork product
development, raw memory release, or autonomous mutation.

rawMemoryReleased=false
