# CVF Agent Work Order - NIS T1H Review Only Manual Arm

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

Batch ID: CVF-NIS-T1H
providerExecutionAuthority: FORBIDDEN
Date: 2026-10-05

Dispatch base head: b94f893d077c89ac5d8deb282da665b754a733bd

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker

Reviewer/closer: Local scorer/reviewer/closer

Worker return path: `docs/reviews/CVF_NIS_T1H_REVIEW_ONLY_MANUAL_ARM_WORKER_RETURN_2026-10-05.md`

## Dispatch Prompt Envelope

```text
Role: fresh INTERNAL_AGENT manual reviewer; Local separate scorer/reviewer/closer.
Canonical packet: docs/work_orders/CVF_AGENT_WORK_ORDER_NIS_T1H_REVIEW_ONLY_MANUAL_ARM_2026-10-05.md; baseline docs/baselines/CVF_GC018_NIS_T1H_REVIEW_ONLY_MANUAL_ARM_2026-10-05.md; inputs docs/reviews/evidence/cvf-nis-t1h-dispatch-inputs-2026-10-05.json.
Commit mode: WORKER_MUST_NOT_COMMIT; sharedWorktreeCoordinationMode: SEPARATE_GIT_WORKTREE.
executionBaseHead: WORKER_MUST_CAPTURE_AT_START; redispatch base b94f893d077c89ac5d8deb282da665b754a733bd is not later worker HEAD.
Current-time notes: redispatch sequence2 / REWORK1 after placement-contaminated blocked sequence1; first retained primary attempt still pending.
Do-not-misread notes: use a fresh context with no placement knowledge; prior experiment documents/key are excluded reads. Do not create a relay file.
Required first actions: progressive startup through current pair only; declare exposure before views, verify hashes and run own pre-implementation.
Return contract: exact3 artifacts with raw responses and real exposure/time records; COMPLETE_PENDING_REVIEW or honest BLOCKED_WITH_REASON; no self-score.
```

## Purpose

Run one manual structural-review attempt on the neutral historical synthetic inputs. Capture unchanged per-case responses and actual exposure/time evidence. A fresh reviewer who has not read placement information is required. Local scores after return; this worker neither scores itself nor selects a helper.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-NIS-T1H --title "NIS T1H Review Only Manual Arm" --date 2026-10-05 --base 3a30c39fc27cd2a0c2891063af145b76abef7a7f --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Fresh reviewer3-output one primary attempt; neutral input only, exact9 Local admission |
| checkerReadAheadConfirmation | governance/compat/check_work_order_dispatch_quality.py; governance/compat/check_work_order_dispatch_quality_source.py; governance/compat/check_work_order_dispatch_quality_artifacts.py; governance/compat/check_dispatch_scaffold_provenance.py; governance/compat/check_gate_to_role_closeability.py; governance/compat/check_governed_artifact_checker_read_ahead.py; governance/compat/check_task_governance_route.py; governance/compat/check_baseline_update_compat.py; governance/compat/check_agent_operation_trace.py; governance/compat/check_work_order_acceptance_ledger.py; governance/compat/check_independent_review_probe_admission.py; governance/compat/check_absorption_blindspot_control_presence.py; governance/compat/check_external_knowledge_intake_routing.py; governance/compat/check_high_risk_local_transaction_proof.py; governance/compat/check_adif_defect_registry_disclosure.py; governance/compat/check_agent_packet_authority_and_encoding.py; governance/compat/check_markdown_structural_completeness.py; governance/compat/check_dispatch_prompt_envelope.py |
| docOnlyNewFields | Task-specific raw response/exposure/time fields only, no product schema |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |


## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: REWORK
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: CVF-NIS-T1H
reviewRoundCount: 1
priorFindingSetDigest: 1f3bb7c4ffe31b935bd8a8086e20abc5c37ed0b4de97e51937975f1ce0a45f47
dependencyAuditDisposition: COMPLETE_BEFORE_FIRST_REPAIR
reworkFindingDisposition: CONSOLIDATED_ALL_DEPENDENT_FINDINGS
newIndependentCriticalEvidence: NONE
regressionGuardDisposition: REQUIRED_AND_PLANNED_FOR_EACH_TARGETED_DEFECT
cumulativeExternalInvocationCount: 0
externalInvocationCeiling: 0
usageAvailability: NOT_APPLICABLE_INTERNAL_AGENT
quotaAdmissionDisposition: NOT_APPLICABLE_INTERNAL_AGENT
nextDispatchDisposition: ONE_CONSOLIDATED_REWORK
rootCauseClusterId: NIS-T1H-PLACEMENT-AWARE-WORKER
reworkGeneration: 1
consolidatedDefectClassSweep: COMPLETE_BEFORE_REWORK_DISPATCH
successorTrancheOpened: NO
implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY
preExecutionReviewAdmission: NOT_REQUIRED_BEFORE_EXECUTION
preExecutionReviewTrigger: NONE
nextRoutineReviewBoundary: WORKER_RETURN
reviewerWorkBoundary: EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION
reviewerLocalRepairBoundary: NEW_EVIDENCE_REQUIRED
reviewerLocalRepairBasis: Local and the prior context are placement-aware; no document edit can erase their exposure. A different context must provide the first retained primary response/time evidence under docs/reviews/CVF_NIS_T1H_DISPATCH_EXPOSURE_INTAKE_2026-10-05.md.

