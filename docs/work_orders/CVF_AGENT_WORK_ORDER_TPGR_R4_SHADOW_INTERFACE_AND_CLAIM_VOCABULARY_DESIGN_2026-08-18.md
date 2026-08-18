# CVF Agent Work Order - TPGR-R4 Shadow Interface And Claim Vocabulary Design

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

docType: work-order

Batch ID: TPGR-R4

Dispatch base head: `783cf1e96cb634beb6bc2b2b119f8a0d8d8a67a3`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: delegated design worker

Reviewer/closer: CVF reviewer/orchestrator

Worker return path: `docs/reviews/CVF_TPGR_R4_SHADOW_INTERFACE_AND_CLAIM_VOCABULARY_DESIGN_WORKER_RETURN_2026-08-18.md`

## Dispatch Prompt Envelope

Role: delegated design worker for TPGR-R4.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_TPGR_R4_SHADOW_INTERFACE_AND_CLAIM_VOCABULARY_DESIGN_2026-08-18.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`.

Current-time notes: artifact date is 2026-08-18; start only from a clean
post-continuity HEAD.

Do-not-misread notes: design only. Do not edit standards, checkers,
registries, catalogs, hooks, state, source corpora, or runtime/product code.

Required first actions: read startup surfaces, guard orientation, literal
gotchas, this packet, paired baseline, R3 assessment/worker return, accepted
reconciliation, targeted critique sections, current TPGR standard, and all
applicable checker sources before authoring.

Return contract: create exactly two outputs, run required gates, leave both
unstaged/uncommitted, and return `COMPLETE_PENDING_REVIEW` or
`BLOCKED_WITH_REASON`.

## Purpose

Produce a documentation-only R4 design that turns accepted R3 floors into a
minimal shadow interface and scope-safe claim vocabulary while routing into,
not duplicating, CVF's existing absorption lifecycle.

## Worker Autonomy / No-Question Rule

Repair allowed-scope checker or contract defects directly. Return to the
reviewer only for a source contradiction, forbidden-path requirement, or
missing authority that makes completion impossible.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| R3 threshold design | accepted material `b029e61de9c44bcb428debb2627d283995a53966` | SATISFIED |
| R4 operator authority | standing instruction to proceed under CVF rules | SATISFIED |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id TPGR-R4 --title "Shadow Interface And Claim Vocabulary Design" --date 2026-08-18 --base 783cf1e96cb634beb6bc2b2b119f8a0d8d8a67a3 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | completed R4 sources, design contract, exact outputs, hostile cases, gates, and closure boundaries |
| checkerReadAheadConfirmation | applicable dispatch and worker-output checker sources inspected |
| docOnlyNewFields | shadow-interface candidates only; no active schema field is added |
| claimBoundary | scaffold provenance only; no implementation claim |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: 22 results, not truncated.

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 50 --json` |
| Returned defect count | 22 |
| Returned defects | ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020, ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044, ADIF-0045, ADIF-0051, ADIF-0052, ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024, ADIF-0031, ADIF-0039, ADIF-0043, ADIF-0049, ADIF-0006 |
| Disclosed defectIds | same exact 22 IDs |
| Dispatch impact | exact scope, source-bound claims, no provider authority, no worker commit, and reviewer-owned closure |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_task_governance_route.py` |
| literalTokensReviewed | `DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; `COMPLETE_PENDING_REVIEW`; `Source Verification Block`; `Agent Handoff Contract Control Block`; `Reviewer Closure Conversion`; `Worker Return Packet Shape Contract`; `DEFERRED_PRIVATE_ONLY` |
| gateRunPurpose | confirmation/evidence, not first discovery |
| claimBoundary | checker conformance only; reviewer independently decides semantic acceptance |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| R4 next-step disposition | predecessor authority | `docs/assessments/CVF_TPGR_R3_ARCHETYPE_THRESHOLD_PROOF_DIVERGENCE_AND_ROLLBACK_FLOOR_DESIGN_2026-08-18.md` | Decision; Final Disposition | `PROCEED_TO_R4_SHADOW_INTERFACE_DESIGN` | R3 design contract | ACCEPT |
| R4 sequence scope | roadmap authority | `docs/reviews/CVF_TPGR_SECOND_UPGRADE_GENERALIZATION_CRITIQUE_RECONCILIATION_AND_R2_RESCOPE_2026-08-17.md` | Revised Delivery Sequence | R4 row | generalized TPGR sequence | ACCEPT |
| Threshold/reference candidates | predecessor design | `docs/assessments/CVF_TPGR_R3_ARCHETYPE_THRESHOLD_PROOF_DIVERGENCE_AND_ROLLBACK_FLOOR_DESIGN_2026-08-18.md` | R4 Candidate Delta Manifest | candidate rows | zero-edit delta manifest | ACCEPT |
| Eight-token vocabulary and anti-aggregation rules | reconciled advisory input | `docs/reviews/CVF_TPGR_SECOND_UPGRADE_GENERALIZATION_EXTERNAL_CRITIQUE_2026-08-17.md` | Semantic Completeness Vocabulary; Binding Rules | claim tokens | advisory routed through accepted reconciliation | ACCEPT |
| Current router remains full-bundle shadow mode | active authority | `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md` | Activation And Enforcement; Claim Boundary | `selectiveExecutionAuthorized` | TPGR routing standard | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Four intended artifact paths | all returned false before authoring | PASS |
| Exact namespace search | `rg -n "TPGR_R4_SHADOW_INTERFACE_AND_CLAIM_VOCABULARY_DESIGN" docs CVF_SESSION` returned no prior artifact | PASS |
| Collision decision | new exact namespace | CREATE_NEW |

