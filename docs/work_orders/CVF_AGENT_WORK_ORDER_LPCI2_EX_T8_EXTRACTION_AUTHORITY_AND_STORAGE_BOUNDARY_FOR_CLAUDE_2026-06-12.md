# CVF Agent Work Order: LPCI2 EX-T8 Extraction Authority And Storage Boundary

docType: work_order

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

dispatchBaseHead: `7c92b20b`

executionBaseHead: `fcf0f545`

closureBaseHead: `fcf0f545`

Commit mode: `CODEX_MULTI_ROLE_REVIEW_AND_COMMIT_AFTER_GATES`

completionReviewPath: `docs/reviews/CVF_LPCI2_EX_T8_EXTRACTION_AUTHORITY_AND_STORAGE_BOUNDARY_COMPLETION_2026-06-12.md`

reviewerOwnedClosurePaths:
- `docs/reviews/CVF_LPCI2_EX_T8_EXTRACTION_AUTHORITY_AND_STORAGE_BOUNDARY_COMPLETION_2026-06-12.md`
- `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md`
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V17_2026-06-07.md`

Date: 2026-06-12

Assigned to: Codex (operator-directed multi-role execution)

---

## Purpose

Deliver four storage/authority boundary decisions as Python dataclass additions
and a machine-readable boundary contract in the CVF extraction foundation.
The pipeline gains: a chunk `authority_level` field, a `rebuildClass` contract,
a `rawOcrRetained` audit flag, and a `ExtractionStorageBoundary` output wrapper.
No OCR execution, corpus ingestion, or external workspace write occurs.

EX-T8 also records a successor dependency: operator-visible scan outcome /
correction report generation is required before EC-T5 or any domain-specific
gate relies on scan-layer metadata gaps, but that report generator is not
implemented in EX-T8.

Operator redirected execution on 2026-06-12: Codex completes the EX tranche in
multi-role mode, then commits only after reviewer-fast, pre-closure, and
pre-commit governance gates pass.

---

## Authority Chain

- GC-018: `docs/baselines/CVF_GC018_LPCI2_EX_T8_EXTRACTION_AUTHORITY_AND_STORAGE_BOUNDARY_2026-06-12.md`
  Status: DISPATCHED
- EX-T7 closure: `docs/reviews/CVF_LPCI2_EX_T7_SENTENCE_BOUNDARY_CHUNKING_COMPLETION_2026-06-12.md`
  Status: CLOSED_PASS_BOUNDED commit `7c92b20b`
- Parent roadmap open question 3 (raw OCR storage):
  `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md`
  line 517

---

## Agent Roles

| Role | Agent | Constraint |
| --- | --- | --- |
| Worker | Codex | Operator-authorized multi-role implementation of EX-T8 only |
| Reviewer | Codex | Reviews artifacts; runs pre-closure gate; commits if PASS |
| Closer | Codex | Updates GC-018, work order, roadmap, GC-051 to CLOSED_PASS_BOUNDED |

---

## Pre-Flight Checks

Before starting, worker must confirm:

1. GC-018 `Status` has been set to `DISPATCHED` by Codex.
2. `dispatchBaseHead` matches or is an ancestor of current `git rev-parse HEAD`.
3. Write-owned files exist at expected paths.
4. `python -m py_compile EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py`
   exits 0 before any edits (baseline compile check).

If any pre-flight check fails, worker must stop and notify Codex.

---

## Required First Reads

1. `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py`
   -- full file: understand `ExtractionChunk`, `ExtractionQualityReport`,
   `ExtractionDscpDescriptorInput`, `build_extraction_dscp_descriptor_inputs`,
   `extract_tier2_ocr`, and the chunk-building functions.
2. `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/tier1_extractor.py`
   -- understand `Tier1ExtractorResult` shape passed into the pipeline.
3. `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_extraction_pipeline.py`
   -- understand existing test patterns; check current line count before adding.
4. `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`
   -- understand current registry structure; find the EX-T7 entries to use
   as the pattern for new EX-T8 entries.
5. `governance/toolkit/05_OPERATION/CVF_GOVERNED_FILE_SIZE_GUARD.md`
   -- check the hard line-count limit for Python source files and test files.

---

## Scope

Allowed scope for worker:

- Add `ExtractionAuthorityLevel` and `RebuildClass` type aliases to
  `extraction_pipeline.py`.
- Add `authority_level` and `rebuild_class` fields to `ExtractionChunk`.
- Add `raw_ocr_retained: bool` field to `ExtractionQualityReport`.
- Add `ExtractionStorageBoundary` dataclass.
- Add `build_extraction_storage_boundary` function.
- Add `authorityLevel` and `rebuildClass` keys to DSCP descriptor metadata.
- Add unit tests for the above.
- Split into `extraction_storage_boundary.py` if GC-023 limit would be exceeded.

Forbidden scope for worker:

- OCR execution, OCR model installation, or `import easyocr / tesseract`.
- File write to `Policy_Local` workspace or external project directory.
- DSCP domain profile JSON value change.
- Corpus JSON data file change.
- EC-02 runtime gate change.
- Retrieval layer change.
- Public-sync commit.
- `IN_FORCE` assignment to any corpus record.
- Current-law or legal correctness claim.
- Raw OCR output written to disk by the pipeline.
- Operator-facing correction report generation or EC-T5/domain activation.

---

## Write Ownership

Worker owns writes to:

- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py`
  OR a new `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_storage_boundary.py`
  if the line count of `extraction_pipeline.py` would exceed its GC-023 limit.
- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_extraction_pipeline.py`
  OR a new `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_extraction_storage_boundary.py`
  if the test file would exceed its GC-023 limit.

All other files are read-only. GC-051 registry is Codex reviewer scope.
No corpus JSON data files. No DSCP profile JSON files. No EC-02 files.
No public-sync. No Policy_Local workspace write.

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

---

## Execution Plan

### Step 1: Add `RebuildClass` and `ExtractionAuthorityLevel` type aliases

Near the top of `extraction_pipeline.py`, after the existing `Literal` type
aliases (around line 23), add:

```python
ExtractionAuthorityLevel = Literal['EXTRACTED_TEXT']
RebuildClass = Literal['TIER1_CHAR_OFFSET', 'TIER2_PAGE_REOCR']
```

### Step 2: Add new fields to `ExtractionChunk`

In `ExtractionChunk` (after `extraction_tier` field, around line 126), add:

```python
authority_level: ExtractionAuthorityLevel = 'EXTRACTED_TEXT'
rebuild_class: RebuildClass = 'TIER1_CHAR_OFFSET'
```

The `rebuild_class` default is `TIER1_CHAR_OFFSET`. Tier 2 OCR chunks must be
explicitly set to `TIER2_PAGE_REOCR` by the chunk-building function based on
`extraction_tier`. Worker must find the function(s) that construct `ExtractionChunk`
objects and set `rebuild_class='TIER2_PAGE_REOCR'` when `extraction_tier='TIER2_OCR'`.

### Step 3: Add `rawOcrRetained` to `ExtractionQualityReport`

In `ExtractionQualityReport` (after `thresholds` field), add:

```python
raw_ocr_retained: bool = False
```

Default is `False` -- the pipeline does not persist raw OCR intermediates.
Callers who capture `Tier2OcrPageResult` objects outside the pipeline and need
to record that fact pass `raw_ocr_retained=True` when building the quality report.

Worker must check the existing function that constructs `ExtractionQualityReport`
and confirm that `raw_ocr_retained=False` is the correct default for all current
call sites.

### Step 4: Add `ExtractionStorageBoundary` dataclass

After `ExtractionDscpDescriptorInput`, add:

```python
@dataclass(frozen=True)
class ExtractionStorageBoundary:
    """Canonical output surface of the CVF extraction pipeline.
    Projects consume this boundary record, not internal chunk lists."""

    descriptor_inputs: list[ExtractionDscpDescriptorInput]
    quality_report: ExtractionQualityReport
    chunk_count: int
    raw_ocr_retained: bool
    boundary_sha256: str
```

### Step 5: Add `build_extraction_storage_boundary` function

```python
def build_extraction_storage_boundary(
    descriptor_inputs: list[ExtractionDscpDescriptorInput],
    quality_report: ExtractionQualityReport,
) -> ExtractionStorageBoundary:
    """Wrap descriptor inputs and quality report into the canonical pipeline output.

    boundary_sha256 is computed over artifact_id and source_hash of every
    descriptor input, in order, so the boundary is tamper-evident without
    storing raw chunk text.
    """
    digest_input = "".join(
        f"{d.artifact_id}:{d.source_hash}" for d in descriptor_inputs
    )
    boundary_hash = sha256(digest_input.encode()).hexdigest()
    return ExtractionStorageBoundary(
        descriptor_inputs=descriptor_inputs,
        quality_report=quality_report,
        chunk_count=len(descriptor_inputs),
        raw_ocr_retained=quality_report.raw_ocr_retained,
        boundary_sha256=boundary_hash,
    )
