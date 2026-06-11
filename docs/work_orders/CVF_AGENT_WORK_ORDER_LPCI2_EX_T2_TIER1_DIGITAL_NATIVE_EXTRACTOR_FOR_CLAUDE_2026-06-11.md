# CVF Agent Work Order: LPCI2 EX-T2 Tier 1 Digital-Native Extractor

Memory class: FULL_RECORD

Status: DISPATCHED

docType: work_order

Date: 2026-06-11

Worker: Claude

Reviewer: Codex

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: 2d6510ca

executionBaseHead: worker must capture before edits

closureBaseHead: reviewer-owned after return

---

## Purpose

Implement the Tier 1 digital-native extraction module for the reusable CVF
scan/extraction foundation. This tranche delivers a Python module that reads
plain text from `.docx` files (via python-docx) and `.pdf` files with a digital
text layer (via pdfplumber), computes per-page character counts, and returns a
structured extraction result with tier, char_count, text, and page-level
metadata. No OCR, no quality gate module, no DSCP wire-in in this tranche.

## Authority Chain

- Operator instruction: 2026-06-11, open EX-T2 bounded to COMPOSED_STACK_PREFERRED
  verdict from EX-T1 audit.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- Roadmap:
  `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md`
- Roadmap design-control gate: roadmap `## Dispatch Boundary`,
  `## Acceptance Criteria`, and `## Verification And Evidence`
- EX-T1 audit report: `docs/reference/CVF_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_REPORT_2026-06-11.md`
- EX-T1 JSON summary: `docs/reference/CVF_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_SUMMARY_2026-06-11.json`
- GC-018: `docs/baselines/CVF_GC018_LPCI2_EX_T2_TIER1_DIGITAL_NATIVE_EXTRACTOR_2026-06-11.md`
- Active handoff: `AGENT_HANDOFF_V17_2026-06-07.md`
- Design-control standard: `docs/reference/CVF_GOVERNED_WORK_LIFECYCLE_AND_DESIGN_CONTROL_STANDARD_2026-06-11.md`

Authority boundary:

- This work order does not authorize work outside the cited authority chain.
- If any authority artifact conflicts with this work order, stop and return to
  Codex for reconciliation before implementation.

## Agent Roles

| Role | Agent | Responsibility |
| --- | --- | --- |
| Orchestrator / dispatcher | Codex | Author dispatch packet and review return |
| Worker | Claude | Execute EX-T2 implementation only; do not commit |
| Reviewer | Codex | Review artifacts, run gates, commit if bounded PASS |
| Operator | Human | Required for EX-T3/T4/T5 authorization, public-sync, provider/key use, OCR model download, or repo dependency addition beyond existing packages |

## Scope / Target / Owner Boundary

Allowed worker scope:

- Create `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/tier1.extractor.py` (new
  Python module; Tier 1 digital-native only).
- Create `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_tier1_extractor.py`
  (focused unit tests for the Tier 1 extractor).
- Create `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/__init__.py` if the extension
  directory does not exist.
- Update `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` (additive
  entries for the new source and test paths).
- Update `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` (Quick Lookup
  rows for new entries).
- Create `docs/reviews/CVF_LPCI2_EX_T2_TIER1_EXTRACTOR_WORKER_RETURN_2026-06-11.md`.

Forbidden worker scope:

- Do not implement OCR fallback (Tier 2: pdf2image, EasyOCR, Tesseract).
- Do not implement the quality gate module (Tier 3).
- Do not implement DSCP pipeline wire-in (descriptor, gate, receipt) -- EX-T5.
- Do not modify runtime/source modules in other extensions, package manifests,
  lockfiles, corpus data, generated chunks, retrieval code, EC-02 contracts,
  DSCP profiles, T12 artifacts, session continuity files, or public-sync files.
- Do not add new Python packages (pdfplumber and python-docx are already
  installed; no new repo dependency authorized).
- Do not download OCR model weights, run OCR over corpus documents, ingest
  corpus files, create vector indexes, call providers, load API keys, or make
  legal/current-law/readiness claims.

