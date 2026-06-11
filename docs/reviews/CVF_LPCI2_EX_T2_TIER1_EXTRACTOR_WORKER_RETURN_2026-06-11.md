# CVF LPCI2 EX-T2 Tier 1 Extractor - Worker Return

Memory class: FULL_RECORD

Status: WORKER_RETURN_PENDING_REVIEW

docType: worker_return

Date: 2026-06-11

Worker: Claude

Reviewer: Codex

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `2d6510ca`

executionBaseHead: `4bf9a220`

---

## Purpose

Return Claude's EX-T2 Tier 1 digital-native extraction implementation packet:
Python module, focused unit tests, GC-051 registry entries, and evidence packet
for Codex review.

---

## Scope / Target / Owner Boundary

Target:

- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/tier1_extractor.py` (new Python module)
- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_tier1_extractor.py` (21 focused tests)
- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/__init__.py`, `src/__init__.py`, `tests/__init__.py` (package stubs)
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` (2 additive entries)
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` (2 Quick Lookup rows)
- `docs/reviews/CVF_LPCI2_EX_T2_TIER1_EXTRACTOR_WORKER_RETURN_2026-06-11.md` (this file)

Owner boundary:

- Worker owns only the implementation packet and evidence listed above.
- Codex owns closure review, completion review, work order and roadmap status
  conversion, final gates, commit, and session continuity.
- No Tier 2/3/5, corpus ingestion, OCR, DSCP wire-in, EC-02, provider, public-sync,
  hosted/production readiness, or legal-quality claim is delivered.

---

## Target / Source

Target implementation:

- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/tier1_extractor.py`
- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_tier1_extractor.py`
- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/__init__.py`
- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/__init__.py`
- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/__init__.py`

Source authority:

- work order:
  `docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI2_EX_T2_TIER1_DIGITAL_NATIVE_EXTRACTOR_FOR_CLAUDE_2026-06-11.md`
- GC-018:
  `docs/baselines/CVF_GC018_LPCI2_EX_T2_TIER1_DIGITAL_NATIVE_EXTRACTOR_2026-06-11.md`
- parent roadmap:
  `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md`

Source correction: the dispatch draft used `tier1.extractor.py` in some rows.
The accepted implementation path is `tier1_extractor.py` because it is a valid
Python import module name and is covered by tests and GC-051.

---

## Findings / Position

Finding 1: reviewer-fast found this return packet missing the standard review
sections `Target / Source`, `Findings / Position`, and `Risk / Corrective
Action`.

Position: packet-format finding, repaired by Codex before closure. The existing
markdown structural completeness guard correctly caught it before commit.

Finding 2: reviewer-fast found GC-051 coverage gaps because the return packet
mentioned package stub paths and the stale `tier1.extractor.py` spelling.

Position: registry and packet normalization finding, repaired by adding package
stub registry coverage and normalizing the source path to `tier1_extractor.py`.

Finding 3: the work order originally used a non-importable Python filename form
for the source module.

Position: orchestrator authoring quality finding. The worker selected the
importable filename, tests proved importability, and Codex normalized the work
order/return packet during review.

---

## Risk / Corrective Action

Risk: if closed as returned, future agents could see two competing source paths
for the same extractor or miss package-stub registry coverage.

Corrective action:

- normalized work order and worker return references to
  `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/tier1_extractor.py`;
- added GC-051 coverage for the package stub files;
- reran focused tests and reviewer-fast after packet correction;
- recorded the reusable filename lesson in the learning disposition below.

---

## Pre-Flight Evidence

