# CVF GC-018 Baseline: LPCI2 EC-T2 Contract Amendment And Machine Semantics

Memory class: FULL_RECORD

Status: DISPATCHED

docType: baseline

Date: 2026-06-11

Author: Claude (operator-directed; Codex review and explicit authorization required before dispatch)

baseHead: `48ad7a93`

---

## Purpose

Authorize a Claude worker to produce the EC-T2 contract amendment and
machine-readable gate semantics JSON. EC-T2 updates the response boundary
enforcement contract from version `policylocal.boundaryContract.t7.v1` to a
new version that incorporates the `documentStatus` three-state enum and the
`QUERY_CLASS_GATED` ec02Gate token. EC-T2 also produces a machine-readable
`CVF_EC02_GATE_SEMANTICS_*.json` artifact that a future checker can validate
against the runtime gate.

EC-T2 does NOT change any runtime TypeScript source, corpus record, DSCP
domain profile value, checker, test, or public documentation. It is a
document-only tranche.

---

## Predecessor Evidence

| Document | Status | Commit |
| --- | --- | --- |
| `docs/baselines/CVF_GC018_LPCI2_EC_T1_REGULATORY_DATE_MODEL_GOVERNANCE_DECISION_2026-06-11.md` | CLOSED_PASS_BOUNDED | `5e184d00` |
| `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md` | EC-T2 row in Part B | authoritative |
| `docs/reference/CVF_LPCI_RESPONSE_BOUNDARY_ENFORCEMENT_CONTRACT_2026-06-04.md` | T7 v1 -- target of amendment | authoritative |

---

## Decision

EC-T2 is authorized as a document-only tranche. The decision is:

- Produce a new response boundary enforcement contract version
  (`policylocal.boundaryContract.ec-t2.v1`) incorporating the EC-T1 decisions.
- Produce a machine-readable EC-02 gate semantics JSON artifact.
- No runtime source change. No corpus record change. No DSCP profile change.

This decision is bounded by EC-T1 D-01 through D-04 (all recorded at commit
`5e184d00`). Any deviation from the EC-T1 decisions requires a new GC-018.

---

## Authorization Summary

Authorized under:

- EC-T1 closure: `docs/baselines/CVF_GC018_LPCI2_EC_T1_REGULATORY_DATE_MODEL_GOVERNANCE_DECISION_2026-06-11.md`
  Status: `CLOSED_PASS_BOUNDED`, commit `5e184d00`
- Roadmap: `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md`
  Part B, Proposed Tranches, EC-T2 row.
- EC-T1 D-01 through D-04 decisions recorded and committed.

No EC-T3, EC-T4, EC-T5, EC-T6, corpus record change, DSCP profile update,
runtime TypeScript change, or public-sync is authorized by this EC-T2 GC-018.

---

## Problem Statement (source-verified)

### Current contract version

Source: `docs/reference/CVF_LPCI_RESPONSE_BOUNDARY_ENFORCEMENT_CONTRACT_2026-06-04.md`
contractVersion: `policylocal.boundaryContract.t7.v1`

EC-02 entry (lines 72-80):
- `trigger`: `current_applicability_before_effective_date`
- `requiredAnswerClass`: `ESCALATE_OR_ABSTAIN`
- `escalationMessage` hardcodes `"effective date of 2026-07-01"`
- No `documentStatus` field referenced.
- No query-class matrix (content query vs applicability query).
- `expiresWhen`: `"effectiveDate reached AND freshnessStatus transitions to current"` -- date-check only.

The contract distinguishes EC-02 trigger as `current_applicability_before_effective_date`
(applicability query only) but the escalationMessage and expiresWhen do not
distinguish content queries from applicability queries. A `SUMMARY_WITH_SOURCE`
answer about document content is indistinguishable from an applicability query
under the current contract prose.

### Machine semantics gap