Risk ceiling:

R1 bounded local implementation using already-installed packages.

## Reviewer Closure Conversion

completionReviewPath:

`docs/reviews/CVF_LPCI2_EX_T2_TIER1_EXTRACTOR_COMPLETION_2026-06-11.md`

reviewerOwnedClosurePaths:

- `docs/reviews/CVF_LPCI2_EX_T2_TIER1_EXTRACTOR_COMPLETION_2026-06-11.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI2_EX_T2_TIER1_DIGITAL_NATIVE_EXTRACTOR_FOR_CLAUDE_2026-06-11.md`
- `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION_MEMORY.md`
- `AGENT_HANDOFF_V17_2026-06-07.md`

Reviewer conversion rule: Claude must not create or edit the completion review
unless a later operator instruction changes ownership. Codex owns closure
conversion, final gate reruns, commit, and continuity sync after worker return.

## Required First Reads

| File | Purpose |
| --- | --- |
| `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md` | Confirm Tier 1 architecture, MIN_CHARS threshold, language-transparency rule |
| `docs/reference/CVF_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_REPORT_2026-06-11.md` | Confirm COMPOSED_STACK_PREFERRED verdict and import probe results |
| `docs/baselines/CVF_GC018_LPCI2_EX_T2_TIER1_DIGITAL_NATIVE_EXTRACTOR_2026-06-11.md` | Confirm authorization and claim boundary |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | Confirm `DscpDomainProfile.languageCodes` owner |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Confirm active mode and parked lanes |

## Pre-Flight Checks