## Semantic Convergence Outcome

Standard: docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md

```json
{
  "schemaVersion": "cvf.semanticConvergenceControl.v1",
  "problemKey": "cvf-nis-t1h-problem",
  "chainMode": "SUCCESSOR",
  "chainOrdinal": 1,
  "predecessor": {
    "path": "docs/reviews/CVF_NIS_T1H_DISPATCH_EXPOSURE_INTAKE_2026-10-05.md",
    "sha256": "7f7993ad45f7d628b83ab0ee1e4830756f8e40e70c4623fe437ccd4dee625ca8"
  },
  "blockerDelta": {
    "prior": [
      "PLACEMENT_CONTAMINATION"
    ],
    "resolved": [],
    "retained": [
      "PLACEMENT_CONTAMINATION"
    ],
    "new": [],
    "reopened": [],
    "current": [
      "PLACEMENT_CONTAMINATION"
    ]
  },
  "resolutionEvidence": {},
  "counters": {
    "partialReadyClosures": 0,
    "reviewerScopeExpansions": 0,
    "sameClaimCorrections": 0,
    "nonDecreasingBlockerTransitions": 1
  },
  "claims": [],
  "requiredDisposition": "CONTINUE_BOUNDED",
  "successorScope": "INITIAL_BOUNDED"
}
```
Actor exposure remains unresolved until fresh-context self-declaration; no source repair or completed attempt claimed.

## Worker Autonomy / No-Question Rule

Worker must repair allowed-scope checker failures directly by reading the failing checker source and matching the literal required shape. Worker should return to orchestrator only for a source contradiction, forbidden-scope need, or missing authority that makes completion impossible.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`documentation`, role=`dispatcher`, lifecyclePhase=`dispatch`.

Command: `python -B governance/compat/run_adif_defect_resolver.py --task-class documentation --role dispatcher --lifecycle-phase dispatch`.
Returned defects: NONE_RETURNED. Actual resolver executed 2026-10-05, candidates=0, returned=0, truncated=false.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | governance/compat/check_work_order_dispatch_quality.py; governance/compat/check_work_order_dispatch_quality_source.py; governance/compat/check_work_order_dispatch_quality_artifacts.py; governance/compat/check_dispatch_scaffold_provenance.py; governance/compat/check_gate_to_role_closeability.py; governance/compat/check_governed_artifact_checker_read_ahead.py; governance/compat/check_task_governance_route.py; governance/compat/check_baseline_update_compat.py; governance/compat/check_agent_operation_trace.py; governance/compat/check_work_order_acceptance_ledger.py; governance/compat/check_independent_review_probe_admission.py; governance/compat/check_absorption_blindspot_control_presence.py; governance/compat/check_external_knowledge_intake_routing.py; governance/compat/check_high_risk_local_transaction_proof.py; governance/compat/check_adif_defect_registry_disclosure.py; governance/compat/check_agent_packet_authority_and_encoding.py; governance/compat/check_markdown_structural_completeness.py; governance/compat/check_dispatch_prompt_envelope.py |
| literalTokensReviewed | DISPATCH_READY; exact3 outputs; acceptance-ledger-json; PENDING_REVIEWER_EXECUTION; structured envelope |
| gateRunPurpose | confirmation/evidence of manual dispatch shapes, not first discovery or experiment success |
| claimBoundary | no score, helper, live or build-ready result |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Neutral review-only input | CURRENT_SOURCE | docs/reviews/evidence/cvf-nis-t1g-reviewer-inputs-review-only-2026-10-05.json | format; genericChecklist; blankAnswerForm; attachments; reviewerViews | reviewerViews | Local filtered input package | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| Exact paths | three admission and three worker output paths absent | ACCEPT |
| Input overlap | existing neutral package reused with exact raw/blob pin | ACCEPT |

## Agent Handoff Contract Control Block

