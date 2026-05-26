# CVF Post Publicization Provider Stability Hardening Roadmap

Memory class: SUMMARY_RECORD

Status: CLOSED_PROVIDER_STABILITY_HARDENING_BOUNDED

docType: roadmap

Date: 2026-05-21

---

## Purpose

Define the next bounded roadmap after post-Phase 2.B publicization/readiness
closed. The goal is to strengthen provider-stability evidence one step beyond
the existing `4/4` narrow repeatability result without claiming broad provider
stability or changing provider runtime behavior.

---

## Authority Chain

- Active state:
  `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- Post-Phase 2.B publicization/readiness completion:
  `docs/reviews/CVF_POST_PHASE_2B_PUBLICIZATION_READINESS_COMPLETION_2026-05-21.md`
- Product readiness assessment:
  `docs/assessments/CVF_POST_PHASE_2B_PRODUCT_READINESS_ASSESSMENT_2026-05-21.md`
- Existing provider repeatability probe:
  `scripts/run_post_phase2b_provider_stability_probe.mjs`
- Public repository boundary: `AGENTS.md`

---

## Authorization / Decision

Operator instruction on 2026-05-21: continue the next roadmap.

Decision: proceed only as a bounded provider-stability hardening tranche.

This roadmap does not authorize broad provider stability, all-provider claims,
provider method expansion, hosted/product readiness claims, persistence or
database implementation, Maika child-data/photo/vision proof, kernel-owner
replacement, or global freeze lift.

---

## Scope

In scope:

- Re-run the existing governed `/api/execute` provider repeatability proof in
  a second evidence window.
- Use the same two proven provider lanes when keys are available:
  `alibaba/qwen-turbo` and `deepseek/deepseek-chat`.
- Increase repeat count to `3` per provider for this tranche.
- Run the mandatory release gate bundle.
- Publish only a bounded public evidence update if the second-window proof
  passes.
- Record failure honestly if either lane degrades.

Out of scope:

- Adding new providers or models.
- Changing provider router/runtime semantics.
- Changing timeout behavior, SSE lifecycle, provider adapters, prompts, or
  model configuration.
- Maika proof, persistence/database implementation, hosted-readiness claim,
  kernel-owner replacement, or freeze release.

---

## Non-Goals

- Do not convert `4/4` plus this second window into a broad provider stability
  claim.
- Do not call this production readiness.
- Do not treat public-sync as permission to publish private provenance
  packets, raw traces, raw environment details, or secrets.
- Do not continue if live keys are unavailable or if failures expose a
  provider/runtime defect that needs remediation.

---

## Current Baseline

Closed baseline:

- Phase 2.B runtime coherence: checksum `fnv1a32:5d3d2dac`.
- One narrow live governance proof: Alibaba `/api/execute`, decision `ALLOW`.
- PBR-01 narrow repeatability: `4/4` PASS across Alibaba and DeepSeek.
- PBR-03 public-sync commit: `a0ac66de`.

Current claim ceiling:

CVF may claim bounded Phase 2.B coherence and narrow two-provider governed
route repeatability. It may not claim broad provider stability or hosted
product readiness.

---

## Roadmap Slices

### PSH-01 - Second-Window Provider Repeatability

Run `scripts/run_post_phase2b_provider_stability_probe.mjs` with:

- `CVF_POST_PHASE2B_PROVIDERS=alibaba,deepseek`
- `CVF_POST_PHASE2B_REPEATS=3`
- a fresh local port

Acceptance:

- `6/6` live journeys pass, or failures are recorded as bounded defects.
- Each journey has HTTP 200, `success=true`, non-mock output, live evidence
  mode, `/api/execute` route id, provider match, routing `ALLOW`, receipt id,
  and trace id.
- No raw key output.

### PSH-02 - Mandatory Release Gate

Run:

```powershell
python scripts/run_cvf_release_gate_bundle.py --json
```

Acceptance:

- Release gate passes, including live governance E2E.
- If it fails, this tranche closes as partial and no public-sync update is
  made.

### PSH-03 - Public Evidence Delta

If PSH-01 and PSH-02 pass, update the sibling public-sync clone with only a
bounded evidence delta.

Acceptance:

- Public-sync remote points to `Controlled-Vibe-Framework-CVF.git`.
- Public text says second-window repeatability, not broad provider stability.
- Public commit SHA is recorded in the completion packet.

---

## Evidence Requirements

- `node scripts/run_post_phase2b_provider_stability_probe.mjs` with repeat
  count `3`.
- `python scripts/run_cvf_release_gate_bundle.py --json`.
- Public-sync `git remote -v` before any public push.
- Docs governance, markdown structural completeness, active session state, and
  local governance hook-chain checks.

---

## Decision / Recommendation / Disposition

Proceed to GC-018 and work order for PSH-01 through PSH-03.

Recommended next move after completion:

- If stable, keep public claim bounded and consider hosted-readiness proof as a
  later separate tranche.
- If unstable, file a provider/runtime stability remediation roadmap before any
  wider public claim.

---

## Work Plan

1. File GC-018 and work order for the bounded second-window proof.
2. Run PSH-01 with the existing provider repeatability probe and `3` repeats
   per provider.
3. Run PSH-02 mandatory release gate.
4. Run PSH-03 public-sync update only if PSH-01 and PSH-02 pass.
5. File completion review with receipt/trace evidence and claim boundary.
6. Sync active session state, review queue, and handoff.

---

## Acceptance Criteria

- PSH-01 returns either PASS `6/6` or an honest partial/failure closure.
- PSH-02 release gate passes before any public update.
- PSH-03 public-sync update, if made, uses only bounded second-window
  repeatability language.
- Public and private completion packets preserve the no-broad-stability
  boundary.
- Governance checks pass before provenance commit.

---

## Claim Boundary

This roadmap can produce only second-window, two-provider, governed-route
repeatability evidence. It cannot prove broad provider stability, all-provider
parity, product readiness, hosted readiness, persistence/database readiness,
Maika proof, kernel-owner replacement, or global freeze lift.
