# CVF GC-018 Baseline: MEOR-T2 Extraction Metadata Finding Normalization

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: baseline

Date: 2026-06-12

Author: Codex

baseHead: `662e3c76`

## Purpose

Authorize a bounded extraction-foundation implementation of the closed MEOR-T1
metadata evidence semantics and integration with the existing EX-T9 report
extension point.

## Scope / Target / Owner Boundary

Target owner: `EXTENSIONS/CVF_EXTRACTION_FOUNDATION`.

Allowed:

- one new metadata evidence normalization module;
- one focused test module;
- adapter output as existing `ScanOutcomeFinding` records;
- GC-051 and closure governance updates.

Forbidden:

- a second report renderer;
- DSCP profile changes;
- external Policy_Local changes;
- OCR, corpus ingestion, provider use, retrieval, or gate activation;
- raw source or extracted content release.

## Dependency Release Evidence

| Dependency | Artifact | Commit | Result |
| --- | --- | --- | --- |
| MEOR-T1 contract | `docs/reference/CVF_METADATA_EVIDENCE_AND_OPERATOR_RESOLUTION_CONTRACT_2026-06-12.md` | `f3c7ff11` | PASS |
| MEOR-T1 semantics | `docs/reference/CVF_METADATA_EVIDENCE_AND_OPERATOR_RESOLUTION_SEMANTICS_2026-06-12.json` | `f3c7ff11` | PASS |
| MEOR-T1 closure | `docs/reviews/CVF_MEOR_T1_METADATA_EVIDENCE_RESOLUTION_CONTRACT_COMPLETION_2026-06-12.md` | `22818605` | CLOSED_PASS_BOUNDED |
| Session sync | active handoff/state/memory | `662e3c76` | PASS |

## Source Verification Summary

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| Generic finding record | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py` | line 32 | `ScanOutcomeFinding` | dataclass | ACCEPT |
| Additional finding extension | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py` | lines 131-144 | `additional_findings` | `build_scan_outcome_report` | ACCEPT |
| Existing renderers | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py` | lines 202, 217 | `render_scan_outcome_report_json`, `render_scan_outcome_report_markdown` | functions | ACCEPT |
| Canonical semantics | `docs/reference/CVF_METADATA_EVIDENCE_AND_OPERATOR_RESOLUTION_SEMANTICS_2026-06-12.json` | `rules`, `invariants` | `cvf.metadataEvidenceResolution.meor.t1.v1` | machine semantics | ACCEPT |

## Decision

Implement a pure deterministic evaluator and a narrow adapter to the existing
report finding record. The evaluator must fail closed and must not load raw
document content.

## Required Evidence

- focused tests for all 21 allowed state/basis pairs;
- invalid-state and missing-pointer failures;
- hint non-release, operator/source distinction, and non-mutation assertions;
- EX-T9 report integration test;
- full extraction-foundation pytest PASS;
- Python compile PASS;
- reviewer-fast and closure gates PASS.

## Claim Boundary

This baseline authorizes local deterministic normalization only. It does not
prove metadata truth, source authenticity, domain eligibility, gate behavior,
Policy_Local readiness, provider behavior, production readiness, or public
readiness.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private foundation implementation; no public-sync authorized.
