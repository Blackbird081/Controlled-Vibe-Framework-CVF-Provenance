# CVF MSEA-R12 MinerU Sample Corpus And Expected Receipt Policy Roadmap

Memory class: FULL_RECORD

Status: ROADMAP_READY_FOR_MSEA_R12_T1_GC018_AND_WORK_ORDER_AUTHORING

docType: roadmap

Date: 2026-07-03

Batch ID: MSEA-R12

External knowledge intake routing: REQUIRED

EPISTEMIC_PROCESS_NA_WITH_REASON: this roadmap carries forward an accepted
route-selection decision and plans a documentation/reference policy tranche.
It does not execute MinerU, compare empirical extraction outputs, or update a
document-truth claim.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_roadmap_closure_freshness.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_source_mirror_migration.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_rescan_intelligence_hardening.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | roadmap structural groups; Checker Source Read-Ahead Block fields; External Knowledge Intake Routing field labels; external repo or copied folder; External Absorption Core field labels; ledger_terminal=; Corpus verdict bullet; overlap dispositions CONFIRMED_EXISTING, ENRICH_EXISTING, REJECT_DIRECT_IMPORT, NO_NEW_VALUE; value lanes DOCTRINE_ADAPTED, RUNTIME_CANDIDATE, PACKAGE_CANDIDATE, CHECKER_CANDIDATE, REJECT_DIRECT_IMPORT, NO_PACKAGE_OR_RUNTIME_VALUE; Source Mirror Migration Control fields; Rescan intelligence verdict; Delta Execution Claim Boundary Control Block fields; DEFERRED_PRIVATE_ONLY |
| gateRunPurpose | Confirmation evidence after roadmap checker read-ahead; not first discovery. |
| claimBoundary | Read-ahead covers this roadmap-only artifact; no GC-018/work-order dispatch, worker execution, MinerU runtime, source import, provider/live proof, package activation, checker implementation, schema implementation, receipt-writer code, adapter implementation, public-sync, or production claim is made. |

## Authorization / Decision

Operator authorization: after MSEA-R11-T1 completion and acceptance, the
operator asked for the next work order. Current session state allowed roadmap
authoring first for the selected route.

Accepted route-selection source:
`docs/reference/CVF_MSEA_R11_T1_MINERU_PRODUCTIZATION_READINESS_ROUTE_SELECTION_DECISION_MATRIX_2026-07-03.md`

Decision:
`OPEN_SAMPLE_CORPUS_AND_EXPECTED_RECEIPT_POLICY_ROADMAP`

Recommended next:
`AUTHOR_MSEA_R12_T1_GC018_AND_WORK_ORDER_FOR_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_DEFINITION`

This roadmap is complete as a roadmap-authoring artifact. It is not a worker
dispatch and does not define the sample corpus or expected receipt policy.

## Purpose

Define the governed path for a documentation/reference tranche that specifies
how CVF should select a small MinerU document-extraction sample corpus and how
future receipt evidence should be judged before schema, writer, runtime, RAG,
provider, S3, Docker, package, checker, or adapter implementation work begins.

MSEA-R11-T1 selected this lane because all implementation-facing alternatives
need concrete input and expected-output boundaries first. R12 turns that
selection into a bounded next work-order route without running MinerU or
creating receipt instances.

## Scope

Allowed by this roadmap:

- Use accepted MSEA-R11-T1, R11, R10, R9, R8, and R7 owner surfaces.
- Define a policy for sample-corpus slots, evidence requirements, exclusion
  rules, operator handoff requirements, and expected receipt assertions.
- Preserve the distinction between corpus policy and actual corpus files.
- Keep implementation lanes held until a later fresh GC-018 and work order.

Not allowed by this roadmap:

- Creating or importing sample documents.
- Claiming a sample corpus exists.
- MinerU install, model download, parser/OCR/VLM/hybrid/API/router/Gradio/
  Docker execution, provider/live call, credentials/S3, RAG write, source
  import, package activation, checker implementation, schema implementation,
  receipt-writer code, adapter implementation, public-sync, Web/MCP/model-
  router/action-authority, automatic invocation, benchmark, document-truth,
  extraction-accuracy, or production-readiness claims.

## Non-Goals

