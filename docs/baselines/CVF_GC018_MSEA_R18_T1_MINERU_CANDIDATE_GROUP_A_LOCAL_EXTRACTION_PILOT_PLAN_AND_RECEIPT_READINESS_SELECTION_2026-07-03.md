# CVF GC-018 Baseline - MSEA-R18-T1 MinerU Candidate Group A Local Extraction Pilot Plan And Receipt Readiness Selection

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: MSEA_R18_T1

Dispatch base head: 37bcd147

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: reviewer/closer

Worker target: delegated worker role

## Purpose

Open a bounded planning-and-selection tranche for the accepted Candidate Group A
private-test corpus. The worker must source-verify MinerU CLI/backend/output
surfaces, define a local extraction pilot command envelope and receipt
readiness matrix, and select the next route without running MinerU, installing
models, reading document body content, or creating extraction outputs.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind source-intake --batch-id MSEA_R18_T1 --title "MinerU Candidate Group A Local Extraction Pilot Plan And Receipt Readiness Selection" --date 2026-07-03 --base 37bcd147 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | source-intake plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Completed placeholders, set DISPATCH_READY, added source-verified MinerU CLI/backend/output facts, preserved R17 privacy boundary, and narrowed execution to planning plus route selection only. |
| checkerReadAheadConfirmation | Read `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_source_intake_decision_packet_preflight.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`. |
| docOnlyNewFields | selectedRouteToken; pilotCommandEnvelope; quarantineOutputRoot; receiptReadinessMatrixPath; runtimePrerequisiteDisposition |
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
| Dispatch impact | This baseline avoids provider-local authority, avoids exhaustive repository claims, mandates checker read-ahead before worker-output writing, uses source mirror authority, and keeps symbol cells to real symbols or sections. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_source_intake_decision_packet_preflight.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py` |
| literalTokensReviewed | Dispatch Prompt Envelope fields; Scaffold Provenance Block fields; Source Verification Block columns; ADIF resolver query exactness; Agent Handoff Contract Control Block fields; Reviewer Closure Conversion fields; Worker Return Packet Shape Contract fields; Source-Intake Decision Packet Fields; Public Export Disposition token `DEFERRED_PRIVATE_ONLY`; Rescan Intelligence Hardening; ledger terminal marker; `CHECKER_CANDIDATE`; `REMOVED_OR_REJECTED`; `RESOLVED_BY_DESIGN`; Delta block field labels; Agent Operation Trace labels. |
| gateRunPurpose | Confirmation evidence after checker source read-ahead, not first discovery; gates confirm this baseline's dispatch shape and source-fidelity evidence. |
| claimBoundary | Read-ahead covers this baseline and paired work order only; worker output artifacts must perform their own checker-source read-ahead before writing. |

## Source Verification Block

| Claimed item | Claim type | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MinerU upstream authority is the pinned source mirror, not the old external clone or legacy adapter folder | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/INDEX.md` | row `opendatalab__MinerU` | `opendatalab__MinerU` | source mirror index | ACCEPT |
| Pinned MinerU mirror commit is recorded for this absorption lane | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/INDEX.md` | row `opendatalab__MinerU` | `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491` | source mirror index | ACCEPT |
| Source mirror boundary forbids install, model download, runtime/parser execution, provider/live proof, public-sync, and direct import | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/INDEX.md` | row `opendatalab__MinerU` | `opendatalab__MinerU` | source mirror index | ACCEPT |
| R17 accepted two Candidate Group A DOCX file metadata rows and local-private boundary | VALUE_SET | VALUE_SET | `docs/reference/CVF_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_LEDGER_2026-07-03.md` | `## Current Path/Hash/Size Verification`; `## Claim Boundary` | Candidate Group A | MSEA-R17-T1 intake ledger | ACCEPT |
| Candidate file 116 hash is the accepted R17 metadata value | VALUE_SET | VALUE_SET | `docs/reference/CVF_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_LEDGER_2026-07-03.md` | `## Current Path/Hash/Size Verification` | `116_2025_QH15_666020.docx` | MSEA-R17-T1 intake ledger | ACCEPT |
| Candidate file 148 hash is the accepted R17 metadata value | VALUE_SET | VALUE_SET | `docs/reference/CVF_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_LEDGER_2026-07-03.md` | `## Current Path/Hash/Size Verification` | `148_2025_QH15_675262.docx` | MSEA-R17-T1 intake ledger | ACCEPT |
| R12 requires sample source identity, permission or license basis, privacy/redaction disposition, slot, format/size, and proof-use confirmation | VALUE_SET | VALUE_SET | `docs/reference/CVF_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_2026-07-03.md` | `## Sample Intake And Provenance Policy`; `## Operator Handoff Requirements` | Sample Intake And Provenance Policy | MSEA-R12-T1 policy reference | ACCEPT |
| R12 local parser runtime pilot row requires a concrete downstream use case and fresh GC-018 authorizing model download, execution, and live/provider proof | VALUE_SET | VALUE_SET | `docs/reference/CVF_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_2026-07-03.md` | runtime pilot gating table | Local parser runtime pilot | MSEA-R12-T1 policy reference | ACCEPT |
| R10 keeps runtime/parser adapter held behind concrete downstream use case and fresh authorization | VALUE_SET | VALUE_SET | `docs/reference/CVF_MSEA_R10_MINERU_ADAPTER_CONTRACT_DRAFT_2026-07-03.md` | `## Held Lanes And Reopen Conditions` | Runtime/parser adapter | MSEA-R10 contract draft | ACCEPT |
| MinerU CLI entry point is `mineru` | EXISTS | EXISTS | `.private_reference/source_mirrors/opendatalab__MinerU/pyproject.toml` | project scripts section | `mineru` | project scripts | ACCEPT |
| MinerU package exposes model-download, API, router, and Gradio scripts that remain forbidden here | EXISTS | EXISTS | `.private_reference/source_mirrors/opendatalab__MinerU/pyproject.toml` | project scripts section | `mineru-models-download` | project scripts | ACCEPT |
| MinerU README states DOCX is a supported input format | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/README.md` | overview and usage sections | `DOCX` | upstream README | ACCEPT |
| MinerU README shows `mineru -p <input_path> -o <output_path>` command envelope | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/README.md` | usage command section | `mineru -p <input_path> -o <output_path>` | upstream README | ACCEPT |
| MinerU README shows `-b pipeline` as a command option example | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/README.md` | usage command section | `-b pipeline` | upstream README | ACCEPT |
| MinerU README warns `mineru` can automatically start a local temporary service when no API URL is provided | RUNTIME_BEHAVIOR | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/README.md` | CLI architecture note | `mineru` | upstream README | ACCEPT |
| Pipeline backend constant exists | EXISTS | EXISTS | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/backend_options.py` | backend constants | `BACKEND_PIPELINE` | backend options module | ACCEPT |
| Default backend is not pipeline | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/backend_options.py` | backend constants | `DEFAULT_BACKEND` | backend options module | ACCEPT |
| HTTP-client backend choices exist and must remain out of this planning-only tranche | EXISTS | EXISTS | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/backend_options.py` | backend choices | `HTTP_CLIENT_BACKEND_CHOICES` | backend options module | ACCEPT |
| Allowed parse methods are auto, txt, and ocr | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/api_request.py` | parse method constant | `ALLOWED_PARSE_METHODS` | API request module | ACCEPT |
| API request module includes server URL and client-side output generation surfaces that require runtime planning | EXISTS | EXISTS | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/api_request.py` | request option definitions | `server_url` | API request module | ACCEPT |
| CLI output path function creates backend-specific output directories | RUNTIME_BEHAVIOR | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/output_paths.py` | output path function | `build_parse_dir` | output path module | ACCEPT |
| MinerU output docs say generated files depend on backend and input document type | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/reference/output_files.md` | output overview | output_files | upstream output documentation | ACCEPT |
| MinerU output docs define `middle.json`, `content_list.json`, and `content_list_v2.json` families | EXISTS | EXISTS | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/reference/output_files.md` | output file sections | `content_list_v2.json` | upstream output documentation | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Existing MSEA-R18 artifacts | `rg -n "MSEA_R18_T1|MSEA-R18-T1|LOCAL_EXTRACTION_PILOT_PLAN_AND_RECEIPT_READINESS_SELECTION|Local Extraction Pilot Plan And Receipt Readiness" docs CVF_SESSION CVF_SESSION_MEMORY.md` found only current next-move references before authoring | NO_PRIOR_ARTIFACT_COLLISION |
| Dispatch packet path check | No existing baseline or work order with these exact R18 names existed before this add operation | ABSENT_BEFORE_AUTHORING |
| Collision decision | MSEA-R18-T1 is a new child tranche after accepted MSEA-R17-T1 private corpus intake | SAFE_TO_CREATE |

