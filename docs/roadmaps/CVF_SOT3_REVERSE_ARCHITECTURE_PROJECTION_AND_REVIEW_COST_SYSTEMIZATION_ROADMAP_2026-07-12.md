# CVF SOT3 Reverse Architecture Projection And Review Cost Systemization Roadmap

Memory class: FULL_RECORD

Status: PROPOSED

Date: 2026-07-12

Roadmap ID: SOT3-RAP-RCS

## Purpose

Close two governance gaps learned during SOT3-T2 without widening into SOT3
runtime implementation:

1. project reviewer-accepted SOT3 architecture facts back into the editable
   as-built Catalog and system-chain GAP sources;
2. decide, only after projection closure, which review-cost and diminishing-
   return controls merit machine enforcement.

## Target / Source

Primary accepted source is
`docs/reviews/CVF_SOT3_T2_COMPLETION_REVIEW_2026-07-12.md` at material commit
`9c7b05b40`. Shared learning sources are ADIF-0026 and ADIF-0027 at commit
`b054829a7`. Current projection owners are the compact JSON source layouts
under the as-built Catalog and system-chain GAP families.

## Scope / Methodology

The roadmap uses two dependency-ordered tranches. T0 performs documentation
and generated-aggregate projection only. T1 is a separate checker-decision
tranche and remains held until T0 review acceptance.

## Authorization / Decision

Operator authorized roadmap and work-order creation after clean SOT3-T2
closure. Decision: release T0 packet authoring and keep T1 held.

## Non-Goals

- no SOT3 runtime or product implementation;
- no public export;
- no semantic-value auto-judgment checker;
- no changes to Catalog/GAP schema, generator, checker, or hooks in T0.

## Design Control Gate

T0 must preserve compact-source authority, generated-aggregate discipline,
accepted-evidence citations, pending-versus-as-built separation, and the
existing TKG-T1 owner boundary.

## Findings / Position

- SOT3-T2 is accepted as `CONTRACT_ONLY`, not as runtime capability.
- Independent Refinery, Truth Kernel runtime, and post-Kernel Truth Flow remain
  owner/runtime candidates or gaps, not as-built implementations.
- Five retained competing shapes remain `REJECTED_COMPETING_SHAPE` evidence.
- Review-cost telemetry is valuable, but semantic root-cause/value judgment
  cannot be honestly claimed as fully machine-checkable.

## Tranche Plan

| Tranche | Objective | Outputs | Status |
|---|---|---|---|
| SOT3-RAP-T0 | Reverse-project accepted SOT3 contract/candidate/gap facts into Catalog/GAP source entries, README summaries, and regenerated aggregates | bounded Catalog entries; GAP entries; refreshed README/index/aggregate; worker return | WORK_ORDER_READY |
| SOT3-RCS-T1 | Decide and, only if justified, implement narrow shape enforcement for review-cost telemetry and reverse-projection presence | fresh GC-018, source-verified checker decision, tests if authorized | HOLD_UNTIL_T0_PASS |

## Work Plan

1. Dispatch and review T0 reverse projection.
2. Commit T0 material and continuity separately.
3. Recompute value/cost evidence from T0.
4. Author T1 only if a narrow machine-check candidate remains justified.

## Verification / Evidence

T0 evidence must include schema validation, generator output, drift-checker
PASS, exact diff/status, reviewer semantic audit, and split committed ranges.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_roadmap_closure_freshness.py` |
| literalTokensReviewed | PROPOSED; WORK_ORDER_READY; HOLD_UNTIL_T0_PASS; Public Export Disposition |
| gateRunPurpose | confirm author-derived roadmap structure and provide dispatch evidence |
| claimBoundary | roadmap gates do not authorize implementation |

## T0 Projection Set

| Accepted SOT3 item | Claim class | Required projection |
|---|---|---|
| SOT three-layer contract family | CONTRACT_ONLY | Catalog interface/module-boundary entry citing accepted T2 |
| independent CVF Refinery | OWNER_CANDIDATE | GAP entry; no runtime owner claim |
| Truth Kernel runtime | RUNTIME_CANDIDATE | GAP entry; retain existing truth-foundation doctrine owner |
| post-Kernel Truth Flow | OWNER_CANDIDATE | GAP entry; no runtime owner claim |
| eight inter-layer contracts | CONTRACT_ONLY | Catalog interface entry or bounded grouped entry |
| five competing retained shapes | REJECTED_COMPETING_SHAPE | exclusion evidence in projection claim boundary; no imported runtime entry |

## Acceptance Criteria

- Every T0 projection cites reviewer-accepted SOT3 evidence.
- No entry claims Refinery, Kernel runtime, or Flow runtime exists.
- Catalog and GAP compact entries validate against the current schema.
- Both generated aggregates reproduce from compact sources.
- Catalog and GAP README summaries name every new stable ID.
- Existing TKG-T1 truth-foundation ownership is enriched, not duplicated.
- T1 remains held until a T0 completion review is accepted.

## Fail Conditions

- Pending or candidate evidence is labeled `AS_BUILT`.
- A generated aggregate is edited without its compact source.
- SOT3 runtime/schema/test/package behavior is claimed or implemented.
- A new Truth Foundation doctrine owner duplicates the existing owner.
- T1 checker implementation is mixed into T0.
- Projection omits a required stable ID from the human front door.

## Risk / Corrective Action

| Risk | Corrective action |
|---|---|
| contract evidence is misread as runtime proof | use explicit `CONTRACT_ONLY` and candidate claim boundaries |
| catalog becomes a speculative design registry | keep candidate/gap facts in bounded GAP entries and cite accepted evidence |
| review-cost checker overclaims semantics | T1 may enforce presence/count fields only; semantic value remains reviewer-owned |
| generated data drifts | edit compact sources, run generator, then drift checker |

## Reverse Architecture Projection

This roadmap is the separately authorized projection route recorded by the
SOT3-T2 completion review. Its own projection disposition is
`NOT_APPLICABLE_WITH_REASON`: it dispatches the projection rather than adding
another architecture capability.

## Implementation Boundary

T0 authorizes documentation/reference JSON source entries and generated
Catalog/GAP outputs only. SOT3 runtime, schemas, tests, packages, provider/live,
Web, public-sync, and product implementation remain `NOT_AUTHORIZED`.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance architecture projection and governance planning.

## Claim Boundary

This roadmap authorizes packet creation and, after dispatch, bounded T0
projection. It does not itself change Catalog/GAP state or authorize T1.