sharedWorktreeCoordinationMode: SEPARATE_GIT_WORKTREE

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | Local dispatcher/reviewer and distinct internal evaluation worker |
| phase | DISPATCH then IMPLEMENTATION then REVIEW |
| baseHeadFor(phase) | dispatchBaseHead=b94f893d077c89ac5d8deb282da665b754a733bd; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | Worker exactly three evidence paths; Local admission and continuity separately |
| traceScope(phase, actor) | worker command/evidence only; Local review does not recreate production replay |
| commitOwner(phase) | Local closer only; WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | Clean isolated worktree; preserve R0/R1 and main history |
| nextMoveSurfaces | active handoff, compact front door and canonical core/next move; generated outputs regenerated by Local |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_NIS_T1H_REVIEW_ONLY_MANUAL_ARM_COMPLETION_2026-10-05.md` required for CLOSED under continuation Rule B |
| reviewerOwnedClosurePaths | Current pair, required completion, bounded Local evidence and exact six continuity paths |
| closureOwner | Local reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Output Checker Read-Ahead Mandate

Before writing each worker-owned output artifact, read checker source for that file's docType, path family, and conditional content class.

| Output artifact | Required read-ahead result |
| --- | --- |
| worker return under `docs/reviews/` | derive exact review headings, worker-return quality terms, trace labels, delta boundary labels, corpus/value/rescan tokens, and no-commit evidence shape before writing |
| companion contract under `docs/reviews/` with docType reference | derive exact reference headings such as Scope / Applies To, Target / Source, source verification, corpus/value/rescan, trace, and claim-boundary labels before writing |

Literal-shape reminders: do not list required headings as backticked `## ...` strings before the real section; write source-not-found disposition spelling instead of the exact blocked enum in literalTokensReviewed; avoid `after ... closure` wording unless a dependency-release row cites the accepted artifact path and commit.

## Architecture Readiness Admission

Architecture-Readiness Admission: NOT_APPLICABLE_INTERNAL_AGENT_WITH_REASON - bounded manual documentary exercise, no product/helper/adapter execution.

## Required Artifact Manifest

| Required artifact | Owner |
|---|---|
| `docs/reviews/CVF_NIS_T1H_REVIEW_ONLY_MANUAL_ARM_WORKER_RETURN_2026-10-05.md` | Worker |
| `docs/reviews/evidence/cvf-nis-t1h-manual-raw-responses-2026-10-05.json` | Worker |
| `docs/reviews/evidence/cvf-nis-t1h-manual-exposure-timing-2026-10-05.json` | Worker |

## Work-Order Acceptance Requirement Ledger

```acceptance-ledger-json
{
  "schemaVersion": "cvf.workOrderAcceptanceLedger@1.0.0",
  "requirements": [
    {
      "requirementId": "REQ-1",
      "mandatory": true,
      "expectedArtifacts": [
        "docs/reviews/evidence/cvf-nis-t1h-manual-raw-responses-2026-10-05.json"
      ],
      "requiredProofIds": [
        "PROOF-RAW"
      ]
    },
    {
      "requirementId": "REQ-2",
      "mandatory": true,
      "expectedArtifacts": [
        "docs/reviews/evidence/cvf-nis-t1h-manual-exposure-timing-2026-10-05.json"
      ],
      "requiredProofIds": [
        "PROOF-TIME"
      ]
    },
    {
      "requirementId": "REQ-3",
      "mandatory": true,
      "expectedArtifacts": [
        "docs/reviews/CVF_NIS_T1H_REVIEW_ONLY_MANUAL_ARM_WORKER_RETURN_2026-10-05.md"
      ],
      "requiredProofIds": [
        "PROOF-RETURN"
      ]
    }
  ],
  "proofCatalog": [
    {
      "proofId": "PROOF-RAW",
      "kind": "ARTIFACT",
      "locator": "docs/reviews/evidence/cvf-nis-t1h-manual-raw-responses-2026-10-05.json"
    },
    {
      "proofId": "PROOF-TIME",
      "kind": "ARTIFACT",
      "locator": "docs/reviews/evidence/cvf-nis-t1h-manual-exposure-timing-2026-10-05.json"
    },
    {
      "proofId": "PROOF-RETURN",
      "kind": "COMMAND",
      "locator": "python -B governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_NIS_T1H_REVIEW_ONLY_MANUAL_ARM_2026-10-05.md"
    }
  ]
}
```

## Tool / Classifier Block Recovery Contract

toolClassifierBlockRecoveryApplicability: NOT_APPLICABLE_WITH_REASON - offline locally installed tooling and synthetic evidence only; classifier/tool denial must be disclosed and routed to Local, never bypassed.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_NIS_T1H_REVIEW_ONLY_MANUAL_ARM_WORKER_RETURN_2026-10-05.md`
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required terms: Purpose; Scope / Methodology; Findings / Position; Risk / Corrective Action; Claim Boundary; Agent Operation Trace Block; Delta Execution Claim Boundary Control Block; Public Export Disposition; executionBaseHead; git status --short.

Conditional terms: External Knowledge Intake Routing; Rescan Intelligence Hardening; Corpus Completeness And Report Integrity; Finding-To-Governance Learning Disposition; Epistemic Process Block; Machine Closure Package.

Use `N/A with reason` for every non-applicable conditional block.

Shape-list rule: when listing required worker-output sections, write section names without the `##` prefix. Reserve actual heading syntax for real sections so structural checkers do not treat this checklist as the artifact section body.

## Verification Commands

