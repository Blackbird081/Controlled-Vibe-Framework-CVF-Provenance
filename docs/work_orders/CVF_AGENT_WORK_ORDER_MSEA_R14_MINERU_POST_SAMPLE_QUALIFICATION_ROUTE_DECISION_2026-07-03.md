# CVF Agent Work Order - MSEA-R14 MinerU Post Sample Qualification Route Decision

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

docType: work_order

Date: 2026-07-03

Batch ID: MSEA-R14

Dispatch base head: 68a3a809

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker role

Reviewer/closer: reviewer/closer

Worker return path: `docs/reviews/CVF_MSEA_R14_MINERU_POST_SAMPLE_QUALIFICATION_ROUTE_DECISION_WORKER_RETURN_2026-07-03.md`

## Dispatch Prompt Envelope

Role: delegated worker for MSEA-R14.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R14_MINERU_POST_SAMPLE_QUALIFICATION_ROUTE_DECISION_2026-07-03.md`

Paired GC-018 baseline:
`docs/baselines/CVF_GC018_MSEA_R14_MINERU_POST_SAMPLE_QUALIFICATION_ROUTE_DECISION_2026-07-03.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: artifact date is 2026-07-03. Treat relative dates as
unsafe; record concrete dates in the worker return.

Do-not-misread notes: this is route decision only. It does not authorize
operator-confirmation collection, sample document import, corpus population,
MinerU runtime, OCR/parser/VLM execution, provider/live proof, RAG write,
schema implementation, receipt-writer code, checker implementation, adapter
implementation, public-sync, legal-domain product work, document-truth,
extraction-accuracy, current-law correctness, legal advice quality, or
production-readiness claims.

Required first actions: read `CVF_SESSION_MEMORY.md`,
`CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`,
`CVF_SESSION/ACTIVE_SESSION_STATE.json`, `AGENT_HANDOFF_V33_2026-07-03.md`,
`docs/reference/guard_orientation/README.md`,
`docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`,
this work order, the paired GC-018 baseline, all Source Verification Block
owner surfaces, and every checker source listed below before writing worker
outputs.

Return contract: create the worker return artifact and companion
route-decision matrix, run required gates, leave changes uncommitted, and
return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Create a CVF-owned route-decision matrix that decides the next MinerU
absorption route after the accepted R12 sample-corpus policy and accepted R13
legal-policy sample-stressor qualification.

The worker must choose exactly one route token from the allowed list, explain
why the other tokens are not selected, and keep route execution out of scope.

## Authority Chain

| Authority | Evidence |
|---|---|
| Operator request | operator accepted option 1 on 2026-07-03 after discussing next route after R13 |
| Active session state | mode routes to next MinerU route decision after MSEA-R13-T1 acceptance |
| Accepted sample policy | `docs/reference/CVF_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_2026-07-03.md` |
| Accepted legal-policy qualification | R13 worker return and qualification ledger cited in the Source Verification Block |
| Held-lane predecessors | MSEA-R9/R10 route and adapter-contract evidence cited in the Source Verification Block |
| Paired baseline | `docs/baselines/CVF_GC018_MSEA_R14_MINERU_POST_SAMPLE_QUALIFICATION_ROUTE_DECISION_2026-07-03.md` |

## Agent Roles

| Role | Assignment | Boundary |
|---|---|---|
| Dispatcher | dispatch author | authors and commits dispatch packet only |
| Worker | delegated worker role | creates pending worker return and companion route-decision matrix only |
| Reviewer/closer | reviewer/closer role | reviews, repairs allowed-scope defects, commits material if accepted |
| Operator | operator | required for proof-use confirmation, privacy/redaction decisions, route execution, runtime execution, public-sync, or implementation-facing lanes |

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
| 8 | `docs/reference/CVF_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_2026-07-03.md` |
| 9 | R13 worker return and qualification ledger |
| 10 | MSEA-R9/R10 held-lane evidence cited in Source Verification |
| 11 | checker source listed in the dispatch and worker-output read-ahead blocks |

## Pre-Flight Checks

| Check | Command or evidence |
|---|---|
| Capture base | `git rev-parse --short HEAD` |
| Capture worktree | `git status --short` |
| Confirm output paths absent | `Test-Path` for named worker return and route-decision matrix |
| Confirm accepted owner surfaces exist | `Test-Path` for R12, R13, R9, and R10 owner surfaces |
| Read output checkers | worker records checker paths and literal tokens before writing outputs |

## Write Ownership

| Actor | Owned paths |
|---|---|
| Worker | `docs/reviews/CVF_MSEA_R14_MINERU_POST_SAMPLE_QUALIFICATION_ROUTE_DECISION_WORKER_RETURN_2026-07-03.md`; `docs/reference/CVF_MSEA_R14_MINERU_POST_SAMPLE_QUALIFICATION_ROUTE_DECISION_MATRIX_2026-07-03.md` |
| Reviewer/closer | allowed-scope repair to worker-owned material artifacts and optional completion review only if required |
| Session-sync steward | active session and handoff surfaces only after accepted material commit |

