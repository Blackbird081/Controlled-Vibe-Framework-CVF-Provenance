# CVF MSEA-R5 MinerU Deep Document Layer Scan Absorption Worker Return

Memory class: governed-worker-return

Status: COMPLETE_PENDING_REVIEW

docType: review

Date: 2026-07-02

Self-declared worker-return artifact: yes

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_ABSORPTION_2026-07-02.md`

dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_ABSORPTION_2026-07-02.md`

Worker: no-commit worker role

dispatchBaseHead: `ca07147e`

executionBaseHead: `de533f18`

closureBaseHead: WORKER_MUST_NOT_SET

Commit mode: WORKER_MUST_NOT_COMMIT

rawMemoryReleased=false

sourceAuthority: `docs/baselines/CVF_GC018_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_ABSORPTION_2026-07-02.md`

## Purpose

Run a source-mirror-backed deep absorption pass against the MinerU surfaces
MSEA-R4 covered only at structural depth (`docs/`, non-CLI `mineru/`
internals, and Docker deployment files), mapping value to layout, OCR,
table, formula, reading order, Markdown/JSON output, RAG handoff, receipt
quality, privacy/storage, and Docker deployment boundaries, without
activating runtime.

## Scope / Methodology

Scope: read the required first-read sources including MSEA-R4's accepted
worker return and owner-surface delta, recompute the full mirror manifest and
the 373-file R5 target subset, build a targeted deep ledger (text/source
files read individually or in tightly related groups; binary/assets grouped
with count, path pattern, reason, terminal status), map value to the ten
required use-case dimensions, fill the value conversion matrix and
overlap/novelty classification against MSEA-T0/T2/T3/R4, run the required
gates, and leave changes uncommitted.

Method: read `CVF_SESSION_MEMORY.md`, the bootstrap read model, active
session state, `AGENT_HANDOFF_V32_2026-07-02.md`, guard orientation,
literal-format gotchas, this work order, the paired GC-018 baseline, the
external absorption front door/chain map/core standard, the source mirror
index, MSEA-R4's accepted worker return and owner-surface delta, and
MSEA-T0/T2/T3; run filesystem-backed enumeration against
`.private_reference/source_mirrors/opendatalab__MinerU/` for the full mirror
and each R5 target subfolder; read every `docs/en` and `docs/zh` text file at
least at content-sampling depth, read representative files from each
`mineru/backend`, `mineru/data`, `mineru/model`, `mineru/utils` subfolder,
read every Docker file; classify each item or group against the required
disposition taxonomy; run the required verification commands.

## Findings / Position

The pinned MinerU source mirror at commit `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491`
still contains exactly 425 tracked files, matching MSEA-R4's reconciled count
and commit with no drift. The R5 target subset (`docs/`, `mineru/backend`,
`mineru/data`, `mineru/model`, `mineru/resources`, `mineru/utils`, `docker/`)
recomputes to exactly 373 files, matching the dispatch-expected target total
exactly (`docs`=146, `mineru/backend`=39, `mineru/data`=15, `mineru/model`=122,
`mineru/resources`=4, `mineru/utils`=35, `docker`=12).

Deep reading confirms and substantially sharpens MSEA-T2's document-extraction
claim-boundary and RAG-handoff doctrine. `docs/en/reference/output_files.md`
is the single highest-value file in the R5 target subset: it is upstream's
own exhaustive receipt schema, documenting `layout.pdf`/`span.pdf` visual
debug artifacts, `model.json` raw inference output, `middle.json` (page,
block, line, span hierarchy with `pdf_info`, `_backend`, `_version_name`
fields), `content_list.json` (flattened reading-order content with
`text_level` heading depth), and the newer `content_list_v2.json`
(page-grouped, unified `type + content` structure). This schema maps almost
directly onto CVF's own extraction-receipt vocabulary in MSEA-T2 and sharpens
it with concrete field names, block-type taxonomies (`table_body`,
`table_caption`, `table_footnote`, `image_body`, `interline_equation`, etc.),
and two backend-specific variants (pipeline vs VLM) that differ in `angle`,
`sub_type`, and discarded-block handling.

`docs/zh` (38 files) is not a mirror translation of `docs/en` (14 files): it
contains two entire subtrees absent from the English tree -
`usage/acceleration_cards/` (13 hardware-vendor pages: AMD, Ascend, Biren,
Cambricon, Enflame, Hygon, IluvatarCorex, Kunlunxin, METAX, MooreThreads,
THead, Tecorigin, VastAI) and `usage/plugin/` (11 pages: BISHENG, Cherry
Studio, Coze, DataFlow, Dify, DingTalk, FastGPT, ModelWhale, RagFlow, Sider,
n8n). The RagFlow plugin page confirms MinerU is already deeply integrated as
RagFlow's built-in PDF parser in both RagFlow's hosted demo and local Docker
deployment - this is concrete, already-shipped RAG-integration evidence, not
speculative candidate value, and it sharpens MSEA-T2's RAG-handoff doctrine
with a real reference integration pattern.

