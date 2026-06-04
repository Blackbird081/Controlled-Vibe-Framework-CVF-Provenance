# CVF Work Order - LPCI2-T7 Corpus Facet Schema Authoring

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-04

dispatchBaseHead: `45b86df3`

executionBaseHead: `45b86df3`

closureBaseHead: `45b86df3`

Commit mode: WORKER_MUST_NOT_COMMIT

## Purpose

Execute LPCI2-T7 to close the seven T6 gaps assigned to this tranche:

| Gap | Description | blockingClass |
| --- | --- | --- |
| T6-GAP-01 | `topicTags` absent from corpus records schema | MUST_CLOSE_BEFORE_SEARCH |
| T6-GAP-02 | `freshnessStatus` / `freshnessCheckedAt` absent | MUST_CLOSE_BEFORE_SEARCH |
| T6-GAP-03 | `sourceFamily` / `familyId` absent | REMEDIATION_RECOMMENDED |
| T6-GAP-04 | Processing ledger is implicit only (no standalone file) | REMEDIATION_RECOMMENDED |
| T6-GAP-07 | Faceted retrieval schema document absent | MUST_CLOSE_BEFORE_SEARCH |
| T6-GAP-09 | Conflict/freshness state machine absent | MUST_CLOSE_BEFORE_SEARCH |
| T6-GAP-10 | Response boundary enforcement contract absent | MUST_CLOSE_BEFORE_SEARCH |

T7 produces three artifacts:

1. **Faceted retrieval schema document** (`CVF_LPCI_FACETED_RETRIEVAL_SCHEMA_2026-06-04.md`)
   — defines all required facet fields (common CVF + PolicyLocal domain
   extensions), freshness state machine, and conflict-resolution rule.

2. **Response boundary enforcement contract**
   (`CVF_LPCI_RESPONSE_BOUNDARY_ENFORCEMENT_CONTRACT_2026-06-04.md`)
   — machine-readable policy contract a search/API layer reads to enforce
   `answerClass`, `ESCALATE_OR_ABSTAIN` triggers, and `DIRECT_CITED_ANSWER`
   block.

3. **Updated corpus records** (`policylocal-corpus-records.json` upgraded to
   schemaVersion `policylocal.corpusRecords.t7.v1`) — adds `topicTags`,
   `freshnessStatus`, `freshnessCheckedAt`, `sourceFamily`, `familyId` fields
   for both DOCX files; no re-extraction, no new provider calls.

Success: all seven gaps closed with evidence; Gate 2 upgrades from PARTIAL to
PASS; Gate 3 upgrades from BLOCKED to PARTIAL or better; Gate 4 upgrades from
PARTIAL to PASS; the readiness verdict after T8 will be READY_WITH_CONDITIONS
or READY.

## Scope / Target / Owner Boundary

Target local workspace:
`D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local`

Target corpus records:
`D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-corpus-records.json`

Owner boundary: Codex executes orchestrator, implementer, reviewer, and closer
roles. WORKER_MUST_NOT_COMMIT.

## Authority Chain