Forbidden worker changes:

- any legal-policy sample document, external bundle, source mirror, external
  repository clone, legacy folder, package/runtime/checker file, generated
  aggregate, public-sync file, Web/MCP/model-router file, session state,
  handoff, or active front-door file;
- operator-confirmation collection, privacy/redaction adjudication, permission
  or license decision, sample document import, corpus population, schema
  implementation, receipt-writer code, adapter code, tests that imply runtime
  behavior, provider/live proof, S3 credentials, Docker build/run, RAG index
  write, package activation, or production-readiness evidence.

## Review Gate

Reviewer/closer must run worker-return fast gate and reviewer-return steward
preflight before accepting material closure. Worker output with failed required
gates must be repaired in allowed scope or returned as `BLOCKED_WITH_REASON`.

## Worker Autonomy / No-Question Rule

Worker must repair allowed-scope checker failures directly by reading the
failing checker source and matching the literal required shape. Worker should
return to orchestrator only for a source contradiction, missing owner surface,
forbidden-scope need, or missing authority that makes completion impossible.

Worker must not ask the operator which route to choose. The task is to decide
from source evidence. If source evidence cannot support any open route, select
a HOLD token and explain the blocking condition.

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intakeRole | DISPATCHER_TO_WORKER |
| workerRole | delegated worker |
| reviewerRole | reviewer/closer |
| commitMode | WORKER_MUST_NOT_COMMIT |
| risk sensitivity | bounded governance route decision; no document content, runtime, provider, public, or legal-advice execution |
| selected role route | dispatcher_to_worker_to_reviewer_closer |
| canonical route mode | SINGLE_AGENT_SINGLE_ROLE |
| routingDecision | worker performs route-decision analysis only and returns uncommitted artifacts |
| escalationRule | return `BLOCKED_WITH_REASON` only for source contradiction, missing owner surface, forbidden-scope need, or missing authority |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R14 --title "MinerU Post Sample Qualification Route Decision" --date 2026-07-03 --base 68a3a809 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Replaced placeholders with MSEA-R12/R13 accepted evidence, MSEA-R9/R10 held-lane conditions, route-token selection instructions, and no-execution boundaries. |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_rescan_intelligence_hardening.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_adif_defect_registry_disclosure.py` |
| docOnlyNewFields | post-sample route token; route-decision matrix; loser-route rationale; proof-precondition summary |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |

## Execution Plan

1. Capture `executionBaseHead` and clean worktree evidence.
2. Read all startup, source authority, and checker files required above.
3. Confirm planned output paths are absent.
4. Build a matrix over every allowed route token using R12/R13/R9/R10 evidence.
5. Select exactly one route token and record why every other token is not selected.
6. Create only the worker return and companion route-decision matrix.
7. Run required gates, record command evidence, and leave the work uncommitted.

## Evidence Requirements

| Evidence class | Required proof |
|---|---|
| source ownership | cite R12 policy, R13 worker return and ledger, and R9/R10 held-lane surfaces |
| route selection | one selected route token plus loser-route rationale for every other token |
| no execution | `git diff --name-status` and `git status --short` evidence showing only worker-owned artifacts |
| checker read-ahead | worker return records checker source and literal tokens reviewed before writing outputs |
| no commit | No-Commit Statement uses `WORKER_MUST_NOT_COMMIT honored` |

## Closure Checklist

| Item | Required disposition |
|---|---|
| selected route token present | checked, or `BLOCKED_WITH_REASON` |
| all non-selected tokens classified | checked, or `BLOCKED_WITH_REASON` |
| worker-owned paths only | checked by changed-file evidence |
| required gates recorded | checked, or blocked with command output |
| no forbidden claim retained | checked by claim-boundary sections |
| no commit/stage/push by worker | checked by git evidence |

## Operator Checkpoint

No operator checkpoint is required during worker execution. Operator input is
reserved for a later selected-route packet if R14 selects a route that needs
permission/license confirmation, privacy/redaction disposition, proof-use
confirmation, runtime authorization, public-sync, or implementation authority.

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
| literalTokensReviewed | Dispatch Prompt Envelope; Status: DISPATCH_READY; Source Verification Block columns; ACCEPT; REJECT; BLOCKED_SOURCE_NOT_FOUND; Roadmap-to-Work-Order Trace Matrix; Negative Search And Collision Discipline; Agent Handoff Contract Control Block; Reviewer Closure Conversion; WORKER_MUST_NOT_COMMIT; WORKER_RETURN_FULL_GATE_V1; CHECKER_SAFE_SKELETON_REQUIRED; External Knowledge Intake Routing field labels; external repo or copied folder; External Absorption Core field labels; ledger_terminal=; DOCTRINE_ADAPTED, RUNTIME_CANDIDATE, CHECKER_CANDIDATE, REJECT_DIRECT_IMPORT, NO_PACKAGE_OR_RUNTIME_VALUE; Corpus verdict bullet; Rescan intelligence verdict; Delta Execution Claim Boundary Control Block fields; DEFERRED_PRIVATE_ONLY |
| gateRunPurpose | Confirmation evidence after dispatcher checker read-ahead; not first discovery. |
| claimBoundary | Read-ahead covers this dispatch packet only. Worker-created review/reference outputs must perform their own checker-source read-ahead by docType before writing. |

## Worker Output Checker Read-Ahead Mandate

Before writing the worker return or companion matrix, worker must read the
checker source as applied to each output file's docType, path family, and
conditional content class.

| Output artifact | Required checker source read-ahead before writing |
|---|---|
| Worker return under the reviews area | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_rescan_intelligence_hardening.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_agent_operation_trace.py` |
| Reference matrix under the reference area | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_rescan_intelligence_hardening.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_agent_operation_trace.py` |

The worker return must state that this read-ahead happened before writing the
outputs, list exact literal headings/tokens reviewed, and use gate runs as
confirmation evidence, not first discovery.

## Route Selection Instructions

Worker must select exactly one token from this table.

| Route token | Select only if source evidence proves |
|---|---|
| `OPEN_SAMPLE_STRESSOR_PROVENANCE_GAP_CLOSURE` | R13 remains accepted; at least one legal-policy candidate group remains useful as a MinerU sample stressor; the only immediate gaps are operator permission/license, privacy/redaction, and proof-use confirmation |
| `OPEN_SAMPLE_CORPUS_POPULATION_POLICY_AFTER_GAP_CLOSURE` | source evidence proves the R13 provenance gaps are already closed by a governed artifact; if not, do not select |
| `OPEN_RECEIPT_SCHEMA_OR_WRITER_READINESS_ROADMAP` | source evidence proves schema/writer readiness can be planned without corpus population, runtime proof, or adapter implementation |
| `OPEN_LOCAL_PARSER_RUNTIME_PILOT_ROADMAP` | source evidence proves a concrete downstream MinerU parsing use case and authorizes planning only, not runtime execution |
| `RETURN_TO_MINERU_ADAPTER_READINESS_ROUTE` | sample-stressor route no longer has near-term value and adapter-contract readiness is the best source-backed next docs route |
| `HOLD_SAMPLE_STRESSOR_LANE_PENDING_OPERATOR_INPUT` | the legal-policy sample route is still plausible but requires operator input before any next work order can be source-backed |
| `HOLD_ALL_IMPLEMENTATION_LANES` | no route has source-backed next value under current boundaries |

Expected default: choose `OPEN_SAMPLE_STRESSOR_PROVENANCE_GAP_CLOSURE` if the
R13 acceptance remains current and no source evidence closes the three gaps.
This is still documentation/governance work only; it is not permission capture,
privacy adjudication, proof-use confirmation, corpus population, or runtime.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| MSEA-R12-T1 is an active sample-corpus and expected-receipt policy reference | VALUE_SET | `docs/reference/CVF_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_2026-07-03.md` | `Status: ACTIVE_REFERENCE`; `## Purpose`; `## Scope / Applies To` | ACTIVE_REFERENCE | MSEA-R12-T1 policy reference | ACCEPT |
| R12-T1 requires explicit permission/license, privacy/redaction, slot assignment, format/size, and proof-use confirmation before corpus population | VALUE_SET | `docs/reference/CVF_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_2026-07-03.md` | `## Sample Intake And Provenance Policy`; `## Operator Handoff Requirements` | Sample Intake And Provenance Policy | MSEA-R12-T1 policy reference | ACCEPT |
| R13-T1 qualifies Candidate Group A and Candidate Group B as partially ready pending operator confirmation | VALUE_SET | `docs/reference/CVF_MSEA_R13_T1_MINERU_LEGAL_POLICY_SAMPLE_CORPUS_CANDIDATE_QUALIFICATION_LEDGER_2026-07-03.md` | `## Sample Intake Provenance Gap Matrix`; `## MinerU Route Implication` | PARTIALLY_READY_PENDING_OPERATOR_CONFIRMATION | MSEA-R13-T1 qualification ledger | ACCEPT |
| R13-T1 rejects the nine ungoverned derived outputs for direct promotion | VALUE_SET | `docs/reference/CVF_MSEA_R13_T1_MINERU_LEGAL_POLICY_SAMPLE_CORPUS_CANDIDATE_QUALIFICATION_LEDGER_2026-07-03.md` | `## Rejected Derived Output Boundary`; `## MinerU Route Implication` | NOT_READY | MSEA-R13-T1 qualification ledger | ACCEPT |
| R13-T1 recommends operator provenance-gap closure before corpus population | VALUE_SET | `docs/reviews/CVF_MSEA_R13_T1_MINERU_LEGAL_POLICY_SAMPLE_CORPUS_CANDIDATE_QUALIFICATION_WORKER_RETURN_2026-07-03.md` | `## Decision / Recommendation`; `## Claim Boundary` | operator provenance-gap closure | MSEA-R13-T1 worker return | ACCEPT |
| R9 held runtime, provider, RAG, S3, Docker, and checker lanes behind concrete reopen conditions | VALUE_SET | `docs/reference/CVF_MSEA_R9_MINERU_CVF_APPLICATION_BLUEPRINT_AND_ADAPTER_CONTRACT_READINESS_2026-07-02.md` | route-decision and held-lane sections | held-lane routing | MSEA-R9 route matrix | ACCEPT |
| R10 adapter contract draft keeps runtime, schema, writer, adapter, and public-sync authorization false | VALUE_SET | `docs/reference/CVF_MSEA_R10_MINERU_ADAPTER_CONTRACT_DRAFT_2026-07-03.md` | contract metadata and claim-boundary sections | runtimeExecutionAuthorized | MSEA-R10 contract draft | ACCEPT |
| Worker-return full-gate profile is a dispatch-quality recognized contract | EXISTS | `governance/compat/check_work_order_dispatch_quality.py` | `WORKER_RETURN_FULL_GATE_PROFILE`; `WORKER_RETURN_FULL_GATE_REQUIRED_TERMS` | WORKER_RETURN_FULL_GATE_V1 | work-order dispatch-quality checker | ACCEPT |
| WORKER_MUST_NOT_COMMIT requires handoff control and reviewer conversion | EXISTS | `governance/compat/check_agent_handoff_boundary.py` | `REVIEWER_CONVERSION`; `WORKER_MUST_NOT_COMMIT` | Agent Handoff Contract Control Block | handoff boundary checker | ACCEPT |

