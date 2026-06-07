# CVF Work Order: LPCI2-T9 PolicyLocal Search Runtime

Memory class: FULL_RECORD

docType: work_order

Status: DISPATCH_READY

Date: 2026-06-07

Worker: Claude

Dispatch base head: `29aa3ffc`

Execution base head: `29aa3ffc`

Closure base head: `29aa3ffc`

dispatchBaseHead: 29aa3ffc
executionBaseHead: 29aa3ffc
closureBaseHead: 29aa3ffc

Commit mode: WORKER_MAY_COMMIT

Risk class: R1_LOCAL_SCRIPT_AND_TEST_ONLY

Authority: Implements LPCI2-T9 scope from
`docs/roadmaps/CVF_LPCI2_T9_POLICYLOCAL_SEARCH_RUNTIME_ROADMAP_2026-06-07.md`.

---

## Purpose

Generate article-boundary chunks from existing t8 corpus records, build a
local deterministic keyword/filter search index, apply the T7 boundary
contract, emit query receipts for every query path, and produce deterministic
acceptance tests for accepted, zero-result, and escalation paths.

No provider calls. No chat runtime. No vector retrieval. No legal advice claim.
No public-sync. No production readiness claim.

---

## Authority Chain

| Authority item | Path |
|---|---|
| Session front door | `CVF_SESSION_MEMORY.md` |
| Machine state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` |
| Active handoff | `AGENT_HANDOFF_V16_2026-06-06.md` |
| T9 roadmap | `docs/roadmaps/CVF_LPCI2_T9_POLICYLOCAL_SEARCH_RUNTIME_ROADMAP_2026-06-07.md` |
| T8 completion | `docs/reviews/CVF_LPCI2_T8_SEARCH_LAYER_SCAFFOLDING_COMPLETION_2026-06-04.md` |
| Chunk schema | `docs/reference/CVF_LPCI_RETRIEVAL_TRACE_DESIGN_2026-06-04.md` |
| Receipt model | `docs/reference/CVF_LPCI_QUERY_RECEIPT_MODEL_2026-06-04.md` |
| Boundary contract | `docs/reference/CVF_LPCI_RESPONSE_BOUNDARY_ENFORCEMENT_CONTRACT_2026-06-04.md` |
| Corpus records | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-corpus-records.json` |
| Work-order template | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` |

---

## Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Orchestrator | Claude (self-dispatch) | Scope owner |
| Worker | Claude | Implement chunks, index, receipts, tests; commit |
| Reviewer / closer | Codex or operator | Verify correctness if escalated |

---

## Worker Autonomy / No-Question Rule

Claude must proceed autonomously inside Allowed Scope. In-scope test failures,
hash drift checks, file-path checks, and gate commands are worker-owned. Claude
must stop only when an action would exceed Allowed Scope, touch forbidden paths,
consume secrets or quota, or if corpus drift check fails (escalate to operator).

---

## Required First Reads

Before any edits, read:

1. `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-corpus-records.json` (full — 2 records, schema t8.v1)
2. `docs/reference/CVF_LPCI_RETRIEVAL_TRACE_DESIGN_2026-06-04.md` (chunk schema §1, index design §2)
3. `docs/reference/CVF_LPCI_QUERY_RECEIPT_MODEL_2026-06-04.md` (required fields, enforcement rules)
4. `docs/reference/CVF_LPCI_RESPONSE_BOUNDARY_ENFORCEMENT_CONTRACT_2026-06-04.md` (EC-01 through EC-04)
5. `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\scripts\policylocal-docx-deep-scan.py` (existing extraction approach)

---

## Pre-Flight Checks

Before edits, capture and record:

```powershell
git rev-parse --short HEAD
git status --short
python -c "import json,hashlib; data=open('D:/UNG DUNG AI/TOOL AI 2026/CVF-Workspace/Policy_Local/data/generated/policylocal-corpus-records.json','rb').read(); print('corpus-hash:', hashlib.sha256(data).hexdigest()[:16])"
```

Confirm:
- HEAD matches `dispatchBaseHead` `29aa3ffc`
- No dirty paths in corpus records or scripts directories
- Two corpus records present; `schemaVersion=policylocal.corpusRecords.t8.v1`

If corpus records hash has drifted from T8 evidence, escalate to operator
before continuing.

---

## Write Ownership

| Path | Ownership |
|---|---|
| `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\scripts\policylocal-chunk-generator.py` | Worker creates |
| `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\scripts\policylocal-search-runtime.py` | Worker creates |
| `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-chunks.json` | Worker generates |
| `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-query-receipts-acceptance.json` | Worker generates |
| `docs/reviews/CVF_LPCI2_T9_SEARCH_RUNTIME_COMPLETION_2026-06-07.md` | Worker creates closure packet |
| `AGENT_HANDOFF_V16_2026-06-06.md` | Worker updates HEAD record in session-sync step |
| All other files | FORBIDDEN |

---

## Allowed / Forbidden Scope

**Allowed:**
- Create `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\scripts\policylocal-chunk-generator.py`
- Create `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\scripts\policylocal-search-runtime.py`
- Generate `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-chunks.json`
- Generate `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-query-receipts-acceptance.json`
- Create `docs/reviews/CVF_LPCI2_T9_SEARCH_RUNTIME_COMPLETION_2026-06-07.md`
- Update `AGENT_HANDOFF_V16_2026-06-06.md` HEAD record in session-sync step
- Update `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` and `.md` if T9 changes the PolicyLocal corpus status

**Forbidden:**
- Provider calls of any kind
- Chat runtime or LLM answer generation
- Vector or embedding retrieval
- Legal advice quality claim or current-law claim
- Changes to `EXTENSIONS/`, `.github/`, package files, lockfiles
- Public-sync or public-facing artifact changes
- Corpus expansion beyond the current two DOCX source files
- Changes to governance checker scripts or CVF core docs
- Production or hosted deployment configuration

---

## Guard Claim-Language Discipline

Use `local deterministic search mechanics` or `query receipt emission proof`.
Do not claim `legal answer quality`, `current law status`, `production ready`,
`hosted ready`, `public ready`, or `chat runtime behavior`.

Allowed claim wording:

> T9 proves that chunk generation, keyword/filter retrieval, boundary
> enforcement (EC-01 through EC-04), and query receipt emission work
> deterministically for the two-document PolicyLocal pilot corpus.

Forbidden claim wording:

> T9 proves the system gives accurate legal answers or is ready for
> production or public deployment.

---

## Execution Plan

| Step | Required action |
|---|---|
| 1 | Pre-flight: read corpus records, verify schema and hash, check for drift |
| 2 | Create `policylocal-chunk-generator.py` — article-boundary split, emit `policylocal-chunks.json` with schema `policylocal.chunk.t8.v1` |
| 3 | Verify chunk output: count chunks, spot-check chunkHash, verify all 14 required fields present |
| 4 | Create `policylocal-search-runtime.py` — filter-first/keyword-rank lookup, boundary contract EC-01 through EC-04, receipt emission |
| 5 | Run acceptance queries: positive (law number lookup), zero-result (out-of-corpus law), escalation (legal advice), freshness-disclosed (not_yet_in_force) |
| 6 | Write receipts to `policylocal-query-receipts-acceptance.json` |
| 7 | Verify receipts: escalation path must have `selectedCandidateIds=[]`; freshness path must have `freshnessDisclosureApplied=true` |
| 8 | Commit implementation scripts and generated files |
| 9 | Create completion review `CVF_LPCI2_T9_SEARCH_RUNTIME_COMPLETION_2026-06-07.md` |
| 10 | Session sync: update handoff HEAD |

---

## Chunk Generator Specification

Input: `policylocal-corpus-records.json` — each record's `sourcePath` points to a DOCX.
Approach: the DOCX text is available in the corpus records via the existing
deep-scan scripts; if full text is not stored in corpus records, use
`policylocal-docx-deep-scan.py` approach to re-extract text for chunking.

Chunk schema `policylocal.chunk.t8.v1` — all 14 fields are required:

| Field | Source |
|---|---|
| `chunkId` | `<familyId>/<normalizedFilename>/<chunkIndex>` (zero-padded 4 digits) |
| `sourcePath` | parent record `normalizedPath` |
| `sourceHash` | parent record `sourceHash` |
| `parentRecordHash` | parent record `textHash` |
| `chunkIndex` | zero-based sequence within document |
| `startChar` | character offset |
| `endChar` | character offset exclusive |
| `chunkText` | article text, 100–2000 chars (hard limit 4000) |
| `chunkHash` | `sha256:<hex>` of `chunkText` |
| `topicTags` | inherited from parent record |
| `knowledgeRegion` | inherited from parent record |
| `answerClass` | inherited from parent record |
| `articleRef` | article number string (e.g. `Dieu 44`) or null |
| `freshnessStatus` | inherited from parent record |

Chunking strategy: split on `Dieu <N>.` article boundaries. Sub-split at
paragraph breaks if article >2000 chars. Skip chunks <100 chars.

---

## Search Runtime Specification

The runtime function signature (Python):

```python
def search(query_text: str, corpus_records: list, chunks: list,
           filters: dict = None) -> dict:
    """
    Returns a query receipt dict matching policylocal.queryReceipt.t8.v1.
    No provider calls. No LLM. No vector search.
    """
