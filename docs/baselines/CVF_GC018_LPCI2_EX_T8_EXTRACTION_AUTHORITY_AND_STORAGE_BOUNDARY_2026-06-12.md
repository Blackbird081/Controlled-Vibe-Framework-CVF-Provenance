# CVF GC-018 Baseline: LPCI2 EX-T8 Extraction Authority And Storage Boundary

Memory class: FULL_RECORD

Status: DISPATCHED

docType: baseline

Date: 2026-06-12

Author: Claude (operator-directed; Codex review and explicit authorization required before dispatch)

baseHead: `7c92b20b`

---

## Purpose

Authorize a bounded Claude worker tranche that formalizes four decisions
the EX-T3 through EX-T7 extraction pipeline deliberately left open:

1. **Raw OCR storage decision** -- whether intermediate raw OCR page output is
   persisted alongside governed chunks, and if so under what authority level and
   with what lifecycle rule.

2. **Chunk authority level** -- what authority level a governed `ExtractionChunk`
   carries and how that level propagates through the DSCP descriptor handoff.

3. **Hash/offset rebuild contract** -- whether `(source_hash, char_start, char_end)`
   is sufficient to reconstruct a chunk from the source file, and what invariants
   the pipeline must enforce to make that true.

4. **Storage boundary for domain-agnostic scan layer** -- where governed chunks
   and their descriptor inputs are handed off, so the scan layer remains
   domain-agnostic and any project (PolicyLocal or otherwise) consumes them
   through a defined interface rather than reading internal pipeline state.

5. **Operator-visible scan outcome dependency** -- which EX follow-up must turn
   scan-layer gap signals into a bounded operator correction report before any
   domain-specific gate such as EC-T5 relies on those signals.

EX-T8 is a contract/schema tranche only. It produces TypeScript-side and
Python-side type additions plus a machine-readable boundary contract. It does
NOT install OCR dependencies, ingest real corpus files, write to Policy_Local
workspace, call providers, or make EC-02 retrieval claims.

---

## Predecessor Evidence

| Document | Status | Commit |
| --- | --- | --- |
| EX-T7 closure review | `docs/reviews/CVF_LPCI2_EX_T7_SENTENCE_BOUNDARY_CHUNKING_COMPLETION_2026-06-12.md` | `7c92b20b` (roadmap sync) |
| EX-T3 through EX-T6 closure review | `docs/reviews/CVF_LPCI2_EX_T3_T6_EXTRACTION_PIPELINE_COMPLETION_2026-06-11.md` | closed |
| EX-T2 Tier 1 extractor closure | `docs/reviews/CVF_LPCI2_EX_T2_TIER1_EXTRACTOR_COMPLETION_2026-06-11.md` | closed |
| EC-T3 schema update | `docs/baselines/CVF_GC018_LPCI2_EC_T3_CORPUS_RECORD_SCHEMA_UPDATE_2026-06-11.md` | `CLOSED_PASS_BOUNDED` |
| Parent roadmap (open question 3 -- raw OCR storage) | `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md` | Part A, line 517 |

---

## Decision

EX-T8 is authorized as a contract/schema-only tranche delivering:

**D-01 -- Raw OCR storage disposition.**
Raw OCR page output (intermediate `Tier2OcrPageResult` objects) is NOT persisted
to disk by the CVF extraction pipeline. The pipeline is stateless with respect
to raw OCR intermediates; callers who need an audit trail must capture and store
`Tier2OcrPageResult` objects themselves outside the pipeline boundary. This
keeps the scan layer domain-agnostic and free of project-specific storage
dependencies. A new `rawOcrRetained: bool` field on `ExtractionQualityReport`
records whether the caller captured raw OCR for audit.

**D-02 -- Chunk authority level.**
A governed `ExtractionChunk` carries `authority_level: Literal['EXTRACTED_TEXT']`
-- a new field added to the dataclass. `EXTRACTED_TEXT` is below `OPERATOR_SUPPLIED`
(manually curated) and below `CANONICAL_SOURCE` (authoritative registry entry),
but above `UNVERIFIED_RAW_OCR` (unvalidated intermediate). This authority level
is propagated into the DSCP descriptor metadata as `authorityLevel: "EXTRACTED_TEXT"`.
Non-extracted records (operator-supplied corpus entries) carry
`authorityLevel: "OPERATOR_SUPPLIED"` and are set by their intake path, not by
this pipeline.

