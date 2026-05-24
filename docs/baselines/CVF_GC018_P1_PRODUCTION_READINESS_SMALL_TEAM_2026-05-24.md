# CVF GC-018 - P1: Production Readiness for Small Team / Non-Coder

Memory class: SUMMARY_RECORD

Status: OPEN

docType: baseline

Date: 2026-05-24

---

## Scope

Authorize a bounded P1 production readiness tranche targeted at non-coders,
solo developers, and small teams — CVF's declared addressable audience.

This is not enterprise SaaS readiness, not multi-tenant hosted GA, and not
broad provider stability. It is a narrow "can a non-coder get to a governed
execution receipt?" proof.

---

## Purpose

CVF v4.0.0 has a complete governed execution stack but the onboarding path
for non-coders and small teams is not documented or proven end-to-end. P1
closes that gap so the public catalog can make a bounded, honest production
readiness claim for the small team / non-coder persona.

---

## Source / Predecessor Evidence

- Post-AIF operational readiness matrix:
  `docs/reference/CVF_POST_AIF_OPERATIONAL_READINESS_MATRIX_2026-05-24.md`
- Public technical catalog:
  `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md` (public-sync)
- C5 hosted smoke (prior evidence):
  `docs/reviews/CVF_C2_C5_POST_AIF_CLAIM_GRADUATION_COMPLETION_2026-05-24.md`
- Roadmap: `docs/roadmaps/CVF_M1_M2_P1_NEXT_VALUE_ROADMAP_2026-05-24.md`

---

## Decision / Baseline / Proposed Tranche

Decision: execute one bounded P1 tranche assessing and improving the
non-coder/small-team production path.

Baseline: C5 proved the hosted `/api/execute` path is reachable under a signed
service token. P1 extends that to ask: can a non-coder user, without knowing
the API internals, reach a governed execution receipt via the web UI or guided
setup?

---

## Guardrails

- The claim is bounded to the non-coder/small-team persona path proven in this
  tranche. No enterprise, multi-tenant, or hosted SaaS claim is authorized.
- The end-to-end proof must use a real governed `/api/execute` call with a live
  receipt — not a mock.
- No raw API key, service token, or signed header may appear in any committed
  artifact. `rawSecretPrinted=false` enforced.
- The friction-point analysis must produce actionable work items, not just
  observations.
- Public catalog update is required before tranche close. Any new claim row
  must have a verified evidence path tested from the public-sync clone.
- This tranche runs in parallel with M2 and M1. No dependency on M2/M1.

---

## Pass Conditions

- Onboarding assessment complete: what must a non-coder do to get their first
  governed AI execution?
- Minimum setup doc: single page, non-coder language, covers template
  selection → governed execution → receipt.
- Top-3 friction points identified and closed (or explicitly deferred with
  reason).
- End-to-end proof: non-coder persona → template selection → governed
  `/api/execute` → receipt in hand, with live receipt evidence.
- Public catalog row updated with bounded small-team production readiness claim
  and verified evidence path.
- Governance review filed at:
  `docs/reviews/CVF_P1_PRODUCTION_READINESS_SMALL_TEAM_COMPLETION_2026-05-24.md`
- TypeScript check PASS on any modified files.

---

## Evidence / Verification

Required evidence before this baseline is closed:

- Onboarding assessment and minimum setup doc filed.
- Top-3 friction points each have a close or defer decision.
- End-to-end proof receipt: HTTP 200, `success=true`, `evidenceMode=live`,
  `rawSecretPrinted=false`.
- Public catalog row updated with bounded claim and verified evidence path from
  public-sync clone.
- Completion review filed at:
  `docs/reviews/CVF_P1_PRODUCTION_READINESS_SMALL_TEAM_COMPLETION_2026-05-24.md`

---

## Claim Boundary

P1 claims production readiness for the non-coder/small-team persona only, with
a proven end-to-end path and receipt evidence. It does not claim enterprise
SaaS readiness, multi-tenant hosted GA, broad provider stability, or broad
production stability beyond the narrow persona path proven.

---

## Disposition

Open. Closed by work order completion review.