| Non-goal | Reason |
|---|---|
| Actual sample corpus population | No operator-provided document set is named; T1 may define slots and selection rules only |
| Runtime/parser pilot | Runtime remains held behind a later fresh GC-018, dependency plan, and proof boundary |
| Receipt schema implementation | R7/R10 provide vocabulary but exact schema types and validation remain downstream work |
| Receipt-writer code | Writer code needs an accepted policy and later schema |
| RAG ingestion | RAG remains held until receipt evidence and quality/downstream-use status exist |
| Provider/S3/Docker/package work | No operator-named use case, credential plan, deployment target, or hardware profile exists |
| Checker implementation | Checker work remains condition-gated behind repeated real misses or authorized ingestion |
| Public export | Private provenance route only |

## Design Control Gate

| Control | Required disposition |
|---|---|
| Corpus policy boundary | Define selection slots and acceptance rules; do not claim actual sample files exist |
| Receipt expectation boundary | Define expected receipt assertions, non-assertions, and evidence categories; do not implement schema or writer code |
| Operator handoff boundary | Record what future operator-provided documents must include before any corpus-population tranche |
| Runtime boundary | Preserve all runtime/parser/provider/RAG/S3/Docker/package/checker lanes as held |
| Source authority | Use accepted MSEA owner surfaces and the pinned source mirror index; legacy copied folder is secondary historical material only |
| Claim boundary | Reject document-truth, extraction-accuracy, production-readiness, and live/provider claims |

## Target / Source

Target: create a roadmap-only R12 owner surface that routes future MinerU
sample-corpus and expected-receipt-policy work to a source-verified
MSEA-R12-T1 GC-018/work order.

Source basis:

- `docs/reference/CVF_MSEA_R11_T1_MINERU_PRODUCTIZATION_READINESS_ROUTE_SELECTION_DECISION_MATRIX_2026-07-03.md`
- `docs/reviews/CVF_MSEA_R11_T1_MINERU_PRODUCTIZATION_READINESS_ROUTE_SELECTION_WORKER_RETURN_2026-07-03.md`
- `docs/roadmaps/CVF_MSEA_R11_MINERU_DOCUMENT_EXTRACTION_PRODUCTIZATION_READINESS_ROADMAP_2026-07-03.md`
- `docs/reference/CVF_MSEA_R10_MINERU_ADAPTER_CONTRACT_DRAFT_2026-07-03.md`
- `docs/reference/CVF_MSEA_R9_MINERU_CVF_APPLICATION_BLUEPRINT_AND_ADAPTER_CONTRACT_READINESS_2026-07-02.md`
- `docs/reference/CVF_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_2026-07-02.md`
- `docs/reference/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md`
- `.private_reference/source_mirrors/INDEX.md`
- `.private_reference/source_mirrors/opendatalab__MinerU/`

Roadmap base head: `414003e9`.

## Scope / Methodology

1. Carry forward the accepted MSEA-R11-T1 route token.
2. Convert the selected route into a bounded policy-definition roadmap.
3. Define the minimum outputs a worker can produce without sample documents or
   runtime execution.
4. Preserve held implementation lanes and concrete reopen conditions.
5. Open only MSEA-R12-T1 GC-018/work-order authoring.

## Findings / Position

Position:
`ROADMAP_READY_FOR_MSEA_R12_T1_GC018_AND_WORK_ORDER_AUTHORING`

MSEA-R12 should not attempt schema, writer, or runtime implementation. The
first useful tranche is a documentation/reference policy that defines:

| Policy area | Required decision | Boundary |
|---|---|---|
| Sample corpus slot taxonomy | Which document classes a future operator-provided corpus should cover | no sample files are created or claimed |
| Evidence intake requirements | What source, license/privacy, and provenance facts must accompany samples | no public export or source import |
| Expected receipt assertion classes | What a future receipt may assert about artifact existence, page/block evidence, backend identity, and quality status | no receipt schema implementation |
| Non-assertions | What future receipts must not claim, including document truth and extraction accuracy | no benchmark or certification |
| Reopen routing | Which later lanes the policy can unblock | no implementation dispatch now |

## Risk / Corrective Action

