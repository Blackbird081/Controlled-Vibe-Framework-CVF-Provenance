# CVF GC-018 Baseline - CSCC-R1-T2A Route Selection And Alibaba Provider Parity Reconciliation

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: CSCC-R1-T2A

Dispatch base head: 3b5ea3cca

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator; reviewer owner: orchestrator/reviewer; worker target: delegated documentation/source-reconciliation worker.

## Purpose

Authorize one narrow source-only tranche that resolves the T2 route-build
selection conflict and determines whether Alibaba can be the first truthful
canonical Gateway provider lane without creating dual provider ownership.

## Decision / Baseline / Proposed Tranche

T2 closed blocked at material commit `2ffe5a803` with a tested but dormant
canonical port. T2A must choose one exact migration posture, prove current
Alibaba protocol/configuration compatibility from source, and return the
smallest owner-correct successor implementation manifest. It does not change
runtime source or consume the operator's Alibaba live-run grant.

## Authorized Scope

- interpret the frozen T1 per-route-build exclusivity rule;
- compare route-wide cutover, Alibaba-only fail-closed canonical build, and
  explicitly amended mixed-provider transition options;
- reconcile Alibaba Web execution behavior with the Gateway generic
  OpenAI-compatible adapter, destination policy, capability registry,
  credential boundary, routing, health, quota and receipt owners;
- specify deterministic zero-call proof and one later bounded Alibaba live
  proof; and
- create an assessment and no-commit worker return only.

## Forbidden Scope

No source, contract, route, adapter, test, package, session, roadmap, registry,
provider, live, credential-value, public, MAO, GC-010, P2, P4 or canary write or
execution is authorized. No API key may be printed, read into output, copied,
validated, or consumed during T2A.

## Operator Alibaba Live Authorization Reservation

operatorAlibabaLiveGrant: RESERVED_FOR_POST_T2A_ACCEPTED_IMPLEMENTATION

authorizedProvider: alibaba

authorizedFutureLiveInvocationCeiling: 1

currentTrancheLiveInvocationCeiling: 0

rerunRule: any failed, partial, timed-out or ambiguous future attempt requires
a secret-safe diagnostic and fresh reviewer authorization before another
provider call.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| T2 blocked closure | `docs/reviews/CVF_CSCC_R1_T2_CANONICAL_WEB_GATEWAY_COMPOSITION_COMPLETION_2026-09-03.md`, material `2ffe5a803` | partial foundation retained; T2A source reconciliation released | ACCEPT |
| T1 selection contract | `docs/reference/CVF_CANONICAL_EXECUTION_PORT_INTERFACE_CONTRACT_2026-09-03.md` | exact per-route-build language remains authoritative until deliberately amended | ACCEPT |
| operator live permission | current operator instruction, 2026-09-03 | reserve one Alibaba live call for a later accepted implementation proof | ACCEPT_BOUNDED_FUTURE_ONLY |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CSCC-R1-T2A --title "Route Selection And Alibaba Provider Parity Reconciliation" --date 2026-09-03 --base 3b5ea3cca --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic worker plus no-commit and provider/live boundary stubs |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with accepted T2 authority, exact source-only scope, Alibaba option matrix and reserved live ceiling |
| checkerReadAheadConfirmation | dispatch, prompt, review-cost, SCEC, trace, worker-return, public and live-boundary owners |
| docOnlyNewFields | `operatorAlibabaLiveGrant`; `authorizedFutureLiveInvocationCeiling`; `currentTrancheLiveInvocationCeiling` |
| claimBoundary | dispatch provenance only; no runtime or provider proof |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Returned defects: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020,
ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044, ADIF-0045,
ADIF-0051, ADIF-0052, ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024,
ADIF-0031, ADIF-0039, ADIF-0043, ADIF-0049, ADIF-0006.

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --json --max-results 50` |
| Returned defect count | 22 |
| Disclosed defectIds | all IDs listed above |
| Dispatch impact | exact source claims, owner-safe provider analysis, zero-call scope and no-commit evidence |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | dispatch status, SCEC fields, no-commit return, trace labels, live authority and public disposition |
| gateRunPurpose | confirmation after current-source reconciliation |
| claimBoundary | structural conformance does not select a route design or prove Alibaba compatibility |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| T2A authoring released | accepted closure | `docs/reviews/CVF_CSCC_R1_T2_CANONICAL_WEB_GATEWAY_COMPOSITION_COMPLETION_2026-09-03.md` | Decision / Recommendation / Disposition | `successorAuthoringReleased` | T2 reviewer | ACCEPT |
| selection is per route build | frozen contract | `docs/reference/CVF_CANONICAL_EXECUTION_PORT_INTERFACE_CONTRACT_2026-09-03.md` | Compatibility / Rollback Matrix | `Exclusive adapter selection` | T1 contract | ACCEPT |
| Alibaba direct path is OpenAI-compatible but behavior-specialized | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/providers.ts` | `executeAlibaba` | `executeAlibaba` | Web AI provider owner | ACCEPT |
| generic Gateway adapter is parameterized | runtime source | `EXTENSIONS/CVF_MODEL_GATEWAY/src/openai-compatible-execute-adapter.ts` | adapter factories | `createCredentialBoundOpenAiCompatibleExecuteAdapter` | Model Gateway | ACCEPT |
| destination policy recognizes Alibaba | runtime source | `EXTENSIONS/CVF_MODEL_GATEWAY/src/adapter-destination-policy.ts` | Gateway-derived endpoints | `GATEWAY_DERIVED_ENDPOINTS` | Model Gateway | ACCEPT |
| Alibaba capability entries exist | runtime source | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | capability registry | `PROVIDER_CAPABILITY_REGISTRY` | Model Gateway | ACCEPT |
| current API-key alias owner exists | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/alibaba-env.ts` | exported resolver | `resolveAlibabaApiKey` | Web configuration owner | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| four T2A target paths | all absent before authoring | ACCEPT_NO_COLLISION |
| active Web route invokes canonical executor | T2 completion plus current route: absent | ACCEPT_BLOCKER_RETAINED |
| provider/live calls in T2A | ceiling zero | FORBIDDEN |

## Current Runtime Freshness Verification

| Field | Value |
| --- | --- |
| runtimeClaimPresent | NO |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | STATIC_RECOMPUTE_REQUIRED |
| reason | T2A selects contracts and owners; it does not claim the route works live |
| requiredFutureAction | after accepted implementation and deterministic rejection proof, use at most one authorized Alibaba call through the named canonical path |

## Evidence / Verification

- current-source symbol and owner recomputation;
- exact T1 selection-language comparison;
- three-option migration matrix and Alibaba field-parity matrix;
- pre-dispatch and pre-commit governance gates;
- exact two-path worker manifest, unchanged worker HEAD and zero calls.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private source-reconciliation dispatch; no public-sync authority.

## Claim Boundary

This baseline authorizes a documentation/source decision only. The reserved
Alibaba permission is not current worker provider authority and proves no
route, Gateway, receipt, deployment or production behavior.
