# CVF Agent Work Order - MSEA-R15 MinerU Sample Stressor Provenance Gap Closure

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

docType: work_order

Date: 2026-07-03

Batch ID: MSEA-R15

Dispatch base head: dd767187

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker role

Reviewer/closer: reviewer/closer

Worker return path: `docs/reviews/CVF_MSEA_R15_MINERU_SAMPLE_STRESSOR_PROVENANCE_GAP_CLOSURE_WORKER_RETURN_2026-07-03.md`

## Dispatch Prompt Envelope

Role: delegated worker for MSEA-R15.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R15_MINERU_SAMPLE_STRESSOR_PROVENANCE_GAP_CLOSURE_2026-07-03.md`

Paired GC-018 baseline:
`docs/baselines/CVF_GC018_MSEA_R15_MINERU_SAMPLE_STRESSOR_PROVENANCE_GAP_CLOSURE_2026-07-03.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: artifact date is 2026-07-03. Treat relative dates as
unsafe; record concrete dates in the worker return.

Do-not-misread notes: this is provenance-gap closure documentation only. It
does not authorize route execution, operator-local file copy, sample document
import, sample corpus population, MinerU runtime, OCR/parser/VLM execution,
provider/live proof, RAG write, schema implementation, receipt-writer code,
checker implementation, adapter implementation, public-sync, legal-domain
product work, document-truth, extraction-accuracy, current-law correctness,
legal advice quality, benchmark, or production-readiness claims.

Required first actions: read `CVF_SESSION_MEMORY.md`,
`CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`,
`CVF_SESSION/ACTIVE_SESSION_STATE.json`, `AGENT_HANDOFF_V33_2026-07-03.md`,
`docs/reference/guard_orientation/README.md`,
`docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`,
this work order, the paired GC-018 baseline, all Source Verification Block
owner surfaces, and every checker source listed below before writing worker
outputs.

Return contract: create the worker return artifact and companion
provenance-gap closure ledger, run required gates, leave changes uncommitted,
and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Create a CVF-owned provenance-gap closure ledger for the legal-policy
sample-stressor candidates after MSEA-R14 selected
`OPEN_SAMPLE_STRESSOR_PROVENANCE_GAP_CLOSURE`.

The worker must determine what the current operator instruction closes, what
remains held, and whether a later sample-corpus population work order can be
authored. The worker must preserve the downstream workflow-chain intent while
keeping live run and runtime work behind a later fresh packet.

## Authority Chain

| Authority | Evidence |
|---|---|
| Operator continuation instruction | operator stated on 2026-07-03 that they want to continue absorbing repo value and may live run if needed to form a workflow-chain system |
| Active session state | mode routes to MSEA-R15 gap-closure work-order authoring after MSEA-R14 acceptance |
| Accepted route decision | `docs/reference/CVF_MSEA_R14_MINERU_POST_SAMPLE_QUALIFICATION_ROUTE_DECISION_MATRIX_2026-07-03.md` |
| Accepted candidate qualification | `docs/reference/CVF_MSEA_R13_T1_MINERU_LEGAL_POLICY_SAMPLE_CORPUS_CANDIDATE_QUALIFICATION_LEDGER_2026-07-03.md` |
| Accepted sample policy | `docs/reference/CVF_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_2026-07-03.md` |
| Paired baseline | `docs/baselines/CVF_GC018_MSEA_R15_MINERU_SAMPLE_STRESSOR_PROVENANCE_GAP_CLOSURE_2026-07-03.md` |

## Agent Roles

| Role | Assignment | Boundary |
|---|---|---|
| Dispatcher | dispatch author | authors and commits dispatch packet only |
| Worker | delegated worker role | creates pending worker return and companion gap-closure ledger only |
| Reviewer/closer | reviewer/closer role | reviews, repairs allowed-scope defects, commits material if accepted |
| Operator | operator | owns permission/license, privacy/redaction tolerance, proof-use authorization, later live run, and any runtime/public/production decision |

## Required First Reads

| Order | Required read |
|---|---|
| 1 | `CVF_SESSION_MEMORY.md` |
| 2 | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| 3 | `CVF_SESSION/ACTIVE_SESSION_STATE.json` |
| 4 | `AGENT_HANDOFF_V33_2026-07-03.md` |
| 5 | `docs/reference/guard_orientation/README.md` |
| 6 | `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` |
| 7 | paired GC-018 baseline and this work order |
| 8 | `docs/reference/CVF_MSEA_R14_MINERU_POST_SAMPLE_QUALIFICATION_ROUTE_DECISION_MATRIX_2026-07-03.md` |
| 9 | `docs/reference/CVF_MSEA_R13_T1_MINERU_LEGAL_POLICY_SAMPLE_CORPUS_CANDIDATE_QUALIFICATION_LEDGER_2026-07-03.md` |
| 10 | `docs/reference/CVF_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_2026-07-03.md` |
| 11 | checker source listed in the dispatch and worker-output read-ahead blocks |

