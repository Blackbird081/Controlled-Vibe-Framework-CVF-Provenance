# CVF GC-018 Baseline - NIS T1G Receiver Manual Baseline

Memory class: governed-dispatch-baseline

Status: CLOSED_PASS_BOUNDED

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
| literalTokensReviewed | CLOSED_PASS_BOUNDED; acceptance-ledger-json; exact four outputs; PENDING_REVIEWER_EXECUTION; structured envelope; exact9 admission |
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

## Reviewer Closure Disposition

Local disposition: CLOSED_PASS_BOUNDED_PREPARATION_MODIFIED_REVIEW_ONLY; LD-1..LD-6 in docs/reviews/CVF_NIS_T1G_RECEIVER_MANUAL_BASELINE_COMPLETION_2026-10-05.md. Independent preparation PASS, no arm executed.
independentProbeDisposition: PASS_INDEPENDENT_PROBE
implementationWorkerActor: nis-t1g-worker
probeExecutorActor: nis-t1g-local-reviewer
workerInvocationId: nis-t1g-worker-20261005
probeInvocationId: nis-t1g-local-independent-20261005
workerOracleSha256: f3cc5972124b5c0879525061812a2173daa2a687ecbc21d8e0b6814113cf88da
probeOracleSha256: 23436ca419ea1f490f29b50cc418737e81d597e8e9c7843ff3a55b15a240438d
workerEvidenceRef: docs/reviews/evidence/cvf-nis-t1g-manual-baseline-casepack-2026-10-05.json
probeEvidenceRef: docs/reviews/evidence/cvf-nis-t1g-local-independent-review-2026-10-05.json
probeCommandOrMethod: python -B .cvf/runtime/nis-t1g-local-review-20261005/probe.py; independent source-byte and preparation protocol assertions, not BC-V1
probeObservedResult:149 assertions PASS and6 negative admission controls;13 source pins,3 exact attachments,11 view hashes; no manual/helper execution
oracleSeparationBasis: distinct Local actor/invocation and assertion source; worker casepack is input, not Local oracle implementation


## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | docs/work_orders/CVF_AGENT_WORK_ORDER_NIS_T1G_RECEIVER_MANUAL_BASELINE_2026-10-05.md | CLOSED_PASS_BOUNDED preparation only | PASS |
| Completion or reviewer artifact | docs/reviews/CVF_NIS_T1G_RECEIVER_MANUAL_BASELINE_COMPLETION_2026-10-05.md | LD-1..LD-6 control original proposal | PASS |
| Roadmap state | docs/roadmaps/CVF_GCLH_MACHINE_FIRST_REVIEW_PREFLIGHT_ROADMAP_2026-09-01.md | current MFRP applied; NCR P11 parked; successor execution excluded | PASS |
| Registry JSON | docs/reviews/evidence/cvf-nis-t1g-local-independent-review-2026-10-05.json | independent preparation proof and original hashes | PASS |
| Registry Markdown | docs/reviews/CVF_NIS_T1G_RECEIVER_MANUAL_BASELINE_COMPLETION_2026-10-05.md | bounded review-only disposition | PASS |
| External evidence digest | docs/reviews/evidence/cvf-nis-t1g-local-independent-review-2026-10-05.json | SHA256 23436ca419ea1f490f29b50cc418737e81d597e8e9c7843ff3a55b15a240438d | PASS |
| System loop interlock | docs/reviews/evidence/cvf-nis-t1g-reviewer-inputs-review-only-2026-10-05.json | neutral inputs prepared; no runtime/catalog promotion | PASS |
| Session continuity | CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json | closed preparation, manual dispatch remains separate, parked lanes retained | PASS |


## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| REQ-1 receiver | concrete source-bound jobs or honest pairing HOLD | exact report bytes and synthetic LG3; job A review-only, accepted-file gap retained | PASS |
| REQ-2 preparation | eleven cases and frozen protocol | NOT_EXECUTED; Local package/cost/scoring/scope corrections control | PASS |
| REQ-3 return | exact4 outputs, gates, no forbidden effects | originals retained, saved87/87 preimpl and final worker fast consumed | PASS |
| Independent probe | distinct actor/oracle |149 assertions and6 admission controls | PASS |
| Reviewer blinding | no placement key in inputs | neutral Local package; seed worker and Local B2, later actor unassigned | PASS |
| Authority | no automatic manual/helper/build | BC-V1 and35 prior cases NOT_EXECUTED; separate later order required | PASS |


## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: Local T1G closure authority/next-move only; worker cannot write protected paths.
Protected paths:
- `AGENT_HANDOFF_V63_2026-09-18.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
Operator authorization: delegated Local orchestrator/reviewer/full handling and requested T1G disposition; no candidate/helper/runtime successor.
Rollback boundary: exact11 closure paths, preserve original4 worker and parked lanes.


## Mixed Protected-Path Atomicity Authorization

Disposition: AUTHORIZED_EXACT_MANIFEST
Atomicity reason: paired closure hashes, independent proof, neutral reviewer inputs and six continuity owners bind one disposition; dedicated material SHA follows.
Rollback boundary: exact11 Local closure paths only.
Exact changed manifest: `docs/baselines/CVF_GC018_NIS_T1G_RECEIVER_MANUAL_BASELINE_2026-10-05.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NIS_T1G_RECEIVER_MANUAL_BASELINE_2026-10-05.md`; `docs/reviews/CVF_NIS_T1G_RECEIVER_MANUAL_BASELINE_COMPLETION_2026-10-05.md`; `docs/reviews/evidence/cvf-nis-t1g-local-independent-review-2026-10-05.json`; `docs/reviews/evidence/cvf-nis-t1g-reviewer-inputs-review-only-2026-10-05.json`; `AGENT_HANDOFF_V63_2026-09-18.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/nextAllowedMove.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`.
