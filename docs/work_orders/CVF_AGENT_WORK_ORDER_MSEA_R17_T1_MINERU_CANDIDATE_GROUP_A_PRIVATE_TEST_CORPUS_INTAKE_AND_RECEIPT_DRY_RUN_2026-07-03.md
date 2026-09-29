# CVF Agent Work Order - MSEA-R17-T1 MinerU Candidate Group A Private Test Corpus Intake And Receipt Dry Run

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: MSEA_R17_T1

Dispatch base head: 32d4a11f

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker

Reviewer/closer: reviewer/closer

Worker return path: `docs/reviews/CVF_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_AND_RECEIPT_DRY_RUN_WORKER_RETURN_2026-07-03.md`

## Dispatch Prompt Envelope

Role: delegated worker for MSEA_R17_T1.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_AND_RECEIPT_DRY_RUN_2026-07-03.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: worker must capture `git rev-parse --short HEAD` before edits.

Current-time notes: artifact date is 2026-07-03; use current repository state, not stale chat memory.

Do-not-misread notes: this packet opens private metadata-only intake for Candidate Group A only; it does not authorize Group B, original document commit, public-sync, MinerU runtime, OCR/parser execution, RAG, schema/writer/adapter/checker implementation, benchmark, document-truth, legal advice, current-law, or production claims.

Required first actions: read startup files, guard orientation, literal gotchas, this work order, the paired GC-018 baseline, and checker source listed in the Checker Source Read-Ahead Block before writing worker outputs.

Return contract: create the worker return and companion intake ledger, run required gates, leave changes uncommitted, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Execute a bounded private-test intake step for the two Candidate Group A DOCX
files named by R13/R16 and newly authorized by the operator for local private
CVF testing. The worker creates a metadata-only intake ledger and receipt
dry-run readiness reference that verifies path presence, size, hash, slot
assignment, operator authorization boundary, and expected receipt
non-claims, without copying source documents into this repository and without
running MinerU.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind source-intake --batch-id MSEA_R17_T1 --title "MinerU Candidate Group A Private Test Corpus Intake And Receipt Dry Run" --date 2026-07-03 --base 32d4a11f --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | source-intake plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Completed placeholders, set DISPATCH_READY, narrowed scope to Group A metadata-only private intake, added operator authorization, source verification, output manifest, execution plan, and no-runtime/public claim boundary. |
| checkerReadAheadConfirmation | Read `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_source_intake_decision_packet_preflight.py`; `governance/compat/check_agent_operation_trace.py`. |
| docOnlyNewFields | operatorPrivateTestingStatement; selectedCandidateGroup; privateIntakeLedgerPath; receiptDryRunReadinessPath; originalDocumentCommitPolicy |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |

## Worker Autonomy / No-Question Rule

Worker must repair allowed-scope checker failures directly by reading the
failing checker source and matching the literal required shape. Worker should
return to orchestrator only for a source contradiction, forbidden-scope need,
missing local file, or missing authority that makes completion impossible.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: ADIF-0001; ADIF-0002; ADIF-0014; ADIF-0015; ADIF-0020; ADIF-0021; ADIF-0007; ADIF-0016; ADIF-0017; ADIF-0006

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch` |
| Returned defect count | 10 |
| Returned defects | ADIF-0001; ADIF-0002; ADIF-0014; ADIF-0015; ADIF-0020; ADIF-0021; ADIF-0007; ADIF-0016; ADIF-0017; ADIF-0006 |
| Disclosed defectIds | ADIF-0001; ADIF-0002; ADIF-0014; ADIF-0015; ADIF-0020; ADIF-0021; ADIF-0007; ADIF-0016; ADIF-0017; ADIF-0006 |
| Dispatch impact | This work order avoids provider-local authority, avoids broad exhaustive claims, uses scaffold provenance, keeps worker output checker read-ahead mandatory, avoids applicability-marker overmatch, and keeps source verification symbol cells to real symbols or sections. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_source_intake_decision_packet_preflight.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_adif_defect_registry_disclosure.py` |
| literalTokensReviewed | Dispatch Prompt Envelope fields; Scaffold Provenance Block fields; Source Verification Block columns; ADIF resolver query exactness; Agent Handoff Contract Control Block fields; Reviewer Closure Conversion fields `completionReviewPath` and `reviewerOwnedClosurePaths`; Worker Return Packet Shape Contract fields; Worker Output Checker Read-Ahead Mandate wording; Source-Intake Decision Packet Fields stub without standalone source-intake applicability declaration; Public Export Disposition token `DEFERRED_PRIVATE_ONLY`; Delta block field labels; Agent Operation Trace labels. |
| gateRunPurpose | Confirmation evidence after checker source read-ahead, not first discovery; gates confirm this work order's dispatch shape and source-fidelity evidence. |
| claimBoundary | Read-ahead covers this work order and paired baseline only; worker output artifacts must perform their own checker-source read-ahead before writing. |

