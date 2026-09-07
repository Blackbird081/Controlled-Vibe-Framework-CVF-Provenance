# CVF Agent Work Order - DARA T2 Architecture Readiness Admission Implementation

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

Batch ID: DARA-T2-IMPLEMENTATION

Dispatch base head: e1a5e3abc45f836c2b35b3580b42e5199c2b18c8

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated implementation worker

Reviewer/closer: Codex reviewer/closer

Worker return path: `docs/reviews/CVF_DARA_T2_ARCHITECTURE_READINESS_ADMISSION_IMPLEMENTATION_WORKER_RETURN_2026-09-06.md`

Completion review path: `docs/reviews/CVF_DARA_T2_ARCHITECTURE_READINESS_ADMISSION_IMPLEMENTATION_COMPLETION_2026-09-06.md`

providerExecutionAuthority: FORBIDDEN

## Dispatch Prompt Envelope

Role: delegated implementation worker for DARA-T2.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_DARA_T2_ARCHITECTURE_READINESS_ADMISSION_IMPLEMENTATION_2026-09-06.md`.

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: DARA-T1 design is accepted bounded at material commit
`e7c559d5f5396b86cdedbc7ab4f4f35a5745d3d2`; MFRP P4-C1 remains the only
automatic evidence collector; WP-ARCH-003 repair remains parked.

Do-not-misread notes: implement only the exact manifest. Do not modify the
paired baseline/work order, MFRP receipt/readout/collector, roadmap, ADIF,
session state, active handoff, parked files, runtime/provider integrations, or
public-sync surfaces. Do not create a second evidence system or commit.

Required first actions: read startup surfaces, guard orientation, literal
gotchas, paired baseline, this packet, T1 design/review, MFRP P4-C1 owners, and
all checker source named below; capture full HEAD/status; run pre-implementation
before editing.

Return contract: implement, test, create the exact worker return, leave every
change uncommitted, and return `COMPLETE_PENDING_REVIEW` or
`BLOCKED_WITH_REASON`. The reviewer will evaluate returned evidence and will
not recreate the implementation.

## Purpose

Implement the accepted DARA-T2 architecture-readiness and quota-admission
control on existing CVF owners. Make incomplete design-bearing external
dispatches fail before invocation, preserve one reviewer workflow, and collect
causally attributed implementation evidence for improving the CVF foundation.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id DARA-T2 --title "DARA T2 Architecture Readiness Admission Foundation Implementation" --date 2026-09-06 --base e1a5e3abc45f836c2b35b3580b42e5199c2b18c8 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --dispatch-kind INITIAL --dispatch-surface EXTERNAL_AGENT_CLI_MCP --review-round-count 0 --cumulative-external-invocation-count 0 --external-invocation-ceiling 2 --stdout` |
| generatedProfile | protected-governance-path plus no-commit external-worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with frozen T1 implementation, hostile tests, exact manifest, reviewer boundary, and measurement evidence |
| checkerReadAheadConfirmation | dispatch, prompt, route, convergence, cost, source, protected-path, return, trace, and public guards |
| docOnlyNewFields | fault counters and worker-experience measurements already defined by T1 |
| claimBoundary | scaffold provenance only; no implementation or acceptance claim |

## Authority Chain

1. `ECOSYSTEM/doctrine/` and `ECOSYSTEM/operating-model/`.
2. `AGENTS.md` and current canonical work-order/review standards.
3. `docs/assessments/CVF_DARA_T1_ARCHITECTURE_READINESS_CONTRACT_DESIGN_2026-09-06.md`.
4. `docs/reviews/CVF_DARA_T1_ARCHITECTURE_READINESS_CONTRACT_DESIGN_REVIEW_2026-09-06.md` at material commit `e7c559d5f5396b86cdedbc7ab4f4f35a5745d3d2`.
5. Paired GC-018 baseline and current code/tests.

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL

dispatchSurface: EXTERNAL_AGENT_CLI_MCP

parentAssignmentId: DARA-T2-IMPLEMENTATION