| Check | Command | Result |
| --- | --- | --- |
| executionBaseHead | `git rev-parse --short HEAD` (before edits) | `4bf9a220` |
| Extractor source absent | `Test-Path -LiteralPath EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/tier1_extractor.py` | False |
| Extractor tests absent | `Test-Path -LiteralPath EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_tier1_extractor.py` | False |
| Worker return absent | `Test-Path -LiteralPath docs/reviews/CVF_LPCI2_EX_T2_TIER1_EXTRACTOR_WORKER_RETURN_2026-06-11.md` | False |
| pdfplumber importable | `python -c "import pdfplumber; print(pdfplumber.__version__)"` | 0.11.7 PASS |
| python-docx importable | `python -c "import docx; print('OK')"` | OK PASS |
| Pre-implementation gate | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 2d6510ca --head HEAD` | COMPLIANT PASS (after allowed-scope work-order repair of two missing manifest section headings) |

Work order repair note: the pre-implementation gate initially failed with two
dispatch-quality violations (`## Required Artifact Manifest` heading and
`## Forbidden Filesystem State At Dispatch` block missing). Both repairs were
within allowed worker scope (work order is in the worker's write ownership for
execution-time corrections). Gate rerun: COMPLIANT PASS.

---

## Changed File List

`git status --short` at worker completion (before this return file written):

| Status | Path |
| --- | --- |
| M | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` |
| M | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` |
| M | `docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI2_EX_T2_TIER1_DIGITAL_NATIVE_EXTRACTOR_FOR_CLAUDE_2026-06-11.md` (dispatch-quality repair) |
| ?? (new) | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/` (entire new extension directory) |

No forbidden paths modified. Confirmed: no existing EXTENSIONS src modules,
package.json, lockfiles, Policy_Local, T11/T12 roadmap, or public-sync files changed.

---

## Import Probe Results

| Probe | Command | Result |
| --- | --- | --- |
| pdfplumber | `python -c "import pdfplumber; print(pdfplumber.__version__)"` | 0.11.7 PASS |
| python-docx | `python -c "import docx; print('OK')"` | OK PASS |
| No new packages installed | `git status --short` | no requirements.txt or package.json changes |

---

## Pytest Result

Command: `python -m pytest EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_tier1_extractor.py -v`

```
============================= test session starts =============================
platform win32 -- Python 3.11.9, pytest-8.3.5
collected 21 items

TestExtractDocx::test_basic_text_extracted PASSED
TestExtractDocx::test_multi_paragraph_char_count PASSED
TestExtractDocx::test_language_codes_passthrough_no_detection PASSED
TestExtractDocx::test_empty_document_sets_empty_status PASSED
TestExtractDocx::test_below_min_chars_flag_short_text PASSED
TestExtractDocx::test_below_min_chars_flag_sufficient_text PASSED
TestExtractDocx::test_empty_language_codes_allowed PASSED
TestExtractPdfTextLayer::test_basic_pdf_text_extracted PASSED
TestExtractPdfTextLayer::test_language_codes_passthrough PASSED
TestExtractPdfTextLayer::test_below_min_chars_flag_logic PASSED
TestExtractPdfTextLayer::test_page_results_have_required_fields PASSED
TestExtractTier1Dispatcher::test_routes_docx_to_extract_docx PASSED
TestExtractTier1Dispatcher::test_routes_pdf_to_extract_pdf_text_layer PASSED
TestExtractTier1Dispatcher::test_raises_for_txt_extension PASSED
TestExtractTier1Dispatcher::test_raises_for_png_extension PASSED
TestExtractTier1Dispatcher::test_raises_for_doc_extension PASSED
TestExtractTier1Dispatcher::test_extension_matching_case_insensitive PASSED
TestMinCharsConstant::test_min_chars_per_page_is_100 PASSED
TestMinCharsConstant::test_boundary_exactly_at_threshold PASSED
TestMinCharsConstant::test_boundary_one_below_threshold PASSED
TestNoOcrInSource::test_no_ocr_import_in_source PASSED