No machine-readable gate semantics artifact exists for EC-02.
Source: grep across all `docs/reference/` JSON files for `ec02Gate` or
`QUERY_CLASS_GATED`.
Result: absent from all `docs/reference/` JSON files.
The only references are prose in the contract and the roadmap.

### EC-T1 decisions (authoritative inputs for EC-T2)

From EC-T1 GC-018 (CLOSED_PASS_BOUNDED, commit `5e184d00`):

- D-01: `documentStatus` ACCEPTED as canonical field name.
- D-02: `QUERY_CLASS_GATED` ACCEPTED as canonical ec02Gate token.
  Runtime consequence: EC-T5 must update line 102 gate logic in
  `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts`
  to handle `QUERY_CLASS_GATED` as a routing signal, not a flat block.
  EC-T2 does NOT touch this file.
- D-03: Non-regulatory records omit `documentStatus` entirely; EC-T3 must
  include `supportsDocumentStatus: boolean` at domain profile level.
- D-04: EC-02 boundary `BLOCKED_UNTIL_2026-07-01` unchanged through EC-T4.

### Collision constraint (from EC-T1 source verification)

`domainFacetFields.documentStatus: "approved"` already exists in
`EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.domain.profile.contract.test.ts`
line 70 (company-docs test fixture).

This is NOT the EC-02 lifecycle enum. The new EC-T2 contract must explicitly
note this collision and state that `domainFacetFields.documentStatus` in
non-regulatory facet metadata is a separate concern from the EC-02 lifecycle
`documentStatus` field on corpus records. The contract must not be interpreted
as authorizing the existing test fixture as EC-02 lifecycle support.

---

## Scope Boundary

In scope for EC-T2:

- New version of the response boundary enforcement contract document (new file,
  references prior version, documents changes).
- Machine-readable EC-02 gate semantics JSON:
  `docs/reference/CVF_EC02_GATE_SEMANTICS_2026-06-11.json`
- Collision note in the contract re: `domainFacetFields.documentStatus` in
  non-regulatory test fixtures.
- `notYetInForceDisclosure` i18n template mechanism (locale from domain profile,
  no hardcoded language strings in pipeline code).
- `QUERY_CLASS_GATED` listed as the authorized ec02Gate value that enables
  query-class routing.

Out of scope for EC-T2:

- Any runtime TypeScript source change.
- Any corpus record field addition, migration, or DSCP domain profile update.
- Any checker, test, or machine-gate addition to the governance hook chain.
- Any public-sync or public documentation update.
- EC-T3 through EC-T6.
- EX-lane work.
- Any current-law, legal correctness, or production readiness claim.

---

## Required Artifacts (worker deliverables)

Worker (Claude) must produce the following uncommitted files. WORKER_MUST_NOT_COMMIT.

### 1. Updated response boundary enforcement contract

**Path:** `docs/reference/CVF_LPCI_RESPONSE_BOUNDARY_ENFORCEMENT_CONTRACT_2026-06-11.md`

New file (do not overwrite the T7 version). Must include:

- `contractVersion`: `policylocal.boundaryContract.ec-t2.v1`
- `priorVersion`: reference to `policylocal.boundaryContract.t7.v1` and its path
- `changedBy`: `LPCI2-EC-T2`
- Updated `escalateConditions` EC-02 entry:
  - Split trigger into two cases: `content_query` and `applicability_query`.
  - `documentStatus=PROMULGATED` + content query -> `SUMMARY_WITH_SOURCE` + mandatory disclosure (not ESCALATE_OR_ABSTAIN).
  - `documentStatus=PROMULGATED` + applicability query -> `ESCALATE_OR_ABSTAIN` (EC-02 fires).
  - `documentStatus=IN_FORCE` + applicability query -> `DIRECT_CITED_ANSWER` allowed (EC-02 does not fire).
  - `documentStatus=STATUS_UNKNOWN` + any query -> `ESCALATE_OR_ABSTAIN`.
  - EC-01, EC-03, EC-04 remain unchanged regardless of `documentStatus`.