| Authority | Path or note | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-04 session — T6 CLOSED_PASS_BOUNDED NOT_READY; T7 is authorized next remediation | ACCEPT |
| T6 completion review gap register | `docs/reviews/CVF_LPCI2_T6_SEARCH_CHAT_READINESS_GATE_COMPLETION_2026-06-04.md` §Gap Register | ACCEPT — T6-GAP-01/02/03/04/07/09/10 are T7 scope |
| Corpus Search And Filter Readiness Standard | `docs/reference/CVF_CORPUS_SEARCH_FILTER_READINESS_STANDARD_2026-06-02.md` | ACCEPT |
| GC-050 Classification standard | `docs/reference/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_STANDARD_2026-06-01.md` | ACCEPT |
| LPCI1-T2 domain classification spec | `docs/reference/CVF_LPCI1_T2_DOMAIN_CLASSIFICATION_SPEC_2026-06-03.md` | ACCEPT — answerClass matrix carries forward |
| LPCI2 roadmap | `docs/roadmaps/CVF_LPCI2_POLICYLOCAL_PRODUCTIZATION_ROADMAP_2026-06-03.md` | ACCEPT — T7 is named remediation stub |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT — mode `lpci2_t6_search_chat_readiness_gate_closed_pass_bounded` |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| T6-GAP-01 topicTags absent | `docs/reviews/CVF_LPCI2_T6_SEARCH_CHAT_READINESS_GATE_COMPLETION_2026-06-04.md` | §Gap Register row T6-GAP-01 | `topicTags` | T6 gap register | ACCEPT |
| T6-GAP-02 freshnessStatus absent | `docs/reviews/CVF_LPCI2_T6_SEARCH_CHAT_READINESS_GATE_COMPLETION_2026-06-04.md` | §Gap Register row T6-GAP-02 | `freshnessStatus` | T6 gap register | ACCEPT |
| T6-GAP-07 faceted retrieval schema absent | `docs/reviews/CVF_LPCI2_T6_SEARCH_CHAT_READINESS_GATE_COMPLETION_2026-06-04.md` | §Gap Register row T6-GAP-07 | `facetedRetrievalSchema` | T6 gap register | ACCEPT |
| T6-GAP-09 freshness state machine absent | `docs/reviews/CVF_LPCI2_T6_SEARCH_CHAT_READINESS_GATE_COMPLETION_2026-06-04.md` | §Gap Register row T6-GAP-09 | `freshnessStateMachine` | T6 gap register | ACCEPT |
| T6-GAP-10 boundary enforcement contract absent | `docs/reviews/CVF_LPCI2_T6_SEARCH_CHAT_READINESS_GATE_COMPLETION_2026-06-04.md` | §Gap Register row T6-GAP-10 | `boundaryEnforcementContract` | T6 gap register | ACCEPT |
| T5 corpus records schema path | `docs/reviews/CVF_LPCI2_T5_POLICYLOCAL_DEEP_CLASSIFICATION_COMPLETION_2026-06-04.md` | §Evidence Trace Block | `policylocal-corpus-records.json` | LPCI2-T5 completion | ACCEPT |
| answerClass canonical values | `docs/reference/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_STANDARD_2026-06-01.md` | Response-Boundary Classes | `answerClass` | GC-050 standard | ACCEPT |
| Common facet schema fields | `docs/reference/CVF_CORPUS_SEARCH_FILTER_READINESS_STANDARD_2026-06-02.md` | §Common Facet Schema table | `topicTags`, `freshnessStatus`, `sourceFamily` | CVF Search/Filter Readiness Standard | ACCEPT |

## New Doc-Only Fields

| New doc-only field | Purpose | Not sourced from runtime? | Runtime claim blocked? | Validation expectation |
| --- | --- | --- | --- | --- |
| `topicTags` | Controlled topic tags for faceted retrieval | Yes | Yes | array of strings; derived from document content classification; no provider call |
| `freshnessStatus` | Freshness state from state machine | Yes | Yes | must be one of: `current`, `not_yet_in_force`, `stale`, `superseded`, `repealed`, `obsolete`, `unknown` |
| `freshnessCheckedAt` | ISO-8601 date of freshness check | Yes | Yes | doc/schema validation only |
| `sourceFamily` | Family grouping for multi-file corpora | Yes | Yes | string; `VN_NATIONAL_ASSEMBLY_2025` for this corpus |
| `familyId` | Stable family identifier | Yes | Yes | string slug |
| `schemaVersion` | Updated to `policylocal.corpusRecords.t7.v1` | Yes | Yes | string; must match T7 schema version |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command | Status |
| --- | --- | --- | --- | --- |
| T6-GAP-01/02: topicTags + freshnessStatus added to corpus records | §Execution Plan step 3 | `policylocal-corpus-records.json` schemaVersion t7.v1 | `python governance/compat/check_corpus_intelligence_classification.py --base 45b86df3 --head HEAD --enforce` | CLOSED_PASS_BOUNDED |
| T6-GAP-07: faceted retrieval schema document | §Execution Plan step 1 | `docs/reference/CVF_LPCI_FACETED_RETRIEVAL_SCHEMA_2026-06-04.md` | `python governance/compat/check_markdown_structural_completeness.py --base 45b86df3 --head HEAD --enforce` | CLOSED_PASS_BOUNDED |
| T6-GAP-09: freshness state machine | §Execution Plan step 1 (part of schema doc) | `docs/reference/CVF_LPCI_FACETED_RETRIEVAL_SCHEMA_2026-06-04.md` §Freshness State Machine | `python governance/compat/check_markdown_structural_completeness.py --base 45b86df3 --head HEAD --enforce` | CLOSED_PASS_BOUNDED |
| T6-GAP-10: response boundary enforcement contract | §Execution Plan step 2 | `docs/reference/CVF_LPCI_RESPONSE_BOUNDARY_ENFORCEMENT_CONTRACT_2026-06-04.md` | `python governance/compat/check_corpus_intelligence_classification.py --base 45b86df3 --head HEAD --enforce` | CLOSED_PASS_BOUNDED |
| T6-GAP-03/04: sourceFamily + processing ledger | §Execution Plan step 3-4 | corpus records + `policylocal-t7-processing-ledger.json` | `python governance/compat/check_corpus_completeness_report_integrity.py --base 45b86df3 --head HEAD --enforce` | CLOSED_PASS_BOUNDED |
| T7 completion review | §Execution Plan step 5 | `docs/reviews/CVF_LPCI2_T7_CORPUS_FACET_SCHEMA_AUTHORING_COMPLETION_2026-06-04.md` | all governance gates | CLOSED_PASS_BOUNDED |
| Session state sync | §Execution Plan step 8 | CVF_SESSION_MEMORY.md, ACTIVE_SESSION_STATE.json, AGENT_HANDOFF_V15 | `python governance/compat/check_active_session_state.py --enforce` | CLOSED_PASS_BOUNDED |

