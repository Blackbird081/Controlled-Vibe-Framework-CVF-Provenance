# CVF GC-018 Baseline - MAO-T4 Reviewer Isolation, Dissent, And Revision Loop

Memory class: governed-baseline

Status: DISPATCH_READY

Date: 2026-07-11

Batch: MAO-T4

dispatchBaseHead: `300c9dfa3`

executionBaseHead: capture actual clean post-dispatch-sync HEAD before editing.

closureBaseHead: N/A with reason: worker and reviewer conversion have not occurred.

## Purpose

Authorize a local reviewer-isolation packet builder, recomputation contract,
self-approval guard, dissent/revision ledger, and bounded repair/escalation tests.
No provider, queue, commit, UI, or live execution is authorized.

## Scope / Target / Owner Boundary

Two execution-plane MAO modules, one focused test, the local MAO barrel, and one
worker return. Provider/network, durable storage, workspace/session state,
public-sync, root barrels, commit interlock, and MAO-T5+ remain excluded.

## Decision / Baseline / Proposed Tranche

MAO-T1 through T3 are accepted. Reviewer authority must derive from an isolated
source packet and recomputed evidence, never worker conclusions. Self-approval
fails closed. Dissent, defect class, repair owner, revision count, and terminal
accept/repair/escalate/reject decisions must be deterministic and bounded by the
authority envelope's maximum revision depth.

## Evidence / Verification

The governing roadmap MAO-T4 row, T0 lifecycle/risk/threat sections, T0
`reviewReceipt` schema, T1 authority/task graph, T3 invocation receipt, and T1
read-model dissent projection were read directly at `300c9dfa3`.

## Dependency Release Evidence

| Dependency | Artifact | Commit | Disposition |
|---|---|---|---|
| MAO-T1 | T1 completion review | `01618e9dc` | `REVIEWER_ACCEPTED_BOUNDED` |
| MAO-T2 | T2 completion review | `854bb3a92` | `REVIEWER_ACCEPTED_BOUNDED` |
| MAO-T3 | T3 completion review | `052845fa1` | `REVIEWER_ACCEPTED_BOUNDED` |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MAO-T4 --title "Reviewer Isolation Dissent And Revision Loop" --date 2026-07-11 --base 300c9dfa3 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic worker dispatch plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | all placeholders replaced with source-backed T4 controls |
| checkerReadAheadConfirmation | applicable checker sources read before authoring |
| docOnlyNewFields | isolation/dissent local types are new implementation outputs |
| claimBoundary | dispatch provenance only |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| T4 deliverables | LITERAL_INVARIANT | `docs/roadmaps/CVF_MULTI_AGENT_ORCHESTRATION_RUNTIME_FOUNDATION_ROADMAP_2026-07-11.md` | MAO-T4 | `MAO-T4 - Reviewer Isolation, Dissent, And Revision Loop` | roadmap | ACCEPT |
| isolation and bounded revision semantics | LITERAL_INVARIANT | `docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_CONTRACT.md` | Task / Role / State Lifecycle and Risk-Based Role Model | lifecycle steps 7-8 | T0 contract | ACCEPT |
| review receipt fields | LITERAL_INVARIANT | `docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_SCHEMA.json` | definitions | `reviewReceipt` | Draft 2020-12 schema | ACCEPT |
| revision ceiling | VALUE_SET | `docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_CONTRACT.md` | Cost / Token / Latency Controls | `maxRevisionDepth` | T0 contract | ACCEPT |
| authority/task identities | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.graph.contract.ts` | exports | `MaoTaskGraph`, `MaoTaskDefinition` | MAO-T1 | ACCEPT |
| invocation receipt input | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/delegation.adapter.contract.ts` | exports | `MaoInvocationReceipt` | MAO-T3 | ACCEPT |
| dissent projection | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/read.model.contract.ts` | read model | `openDissent` | MAO-T1 | ACCEPT |

## Current Runtime Freshness Verification

All ACCEPT paths/symbols exist at `300c9dfa3`. Proposed T4 types do not yet
exist and are not represented as current source facts.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`reviewer isolation implementation`, role=`worker`, lifecyclePhase=`implementation`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "reviewer isolation implementation" --role worker --lifecycle-phase implementation --surface-selector "multi-agent orchestration dissent revision" --risk-ceiling HIGH --max-results 20 --json`

Returned defects: NONE_RETURNED

Disclosed defectIds: N/A with reason: NONE_RETURNED.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | ready status; source verification; no-commit route; worker return; public disposition |
| gateRunPurpose | confirmation after source-backed authoring; not first discovery |
| claimBoundary | packet shape/fidelity only |

## Intake Role Routing Decision

Selected route: `MULTI_AGENT_MULTI_ROLE`

rolePattern: `worker-no-commit split`

Intake summary: local reviewer-isolation and revision-policy foundation.

Scope classification: `RUNTIME_FOUNDATION_LOCAL_NO_PROVIDER`

Risk sensitivity: HIGH because self-approval and unbounded repair must fail closed.

Escalation condition: authority conflict, impossible isolation, forbidden path,
provider/live need, unbounded revision, or source contradiction.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | runtime/provider/mcp/readiness claim |
| Chain map route | NOT_APPLICABLE_WITH_REASON |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | paired MAO-T4 packet |
| Disposition | NOT_APPLICABLE_WITH_REASON: internal sources only |
| Claim boundary | no external intake claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Next action: retain in private provenance through MAO closure.

## Machine Closure Package

| Field | Value |
|---|---|
| Baseline state | `DISPATCH_READY` |
| Dependencies | T1-T3 accepted |
| Commit mode | `WORKER_MUST_NOT_COMMIT` |
| Next action | execute paired work order only |

## Acceptance Receipt Assertion Matrix

| Assertion | Required evidence |
|---|---|
| reviewer isolation | packet hash and excluded-context tests |
| no self approval | actor/task negative tests |
| dissent and repair | deterministic ledger/owner tests |
| bounded revision | accept/repair/escalate/reject boundary tests |

## Claim Boundary

This baseline authorizes local deterministic review-policy mechanics only. It
does not prove independent-review quality, provider execution, durable runtime,
closer/commit interlock, public readiness, or production orchestration.