```

Lookup sequence (from retrieval trace design lines 108-116):
1. Hard filters: `jurisdiction=VN_NATIONAL`, exclude `answerClass=ESCALATE_OR_ABSTAIN` chunks
2. Soft filters: `topicTags` match if query terms overlap, `freshnessStatus` acceptable
3. Keyword match `chunkText` against `normalizedQuery` (substring or token overlap)
4. Rank: exact `articleRef` > `topicTags` overlap > keyword frequency
5. Take top-5 candidates (configurable)
6. Apply boundary contract EC-01 through EC-04
7. Emit receipt with all 21 required fields

Boundary contract EC rules (from response boundary enforcement contract):
- EC-01: legal advice query → `ESCALATE_OR_ABSTAIN`, `selectedCandidateIds=[]`
- EC-02: current applicability before effective date → `ESCALATE_OR_ABSTAIN`
- EC-03: legal interpretation / compliance determination → `ESCALATE_OR_ABSTAIN`
- EC-04: out-of-jurisdiction query → `ESCALATE_OR_ABSTAIN`
- `DIRECT_CITED_ANSWER` is blocked for the pilot corpus
- `freshnessStatus=not_yet_in_force` → `freshnessDisclosureApplied=true`

---

## Acceptance Query Set

Worker must produce deterministic receipts for all five paths:

| Query ID | Query text | Expected answerClass | Key assertions |
|---|---|---|---|
| AQ-01 | `Luat so 116/2025/QH15 quy dinh ve gi` | `SUMMARY_WITH_SOURCE` | `selectedCandidateIds` non-empty; `freshnessDisclosureApplied=true`; `citations` non-empty |
| AQ-02 | `Luat so 999/2025/QH15` | `ESCALATE_OR_ABSTAIN` | `selectedCandidateIds=[]`; `candidateCountAfter=0`; zero-result |
| AQ-03 | `Tai lieu mat` | `ESCALATE_OR_ABSTAIN` | out-of-corpus; `selectedCandidateIds=[]` |
| AQ-04 | `Tu van phap ly ve viec ap dung luat` | `ESCALATE_OR_ABSTAIN` | EC-01 legal advice escalation; `escalateConditionTriggered=EC-01`; `selectedCandidateIds=[]` |
| AQ-05 | `Luat 148/2025/QH15 co hieu luc chua` | `ESCALATE_OR_ABSTAIN` | EC-02 current-applicability before effective date; `freshnessStatus=not_yet_in_force`; `selectedCandidateIds=[]` |

---

## Evidence Requirements

After implementation, record in the completion review:

```powershell
git rev-parse --short HEAD
python D:/UNG\ DUNG\ AI/TOOL\ AI\ 2026/CVF-Workspace/Policy_Local/scripts/policylocal-chunk-generator.py
python D:/UNG\ DUNG\ AI/TOOL\ AI\ 2026/CVF-Workspace/Policy_Local/scripts/policylocal-search-runtime.py --acceptance
```

Record:
- Chunk count per document
- Chunk hash sample (first 3 chunks)
- Receipt count for acceptance run
- All 5 acceptance queries: answerClass, selectedCandidateIds length, escalateConditionTriggered
- Hash of generated `policylocal-chunks.json`

---

## Review Gate

Close only if:
- `policylocal-chunks.json` exists with schema `policylocal.chunk.t8.v1`
- All 14 chunk fields present in every chunk row
- `policylocal-query-receipts-acceptance.json` exists with 5 receipts
- AQ-01 produces `SUMMARY_WITH_SOURCE` with `freshnessDisclosureApplied=true`
- AQ-02 through AQ-05 produce `ESCALATE_OR_ABSTAIN` with `selectedCandidateIds=[]`
- No provider calls, no LLM output in any receipt
- Pre-commit hook chain passes

---

## Closure Checklist

| Item | Required close state |
|---|---|
| Corpus drift check | PASS — no hash drift before chunking |
| Chunk file generated | PRESENT — `policylocal-chunks.json`, schema `policylocal.chunk.t8.v1` |
| All 14 chunk fields | VERIFIED |
| Chunk generator script | PRESENT — `policylocal-chunk-generator.py` |
| Search runtime script | PRESENT — `policylocal-search-runtime.py` |
| Acceptance receipts | PRESENT — `policylocal-query-receipts-acceptance.json`, 5 receipts |
| AQ-01 SUMMARY_WITH_SOURCE | VERIFIED |
| AQ-02 through AQ-05 ESCALATE | VERIFIED |
| Freshness disclosure (AQ-01, AQ-05) | VERIFIED — `freshnessDisclosureApplied=true` |
| No provider calls | VERIFIED |
| Pre-commit hook chain | PASS |

---

## Return-To-Orchestrator Conditions

Return if:
- Corpus records hash has drifted from T8 evidence — escalate to operator
- DOCX source text is not recoverable from existing scripts and corpus records
- A needed action would touch forbidden paths
- Receipt schema cannot be satisfied without provider calls

---

## Operator Checkpoint

`operator.checkpoint.waiver` — R1 local-script-and-test-only work; no live
provider proof, no public-sync, no secrets use, no production deployment.
Worker may proceed without separate operator approval.

---

## Source Verification Table

| Token / Symbol | Source file | Verified line |
|---|---|---|
| `policylocal.corpusRecords.t8.v1` schemaVersion | `data/generated/policylocal-corpus-records.json` | top-level key |
| Two corpus records present | `data/generated/policylocal-corpus-records.json` | records array length=2 |
| `sourceHash` field format `sha256:<hex>` | `data/generated/policylocal-corpus-records.json` | record[0].sourceHash |
| `topicTags` array present in records | `data/generated/policylocal-corpus-records.json` | record[0].topicTags |
| `freshnessStatus=not_yet_in_force` for both records | `data/generated/policylocal-corpus-records.json` | record[0,1].freshnessStatus |
| `policylocal.chunk.t8.v1` schema version | `docs/reference/CVF_LPCI_RETRIEVAL_TRACE_DESIGN_2026-06-04.md` | line 72 |
| 14 chunk fields: `chunkId`, `sourcePath`, `sourceHash`, `parentRecordHash`, `chunkIndex`, `startChar`, `endChar`, `chunkText`, `chunkHash`, `topicTags`, `knowledgeRegion`, `answerClass`, `articleRef`, `freshnessStatus` | `docs/reference/CVF_LPCI_RETRIEVAL_TRACE_DESIGN_2026-06-04.md` | lines 56-72 |
| Article-boundary chunking on `Dieu <N>.` | `docs/reference/CVF_LPCI_RETRIEVAL_TRACE_DESIGN_2026-06-04.md` | lines 76-84 |
| Filter-first keyword-rank lookup sequence (7 steps) | `docs/reference/CVF_LPCI_RETRIEVAL_TRACE_DESIGN_2026-06-04.md` | lines 108-118 |
| No vector store in T9 | `docs/reference/CVF_LPCI_RETRIEVAL_TRACE_DESIGN_2026-06-04.md` | lines 122-124 |
| `policylocal.queryReceipt.t8.v1` schema version | `docs/reference/CVF_LPCI_QUERY_RECEIPT_MODEL_2026-06-04.md` | line 57 |
| 21 required receipt fields | `docs/reference/CVF_LPCI_QUERY_RECEIPT_MODEL_2026-06-04.md` | lines 50-71 |
| `selectedCandidateIds=[]` for ESCALATE_OR_ABSTAIN | `docs/reference/CVF_LPCI_QUERY_RECEIPT_MODEL_2026-06-04.md` | lines 97, 105-106 |
| `freshnessDisclosureApplied=true` for not_yet_in_force | `docs/reference/CVF_LPCI_QUERY_RECEIPT_MODEL_2026-06-04.md` | lines 98-99 |
| EC-01 through EC-04 boundary rules | `docs/reference/CVF_LPCI_RESPONSE_BOUNDARY_ENFORCEMENT_CONTRACT_2026-06-04.md` | EC section |
| `DIRECT_CITED_ANSWER` blocked for pilot corpus | `docs/reference/CVF_LPCI_RESPONSE_BOUNDARY_ENFORCEMENT_CONTRACT_2026-06-04.md` | line 21 |
| T8 final readiness verdict `READY` | `docs/reviews/CVF_LPCI2_T8_SEARCH_LAYER_SCAFFOLDING_COMPLETION_2026-06-04.md` | lines 163, 253 |
| T8 next control action: generate chunks, build index, emit receipts, run tests | `docs/reviews/CVF_LPCI2_T8_SEARCH_LAYER_SCAFFOLDING_COMPLETION_2026-06-04.md` | line 277 |
| `policylocal-chunks.json` not yet generated (T8 design-only) | `docs/reviews/CVF_LPCI2_T8_SEARCH_LAYER_SCAFFOLDING_COMPLETION_2026-06-04.md` | lines 205, 227 |
| Existing scripts path | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\scripts\` | directory listing |

---

## Acceptance Criteria

- `policylocal-chunks.json` present with schema `policylocal.chunk.t8.v1`
- Every chunk row has all 14 required fields; no field is null/missing
- `policylocal-query-receipts-acceptance.json` present with exactly 5 receipts
- AQ-01 receipt: `answerClass=SUMMARY_WITH_SOURCE`, `freshnessDisclosureApplied=true`, `selectedCandidateIds` non-empty
- AQ-02, AQ-03 receipts: `answerClass=ESCALATE_OR_ABSTAIN`, `selectedCandidateIds=[]`
- AQ-04 receipt: `answerClass=ESCALATE_OR_ABSTAIN`, `escalateConditionTriggered=EC-01`, `selectedCandidateIds=[]`
- AQ-05 receipt: `answerClass=ESCALATE_OR_ABSTAIN`, `escalateConditionTriggered=EC-02`, `selectedCandidateIds=[]`
- No provider call, LLM call, or vector store call in any receipt or script
- Pre-commit hook chain passes
- Completion review filed with deterministic evidence

---

## Claim Boundary

This work order claims only:

> T9 proves that article-boundary chunk generation, keyword/filter retrieval,
> boundary enforcement (EC-01 through EC-04), freshness disclosure, and query
> receipt emission work deterministically for the two-document PolicyLocal
> pilot corpus (`policylocal.corpusRecords.t8.v1`).

Does not claim:
- Legal answer quality or accuracy
- Current-law status as of any date
- Compliance or interpretation guidance
- Production, hosted, or public readiness
- Chat runtime or conversational AI behavior
- Vector or semantic retrieval
- Corpus coverage beyond the current two DOCX files

---

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_WO_LPCI2_T9_POLICYLOCAL_SEARCH_RUNTIME_2026-06-07.md` | Status `CLOSED`, claim-language discipline recorded | PENDING |
| Completion or reviewer artifact | `docs/reviews/CVF_LPCI2_T9_SEARCH_RUNTIME_COMPLETION_2026-06-07.md` | Final disposition, receipts evidence, claim boundary | PENDING |
| Generated chunk file | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-chunks.json` | schema `policylocal.chunk.t8.v1`, all 14 fields | PENDING |
| Acceptance receipt file | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-query-receipts-acceptance.json` | 5 receipts, AQ-01 through AQ-05 | PENDING |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | GC-051 state update if corpus status changes | PENDING |
| Session continuity | `AGENT_HANDOFF_V16_2026-06-06.md` | Active handoff HEAD record updated | PENDING |

