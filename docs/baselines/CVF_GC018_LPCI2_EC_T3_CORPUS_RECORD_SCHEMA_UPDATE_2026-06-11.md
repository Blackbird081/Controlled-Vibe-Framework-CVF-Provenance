# CVF GC-018 Baseline: LPCI2 EC-T3 Corpus Record Schema Update

Memory class: FULL_RECORD

Status: DISPATCHED

docType: baseline

Date: 2026-06-11

Author: Claude (operator-directed; Codex review and explicit authorization required before dispatch)

baseHead: `b357b519`

---

## Purpose

Authorize a Claude worker to add the EC-02 lifecycle fields (`documentStatus`,
`promulgationDate`, `effectiveDate`) to the corpus record TypeScript schema in
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts`, add the
`supportsDocumentStatus` flag to `DscpDomainProfile`, and add a migration rule
asserting that no record transitions from `BLOCKED_UNTIL_*` to `IN_FORCE`
without an operator-supplied `effectiveDate` that has actually passed.

EC-T3 is a TypeScript-only schema update. It does NOT change runtime gate
logic, corpus JSON data files, DSCP profile values, retrieval behavior, or
any test that would require a live run or provider call.

---

## Predecessor Evidence

| Document | Status | Commit |
| --- | --- | --- |
| `docs/baselines/CVF_GC018_LPCI2_EC_T2_CONTRACT_AMENDMENT_AND_MACHINE_SEMANTICS_2026-06-11.md` | CLOSED_PASS_BOUNDED | `cb026168` |
| `docs/reference/CVF_EC02_GATE_SEMANTICS_2026-06-11.json` | produced by EC-T2 | `cb026168` |
| `docs/reference/CVF_LPCI_RESPONSE_BOUNDARY_ENFORCEMENT_CONTRACT_2026-06-11.md` | produced by EC-T2 | `cb026168` |
| EC-T1 D-01 through D-04 decisions | `docs/baselines/CVF_GC018_LPCI2_EC_T1_REGULATORY_DATE_MODEL_GOVERNANCE_DECISION_2026-06-11.md` | `5e184d00` |

---

## Decision

EC-T3 is authorized as a TypeScript schema-only tranche:

- Add `DocumentStatus` type alias to `types.ts` (new export).
- Add `documentStatus?: DocumentStatus` and `promulgationDate?: string` to
  `LpciIndexRecord`, `ManifestEntry`, and `IntakeRecord`.
- Add `supportsDocumentStatus?: boolean` to `DscpDomainProfile` in
  `dscp.domain.profile.contract.ts`.
- Add or update `types.ts` tests to cover the new fields.
- Migration invariant: no record may carry `documentStatus: 'IN_FORCE'`
  unless `effectiveDate` is operator-supplied and has passed. EC-T3 may record
  this as a type-level/test-name invariant only; runtime enforcement remains
  EC-T5 scope.

No DSCP domain profile JSON values are changed. No corpus JSON data files are
changed. No runtime gate logic is changed. No public-sync. No current-law claim.

---

## Authorization Summary

Authorized under:

- EC-T2 closure: `docs/baselines/CVF_GC018_LPCI2_EC_T2_CONTRACT_AMENDMENT_AND_MACHINE_SEMANTICS_2026-06-11.md`
  Status: `CLOSED_PASS_BOUNDED`, commit `cb026168`
- EC-T1 D-01 (`documentStatus` name ACCEPTED), D-03 (non-regulatory omit,
  `supportsDocumentStatus` flag required), D-04 (boundary unchanged through EC-T4).
- Roadmap: `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md`
  Part B, EC-T3 row.

No EC-T4, EC-T5, EC-T6, corpus JSON data changes, DSCP profile value changes,
retrieval gate changes, checker additions, or public-sync is authorized.

---

## Problem Statement (source-verified)

### Current schema state (types.ts)

Source: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts`

`LpciIndexRecord` (line 29-44):
- Has `effectiveDate?: string` (line 36) -- already present.
- Has `status: RecordStatus` (line 37) -- this is the EXISTING `RecordStatus`
  enum (`effective | draft | amended | superseded | repealed | obsolete | unknown`).
  This is NOT the EC-02 `documentStatus` three-state enum.
- Does NOT have `promulgationDate`, `documentStatus` (EC-02 lifecycle).

`ManifestEntry` (line 106-115):
- Has `effectiveDate?: string` (line 113) -- already present.
- Does NOT have `promulgationDate`, `documentStatus`.