## Agent Roles

| Role | Owner |
| --- | --- |
| Orchestrator | Codex |
| Implementer | Codex |
| Reviewer | Codex reviewer role |
| Closer | Codex closer role |
| Worker commit boundary | WORKER_MUST_NOT_COMMIT |

## Worker Autonomy / No-Question Rule

The assigned agent must author all three artifacts and update corpus records
without asking the operator, as long as work stays within Allowed scope.

Escalation reserved for:
- topicTags or freshnessStatus values would require legal interpretation beyond
  what document content supports;
- corpus records file is missing or hash-drifted from T5 values;
- any action that would exceed Allowed scope, open search/chat/runtime, or
  consume provider quota.

## Allowed Scope

- Author `docs/reference/CVF_LPCI_FACETED_RETRIEVAL_SCHEMA_2026-06-04.md` (NEW)
- Author `docs/reference/CVF_LPCI_RESPONSE_BOUNDARY_ENFORCEMENT_CONTRACT_2026-06-04.md` (NEW)
- Update `Policy_Local/data/generated/policylocal-corpus-records.json` to
  schemaVersion `policylocal.corpusRecords.t7.v1` (add topicTags,
  freshnessStatus, freshnessCheckedAt, sourceFamily, familyId)
- Author `Policy_Local/data/generated/policylocal-t7-processing-ledger.json` (NEW)
- Write T7 completion review at
  `docs/reviews/CVF_LPCI2_T7_CORPUS_FACET_SCHEMA_AUTHORING_COMPLETION_2026-06-04.md` (NEW)
- Update `docs/roadmaps/CVF_LPCI2_POLICYLOCAL_PRODUCTIZATION_ROADMAP_2026-06-03.md`
  T7 row status
- Update `CVF_SESSION_MEMORY.md`, `CVF_SESSION/ACTIVE_SESSION_STATE.json`, and
  `AGENT_HANDOFF_V15_2026-05-29.md`
- Run local CVF governance gate commands

## Forbidden Scope

- Do not re-extract DOCX text (T5 extraction is authoritative).
- Do not make provider calls or run inference to derive topicTags.
- Do not build a search index, vector store, embedding pipeline, API route,
  chatbot, or any runtime component.
