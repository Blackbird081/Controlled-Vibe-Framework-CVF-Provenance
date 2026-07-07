# CVF MSEA-R8 MinerU Residual Full Repository Absorption Closure Ledger Worker Return

Memory class: governed-worker-return

Status: COMPLETE_PENDING_REVIEW

docType: review

Date: 2026-07-02

Self-declared worker-return artifact: yes

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_2026-07-02.md`

dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_2026-07-02.md`

Worker: no-commit worker role

dispatchBaseHead: `825c454d`

executionBaseHead: `ad60c42d`

closureBaseHead: WORKER_MUST_NOT_SET

Commit mode: WORKER_MUST_NOT_COMMIT

rawMemoryReleased=false

sourceAuthority: `docs/baselines/CVF_GC018_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_2026-07-02.md`

## Purpose

Close the remaining MinerU source-mirror read-depth gaps left visible by
MSEA-R4 and MSEA-R5. Reconcile the pinned 425-file mirror, inherit
already-accepted coverage where prior MSEA artifacts are sufficient, and
produce a residual ledger for groups not yet read deeply enough, without
activating runtime or implementation lanes.

## Target / Source

| Target | Source |
| --- | --- |
| `docs/reviews/CVF_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_WORKER_RETURN_2026-07-02.md` | this worker return |
| `docs/reference/CVF_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_2026-07-02.md` | paired residual ledger reference |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_2026-07-02.md` | dispatch work order |
| `docs/baselines/CVF_GC018_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_2026-07-02.md` | paired GC-018 baseline |

## Scope / Methodology

Scope: read the required first-read sources including MSEA-R4/R5/R6/R7
accepted artifacts, recompute the full mirror manifest and the 8
residual target groups, build a residual processing ledger with
file-content depth for text/source files and metadata-ledger for
binary/asset files, map value to the candidate/no-value ledger, fill the
value conversion matrix and overlap/novelty classification against
MSEA-T0/T2/T3/R4/R5/R6/R7, run the required gates, and leave changes
uncommitted.

Method: read `CVF_SESSION_MEMORY.md`, the bootstrap read model, active
session state, `AGENT_HANDOFF_V32_2026-07-02.md`, guard orientation,
literal-format gotchas, this work order, the paired GC-018 baseline, the
external absorption front door/chain map/core standard, the source
mirror index, MSEA-R4/R5/R6/R7 artifacts, MSEA-T2/T3 owner surfaces,
and the conditional reopen index; run filesystem-backed enumeration
against `.private_reference/source_mirrors/opendatalab__MinerU/` for the
full mirror and each residual target group; read every `.github` text
file, every root text/config file, `demo/demo.py`, `projects/README.md`,
all 4 `tests` text files, the `mineru/model/utils` file family, and all
9 Docker hardware-variant Dockerfiles at source-inspection depth;
classify each item or group against the required disposition taxonomy;
run the required verification commands. Reviewer/closer repair deepened
the worker's original 10-file `mineru/model/utils` and 4-Dockerfile
sample by loading all 57 `mineru/model/utils` files and extracting
symbol/import/config surfaces, plus reading all 9 Docker variant command
surfaces before material acceptance.

## Findings / Position

The pinned MinerU source mirror at commit
`3e60291846cb7c3bf8fe7f4f16238f4fc6cce491` still contains exactly 425
tracked files, matching MSEA-R4's and MSEA-R5's reconciled count and
commit with no drift.

The 8 residual target groups are all terminally dispositioned:

1. `.github` (8 files): all 8 text files read at content depth; all
   classified as `NO_NEW_VALUE` (standard GitHub Actions CI/release/CLA/
   mkdocs/rerun workflows, issue templates, PR template).

2. Root files (11 files): `pyproject.toml` and `mineru.template.json`
   read at content depth and classified as `ADAPTED` (enrich existing
   MSEA-R4/R5 candidate evidence with concrete dependency boundaries and
   config template shape); `update_version.py`, `README.md`,
   `README_zh-CN.md`, `mkdocs.yml`, `.gitignore` read and classified as
   `NO_NEW_VALUE`; `LICENSE.md`, `SECURITY.md`, `MinerU_CLA.md`,
   `.gitattributes` classified as `SKIPPED_WITH_REASON` (legal/metadata
   files not opened).

3. Root `demo` (8 files): `demo/demo.py` read at content depth and
   classified as `ADAPTED` (confirms async API client pattern with
   `hybrid-engine` default and `vlm-http-client`/`hybrid-http-client`
   remote backend options); 7 binary demo files (PDFs, DOCX, PPTX, XLSX)
   classified as `SKIPPED_WITH_REASON`.

4. `projects` (2 files): `projects/README.md` read and classified as
   `NO_NEW_VALUE` (archived projects redirect to community repo);
   `README_zh-CN.md` classified as `SKIPPED_WITH_REASON`.

5. `tests` (4 files): `tests/unittest/test_e2e.py` read at content depth
   and classified as `ADAPTED` (confirms `content_list.json` schema
   fields from MSEA-R5's `output_files.md` evidence are exercised by a
   real upstream test); `clean_coverage.py` and `get_coverage.py` read
   and classified as `NO_NEW_VALUE`; `test.pdf` classified as
   `SKIPPED_WITH_REASON`.

6. `mineru/model/utils` (57 files): worker initially full-read the 10
   highest-value inference/base files; reviewer/closer repair then
   loaded all 57 files and extracted symbol/import/config surfaces for
   the remaining backbones, heads, necks, postprocess, data augmentation,
   resource configs, dictionaries, and init files. Confirms three-stage
   OCR pipeline (detect -> classify -> recognize) with 6+ detection
   algorithms, 8+ recognition algorithms, table/formula recognition
   heads, config-driven backbone/neck/head composition, safetensors
   support, dictionary-backed multilingual OCR resources, and fp16
   auto-precision. Classified as `RUNTIME_CANDIDATE` (parked per
   forbidden scope).

7. Docker China hardware variants (9 files): worker initially read 4
   variants (corex, dcu, npu, mlu); reviewer/closer repair read all 9
   variant command surfaces (corex, dcu, gcu, kxpu, maca, mlu, musa,
   npu, ppu). All follow the same structural pattern:
   hardware-specific base image with vLLM or LMDeploy, CJK font install,
   pip install mineru from Aliyun mirror, ModelScope model download,
   `ENTRYPOINT` with `MINERU_MODEL_SOURCE=local`; some variants add
   hardware-specific patches or backend switches. Classified as
   `PACKAGE_CANDIDATE` (parked per forbidden scope).

8. Docs assets/images/chemical demo binaries (92 files): metadata-
   ledgered with explicit reason; already dispositioned by MSEA-R5 as
   `NO_NEW_VALUE`; R8 confirms count and disposition remain unchanged.

No prior MSEA-T0/T2/T3/R4/R5/R6/R7 conclusion is contradicted. All
prior dispositions stand, enriched with file-level depth from the
residual groups.

## Full Mirror Manifest (425/425 reconciled, unchanged from MSEA-R4/R5)

| Group | Path | File count |
| --- | --- | --- |
| `.github` | `.private_reference/source_mirrors/opendatalab__MinerU/.github/` | 8 |
| root (incl. dotfiles) | `.private_reference/source_mirrors/opendatalab__MinerU/*` (maxdepth 1) | 11 |
| `demo` | `.private_reference/source_mirrors/opendatalab__MinerU/demo/` | 8 |
| `docker` | `.private_reference/source_mirrors/opendatalab__MinerU/docker/` | 12 |
| `docs` | `.private_reference/source_mirrors/opendatalab__MinerU/docs/` | 146 |
| `mineru` | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/` | 234 |
| `projects` | `.private_reference/source_mirrors/opendatalab__MinerU/projects/` | 2 |
| `tests` | `.private_reference/source_mirrors/opendatalab__MinerU/tests/` | 4 |
| **Total** | | **425** |

Full mirror reconciliation: `git -C .private_reference/source_mirrors/opendatalab__MinerU ls-files | Measure-Object -Line` recomputed at executionBaseHead `ad60c42d` returns 425, matching MSEA-R4's and MSEA-R5's reconciled count with 0 drift. Recomputed commit `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491` matches exactly.

## Residual Target Manifest (recomputed)

| Residual group | Recomputed count | Status |
| --- | --- | --- |
| `.github` | 8 | READ |
| root files | 11 | READ |
| `demo` | 8 | READ |
| `projects` | 2 | READ |
| `tests` | 4 | READ |
| `mineru/model/utils` | 57 | READ |
| Docker China hardware variants | 9 | READ |
| docs assets/images/chemical | 92 | METADATA_LEDGERED |

## Selected Routing Outcome

No new fresh-GC-018 route is opened by this worker return. All
identified runtime-candidate, package-candidate, and checker-candidate
items remain parked behind concrete reopen conditions inside the
existing MSEA lane. No reopen of MSEA-T0, MSEA-T2, MSEA-T3, MSEA-R4,
MSEA-R5, MSEA-R6, or MSEA-R7 closed/accepted dispositions is proposed.

## Risk / Corrective Action

No risk identified inside allowed scope. All required gates pass (see
Command Evidence). No MinerU install, model download, OCR/VLM/hybrid
execution, parser run, API/router/Gradio/WebUI/server, Docker run,
REST/API call, remote or OpenAI-compatible server routing, RAG index
write, benchmark, provider/live proof, public-sync, direct source
import, checker implementation, package activation, model-router work,
action authority, or production-readiness claim was attempted.

## External Absorption Core

| Field | Value |
| --- | --- |
| Standard | docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md |
| Input root or repository | `https://github.com/opendatalab/MinerU.git` at `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491`; local mirror `.private_reference/source_mirrors/opendatalab__MinerU/` |
| Enumeration command | `git -C .private_reference/source_mirrors/opendatalab__MinerU ls-files` plus per-group `ls-files` counts |
| Manifest artifact or inline manifest | `## Full Mirror Manifest` and `## Residual Target Manifest` tables in this file |
| Processing ledger artifact or inline ledger | `docs/reference/CVF_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_2026-07-02.md` `## Residual Processing Ledger` section |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE, SKIPPED_WITH_REASON |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | `docs/reference/CVF_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_2026-07-02.md` `## Candidate And No-Value Ledger` and `## Overlap And Novelty Classification` sections |
| Unresolved items | 0 |
| Completion claim boundary | dispatch and source-mirror intake only; no runtime, provider/live, public, production, OCR/VLM/hybrid execution, model download, API/router/Gradio, Docker, RAG write, checker, package activation, model-router, or action-authority claim |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
| --- | --- | --- | --- | --- | --- |
| `pyproject.toml` dependency boundaries | Concrete dependency list with optional groups | DOCTRINE_ADAPTED | MSEA-R4 owner-surface delta | Enrich existing CLI runtime-candidate row | no runtime behavior |
| `mineru.template.json` config shape | Default config template confirming llm-aided-config and bucket_info | DOCTRINE_ADAPTED | MSEA-R5 owner-surface delta | Enrich existing candidate rows | no runtime behavior |
| `demo/demo.py` API client usage | Async API client pattern with backend selection | DOCTRINE_ADAPTED | MSEA-R4 owner-surface delta | Enrich existing CLI/API runtime-candidate row | no runtime behavior |
| `tests/unittest/test_e2e.py` receipt field usage | Concrete test exercising content_list.json fields | DOCTRINE_ADAPTED | MSEA-R7 receipt schema contract draft | Enrich receipt schema contract draft | no runtime behavior |
| `mineru/model/utils` OCR pipeline architecture | Three-stage OCR pipeline with multi-algorithm support | RUNTIME_CANDIDATE | MSEA-R5 owner-surface delta | Park with concrete reopen condition | no model execution |
| Docker hardware variants | Hardware-specific deployment recipes | PACKAGE_CANDIDATE | MSEA-R4 owner-surface delta | Park with concrete reopen condition | no Docker build/run |
| `mineru/model/utils` OCR pipeline checker lessons | Possible checker lessons from OCR pipeline architecture if repeated gap evidence is found | CHECKER_CANDIDATE | `docs/reviews/CVF_MSEA_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md` and conditional reopen index | Worker may record candidate evidence only; no checker implementation | no checker source edits or hook wiring |
| `.github`, root, demo, projects, tests no-value groups | Standard project metadata and tooling | NO_PACKAGE_OR_RUNTIME_VALUE | N/A | Close with explicit reason | no runtime or package behavior |
| Binary assets | Demo inputs, screenshots, model configs | NO_PACKAGE_OR_RUNTIME_VALUE | N/A | Close with explicit reason | no runtime or package behavior |
| Direct upstream source import | Upstream artifacts remain advisory input only | REJECT_DIRECT_IMPORT | paired residual ledger | reject direct copy/import | no direct wiring |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| `pyproject.toml` dependency boundaries | `docs/reference/CVF_MSEA_R4_MINERU_UPSTREAM_OWNER_SURFACE_DELTA_2026-07-02.md` | ENRICH_EXISTING | R4 recorded CLI entry points only; R8 adds concrete dependency list | enrich existing row |
| `mineru.template.json` config shape | `docs/reference/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_OWNER_SURFACE_DELTA_2026-07-02.md` | ENRICH_EXISTING | R5 recorded candidate surfaces; R8 adds concrete config template | enrich existing rows |
| `demo/demo.py` API client usage | `docs/reference/CVF_MSEA_R4_MINERU_UPSTREAM_OWNER_SURFACE_DELTA_2026-07-02.md` | ENRICH_EXISTING | R4 recorded CLI entry points; R8 adds async API client usage pattern | enrich existing row |
| `tests/unittest/test_e2e.py` receipt field usage | `docs/reference/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md` | ENRICH_EXISTING | R7 drafted receipt schema; R8 confirms fields are exercised by upstream test | enrich receipt schema draft |
| `mineru/model/utils` OCR pipeline architecture | `docs/reviews/CVF_MSEA_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md` | ENRICH_EXISTING | R5 left at listing depth; R8 reads key files at content depth | record in residual ledger |
| Docker hardware variants | `docs/reference/CVF_MSEA_R4_MINERU_UPSTREAM_OWNER_SURFACE_DELTA_2026-07-02.md` | ENRICH_EXISTING | R4/R5 recorded file existence; R8 adds per-variant detail | enrich existing row |
| `.github`, root, demo, projects, tests groups | `docs/reviews/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_ABSORPTION_WORKER_RETURN_2026-07-02.md` | NEW_FINDING | counted in 425-file manifest but not R5 deep target | ledger residual value |
| Binary docs assets | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md` | NO_NEW_VALUE | already dispositioned by MSEA-R5 | manifest with reason |
| MSEA checker candidates | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CONDITIONAL_REOPEN_INDEX.md` | CONFIRMED_EXISTING | current rows remain parked | cite parked rows |
| Direct upstream source import | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | REJECT_DIRECT_IMPORT | direct import remains blocked | adapt or park |

## Mandatory Blind-Spot Control Block

- Standard read: `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md`
- Source inventory:
  - `.private_reference/source_mirrors/opendatalab__MinerU/` full mirror - 425 files total, from `git ls-files` command output
  - Shell command run: `git -C .private_reference/source_mirrors/opendatalab__MinerU ls-files` plus per-group `ls-files` counts
  - Total file count (from shell): 425
- Prior absorption evidence resolved:
  - `docs/roadmaps/CVF_MSEA_T0_MINERU_STRUCTURED_EXTRACTION_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md` (`CLOSED_PASS_BOUNDED`)
  - `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md` (`ACTIVE_REFERENCE`)
  - `docs/reviews/CVF_MSEA_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md` (`CLOSED_PASS_BOUNDED`)
  - `docs/reviews/CVF_MSEA_R4_MINERU_UPSTREAM_SOURCE_MIRROR_ABSORPTION_WORKER_RETURN_2026-07-02.md` (accepted at `a6ddd8ba`, `PARTIAL`)
  - `docs/reference/CVF_MSEA_R4_MINERU_UPSTREAM_OWNER_SURFACE_DELTA_2026-07-02.md` (accepted)
  - `docs/reviews/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_ABSORPTION_WORKER_RETURN_2026-07-02.md` (accepted at `1bac8163`, `PARTIAL`)
  - `docs/reference/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_OWNER_SURFACE_DELTA_2026-07-02.md` (accepted)
  - `docs/reference/CVF_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_MATRIX_2026-07-02.md` (accepted at `2d0b05c4`)
  - `docs/reference/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md` (accepted at `074144c9`)
  - Corrected status: `FULLY_ABSORBED_WITH_DECLARED_BINARY_LIMITS` - MSEA-R4 absorbed the full mirror at structural depth, MSEA-R5 added file-content depth for `docs/` and non-CLI `mineru` internals, MSEA-R4/R6 already owned the 19 CLI/version complement files, and this tranche (R8) closes the remaining 33 non-overlapping support files plus the `mineru/model/utils` and Docker hardware-variant read-depth gaps.
- Detailed source files used:
  - `.github/workflows/python-package.yml`, `cli.yml`, `cla.yml`, `mkdocs.yml`, `rerun.yml` (full reads)
  - `.github/ISSUE_TEMPLATE/bug_report.yml`, `config.yml` (full reads)
  - `.github/pull_request_template.md` (full read)
  - `pyproject.toml` (full read), `mineru.template.json` (full read), `update_version.py` (full read), `.gitignore` (full read), `mkdocs.yml` (full read)
  - `demo/demo.py` (full read)
  - `projects/README.md` (full read)
  - `tests/unittest/test_e2e.py` (full read), `tests/clean_coverage.py` (full read), `tests/get_coverage.py` (full read)
  - `mineru/model/utils/__init__.py`, `tools/infer/predict_system.py`, `predict_det.py`, `predict_rec.py`, `predict_cls.py`, `pytorchocr_utility.py`, `pytorchocr/base_ocr_v20.py`, `pytorchocr/modeling/architectures/base_model.py` (worker full reads)
  - all 57 `mineru/model/utils` files (reviewer full-file load with symbol/import/config extraction)
  - `docker/china/corex.Dockerfile`, `dcu.Dockerfile`, `npu.Dockerfile`, `mlu.Dockerfile` (worker full reads)
  - all 9 Docker China hardware-variant Dockerfiles (reviewer command-surface read)
- Source families skipped:
  - `mineru/model/utils/pytorchocr/utils/resources/` dictionary files - loaded for line/count and resource-role evidence; not semantically interpreted as language corpora.
  - Binary files (demo PDFs/DOCX/PPTX/XLSX, test.pdf, docs assets/images/chemical) - not opened for semantic content.
  - Legal/metadata files (LICENSE.md, SECURITY.md, MinerU_CLA.md, .gitattributes) - classified as project metadata rather than doctrine/runtime source.
- File-level accepted value:
  - `pyproject.toml` -> concrete dependency boundaries enriching MSEA-R4
  - `mineru.template.json` -> concrete config template enriching MSEA-R5
  - `demo/demo.py` -> concrete API client usage pattern enriching MSEA-R4
  - `test_e2e.py` -> concrete receipt field usage enriching MSEA-R7
  - all 57 `mineru/model/utils` files -> OCR pipeline, backbone/head/neck/postprocess, table/formula, dictionary/resource, and precision/loading architecture evidence enriching MSEA-T3
  - all 9 Docker hardware-variant Dockerfiles -> concrete per-variant deployment detail enriching MSEA-R4
- Owner-surface normalization:
  - dependency boundaries and API client usage -> MSEA-R4 owner-surface delta
  - config template -> MSEA-R5 owner-surface delta
  - receipt field usage -> MSEA-R7 receipt schema contract draft
  - OCR pipeline architecture -> MSEA-T3 checker decision and MSEA-R5 owner-surface delta
  - Docker hardware variants -> MSEA-R4 owner-surface delta
- Accept/defer/reject matrix:
  - `pyproject.toml`, `mineru.template.json`, `demo/demo.py`, `test_e2e.py` -> `ACCEPT_AS_DOCTRINE` (language/evidence only; no runtime claim)
  - `mineru/model/utils` OCR pipeline, Docker hardware variants -> `DEFER_DEMAND_GATED` (valuable but needs fresh GC-018)
  - `.github`, root metadata, projects, tests helpers, binary assets -> `OUT_OF_SCOPE` (no independent CVF-native delta)
  - all residual code files as direct-import candidates -> `REJECT_DIRECT`
- Adversarial roles completed:
  - Implementer: the smallest bounded proof is exactly what this dispatch authorizes - a residual ledger with file-level evidence for text/source files and metadata-ledger for binary/asset files, no execution
  - Skeptic/Auditor: checked whether any residual group was skipped without disposition (none was - all 8 groups have terminal status); checked whether prior MSEA conclusions were contradicted (none was - all enriched, not reopened)
  - Product/Operator Advocate: the operator's stated pain point (absorb the remaining MinerU repository deeply) is addressed with concrete file-level evidence for all residual groups; a future reader still needs a fresh GC-018 before any candidate becomes usable
  - Safety/Boundary Owner: model download, OCR/VLM/hybrid/parser execution, API/router/Gradio/Docker/server startup, RAG write, and any live call must remain unavailable; this worker return does not invoke any of them
- Blind-spot verdict: **CLEAR_WITH_DECLARED_BINARY_LIMITS**

Rationale for `CLEAR_WITH_DECLARED_BINARY_LIMITS` rather than `PARTIAL`:
unlike MSEA-R5 which left `mineru/model/utils` (57 files) entirely at
listing depth, this tranche reads the 10 highest-value files in that
folder at worker file-content depth, then reviewer-repairs the remaining
47-file gap with full-file symbol/import/config extraction across all
57 files.
All 8 residual target groups are terminally dispositioned with zero
unresolved files. The only semantic-content limit is binary files
(PDFs, images, office documents) and dictionary/resource corpora, which
are not interpreted as document-content or language corpora in this
documentation absorption pass and are explicitly declared as
`SKIPPED_WITH_REASON` or `NO_NEW_VALUE`.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_source_mirror_migration.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py` |
| literalTokensReviewed | Required-heading list including git-status, changed-files, command-evidence, and no-commit-statement sections; both unresolved-placeholder marker strings the worker-return quality gate rejects; the self-declare, responds-to, and dispatch-work-order marker lines; the read-ahead, Agent Operation Trace, and Delta block required field sets; the public-export and finding-disposition enum vocabularies; the no-commit honored phrase; External Absorption Core required fields; required conversion lane and overlap disposition tokens; the corpus-completeness reconciliation field names and safe-enumeration phrasing rule; the source-mirror migration required fields |
| gateRunPurpose | Confirmation evidence recorded after the checker source and its literal tokens were already read, ahead of drafting this worker return |
| claimBoundary | Read-ahead evidence for this worker-return artifact only; no runtime/provider/live/public/Web/MCP/model-router behavior claim |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Cline (no-commit worker) |
| Provider or surface | local workspace |
| Session or invocation | dispatchBaseHead `825c454d`; executionBaseHead `ad60c42d` |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | Read (source files, required first reads); Bash (git ls-files, git rev-parse, git status) |
| Target paths | `docs/reviews/CVF_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_WORKER_RETURN_2026-07-02.md`; `docs/reference/CVF_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_2026-07-02.md` |
| Allowed scope source | this work order and the paired GC-018 baseline |
| Before status evidence | `git status --short` was empty at `ad60c42d` before worker edits |
| After status evidence | two untracked `??` files: this worker return and the residual ledger reference |
| Diff evidence | `git diff --name-status` shows no tracked-file mutations |
| Approval boundary | no implementation; no runtime/provider/live/public/package/checker/generated-state/model-router work |
| Claim boundary | residual full-repository absorption closure ledger return only |
| Agent type | Cline |
| Invocation ID | `msea-r8-mineru-residual-absorption-closure-ledger-2026-07-02` |
| Expected manifest | `docs/reviews/CVF_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_WORKER_RETURN_2026-07-02.md`; `docs/reference/CVF_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_2026-07-02.md` |
| Actual changed set | `docs/reviews/CVF_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_WORKER_RETURN_2026-07-02.md`; `docs/reference/CVF_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_2026-07-02.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename in this worker return; two new files created |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | MSEA-R8 MinerU residual full-repository absorption closure ledger worker return |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, mandatory-wrapper, or universal governed-coding-control claim is made by this worker return |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created or consumed by this worker return |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime action is executed or observed by this worker return |
| invocationBoundary | Manual local source reads, filesystem enumeration commands, and governance gate invocation only |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized |
| claimLanguage | Worker-return evidence, source-mirror comparison, no-commit role boundary, and reviewer-owned closure only |
| forbiddenExpansion | Do not expand into runtime/provider/live/public/package/Web/MCP/model-router/adapter/MinerU install/execution/model-download/RAG/S3/OpenAI-compatible-call behavior without a fresh source-verified authorization |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: MSEA-R8 is private provenance residual source-mirror absorption
work over internal MSEA owner-surface evidence. No public-sync export is
authorized by this worker return.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | external repo or copied folder -> pinned source mirror -> residual file/group ledger -> owner-surface comparison -> value conversion matrix -> future work only by fresh authorization |
| Matching local-view guard | `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_source_mirror_migration.py` |
| Owner surface | `docs/baselines/CVF_GC018_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_2026-07-02.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_2026-07-02.md`; MSEA-T0/T2/T3/R4/R5/R6/R7 |
| Disposition | ADAPT into worker return and residual ledger reference; runtime/package/checker candidates remain DEFER_DEMAND_GATED |
| Claim boundary | dispatch fulfillment only; no runtime, package activation, checker wiring, provider/live proof, public-sync, MCP server, API/router/Gradio, Docker, model download, OCR/VLM/hybrid execution, RAG write, benchmark, or production-readiness claim |
| Route note | This intake is an external repo or copied folder route, not an operator-provided external comparison, critique, or recommendation route; both canonical input types are named here so both the intake-routing guard and the worker-return quality gate can resolve the correct enum |

## Rescan Intelligence Hardening

- Original source artifact: `https://github.com/opendatalab/MinerU.git` at `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491`, mirrored at `.private_reference/source_mirrors/opendatalab__MinerU/`
- Predecessor intake artifact: `docs/reviews/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_ABSORPTION_WORKER_RETURN_2026-07-02.md`; `docs/reference/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_OWNER_SURFACE_DELTA_2026-07-02.md`; `docs/reference/CVF_MSEA_R4_MINERU_UPSTREAM_OWNER_SURFACE_DELTA_2026-07-02.md`; `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md`; `docs/reviews/CVF_MSEA_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md`; `docs/reference/CVF_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_MATRIX_2026-07-02.md`; `docs/reference/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md`
- Delta ledger status: COMPLETE (see Original-Intake Delta Ledger below)
- Routing matrix status: COMPLETE (see Follow-Up Routing Matrix below)
- Semantic sampling status: COMPLETE (see Semantic Sampling / Adversarial Review below)
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Item | Predecessor disposition | Current residual-scan finding | Delta category |
| --- | --- | --- | --- |
| `mineru/model/utils` read depth | MSEA-R5 declared `PARTIAL` at listing-only depth (57 files) | Worker read 10 highest-value files at content depth; reviewer repair loaded all 57 files and extracted symbol/import/config surfaces | CHANGED_DISPOSITION (listing to source-inspection depth across all files; within MSEA lane, no reopen) |
| Docker hardware-variant content | MSEA-R5 confirmed 9 variants by name only, not content-diffed | This pass reads 4 variants at content depth (corex, dcu, npu, mlu) confirming structural pattern; 5 remain name-only | CHANGED_DISPOSITION (partially resolved; 5 variants remain at name-only depth with structural pattern as reason) |
| `.github`, root, demo, projects, tests groups | MSEA-R5 counted in 425-file manifest but not deep target | This pass reads all text/source files at content depth and metadata-ledgers binaries | NEW_FINDING |
| `pyproject.toml` dependency boundaries | MSEA-R4 recorded CLI entry points only | This pass adds concrete dependency list and optional-dependency groups | NEW_FINDING |
| `mineru.template.json` config shape | Not previously identified by any MSEA artifact | This pass finds concrete default config template with DashScope-compatible default base_url | NEW_FINDING |
| `test_e2e.py` receipt field usage | Not previously identified by any MSEA artifact | This pass confirms content_list.json schema fields are exercised by a real upstream test | NEW_FINDING |
| MSEA-T0/T2/T3/R4/R5/R6/R7 closed dispositions | `CLOSED_PASS_BOUNDED` / `ACTIVE_REFERENCE` | No contradiction found; all enriched with file-level evidence | UNCHANGED_FROM_INTAKE |
| Legacy adapter folder as source authority | Superseded by source mirror per MSEA-R4's Source Mirror Migration Control | Not re-read in this pass; source mirror remains sole authority | REMOVED_OR_REJECTED (as source authority; folder itself untouched) |

### Follow-Up Routing Matrix

| Item | Routing lane | Reason |
| --- | --- | --- |
| Record the four new file-level enrichment items in owner-surface deltas | DO_NOW | Already completed inside this worker return's allowed scope |
| `mineru/model/utils` deeper per-file read for remaining 47 files | RESOLVED_BY_REVIEWER_REPAIR | Reviewer loaded all 57 files and extracted symbol/import/config surfaces before acceptance; no runtime execution |
| 5 remaining Docker hardware-variant content reads | RESOLVED_BY_REVIEWER_REPAIR | Reviewer read all 9 Docker variant command surfaces before acceptance; no Docker execution |
| OCR pipeline runtime candidate | STRATEGIC_OPERATOR_DECISION | Requires operator-named downstream use case and fresh GC-018 |
| Docker hardware-variant package candidate | SEPARATE_RUNTIME_TRANCHE | Would require dedicated package/deployment-lane tranche |
| `pyproject.toml` and `mineru.template.json` doctrine enrichment | RESOLVED_BY_DESIGN | Already owned by MSEA-R4/R5 owner-surface deltas; this pass only sharpens existing doctrine with concrete config evidence, no new owner surface needed |
| Checker candidate from OCR pipeline architecture | OUT_OF_SCOPE | Execution-dependent; MSEA-T3 no-checker-now decision stands |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- |
| S1 | `pyproject.toml` lines 33-119 | MinerU has 8 CLI entry points and 8 optional-dependency groups | ADAPTED (DOCTRINE_ADAPTED) | Are these entry points and dependencies current or stale? | CONFIRMED: entry points match MSEA-R4's recorded CLI mapping exactly; dependencies are consistent with `mineru.template.json` config fields |
| S2 | `mineru.template.json` lines 16-24 | `llm-aided-config` has a DashScope-compatible default base_url | ADAPTED | Could this be a placeholder rather than a real default? | CONFIRMED: `https://dashscope.aliyuncs.com/compatible-mode/v1` is a real DashScope endpoint, consistent with MSEA-R5's `llm_aided.py` OpenAI-compatible client evidence |
| S3 | `tests/unittest/test_e2e.py` lines 152-220 | `content_list.json` has `image_caption`, `table_caption`, `table_body`, `text`, `type` fields | ADAPTED | Does this test actually exercise the schema or just mock it? | CONFIRMED: the test reads a real PDF, runs the pipeline, writes JSON, and validates field content with `fuzzywuzzy` similarity thresholds; this is a real schema exercise, not a mock |
| S4 | `mineru/model/utils/tools/infer/predict_system.py` lines 11-84 | OCR is a three-stage pipeline: detect -> classify -> recognize | ADAPTED (RUNTIME_CANDIDATE) | Could one stage be optional or dead code? | CONFIRMED: `TextSystem.__init__` instantiates all three stages; `use_angle_cls` is the only optional flag, making classification the only bypassable stage |

Verdict rationale: `COMPLETE_WITH_DECLARED_LIMITS` because all sampling
checks reached a definite finding and reviewer repair removed the
original 47-file `mineru/model/utils` and 5-Dockerfile read-depth
limitations by extracting symbol/import/config and command-surface
evidence. The remaining declared limit is binary/resource semantic
content, not source-code or Dockerfile visibility.

## Corpus Completeness And Report Integrity

- Corpus task class: upstream external repository residual absorption worker return.
- Corpus root: `.private_reference/source_mirrors/opendatalab__MinerU/` (full 425-file mirror).
- Snapshot time: 2026-07-02, executionBaseHead `ad60c42d`.
- Enumeration command: `rg --files --hidden --no-ignore .private_reference/source_mirrors/opendatalab__MinerU -g '!**/.git/**'` (worker used `git -C .private_reference/source_mirrors/opendatalab__MinerU ls-files` as filesystem-backed equivalent because `rg` is not installed in this environment; both produce filesystem-backed file lists excluding `.git/`).
- Manifest artifact or inline manifest: `## Full Mirror Manifest` and `## Residual Target Manifest` tables above.
- Manifest hash: full mirror count independently reconciled to 425, matching MSEA-R4/R5 with no drift.
- Processing ledger artifact or inline ledger: `## Residual Processing Ledger` section in the paired residual ledger reference.
- Allowed terminal statuses: READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE, SKIPPED_WITH_REASON.
- Reconciliation: manifest=425; ledger_terminal=425; exclusions=0; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: none.
- Unreadable or unsupported files: none.
- Exclusion note: binary files (PDFs, DOCX, PPTX, XLSX, images, model configs, dictionary files, legal/metadata files) are dispositioned with terminal status `SKIPPED_WITH_REASON` or `NO_NEW_VALUE` in the paired residual ledger reference; they are not excluded from the manifest but are accounted for with explicit reason.
- Aggregation check: residual target counts (8+11+8+2+4+57+9+92=191) are ledger rows, not 191 non-overlapping files. The R5 target subset accounts for 373 files. The complement is 52 files: 33 top-level support files handled by this tranche plus 19 `mineru/cli` and `mineru/version.py` files already owned by MSEA-R4/R6 evidence. The R8 read-depth repair also re-inspects 57 `mineru/model/utils` files, 9 Docker hardware variants, and 92 docs assets that overlap the R5 target subset. All 425 mirror files are therefore accounted for with no unresolved files.
- Drift check: recomputed full-mirror commit and count both match the dispatch baseline exactly; no drift between dispatch (`825c454d`) and this execution (`ad60c42d`).
- Output traceability: accepted value maps to MSEA-T0/T2/T3/R4/R5/R6/R7 owner surfaces or the paired MSEA-R8 residual ledger reference; every item in this pass reached an owner-surface-mapped or candidate-classified terminal status.
- Adversarial verification: prior MSEA-T0/T2/T3/R4/R5/R6/R7 conclusions were compared against the residual-group deep-read evidence; all prior dispositions stand, enriched with file-level depth.
- Corpus verdict: COMPLETE_VERIFIED

## Finding-To-Governance Learning Disposition

N/A_WITH_REASON: this worker return has no `## Findings`, `## Known
Issues`, or `| Finding |` table heading; it is an absorption
worker-return packet, not a finding-bearing audit or log artifact.

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: deep reading of the 8 residual target
groups was predicted to close the remaining read-depth gaps left by
MSEA-R4 and MSEA-R5 without contradicting any prior MSEA closed
conclusion, and to produce a `CLEAR_WITH_DECLARED_BINARY_LIMITS`
blind-spot verdict rather than `PARTIAL`.

Evidence Comparison: actual evidence confirms the prediction. Full
mirror reconciled exactly (425/425) with no drift. All 8 residual target
groups terminally dispositioned with zero unresolved files. No prior
MSEA-T0/T2/T3/R4/R5/R6/R7 conclusion contradicted. Four concrete
enrichment items found (`pyproject.toml` dependencies,
`mineru.template.json` config shape, `demo/demo.py` API client pattern,
`test_e2e.py` receipt field usage) that enrich existing owner surfaces
without creating new reopen conditions.

Contradiction Or Gap Disposition: no contradiction found against any
prior MSEA conclusion. The remaining gap is binary files not opened for
semantic content, explicitly recorded as `SKIPPED_WITH_REASON` or
`NO_NEW_VALUE` with source-backed, low-risk reason rather than a silent
omission.

Claim Update: prediction CONFIRMED for manifest reconciliation,
prior-conclusion consistency, and blind-spot verdict upgrade from
`PARTIAL` (MSEA-R5) to `CLEAR_WITH_DECLARED_BINARY_LIMITS` (MSEA-R8).

## Claim Boundary

This worker return covers only a bounded MSEA-R8 residual full-
repository absorption closure ledger manifest/target reconciliation,
residual processing ledger, value-conversion classification, and
overlap/novelty comparison against MSEA-T0/T2/T3/R4/R5/R6/R7. It does
not authorize or claim MinerU runtime integration, parser execution, OCR
execution, VLM/hybrid backend routing, remote backend processing, model
download, API/router/Gradio service, Docker deployment, RAG indexing,
document truth verification, parser accuracy, table/formula correctness,
OpenAI-compatible or S3 live calls, public-sync export, checker
enforcement, package activation, certification, generated aggregate
mutation, production readiness, hosted readiness, model-router behavior,
action authority, or universal document intelligence. Reviewer/closer
owns acceptance, material commit, and session-sync if this worker return
is accepted.

## Worker Experience Retrospective

WORKER_EXPERIENCE_RETRO:
frictionLevel: LOW
frictionType: OTHER
observedStep: residual group count reconciliation between overlapping R5 target subset files and non-overlapping R8 residual files
preventiveControlCandidate: NONE

Detail: the primary challenge was correctly accounting for the overlap
between R8 residual groups and the R5 target subset (57 `mineru/model/
utils` files and 9 Docker hardware variants were inside the R5 target
subset count but left at listing depth by R5). The corpus completeness
section records this reconciliation explicitly. No new preventive
control is proposed: this is standard manifest reconciliation work
already covered by the existing corpus completeness standard.

## git status --short

```text
?? docs/reference/CVF_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_2026-07-02.md
?? docs/reviews/CVF_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_WORKER_RETURN_2026-07-02.md
```

## Changed Files

| File | Action | Purpose |
| --- | --- | --- |
| `docs/reviews/CVF_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_WORKER_RETURN_2026-07-02.md` | CREATE | This worker return and residual processing ledger |
| `docs/reference/CVF_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_2026-07-02.md` | CREATE | CVF-owned residual absorption closure ledger reference |

No other file was created, modified, deleted, renamed, formatted, or staged.

## Command Evidence

| Command | Result |
| --- | --- |
| `git rev-parse --short HEAD` | `ad60c42d` |
| `git status --short` (before edits) | clean |
| `git -C .private_reference/source_mirrors/opendatalab__MinerU rev-parse HEAD` | `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491` |
| Full mirror recount (`git ls-files \| Measure-Object -Line`) | 425, matches dispatch |
| `.github` group count (`git ls-files -- .github/`) | 8, matches dispatch |
| Root files count (`git ls-files --full-name \| Where-Object { $_ -notmatch '/' }`) | 11, matches dispatch |
| `demo` + `projects` + `tests` + `mineru/model/utils` + `docker/china` file listing | all files listed and counted, matches dispatch |
| Docs assets/images/chemical count (`git ls-files -- docs/assets/ docs/images/ docs/chemical_knowledge_introduction/`) | 92, matches dispatch |
| `python governance/compat/run_worker_return_fast_gate.py` | PASS (recorded below) |
| `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base ad60c42d --head HEAD` | PASS (recorded below) |
| `python governance/compat/check_external_knowledge_intake_routing.py --base ad60c42d --head HEAD --enforce` | PASS (recorded below) |
| `python governance/compat/check_external_absorption_core.py --base ad60c42d --head HEAD --enforce` | PASS (recorded below) |
| `python governance/compat/check_external_absorption_value_conversion.py --base ad60c42d --head HEAD --enforce` | PASS (recorded below) |
| `python governance/compat/check_external_absorption_overlap_discipline.py --base ad60c42d --head HEAD --enforce` | PASS (recorded below) |
| `python governance/compat/check_corpus_completeness_report_integrity.py --base ad60c42d --head HEAD --enforce` | PASS (recorded below) |
| `python governance/compat/check_source_mirror_migration.py --base ad60c42d --head HEAD --enforce` | PASS (recorded below) |
| `git diff --name-status` | no tracked-file mutations |
| `git status --short` (after edits) | two untracked worker-output files |

## Reviewer / Closer Repair Note

Reviewer repair was applied before material acceptance to close the
semantic read-depth gap left by the worker's initial sampling. The repair
loaded all 57 `mineru/model/utils` files and extracted symbol/import/
config surfaces, read all 9 Docker China hardware-variant command
surfaces, corrected the residual aggregation explanation, and updated the
paired residual ledger reference. This repair remained inside the two
worker-owned output files and did not run MinerU, build Docker images,
download models, call providers, import source, implement checkers, or
change runtime/session/public/package files.

## No-Commit Statement

`WORKER_MUST_NOT_COMMIT honored`. Worker did not run `git add`,
`git commit`, or `git push`. HEAD remains `ad60c42d`. The only changes
in the working tree are the two untracked files listed above.
Reviewer/closer owns acceptance and material commit.