**D-03 -- Hash/offset rebuild contract.**
`(source_hash, char_start, char_end)` is the canonical rebuild key for a chunk
derived from a digital-native (Tier 1) extraction. For Tier 2 OCR chunks,
`source_hash` alone plus `page_start/page_end` is the rebuild key;
`char_start/char_end` are offsets into the OCR output string, not into the
source file byte stream, so they are NOT sufficient to reconstruct OCR text from
the source file without re-running OCR. A new `rebuildClass` field on
`ExtractionChunk` encodes which rebuild contract applies:
`TIER1_CHAR_OFFSET` (deterministic, char-level rebuild from source)
vs `TIER2_PAGE_REOCR` (requires re-running OCR on source pages).

**D-04 -- Storage boundary contract.**
The extraction pipeline hands off `ExtractionDscpDescriptorInput` records
through a new `ExtractionStorageBoundary` dataclass. This boundary type is the
canonical output surface of the pipeline. A project consumes the boundary record,
not internal chunk lists. The boundary record carries: `descriptor_inputs`,
`quality_report`, `chunk_count`, `rawOcrRetained` flag, and a `boundary_sha256`
hash over the descriptor_input artifact_ids and source_hashes. Projects must NOT
read `ExtractionChunk.text` directly; they consume chunks through descriptor
inputs only.

**D-05 -- Operator correction report successor boundary.**
EX-T8 does not implement operator correction report generation. It must preserve
the extraction authority, rebuild, storage, quality, and raw-OCR-retention
signals needed by a successor EX tranche to produce an operator-visible scan
outcome report. Any EC-T5 or domain-specific activation remains blocked until a
separate operator-facing report/confirmation path exists or the operator
explicitly authorizes a bounded exception.

---

## Authorization Summary

Authorized under:

- EX-T7 closure at `7c92b20b` (roadmap sync commit).
- Parent roadmap open question 3 (raw OCR storage tradeoff, line 517).
- Operator instruction on 2026-06-12: formalize storage boundary as
  domain-agnostic foundation before Policy_Local real-file consumption.

No EC-T4, EC-T5, EC-T6, T12, corpus ingestion, OCR model download, OCR
execution, Policy_Local workspace mutation, provider call, or public-sync
is authorized.

---

## Problem Statement (source-verified)

### Current extraction pipeline gap

Source: `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py`

`ExtractionChunk` (line 117-133): has `text`, `source_hash`, `char_start`,
`char_end`, `extraction_tier`, `quality_flags`, `language_codes` -- but does NOT
have `authority_level`, `rebuildClass`, or any field that signals which rebuild
contract applies.

`build_extraction_dscp_descriptor_inputs` (line 400-449): propagates `rawContentReleased: "false"` into DSCP metadata but does NOT propagate `authorityLevel`
or `rebuildClass`. The boundary between pipeline output and project consumption
is implicit -- callers receive a `list[ExtractionDscpDescriptorInput]` with no
wrapper that captures quality report, chunk count, or raw OCR audit flag.

`ExtractionQualityReport` (line 99-113): has `status`, `quality_flags`,
`mean_ocr_confidence`, `thresholds` -- but no `rawOcrRetained` flag.

`Tier2OcrPageResult` (line 67-74): raw OCR intermediates are returned from
`extract_tier2_ocr` but there is no policy on whether callers should or
must not persist them. The roadmap notes this as open question 3 (line 517).

### Absence of authority-level vocabulary

Grep result: `authority_level`, `EXTRACTED_TEXT`, `OPERATOR_SUPPLIED`,
`CANONICAL_SOURCE`, `UNVERIFIED_RAW_OCR`, `rebuildClass`, `TIER1_CHAR_OFFSET`,
`TIER2_PAGE_REOCR`, `ExtractionStorageBoundary`, `rawOcrRetained`,
`boundary_sha256` -- all ABSENT from EXTENSIONS source at baseHead `7c92b20b`.

These are new tokens. No collision with existing source.

---

## Scope Boundary

In scope for EX-T8:

- `authority_level: Literal['EXTRACTED_TEXT']` field added to `ExtractionChunk`.
- `rebuildClass: Literal['TIER1_CHAR_OFFSET', 'TIER2_PAGE_REOCR']` field added
  to `ExtractionChunk` (set by the chunk-building function based on `extraction_tier`).