---

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order obligation | Roadmap section | Status |
|---|---|---|---|
| Use T8 READY scaffold | cite T8 completion and registry; verify corpus records schema | §Authority Chain | SATISFIED |
| Generate chunks before index | produce `policylocal-chunks.json` with schema `policylocal.chunk.t8.v1` | §Tranche Plan T9B | REQUIRED |
| Preserve source trace | all 14 chunk fields including sourceHash, parentRecordHash, chunkHash, articleRef | §Source Verification | REQUIRED |
| Use filter-first keyword retrieval | lookup sequence: hard filter → soft filter → keyword → rank → boundary → receipt | §Tranche Plan T9C | REQUIRED |
| Emit query receipts | every acceptance query produces `policylocal.queryReceipt.t8.v1` receipt | §Tranche Plan T9D | REQUIRED |
| Enforce escalate boundary | AQ-02 through AQ-05 must have `selectedCandidateIds=[]` | §Acceptance Query Set | REQUIRED |
| Preserve freshness disclosure | AQ-01 and AQ-05 must have `freshnessDisclosureApplied=true` | §Acceptance Query Set | REQUIRED |
| Exclude vector retrieval | no embeddings, no vector store, no external model | §Forbidden | REQUIRED |
| Produce runtime negative evidence | AQ-02, AQ-03 zero-result receipts | §Acceptance Query Set | REQUIRED |