`RecordStatus` type (line 9-16) -- existing, DO NOT RENAME OR MODIFY.
It uses `status` as the field name, which is different from `documentStatus`.
No collision risk -- these are two independent fields on `LpciIndexRecord`.

### Current schema state (DscpDomainProfile)

Source: `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts`

`DscpDomainProfile` (line 23-50):
- Has `domainFacetFields: Record<string, string>` (line 38).
- Has `boundaryRules: Record<string, string>` (line 46).
- Does NOT have `supportsDocumentStatus`.

### Collision constraint (carried from EC-T1/EC-T2)

`domainFacetFields.documentStatus: "approved"` exists in
`EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.domain.profile.contract.test.ts`
line 70 (company-docs test fixture, generic facet field).

EC-T3 MUST NOT change this test fixture. The new `documentStatus` EC-02
lifecycle field lives at `LpciIndexRecord.documentStatus` and
`ManifestEntry.documentStatus`, NOT inside `domainFacetFields`. They are
separate TypeScript fields. No conflict at the type level.

If EC-T3 adds `supportsDocumentStatus` to `DscpDomainProfile`, the
company-docs profile test fixture must be updated to include
`supportsDocumentStatus: false` (or the field may be optional with `false`
as the default). Worker must check whether the existing test breaks.

---

## Scope Boundary

In scope for EC-T3:

- `DocumentStatus` type alias export in `types.ts`.
- `documentStatus?: DocumentStatus` and `promulgationDate?: string` added
  to `LpciIndexRecord`, `ManifestEntry`, `IntakeRecord` (if it extends
  `LpciIndexRecord`, it inherits automatically -- worker must verify).
- `supportsDocumentStatus?: boolean` added to `DscpDomainProfile`; absent or
  undefined must be treated as false by later runtime work.
- Unit tests covering the new fields.
- Migration invariant assertion: test name or local assertion documents that
  `documentStatus: 'IN_FORCE'` requires operator-supplied `effectiveDate`;
  EC-T3 must not claim runtime enforcement for this invariant.
- Fix to company-docs test fixture if `supportsDocumentStatus` addition
  breaks existing tests.

Out of scope for EC-T3:

- Any DSCP domain profile JSON value change (ec02Gate, languageCodes, etc.).
- Any corpus JSON data file change.
- Any runtime gate logic change (EC-T5 scope).
- Any retrieval behavior change (EC-T5/EC-T6 scope).
- Any checker addition to governance hook chain.
- Any public-sync or public documentation update.
- EC-T4 per-project metadata backfill (requires operator-supplied dates).
- EC-T5 through EC-T6.
- EX-lane work.
- Setting `documentStatus: 'IN_FORCE'` on any existing record.
- Any current-law, legal correctness, or production readiness claim.

---

## Evidence

All source items verified at baseHead `b357b519`.

Key findings:

- `LpciIndexRecord` in `types.ts` line 29: `effectiveDate?: string` present;
  `promulgationDate` and `documentStatus` (EC-02) absent.
- `RecordStatus` type (line 9-16) uses `status` field -- no collision with
  the new `documentStatus` EC-02 field.
- `ManifestEntry` line 106: `effectiveDate?: string` present; `promulgationDate`
  and `documentStatus` absent.
- `IntakeRecord` line 124: `extends LpciIndexRecord` -- inherits new fields
  automatically once added to `LpciIndexRecord`.
- `DscpDomainProfile` in `dscp.domain.profile.contract.ts` line 23: no
  `supportsDocumentStatus` field.
- Company-docs fixture collision: `domainFacetFields.documentStatus: "approved"`
  in `tests/dscp.domain.profile.contract.test.ts` line 70 -- NOT the EC-02
  lifecycle field; no type-level conflict.
- EC-02 gate semantics JSON produced by EC-T2 at `cb026168` defines the
  three-state enum: `PROMULGATED | IN_FORCE | STATUS_UNKNOWN`.

---

## Source Verification Table