```

### Step 6: Update `build_extraction_dscp_descriptor_inputs`

In the metadata dict built for each descriptor, add after `rawContentReleased`:

```python
"authorityLevel": chunk.authority_level,
"rebuildClass": chunk.rebuild_class,
```

### Step 7: Check GC-023 line count

After all edits, run `wc -l extraction_pipeline.py`. If it exceeds the GC-023
hard limit for Python source files, move `ExtractionStorageBoundary` and
`build_extraction_storage_boundary` to a new
`EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_storage_boundary.py` file
and add the corresponding import to `extraction_pipeline.py`.

### Step 8: Run existing tests for regressions

```
python -m pytest EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests -q
```

All existing tests must pass before adding new ones.

### Step 9: Add unit tests

Add tests (in `test_extraction_pipeline.py` or a new `test_extraction_storage_boundary.py`) covering:

- `ExtractionChunk` built from Tier 1 extraction has `authority_level='EXTRACTED_TEXT'`
  and `rebuild_class='TIER1_CHAR_OFFSET'`.
- `ExtractionChunk` built from Tier 2 OCR has `rebuild_class='TIER2_PAGE_REOCR'`.
- `ExtractionQualityReport` has `raw_ocr_retained=False` by default.
- `build_extraction_storage_boundary` produces a stable `boundary_sha256` for
  the same set of descriptor inputs (determinism test: call twice, compare hashes).
- `ExtractionStorageBoundary.chunk_count` equals `len(descriptor_inputs)`.
- `authorityLevel: "EXTRACTED_TEXT"` is present in the DSCP descriptor metadata
  produced by `build_extraction_dscp_descriptor_inputs`.
- `rebuildClass: "TIER1_CHAR_OFFSET"` and `"TIER2_PAGE_REOCR"` are present in
  DSCP descriptor metadata for the corresponding tiers.

### Step 10: Stage all changed files

`git add` the changed source and test files. Do NOT commit.

---

## Negative Search And Collision Discipline

Verified at baseHead `7c92b20b`:

| Token | Disposition |
| --- | --- |
| `authority_level` | ABSENT from EXTENSIONS Python source. New field. |
| `EXTRACTED_TEXT` | ABSENT from EXTENSIONS source. New Literal value. |
| `rebuildClass` / `rebuild_class` | ABSENT from EXTENSIONS source. New field and metadata key. |
| `TIER1_CHAR_OFFSET` | ABSENT from EXTENSIONS source. New Literal value. |
| `TIER2_PAGE_REOCR` | ABSENT from EXTENSIONS source. New Literal value. |
| `ExtractionStorageBoundary` | ABSENT from EXTENSIONS source. New dataclass. |
| `rawOcrRetained` / `raw_ocr_retained` | ABSENT from EXTENSIONS source. New field. |
| `boundary_sha256` | ABSENT from EXTENSIONS source. New field. |
| `authorityLevel` (metadata key string) | Absent from `extraction_pipeline.py` metadata dict. The TypeScript `LpciIndexRecord` has an `authorityLevel?: string` field -- different schema, different file, no runtime collision since Python uses string metadata dicts. |

Machine-gate failures inside this work order's scope must be resolved before
returning the packet to Codex. If a pre-existing test failure is found that is
outside this work order's scope, worker must surface it as a finding and stop.

---

## Evidence Requirements

Worker packet must include:

1. Diff summary: which lines changed in each file.
2. `python -m pytest EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests -q` output
   (PASS or documented pre-existing FAIL with scope assessment).
3. `python -m py_compile` result for all modified Python files.
4. Line count of `extraction_pipeline.py` after edits (confirm within GC-023 limit
   or confirm split was performed).
5. Confirmation that `Tier2OcrPageResult` and raw OCR intermediate objects are NOT
   written to disk by any pipeline function.
6. Confirmation that no corpus JSON data or DSCP profile JSON files were changed.
7. Confirmation that no operator correction report, EC-T5 gate, domain-specific
   metadata decision, retrieval behavior, or external workspace change was made.

---

## Acceptance Criteria

1. `ExtractionAuthorityLevel` and `RebuildClass` type aliases present.
2. `authority_level: ExtractionAuthorityLevel` and `rebuild_class: RebuildClass`
   on `ExtractionChunk`, set correctly for Tier 1 vs Tier 2.
3. `raw_ocr_retained: bool = False` on `ExtractionQualityReport`.
4. `ExtractionStorageBoundary` dataclass present.
5. `build_extraction_storage_boundary` function present and produces stable hash.
6. `authorityLevel` and `rebuildClass` keys in DSCP descriptor metadata.
7. All existing tests pass. New tests pass.
8. GC-023 limits respected.
9. Reviewer-fast PASS.
10. Pre-closure autorun gate PASS.
11. Closure records that operator-visible scan outcome / correction report
    generation remains successor EX scope and that EC-T5 remains blocked by its
    own authorization path.

---

## Review Gate

Codex reviewer must:

1. Confirm all acceptance criteria met.
2. Run pre-closure autorun gate.
3. Run reviewer-fast.
4. Confirm no out-of-scope changes (corpus data, DSCP profiles, EC files,
   Policy_Local workspace, public-sync).
5. Update GC-051 registry with EX-T8 source and test rows.
6. Update GC-018 Status to CLOSED_PASS_BOUNDED.
7. Update roadmap EX-T8 row to CLOSED_PASS_BOUNDED.
8. Record successor EX dependency for operator-visible scan outcome reporting
   without activating EC-T5.
9. Commit with a message referencing EX-T8 closure.

---

## Closure Checklist

- [x] `ExtractionAuthorityLevel` and `RebuildClass` type aliases added
- [x] `authority_level` and `rebuild_class` on `ExtractionChunk`
- [x] `rebuild_class` set correctly for Tier 2 OCR chunks in chunk-building code
- [x] `raw_ocr_retained: bool = False` on `ExtractionQualityReport`
- [x] `ExtractionStorageBoundary` dataclass added
- [x] `build_extraction_storage_boundary` function added
- [x] `authorityLevel` and `rebuildClass` in DSCP descriptor metadata
- [x] All existing tests pass
- [x] New tests added and passing
- [x] GC-023 limits respected
- [x] Reviewer-fast PASS
- [x] Pre-closure autorun gate PASS
- [x] GC-018 Status CLOSED_PASS_BOUNDED
- [x] Roadmap EX-T8 row CLOSED_PASS_BOUNDED
- [x] GC-051 registry updated
- [x] Successor EX operator-scan-outcome dependency recorded without EC-T5 activation

---

## Return-To-Orchestrator Conditions

Worker returns uncommitted packet to Codex when:

- All source edits are complete and staged.
- `python -m pytest EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests -q` is run
  (PASS or pre-existing FAIL documented).
- `python -m py_compile` passes for all modified files.
- Evidence requirements above are satisfied.

Worker must NOT return early with partial edits. Worker must NOT commit.

---

## Operator Checkpoint

No operator checkpoint required before execution. However:

- If adding all fields would push `extraction_pipeline.py` past the GC-023
  hard limit, worker must split into `extraction_storage_boundary.py` without
  asking -- the split strategy is pre-authorized by this work order.
- If a pre-existing test failure of unknown scope is found, worker must surface
  it and stop rather than attempting out-of-scope fixes.

---

## Claim Boundary

This work order authorizes Python dataclass/type additions and a storage boundary
contract only. Completion of EX-T8 does not claim OCR quality, retrieval
correctness, legal correctness, production readiness, EC-02 enforcement, or any
guarantee beyond the schema/contract additions.

EC-02 hard boundary 2026-07-01 remains in force after EX-T8 closes.

---

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | this file | Status field set to CLOSED_PASS_BOUNDED | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_LPCI2_EX_T8_EXTRACTION_AUTHORITY_AND_STORAGE_BOUNDARY_COMPLETION_2026-06-12.md` | File existence + PASS disposition | PASS |
| Roadmap state | `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md` | EX-T8 row updated to CLOSED_PASS_BOUNDED | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | EX-T8 source and test entries present | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | EX-T8 quick lookup rows present | PASS |
| External evidence digest | N/A with reason -- EX-T8 is Python type/schema additions only; no external corpus, provider, or non-git artifact consumed | No external path artifact in scope | N/A with reason |
| System loop interlock | GC-052: no looping worker pattern; Claude executes once and returns | Single-pass execution, no loop | N/A with reason |
| Session continuity | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | nextAllowedMove updated during Codex closure; handoff reflects closure HEAD | PASS |

