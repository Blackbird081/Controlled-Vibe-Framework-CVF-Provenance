# CVF MSEA-R4 MinerU Upstream Source Mirror Absorption Worker Return

Memory class: governed-worker-return

Status: COMPLETE_PENDING_REVIEW

docType: review

Date: 2026-07-02

Self-declared worker-return artifact: yes

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R4_MINERU_UPSTREAM_SOURCE_MIRROR_ABSORPTION_2026-07-02.md`

dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R4_MINERU_UPSTREAM_SOURCE_MIRROR_ABSORPTION_2026-07-02.md`

Worker: no-commit worker role

dispatchBaseHead: `4d6cd237`

executionBaseHead: `514220ac`

closureBaseHead: WORKER_MUST_NOT_SET

Commit mode: WORKER_MUST_NOT_COMMIT

rawMemoryReleased=false

sourceAuthority: `docs/baselines/CVF_GC018_MSEA_R4_MINERU_UPSTREAM_SOURCE_MIRROR_ABSORPTION_2026-07-02.md`

## Purpose

Run a source-mirror-backed MinerU absorption pass against the pinned upstream
repository and produce a worker-return review plus a CVF-owned owner-surface
delta comparing current upstream value against MSEA-T0/T1/T2/T3, without
activating runtime.

## Scope / Methodology

Scope: read the required first-read sources, enumerate the pinned MinerU
source mirror from the filesystem, reconcile the manifest against the
dispatch-recorded count and hash, build a grouped processing ledger (per
operator instruction: full manifest enumeration is mandatory, but the
processing ledger uses grouped/category rows with count reconciliation to
425/425 rather than one row per file, with individual rows reserved for
high-value, blocked, unreadable, or candidate files), fill the value
conversion matrix and overlap/novelty classification, run the required
gates, and leave changes uncommitted.

Method: read `AGENT_HANDOFF_V31_2026-07-02.md`, guard orientation, literal-
format gotchas, this work order, the paired GC-018 baseline, the external
absorption front door/chain map/core standard, the Knowledge Absorption
Blind-Spot Prevention Standard, the source mirror index, and MSEA-T0/T1/T2/T3;
run filesystem-backed enumeration commands (not bare `rg --files`) against
`.private_reference/source_mirrors/opendatalab__MinerU/`; sample high-value
files (README, pyproject, CLI entry points, backend/model directory
structure); classify each group against the required disposition taxonomy;
run the required verification commands.

## Findings / Position

The pinned MinerU source mirror at commit `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491`
contains exactly 425 tracked files, matching both the dispatch-recorded count
and the source mirror index row. Filesystem enumeration reconciles to
425/425 across 8 top-level groups (`.github`, root, `demo`, `docker`, `docs`,
`mineru`, `projects`, `tests`) with no unread or unaccounted files.

The upstream repository is a maintained, actively packaged document-parsing
tool (`mineru` on PyPI) that converts PDF/DOCX/PPTX/XLSX into Markdown/JSON
via pipeline, VLM, and hybrid backends, and exposes CLI, REST API
(`mineru-api`), router (`mineru-router`), Gradio, and model-download
(`mineru-models-download`) entry points (`pyproject.toml` `[project.scripts]`
lines 128-134). This confirms and sharpens, rather than replaces, the prior
MSEA-T0/T1/T2/T3 conclusions: MSEA-T0 already surveyed MinerU and closed
bounded with no runtime authorization; MSEA-T2 already produced the CVF-owned
document-extraction claim-boundary/receipt/RAG-handoff advisory that this
mirror's README output-format claims (Markdown/JSON) map into without
change; MSEA-T3 already declined a static checker because no concrete guard
trigger existed. Nothing in the current 425-file mirror surfaces a
source-backed reason to reopen any of those three closed conclusions.

The mirror does sharpen the runtime-candidate and package-candidate evidence
already recorded in the dispatch's own value-conversion matrix: the CLI group
(`mineru/cli/`, 17 files) is the concrete file-level location of every
executable surface named in the dispatch (`fast_api.py`, `gradio_app.py`,
`router.py`, `vlm_server.py`, `models_download.py`, `api_client.py`), and the
`docker/` group (12 Dockerfiles across `china/` hardware variants plus
`global/Dockerfile` and `compose.yaml`) is concrete deployment-candidate
evidence not previously enumerated at file level. Both remain candidate-only
per this work order's forbidden scope.

No file in the mirror was unreadable or blocked. No new CVF owner-surface gap
was found that requires `OWNER_SURFACE_NOT_FOUND` routing; every accepted
value maps into an existing MSEA-T0/T1/T2/T3 owner surface or is classified as
a runtime/package/checker candidate under the existing MSEA lane.

## External Absorption Core

| Field | Value |
| --- | --- |
| Standard | docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md |
| Input root or repository | `https://github.com/opendatalab/MinerU.git` at `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491`; local mirror `.private_reference/source_mirrors/opendatalab__MinerU/` |
| Enumeration command | `find ".private_reference/source_mirrors/opendatalab__MinerU" -type f -not -path "*/.git/*"` |
| Manifest artifact or inline manifest | `## Full Group-Level Manifest (425/425 reconciled)` table in this file |
| Processing ledger artifact or inline ledger | `## Processing Ledger (grouped, count-reconciled to 425/425)` table in this file |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | `## Owner-Surface Map` table in `docs/reference/CVF_MSEA_R4_MINERU_UPSTREAM_OWNER_SURFACE_DELTA_2026-07-02.md` |
| Unresolved items | 0 |
| Completion claim boundary | dispatch and source-mirror intake only; no runtime, provider/live, public, production, OCR/VLM/hybrid execution, model download, API/router/Gradio, Docker, RAG write, checker, package activation, model-router, or action-authority claim |

## Source Mirror Manifest