---

## Pending Artifact Evidence Finality

All machine closure package items are `PENDING` at dispatch. Finalized by worker
at implementation commit. Completion review records final evidence.
No gate evidence is pre-finalized.

---

## Mandatory Gate-Failure Remediation Protocol

If any gate fails during implementation:

1. Record the failing gate, command, and output in the completion review
2. Do not suppress or skip failing gates
3. If failure is in-scope, fix and re-run the gate before closure
4. If fixing would exceed Allowed Scope, escalate to operator before continuing

---

## Self-Reported Gate Evidence Consistency

Gate evidence in this work order is pre-dispatch only. Final gate evidence
belongs in the completion review. Self-reported pre-dispatch gate results
are advisory only; only completion review evidence is authoritative.

---

## Near-Threshold Plan

Governed file size guard: `docs/work_orders/` markdown files have an
`active_markdown` class. This work order is approximately 250 lines — well
within the advisory threshold. No size remediation needed.

---

## Fulfillment Manifest

| Artifact | Governed path | Status |
|---|---|---|
| Work order | `docs/work_orders/CVF_WO_LPCI2_T9_POLICYLOCAL_SEARCH_RUNTIME_2026-06-07.md` | THIS_FILE |
| Completion review | `docs/reviews/CVF_LPCI2_T9_SEARCH_RUNTIME_COMPLETION_2026-06-07.md` | PENDING |
| Chunk generator | `CVF-Workspace/Policy_Local/scripts/policylocal-chunk-generator.py` | PENDING |
| Search runtime | `CVF-Workspace/Policy_Local/scripts/policylocal-search-runtime.py` | PENDING |
| Chunk output | `CVF-Workspace/Policy_Local/data/generated/policylocal-chunks.json` | PENDING |
| Receipt output | `CVF-Workspace/Policy_Local/data/generated/policylocal-query-receipts-acceptance.json` | PENDING |