## Required First Reads

1. `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
2. `CVF_SESSION_MEMORY.md`
3. `AGENT_HANDOFF_V59_2026-08-11.md`
4. `docs/reference/guard_orientation/README.md`
5. `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
6. paired R4 baseline and this work order
7. R3 assessment and worker return
8. generalized critique reconciliation and targeted external-critique stage/vocabulary sections
9. `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md`
10. targeted Layer A owners cited by the R3 Canonical Fact-Owner Map

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| `docs/assessments/CVF_TPGR_R4_SHADOW_INTERFACE_AND_CLAIM_VOCABULARY_DESIGN_2026-08-18.md` | create complete R4 shadow-interface and vocabulary design |
| `docs/reviews/CVF_TPGR_R4_SHADOW_INTERFACE_AND_CLAIM_VOCABULARY_DESIGN_WORKER_RETURN_2026-08-18.md` | create full worker-return evidence packet |

Forbidden paths: every other repository path.

## Design Contract

The assessment must include:

- an S0-S8 reference map to existing CVF owners, explicitly not a new lifecycle;
- a minimal shadow-interface field table covering `intakeStage`, `claimToken`,
  `claimScopeRef`, `evidenceRefs`, `invalidatedBy`, `reviewAuthority`,
  `routeOutcome`, and `eligibilityState`;
- field owner, type, allowed values, who may assert it, validation source,
  missing/malformed behavior, and invalidation trigger;
- exactly eight claim tokens and exact positive/forbidden implications;
- no promotion by aggregation: cluster receipts never imply corpus absorption;
- `CORPUS_SEMANTICALLY_ABSORBED` proof requiring explicit unread-file
  reconciliation and scope-total equality;
- escalation-only uncertainty treatment with negative proof that worker input
  cannot select a lighter route;
- upstream-drift handling even when selected file hashes remain stable;
- hostile cases and decision tables for unknown token, missing scope/evidence,
  stale dependency, contradictory owner facts, and authority laundering;
- R5 candidate command/receipt invalidation manifest with zero current edits;
- one allowed final disposition.

## Exact Claim Vocabulary