| Risk | Corrective action |
|---|---|
| Roadmap could be misread as saying a sample corpus exists | Explicit non-goals and claim boundary forbid corpus-existence claims |
| Policy could drift into schema implementation | T1 must define expected receipt policy only; schema/writer lanes remain downstream |
| Operator documents could be ingested too early | T1 must define operator handoff requirements without accepting documents |
| Runtime enthusiasm could skip the policy layer | Roadmap keeps runtime/parser/RAG/provider/S3/Docker/package/checker lanes held |
| RAG or accuracy claims could be smuggled into receipts | T1 must define non-assertion rules for document truth and extraction accuracy |

## Work Plan

| Step | Output | Status |
|---|---|---|
| R12.1 | Create this sample-corpus and expected-receipt-policy roadmap | COMPLETE |
| R12.2 | Author MSEA-R12-T1 GC-018 and work order for policy-definition worker output | READY_NEXT |
| R12.3 | Worker creates sample corpus policy and expected receipt policy reference | FUTURE |
| R12.4 | Reviewer accepts or rejects the policy reference | FUTURE |
| R12.5 | If accepted, later route can decide whether to populate corpus, implement schema, or implement receipt writer | FUTURE_CONDITIONED |

## Acceptance Criteria

| Criterion | Evidence | Status |
|---|---|---|
| R11-T1 accepted route exists | material commit `bfa451dc` selected `OPEN_SAMPLE_CORPUS_AND_EXPECTED_RECEIPT_POLICY_ROADMAP` | PASS |
| Roadmap does not create sample files | Scope and Non-Goals forbid corpus population | PASS |
| Roadmap does not implement schema/writer/runtime | Non-Goals and Claim Boundary reject those lanes | PASS |
| R12-T1 output is bounded | Work Plan opens policy-definition worker output only | PASS |
| Source mirror remains advisory input | Source Mirror Migration Control | PASS |
| Runtime/provider/live/public claims are rejected | Claim Boundary and Delta block | PASS |

## Verification / Evidence

| Evidence item | Result |
|---|---|
| `git rev-parse --short HEAD` before authoring | `414003e9` |
| Planned R12 roadmap path existed before authoring | `False` |
| Planned R12-T1 baseline path existed before authoring | `False` |
| Planned R12-T1 work-order path existed before authoring | `False` |
| MSEA-R11-T1 material acceptance commit | `bfa451dc` |
| Source mirror HEAD recompute | `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491` |
| Source mirror file count recompute | `425` |
| Expected changed set | this roadmap only |
| Verification target before commit | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 414003e9 --head HEAD` |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| R11-T1 selected sample corpus and expected receipt policy route | VALUE_SET | `docs/reference/CVF_MSEA_R11_T1_MINERU_PRODUCTIZATION_READINESS_ROUTE_SELECTION_DECISION_MATRIX_2026-07-03.md` | `## Selected Route`; `## Rationale` | `OPEN_SAMPLE_CORPUS_AND_EXPECTED_RECEIPT_POLICY_ROADMAP` | MSEA-R11-T1 decision matrix | ACCEPT |
| R11-T1 did not define sample corpus or receipt policy | VALUE_SET | `docs/reference/CVF_MSEA_R11_T1_MINERU_PRODUCTIZATION_READINESS_ROUTE_SELECTION_DECISION_MATRIX_2026-07-03.md` | `## Rationale`; `## Explicit Non-Claims` | sample corpus or expected receipt policy has not been defined | MSEA-R11-T1 decision matrix | ACCEPT |
| R7 owns receipt artifact families and field families, not executable schema | EXISTS | `docs/reference/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md` | `## Receipt Artifact Family Map`; `## Field Family Map`; `## Explicit Non-Claims` | Receipt Artifact Family Map; Field Family Map | MSEA-R7 reference | ACCEPT |
| R10 does not authorize receipt schema implementation or receipt-writer code | VALUE_SET | `docs/reference/CVF_MSEA_R10_MINERU_ADAPTER_CONTRACT_DRAFT_2026-07-03.md` | `## Contract Class`; `## Explicit Non-Claims` | `schemaImplementationAuthorized`; `receiptWriterAuthorized` | MSEA-R10 reference | ACCEPT |
| R9 keeps runtime/provider/RAG/S3/checker routes held behind concrete conditions | VALUE_SET | `docs/reference/CVF_MSEA_R9_MINERU_CVF_APPLICATION_BLUEPRINT_AND_ADAPTER_CONTRACT_READINESS_2026-07-02.md` | `## Source-Backed Hold Conditions`; `## Adapter Contract Readiness Matrix` | runtime/provider/RAG/S3/checker hold conditions | MSEA-R9 reference | ACCEPT |
| R8 preserves runtime/package candidates without execution | VALUE_SET | `docs/reference/CVF_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_2026-07-02.md` | `## Candidate And No-Value Ledger`; `## External Absorption Value Conversion Matrix` | `RUNTIME_CANDIDATE`; `PACKAGE_CANDIDATE`; `REJECT_DIRECT_IMPORT` | MSEA-R8 residual ledger | ACCEPT |
| Source mirror is pinned and preferred over legacy copied folder facts | VALUE_SET | `.private_reference/source_mirrors/INDEX.md` | row `opendatalab__MinerU` | `.private_reference/source_mirrors/opendatalab__MinerU/` | source mirror index | ACCEPT |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | accepted MSEA owner surfaces plus pinned MinerU source mirror -> R11-T1 selected route -> R12 policy-definition roadmap -> future R12-T1 source-verified work order |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_source_mirror_migration.py` |
| Owner surface | this roadmap |
| Disposition | ADAPT: convert accepted MinerU route selection into policy-definition planning |
| Claim boundary | roadmap-only; no runtime/provider/live/S3/RAG/Docker/package/checker/source-import/schema/receipt-writer/adapter implementation/public-sync/production claim |

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | `https://github.com/opendatalab/MinerU.git` at `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491`; local mirror `.private_reference/source_mirrors/opendatalab__MinerU/`; accepted MSEA-T2/R4/R5/R6/R7/R8/R9/R10/R11/R11-T1 evidence |
| Enumeration command | `rg --files --hidden --no-ignore .private_reference/source_mirrors/opendatalab__MinerU -g '!**/.git/**'` returned `425` during roadmap authoring |
| Manifest artifact or inline manifest | `.private_reference/source_mirrors/INDEX.md` row `opendatalab__MinerU` |
| Processing ledger artifact or inline ledger | `docs/roadmaps/CVF_MSEA_R12_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_ROADMAP_2026-07-03.md` |
| Ledger terminal statuses | READ, SOURCE_VERIFIED, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, SKIPPED_WITH_REASON, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | MSEA-R7/R8/R9/R10/R11/R11-T1 owner surfaces |
| Unresolved items | none for roadmap authoring; T1 must define policy and keep corpus-population as separate later work |
| Completion claim boundary | roadmap planning only; no runtime/provider/public/package/checker/source-import/schema/receipt-writer/adapter expansion |

