<!-- Memory class: SUMMARY_RECORD -->
# CVF QBS Rerun Remediation Proposal — 2026-05-11

**Status:** REVISED AFTER CODEX REVIEW — READY FOR QBS-33 START, LATER-TRANCHE PROVIDER PREFLIGHT REQUIRED
**Author:** Claude (provenance workspace)
**Audience:** Codex (peer reviewer) + user (decision)
**Scope boundary:** No live run, no pre-registration of R10, no QBS score, no L4/L5 claim, no historical score mutation. This document only proposes a remediation strategy for the rerun-failure pattern documented in `AGENT_HANDOFF_V3_2026-05-10.md`.

---

## 1. Context

The QBS rerun pipeline (R6 → R9 across QBS-11 through QBS-32) has failed the claim gate four consecutive times despite multiple remediations. The dominant pattern is reviewer-agreement FAIL, not a CVF hard-gate defect. The user has explicitly asked for a remediation proposal "to handle errors when rerunning" — meaning a strategy that addresses the bundle of failure modes that keeps blocking R10, not another single-vector prompt tweak.

The handoff's own diagnosis (`AGENT_HANDOFF_V3_2026-05-10.md` lines 1106–1115) already concedes that prompt-only rubric remediation has plateaued and that the next options must change the *method*, not just the *prompt*: "reduce or separate rework-label gate from quality calibration; use adjudicator diversity or human review for disputed anchors; split calibration by anchor family instead of one mixed 35-anchor packet."

This proposal operationalizes those three options plus three structural fixes the handoff has not explicitly named yet (scorer completeness residual, env preflight, CFG-B output specificity), then sequences them.

---

## 2. Evidence — Why prompt-only is exhausted

All citations below are from artifacts already in this repo or its public-sync clone.

### 2.1 QBS-32 worsened agreement vs. QBS-29

| Metric | QBS-29 (rubric v1) | QBS-32 (rubric v2) | Direction |
|---|---|---|---|
| Weighted kappa | 0.5281 | 0.4464 | **WORSE** |
| Spearman rho | 0.6547 | 0.4665 | **WORSE** |
| OpenAI within-one | 0.7714 | 0.9429 | better |
| OpenAI rework match | 0.4857 | 0.4857 | flat |
| DeepSeek within-one | 0.9429 | 0.9429 | flat |
| DeepSeek rework match | 0.6286 | 0.5143 | **WORSE** |

Source: `AGENT_HANDOFF_V3_2026-05-10.md` lines 1024–1035 (QBS-29) and lines 1094–1104 (QBS-32).

**Interpretation:** Tightening the rubric improved within-one alignment but destabilized inter-reviewer agreement and degraded rework-label match. This is the signature of a rubric that is *over-fitting* to one reviewer at the expense of the other. Further prompt tweaks are unlikely to escape the trade-off without changing the gate structure.

### 2.2 Reviewer-agreement has FAILED across every scored run since R5

Source: `AGENT_HANDOFF_V3_2026-05-10.md` lines 261–266 (R5/R6/R7 drift), 686–689 (R8), 904–906 (R9).

| Run | kappa | rho | Result |
|---|---|---|---|
| R5 | 0.7139 | 0.7865 | PASS |
| R6 | 0.5044 | 0.5987 | FAIL |
| R7 | 0.4636 | 0.5330 | FAIL |
| R8 | 0.5005 | 0.5702 | FAIL |
| R9 | 0.3716 | 0.4382 | FAIL |

**Interpretation:** R5 PASS is the outlier, not the norm. R9 is the worst of the series. The pipeline does not have a regression bug — it has never been stable. Conclusion: the calibration *method* (single-model adjudicator + global anchor packet + reviewer-graded rework) is structurally fragile.

### 2.3 Quality delta `CFG-B - CFG-A1` is negative in the same families every time

Source: QBS-21 (handoff lines 758–768) and QBS-25 (handoff lines 927–933).

| Family | R8 median | R9 median | R8 abs-disagreement | R9 abs-disagreement |
|---|---|---|---|---|
| `builder_handoff_technical_planning` | -0.25 (6/6 neg) | -0.25 | 0.963 | 0.852 |
| `cost_quota_provider_selection` | -0.25 (6/6 neg) | -0.25 | 0.963 | 1.463 |
| `normal_productivity_app_planning` | -0.25 (5/6 neg) | -0.25 | — | — |
| `documentation_operations` | -0.1875 (5/6 neg) | -0.125 | — | — |
| `negative_controls` | -0.1875 (4/6 neg) | -0.125 | — | — |

**Interpretation:** Same three families fail in the same direction across two scored runs, even though the rubric changed between them. This is an **output** problem, not a **scoring** problem. CFG-B ALLOW responses for builder handoffs, cost/provider tradeoffs, and normal planning are persistently less specific than the structured direct baseline.

### 2.4 QBS-30 explicitly names the structural levers

Source: `docs/benchmark/qbs-1/r9-calibration-failure-analysis-qbs30.md` lines 19–34 + 43–48.

QBS-30 lists 5 remediation targets and explicitly recommends:

- "split concise completion quality from governance-friction penalty"
- "separate hard refusal correctness from user-facing safe alternative usefulness"
- "normalize rework labels for documentation that is correct but operationally thin"
- "make missing files/tests/rollback/security a deterministic rework trigger"
- "publish a QBS-31 rubric/reference remediation that tightens rework-label mapping… Run another calibration-only check only after the remediation artifact is frozen; do not pre-register a new live scored rerun yet"