## Pre-Flight Checks

| Check | Command or evidence |
|---|---|
| Capture base | `git rev-parse --short HEAD` |
| Capture worktree | `git status --short` |
| Confirm output paths absent | `Test-Path` for named worker return and provenance-gap closure ledger |
| Confirm accepted owner surfaces exist | `Test-Path` for R12, R13, and R14 owner surfaces |
| Read output checkers | worker records checker paths and literal tokens before writing outputs |

## Write Ownership

| Actor | Owned paths |
|---|---|
| Worker | `docs/reviews/CVF_MSEA_R15_MINERU_SAMPLE_STRESSOR_PROVENANCE_GAP_CLOSURE_WORKER_RETURN_2026-07-03.md`; `docs/reference/CVF_MSEA_R15_MINERU_SAMPLE_STRESSOR_PROVENANCE_GAP_CLOSURE_LEDGER_2026-07-03.md` |
| Reviewer/closer | allowed-scope repair to worker-owned material artifacts and optional completion review only if required |
| Session-sync steward | active session and handoff surfaces only after accepted material commit |

Forbidden worker changes:

- any legal-policy sample document, external bundle, source mirror, external
  repository clone, legacy folder, package/runtime/checker file, generated
  aggregate, public-sync file, Web/MCP/model-router file, session state,
  handoff, or active front-door file;
- sample document copy or import, corpus population, schema implementation,
  receipt-writer code, adapter code, tests that imply runtime behavior,
  provider/live proof, S3 credentials, Docker build/run, RAG index write,
  package activation, public-sync, or production-readiness evidence;
- treating the operator's current high-level continuation instruction as
  automatic privacy/redaction clearance for all documents if the source
  evidence does not support that conclusion.

## Review Gate

Reviewer/closer must run worker-return fast gate and reviewer-return steward
preflight before accepting material closure. Worker output with failed required
gates must be repaired in allowed scope or returned as `BLOCKED_WITH_REASON`.

## Worker Autonomy / No-Question Rule

Worker must repair allowed-scope checker failures directly by reading the
failing checker source and matching the literal required shape. Worker should
return to orchestrator only for a source contradiction, missing owner surface,
forbidden-scope need, or missing authority that makes completion impossible.