- Do not touch runtime source files under `EXTENSIONS/` or `cvf-web/`.
- Do not open T8 or any follow-on search implementation in this tranche.
- Do not claim search/chat readiness — T8 is required after T7.

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V15_2026-05-29.md`
- `docs/reviews/CVF_LPCI2_T6_SEARCH_CHAT_READINESS_GATE_COMPLETION_2026-06-04.md`
- `docs/reference/CVF_CORPUS_SEARCH_FILTER_READINESS_STANDARD_2026-06-02.md`
- `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-corpus-records.json`

## Pre-Flight Checks

```powershell
git rev-parse --short HEAD
git status --short --branch
Test-Path "D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-corpus-records.json"
Test-Path "D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\116_2025_QH15_666020.docx"
Test-Path "D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\148_2025_QH15_675262.docx"
python governance/compat/check_active_session_state.py --enforce
```

## 6A. Source-Fidelity Pass

Existing paths verified before dispatch:

- `docs/reviews/CVF_LPCI2_T6_SEARCH_CHAT_READINESS_GATE_COMPLETION_2026-06-04.md` — PRESENT
- `docs/reference/CVF_CORPUS_SEARCH_FILTER_READINESS_STANDARD_2026-06-02.md` — PRESENT
- `docs/reference/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_STANDARD_2026-06-01.md` — PRESENT
- `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-corpus-records.json` — PRESENT (schemaVersion policylocal.corpusRecords.t5.v1)

Planned new paths (marked NEW):

- NEW: `docs/reference/CVF_LPCI_FACETED_RETRIEVAL_SCHEMA_2026-06-04.md`
- NEW: `docs/reference/CVF_LPCI_RESPONSE_BOUNDARY_ENFORCEMENT_CONTRACT_2026-06-04.md`
- NEW: `docs/reviews/CVF_LPCI2_T7_CORPUS_FACET_SCHEMA_AUTHORING_COMPLETION_2026-06-04.md`
- NEW: `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-t7-processing-ledger.json`
- UPDATE: `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-corpus-records.json`

## 6C. System Loop Interlock Routing

Upstream: T6 gap register → T7 authoring scope (7 gaps).

Downstream: T7 schema + contract + updated corpus records → T8 Search Layer
Scaffolding (query receipt model, derived retrieval trace).

Claim boundary: T7 authors governance schema documents and updates corpus
records. It does NOT implement a search index, query engine, vector store,
embedding pipeline, or chat runtime.

## Execution Plan

1. Author `docs/reference/CVF_LPCI_FACETED_RETRIEVAL_SCHEMA_2026-06-04.md`:
   - Common CVF facet fields (all from standard §Common Facet Schema)
   - PolicyLocal domain extensions (jurisdiction, authorityLevel, issuingBody,
     effectiveDate, amendmentStatus, sourceAuthority)
   - `topicTags` controlled vocabulary for VN_NATIONAL_ASSEMBLY_2025 corpus:
     derive from T5 corpus content (law numbers, subjects mentioned in extracted
     text snippets, amendment scope) — no provider call; structural derivation only
   - `sourceFamily` / `familyId` definition
   - Freshness state machine: states `current` | `not_yet_in_force` |
     `stale` | `superseded` | `repealed` | `obsolete` | `unknown`; transition
     rules based on effectiveDate vs run date and status field
   - Conflict resolution rule for overlapping amended laws
   - Schema version identifier: `policylocal.facetSchema.t7.v1`

2. Author `docs/reference/CVF_LPCI_RESPONSE_BOUNDARY_ENFORCEMENT_CONTRACT_2026-06-04.md`:
   - Machine-readable policy contract (JSON-like block in markdown)
   - Fields: `contractVersion`, `corpusId`, `defaultAnswerClass`,
     `escalateConditions` (array), `blockedAnswerClasses` (array),
     `notYetInForceRule`, `legalAdviceRule`, `citationRequirement`
   - Escalate conditions: legal-advice requests, current-applicability queries
     before effectiveDate, legal-interpretation requests
   - Blocked: `DIRECT_CITED_ANSWER` (citation depth insufficient)
   - Source: derived from T5 adversarial sampling S1-S4 outcomes and T2
     answerClass matrix

3. Update `policylocal-corpus-records.json` to schemaVersion
   `policylocal.corpusRecords.t7.v1`:
   - Add to both records: `topicTags` (array), `freshnessStatus`,
     `freshnessCheckedAt`, `sourceFamily`, `familyId`
   - `topicTags` for file-116: derive from law number, subject area of Law
     116/2025/QH15 (cybersecurity / information security amendment)
   - `topicTags` for file-148: derive from law number, subject area of Law
     148/2025/QH15 (information technology / digital law amendment)
   - `freshnessStatus`: `not_yet_in_force` for both (effectiveDate=2026-07-01;
     run date 2026-06-04)
   - `freshnessCheckedAt`: `2026-06-04`
   - `sourceFamily`: `VN_NATIONAL_ASSEMBLY_2025`
   - `familyId`: `vn-national-assembly-2025`
   - Do not change any existing T5 fields

4. Author `policylocal-t7-processing-ledger.json` — explicit standalone
   processing ledger with one row per file covering all processing stages
   from T4S through T7.

5. Write T7 completion review
   `docs/reviews/CVF_LPCI2_T7_CORPUS_FACET_SCHEMA_AUTHORING_COMPLETION_2026-06-04.md`
   including:
   - `## Scope`
   - `## Purpose`
   - `## Gap Closure Evidence` (table: gapId → artifact → field → verdict)
   - `## Faceted Retrieval Schema Summary`
   - `## Boundary Enforcement Contract Summary`
   - `## Updated Corpus Records Summary`
   - `## T6 Gate Re-evaluation` (re-score Gates 2, 3, 4, 5 after T7 artifacts)
   - `## Revised Readiness Verdict` (what verdict becomes after T7)
   - `## Findings`
   - `## Risk`
   - `## Acceptance Criteria`
   - `## Verification` (gate commands + results)
   - `## Finding-To-Governance Learning Disposition`
   - `## Source Verification Block`
   - `## Public Export Disposition`
   - `## Claim Boundary`