reviewRoundCount: 0

priorFindingSetDigest: NOT_APPLICABLE_INITIAL_DISPATCH

dependencyAuditDisposition: COMPLETE_INITIAL_ACCEPTANCE_MATRIX

reworkFindingDisposition: NOT_APPLICABLE_INITIAL_DISPATCH

newIndependentCriticalEvidence: NONE

regressionGuardDisposition: BASELINE_NEGATIVE_TESTS_PLANNED

cumulativeExternalInvocationCount: 0

externalInvocationCeiling: 2

usageAvailability: KNOWN_FOR_ADMISSION

quotaAdmissionDisposition: ADMITTED_WITHIN_CUMULATIVE_CEILING

nextDispatchDisposition: INITIAL_DISPATCH

rootCauseClusterId: NOT_APPLICABLE_INITIAL_DISPATCH

reworkGeneration: 0

consolidatedDefectClassSweep: COMPLETE_INITIAL_ACCEPTANCE_MATRIX

successorTrancheOpened: NO

implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY

preExecutionReviewAdmission: NOT_REQUIRED_BEFORE_EXECUTION

preExecutionReviewTrigger: NONE

nextRoutineReviewBoundary: WORKER_RETURN

reviewerWorkBoundary: EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION

Admission rationale: the immutable T1 contract and exact owner map were already
reviewed and accepted; this packet transcribes that bounded identity without
changing owner, path, risk, authority, or external-effect scope. Dispatch will
consume invocation 1 of 2. A rework may consume invocation 2 only after one
consolidated finding set; no third automatic dispatch is allowed.

## Semantic Convergence Outcome

Standard: `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md`