Worker must not ask the operator a preference question during this execution.
The worker must classify the current operator statement exactly as source
evidence supports it. If privacy/redaction or permission/license remains
insufficiently specific, select `PARTIAL_GAP_CLOSURE_PENDING_OPERATOR_DETAIL`
or `HOLD_SAMPLE_STRESSOR_LANE` and explain the missing detail.

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intakeRole | DISPATCHER_TO_WORKER |
| workerRole | delegated worker |
| reviewerRole | reviewer/closer |
| commitMode | WORKER_MUST_NOT_COMMIT |
| risk sensitivity | legal-policy sample-stressor provenance and privacy classification; no document content import or runtime action |
| selected role route | dispatcher_to_worker_to_reviewer_closer |
| canonical route mode | SINGLE_AGENT_SINGLE_ROLE |
| routingDecision | worker performs provenance-gap closure analysis only and returns uncommitted artifacts |
| escalationRule | return `BLOCKED_WITH_REASON` only for source contradiction, missing owner surface, forbidden-scope need, or missing authority |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R15 --title "MinerU Sample Stressor Provenance Gap Closure" --date 2026-07-03 --base dd767187 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Replaced placeholders with MSEA-R12/R13/R14 accepted evidence, operator continuation intent, gap-closure classification tokens, next-route tokens, and no-runtime boundaries. |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_rescan_intelligence_hardening.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_adif_defect_registry_disclosure.py` |
| docOnlyNewFields | gap-closure classification token; provenance-gap closure ledger; downstream workflow-chain readiness route |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |

## Execution Plan

1. Capture `executionBaseHead` and worktree evidence.
2. Read all startup, source authority, and checker files required above.
3. Confirm planned output paths are absent.
4. Build a candidate-group-by-gap matrix for Group A and the T11B-verified subset of Group B.
5. Classify each gap using only the allowed gap-closure tokens.
6. Select exactly one next-route token and explain downstream workflow-chain implications.
7. Create only the worker return and companion provenance-gap closure ledger.
8. Run required gates, record command evidence, and leave the work uncommitted.

## Gap Closure Classification Instructions

| Gap | Worker must determine |
|---|---|
| permission/license statement | whether the operator's 2026-07-03 instruction is enough to authorize internal private CVF processing/storage for the candidate group, and whether any candidate remains excluded |
| privacy/redaction disposition | whether the candidate group is low-risk enough to proceed, requires redaction, or must remain held pending explicit operator detail |
| proof-use confirmation | whether the operator's workflow-chain/live-run intent authorizes using the candidate group as proof-grade stressor evidence in later packets, without authorizing runtime now |

Allowed gap-classification tokens:

- `CLOSED_BY_OPERATOR_STATEMENT`
- `PARTIAL_WITH_LIMITS`
- `HELD_PENDING_OPERATOR_DETAIL`
- `REJECTED_FOR_THIS_LANE`

Allowed next-route tokens:

- `OPEN_SAMPLE_CORPUS_POPULATION_WORK_ORDER`
- `PARTIAL_GAP_CLOSURE_PENDING_OPERATOR_DETAIL`
- `HOLD_SAMPLE_STRESSOR_LANE`

Expected default: choose `PARTIAL_GAP_CLOSURE_PENDING_OPERATOR_DETAIL` unless
the current operator statement and accepted owner surfaces are specific enough
to close all three gaps for at least one candidate group without relying on
assumption.

## Evidence Requirements

| Evidence class | Required proof |
|---|---|
| source ownership | cite R12 policy, R13 qualification ledger, R14 route matrix, and operator continuation instruction |
| gap closure | matrix with three gap rows for Candidate Group A and the T11B-verified subset of Candidate Group B |
| rejected material | keep 9 ungoverned derived outputs rejected for direct promotion |
| downstream workflow-chain route | next-route token plus explanation of whether corpus-population work order is now authorable |
| no execution | `git diff --name-status` and `git status --short` evidence showing only worker-owned artifacts |
| checker read-ahead | worker return records checker source and literal tokens reviewed before writing outputs |
| no commit | No-Commit Statement uses `WORKER_MUST_NOT_COMMIT honored` |

## Acceptance Criteria

| Criterion | Required evidence |
|---|---|
| gap matrix complete | every required gap is classified for Candidate Group A and the T11B-verified subset of Candidate Group B |
| operator intent bounded | worker states exactly what the 2026-07-03 operator instruction closes and what it does not close |
| privacy/license caution retained | unsupported permission/license or privacy/redaction assumptions become held or partial rows |
| downstream route selected | exactly one allowed next-route token is selected |
| no execution claim | claim boundary rejects corpus population, runtime/live proof, schema/writer/adapter/checker work, and production readiness |
| no worker commit | worker leaves both artifacts uncommitted for reviewer/closer |

## Closure Checklist

| Item | Required disposition |
|---|---|
| every required gap classified for each candidate group | checked, or `BLOCKED_WITH_REASON` |
| next-route token present | checked, or `BLOCKED_WITH_REASON` |
| derived-output rejection retained | checked |
| worker-owned paths only | checked by changed-file evidence |
| required gates recorded | checked, or blocked with command output |
| no forbidden claim retained | checked by claim-boundary sections |
| no commit/stage/push by worker | checked by git evidence |

## Operator Checkpoint

No interactive operator checkpoint is required during worker execution. The
operator's current 2026-07-03 continuation instruction is evidence to classify,
not a blank check. If the instruction is insufficient to close a specific gap,
the worker records the missing detail in the ledger and returns a held or
partial next-route token.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | No mandatory ADIF defectIds apply. Worker must still obey output-artifact checker read-ahead and literal-format gotchas. |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_rescan_intelligence_hardening.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_adif_defect_registry_disclosure.py` |
| literalTokensReviewed | Dispatch Prompt Envelope; Status: DISPATCH_READY; Source Verification Block columns; ACCEPT; REJECT; source-not-found disposition spelling; Roadmap-to-Work-Order Trace Matrix; Negative Search And Collision Discipline; Agent Handoff Contract Control Block; Reviewer Closure Conversion; WORKER_MUST_NOT_COMMIT; WORKER_RETURN_FULL_GATE_V1; CHECKER_SAFE_SKELETON_REQUIRED; External Knowledge Intake Routing field labels; external repo or copied folder; External Absorption Core field labels; ledger_terminal=; DOCTRINE_ADAPTED, RUNTIME_CANDIDATE, CHECKER_CANDIDATE, REJECT_DIRECT_IMPORT, NO_PACKAGE_OR_RUNTIME_VALUE; Corpus verdict bullet; Rescan intelligence verdict; Delta Execution Claim Boundary Control Block fields; DEFERRED_PRIVATE_ONLY |
| gateRunPurpose | Confirmation evidence after dispatcher checker read-ahead; not first discovery. |
| claimBoundary | Read-ahead covers this dispatch packet only. Worker-created review/reference outputs must perform their own checker-source read-ahead by docType before writing. |

