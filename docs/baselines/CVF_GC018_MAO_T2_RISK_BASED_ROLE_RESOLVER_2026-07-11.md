# CVF GC-018 Baseline - MAO-T2 Risk-Based Role Resolver

Memory class: governed-baseline

Status: DISPATCH_READY

Date: 2026-07-11

Batch: MAO-T2

dispatchBaseHead: `8b9f8f528`

executionBaseHead: capture actual clean post-dispatch-sync HEAD before editing.

closureBaseHead: N/A with reason: pending worker return and reviewer closure.

## Purpose

Authorize one bounded no-commit implementation of the MAO control-plane role
resolver. The resolver defaults to one worker and returns a deterministic
admission receipt without invoking a provider.

## Scope / Target / Owner Boundary

Allowed material is one resolver module, one focused test, one local MAO barrel
update, and one worker-return packet. Provider routing, adapters, queues, UI,
workspace/session state, public-sync, root barrels, and MAO-T3+ are excluded.

## Decision / Baseline / Proposed Tranche

MAO-T1 is accepted at `01618e9dc`. MAO-T2 may implement the T0-defined role
resolution decisions and evidence requirements as a pure control-plane policy
function. Single-worker admission is the default. Multi-role admission must be
bounded by risk, decomposability, write isolation or serialization, capability,
budget, closer, source-packet, and checkpoint evidence.

## Evidence / Verification

- Roadmap MAO-T2 deliverables: role resolver, admission/rejection reasons,
  human-checkpoint result, and budget plan; no provider invocation.
- T0 contract Role Resolver Ownership and Risk-Based Role Model define the
  authoritative decisions and route conditions.
- T0 schema defines `riskLevel`, `budgetAllocation`, `taskDefinition`, and
  `roleResolutionReceipt`.
- T1 source provides compiled graph, authority, task-role, scope, and budget
  inputs at material commit `01618e9dc`.

## Dependency Release Evidence

| Dependency | Artifact | Commit | Disposition |
|---|---|---|---|
| MAO-T1 accepted | `docs/reviews/CVF_MAO_T1_TASK_GRAPH_AND_STATE_CONTRACT_COMPLETION_2026-07-11.md` | `01618e9dc` | `REVIEWER_ACCEPTED_BOUNDED` |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MAO-T2 --title "Risk-Based Role Resolver" --date 2026-07-11 --base 8b9f8f528 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic worker dispatch plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | all placeholders replaced with MAO-T2 source-backed controls |
| checkerReadAheadConfirmation | applicable checker sources read before final authoring |
| docOnlyNewFields | new resolver-local reason vocabulary will be implemented, not claimed as existing |
| claimBoundary | dispatch provenance only |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| MAO-T2 deliverables and no-provider boundary | `docs/roadmaps/CVF_MULTI_AGENT_ORCHESTRATION_RUNTIME_FOUNDATION_ROADMAP_2026-07-11.md` | Work Plan And Dependencies / MAO-T2 | `MAO-T2 - Risk-Based Role Resolver` | roadmap tranche | ACCEPT |
| resolver ownership and four decisions | `docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_CONTRACT.md` | Role Resolver Ownership | `role resolver` | MAO T0 contract | ACCEPT |
| risk routes and evidence | `docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_CONTRACT.md` | Risk-Based Role Model | `Risk-Based Role Model` | MAO T0 contract | ACCEPT |
| risk, budget, task, and receipt fields | `docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_SCHEMA.json` | definitions | `riskLevel`, `budgetAllocation`, `taskDefinition`, `roleResolutionReceipt` | Draft 2020-12 schema | ACCEPT |
| compiled graph and authority inputs | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.graph.contract.ts` | exported types and compiler | `MaoCompiledTaskGraph`, `MaoAuthorityEnvelope`, `MaoTaskDefinition` | MAO-T1 task graph contract | ACCEPT |

## Current Runtime Freshness Verification

The source-fidelity pass used current files at `8b9f8f528`; all ACCEPT paths and
symbols exist. Proposed MAO-T2 module symbols are new and are not represented as
existing source facts.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`runtime implementation`, role=`worker`, lifecyclePhase=`implementation`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "runtime implementation" --role worker --lifecycle-phase implementation --surface-selector "multi-agent orchestration role resolver" --risk-ceiling HIGH --max-results 20 --json`

Returned defects: NONE_RETURNED

Disclosed defectIds: N/A with reason: NONE_RETURNED.

The empty packet does not prove that any caller read or understood the registry.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | `DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; Source Verification Block; ADIF query; public disposition |
| gateRunPurpose | confirmation and evidence after source-backed authoring; not first discovery |
| claimBoundary | packet shape and source fidelity only |

## Intake Role Routing Decision

| Question | Disposition |
|---|---|
| External knowledge intake | NOT_APPLICABLE_WITH_REASON: implementation uses CVF-governed source only. |
| External agent CLI or MCP | CONTRACT_ONLY: no adapter or external invocation is authorized. |
| Provider or live proof | FORBIDDEN for MAO-T2. |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | runtime/provider/mcp/readiness claim |
| Chain map route | NOT_APPLICABLE_WITH_REASON |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | paired MAO-T2 baseline and work order |
| Disposition | NOT_APPLICABLE_WITH_REASON: CVF-governed source only |
| Claim boundary | no external knowledge absorption claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Next action: retain in provenance through MAO-T9 closure and require a separate
public-safe projection packet before any export.

## Machine Closure Package

| Field | Value |
|---|---|
| Baseline state | `DISPATCH_READY` |
| Dependency | released by `01618e9dc` |
| Commit mode | `WORKER_MUST_NOT_COMMIT` |
| Runtime claim | local deterministic control-plane policy only |
| Next action | execute only under the paired work order |

## Acceptance Receipt Assertion Matrix

| Assertion | Required evidence |
|---|---|
| default route is one worker | focused positive and negative tests |
| fan-out is bounded | budget, risk, overlap, capability, closer, packet, and checkpoint tests |
| every decision explains itself | deterministic role-resolution receipt assertions |
| no provider invocation | changed-set and dependency scan |

## Claim Boundary

This baseline authorizes a local deterministic role-admission policy only. It
does not authorize provider selection/invocation, adapters, queues, UI, commit,
session mutation, public export, or production orchestration claims.
