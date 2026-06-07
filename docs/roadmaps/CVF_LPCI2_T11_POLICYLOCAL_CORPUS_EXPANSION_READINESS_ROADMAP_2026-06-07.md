# CVF LPCI2-T11 PolicyLocal Corpus Expansion Readiness Roadmap

Memory class: SUMMARY_RECORD

Status: PROPOSED

docType: roadmap

Date: 2026-06-07

baseHead: `93bf9909`

---

## Purpose

Open the next PolicyLocal Corpus Intelligence roadmap after LPCI2-T10 reached
`CLOSED_PASS_BOUNDED` at `866f92cd`, confirming that the two-document pilot
corpus and its generated T9 search artifacts are hash-bound, schema-verified,
and claim-boundary safe.

This roadmap scopes the inventory and source-verification work required before
the PolicyLocal runtime can be expanded beyond the current two-document pilot.
It does not authorize new corpus ingestion, runtime changes, or provider use.
Those are gated behind the T11 readiness verdict.

**EC-02 hard boundary:** No current-law claim or production runtime claim is
permitted before or until the EC-02 freshness review on or after 2026-07-01.
This applies to every tranche in this roadmap.

## Authorization / Decision

Operator authorization on 2026-06-07: proceed from T10 foundation readiness to
T11 corpus expansion readiness, and account for newly added real-case
PolicyLocal input files that are relevant to the policy/legal workflow but are
not pure statute text.

Decision: T11 may inventory and source-verify mixed candidate material,
including laws, notices, administrative decisions, project lists, review
reports, petitions, and other applied-policy case records. Mixed candidate
material must be classified conservatively and must not be promoted into
runtime corpus ingestion until T11-D returns an allowed readiness verdict.

---

## Scope / Applies To

Applies to:

- the existing two-record pilot corpus at
  `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-corpus-records.json`;