## Worker Output Checker Read-Ahead Mandate

Before writing the worker return or companion ledger, worker must read the
checker source as applied to each output file's docType, path family, and
conditional content class.

| Output artifact | Required checker source read-ahead before writing |
|---|---|
| Worker return under the reviews area | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_rescan_intelligence_hardening.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_agent_operation_trace.py` |
| Reference ledger under the reference area | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_rescan_intelligence_hardening.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_agent_operation_trace.py` |

The worker return must state that this read-ahead happened before writing the
outputs, list exact literal headings/tokens reviewed, and use gate runs as
confirmation evidence, not first discovery.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| MSEA-R14 selected the sample-stressor provenance-gap closure route | VALUE_SET | `docs/reference/CVF_MSEA_R14_MINERU_POST_SAMPLE_QUALIFICATION_ROUTE_DECISION_MATRIX_2026-07-03.md` | line 63; `## Selected Route`; `## Proof-Precondition Summary` | OPEN_SAMPLE_STRESSOR_PROVENANCE_GAP_CLOSURE | MSEA-R14 route-decision matrix | ACCEPT |
| R14 requires permission/license, privacy/redaction, and proof-use confirmation before downstream work | VALUE_SET | `docs/reference/CVF_MSEA_R14_MINERU_POST_SAMPLE_QUALIFICATION_ROUTE_DECISION_MATRIX_2026-07-03.md` | lines 104-118; `## Proof-Precondition Summary` | Proof-Precondition Summary | MSEA-R14 route-decision matrix | ACCEPT |
| R12 defines sample intake evidence requirements including permission/license, privacy/redaction, slot, format/size, and proof-use confirmation | VALUE_SET | `docs/reference/CVF_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_2026-07-03.md` | lines 75-91; `## Sample Intake And Provenance Policy` | Sample Intake And Provenance Policy | MSEA-R12 sample-corpus policy | ACCEPT |
| R12 keeps sample corpus population behind a fresh GC-018 after policy evidence exists | VALUE_SET | `docs/reference/CVF_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_2026-07-03.md` | lines 126-142; `## Held-Lane Reopen Routing` | Sample corpus population | MSEA-R12 sample-corpus policy | ACCEPT |
| R13 classifies Candidate Group A and the T11B-verified subset of Candidate Group B as partially ready pending operator confirmation | VALUE_SET | `docs/reference/CVF_MSEA_R13_T1_MINERU_LEGAL_POLICY_SAMPLE_CORPUS_CANDIDATE_QUALIFICATION_LEDGER_2026-07-03.md` | lines 115-137; `## Sample Intake Provenance Gap Matrix` | PARTIALLY_READY_PENDING_OPERATOR_CONFIRMATION | MSEA-R13 qualification ledger | ACCEPT |
| R13 rejects the nine ungoverned derived outputs for direct promotion | VALUE_SET | `docs/reference/CVF_MSEA_R13_T1_MINERU_LEGAL_POLICY_SAMPLE_CORPUS_CANDIDATE_QUALIFICATION_LEDGER_2026-07-03.md` | lines 139-158; `## Rejected Derived Output Boundary` | NOT_READY | MSEA-R13 qualification ledger | ACCEPT |
| R13 says legal-policy evidence is a sample stressor, not a legal-domain product lane or runtime reopen condition | VALUE_SET | `docs/reference/CVF_MSEA_R13_T1_MINERU_LEGAL_POLICY_SAMPLE_CORPUS_CANDIDATE_QUALIFICATION_LEDGER_2026-07-03.md` | lines 160-186; `## MinerU Route Implication` | MinerU Route Implication | MSEA-R13 qualification ledger | ACCEPT |
| Worker-return full-gate profile is a dispatch-quality recognized contract | EXISTS | `governance/compat/check_work_order_dispatch_quality.py` | `WORKER_RETURN_FULL_GATE_PROFILE`; `WORKER_RETURN_FULL_GATE_REQUIRED_TERMS` | WORKER_RETURN_FULL_GATE_V1 | work-order dispatch-quality checker | ACCEPT |
| WORKER_MUST_NOT_COMMIT requires handoff control and reviewer conversion | EXISTS | `governance/compat/check_agent_handoff_boundary.py` | `REVIEWER_CONVERSION`; `WORKER_MUST_NOT_COMMIT` | Agent Handoff Contract Control Block | handoff boundary checker | ACCEPT |

## New Doc-Only Fields