---

## Current Runtime Freshness Verification

| Symbol / path | Verified in current source | Line or evidence |
|---|---|---|
| `policylocal-corpus-records.json` | YES | directory listing + hash pre-flight above |
| `schemaVersion: policylocal.corpusRecords.t8.v1` | YES | corpus records top-level key |
| `policylocal.chunk.t8.v1` chunk schema | YES | retrieval trace design line 72 |
| `policylocal.queryReceipt.t8.v1` receipt schema | YES | query receipt model line 57 |
| EC-01 through EC-04 boundary rules | YES | response boundary contract EC section |
| `policylocal-chunks.json` does NOT yet exist | VERIFIED_ABSENT | Policy_Local generated dir listing |

---

## ACCEPT_AS_OWNER_MAP coverage

This work order does not touch `EXTENSIONS/` or the CVF ownership map.
File writes are limited to the `Policy_Local` workspace (`CVF-Workspace/`)
and `docs/` subdirs. No owner-map disposition changes are needed — scope
is confined to local workspace scripts, generated data files, and a closure
review under `docs/reviews/`.

---

## check_work_order_dispatch_quality.py

`governance/compat/check_work_order_dispatch_quality.py` is the dispatch
quality machine guard for this work order. Run before dispatch:

```powershell
python governance/compat/check_work_order_dispatch_quality.py --base 29aa3ffc --head HEAD --enforce
```

Expected result: 0 violations, COMPLIANT.