## New Doc-Only Fields

| Field | Required worker treatment |
|---|---|
| post-sample route token | select exactly one allowed token |
| route-decision matrix | compare all allowed route tokens against source-backed preconditions |
| loser-route rationale | record why each non-selected token is not selected |
| proof-precondition summary | list what a later selected-route work order would need before execution |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| Baseline path existence before authoring | `Test-Path` returned `False` for the paired baseline path | PASS |
| Work-order path existence before authoring | `Test-Path` returned `False` for this work-order path | PASS |
| Planned worker-return path existence before authoring | `Test-Path` returned `False` for the planned worker-return path | PASS |
| Planned matrix path existence before authoring | `Test-Path` returned `False` for the planned route-decision matrix path | PASS |
| Collision search for R14 dispatch tokens | search roots: `docs/baselines docs/work_orders docs/reviews docs/reference docs/roadmaps CVF_SESSION`; search query used the R14 batch and title tokens; result: ZERO_R14_ARTIFACT_COLLISION before authoring | PASS |
| Generic token collision coverage | tokens `DOC`, `literalTokensReviewed`, `CHECKER_SAFE_SKELETON`, `WORKER_MUST_NOT_COMMIT`, and `WORKER_RETURN_FULL_GATE_V1` are generic governance/checker vocabulary with repo-local non-authoritative occurrences | PASS |
| Collision decision | No existing R14 artifact found; dispatch path is new | DISPATCH_ALLOWED |

