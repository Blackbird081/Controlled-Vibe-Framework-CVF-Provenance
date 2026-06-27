# CVF GC-018 LPCI2 EX-T7 Sentence Boundary Chunking

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: baseline

Date: 2026-06-12

executionBaseHead: `39079125`

---

## Purpose

Authorize Codex single-agent multi-role completion of the LPCI2 EX-T7
sentence-boundary chunking upgrade after EX-T3 through EX-T6 closed the base
local extraction pipeline.

This batch adds a deterministic optional chunking strategy for extracted text.
It preserves the existing fixed-window default and does not change OCR,
corpus ingestion, DSCP profile activation, EC-02 retrieval semantics, or
Policy_Local runtime behavior.

## Authorization

Operator instruction on 2026-06-12: continue under the prior rule that Codex
may close multiple roles and complete related roadmap work.

Active state:

`CVF_SESSION/ACTIVE_SESSION_STATE.json`

Active handoff:

`AGENT_HANDOFF_V17_2026-06-07.md`

## Decision

Open and close EX-T7 as a bounded extraction-foundation upgrade:

- add `sentence-boundary-chars` as an optional `ChunkingStrategy`;
- keep `fixed-window-chars` as the default strategy;
- add page-local `charStart` and `charEnd` trace metadata;
- add focused tests for sentence grouping, long-sentence fallback, and
  deterministic chunk IDs.

## Scope / Target / Owner Boundary

In scope:

- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py`;
- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_extraction_pipeline.py`;
- GC-051 JSON/Markdown registry coverage for EX-T7;
- parent roadmap row/status update;
- EX-T7 work order, completion review, and session continuity.

Out of scope:

- no OCR dependency installation;
- no OCR model, Poppler, LibreOffice, or ImageMagick download;
- no package/lockfile update;
- no external Policy_Local mutation;
- no corpus ingestion or generated corpus mutation;
- no provider/API-key use;
- no public-sync;
- no EC-02 runtime disclosure, `QUERY_CLASS_GATED` activation, T12 unlock,
  current-law/legal-quality claim, production readiness, public readiness,
  memory reinjection, high-risk promotion, or autonomous mutation.

## Source Verification Summary

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| EXISTS: EX-T7 upgrade path | `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md` | Open Questions for Codex Rebuttal, Chunking strategy | `EX-T7` | parent roadmap | ACCEPT |
| EXISTS: current chunk owner | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 348 | `chunk_extracted_pages` | EX extraction pipeline module | ACCEPT |
| VALUE_SET: existing default chunk max | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 20 | `DEFAULT_CHUNK_MAX_CHARS` | EX extraction pipeline module | ACCEPT |
| EXISTS: chunk schema owner | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 113 | `ExtractionChunk` | EX extraction pipeline module | ACCEPT |
| EXISTS: DSCP descriptor handoff owner | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 409 | `build_extraction_dscp_descriptor_inputs` | EX extraction pipeline module | ACCEPT |
| DOC_ONLY_NEW: EX-T7 strategy literal | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 24 | `sentence-boundary-chars` | `ChunkingStrategy` | ACCEPT |

## Evidence Reuse And Encoding Plan

verificationMode: `REUSE_PRIOR_VERIFICATION`

priorVerificationArtifact:

- `docs/reviews/CVF_LPCI2_EX_T3_T6_EXTRACTION_PIPELINE_COMPLETION_2026-06-11.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI2_EX_T3_T6_EXTRACTION_PIPELINE_FOR_CODEX_2026-06-11.md`

priorVerificationAnchor: EX-T3 through EX-T6 closed the local extraction
pipeline owner, tests, and GC-051 coverage.

freshRecomputeRequired: `NO`

recomputeReason: `N/A with reason - no external source binaries are opened.`

unicodePathHandling: `N/A with reason - no external Unicode paths are opened.`

extractedTextAuthority: `N/A with reason`

## Claim Boundary

This baseline authorizes deterministic local chunking behavior only. It does
not prove OCR model quality, retrieval quality, Policy_Local integration,
legal answer quality, current-law status, T12 readiness, production readiness,
public readiness, or release readiness.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance baseline; no public-sync authorized.