- `documentStatus` listed as a required corpus record field checked at retrieval time.
- `notYetInForceDisclosure` updated to i18n template mechanism:
  - Template fields: `{promulgationDate}`, `{effectiveDate}`, `{freshnessCheckedAt}`
  - locale from domain profile; default `en`.
  - No hardcoded Vietnamese or other language strings in pipeline code.
  - Template entries for `en` and `vi` (as reference examples).
- Collision note:
  - `domainFacetFields.documentStatus: "approved"` in the company-docs
    DSCP-T10 test fixture is NOT EC-02 lifecycle support.
  - EC-02 lifecycle `documentStatus` is a corpus-record-level field, not a
    `domainFacetFields` subkey.
  - EC-T3 must isolate or rename the non-regulatory fixture if the schema
    collision would cause runtime confusion.
- `QUERY_CLASS_GATED` listed as the authorized ec02Gate value for query-class
  routing; not yet active in runtime (EC-T5 scope).
- `reviewRequired` updated: add trigger for `documentStatus` field change on
  any corpus record.
- All EC-01, EC-03, EC-04 entries carried forward unchanged from v1.

**Line count target:** <= 200 lines (GC-023 governed).

### 2. Machine-readable EC-02 gate semantics JSON

**Path:** `docs/reference/CVF_EC02_GATE_SEMANTICS_2026-06-11.json`

New file. Must be valid JSON. Must include:

```json
{
  "schemaVersion": "ec02-gate-semantics.v1",
  "authoredBy": "LPCI2-EC-T2",
  "authoredAt": "2026-06-11",
  "ec02GateToken": "QUERY_CLASS_GATED",
  "runtimeNote": "EC-T5 must update dscp.domain.profile.contract.ts line 102 to handle QUERY_CLASS_GATED as a routing signal, not a flat block",
  "documentStatusEnum": ["PROMULGATED", "IN_FORCE", "STATUS_UNKNOWN"],
  "queryClassMatrix": [
    {
      "documentStatus": "PROMULGATED",
      "queryClass": "content_query",
      "requiredAnswerClass": "SUMMARY_WITH_SOURCE",
      "disclosureRequired": true,
      "ec02Fires": false,
      "note": "document content may be cited with mandatory notYetInForceDisclosure"
    },
    {
      "documentStatus": "PROMULGATED",
      "queryClass": "applicability_query",
      "requiredAnswerClass": "ESCALATE_OR_ABSTAIN",
      "disclosureRequired": false,
      "ec02Fires": true,
      "note": "applicability claims blocked; EC-02 fires"
    },
    {
      "documentStatus": "IN_FORCE",
      "queryClass": "content_query",
      "requiredAnswerClass": "SUMMARY_WITH_SOURCE",
      "disclosureRequired": false,
      "ec02Fires": false,
      "note": "document is in force; content queries allowed"
    },
    {
      "documentStatus": "IN_FORCE",
      "queryClass": "applicability_query",
      "requiredAnswerClass": "DIRECT_CITED_ANSWER",
      "disclosureRequired": false,
      "ec02Fires": false,
      "note": "document is in force; applicability answers allowed with citation"
    },
    {
      "documentStatus": "STATUS_UNKNOWN",
      "queryClass": "any",
      "requiredAnswerClass": "ESCALATE_OR_ABSTAIN",
      "disclosureRequired": false,
      "ec02Fires": true,
      "note": "unknown status forces escalation; no content or applicability answer"
    }
  ],
  "independentGates": ["EC-01", "EC-03", "EC-04"],
  "independentGatesNote": "EC-01 legal_advice, EC-03 legal_interpretation, EC-04 compliance_determination fire regardless of documentStatus",
  "boundaryConstraints": {
    "ec02Boundary": "BLOCKED_UNTIL_2026-07-01",
    "boundaryActiveThrough": "EC-T4_INCLUSIVE",
    "noRecordMayReceive": "documentStatus=IN_FORCE before 2026-07-01",
    "ec02GateTokenActiveFrom": "EC-T5_AFTER_OPERATOR_SUPPLIED_EFFECTIVE_DATES"
  },
  "collisionNote": {
    "existingKey": "domainFacetFields.documentStatus",
    "existingValue": "approved",
    "existingSource": "EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.domain.profile.contract.test.ts line 70",
    "existingPurpose": "company-docs test fixture facet metadata, NOT EC-02 lifecycle enum",
    "ec02LifecycleField": "corpus-record-level documentStatus, not domainFacetFields subkey",
    "resolution": "EC-T3 must isolate or rename this fixture key if schema collision causes runtime confusion"
  },
  "checkerNote": "Future checker must assert: (1) no corpus record carries documentStatus=IN_FORCE before effectiveDate passes; (2) all BLOCKED_UNTIL_* records carry documentStatus=PROMULGATED after EC-T3 migration; (3) ec02GateToken in domain profile matches this file's ec02GateToken value"
}
```