python -B governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_NIS_T1H_REVIEW_ONLY_MANUAL_ARM_2026-10-05.md --receipt-dir .cvf/runtime/nis-t1h-worker-20261005/pre-implementation

python -B governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_NIS_T1H_REVIEW_ONLY_MANUAL_ARM_2026-10-05.md

Governance, extraction/hash/clock evidence only. No automated substantive checks/scoring. Raw forms freeze before return/gate packaging; preserve failed logs.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local dispatcher |
| Provider or surface | Local private provenance workspace |
| Session or invocation | nis-t1h-redispatch-20261005 |
| Working directory | repository root |
| Command or tool surface | Bounded source reads, local scaffold and admission gates |
| Target paths | exact11 Local intake/redispatch/continuity; future3 outputs |
| Allowed scope source | operator continue and delegated Local orchestration |
| Before status evidence | clean worktree main b94f893d077c89ac5d8deb282da665b754a733bd |
| After status evidence | blocked sequence1 retained; redispatch sequence2 pending fresh context |
| Diff evidence | admission-paths.json exact11; dataset unchanged |
| Approval boundary | one manual review-only attempt, no automated evaluator |
| Claim boundary | dispatch authoring only |
| Agent type | dispatcher |
| Invocation ID | nis-t1h-redispatch-20261005 |
| Expected manifest | N/A with reason: exact9 Local admission only; future3 outputs separately named |
| Actual changed set | N/A with reason: admission only, worker pending |
| Manifest delta | N/A with reason: worker pending |
| Deletion or rename disposition | N/A with reason: no deletion or rename authorized |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | offline artifact transformation/source evaluation |
| claimDisposition | CLAIM_REJECTED: no runtime enforcement or AI governance behavior claimed |
| receiptEvidence | N/A with reason: dispatch only; worker evidence pending |
| actionEvidence | N/A with reason: dispatch only; worker artifacts pending |
| invocationBoundary | Local installed tools; zero provider/API calls |
| interceptionBoundary | No proxy/interception enforcement claimed |
| claimLanguage | Synthetic artifact fitness only |
| forbiddenExpansion | Provider, source fixes, store, UAC, real data, BUILD, deploy/public and parked lanes |

## Claim Boundary

rawMemoryReleased=false. Review-only historical synthetic bytes, not a current acceptance event, actual noncoder UX, build-ready certificate, live governance or two-arm cost proof. Shared-workspace blinding is a role protocol and self-declared exposure, not access isolation. No helper/evaluator/product/source/store/registry/checker/continuity/provider/network/install/BUILD/public/deploy/general S2 or parked-lane action. One primary attempt; no invented timing, score or blind status.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Private evaluation packet; no public export or push authorized.


## Authority Chain

Operator continue under delegated Local authority selects one manual review-only attempt after closed T1G preparation. Local verified the predecessor disposition before dispatch; this current pair is the execution authority. The reviewer must not open predecessor experimental artifacts because they disclose placement. No helper, candidate, provider/runtime or accepted-source experiment grant.

## Agent Roles

| Role | Owner | Boundary |
|---|---|---|
| Dispatcher | Local | scope/pins/release |
| Worker | fresh INTERNAL_AGENT context | one primary reasoning attempt, no self-score/commit |
| Scorer/reviewer/closer | Local placement-aware actor | evaluate retained answers after return, independent integrity probe and commits |

## Required First Reads

Progressive bootstrap/front door/current handoff; this CURRENT pair and docs/reviews/evidence/cvf-nis-t1h-dispatch-inputs-2026-10-05.json. Generic guard orientation/literal gotchas/output checkers only. Neutral docs/reviews/evidence/cvf-nis-t1g-reviewer-inputs-review-only-2026-10-05.json hash first, format/checklist/attachments only after preparation clock starts, views one at a time after per-case clock starts. Do not follow earlier experimental authority paths; current authority will name this pair.

## Allowed Scope

One human-style reasoning review-only attempt; exact3 outputs plus ignored .cvf/runtime/nis-t1h-worker-20261005 raw timing/submit evidence. Python/Git allowed only for governance, raw hash/JSON extraction/UTF-8 decoding and clock/file evidence. No dependency reads or automated substantive checking.

## Forbidden Scope

No answer key/placement source/old experiment docs/generators/Local probe/history/diffs/prior responses read; no replay/practice/backfill or editing submitted forms. No helper/evaluator/scorer/detector/product/source/test/store/registry/checker/continuity mutation; provider/network/install/upstream/browser/server/BUILD/public/push/deploy/general S2 or parked-lane effects. No stage/commit/stash/discard. No new relay/cover note.

## Write Ownership

Worker owns exactly3 output files and ignored raw evidence scratch. Local owns admission/continuity, correctness scoring, later independent evidence-integrity checks and commits. The worker must not manufacture benchmark scores.

## Pre-Flight Checks