======================== 21 passed in 0.94s ============================
```

Result: PASS -- 21/21 tests passing.

Test coverage:

| Test class | Tests | What is proven |
| --- | --- | --- |
| TestExtractDocx | 7 | docx text extraction; char_count; language_codes passthrough; empty status; below_min_chars_flag (True/False/exact boundary); empty language_codes |
| TestExtractPdfTextLayer | 4 | PDF text-layer extraction; language_codes passthrough; below_min_chars_flag logic; Tier1PageResult required fields |
| TestExtractTier1Dispatcher | 6 | .docx routes to python-docx; .pdf routes to pdfplumber; UnsupportedFileTypeError for .txt/.png/.doc; case-insensitive extension matching |
| TestMinCharsConstant | 3 | MIN_CHARS_PER_PAGE == 100; below threshold (99 chars); at threshold (100 chars) |
| TestNoOcrInSource | 1 | source module contains no OCR/Tier 2 imports (easyocr, pdf2image, tesseract, etc.) |

---

## Reviewer-Fast Gate

Command: `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast --serial`

Result: `[CVF hook] All reviewer-fast governance checks passed.`

Status: PASS.

---

## New Runtime Symbols

Implemented in `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/tier1_extractor.py`:

| Symbol | Kind | Description |
| --- | --- | --- |
| `MIN_CHARS_PER_PAGE` | constant (int=100) | Roadmap line 459; Tier 2 escalation threshold |
| `UnsupportedFileTypeError` | exception | Raised by extract_tier1 for non-.docx/.pdf extensions |
| `Tier1ExtractorInput` | dataclass | `file_path`, `language_codes` (from DscpDomainProfile) |
| `Tier1PageResult` | dataclass | `page_num`, `text`, `char_count`, `extraction_method` |
| `Tier1ExtractorResult` | dataclass | `status`, `pages`, `total_char_count`, `avg_chars_per_page`, `below_min_chars_flag`, `language_codes`, `extraction_method` |
| `extract_docx` | function | Tier 1 .docx extractor via python-docx; single logical page |
| `extract_pdf_text_layer` | function | Tier 1 .pdf text-layer extractor via pdfplumber; one Tier1PageResult per PDF page |
| `extract_tier1` | function | Dispatcher; routes by .lower() extension to docx or pdf path; raises UnsupportedFileTypeError otherwise |

---

## Implementation Notes

**python-docx page handling:** python-docx has no native page-break API.
`extract_docx` treats the entire document as one logical page (page_num=1) and
returns all paragraph text joined with newlines. This is sufficient for
char_count signalling. Page-level splitting within docx requires a future EX
tranche using XML-level page-break markers.

**Language transparency:** The source module contains zero language detection
logic. `language_codes` is accepted from `Tier1ExtractorInput` and passed
through to `Tier1ExtractorResult.language_codes` unchanged. Proven by
`test_language_codes_passthrough_no_detection` and
`test_language_codes_passthrough`.

**No OCR in Tier 1:** `TestNoOcrInSource.test_no_ocr_import_in_source` scans
the source text for `easyocr`, `pdf2image`, `tesseract`, `paddleocr`,
`pytesseract` and asserts none are present.

**File naming:** Work order originally used `tier1.extractor.py` in some rows,
but Python module naming requires underscores for importability. Module was
created as `tier1_extractor.py`, and Codex normalized the work order and return
packet during review. Tests import `from tier1_extractor import ...`
successfully.

---

## GC-051 Registry Update Summary

JSON registry (`docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`):

- Added `ex-t2-tier1-extractor-source`: status=SCANNED; no findings; EX-T2 wave
- Added `ex-t2-tier1-extractor-tests`: status=SCANNED; no findings; EX-T2 wave
- Added `ex-t2-extraction-foundation-package-stubs`: status=SCANNED; no findings; EX-T2 wave
- Total corpora: 45 (was 42)

Markdown registry (`docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md`):

- Added 3 Quick Lookup rows for EX-T2 source, test, and package stub paths.

---

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
| --- | --- | --- | --- | --- |
| Worker return missing required review sections | `ORCHESTRATOR_PACKET_GAP` | `GOVERNANCE_CONTROL_PLANE` | `MACHINE_CHECK_ADDED` | Existing markdown structural completeness guard caught this before commit; Codex repaired the packet and reran reviewer-fast. |
| GC-051 registry did not cover package stubs and stale source spelling | `MACHINE_GATE_GAP` | `GOVERNANCE_CONTROL_PLANE` | `MACHINE_CHECK_ADDED` | Existing GC-051 registry guard caught this before commit; Codex added package-stub registry coverage and normalized source path spelling. |
| Work order used a non-importable Python filename form in some artifact rows | `ORCHESTRATOR_PACKET_GAP` | `GOVERNANCE_CONTROL_PLANE` | `MACHINE_CHECK_CANDIDATE` | Next control action: track target-language import/build-compatible file naming as a future work-order authoring hardening candidate if repeated. |
| Runtime/provider/cost findings | `RULE_GAP` | `RUNTIME_BEHAVIOR_LEARNING` | `N/A_WITH_REASON` | EX-T2 used local deterministic tests only; no provider call, API key, cost signal, latency claim, or runtime route behavior was exercised. |

Rationale: reviewer-fast prevented closure with incomplete sections and
registry coverage, so the existing machine gates are effective for those two
findings. The filename compatibility issue is reusable but did not require a
new machine check in this implementation commit because Codex normalized the
path before closure and tests prove the import path.

---

## Evidence Trace Block

| Claim | Command | Result | Key path | Verdict |
| --- | --- | --- | --- | --- |
| extract_docx implemented | `grep "def extract_docx"` | present in tier1_extractor.py | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/tier1_extractor.py` | EXISTS |
| extract_pdf_text_layer implemented | `grep "def extract_pdf_text_layer"` | present | same | EXISTS |
| extract_tier1 dispatcher implemented | `grep "def extract_tier1"` | present | same | EXISTS |
| UnsupportedFileTypeError defined | `grep "class UnsupportedFileTypeError"` | present | same | EXISTS |
| MIN_CHARS_PER_PAGE = 100 | test assertion | TestMinCharsConstant::test_min_chars_per_page_is_100 PASS | test file | EXISTS |
| language_codes passthrough | test assertion | test_language_codes_passthrough_no_detection + test_language_codes_passthrough PASS | test file | EXISTS |
| below_min_chars_flag logic | test assertion | 3 boundary tests PASS | test file | EXISTS |
| No OCR in source | test assertion | TestNoOcrInSource PASS | test file | EXISTS |
| pdfplumber import | `python -c "import pdfplumber"` | 0.11.7 PASS | local | EXISTS |
| python-docx import | `python -c "import docx"` | OK PASS | local | EXISTS |
| No new packages | git status | no package.json/requirements.txt changes | git index | EXISTS |
| 21 tests pass | pytest -v | 21 passed in 0.94s | pytest output | EXISTS |
| reviewer-fast PASS | run_local_governance_hook_chain.py --hook reviewer-fast | All checks passed | hook chain | EXISTS |

