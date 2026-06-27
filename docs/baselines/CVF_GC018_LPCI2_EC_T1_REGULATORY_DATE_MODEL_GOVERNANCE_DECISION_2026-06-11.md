# CVF GC-018 Baseline: LPCI2 EC-T1 Regulatory Date Model Governance Decision

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: baseline

Date: 2026-06-11

Author: Claude (operator-directed; Codex review and explicit authorization required before dispatch)

baseHead: `557d4f73`

---

## Purpose

Establish the CVF-layer governance decision record for the regulatory date
model (EC-02 refinement). Records operator decisions required to authorize
the EC-T2 contract amendment lane. This is a decision record only -- no
runtime source, corpus record, or DSCP profile is changed by EC-T1.

---

## Authorization Summary

EC-T1 is a governance decision record only. It does not dispatch a Claude
implementation worker. It does not change any runtime source, corpus record,
or DSCP profile value. It establishes the CVF-layer authorization for the
`documentStatus` three-state enum and the `QUERY_CLASS_GATED` ec02Gate token
concept, and commits operator decisions on open questions that block EC-T2
(contract amendment).

No EC-T2, EC-T3, EC-T4, EC-T5, EC-T6, corpus record migration, schema
change, DSCP profile update, retrieval gate change, or public-sync is
authorized by this EC-T1 GC-018.

---

## Problem Statement (source-verified)

### Current EC-02 gate behavior (runtime source)

Source: `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts`
Line 100-111:

```ts
for (const [ruleKey, ruleValue] of Object.entries(profile.boundaryRules)) {
  if (ruleValue.startsWith("BLOCKED") || ruleValue === "PROHIBITED") {
    return { ... blocked: true, ... };
  }
}
```

`boundaryRules` type: `Record<string, string>` (line 46).

Current value in all 6 PolicyLocal T11 candidate records:
`"ec02Gate": "BLOCKED_UNTIL_2026-07-01"`
Source: external operator workspace
`D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-t11-candidate-manifest.json`
SHA256:
`023F1276092756232949662E9BE6E635D545AB22B2BD19284F11F82789C7FD1A`

Current behavior: any `boundaryRules` value starting with `"BLOCKED"` blocks
profile application for the entire artifact. This is a flat date block -- it
applies equally to content queries (SUMMARY_WITH_SOURCE) and applicability
queries (ESCALATE_OR_ABSTAIN). The two query classes are not distinguished.

### Current response boundary contract

Source: `docs/reference/CVF_LPCI_RESPONSE_BOUNDARY_ENFORCEMENT_CONTRACT_2026-06-04.md`
Contract version: `policylocal.boundaryContract.t7.v1`

EC-02 entry (line 72-80):
```json
{
  "id": "EC-02",
  "trigger": "current_applicability_before_effective_date",
  "requiredAnswerClass": "ESCALATE_OR_ABSTAIN",
  "expiresWhen": "effectiveDate reached AND freshnessStatus transitions to current"
}
```

The contract already distinguishes EC-02 trigger as
`current_applicability_before_effective_date` -- content queries are not
named as a trigger. But the runtime gate at `dscp.domain.profile.contract.ts`
line 102 does not read the contract; it reads `boundaryRules` values directly.
The contract and the runtime gate are not wired together. This is the core
gap EC-T1 authorizes remedying.

### `QUERY_CLASS_GATED` runtime status

Source: grep across all EXTENSIONS/ TypeScript and JSON source.
Result: NOT FOUND in any EXTENSIONS source file.
The token `QUERY_CLASS_GATED` exists only in the roadmap proposal at
`docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md`.
It is a proposed token, not a runtime claim.

---

## Scope Boundary

In scope for EC-T1:

- Governance decision record establishing `documentStatus` as a CVF-layer
  concept applicable to any domain with promulgation/effective date split.