```json
{
  "schemaVersion": "cvf.semanticConvergenceControl.v1",
  "problemKey": "DARA-ARCHITECTURE-READINESS",
  "chainMode": "INITIAL",
  "chainOrdinal": 0,
  "predecessor": null,
  "blockerDelta": {
    "prior": [],
    "resolved": [],
    "retained": [],
    "new": ["architecture_control_not_implemented", "worker_evidence_not_returned"],
    "reopened": [],
    "current": ["architecture_control_not_implemented", "worker_evidence_not_returned"]
  },
  "resolutionEvidence": {},
  "counters": {"partialReadyClosures": 0, "reviewerScopeExpansions": 0, "sameClaimCorrections": 0, "nonDecreasingBlockerTransitions": 0},
  "claims": [{"claimId": "DARA-T2-DISPATCH", "claimClass": "DOCUMENTATION_ONLY", "proofClass": "PROPOSAL_ONLY_NO_RUNTIME_READINESS", "evidenceRef": "docs/reviews/CVF_DARA_T1_ARCHITECTURE_READINESS_CONTRACT_DESIGN_REVIEW_2026-09-06.md"}],
  "requiredDisposition": "CONTINUE_BOUNDED",
  "successorScope": "INITIAL_BOUNDED"
}
```

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"DARA-T2-IMPLEMENTATION","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"PURE_LOCAL_IMPLEMENTATION","authorityImpact":"ENRICHES_EXISTING_OWNER","externalEffect":"NONE","dataSensitivity":"PRIVATE_REPO","reversibility":"GIT_REVERSIBLE","sourceScale":"NAMED_FILES","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"NEW_INTERFACE"},"pathFamilies":["docs/baselines/","docs/reference/","governance/compat/","docs/reviews/"],"claims":["accepted DARA-T1 contract can be implemented on ten existing owners"],"requiredProof":["focused positive tests","sixteen hostile families","scaffold alignment","MFRP non-regression","fault attribution","no-commit return"],"operatorCheckpoints":["reviewer acceptance","provider/live","public sync"],"forbiddenEffects":["worker commit","MFRP collector change","runtime provider call","session mutation","public sync","automatic successor"],"sourceEvidence":{"selectedFilesFullyRead":true,"corpusReceiptRef":"N/A with reason: bounded named files","completenessClaimChanged":false}}
```

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | accepted local DARA-T1 design and review |
| Route | `MULTI_AGENT_MULTI_ROLE` |
| canonical route mode | `MULTI_AGENT_MULTI_ROLE` |
| scope classification | bounded local governance implementation on existing owners |
| risk sensitivity | HIGH because dispatch admission and protected guard paths change |
| selected role route | dispatch author freezes contract; worker implements without commit; reviewer evaluates evidence without implementation |
| External agent disposition | one initial external CLI/MCP invocation admitted; maximum one consolidated rework |
| escalation condition | source contradiction, eleventh implementation path, MFRP seam change, or invocation ceiling reached |

## Worker Autonomy / No-Question Rule

Repair allowed-scope implementation and test failures directly. Ask only if a
current authority contradicts T1, a required path lies outside the exact
manifest, or completion would require a forbidden MFRP/runtime/session/public
change. Do not ask the reviewer to choose an implementation that the frozen
contract already determines.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Returned defects: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020,
ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044, ADIF-0045,
ADIF-0051, ADIF-0052, ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024,
ADIF-0031, ADIF-0039, ADIF-0043, ADIF-0049, ADIF-0006.

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --json --max-results 50` |
| Returned defect count | 22 |
| Disclosed defectIds | all IDs listed above |
| Dispatch impact | exact path/symbol contract; protected-path authorization; verified commands; return freshness; causal fault metrics; no duplicate reviewer work |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_absorption_blindspot_control_presence.py` |
| literalTokensReviewed | DISPATCH_READY, source table columns, INITIAL sentinel values, no-commit return profile, task route JSON, protected-path authorization, trace labels, public disposition |
| gateRunPurpose | confirm the packet after exact contract authoring |
| claimBoundary | structural PASS does not prove DARA implementation or semantic acceptance |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| immutable authoring preimage and derived-field exclusion | accepted contract | `docs/assessments/CVF_DARA_T1_ARCHITECTURE_READINESS_CONTRACT_DESIGN_2026-09-06.md` | Architecture Binding Matrix Contract | `architectureMatrixCanonicalDigest` | `cvf.dara.architectureBindingMatrix.v1` | ACCEPT |
| exact ten-path owner map | accepted contract | `docs/assessments/CVF_DARA_T1_ARCHITECTURE_READINESS_CONTRACT_DESIGN_2026-09-06.md` | DARA-T2 Exact Owner Change Map | `DARA-T2` | DARA roadmap | ACCEPT |
| sixteen hostile families | accepted contract | `docs/assessments/CVF_DARA_T1_ARCHITECTURE_READINESS_CONTRACT_DESIGN_2026-09-06.md` | Hostile Test Contract | `Minimum T2 test families` | DARA-T1 contract | ACCEPT |
| bounded design accepted | review evidence | `docs/reviews/CVF_DARA_T1_ARCHITECTURE_READINESS_CONTRACT_DESIGN_REVIEW_2026-09-06.md` | Decision / Disposition | `DESIGN_ACCEPTED_BOUNDED` | T1 reviewer | ACCEPT |
| no second MFRP collector | existing owner | `docs/work_orders/CVF_AGENT_WORK_ORDER_MFRP_P4_C1_AUTOMATIC_EVIDENCE_COLLECTION_2026-09-02.md` | Purpose | `P4-C1` | MFRP roadmap | ACCEPT |
| reviewer non-duplication | canonical standard | `docs/reference/review_cost_control/CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md` | Reviewer Work Boundary | `EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION` | Review Cost standard | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| target baseline, work order, and return | exact path checks before authoring; all absent | ACCEPT_NO_COLLISION |
| implementation token | exact search across governed docs/session returned no conflicting T2 packet | ACCEPT_NO_COLLISION |
| existing worker return route | both scaffold generators exist and are named in manifest | EXTEND_EXISTING |
| DARA evidence subsystem | forbidden; MFRP P4-C1 is retained | REJECT_PARALLEL_OWNER |

## Architecture Readiness Implementation Contract

Implement the full field contract and closed chain from T1. Applicability is
external `EXTERNAL_AGENT_CLI_MCP`, HIGH or CRITICAL risk or authority expansion,
and design-bearing work. Applicable packets fail closed unless the matrix is
machine complete, semantic review identity is immutable and current, known
cumulative usage is below its ceiling, and reviewer work boundary is exact.

Digest serialization must be UTF-8 without BOM, forward-slash repo-relative
paths, ordinal/code-point row order by `criterionId`, LF separators, and one
trailing LF. Hash only immutable authoring fields from `criterionId` through
`evidenceOutputPath`; never hash machine/reviewer-derived fields.

The matrix chain is authority -> owner -> implementation -> producer/trust ->
carrier -> export -> registration or accepted absence -> composition root ->
non-test consumer or explicit contract-only boundary -> positive, negative,
bypass, and composition tests -> literal evidence output.

## Required Artifact Manifest

| Artifact | Required worker action |
|---|---|
| `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | add applicability, matrix/scalars, fault attribution, echo contract, and quota ordering |
| `governance/compat/build_dispatch_packet_scaffold.py` | emit checker-safe blocked defaults and matrix headings; never invent rows |
| `governance/compat/test_build_dispatch_packet_scaffold.py` | prove blocked defaults and absence of a second reviewer workflow |
| `governance/compat/build_worker_return_skeleton_scaffold.py` | emit immutable architecture identity echo only |
| `governance/compat/run_worker_return_scaffold.py` | align standalone generation with the same echo contract |
| `governance/compat/test_run_worker_return_scaffold.py` | prove generator alignment and identity-drift blocking |
| `governance/compat/check_work_order_dispatch_quality.py` | define shared markers/enums and architecture validation |
| `governance/compat/check_work_order_dispatch_quality_range.py` | call architecture validation only for applicable changed work orders |
| `governance/compat/check_work_order_dispatch_quality_source.py` | reuse exact path/symbol/locator validation for matrix identities |
| `governance/compat/test_check_work_order_dispatch_quality.py` | implement positive and hostile dispatch cases |
| `docs/reviews/CVF_DARA_T2_ARCHITECTURE_READINESS_ADMISSION_IMPLEMENTATION_WORKER_RETURN_2026-09-06.md` | return evidence using full-gate profile; no other output |