6. Update GC-051 corpus scan registry T7 scan wave entry.

7. Update roadmap T7 row to `CLOSED_PASS_BOUNDED`.

8. Run required governance gates.

9. Update session state files.

10. Stop for operator commit (WORKER_MUST_NOT_COMMIT).

## Required Governance Gates

```powershell
git add docs/reference/CVF_LPCI_FACETED_RETRIEVAL_SCHEMA_2026-06-04.md
git add docs/reference/CVF_LPCI_RESPONSE_BOUNDARY_ENFORCEMENT_CONTRACT_2026-06-04.md
git add docs/reviews/CVF_LPCI2_T7_CORPUS_FACET_SCHEMA_AUTHORING_COMPLETION_2026-06-04.md

python governance/compat/check_corpus_completeness_report_integrity.py --base 45b86df3 --head HEAD --enforce
python governance/compat/check_corpus_to_knowledge_map_reconciliation.py --base 45b86df3 --head HEAD --enforce
python governance/compat/check_corpus_intelligence_classification.py --base 45b86df3 --head HEAD --enforce
python governance/compat/check_markdown_structural_completeness.py --base 45b86df3 --head HEAD --enforce
python governance/compat/check_finding_to_governance_learning.py --base 45b86df3 --head HEAD --enforce
python governance/compat/check_work_order_dispatch_quality.py --base 45b86df3 --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 45b86df3 --head HEAD
```

## Required Outputs

| Output | Path | Required at handoff |
| --- | --- | --- |
| Faceted retrieval schema | `docs/reference/CVF_LPCI_FACETED_RETRIEVAL_SCHEMA_2026-06-04.md` | Yes |
| Boundary enforcement contract | `docs/reference/CVF_LPCI_RESPONSE_BOUNDARY_ENFORCEMENT_CONTRACT_2026-06-04.md` | Yes |
| Updated corpus records (t7.v1) | `Policy_Local/data/generated/policylocal-corpus-records.json` | Yes |
| Processing ledger | `Policy_Local/data/generated/policylocal-t7-processing-ledger.json` | Yes |
| GC-051 registry update | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` and `.md` | Yes |
| T7 completion review | `docs/reviews/CVF_LPCI2_T7_CORPUS_FACET_SCHEMA_AUTHORING_COMPLETION_2026-06-04.md` | Yes |
| Session state synced | CVF_SESSION_MEMORY.md, ACTIVE_SESSION_STATE.json, AGENT_HANDOFF_V15 | Yes |

## Acceptance Criteria

- [x] T6-GAP-01: `topicTags` present in both corpus records with at least 2 tags each
- [x] T6-GAP-02: `freshnessStatus=not_yet_in_force` and `freshnessCheckedAt=2026-06-04` in both records
- [x] T6-GAP-03: `sourceFamily=VN_NATIONAL_ASSEMBLY_2025` and `familyId` present in both records
- [x] T6-GAP-04: standalone `policylocal-t7-processing-ledger.json` present with all stages T4S→T7
- [x] T6-GAP-07: `CVF_LPCI_FACETED_RETRIEVAL_SCHEMA_2026-06-04.md` present with all common + domain fields and freshness state machine
- [x] T6-GAP-09: freshness state machine section present in schema doc with all 7 states and transition rules
- [x] T6-GAP-10: `CVF_LPCI_RESPONSE_BOUNDARY_ENFORCEMENT_CONTRACT_2026-06-04.md` present with machine-readable policy block
- [x] Corpus records schemaVersion upgraded to `policylocal.corpusRecords.t7.v1`
- [x] All existing T5 fields preserved unchanged (no re-extraction)
- [x] All 7 governance gates PASS
- [x] Session state COMPLIANT

## Forbidden Filesystem State At Dispatch

| Forbidden path | Expected state | Actual state at dispatch | Action if PRESENT |
| --- | --- | --- | --- |
| `docs/reference/CVF_LPCI_FACETED_RETRIEVAL_SCHEMA_2026-06-04.md` | ABSENT | ABSENT ✓ | Stop; reconcile before re-dispatch |
| `docs/reference/CVF_LPCI_RESPONSE_BOUNDARY_ENFORCEMENT_CONTRACT_2026-06-04.md` | ABSENT | ABSENT ✓ | Stop; reconcile before re-dispatch |
| `docs/reviews/CVF_LPCI2_T7_CORPUS_FACET_SCHEMA_AUTHORING_COMPLETION_2026-06-04.md` | ABSENT | ABSENT ✓ | Stop; reconcile before re-dispatch |

## Write Ownership

Owned repo paths:

- `docs/reference/CVF_LPCI_FACETED_RETRIEVAL_SCHEMA_2026-06-04.md` (NEW)
- `docs/reference/CVF_LPCI_RESPONSE_BOUNDARY_ENFORCEMENT_CONTRACT_2026-06-04.md` (NEW)
- `docs/reviews/CVF_LPCI2_T7_CORPUS_FACET_SCHEMA_AUTHORING_COMPLETION_2026-06-04.md` (NEW)
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` (UPDATE — T7 schema-upgrade metadata)
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` (UPDATE — T7 quick lookup)
- `docs/roadmaps/CVF_LPCI2_POLICYLOCAL_PRODUCTIZATION_ROADMAP_2026-06-03.md` (UPDATE — T7 row)
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V15_2026-05-29.md`