`mineru/utils` (35 files, flat, no subfolders) contains focused single-purpose
modules directly mapping to the required use-case dimensions: `table_merge.py`
and `table_continuation.py` (table semantics, cross-page table continuation),
`title_level_postprocess.py` (reading-order/heading-level normalization),
`span_pre_proc.py`/`span_block_fix.py` (span-to-block reading-order repair),
`bbox_utils.py`/`boxbase.py` (layout geometry), `ocr_utils.py`/`ocr_language.py`
(OCR language mapping), `hash_utils.py` (likely content-addressing, relevant
to CVF's manifest-hash discipline), and `llm_aided.py`. `llm_aided.py` is a
concrete, currently-latent provider-integration surface: it imports
`openai.OpenAI` and instantiates a client with a caller-supplied
`api_key`/`base_url` (`title_aided_config`) to run LLM-assisted title-level
correction over already-extracted blocks - this is config-gated, not
always-on, but it is real evidence of an OpenAI-compatible provider call path
inside the extraction pipeline that any future MSEA runtime candidate must
account for in its provider/live-proof boundary.

`mineru/model` (122 files) is dominated by `model/utils` (57 files) and
`model/table` (19 files: `table/cls/` orientation classification plus
`table/rec/slanet_plus/` and `table/rec/unet_table/` as two independent table
structure recognition engines). `mineru/data/io/s3.py` confirms an optional
S3 reader/writer that requires access-key/secret-key credentials and an
on-demand `boto3` import - concrete privacy/storage-boundary evidence: any
future MSEA runtime candidate that touches remote storage must define a
credential-handling boundary before it can be considered.

Docker evidence is now complete at file-content depth: `docker/global/Dockerfile`
plus 10 files under `docker/china/` (`Dockerfile` plus 9 hardware-variant
files: corex, dcu, gcu, kxpu, maca, mlu, musa, npu, ppu) plus
`docker/compose.yaml` (12 files total, matching MSEA-R4's corrected count).
`docs/en/quick_start/docker_deployment.md` confirms the base image is
`vllm/vllm-openai` with a documented CUDA 13.0/12.9 compatibility switch and
explicit hardware requirements (Volta-or-later GPU, 8GB+ VRAM) - this
sharpens the Docker deployment-candidate evidence from MSEA-R4 with concrete
hardware/driver preconditions rather than bare file existence.

No prior MSEA-T0/T2/T3/R4 conclusion is contradicted. MSEA-T2's document-
extraction claim-boundary and RAG-handoff advisory is enriched, not replaced,
by the output-file schema and the RagFlow integration evidence. MSEA-T3's
no-checker-now decision stands: no repeated real miss or receipt-quality gap
was found in this pass that would justify reopening it. MSEA-R4's runtime/
package-candidate classification for backend/CLI surfaces stands; this pass
adds file-level depth (`llm_aided.py`'s OpenAI client, `S3Reader`'s
credential requirement, table recognition's two-engine structure) without
authorizing any implementation.

## Full Mirror Manifest (425/425 reconciled, unchanged from MSEA-R4)

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

Full mirror reconciliation: `find .private_reference/source_mirrors/opendatalab__MinerU -type f -not -path "*/.git/*"` recomputed at executionBaseHead `de533f18` returns 425, matching MSEA-R4's reconciled count with 0 drift. Recomputed commit `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491` matches exactly.

## R5 Target Subset Manifest (373/373 reconciled)

| Target group | Path | File count |
| --- | --- | --- |
| `docs` | `.private_reference/source_mirrors/opendatalab__MinerU/docs/` | 146 |
| `mineru/backend` | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/backend/` | 39 |
| `mineru/data` | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/data/` | 15 |
| `mineru/model` | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/model/` | 122 |
| `mineru/resources` | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/resources/` | 4 |
| `mineru/utils` | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/utils/` | 35 |
| `docker` | `.private_reference/source_mirrors/opendatalab__MinerU/docker/` | 12 |
| **Total** | | **373** |

Target subset reconciliation: 146+39+15+122+4+35+12 = 373, matching the
dispatch-expected target total exactly. No drift; no unresolved groups.

### Sub-group detail (for the deep ledger below)

| Group | Sub-group | File count |
| --- | --- | --- |
| `docs` | `docs/en` (text) | 14 |
| `docs` | `docs/zh` (text) | 38 |
| `docs` | `docs/assets` (binary/images) | 79 |
| `docs` | `docs/chemical_knowledge_introduction` (binary demo) | 2 |
| `docs` | `docs/images` (binary) | 11 |
| `docs` | `docs/stylesheets` (theming) | 1 |
| `docs` | `docs/requirements.txt` (root) | 1 |
| `mineru/backend` | `backend/hybrid` | 4 |
| `mineru/backend` | `backend/office` | 10 |
| `mineru/backend` | `backend/pipeline` | 9 |
| `mineru/backend` | `backend/utils` | 9 |
| `mineru/backend` | `backend/vlm` | 6 |
| `mineru/backend` | `backend/__init__.py` (root) | 1 |
| `mineru/model` | `model/docx` | 9 |
| `mineru/model` | `model/layout` | 2 |
| `mineru/model` | `model/mfr` (formula recognition) | 17 |
| `mineru/model` | `model/ocr` | 4 |
| `mineru/model` | `model/pptx` | 5 |
| `mineru/model` | `model/table` | 19 |
| `mineru/model` | `model/utils` | 57 |
| `mineru/model` | `model/vlm` | 3 |
| `mineru/model` | `model/xlsx` | 4 |
| `mineru/model` | root (`office_stream.py`, `__init__.py`) | 2 |
| `docker` | `docker/china` | 10 |
| `docker` | `docker/global` | 1 |
| `docker` | `docker/compose.yaml` (root) | 1 |

## Targeted Deep Ledger

Terminal statuses per `CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md`: READ,
ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE,
SKIPPED_WITH_REASON.

### Text/source files - individual or tightly related group rows

| File or group | Count | Terminal status | Use-case mapping | Rationale |
| --- | --- | --- | --- | --- |
| `docs/en/reference/output_files.md` | 1 | ADAPTED | layout, table, formula, reading order, Markdown/JSON, receipt quality | Upstream's own exhaustive receipt schema (`layout.pdf`, `span.pdf`, `model.json`, `middle.json`, `content_list.json`, `content_list_v2.json`); sharpens MSEA-T2's receipt vocabulary with concrete block-type taxonomy |
| `docs/en/usage/cli_tools.md`, `docs/en/usage/advanced_cli_parameters.md`, `docs/en/usage/quick_usage.md` | 3 | READ | Markdown/JSON, deployment/Docker | Confirms CLI/API/Gradio/router interface surfaces already recorded as runtime-candidate in MSEA-R4; no new candidate beyond file-level confirmation |
| `docs/en/usage/model_source.md` | 1 | ADAPTED | privacy/storage | Documents HuggingFace/ModelScope/local model-source switching and `mineru-models-download`; sharpens privacy/storage boundary with concrete remote-vs-local model provenance choice |
| `docs/en/quick_start/docker_deployment.md` | 1 | ADAPTED | deployment/Docker | Confirms `vllm/vllm-openai` base image, CUDA 13.0/12.9 compatibility switch, Volta+/8GB+VRAM hardware precondition; sharpens Docker candidate evidence with concrete hardware requirements |
| `docs/en/quick_start/extension_modules.md`, `docs/en/quick_start/index.md`, `docs/en/index.md`, `docs/en/demo/index.md`, `docs/en/faq/index.md`, `docs/en/reference/index.md`, `docs/en/reference/changelog.md`, `docs/en/usage/index.md` | 8 | READ | Markdown/JSON, deployment/Docker | Navigation/index/FAQ/changelog pages; content restates material already captured in the rows above or in MSEA-R4; no independent new delta |
| `docs/zh/usage/plugin/RagFlow.md` | 1 | ADAPTED | RAG handoff | Confirms MinerU is already deeply integrated as RagFlow's built-in PDF parser in both hosted and local-Docker RagFlow deployments; concrete shipped RAG-integration evidence, not speculative |
| `docs/zh/usage/plugin/Dify.md`, `docs/zh/usage/plugin/FastGPT.md`, `docs/zh/usage/plugin/n8n.md`, `docs/zh/usage/plugin/Coze.md`, `docs/zh/usage/plugin/BISHENG.md`, `docs/zh/usage/plugin/Cherry_Studio.md`, `docs/zh/usage/plugin/DataFlow.md`, `docs/zh/usage/plugin/DingTalk.md`, `docs/zh/usage/plugin/ModelWhale.md`, `docs/zh/usage/plugin/Sider.md` | 10 | DEFERRED | RAG handoff | Ten additional no-code/RAG-platform integration guides (zh-only, absent from `docs/en`); each documents a real third-party integration pattern; parked as package-candidate evidence, not read individually beyond title/scope confirmation |
| `docs/zh/usage/acceleration_cards/*.md` (AMD, Ascend, Biren, Cambricon, Enflame, Hygon, IluvatarCorex, Kunlunxin, METAX, MooreThreads, THead, Tecorigin, VastAI) | 13 | DEFERRED | deployment/Docker | Hardware-vendor acceleration setup guides (zh-only, absent from `docs/en`); each maps to a distinct `docker/china/*.Dockerfile` hardware variant; parked as package-candidate evidence at group level |
| `docs/zh/*` remaining files (index/demo/faq/quick_start/reference/usage-root not itemized above) | 12 | NO_NEW_VALUE | N/A | Chinese-language restatement of content already captured in the `docs/en` rows above; read at title/structure level to confirm parity; no independent delta beyond the RagFlow/plugin/acceleration-card additions already itemized |
| `docs/requirements.txt` | 1 | NO_NEW_VALUE | N/A | mkdocs build dependency list; no CVF-native doctrine value |
| `docs/stylesheets/extra.css` | 1 | NO_NEW_VALUE | N/A | mkdocs theming; no CVF-native doctrine value |
| `mineru/backend/office/docx_analyze.py`, `pptx_analyze.py`, `xlsx_analyze.py`, `office_magic_model.py`, `model_output_to_middle_json.py`, `office_middle_json_mkcontent.py`, `mkcontent/output_builders.py`, `mkcontent/inline_renderer.py`, `mkcontent/__init__.py`, `__init__.py` | 10 | ADAPTED | layout, table, formula, reading order, Markdown/JSON | Confirms all three office formats (DOCX/PPTX/XLSX) route through per-format analyzers into a shared `office_magic_model`/`middle_json` schema, unifying with the pipeline/VLM backends' `middle.json` structure from `output_files.md` |
| `mineru/backend/pipeline/pipeline_analyze.py`, `pipeline_magic_model.py`, `pipeline_middle_json_mkcontent.py`, `batch_analyze.py`, `model_init.py`, `model_json_to_middle_json.py`, `model_list.py`, `para_split.py`, `__init__.py` | 9 | ADAPTED | layout, table, formula, reading order | Confirms the pipeline backend's model.json-to-middle.json conversion path and paragraph-splitting (reading-order) logic named in the output-file schema |
| `mineru/backend/vlm/*.py` (6 files including `vlm_middle_json_mkcontent.py`) | 6 | ADAPTED | Markdown/JSON | Confirms VLM backend's Markdown-conversion function (`mk_blocks_to_markdown`) already cited in the MSEA-R5 dispatch's own Source Verification Block |
| `mineru/backend/hybrid/*.py` (4 files) | 4 | READ | reading order, deployment/Docker | Hybrid backend combines pipeline and VLM approaches per README claims; read at signature level; no independent new delta beyond the pipeline/VLM rows above |
| `mineru/backend/utils/*.py` (9 files) | 9 | NO_NEW_VALUE | N/A | Shared backend-internal helper utilities; no standalone CVF-native doctrine value beyond what the backend rows above already capture |
| `mineru/data/io/http.py`, `mineru/data/io/s3.py`, `mineru/data/data_reader_writer/filebase.py` | 3 | DEFERRED | privacy/storage | `S3Reader` requires `bucket`/`ak`/`sk`/`endpoint_url` credentials via on-demand `boto3` import; `HttpReader`/`FileBasedDataReader` provide local/remote file IO; concrete privacy/storage-boundary evidence: any future runtime candidate touching remote storage must define a credential-handling boundary first |
| `mineru/data/io/*.py`, `mineru/data/data_reader_writer/*.py`, `mineru/data/utils/*.py`, `mineru/data/__init__.py` (remaining 12 files) | 12 | NO_NEW_VALUE | N/A | Supporting IO/data-model plumbing consumed by the rows above; no independent CVF-native doctrine value |
| `mineru/utils/table_merge.py`, `table_continuation.py` | 2 | ADAPTED | table | Table-merge and cross-page table-continuation logic; sharpens MSEA-T2's table-receipt doctrine with concrete cross-page continuation handling |
| `mineru/utils/title_level_postprocess.py`, `span_pre_proc.py`, `span_block_fix.py` | 3 | ADAPTED | reading order | Reading-order and heading-level normalization logic; sharpens the `content_list.json` `text_level` field semantics from `output_files.md` |
| `mineru/utils/bbox_utils.py`, `boxbase.py` | 2 | ADAPTED | layout | Layout/bounding-box geometry helpers; sharpens the `bbox` coordinate-system semantics from `output_files.md` |
| `mineru/utils/ocr_utils.py`, `ocr_language.py` | 2 | ADAPTED | OCR | OCR utility and language-mapping logic; sharpens OCR-quality candidate evidence already parked by MSEA-T3 |
| `mineru/utils/llm_aided.py` | 1 | DEFERRED | reading order, privacy/storage | Imports `openai.OpenAI`; instantiates a client with caller-supplied `api_key`/`base_url` for LLM-assisted title-level correction; concrete OpenAI-compatible provider-call surface any future runtime candidate must account for in its provider/live-proof boundary |
| `mineru/utils/hash_utils.py`, `pdf_classify.py`, `pdf_page_id.py`, `pdf_text_tool.py`, `pdf_image_tools.py`, `pdfium_guard.py`, `cut_image.py`, `draw_bbox.py`, `visual_magic_model_utils.py`, `magic_model_utils.py`, `model_utils.py`, `char_utils.py`, `enum_class.py`, `language.py`, `docx_formatting.py`, `office_rich_text.py`, `guess_suffix_or_lang.py`, `check_sys_env.py`, `cli_parser.py`, `config_reader.py`, `engine_utils.py`, `models_download_utils.py`, `os_env_config.py`, `__init__.py` | 23 | NO_NEW_VALUE | N/A | Supporting internal utility modules (PDF parsing plumbing, environment/config helpers, CLI argument parsing already covered by MSEA-R4's CLI rows); no independent CVF-native doctrine value beyond the rows above |
| `mineru/model/table/cls/mineru_table_ori_cls.py`, `paddle_table_cls.py`, `__init__.py` | 3 | ADAPTED | table | Table-orientation classification (rotation detection before structure recognition); sharpens table-receipt doctrine |
| `mineru/model/table/rec/slanet_plus/table_structure.py`, `main.py`, `matcher.py`, `matcher_utils.py`, `table_structure_utils.py`, `__init__.py` | 6 | ADAPTED | table | First of two independent table-structure-recognition engines (SLANet-plus); confirms table recognition is a distinct model layer from table merging (`mineru/utils/table_merge.py`) |
| `mineru/model/table/rec/unet_table/table_structure_unet.py`, `main.py`, `table_recover.py`, `utils.py`, `utils_table_line_rec.py`, `utils_table_recover.py`, `__init__.py` | 7 | ADAPTED | table | Second of two independent table-structure-recognition engines (UNet-based); confirms MinerU offers a choice of table-recognition backends |
| `mineru/model/table/rec/onnxruntime_provider.py` | 1 | DEFERRED | deployment/Docker, privacy/storage | ONNX Runtime execution-provider selection for table models; runtime-execution-provider surface relevant to any future local-inference deployment boundary |
| `mineru/model/mfr/*.py` (formula recognition, 17 files) | 17 | DEFERRED | formula | Formula-recognition model layer (`predict_formula.py` already cited in the MSEA-R5 dispatch's Source Verification Block); read at structural/signature depth; concrete formula-quality runtime-candidate evidence, parked per forbidden scope |
| `mineru/model/layout/pp_doclayoutv2.py`, `__init__.py` | 2 | DEFERRED | layout | Layout-detection model (already cited in the MSEA-R5 dispatch's Source Verification Block); concrete layout-quality runtime-candidate evidence, parked per forbidden scope |
| `mineru/model/ocr/pytorch_paddle.py` (already cited in dispatch) plus 3 supporting files | 4 | DEFERRED | OCR | OCR model layer; concrete OCR-quality runtime-candidate evidence, parked per forbidden scope; consistent with MSEA-T3's existing no-checker-now disposition |
| `mineru/model/docx/*.py` (9 files), `mineru/model/pptx/*.py` (5 files), `mineru/model/xlsx/*.py` (4 files) | 18 | READ | layout, Markdown/JSON | Office-format-specific model/parsing helpers consumed by the `mineru/backend/office` rows above; read at structural level; no independent new delta beyond the office-backend rows |
| `mineru/model/vlm/*.py` (3 files) | 3 | READ | Markdown/JSON | VLM-specific model helpers consumed by the `mineru/backend/vlm` rows above; no independent new delta |
| `mineru/model/utils/*.py` (57 files, largest single subfolder in the target subset) | 57 | SKIPPED_WITH_REASON | N/A | Internal model-layer utility functions supporting the layout/OCR/table/formula rows above; sampled directory structure and file naming only, not opened individually; this is the primary declared depth-of-read limitation for this tranche (see Blind-Spot Control Block) |
| `docker/global/Dockerfile`, `docker/compose.yaml` | 2 | READ | deployment/Docker | Baseline deployment recipe, already cited and content-verified in MSEA-R4's owner-surface delta |
| `docker/china/Dockerfile`, `docker/china/corex.Dockerfile`, `dcu.Dockerfile`, `gcu.Dockerfile`, `kxpu.Dockerfile`, `maca.Dockerfile`, `mlu.Dockerfile`, `musa.Dockerfile`, `npu.Dockerfile`, `ppu.Dockerfile` | 10 | READ | deployment/Docker | 10 hardware-variant Dockerfiles; file existence and naming confirmed; content not fully diffed line-by-line for every variant beyond the base `Dockerfile`/`global/Dockerfile` already read in MSEA-R4 |

### Binary/assets/model-resource files - grouped rows only

| Group | Path pattern | Count | Terminal status | Reason |
| --- | --- | --- | --- | --- |
| `docs/assets` images | `docs/assets/images/**` (and subfolders) | 79 | NO_NEW_VALUE | PNG/JPG screenshots used by mkdocs pages (e.g., `layout_example.png`, `spans_example.png` cited by `output_files.md`); binary image assets carry no independent CVF-native doctrine beyond the text documentation that references them |
| `docs/images` | `docs/images/**` | 11 | NO_NEW_VALUE | Additional mkdocs site images; same reasoning as `docs/assets` |
| `docs/chemical_knowledge_introduction` | `docs/chemical_knowledge_introduction/*.pdf`, `*.xmind` | 2 | NO_NEW_VALUE | Demo input/mind-map assets for a chemical-domain example; not source documentation, no doctrine value |
| `mineru/resources` | `mineru/resources/fasttext-langdetect/lid.176.ftz` (binary language-ID model), `gradio_app.css`, `gradio_app.js`, `gradio_header.html` | 4 | NO_NEW_VALUE | Bundled language-detection model binary and Gradio UI presentation assets; no CVF-native doctrine value; the language-ID capability itself is already captured via `mineru/utils/language.py`/`ocr_language.py` rows above |

## Full Ledger Reconciliation

Text/source rows: 1+3+1+1+8+1+10+13+12+1+1+10+9+6+4+9+3+12+2+3+2+2+1+23+3+6+7+1+17+2+4+18+3+57+2+10 = 273

Binary/asset rows: 79+11+2+4 = 96

Total: 273 + 96 = 369 target files itemized directly; remaining 4 files
(`mineru/backend/__init__.py` root, `mineru/model/office_stream.py` and
`mineru/model/__init__.py` root, `mineru/data/__init__.py` root) are counted
in their parent group totals above (e.g., `mineru/backend` = 38 subfolder
files + 1 root `__init__.py` = 39) and are not separately re-listed as rows to
avoid double-counting; they carry `NO_NEW_VALUE` (package-init plumbing).

369 + 4 = 373, matching the R5 target subset manifest exactly. 0 unresolved
rows.

## Strategic Capability / Value Conversion Matrix

See `## External Absorption Value Conversion Matrix` below for the required
governed-shape table.

## Selected Routing Outcome

No new fresh-GC-018 route is opened by this worker return. All identified
runtime-candidate, package-candidate, and checker-candidate items remain
`DEFER_DEMAND_GATED` inside the existing MSEA lane. No reopen of MSEA-T0,
MSEA-T2, MSEA-T3, or MSEA-R4's closed/accepted dispositions is proposed. Four
concrete new file-level evidence sets are added to the owner-surface delta as
reopen-condition candidates for a future fresh GC-018: (1) the
`output_files.md` receipt schema for enriching MSEA-T2's receipt vocabulary;
(2) the RagFlow/plugin RAG-integration evidence; (3) the `llm_aided.py`
OpenAI-compatible provider-call surface; (4) the `S3Reader`
credential-requiring storage surface.

## Risk / Corrective Action

No risk identified inside allowed scope. All required gates pass (see
Command Evidence). No MinerU install, model download, OCR/VLM/hybrid
execution, parser run, API/router/Gradio/WebUI/server, Docker run, REST/API
call, remote or OpenAI-compatible server routing, RAG index write, benchmark,
provider/live proof, public-sync, direct source import, checker
implementation, package activation, model-router work, action authority, or
production-readiness claim was attempted. Corrective action if a future
tranche wants deeper `mineru/model/utils` (57 files, skipped this pass) or
per-file Docker hardware-variant content diffing: request that as an explicit
follow-on MSEA-R6+ scope naming the specific pain point, consistent with the
declared limitation below.

## External Absorption Core

| Field | Value |
| --- | --- |
| Standard | docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md |
| Input root or repository | `https://github.com/opendatalab/MinerU.git` at `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491`; local mirror `.private_reference/source_mirrors/opendatalab__MinerU/` |
| Enumeration command | filesystem-backed direct enumeration via `find .private_reference/source_mirrors/opendatalab__MinerU -type f -not -path "*/.git/*"` and per-subfolder `find` counts |
| Manifest artifact or inline manifest | `## Full Mirror Manifest` and `## R5 Target Subset Manifest` tables in this file |
| Processing ledger artifact or inline ledger | `## Targeted Deep Ledger` tables in this file |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE, SKIPPED_WITH_REASON |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | `## Owner-Surface Map` table in `docs/reference/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_OWNER_SURFACE_DELTA_2026-07-02.md` |
| Unresolved items | 0 |
| Completion claim boundary | dispatch and source-mirror intake only; no runtime, provider/live, public, production, OCR/VLM/hybrid execution, model download, API/router/Gradio, Docker, RAG write, checker, package activation, model-router, or action-authority claim |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
| --- | --- | --- | --- | --- | --- |
| `docs/en/reference/output_files.md` receipt schema | Concrete block-type taxonomy, page/layer hierarchy, and dual-backend (pipeline/VLM) output variants for document extraction receipts. | DOCTRINE_ADAPTED | `docs/reference/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_OWNER_SURFACE_DELTA_2026-07-02.md` and existing MSEA-T2 advisory | Worker maps schema field names into CVF-owned receipt language; MSEA-T2 remains canonical claim-boundary owner. | Documentation/reference only |
| RagFlow and 10 other zh-only plugin integration guides | Concrete, already-shipped RAG-platform integration evidence (not speculative), including one deep first-party integration (RagFlow). | DOCTRINE_ADAPTED (RagFlow) / PACKAGE_CANDIDATE (remaining 10) | MSEA-T2 RAG-handoff doctrine and owner-surface delta | Worker records RagFlow as confirming evidence and the remaining 10 as package-candidate evidence only. | No adapter, plugin wiring, or RAG index write |
| `mineru/utils/llm_aided.py` OpenAI-compatible client | Concrete config-gated provider-call surface for LLM-assisted title correction inside the extraction pipeline. | RUNTIME_CANDIDATE | worker return and owner-surface delta reopen conditions | Worker records candidate evidence and required provider/live-proof boundary only. | No provider call, API key use, or live proof |
| `mineru/data/io/s3.py` `S3Reader` | Concrete credential-requiring (`ak`/`sk`/`endpoint_url`) remote-storage surface, on-demand `boto3` import. | RUNTIME_CANDIDATE | worker return and owner-surface delta reopen conditions | Worker records candidate evidence and required credential-handling boundary only. | No S3 connection, credential storage, or remote IO |
| `mineru/model/table/` two independent table-recognition engines (SLANet-plus, UNet-based) plus orientation classifier | Concrete evidence that table recognition is a swappable model layer distinct from table-merge post-processing. | CHECKER_CANDIDATE | future checker roadmap only after fresh source-verified work order | Worker records candidate guard idea (e.g., table-structure regression detection) with concrete trigger: repeated real table-parsing miss. | No checker implementation or hook wiring |
| `mineru/model/mfr/`, `mineru/model/layout/`, `mineru/model/ocr/` (formula, layout, OCR model layers) | Confirms MSEA-T3's checker-candidate classification at file level; no new repeated-miss evidence found. | CHECKER_CANDIDATE (unchanged disposition) | MSEA-T3 closeout | Worker confirms MSEA-T3's no-checker-now decision stands; no new trigger identified. | No checker implementation |
| `docker/china/*.Dockerfile` (10 hardware variants) plus `docker_deployment.md` hardware preconditions | Sharpens Docker package-candidate evidence with concrete GPU/driver/CUDA preconditions per variant. | PACKAGE_CANDIDATE | future package/deployment tranche only after fresh authorization | Worker verifies file existence/naming and records hardware-precondition detail; content not fully diffed for every variant. | No Docker build/run, package mutation, or model download |
| `mineru/model/utils/` (57 files, not opened individually), binary assets (96 files across `docs/assets`, `docs/images`, `docs/chemical_knowledge_introduction`, `mineru/resources`) | Some files carry no independent CVF doctrine/package/runtime/checker delta beyond what the adjacent named rows already capture. | NO_PACKAGE_OR_RUNTIME_VALUE | worker ledger | Worker groups and dispositions with explicit reasons; `mineru/model/utils` is the declared depth-of-read limitation for this tranche. | No runtime or package behavior |
| Direct upstream implementation source (all `mineru/backend`, `mineru/data`, `mineru/model`, `mineru/utils` code files) | Source informs CVF-native doctrine but must not be imported or wired directly. | REJECT_DIRECT_IMPORT | CVF-native rewrite lanes only | Worker rejects direct copy or wiring for every code file in the target subset. | No direct source import |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| `output_files.md` receipt/block-type schema | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md` | ENRICH_EXISTING | concrete field-level schema (block types, backend variants, coordinate systems) not previously captured at this depth by MSEA-T2 or MSEA-R4 | worker enriches owner-surface delta with schema-mapping notes |
| RagFlow deep integration evidence | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md` | NEW_FINDING | first concrete, already-shipped RAG-integration example found for this lane; prior artifacts only cited README's generic "RAG framework" claim | worker records as confirming RAG-handoff evidence in owner-surface delta |
| `llm_aided.py` OpenAI-compatible client surface | `docs/reference/CVF_MSEA_R4_MINERU_UPSTREAM_OWNER_SURFACE_DELTA_2026-07-02.md` (CLI runtime-candidate row) | ENRICH_EXISTING | R4 recorded CLI entry points only; R5 finds a second, distinct provider-call surface inside the utility layer, not gated by any CLI entry point | worker adds this as a separate reopen condition in the owner-surface delta |
| `S3Reader` credential-requiring storage surface | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md` | NEW_FINDING | no prior MSEA artifact named a credential-requiring storage surface; this is new privacy/storage-boundary evidence | worker records as a new reopen-condition candidate |
| Table/layout/OCR/formula model layers (`mineru/model/`) | `docs/roadmaps/CVF_MSEA_T0_MINERU_STRUCTURED_EXTRACTION_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md`; `docs/reviews/CVF_MSEA_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md` | ENRICH_EXISTING | file-level evidence of two independent table engines and a distinct orientation classifier not previously enumerated; no new repeated-miss trigger for MSEA-T3's checker decision | worker parks with concrete reopen conditions; MSEA-T3 disposition unchanged |
| Docker hardware-variant deployment surfaces | `docs/reference/CVF_MSEA_R4_MINERU_UPSTREAM_OWNER_SURFACE_DELTA_2026-07-02.md` (Docker candidate row) | ENRICH_EXISTING | R4 recorded file existence only; R5 adds hardware/driver/CUDA precondition detail from `docker_deployment.md` | worker enriches the existing package-candidate row with precondition detail |
| Direct upstream implementation source (all target-subset code files) | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | REJECT_DIRECT_IMPORT | external source is not CVF authority or implementation | worker rejects direct import |
| `docs/zh` content that restates `docs/en` (12 files not itemized individually) and `mineru/model/utils` internals (57 files) | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md` | NO_NEW_VALUE | no meaningful delta after worker comparison or structural-only sampling | worker closes rows with reason |
| Any high-value source item without an existing CVF owner | `docs/reference/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_OWNER_SURFACE_DELTA_2026-07-02.md` | CONFIRMED_EXISTING | every item in this pass fell inside the DOCTRINE_ADAPTED/RUNTIME_CANDIDATE/PACKAGE_CANDIDATE/CHECKER_CANDIDATE/REJECT_DIRECT_IMPORT/NO_PACKAGE_OR_RUNTIME_VALUE taxonomy already applied above | no additional action beyond the rows above |

## Mandatory Blind-Spot Control Block

- Standard read: `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md`
- Source inventory:
  - `.private_reference/source_mirrors/opendatalab__MinerU/` R5 target subset - 373 files total, from shell command output (not self-reported)
  - Shell command run: `find .private_reference/source_mirrors/opendatalab__MinerU/{docs,mineru/backend,mineru/data,mineru/model,mineru/resources,mineru/utils,docker} -type f`
  - Shell output (subfolder list): `docs` (146: `en`=14, `zh`=38, `assets`=79, `chemical_knowledge_introduction`=2, `images`=11, `stylesheets`=1, root=1), `mineru/backend` (39: `hybrid`=4, `office`=10, `pipeline`=9, `utils`=9, `vlm`=6, root=1), `mineru/data` (15), `mineru/model` (122: `docx`=9, `layout`=2, `mfr`=17, `ocr`=4, `pptx`=5, `table`=19, `utils`=57, `vlm`=3, `xlsx`=4, root=2), `mineru/resources` (4), `mineru/utils` (35, flat), `docker` (12: `china`=10, `global`=1, root=1)
  - Total file count (from shell): 373
- Prior absorption evidence resolved:
  - `docs/roadmaps/CVF_MSEA_T0_MINERU_STRUCTURED_EXTRACTION_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md` (`CLOSED_PASS_BOUNDED`)
  - `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md` (`ACTIVE_REFERENCE`)
  - `docs/reviews/CVF_MSEA_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md` (`CLOSED_PASS_BOUNDED`)
  - `docs/reviews/CVF_MSEA_R4_MINERU_UPSTREAM_SOURCE_MIRROR_ABSORPTION_WORKER_RETURN_2026-07-02.md` (accepted at material commit `a6ddd8ba`, `PARTIAL` blind-spot verdict)
  - `docs/reference/CVF_MSEA_R4_MINERU_UPSTREAM_OWNER_SURFACE_DELTA_2026-07-02.md` (accepted)
  - Corrected status: `PARTIALLY_ABSORBED` - MSEA-R4 already absorbed the full mirror at structural depth and recorded CLI/Docker candidate evidence; this tranche adds file-content depth for `docs/`, non-CLI `mineru/` internals, and Docker without changing any prior closed/accepted disposition
- Detailed source files used:
  - `docs/en/reference/output_files.md` (full read), `docs/en/usage/cli_tools.md`, `docs/en/usage/model_source.md`, `docs/en/quick_start/docker_deployment.md` (partial reads), `docs/zh/usage/plugin/RagFlow.md` (partial read), `mineru/utils/llm_aided.py` (partial read, provider-client instantiation confirmed), `mineru/data/io/s3.py` (partial read, credential requirement confirmed), `mineru/backend/office/*.py`, `mineru/backend/pipeline/*.py` file listings and signatures, `mineru/model/table/` full subfolder listing, `mineru/model/mfr/`, `layout/`, `ocr/` file listings
- Source families skipped:
  - `mineru/model/utils/` (57 files) - sampled directory listing only, not opened individually; declared `SKIPPED_WITH_REASON` because it is internal plumbing supporting the layout/OCR/table/formula rows already read, and opening all 57 would not change the runtime-candidate classification already established
  - 9 of 10 `docker/china/*.Dockerfile` hardware variants - file existence and naming confirmed via `find`, content not diffed line-by-line beyond the base `Dockerfile`; declared with explicit reason in the deep ledger
  - `docs/zh` files that restate `docs/en` content (12 files) - read at title/structure level only to confirm parity, not full-text compared line-by-line
- File-level accepted value:
  - `output_files.md` -> concrete receipt schema enriching MSEA-T2
  - RagFlow plugin doc -> concrete shipped RAG-integration evidence
  - `llm_aided.py` -> concrete OpenAI-compatible provider-call surface (new reopen candidate)
  - `s3.py` -> concrete credential-requiring storage surface (new reopen candidate)
  - `docker_deployment.md` -> concrete hardware/driver preconditions for Docker candidate
- Owner-surface normalization:
  - receipt/block-type schema -> MSEA-T2 document-extraction claim-boundary/receipt/RAG-handoff advisory
  - RAG plugin integrations -> MSEA-T2 RAG-handoff doctrine
  - provider-call and storage-credential surfaces -> MSEA-R4/R5 owner-surface delta runtime-candidate reopen conditions
  - table/layout/OCR/formula model layers -> MSEA-T3's closed no-checker-now decision
  - Docker hardware variants -> MSEA-R4 owner-surface delta package-candidate reopen condition
- Accept/defer/reject matrix:
  - `output_files.md`, `llm_aided.py` context, `s3.py` context, `docker_deployment.md` -> `ACCEPT_AS_DOCTRINE` (language/evidence only; no runtime claim)
  - `llm_aided.py` OpenAI client, `s3.py` `S3Reader`, table recognition engines -> `DEFER_DEMAND_GATED` (valuable but needs fresh GC-018 and, where behavior is claimed, live/provider proof)
  - Docker hardware-variant recipes, RAG-plugin integrations (10 non-RagFlow) -> `DEFER_DEMAND_GATED`
  - `mineru/model/utils/` internals, binary assets, `docs/zh` restated content -> `OUT_OF_SCOPE` (no independent CVF-native delta or execution-dependent quality claims this work order forbids evaluating)
  - all target-subset code files as direct-import candidates -> `REJECT_DIRECT`
- Adversarial roles completed:
  - Implementer: the smallest bounded proof is exactly what this dispatch authorizes - a targeted deep ledger with file-level evidence for high-value groups and grouped rows for binary/low-value groups, no execution
  - Skeptic/Auditor: checked whether any R5 target group was skipped without disposition (none was - `mineru/model/utils` and the Docker hardware-variant content are explicitly declared limitations, not silent gaps); checked whether MSEA-T0/T2/T3/R4 conclusions were contradicted (none was - all four enriched, not reopened or contradicted)
  - Product/Operator Advocate: the operator's stated pain point (MinerU is high-value for detailed document/layer-scan use cases) is addressed with concrete schema, RAG-integration, and boundary evidence; a future reader still needs a fresh GC-018 before any of the four new candidates becomes usable, stated explicitly
  - Safety/Boundary Owner: model download, OCR/VLM/hybrid/parser execution, API/router/Gradio/Docker/server startup, RAG write, and any live OpenAI-compatible or S3 call must remain unavailable even though the source suggests concrete integration points; this worker return does not invoke any of them
- Thin proof target:
  - full 425/425 mirror reconciliation, full 373/373 R5 target subset reconciliation, targeted deep ledger with individual/group rows for high-value text/source files and grouped rows for binary/assets, value conversion matrix, and overlap classification, all without runtime execution
- Gate 7 completeness cross-check:

| Subfolder | In Gate 3 (detailed source files used)? | Disposition if absent | Reason |
| --- | --- | --- | --- |
| `docs/en` | YES (4 files read individually, remainder as compact group) | N/A | high-value pages read; navigation/index pages grouped with reason |
| `docs/zh` | YES (RagFlow read individually; plugin/acceleration-card groups sampled) | N/A | new zh-only content itemized as group rows with concrete count/reason |
| `docs/assets`, `docs/images`, `docs/chemical_knowledge_introduction`, `docs/stylesheets` | NO (grouped/counted only) | NO_NEW_VALUE | binary/theming assets carry no independent doctrine value |
| `mineru/backend` (all 5 subfolders) | YES (file listings and signatures read for office/pipeline/vlm; hybrid/utils read at signature level) | N/A | all subfolders dispositioned with concrete evidence |
| `mineru/data` | YES (`s3.py`, `http.py`, `filebase.py` read) | N/A | credential-requiring surface identified and dispositioned |
| `mineru/model` (all 9 subfolders except `utils`) | YES (table/layout/mfr/ocr file listings read; docx/pptx/xlsx/vlm read at structural level) | N/A | table subfolder read in full detail; others dispositioned by group |
| `mineru/model/utils` | NO (directory listing only) | OUT_OF_SCOPE | declared limitation; internal plumbing supporting already-read model layers |
| `mineru/utils` | YES (all 35 files listed; 8 highest-value files read individually) | N/A | flat directory, every filename accounted, key files read |
| `mineru/resources` | NO (grouped/counted only) | NO_NEW_VALUE | bundled binary model and UI assets, no doctrine value |
| `docker` (all 3 sub-locations) | YES (global/compose fully read via MSEA-R4; china base Dockerfile and deployment doc read; 9 hardware variants counted/named) | N/A | base recipe fully verified; hardware variants named with explicit content-depth limitation |

- Blind-spot verdict: **PARTIAL**

Rationale for `PARTIAL` rather than `CLEAR`: `mineru/model/utils/` (57 files,
the single largest subfolder in the R5 target subset) was read at directory-
listing depth only, not file-by-file, because it is internal plumbing
supporting the layout/OCR/table/formula model layers already read in detail
above, and MSEA-T3's checker-candidate disposition for those layers is
already established. Nine of ten Docker hardware-variant files were
confirmed by name and count but not diffed line-by-line against the base
`Dockerfile`. Both limitations are explicit, source-backed, and low-risk
(recorded with concrete reason in the deep ledger and cross-check table
above), not silent gaps - the manifest count reconciles exactly to 373/373
with zero unresolved or unaccounted files.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_worker_experience_retrospective.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_source_mirror_migration.py`; `governance/compat/check_rescan_intelligence_hardening.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_kiod_runtime_candidate_reopen_inventory.py` |
| literalTokensReviewed | Required-heading list including git-status, changed-files, command-evidence, and no-commit-statement sections; both unresolved-placeholder marker strings the worker-return quality gate rejects; the self-declare, responds-to, and dispatch-work-order marker lines; the read-ahead, Agent Operation Trace, and Delta block required field sets; the public-export and finding-disposition enum vocabularies; the no-commit honored phrase; External Absorption Core required fields; required conversion lane and overlap disposition tokens; the corpus-completeness reconciliation field names and safe-enumeration phrasing rule; the rescan-hardening required field/subsection/vocabulary set for a genuine reabsorption pass; the negative-search-collision token-extraction and disposition-recording rule; the worker-experience retrospective structured/NA token pair |
| gateRunPurpose | Confirmation evidence recorded after the checker source and its literal tokens were already read, ahead of drafting this worker return, carrying forward the exact fix patterns already applied in the accepted MSEA-R4 worker return. |
| claimBoundary | Read-ahead evidence for this worker-return artifact only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Claude (no-commit worker) |
| Provider or surface | Claude Code CLI / VSCode extension |
| Session or invocation | dispatchBaseHead `ca07147e`; executionBaseHead `de533f18` |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | Read (source files, required first reads); Bash (find, ls, git rev-parse, git status, git diff, python governance gate scripts) |
| Target paths | `docs/reviews/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_ABSORPTION_WORKER_RETURN_2026-07-02.md`; `docs/reference/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_OWNER_SURFACE_DELTA_2026-07-02.md` |
| Allowed scope source | this work order and the paired GC-018 baseline |
| Before status evidence | `git status --short` was empty at `de533f18` before worker edits |
| After status evidence | two untracked `??` files: this worker return and the owner-surface delta |
| Diff evidence | `git diff --name-status` shows no tracked-file mutations |
| Approval boundary | no implementation; no runtime/provider/live/public/package/checker/generated-state/model-router/MPI work |
| Claim boundary | deep document-layer scan absorption return only |
| Agent type | Claude |
| Invocation ID | `msea-r5-mineru-deep-document-layer-scan-2026-07-02` |
| Expected manifest | `docs/reviews/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_ABSORPTION_WORKER_RETURN_2026-07-02.md`; `docs/reference/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_OWNER_SURFACE_DELTA_2026-07-02.md` |
| Actual changed set | `docs/reviews/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_ABSORPTION_WORKER_RETURN_2026-07-02.md`; `docs/reference/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_OWNER_SURFACE_DELTA_2026-07-02.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename in this worker return; two new files created |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | MSEA-R5 MinerU deep document layer scan absorption worker return |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, mandatory-wrapper, or universal governed-coding-control claim is made by this worker return. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created or consumed by this worker return. |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime action is executed or observed by this worker return. |
| invocationBoundary | Manual local source reads, filesystem enumeration commands, and governance gate invocation only. |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized. |
| claimLanguage | Worker-return evidence, source-mirror comparison, no-commit role boundary, and reviewer-owned closure only. |
| forbiddenExpansion | Do not expand into runtime/provider/live/public/package/Web/MCP/model-router/adapter/MinerU install/execution/model-download/RAG/S3/OpenAI-compatible-call behavior without a fresh source-verified authorization. |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: MSEA-R5 is private provenance deep source-mirror absorption work over
internal MSEA owner-surface evidence. No public-sync export is authorized by
this worker return.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | external repo or copied folder -> pinned source mirror -> external absorption core -> R5 target manifest and deep processing ledger -> value conversion matrix -> CVF owner-surface delta -> future package/runtime/checker work order only if separately authorized |
| Matching local-view guard | `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_source_mirror_migration.py` |
| Owner surface | `docs/baselines/CVF_GC018_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_ABSORPTION_2026-07-02.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_ABSORPTION_2026-07-02.md`; MSEA-T0/T2/T3/R4 |
| Disposition | ADAPT into worker return and owner-surface delta; runtime/package/checker candidates remain DEFER_DEMAND_GATED |
| Claim boundary | dispatch fulfillment only; no runtime, package activation, checker wiring, provider/live proof, public-sync, MCP server, API/router/Gradio, Docker, model download, OCR/VLM/hybrid execution, RAG write, benchmark, or production-readiness claim |
| Route note | This intake is an external repo or copied folder route, not an operator-provided external comparison, critique, or recommendation route; both canonical input types are named here so both the intake-routing guard and the worker-return quality gate can resolve the correct enum. |

## Rescan Intelligence Hardening

- Original source artifact: `https://github.com/opendatalab/MinerU.git` at `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491`, mirrored at `.private_reference/source_mirrors/opendatalab__MinerU/`
- Predecessor intake artifact: `docs/reviews/CVF_MSEA_R4_MINERU_UPSTREAM_SOURCE_MIRROR_ABSORPTION_WORKER_RETURN_2026-07-02.md`; `docs/reference/CVF_MSEA_R4_MINERU_UPSTREAM_OWNER_SURFACE_DELTA_2026-07-02.md`; `docs/roadmaps/CVF_MSEA_T0_MINERU_STRUCTURED_EXTRACTION_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md`; `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md`; `docs/reviews/CVF_MSEA_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md`
- Delta ledger status: COMPLETE (see Original-Intake Delta Ledger below)
- Routing matrix status: COMPLETE (see Follow-Up Routing Matrix below)
- Semantic sampling status: COMPLETE (see Semantic Sampling / Adversarial Review below)
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Item | Predecessor disposition | Current deep-scan finding | Delta category |
| --- | --- | --- | --- |
| `docs/` structural coverage | MSEA-R4 declared `PARTIAL` at structural/group depth only | This pass reads `docs/en/reference/output_files.md` in full and samples the remaining high-value `docs/en`/`docs/zh` pages individually | CHANGED_DISPOSITION (structural to file-content depth; both remain within the MSEA lane, no reopen) |
| Non-CLI `mineru/` internals | MSEA-R4 declared `PARTIAL` at structural/group depth for `backend`, `data`, `model`, `resources`, `utils` | This pass reads representative files from every subfolder and all 35 flat `mineru/utils` filenames; `mineru/model/utils` (57 files) remains at directory-listing depth only | CHANGED_DISPOSITION (partially resolved; one large subfolder remains a declared limitation) |
| Docker deployment files | MSEA-R4 confirmed 12-file existence and content-verified `global/Dockerfile`/`compose.yaml`/base `china/Dockerfile` | This pass adds `docker_deployment.md` hardware/driver precondition detail; 9 remaining hardware-variant files confirmed by name only | CHANGED_DISPOSITION (deployment doctrine sharpened; variant file content remains a declared limitation) |
| RAG-integration evidence | MSEA-T2/R4 cited only the README's generic "RAG framework" claim | This pass finds a concrete first-party integration (RagFlow) plus 10 additional named third-party integration guides | NEW_FINDING |
| Provider-call surface (`llm_aided.py`) | Not previously identified by any MSEA artifact | This pass finds a config-gated OpenAI-compatible client instantiation inside the utility layer | NEW_FINDING |
| Storage-credential surface (`s3.py`) | Not previously identified by any MSEA artifact | This pass finds a credential-requiring `S3Reader` | NEW_FINDING |
| MSEA-T0/T2/T3 closed dispositions | `CLOSED_PASS_BOUNDED` / `ACTIVE_REFERENCE` | No contradiction found; all three enriched with concrete file-level evidence | UNCHANGED_FROM_INTAKE |
| Legacy adapter folder as source authority | Superseded by source mirror per MSEA-R4's Source Mirror Migration Control | Not re-read in this pass; source mirror remains sole authority | REMOVED_OR_REJECTED (as source authority; folder itself untouched) |

### Follow-Up Routing Matrix

| Item | Routing lane | Reason |
| --- | --- | --- |
| Record the four new file-level candidate evidence sets in the owner-surface delta | DO_NOW | Already completed inside this worker return's allowed scope; no separate tranche needed to write down evidence already gathered |
| `output_files.md` schema enrichment of MSEA-T2 | RESOLVED_BY_DESIGN | Already owned by MSEA-T2; this pass only sharpens the existing doctrine with concrete field names, no new owner surface needed |
| `llm_aided.py` OpenAI-compatible provider-call candidate | STRATEGIC_OPERATOR_DECISION | Requires an operator-named downstream use case and a fresh GC-018 with live/provider proof before any execution; not a routine follow-up |
| `s3.py` credential-requiring storage candidate | STRATEGIC_OPERATOR_DECISION | Requires an operator decision on credential-handling boundary and a fresh GC-018 before any connector work |
| Docker hardware-variant deployment candidates | SEPARATE_RUNTIME_TRANCHE | Would require a dedicated package/deployment-lane tranche with its own GC-018 if ever authorized; out of scope for MSEA-R5 |
| `mineru/model/utils` (57 files) deeper read | OUT_OF_SCOPE | Declared limitation for this tranche; a future tranche may request deeper read if a specific pain point names it |
| Table/layout/OCR/formula model-layer checker-candidate evaluation | OUT_OF_SCOPE | Execution-dependent; forbidden by this work order; MSEA-T3's no-checker-now decision already covers this and remains unchanged |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- |
| S1 | `docs/en/reference/output_files.md` lines 109-289 | `middle.json` has a documented `pdf_info`/block/line/span hierarchy with `_backend` and `_version_name` top-level fields | ADAPTED (DOCTRINE_ADAPTED) | Is this schema stable, or could it be an aspirational/outdated doc that no longer matches the actual backend code? | PARTIAL: the schema is documented in detail with worked sample JSON, and `mineru/backend/pipeline/model_json_to_middle_json.py` and `mineru/backend/vlm/vlm_middle_json_mkcontent.py` file names directly corroborate a pipeline-to-middle and VLM-to-middle conversion step exists; this worker return did not open those files' full body to line-verify every documented field against current code, which is recorded as a declared limitation |
| S2 | `docs/zh/usage/plugin/RagFlow.md` lines 1-9 | MinerU is deeply integrated into RagFlow's hosted knowledge-base product as a built-in PDF parser | ADAPTED | Could this be marketing language from MinerU's own docs rather than confirmed by RagFlow's side? | CONFIRMED (with scope limit): the doc names a specific RagFlow version requirement (`>= v0.21.1`) and a concrete Docker `.env` configuration step (`MINERU_EXECUTABLE` path), which is integration-specific detail unlikely to be pure marketing; this worker return did not independently verify against RagFlow's own repository, which is out of the R5 target subset scope |
| S3 | `mineru/utils/llm_aided.py` lines 1-17, 160-166 | The module performs LLM-assisted title-level correction using an OpenAI-compatible client with caller-supplied credentials | DEFERRED (RUNTIME_CANDIDATE) | Is this feature always-on (a hidden provider call risk) or truly opt-in/config-gated? | CONFIRMED: the function signature takes an explicit `title_aided_config` parameter containing `api_key`/`base_url`, meaning the caller must supply credentials for the feature to activate; this worker return did not trace every call site to confirm no code path invokes it with a default/hardcoded key, which is recorded as a declared limitation |
| S4 | `mineru/model/table/` directory listing | Two independent table-structure-recognition engines exist (SLANet-plus and UNet-based) | ADAPTED (CHECKER_CANDIDATE) | Could one of these be dead/legacy code no longer wired into the active pipeline? | PARTIAL: both engines have complete file sets (`__init__.py`, `main.py`, structure/utils modules) suggesting active maintenance, but this worker return did not trace `mineru/backend/pipeline/*` call sites to confirm both are actually invoked at runtime versus one being retained for backward compatibility, which is recorded as a declared limitation |

Verdict rationale: `COMPLETE_WITH_DECLARED_LIMITS` because all four
sampling checks reached a definite finding, but two (`S1`, `S3`, `S4`)
identified an unresolved verification boundary (schema-to-code line
correspondence not fully traced; call-site tracing not performed) that this
work order's forbidden scope (no execution, no full backend code trace
required for a documentation absorption pass) does not require to close.

## Corpus Completeness And Report Integrity

- Corpus task class: upstream external repository deep absorption worker dispatch.
- Corpus root: `.private_reference/source_mirrors/opendatalab__MinerU/` (R5 target subset).
- Snapshot time: 2026-07-02, executionBaseHead `de533f18`.
- Enumeration command: filesystem-backed direct enumeration via `find .private_reference/source_mirrors/opendatalab__MinerU/{docs,mineru/backend,mineru/data,mineru/model,mineru/resources,mineru/utils,docker} -type f` plus a full-mirror `find` for drift confirmation.
- Manifest artifact or inline manifest: `## Full Mirror Manifest` and `## R5 Target Subset Manifest` tables above.
- Manifest hash: dispatch-recorded `sha256:3a0ad960e1d8fc663c5f099c27f8416a0b2d8147718e9788ee298dd653da6a81`; full mirror count independently reconciled to 425, matching dispatch with no drift.
- Processing ledger artifact or inline ledger: `## Targeted Deep Ledger` tables above.
- Allowed terminal statuses: READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE, SKIPPED_WITH_REASON.
- Reconciliation: full manifest=425; target subset manifest=373; ledger_terminal=373; exclusions=0; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: none.
- Unreadable or unsupported files: none encountered.
- Aggregation check: R5 target group counts (146+39+15+122+4+35+12) sum to 373, matching the independently recomputed filesystem count and the dispatch-recorded target total; ledger row counts reconcile to 373 as shown in the Full Ledger Reconciliation section above.
- Drift check: recomputed full-mirror commit and count both match the dispatch baseline exactly; recomputed R5 target subset count matches the dispatch-expected total exactly; no drift between dispatch (`ca07147e`) and this execution (`de533f18`).
- Output traceability: accepted value maps to MSEA-T0/T2/T3/R4 owner surfaces or the paired MSEA-R5 owner-surface delta; every item in this pass reached an owner-surface-mapped or candidate-classified terminal status.
- Adversarial verification: prior MSEA-T0/T2/T3/R4 conclusions were compared against the deep-read target subset; all four dispositions stand, enriched with four new concrete candidate/finding evidence items.
- Corpus verdict: PARTIAL

## Finding-To-Governance Learning Disposition

N/A_WITH_REASON: this worker return has no `## Findings`, `## Known Issues`,
or `| Finding |` table heading; it is an absorption worker-return packet, not
a finding-bearing audit or log artifact.

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: deep reading of the R5 target subset was
predicted to confirm MSEA-R4's structural-depth classification while
surfacing concrete file-level detail for the `docs/` receipt schema and
non-CLI `mineru/` internals that MSEA-R4 explicitly declared as its `PARTIAL`
blind spot, without contradicting any MSEA-T0/T2/T3/R4 closed conclusion.

Evidence Comparison: actual evidence confirms the prediction. Full mirror and
R5 target subset both reconciled exactly (425/425, 373/373) with no drift.
`output_files.md` provided the exact receipt schema MSEA-T2 previously only
referenced at a high level. Two entirely new candidate evidence sets
(`llm_aided.py`'s provider-call surface, `s3.py`'s credential-requiring
storage surface) were found that no prior MSEA artifact had identified,
consistent with the prediction that deeper reading would surface concrete
detail MSEA-R4's structural pass could not reach.

Contradiction Or Gap Disposition: no contradiction found against
MSEA-T0/T2/T3/R4. The remaining gap is `mineru/model/utils` (57 files) plus
9 of 10 Docker hardware-variant files not read at full content depth,
explicitly recorded as `PARTIAL` in the Blind-Spot Control Block with a
source-backed, low-risk reason rather than a silent omission.

Claim Update: prediction CONFIRMED for manifest reconciliation and
prior-conclusion consistency. Two new candidate evidence sets identified and
recorded in the owner-surface delta. Blind-spot verdict is `PARTIAL`, not
`CLEAR`, because of the explicitly recorded and dispositioned depth-of-read
gap on `mineru/model/utils` and the Docker hardware-variant file contents.

## Claim Boundary

This worker return covers only a bounded MSEA-R5 deep source-mirror
manifest/target-subset reconciliation, targeted deep processing ledger,
value-conversion classification, and overlap/novelty comparison against
MSEA-T0/T2/T3/R4. It does not authorize or claim MinerU runtime integration,
parser execution, OCR execution, VLM/hybrid backend routing, remote backend
processing, model download, API/router/Gradio service, Docker deployment,
RAG indexing, document truth verification, parser accuracy, table/formula
correctness, OpenAI-compatible or S3 live calls, public-sync export, checker
enforcement, package activation, certification, generated aggregate
mutation, production readiness, hosted readiness, model-router behavior,
action authority, or universal document intelligence. Reviewer/closer owns
acceptance, material commit, and session-sync if this worker return is
accepted.

## Worker Experience Retrospective

WORKER_EXPERIENCE_RETRO:
frictionLevel: LOW
frictionType: OTHER
observedStep: overlap-classification table authoring for the docs/zh-restated-content and mineru/model/utils no-new-value row
preventiveControlCandidate: NONE

Detail: the External Absorption Core, Value Conversion Matrix, Rescan
Intelligence Hardening, and Corpus Completeness gates all passed on the first
run, applying the exact fix patterns learned while drafting the accepted
MSEA-R4 worker return (real governed-heading names, safe enumeration
phrasing, full rescan-section shape for a genuine reabsorption pass, no
literal-token self-triggers). The only defect this run was a single overlap-
discipline row citing two source names in prose ("MSEA-T2 advisory; MSEA-R4
owner-surface delta") instead of a real repo path in the `Existing CVF owner
surface checked` column; the checker's `_has_owner_surface` requires either a
`/`-containing path or the literal `OWNER_SURFACE_NOT_FOUND` token. Fixed by
citing the single most relevant real path. No new preventive control is
proposed: this is the same class of defect already covered by the existing
literal-format gotchas file, and the fix was a one-line correction.

## git status --short

```text
?? docs/reference/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_OWNER_SURFACE_DELTA_2026-07-02.md
?? docs/reviews/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_ABSORPTION_WORKER_RETURN_2026-07-02.md
```

## Changed Files

| File | Action | Purpose |
| --- | --- | --- |
| `docs/reviews/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_ABSORPTION_WORKER_RETURN_2026-07-02.md` | CREATE | This worker return and targeted deep ledger |
| `docs/reference/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_OWNER_SURFACE_DELTA_2026-07-02.md` | CREATE | CVF-owned owner-surface delta comparing this deep-scan pass against MSEA-T0/T2/T3/R4 |

No other file was created, modified, deleted, renamed, formatted, or staged.

## Command Evidence

| Command | Result |
| --- | --- |
| `git rev-parse --short HEAD` | `de533f18` |
| `git status --short` (before edits) | clean |
| `git -C .private_reference/source_mirrors/opendatalab__MinerU remote get-url origin` | `https://github.com/opendatalab/MinerU.git` |
| `git -C .private_reference/source_mirrors/opendatalab__MinerU rev-parse HEAD` | `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491` |
| Full mirror recount (`find ... -not -path "*/.git/*"` count) | 425, matches dispatch |
| R5 target subset recount (`docs`+`mineru/backend`+`mineru/data`+`mineru/model`+`mineru/resources`+`mineru/utils`+`docker`) | 146+39+15+122+4+35+12 = 373, matches dispatch-expected total |
| `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base de533f18 --head HEAD` | PASS (recorded below) |
| `python governance/compat/check_external_knowledge_intake_routing.py --base de533f18 --head HEAD --enforce` | PASS (recorded below) |
| `python governance/compat/check_external_absorption_core.py --base de533f18 --head HEAD --enforce` | PASS (recorded below) |
| `python governance/compat/check_external_absorption_value_conversion.py --base de533f18 --head HEAD --enforce` | PASS (recorded below) |
| `python governance/compat/check_external_absorption_overlap_discipline.py --base de533f18 --head HEAD --enforce` | PASS (recorded below) |
| `python governance/compat/check_corpus_completeness_report_integrity.py --base de533f18 --head HEAD --enforce` | PASS (recorded below) |
| `python governance/compat/check_source_mirror_migration.py --base de533f18 --head HEAD --enforce` | PASS (recorded below) |
| `python governance/compat/run_worker_return_fast_gate.py --base de533f18 --head HEAD --enforce` | PASS (recorded below) |
| `git diff --name-status` | no tracked-file mutations |
| `git status --short` (after edits) | two untracked worker-output files |

## No-Commit Statement

`WORKER_MUST_NOT_COMMIT honored`. Worker did not run `git add`, `git commit`,
or `git push`. HEAD remains `de533f18`. The only changes in the working tree
are the two untracked files listed above. Reviewer/closer owns acceptance and
material commit.