- Operator decisions on four open roadmap questions (named below).
- Authorization boundary for EC-T2: what the contract amendment must contain.
- Authorization boundary for EC-T3: corpus record schema fields required.
- Source verification table for all referenced symbols, contracts, and schema
  owners.

Out of scope for EC-T1:

- Any runtime source change.
- Any corpus record field addition or migration.
- Any DSCP domain profile `ec02Gate` value change.
- Any checker, test, or machine-gate addition.
- Any public-sync or public documentation update.
- EC-T2 through EC-T6 implementation.
- EX-lane work (EX-T3 through EX-T6).

---

## Decision

EC-T1 is authorized as a governance decision record under operator direction
on 2026-06-11. The four operator decision gates (D-01 through D-04) below
must be filled in by Codex before this GC-018 closes. No implementation
dispatch follows EC-T1 -- the next dispatch is EC-T2 (contract amendment)
after D-01 through D-04 are recorded and this baseline is
`CLOSED_PASS_BOUNDED`.

Predecessor evidence:

- `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md`
  (Part B, Proposed Tranches section) -- EC-T1 governance decision record
  listed as first EC lane tranche.
- `docs/reference/CVF_LPCI_RESPONSE_BOUNDARY_ENFORCEMENT_CONTRACT_2026-06-04.md`
  -- current EC-02 contract this decision record targets for EC-T2 amendment.
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts`
  -- current runtime `boundaryRules` gate logic this decision record
  authorizes changing at EC-T5.

---

## Operator Decision Gates (required before EC-T1 can close)

Codex must record operator decisions on the following four open questions
from the roadmap before this GC-018 transitions to `CLOSED_PASS_BOUNDED`.

### D-01 Field naming: `documentStatus` vs `legalStatus`

Proposed: `documentStatus` (language-agnostic, applies to standards, policy,
law, corporate docs). Prior draft used `legalStatus`. Name is breaking once
downstream corpus records are written.

**Decision required:** accept `documentStatus` OR rename to `legalStatus`
OR propose alternative name.

Decision: ACCEPTED -- `documentStatus`.

Rationale: CVF-layer concept applies to EU directives, ISO standards,
corporate policies, and Vietnamese legislation equally. `legalStatus`
would create incorrect coupling to law-domain-only semantics. Name is
not yet breaking for EC-02 lifecycle corpus records because no downstream
EC-02 corpus records have been written. A pre-existing DSCP-T10
company-docs test fixture already uses `domainFacetFields.documentStatus:
"approved"` as generic metadata; EC-T2 and EC-T3 must treat that as a
collision to isolate, not as evidence that the EC-02 lifecycle enum already
exists. All EC-T2 through EC-T6 artifacts must use `documentStatus` as the
canonical EC-02 lifecycle field name, with lifecycle-specific gating.
Recorded 2026-06-11 under operator delegation to Claude audit.

### D-02 `QUERY_CLASS_GATED` token: accept, rename, or reject

The proposed token replaces `"BLOCKED_UNTIL_2026-07-01"` as the
`ec02Gate` value in `boundaryRules`. Runtime consequence:
`dscp.domain.profile.contract.ts` line 102 would NOT match
`QUERY_CLASS_GATED` as a blocking value (does not start with `"BLOCKED"`),
so the profile application would NOT be blocked.

This means EC-T5 (DSCP gate value update) must also update the runtime gate
logic at line 102 to handle `QUERY_CLASS_GATED` by routing to the
query-class matrix rather than blocking wholesale.

**Decision required:** accept `QUERY_CLASS_GATED` as the canonical token
name, OR propose alternative (e.g. `QUERY_CLASS_MATRIX`, `SELECTIVE_GATE`).

Decision: ACCEPTED -- `QUERY_CLASS_GATED`.

Rationale: Self-describing and consistent with the contract's own
`query_class` / `escalateConditions` vocabulary. No alternative name
communicates the query-class dimension more clearly. Runtime consequence
confirmed: EC-T5 must extend `dscp.domain.profile.contract.ts` line 102
gate logic to handle `QUERY_CLASS_GATED` as a routing signal (not a flat
block) -- this is a required EC-T5 design constraint, not an EC-T1 or
EC-T2 action. Recorded 2026-06-11 under operator delegation to
Claude audit.

### D-03 `documentStatus` for non-regulatory domains

Technical project docs and company docs do not typically have
`promulgationDate`/`effectiveDate`. Should:
- (A) `documentStatus` default to `IN_FORCE` for non-regulatory domain
  families, or
- (B) non-regulatory records omit the field entirely and have no EC-02
  check.

**Decision required:** select A or B, or propose alternative.

Decision: OPTION B -- non-regulatory records omit `documentStatus`,
`promulgationDate`, and `effectiveDate` entirely. EC-02 gate does not
fire for these records.

Rationale: Adding `documentStatus=IN_FORCE` as a default to technical
project docs and company docs creates schema noise with no governance
value and risks future agents treating the field as a regulatory signal.
Only domain families with a known promulgation/effective-date lifecycle
(e.g. `VN_NATIONAL_ASSEMBLY`, EU directive families, ISO standard
families) carry `documentStatus`. EC-T3 schema update must include a
`supportsDocumentStatus: boolean` flag at domain profile level to gate
field presence. Existing non-regulatory test-fixture usage of
`domainFacetFields.documentStatus: "approved"` must not activate EC-02
lifecycle behavior and must be renamed, removed, or explicitly isolated in
EC-T3 if it would confuse the schema. Recorded 2026-06-11 under operator
delegation to Claude audit.

### D-04 EC-02 2026-07-01 date boundary status

Current EC-02 hard boundary `BLOCKED_UNTIL_2026-07-01` remains active.
Today is 2026-06-11 -- 20 days before the boundary date.

EC-T1 does NOT remove or modify this boundary. EC-T3 (corpus record schema)
and EC-T4 (per-project metadata backfill) are required before EC-T5 can
update the DSCP profile gate values. The boundary must not be relaxed in
any intermediate EC tranche.

**Decision required:** confirm EC-02 boundary remains unchanged through
EC-T4 inclusive, OR record any exception. No exception is expected.

Decision: CONFIRMED -- EC-02 boundary `BLOCKED_UNTIL_2026-07-01` remains
active and unchanged through EC-T4 inclusive. No exception recorded.

Consequence: `ec02Gate: "BLOCKED_UNTIL_2026-07-01"` in all 6 PolicyLocal
T11 candidate records is untouched until EC-T5. EC-T3 adds
`documentStatus=PROMULGATED` to these records alongside the existing
`ec02Gate` value -- the two fields coexist until EC-T5 replaces
`BLOCKED_UNTIL_2026-07-01` with `QUERY_CLASS_GATED`. No record may
receive `documentStatus=IN_FORCE` before 2026-07-01. Recorded 2026-06-11
under operator delegation to Claude audit.

---

## Evidence

All source-verification evidence gathered before this GC-018 was authored.
No source item below is accepted without direct grep or file evidence at
HEAD `557d4f73` before authoring.

Key findings:

- `boundaryRules` type is `Record<string, string>` -- flat string values.
- Runtime block check: `ruleValue.startsWith("BLOCKED")` at line 102. This
  means `QUERY_CLASS_GATED` would NOT block profile application under current
  runtime logic. EC-T5 must update the runtime gate to handle the new token.
- `QUERY_CLASS_GATED` and `promulgationDate` are NOT present in any
  EXTENSIONS TypeScript/JSON source -- they are proposed by this decision
  record only.
- `documentStatus` is present once in
  `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.domain.profile.contract.test.ts`
  line 70 as `domainFacetFields.documentStatus: "approved"` in a
  company-docs test fixture. This is not the EC-02 lifecycle enum proposed
  here and must be treated as a collision/isolation requirement for EC-T2
  and EC-T3, not as existing runtime support.
- All 6 PolicyLocal T11 candidate records carry `"ec02Gate":
  "BLOCKED_UNTIL_2026-07-01"` in the manifest JSON.
- EC-02 contract distinguishes `current_applicability_before_effective_date`
  as the trigger -- but the runtime gate does not read the contract; it reads
  `boundaryRules` directly. Contract and runtime are currently misaligned.

---

## Source Verification Table

| Symbol / path | File | Verified line / section |
| --- | --- | --- |
| `boundaryRules: Record<string, string>` | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | line 46 |
| `ruleValue.startsWith("BLOCKED")` gate | same | line 102 |
| `ec02Gate: "BLOCKED_UNTIL_2026-07-01"` (6 records) | external operator workspace: `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-t11-candidate-manifest.json`; SHA256 `023F1276092756232949662E9BE6E635D545AB22B2BD19284F11F82789C7FD1A` | lines 30, 57, 85, 113, 140, 168 |
| `EC-02` escalation condition | `docs/reference/CVF_LPCI_RESPONSE_BOUNDARY_ENFORCEMENT_CONTRACT_2026-06-04.md` | line 72-80 |
| `QUERY_CLASS_GATED` token | grep across all EXTENSIONS/ TS + JSON | NOT FOUND (proposed only; exists in roadmap doc only) |
| `documentStatus` existing non-EC-02 fixture key | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.domain.profile.contract.test.ts` | line 70: `domainFacetFields.documentStatus: "approved"` |
| EC-02 lifecycle `documentStatus` enum values | grep across all EXTENSIONS/ TS + JSON | NOT FOUND for `PROMULGATED`, `IN_FORCE`, `STATUS_UNKNOWN` enum usage |
| `promulgationDate` field | grep across all EXTENSIONS/ TS + JSON | NOT FOUND (proposed only) |
| `effectiveDate` field in contract | `docs/reference/CVF_LPCI_RESPONSE_BOUNDARY_ENFORCEMENT_CONTRACT_2026-06-04.md` | line 104, 130 |
| Roadmap authority | `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md` | Part B, Proposed Tranches section |
| EC-01/EC-03/EC-04 escalation conditions | `docs/reference/CVF_LPCI_RESPONSE_BOUNDARY_ENFORCEMENT_CONTRACT_2026-06-04.md` | line 63-98 |
| `notYetInForceDisclosure` mechanism | same | line 104-105 |
| Domain profile apply function | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | line 92-165 |