- candidate documents proposed for addition to the PolicyLocal corpus;
- mixed candidate material under `Policy_Local\data_input\`, including
  law-like documents and applied-policy case records;
- governing repo artifacts under `docs/reference/`, `docs/reviews/`,
  `docs/work_orders/`, `docs/baselines/`, and `docs/corpus-intelligence/`;
- `CVF-Workspace\Policy_Local\data\generated\` for generated candidate
  manifests and classification evidence.

---

## Why This Roadmap Is Needed

LPCI2-T9 built a deterministic local search runtime for the pilot corpus.
LPCI2-T10 confirmed the search artifacts pass hash, schema, receipt, and
boundary checks.

Before expanding beyond the two-document pilot — adding more laws, decrees,
circulars, notices, decisions, case records, project lists, petitions, review
reports, or other applied-policy domain documents — CVF requires:

1. a candidate inventory with source metadata (title, issuer, date, status,
   jurisdiction, document type);
2. a source-verification table confirming each candidate is accessible and
   readable;
3. a classification pre-check confirming each candidate can meet the T2 domain
   classification matrix and T5 deep-scan boundary;
4. an EC-02 boundary gate confirming the corpus-expansion plan does not add
   content that makes a current-law or production readiness claim before
   2026-07-01;
5. a readiness verdict (`READY` / `NOT_READY` / `READY_WITH_CONDITIONS`)
   gating the T12 corpus-ingestion work order.

---

## Tranche Plan

## Work Plan

1. T11-A inventories named candidate files and produces a machine-readable
   manifest without reading document body text beyond filesystem metadata.
2. T11-B source-verifies accessibility and hashes each candidate source file.
3. T11-C classifies accessible candidates against the T2 vocabulary and EC-02
   boundary before any ingestion is authorized.
4. T11-D aggregates evidence into a readiness verdict and either gates T12 or
   parks corpus expansion with explicit blockers.

## Acceptance Criteria

T11 can close only when all T11-A/B/C/D sub-tranches are closed with bounded
evidence, candidate totals reconcile across markdown and manifest artifacts,
the EC-02 boundary is preserved, and the final T11-D verdict is one of
`READY`, `READY_WITH_CONDITIONS`, or `NOT_READY`.

## Verification / Evidence

Required evidence includes filesystem-backed candidate enumeration, source
hashes for accessible files, manifest/inventory reconciliation, T2 answerClass
vocabulary validation, EC-02 gate accounting, changed-file evidence, and
autorun gate output for each sub-tranche.

## Claim Boundary

T11 may claim only corpus-expansion readiness planning over named candidate
files. T11 does not claim extraction correctness, corpus ingestion, chunking,
search runtime behavior, provider behavior, legal advice quality, current-law
status, hosted readiness, production readiness, public readiness, or release
readiness.

## Non-Goals

T11 does not ingest candidate documents, parse full text, generate chunks,
modify search runtime, call providers, run live governance proof, update
public-sync, or decide that mixed case records are legally authoritative.

### T11-A: Candidate Inventory

**Goal:** enumerate candidate documents for corpus expansion.

**Deliverables:**

- `docs/reference/CVF_LPCI2_T11_CANDIDATE_INVENTORY_2026-06-07.md` — a
  tabular inventory of each candidate: title, issuer, law number, date
  enacted, effective date, jurisdiction, document type, current status
  (`in_force` / `not_yet_in_force` / `amended` / `superseded` / `unknown`),
  and proposed answerClass from the T2 domain matrix;
  candidateFamily (`legal_source` / `administrative_notice` /
  `administrative_decision` / `project_case_record` /
  `applied_policy_record` / `unknown`);
- `CVF-Workspace\Policy_Local\data\generated\policylocal-t11-candidate-manifest.json`
  — machine-readable companion: schemaVersion
  `policylocal.candidateManifest.t11.v1`, one record per candidate with the
  same fields plus a `readableAt` path or URL (private, not public-sync).

**Scope boundary:**

- inventory only; no extraction, no corpus ingestion, no runtime change;
- candidates may be proposed by operator instruction or derived from existing
  DOCX/PDF files already present in the workspace;
- mixed case/practice files must be inventoried as candidates only and must
  not be treated as binding law without T11-C classification evidence;
- EC-02 applies: candidates with `not_yet_in_force` effective dates must be
  flagged with `ec02Applies=true` and will not be moved to `in_force` status
  before the EC-02 review date.

**Acceptance criteria:**

1. inventory file is present and passes markdown structural check;
2. manifest JSON is valid, schemaVersion matches, and record count is
   consistent with the inventory;
3. every candidate has a non-empty `currentStatus` and a proposed
   `answerClass`;
4. all `not_yet_in_force` candidates carry `ec02Applies=true`;
5. no claim of completeness beyond named candidates.

---

### T11-B: Source Verification

**Goal:** confirm each candidate in the T11-A inventory is accessible, has a
readable source, and can be used as corpus input under existing standards.

**Deliverables:**

- `docs/reference/CVF_LPCI2_T11_SOURCE_VERIFICATION_TABLE_2026-06-07.md` —
  Source Verification Table per the work-order template standard
  (`docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`) with required
  columns: `Claimed item`, `Source file`, `Verified line/section`,
  `Verified path or symbol`, `Owning interface/function/schema`,
  `Disposition`;
- one row per candidate from T11-A;
- an access-verdict companion table with `accessVerdict` values:
  `ACCESSIBLE` / `NOT_ACCESSIBLE` / `REQUIRES_OPERATOR_INPUT`.

**Scope boundary:**

- read and hash candidate source files only (no extraction, no ingestion,
  no runtime change);
- verification must cite the actual file path or accessible URL (private;
  not public-sync);
- candidates marked `NOT_ACCESSIBLE` or `REQUIRES_OPERATOR_INPUT` are
  excluded from T12 scope unless the operator resolves them.

**Acceptance criteria:**

1. source verification table is present and passes markdown structural check;
2. every candidate from T11-A has a row with a non-empty `accessVerdict`;
3. every `ACCESSIBLE` candidate includes a SHA-256 hash in the notes column
   (or a cited manifest entry) per
   `docs/reference/CVF_CORPUS_SOURCE_HASH_STANDARD_2026-06-02.md` (NR-04);
4. no `ACCESSIBLE` candidate has an empty `verified path or symbol` cell.

---

### T11-C: Classification Pre-Check

**Goal:** confirm each accessible candidate can meet the T2 domain
classification matrix, the T5 deep-scan boundary requirements, and the EC-02
freshness gate before T12 ingestion is authorized.

**Deliverables:**

- `docs/reference/CVF_LPCI2_T11_CLASSIFICATION_PRE_CHECK_2026-06-07.md` —
  per-candidate classification pre-check rows covering: domain category
  (from T2 spec `docs/reference/CVF_LPCI1_T2_DOMAIN_CLASSIFICATION_SPEC_2026-06-03.md`),
  expected answerClass, `ec02Gate` (`BLOCKED_UNTIL_2026-07-01` /
  `PASSES_EC02` / `REQUIRES_REVIEW`), and `t12Eligible` (`YES` / `NO` /
  `CONDITIONAL`);
- updated `CVF-Workspace\Policy_Local\data\generated\policylocal-t11-candidate-manifest.json`
  with `classificationPreCheck` fields added per candidate.

**Scope boundary:**

- classification pre-check only; no extraction, no chunking, no ingestion,
  no search runtime change, no provider calls;
- `ec02Gate=BLOCKED_UNTIL_2026-07-01` candidates may not be marked
  `t12Eligible=YES` before the EC-02 review date;
- answerClass assignments follow the T2 matrix exactly; new answerClass
  values require a separate governed vocabulary extension.
- candidateFamily values are planning metadata only and do not expand the T2
  answerClass vocabulary.

**Acceptance criteria:**

1. pre-check file is present and passes markdown structural check;
2. every accessible candidate from T11-B has a row with non-empty
   `ec02Gate` and `t12Eligible`;
3. zero candidates with `ec02Gate=BLOCKED_UNTIL_2026-07-01` carry
   `t12Eligible=YES`;
4. answerClass values match the T2 matrix vocabulary only
   (`DIRECT_CITED_ANSWER`, `SUMMARY_WITH_SOURCE`, `PROCEDURAL_GUIDANCE`,
   `ESCALATE_OR_ABSTAIN`);
5. manifest JSON updated without removing prior T11-A fields.

---

### T11-D: Readiness Gate

**Goal:** aggregate T11-A/B/C findings into a single corpus-expansion
readiness verdict gating T12.

**Deliverables:**

- `docs/reviews/CVF_LPCI2_T11_CORPUS_EXPANSION_READINESS_GATE_2026-06-07.md`
  — readiness gate review with:
  - candidate summary table (count by verdict: `t12Eligible=YES` /
    `NO` / `CONDITIONAL`);
  - EC-02 gate summary (count of `BLOCKED_UNTIL_2026-07-01` candidates);
  - overall readiness verdict:
    - `READY` — at least one `t12Eligible=YES` candidate, zero
      unresolved T11-B blockers, EC-02 boundary confirmed;
    - `READY_WITH_CONDITIONS` — eligible candidates exist but some are
      `CONDITIONAL` pending operator resolution;
    - `NOT_READY` — no eligible candidates or unresolved hard blockers;
  - next allowed move statement.

**Scope boundary:**

- aggregation and verdict only; no new corpus ingestion, runtime change,
  provider calls, or public-sync;
- `READY` verdict is required before T12 work order authoring may begin;
- `READY_WITH_CONDITIONS` requires the condition list to be attached to
  the T12 work order.

**Acceptance criteria:**

1. readiness gate review is present and passes markdown structural check;
2. candidate summary counts match T11-A/B/C totals;
3. verdict is one of the three allowed values;
4. EC-02 gate summary is present and non-empty;
5. next allowed move statement is present and references T12 or a
   blocking condition explicitly.

---

## Execution Order

```
T11-A (Candidate Inventory)
  → T11-B (Source Verification, depends on T11-A)
    → T11-C (Classification Pre-Check, depends on T11-B)
      → T11-D (Readiness Gate, depends on T11-A/B/C)
