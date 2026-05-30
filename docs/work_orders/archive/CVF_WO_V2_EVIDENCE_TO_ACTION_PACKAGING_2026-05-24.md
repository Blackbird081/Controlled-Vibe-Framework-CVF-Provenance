# CVF Work Order: V2 Evidence-To-Action Packaging

Memory class: FULL_RECORD

Status: AUTHORIZED

docType: work_order

Date: 2026-05-24

Tranche: V2

Roadmap: `docs/roadmaps/CVF_VALUE_SCREENED_NEXT_TRANCHE_ROADMAP_2026-05-24.md`

---

## Purpose

Make existing CVF evidence receipts easier for non-coders to understand and
reuse by packaging them as a short action artifact.

## Scope / Target / Owner Boundary

Target:

- `ResultViewer.tsx`
- `ResultViewer.test.tsx`

Owner: Codex implementer.

Out of scope: receipt-envelope schema changes, benchmark engine changes,
provider/runtime changes, new export formats, public-sync claim expansion, or
production readiness claims.

## Authority Chain

- GC-018:
  `docs/baselines/CVF_GC018_V2_EVIDENCE_TO_ACTION_PACKAGING_2026-05-24.md`
- Roadmap:
  `docs/roadmaps/CVF_VALUE_SCREENED_NEXT_TRANCHE_ROADMAP_2026-05-24.md`

## Agent Roles

| Role | Responsibility |
| --- | --- |
| Product Reviewer | Confirm evidence text answers user handoff needs. |
| Implementer | Add action sections to existing export/copy path. |
| QA | Verify copy/export content and secret hygiene. |
| Governance Reviewer | Confirm no receipt schema expansion. |
| Release Manager | File closure and update session routing. |

## Required First Reads

- `docs/roadmaps/CVF_VALUE_SCREENED_NEXT_TRANCHE_ROADMAP_2026-05-24.md`
- `docs/reviews/CVF_S3_GOVERNANCE_BENCHMARK_PUBLIC_CLAIM_COMPLETION_2026-05-24.md`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ResultViewer.tsx`

## Pre-Flight Checks

- Confirm existing receipt fields remain unchanged.
- Confirm text is bounded for non-live evidence.
- Confirm no raw secret values are added to exports.

## Write Ownership

Allowed:

- ResultViewer receipt copy/export wording.
- ResultViewer focused tests.

Forbidden:

- receipt-envelope schema changes
- provider/runtime changes
- benchmark metric changes

## Work Plan

1. Preserve existing receipt field export.
2. Add "What happened", "Why this can be used", and "What to do next".
3. Keep wording bounded for non-live evidence.
4. Update tests.

## Execution Plan

1. Extend receipt export content with action sections.
2. Preserve existing receipt field list.
3. Update copy test for action sections and secret hygiene.

## Evidence Requirements

- Targeted ResultViewer test.
- Typecheck.
- Release gate after all V1/V2/V3 changes.

## Acceptance Criteria

- [ ] Copied receipt content includes action sections.
- [ ] Existing receipt fields remain present.
- [ ] Secret hygiene assertion remains passing.
- [ ] Targeted tests pass.

## Verification / Evidence

- ResultViewer targeted tests.
- cvf-web typecheck.
- Release gate after all V1/V2/V3 changes.

## Review Gate

Closure must confirm evidence wording improves handoff clarity without changing
the receipt contract.

## Operator Checkpoint

Operator authorized V1/V2/V3 processing in the 2026-05-24 session.

## Closure Checklist

- [ ] Action sections implemented.
- [ ] Raw receipt fields preserved.
- [ ] Tests passed.
- [ ] Closure review filed.
- [ ] Session routing updated.

## Return-To-Orchestrator Conditions

Return blocked if packaging requires a receipt-envelope schema change or a new
public benchmark claim.

## Claim / Final / Verification Boundary

V2 may claim clearer evidence-to-action packaging for existing ResultViewer
exports only. It must not claim new governance evidence semantics.