| Field | Intended owner surface | Runtime/source status |
|---|---|---|
| gap-closure classification token | MSEA-R15 provenance-gap closure ledger | DOC_ONLY_NEW |
| provenance-gap closure ledger | MSEA-R15 provenance-gap closure ledger | DOC_ONLY_NEW |
| downstream workflow-chain readiness route | MSEA-R15 provenance-gap closure ledger | DOC_ONLY_NEW |
| operator continuation intent | MSEA-R15 provenance-gap closure ledger | DOC_ONLY_NEW |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| Baseline path existence before authoring | `Test-Path` returned `False` for the paired baseline path | PASS |
| Work-order path existence before authoring | `Test-Path` returned `False` for this work-order path | PASS |
| Planned worker-return path existence before authoring | `Test-Path` returned `False` for the planned worker-return path | PASS |
| Planned ledger path existence before authoring | `Test-Path` returned `False` for the planned provenance-gap closure ledger path | PASS |
| Collision search for R15 dispatch tokens | search roots: governed artifact roots plus session state; query used MSEA-R15, MSEA_R15, title, and selected route tokens; result: ZERO_R15_ARTIFACT_COLLISION before authoring | PASS |
| Generic route-token collision coverage | `OPEN_SAMPLE_STRESSOR_PROVENANCE_GAP_CLOSURE` appears in R14 and session state as predecessor evidence; R15-specific artifact collision count is zero | PASS |
| Collision decision | R15 dispatch paths are new and collision-free | DISPATCH_ALLOWED |

## Roadmap-to-Work-Order Trace Matrix

| Requirement source | Requirement | Work-order instruction | Worker output evidence |
|---|---|---|---|
| MSEA-R14 route decision | open provenance-gap closure before sample corpus population | classify the three required gaps by candidate group | R15 closure ledger |
| MSEA-R13 qualification | Group A and the T11B-verified subset of Group B remain partially ready pending operator confirmation | evaluate only these candidate groups; keep derived outputs rejected | R15 candidate-group matrix |
| MSEA-R12 policy | corpus population requires source identity, permission/license, privacy/redaction, slot, format/size, and proof-use confirmation | do not authorize corpus population; only determine whether prerequisite evidence is now sufficient | R15 next-route token |
| Operator 2026-07-03 instruction | continue absorbing MinerU value toward a workflow-chain system, with live run later if needed | record operator intent as evidence, but do not treat it as runtime/live authorization | R15 proof-use and downstream-route discussion |

## Evidence Reuse And Encoding Plan

| Field | Value |
|---|---|
| verificationMode | REUSE_PRIOR_VERIFICATION |
| reusedEvidence | R12 policy, R13 qualification ledger, R14 route decision, and T11B evidence cited through R13 |
| priorVerificationArtifact | `docs/reference/CVF_MSEA_R13_T1_MINERU_LEGAL_POLICY_SAMPLE_CORPUS_CANDIDATE_QUALIFICATION_LEDGER_2026-07-03.md`; `docs/reference/CVF_MSEA_R14_MINERU_POST_SAMPLE_QUALIFICATION_ROUTE_DECISION_MATRIX_2026-07-03.md` |
| priorVerificationAnchor | R13 `## Source Verification Summary`; R14 `## Proof-Precondition Summary` |
| freshRecomputeRequired | NO |
| recomputeScope | worker may confirm governed artifact presence and output path absence only |
| unicodePathHandling | use literal paths and UTF-8-safe readers if a governed artifact is read; operator-local paths and Vietnamese filenames remain cited only through accepted governed artifacts; worker must not copy, normalize, or re-encode source files |
| extractedTextAuthority | AUXILIARY_ONLY |
| claimBoundary | evidence reuse only; no source import, file copy, hash recompute requirement, runtime/provider/live proof, or document-truth claim |