## Operator Authorization Block

Operator statement received in the current session on 2026-07-03:

```text
Operator confirms Candidate Group A source documents are authorized for local private CVF testing only. They must not be public-synced or redistributed. Derived outputs may be generated for governed internal receipts/evaluation, but original documents and sensitive personal/legal details must remain private; any committed artifact must use metadata, redaction, or excerpt-minimal evidence unless operator separately approves fuller inclusion.
```

Dispatch interpretation:

- authorizes local private CVF testing for Candidate Group A only;
- allows metadata, hashes, slot assignment, and governed internal receipt or
  evaluation evidence;
- forbids public-sync, redistribution, committing original DOCX files, and
  fuller content inclusion without separate operator approval;
- leaves Candidate Group B and nine rejected derived outputs outside scope.

## Source Verification Block

| Claimed item | Claim type | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R16-T1 selected Candidate Group A only as first-use target | VALUE_SET | VALUE_SET | `docs/reference/CVF_MSEA_R16_T1_MINERU_SAMPLE_CORPUS_OPERATOR_DETAIL_AND_MINIMAL_POPULATION_READINESS_2026-07-03.md` | `## First-Use Candidate Decision` | `CANDIDATE_GROUP_A_ONLY` | MSEA-R16-T1 reference | ACCEPT |
| R16-T1 named the two Candidate Group A DOCX files as the future population target after operator detail | VALUE_SET | VALUE_SET | `docs/reference/CVF_MSEA_R16_T1_MINERU_SAMPLE_CORPUS_OPERATOR_DETAIL_AND_MINIMAL_POPULATION_READINESS_2026-07-03.md` | `## Minimal Population Readiness` | `116_2025_QH15_666020.docx`; `148_2025_QH15_675262.docx` | MSEA-R16-T1 reference | ACCEPT |
| R12 sample policy requires source identity, permission/license, privacy/redaction, slot, format/size, and proof-use confirmation | VALUE_SET | VALUE_SET | `docs/reference/CVF_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_2026-07-03.md` | `## Sample Intake And Provenance Policy`; `## Operator Handoff Requirements` | Sample Intake And Provenance Policy | MSEA-R12-T1 reference | ACCEPT |
| R13 records Group A filenames, hashes, sizes, source identity, and READ_DEEP status | VALUE_SET | VALUE_SET | `docs/reference/CVF_MSEA_R13_T1_MINERU_LEGAL_POLICY_SAMPLE_CORPUS_CANDIDATE_QUALIFICATION_LEDGER_2026-07-03.md` | `### Candidate Group A: T4/T5 two-DOCX Vietnamese law set` | Candidate Group A | MSEA-R13-T1 reference | ACCEPT |
| Operator supplied local-private testing authorization and privacy-preserving disposition for Candidate Group A in this session | DOC_ONLY_NEW | DOC_ONLY_NEW | `docs/baselines/CVF_GC018_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_AND_RECEIPT_DRY_RUN_2026-07-03.md` | `## Operator Authorization Block` | operatorPrivateTestingStatement | MSEA-R17-T1 dispatch packet | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Planned artifact paths | Four `Test-Path` checks for the planned baseline, work order, worker return, and companion reference returned `False` before authoring | ABSENT_BEFORE_AUTHORING |
| Prior MSEA-R17 packet search | targeted governed-artifact and session-surface search found no prior MSEA-R17 dispatch or closure artifact; a too-broad first search timed out and was replaced with exact path checks and targeted MSEA-owner searches | NO_COLLISION |
| Collision decision | This is a new MSEA-R17-T1 child tranche after R16-T1 acceptance and operator detail | SAFE_TO_CREATE |