## Source-Intake Decision Packet Fields

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | source-mirror absorption follow-on planning |
| Negative search performed | Yes - see Negative Search And Collision Discipline |
| Disposition | ADAPT |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| R17 private Candidate Group A intake | `docs/reference/CVF_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_LEDGER_2026-07-03.md` | CONFIRMED_EXISTING | path/hash/private boundary already owned | reuse and recompute metadata only |
| MinerU CLI/backend/output facts | `.private_reference/source_mirrors/INDEX.md`; `docs/reference/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md`; `docs/reference/CVF_MSEA_R10_MINERU_ADAPTER_CONTRACT_DRAFT_2026-07-03.md` | ENRICH_EXISTING | converts candidate facts into a pilot planning matrix | source-verify and classify |
| Direct source import or public export | `.private_reference/source_mirrors/INDEX.md`; `docs/reference/CVF_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_LEDGER_2026-07-03.md` | REJECT_DIRECT_IMPORT | private-only documents must not be copied or public-synced | forbid |

## Baseline Decision

MSEA-R18-T1 is authorized for planning and route selection only. The worker may
author a worker return and a companion receipt-readiness matrix that choose
whether a later MSEA-R19 local extraction pilot work order is now ready, or
whether receipt schema, environment/model planning, or operator approval must
come first. This GC-018 does not authorize runtime execution.