---

## EC-T2 Authorization Boundary (what the contract amendment must contain)

When EC-T1 is closed (D-01 through D-04 recorded), EC-T2 is authorized
to produce:

1. Updated `docs/reference/CVF_LPCI_RESPONSE_BOUNDARY_ENFORCEMENT_CONTRACT_*`
   (new version, references prior contract version):
   - EC-02 trigger matrix split by `documentStatus` x query class.
   - Collision note: pre-existing
     `domainFacetFields.documentStatus: "approved"` in the company-docs
     DSCP-T10 test fixture is not EC-02 lifecycle support.
   - `notYetInForceDisclosure` template mechanism (i18n-ready, locale from
     domain profile, no hardcoded language strings in pipeline code).
   - `documentStatus` listed as a required corpus record field checked at
     retrieval time.
   - `QUERY_CLASS_GATED` (or accepted-name token) listed as the authorized
     `ec02Gate` value that enables query-class routing.

2. Machine-readable gate semantics artifact:
   `docs/reference/CVF_EC02_GATE_SEMANTICS_*.json`
   This file must exist and be checker-verifiable before EC-T5. Prose alone
   is not dispatch-ready evidence for runtime gate behavior.

EC-T2 does NOT update any runtime TypeScript source. It updates only the
contract document and the machine-readable semantics JSON.