## Roadmap-to-Work-Order Trace Matrix

| Requirement source | Requirement | Work-order instruction | Worker output evidence |
|---|---|---|---|
| R12-T1 Sample Intake And Provenance Policy | sample corpus work needs permission/license, privacy/redaction, slot assignment, format/size, and proof-use confirmation | compare post-R13 evidence against these preconditions | R14 route-decision matrix |
| R13-T1 Candidate Qualification | legal-policy candidate groups are partially ready but have three operator-owned gaps | decide whether the next route should close those gaps or hold the lane | R14 selected route token |
| R9/R10 held-lane routing | implementation-facing lanes require concrete reopen conditions and fresh GC-018 | keep runtime/provider/RAG/S3/Docker/checker/adapter lanes held unless a source-backed condition is met | loser-route rationale |
| Active session next move | operator chooses next MinerU route after R13 | create route-decision worker return only | worker return |
| MSEA claim boundary | no runtime, source import, corpus population, or production claim | require no-execution route decision | claim boundary sections |

## Required Worker Outputs

Worker must create exactly these two artifacts:

| Artifact | Required status | Required role |
|---|---|---|
| `docs/reviews/CVF_MSEA_R14_MINERU_POST_SAMPLE_QUALIFICATION_ROUTE_DECISION_WORKER_RETURN_2026-07-03.md` | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` | worker return |
| `docs/reference/CVF_MSEA_R14_MINERU_POST_SAMPLE_QUALIFICATION_ROUTE_DECISION_MATRIX_2026-07-03.md` | `ACTIVE_REFERENCE` or `BLOCKED_REFERENCE_WITH_REASON` | route-decision matrix |

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py --base <executionBaseHead> --head HEAD`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Minimum required sections:

- Checker Source Read-Ahead Block
- Source Inventory
- Purpose
- Target / Source
- Scope / Methodology
- Findings / Position
- Risk / Corrective Action
- Decision / Recommendation
- External Knowledge Intake Routing
- External Absorption Core
- External Absorption Value Conversion Matrix
- Overlap And Novelty Classification
- Corpus Completeness And Report Integrity
- Rescan Intelligence Hardening
- Delta Execution Claim Boundary Control Block
- Agent Operation Trace Block
- Git Status Short
- Changed Files
- Command Evidence
- No-Commit Statement
- Finding-To-Governance Learning Disposition
- Claim Boundary

