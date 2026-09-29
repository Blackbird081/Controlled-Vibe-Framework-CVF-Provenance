# CVF GC-018 Baseline - MSEA-R17-T1 MinerU Candidate Group A Private Test Corpus Intake And Receipt Dry Run

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: MSEA_R17_T1

Dispatch base head: 32d4a11f

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: Operator

Reviewer owner: reviewer/closer

Worker target: delegated worker role

## Purpose

Authorize a bounded no-commit worker to convert the operator's Candidate
Group A private-testing statement into a private test-corpus intake ledger and
receipt dry-run readiness reference for the two named Group A DOCX files. The
baseline authorizes metadata, path, hash, size, slot, and non-claim evidence
only; it does not authorize committing source documents, public-sync, MinerU
runtime execution, OCR/parser execution, RAG write, schema/writer code,
adapter implementation, benchmark, document-truth, extraction-accuracy,
legal-advice-quality, current-law-correctness, or production-readiness claims.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind source-intake --batch-id MSEA_R17_T1 --title "MinerU Candidate Group A Private Test Corpus Intake And Receipt Dry Run" --date 2026-07-03 --base 32d4a11f --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | source-intake plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Completed all placeholders, narrowed the packet to Candidate Group A only, added operator authorization, source verification, negative-search evidence, output manifest, and private-test claim boundary. |
| checkerReadAheadConfirmation | Read `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_source_intake_decision_packet_preflight.py`; `governance/compat/check_agent_operation_trace.py`. |
| docOnlyNewFields | operatorPrivateTestingStatement; selectedCandidateGroup; privateIntakeLedgerPath; receiptDryRunReadinessPath; originalDocumentCommitPolicy |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: ADIF-0001; ADIF-0002; ADIF-0014; ADIF-0015; ADIF-0020; ADIF-0021; ADIF-0007; ADIF-0016; ADIF-0017; ADIF-0006

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch` |
| Returned defect count | 10 |
| Returned defects | ADIF-0001; ADIF-0002; ADIF-0014; ADIF-0015; ADIF-0020; ADIF-0021; ADIF-0007; ADIF-0016; ADIF-0017; ADIF-0006 |
| Disclosed defectIds | ADIF-0001; ADIF-0002; ADIF-0014; ADIF-0015; ADIF-0020; ADIF-0021; ADIF-0007; ADIF-0016; ADIF-0017; ADIF-0006 |
| Dispatch impact | This packet avoids provider-local authority, reads checker source before writing, uses the scaffold helper, avoids broad exhaustive corpus claims, keeps Group B and derived outputs excluded, splits future runtime work, and keeps Source Verification symbol cells to real symbols or section names. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_source_intake_decision_packet_preflight.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_adif_defect_registry_disclosure.py` |
| literalTokensReviewed | Checker Source Read-Ahead Block fields `applicableCheckersRead`, `literalTokensReviewed`, `gateRunPurpose`, `claimBoundary`; Scaffold Provenance Block fields; Source Verification Block column names; ADIF resolver query exactness; dispatch-ready status tokens; Source-Intake Decision Packet Fields stub without standalone source-intake applicability declaration; public export token `DEFERRED_PRIVATE_ONLY`; no-commit token `WORKER_MUST_NOT_COMMIT`; Agent Operation Trace labels; Delta block field labels. |
| gateRunPurpose | Confirmation evidence after checker source read-ahead, not first discovery; pre-dispatch gates are used to confirm this packet's shape and source-fidelity evidence. |
| claimBoundary | Read-ahead covers this GC-018 baseline and paired MSEA-R17-T1 work order only; it does not prove future worker output shape, runtime behavior, document extraction, public export, or production readiness. |

## Operator Authorization Block

Operator statement received in the current session on 2026-07-03:

```text
Operator confirms Candidate Group A source documents are authorized for local private CVF testing only. They must not be public-synced or redistributed. Derived outputs may be generated for governed internal receipts/evaluation, but original documents and sensitive personal/legal details must remain private; any committed artifact must use metadata, redaction, or excerpt-minimal evidence unless operator separately approves fuller inclusion.
```

