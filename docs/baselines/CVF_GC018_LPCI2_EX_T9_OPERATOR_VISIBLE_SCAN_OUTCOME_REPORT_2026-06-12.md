# CVF GC-018 Baseline: LPCI2 EX-T9 Operator-Visible Scan Outcome Report

Memory class: FULL_RECORD

Status: DISPATCHED

docType: baseline

Date: 2026-06-12

baseHead: `6b8e75a9`

---

## Purpose

Authorize a bounded EX tranche that turns extraction quality and storage
boundary evidence into a domain-agnostic operator report.

## Predecessor Evidence

| Artifact | Evidence | Disposition |
| --- | --- | --- |
| EX-T8 material closure | commit `43eb9624` | ACCEPT |
| EX-T8 completion | `docs/reviews/CVF_LPCI2_EX_T8_EXTRACTION_AUTHORITY_AND_STORAGE_BOUNDARY_COMPLETION_2026-06-12.md` | ACCEPT |
| EX-T9 roadmap | `docs/roadmaps/CVF_LPCI2_EX_T9_OPERATOR_VISIBLE_SCAN_OUTCOME_REPORT_ROADMAP_2026-06-12.md` | ACCEPT |

## Decision

Authorize:

- `ScanOutcomeFinding` and `ScanOutcomeReport` immutable records;
- stable mapping from extraction quality flags to operator actions;
- optional generic additional findings;
- deterministic JSON and Markdown rendering;
- UTF-8 file output to caller-selected paths;
- no raw chunk/OCR text release.

## Scope Boundary

In scope:

- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py`;
- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_scan_outcome_report.py`;
- focused tests, registry, roadmap, completion, and session closure.

Out of scope:

- changes to EC files or Policy_Local;
- inference of missing metadata;
- provider calls, OCR execution, corpus ingestion, retrieval, or public-sync;
- legal/current-status or production/public-readiness claims.

## Source Verification Table

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| Extraction quality report exists | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 101 | `ExtractionQualityReport` | extraction pipeline dataclass | ACCEPT |
| Quality flags exist | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 105 | `quality_flags` | `ExtractionQualityReport` | ACCEPT |
| Storage boundary exists | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 152 | `ExtractionStorageBoundary` | extraction pipeline dataclass | ACCEPT |
| Boundary hash exists | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 159 | `boundary_sha256` | `ExtractionStorageBoundary` | ACCEPT |
| Storage boundary builder exists | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 424 | `build_extraction_storage_boundary` | extraction pipeline function | ACCEPT |

## New Doc-Only Fields

| Field | Purpose |
| --- | --- |
| `reportVersion` | version the serialized report contract |
| `operatorReviewRequired` | expose whether operator action is required |
| `claimBoundary` | prevent report output from being read as semantic validation |

## Negative Search And Collision Discipline

Search root: `EXTENSIONS/`, `docs/`, and `governance/`.

Search command:

`rg -n --fixed-strings "ScanOutcomeReport|build_scan_outcome_report|write_scan_outcome_report_files" EXTENSIONS docs governance`

Result at base `6b8e75a9`: proposed runtime symbols are absent. Existing
operator reports are domain-specific documents and do not collide with the
new generic EX runtime contract.

## Acceptance Criteria

1. Stable quality-flag-to-action mapping.
2. Deterministic JSON and Markdown.
3. UTF-8 Unicode path support.
4. No raw content release.
5. Tests and governance gates pass.
6. EC remains parked.

## Evidence / Verification

- source-owner verification against `extraction_pipeline.py`;
- focused synthetic tests for PASS and each current quality flag;
- deterministic JSON parse and Markdown content assertions;
- Unicode filename write/read evidence;
- full extraction-foundation pytest;
- reviewer-fast and pre-commit governance gates.

## Claim Boundary

This baseline authorizes reporting mechanics only. It does not authorize
metadata correction, domain decisions, retrieval, provider use, or readiness.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private EX control-plane/runtime foundation batch.