The companion reference matrix must include `## Purpose`, `## Scope / Applies
To`, route-token comparison, source-backed selected route, non-selected route
rationale, external absorption blocks, corpus completeness block, rescan
hardening block, delta boundary block, and claim boundary.

## Evidence Reuse And Encoding Plan

verificationMode: REUSE_PRIOR_VERIFICATION
priorVerificationArtifact: docs/reference/CVF_MSEA_R13_T1_MINERU_LEGAL_POLICY_SAMPLE_CORPUS_CANDIDATE_QUALIFICATION_LEDGER_2026-07-03.md
priorVerificationAnchor: R13 qualification rows plus R12 sample policy and R9/R10 held-lane evidence
freshRecomputeRequired: NO
unicodePathHandling: use literal paths or UTF-8-safe readers if existing source filenames must be cited; do not open or import legal-policy sample files
extractedTextAuthority: AUXILIARY_ONLY

| Field | Value |
|---|---|
| verificationMode | REUSE_PRIOR_VERIFICATION |
| Prior verification mode | REUSE_PRIOR_VERIFICATION; no new hash, document read, or filesystem enumeration required |
| Prior evidence sources | MSEA-R12/R13 plus MSEA-R9/R10 owner surfaces cited in Source Verification |
| Recompute requirement | none for sample files; worker may confirm owner-surface paths exist |
| unicodePathHandling | Use literal paths or UTF-8-safe readers if existing source filenames must be cited; use ASCII route labels in new prose |
| extractedTextAuthority | AUXILIARY_ONLY |
| Claim boundary | reused evidence supports route decision only; it does not prove document truth, extraction accuracy, legal advice quality, runtime behavior, or corpus readiness |

## Legacy Absorption Coverage Index Disposition

