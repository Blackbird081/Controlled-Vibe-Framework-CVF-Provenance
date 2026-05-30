# GC-018: V2 Evidence-To-Action Packaging

Memory class: FULL_RECORD

Status: AUTHORIZED

docType: baseline

Date: 2026-05-24

---

## Purpose

Authorize a bounded V2 tranche that turns existing evidence receipts into a
clear "what happened / why this can be used / what to do next" artifact for
non-coder handoff and export.

## Scope / Target / Owner Boundary

Scope: existing ResultViewer evidence receipt export and copy path.

Target: user-facing evidence explanation only.

Owner: Codex implementer.

Out of scope: receipt-envelope schema expansion, new benchmark metrics, new
provider behavior, new governance semantics, memory reinjection, graph
authority, hosted readiness, production readiness, or public claim expansion.

## Depth Audit

Depth score: 8/10.

Rationale:

- S3 metric clarity showed raw evidence can mislead readers without
  call-level explanation.
- Non-coders need evidence they can reuse, not only raw receipt fields.
- The smallest useful change is to enrich existing export/copy content.

## Source / Predecessor Evidence

- S3 metric-clarity review:
  `docs/reviews/CVF_S3_GOVERNANCE_BENCHMARK_PUBLIC_CLAIM_COMPLETION_2026-05-24.md`
- Value-screened roadmap:
  `docs/roadmaps/CVF_VALUE_SCREENED_NEXT_TRANCHE_ROADMAP_2026-05-24.md`
- Existing evidence export surface:
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ResultViewer.tsx`

## Authorized Change

- Add action-oriented evidence sections to receipt export/copy content.
- Preserve existing raw receipt fields.
- Preserve secret hygiene.

## Decision / Baseline / Proposed Tranche

Decision: continue.

Baseline: receipt fields exist but need action-oriented framing for non-coder
handoff.

Proposed tranche: V2 evidence-to-action packaging, bounded to ResultViewer
copy/export content.

## Evidence Plan

- ResultViewer targeted tests.
- Existing export/copy assertions.
- Release gate after runtime/UI changes.

## Acceptance Criteria

- [ ] Evidence export includes "What happened".
- [ ] Evidence export includes "Why this can be used".
- [ ] Evidence export includes "What to do next".
- [ ] Raw provider keys remain absent.

## Verification / Evidence

Closure must cite targeted tests and release gate result.

## Claim / Final / Verification Boundary

This GC-018 authorizes evidence explanation only. It does not create a new
receipt contract or public benchmark certification claim.