Exact-manifest rule: these eleven worker-owned paths are exhaustive. If another
path is required, stop with `BLOCKED_WITH_REASON`; do not add it implicitly.

## Work-Order Fulfillment Manifest

Fulfillment is exact equality between the eleven Required Artifact Manifest
paths, the actual changed paths, and the paths named in the worker return. No
deletion or rename is allowed. The paired baseline and this work order are
dispatcher-owned committed inputs and must not appear in the worker diff.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | existing reference template, compat helpers/checkers/tests, and one review return |
| Storage decision | extend existing owners; create no new foundation root or evidence store |
| Existing aggregate impact | none |
| Generated state impact | none during worker execution |
| Durable governance boundary | work order remains contract owner; MFRP P4-C1 remains automatic measurement owner |

## Agent Roles

| Role | Responsibility |
|---|---|
| operator | authorizes scope and external-worker dispatch |
| dispatcher | freezes exact contract, manifest, and invocation ceiling |
| worker | implements and returns evidence without commit |
| reviewer/closer | evaluates returned evidence without implementation and owns accepted commits |

## Required First Reads

Read the startup front door/bootstrap/active handoff progressively, guard
orientation and literal gotchas, paired baseline/work order, T1 design and
review, all ten owner files, their focused tests, and every applicable checker
before writing.

## Pre-Flight Checks

Capture `git rev-parse HEAD`, `git status --short`, exact output-path absence,
and the real pre-implementation gate result. Stop if HEAD differs from the
committed dispatch head or if an unrelated changed path overlaps the manifest.

## Write Ownership

