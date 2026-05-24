# GC-018: V1 Non-Coder First-Value Journey Hardening

Memory class: FULL_RECORD

Status: AUTHORIZED

docType: baseline

Date: 2026-05-24

---

## Purpose

Authorize a bounded V1 tranche after V3 diagnostic implementation so the
non-coder first-value journey does not hide failed live executions behind mock
fallback when CVF has a classified diagnostic.

## Scope / Target / Owner Boundary

Scope: user-visible first-value recovery state in the existing CVF Web
ProcessingScreen.

Target: small UI/workflow hardening only.

Owner: Codex implementer with reviewer, QA, governance, and release roles.

Out of scope: new templates, new provider behavior, new governance semantics,
new receipt envelope fields, memory reinjection, graph authority, hosted
readiness, production readiness, or freeze release.

## Depth Audit

Depth score: 9/10.

Rationale:

- V3 diagnostic contract is now the prerequisite for safe live-run recovery.
- The existing non-coder path can fall back to demo/mock output after a real
  execution failure, which is confusing and weakens first-value trust.
- A small UI change can improve value without expanding runtime semantics.

## Source / Predecessor Evidence

- V3 standard:
  `docs/reference/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`
- Value-screened roadmap:
  `docs/roadmaps/CVF_VALUE_SCREENED_NEXT_TRANCHE_ROADMAP_2026-05-24.md`
- Existing non-coder evidence/pack surfaces:
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ProcessingScreen.tsx`

## Authorized Change

- If `/api/execute` returns `success=false` with a V3 diagnostic, show the
  diagnostic and next action to the user.
- Do not fall back to mock output for a classified live execution failure.
- Preserve existing successful execution, receipt visibility, and pack export
  behavior.

## Decision / Baseline / Proposed Tranche

Decision: continue.

Baseline: V3 diagnostics are the required failure explanation surface.

Proposed tranche: V1 non-coder first-value journey hardening, bounded to
diagnostic recovery visibility and no-mock fallback for classified failures.

## Evidence Plan

- Focused ProcessingScreen tests.
- Existing ResultViewer/route diagnostic tests as support.
- Release gate after runtime/UI changes.

## Acceptance Criteria

- [ ] Classified live execution failures render a diagnostic panel.
- [ ] Diagnostic panel includes stage, class, retryability, userAction, and
      receipt/trace when present.
- [ ] Mock fallback is not used when a real diagnostic exists.
- [ ] Existing success path remains intact.

## Verification / Evidence

Closure must cite targeted tests and release gate result.

## Claim / Final / Verification Boundary

This GC-018 authorizes only first-value recovery clarity. It does not claim
stable provider operation, hosted readiness, production readiness, or a new
governance decision surface.
