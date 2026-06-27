# CVF GC-018 LPCI2 EX-T2 Tier 1 Digital-Native Extractor Baseline

Memory class: FULL_RECORD

Status: DISPATCHED

docType: baseline

Date: 2026-06-11

---

## Purpose

Authorize LPCI2 EX-T2 as a bounded Tier 1 digital-native extractor
implementation lane using the EX-T1 COMPOSED_STACK_PREFERRED dependency
verdict. This baseline exists to give the worker a source-backed authority shell
before implementation.

## Authorization

Authorized by operator instruction on 2026-06-11: open EX-T2 child lane as
Tier 1 digital-native extraction implementation, bounded to COMPOSED_STACK_PREFERRED
verdict from EX-T1 audit (python-docx + pdfplumber).

Active state:

`CVF_SESSION/ACTIVE_SESSION_STATE.json`

Active handoff:

`AGENT_HANDOFF_V17_2026-06-07.md`

## Decision

Open LPCI2 EX-T2 as a bounded implementation tranche for Tier 1 digital-native
document text extraction. Worker delivers a new owned extraction module, focused
unit tests, and GC-051 registry entries. Codex reviews, gates, and commits.

This tranche implements only Tier 1 (digital-native): python-docx for .docx
files and pdfplumber for PDF text-layer extraction. Tier 2 (OCR fallback) and
Tier 3 (quality gate) remain blocked until EX-T3 and EX-T4 are separately
authorized.

## Predecessor Evidence

| Predecessor | Closure evidence | Disposition |
| --- | --- | --- |
| EX-T1 dependency source audit | `docs/reference/CVF_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_REPORT_2026-06-11.md`; `docs/reference/CVF_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_SUMMARY_2026-06-11.json`; recommendation `COMPOSED_STACK_PREFERRED` | ACCEPT |
| EX-T1 worker return | `docs/reviews/CVF_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_WORKER_RETURN_2026-06-11.md` | ACCEPT |
| Extraction and EC-02 roadmap | `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md`; EX-T2 tranche defined at line 472 | ACCEPT |
| Governed work design-control standard | `docs/reference/CVF_GOVERNED_WORK_LIFECYCLE_AND_DESIGN_CONTROL_STANDARD_2026-06-11.md` | ACCEPT |
| DSCP-T11F profile selection adapter | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.profile.selection.adapter.ts`; commit `76cdf464` | ACCEPT |

## Scope / Target / Owner Boundary

In scope:

- Implement a new CVF extraction owner module for Tier 1 digital-native
  extraction (.docx via python-docx; .pdf text layer via pdfplumber).
- Write focused unit tests for the Tier 1 extractor covering both file classes
  and quality-signal surface (char count per page).
- Update GC-051 corpus scan registry for new source and test paths.
- Produce worker return packet.

Out of scope:

- No Tier 2 OCR fallback (pdf2image, EasyOCR, Tesseract) -- blocked to EX-T3.
- No Tier 3 quality gate module -- blocked to EX-T4.
- No DSCP pipeline wire-in (descriptor, gate, receipt) -- blocked to EX-T5.
- No repo dependency addition for packages not already installed (pdfplumber
  and python-docx are already present; no new lockfile entries).
- No corpus ingestion, chunking, retrieval, vector index, or EC-02 semantic change.
- No provider calls, API keys, public-sync, hosted readiness, production
  readiness, public readiness, legal-quality claim, or current-law claim.
- No EX-T3 / EX-T4 / EX-T5 scope in this work order.

## Source Verification Summary

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| EXISTS: EX-T2 tranche in roadmap | `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md` | line 472 | `EX-T2` | parent roadmap work plan | ACCEPT |
| EXISTS: Tier 1 architecture (.docx + pdfplumber) | `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md` | line 316 | `Option 1 - Composed stack` | parent roadmap | ACCEPT |
| EXISTS: OCR auto-escalation threshold | `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md` | lines 396 and 407 | `char_count/page`; `MIN_CHARS` | parent roadmap architecture | ACCEPT |
| EXISTS: Quality gate threshold | `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md` | line 459 | `MIN_CHARS` | parent roadmap Quality Gates table | ACCEPT |
| EXISTS: COMPOSED_STACK_PREFERRED audit verdict | `docs/reference/CVF_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_REPORT_2026-06-11.md` | lines 295 and 307 | `COMPOSED_STACK_PREFERRED` | EX-T1 audit report | ACCEPT |
| EXISTS: pdfplumber import probe | `docs/reference/CVF_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_REPORT_2026-06-11.md` | lines 95 and 318 | `importProbeResult`; `pdfplumber.__version__` | EX-T1 audit | ACCEPT |
| EXISTS: python-docx import probe | `docs/reference/CVF_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_REPORT_2026-06-11.md` | lines 116, 319, and 320 | `importProbeResult`; `docx` | EX-T1 audit | ACCEPT |
| EXISTS: DscpDomainProfile.languageCodes | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | line 31 | `languageCodes` | `DscpDomainProfile` | ACCEPT |
| EXISTS: design-control standard | `docs/reference/CVF_GOVERNED_WORK_LIFECYCLE_AND_DESIGN_CONTROL_STANDARD_2026-06-11.md` | line 93 | `Design Control Gate` | lifecycle standard | ACCEPT |
| EXISTS: work-order design carry-forward | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | line 981 | `Design Control Carry-Forward` | work-order template | ACCEPT |

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

## Evidence / Verification

| Evidence | Required result |
| --- | --- |
| Tier 1 extractor source module | present; passes TypeScript or Python type check |
| Focused unit tests | present; all tests pass |
| GC-051 registry update | JSON + Markdown entries added for source and test paths |
| Worker return packet | present with git evidence and claim boundary |
| Reviewer-fast gate | PASS before return (after Codex handoff sync) |
| Forbidden path scan | no Tier 2/3/5, corpus, EC-02, provider, or public-sync path modified |

## Dispatch Evidence Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI2_EX_T2_TIER1_DIGITAL_NATIVE_EXTRACTOR_FOR_CLAUDE_2026-06-11.md` | `Status: DISPATCHED` before worker execution | PASS |
| Extractor source | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/tier1.extractor.py` | worker-created module | N/A with reason: worker output |
| Extractor tests | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_tier1_extractor.py` | worker-created tests | N/A with reason: worker output |
| GC-051 JSON entry | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | additive entry for extractor source and test | N/A with reason: worker output |
| GC-051 MD entry | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | Quick Lookup row added | N/A with reason: worker output |
| Worker return | `docs/reviews/CVF_LPCI2_EX_T2_TIER1_EXTRACTOR_WORKER_RETURN_2026-06-11.md` | worker return packet | N/A with reason: worker output |
| Session continuity | active handoff and state registry | reviewer sync after Codex review | N/A with reason: reviewer output |

## Claim Boundary

This baseline authorizes Tier 1 digital-native extraction implementation and
focused tests only. It does not prove OCR quality, Tier 2/3 extraction,
retrieval quality, corpus ingestion, EC-02 runtime behavior, T12 eligibility,
provider behavior, public readiness, hosted readiness, production readiness,
public-sync, memory reinjection, high-risk promotion, Learning Orchestrator
runtime behavior, or autonomous mutation.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance baseline; not public-synced.
