# CVF Agent Work Order: LPCI2 EX-T7 Sentence Boundary Chunking

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-12

Worker: Codex

Reviewer: Codex

Commit mode: WORKER_MAY_COMMIT

executionBaseHead: `39079125`

closureBaseHead: `39079125`

completionReviewPath:

`docs/reviews/CVF_LPCI2_EX_T7_SENTENCE_BOUNDARY_CHUNKING_COMPLETION_2026-06-12.md`

---

## Purpose

Implement and close EX-T7 from the LPCI2 extraction roadmap as a bounded
sentence-boundary chunking upgrade for the local extraction foundation.

## Authority Chain

- Operator instruction: 2026-06-12, continue under the prior single-agent
  multi-role rule and complete related roadmap work.
- Active state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Active handoff: `AGENT_HANDOFF_V17_2026-06-07.md`.
- Parent roadmap:
  `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md`.
- GC-018:
  `docs/baselines/CVF_GC018_LPCI2_EX_T7_SENTENCE_BOUNDARY_CHUNKING_2026-06-12.md`.

## Agent Roles

| Role | Agent | Responsibility |
| --- | --- | --- |
| Operator | Human | Authorizes continuation and single-agent multi-role closure |
| Orchestrator | Codex | Bound EX-T7 and keep EC/T12 blocked claims out of scope |
| Worker | Codex | Implement deterministic strategy and focused tests |
| Reviewer | Codex | Run tests/gates, close packet, and update continuity |

## Intake Role Routing Decision

| Field | Decision |
| --- | --- |
| Intake summary | Operator asked Codex to continue the remaining related roadmap work after EX-T3 through EX-T6 closed. |
| Scope classification | Bounded local extraction foundation upgrade. |
| Risk sensitivity | R2 because chunking can be overclaimed as retrieval quality if boundaries are loose. |
| Selected canonical route mode | SINGLE_AGENT_MULTI_ROLE. |
| Role separation basis | Scope is local deterministic source/tests/docs only; no provider, external mutation, OCR model download, public-sync, corpus ingestion, or EC activation. |
| Escalation condition | Stop or close blocked if work requires OCR dependency install, external Policy_Local mutation, EC-02 runtime disclosure, public-sync, provider proof, or T12 activation. |

## Single-Agent Multi-Role Control Block

roleMode: `SINGLE_AGENT_MULTI_ROLE`

allowedBecause: bounded source/test/docs closure with machine gates, no external
workspace mutation, no live/provider proof, and no production/public claim.

roleSeparationMechanism:

- source verification table;
- focused pytest evidence;
- GC-051 registry coverage;
- reviewer-fast and autorun workflow gates;
- explicit claim boundary.

forbiddenSelfApprovalClaims:

- no semantic retrieval quality claim;
- no OCR quality or OCR dependency readiness claim;
- no corpus ingestion or external Policy_Local mutation claim;
- no governed retrieval behavior claim;
- no current-law/legal-quality claim;
- no production/public readiness claim.

## Scope / Target / Owner Boundary

Allowed scope:

- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py`;
- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_extraction_pipeline.py`;
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`;
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md`;
- `docs/baselines/CVF_GC018_LPCI2_EX_T7_SENTENCE_BOUNDARY_CHUNKING_2026-06-12.md`;
- `docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI2_EX_T7_SENTENCE_BOUNDARY_CHUNKING_FOR_CODEX_2026-06-12.md`;
- `docs/reviews/CVF_LPCI2_EX_T7_SENTENCE_BOUNDARY_CHUNKING_COMPLETION_2026-06-12.md`;
- `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md`;
- `CVF_SESSION_MEMORY.md`;
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`;
- `AGENT_HANDOFF_V17_2026-06-07.md`.

Forbidden scope:

- no package/lockfile edit;
- no OCR dependency install or model download;
- no external Policy_Local edit;
- no corpus ingestion or generated corpus mutation;
- no provider/API-key use;
- no public-sync;
- no EC-02 runtime disclosure or `QUERY_CLASS_GATED` activation.

## Required First Reads

| File | Purpose |
| --- | --- |
| `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md` | confirm EX-T7 sentence-boundary upgrade path |
| `docs/reviews/CVF_LPCI2_EX_T3_T6_EXTRACTION_PIPELINE_COMPLETION_2026-06-11.md` | confirm predecessor closure and boundary |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | confirm current chunk owner |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_extraction_pipeline.py` | confirm focused test owner |

## Source Verification

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

## Current Runtime Freshness Verification

Runtime freshness command:

`rg -n "ChunkingStrategy|def chunk_extracted_pages|class ExtractionChunk|build_extraction_dscp_descriptor_inputs|sentence-boundary-chars" EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py`

Observed result:

- current extraction pipeline owns `ExtractionChunk`;
- current extraction pipeline owns `chunk_extracted_pages`;
- EX-T7 adds the `sentence-boundary-chars` literal as an optional strategy;
- descriptor metadata remains owned by `build_extraction_dscp_descriptor_inputs`.

Freshness disposition: `SOURCE_VERIFIED_LOCAL_DETERMINISTIC`.

## External Artifact Hash Manifest

