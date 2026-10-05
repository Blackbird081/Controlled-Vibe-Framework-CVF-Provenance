# CVF GC-018 Baseline - NIS T1G Receiver Manual Baseline

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: CVF-NIS-T1G
providerExecutionAuthority: FORBIDDEN
Date: 2026-10-05

Dispatch base head: 7747d206264bbc24c86b31ef042485db8f81b147

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: Operator; delegated Local dispatcher

Reviewer owner: Local reviewer/closer

Worker target: INTERNAL_AGENT documentary preparation worker

## Purpose

Prepare a usable documentary receiver and frozen manual-baseline materials for BC-V1, following T1F Local C-1..C-7. Give the existing downstream technical reviewer/builder a source-bound requirement/design/task/validation readout, two concrete job examples and a reproducible comparison protocol. This slice prepares the experiment; it does not execute either arm or implement a helper.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-NIS-T1G --title "NIS T1G Receiver Manual Baseline" --date 2026-10-05 --base 7747d206264bbc24c86b31ef042485db8f81b147 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Concrete documentary receiver, two frozen source-bound jobs,11 cases and baseline protocol; exact4 outputs/exact9 admission |
| checkerReadAheadConfirmation | governance/compat/check_work_order_dispatch_quality.py; governance/compat/check_work_order_dispatch_quality_source.py; governance/compat/check_work_order_dispatch_quality_artifacts.py; governance/compat/check_dispatch_scaffold_provenance.py; governance/compat/check_gate_to_role_closeability.py; governance/compat/check_governed_artifact_checker_read_ahead.py; governance/compat/check_task_governance_route.py; governance/compat/check_baseline_update_compat.py; governance/compat/check_agent_operation_trace.py; governance/compat/check_work_order_acceptance_ledger.py; governance/compat/check_independent_review_probe_admission.py; governance/compat/check_absorption_blindspot_control_presence.py; governance/compat/check_external_knowledge_intake_routing.py; governance/compat/check_high_risk_local_transaction_proof.py; governance/compat/check_adif_defect_registry_disclosure.py; governance/compat/check_agent_packet_authority_and_encoding.py; governance/compat/check_markdown_structural_completeness.py; governance/compat/check_dispatch_prompt_envelope.py |
| docOnlyNewFields | Task-specific documentary experiment fields only; no adopted product schema |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |


## ADIF Defect Registry Disclosure

Resolver query: taskClass=`documentation`, role=`dispatcher`, lifecyclePhase=`dispatch`.

Command: `python -B governance/compat/run_adif_defect_resolver.py --task-class documentation --role dispatcher --lifecycle-phase dispatch`.
Returned defects: NONE_RETURNED. Actual resolver executed 2026-10-05, candidates=0, returned=0, truncated=false.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | governance/compat/check_work_order_dispatch_quality.py; governance/compat/check_work_order_dispatch_quality_source.py; governance/compat/check_work_order_dispatch_quality_artifacts.py; governance/compat/check_dispatch_scaffold_provenance.py; governance/compat/check_gate_to_role_closeability.py; governance/compat/check_governed_artifact_checker_read_ahead.py; governance/compat/check_task_governance_route.py; governance/compat/check_baseline_update_compat.py; governance/compat/check_agent_operation_trace.py; governance/compat/check_work_order_acceptance_ledger.py; governance/compat/check_independent_review_probe_admission.py; governance/compat/check_absorption_blindspot_control_presence.py; governance/compat/check_external_knowledge_intake_routing.py; governance/compat/check_high_risk_local_transaction_proof.py; governance/compat/check_adif_defect_registry_disclosure.py; governance/compat/check_agent_packet_authority_and_encoding.py; governance/compat/check_markdown_structural_completeness.py; governance/compat/check_dispatch_prompt_envelope.py |
| literalTokensReviewed | DISPATCH_READY; acceptance-ledger-json; exact four outputs; PENDING_REVIEWER_EXECUTION; structured envelope; exact9 admission |
| gateRunPurpose | confirmation/evidence of documentary dispatch shapes, not first discovery or experimental result |
| claimBoundary | BC-V1 and product cases NOT_EXECUTED |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Receiver/baseline controlling input | CURRENT_SOURCE | docs/reviews/CVF_NIS_T1F_BUILD_READY_BRIDGE_CONTRACT_COMPLETION_2026-10-05.md | Minimum Next Delta | Minimum Next Delta | Local completion / existing packet owner / synthetic evidence | ACCEPT |
| Receiver/baseline controlling input | CURRENT_SOURCE | docs/reviews/CVF_NIS_T1F_BUILD_READY_BRIDGE_CONTRACT_2026-10-05.md | BC-V1 | BC-V1 | Local completion / existing packet owner / synthetic evidence | ACCEPT |
| Receiver/baseline controlling input | CURRENT_SOURCE | docs/reviews/evidence/cvf-nis-t1f-build-ready-acceptance-plan-2026-10-05.json | valueFalsifier | valueFalsifier | Local completion / existing packet owner / synthetic evidence | ACCEPT |
| Receiver/baseline controlling input | CURRENT_SOURCE | docs/reviews/evidence/cvf-nis-t1f-local-independent-review-2026-10-05.json | claimBoundary | claimBoundary | Local completion / existing packet owner / synthetic evidence | ACCEPT |
| Receiver/baseline controlling input | CURRENT_SOURCE | docs/reviews/evidence/cvf-nis-t1e-frozen-legacy-2026-10-05.json | controls | controls | Local completion / existing packet owner / synthetic evidence | ACCEPT |
| Receiver/baseline controlling input | CURRENT_SOURCE | docs/reviews/evidence/cvf-nis-t1e-local-independent-review-2026-10-05.json | localOldProducerCapture | localOldProducerCapture | Local completion / existing packet owner / synthetic evidence | ACCEPT |
| Receiver/baseline controlling input | CURRENT_SOURCE | docs/reviews/evidence/cvf-nis-t1d-acceptance-plan-2026-10-05.json | fixtures | fixtures | Local completion / existing packet owner / synthetic evidence | ACCEPT |
| Receiver/baseline controlling input | CURRENT_SOURCE | docs/reviews/evidence/cvf-nis-t1c-scenario-2026-10-05.json | stageInputs | stageInputs | Local completion / existing packet owner / synthetic evidence | ACCEPT |
| Receiver/baseline controlling input | CURRENT_SOURCE | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/intent-spec-review.ts | decisionNeedsReview | decisionNeedsReview | Local completion / existing packet owner / synthetic evidence | ACCEPT |
| Receiver/baseline controlling input | CURRENT_SOURCE | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/intent-spec-open-items.ts | ReviewOpenItem | ReviewOpenItem | Local completion / existing packet owner / synthetic evidence | ACCEPT |
| Receiver/baseline controlling input | CURRENT_SOURCE | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/intent-spec-confirmation.ts | createSpecConfirmationCandidate | createSpecConfirmationCandidate | Local completion / existing packet owner / synthetic evidence | ACCEPT |
| Receiver/baseline controlling input | CURRENT_SOURCE | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/intent-spec-acceptance.ts | prepareIntentSpecAcceptance | prepareIntentSpecAcceptance | Local completion / existing packet owner / synthetic evidence | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| Exact new paths | three admission paths and four worker outputs absent before authoring | ACCEPT |
| Existing owner | source-bound NIS packet and T1F Local receiving route retained; no separate product module | ACCEPT |