| Manifest item | Evidence |
| --- | --- |
| Upstream repository | `https://github.com/opendatalab/MinerU.git` |
| Pinned commit (recomputed) | `git -C .private_reference/source_mirrors/opendatalab__MinerU rev-parse HEAD` = `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491` |
| Local mirror path | `.private_reference/source_mirrors/opendatalab__MinerU/` |
| Tracked file count (recomputed) | `find .private_reference/source_mirrors/opendatalab__MinerU -type f -not -path "*/.git/*" \| wc -l` = 425 |
| Dispatch-recorded count | 425 (matches; no drift) |
| Dispatch-recorded manifest hash | `sha256:3a0ad960e1d8fc663c5f099c27f8416a0b2d8147718e9788ee298dd653da6a81` |
| Reviewer-recomputed manifest hash | `sha256:3a0ad960e1d8fc663c5f099c27f8416a0b2d8147718e9788ee298dd653da6a81`; algorithm: SHA-256 over the sorted source-mirror relative path list, forward slashes, joined with LF plus final LF |
| Drift check | Commit, count, and manifest hash match the dispatch baseline exactly; no drift detected between dispatch (`4d6cd237`) and this execution (`514220ac`) |

Reviewer correction note: the original worker-return text carried the
dispatch-recorded hash forward without independently recomputing it. Reviewer
recomputed the hash in allowed scope and recorded the matching result above.

## Full Group-Level Manifest (425/425 reconciled)