verificationMode: REUSE_PRIOR_VERIFICATION
priorVerificationArtifact: docs/reference/CVF_MSEA_R13_T1_MINERU_LEGAL_POLICY_SAMPLE_CORPUS_CANDIDATE_QUALIFICATION_LEDGER_2026-07-03.md and docs/reference/CVF_MSEA_R14_MINERU_POST_SAMPLE_QUALIFICATION_ROUTE_DECISION_MATRIX_2026-07-03.md
priorVerificationAnchor: R13 Source Verification Summary and R14 Proof-Precondition Summary
freshRecomputeRequired: NO
unicodePathHandling: use literal paths and UTF-8-safe readers for governed artifact reads; do not copy, normalize, or re-encode operator-local paths or Vietnamese filenames.
extractedTextAuthority: AUXILIARY_ONLY

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: this work order is a forward MSEA MinerU
sample-stressor provenance packet using accepted R12/R13/R14 owner surfaces.
It does not reopen legacy foundation-plane coverage, legacy workflow-chain
coverage, or the legacy absorption coverage index.

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| storageChange | NO_FOUNDATION_STORAGE_MUTATION |
| durableGovernanceFiles | none created, split, relocated, or refactored by the worker |
| generatedAggregateImpact | none; worker must not edit generated aggregates or session state |
| claimBoundary | workflow-chain wording is downstream intent only; no foundation storage layout, memory tier, runtime state, or production workflow-chain storage is authorized |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch author |
| Provider or surface | local workspace |
| Session or invocation | MSEA-R15 MinerU Sample Stressor Provenance Gap Closure dispatch, 2026-07-03 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | `rg`; `Test-Path`; `git`; `python governance/compat/build_dispatch_packet_scaffold.py`; `apply_patch`; governance gates |
| Target paths | this work order; paired GC-018 baseline |
| Allowed scope source | MSEA-R14 accepted route decision and operator 2026-07-03 continuation instruction |
| Before status evidence | HEAD `dd767187`; clean worktree; `git status --short` was empty before dispatch authoring |
| After status evidence | two new untracked dispatch artifacts only before pre-dispatch repair |
| Diff evidence | `git diff --name-status` for tracked diff plus `git status --short` for untracked dispatch artifacts |
| Approval boundary | dispatch packet authoring only |
| Claim boundary | no runtime/provider/live/corpus/source-import/schema/writer/adapter/checker/public/production claim |
| Agent type | dispatcher |
| Invocation ID | `msea-r15-mineru-sample-stressor-provenance-gap-closure-dispatch-2026-07-03` |
| Expected manifest | `docs/baselines/CVF_GC018_MSEA_R15_MINERU_SAMPLE_STRESSOR_PROVENANCE_GAP_CLOSURE_2026-07-03.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R15_MINERU_SAMPLE_STRESSOR_PROVENANCE_GAP_CLOSURE_2026-07-03.md` |
| Actual changed set | `docs/baselines/CVF_GC018_MSEA_R15_MINERU_SAMPLE_STRESSOR_PROVENANCE_GAP_CLOSURE_2026-07-03.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R15_MINERU_SAMPLE_STRESSOR_PROVENANCE_GAP_CLOSURE_2026-07-03.md` |
| Manifest delta | MATCH |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher_to_worker_to_reviewer_closer |
| phase | dispatch |
| baseHeadFor(phase) | dispatchBaseHead=dd767187; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | worker may create only the named worker return and companion ledger |
| traceScope(phase, actor) | worker records Agent Operation Trace Block in worker return and companion ledger |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer/closer owns material commit |
| crossBatchIsolation | MSEA-R15 only; clean worktree before authoring; no R14/R13/R12 artifact mutation by worker |
| nextMoveSurfaces | session-sync steward updates active session surfaces only after accepted material commit |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_MSEA_R15_MINERU_SAMPLE_STRESSOR_PROVENANCE_GAP_CLOSURE_COMPLETION_2026-07-03.md` (optional; prefer repairing evidence in the worker return per literal-format gotcha 30) |
| reviewerOwnedClosurePaths | worker return and companion ledger, plus optional completion review only if reviewer requires it |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| `docs/reviews/CVF_MSEA_R15_MINERU_SAMPLE_STRESSOR_PROVENANCE_GAP_CLOSURE_WORKER_RETURN_2026-07-03.md` | create worker return with source inventory, gap-closure findings, command evidence, no-commit statement, and required checker sections |
| `docs/reference/CVF_MSEA_R15_MINERU_SAMPLE_STRESSOR_PROVENANCE_GAP_CLOSURE_LEDGER_2026-07-03.md` | create companion ledger with candidate-group gap matrix, next-route token, derived-output rejection, downstream workflow-chain boundary, and claim boundary |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R15_MINERU_SAMPLE_STRESSOR_PROVENANCE_GAP_CLOSURE_WORKER_RETURN_2026-07-03.md`
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base dd767187 --head HEAD
python governance/compat/run_worker_return_fast_gate.py
git status --short
```

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | accepted MinerU source absorption and legal-policy sample-stressor evidence plus operator continuation intent -> MSEA-R15 provenance-gap closure ledger |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_corpus_completeness_report_integrity.py` |
| Owner surface | this work order and paired baseline |
| Disposition | ADAPT: convert accepted R12/R13/R14 evidence and current operator intent into a bounded gap-closure ledger without importing or executing documents |
| Claim boundary | dispatch-only; no runtime/provider/live/S3/RAG/Docker/package/checker/source-import/schema/receipt-writer/adapter implementation/public-sync/production claim |

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | accepted MSEA MinerU absorption evidence, governed LPCI legal-policy candidate evidence, and operator continuation intent; no source copy into this repository |
| Enumeration command | Not applicable to new filesystem enumeration; R15 consumes accepted governed artifacts only |
| Manifest artifact or inline manifest | R12 policy, R13 qualification ledger, R14 route-decision matrix |
| Processing ledger artifact or inline ledger | this work order and paired baseline |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, SKIPPED_WITH_REASON, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | MSEA-R12 policy; MSEA-R13 qualification; MSEA-R14 route decision |
| Unresolved items | actual gap-closure verdict remains worker output; downstream corpus/runtime/live work remains unresolved until later packets |
| Completion claim boundary | dispatch only; no corpus population, runtime execution, source import, provider/live proof, RAG write, schema/writer/adapter/checker work |