ledger_terminal=READ for accepted MSEA owner surfaces; ledger_terminal=SOURCE_VERIFIED for source mirror commit/count; ledger_terminal=ADAPTED for sample-corpus/receipt-policy roadmap routing; ledger_terminal=DEFERRED for corpus population and all implementation-facing lanes; ledger_terminal=REJECTED for direct upstream import; ledger_terminal=NO_NEW_VALUE for already-owned absorption facts.

## Corpus Completeness And Report Integrity

- Corpus task class: roadmap planning for sample-corpus and expected-receipt-policy definition.
- Corpus root: `.private_reference/source_mirrors/opendatalab__MinerU/` plus accepted MSEA owner surfaces.
- Snapshot time: 2026-07-03 roadmap authoring.
- Enumeration command: `rg --files --hidden --no-ignore .private_reference/source_mirrors/opendatalab__MinerU -g '!**/.git/**'`.
- Manifest artifact or inline manifest: `.private_reference/source_mirrors/INDEX.md` row `opendatalab__MinerU`.
- Manifest hash: source mirror commit `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491`.
- Processing ledger artifact or inline ledger: this roadmap.
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED | BLOCKED_UNREADABLE.
- Reconciliation: manifest=source mirror index row plus accepted MSEA owner surfaces; ledger_terminal=READ for owner surfaces and SOURCE_VERIFIED for mirror commit/count; exclusions=sample document import, full reabsorption, runtime execution, package activation, provider/live proof, source import, schema implementation, receipt-writer code, adapter implementation, production readiness; unresolved=0.
- Unresolved files: none for this roadmap-authoring scope.
- Declared exclusions: sample document import, corpus population, full 425-file reabsorption, runtime execution, package activation, provider/live proof, source import, schema implementation, receipt-writer code, adapter implementation, production-readiness claims.
- Unreadable or unsupported files: none identified for roadmap authoring.
- Aggregation check: accepted MSEA owner surfaces are cited instead of regenerated into a new corpus aggregate.
- Drift check: source mirror HEAD and file count recomputed during roadmap authoring matched the source mirror index.
- Output traceability: roadmap routes to MSEA-R12-T1 GC-018/work-order authoring only.
- Adversarial verification: roadmap rejects actual corpus population, runtime execution, schema implementation, receipt-writer code, adapter implementation, document truth, extraction accuracy, and production readiness.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| MSEA-R11-T1 selected route | sample corpus and expected receipt policy should be first | DOCTRINE_ADAPTED | this roadmap | open R12-T1 policy-definition work order authoring | no implementation |
| MSEA-R7 receipt vocabulary | artifact families and field families require concrete policy grounding | DOCTRINE_ADAPTED | R12-T1 policy output | define expected receipt assertions and non-assertions | no schema implementation |
| MSEA-R10 prerequisites | schema and writer remain separate downstream steps | DOCTRINE_ADAPTED | R12 Work Plan | keep schema/writer held | no writer code |
| MSEA-R9/R10 runtime holds | runtime/provider/RAG/S3/checker lanes need concrete reopen conditions | RUNTIME_CANDIDATE | held-lane routing | keep demand-gated | no runtime/provider/RAG/S3 action |
| MSEA-R8 Docker/package evidence | deployment/package candidates remain held | PACKAGE_CANDIDATE | held-lane routing | keep deployment/package work held | no Docker build/run or package activation |
| MSEA-T3/R6/R9/R10 checker notes | overclaim checker remains condition-gated | CHECKER_CANDIDATE | held-lane routing | defer checker work | no checker implementation |
| Direct upstream files | advisory input only | REJECT_DIRECT_IMPORT | source mirror control | reject direct import | no source import |
| Prior MSEA absorption facts | already-owned evidence | NO_PACKAGE_OR_RUNTIME_VALUE | predecessor owner surfaces | cite only | no runtime/package behavior |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| Sample-corpus and expected-receipt-policy route | `docs/reference/CVF_MSEA_R11_T1_MINERU_PRODUCTIZATION_READINESS_ROUTE_SELECTION_DECISION_MATRIX_2026-07-03.md` | ENRICH_EXISTING | converts selected route into a roadmap and T1 seed | create roadmap |
| Receipt vocabulary | `docs/reference/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md` | CONFIRMED_EXISTING | R12 uses vocabulary without implementing schema | cite |
| Adapter contract prerequisites | `docs/reference/CVF_MSEA_R10_MINERU_ADAPTER_CONTRACT_DRAFT_2026-07-03.md` | CONFIRMED_EXISTING | R12 preserves schema/writer/runtime holds | cite |
| Runtime/provider/S3/Docker/RAG/package/checker holds | `docs/reference/CVF_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_2026-07-02.md`; `docs/reference/CVF_MSEA_R9_MINERU_CVF_APPLICATION_BLUEPRINT_AND_ADAPTER_CONTRACT_READINESS_2026-07-02.md`; `docs/reference/CVF_MSEA_R10_MINERU_ADAPTER_CONTRACT_DRAFT_2026-07-03.md` | CONFIRMED_EXISTING | no held lane is reopened by roadmap | defer |
| Direct upstream implementation | `.private_reference/source_mirrors/INDEX.md` | REJECT_DIRECT_IMPORT | direct import remains forbidden | reject |

