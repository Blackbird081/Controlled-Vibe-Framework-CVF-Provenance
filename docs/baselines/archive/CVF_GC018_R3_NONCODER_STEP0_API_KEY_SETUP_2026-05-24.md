# CVF GC-018 - R3: Non-Coder Step 0 API-Key Setup

Memory class: SUMMARY_RECORD

Status: AUTHORIZED

docType: baseline

Date: 2026-05-24

---

## Scope

Authorize one documentation/onboarding tranche to close the P1 Step 0 gap:
how a non-coder or small-team operator configures the first provider key
without committing or exposing secrets.

---

## Purpose

P1 proved a first-receipt path after an operator had already configured live
provider access. R3 adds the missing precondition guide so the small-team path
is understandable from provider-key setup through first receipt.

---

## Source / Predecessor Evidence

- P1 completion:
  `docs/reviews/CVF_P1_PRODUCTION_READINESS_SMALL_TEAM_COMPLETION_2026-05-24.md`
- Existing first-receipt guide:
  `docs/guides/CVF_NON_CODER_SETUP_GUIDE_2026-05-24.md`
- R1/R2/P2 roadmap:
  `docs/roadmaps/CVF_R1_R2_P2_POST_M1_GAP_CLOSURE_ROADMAP_2026-05-24.md`
- Public repository boundary in root `AGENTS.md`.

---

## Decision / Baseline / Proposed Tranche

Decision: execute R3 as the renamed P2 Step 0 setup tranche. Public-safe docs
may be updated in public-sync after verifying the public repository remote.

Baseline: existing guide says an approved provider key must already be
configured. It does not explain how to configure the first key.

---

## Guardrails

- No raw key, service token, signed header, or real secret may be committed.
- Verification commands must print only boolean/masked readiness.
- Do not promise provider procurement, universal provider availability, hosted
  secret vaults, or enterprise credential management.
- Public-facing updates must be made from the public-sync clone only.

---

## Pass Conditions

- Step 0 setup guide filed.
- First-receipt guide links to Step 0.
- Secret hygiene scan passes.
- Public-sync guide/catalog updated if public claim changes.
- Public-sync paths verified.
- Completion review filed.

---

## Evidence / Verification

Required evidence:

- Step 0 guide path.
- Secret scan command result.
- Public-sync remote verification and Test-Path result if public docs change.
- Completion review:
  `docs/reviews/CVF_R3_NONCODER_STEP0_API_KEY_SETUP_COMPLETION_2026-05-24.md`

---

## Claim Boundary

R3 may claim a documented small-team provider-key setup path. It does not
claim automated onboarding, hosted credential management, provider account
availability, broad production readiness, or enterprise SaaS readiness.