- `rawOcrRetained: bool` field added to `ExtractionQualityReport`.
- `ExtractionStorageBoundary` dataclass added to `extraction_pipeline.py`:
  `descriptor_inputs`, `quality_report`, `chunk_count`, `rawOcrRetained`,
  `boundary_sha256`.
- `authorityLevel` key added to DSCP descriptor metadata in
  `build_extraction_dscp_descriptor_inputs`.
- `rebuildClass` key added to DSCP descriptor metadata.
- A new `build_extraction_storage_boundary` function that wraps the descriptor
  input list, quality report, and hash into the boundary record.
- Tests covering: `authority_level` on chunks, `rebuildClass` logic,
  `rawOcrRetained` propagation, `boundary_sha256` determinism.
- GC-051 registry update for EX-T8 source and test rows.

Out of scope for EX-T8:

- Any OCR execution or OCR model install.
- Any corpus JSON data file change.
- Any DSCP domain profile JSON value change.
- Any EC-02 runtime gate logic change.
- Any retrieval behavior change.
- Any write to Policy_Local workspace or external project directory.
- Any public-sync or public documentation update.
- EC-T4, EC-T5, EC-T6, T12 work.
- EX-T3 authority-level enum change to `LpciIndexRecord` -- the LPCI index
  schema already uses `RecordStatus` and `authorityLevel` is NOT added there
  in EX-T8 scope. EX-T8 governs the extraction pipeline layer only.
- Any current-law, legal correctness, or production readiness claim.
- Raw OCR file storage on disk -- D-01 explicitly resolves this as NOT
  persisted by the pipeline.

---

## Evidence

All source items verified at baseHead `7c92b20b`.

Key findings:

- `ExtractionChunk` (line 117-133): `authority_level` absent; `rebuildClass` absent.
  `extraction_tier: ExtractionTier` IS present -- encodes `TIER1_DIGITAL` vs
  `TIER2_OCR`, which is the input to the new `rebuildClass` computation.
- `ExtractionQualityReport` (line 99-113): `rawOcrRetained` absent.
- `build_extraction_dscp_descriptor_inputs` (line 400-449): `authorityLevel` and
  `rebuildClass` absent from metadata dict.
- `ExtractionStorageBoundary`: absent (new dataclass).
- `build_extraction_storage_boundary`: absent (new function).
- `rawOcrRetained`, `boundary_sha256`, `EXTRACTED_TEXT`, `OPERATOR_SUPPLIED`,
  `TIER1_CHAR_OFFSET`, `TIER2_PAGE_REOCR`: all absent from EXTENSIONS/ source.
- `extraction_pipeline.py` current line count: 450L.
  EX-T8 additions are estimated ~60-80L. Worker must verify before staging that
  the file does not exceed the GC-023 hard limit for Python source files
  (`docs/reference/CVF_GOVERNED_FILE_SIZE_GUARD.md`). If the limit would be
  exceeded, worker must split the boundary module into a new
  `extraction_storage_boundary.py` file.
- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_extraction_pipeline.py`:
  current line count checked before adding tests. If adding would exceed limit,
  worker must add a new `test_extraction_storage_boundary.py` file.

---

## Source Verification Table

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| `ExtractionChunk` dataclass exists | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 117 | `ExtractionChunk` | `ExtractionChunk` dataclass | ACCEPT |
| Extraction tier is available for rebuild-class derivation | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 126 | `extraction_tier` | `ExtractionChunk` dataclass | ACCEPT |
| Character offsets exist on chunks | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | lines 130-131 | `char_start`, `char_end` | `ExtractionChunk` dataclass | ACCEPT |
| Quality report dataclass exists | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 99 | `ExtractionQualityReport` | `ExtractionQualityReport` dataclass | ACCEPT |
| Descriptor-input builder exists | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 400 | `build_extraction_dscp_descriptor_inputs` | `build_extraction_dscp_descriptor_inputs` function | ACCEPT |
| Existing descriptor metadata releases no raw content | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 425 | `rawContentReleased` | descriptor metadata dict | ACCEPT |
| Descriptor input dataclass exists | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 136 | `ExtractionDscpDescriptorInput` | `ExtractionDscpDescriptorInput` dataclass | ACCEPT |
| Tier 2 OCR page result exists but has no storage policy | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | lines 67-74 | `Tier2OcrPageResult` | `Tier2OcrPageResult` dataclass | ACCEPT |
| Extraction tier literal exists | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 23 | `ExtractionTier` | `ExtractionTier` type alias | ACCEPT |
| Parent roadmap authorizes raw OCR storage decision | `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md` | line 517 | open question 3 | parent roadmap | ACCEPT |
| EX-T7 predecessor is closed | `docs/reviews/CVF_LPCI2_EX_T7_SENTENCE_BOUNDARY_CHUNKING_COMPLETION_2026-06-12.md` | `CLOSED_PASS_BOUNDED` | EX-T7 closure | closure review | ACCEPT |

---

## Negative Search And Collision Discipline

Coverage: `EXTENSIONS/` Python source. Verified at baseHead `7c92b20b`.

| Token | Disposition |
| --- | --- |
| `authority_level` | ABSENT from EXTENSIONS Python source. ABSENT from TypeScript source. New field on `ExtractionChunk`. |
| `EXTRACTED_TEXT` | ABSENT from EXTENSIONS source. No collision. |
| `OPERATOR_SUPPLIED` | ABSENT from EXTENSIONS source. No collision. |
| `rebuildClass` | ABSENT from EXTENSIONS source. New field. |
| `TIER1_CHAR_OFFSET` | ABSENT from EXTENSIONS source. New Literal value. |
| `TIER2_PAGE_REOCR` | ABSENT from EXTENSIONS source. New Literal value. |
| `ExtractionStorageBoundary` | ABSENT from EXTENSIONS source. New dataclass. |
| `rawOcrRetained` | ABSENT from EXTENSIONS source. New field. |
| `boundary_sha256` | ABSENT from EXTENSIONS source. New field. |
| `authorityLevel` (metadata key) | Absent from `extraction_pipeline.py` metadata dict. Present in TypeScript `LpciIndexRecord` as a separate field on a different schema -- no runtime collision; Python pipeline uses string metadata dicts, not TypeScript interfaces. |

---

## Forbidden Scope

The following must not appear in EX-T8 artifacts:

- Any OCR execution, OCR model installation, or `import easyocr / tesseract`.
- Any file write to `Policy_Local` workspace or external project directory.
- Any DSCP domain profile JSON value change.
- Any corpus JSON data file change.
- Any EC-02 runtime gate change.
- Any retrieval layer change.
- Any public-sync commit.
- Any `IN_FORCE` assignment to any corpus record.
- Any current-law or legal correctness claim.
- Raw OCR output written to disk by the pipeline (D-01 resolves this as
  caller responsibility outside the pipeline boundary).
- Operator-facing correction report generation. That is successor EX scope, not
  EX-T8 implementation scope.

---

## Acceptance Criteria For EX-T8 Closure

1. `authority_level: Literal['EXTRACTED_TEXT']` present on `ExtractionChunk`.
2. `rebuildClass: Literal['TIER1_CHAR_OFFSET', 'TIER2_PAGE_REOCR']` present
   on `ExtractionChunk`; set from `extraction_tier` in the chunk-building
   function.
3. `rawOcrRetained: bool` present on `ExtractionQualityReport`.
4. `ExtractionStorageBoundary` dataclass present with fields:
   `descriptor_inputs`, `quality_report`, `chunk_count`, `rawOcrRetained`,
   `boundary_sha256`.
5. `build_extraction_storage_boundary` function wraps descriptor inputs,
   quality report, and computes `boundary_sha256`.
6. `authorityLevel: "EXTRACTED_TEXT"` and `rebuildClass` present in DSCP
   descriptor metadata dict produced by `build_extraction_dscp_descriptor_inputs`.
7. All existing tests pass (no regressions).
8. New tests cover: `authority_level` on chunks, `rebuildClass` from tier,
   `rawOcrRetained` propagation, `boundary_sha256` determinism.
9. GC-051 registry updated with EX-T8 source and test rows.
10. GC-023 file size limit respected: if `extraction_pipeline.py` would exceed
    its limit, split into a new `extraction_storage_boundary.py`.
11. Pre-closure autorun gate passes.
12. Reviewer-fast passes.
13. `python -m pytest EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests -q` PASS.
14. Closure explicitly records that operator correction report generation is
    successor EX scope and no EC-T5/domain activation is authorized by EX-T8.

---

## Claim Boundary

This GC-018 authorizes Python dataclass/type additions and a storage boundary
contract only. It does not prove OCR quality, retrieval correctness, legal
correctness, production readiness, or any guarantee beyond the schema/contract
additions themselves.

EC-02 hard boundary 2026-07-01 remains in force.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