```

All four sub-tranches must reach `CLOSED_PASS_BOUNDED` before T11 is
considered complete and T12 may be authorized.

---

## Forbidden Under This Roadmap

Unless a later work order explicitly authorizes it:

- corpus ingestion of any new document;
- extraction (text parsing) beyond read/hash for verification;
- chunking or indexing of new documents;
- runtime search query execution against new documents;
- provider calls of any kind;
- vector or embedding retrieval;
- legal advice quality claims;
- current-law or latest-law claims;
- production, hosted, or public readiness claims;
- EC-02 current-law transition before 2026-07-01;
- public-sync of private workspace paths or candidate hashes;
- autonomous mutation of existing T9/T10 artifacts.

## Text Encoding And Symbol Boundary

Roadmap prose and future agent-authored artifacts default to ASCII. Existing
candidate filenames may contain Vietnamese Unicode characters; those filenames
may be quoted exactly as source evidence under the exception for existing
Unicode filenames in
`docs/reference/CVF_TEXT_ENCODING_AND_SYMBOL_DISCIPLINE_STANDARD_2026-06-07.md`.

---

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI2_T11A_POLICYLOCAL_CANDIDATE_INVENTORY_FOR_CLAUDE_2026-06-07.md` | `Status: DISPATCHED_TO_WORKER`; `Commit mode: WORKER_MUST_NOT_COMMIT` | PASS for dispatch |
| Completion or reviewer artifact | N/A with reason | T11A has not returned from worker execution; no completion or reviewer packet is claimed in this dispatch batch | N/A with reason |
| Roadmap state | `docs/roadmaps/CVF_LPCI2_T11_POLICYLOCAL_CORPUS_EXPANSION_READINESS_ROADMAP_2026-06-07.md` | `Status: PROPOSED`; authorizes staged T11-A/B/C/D readiness work only | PASS for dispatch |
| Registry JSON | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | `currentMode=lpci2_t11a_candidate_inventory_dispatched`; next allowed move routes Claude to T11A | PASS for dispatch |
| Registry Markdown | `CVF_SESSION_MEMORY.md`; `AGENT_HANDOFF_V16_2026-06-06.md` | Active session front doors record T11A dispatch route and worker-must-not-commit boundary | PASS for dispatch |
| External evidence digest | N/A with reason | External candidate files are input authority for T11A; worker must produce the bounded manifest/digest before any T11A completion claim | N/A with reason |
| System loop interlock | `docs/baselines/CVF_GC018_LPCI2_T11A_POLICYLOCAL_CANDIDATE_INVENTORY_2026-06-07.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI2_T11A_POLICYLOCAL_CANDIDATE_INVENTORY_FOR_CLAUDE_2026-06-07.md` | GC-018 baseline plus work order keep implementation in inventory-only mode; T11B/T11C/T11D remain dependency-gated | PASS for dispatch |
| Session continuity | `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `AGENT_HANDOFF_V16_2026-06-06.md` | Current mode and next allowed move route Claude to T11A candidate inventory under worker-must-not-commit boundary | PASS for dispatch |

---

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Runtime receipt acceptance | No runtime, provider, query, search, ingestion, or receipt acceptance claim in T11A dispatch | T11A dispatch authorizes inventory/manifest only; worker must not run provider, runtime query, ingestion, OCR, or extraction | PASS |
| Candidate manifest receipt | Worker-generated manifest is required before T11A completion can be reviewed | No completion manifest is claimed by this roadmap dispatch batch | PASS |

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private Policy_Local corpus candidates and private workspace paths are
in scope for T11A dispatch.

This roadmap and the T11A dispatch packet concern private Policy_Local corpus
candidates and private workspace paths. No public-sync repository change,
public remote push, public catalog update, public readiness claim, or public
artifact export is authorized by this T11A dispatch batch.

Next public action: N/A with reason. Public export can be reconsidered only
after a later roadmap creates a public-safe summary that excludes private
workspace paths, candidate hashes, and non-public source materials.

---

## Relationship To Prior Tranches

| Tranche | Status | Relevance |
|---|---|---|
| LPCI2-T1 | CLOSED_PASS_BOUNDED | Build control packet — foundational |
| LPCI2-T2 | CLOSED_PASS_BOUNDED | Frontend prototype readiness |
| LPCI2-T4 | CLOSED_PASS_BOUNDED | Corpus classification evidence for existing 2 docs |
| LPCI2-T5 | CLOSED_PASS_BOUNDED | Deep scan — effective date `2026-07-01` confirmed |
| LPCI2-T6 | CLOSED_PASS_BOUNDED | Search/chat readiness gate (10 gaps) |
| LPCI2-T7 | CLOSED_PASS_BOUNDED | Corpus facet schema — 7 gaps closed |
| LPCI2-T8 | CLOSED_PASS_BOUNDED | Search layer scaffolding — `finalReadinessVerdict=READY` |
| LPCI2-T9 | CLOSED_PASS_BOUNDED_CORRECTION_CLEAN | Local search runtime |
| LPCI2-T10 | CLOSED_PASS_BOUNDED | Foundation readiness hash/schema/receipt verification |
| **LPCI2-T11** | **PROPOSED** | **Corpus expansion readiness — this roadmap** |
| LPCI2-T12 | NOT_YET_AUTHORIZED | Corpus ingestion — gated behind T11-D `READY` verdict |

---

## Governance Gates Required Before Any T11 Sub-Tranche Work Order

1. This roadmap must be committed with a material commit hash recorded as
   `baseHead` here.
2. A fresh GC-018 (`docs/baselines/CVF_GC018_LPCI2_T11_*`) must be authored
   and committed before any T11 sub-tranche work order is dispatched.
3. Each T11 sub-tranche work order must carry:
   - `WORKER_MUST_NOT_COMMIT` or `WORKER_MAY_COMMIT` commit mode with
     `dispatchBaseHead`, `executionBaseHead`, `closureBaseHead`;
   - Worker Autonomy / No-Question Rule per
     `docs/reference/CVF_WORKER_AUTONOMY_DISPATCH_PROMPT_STANDARD_2026-06-01.md`;
   - Source Verification Table per
     `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`.
4. EC-02 boundary must be stated in every T11 sub-tranche work order.

---

## Next Allowed Move After This Roadmap Is Committed

Author a fresh GC-018 and a source-verified T11-A Candidate Inventory work
order. The work order must name the candidate documents already present in
`Policy_Local\data_input\`, cite the T11-A acceptance criteria above, and carry
the EC-02 boundary statement.

Operator input required before T11-A dispatch:

- confirmation that EC-02 boundary applies to all `not_yet_in_force`
  candidates.

If the operator has no additional candidates at this time, T11 may be
scoped to a zero-candidate inventory, producing a `NOT_READY` verdict and
parking T12 until candidates are available.