ledger_terminal=READ for accepted MSEA-R12/R13/R14 owner surfaces; ledger_terminal=ADAPTED for the gap-closure classification assignment; ledger_terminal=DEFERRED for corpus population, runtime/live proof, and workflow-chain execution; ledger_terminal=REJECTED for direct promotion of ungoverned derived outputs and implementation overclaims; ledger_terminal=NO_NEW_VALUE for already-owned sample policy and qualification facts.

## Corpus Completeness And Report Integrity

- Corpus task class: dispatch authoring for provenance-gap closure ledger.
- Corpus root: accepted MSEA MinerU absorption artifacts plus accepted LPCI sample-stressor qualification evidence.
- Snapshot time: 2026-07-03 dispatch authoring.
- Enumeration command: not applicable to new filesystem enumeration; R15 reads accepted governed artifacts only.
- Manifest artifact or inline manifest: R12 policy, R13 qualification ledger, and R14 route-decision matrix.
- Manifest hash: N/A with reason: this dispatch consumes governed artifacts, not a new file corpus.
- Processing ledger artifact or inline ledger: this work order and paired baseline.
- Allowed terminal statuses: READ | ADAPTED | DEFERRED | REJECTED | NO_NEW_VALUE | SKIPPED_WITH_REASON | BLOCKED_UNREADABLE.
- Reconciliation: manifest=R12/R13/R14 accepted artifacts; ledger_terminal=READ/ADAPTED/DEFERRED/REJECTED/NO_NEW_VALUE/SKIPPED_WITH_REASON/BLOCKED_UNREADABLE for dispatch scope; exclusions=corpus population, document import, MinerU runtime execution, provider/live proof, source import, schema implementation, receipt-writer code, adapter implementation, checker implementation, production-readiness claims; unresolved=0 for dispatch scope.
- Unresolved files: none for dispatch authoring.
- Declared exclusions: sample document import, corpus population, full body extraction, MinerU runtime, provider/live proof, RAG write, source import, schema implementation, receipt-writer code, adapter implementation, checker implementation, production-readiness claims.
- Unreadable or unsupported files: none identified for dispatch authoring.
- Aggregation check: accepted owner surfaces are cited instead of regenerated into a new corpus aggregate.
- Drift check: PASS for dispatch scope.
- Output traceability: this work order routes only to the two named worker-owned artifacts.
- Adversarial verification: dispatch rejects document-truth, extraction-accuracy, legal advice quality, current-law correctness, runtime behavior, live proof, and production readiness.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| R14 selected route | three provenance gaps must be closed before population | DOCTRINE_ADAPTED | R15 closure ledger | classify each gap by candidate group | no corpus population |
| R13 qualification ledger | two candidate groups partially ready pending operator confirmation, derived outputs rejected | DOCTRINE_ADAPTED | R15 closure ledger | evaluate only proof-grade source groups | no source import |
| Operator continuation intent | workflow-chain value target and later live-run willingness | DOCTRINE_ADAPTED | R15 proof-use discussion | determine what it does and does not close | no live run now |
| R9/R10 runtime/parser/RAG/provider holds | implementation lanes have concrete source-backed reopen conditions | RUNTIME_CANDIDATE | R15 downstream route section | keep held unless later condition is met | no runtime/provider/RAG action now |
| Checker lane | legal use case is high-risk for overclaims but no repeated checker miss is source-backed | CHECKER_CANDIDATE | R15 downstream route section | keep held unless later condition is met | no checker implementation |
| Ungoverned extracted text/rendered outputs | comparison evidence only | REJECT_DIRECT_IMPORT | R15 closure ledger | keep rejected | no source import |
| Existing MSEA evidence | already-owned MinerU absorption facts | NO_PACKAGE_OR_RUNTIME_VALUE | predecessor owner surfaces | cite only | no runtime/package behavior |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| R14 selected route | R14 route-decision matrix | CONFIRMED_EXISTING | converted into executable gap-closure worker assignment | cite and execute docs-only closure |
| R13 legal-policy qualification | R13 worker return and ledger | CONFIRMED_EXISTING | gap closure is evaluated after operator continuation intent | cite and classify |
| Operator workflow-chain intent | active operator instruction | ENRICH_EXISTING | adds proof-use direction but not runtime/live authorization | adapt cautiously |
| Direct corpus or runtime execution | no accepted current execution packet | REMOVED_OR_REJECTED | not authorized by R15 | reject |