## Planned Artifact Manifest

| Artifact | Owner | Disposition |
| --- | --- | --- |
| `docs/reviews/CVF_MSEA_R18_T1_MINERU_CANDIDATE_GROUP_A_LOCAL_EXTRACTION_PILOT_PLAN_AND_RECEIPT_READINESS_SELECTION_WORKER_RETURN_2026-07-03.md` | worker | create uncommitted |
| `docs/reference/CVF_MSEA_R18_T1_MINERU_CANDIDATE_GROUP_A_LOCAL_EXTRACTION_PILOT_PLAN_AND_RECEIPT_READINESS_MATRIX_2026-07-03.md` | worker | create uncommitted |

## Verification Evidence

| Evidence | Command or source | Result |
| --- | --- | --- |
| Startup base | `git rev-parse --short HEAD` | `37bcd147` |
| Source mirror authority | `.private_reference/source_mirrors/INDEX.md` | pinned MinerU mirror row accepted |
| ADIF disclosure | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch` | 10 returned defects disclosed |
| Checker read-ahead | targeted reads of listed `governance/compat/check_*.py` files | literal shape controls copied into this packet |

## Claim Boundary

This baseline authorizes only dispatch and no-commit worker planning for a
future private local MinerU extraction pilot. It does not authorize MinerU
install, model download, parser/OCR/VLM/hybrid/API/router/Gradio/Docker
execution, local temporary service startup, provider/live proof, S3/RAG, source
document copy/import, fuller content quotation, schema/writer/adapter/checker
implementation, package activation, public-sync, benchmark, document-truth,
extraction-accuracy, legal advice quality, current-law correctness, production
readiness, action authority, or workflow-chain completion claim.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: Candidate Group A source documents and any future derived outputs are
authorized only for local private CVF testing unless the operator separately
approves fuller inclusion or public export.