| Symbol / path | File | Verified line / section |
| --- | --- | --- |
| `LpciIndexRecord` interface | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts` | line 29 |
| `effectiveDate?: string` in `LpciIndexRecord` | same | line 36 |
| `status: RecordStatus` in `LpciIndexRecord` | same | line 37 |
| `RecordStatus` type enum | same | lines 9-16 |
| `ManifestEntry` interface | same | line 106 |
| `effectiveDate?: string` in `ManifestEntry` | same | line 113 |
| `IntakeRecord extends LpciIndexRecord` | same | line 124 |
| `DscpDomainProfile` interface | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | line 23 |
| `domainFacetFields: Record<string, string>` | same | line 38 |
| `boundaryRules: Record<string, string>` | same | line 46 |
| `supportsDocumentStatus` -- absent from profile | grep `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | ABSENT (new field) |
| `promulgationDate` -- absent from types.ts | grep `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts` | ABSENT (new field) |
| `DocumentStatus` type -- absent from types.ts | same | ABSENT (new export) |
| Company-docs fixture collision | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.domain.profile.contract.test.ts` | line 70 |
| EC-02 semantics JSON | `docs/reference/CVF_EC02_GATE_SEMANTICS_2026-06-11.json` | `documentStatusEnum` field |
| EC-T1 D-01 `documentStatus` accepted | `docs/baselines/CVF_GC018_LPCI2_EC_T1_REGULATORY_DATE_MODEL_GOVERNANCE_DECISION_2026-06-11.md` | D-01 section |
| EC-T1 D-03 Option B + `supportsDocumentStatus` | same | D-03 section |
| EC-T1 D-04 boundary confirmed | same | D-04 section |
| Roadmap EC-T3 row | `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md` | Part B, EC-T3 row |

---

## Negative Search And Collision Discipline

Search command: `rg <token> EXTENSIONS/` TypeScript source.
Coverage: EXTENSIONS/ TS source and test files. Verified at baseHead `b357b519`.

| Token | Search roots | Disposition |
| --- | --- | --- |
| `DocumentStatus` (EC-02 type alias) | `EXTENSIONS/` TS | Absent as a type export. One same-token word `documentStatus` exists as a `domainFacetFields` key in company-docs test fixture (line 70) -- different semantic scope; no type collision. |
| `promulgationDate` | `EXTENSIONS/` TS | Absent from all EXTENSIONS source. Non-authoritative occurrence in roadmap/GC-018 planning docs only. No collision. |
| `supportsDocumentStatus` | `EXTENSIONS/` TS | Absent from all EXTENSIONS source. New field. No collision. |

Absent-versus-collision disposition: `DocumentStatus` has one same-token
occurrence as a string-valued `domainFacetFields` key (`"approved"`), not as
a TypeScript type. The new export is a type alias -- no runtime collision.
`promulgationDate` and `supportsDocumentStatus` have zero EXTENSIONS occurrences.

---

## Forbidden Scope

The following must not appear in EC-T3 artifacts:

- Any change to DSCP domain profile JSON values (`ec02Gate`, `languageCodes`,
  `boundaryRules` values, etc.).
- Any corpus JSON data file change.
- Any runtime gate logic change in `dscp.domain.profile.contract.ts` (line 102
  gate logic is EC-T5 scope).
- Any `documentStatus: 'IN_FORCE'` assignment to any existing record.
- Any public-sync commit.
- Any relaxation of EC-01, EC-03, or EC-04.
- Any current-law, legal correctness, or production readiness claim.
- Renaming or modifying `RecordStatus` enum or the `status` field on
  `LpciIndexRecord` (separate concept from `documentStatus`).

---

## Acceptance Criteria For EC-T3 Closure

1. `DocumentStatus` type alias exported from `types.ts` with values
   `'PROMULGATED' | 'IN_FORCE' | 'STATUS_UNKNOWN'`.
2. `documentStatus?: DocumentStatus` and `promulgationDate?: string` added to
   `LpciIndexRecord` and `ManifestEntry` in `types.ts`.
3. `supportsDocumentStatus?: boolean` added to `DscpDomainProfile` in
   `dscp.domain.profile.contract.ts`.
4. Existing tests all pass (no regressions). New tests cover new fields.
5. Company-docs fixture updated if `supportsDocumentStatus` addition breaks
   existing tests.
6. `RecordStatus` type and `status` field are unchanged.
7. No corpus JSON data or DSCP profile JSON values changed.
8. Pre-closure autorun gate passes:
   `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base b357b519 --head HEAD`
9. Reviewer-fast passes:
   `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast --serial`
10. CI passes: `npm run test:run` in `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/`
    and type check in `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/`.

---

## Claim Boundary

This GC-018 authorizes TypeScript type additions only. It does not prove
runtime gate correctness, legal correctness, retrieval quality, EC-02
enforcement efficacy, production readiness, public readiness, or any claim
beyond the schema change authorization itself.

EC-02 hard boundary 2026-07-01 remains in force.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