Worker owns uncommitted changes to exactly the eleven manifest paths.
Reviewer/closer owns review disposition, any optional completion review,
material commit, and later separately authorized continuity sync. Worker must
not edit dispatcher inputs or repair parked findings.

## Execution Plan

1. Read checker/source owners and capture pre-edit evidence.
2. Implement shared matrix parsing/validation without adding a second gate
   entrypoint or reviewer workflow.
3. Update both scaffold routes with blocked defaults and exact echo semantics.
4. Add all hostile/positive tests and retain existing P4-C1 behavior.
5. Run focused tests, repair only in scope, then run the mandated return gates.
6. Complete the worker return with first-run and final-run evidence.

## Evidence Requirements

The returned evidence must prove exact manifest equality, all sixteen test
families, both generator routes, unchanged MFRP ownership, six causal counters,
invocation 0-to-1 accounting, command failures/repairs, no commit, and any
usage/time limitation. Evidence IDs must resolve inside the return.

## Acceptance Criteria

- Applicable HIGH/CRITICAL external design-bearing dispatches fail closed on
  incomplete, unclassified, stale, over-ceiling, or reviewer-recreation state.
- Complete accepted matrices pass with deterministic digest and exact review
  binding; machine PASS cannot create semantic acceptance.
- Documentation echo does not demand a second review; identity drift blocks.
- Internal-agent non-applicability and existing MFRP P4-C1 behavior remain
  unchanged.
- The worker return has exact causal metrics and full first/final evidence.
- The actual changed set equals the eleven-path manifest and HEAD is unchanged.

## Review Gate

Reviewer evaluates the returned evidence and targeted diff, then runs the
worker-return fast gate and reviewer-return steward preflight. Reviewer does
not implement or broad-rerun evidence absent a named contradiction, expected
information gain, and cost reason. Any repair request is one consolidated set.

## Closure Checklist

- exact manifest and protected authorization match;
- no placeholders, invented symbols, or stale hashes;
- focused and hostile tests pass;
- existing MFRP owner and receipt semantics are unchanged;
- fault counters reconcile to evidence IDs;
- no worker commit or staged changes;
- reviewer disposition precedes material commit;
- continuity and any DARA-T3 decision remain separate.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only when all acceptance criteria and commands
pass with actual evidence. Otherwise return `BLOCKED_WITH_REASON` with one
precise blocker and no out-of-scope workaround.

## Operator Checkpoint

No checkpoint is needed for in-scope implementation. Stop for an eleventh
implementation path, MFRP seam change, source contradiction, provider/live or
public action, destructive operation, or a second rework beyond ceiling.

## Hostile Test And Acceptance Matrix

| ID | Required case | Acceptance |
|---|---|---|
| HT-01 | complete accepted HIGH external matrix | passes dispatch quality |
| HT-02 | missing applicability declaration or row | blocks before invocation |
| HT-03 | placeholder or path-class evidence output | blocks |
| HT-04 | duplicate behavior identity or two owners for one behavior | blocks; same owner may own distinct behaviors |
| HT-05 | nonexistent existing path, locator, or symbol | blocks |
| HT-06 | producer chain missing carrier/export/registration/composition/consumer | blocks |
| HT-07 | planned component without production composition test | blocks |
| HT-08 | worker-selected owner or pending semantic state | blocks |
| HT-09 | review path, commit, or file SHA mismatch | blocks |
| HT-10 | canonical matrix digest drift | blocks |
| HT-11 | usage unknown or ceiling reached | blocks |
| HT-12 | machine PASS plus reviewer-recreation language | blocks |
| HT-13 | frozen-design documentation echo | passes without a second review |
| HT-14 | internal-agent non-applicability | excluded from external count |
| HT-15 | current P4-C1 collector and receipt-v3 focused tests | unchanged and pass |
| HT-16 | historical WP-ARCH-003 Initial/R1/R2 fixture | remains unused until DARA-T3 |

## Fault Attribution And Evidence Measurement Contract