| Token | Minimum meaning | Forbidden implication |
| --- | --- | --- |
| `SOURCE_REGISTERED` | identity and scope known | any reading occurred |
| `STRUCTURALLY_ENUMERATED` | manifest/hash/count reconciled | any file was substantively read |
| `LEDGER_DISPOSITIONED` | every item has terminal disposition | every file was substantively understood |
| `TRIAGE_CLASSIFIED` | overlap/novelty triage completed | value confirmed or materialized |
| `CLUSTER_SEMANTICALLY_READ` | exact named cluster substantively read | repository-level understanding |
| `CAPABILITY_ABSORBED` | bounded capability materialized in a named CVF owner | repository absorbed |
| `CORPUS_SEMANTICALLY_ABSORBED` | every substantive file read and reconciled into owners | N/A; highest corpus semantic claim |
| `DELTA_ACCOUNTED` | upstream change enumerated against pinned prior | delta absorbed or semantically resolved |

## Required Hostile Cases

1. Ten cluster receipts are aggregated into a corpus claim.
2. Ledger completeness is cited as semantic understanding.
3. Upstream commit changes while selected file hashes stay stable.
4. Worker declares low uncertainty or low authority impact.
5. Claim token is unknown, missing, or malformed.
6. Claim scope exceeds evidence scope by one file.
7. Owner changes after receipt creation.
8. `OWNER_GAP` is used to auto-create a new CVF owner.
9. Project source is cited as CVF authority.
10. Corpus claim omits unread-file reconciliation.

Every case must fail closed to a named route and preserve historical receipt
evidence without preserving current eligibility.

## Allowed Final Dispositions

- `PROCEED_TO_R5_SHADOW_COMMAND_AND_RECEIPT_INVALIDATION`
- `REVISE_R4_INTERFACE`
- `NARROW_TO_CLAIM_VOCABULARY_ONLY`
- `STOP_TPGR_SECOND_UPGRADE`

## Acceptance Criteria