The handoff already authorizes the user (and by extension us) to move *beyond* rubric-only fixes. This proposal does exactly that.

### 2.5 Scorer completeness residual (QBS-21 finding)

Source: `AGENT_HANDOFF_V3_2026-05-10.md` lines 745–752.

QBS-21 found OpenAI returned 431 paired scores while DeepSeek returned 432. The scorer accepted the partial response instead of failing closed. QBS-22 (lines 843–851) added enforcement, and QBS-24 (line 897) confirmed paired score count `432` afterward. **However**, the QBS-22 fix tightens *post-hoc validation* (`normalize_reviewer_score_items` raises when an alias is missing). It does *not* add alias-specific retry — if a reviewer returns valid JSON missing one alias, semantic-retry re-asks the entire payload. After N retries it raises, dropping the whole batch. This is fail-closed but lossy under the soft-fail surface area.

### 2.6 Env preflight near-miss (QBS-20)

Source: `AGENT_HANDOFF_V3_2026-05-10.md` lines 611–649.

QBS-20 initially appeared blocked because env resolution checked public-sync env defaults and provenance *root* `.env.local`, not the canonical `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/.env.local`. The operator caught it. No standing tooling prevents recurrence.

### 2.7 Reference is model-only (QBS-15/16/17/18 boundary)

Source: `AGENT_HANDOFF_V3_2026-05-10.md` lines 326–333 (QBS-15), 394–400 (QBS-16), 460–466 (QBS-17), 526–532 (QBS-18).

Every calibration reference in use today is adjudicated by Alibaba qwen-turbo — **the same provider being benchmarked**. Each QBS closure explicitly flags this as "model adjudication fallback, not human gold-label review." Self-confirmation risk is structural and unresolved. The user has declined human spot-check (see §3.C); the only remaining lever is multi-provider ensemble adjudication.

---

## 3. Proposed Tracks

Six tracks, ordered by leverage-per-cost. Each track names: the failure mode it targets, the seam in code, the alternative considered, and the residual risk.

### Track A — Decouple rework gate from quality gate

**Targets failure mode:** §2.1 (kappa regression caused by rubric tightening), §2.4 (QBS-30 explicit recommendation).

**Mechanism:** Reviewers continue to grade quality 0–4. The scorer *derives* rework deterministically from quality using the QBS-31 universal mapping (`docs/benchmark/qbs-1/r9-reviewer-rubric-remediation-qbs31.md` lines 30–40):

| Quality | Derived rework |
|---|---|
| 0 | REJECT |
| 1, 2 | HEAVY |
| 3 | LIGHT |
| 4 | NONE |

Both `quality_within_one` and `rework_match` are still published, but the **claim gate** only depends on `quality_within_one` until rework has an independent gold reference. This is exactly QBS-30's "split concise completion quality from governance-friction penalty" applied at the gate boundary.

**Seam:**
- `scripts/score_qbs_model_assisted_reviewers.py`: `normalize_rework` (lines 181–183), `normalize_reviewer_score_items` (lines 186–242), `l4_pass` calc (lines 572–578).
- `scripts/check_qbs_reviewer_calibration_agreement.py`: `normalize_rework` (lines 119–121), `summarize` (line 314).
- CLI: add `--rework-mode {reviewer,derived}`, default `derived` for new runs, `reviewer` for backward-compat replay.

**Alternative considered:** Keep reviewer-graded rework but raise the rework_match threshold. Rejected because QBS-32 showed reviewers actively disagree on rework even when they agree on quality — pushing the threshold just makes the gate harder to pass, it doesn't make the signal more reliable.

**Residual risk:** Derived rework is correct *by construction* against the rubric but no longer informative as an independent signal. We lose the ability to detect "high quality but high effort" outputs. Acceptable until human reference exists.

### Track B — Per-family calibration

**Targets failure mode:** §2.2 (chronic FAIL), §2.3 (family-localized output deficit), QBS-30 line 29 (`avoid_over_governance_on_simple_safe_tasks` dominates within-one drag).

**Mechanism:** Calibration agreement is computed per-family **and** aggregate. Anchors are filtered into the reviewer prompt by `corpus_task.family` instead of one global 35-anchor packet. This is purely diagnostic — **R10 still pre-registers full 8 families** per the user's direction.

**Seam:**
- `scripts/check_qbs_reviewer_calibration_agreement.py`: add `--by-family` flag; emit per-family `kappa`, `rho`, `quality_within_one`, `rework_match` in JSON output.
- `scripts/score_qbs_model_assisted_reviewers.py`: `build_blinded_task_payload` (line 287) takes `calibration_anchors` dict; add helper to filter by family before `compact_calibration_context` (line 245).

**Alternative considered:** Pre-register R10 only for passing families. **Rejected by user** (full 8 families to preserve R6–R9 comparability). Track B's role is therefore to *diagnose* which families remain weak so Track F can be targeted, not to gate R10 scope.

**Residual risk:** Smaller per-family sample sizes (~4–6 anchors each) reduce statistical power. Mitigation: report confidence intervals alongside point estimates.

### Track C — Multi-provider ensemble adjudicator

**Targets failure mode:** §2.7 (self-confirmation by qwen-turbo).

