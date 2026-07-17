# CVF GC-018 Baseline - MAO-OA-T6A Harder Candidate Direct Baseline Calibration

Memory class: governed-baseline

Status: REVIEWER_ACCEPTED_IMPLEMENTATION_LIVE_RESULT_NOT_ACCEPTED

Batch ID: MAO-OA-T6A

Base head: `95fb21377`

Commit mode: WORKER_MUST_NOT_COMMIT

## Authorization / Decision

The operator's standing instruction to continue through the roadmap authorizes
one bounded live calibration call. T6B is not authorized by this baseline; it
releases only after independent review accepts a direct score of 80/100 or
lower or one predeclared material defect.

## Purpose

Establish an accepted direct-provider baseline for a materially harder
agent-project planning task before spending calls on a MAO comparison.

## Baseline Decision

Proceed with one Alibaba/DashScope-compatible direct call through the existing
Model Gateway live harness. Use the fixed task, schema, rubric, defect rules,
model lane, and secret-safe evidence contract in the paired work order. Do not
retry and do not run a MAO lane in T6A.

## Scope / Target / Owner Boundary

The worker may add one pure candidate/rubric contract, focused fake-fetch tests,
one local live runner, one evidence JSON, one GC-051 entry and generated
aggregate, and one worker return. The existing Model Gateway harness owns the
provider call. No new provider, credential, queue, UI, CLI/MCP, session state,
public-sync, commit, push, or production owner is authorized.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
|---|---|---|
| accepted T5 | `3e259039a`; `docs/reviews/CVF_MAO_OA_T5_COMPLETION_REVIEW_2026-07-17.md` | ACCEPT |
| harder-candidate rule | concrete reopen conditions in `docs/roadmaps/CVF_MAO_LIVE_PROVIDER_ADAPTER_VALUE_PILOT_ROADMAP_2026-07-12.md` | ACCEPT |
| explicit live authority | operator standing continuation instruction | ACCEPT_BOUNDED_ONE_CALL |
| live owner | current Model Gateway `runLiveProof` source | ACCEPT |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldTool | `governance/compat/build_dispatch_packet_scaffold.py` |
| packetKind | `runtime-provider-live` |
| scaffoldBase | `95fb21377` |
| scaffoldDisposition | completed against current sources and guards |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind runtime-provider-live --batch-id MAO-OA-T6A --title "Harder Candidate Direct Baseline Calibration" --date 2026-07-17 --base 95fb21377 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "MAO-OA-T5 accepted closure 3e259039a" --stdout --include-worker-return-skeleton` |
| generatedProfile | `runtime-provider-live` |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | source verification, exact scope, rubric, release rule, and evidence controls |
| checkerReadAheadConfirmation | applicable checker sources were read before final packet text |
| docOnlyNewFields | T6B release tokens are declared only in the paired work order |
| claimBoundary | scaffold provenance does not prove execution or live results |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`MAO harder candidate live calibration`, role=`worker`, lifecyclePhase=`pre-implementation`

Returned defects: NONE_RETURNED

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| live call owner | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/p4b-b-live-proof-harness.ts` | exported function around line 188 | `runLiveProof` | Model Gateway live proof harness | ACCEPT |
| injectable fetch | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/p4b-b-live-proof-harness.ts` | exported type around line 51 | `LiveProofFetch` | Model Gateway live proof harness | ACCEPT |
| live options | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/p4b-b-live-proof-harness.ts` | exported interface at line 64 | `LiveProofHarnessOptions` | Model Gateway live proof harness | ACCEPT |
| credential reference | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/credential-boundary.ts` | exported interface | `CredentialReference` | Model Gateway credential boundary | ACCEPT |
| key bootstrap pattern | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/scripts/run-mao-live-provider-value-pilot.ts` | environment constant and loader around lines 40-42 and 102 | `ENV_LOCAL` | prior MAO live runner | ACCEPT |
| diagnostic rule | EXISTS | `docs/reference/archive/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md` | required diagnostic fields | `Live Run Diagnostic` | governed diagnostic standard | ACCEPT |

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | YES |
| runtimeMutationAuthorized | YES_BOUNDED_NEW_LOCAL_RUNNER_AND_CONTRACT |
| freshnessVerificationMode | CURRENT_SOURCE_PLUS_ONE_FRESH_LIVE_CALL |
| verifiedBase | `95fb21377` |
| priorResultUse | context only; prior receipts cannot satisfy T6A |

## Runtime Expansion Control Block

| Field | Value |
|---|---|
| expansionClass | bounded local runner and pure scorer |
| existingOwnerReuse | Model Gateway `runLiveProof` |
| sideEffectCeiling | one provider call and one evidence file |
| retryCeiling | zero retries |
| forbiddenOwners | provider routing, credential storage, MAO execution, queue, UI |

## Allowed Scope

Exactly the seven worker paths listed in the paired work order.

## Forbidden Scope

All other paths; commit; push; second call; retry; MAO comparison; raw secret
or raw provider payload persistence; production/public claims.

## Evidence / Verification

Focused fake-fetch tests, TypeScript check, exact one-call ledger, deterministic
rubric result, secret scan, GC-051 checks, worker-return fast gate, and exact
diff/status evidence are required.

## Machine Closure Package

| Field | Value |
|---|---|
| closeableState | COMPLETE_PENDING_REVIEW |
| requiredDecision | reviewer independently recomputes score, defects, call count, secret safety, and T6B release |
| generatedAggregateDisposition | GC-051 source entry plus generated aggregate required |
| sessionStateDisposition | N/A with reason: worker may not mutate protected continuity |
| commitDisposition | N/A with reason: WORKER_MUST_NOT_COMMIT |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | source columns; ADIF query; handoff route; live diagnostic; exact manifest; public disposition |
| gateRunPurpose | confirm and evidence one-call authority before worker execution |
| claimBoundary | dispatch conformance does not prove a call, score, defect, or value gain |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance calibration; public export is not authorized.

## Claim Boundary

This packet authorizes one direct baseline call only. It does not claim a call
succeeded, the candidate is hard enough, MAO adds value, or production readiness.