- exact two-path output manifest; no stage/commit;
- interface is smaller than and references Layer A rather than duplicating it;
- exactly eight tokens with scope-safe implications;
- no aggregation promotion and no worker self-downgrade;
- missing, malformed, stale, unknown, or contradictory facts fail closed;
- S8 upstream identity drift invalidates relevant eligibility even with stable selected hashes;
- no new truth store, registry, lifecycle, or command catalog;
- no implementation or protected edit;
- R5 candidate manifest is zero-edit and exact;
- worker-return fast, reviewer-fast, and full pre-implementation gates pass.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | dispatcher -> external design worker -> independent reviewer/closer |
| phase | R4 design execution pending reviewer return |
| baseHeadFor(phase) | dispatchBaseHead=`783cf1e96cb634beb6bc2b2b119f8a0d8d8a67a3`; executionBaseHead=worker capture; closureBaseHead=reviewer set |
| changedSetScope(phase) | worker exactly two output paths; reviewer later owns repair/commit/continuity |
| traceScope(phase, actor) | worker records reads, edits, commands, base, status, and no-commit evidence |
| commitOwner(phase) | reviewer/closer only; worker forbidden |
| crossBatchIsolation | stop if any unrelated path is dirty |
| nextMoveSurfaces | active handoff, bootstrap read model, generated session state, and front door upon reviewer acceptance with material commit evidence |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_TPGR_R4_SHADOW_INTERFACE_AND_CLAIM_VOCABULARY_DESIGN_COMPLETION_2026-08-18.md` (optional reviewer-owned artifact) |
| reviewerOwnedClosurePaths | accepted output repair/commit and later continuity surfaces |
| closureOwner | CVF reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Output Checker Read-Ahead Mandate

Before writing each output, derive exact required headings, field labels,
enums, conditional sections, trace fields, no-commit evidence, and claim
boundaries from applicable checker source. The dispatch checklist is not a
substitute for output-specific checker read-ahead.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_TPGR_R4_SHADOW_INTERFACE_AND_CLAIM_VOCABULARY_DESIGN_WORKER_RETURN_2026-08-18.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Verification Commands

```powershell
python governance/compat/run_worker_return_scaffold.py --write docs/reviews/CVF_TPGR_R4_SHADOW_INTERFACE_AND_CLAIM_VOCABULARY_DESIGN_WORKER_RETURN_2026-08-18.md --title "CVF TPGR-R4 Shadow Interface And Claim Vocabulary Design Worker Return" --profile WORKER_RETURN_FULL_GATE_V1
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/check_task_governance_route.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast
git diff --check
git status --short --untracked-files=all
```

Do not run pre-commit; the worker must not stage or commit.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | delegated design worker |
| Provider or surface | operator-transferred external worker; repository-local evidence only |
| Session or invocation | TPGR-R4 design execution |
| Working directory | repository root |
| Command or tool surface | governed reads, scaffold, local queries, gates, and Git diagnostics |
| Target paths | exact assessment and worker-return paths |
| Allowed scope source | paired baseline and this work order |
| Before status evidence | clean worktree and captured executionBaseHead required before edits |
| After status evidence | exactly two unstaged/untracked outputs |
| Diff evidence | untracked-aware status plus name-status |
| Approval boundary | documentation-only design |
| Claim boundary | no implementation or authority mutation |
| Agent type | external delegated worker |
| Invocation ID | tpgr-r4-worker-2026-08-18 |
| Expected manifest | exact two output paths |
| Actual changed set | worker records final exact set |
| Manifest delta | MATCH required |
| Deletion or rename disposition | N/A with reason: forbidden |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | documentation-only R4 design |
| claimDisposition | CLAIM_REJECTED_NO_EXECUTION |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT |
| actionEvidence | CLAIM_REJECTED_NO_ACTION |
| invocationBoundary | local reads, design authoring, and deterministic gates |
| interceptionBoundary | no wrapper, proxy, hook, runtime gate, or agent-control interception |
| claimLanguage | proposed shadow interface and vocabulary only |
| forbiddenExpansion | R5-R9 execution, T15, protected edits, intake, selective execution, runtime/provider/live/public/deploy/production |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | reconciled critique -> accepted R2G -> accepted R3 -> bounded R4 design |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | TPGR standard and existing Layer A owners |
| Disposition | RECONCILED_DESIGN_INPUT_ONLY |
| Claim boundary | no direct import, authority promotion, or new corpus intake |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON
- N/A with reason: existing governed evidence is reused; no source refresh or completeness update.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - design fixtures only; no new corpus or complete-scan claim.

## Finding-To-Governance Learning Disposition

Record any reusable defect using checker-accepted class/lane/disposition; if
none, state N/A with reason. Do not edit ADIF, standards, or checkers.

## Epistemic Process Block

Expected Result / Prediction: a small interface and reserved vocabulary can
prevent stage-claim laundering without duplicating Layer A.

Evidence Comparison: compare against R3 floors, S0-S8 advisory model, current
TPGR authority, existing Layer A owners, and all hostile cases.

Contradiction Or Gap Disposition: duplication, unsafe aggregation, stale
eligibility, or unowned fields require revision, narrowing, or stop.

Claim Update: return one allowed R4 disposition and change no authority.

## Foundation Storage Layout Block

Use existing assessment and review directories only. No new directory,
schema, registry, aggregate, catalog, package, or runtime surface.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private documentation-only design dispatch.

## Claim Boundary

This work order authorizes exactly two R4 documentation outputs. It does not
authorize active standard/interface changes, implementation, selective
execution, R5-R9, T15, protected edits, source intake, runtime/provider/live,
public-sync, deployment, or production.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "TPGR-R4",
  "requestedProfile": "P2_BOUNDED",
  "classification": {
    "taskKind": "DOC_CHANGE",
    "authorityImpact": "USES_EXISTING_OWNER",
    "externalEffect": "NONE",
    "dataSensitivity": "PRIVATE_REPO",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "BOUNDED_CLUSTER",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "OWNER_COMPOSITION"
  },
  "pathFamilies": ["docs/baselines/", "docs/assessments/", "docs/reviews/"],
  "claims": ["bounded shadow-interface and claim-vocabulary design"],
  "requiredProof": ["S0-S8 map", "eight-token vocabulary", "hostile cases", "full legacy gate"],
  "operatorCheckpoints": [],
  "forbiddenEffects": ["protected mutation", "new intake", "selective execution", "runtime or external effects"],
  "sourceEvidence": {
    "selectedFilesFullyRead": true,
    "corpusReceiptRef": "N/A with reason: accepted design evidence only; no corpus claim",
    "completenessClaimChanged": false
  }
}
```