---

## EC-T3 Authorization Boundary (corpus record schema)

EC-T3 (authorized after EC-T2 closes) adds to the corpus record schema:

- `promulgationDate: string | null` -- ISO 8601 or null
- `effectiveDate: string | null` -- ISO 8601 or null
- `documentStatus: "PROMULGATED" | "IN_FORCE" | "STATUS_UNKNOWN"` -- computed
- `supportsDocumentStatus: boolean` or equivalent domain-profile guard so
  non-regulatory records do not inherit EC-02 lifecycle fields from generic
  metadata keys.
- Migration rule: all existing records with `BLOCKED_UNTIL_*` value receive
  `documentStatus=PROMULGATED` (not `IN_FORCE`). No record may transition
  from `BLOCKED_*` to `IN_FORCE` without an operator-supplied `effectiveDate`
  that has actually passed.

EC-T3 does NOT change DSCP domain profile `ec02Gate` values. That is EC-T5.

---

## Forbidden Scope

The following must not appear in EC-T1 through EC-T4 artifacts:

- Any `ec02Gate` value change in DSCP domain profiles.
- Any retrieval layer gate change.
- Any runtime TypeScript source change.
- Any public-sync commit.
- Any relaxation of EC-01, EC-03, or EC-04 conditions.
- Any claim that current-law content is authoritative or legally current.
- Any `documentStatus=IN_FORCE` for records whose `effectiveDate` has not
  yet passed as of the current date.