## Authority Chain

- Operator instruction: current-session Candidate Group A local-private testing statement recorded in the paired GC-018 baseline.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Active handoff: `AGENT_HANDOFF_V34_2026-07-03.md`.
- Predecessor acceptance: `docs/reference/CVF_MSEA_R16_T1_MINERU_SAMPLE_CORPUS_OPERATOR_DETAIL_AND_MINIMAL_POPULATION_READINESS_2026-07-03.md`.
- Sample policy: `docs/reference/CVF_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_2026-07-03.md`.
- Candidate evidence: `docs/reference/CVF_MSEA_R13_T1_MINERU_LEGAL_POLICY_SAMPLE_CORPUS_CANDIDATE_QUALIFICATION_LEDGER_2026-07-03.md`.
- GC-018 baseline: `docs/baselines/CVF_GC018_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_AND_RECEIPT_DRY_RUN_2026-07-03.md`.

Authority boundary: if any source contradicts this packet, stop and return
`BLOCKED_WITH_REASON`. This work order does not authorize anything outside
Candidate Group A private metadata-only intake.

## Agent Roles

| Role | Owner | Responsibility |
| --- | --- | --- |
| Operator | operator | owns local-private testing authorization and any later fuller-content or runtime decision |
| Dispatcher | dispatcher role | authors this GC-018/work order and runs pre-dispatch gates |
| Worker | delegated worker role | creates only the named worker return and companion reference, without commit |
| Reviewer/closer | reviewer/closer | reviews returned artifacts, repairs allowed-scope shape defects if needed, commits material if accepted |
| Session-sync steward | reviewer/closer after material acceptance | updates active session state only after accepted material closure |

## Pre-Flight Checks

Required before worker execution:

```powershell
git rev-parse --short HEAD
git status --short
Test-Path 'docs\reviews\CVF_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_AND_RECEIPT_DRY_RUN_WORKER_RETURN_2026-07-03.md'
Test-Path 'docs\reference\CVF_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_LEDGER_2026-07-03.md'
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
```

