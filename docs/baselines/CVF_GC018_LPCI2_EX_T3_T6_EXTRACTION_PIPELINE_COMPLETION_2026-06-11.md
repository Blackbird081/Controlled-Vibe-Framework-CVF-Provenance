# CVF GC-018 LPCI2 EX-T3 Through EX-T6 Extraction Pipeline Completion

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: baseline

Date: 2026-06-11

executionBaseHead: `041cb307`

---

## Purpose

Authorize Codex single-agent multi-role completion of the unblocked LPCI2
extraction roadmap rows EX-T3 through EX-T6 as one bounded local deterministic
foundation batch.

This batch completes the pipeline contract surfaces that can be safely closed
without downloading OCR models, adding repo dependencies, ingesting corpus
content, mutating external Policy_Local, or making EC-02/current-law claims.

## Authorization

Operator instruction on 2026-06-11 authorized Codex to use the prior
single-agent multi-role rule and complete the related roadmap work.

Active state:

`CVF_SESSION/ACTIVE_SESSION_STATE.json`

Active handoff:

`AGENT_HANDOFF_V17_2026-06-07.md`

## Decision

Open and close a bounded EX-T3 through EX-T6 local foundation tranche:

- EX-T3: Tier 2 OCR fallback adapter boundary and OCR language mapping.
- EX-T4: Tier 3 quality gate and fixed-window chunk schema.
- EX-T5: DSCP descriptor handoff shape for extracted chunks.
- EX-T6: GC-051 source/test coverage for the new extraction pipeline surfaces.

## Scope / Target / Owner Boundary

In scope:

- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py`;
- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_extraction_pipeline.py`;
- GC-051 JSON/Markdown registry coverage;
- parent roadmap row/status updates;
- completion/work-order evidence and session continuity.

Out of scope:

- no OCR dependency installation;
- no EasyOCR/Tesseract/Poppler/LibreOffice/ImageMagick model or binary
  download;
- no package/lockfile update;
- no external Policy_Local mutation;
- no corpus ingestion, OCR quality claim, provider/API-key use, public-sync,
  current-law/legal-quality claim, EC-T5 successor activation, EC-T6 retrieval
  disclosure, T12 unlock, production readiness, public readiness, memory
  reinjection, high-risk promotion, or autonomous mutation.

## Source Verification Summary

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| EXISTS: EX-T3 through EX-T6 rows | `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md` | lines 487-490 | `EX-T3`; `EX-T4`; `EX-T5`; `EX-T6` | parent roadmap | ACCEPT |
| VALUE_SET: MIN_CHARS threshold is 100 | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/tier1_extractor.py` | line 19 | `MIN_CHARS_PER_PAGE` | Tier 1 extractor module | ACCEPT |
| EXISTS: Tier 1 escalation signal | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/tier1_extractor.py` | lines 55 and 131 | `below_min_chars_flag` | Tier 1 extractor result | ACCEPT |
| EXISTS: DSCP domain profile application helper | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | line 96 | `applyDomainProfileToDescriptorInput` | DSCP domain profile contract | ACCEPT |
| EXISTS: DSCP profile selection adapter | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.profile.selection.adapter.ts` | line 57 | `selectAndApplyDscpDomainProfile` | DSCP profile selection adapter | ACCEPT |
| DOC_ONLY_NEW: extraction pipeline module | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 143 and following | `map_ocr_language_codes`; `extract_tier2_ocr`; `evaluate_extraction_quality`; `chunk_extracted_pages`; `build_extraction_dscp_descriptor_inputs` | EX-T3 through EX-T5 local pipeline | ACCEPT |

## Evidence Reuse And Encoding Plan

verificationMode: `REUSE_PRIOR_VERIFICATION`

priorVerificationArtifact:

- `docs/reference/CVF_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_SUMMARY_2026-06-11.json`
- `docs/reference/CVF_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_REPORT_2026-06-11.md`
- `docs/reviews/CVF_LPCI2_EX_T2_TIER1_EXTRACTOR_COMPLETION_2026-06-11.md`

priorVerificationAnchor: EX-T1 selected the composed stack for EX-T2 only and
kept OCR dependency/model decisions conditional; EX-T2 closed Tier 1
digital-native extraction with no OCR.

freshRecomputeRequired: `NO`

recomputeReason: `N/A with reason - this batch consumes committed predecessor
evidence and does not reopen external source binaries.`

unicodePathHandling: `N/A with reason - no external Unicode paths are opened.`

extractedTextAuthority: `N/A with reason`

## Claim Boundary

This baseline authorizes local deterministic extraction foundation work only.
It does not prove OCR model quality, production OCR readiness, legal-policy
answer quality, governed retrieval behavior, or public readiness.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance baseline; no public-sync authorized.
