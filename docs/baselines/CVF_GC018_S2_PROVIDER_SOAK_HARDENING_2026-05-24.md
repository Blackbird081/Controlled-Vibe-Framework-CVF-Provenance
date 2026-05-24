# CVF GC-018 - S2: Provider Soak Hardening

Memory class: SUMMARY_RECORD

Status: OPEN

docType: baseline

Date: 2026-05-24

---

## Scope

Authorize one bounded S2 soak tranche extending the provider repeatability
window from C4's 2-journey baseline to ≥5 journeys per provider across
Alibaba, DeepSeek, and OpenAI.

---

## Purpose

C4 proved a narrow 6-journey window (2 per provider). The claim is deliberately
bounded. S2 extends the soak to a longer per-provider window to support a
stronger — but still bounded — repeatability claim without asserting universal
stability.

---

## Source / Predecessor Evidence

- C4 completion: `docs/reviews/CVF_C2_C5_POST_AIF_CLAIM_GRADUATION_COMPLETION_2026-05-24.md`
  (C4 evidence section)
- Existing probe script:
  `scripts/run_post_phase2b_provider_stability_probe.mjs`
- Roadmap: `docs/roadmaps/CVF_S1_S2_S3_NEXT_VALUE_ROADMAP_2026-05-24.md`

---

## Decision / Baseline / Proposed Tranche

Decision: execute one bounded S2 soak tranche with ≥5 journeys per provider.

Baseline: C4 proved 2/2 per provider. S2 does not replace C4; it adds a longer
soak window on top.

Proposed tranche: extend or create a soak probe script running at least 5
journeys per provider with inter-journey cooldown, partial-pass detection, and
failure classification. Record live receipts for every journey.

---

## Guardrails

- Soak must use live keys loaded from approved local env files. No raw key
  printed or committed.
- Inter-journey cooldown must be preserved (minimum 1500ms, matching C4
  baseline).
- Failure classification required: each failed journey must record the failure
  reason (timeout, HTTP error, policy block, etc.).
- Partial-pass detection: a run with ≥1 failure is `PARTIAL_PASS`, not `PASS`.
- Claim must state the exact journey count proven (e.g., `15/15`) — not
  "unlimited stability" or "universal provider stability".
- OpenAI journeys must use `cvfRiskLevel=R2` or lower (router cap).

---

## Pass Conditions

- ≥5 journeys per provider run with live keys.
- Live receipts for all journeys (HTTP 200, `success=true`, `evidenceMode=live`,
  `rawSecretPrinted=false` per journey).
- Failure classification recorded for any failed journey.
- Soak summary: total/pass/fail per provider.
- Completion review filed with bounded claim language (exact N/N window).

---

## Evidence / Verification

Required evidence:

- Soak probe script run log with receipts.
- Per-provider pass/fail summary.
- Completion review: `docs/reviews/CVF_S2_PROVIDER_SOAK_HARDENING_COMPLETION_2026-05-24.md`

---

## Claim Boundary

S2 claims a bounded N-journey-per-provider soak window (exact N per evidence).
It does not claim universal provider stability, SLA-level availability, broad
production reliability, or enterprise provider contracts.

---

## Disposition

Open. Closed by work order completion review.