Expected result: clean worktree at execution start, planned worker outputs
absent before writing, and pre-implementation gate passing after worker output
authoring and allowed-scope repairs.

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| intakeRole | dispatcher-authored private metadata-intake work order |
| workerRole | no-commit metadata verifier and ledger author |
| reviewerRole | reviewer/closer validates worker return and companion reference |
| operatorRole | owns authorization for fuller content, runtime, public-sync, or Group B |
| route mode | MULTI_AGENT_SINGLE_ROLE |
| routeDecision | proceed with Candidate Group A private metadata-only intake; hold runtime and public routes |
| escalationCondition | missing file, hash mismatch requiring scope change, need to quote fuller content, need to run MinerU/runtime/provider, or any Group B use |
| claimBoundary | role routing only; no automatic execution, provider routing, public export, or production claim |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher authors packet; delegated worker executes under no-commit; reviewer/closer accepts or rejects |
| phase | dispatch |
| baseHeadFor(phase) | dispatchBaseHead=32d4a11f; executionBaseHead=worker captures at start; closureBaseHead=reviewer/closer sets before material commit |
| changedSetScope(phase) | dispatch may add only this work order and paired GC-018 baseline; worker may add only the named worker return and companion reference |
| traceScope(phase, actor) | dispatcher trace in this work order; worker trace in worker return and companion reference; reviewer trace in commit/steward evidence |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer/closer owns any material commit after review |
| crossBatchIsolation | clean worktree required before worker execution; worker must not touch session, handoff, runtime, public, source-mirror, package, or checker paths |
| nextMoveSurfaces | reviewer/closer updates active session state only after accepting material closure; worker must not edit session state |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_AND_RECEIPT_DRY_RUN_COMPLETION_2026-07-03.md` (optional; prefer reviewer repair inside the worker return unless a separate completion artifact is necessary) |
| reviewerOwnedClosurePaths | worker return and companion reference named in Work-Order Fulfillment Manifest; session-sync surfaces only after material acceptance |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Output Checker Read-Ahead Mandate

Before writing each worker-owned output artifact, read checker source for that
file's docType, path family, and conditional content class.

| Output artifact | Required read-ahead result |
| --- | --- |
| worker return under reviews | derive exact review headings, worker-return quality terms, trace labels, delta boundary labels, corpus/value/non-claim tokens, no-commit evidence shape, and current `git status --short` finality before writing |
| companion reference under reference | derive exact reference headings such as Scope / Applies To, Target / Source, source verification, corpus/value routing, trace, Public Export Disposition, and claim-boundary labels before writing |

Literal-shape reminders: list section names without heading prefixes in any
checklist, write source-not-found disposition spelling instead of the exact
blocked enum in literalTokensReviewed, and avoid broad closure-dependency
phrasing unless the row cites accepted artifact path and commit evidence.

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| `docs/reviews/CVF_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_AND_RECEIPT_DRY_RUN_WORKER_RETURN_2026-07-03.md` | create uncommitted worker return with `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`, command evidence, git status, no-commit statement, and worker-output checker read-ahead evidence |
| `docs/reference/CVF_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_LEDGER_2026-07-03.md` | create uncommitted metadata-only intake ledger and receipt dry-run readiness reference for exactly the two Group A files |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_AND_RECEIPT_DRY_RUN_WORKER_RETURN_2026-07-03.md`
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Shape-list rule: when listing required worker-output sections, write section
names without the heading prefix. Reserve actual heading syntax for real
sections so structural checkers do not treat this checklist as the artifact
section body.

## Source-Intake Decision Packet Fields

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Negative search performed | Yes - see Negative Search And Collision Discipline |
| Disposition | ADAPT |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| Operator Candidate Group A private-testing statement | `docs/baselines/CVF_GC018_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_AND_RECEIPT_DRY_RUN_2026-07-03.md` | ENRICH_EXISTING | closes the specific R16-T1 operator-detail prerequisite for Group A private metadata intake only | use as dispatch authority for this tranche |
| Candidate Group A source identity, hashes, sizes, and prior deep classification | `docs/reference/CVF_MSEA_R13_T1_MINERU_LEGAL_POLICY_SAMPLE_CORPUS_CANDIDATE_QUALIFICATION_LEDGER_2026-07-03.md` | CONFIRMED_EXISTING | existing evidence is reused and recomputed only for path/hash/size drift | cite and verify |
| R12 sample intake policy | `docs/reference/CVF_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_2026-07-03.md` | CONFIRMED_EXISTING | policy is applied to a metadata-only Group A intake ledger | cite and adapt |
| Candidate Group B and rejected derived outputs | `docs/reference/CVF_MSEA_R13_T1_MINERU_LEGAL_POLICY_SAMPLE_CORPUS_CANDIDATE_QUALIFICATION_LEDGER_2026-07-03.md`; `docs/reference/CVF_MSEA_R16_T1_MINERU_SAMPLE_CORPUS_OPERATOR_DETAIL_AND_MINIMAL_POPULATION_READINESS_2026-07-03.md` | CONFIRMED_EXISTING | exclusion is carried forward unchanged | keep out of scope |
| MinerU runtime/parser/RAG/schema/writer/adapter/checker lanes | `docs/reference/CVF_MSEA_R9_MINERU_CVF_APPLICATION_BLUEPRINT_AND_ADAPTER_CONTRACT_READINESS_2026-07-02.md`; `docs/reference/CVF_MSEA_R10_MINERU_ADAPTER_CONTRACT_DRAFT_2026-07-03.md`; `docs/reference/CVF_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_2026-07-03.md`; `docs/reference/CVF_MSEA_R16_T1_MINERU_SAMPLE_CORPUS_OPERATOR_DETAIL_AND_MINIMAL_POPULATION_READINESS_2026-07-03.md` | CONFIRMED_EXISTING | no implementation-facing lane is reopened by this intake dispatch | defer |