| Artifact | sha256 | Role |
| --- | --- | --- |
| `docs/reviews/CVF_LPCI2_EX_T3_T6_EXTRACTION_PIPELINE_COMPLETION_2026-06-11.md` | `N/A with reason - predecessor closure is repo-local committed evidence; this batch does not recompute external artifacts` | predecessor closure |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI2_EX_T3_T6_EXTRACTION_PIPELINE_FOR_CODEX_2026-06-11.md` | `N/A with reason - predecessor work order is repo-local committed evidence; this batch does not recompute external artifacts` | predecessor work order |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order handling | Disposition |
| --- | --- | --- |
| EX-T7 sentence-boundary upgrade after base pipeline is stable | Add optional `sentence-boundary-chars` strategy while preserving fixed-window default | PASS_BOUNDED |
| Keep chunking language-agnostic | Use punctuation/newline boundaries only; do not infer natural language or locale | PASS_BOUNDED |
| Preserve raw-content and retrieval boundary | Descriptor metadata keeps `rawContentReleased=false`; no receipt or query runtime claim | PASS |

## Pre-Flight Checks

| Check | Command or evidence | Required result |
| --- | --- | --- |
| Base HEAD captured | `git rev-parse --short HEAD` | `39079125` |
| Worktree scope | `git status --short` | no unrelated tracked edits before implementation |
| Source freshness | `rg` command in Current Runtime Freshness Verification | expected symbols present |
| Focused pytest | `python -m pytest EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests -q` | PASS |

## Write Ownership

Codex owns only the allowed paths listed above. Any expansion into dependency
installation, model download, external workspace mutation, public-sync,
provider/live proof, EC activation, or Policy_Local mutation requires a
separate governed packet.

## Execution Plan

1. Add optional sentence-boundary chunking helpers and strategy selection.
2. Preserve `fixed-window-chars` as the default.
3. Add `charStart` and `charEnd` trace metadata on chunks and descriptors.
4. Add focused deterministic tests.
5. Update GC-051 registry, roadmap, completion review, and session continuity.
6. Run pytest, py_compile, reviewer-fast, autorun, and pre-commit gates.

## Evidence Requirements

| Evidence | Required result |
| --- | --- |
| Focused pytest | all extraction foundation tests pass |
| Python compile | `py_compile` passes for Tier 1 and pipeline modules |
| Registry coverage | GC-051 JSON/Markdown entries cover EX-T7 source and test surfaces |
| Claim boundary | no OCR dependency/model, corpus ingestion, provider, public, legal-quality, or production claim |

## Acceptance Criteria

| Criterion | Required outcome | Status |
| --- | --- | --- |
| Default behavior preserved | `chunk_extracted_pages` still defaults to `fixed-window-chars` | PASS |
| Optional sentence-boundary strategy added | `sentence-boundary-chars` groups sentence-like spans within `max_chars` | PASS |
| Long-span guard | spans longer than `max_chars` fall back to deterministic fixed windows | PASS |
| Trace metadata | `charStart` and `charEnd` appear in chunk provenance and descriptor metadata | PASS |
| Boundary preserved | no provider call, corpus ingestion, OCR model download, retrieval receipt, or query response behavior | PASS |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
| --- | --- | --- |
| Retrieval receipt acceptance claim | N/A with reason: EX-T7 builds extraction chunks/descriptors only; governed retrieval receipt remains downstream owner scope | PASS |
| Query acceptance claim | N/A with reason: no query runtime or response acceptance path was executed | PASS |
| Raw content release boundary | `rawContentReleased=false` remains in descriptor input records | PASS |

## Claim Boundary

EX-T7 closes deterministic local sentence-boundary chunking only. It does not
claim semantic retrieval quality, OCR model availability, OCR quality, corpus
ingestion, Policy_Local runtime update, governed retrieval behavior, legal
answer quality, current-law status, T12 readiness, production readiness,
public readiness, or release readiness.

## Review Gate

Reject closure if package files change, OCR dependencies are installed, external
Policy_Local paths are modified, generated corpus files are written, retrieval
receipt behavior is claimed, or tests and governance gates fail.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_LPCI2_EX_T7_SENTENCE_BOUNDARY_CHUNKING_COMPLETION_2026-06-12.md` | final closure review | PASS |
| Roadmap state | `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md` | EX-T7 closed; EC side still blocked | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | entry `ex-t7-sentence-boundary-chunking-source` | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | quick lookup rows for EX-T7 source/tests | PASS |
| External evidence digest | predecessor EX-T3 through EX-T6 closure | repo-local committed evidence, no external recompute | N/A with reason |
| System loop interlock | no system-loop mutation | local extraction foundation only | N/A with reason: no runtime loop changed |
| Session continuity | `CVF_SESSION_MEMORY.md`, `CVF_SESSION/ACTIVE_SESSION_STATE.json`, `AGENT_HANDOFF_V17_2026-06-07.md` | reviewer-owned final sync | PASS |

## Closure Checklist

- [x] Source verification complete.
- [x] Evidence reuse plan complete.
- [x] Focused tests pass.
- [x] GC-051 coverage updated.
- [x] Roadmap rows updated.
- [x] Claim boundary preserved.

## Return-To-Orchestrator Conditions

Return blocked if any requested continuation requires OCR dependency
installation, model download, external corpus mutation, public-sync,
provider/live proof, EC-02 runtime retrieval disclosure, or T12 activation.

## Operator Checkpoint

No extra operator decision is required for this local deterministic foundation
batch. Operator approval is still required for dependency installation, OCR
model download, external Policy_Local mutation, public-sync, provider/API-key
proof, EC successor activation, or T12 authoring.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance work order; no public-sync authorized.