---

## Roadmap-To-Work-Order Trace Matrix

| Roadmap row / open question | This WO section |
| --- | --- |
| Open Q3: raw OCR storage tradeoff | D-01 decision + `raw_ocr_retained` field + Step 3 |
| EX-T8: extraction authority and storage boundary | D-01 through D-04 decisions, Steps 1-10 |
| D-02: chunk authority level | Steps 1-2 + `authority_level` field |
| D-03: hash/offset rebuild contract | Step 2 `rebuild_class` + Step 9 test |
| D-04: storage boundary contract | Steps 4-5 `ExtractionStorageBoundary` |
| D-05: operator-visible scan outcome dependency | Evidence item 7 + acceptance item 11 |

---

## Intake Role Routing Decision

| Field | Decision |
| --- | --- |
| Intake summary | Operator instructed Codex to finish the EX foundation before returning to EC; EX-T8 formalizes extraction authority, rebuild, raw-OCR retention, and storage-boundary contracts using the closed EX-T7 evidence at commit `7c92b20b`. |
| Scope classification | Bounded Python contract/schema tranche with focused tests; no corpus ingestion, retrieval behavior, external workspace mutation, public-sync, or provider/live proof. |
| Risk sensitivity | R2 because extraction authority and storage-boundary wording could be misread as retrieval, current-law, or Policy_Local activation if overclaimed. |
| Selected canonical route mode | SINGLE_AGENT_MULTI_ROLE. |
| Role separation basis | Operator explicitly redirected Codex to complete all EX work before EC; role separation is enforced through source verification, focused tests, reviewer-fast, pre-closure, pre-commit gates, completion review, and machine closure package. |
| Escalation condition | Stop and return to Codex if implementation requires EC files, corpus JSON, DSCP profile values, external Policy_Local writes, OCR dependency/model installation, provider/API-key use, or operator correction report generation. |