| Field | Disposition |
|---|---|
| Applicability | NOT_APPLICABLE_WITH_REASON: this route-decision dispatch does not reopen a legacy coverage index item |
| Coverage index row evidence | N/A with reason: no legacy coverage row is accepted, modified, or closed by this dispatch |
| Claim boundary | no legacy copied folder, historical adapter, or prior absorption source is promoted to current authority |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Storage layout change | NOT_APPLICABLE_WITH_REASON: dispatch creates documentation packets only |
| Durable governance foundation file change | none authorized for worker |
| Generated aggregate change | none authorized for worker |
| External bundle storage | no copy/import/move/write authorized |
| Claim boundary | no corpus storage, source import, generated aggregate mutation, RAG index, S3, package, runtime storage, or production storage claim |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | accepted MinerU source absorption and legal-policy sample-stressor evidence -> R14 route-decision matrix |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_corpus_completeness_report_integrity.py` |
| Owner surface | this work order |
| Disposition | ADAPT: convert R12/R13 sample-stressor evidence into a next-route decision without executing any route |
| Claim boundary | dispatch-only; no runtime/provider/live/S3/RAG/Docker/package/checker/source-import/schema/receipt-writer/adapter implementation/public-sync/production claim |

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | accepted MSEA MinerU absorption evidence and governed LPCI legal-policy candidate evidence; no source copy into this repository |
| Enumeration command | Not applicable to new filesystem enumeration; R14 consumes accepted governed artifacts only |
| Manifest artifact or inline manifest | `docs/reference/CVF_MSEA_R13_T1_MINERU_LEGAL_POLICY_SAMPLE_CORPUS_CANDIDATE_QUALIFICATION_LEDGER_2026-07-03.md`; `docs/reference/CVF_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_2026-07-03.md` |
| Processing ledger artifact or inline ledger | this work order |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, SKIPPED_WITH_REASON, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | MSEA-R12 policy; MSEA-R13 qualification; MSEA-R9/R10 held-lane evidence |
| Unresolved items | route execution remains unresolved until a selected next-route work order is separately authored |
| Completion claim boundary | dispatch only; no corpus population, runtime execution, source import, provider/live proof, RAG write, schema/writer/adapter/checker work |

ledger_terminal=READ for accepted MSEA-R9/R10/R12/R13 owner surfaces; ledger_terminal=ADAPTED for route-decision conversion; ledger_terminal=DEFERRED for all route execution; ledger_terminal=REJECTED for direct promotion of ungoverned derived outputs and implementation overclaims; ledger_terminal=NO_NEW_VALUE for already-owned sample policy and qualification facts.

## Corpus Completeness And Report Integrity

- Corpus task class: dispatch authoring for post-sample route decision.
- Corpus root: accepted MSEA MinerU absorption artifacts plus accepted LPCI sample-stressor qualification evidence.
- Snapshot time: 2026-07-03 dispatch authoring.
- Enumeration command: not applicable to new filesystem enumeration; R14 reads accepted governed artifacts only.
- Manifest artifact or inline manifest: R12 policy and R13 qualification ledger.
- Manifest hash: N/A with reason: route decision consumes governed artifacts, not a new file corpus.
- Processing ledger artifact or inline ledger: this work order.
- Allowed terminal statuses: READ | ADAPTED | DEFERRED | REJECTED | NO_NEW_VALUE | SKIPPED_WITH_REASON | BLOCKED_UNREADABLE.
- Reconciliation: manifest=R12/R13 accepted artifacts plus R9/R10 held-lane evidence; ledger_terminal=READ/ADAPTED/DEFERRED/REJECTED/NO_NEW_VALUE/SKIPPED_WITH_REASON/BLOCKED_UNREADABLE for dispatch scope; exclusions=corpus population, document import, MinerU runtime execution, provider/live proof, source import, schema implementation, receipt-writer code, adapter implementation, checker implementation, production-readiness claims; unresolved=0 for dispatch scope.
- Unresolved files: none for dispatch authoring.
- Declared exclusions: sample document import, corpus population, full body extraction, MinerU runtime, provider/live proof, RAG write, source import, schema implementation, receipt-writer code, adapter implementation, checker implementation, production-readiness claims.
- Unreadable or unsupported files: none identified for dispatch authoring.
- Aggregation check: accepted owner surfaces are cited instead of regenerated into a new corpus aggregate.
- Drift check: PASS for dispatch scope.
- Output traceability: this work order routes only to the two named worker outputs.
- Adversarial verification: dispatch rejects document-truth, extraction-accuracy, legal advice quality, current-law correctness, runtime behavior, and production readiness.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| R12-T1 sample-corpus policy | gap-closure prerequisites before sample corpus population | DOCTRINE_ADAPTED | R14 route-decision matrix | decide whether to open gap-closure route | no corpus population |
| R13-T1 qualification ledger | two candidate groups partially ready pending operator confirmation, derived outputs rejected | DOCTRINE_ADAPTED | R14 route-decision matrix | select route token | no source import |
| R9/R10 runtime/parser/RAG/provider holds | implementation lanes have concrete source-backed reopen conditions | RUNTIME_CANDIDATE | R14 loser-route rationale | keep held unless condition met | no runtime/provider/RAG action now |
| Checker lane | legal use case is high-risk for overclaims but no repeated checker miss is source-backed | CHECKER_CANDIDATE | R14 loser-route rationale | keep held unless R9 condition met | no checker implementation |
| Ungoverned extracted text/rendered outputs | comparison evidence only | REJECT_DIRECT_IMPORT | R14 route-decision matrix | do not promote | no source import |
| Existing MSEA evidence | already-owned MinerU absorption facts | NO_PACKAGE_OR_RUNTIME_VALUE | predecessor owner surfaces | cite only | no runtime/package behavior |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| R12-T1 sample policy | R12 policy reference | CONFIRMED_EXISTING | now used as route-selection criterion | cite |
| R13-T1 legal-policy qualification | R13 worker return and ledger | CONFIRMED_EXISTING | route decision after qualification | cite and classify |
| R9/R10 held implementation lanes | R9 route matrix and R10 adapter draft | CONFIRMED_EXISTING | check whether R13 changes any reopen condition | classify and defer if not met |
| Direct route execution | no accepted current route-execution packet | REMOVED_OR_REJECTED | not authorized by R14 | reject |

## Rescan Intelligence Hardening

Original source artifact: `docs/reference/CVF_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_2026-07-03.md`

Predecessor intake artifact: `docs/reference/CVF_MSEA_R13_T1_MINERU_LEGAL_POLICY_SAMPLE_CORPUS_CANDIDATE_QUALIFICATION_LEDGER_2026-07-03.md`

Delta ledger status: COMPLETE_WITH_DECLARED_EXCLUSIONS

Routing matrix status: REQUIRED_FOR_WORKER_OUTPUT

Semantic sampling status: REQUIRED_FOR_WORKER_OUTPUT

- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Delta category | R14 disposition |
|---|---|
| UNCHANGED_FROM_INTAKE | R12 policy and R13 qualification remain accepted owner surfaces |
| CHANGED_DISPOSITION | route execution is rejected by this dispatch and converted into decision-only analysis |
| NEW_FINDING | no new source file finding; route-token matrix is new doc-only synthesis |

### Follow-Up Routing Matrix

| Routing lane | R14 disposition |
|---|---|
| DO_NOW | route-decision worker return and companion matrix only |
| SEPARATE_RUNTIME_TRANCHE | runtime/provider/RAG/schema/writer/adapter/checker work remains parked |
| STRATEGIC_OPERATOR_DECISION | later operator confirmation may be needed by the selected next-route packet |
| OUT_OF_SCOPE | direct implementation-route execution without fresh GC-018 is REMOVED_OR_REJECTED |
| RESOLVED_BY_DESIGN | R14 handles route selection by matrix rather than reopening source absorption |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge |
|---|---|---|---|---|
| R14-S1 | R13 MinerU Route Implication | sample stressor has provenance gaps | DEFERRED | do not treat partial readiness as corpus authorization |
| R14-S2 | R9/R10 held lanes | runtime and adapter lanes remain held | REMOVED_OR_REJECTED | do not reopen implementation lanes by implication |
| R14-S3 | R12 Scope / Applies To | policy does not create sample files | UNCHANGED_FROM_INTAKE | do not claim corpus population |

## KIOD Runtime-Candidate Parking Checks

| Candidate | Parking decision | Reason |
|---|---|---|
| runtime/provider/live proof | PARKED | no concrete source-backed runtime governance behavior claim is authorized by R14 |
| parser/OCR/VLM execution | PARKED | R14 is route decision only |
| RAG/index/write path | PARKED | no RAG use-case reopen condition is source-backed |
| schema/writer/adapter implementation | PARKED | R10 keeps these authorization flags false until later packet |
| checker implementation | PARKED | no repeated overclaim miss or authorized checker lane exists |

## Agent Handoff Contract Control Block

| Field | Value |
|---|---|
| routeToken | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher -> delegated worker -> reviewer/closer |
| commitMode | WORKER_MUST_NOT_COMMIT |
| contractSource | archive-qualified standard exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| baseHeadFor(phase) | dispatchBaseHead=68a3a809; worker must capture executionBaseHead at start; reviewer must capture closureBaseHead before reviewer conversion |
| changedSetScope(phase) | worker may create only the named worker return and companion route-decision matrix |
| traceScope(phase, actor) | worker return must include Agent Operation Trace Block and clean-worktree/no-commit evidence |
| commitOwner(phase) | reviewer/closer owns material commit when worker return is accepted; session-sync steward owns session-sync commit after that material commit |
| crossBatchIsolation | R14 must not modify R12/R13 accepted artifacts, R9/R10 artifacts, runtime source, source mirror, corpus files, session state, or public-sync surfaces |
| nextMoveSurfaces | reviewer/closer updates next-move surfaces only when material acceptance is committed |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_MSEA_R14_MINERU_POST_SAMPLE_QUALIFICATION_ROUTE_DECISION_COMPLETION_REVIEW_2026-07-03.md` if reviewer needs a separate closure packet; otherwise reviewer may convert the worker return directly |
| reviewerOwnedClosurePaths | worker return, companion route-decision matrix, optional completion review, and session-sync surfaces following material commit |
| conversionRule | Worker leaves artifacts uncommitted. Reviewer may repair allowed-scope format defects, run gates, commit accepted material, then run session-sync as a separate commit. |

