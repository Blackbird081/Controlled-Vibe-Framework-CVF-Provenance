# CVF GC-018 Baseline - MAO-T3 Provider-Neutral Delegation Adapter

Memory class: governed-baseline

Status: DISPATCH_READY

Date: 2026-07-11

Batch: MAO-T3

dispatchBaseHead: `ecb2679a6`

executionBaseHead: capture actual clean post-dispatch-sync HEAD before editing.

closureBaseHead: N/A with reason: worker and reviewer conversion have not occurred.

## Purpose

Authorize a provider-neutral invocation port, capability/authority contract,
idempotency boundary, diagnostic envelope, and fake/local contract tests. No
real provider or network call is authorized.

## Scope / Target / Owner Boundary

One execution-plane adapter module, one focused test, the local MAO barrel, and
one worker return. Provider configuration, secrets, live proof, queues, UI,
workspace/session state, public-sync, root barrels, and MAO-T4+ are excluded.

## Decision / Baseline / Proposed Tranche

MAO-T1 and MAO-T2 are accepted at `01618e9dc` and `854bb3a92`. The adapter may
accept only admitted role requests, immutable authority, capability declarations,
input-manifest identity, and caller idempotency identity. Fake/local execution
must return deterministic invocation receipts or fail-closed diagnostics.

## Dependency Release Evidence

| Dependency | Artifact | Commit | Disposition |
|---|---|---|---|
| MAO-T1 | `docs/reviews/CVF_MAO_T1_TASK_GRAPH_AND_STATE_CONTRACT_COMPLETION_2026-07-11.md` | `01618e9dc` | `REVIEWER_ACCEPTED_BOUNDED` |
| MAO-T2 | `docs/reviews/CVF_MAO_T2_RISK_BASED_ROLE_RESOLVER_COMPLETION_2026-07-11.md` | `854bb3a92` | `REVIEWER_ACCEPTED_BOUNDED` |

## Evidence / Verification

Direct source reads confirm the T3 roadmap deliverables, T0 port/receipt
contract, accepted T1/T2 inputs, and existing provider-selection owners. The
worker must reproduce these checks and run focused tests plus typecheck.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MAO-T3 --title "Provider-Neutral Delegation Adapter" --date 2026-07-11 --base ecb2679a6 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic worker dispatch plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | all placeholders replaced with source-backed T3 controls |
| checkerReadAheadConfirmation | applicable checkers read before authoring |
| docOnlyNewFields | adapter-local capability and diagnostic types are new outputs |
| claimBoundary | dispatch provenance only |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| T3 deliverables | LITERAL_INVARIANT | `docs/roadmaps/CVF_MULTI_AGENT_ORCHESTRATION_RUNTIME_FOUNDATION_ROADMAP_2026-07-11.md` | MAO-T3 | `MAO-T3 - Provider-Neutral Delegation Adapter` | roadmap | ACCEPT |
| capability and authority port | LITERAL_INVARIANT | `docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_CONTRACT.md` | Provider-Neutral Capability Port | capability declaration and authority envelope | T0 contract | ACCEPT |
| invocation receipt fields | LITERAL_INVARIANT | `docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_SCHEMA.json` | `invocationReceipt` | `invocationReceipt` | Draft 2020-12 schema | ACCEPT |
| authority/hash/task inputs | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.graph.contract.ts` | exports | `MaoTaskGraph`, `verifyAuthorityEnvelope` | MAO-T1 | ACCEPT |
| admission receipt | EXISTS | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/mao/role.resolver.contract.ts` | exports | `MaoRoleResolutionReceipt` | MAO-T2 | ACCEPT |
| provider policy owner | EXISTS | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/provider.router.contract.ts` | class method | `route` | `ProviderRouterContract` | ACCEPT |
| model-gateway provider registry | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | exported class | `ProviderRegistry` | model gateway | ACCEPT |
| capability registry owner | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | exported constant | `PROVIDER_CAPABILITY_REGISTRY` | model gateway | ACCEPT |

## Current Runtime Freshness Verification

Verified at `ecb2679a6`; all ACCEPT files and symbols exist. Proposed adapter
symbols are new outputs and are not claimed as current runtime facts.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`adapter contract implementation`, role=`worker`, lifecyclePhase=`implementation`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "adapter contract implementation" --role worker --lifecycle-phase implementation --surface-selector "multi-agent orchestration provider-neutral delegation adapter" --risk-ceiling HIGH --max-results 20 --json`

Returned defects: NONE_RETURNED

Disclosed defectIds: N/A with reason: NONE_RETURNED.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | ready status; no-commit route; source verification; worker return; public disposition |
| gateRunPurpose | confirmation and evidence after source-backed authoring; not first discovery |
| claimBoundary | packet shape and fidelity only |

## Intake Role Routing Decision

Selected route: `MULTI_AGENT_MULTI_ROLE`

rolePattern: `worker-no-commit split`

Intake summary: local adapter contract with independent review.

Scope classification: `RUNTIME_FOUNDATION_FAKE_LOCAL_NO_LIVE_PROVIDER`

Risk sensitivity: HIGH because authority/idempotency failures must fail closed.

Escalation condition: provider/live requirement, authority widening, ambiguous
side effect, forbidden path, or source contradiction.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | runtime/provider/mcp/readiness claim |
| Chain map route | NOT_APPLICABLE_WITH_REASON |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | paired MAO-T3 packet |
| Disposition | NOT_APPLICABLE_WITH_REASON: internal CVF sources only |
| Claim boundary | no external intake claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Next action: retain in provenance through MAO closure.

## Machine Closure Package

| Field | Value |
|---|---|
| Baseline state | `DISPATCH_READY` |
| Dependencies | T1/T2 accepted |
| Commit mode | `WORKER_MUST_NOT_COMMIT` |
| Next action | execute paired work order only |

## Acceptance Receipt Assertion Matrix

| Assertion | Required evidence |
|---|---|
| authority and admission binding | positive and tamper-negative tests |
| duplicate protection | same key returns existing receipt; conflicts fail closed |
| diagnostic envelope | classified fake/local failure tests |
| provider neutrality | no named-provider schema branch or network call |

## Claim Boundary

This baseline authorizes fake/local adapter contract behavior only. It does not
prove provider support, network execution, retry lifecycle, queueing, UI,
automatic commit, public readiness, or production orchestration.
