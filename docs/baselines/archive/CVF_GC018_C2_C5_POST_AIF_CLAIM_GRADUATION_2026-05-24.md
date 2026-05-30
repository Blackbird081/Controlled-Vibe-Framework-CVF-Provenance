# CVF GC-018 - C2-C5 Post-AIF Claim Graduation

Memory class: SUMMARY_RECORD

Status: CLOSED_PASS

docType: baseline

Date: 2026-05-24

---

## Scope

Authorize one bounded implementation tranche for the remaining Post-AIF claim
graduation items:

- C2 live memory reinjection;
- C3 graph authority;
- C4 broad provider stability;
- C5 hosted/production readiness smoke.

This GC-018 supersedes the earlier "next tranche required" posture for C2-C5
only within the pass conditions already listed in
`docs/roadmaps/CVF_POST_AIF_CLAIM_GRADUATION_ROADMAP_2026-05-24.md`.

---

## Purpose

Provide the governing baseline for a bounded C2-C5 implementation tranche.

---

## Source / Predecessor Evidence

- C1 claim-graduation roadmap:
  `docs/roadmaps/CVF_POST_AIF_CLAIM_GRADUATION_ROADMAP_2026-05-24.md`
- C1 public preview completion:
  `docs/reviews/CVF_C1_PUBLIC_AIF_PREVIEW_RUNTIME_AVAILABILITY_COMPLETION_2026-05-24.md`
- Post-AIF operational readiness matrix:
  `docs/reference/CVF_POST_AIF_OPERATIONAL_READINESS_MATRIX_2026-05-24.md`

---

## Decision / Baseline / Proposed Tranche

Decision: execute one bounded C2-C5 tranche in private provenance.

Baseline: C2-C5 were previously unclaimed and required fresh GC-018/work order.

Proposed tranche: implement the narrow runtime/probe contracts needed to close
only the explicit pass conditions below.

---

## Guardrails

- Memory reinjection must be route-level opt-in, summary-only, policy-gated,
  and auditable by receipt.
- Raw memory, secret memory, disputed memory, expired memory, and
  low-provenance memory must not enter the provider prompt.
- Graph evidence may authorize bounded context inclusion only after governance
  policy allows execution; it must not become approval authority.
- Provider stability may be claimed only as a bounded tri-provider repeatability
  window, not universal provider stability.
- Hosted readiness may be claimed only as a bounded protected-workflow smoke,
  not full SaaS/GA production readiness.
- Mandatory release-gate proof must use live provider execution.

---

## Pass Conditions

- C2: helper and route tests for allow/deny/exclusion plus one live provider
  `/api/execute` receipt proving injected memory ids.
- C3: deterministic graph-authority gate with thresholds, receipt, allow/deny
  tests, and policy-dominance proof.
- C4: live Alibaba, DeepSeek, and OpenAI matrix with at least two journeys per
  provider, cooldown, live receipts, and failure classification.
- C5: signed hosted protected-workflow smoke with live receipt, secrets/auth
  posture, observability identifiers, rollback/incident boundary, and release
  gate PASS.

---

## Evidence / Verification

Evidence is recorded in:

- `docs/reviews/CVF_C2_C5_POST_AIF_CLAIM_GRADUATION_COMPLETION_2026-05-24.md`
- `docs/reviews/CVF_C2_C5_POST_AIF_CLAIM_GRADUATION_EVIDENCE_2026-05-24.json`

Required verification:

- C2 unit/route tests and live provider receipt.
- C3 graph authority tests and TypeScript check.
- C4 live tri-provider matrix.
- C5 hosted signed smoke.
- Mandatory release gate PASS.

---

## Claim Boundary

Final claim is bounded to C2-C5 pass evidence only. This baseline does not
authorize durable memory, autonomous reinjection, graph approval authority,
universal provider stability, hosted SaaS/GA readiness, full production
readiness, Maika proof, or freeze release.

---

## Disposition

Closed by `docs/reviews/CVF_C2_C5_POST_AIF_CLAIM_GRADUATION_COMPLETION_2026-05-24.md`.