Capture clean HEAD/status/index, expose context history honestly, verify neutral raw/blob pin without displaying views, verify3 new outputs absent, then run worker-owned bound pre-implementation. Prepare timers/response schema before preparation time starts. Placement knowledge blocks admission, never relabelled as freshness.

## Execution Plan

1. BEFORE opening any package view or earlier experiment material, declare actor/session/invocation, context origin, taxonomy familiarity, prior view exposure and placement knowledge. A fresh context may know generic review taxonomy, but must not know specific placement, key, case diffs or prior answers. Any seed author, Local key reader or placement-aware context must return BLOCKED_WITH_REASON before the attempt. Do not falsely reset identity by changing roles or opening a new file. Exposure is self-declared, not machine-verified.

2. Read only generic startup/authority/output rules and this pair/input. Verify the package raw/blob hash without displaying its views. Run own bound pre-implementation and prepare the output shapes and timer infrastructure before timing. Do not open previous NIS work orders, completions, full receiver, casepack, original protocol, scratch generators, Local probe scripts or diff history. No dependency reads or repository-wide search. Earlier files exist in the shared workspace; this prohibition is a cooperative role boundary, not access isolation.

3. Start the preparation clock when first displaying the neutral format/checklist/blank form and attachments. Preparation limit20 minutes. Read only those fields during preparation; do not display reviewerViews yet. Record real UTC start/end and monotonic elapsed time, clock source and any interruption. Frozen source placeholders and the absent accepted-file pairing are disclosed evidence limitations; this run is review-only and does not remove acceptance HOLD. Taxonomy familiarity supplied by the checklist is expected and declared separately.

4. In package order, open exactly one reviewer view and start its clock before displaying it. Review by reasoning over supplied text and attachments; JSON extraction/UTF-8 decoding, hashing and clock recording are allowed. Never write/run a helper, cross-link/quote/cycle detector, evaluator/scorer, test runner or automated answer generator; do not compute verdicts using a script. Use the supplied blank per-case form. Case limit12 minutes and overall active limit180 minutes including preparation. Submit each raw form before opening the next; record submit timestamp/hash immediately in scratch. Never revisit, amend or replace a submitted case. If a box expires, record NOT_ANSWERED with retained partial notes; do not backfill later. No practice attempt, no cross-case diff against a supposed clean record and no previous reviewer results. Different views may naturally look similar; any inadvertent outside information is disclosed.

5. Per case retain case id, cited source identity, unedited raw response including verdict, defect findings and limitations, start/end timestamps, monotonic elapsed seconds, interruption records and submitted response hash. Do not provide seeded class labels, hit counts, expected answers, correctness scores or a winning route. Local evaluates the actual finding/cause/locator after return. A justified unseeded concern is preserved, never suppressed to match an assumed key. No uncertainty is silently resolved as a user decision or authority grant.

6. Freeze three outputs: raw response JSON in presentation order, exposure/timing JSON, full worker return. Copy raw strings without editorial rewriting, verify per-response/file hashes and sequential timestamps, retain the ignored timestamp/submit log and failed attempts. Active time is measured from a monotonic source excluding explicitly logged interruptions; retain wall time separately. Include preparation plus per-case minutes in the effort evidence; no person-productivity or human cost equivalence claim for an agent attempt. If real clock measurement is unavailable, report NOT_MEASURED and do not invent elapsed values or claim a valid timed baseline. An incomplete/contaminated attempt is valid honest return evidence, never a success claim. Run full worker-return fast gate; leave HEAD/index unchanged.

## Evidence Requirements

Unedited per-case forms and submit hashes; actual UTC/monotonic preparation and per-case intervals; exclusions/interruptions and source clock; self-declared taxonomy/placement/prior exposure; sequential one-at-a-time evidence; full gate receipts and unchanged HEAD/index. No hit count or comparative cost/UX/live-governance claim. Report honest contamination/timeouts/NOT_MEASURED instead of replacing them.

## Acceptance Criteria

REQ-1: retained raw responses for all eleven views or explicit NOT_ANSWERED/NOT_EXECUTED with reasons, exact order and submit hashes; no response edited after submit, no self-scoring.
REQ-2: exposure/admission and actual clocks, preparation/timebox/interruptions evidence with measured or honestly unmeasured status; placement-aware actor blocked before attempt.
REQ-3: exact3-path full return, valid full fast gate, no forbidden effects, HEAD/index unchanged. A valid return may report incomplete/contaminated attempt; it is not a passing performance result.

## Review Gate

Local consumes retained responses and worker gate evidence; score semantic cause/locator using private key after return and independently verify time/hash/exposure joins. A real unseeded input defect invalidates the affected control/case rather than being a false positive. No rerun of the primary attempt. EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION; no broad duplicate source suite.

## Closure Checklist

Exact3 worker outputs; score only after raw responses frozen; independent response/hash/time integrity, incomplete/contaminated limits explicit; material and dedicated continuity commits; final bounded closure. No automatic helper or accepted-source promotion.

## Return-To-Orchestrator Conditions