## Source Mirror Migration Control

| Field | Disposition |
|---|---|
| Legacy source path | Legacy MinerU adapter folder remains secondary historical material only |
| Source mirror path | `.private_reference/source_mirrors/opendatalab__MinerU/` |
| Mirror index row | `.private_reference/source_mirrors/INDEX.md` row `opendatalab__MinerU` |
| Pinned upstream commit | `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491` |
| Migration disposition | MIGRATED_TO_SOURCE_MIRROR |
| Legacy cleanup disposition | LEGACY_REFERENCE_ONLY_WITH_REASON: historical comparison only; source facts prefer pinned mirror or governed MSEA artifacts |
| Claim boundary | source-mirror authority control only; no runtime, install, package activation, provider/live proof, public-sync, checker implementation, source import, schema implementation, receipt-writer code, adapter implementation, or production-readiness claim |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

Reason: this roadmap carries forward an accepted route-selection decision. It
is not a rescan, intake-refresh, source-backed reassessment, or residual
repository absorption pass.

## Explicit Non-Claims

This roadmap does not claim:

- that a sample corpus exists;
- that operator-provided sample documents were received;
- that expected receipt policy has been defined;
- that a CVF-owned receipt schema or receipt writer has been implemented;
- that MinerU has been installed, executed, or is production-ready;
- that any parser, OCR, table, formula, layout, or VLM output is accurate or
  represents document truth;