**Line count target:** <= 80 lines (JSON; GC-023 governed).

---

## Evidence

All source items below were verified at HEAD `48ad7a93` before this GC-018
was authored. No item is accepted without direct grep or file evidence.

Key findings:

- T7 v1 contract has a single EC-02 entry with no query-class split.
- `notYetInForceDisclosure` in T7 v1 is a hardcoded English string, not an
  i18n template.
- No machine-readable EC-02 gate semantics JSON exists in `docs/reference/`.
- `QUERY_CLASS_GATED` and `promulgationDate` are NOT present in any EXTENSIONS
  TypeScript or JSON source.
- `documentStatus` exists once in the EXTENSIONS test suite as a non-EC-02
  facet field (`"approved"` value, company-docs fixture) -- not EC-02 lifecycle.
- EC-T1 D-01 through D-04 are all recorded and committed at `5e184d00`.

---

## Source Verification Table

| Symbol / path | File | Verified line / section |
| --- | --- | --- |
| `contractVersion: policylocal.boundaryContract.t7.v1` | `docs/reference/CVF_LPCI_RESPONSE_BOUNDARY_ENFORCEMENT_CONTRACT_2026-06-04.md` | line 49 |
| EC-02 entry `trigger: current_applicability_before_effective_date` | same | lines 72-80 |
| `notYetInForceDisclosure` mechanism | same | line 104-105 |
| `effectiveDate` in contract citation minimum | same | line 115 |
| `reviewRequired` lifecycle trigger | same | line 130 |
| EC-01 trigger `legal_advice_request` | same | lines 63-70 |
| EC-03 trigger `legal_interpretation_request` | same | lines 82-90 |
| EC-04 trigger `compliance_determination` | same | lines 91-98 |
| `boundaryRules: Record<string, string>` | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | line 46 |
| `ruleValue.startsWith("BLOCKED")` gate | same | line 102 |
| `domainFacetFields.documentStatus: "approved"` fixture | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.domain.profile.contract.test.ts` | line 70 |
| EC-02 machine semantics -- no prior JSON | grep `docs/reference/` for `ec02Gate` or `QUERY_CLASS_GATED` | ABSENT -- new artifact, no prior file with this name |
| EC-T1 D-01 decision `documentStatus` ACCEPTED | `docs/baselines/CVF_GC018_LPCI2_EC_T1_REGULATORY_DATE_MODEL_GOVERNANCE_DECISION_2026-06-11.md` | D-01 section |
| EC-T1 D-02 decision `QUERY_CLASS_GATED` ACCEPTED | same | D-02 section |
| EC-T1 D-03 decision Option B (non-regulatory omit) | same | D-03 section |
| EC-T1 D-04 decision boundary confirmed | same | D-04 section |
| Roadmap EC-T2 tranche row | `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md` | Part B, Proposed Tranches |

---

## Forbidden Scope

The following must not appear in any EC-T2 artifact:

- Any runtime TypeScript source change.
- Any corpus record field addition, migration, or value change.
- Any DSCP domain profile `ec02Gate` value change.
- Any checker or test addition.
- Any public-sync commit.
- Any relaxation of EC-01, EC-03, or EC-04 conditions.
- Any current-law or legal correctness claim.
- Any `documentStatus=IN_FORCE` for any record (EC-T4 scope, after operator supplies dates).
- Overwriting `docs/reference/CVF_LPCI_RESPONSE_BOUNDARY_ENFORCEMENT_CONTRACT_2026-06-04.md`
  (the T7 v1 contract must remain intact; EC-T2 produces a new file).

---

## Acceptance Criteria For EC-T2 Closure

This GC-018 may transition from `PROPOSED` to `CLOSED_PASS_BOUNDED` only when:

1. Both required artifacts produced by worker: contract v2 file + gate semantics JSON.
2. New contract version references prior version and documents changes.
3. EC-02 query-class matrix in the contract matches the matrix in the gate semantics JSON.
4. Collision note present in both artifacts re: `domainFacetFields.documentStatus`.
5. `notYetInForceDisclosure` uses i18n template mechanism (no hardcoded language strings in pipeline code).
6. All EC-01, EC-03, EC-04 entries carried forward unchanged.
7. Line count: contract <= 200 lines; gate semantics JSON <= 80 lines.
8. Pre-closure autorun gate passes:
   `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 48ad7a93 --head HEAD`
9. Reviewer-fast passes:
   `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast --serial`
10. Codex updates status to `CLOSED_PASS_BOUNDED` before committing.

---

## Work Order

The Claude worker work order for this tranche is:

`docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI2_EC_T2_CONTRACT_AMENDMENT_FOR_CLAUDE_2026-06-11.md`

WORKER_MUST_NOT_COMMIT. Worker produces uncommitted artifacts. Codex reviews,
gates, and commits.

---

## Negative Search And Collision Discipline

Search command: `rg <token> EXTENSIONS/` TypeScript + JSON. Coverage:
EXTENSIONS/ all TS/JSON source files. Verified at baseHead `48ad7a93`.

| Token | Search roots | Disposition |
| --- | --- | --- |
| `QUERY_CLASS_GATED` | `EXTENSIONS/` TS + JSON; `docs/roadmaps/` | Absent from runtime source. Non-authoritative occurrence in roadmap prose (planning doc only, not binding). No EXTENSIONS collision. |
| `promulgationDate` | `EXTENSIONS/` TS + JSON | Absent from runtime source. Non-authoritative occurrence in roadmap prose only. No EXTENSIONS collision. |
| `CVF_EC02_GATE_SEMANTICS` | `docs/reference/` JSON filenames | Absent. New artifact. No collision. |
| `documentStatus` (EC-02 lifecycle enum) | `EXTENSIONS/` TS + JSON | Absent as EC-02 lifecycle enum. One same-token occurrence: `domainFacetFields.documentStatus: "approved"` in `tests/dscp.domain.profile.contract.test.ts` line 70 (company-docs fixture). Collision disposition: different semantic scope, not EC-02 lifecycle. EC-T3 must isolate. |

Absent-versus-collision disposition: tokens `QUERY_CLASS_GATED` and
`promulgationDate` have zero EXTENSIONS occurrences -- their only occurrence is
non-authoritative roadmap planning prose. `documentStatus` has one same-token
occurrence in a test fixture with a different semantic scope; this is a
documented collision, not a binding conflict for EC-T2 scope.

---

## Claim Boundary

This GC-018 authorizes a document-only contract amendment and machine-readable
semantics JSON. It does not prove runtime gate correctness, legal correctness,
retrieval quality, EC-02 enforcement efficacy, production readiness, public
readiness, or any claim beyond the authorization record itself.

EC-02 hard boundary 2026-07-01 remains in force.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: internal governance authorization record; not public-synced.