## Rescan Intelligence Hardening

Original source artifact: `docs/reference/CVF_MSEA_R14_MINERU_POST_SAMPLE_QUALIFICATION_ROUTE_DECISION_MATRIX_2026-07-03.md`

Predecessor intake artifact: `docs/reference/CVF_MSEA_R13_T1_MINERU_LEGAL_POLICY_SAMPLE_CORPUS_CANDIDATE_QUALIFICATION_LEDGER_2026-07-03.md`

Delta ledger status: COMPLETE_WITH_DECLARED_EXCLUSIONS

Routing matrix status: REQUIRED_FOR_WORKER_OUTPUT

Semantic sampling status: REQUIRED_FOR_WORKER_OUTPUT

- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Delta category | R15 disposition |
|---|---|
| UNCHANGED_FROM_INTAKE | R12/R13/R14 owner surfaces remain accepted and unchanged |
| CHANGED_DISPOSITION | operator continuation intent is routed into gap-closure classification only |
| NEW_FINDING | no new source-file finding; gap-closure ledger is new doc-only synthesis |

### Follow-Up Routing Matrix

| Routing lane | R15 disposition |
|---|---|
| DO_NOW | provenance-gap closure worker return and companion ledger only |
| SEPARATE_RUNTIME_TRANCHE | runtime/provider/RAG/schema/writer/adapter/checker/live work remains parked |
| STRATEGIC_OPERATOR_DECISION | explicit operator detail remains required if worker cannot close permission/license or privacy/redaction from current evidence |
| OUT_OF_SCOPE | corpus population, runtime/live proof, schema/writer/adapter/checker work, and production workflow-chain claims |

### Sampling And Rejection Control

| Control | Disposition |
|---|---|
| REMOVED_OR_REJECTED | direct corpus population, runtime execution, live proof, and ungoverned derived outputs remain rejected for this dispatch |
| RESOLVED_BY_DESIGN | this dispatch permits classification of the three R14 gaps only, with a held token available when evidence remains insufficient |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge |
|---|---|---|---|---|
| R15-S1 | MSEA-R14 `## Proof-Precondition Summary` | three gaps must close before downstream work | route-to-gap mapping | operator's broad workflow-chain intent could be overread as live-run authorization |
| R15-S2 | MSEA-R13 `## Rejected Derived Output Boundary` | nine derived outputs are rejected for direct promotion | rejection carry-forward | worker may be tempted to use prior extracted text as sample material |
| R15-S3 | MSEA-R12 `## Held-Lane Reopen Routing` | sample corpus population still needs a fresh GC-018 | downstream hold | gap closure does not itself authorize document import |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | MSEA-R15 provenance-gap closure dispatch |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, mandatory-wrapper, provider, parser, adapter, schema, receipt-writer, or production behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created or consumed |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime action is executed or observed |
| invocationBoundary | local governed documentation dispatch only |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, CLI, MCP, Web runtime, adapter, package, watcher, daemon, parser, RAG index, or production route interception claim |
| claimLanguage | provenance-gap closure dispatch and source-backed non-claim boundary only |
| forbiddenExpansion | no sample document import, corpus population, MinerU runtime, install, model download, parser/OCR/VLM/hybrid/API/router/Gradio/Docker execution, provider/live call, credentials/S3, RAG write, source import, package activation, checker implementation, public-sync, Web/MCP/model-router/action-authority, automatic invocation, benchmark, document-truth, extraction-accuracy, legal advice quality, current-law correctness, schema implementation, receipt-writer code, adapter implementation, or production-readiness claim |

## Claim Boundary

This work order authorizes only worker creation of the two named
provenance-gap closure artifacts. It does not close any gap by dispatch text
alone, does not import or copy any document, does not populate a sample
corpus, does not execute MinerU or any provider/live proof, does not implement
schema/writer/adapter/checker code, does not create a legal-domain product
lane, and does not claim document truth, extraction accuracy, legal advice
quality, current-law correctness, benchmark value, workflow-chain production
readiness, or universal document intelligence.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch using operator-local legal-policy data
references; no public-sync authorization.