The worker return must include non-negative values for
`dispatcherDefectCount`, `workerExecutionDefectCount`,
`reviewerLateDiscoveryCount`, `repairIntroducedDefectCount`,
`machineCoverageGapCount`, `unattributedDefectCount`, and
`faultAttributionEvidenceIds`. Every non-zero value needs an evidence ID and a
row stating observation, earliest preventable boundary, accountable class, and
why other roles are not charged. A missing upstream binding is an orchestrator
defect, not a worker defect.

Also record:

- full start/end HEAD and exact changed manifest;
- external invocation count before=0 and after=1 for this dispatch;
- token/quota usage and elapsed worker time when observable, otherwise an exact
  unavailability reason;
- number of ambiguities, clarification questions, failed commands, and repair
  iterations;
- first-run and final-run results for each focused command;
- a gate-failure ledger with failure ID, command, defect class, cause, repair,
  and regression test;
- scaffold/manual-authoring friction and any reusable CVF learning candidate;
- natural `P4 Automatic Evidence Observation Block` values produced by existing
  P4-C1 logic. Do not manufacture eligibility or a sample.

This evidence is part of the worker return, not a new collector, ledger,
readout, receipt, checkpoint, or per-row reviewer workflow.

## Reviewer Non-Duplication Contract

The reviewer will consume valid worker test outputs, hashes, manifests, and
failure ledger. Review is bounded to source/diff inspection, targeted
contradiction checks, worker-return fast gate, preflight/steward gates, and any
M5/M10/safety/M20 action admitted by MFRP. The reviewer must not edit worker
implementation or repeat broad suites merely to recreate evidence. If the
return fails, the reviewer issues one consolidated finding set with causal
attribution and expected information gain; rework remains within the ceiling.

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

priorVerificationArtifact: `docs/reviews/CVF_DARA_T1_ARCHITECTURE_READINESS_CONTRACT_DESIGN_REVIEW_2026-09-06.md`

priorVerificationAnchor: material commit `e7c559d5f5396b86cdedbc7ab4f4f35a5745d3d2`

freshRecomputeRequired: YES

recomputeReason: T2 changes executable checker and scaffold behavior, so fresh focused and range evidence is required

unicodePathHandling: use literal paths and UTF-8-safe readers; do not normalize or rewrite unrelated Unicode paths

extractedTextAuthority: current governed repository source and direct command output only

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | dispatch author -> no-commit implementation worker -> independent implementation reviewer/closer |
| phase | DARA-T2 implementation |
| baseHeadFor(phase) | dispatchBaseHead=e1a5e3abc45f836c2b35b3580b42e5199c2b18c8; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | exact eleven worker-owned paths |
| traceScope(phase, actor) | worker records commands/diff/failures; reviewer records targeted evidence evaluation |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer/closer only after acceptance |
| crossBatchIsolation | preserve two parked WP-ARCH-003 untracked files and exclude them from all DARA diffs/gates/commits |
| nextMoveSurfaces | worker return, then reviewer decision; no automatic DARA-T3 or WP-ARCH-003 resume |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | N/A with reason: implementation evidence returns through the governed worker-return route |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | paired baseline, this work order, T1 design/review, and current code owners |
| Disposition | NOT_APPLICABLE_WITH_REASON: no external knowledge is promoted as authority |
| Claim boundary | the worker return is pending evidence until reviewer acceptance |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | optional; prefer an in-place reviewer disposition in the worker return unless an independent completion packet is required |
| reviewerOwnedClosurePaths | accepted worker-output material commit and later bounded continuity update only |
| closureOwner | Codex reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_DARA_T2_ARCHITECTURE_READINESS_ADMISSION_IMPLEMENTATION_WORKER_RETURN_2026-09-06.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required terms: Purpose; Scope / Methodology; Findings / Position; Risk /
Corrective Action; Claim Boundary; Checker Source Read-Ahead Block; Agent
Operation Trace Block; Delta Execution Claim Boundary Control Block; Public
Export Disposition; executionBaseHead; git status --short; Changed Files;
Command Evidence; No-Commit Statement.