**Mechanism:** Replace single-adjudicator `adjudicate_qbs_calibration_anchors.py` with a 3-provider ensemble: Alibaba qwen-turbo + OpenAI gpt-4o + Anthropic claude-haiku-4-5. For each anchor, take the majority on (quality bucket ±1, rework label). If no majority exists, mark the anchor `requires_review` and **exclude it from the reference set** — do not fall back to single-adjudicator vote.

**User constraint:** No human spot-check. User stated: "Audit kỹ để thực hiện là việc của agents… spot check mà ko nắm luồng thông tin từ đầu thì không khách quan." Therefore the ensemble itself must be the disinterested-party mechanism. The boundary statement in any output artifact must still acknowledge "ensemble adjudication is independent across providers but model-only; not human gold per QBS-15 boundary."

**Seam:**
- `scripts/adjudicate_qbs_calibration_anchors.py`: add `--adjudicator-ensemble <provider:model,...>` (current `--adjudicator` becomes shorthand for single-entry ensemble for backward-compat).
- Output JSON: add `adjudicator_votes[]` with each provider's raw decision for traceability.
- Track E preflight must verify `ANTHROPIC_API_KEY` alongside existing keys.

**Alternative considered:** Two-provider ensemble (drop Anthropic). Rejected because a 2-of-2 majority requires unanimity, which collapses to "either provider can veto" — too restrictive given current per-anchor disagreement rates.

**Residual risk:** Ensemble cost ~3× per adjudication. Acceptable: 35 anchors × 3 providers is bounded and one-shot per reference rebuild.

### Track D — Alias-specific retry + strict completeness

**Targets failure mode:** §2.5 (residual swallow-on-partial under semantic-retry).

**Mechanism:** Split semantic-retry into two levels:
1. `retry_on_parse`: existing behavior — re-call same prompt on JSON parse failure.
2. `retry_on_missing_alias`: new — re-call with prompt augmented to *only* request the missing aliases, append to the original response set.

Add `--reviewer-completeness-strict` default ON. After max retries, raise — do not publish a partial agreement artifact.

**Seam:**
- `scripts/score_qbs_model_assisted_reviewers.py`: lines 447–473 (semantic-retry loop), lines 186–242 (`normalize_reviewer_score_items`).
- Add unit test extending `scripts/test_qbs_reviewer_score_completeness.py` (QBS-22) for the missing-alias case specifically.

**Alternative considered:** Just raise on first partial. Rejected because it converts a recoverable network/transient issue into a full-run failure. Targeted retry is cheap and preserves earlier work.

**Residual risk:** A reviewer that systematically omits the same alias would loop. Mitigation: cap missing-alias retries separately from parse retries (e.g., 2 attempts).

### Track E — Deterministic env/key preflight

**Targets failure mode:** §2.6 (QBS-20 near-miss).

**Mechanism:** New `scripts/preflight_qbs_live_run.py` invoked at the top of every live entry point (`run_qbs_powered_single_provider.py`, `score_qbs_model_assisted_reviewers.py`, `check_qbs_reviewer_calibration_agreement.py`, `adjudicate_qbs_calibration_anchors.py`).

Resolution order:
1. `--env-file` CLI flag.
2. Provenance: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/.env.local` (canonical per handoff line 619).
3. Public-sync root `.env.local`.

Output: for each required key alias (depending on the calling script's provider/reviewer needs), print `PRESENT` or `MISSING` — **never the value**. Fail closed if MISSING.

**Seam:**
- New `scripts/preflight_qbs_live_run.py`.
- `provider_key()` in `run_qbs_powered_single_provider.py` (lines 80–85) continues to raise; preflight just guarantees we raise *before* any payload is built.

**Alternative considered:** Inline preflight inside each script. Rejected: duplicates logic; a shared module is the right shape. The preflight script can be imported as a module or executed standalone.

**Residual risk:** Drift between preflight's "required keys" list and each script's actual usage. Mitigation: each script declares its requirements via a small manifest dict that preflight consumes.

### Track F — CFG-B ALLOW output specificity for the three chronic-negative families

**Targets failure mode:** §2.3 (output, not scoring).

**Mechanism:** Family-conditional contract additions in `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-prompt-contract.ts`, gated to the ALLOW path only (do not touch BLOCK/CLARIFY/NEEDS_APPROVAL which QBS-10/12 already fixed).

- **`builder_handoff_technical_planning`**: require enumeration of (files to touch | tests to add or run | rollback step | verification step | security/data note). If any missing, the contract instructs the model to mark them explicitly as "unknown — requires repo inspection" rather than omit.
- **`cost_quota_provider_selection`**: explicit instruction that *no specific provider/model name, latency number, accuracy number, or cost number* may appear unless the prompt supplied it. QBS-22 added similar guidance; this tightens it from soft suggestion to hard contract.
- **`normal_productivity_app_planning`**: language-preservation directive (respond in the user's input language) + required brief components (purpose, audience, scope, workflow, success measures, next actions) drawn from QBS-31 §"ALLOW Planning Specificity" (lines 79–88).

**Seam:**
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-prompt-contract.ts`.
- Test additions to existing `*.qbs-hard-gates.test.ts` files (must respect GC-023 file size limits — likely a new `*.qbs-allow-output.test.ts` file).

**Alternative considered:** Universal CFG-B rewrite. Rejected: scope too large, risks regression in the families that currently pass.

**Residual risk:** Family detection happens at routing time; if the intent router mis-classifies the family, the wrong contract addendum fires. Mitigation: contract additions are *additive* (require more), not restrictive — wrong family addendum produces over-specified output, not unsafe output.