Dispatch interpretation:

- permission/license for Candidate Group A private testing is closed for this
  bounded local-private tranche;
- privacy/redaction disposition is closed only as a privacy-preserving rule:
  metadata, hashes, slot assignment, path presence, and excerpt-minimal
  evidence are allowed, while original documents and sensitive details stay
  private;
- Candidate Group B is not authorized by this statement;
- the nine ungoverned derived outputs remain rejected for direct promotion;
- any fuller content inclusion, public-sync, or runtime/parser execution needs
  a later fresh source-verified packet.

## Source Verification Block

| Claimed item | Claim type | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R16-T1 selected Candidate Group A only as first-use target | VALUE_SET | VALUE_SET | `docs/reference/CVF_MSEA_R16_T1_MINERU_SAMPLE_CORPUS_OPERATOR_DETAIL_AND_MINIMAL_POPULATION_READINESS_2026-07-03.md` | `## First-Use Candidate Decision` | `CANDIDATE_GROUP_A_ONLY` | MSEA-R16-T1 reference | ACCEPT |
| R16-T1 required a fresh GC-018/work order naming the two Group A files before population work | VALUE_SET | VALUE_SET | `docs/reference/CVF_MSEA_R16_T1_MINERU_SAMPLE_CORPUS_OPERATOR_DETAIL_AND_MINIMAL_POPULATION_READINESS_2026-07-03.md` | `## Minimal Population Readiness` | `116_2025_QH15_666020.docx`; `148_2025_QH15_675262.docx` | MSEA-R16-T1 reference | ACCEPT |
| R12 requires source identity, permission/license, privacy/redaction, slot, format/size, and proof-use evidence before sample corpus population | VALUE_SET | VALUE_SET | `docs/reference/CVF_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_2026-07-03.md` | `## Sample Intake And Provenance Policy`; `## Operator Handoff Requirements` | Sample Intake And Provenance Policy | MSEA-R12-T1 reference | ACCEPT |
| R13 records the Candidate Group A filenames, hashes, sizes, source identity, and READ_DEEP status | VALUE_SET | VALUE_SET | `docs/reference/CVF_MSEA_R13_T1_MINERU_LEGAL_POLICY_SAMPLE_CORPUS_CANDIDATE_QUALIFICATION_LEDGER_2026-07-03.md` | `### Candidate Group A: T4/T5 two-DOCX Vietnamese law set` | Candidate Group A | MSEA-R13-T1 reference | ACCEPT |
| R13 flags Candidate Group B privacy risk and rejects ungoverned derived outputs from direct promotion | VALUE_SET | VALUE_SET | `docs/reference/CVF_MSEA_R13_T1_MINERU_LEGAL_POLICY_SAMPLE_CORPUS_CANDIDATE_QUALIFICATION_LEDGER_2026-07-03.md` | `## Sample Intake Provenance Gap Matrix`; `## Rejected Derived Output Boundary` | Candidate Group B; Rejected Derived Output Boundary | MSEA-R13-T1 reference | ACCEPT |
| The current active handoff authorizes a fresh source-verified operator-detail closure or Candidate Group A population-readiness step only after operator detail exists | VALUE_SET | VALUE_SET | `AGENT_HANDOFF_V34_2026-07-03.md` | `## Next Allowed Move` | `AGENT_HANDOFF_V34_2026-07-03.md` | active handoff | ACCEPT |
| Operator provided local-private testing authorization and privacy-preserving disposition for Candidate Group A in this session | DOC_ONLY_NEW | DOC_ONLY_NEW | `docs/baselines/CVF_GC018_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_AND_RECEIPT_DRY_RUN_2026-07-03.md` | `## Operator Authorization Block` | operatorPrivateTestingStatement | MSEA-R17-T1 dispatch packet | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Path existence for planned baseline | `Test-Path 'docs\baselines\CVF_GC018_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_AND_RECEIPT_DRY_RUN_2026-07-03.md'` returned `False` before authoring | ABSENT_BEFORE_AUTHORING |
| Path existence for planned work order | `Test-Path 'docs\work_orders\CVF_AGENT_WORK_ORDER_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_AND_RECEIPT_DRY_RUN_2026-07-03.md'` returned `False` before authoring | ABSENT_BEFORE_AUTHORING |
| Path existence for planned worker return | `Test-Path 'docs\reviews\CVF_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_AND_RECEIPT_DRY_RUN_WORKER_RETURN_2026-07-03.md'` returned `False` before authoring | ABSENT_BEFORE_AUTHORING |
| Path existence for planned companion reference | `Test-Path 'docs\reference\CVF_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_LEDGER_2026-07-03.md'` returned `False` before authoring | ABSENT_BEFORE_AUTHORING |
| Token search for MSEA-R17 before authoring | targeted search over governed MSEA artifacts and session surfaces found no prior MSEA-R17 dispatch or closure artifact; broad first search timed out and was replaced with targeted path checks plus exact artifact-path absence | NO_COLLISION |
| Collision decision | MSEA-R17-T1 is a new child tranche after accepted R16-T1 and operator detail; it does not overwrite an existing packet | SAFE_TO_CREATE |