Owned external workspace paths:

- `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-corpus-records.json` (UPDATE — t7.v1)
- `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-t7-processing-ledger.json` (NEW)

Forbidden paths (do not touch):

- All runtime source files under `EXTENSIONS/` and `cvf-web/`
- DOCX source files (read-only; no re-extraction)
- Public-sync clone
- Any file not in the owned list above

## Review Gate

Reviewer must verify:

- All 7 T7-scope gaps (T6-GAP-01/02/03/04/07/09/10) have closure evidence in
  the completion review §Gap Closure Evidence table;
- Corpus records schemaVersion = `policylocal.corpusRecords.t7.v1`;
- `topicTags` present in both records (minimum 2 tags each);
- `freshnessStatus=not_yet_in_force` and `freshnessCheckedAt=2026-06-04` both records;
- Faceted retrieval schema document present with `## Scope / Applies To`,
  freshness state machine (7 states), and topicTags vocabulary;
- Boundary enforcement contract present with machine-readable JSON block and
  at least 3 escalate conditions;
- No provider calls, no search index, no runtime implementation;
- All T5 fields preserved (no hash drift, no re-extraction);
- Session state COMPLIANT and all 7 governance gates PASS.

## Operator Checkpoint

Operator checkpoint is required before opening T8 Search Layer Scaffolding or
any search/chat implementation work.

If T7 revised verdict is READY_WITH_CONDITIONS: operator reviews remaining
T8-scope gaps (T6-GAP-05/06/08) and authorizes T8.

If any T7 gate fails on re-evaluation: operator decides whether to remediate
within T7 scope or open a new bounded repair tranche.

## Return Conditions

Return to orchestrator without implementation closure if:

- DOCX files are inaccessible or hash-drifted from T5 values;
- topicTags derivation would require legal interpretation beyond document
  content (record tags as `unknown` and escalate);
- any action within Allowed scope would inadvertently open search/chat runtime;
- required governance gates fail outside Allowed scope.

## Closure Checklist

- [x] Work order has source verification block
- [x] Work order has roadmap-to-work-order trace matrix
- [x] Work order has Worker Autonomy / No-Question Rule
- [x] Work order names all 7 T7-scope gaps from T6 gap register
- [x] Work order names faceted retrieval schema, boundary contract, and corpus records upgrade as required outputs
- [x] Work order forbids search/chat/runtime/product implementation
- [x] Work order names T8 as the next tranche after T7
- [x] Work order has `executionBaseHead` and `closureBaseHead` anchor fields
- [x] Forbidden filesystem state at dispatch verified ABSENT

## Public Export Disposition

DEFERRED_PRIVATE_ONLY — references private local workspace and internal LPCI
governance chain. Sanitized guide may follow as separate public-sync batch.

## Claim Boundary

This work order authorizes schema authoring, boundary contract authoring, and
corpus records schema upgrade only. It does not authorize search runtime, chat
runtime, vector store, embedding pipeline, API route, provider calls, legal
advice, production readiness, or public export. T8 is the next tranche after T7.
