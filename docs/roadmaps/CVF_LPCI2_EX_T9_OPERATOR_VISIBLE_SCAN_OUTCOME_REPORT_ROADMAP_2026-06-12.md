# CVF LPCI2 EX-T9 Operator-Visible Scan Outcome Report Roadmap

Memory class: FULL_RECORD

Status: DISPATCHED

docType: roadmap

Date: 2026-06-12

Owner: Codex

---

## Authorization / Decision

Decision: `EX_T9_DISPATCHED`.

Operator authorization and EX-T8 closure permit this final bounded EX
foundation tranche. EC remains parked.

## Purpose

Close the final known EX foundation gap before EC resumes: convert generic
scan/extraction quality signals into a deterministic report that both machines
and non-coder operators can inspect.

The report is domain-agnostic. It does not know whether the source belongs to
legal policy, a technical project, company documents, or another domain.

## Scope / Target / Owner Boundary

Target: CVF Extraction Foundation operator reporting contract.

Owner: `EXTENSIONS/CVF_EXTRACTION_FOUNDATION`.

Boundary: generic scan signals only; no domain decision or external workspace.

## Scope

- generic report records;
- quality-flag normalization;
- JSON and Markdown rendering;
- UTF-8 caller-selected output paths;
- focused tests and governance closure.

## Non-Goals

- metadata inference or correction;
- EC activation;
- external Policy_Local integration;
- OCR execution, provider calls, retrieval, or public-sync;
- semantic quality or readiness claims.

## Authority Chain

- Operator instruction on 2026-06-12: finish all EX work before returning to EC.
- EX-T8 material closure: commit `43eb9624`.
- EX-T8 completion:
  `docs/reviews/CVF_LPCI2_EX_T8_EXTRACTION_AUTHORITY_AND_STORAGE_BOUNDARY_COMPLETION_2026-06-12.md`.
- Governed lifecycle standard:
  `docs/reference/CVF_GOVERNED_WORK_LIFECYCLE_AND_DESIGN_CONTROL_STANDARD_2026-06-11.md`.

## Current Runtime Freshness Verification

Verified at base `6b8e75a9`:

`rg -n "class ExtractionQualityReport|class ExtractionStorageBoundary|quality_flags:|boundary_sha256:|def build_extraction_storage_boundary" EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py`

Observed:

- `ExtractionQualityReport` exists and carries quality flags and metrics.
- `ExtractionStorageBoundary` exists and carries the quality report and boundary hash.
- No `ScanOutcomeReport`, `build_scan_outcome_report`, or
  `write_scan_outcome_report_files` symbol exists in current source.

## Design Control Gate

Design verdict: `PASS_BOUNDED`.

Selected design:

1. Add a separate `scan_outcome_report.py` module.
2. Normalize extraction flags into operator findings.
3. Permit additional domain-agnostic findings from later pipeline stages.
4. Produce deterministic JSON and readable Markdown without raw chunk text.
5. Write UTF-8 files through `pathlib.Path`, including Unicode paths.

Rejected design:

- Embedding Policy_Local or EC-02 fields in the EX report.
- Writing raw OCR or chunk text into the report.
- Coupling report generation to providers, retrieval, or corpus ingestion.

## Dispatch Boundary

Allowed:

- new EX source module and focused test module;
- JSON and Markdown serialization;
- caller-selected UTF-8 file output;
- generic additional findings;
- GC-051 registry and governed closure artifacts.

Forbidden:

- EC-T4 metadata decisions or EC-T5/EC-T6 activation;
- external Policy_Local writes;
- corpus ingestion or mutation;
- OCR dependency/model installation;
- provider/API-key use;
- retrieval behavior;
- public-sync;
- current-law, legal-quality, production, or public-readiness claims.

## Proposed Tranche

| Tranche | Deliverable | Status |
| --- | --- | --- |
| EX-T9 | Domain-agnostic `ScanOutcomeReport`, quality-flag normalization, deterministic JSON/Markdown rendering, UTF-8 file writer, focused tests | DISPATCHED |

## Work Plan

1. Dispatch source-verified GC-018 and work order.
2. Implement the separate report module.
3. Add focused synthetic tests.
4. Run full extraction-foundation tests and governance gates.
5. Close EX-T9, update GC-051, and sync continuity.

## Acceptance Criteria

1. PASS extraction produces `READY_FOR_DOWNSTREAM` with no required operator action.
2. Any quality flag produces `OPERATOR_REVIEW_REQUIRED`.
3. `EMPTY`, `NEEDS_TIER2_OCR`, `PARTIAL_EXTRACTION`, and
   `OCR_LOW_CONFIDENCE` map to stable finding codes and actions.
4. Additional generic findings can be appended without domain-specific fields.
5. JSON output is deterministic and machine-readable.
6. Markdown output contains source, disposition, metrics, findings, and actions.
7. Reports contain no descriptor list, raw chunk text, or raw OCR text.
8. UTF-8 output works with a Unicode filename.
9. Focused tests and governance gates pass.

## Verification And Evidence

- `python -m py_compile` for the new source module;
- focused pytest for EX-T9;
- full extraction-foundation pytest;
- JSON parse of rendered report;
- Unicode-path write/read test;
- reviewer-fast and pre-commit governance gates;
- changed-path evidence proving no EC, Policy_Local, provider, or public-sync change.

## Governed Work Lifecycle

`INTAKE -> DESIGN -> SPEC -> WORK ORDER -> BUILD -> REVIEW -> FREEZE`

- INTAKE: operator requires all EX foundation work closed first.
- DESIGN: this roadmap selects a domain-agnostic reporting contract.
- SPEC: GC-018 fixes report fields and claim boundary.
- WORK ORDER: EX-T9 work order fixes implementation and evidence scope.
- BUILD: Codex implements source and tests.
- REVIEW: focused tests plus governance gates.
- FREEZE: closure packet, registry update, and session sync.

## Claim Boundary

EX-T9 proves only deterministic report generation from supplied scan signals.
It does not prove extraction accuracy, OCR quality, metadata correctness,
domain eligibility, legal/current status, retrieval quality, or readiness.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance EX foundation work; no public-sync authorized.