- that RAG/context ingestion, provider/live calls, S3 access, Docker/package
  activation, or checker enforcement is authorized.

## Future R12-T1 Work-Order Seed

| Question | Required source basis | Required output |
|---|---|---|
| What sample-corpus slots should CVF require before runtime/schema/writer work? | MSEA-R11-T1 selected route; R7 receipt families; R10 prerequisites | sample corpus slot taxonomy |
| What evidence must accompany future operator-provided samples? | R9/R10 hold conditions and claim boundary | sample intake and provenance policy |
| What should a future receipt assert or refuse to assert? | R7/R10 receipt vocabulary; T2/R9 claim boundaries | expected receipt assertion/non-assertion policy |
| Which lanes remain held after policy definition? | R8/R9/R10 held-lane evidence | held-lane table with reopen conditions |

Expected worker-owned output for T1:
`docs/reference/CVF_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_2026-07-03.md`

T1 must be WORKER_MUST_NOT_COMMIT and documentation/reference-only.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | MSEA-R12 sample corpus and expected receipt policy roadmap |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, mandatory-wrapper, provider, parser, adapter, schema, receipt-writer, or production behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created or consumed |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime action is executed or observed |
| invocationBoundary | local governed roadmap authoring only |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, CLI, MCP, Web runtime, adapter, package, watcher, daemon, parser, RAG index, or production route interception claim |
| claimLanguage | roadmap planning and future work-order seed only |
| forbiddenExpansion | no MinerU runtime, install, model download, parser/OCR/VLM/hybrid/API/router/Gradio/Docker execution, provider/live call, credentials/S3, RAG write, source import, package activation, checker implementation, public-sync, Web/MCP/model-router/action-authority, automatic invocation, benchmark, document-truth, extraction-accuracy, schema implementation, receipt-writer code, adapter implementation, or production-readiness claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance roadmap. No public-sync export is authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | roadmap author |
| Provider or surface | Codex local workspace |
| Session or invocation | MSEA-R12 roadmap authoring, 2026-07-03 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, `rg`, source reads, `apply_patch`, governance gates |
| Target paths | `docs/roadmaps/CVF_MSEA_R12_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_ROADMAP_2026-07-03.md` |
| Allowed scope source | operator request plus MSEA-R11-T1 material acceptance commit `bfa451dc` |
| Before status evidence | clean worktree; `git status --short` was empty before roadmap authoring |
| After status evidence | one new roadmap pending pre-dispatch gates |
| Diff evidence | `git diff --name-status` before material commit |
| Approval boundary | roadmap authoring for sample-corpus/expected-receipt-policy route only |
| Claim boundary | no runtime/provider/live/public/package/checker/source-import/schema/receipt-writer/adapter/Web/MCP/model-router/action-authority claim |
| Agent type | roadmap author |
| Invocation ID | `msea-r12-sample-corpus-expected-receipt-policy-roadmap-2026-07-03` |
| Expected manifest | this roadmap |
| Actual changed set | this roadmap |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename; one new roadmap |

## Claim Boundary

This roadmap authorizes only future MSEA-R12-T1 GC-018/work-order authoring
for a documentation/reference sample-corpus and expected-receipt-policy
definition tranche. It does not authorize or claim sample corpus population,
MinerU installation, parser execution, OCR/VLM/hybrid routing, remote backend
processing, model download, API/router/Gradio service, Docker deployment,
provider/live proof, S3 access, credential handling, RAG indexing, source
import, checker enforcement, package activation, schema implementation,
receipt-writer code, adapter implementation, public-sync export, document
truth, extraction accuracy, benchmark, certification, generated aggregate
mutation, production readiness, model-router behavior, action authority,
automatic invocation, or universal document intelligence.