| Check | Command | Required result |
| --- | --- | --- |
| Base HEAD captured | `git rev-parse --short HEAD` | record as `executionBaseHead` |
| Extractor source absent | `Test-Path -LiteralPath EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/tier1.extractor.py` | False |
| Extractor tests absent | `Test-Path -LiteralPath EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_tier1_extractor.py` | False |
| Worker return absent | `Test-Path -LiteralPath docs/reviews/CVF_LPCI2_EX_T2_TIER1_EXTRACTOR_WORKER_RETURN_2026-06-11.md` | False |
| pdfplumber importable | `python -c "import pdfplumber; print(pdfplumber.__version__)"` | version printed; no error |
| python-docx importable | `python -c "import docx; print('OK')"` | OK printed; no error |
| Pre-implementation gate | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <dispatchBaseHead> --head HEAD` | PASS before worker edits |

If a pre-flight check fails inside allowed scope, repair and rerun it. If repair
requires forbidden scope, stop and return a blocked diagnostic.

## Source Verification

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| EXISTS: EX-T2 tranche in roadmap | `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md` | line 472 | `EX-T2` | parent roadmap work plan | ACCEPT |
| EXISTS: Tier 1 architecture (python-docx + pdfplumber) | `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md` | line 316 | `Option 1 - Composed stack` | parent roadmap | ACCEPT |
| EXISTS: MIN_CHARS threshold = 100 chars/page | `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md` | line 459 | `MIN_CHARS` | Quality Gates table | ACCEPT |
| EXISTS: OCR auto-escalation rule | `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md` | lines 396 and 407 | `char_count/page`; `MIN_CHARS` | 3-Tier pipeline architecture diagram | ACCEPT |
| EXISTS: languageCodes on DscpDomainProfile | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | line 31 | `languageCodes` | `DscpDomainProfile` | ACCEPT |
| EXISTS: COMPOSED_STACK_PREFERRED verdict | `docs/reference/CVF_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_REPORT_2026-06-11.md` | lines 295 and 307 | `COMPOSED_STACK_PREFERRED` | EX-T1 audit report | ACCEPT |
| EXISTS: pdfplumber import probe | `docs/reference/CVF_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_REPORT_2026-06-11.md` | lines 95 and 318 | `importProbeResult`; `pdfplumber.__version__` | EX-T1 audit report | ACCEPT |
| EXISTS: python-docx import probe | `docs/reference/CVF_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_REPORT_2026-06-11.md` | lines 116, 319, and 320 | `importProbeResult`; `docx` | EX-T1 audit report | ACCEPT |
| EXISTS: language-transparency rule | `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md` | lines 436 and 437 | `languageCodes` | parent roadmap key design decisions | ACCEPT |
| EXISTS: design-control standard | `docs/reference/CVF_GOVERNED_WORK_LIFECYCLE_AND_DESIGN_CONTROL_STANDARD_2026-06-11.md` | line 93 | `Design Control Gate` | lifecycle standard | ACCEPT |
| EXISTS: work-order design carry-forward section | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | line 981 | `Design Control Carry-Forward` | work-order template | ACCEPT |

## Current Runtime Freshness Verification

Dispatch base: `2d6510ca`

| Check | Command | Observed result | Disposition |
| --- | --- | --- | --- |
| Tier 1 extractor source absent | `Test-Path -LiteralPath EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/tier1.extractor.py` | False | ACCEPT |
| Tier 1 extractor tests absent | `Test-Path -LiteralPath EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_tier1_extractor.py` | False | ACCEPT |
| EX-T2 worker return absent | `Test-Path -LiteralPath docs/reviews/CVF_LPCI2_EX_T2_TIER1_EXTRACTOR_WORKER_RETURN_2026-06-11.md` | False | ACCEPT |
| Existing EX-T2 runtime symbols absent | `rg -n "Tier1Extractor|extract_tier1|extract_pdf_text_layer|extract_docx|MIN_CHARS_PER_PAGE|tier1\.extractor" EXTENSIONS` | no matches | ACCEPT |
| pdfplumber import probe | `python -c "import pdfplumber; print(pdfplumber.__version__)"` | 0.11.7 | ACCEPT |
| python-docx import probe | `python -c "import docx; print('OK')"` | OK | ACCEPT |

## New Doc-Only Fields

None. All output fields are in the new Python extractor module and its tests,
not in doc-only audit tables.

## New Runtime Symbols To Be Created

The following symbols are NEW and will be created by this work order.
They are proposed implementation outputs and are listed outside the Source
Verification table because the worker owns their creation.

| New symbol | Kind | Location | Description |
| --- | --- | --- | --- |
| `Tier1ExtractorInput` | dataclass or TypedDict | `tier1.extractor.py` | Input: `file_path`, `language_codes` from profile |
| `Tier1PageResult` | dataclass or TypedDict | `tier1.extractor.py` | Per-page result: `page_num`, `text`, `char_count`, `extraction_method` |
| `Tier1ExtractorResult` | dataclass or TypedDict | `tier1.extractor.py` | Full result: `status`, `pages`, `total_char_count`, `avg_chars_per_page`, `below_min_chars_flag`, `language_codes`, `extraction_method` |
| `extract_docx` | function | `tier1.extractor.py` | Extract text from `.docx` via python-docx; returns `Tier1ExtractorResult` |
| `extract_pdf_text_layer` | function | `tier1.extractor.py` | Extract text from `.pdf` text layer via pdfplumber; returns `Tier1ExtractorResult` |
| `extract_tier1` | function | `tier1.extractor.py` | Dispatcher: routes by file extension to `extract_docx` or `extract_pdf_text_layer`; raises `UnsupportedFileTypeError` for other extensions |
| `UnsupportedFileTypeError` | exception | `tier1.extractor.py` | Raised when file extension is not `.docx` or `.pdf` |
| `MIN_CHARS_PER_PAGE` | constant | `tier1.extractor.py` | 100 (from roadmap Quality Gates table; line 459) |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
| --- | --- | --- | --- | --- |
| Tier 1 python-docx .docx extraction | Execution Plan step 3 | `extract_docx` function | `pytest test_tier1_extractor.py -k docx` | ASSIGNED |
| Tier 1 pdfplumber .pdf text-layer extraction | Execution Plan step 4 | `extract_pdf_text_layer` function | `pytest test_tier1_extractor.py -k pdf` | ASSIGNED |
| char_count/page output (MIN_CHARS signal) | Execution Plan step 5 | `Tier1PageResult.char_count`; `avg_chars_per_page` | test: below_min_chars_flag set when avg < 100 | ASSIGNED |
| language_codes carried from profile (not inferred) | Execution Plan step 6 | `Tier1ExtractorResult.language_codes` | test: language_codes in result match input; no detection logic | ASSIGNED |
| No Tier 2 / OCR in this tranche | Forbidden scope | no OCR import, no pdf2image import | reviewer scan: grep for OCR/pdf2image in source | ASSIGNED |
| No runtime claim beyond Tier 1 source | Claim Boundary | claim boundary text in return packet | reviewer claim scan | ASSIGNED |
| GC-051 coverage | Execution Plan step 8 | JSON + MD registry entries | registry checker | ASSIGNED |

## Worker Autonomy / No-Question Rule

Allowed-scope gate or formatting failures are mandatory remediation. The worker
must repair and rerun them without asking the operator. Escalate only when the
repair requires forbidden paths, public-sync, provider/key use, OCR model
download, corpus ingestion, repo dependency addition, or a higher-risk claim.

## Work-Order Fulfillment Manifest

| Path | Required at handoff | Purpose |
| --- | --- | --- |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/tier1.extractor.py` | Yes | Tier 1 extractor module |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_tier1_extractor.py` | Yes | Focused unit tests |
| `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | Yes (additive update) | GC-051 registry |
| `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | Yes (additive update) | GC-051 human index |
| `docs/reviews/CVF_LPCI2_EX_T2_TIER1_EXTRACTOR_WORKER_RETURN_2026-06-11.md` | Yes | Worker evidence packet |

## Forbidden Path Manifest

| Path | Reason |
| --- | --- |
| `EXTENSIONS/**/package.json` | No repo dependency addition authorized |
| `EXTENSIONS/**/package-lock.json` | No repo dependency lockfile update authorized |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/**` | Existing CPF source must not be modified |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/**` | Existing LPF source must not be modified |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/**` | Web UI out of scope |
| `CVF-Workspace/Policy_Local/**` | External product workspace out of scope |
| `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` except additive entry | No destructive registry edit |
| `docs/roadmaps/CVF_LPCI2_T11_POLICYLOCAL_CORPUS_EXPANSION_READINESS_ROADMAP_2026-06-07.md` | T11/T12 readiness must not reopen |
| `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync\**` | No public-sync authorized |

## Write Ownership

Owned files or modules:

- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/tier1.extractor.py` (create-only)
- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_tier1_extractor.py` (create-only)
- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/__init__.py` (create-only if needed)
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` (additive update)
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` (additive update)
- `docs/reviews/CVF_LPCI2_EX_T2_TIER1_EXTRACTOR_WORKER_RETURN_2026-06-11.md` (create-only)

Write mode:

create-only for worker artifacts; additive-update for registry files.

## Execution Plan

1. Capture `executionBaseHead` with `git rev-parse --short HEAD`.
2. Run required pre-flight checks (import probes + Test-Path + pre-implementation gate).
3. Create `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/` directory structure if absent:
   `src/` and `tests/` subdirectories with `__init__.py` stubs.
4. Implement `extract_docx(input: Tier1ExtractorInput) -> Tier1ExtractorResult`:
   - Use `python-docx` (`from docx import Document`) to open `.docx` file.
   - Extract paragraph text per paragraph, group by page approximation
     (python-docx has no native page breaks; treat the full document as one
     logical "page" for Tier 1; record `page_count=1` and `page_num=1`).
   - Compute `char_count` and `avg_chars_per_page`.
   - Set `below_min_chars_flag = avg_chars_per_page < MIN_CHARS_PER_PAGE`.
   - Copy `language_codes` from input (do not infer from content).
   - Return `Tier1ExtractorResult` with `extraction_method="python-docx"`.
5. Implement `extract_pdf_text_layer(input: Tier1ExtractorInput) -> Tier1ExtractorResult`:
   - Use `pdfplumber` to open `.pdf` file.
   - For each page, extract text via `page.extract_text()` or empty string if None.
   - Record per-page `Tier1PageResult` with `char_count = len(text)`.
   - Compute `avg_chars_per_page = total_char_count / page_count`.
   - Set `below_min_chars_flag = avg_chars_per_page < MIN_CHARS_PER_PAGE`.
   - Copy `language_codes` from input (do not infer from content).
   - Return `Tier1ExtractorResult` with `extraction_method="pdfplumber"`.
6. Implement `extract_tier1(input: Tier1ExtractorInput) -> Tier1ExtractorResult`:
   - Inspect `file_path` extension (`.lower()`).
   - `.docx` --> call `extract_docx`.
   - `.pdf` --> call `extract_pdf_text_layer`.
   - Anything else --> raise `UnsupportedFileTypeError`.
7. Write focused unit tests in `test_tier1_extractor.py`:
   - Test `extract_docx` with an in-memory `.docx` (use `python-docx` to create
     a temp docx file with known text; assert char_count and language_codes).
   - Test `extract_pdf_text_layer` with a minimal synthetic `.pdf` (use
     `pdfplumber` with a fixture; if creating a minimal PDF inline is not
     feasible without additional deps, use a small fixture file or skip with
     a clear evidence comment; do not download test assets from external URLs).
   - Test `extract_tier1` dispatcher: correct routing for `.docx` and `.pdf`
     extensions; `UnsupportedFileTypeError` raised for `.txt` and `.png`.
   - Test `below_min_chars_flag`: set True when avg < 100, False when avg >= 100.
   - Test `language_codes` pass-through: output matches input; no detection.
   - All tests must be deterministic and local (no network, no corpus files).
8. Update `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` with additive
   entries for the new source module and test file (status `SCANNED`,
   `findings: []`, `negativeSearchTerms: []`, `nextScanRecommendation: "NONE_REQUIRED"`).
9. Update `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` with Quick
   Lookup rows for the two new entries.
10. Run `python -m pytest EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/ -v` and
    record result.
11. Run `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast --serial`
    and record result. Repair any allowed-scope violations before return.
12. Run `git status --short` and `git diff --name-status` to confirm only owned
    paths are modified.
13. Stage only the owned worker artifacts and return without committing.

## Design Control Carry-Forward

| Design control | Roadmap source | Work-order handling | Verdict |
| --- | --- | --- | --- |
| Scope boundary | roadmap `## Scope` | Tier 1 only; Tier 2/3/5 and DSCP wire-in blocked | PASS |
| Non-goals | roadmap `## Non-Goals` | forbidden scope blocks OCR/provider/corpus/EC-02/legal/public claims | PASS |
| Lane split | roadmap `## Dispatch Boundary` | executes EX lane Tier 1 only; EC lane remains pending operator decision | PASS |
| Dependency/source-verification plan | EX-T1 audit report; roadmap lines 310-328 | COMPOSED_STACK_PREFERRED confirmed; pdfplumber + python-docx import PASS | PASS |
| Claim boundary | roadmap `## Claim Boundary` | inherited and repeated in this work order | PASS |
| Acceptance criteria | roadmap `## Acceptance Criteria` | mapped in trace matrix above | PASS |
| Verification/evidence | roadmap `## Verification And Evidence` | pytest run + reviewer-fast + git diff required | PASS |
| Dispatch-readiness decision | EX-T1 COMPOSED_STACK_PREFERRED + operator 2026-06-11 instruction | EX-T2 Tier 1 may dispatch; EX-T3+ remain blocked | PASS |

## Evidence Requirements

Required evidence:

- `git rev-parse --short HEAD` result recorded as `executionBaseHead`.
- `git status --short` before return.
- `git diff --name-status` showing only owned worker files.
- Import probes for pdfplumber and python-docx (recorded in return packet).
- `pytest` result for all Tier 1 tests.
- `reviewer-fast` command and result (or bounded blocker with action required).
- Claim boundary statement.

Evidence Trace Block requirements:

| Claim | Command | Result | Key path | Verdict |
| --- | --- | --- | --- | --- |
| Worker must fill one row per significant implementation claim | command or assertion | observed evidence | source path or test | EXISTS / ABSENT / PARTIAL / DRIFT |

Base-anchor evidence:

- `dispatchBaseHead`: `2d6510ca`
- `executionBaseHead`: worker must capture before edits
- `closureBaseHead`: reviewer-owned after return
- Commit mode: `WORKER_MUST_NOT_COMMIT`
- Pending-artifact component gates: reviewer-fast required before return
- Committed-range `pre-closure`: N/A before Codex review

## Acceptance Criteria

| Criterion | Required result |
| --- | --- |
| `extract_docx` function present and returns `Tier1ExtractorResult` | PASS |
| `extract_pdf_text_layer` function present and returns `Tier1ExtractorResult` | PASS |
| `extract_tier1` dispatcher routes by extension; raises `UnsupportedFileTypeError` for unsupported types | PASS |
| `below_min_chars_flag` set True when avg < 100 chars/page | PASS |
| `language_codes` in result matches input (no detection logic in source) | PASS |
| All focused tests pass | PASS |
| No OCR, pdf2image, or Tier 2/3 import present in source | PASS |
| GC-051 registry entries added | PASS |
| No forbidden path modified | PASS |

## Fail Conditions

| Condition | Action |
| --- | --- |
| Worker needs OCR or pdf2image import to complete Tier 1 | STOP and return blocked diagnostic |
| Worker needs new Python package not already installed | STOP and return blocked diagnostic |
| Worker needs provider/API key use | STOP and return blocked diagnostic |
| Worker needs corpus file ingestion | STOP and return blocked diagnostic |
| Any test fails | Repair within allowed scope; rerun; do not return until tests pass |
| Any forbidden path changes | STOP and return blocked diagnostic |
| Language detection logic introduced | STOP and return blocked diagnostic |

## Review Gate

Implementation may proceed only after:

- this work order is dispatched;
- GC-018 exists;
- worker captures `executionBaseHead`;
- `pre-implementation` gate passes on the dispatch range.

Closure may proceed only after Codex confirms:

- all Tier 1 tests pass;
- no Tier 2/3/OCR/provider/corpus/EC-02/T12/legal-quality/current-law/public
  claim was introduced;
- forbidden paths are untouched;
- reviewer-fast passed or a bounded blocker is recorded.

## Return Packet Requirements

Claude must return uncommitted artifacts with:

- `executionBaseHead`;
- `git status --short`;
- `git diff --name-status`;
- import probe results;
- `pytest` result (all tests, pass/fail count);
- `reviewer-fast` result;
- exact changed files;
- claim boundary.

## Closure Checklist

- [ ] Worker return reviewed by Codex
- [ ] All Tier 1 tests pass confirmed
- [ ] Forbidden path scan PASS
- [ ] Reviewer-fast PASS confirmed or bounded blocker recorded
- [ ] Codex commits accepted worker artifacts if PASS
- [ ] Session continuity synced after material commit
- [ ] Next tranche decision recorded: EX-T3 (OCR), alternate design, or blocked

## Return-To-Orchestrator Conditions

Return to Codex without continuing if:

- pre-flight fails outside allowed remediation;
- Tier 1 implementation requires a package that is not already installed;
- tests cannot be made deterministic and local without external corpus files;
- any forbidden path changes.

## Operator Checkpoint

operator.checkpoint.waiver: operator authorized EX-T2 work-order creation on
2026-06-11. Operator approval remains required for EX-T3 (OCR), EX-T4 (quality
gate), EX-T5 (DSCP wire-in), dependency addition, OCR model download, corpus
ingestion, public-sync, provider/key use, or readiness claims.

## Claim Boundary

This work order authorizes only Tier 1 digital-native extraction source,
focused tests, and GC-051 registry entries. It does not prove OCR quality,
Tier 2/3 extraction fitness, retrieval quality, corpus ingestion, EC-02 runtime
behavior, T12 eligibility, legal advice quality, current-law status, provider
behavior, hosted readiness, production readiness, public readiness, public-sync,
memory reinjection, high-risk promotion, Learning Orchestrator runtime behavior,
or autonomous mutation.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance work order; not public-synced.