COMPLETE_PENDING_REVIEW with exact3 outputs, or BLOCKED_WITH_REASON for placement exposure/authority gap before an attempt. Preserve incomplete attempt if time/exposure fails during execution; no redispatch pretending first occurrence or fresh baseline.

## Operator Checkpoint

No further confirmation for the admitted review-only attempt by a fresh eligible context. Placement-aware worker must stop before views and return consolidated exposure blocker. Helper/candidate/runtime/public effects remain excluded.

## High-Risk Local Transaction Proof Routing

High-Risk Local Transaction Proof Applicability: NOT_APPLICABLE_WITH_REASON - no cross-process writer, durable store, rollback, owner/DACL mutation or post-acquire transaction is authorized; ordinary synthetic evidence-file writes only.


## Evidence Reuse And Encoding Plan

Reuse neutral package exact bytes and preserved views; no regeneration or upstream/source audit. Actual responses are new evidence, not predictions. Canonical-equivalent checkout materialization by Local only, no source repin.

## Gate-To-Role Closeability Contract

closeabilityContractVersion: cvf.gate-role-closeability@1.0.0
closeabilityDisposition: CLOSEABLE
implementationTopologyPolicy: EXACT_PATHS_WITH_NO_FORESEEABLE_SPLIT
foreseeableFileSplitDisposition: NOT_REQUIRED_UNDER_SIZE_BUDGET
returnTimeRecheck: REQUIRED_BEFORE_REPAIR

| gateId | mustPassBy | repairOwner | repairPhase | mutationSurface | topology | commitOwner | commitPhase | dependsOn |
|---|---|---|---|---|---|---|---|---|
| authorization_review | PRE_DISPATCH | dispatcher | PRE_DISPATCH | exact new pair and source input JSON | EXACT_PATHS | closer | DISPATCH_COMMIT | NONE |
| pre_dispatch_gate | PRE_DISPATCH | dispatcher | PRE_DISPATCH | exact new pair and source input JSON | EXACT_PATHS | closer | DISPATCH_COMMIT | authorization_review |
| dispatch_continuity | IMPLEMENTATION | session-sync-steward | IMPLEMENTATION | AGENT_HANDOFF_V63_2026-09-18.md material-SHA marker and six exact continuity paths | EXACT_PATHS | session-sync-steward | DISPATCH_CONTINUITY_COMMIT | pre_dispatch_gate |
| pre_implementation_autorun | IMPLEMENTATION | worker | IMPLEMENTATION | exact three worker source/contract artifacts | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | exact three worker source/contract artifacts | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity, pre_implementation_autorun |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | worker return disclosure; no ADIF entry edit | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| worker_return_fast | REVIEW | worker | WORKER_RETURN | exact three worker source/contract artifacts | EXACT_PATHS | closer | MATERIAL_COMMIT | adif_integrity |
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | worker paths plus reviewer-owned disposition/evidence | EXACT_PATHS | closer | MATERIAL_COMMIT | worker_return_fast |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted material and fresh captured closure base | EXACT_PATHS | closer | MATERIAL_COMMIT | reviewer_fast |
| terminal_completion_review | PRE_MATERIAL_COMMIT | reviewer | REVIEW | required named completion plus worker-return disposition | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | exact six continuity paths | EXACT_PATHS | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL | split clean committed material/continuity ranges | EXACT_PATHS | closer | CORRECTIVE_MATERIAL_COMMIT | continuity |


## Current Runtime Freshness Verification

N/A_WITH_REASON - review-only exercise of frozen documentary bytes; no runtime/producer/acceptance activation.

## Intake Role Routing Decision

Intake: neutral internal documentary package. Selected role route: MULTI_AGENT_MULTI_ROLE; worker INTERNAL_AGENT regardless of provider/model, Local owns scoring and final decision.
Scope classification: exact3-output manual reasoning exercise, no evaluator.
Escalation condition: placement exposure, unavailable input/clock or required outside-scope action -> honest bounded return, never widen.

## Work-Order Fulfillment Manifest

Exact3 outputs; PROOF-RAW, PROOF-TIME, PROOF-RETURN. No automatic success/score or helper result.

## Independent Review Probe Admission Contract

independentProbeRequired: YES
independentProbeRiskClass: RESPONSE_TIME_AND_EXPOSURE_BINDING
independentProbeDispositionAtDispatch: PENDING_REVIEWER_EXECUTION
probeExecutorRole: LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER
implementationOracleSeparation: Local integrity/scoring invocation distinct from manual reviewer; does not recreate attempt
positiveControl: exact response/view ids and retained submit hashes/time intervals
negativeMutationClasses: edited response, reordered view, clock overlap, missing preparation, invented elapsed time, undisclosed placement exposure, scoring before freeze
expectedInformationGain: reject invalid attempt/evidence joins, score retained findings once
rerunCostReason: integrity only, no primary review replay
reviewerDecisionOwner: LOCAL

## Foundation Storage Layout Block