Expected route: `ROUTED_SHADOW`, `P2_BOUNDED`, selective execution false,
and `RUN_FULL_LEGACY_BUNDLE`.

## Authority Chain

Frozen doctrine -> `AGENTS.md` and active continuity -> accepted R3 -> paired
R4 baseline -> this work order. Stop on conflict or expansion.

## Agent Roles

- Dispatcher authors and commits dispatch.
- Worker creates exactly two outputs and does not stage/commit.
- Reviewer independently verifies, repairs within scope, and commits.
- Operator retains scope expansion and external-effect authority.

## Pre-Flight Checks

Run `git rev-parse HEAD`, untracked-aware clean status, full
pre-implementation, and task-governance route checks before editing. Expected:
clean base, all gates PASS, shadow route, selective execution false.

## Intake Role Routing Decision

| Field | Decision |
| --- | --- |
| Intake summary | no new intake; accepted governed design evidence only |
| Scope classification | documentation-only bounded interface design |
| Risk sensitivity | MEDIUM, authority-sensitive and reversible |
| Selected role route | routeMode=`MULTI_AGENT_SINGLE_ROLE`; dispatcher -> worker -> reviewer/closer |
| Role separation basis | worker cannot commit; reviewer reproduces evidence |
| Worker role | interface and vocabulary designer |
| Reviewer role | source, ownership, anti-aggregation, invalidation, hostile-case, and gate reviewer |
| Escalation condition | dirty start, contradiction, missing owner, forbidden path, network need, or unrepairable gate failure |
| Source authority | CVF-governed sources; critique only through accepted reconciliation |
| Corpus action | none |
| Direct import | forbidden |

## Write Ownership

Worker owns only the assessment and worker-return paths. Reviewer/closer owns
bounded corrections, material commit, and continuity.

## Execution Plan

Capture base; run pre-flight; scaffold return; read authorities/checkers;
build stage/interface/vocabulary/hostile/invalidation tables; produce zero-edit
R5 candidate manifest; run gates; return exact uncommitted outputs.

## Evidence Requirements

Every interface field and token must name its owner, scope, assertion
authority, validator, missing/malformed behavior, and invalidator. Unknown or
projected behavior must remain explicitly non-implemented.

## Review Gate

Worker return is not acceptance. Reviewer independently verifies all sources,
eight tokens, S0-S8 references, hostile cases, exact paths, and gates.

## Operator Checkpoint

No checkpoint inside R4 design. R5, implementation, protected mutation,
selective execution, source intake, or external effects require a fresh
governed boundary decision.

## Closure Checklist

- [ ] Execution-base worktree status captured.
- [ ] Exactly two uncommitted outputs.
- [ ] S0-S8 map and eight-token vocabulary complete.
- [ ] Aggregation and self-downgrade fail closed.
- [ ] Stable-file upstream drift invalidates eligibility.
- [ ] Zero-edit R5 manifest and one allowed disposition.
- [ ] Required gates pass; reviewer alone commits.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only with exact manifest and evidence; return
`BLOCKED_WITH_REASON` for contradiction, forbidden scope, missing authority,
or unrepairable failure.

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: R4 designs a shadow interface and claim vocabulary
from accepted evidence and changes no legacy absorption coverage claim or
coverage-index row.