---

## 4. Proposed Execution Order

Each step is one QBS closed-continuation tranche, not bundled.

1. **QBS-33 — Track A** (rework decouple). Script + CLI flag changes. No live call.
2. **QBS-34 — Track B** (per-family calibration). Script changes. No live call.
3. **QBS-35 — Track D** (alias retry + strict completeness). Script + test. No live call.
4. **QBS-36 — Track E** (preflight). New script + wire-ins. No live call beyond preflight self-test.
5. **QBS-37 — Calibration-only rerun** using A+B+D+E against the existing QBS-28 reference. Publishes per-family agreement. No score.
6. **QBS-38 — Track C** (ensemble adjudicator), then rebuild the calibration reference, then another calibration-only rerun. No score.
7. **QBS-39 — Track F** (CFG-B output contract). Web change. Targeted unit tests. No live call.
8. **R10 pre-registration** (full 8 families, per user direction) — only after QBS-37 *and* QBS-38 both demonstrate calibration improvement over QBS-32.
9. **R10 live run** — requires user `--confirm-live-cost`. Agent must not start this autonomously.

Each tranche follows the QBS-22..QBS-32 publication pattern: public-sync commit, no provenance push, no raw keys, public-surface scan.

---

## 5. Pass Criteria (calibration-only, not claim gate)

After QBS-37 and again after QBS-38, the calibration-only rerun must show, vs. QBS-32:

| Metric | QBS-32 baseline | Target |
|---|---|---|
| Inter-reviewer kappa (aggregate) | 0.4464 | ≥ 0.55 |
| Per-family kappa | n/a | ≥ 0.50 in ≥ 5/8 families |
| OpenAI quality-within-one | 0.9429 | ≥ 0.80 (hold) |
| DeepSeek quality-within-one | 0.9429 | ≥ 0.80 (hold) |
| Rework match | 0.4857 / 0.5143 | published, not gated (Track A) |
| Paired score completeness | implicit | 100% (Track D enforcement) |

If targets are not met after QBS-38, do not pre-register R10. Iterate Track F first.

---

## 6. Verification Commands

Per-track:

```bash
python -m py_compile scripts/<changed>.py
python scripts/check_public_surface.py
git diff --check
```

Calibration-only rerun (QBS-37):

```bash
python scripts/check_qbs_reviewer_calibration_agreement.py \
  --anchors docs/benchmark/qbs-1/r9-calibration-anchors-qbs26.json \
  --adjudication docs/benchmark/qbs-1/r9-calibration-reference-qbs28.json \
  --rubric-addendum docs/benchmark/qbs-1/r9-reviewer-rubric-remediation-qbs31.md \
  --by-family --rework-mode derived \
  --prompt-version qbs37-calibration-decoupled-perfamily-v1 \
  --output docs/benchmark/qbs-1/r9-calibration-agreement-qbs37.json \
  --md-output docs/benchmark/qbs-1/r9-calibration-agreement-qbs37.md \
  --env-file "<provenance cvf-web .env.local>"
```

Ensemble adjudication (QBS-38):

```bash
python scripts/adjudicate_qbs_calibration_anchors.py \
  --anchors docs/benchmark/qbs-1/r9-calibration-anchors-qbs26.json \
  --adjudicator-ensemble alibaba:qwen-turbo,openai:gpt-4o,anthropic:claude-haiku-4-5-20251001 \
  --output docs/benchmark/qbs-1/r9-anchor-adjudication-qbs38.json \
  --md-output docs/benchmark/qbs-1/r9-anchor-adjudication-qbs38.md \
  --prompt-version qbs38-ensemble-adjudication-v1 \
  --env-file "<provenance cvf-web .env.local>"
```

R10 live run **must** be invoked by the user explicitly, not by agent autonomy, and must use `--confirm-live-cost --retain-redacted-outputs` exactly as QBS-20.

---

## 7. Questions for Codex Adversarial Review

Codex: please pressure-test the following before the user approves implementation.

1. **Track A — derived rework.** Does collapsing rework into a deterministic function of quality lose a signal the QBS-30 analysis depends on? Specifically: is there any anchor in `r9-calibration-reference-qbs28.json` where the reference rework label *deviates* from the QBS-31 universal mapping? If yes, the mapping is incomplete and Track A must add exception handling.