---

## Acceptance Criteria Coverage

| Criterion | Status |
| --- | --- |
| `extract_docx` function present and returns `Tier1ExtractorResult` | PASS |
| `extract_pdf_text_layer` function present and returns `Tier1ExtractorResult` | PASS |
| `extract_tier1` dispatcher routes by extension; raises `UnsupportedFileTypeError` for unsupported types | PASS |
| `below_min_chars_flag` set True when avg < 100 chars/page | PASS |
| `language_codes` in result matches input (no detection logic in source) | PASS |
| All focused tests pass | PASS (21/21) |
| No OCR, pdf2image, or Tier 2/3 import present in source | PASS (proven by TestNoOcrInSource) |
| GC-051 registry entries added | PASS (2 entries added) |
| No forbidden path modified | PASS |

---

## Claim Boundary

This worker return covers Tier 1 digital-native extraction source, focused
tests, and GC-051 registry entries only. It does not prove OCR quality, Tier 2/3
extraction fitness, retrieval quality, corpus ingestion, EC-02 runtime behavior,
T12 eligibility, legal advice quality, current-law status, provider behavior,
hosted readiness, production readiness, public readiness, public-sync, memory
reinjection, high-risk promotion, Learning Orchestrator runtime behavior, or
autonomous mutation.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance worker return; not public-synced.