N/A with reason: dated source/contract artifacts only, no storage/foundation relocation.


## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md |
| Input type | internal governed input (no external intake) |
| Internal source | docs/reviews/evidence/cvf-nis-t1g-reviewer-inputs-review-only-2026-10-05.json |
| Chain map route | neutral input -> separate manual attempt -> Local scoring/disposition |
| Matching local-view guard | governance/compat/check_external_knowledge_intake_routing.py |
| Owner surface | existing NIS receiver / Local technical reviewer |
| Disposition | bounded review-only attempt; helper deferred |
| Claim boundary | no accepted-source or runtime proof |

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

NOT_APPLICABLE_WITH_REASON - no migration or external absorption.

## External Repository Absorption Entry Control

NOT_APPLICABLE_WITH_REASON - internal neutral documentary inputs only; no source acquisition or absorption.

## Mandatory Blind-Spot Control Block

Blind-spot verdict: NOT_APPLICABLE_WITH_REASON - one bounded manual exercise, no corpus/repository novelty claim.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - named neutral inputs, not a repository scan or complete requirement audit.

## Overlap And Novelty Classification

| Source item | Existing owner | Overlap disposition | Delta | Action |
|---|---|---|---|---|
| Neutral format/views | existing NIS receiver and Local input package | CONFIRMED_EXISTING | exact documentary inputs | reuse |
| Raw manual findings and clocks | Local experiment evaluation owner | ENRICH_EXISTING | one new primary attempt | retain no self-score |

## Dependency Gate

| Dependency | Evidence | Disposition |
|---|---|---|
| Neutral source package | docs/reviews/evidence/cvf-nis-t1g-reviewer-inputs-review-only-2026-10-05.json exact pin | ACCEPT |
| Fresh reviewer | exposure declared before views | CONDITIONAL_ADMISSION; placement-aware context returns blocked |
| Clock/governance tooling | installed Python/Git | ACCEPT, no dependency or provider invocation |

## Roadmap-To-Work-Order Trace Matrix

| Source milestone | Current disposition | This work order | Authority boundary |
|---|---|---|---|
| NIS build-ready target/document receiver experiment | one review-only primary attempt selected | REQ-1 raw findings, REQ-2 clocks/exposure | no accepted-source, product or helper proof |
| Helper/general S2/NCR P11 | excluded/parked | not admitted | no automatic successor |


## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: Local T1H admission-only current-authority/next-move. Worker cannot write protected paths.
Protected paths:
- `AGENT_HANDOFF_V63_2026-09-18.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
Operator authorization: continue under delegated Local orchestrator/reviewer/work-order/commit authority,2026-10-05.
Rollback boundary: exact11 Local admission paths; preserve prior closures, workers and parked lanes.
Local blocked-intake and redispatch history maintenance authorized by the latest operator request; no contaminated-worker return invented.

## Mixed Protected-Path Atomicity Authorization

Disposition: AUTHORIZED_EXACT_MANIFEST
Atomicity reason: blocked-intake/SCEC anchor, redispatch pair/input and six continuity owners bind one context-replacement grant. Dedicated material SHA follows.
Rollback boundary: exact11 Local intake/admission paths; original worker and old receipts retained.
Exact changed manifest: `docs/baselines/CVF_GC018_NIS_T1H_REVIEW_ONLY_MANUAL_ARM_2026-10-05.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NIS_T1H_REVIEW_ONLY_MANUAL_ARM_2026-10-05.md`; `docs/reviews/evidence/cvf-nis-t1h-dispatch-inputs-2026-10-05.json`; `docs/reviews/evidence/cvf-nis-t1h-dispatch-attempts-2026-10-05.json`; `docs/reviews/CVF_NIS_T1H_DISPATCH_EXPOSURE_INTAKE_2026-10-05.md`; `AGENT_HANDOFF_V63_2026-09-18.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/nextAllowedMove.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "CVF-NIS-T1H",
  "requestedProfile": "P3_ELEVATED",
  "classification": {
    "taskKind": "DOC_CHANGE",
    "authorityImpact": "USES_EXISTING_OWNER",
    "externalEffect": "LOCAL_REVERSIBLE",
    "dataSensitivity": "PRIVATE_REPO",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "NAMED_FILES",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "KNOWN_PATTERN"
  },
  "pathFamilies": [
    "docs/baselines/CVF_GC018_NIS_T1H_REVIEW_ONLY_MANUAL_ARM_2026-10-05.md",
    "docs/work_orders/CVF_AGENT_WORK_ORDER_NIS_T1H_REVIEW_ONLY_MANUAL_ARM_2026-10-05.md",
    "docs/reviews/evidence/cvf-nis-t1h-dispatch-inputs-2026-10-05.json",
    "docs/reviews/evidence/cvf-nis-t1h-dispatch-attempts-2026-10-05.json",
    "docs/reviews/CVF_NIS_T1H_DISPATCH_EXPOSURE_INTAKE_2026-10-05.md",
    "AGENT_HANDOFF_V63_2026-09-18.md",
    "CVF_SESSION_MEMORY.md",
    "CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json",
    "CVF_SESSION/state/entries/nextAllowedMove.json",
    "CVF_SESSION/ACTIVE_SESSION_STATE.json",
    "CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json",
    "docs/reviews/CVF_NIS_T1H_REVIEW_ONLY_MANUAL_ARM_WORKER_RETURN_2026-10-05.md",
    "docs/reviews/evidence/cvf-nis-t1h-manual-raw-responses-2026-10-05.json",
    "docs/reviews/evidence/cvf-nis-t1h-manual-exposure-timing-2026-10-05.json"
  ],
  "claims": [
    "MANUAL_REVIEW_ONLY_HISTORICAL_SYNTHETIC_INPUTS",
    "NO_RUNTIME_OR_BUILD_READY_ACCEPTANCE"
  ],
  "requiredProof": [
    "RAW_RESPONSES",
    "EXPOSURE_AND_REAL_CLOCKS",
    "FULL_LEGACY_GATES"
  ],
  "operatorCheckpoints": [
    "HELPER_CANDIDATE_RUNTIME_NOT_AUTHORIZED"
  ],
  "forbiddenEffects": [
    "PROVIDER_CALL",
    "NETWORK_ACCESS",
    "PRODUCT_MUTATION",
    "HELPER_IMPLEMENTATION",
    "STORE_MUTATION",
    "BUILD_EXECUTION",
    "PUBLIC_WRITE"
  ],
  "sourceEvidence": {
    "selectedFilesFullyRead": false,
    "corpusReceiptRef": null,
    "completenessClaimChanged": false
  }
}
```

## Task Governance Routing Receipt

```json
{
  "classification": {
    "authorityImpact": "USES_EXISTING_OWNER",
    "dataSensitivity": "PRIVATE_REPO",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "externalEffect": "LOCAL_REVERSIBLE",
    "novelty": "KNOWN_PATTERN",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "NAMED_FILES",
    "taskKind": "DOC_CHANGE"
  },
  "computedMinimumProfile": "P3_ELEVATED",
  "escalationTriggers": [
    "CONTINUITY_STATE_SURFACE",
    "DELEGATION_MULTI_ROLE_NO_COMMIT",
    "TASKKIND_DOC_CHANGE"
  ],
  "estimatedCommandCount": 5,
  "legacyGateDisposition": "RUN_FULL_LEGACY_BUNDLE",
  "profile": "P3_ELEVATED",
  "receiptStatus": "ROUTED_SHADOW",
  "schemaVersion": "cvf.taskGovernanceRoute.v1",
  "selectedBundles": [
    "CORE_INTEGRITY",
    "ARTIFACT_SHAPE",
    "SOURCE_PROVENANCE",
    "DELEGATION_HANDOFF",
    "CONTINUITY"
  ],
  "selectiveExecutionAuthorized": false,
  "skippedBundles": {
    "CODE_QUALITY": "NO_IMPLEMENTATION_SOURCE",
    "CORPUS_ACCOUNTING": "NO_CORPUS_OR_COMPLETENESS_CHANGE",
    "PUBLIC_RELEASE": "NO_PUBLIC_RELEASE_OR_DESTRUCTIVE_EFFECT",
    "RUNTIME_LIVE": "NO_RUNTIME_NETWORK_OR_LIVE_EFFECT",
    "STATE_AND_SECURITY": "NO_STATE_AUTH_SECRET_DEPENDENCY_OR_MUTATION_TRIGGER"
  },
  "taskId": "CVF-NIS-T1H",
  "validationErrors": []
}
```
T0 SHADOW_FULL_GATE_FALLBACK; selectiveExecutionAuthorized=false; full legacy bundles mandatory.

## Dispatch Attempt History And Fresh Context Admission

Dispatch sequence1 is BLOCKED_WITH_REASON / PLACEMENT_CONTAMINATION, recorded by Local in docs/reviews/CVF_NIS_T1H_DISPATCH_EXPOSURE_INTAKE_2026-10-05.md and docs/reviews/evidence/cvf-nis-t1h-dispatch-attempts-2026-10-05.json. Actual blocked worker return and worker-owned gate evidence are pinned in the ledger; no retained primary attempt exists. Redispatch sequence2, same T1H assignment, REWORK round1; dataset and exact3 outputs unchanged. Use NEW context that has NEVER read T1G experiment docs/full receiver/casepack, answer key, seed generators, Local probes/scoring or earlier answers; not seed author/key reader. Only the pinned neutral reviewer package plus current pair/startup/generic governance rules may be opened. The sole T1G-named file allowed is the neutral reviewer-inputs-review-only package; no other T1G artifact. A session reset with inherited context is not a fresh actor. Self-declare no such exposure before viewing anything; otherwise return blocked. These are cooperative read constraints, not filesystem isolation.