---

## Acceptance Criteria For EC-T1 Closure

This GC-018 may transition from `PROPOSED` to `CLOSED_PASS_BOUNDED` only when:

1. Operator decisions D-01 through D-04 are recorded (Codex fills in above).
2. Source verification table is reviewed and all `NOT FOUND` tokens confirmed
   as genuinely new (not missing from grep scope).
3. EC-T2 authorization boundary is accepted as stated.
4. Pre-closure autorun gate passes:
   `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base f15bdac8 --head HEAD`
5. Reviewer-fast passes:
   `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast --serial`

There is no worker dispatch step for EC-T1. Codex fills in operator decisions,
reviews the source verification table, runs gates, updates status to
`CLOSED_PASS_BOUNDED`, and commits.

---

## Finding-To-Governance Learning Disposition

Defect class: `SOURCE_VERIFICATION_NEGATIVE_SEARCH_SCOPE_GAP`

Learning lane: `governance/control-plane learning`

Finding: the initial EC-T1 baseline claimed `documentStatus` was NOT FOUND in
EXTENSIONS TypeScript/JSON. Codex closure review found one existing
`domainFacetFields.documentStatus: "approved"` fixture in
`EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.domain.profile.contract.test.ts`
line 70.

Disposition: `MACHINE_CHECK_CANDIDATE`

Next control action: future source-verification work orders and GC-018 packets
that claim a token is NOT FOUND must record the search roots and must classify
same-token collisions separately from the proposed runtime/schema meaning.
EC-T2 must carry forward the company-docs fixture collision as a contract
constraint.

---

## Claim Boundary

This GC-018 establishes governance authorization and records operator decisions.
It does not prove runtime correctness, legal correctness, retrieval quality,
EC-02 enforcement efficacy, production readiness, public readiness, or any
claim beyond the decision record itself.

EC-02 hard boundary 2026-07-01 remains in force until EC-T5 closes with
operator-supplied `effectiveDate` evidence for each record.

---

## Downstream Dependency Chain

```
EC-T1 (this) -- decision record only
  -> EC-T2    -- contract amendment + machine semantics JSON
    -> EC-T3  -- corpus record schema update (documentStatus field)
      -> EC-T4 -- per-project metadata backfill (operator supplies dates)
        -> EC-T5 -- DSCP gate value update (ec02Gate token change + runtime gate logic)
          -> EC-T6 -- retrieval disclosure wire-in (i18n disclosure on PROMULGATED records)
```

EX lane (EX-T3 through EX-T6) is independent of EC lane and proceeds in
parallel under separate authorization.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: internal governance decision record; not public-synced.
