# CVF Work Order: S2 — Provider Soak Hardening

Memory class: FULL_RECORD

Status: WORK_ORDER_READY

docType: work_order

Date: 2026-05-24

Tranche: S2

Roadmap: `docs/roadmaps/CVF_S1_S2_S3_NEXT_VALUE_ROADMAP_2026-05-24.md`

---

## Purpose

Extend the provider repeatability proof from C4's 2-journey baseline to ≥5
journeys per provider (Alibaba, DeepSeek, OpenAI) with inter-journey cooldown,
failure classification, and partial-pass detection. Produce live receipts for
every journey and file a bounded soak completion review.

---

## Authority Chain

- GC-018: `docs/baselines/CVF_GC018_S2_PROVIDER_SOAK_HARDENING_2026-05-24.md`
- Roadmap: `docs/roadmaps/CVF_S1_S2_S3_NEXT_VALUE_ROADMAP_2026-05-24.md`
- C4 predecessor:
  `docs/reviews/CVF_C2_C5_POST_AIF_CLAIM_GRADUATION_COMPLETION_2026-05-24.md`
  (C4 evidence section)
- Existing probe:
  `scripts/run_post_phase2b_provider_stability_probe.mjs`

---

## Scope / Target / Owner Boundary

Target: provider stability probe scripts and completion evidence.

Owner: CVF provider stability and evidence surface.

Out of scope:

- Universal provider stability claim.
- SLA-level availability.
- Enterprise provider contracts.
- Any route, memory, or kernel surface change.
- OpenAI R2+ payloads (must use `cvfRiskLevel=R2` or lower per router cap).

---

## Agent Roles

| Role | Responsibility |
| --- | --- |
| Planner | Read C4 evidence and existing probe script before designing S2 run. |
| Implementer | Extend or create soak probe; run ≥5 journeys per provider. |
| QA | Verify live receipts for all journeys; check failure classification; confirm `rawSecretPrinted=false`. |
| Governance Reviewer | Confirm claim is bounded to exact N/N window only. |
| Release Manager | File completion review; commit. |

---

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `scripts/run_post_phase2b_provider_stability_probe.mjs` (existing C4 probe)
- `docs/reviews/CVF_C2_C5_POST_AIF_CLAIM_GRADUATION_COMPLETION_2026-05-24.md`
  (C4 evidence section for baseline)
- `docs/roadmaps/CVF_S1_S2_S3_NEXT_VALUE_ROADMAP_2026-05-24.md`

---

## Write Ownership

- `scripts/run_cvf_s2_provider_soak_probe.mjs` (new soak script, or extend
  existing probe — Codex decides based on reading existing script first)
- `docs/reviews/CVF_S2_PROVIDER_SOAK_HARDENING_COMPLETION_2026-05-24.md`
- `docs/roadmaps/CVF_S1_S2_S3_NEXT_VALUE_ROADMAP_2026-05-24.md` — update S2
  row to `CLOSED_PASS`.

---

## Pre-Flight Checks

- Confirm all three provider keys are available in local env:
  Alibaba (`DASHSCOPE_API_KEY` / `ALIBABA_API_KEY` / `CVF_BENCHMARK_ALIBABA_KEY`),
  DeepSeek (`DEEPSEEK_API_KEY`), OpenAI (`OPENAI_API_KEY`).
  Do not print key values.
- Confirm local web server or hosted `/api/execute` target is reachable.
- Read the existing C4 probe script to understand cooldown and receipt
  collection pattern before writing new code.

---

## Allowed / Forbidden Scope

Allowed:

- Run ≥5 journeys per provider with live keys.
- Inter-journey cooldown ≥1500ms.
- Failure classification for any failed journey (timeout, HTTP error, BLOCK,
  receipt missing, etc.).
- Partial-pass detection: `PARTIAL_PASS` if any journey fails.
- Collect live receipts (HTTP 200, `success=true`, `evidenceMode=live`,
  `rawSecretPrinted=false` per journey).
- Soak summary: total/pass/fail per provider.
- Extend existing probe script or create a new one — Codex decides.

Forbidden:

- Claiming universal provider stability.
- Running OpenAI with `cvfRiskLevel` above R2.
- Printing raw API keys or signed headers.
- Any route, memory, or kernel change.

---

## Execution Plan

1. Read required first reads.
2. Decide: extend `run_post_phase2b_provider_stability_probe.mjs` with
   `CVF_POST_PHASE2B_REPEATS=5` or create `run_cvf_s2_provider_soak_probe.mjs`.
3. Run soak: `CVF_POST_PHASE2B_PROVIDERS=alibaba,deepseek,openai`,
   `CVF_POST_PHASE2B_REPEATS=5` (or equivalent), cooldown ≥1500ms.
4. Collect receipts for all 15 journeys.
5. Classify any failures.
6. Record soak summary: total/pass/fail per provider.
7. File completion review with bounded claim language (exact `N/N` proven).
8. Commit.

---

## Evidence Requirements

- Soak run log with receipts for all journeys.
- Per-provider pass/fail summary: `Alibaba N/N`, `DeepSeek N/N`, `OpenAI N/N`.
- `rawSecretPrinted=false` confirmed per journey.
- Failure classification for any failed journey (or "none" if all pass).
- Completion review filed with exact N/N claim language.

---

## Acceptance Criteria

- [ ] ≥5 journeys per provider run with live keys.
- [ ] Live receipts for all journeys.
- [ ] `rawSecretPrinted=false` confirmed per journey.
- [ ] Failure classification present (or "none").
- [ ] Soak summary: total/pass/fail per provider.
- [ ] Completion review filed with bounded exact N/N claim.
- [ ] No raw key in any committed artifact.

---

## Review Gate

The completion review must confirm:

- Exact journey count proven (N/N format).
- Claim language does not assert universal stability.
- `rawSecretPrinted=false` for every journey.
- Failure classification present for any failure.
- OpenAI journeys used `cvfRiskLevel=R2` or lower.

---

## Operator Checkpoint

Operator authorized S2 on 2026-05-24. All three provider keys are available
locally.

Codex must self-execute and return the final result after tranche completion.

---

## Closure Checklist

- [ ] Soak run completed.
- [ ] Live receipts collected for all journeys.
- [ ] Soak summary recorded.
- [ ] Failure classification present.
- [ ] Completion review filed and committed.
- [ ] No raw key in any artifact.

---

## Return-To-Orchestrator Conditions

Return blocked if: any provider key is missing, all journeys for a provider
fail, or `rawSecretPrinted=true` in any receipt.

---

## Tasks

| Task | Status | Output |
| --- | --- | --- |
| Read C4 probe + evidence | PENDING | Design decision noted. |
| Soak run (≥5 per provider) | PENDING | 15+ live receipts. |
| Failure classification | PENDING | Per-journey reason or "none". |
| Soak summary | PENDING | Total/pass/fail per provider. |
| Completion review | PENDING | Filed with exact N/N claim. |

---

## Claim Boundary

S2 claims a bounded N-journey-per-provider soak window (exact N per evidence)
for Alibaba, DeepSeek, and OpenAI. It does not claim universal stability,
SLA-level availability, or enterprise provider guarantees.