## Delta Execution Claim Boundary Control Block

Delta execution claim boundary: REQUIRED

| Field | Value |
|---|---|
| claimScope | route-decision dispatch only |
| claimDisposition | CLAIM_REJECTED for execution-control behavior; documentation-only dispatch is bounded by source evidence |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT for runtime behavior; this work order and paired baseline are documentation receipts only |
| actionEvidence | CLAIM_REJECTED_NO_ACTION for runtime behavior; no runtime action authorized |
| invocationBoundary | no automatic invocation, parser call, provider call, RAG write, or adapter execution |
| interceptionBoundary | no production control or runtime governance interception claim |
| claimLanguage | selected route is a governance recommendation, not an executed lane |
| forbiddenExpansion | no corpus population, source import, runtime/provider/live/public/Web/MCP/package/model-router/action-authority implementation |

## Verification Commands

Worker must run:

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/check_worker_return_quality_gate.py --paths docs/reviews/CVF_MSEA_R14_MINERU_POST_SAMPLE_QUALIFICATION_ROUTE_DECISION_WORKER_RETURN_2026-07-03.md
python governance/compat/check_markdown_structural_completeness.py --paths docs/reviews/CVF_MSEA_R14_MINERU_POST_SAMPLE_QUALIFICATION_ROUTE_DECISION_WORKER_RETURN_2026-07-03.md docs/reference/CVF_MSEA_R14_MINERU_POST_SAMPLE_QUALIFICATION_ROUTE_DECISION_MATRIX_2026-07-03.md
python governance/compat/check_governed_artifact_checker_read_ahead.py --paths docs/reviews/CVF_MSEA_R14_MINERU_POST_SAMPLE_QUALIFICATION_ROUTE_DECISION_WORKER_RETURN_2026-07-03.md docs/reference/CVF_MSEA_R14_MINERU_POST_SAMPLE_QUALIFICATION_ROUTE_DECISION_MATRIX_2026-07-03.md
python governance/compat/check_external_knowledge_intake_routing.py --paths docs/reviews/CVF_MSEA_R14_MINERU_POST_SAMPLE_QUALIFICATION_ROUTE_DECISION_WORKER_RETURN_2026-07-03.md docs/reference/CVF_MSEA_R14_MINERU_POST_SAMPLE_QUALIFICATION_ROUTE_DECISION_MATRIX_2026-07-03.md
python governance/compat/check_external_absorption_core.py --paths docs/reviews/CVF_MSEA_R14_MINERU_POST_SAMPLE_QUALIFICATION_ROUTE_DECISION_WORKER_RETURN_2026-07-03.md docs/reference/CVF_MSEA_R14_MINERU_POST_SAMPLE_QUALIFICATION_ROUTE_DECISION_MATRIX_2026-07-03.md
python governance/compat/check_external_absorption_value_conversion.py --paths docs/reviews/CVF_MSEA_R14_MINERU_POST_SAMPLE_QUALIFICATION_ROUTE_DECISION_WORKER_RETURN_2026-07-03.md docs/reference/CVF_MSEA_R14_MINERU_POST_SAMPLE_QUALIFICATION_ROUTE_DECISION_MATRIX_2026-07-03.md
python governance/compat/check_external_absorption_overlap_discipline.py --paths docs/reviews/CVF_MSEA_R14_MINERU_POST_SAMPLE_QUALIFICATION_ROUTE_DECISION_WORKER_RETURN_2026-07-03.md docs/reference/CVF_MSEA_R14_MINERU_POST_SAMPLE_QUALIFICATION_ROUTE_DECISION_MATRIX_2026-07-03.md
python governance/compat/check_corpus_completeness_report_integrity.py --paths docs/reviews/CVF_MSEA_R14_MINERU_POST_SAMPLE_QUALIFICATION_ROUTE_DECISION_WORKER_RETURN_2026-07-03.md docs/reference/CVF_MSEA_R14_MINERU_POST_SAMPLE_QUALIFICATION_ROUTE_DECISION_MATRIX_2026-07-03.md
python governance/compat/check_rescan_intelligence_hardening.py --paths docs/reviews/CVF_MSEA_R14_MINERU_POST_SAMPLE_QUALIFICATION_ROUTE_DECISION_WORKER_RETURN_2026-07-03.md docs/reference/CVF_MSEA_R14_MINERU_POST_SAMPLE_QUALIFICATION_ROUTE_DECISION_MATRIX_2026-07-03.md
python governance/compat/run_worker_return_fast_gate.py --base <executionBaseHead> --head HEAD
python governance/compat/check_delta_execution_claim_boundary.py --base <executionBaseHead> --head HEAD
python governance/compat/check_agent_operation_trace.py --base <executionBaseHead> --head HEAD
git diff --name-status
git status --short
```

Worker may use reviewer-fast or pre-implementation autorun as additional
confirmation, but must not commit.

## Acceptance Criteria

| Criterion | Required evidence |
|---|---|
| Exactly one selected route token | worker return and matrix record one selected token from the allowed list |
| Non-selected route rationale | every other allowed token has source-backed hold/reject/defer rationale |
| No route execution | changed-files evidence shows only the two worker-owned artifacts |
| Output checker read-ahead | worker return records checker-source read-ahead before writing outputs |
| No commit | worker return includes no-commit statement pairing `WORKER_MUST_NOT_COMMIT` with `honored` |
| Gates | command evidence records PASS/BLOCKED_WITH_REASON for required commands |

## Agent Operation Trace Block

| Field | Value |
|---|---|
| Actor | dispatch author |
| Provider or surface | Codex local workspace |
| Session or invocation | MSEA-R14 dispatch authoring |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | `apply_patch`; `python governance/compat/run_agent_autorun_workflow_gate.py`; `git status --short` |
| Target paths | this work order and paired baseline |
| Allowed scope source | operator option 1 approval plus active session next-move state |
| Before status evidence | `git status --short` clean before authoring |
| After status evidence | pre-dispatch gate and `git status --short` before commit |
| Diff evidence | `git diff --name-status` for dispatch paths |
| Approval boundary | operator explicitly selected option 1 |
| Claim boundary | dispatch packet only; no route execution |
| Agent type | dispatcher |
| Invocation ID | MSEA-R14-dispatch |
| Expected manifest | two dispatch artifacts |
| Actual changed set | two dispatch artifacts |
| Manifest delta | matches expected dispatch manifest |
| Operation class | DISPATCH_PACKET |
| Commit mode | WORKER_MUST_NOT_COMMIT |
| Protected delete/rename disposition | none authorized |
| Expected changed files | this work order and paired baseline for dispatcher; worker return and route-decision matrix for worker |
| Clean worktree evidence | dispatcher and worker must record `git status --short` evidence |
| Cross-batch isolation | R14 must not mutate accepted R9/R10/R12/R13 artifacts or session surfaces during worker execution |

## Claim Boundary

This work order authorizes route-decision documentation only. It does not
authorize operator-confirmation collection, privacy/redaction adjudication,
permission/license decisions, sample document copy/import, corpus population,
MinerU runtime or model download, parser/OCR/VLM execution, provider/live
proof, S3 credentials, RAG/index writes, schema or writer implementation,
adapter code, checker implementation, legal-domain product lane, public-sync,
production-readiness claims, or current-law/legal-advice quality claims.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is a private provenance dispatch packet. No public-sync or public
catalog export is authorized.