## Single-Agent Multi-Role Control Block

roleMode: `SINGLE_AGENT_MULTI_ROLE`

allowedBecause: operator explicitly instructed Codex to finish the bounded EX
tranche before EC; scope is local deterministic Python source/test plus
governance closure only.

roleSeparationMechanism:

- Source Verification Table and negative-search discipline;
- focused pytest and py_compile evidence;
- GC-051 registry coverage;
- reviewer-fast, pre-closure, and pre-commit gates;
- completion review with claim boundary.

forbiddenSelfApprovalClaims:

- no OCR quality claim;
- no corpus ingestion claim;
- no operator correction report generation claim;
- no EC-T5/domain activation claim;
- no retrieval behavior claim;
- no current-law/legal-quality claim;
- no production/public readiness claim.

## Evidence Reuse And Encoding Plan

verificationMode: `REUSE_PRIOR_VERIFICATION`

priorVerificationArtifact: docs/reviews/CVF_LPCI2_EX_T7_SENTENCE_BOUNDARY_CHUNKING_COMPLETION_2026-06-12.md; docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md

priorVerificationAnchor: EX-T7 closure commit 7c92b20b and parent roadmap open question 3 authorize the bounded EX-T8 storage-boundary decision; source field existence is verified directly against EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py.

freshRecomputeRequired: `NO`

recomputeReason: `N/A with reason - EX-T8 does not consume external PDFs,
source bundles, extracted text folders, or T11B hash/size evidence.`

unicodePathHandling: `N/A with reason - EX-T8 does not open Unicode external workspace paths; any future Unicode path handling must use literal paths and UTF-8-safe readers.`

extractedTextAuthority: `N/A with reason`

---

## Reviewer Closure Conversion Block

Codex closure conversion completed:

1. GC-018 status set to `CLOSED_PASS_BOUNDED`.
2. This work order status set to `CLOSED_PASS_BOUNDED`.
3. EX-T8 row added to roadmap Part A tranche table.
4. EX-T8 source and test rows added to GC-051 registry JSON and Markdown.
5. Completion review authored at `completionReviewPath`.
6. EX-T8 closure committed as a bounded private provenance batch.

---

## Worker Autonomy / No-Question Rule

Worker proceeds without asking questions if:

- All new fields are optional with defaults (Python dataclass `field` or
  direct default value).
- The GC-023 split strategy (new file `extraction_storage_boundary.py`) is
  needed -- it is pre-authorized.
- The company-docs fixture or profile test fix is not needed (no TypeScript
  files are touched).

Worker STOPS and returns to Codex if:

- A pre-existing test failure of unknown scope is encountered.
- Any step requires changing DSCP profile JSON, corpus data, or EC-02 files.
- Line count would exceed GC-023 AND the split strategy itself would exceed
  limits for a new file.