## Scope

Allowed scope:

- Read the two operator-local Candidate Group A DOCX file paths only for
  filesystem metadata and SHA-256 hashing.
- Verify that the current hash/size evidence matches or explicitly differs
  from R13/T4S recorded evidence.
- Assign the two files to R12 sample-corpus slots, with a conservative note
  that assignment does not certify document truth or extraction accuracy.
- Record the operator private-testing statement and privacy/redaction
  disposition in the companion reference.
- Create the two worker-owned artifacts named in the manifest.
- Run pre-implementation autorun and worker-return fast gate, repairing
  allowed-scope shape failures.

Forbidden scope:

- Do not copy, import, stage, commit, public-sync, redistribute, or embed the
  original DOCX files.
- Do not quote sensitive personal/legal details or fuller source content.
- Do not use Candidate Group B or any of the nine rejected derived outputs.
- Do not run MinerU, install models, execute parser/OCR/VLM/API/Docker, call a
  provider, write RAG index, use S3 credentials, implement schema/writer/
  adapter/checker code, edit source mirrors, or mutate runtime/package/Web/MCP
  surfaces.
- Do not claim document truth, extraction accuracy, legal advice quality,
  current-law correctness, benchmark result, production readiness, or workflow
  chain completion.
- Do not edit session state, active handoff, front door, or protected
  governance paths.

Risk ceiling: R1 private metadata-only document-intake evidence.

## Write Ownership

Owned files:

- `docs/reviews/CVF_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_AND_RECEIPT_DRY_RUN_WORKER_RETURN_2026-07-03.md`
- `docs/reference/CVF_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_LEDGER_2026-07-03.md`

Forbidden paths:

- original DOCX source documents;
- Candidate Group B files and the nine rejected derived outputs;
- active session front door, generated session state surfaces, and active handoff files;
- `governance/compat/**`;
- `.private_reference/source_mirrors/**`;
- runtime, package, Web, MCP, schema, writer, adapter, checker, public-sync,
  and generated aggregate paths.

Write mode: create-only for the two owned worker output artifacts.

## Required First Reads

Before writing worker outputs, read:

- `CVF_SESSION_MEMORY.md` - active session front door.
- `CVF_SESSION/ACTIVE_SESSION_STATE.json` - canonical state registry.
- `AGENT_HANDOFF_V34_2026-07-03.md` - active handoff and next allowed move.
- `docs/reference/guard_orientation/README.md` - guard routing.
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` - literal-format traps.
- this work order and paired GC-018 baseline.
- `docs/reference/CVF_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_2026-07-03.md`.
- `docs/reference/CVF_MSEA_R13_T1_MINERU_LEGAL_POLICY_SAMPLE_CORPUS_CANDIDATE_QUALIFICATION_LEDGER_2026-07-03.md`.
- `docs/reference/CVF_MSEA_R16_T1_MINERU_SAMPLE_CORPUS_OPERATOR_DETAIL_AND_MINIMAL_POPULATION_READINESS_2026-07-03.md`.
- applicable worker-output checker source listed in the Worker Output Checker Read-Ahead Mandate.

## Execution Plan

1. Capture `executionBaseHead` and `git status --short`.
2. Generate the worker return from the checker-safe skeleton before long prose.
3. Verify the two Group A file paths using literal PowerShell paths.
4. Compute SHA-256 and size for exactly the two Group A files, and compare
   with R13 recorded values.
5. Create a companion metadata-only intake ledger with slot assignment,
   operator authorization boundary, privacy/redaction disposition,
   receipt dry-run expected assertions, and non-assertions.
6. Create the worker return with command evidence, current dirty status, no
   commit statement, and explicit forbidden-scope non-claims.
7. Run required gates; repair allowed-scope shape failures; return
   `COMPLETE_PENDING_REVIEW` if all required checks pass, otherwise
   `BLOCKED_WITH_REASON`.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap or predecessor requirement | Work order section | Output artifact or field | Verification command or check | Status |
| --- | --- | --- | --- | --- |
| R16-T1 requires operator detail before a Group A packet | Operator Authorization Block | companion reference authorization boundary | reviewer checks statement is recorded | PASS |
| R16-T1 allows only Candidate Group A first use | Scope; Fulfillment Manifest | selectedCandidateGroup row in companion reference | worker verifies no Group B rows are promoted | PASS |
| R12 requires source identity, permission/license, privacy/redaction, slot, format/size, proof-use | Execution Plan; companion reference | intake evidence matrix | worker compares against R12 policy | PASS |
| R13 provides filenames, hashes, sizes, source identity | Source Verification Block | metadata ledger rows | worker recomputes path/hash/size | PASS |
| R12/R16 forbid runtime and production claims | Forbidden scope; Claim Boundary | Explicit Non-Claims in outputs | worker-return fast gate and reviewer read | PASS |

## Evidence Requirements

Worker must record:

- `git rev-parse --short HEAD` before edits.
- `git status --short` before edits and at handoff.
- `Test-Path` for each of the two Group A file paths.
- `Get-FileHash -Algorithm SHA256` for each file.
- `Get-Item` size for each file.
- `git diff --name-status`.
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD`.
- `python governance/compat/run_worker_return_fast_gate.py`.