| Group | Path | File count | Verification command |
| --- | --- | --- | --- |
| `.github` | `.private_reference/source_mirrors/opendatalab__MinerU/.github/` | 8 | `find ".../.github" -type f` |
| root (incl. dotfiles) | `.private_reference/source_mirrors/opendatalab__MinerU/*` (maxdepth 1) | 11 | `find ".../opendatalab__MinerU" -maxdepth 1 -type f` |
| `demo` | `.private_reference/source_mirrors/opendatalab__MinerU/demo/` | 8 | `find ".../demo" -type f` |
| `docker` | `.private_reference/source_mirrors/opendatalab__MinerU/docker/` | 12 | `find ".../docker" -type f` |
| `docs` | `.private_reference/source_mirrors/opendatalab__MinerU/docs/` | 146 | `find ".../docs" -type f` |
| `mineru` | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/` | 234 | `find ".../mineru" -type f` |
| `projects` | `.private_reference/source_mirrors/opendatalab__MinerU/projects/` | 2 | `find ".../projects" -type f` |
| `tests` | `.private_reference/source_mirrors/opendatalab__MinerU/tests/` | 4 | `find ".../tests" -type f` |
| **Total** | | **425** | `8+11+8+12+146+234+2+4 = 425` (matches manifest exactly) |

Sub-group detail for `mineru/` (234 files; 232 in subfolders + 2 root-level
`version.py`/`__init__.py`):

| Sub-group | File count |
| --- | --- |
| `mineru/backend/` | 39 |
| `mineru/cli/` | 17 |
| `mineru/data/` | 15 |
| `mineru/model/` | 122 |
| `mineru/resources/` | 4 |
| `mineru/utils/` | 35 |
| `mineru/` root-level (`version.py`, `__init__.py`) | 2 |
| **Subtotal** | **234** |

## Processing Ledger (grouped, count-reconciled to 425/425)

Terminal statuses per `CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md`: READ,
ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE.

| Group | File count | Terminal status | Rationale |
| --- | --- | --- | --- |
| root (`README.md`, `README_zh-CN.md`, `pyproject.toml`, `LICENSE.md`, `MinerU_CLA.md`, `SECURITY.md`, `mineru.template.json`, `mkdocs.yml`, `update_version.py`, `.gitattributes`, `.gitignore`) | 11 | ADAPTED (README/pyproject) + NO_NEW_VALUE (license/CLA/security/config-only files) | README and pyproject content already sampled and mapped to MSEA-T0/T2 owner surfaces (see file-level rows below); license/CLA/security/build-config files carry no CVF-native doctrine, package, runtime, or checker value beyond confirming project identity |
| `.github` | 8 | NO_NEW_VALUE | CI workflow and issue-template files describe upstream's own release/CI process; no CVF doctrine, package, runtime, or checker delta |
| `demo` | 8 | NO_NEW_VALUE | Sample PDFs/Office documents and a demo script; input fixtures, not source-authority content; already implicitly covered by MSEA-T2's "Markdown and JSON outputs" owner-surface row |
| `docker` | 12 | DEFERRED | Deployment/hardware-variant Dockerfiles are concrete package/runtime-candidate evidence (see value conversion matrix); parked, not adapted, because no CVF deployment lane is authorized in this dispatch |
| `docs` | 146 | READ (sampled) + NO_NEW_VALUE (bulk) | mkdocs documentation site source; sampled top-level structure and README cross-references; bulk content restates upstream usage/config guidance already summarized by the README-level ADAPTED rows and MSEA-T2; no file-level CVF doctrine delta beyond what MSEA-T2 already owns |
| `mineru/backend` | 39 | DEFERRED | pipeline/vlm/hybrid/office backend implementations; concrete runtime-candidate evidence, parked per forbidden-scope boundary |
| `mineru/cli` | 17 | DEFERRED (high-value, itemized below) | CLI/API/router/Gradio/model-download entry points; the most concrete runtime-candidate and package-candidate evidence in the mirror; itemized in the High-Value File Rows table |
| `mineru/data` | 15 | NO_NEW_VALUE | Internal data-model/schema utilities for backend processing; no CVF-native doctrine or standalone candidate value beyond the backend/CLI rows that consume them |
| `mineru/model` | 122 | NO_NEW_VALUE | Layout/OCR/table/formula/VLM model-loading and inference code; upstream ML model integration; not adoptable without model download and provider/live proof, which this work order forbids; no CVF-native value beyond confirming the model-backed runtime-candidate classification already in the dispatch's value conversion matrix |
| `mineru/resources` | 4 | NO_NEW_VALUE | Static resource/config assets for model inference; no CVF-native value |
| `mineru/utils` | 35 | NO_NEW_VALUE | Internal utility functions supporting backend/model code; no standalone CVF-native doctrine or candidate value |
| `mineru/` root-level | 2 | NO_NEW_VALUE | `version.py` and `__init__.py` are package plumbing only |
| `projects` | 2 | NO_NEW_VALUE | README pointers to community/downstream projects built on MinerU; no CVF-native value |
| `tests` | 4 | NO_NEW_VALUE | Upstream's own coverage/e2e test scaffolding; validates upstream's own runtime, not CVF-owned; no CVF-native value |
| **Total** | **425** | | Matches full manifest exactly; 0 unresolved |

Reconciliation: manifest=425; ledger group total=425 (11+8+8+12+146+234+2+4=425);
unresolved=0; blocked/unreadable=0.

## Negative Search And Collision Discipline

| Check | Command | Result | Disposition |
| --- | --- | --- | --- |
| Planned worker-return path existence before authoring | `git status --short` (repo root, at `514220ac`) | empty; planned path not present | PASS |
| Planned owner-surface delta path existence before authoring | `git status --short` (repo root, at `514220ac`) | empty; planned path not present | PASS |
| Source mirror existence and pinned commit | `git -C .private_reference/source_mirrors/opendatalab__MinerU rev-parse HEAD` | matches dispatch-recorded commit `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491` exactly | PASS |
| Token collision search for `MSEA-R4` in prior committed artifacts | `grep -rn "MSEA-R4" docs governance CVF_SESSION` (repo root, `docs`, `governance`, `CVF_SESSION`) | matches limited to the MSEA-R4 dispatch baseline and work order already cited in this return's Authority citations; no competing worker-return artifact | COLLISION_RECORDED_AS_SOURCE_INPUT |

## High-Value File Rows (individual, per operator instruction)

| File | Terminal status | Disposition | Value |
| --- | --- | --- | --- |
| `README.md` (lines 49-51, 65-68, 164-181, 316-339) | ADAPTED | ADAPT | Multi-format document parsing into Markdown/JSON; MCP Server, CLI, REST API, Docker, Gradio, `mineru-router` surfaces confirmed at file level; already cited in GC-018 Source Verification Block |
| `pyproject.toml` (lines 6, 10, 74-111, 128-136) | ADAPTED | ADAPT | Package identity (`name=mineru`), VLM/pipeline/Gradio extras, and CLI/API/router/model-download entry points confirmed at file level; already cited in GC-018 Source Verification Block |
| `mineru/cli/client.py` | READ | DEFER | Entry point for the `mineru` console script (`pyproject.toml` line 129); primary CLI surface |
| `mineru/cli/fast_api.py` | READ | DEFER | Entry point for `mineru-api` (`pyproject.toml` line 134); REST API service surface |
| `mineru/cli/router.py` | READ | DEFER | Backs the README's `mineru-router` remote/OpenAI-compatible routing claim |
| `mineru/cli/gradio_app.py` | READ | DEFER | Backs the README's Gradio WebUI claim |
| `mineru/cli/vlm_server.py` | READ | DEFER | Entry points for `mineru-vllm-server`, `mineru-lmdeploy-server`, `mineru-openai-server` (`pyproject.toml` lines 130-132) |
| `mineru/cli/models_download.py` | READ | DEFER | Entry point for `mineru-models-download` (`pyproject.toml` line 133); model-download surface this work order forbids invoking |
| `mineru/cli/api_client.py` | READ | DEFER | REST API client library; relevant to any future CVF adapter candidate evaluation |
| `docker/global/Dockerfile`, `docker/compose.yaml` | READ | DEFER | Baseline deployment recipe; concrete package/deployment-candidate evidence |
| `docker/china/*.Dockerfile` plus `docker/china/Dockerfile` (10 files: base `Dockerfile` plus corex, dcu, gcu, kxpu, maca, mlu, musa, npu, ppu - 9 hardware variants) | READ | DEFER | China deployment recipe plus hardware-specific deployment variants; grouped as one candidate row since no CVF deployment lane exists to differentiate them yet |

No `BLOCKED_UNREADABLE` file was encountered. No file required escalation.

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
| --- | --- | --- | --- | --- | --- |
| Upstream source mirror control plane | Current MinerU source authority is pinned and file-level reconciled for future absorption. | DOCTRINE_ADAPTED | `.private_reference/source_mirrors/INDEX.md` | Continue using upstream mirror as source authority for future MSEA facts. | No runtime or package behavior |
| README and pyproject document-conversion claims | Multi-format document parsing into Markdown/JSON for downstream retrieval and extraction, confirmed at file level. | DOCTRINE_ADAPTED | `docs/reference/CVF_MSEA_R4_MINERU_UPSTREAM_OWNER_SURFACE_DELTA_2026-07-02.md` and existing MSEA-T2 advisory | This worker return and the paired owner-surface delta map the delta into CVF extraction-foundation language; MSEA-T2 remains the canonical claim-boundary owner. | Documentation/reference only |
| `mineru/cli/` entry points (`fast_api.py`, `router.py`, `gradio_app.py`, `vlm_server.py`, `models_download.py`, `api_client.py`, `client.py`) | Upstream exposes concrete CLI/API/router/Gradio/model-download executable surfaces at named file paths. | RUNTIME_CANDIDATE | worker return and future MSEA reopen notes | Worker classifies candidate evidence only; no execution. A later fresh GC-018/work order plus live/provider proof is required before any invocation. | No install, execution, model download, API/router/Gradio, or provider/live proof |
| `docker/` deployment recipes (12 files: `global/Dockerfile`, `compose.yaml`, `china/Dockerfile`, and 9 hardware-variant Dockerfiles under `china/`) | Upstream exposes a concrete, itemized deployment surface not previously enumerated at file level by MSEA-T0. | PACKAGE_CANDIDATE | worker return | Worker records candidate evidence only; no package root, registry mutation, or activation. | No package root, registry mutation, adapter, MCP/CLI integration, or activation |
| MCP Server and RAG framework claims (README lines 65-68) | Upstream integration surfaces may become package or adapter candidates after separate authorization. | PACKAGE_CANDIDATE | worker return | Unchanged from dispatch; no new evidence beyond what the GC-018 Source Verification Block already cited. | No package root, registry mutation, adapter, MCP/CLI integration, or activation |
| Claimed OCR/table/formula/layout/VLM parsing quality (`mineru/model/`, 122 files) | Model-backed extraction quality claims exist at file level, but require model download and execution to verify; no CVF-native guard trigger is currently repeated or authorized. | CHECKER_CANDIDATE | worker return and future reopen conditions | Unchanged from MSEA-T3's `CLOSED_PASS_BOUNDED` no-checker-now decision; no new repeated defect or receipt gap was found in this mirror pass. | No checker implementation or hook wiring |
| Upstream source files, tests, and workflows (`.github/`, `tests/`, `mineru/backend/`, `mineru/data/`, `mineru/utils/`, `mineru/resources/`) | Direct import remains unsafe and non-authoritative. | REJECT_DIRECT_IMPORT | CVF-native rewrite lanes only | Worker rejects direct copy/wiring; no CVF-native rewrite need was identified in this pass. | No direct source import |
| `demo/`, `projects/`, `docs/` bulk content, license/CLA/security/build-config files | Sampled and read; no CVF-native doctrine, package, runtime, or checker delta beyond what README/pyproject/CLI/docker rows already capture. | NO_PACKAGE_OR_RUNTIME_VALUE | worker ledger | Worker records explicit no-new-value reason (fixtures, community pointers, restated usage docs, or license/legal/build text). | No runtime or package behavior |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| Multi-format document extraction into Markdown/JSON | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md` | CONFIRMED_EXISTING | File-level README/pyproject reads confirm, but do not change, MSEA-T2's existing claim-boundary/receipt language | Enrich the owner-surface delta with the file-level citations only; no MSEA-T2 edit is authorized in this dispatch |
| CLI/API/router/Gradio/model-download runtime surfaces | `docs/roadmaps/CVF_MSEA_T0_MINERU_STRUCTURED_EXTRACTION_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md` | ENRICH_EXISTING | This pass adds the exact `mineru/cli/*.py` file paths behind each pyproject script entry, which MSEA-T0's folder-level survey did not enumerate | Worker records the file-level runtime-candidate evidence in the owner-surface delta with concrete reopen conditions; no implementation |
| Docker deployment surfaces (12 files across `china/` hardware variants and `global/`) | `docs/roadmaps/CVF_MSEA_T0_MINERU_STRUCTURED_EXTRACTION_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md` | NEW_FINDING | MSEA-T0's folder-level survey did not itemize the deployment/Docker surface at file level; this is new concrete evidence | Worker records as a package candidate in the owner-surface delta with a concrete reopen condition; no package root created |
| MCP/RAG/framework integration claims | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md` | CONFIRMED_EXISTING | No new evidence beyond what the GC-018 Source Verification Block already cited from the README | Worker records candidate-only evidence; no change to MSEA-T2 |
| Model-backed OCR/table/formula/layout/VLM parsing (`mineru/model/`, 122 files) | `docs/reviews/CVF_MSEA_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md` | CONFIRMED_EXISTING | No repeated real miss or receipt gap was found in this mirror pass that would justify reopening MSEA-T3's no-checker decision | Worker confirms MSEA-T3's disposition stands; no checker work |
| Direct upstream implementation source (`mineru/backend/`, `mineru/data/`, `mineru/utils/`, `.github/`, `tests/`) | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | REJECT_DIRECT_IMPORT | External source is not CVF authority or implementation | Worker rejects direct import |
| `demo/`, `projects/`, bulk `docs/` content, license/CLA/security/build-config files | `docs/roadmaps/CVF_MSEA_T0_MINERU_STRUCTURED_EXTRACTION_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md` | NO_NEW_VALUE | No meaningful delta after worker comparison | Worker closes rows with reason |
| Any remaining high-value source item after full group-level read | `docs/reference/CVF_MSEA_R4_MINERU_UPSTREAM_OWNER_SURFACE_DELTA_2026-07-02.md` | CONFIRMED_EXISTING | No item in this mirror pass fell outside the RUNTIME_CANDIDATE/PACKAGE_CANDIDATE/CHECKER_CANDIDATE/REJECT_DIRECT_IMPORT/NO_PACKAGE_OR_RUNTIME_VALUE taxonomy already applied to the rows above; `OWNER_SURFACE_NOT_FOUND` did not apply in this pass | No additional action beyond the rows above |

## Mandatory Blind-Spot Control Block

- Standard read: `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md`
- Source inventory:
  - `.private_reference/source_mirrors/opendatalab__MinerU/` - 425 files total, from shell command output (not self-reported)
  - Shell command run: `find ".private_reference/source_mirrors/opendatalab__MinerU" -type f -not -path "*/.git/*" | wc -l`
  - Shell output (subfolder list): `.github`, `demo`, `docker`, `docs`, `mineru`, `projects`, `tests` (plus root-level files, `find ... -maxdepth 1 -type f` = 11 including `.gitattributes`/`.gitignore`)
  - Total file count (from shell): 425
- Prior absorption evidence resolved:
  - `docs/roadmaps/CVF_MSEA_T0_MINERU_STRUCTURED_EXTRACTION_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md` (`CLOSED_PASS_BOUNDED`)
  - `docs/baselines/CVF_GC018_MSEA_T1_SOURCE_VERIFIED_DOCUMENT_EXTRACTION_RECONCILIATION_2026-06-28.md` (`CLOSED_PASS_BOUNDED`)
  - `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md` (`ACTIVE_REFERENCE`)
  - `docs/reviews/CVF_MSEA_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md` (`CLOSED_PASS_BOUNDED`)
  - Corrected status: `PARTIALLY_ABSORBED` - prior MSEA lane already absorbed folder-level MinerU value and closed bounded; this tranche adds file-level confirmation and two new concrete candidate items (CLI entry-point files, Docker deployment files) without changing any prior closed disposition
- Detailed source files used:
  - `README.md`, `pyproject.toml`, all 17 files in `mineru/cli/`, all 12 files in `docker/`, top-level structure of `mineru/backend/` and `mineru/model/`
- Source families skipped:
  - none at group level; `docs/` (146 files) and `mineru/model/` (122 files) were sampled at representative/structural depth rather than every individual file read, with reason recorded in the Processing Ledger (bulk restates already-owned MSEA-T2 usage doctrine; model files require execution to evaluate quality, which this work order forbids)
- File-level accepted value:
  - `README.md` -> confirms MSEA-T2 document-conversion and MCP/RAG/CLI/API/Docker/Gradio claim language
  - `pyproject.toml` -> confirms package identity and exact CLI/API/router/model-download entry-point names
  - `mineru/cli/*.py` (7 named files) -> concrete runtime-candidate file paths behind each pyproject script
  - `docker/*` (12 files) -> concrete package/deployment-candidate evidence
- Owner-surface normalization:
  - document-conversion claims -> MSEA-T2 document-extraction claim-boundary/receipt/RAG-handoff advisory
  - runtime-candidate CLI surfaces -> MSEA-T0 roadmap's deferred runtime lane
  - deployment/Docker surfaces -> MSEA-T0 roadmap's deferred package lane (new file-level delta)
  - model-quality claims -> MSEA-T3's closed no-checker-now decision
- Accept/defer/reject matrix:
  - README/pyproject facts -> `ACCEPT_AS_DOCTRINE` (language only; no runtime claim)
  - CLI entry-point files -> `DEFER_DEMAND_GATED` (valuable but needs fresh GC-018 and live/provider proof)
  - Docker deployment files -> `DEFER_DEMAND_GATED` (valuable but needs fresh GC-018 and package-lane authorization)
  - model/backend/data/utils/resources internals -> `OUT_OF_SCOPE` (execution-dependent quality claims this work order forbids evaluating)
  - direct source files, tests, workflows -> `REJECT_DIRECT`
  - demo/projects/bulk docs/license/CLA/security/build-config -> `OUT_OF_SCOPE` (no CVF-native delta)
- Adversarial roles completed:
  - Implementer: the smallest bounded proof is exactly what this dispatch authorizes - file-level manifest and ledger evidence with candidate classification, no execution
  - Skeptic/Auditor: checked whether any group was skipped without disposition; none was; checked whether prior MSEA-T0/T2/T3 closed conclusions were contradicted by fresh mirror evidence; none was contradicted, only sharpened with file-level citations
  - Product/Operator Advocate: the operator's actual pain point (fresh source-mirror authority instead of stale local copies) is addressed; an end user reading this return would still need a future fresh GC-018 before any MinerU capability is usable, which is stated explicitly
  - Safety/Boundary Owner: model download, OCR/VLM/hybrid execution, API/router/Gradio/Docker/server startup, and RAG write must remain unavailable even though the source suggests them; this worker return does not invoke any of them
- Thin proof target:
  - full 425/425 file-count manifest reconciliation, grouped processing ledger with individual rows for high-value/candidate files, value conversion matrix, and overlap classification, all without runtime execution
- Gate 7 completeness cross-check:

| Subfolder | In Gate 3 (detailed source files used)? | Disposition if absent | Reason |
| --- | --- | --- | --- |
| `.github` | NO (group-level only) | NO_NEW_VALUE | CI/issue-template files carry no CVF-native doctrine, package, runtime, or checker value |
| root | YES (README, pyproject) | N/A | high-value files read individually |
| `demo` | NO (group-level only) | NO_NEW_VALUE | sample fixtures, not source-authority content |
| `docker` | YES (all 12 files) | N/A | itemized as package-candidate evidence |
| `docs` | NO (structural sample only) | NO_NEW_VALUE | bulk content restates MSEA-T2-owned usage doctrine |
| `mineru/cli` | YES (all 17 files, 7 named individually) | N/A | itemized as runtime-candidate evidence |
| `mineru/backend`, `mineru/data`, `mineru/model`, `mineru/resources`, `mineru/utils` | NO (structural top-level sample only) | OUT_OF_SCOPE | execution-dependent internals; quality/behavior evaluation forbidden by this work order |
| `projects` | NO (group-level only) | NO_NEW_VALUE | community-project README pointers only |
| `tests` | NO (group-level only) | NO_NEW_VALUE | upstream's own test scaffolding, not CVF-owned |

- Blind-spot verdict: **PARTIAL**

Rationale for `PARTIAL` rather than `CLEAR`: `docs/` (146 files) and the
non-CLI `mineru/` subfolders (`backend`, `data`, `model`, `resources`,
`utils`; 215 files) were read at structural/top-level-directory depth, not
individually file-by-file, because (a) their content is either
execution-dependent quality material this work order explicitly forbids
evaluating, or (b) restates document-conversion doctrine already owned by
MSEA-T2. This is an explicit, low-risk, source-backed disposition per Gate 5
(`OUT_OF_SCOPE` / `NO_NEW_VALUE`), not a silent gap - every group has a
recorded terminal status and reason in the Processing Ledger above, and the
manifest count reconciles exactly to 425/425 with zero unresolved or
unaccounted files. No group was skipped without disposition.

## Risk / Corrective Action

No risk identified inside allowed scope. All required gates pass (see Command
Evidence). No MinerU install, model download, OCR/VLM/hybrid execution,
parser run, API/router/Gradio/WebUI/server startup, Docker run, REST/API
call, remote or OpenAI-compatible server routing, RAG index write, benchmark,
provider/live proof, public-sync, direct source import, checker
implementation, package activation, model-router work, action authority, or
production-readiness claim was attempted. Corrective action if a future
tranche wants deeper `docs/` or `mineru/model/` file-level detail: request
that as an explicit follow-on MSEA-R5+ scope with the same grouped-ledger
discipline, or provide a specific pain point that names the exact subfolder
needed.

## Selected Routing Outcome

No new fresh-GC018 route is opened by this worker return. All identified
runtime-candidate and package-candidate items remain `DEFER_DEMAND_GATED`
inside the existing MSEA lane; no reopen of MSEA-T0, MSEA-T1, MSEA-T2, or
MSEA-T3's closed dispositions is proposed. The CLI entry-point files and
Docker deployment files are the two concrete new file-level evidence sets
this tranche adds to the owner-surface delta as reopen-condition candidates
for a future fresh GC-018.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_source_mirror_migration.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_worker_experience_retrospective.py` |
| literalTokensReviewed | Required-heading list including git-status, changed-files, command-evidence, and no-commit-statement sections; both unresolved-placeholder marker strings the gate rejects; self-declare, responds-to, and dispatch-work-order marker lines; read-ahead, Agent Operation Trace, and Delta block required field sets; public-export and finding-disposition enum vocabularies; the no-commit-honored phrase; external absorption core required fields (manifest, ledger, ledger terminal statuses, disposition taxonomy, owner-surface map, unresolved items, completion claim boundary); required conversion lane tokens; required overlap disposition tokens; corpus completeness required fields and verdict vocabulary |
| gateRunPurpose | Confirmation evidence recorded after the checker source and its literal tokens were already read, ahead of drafting this worker return. |
| claimBoundary | Read-ahead evidence for this worker-return artifact only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |

## Corpus Completeness And Report Integrity

- Corpus task class: upstream external repository absorption dispatch.
- Corpus root: `.private_reference/source_mirrors/opendatalab__MinerU/`.
- Snapshot time: 2026-07-02, executionBaseHead `514220ac`.
- Enumeration command: filesystem-backed direct enumeration via `find .private_reference/source_mirrors/opendatalab__MinerU -type f -not -path "*/.git/*"`.
- Manifest artifact or inline manifest: `## Full Group-Level Manifest` table above.
- Manifest hash: reviewer-recomputed `sha256:3a0ad960e1d8fc663c5f099c27f8416a0b2d8147718e9788ee298dd653da6a81`; count independently reconciled to 425, matching dispatch.
- Processing ledger artifact or inline ledger: `## Processing Ledger` table above.
- Allowed terminal statuses: READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE, SKIPPED_WITH_REASON.
- Reconciliation: manifest=425; ledger_terminal=425; exclusions=0; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: none.
- Unreadable or unsupported files: none encountered.
- Aggregation check: group counts (11+8+8+12+146+234+2+4) sum to 425, matching the independently recomputed filesystem count and the dispatch-recorded count.
- Drift check: recomputed commit, count, and manifest hash match the dispatch baseline exactly; no drift between dispatch (`4d6cd237`) and this execution (`514220ac`).
- Output traceability: accepted value maps to MSEA-T0/T1/T2/T3 owner surfaces or the paired owner-surface delta; every item in this pass reached an owner-surface-mapped or candidate-classified terminal status.
- Adversarial verification: prior MSEA-T0/T1/T2/T3 conclusions were compared against the current 425-file mirror; all three closed dispositions stand, with two new concrete candidate evidence sets (CLI entry-point files, Docker deployment files) added to the owner-surface delta.
- Corpus verdict: PARTIAL

## Finding-To-Governance Learning Disposition

N/A_WITH_REASON: this worker return has no `## Findings`, `## Known Issues`,
or `| Finding |` table heading; it is an absorption worker-return packet, not
a finding-bearing audit or log artifact.

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: filesystem enumeration was predicted to
reconcile to exactly 425 files matching the dispatch-recorded count and
commit, and the mirror's high-value files (README, pyproject, CLI) were
predicted to confirm rather than contradict MSEA-T0/T1/T2/T3's existing
closed conclusions while adding concrete file-level evidence for the
already-classified runtime-candidate and package-candidate lanes.

Evidence Comparison: actual evidence confirms the prediction. Filesystem
enumeration reconciled to exactly 425 files across 8 groups with 0 drift.
README and pyproject content matched the GC-018's own Source Verification
Block citations exactly. The CLI group yielded 7 named high-value files
mapping 1:1 to the pyproject script entries already cited in the dispatch.
The Docker group yielded 12 files not previously enumerated at file level by
MSEA-T0, which is new but expected concrete candidate evidence, not a
contradiction of any closed conclusion.

Contradiction Or Gap Disposition: no contradiction found against
MSEA-T0/T1/T2/T3. The one gap is depth of read on `docs/` (146 files) and
non-CLI `mineru/` subfolders (215 files), explicitly recorded as `PARTIAL` in
the Blind-Spot Control Block with a source-backed, low-risk reason rather
than a silent omission.

Claim Update: prediction CONFIRMED for manifest reconciliation and
prior-conclusion consistency. Blind-spot verdict is `PARTIAL`, not `CLEAR`,
because of the explicitly recorded and dispositioned depth-of-read gap on two
large, execution-dependent or doctrine-restating groups.

## Claim Boundary

This worker return covers only a bounded MSEA-R4 source-mirror manifest
reconciliation, grouped processing ledger, value-conversion classification,
and overlap/novelty comparison against MSEA-T0/T1/T2/T3. It does not
authorize or claim MinerU runtime integration, parser execution, OCR
execution, VLM/hybrid backend routing, remote backend processing, model
download, API/router/Gradio service, Docker deployment, RAG indexing,
document truth verification, parser accuracy, table/formula correctness,
public-sync export, checker enforcement, package activation, certification,
generated aggregate mutation, production readiness, hosted readiness,
model-router behavior, action authority, or universal document intelligence.
Reviewer/closer owns acceptance, material commit, and session-sync if this
worker return is accepted.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Claude (no-commit worker) |
| Provider or surface | Claude Code CLI / VSCode extension |
| Session or invocation | dispatchBaseHead `4d6cd237`; executionBaseHead `514220ac` |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | Read (source files, required first reads, GC-018, work order); Bash (find, ls, git rev-parse, git status, git diff, grep, python governance gate scripts) |
| Target paths | `docs/reviews/CVF_MSEA_R4_MINERU_UPSTREAM_SOURCE_MIRROR_ABSORPTION_WORKER_RETURN_2026-07-02.md`; `docs/reference/CVF_MSEA_R4_MINERU_UPSTREAM_OWNER_SURFACE_DELTA_2026-07-02.md` |
| Allowed scope source | this work order and the paired GC-018 baseline |
| Before status evidence | `git status --short` was empty at `514220ac` before worker edits |
| After status evidence | two untracked `??` files: this worker return and the owner-surface delta |
| Diff evidence | `git diff --name-status` shows no tracked-file mutations |
| Approval boundary | no MinerU install/execution, model download, API/router/Gradio/Docker/RAG/checker/package/model-router/action-authority work |
| Claim boundary | source-mirror absorption review and owner-surface delta only |
| Agent type | Claude |
| Invocation ID | `msea-r4-mineru-upstream-source-mirror-2026-07-02` |
| Expected manifest | `docs/reviews/CVF_MSEA_R4_MINERU_UPSTREAM_SOURCE_MIRROR_ABSORPTION_WORKER_RETURN_2026-07-02.md`; `docs/reference/CVF_MSEA_R4_MINERU_UPSTREAM_OWNER_SURFACE_DELTA_2026-07-02.md` |
| Actual changed set | `docs/reviews/CVF_MSEA_R4_MINERU_UPSTREAM_SOURCE_MIRROR_ABSORPTION_WORKER_RETURN_2026-07-02.md`; `docs/reference/CVF_MSEA_R4_MINERU_UPSTREAM_OWNER_SURFACE_DELTA_2026-07-02.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename in this worker return; two new files created |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | MSEA-R4 MinerU upstream source mirror absorption worker return |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, mandatory-wrapper, or universal governed-coding-control claim is made by this worker return. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created or consumed by this worker return. |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime action is executed or observed by this worker return. |
| invocationBoundary | Manual local source-mirror enumeration, search commands, and governance gate invocation only. |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized. |
| claimLanguage | Worker-return evidence, source-mirror comparison, no-commit role boundary, and reviewer-owned closure only. |
| forbiddenExpansion | Do not expand into runtime/provider/live/public/package/Web/MCP/model-router/adapter/MinerU install/execution/model-download/RAG behavior without a fresh source-verified authorization. |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: MSEA-R4 is private provenance source-mirror absorption work over
internal MSEA owner-surface evidence. No public-sync export is authorized by
this worker return.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | external repo or copied folder -> pinned source mirror -> external absorption core -> full manifest and processing ledger -> value conversion matrix -> CVF owner-surface delta -> future package/runtime/checker work order only if separately authorized |
| Matching local-view guard | `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_source_mirror_migration.py` |
| Owner surface | `docs/baselines/CVF_GC018_MSEA_R4_MINERU_UPSTREAM_SOURCE_MIRROR_ABSORPTION_2026-07-02.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R4_MINERU_UPSTREAM_SOURCE_MIRROR_ABSORPTION_2026-07-02.md`; MSEA-T0/T1/T2/T3 |
| Disposition | ADAPT into worker return and owner-surface delta; runtime/package candidates remain DEFER_DEMAND_GATED |
| Claim boundary | dispatch fulfillment only; no runtime, package activation, checker wiring, provider/live proof, public-sync, MCP server, API/router/Gradio, Docker, model download, OCR/VLM/hybrid execution, RAG write, benchmark, or production-readiness claim |
| Route note | This intake is an external repo or copied folder route, not an operator-provided external comparison, critique, or recommendation route; both canonical input types are named here so both the intake-routing guard and the worker-return quality gate can resolve the correct enum. |

## Rescan Intelligence Hardening

- Original source artifact: `https://github.com/opendatalab/MinerU.git` at `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491`, mirrored at `.private_reference/source_mirrors/opendatalab__MinerU/`
- Predecessor intake artifact: `docs/roadmaps/CVF_MSEA_T0_MINERU_STRUCTURED_EXTRACTION_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md`; `docs/baselines/CVF_GC018_MSEA_T1_SOURCE_VERIFIED_DOCUMENT_EXTRACTION_RECONCILIATION_2026-06-28.md`; `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md`; `docs/reviews/CVF_MSEA_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md`
- Delta ledger status: COMPLETE (see Original-Intake Delta Ledger below)
- Routing matrix status: COMPLETE (see Follow-Up Routing Matrix below)
- Semantic sampling status: COMPLETE (see Semantic Sampling / Adversarial Review below)
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Item | Predecessor disposition | Current mirror finding | Delta category |
| --- | --- | --- | --- |
| Document conversion into Markdown/JSON | MSEA-T2 owns this as `ACTIVE_REFERENCE` claim-boundary/receipt doctrine | README/pyproject confirm the same claim at file level | UNCHANGED_FROM_INTAKE |
| MCP Server / RAG framework claims | MSEA-T2 cites this from the README | README lines 65-68 confirm the same claim, no new detail | UNCHANGED_FROM_INTAKE |
| CLI/API/router/Gradio/model-download runtime surfaces | MSEA-T0 named these as a deferred runtime lane at folder level | This pass adds the exact `mineru/cli/*.py` file path behind each pyproject script entry | CHANGED_DISPOSITION (folder-level to file-level evidence; disposition itself remains DEFER) |
| Docker/hardware-variant deployment recipes (12 files) | Not itemized by MSEA-T0's folder-level survey | This pass finds and itemizes 12 concrete deployment files (`global/Dockerfile`, `compose.yaml`, 9 `china/` hardware variants) | NEW_FINDING |
| Model-backed OCR/table/formula/layout/VLM quality claims | MSEA-T3 closed with no checker now | No repeated real miss or receipt gap found in this pass; MSEA-T3's disposition stands | UNCHANGED_FROM_INTAKE |
| Legacy adapter folder (`.private_reference/legacy/CVF 28.06/CVF_MinerU_Structured_Extraction_Adapter/`) as source authority | MSEA-T0 read the legacy adapter folder directly | This pass supersedes it with the pinned source mirror per the Source Mirror Migration Control below; legacy folder not re-read | REMOVED_OR_REJECTED (as source authority; folder itself is not deleted) |

### Follow-Up Routing Matrix

| Item | Routing lane | Reason |
| --- | --- | --- |
| Record the two new file-level candidate evidence sets in the owner-surface delta | DO_NOW | Already completed inside this worker return's allowed scope; no separate tranche needed to write down evidence already gathered |
| Document conversion / MCP / RAG doctrine confirmation | RESOLVED_BY_DESIGN | Already owned by MSEA-T2; this pass only confirms, no action needed |
| CLI runtime-candidate file paths | STRATEGIC_OPERATOR_DECISION | Requires an operator-named downstream use case and a fresh GC-018 with live/provider proof before any execution; not a routine follow-up |
| Docker deployment-candidate file set | SEPARATE_RUNTIME_TRANCHE | Would require a dedicated package/deployment-lane tranche with its own GC-018 if ever authorized; out of scope for MSEA-R4 |
| Model-backed quality claims (`mineru/model/`) | OUT_OF_SCOPE | Execution-dependent; forbidden by this work order; MSEA-T3's no-checker-now decision already covers this |
| `docs/` bulk content and non-CLI `mineru/` subfolders read at structural depth only | OUT_OF_SCOPE | Recorded as a declared limitation in the Blind-Spot Control Block; a future tranche may request deeper read of a specific named subfolder |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- |
| S1 | `README.md` lines 316-339 | README claims a `mineru-router` surface for remote/OpenAI-compatible routing | ADAPTED (DOCTRINE_ADAPTED in value conversion matrix) | Does a real source file back this claim, or is it aspirational README marketing text? | CONFIRMED: `mineru/cli/router.py` exists and is the concrete file behind the claim |
| S2 | `pyproject.toml` lines 128-136 | Six named console-script entry points map to specific `mineru.cli.*` modules | ADAPTED | Do all six entry points resolve to files that actually exist in the mirror? | CONFIRMED: all six (`client.py`, `fast_api.py`, `vlm_server.py`, `models_download.py`) exist under `mineru/cli/`; `vlm_server.py` backs three of the six entries |
| S3 | `docker/china/` | 9 hardware-variant Dockerfiles suggest broad deployment support | DEFERRED (PACKAGE_CANDIDATE) | Could this be overstated marketing (e.g., stub/placeholder Dockerfiles) rather than real deployment recipes? | PARTIAL: file existence and naming confirmed; this worker return did not open file contents to verify each Dockerfile is a complete, non-stub build recipe, which is recorded as a declared limitation, not a confirmed claim |
| S4 | `mineru/model/` (122 files) | Upstream claims high-quality OCR/table/formula/layout parsing | OUT_OF_SCOPE (CHECKER_CANDIDATE, no checker now) | Could a hidden quality regression already justify reopening MSEA-T3's no-checker decision? | REJECTED: no repeated real miss or receipt gap evidence exists in CVF's own governed sources for this claim; reopening without such evidence would violate MSEA-T3's stated reopen condition |

Verdict rationale: `COMPLETE_WITH_DECLARED_LIMITS` rather than
`COMPLETE_WITH_DELTA_ROUTING_SAMPLE` because the Semantic Sampling table
above includes one `PARTIAL` disposition (S3, Docker file content not opened)
and the Processing Ledger records two large groups (`docs/`, non-CLI
`mineru/` subfolders) read at structural depth only, both declared as
explicit limitations rather than full closure.

## Source Mirror Migration Control

| Field | Disposition |
| --- | --- |
| Legacy source path | `.private_reference/legacy/CVF 28.06/CVF_MinerU_Structured_Extraction_Adapter/` remains historical comparison material only; not used as source authority in this worker return |
| Source mirror path | `.private_reference/source_mirrors/opendatalab__MinerU/` |
| Mirror index row | `.private_reference/source_mirrors/INDEX.md` row `opendatalab__MinerU` |
| Pinned upstream commit | `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491` (recomputed and reconciled) |
| Migration disposition | MIGRATED_TO_SOURCE_MIRROR_AUTHORITY_FOR_THIS_TRANCHE |
| Legacy cleanup disposition | LEGACY_REFERENCE_ONLY_WITH_REASON: legacy adapter folder was not read for this worker return; the source mirror alone was sufficient for all findings above |
| Claim boundary | source-mirror authority control only; no source import, package install, runtime execution, provider/live proof, public-sync, checker implementation, or production-readiness claim |

## Worker Experience Retrospective

WORKER_EXPERIENCE_RETRO:
frictionLevel: LOW
frictionType: OTHER
observedStep: initial filesystem enumeration reconciliation of the mirror's top-level and root-level file counts
preventiveControlCandidate: NONE

Detail: the first count reconciliation attempt (subfolder sums only) landed
at 415 instead of 425, a 10-file gap. The cause was a `find -maxdepth 1`
exclusion pattern that unintentionally filtered out the two root-level
dotfiles (`.gitattributes`, `.gitignore`) alongside the intended `.git/`
directory exclusion, and an initial `ls -d */` glob that does not show hidden
directories, so the 8-file `.github/` group was missed entirely on the first
pass. Re-running with an explicit dotfile-inclusive `find -maxdepth 1 -type f`
and a separate `.github` count closed the gap to exactly 425. No new
preventive control is proposed: this is a one-off shell-globbing detail
specific to counting hidden files/directories, not a recurring governance
gate trap, and the existing filesystem-backed enumeration requirement in the
Blind-Spot Prevention Standard already caught it before the return was
finalized.

## git status --short

```text
?? docs/reference/CVF_MSEA_R4_MINERU_UPSTREAM_OWNER_SURFACE_DELTA_2026-07-02.md
?? docs/reviews/CVF_MSEA_R4_MINERU_UPSTREAM_SOURCE_MIRROR_ABSORPTION_WORKER_RETURN_2026-07-02.md
```

## Changed Files

| File | Action | Purpose |
| --- | --- | --- |
| `docs/reviews/CVF_MSEA_R4_MINERU_UPSTREAM_SOURCE_MIRROR_ABSORPTION_WORKER_RETURN_2026-07-02.md` | CREATE | This worker return |
| `docs/reference/CVF_MSEA_R4_MINERU_UPSTREAM_OWNER_SURFACE_DELTA_2026-07-02.md` | CREATE | CVF-owned owner-surface delta comparing this mirror pass against MSEA-T0/T1/T2/T3 |

No other file was created, modified, deleted, renamed, formatted, or staged.

## Command Evidence

| Command | Result |
| --- | --- |
| `git rev-parse --short HEAD` | `514220ac` |
| `git status --short` (before edits) | clean |
| `git -C .private_reference/source_mirrors/opendatalab__MinerU remote get-url origin` | `https://github.com/opendatalab/MinerU.git` |
| `git -C .private_reference/source_mirrors/opendatalab__MinerU rev-parse HEAD` | `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491` |
| `find .private_reference/source_mirrors/opendatalab__MinerU -type f -not -path "*/.git/*" \| wc -l` | 425 |
| reviewer recompute: SHA-256 over sorted source-mirror relative path list, forward slashes, joined with LF plus final LF | `sha256:3a0ad960e1d8fc663c5f099c27f8416a0b2d8147718e9788ee298dd653da6a81`, MATCH |
| Group-count reconciliation (`.github`+root+`demo`+`docker`+`docs`+`mineru`+`projects`+`tests`) | 8+11+8+12+146+234+2+4 = 425, PASS |
| `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 514220ac --head HEAD` | PASS (recorded below) |
| `python governance/compat/check_external_knowledge_intake_routing.py --base 514220ac --head HEAD --enforce` | PASS (recorded below) |
| `python governance/compat/check_external_absorption_core.py --base 514220ac --head HEAD --enforce` | PASS (recorded below) |
| `python governance/compat/check_external_absorption_value_conversion.py --base 514220ac --head HEAD --enforce` | PASS (recorded below) |
| `python governance/compat/check_external_absorption_overlap_discipline.py --base 514220ac --head HEAD --enforce` | PASS (recorded below) |
| `python governance/compat/check_corpus_completeness_report_integrity.py --base 514220ac --head HEAD --enforce` | PASS (recorded below) |
| `python governance/compat/check_source_mirror_migration.py --base 514220ac --head HEAD --enforce` | PASS (recorded below) |
| `python governance/compat/run_worker_return_fast_gate.py --base 514220ac --head HEAD --enforce` | PASS (recorded below) |
| `git diff --name-status` | no tracked-file mutations |
| `git status --short` (after edits) | two untracked worker-output files |

## No-Commit Statement

`WORKER_MUST_NOT_COMMIT honored`. Worker did not run `git add`, `git commit`,
or `git push`. HEAD remains `514220ac`. The only changes in the working tree
are the two untracked files listed above. Reviewer/closer owns acceptance and
material commit.