## Claim Boundary

rawMemoryReleased=false. Documentary receiver and experiment preparation only. Frozen synthetic accepted-file evidence is historical, not a current real record or actor verification. No product/source/test/registry/checker/continuity edits by worker, helper implementation, baseline performance execution, runtime/provider/upstream/install/network/store/UAC/browser/BUILD/public/deploy or parked-lane reopening. Existing35 cases remain NOT_EXECUTED; BC-V1 NOT_EXECUTED; cost UNKNOWN; no build-ready certificate.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Private evaluation packet; no public export or push authorized.


## Scope / Applies To

Documentary receiver and frozen manual-baseline preparation, exact four outputs in docs/work_orders/CVF_AGENT_WORK_ORDER_NIS_T1G_RECEIVER_MANUAL_BASELINE_2026-10-05.md. Input docs/reviews/evidence/cvf-nis-t1g-dispatch-inputs-2026-10-05.json. No experiment execution or helper implementation.

## Decision / Authorization

Operator next under delegated Local authority after T1F Local MODIFY selects Minimum Next Delta. Final technical decision owner Local; no source/helper/runtime grant.

## Verification

Bound pre-dispatch and worker-owned pre-implementation, full worker fast gate, source-byte/case/protocol checks, independent Local preparation review. BC-V1 and product cases NOT_EXECUTED.

## External Repository Absorption Entry Control

NOT_APPLICABLE_WITH_REASON - internal governed T1F disposition and existing native/frozen fixture inputs only; upstream source reassessment and acquisition excluded.

## Mandatory Blind-Spot Control Block

Blind-spot verdict: NOT_APPLICABLE_WITH_REASON - named internal documentary preparation; no corpus-wide novelty, external absorption or value closure claim.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - named source/fixture pins, not a completed corpus scan. Worker accounts for actually used locators and exclusions; no all-repository-read claim.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md |
| Input type | internal governed input (no external intake) |
| Internal source | docs/reviews/CVF_NIS_T1F_BUILD_READY_BRIDGE_CONTRACT_COMPLETION_2026-10-05.md |
| Chain map route | accepted Local contract disposition -> documentary receiver and baseline preparation |
| Matching local-view guard | governance/compat/check_external_knowledge_intake_routing.py |
| Owner surface | existing NIS packet receiver / Local technical reviewer |
| Disposition | ADAPT_EXISTING; helper and experiment execution deferred |
| Claim boundary | historic upstream-derived proposal is input, no new acquisition or runtime grant |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| clarify/checklist source candidates | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/intent-spec-review.ts and intent-spec-acceptance.ts | ENRICH_EXISTING | T1C explicit subitem/effective-rule gap; exact upstream fit still unreviewed | Selected source comparison, no conversion |
| plan/tasks/analyze source candidates | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/SpecExport.tsx | ENRICH_EXISTING | Existing future design/build directions; structured artifacts/dependencies not yet accepted | Worker independently dispositions pattern/runtime/value; no automatic S2 |


## External/Local Coordination Binding

```json
{
  "contractId": "cvf.external-local-absorption-coordination@1",
  "invariants": {
    "externalRole": "ADVISORY_RESEARCH_AND_PATTERN_MAPPING",
    "externalContext": "PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ",
    "localRole": "SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION",
    "finalDecisionOwner": "LOCAL",
    "localCoverageBasis": "SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST",
    "externalEvidenceAuthority": "INPUT_NOT_PRIVATE_CVF_PROOF"
  },
  "contractSha256": "92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c",
  "parentArtifact": null
}
```


## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON - no migration or external absorption closure.