Conditional blocks must use `N/A with reason` when genuinely inapplicable.
Before writing the return, read the current return-quality checker and both
scaffold generators; replace every placeholder with actual evidence.

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python -m unittest governance.compat.test_build_dispatch_packet_scaffold governance.compat.test_run_worker_return_scaffold governance.compat.test_check_work_order_dispatch_quality
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/run_agent_automation_assist.py --base <executionBaseHead> --head HEAD --json --enforce
git diff --name-status
git status --short
```

Before running a command, confirm its `--help` or source signature. If the
module-style unittest command is unsupported in this repository, record that
first failure and run the exact supported focused commands without hiding it.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: implement only the accepted DARA-T2
contract on these protected paths.

Protected paths:

- `governance/compat/build_dispatch_packet_scaffold.py`
- `governance/compat/test_build_dispatch_packet_scaffold.py`
- `governance/compat/build_worker_return_skeleton_scaffold.py`
- `governance/compat/run_worker_return_scaffold.py`
- `governance/compat/test_run_worker_return_scaffold.py`
- `governance/compat/check_work_order_dispatch_quality.py`
- `governance/compat/check_work_order_dispatch_quality_range.py`
- `governance/compat/check_work_order_dispatch_quality_source.py`
- `governance/compat/test_check_work_order_dispatch_quality.py`

Operator authorization: improve the CVF foundation first, delegate T2 to the
external implementation worker, retain Codex as reviewer, and gather real
evidence for foundation improvement, on 2026-09-06.

Rollback boundary: revert only the eventual DARA-T2 material commit if the
reviewer rejects it; preserve T1, MFRP P4-C1, parked WP-ARCH-003 files, and
unrelated worktree state.

Not authorized: worker commits, extra paths, MFRP collector/receipt/readout,
session/roadmap/ADIF edits, provider/live/public/deploy actions, or automatic
successor work.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatch author preparing later reviewer-only evaluation |
| Provider or surface | local private CVF workspace |
| Session or invocation | DARA-T2 implementation dispatch, 2026-09-06 |
| Working directory | repository root |
| Command or tool surface | source/checker reads, ADIF resolver, scaffold preview, exact collision checks, apply_patch, pre-dispatch gate |
| Target paths | paired GC-018 baseline and this work order |
| Allowed scope source | operator instruction to prompt the external worker and keep Codex as reviewer |
| Before status evidence | clean worktree for the DARA dispatch range at gate/commit time after exact isolation of two unrelated parked untracked files; HEAD `e1a5e3abc45f836c2b35b3580b42e5199c2b18c8` |
| After status evidence | exactly two dispatch artifacts pending validation; no implementation |
| Diff evidence | `git diff --name-status`; `git status --short` |
| Approval boundary | work-order authoring and dispatch only |
| Claim boundary | no worker execution, reviewer acceptance, runtime/provider/live/public effect |
| Agent type | dispatcher now; reviewer after worker return |
| Invocation ID | `dara-t2-implementation-dispatch-2026-09-06` |
| Expected manifest | paired baseline and this work order |
| Actual changed set | same two paths, excluding pre-existing parked untracked files |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | DARA-T2 local governance helper/checker/template implementation and tests |
| claimDisposition | CLAIM_REJECTED until worker evidence and reviewer acceptance exist |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no new runtime receipt is authorized |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime/provider action is authorized |
| invocationBoundary | one external worker invocation admitted within cumulative ceiling 2 |
| interceptionBoundary | no direct interception, provider wrapper, runtime gate, or agent coding control |
| claimLanguage | bounded pre-invocation dispatch-quality control candidate |
| forbiddenExpansion | MFRP duplication, runtime/provider/live/public/package/deploy behavior |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private foundation work order; no public-sync authority.

## Claim Boundary

This work order authorizes exactly ten existing owner changes plus one worker
return. It does not authorize a commit, a second evidence collector, MFRP
receipt/readout changes, session or roadmap mutation, DARA-T3, WP-ARCH-003
repair, provider/live execution, public sync, deployment, or production claim.