## Baseline Decision

Decision: DISPATCH_READY.

Authorized tranche: MSEA-R17-T1 Candidate Group A private metadata-only test
corpus intake and receipt dry-run readiness.

Selected candidate group: `CANDIDATE_GROUP_A_ONLY`.

Selected worker mode: `WORKER_MUST_NOT_COMMIT`.

This decision is based on accepted MSEA-R16-T1 plus the operator's explicit
local-private testing statement. It does not open Candidate Group B, the nine
rejected derived outputs, MinerU runtime, public-sync, or production work.

## Verification Evidence

| Evidence | Command or source | Result |
| --- | --- | --- |
| Dispatch base head | `git rev-parse --short HEAD` | `32d4a11f` |
| Worktree before authoring | `git status --short` | clean |
| Planned path absence | four `Test-Path` checks recorded in Negative Search And Collision Discipline | all planned paths absent before authoring |
| Candidate file path discovery | `Get-ChildItem -LiteralPath 'D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local' -Recurse -Filter <filename>` | both Group A DOCX files discovered under `Policy_Local\data_input` |
| ADIF disclosure | resolver command in ADIF section | 10 defect IDs disclosed |
| Scaffold provenance | scaffold helper command in Scaffold Provenance Block | scaffold used as starting point |

## Source-Intake Decision Packet Fields

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Negative search performed | Yes - see Negative Search And Collision Discipline |
| Disposition | ADAPT |

## Planned Artifact Manifest

| Artifact | Owner | Required disposition |
| --- | --- | --- |
| `docs/reviews/CVF_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_AND_RECEIPT_DRY_RUN_WORKER_RETURN_2026-07-03.md` | worker | create uncommitted worker return |
| `docs/reference/CVF_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_LEDGER_2026-07-03.md` | worker | create uncommitted private intake ledger and receipt dry-run readiness reference |

## Acceptance Boundary

The worker may verify local path presence, file size, and SHA-256 for the two
Group A DOCX files at their existing operator-local paths, then record a
metadata-only intake ledger. The worker must not copy the original documents
into this repository, stage them, public-sync them, redistribute them, quote
sensitive details, or run MinerU/parser/OCR/VLM/RAG/provider/runtime work.

## Claim Boundary

This baseline authorizes dispatch of a private, metadata-only Candidate Group
A intake ledger and receipt dry-run readiness reference. It does not authorize
sample document copy/import into the repository, original document commit,
public-sync export, MinerU install/runtime/model download/parser/OCR/VLM/API/
Docker execution, provider/live proof, RAG write, S3/credential handling,
schema implementation, receipt-writer code, adapter implementation, checker
implementation, benchmark, document-truth, extraction-accuracy, legal advice
quality, current-law correctness, production readiness, model-router behavior,
or action authority.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: Candidate Group A source documents and any derived internal receipts
are authorized only for local private CVF testing. No public-sync export is
authorized.