## Verification Commands

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 32d4a11f --head HEAD
python governance/compat/run_worker_return_fast_gate.py
git status --short
```

## Acceptance Criteria

- [ ] Worker creates exactly the two planned artifacts and leaves them uncommitted.
- [ ] Companion reference accounts for exactly the two Group A DOCX files.
- [ ] Current path, hash, and size are recorded for both files.
- [ ] Operator local-private testing authorization and privacy/redaction boundary are recorded.
- [ ] Original documents are not copied, imported, staged, committed, public-synced, or redistributed.
- [ ] Group B and the nine rejected derived outputs remain out of scope.
- [ ] No MinerU runtime, provider/live, RAG, schema/writer, adapter, checker, package, Web, MCP, model-router, benchmark, document-truth, extraction-accuracy, legal-advice, current-law, or production claim is made.
- [ ] Required worker gates pass or the worker returns `BLOCKED_WITH_REASON`.

Fail conditions:

- [ ] Any planned Group A file is missing or hash/size evidence cannot be captured.
- [ ] Worker copies, imports, stages, commits, or public-syncs source documents.
- [ ] Worker includes fuller source content or sensitive details beyond metadata/redaction/excerpt-minimal evidence.
- [ ] Worker runs MinerU or any runtime/provider/live/parser/OCR/VLM/RAG route.
- [ ] Worker edits outside the two planned worker-owned artifacts.

## Review Gate

Worker handoff is not closure. Reviewer/closer must review the returned
artifacts, may repair allowed-scope artifact-shape defects, and owns any
material commit plus later session-sync if accepted.

Reviewer validation command:

```powershell
python governance/compat/run_agent_commit_steward_preflight.py --mode reviewer-return --base <closureBaseHead> --head HEAD --enforce
```

## Operator Checkpoint

Operator checkpoint satisfied for this dispatch: the operator provided a
Candidate Group A local-private testing statement and privacy-preserving
disposition in the current session. Further operator approval is required for
any fuller content inclusion, source document copy/import into this
repository, public-sync, Group B use, MinerU runtime/parser/OCR execution,
provider/live proof, RAG write, schema/writer/adapter/checker implementation,
or production claim.

## Closure Checklist

- [ ] Worker creates exactly the two planned artifacts.
- [ ] Worker records actual `git status --short` at handoff.
- [ ] Worker records path, hash, and size evidence for both Group A files.
- [ ] Worker records operator authorization and privacy/redaction boundary.
- [ ] Worker return fast gate passes.
- [ ] Reviewer-return commit steward preflight passes before material commit.
- [ ] Committed-range pre-closure gate passes after accepted material commit.
- [ ] Session-sync surfaces are updated separately only if material closure changes next move.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher |
| Provider or surface | local workspace |
| Session or invocation | MSEA_R17_T1 MinerU Candidate Group A Private Test Corpus Intake And Receipt Dry Run, 2026-07-03 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, `rg`, `Get-ChildItem`, scaffold helper, `apply_patch`, governance gates |
| Target paths | `docs/baselines/CVF_GC018_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_AND_RECEIPT_DRY_RUN_2026-07-03.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_AND_RECEIPT_DRY_RUN_2026-07-03.md` |
| Allowed scope source | operator private-testing statement, accepted MSEA-R16-T1, and this paired GC-018 baseline |
| Before status evidence | clean worktree at dispatch start; `git rev-parse --short HEAD` returned `32d4a11f` |
| After status evidence | dispatch packet pending pre-dispatch gate and material commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | dispatch authoring only for Candidate Group A private metadata intake |
| Claim boundary | no runtime/provider/live/public/package/source-import/schema/writer/adapter/checker/Web/MCP/model-router/action-authority/legal-domain product claim |
| Agent type | dispatcher |
| Invocation ID | `msea-r17-t1-2026-07-03` |
| Expected manifest | `docs/baselines/CVF_GC018_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_AND_RECEIPT_DRY_RUN_2026-07-03.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_AND_RECEIPT_DRY_RUN_2026-07-03.md` |
| Actual changed set | `docs/baselines/CVF_GC018_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_AND_RECEIPT_DRY_RUN_2026-07-03.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_AND_RECEIPT_DRY_RUN_2026-07-03.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename is authorized |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | MSEA-R17-T1 Candidate Group A private metadata-only test-corpus intake and receipt dry-run readiness dispatch |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, mandatory-wrapper, provider, parser, adapter, schema, receipt-writer, corpus-processing, or production behavior is claimed |
| receiptEvidence | N/A with reason: no runtime receipt exists; worker may create documentation-only expected receipt dry-run fields |
| actionEvidence | N/A with reason: dispatch authoring only; worker may capture file metadata and hashes but no runtime action |
| invocationBoundary | local governed documentation and metadata verification only |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized |
| claimLanguage | private metadata-intake dispatch only |
| forbiddenExpansion | no source document commit, public-sync, MinerU runtime, install, model download, parser/OCR/VLM/API/Docker execution, provider/live call, S3/RAG, schema/writer/adapter/checker implementation, benchmark, document-truth, extraction-accuracy, legal advice quality, current-law correctness, production readiness, Web/MCP/model-router behavior, or action authority |

## Claim Boundary

This work order authorizes only a no-commit worker to create a private
metadata-only intake ledger and receipt dry-run readiness reference for the
two named Candidate Group A DOCX files. It does not authorize source document
copy/import into this repository, original document commit, public-sync,
MinerU install/runtime/parser/OCR/VLM/API/Docker execution, provider/live
proof, RAG write, S3/credential handling, schema implementation,
receipt-writer code, adapter implementation, checker implementation,
benchmark, document-truth, extraction-accuracy, legal advice quality,
current-law correctness, production readiness, model-router behavior, action
authority, or workflow-chain completion claim.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: Candidate Group A source documents and derived internal receipts are
authorized only for local private CVF testing. No public-sync export is
authorized.