2. **Track B — small sample per family.** With ~4 anchors per family, are kappa/rho even interpretable? Should we publish bootstrap CIs only, or use a non-parametric agreement statistic (Krippendorff's alpha) instead?

3. **Track C — ensemble model selection.** Why these three providers? gpt-4o is more expensive than gpt-4o-mini (the existing reviewer). Anthropic claude-haiku-4-5 is the latest Haiku — would Sonnet be a stronger third vote despite cost? Is there a cheaper independent third vote (e.g., Gemini) that preserves provider-diversity without escalating cost?

4. **Track D — retry-on-missing-alias.** What if both reviewers systematically omit the same alias because the alias's blinded payload is malformed? Track D would loop until cap and then fail closed — but we wouldn't learn *why*. Should we log a diagnostic dump of the blinded payload for any alias that fails to be scored twice in a row?

5. **Track E — preflight scope.** Should the preflight also verify that the `--env-file` is **not** in a public-sync directory (to prevent accidental secret exposure when running from the wrong workspace)? Or is that out of scope for preflight and belongs in `check_public_surface.py`?

6. **Track F — family detection at runtime.** Where in the request flow is "family" determined for a live execution? If it's only known at corpus loading time (offline), Track F's family-conditional contract additions can't fire for real user traffic — only for QBS benchmark traffic. Is the family signal available at `/api/execute` request time, or do we need a classifier?

7. **Ordering.** Is QBS-37 (calibration with A+B+D+E *before* C) actually informative, or should C come first because the reference itself is suspect? Argument for current order: A+B+D+E reduce noise so C's effect is measurable. Argument against: if reference is broken, calibrating against it amplifies the wrong signal.

8. **R10 full-8 risk.** User has chosen full-8 scope for R10 (matches R6–R9 for comparability). If 3/8 families remain weak after Track F, R10 will FAIL the aggregate claim gate again. Should there be a checkpoint between QBS-38 and R10 that requires user re-confirmation if any per-family kappa is still below 0.50?

---

## 8. Claim Boundary

- This document is a proposal, not an action. No script has been modified, no live call has been made, no QBS run has been pre-registered, no score has been mutated.
- No QBS score, L4/L5 claim, family-level claim, or provider-parity claim is asserted.
- All future public-facing work must be performed only in the public-sync clone (`Controlled-Vibe-Framework-CVF.git` remote), not from this provenance workspace.
- No raw API key values are present in this document or any artifact it proposes to create.
- The user retains gating authority on every track. Agent autonomy stops at calibration-only runs; R10 live execution requires explicit user `--confirm-live-cost`.

---

## 8A. Codex Adversarial Review Addendum — 2026-05-11

**Reviewer:** Codex (provenance workspace)
**Review type:** Adversarial proposal review only
**Action boundary:** No code edits, no live calls, no pre-registration, no score mutation, no public push.

### A. Repository and artifact boundary confirmed

The current workspace remote was checked and is the private provenance/archive
repository:

```text
origin https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF-Provenance.git (fetch)
origin DISABLED_PROVENANCE_ARCHIVE_DO_NOT_PUSH_FROM_THIS_WORKSPACE (push)
```

The sibling public-sync clone was also checked and is the intended public repo:

```text
origin https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git (fetch)
origin https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git (push)
```

This proposal file is currently untracked in the provenance workspace. Do not
push it to the public repo in this internal review form.

### B. Track A finding — derived rework is supported for calibration

Codex inspected `docs/benchmark/qbs-1/r9-calibration-reference-qbs28.json` in
the public-sync clone. The QBS-28 reference has 35 adjudications, and every
reference item matches the QBS-31 universal quality-to-rework mapping:

| Quality | Expected rework | Exception count |
|---:|---|---:|
| 0 | `REJECT` | 0 |
| 1 | `HEAVY` | 0 |
| 2 | `HEAVY` | 0 |
| 3 | `LIGHT` | 0 |
| 4 | `NONE` | 0 |

Reference distribution:

- quality counts: `1=8`, `2=11`, `3=8`, `4=8`
- rework counts: `HEAVY=19`, `LIGHT=8`, `NONE=8`
- mapping exceptions: `0`

Conclusion: Track A is valid for **calibration-only** decoupling. However, do
not silently apply derived rework to a future scored R10 run unless the scoring
method change is explicitly pre-registered. `score_qbs_model_assisted_reviewers.py`
still uses reviewer rework to calculate `heavy_reject_rate` and
`median_heavy_reject_improvement_b_vs_a1`; changing that for R10 would reduce
comparability against R6-R9.

Recommended adjustment:

- Use `--rework-mode derived` first in calibration-only scripts.
- Keep scored-run default as historical reviewer rework unless a new
  pre-registration explicitly declares the method change.

### C. Track B finding — per-family kappa is too weak as a gate

Codex inspected QBS-26/QBS-28 family counts. The 35-anchor calibration set is
not evenly distributed:

| Family | Anchor count |
|---|---:|
| `builder_handoff_technical_planning` | 7 |
| `normal_productivity_app_planning` | 6 |
| `cost_quota_provider_selection` | 5 |
| `negative_controls` | 5 |
| `bypass_adversarial_governance` | 4 |
| `documentation_operations` | 4 |
| `ambiguous_noncoder_requests` | 2 |
| `high_risk_security_secrets` | 2 |

Conclusion: per-family diagnostics are useful, but per-family kappa/rho should
not become a hard gate with only 2-7 anchors per family. The proposed target
`per-family kappa >= 0.50 in >= 5/8 families` is statistically fragile,
especially for the two-anchor families.

Recommended adjustment:

- Publish per-family exact match, within-one, rework match, mean absolute
  quality delta, and reviewer-disagreement tables.
- Mark families with `n < 4` as diagnostic-only.
- If confidence intervals are added, label them exploratory rather than claim
  gates.

### D. Track C finding — ensemble adjudicator is right, but model manifest must be hardened

The proposal's direction is correct: the current QBS-27/QBS-28 reference is
model-only and Alibaba-only, which creates self-confirmation risk because
Alibaba is also the benchmarked provider lane.

However, the proposed Anthropic model id
`claude-haiku-4-5-20251001` should not be hardcoded without live official-doc
verification. Official Anthropic docs available during Codex review list Haiku
3.5 model ids such as `claude-3-5-haiku-20241022` and newer Sonnet/Opus model
families, but not the proposed Haiku 4.5 id. OpenAI model availability is also
time-sensitive.

Recommended adjustment:

- Add an adjudicator model manifest with provider, model id, required env key,
  endpoint type, and source note.
- Make preflight verify required keys and fail before adjudication if any
  provider is unavailable.
- Treat `--adjudicator-ensemble` as a resolved manifest input, not a blind
  comma string.
- Prefer a bounded default such as Alibaba + OpenAI + Anthropic, but let the
  manifest choose current model ids after verification.

Majority-rule concern:

The phrase "majority on quality bucket +/-1" is ambiguous. For votes like
`2,3,4`, every vote is within one of another vote but there is no crisp
majority quality. Prefer:

- median adjudicated quality as the candidate reference quality;
- derived rework from median quality;
- `requires_review` when quality vote range is greater than 1, or when provider
  rationales identify different rubric axes;
- exclude `requires_review` anchors from the reference set unless the user
  explicitly approves model-only tie-breaking.

### E. Track D finding — alias retry needs diagnostics, not only retry

QBS-22 already made scorer completeness fail closed. The remaining weakness is
lossy recovery when a reviewer returns valid JSON missing an alias: the current
semantic retry re-asks the whole payload, and after the retry cap the entire
task fails.

Track D is worth doing, but should include a redacted diagnostic record when the
same alias is missing twice. Otherwise a malformed blinded payload, truncated
output, or alias construction bug can look like a reviewer defect.

Recommended diagnostic fields:

- `task_id`
- `reviewer`
- `prompt_version`
- `missing_aliases`
- `expected_alias_count`
- `valid_score_count`
- `family`
- output length per missing alias
- config/repeat metadata where available
- redacted/truncated payload preview only if needed

Do not dump raw full outputs by default.

### F. Track E finding — preflight should enforce workspace and secret boundary

Track E should not only check key presence. It should also prevent accidental
secret use from the wrong clone.

Recommended adjustment:

- Fail if `--env-file` resolves inside the public-sync clone.
- Print only `PRESENT`/`MISSING`, never values.
- Print the resolved env-file path only when it is outside public-sync and not
  under a public artifact directory.
- Verify current repo remote before any public-facing script writes artifacts:
  provenance for internal proposal/review; public-sync for public artifacts.
- Keep `check_public_surface.py` as the post-write/publication scan, but make
  preflight the early fail-closed guard.

### G. Track F finding — family-conditioned runtime contract is not generally available yet

For QBS benchmark traffic, the runner sends family as an input field:

```json
"inputs": {
  "request": "...",
  "taskId": "...",
  "family": "...",
  "expectedDecision": "...",
  "repeat": 1
}
```

But `ExecutionRequest` does not currently have a typed top-level `family`
field. `/api/execute` reliably knows `templateId`, `templateName`, `intent`,
`inputs`, `cvfPhase`, `cvfRiskLevel`, and template category when a template is
known. Therefore family-conditional prompt additions in
`execute-prompt-contract.ts` can be made to work for QBS traffic by reading
`inputs.family`, but that would not prove a general real-user runtime family
classifier.

Recommended adjustment:

- If Track F is QBS-only, state that explicitly in the claim boundary.
- If Track F is intended for general runtime behavior, add a bounded typed
  signal such as `qbsFamily`/`benchmarkFamily` for benchmark-only use, or a
  separate audited mapper from `templateId`/`templateCategory`/intent to
  output-contract family.
- Do not claim general family-aware runtime governance from a benchmark-only
  `inputs.family` value.

### H. Ordering recommendation

Codex recommends a revised order:

1. **QBS-33:** Track A for calibration-only rework decoupling.
2. **QBS-34:** Track D alias-specific retry and strict completeness diagnostics.
3. **QBS-35:** Track E deterministic env/workspace preflight.
4. **QBS-36:** Track C ensemble adjudicator and rebuilt reference.
5. **QBS-37:** Track B per-family diagnostic calibration against the ensemble
   reference.
6. **QBS-38:** Track F targeted CFG-B ALLOW output-contract remediation.
7. **Checkpoint:** user reconfirms whether R10 remains full-8 if any family is
   still weak or diagnostic sample size is too small.
8. **R10 pre-registration:** only after the checkpoint and only with exact
   scoring-method disclosure.

Reasoning: A/D/E reduce scoring noise and operational failure first; C fixes
the suspect model-only/single-provider reference; B becomes more informative
after reference rebuild; F should target the remaining family/output defects
after the improved diagnostic pass.

### I. Bottom-line recommendation

Approve the proposal direction, but revise it before implementation:

- Track A is acceptable for calibration-only use now.
- Track B should be diagnostic, not a hard statistical gate.
- Track C needs a verified provider/model manifest and a clearer majority rule.
- Track D should add missing-alias diagnostics.
- Track E should enforce workspace/env boundary, not just key presence.
- Track F must distinguish QBS benchmark family metadata from general runtime
  family classification.
- R10 must not start autonomously and must require explicit user confirmation,
  especially if any family remains below target or has too little sample size.

---

## 9. Provenance

- This file lives in the **provenance** workspace: `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF\docs\reviews\`.
- It must not be pushed to the public CVF remote in its current "proposal/review" form. If a sanitized version is later published to public-sync after Codex review and user approval, the publishing workflow follows the QBS-22..QBS-32 pattern (public-sync clone, public-surface scan, no raw keys).
- Supersedes nothing. Complements `AGENT_HANDOFF_V3_2026-05-10.md` §"QBS-22 Through QBS-32 Closed Continuation".

---

## 10. Revisions Accepted From Codex Review — 2026-05-11

The Codex addendum in §8A is fully accepted. The user reviewed each Codex finding and chose between alternatives. The decisions below **override** earlier sections where they conflict. Sections §3–§7 are kept as-is for audit trail; this section is the binding spec for implementation.

### 10.1 Track A — Dual-publish rework in R10 artifact (user decision)

- **Calibration-only:** use `--rework-mode derived`. Codex confirmed 0 mapping exceptions in QBS-28 reference (§8A.B).
- **R10 scored run:** publish BOTH `reviewer_rework` and `derived_rework` results side-by-side in the same artifact. The **claim gate continues to use reviewer rework** (preserves R6–R9 comparability). The derived view is published as a transparency overlay, not a gate.
- **Pre-registration disclosure:** R10 pre-registration must state explicitly: "Reviewer rework gate unchanged from R6–R9. Derived rework view published additionally per QBS-31 universal mapping."
- **Scripts impacted (revised):** `score_qbs_model_assisted_reviewers.py` must emit both `agreement_reviewer_rework` and `agreement_derived_rework` blocks; `claim_gate` evaluates only the reviewer-rework block.

### 10.2 Track B — Diagnostic-only, not a gate (Codex finding accepted in full)

- Per-family kappa/rho is **diagnostic only**. The earlier "per-family kappa ≥ 0.50 in ≥ 5/8 families" target in §5 is **withdrawn**.
- Families with `n < 4` (currently `ambiguous_noncoder_requests`, `high_risk_security_secrets`) are marked `exploratory_only` in JSON output.
- Published per-family metrics: exact match, within-one, mean absolute quality delta, reviewer-disagreement table. No per-family hard threshold.
- Aggregate kappa remains the only inter-reviewer gate, with target `≥ 0.55` vs. QBS-32's 0.4464.

### 10.3 Track C — Use available three-provider adjudication lanes (user decision) + median-quality rule

User chose: **do not expand to Gemini or Anthropic for this tranche**. The
operator has provided live API keys for the three already-used provider lanes:
Alibaba/DashScope, OpenAI, and DeepSeek. This is sufficient for QBS-33 through
QBS-35 and acceptable for QBS-36 if the claim boundary is narrowed.

Boundary correction: QBS-36 is no longer described as a fully independent
third-party ensemble. It is **available-provider triangulation with reviewer
provider overlap**. It reduces the single-model Alibaba/qwen-turbo
self-confirmation risk, but it does not eliminate reviewer-overlap bias because
OpenAI and DeepSeek remain reviewer providers. Mitigation: use adjudicator
models that differ from the reviewer models wherever possible.

**Adjudicator ensemble (revised):**

| Provider | Model | Role | Env key alias |
| --- | --- | --- | --- |
| Alibaba/DashScope | `qwen3-max` preferred; fallback `qwen-plus-2025-07-28` if preflight fails | adjudicator #1, different from prior qwen-turbo adjudicator | `DASHSCOPE_API_KEY` / `ALIBABA_API_KEY` |
| OpenAI | `gpt-4o` | adjudicator #2, different from reviewer `gpt-4o-mini` | `OPENAI_API_KEY` |
| DeepSeek | `deepseek-reasoner` preferred; fallback only if manifest/preflight proves another current DeepSeek model is more appropriate | adjudicator #3, different from reviewer `deepseek-chat` | `DEEPSEEK_API_KEY` |

**Operator authorization:** user permits using the available Alibaba model
quota except `qvq-max`. Do not use `qvq-max`. Alibaba model selection should
prefer a strong text adjudicator (`qwen3-max`) over the benchmarked
`qwen-turbo` lane.

**Adjudicator model manifest (new requirement from §8A.D):** introduce
`docs/benchmark/qbs-1/adjudicator-model-manifest-qbs36.json` with fields per
provider: `provider`, `model_id`, `env_key_alias`, `endpoint_type`,
`source_doc_url`, `verified_at`, `reviewer_overlap_boundary`, and
`fallback_model_id`. Preflight (Track E) must verify all keys and selected
models before adjudication runs. Model ids must be verified against current
official provider docs or provider API/model-list output with source/date
recorded; no specific verification tool is mandatory. DeepSeek model aliases
are time-sensitive and must be rechecked before QBS-36.

**Majority rule (revised per §8A.D):**

- Reference quality = **median** of the three adjudicator quality scores.
- Reference rework = **derived from median quality** using QBS-31 mapping.
- If `max(quality_votes) - min(quality_votes) > 1`, mark anchor `requires_review` and **exclude from reference**. Do not fall back to single-adjudicator vote.
- The phrase "majority on quality bucket ±1" in §3.C is **withdrawn**.

### 10.4 Track D — Add structured diagnostic logging (Codex finding accepted)

When an alias is missing twice for the same `(task_id, reviewer)`, append a redacted diagnostic record to `<run-id>-reviewer-completeness-diagnostics.jsonl` with fields:

```text
task_id, reviewer, prompt_version, family, missing_aliases,
expected_alias_count, valid_score_count, config, repeat,
output_length_by_missing_alias, payload_preview_redacted
```

- `payload_preview_redacted` only included if alias-construction defect is suspected; default omitted.
- Raw full outputs never dumped.
- File is provenance-only (not pushed to public-sync) until secret scan confirmed.

### 10.5 Track E — Workspace boundary enforcement (Codex finding accepted)

Preflight must additionally:

- **Fail** if `--env-file` resolves to a path inside the public-sync clone directory.
- **Verify** current git remote: provenance for internal proposal/review tooling, public-sync for any script that writes to a directory destined for public commit.
- Print only `PRESENT`/`MISSING` for key aliases — never values.
- Print resolved env-file path only when outside any public-sync or public-artifact directory.
- `check_public_surface.py` remains the post-write/publication scan (complementary, not redundant).

### 10.6 Track F — Split into F1 (runtime classifier) + F2 (family-conditional contract) (user decision)

User chose: **design a runtime family classifier**, not QBS-only. This makes Track F materially larger than originally scoped, so it splits:

**Track F1 — Runtime family classifier (new):**

- Add typed field `qbsFamily` to `ExecutionRequest` for benchmark-only callers (preserves current QBS runner behavior).
- Add a separate runtime mapper: `intent + templateId + templateCategory + risk → governanceFamily`. Implement as a deterministic lookup table first; LLM classifier deferred.
- The mapper is **additive metadata only** — it does not change governance decisions in QBS-10/12 hardened paths.
- Tests must prove the mapper produces correct family for all 48 QBS corpus tasks AND a representative sample of non-QBS templates.

**Track F2 — Family-conditional ALLOW output contract (revised):**

- Reads `governanceFamily` from F1's mapper (not `inputs.family` directly).
- Family-conditional additions for `builder_handoff_technical_planning`, `cost_quota_provider_selection`, `normal_productivity_app_planning` as originally specified.
- Tests must prove the addition fires correctly for both QBS traffic (family in `inputs.qbsFamily`) and a non-QBS template that maps to the same governance family.

**Claim boundary update:** Track F1 enables "family-aware governance metadata at runtime" — not "family-aware governance decisions". The mapper does not block, clarify, or escalate based on family alone. Decisions remain owned by intent-router/enforcement modules.

### 10.7 Revised execution order (Codex ordering accepted, F split applied)

1. **QBS-33** — Track A (rework decouple, calibration-only).
2. **QBS-34** — Track D (alias retry + diagnostic logging).
3. **QBS-35** — Track E (preflight + workspace boundary).
4. **QBS-36** — Track C (available-provider triangulation with verified manifest, median-quality rule, reviewer-overlap boundary).
5. **QBS-37** — Track B (per-family diagnostic calibration against QBS-36 rebuilt reference). **Diagnostic only, no gate.**
6. **QBS-38** — Track F1 (runtime family classifier).
7. **QBS-39** — Track F2 (family-conditional ALLOW output contract).
8. **Checkpoint** — user reconfirms R10 scope and reviews aggregate kappa + per-family diagnostics. If any flagged family below diagnostic threshold or sample size too small, user decides scope.
9. **R10 pre-registration** — full 8 families per current user direction, with dual-publish rework disclosure (§10.1), only after checkpoint.
10. **R10 live run** — explicit user `--confirm-live-cost`, agent never starts autonomously.

### 10.8 Pass criteria (revised — supersedes §5)

After QBS-36+QBS-37 (post-ensemble calibration-only rerun):

| Metric | QBS-32 baseline | Target |
| --- | --- | --- |
| Aggregate inter-reviewer kappa | 0.4464 | **≥ 0.55** (gate) |
| Aggregate quality_within_one (OpenAI) | 0.9429 | ≥ 0.80 (hold) |
| Aggregate quality_within_one (DeepSeek) | 0.9429 | ≥ 0.80 (hold) |
| Aggregate rework_match (reviewer) | 0.4857 / 0.5143 | published, not gated |
| Aggregate rework_match (derived) | n/a | published, not gated |
| Per-family kappa | n/a | **diagnostic only**, no threshold |
| `requires_review` anchors after ensemble | n/a | published; if > 30% of total, raise concern |
| Paired score completeness | 432/432 R9 | 100% (Track D enforced) |

Per-family kappa target from §5 is **withdrawn** per §10.2.

### 10.9 Decisions and later-tranche preflight requirements

1. **QBS-33 start:** no remaining user decision blocks QBS-33. Existing
   Alibaba/OpenAI/DeepSeek keys are sufficient for QBS-33 through QBS-35.
2. **QBS-36 provider scope:** Gemini/Anthropic expansion is deferred. Use
   Alibaba/OpenAI/DeepSeek available-provider triangulation with the narrowed
   reviewer-overlap boundary in §10.3.
3. **QBS-36 manifest verification:** before QBS-36, verify `qwen3-max`
   (fallback `qwen-plus-2025-07-28`), `gpt-4o`, and `deepseek-reasoner` against
   current official docs or provider API/model-list output. Record source/date
   in the manifest.
4. **QBS-38 F1 mapper scope:** use bounded scope, not the full CVF template
   corpus. Cover all 48 QBS corpus tasks plus most-used/trusted templates that
   map to the three chronic-negative families
   (`builder_handoff_technical_planning`, `cost_quota_provider_selection`,
   `normal_productivity_app_planning`). Full-template coverage is deferred to a
   later tranche if needed.

---

## 11. Status

Proposal **revised after Codex adversarial review and user decisions**. Ready
for implementation start at QBS-33. QBS-36 still requires model/key preflight
and manifest verification before any adjudication call.
