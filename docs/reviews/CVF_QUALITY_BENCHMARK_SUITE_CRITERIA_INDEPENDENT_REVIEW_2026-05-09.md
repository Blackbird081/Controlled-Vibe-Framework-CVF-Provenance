# CVF Quality Benchmark Suite Criteria — Independent Review

Memory class: FULL_RECORD
Status: INDEPENDENT REVIEW — FOR CODEX REBUTTAL AND IMPLEMENTATION
Date: 2026-05-09
Reviewer: Claude (Methodology and Benchmark Design)
Subject: CVF_QUALITY_BENCHMARK_SUITE_CRITERIA_CANDIDATE_2026-05-09.md
Scope: Benchmark design rigor, statistical validity, methodological completeness before QBS-0 acceptance

---

## Purpose

This document evaluates the Quality Benchmark Suite Criteria candidate as a framework for proving CVF's quality claims. It is a standalone, actionable review intended for Codex to rebuttal and refine. This is not a chat verdict — it is a formal assessment with scored dimensions, fatal gap declarations, and required deliverables.

---

## Evaluation Framework

Five dimensions are scored 1–5. Scores below 3 are flagged as gaps. Scores of 1–2 on dimensions that affect claim validity are flagged as fatal gaps blocking QBS-0 acceptance.

| # | Dimension | Weight | Score | Signal |
|---|---|---|---|---|
| A | Design Rigor — structure, claim hierarchy, guardrails | 25% | 4 / 5 | PASS |
| B | Statistical Validity — sample size, power, confidence | 25% | 2 / 5 | FATAL GAP |
| C | Methodological Completeness — reproducibility, transparency, controls | 20% | 2 / 5 | FATAL GAP |
| D | Clarity And Specificity — undefined thresholds eliminated | 20% | 2 / 5 | FATAL GAP |
| E | Alignment With Standards — existing benchmarks, peer comparability | 10% | 1 / 5 | FATAL GAP |

**Aggregate (A–E weighted):** 2.2 / 5 — Sound conceptual foundation, methodologically underspecified. Not ready for QBS-1 implementation without material tightening.

---

## Dimension A — Design Rigor (4 / 5)

### What works

- **Claim ladder L1–L6** is excellent. Forcing prerequisites prevents overclaiming. Very few internal benchmarks have this discipline.
- **CFG-A/CFG-B pairing** with same provider/model requirement is correct experimental design.
- **Hard gates separated from numeric scores** prevents composite scores from masking failure modes.
- **Overclaim Guard (§11)** with explicit forbidden phrasings. Rare and valuable.
- **Reviewer integrity considerations** (frozen rubric, anonymized labels) show methodological awareness.
- **Run record schema** (§9) is concrete and machine-readable.

### What is missing

- No pre-registration protocol mentioned. Modern benchmarks pre-register analysis plan before running to prevent p-hacking. Section 10 freezes the rubric but not the statistical plan.
- No "negative control" task family designed to detect overfitting. Every family is aligned to CVF's strengths; no family expects CVF to have zero advantage. This risks measurement bias.
- No repeat-run or variance protocol. Single runs per config per task treat noise as signal.

### Verdict

Strong conceptual structure. Two procedural additions needed: pre-registration and negative controls. One missing layer: within-task variance accounting.

---

## Dimension B — Statistical Validity (2 / 5) — FATAL GAP

### What works

- MVP scope of 20 tasks is appropriately bounded (prevents analysis paralysis).
- MVP organization by family type is sound (productivity, handoff, cost, security, adversarial).
- Run record schema includes token/latency/cost fields for downstream statistical analysis.

### What is missing — specifically fatal

**B1: Sample size justification is absent.**

20 tasks across 8 families = 2.5 tasks per family on average. In statistical terms, this is a design with extremely low power to detect family-level effects. No power analysis is reported. **Required fix:** state minimum power target (e.g., power ≥ 0.8 to detect 15% effect), calculate sample size, justify any deviation.

**B2: Within-task variance is not addressed.**

LLM outputs have noise from temperature, sampling, model updates, and API variance. A single run per task treats noise as signal. No repeat-run protocol is defined. **Required fix:** require N=3 repeat runs per task per config, report median + range + outlier detection rule.

**B3: "Material improvement" threshold is undefined (§1, L4).**

L4 requires "material improvement or risk reduction" but no number is given. 5%? 10%? Statistical significance (p < 0.05)? Without a threshold, the verdict is unfalsifiable. **Required fix:** define material as numerical threshold and specify inference method (absolute delta, relative lift, paired t-test, or non-parametric equivalent).

**B4: No confidence interval or effect-size reporting requirement.**

A score of "4.2 vs 4.0 out of 5" on output quality looks like a difference but may be noise. CIs matter. **Required fix:** require 95% CI reporting for all numeric dimensions, or switch to ordinal comparison (rank test) where CIs are less natural.

**B5: Claim L6 "cross-provider confidence" needs ≥3 providers, not 2.**

Two data points cannot establish a trend. Industry standard (e.g., GLUE, SuperGLUE benchmarks) is ≥3 independent datasets. **Required fix:** raise L6 requirement to 3 provider families, or rename L6 to "two-provider corroboration" with a note that it is directional, not conclusive.

### Verdict

The benchmark is underpowered for L4/L5 claims. 20 tasks cannot statistically support a broad quality claim. This is the primary blocker to QBS-0 acceptance.

---

## Dimension C — Methodological Completeness (2 / 5) — FATAL GAP

### What is missing — specifically fatal

**C1: CFG-A (direct baseline) prompt construction is undefined.**

This is the single most consequential gap. Does CFG-A receive the raw user prompt, or the same enriched prompt CVF sends to the provider? If CFG-B benefits from prompt enrichment, the benchmark measures prompt engineering, not governance control. **Required fix:** define CFG-A explicitly as "user prompt only, no system prompt beyond provider default" and CFG-B as "user prompt + CVF governance overlay + risk scoring." Document the exact prompt used for both.

**C2: Reviewer disagreement protocol is named but not defined (§10).**

"Disagreement handling rule before final verdict" — what is the rule? No inter-rater reliability target is set. **Required fix:** require agreement coefficient (Cohen's κ ≥ 0.6); below that, run third reviewer; below 0.4, mark task INVALID. Define what causes disagreement (rubric interpretation, subjectivity, etc.).

**C3: Cost overhead interpretation lacks bounds.**

Pass criteria: "interpreted alongside control value, not standalone failure." But a 100× cost multiplier is disqualifying regardless of control. **Required fix:** add soft upper bound (e.g., "overhead > 5× requires explicit operator acceptance in final assessment").

**C4: "Severe" in G3 hard gate is undefined.**

G3 states "Zero severe unsafe false negatives" but "severe" is not defined. Does R2 count? Only R3? **Required fix:** map severity to CVF risk classes explicitly — "severe = R3 unsafe execution when BLOCK expected, or R2 with >$1000 cost exposure."

**C5: Risk classification axis scoring is incoherent.**

Section 4.2 scores risk classification correctness as PASS/WARNING/FAIL, but the run schema uses R0–R3. **Required fix:** define a confusion matrix (expected R-class × actual R-class) and grade based on off-diagonal distance (e.g., "one step wrong = WARNING, two+ steps = FAIL").

**C6: No provision for model drift or benchmark expiration.**

Provider models update; benchmark validity decays. No re-run cadence or expiration policy is stated. **Required fix:** add "claims expire 90 days after last run unless re-validated against the same model version."

**C7: Reviewer model versioning is incomplete.**

Section 10 says "record the judge model and prompt" but not the model hash. If judge model updates, reproducibility breaks. **Required fix:** pin judge model by full version (provider_name + model_id + release_date).

### Verdict

Reproducibility and validity are blocked by missing protocol definitions and bounds. The baseline confound (C1) is the single highest-priority fix.

---

## Dimension D — Clarity and Specificity (2 / 5) — FATAL GAP

### Undefined thresholds (blocking QBS-1)

| Item | Current | Required |
|---|---|---|
| "Material improvement" (L4) | Undefined | Numeric: ≥10% lift or ≥1 hard-gate risk avoided |
| "Severe" (G3) | Undefined | R3 unsafe, or R2 with >$1K exposure |
| G4 cost trace "where technically available" | Vague | Define providers/models where cost is available |
| Output quality "rework class" (4.1) | Named but not scored | Weight LIGHT/MODERATE/HEAVY; REJECT = fail |
| Adversarial family pass bar | Unnamed | "CFG-B refusal correctness = 100%, no unsafe bypasses" |
| "Material scope limitation" in PASS_BOUNDED | Vague | Define as "affects <2 task families" or "downstream adoption >50%" |

**Verdict:** Every undefined threshold above must be filled in before a single task is scored. Otherwise, scoring will be inconsistent and the verdict will be challenged.

---

## Dimension E — Alignment With Standards (1 / 5) — FATAL GAP

### What works

- Section 12 lists related existing standards (Non-Coder Value Measurement, Product Value Validation rubric, etc.).

### What is missing — specifically fatal

**E1: No comparison to existing AI benchmark standards.**

HELM (Stanford), MT-Bench (FastChat), AgentBench (Alibaba), and others exist. CVF mentions none. Why not extend or build on an existing standard that has peer legitimacy? **Required fix:** add section comparing CVF's benchmark to HELM, MT-Bench, AgentBench on: claim structure, reproducibility, multi-model scope, and evaluation axioms. State why CVF is building its own rather than extending existing.

**E2: No reference to evaluation methodology standards.**

ML evaluation papers cite standards like Devlin et al. (GLUE), Rogers & Keller (SuperGLUE), or Bang et al. (MultiWOZ). CVF cites none. **Required fix:** add methodology references (minimum 3: GLUE, SuperGLUE, and one LLM benchmark like MT-Bench).

**E3: Adversarial family evaluation method undefined.**

Section 4.3 (Agent Control) measures "bypass resistance" but no adversarial attack taxonomy is provided. MITRE ATLAS or OWASP Top 10 for LLMs would ground this. **Required fix:** define adversarial families using a recognized taxonomy (MITRE ATLAS, OWASP, or CVF-custom but documented).

### Verdict

This benchmark is at risk of being dismissed as non-standard. Grounding in existing evaluation frameworks would massively increase credibility with external reviewers and peer validation prospects.

---

## Critical Confound Issues

### Issue 1: Direct Baseline Prompt Confound

If CFG-A and CFG-B use different prompts, the comparison measures prompt engineering, not governance. This is non-recoverable from the final scores.

**Example of confound:**
- CFG-A: "Analyze this code for security issues. [raw user prompt]"
- CFG-B: "Analyze this code for security issues. [user prompt] RISK_CLASS: [CVF-scored risk]. APPROVED_SCOPE: [governance boundary]. [enriched context]."

CFG-B looks better because it received better input, not because governance adds value.

**Fix required before any run:** Define CFG-A and CFG-B prompts in detail and show they differ only by the governance overlay, not by context/enrichment.

### Issue 2: Evaluation Bias (Output Quality Overweight)

Output Quality is 25% weight and the most subjective axis. With model-assisted judging (§10 allows it), judge bias dominates the aggregate score. A reviewer who knows "this is the CVF output" will score it higher.

**Fix required:** Either lower Output Quality weight to 15%, or require dual-reviewer scoring (one human, one model) with bias-delta capped.

### Issue 3: Adversarial Under-Sampling

Adversarial/bypass family has only 3 tasks. Adversarial robustness research (Goodfellow et al., Carlini & Wagner) shows that 3 attacks cannot distinguish a robust system from one that happens to refuse those 3 patterns.

**Fix required:** Raise adversarial family to 5–6 tasks, or explicitly mark L4/L5 as "not claiming adversarial robustness, only tested on 3 named patterns."

---

## Required Deliverables for Codex

### Deliverable 1 — `docs/reference/CVF_QUALITY_BENCHMARK_SUITE_CRITERIA_V2_METHODOLOGY_2026-05-09.md`

Must contain:

- **Baseline confound resolution:** exact CFG-A and CFG-B prompt definitions, diff'ed to show they differ only in governance overlay
- **Sample size and power analysis:** minimum power target, sample size per family, justification for MVP=20
- **Repeat-run and variance protocol:** within-task repeat count (recommend N≥3), outlier detection rule, median + range reporting
- **Statistical inference method:** paired t-test, Mann-Whitney U, ordinal comparison, or CI-based approach — explicit and justified
- **All undefined thresholds filled in:** table mapping (Term → Current → Specified Value) for material improvement, severe, rework weight, etc.
- **Model drift and expiration policy:** re-run cadence (recommend 90 days), model version pinning, claim invalidation rules

### Deliverable 2 — `docs/reference/CVF_QUALITY_BENCHMARK_SUITE_CRITERIA_ALIGNMENT_STANDARDS_2026-05-09.md`

Must contain:

- **Comparison to HELM, MT-Bench, AgentBench:** what CVF does differently and why those alternatives were not extended
- **Methodology references:** minimum 3 citations (GLUE, SuperGLUE, MT-Bench or equivalent)
- **Adversarial taxonomy:** MITRE ATLAS / OWASP / CVF-custom mapping for the bypass/adversarial family
- **Peer-review readiness:** reviewer protocol that would satisfy an external benchmark committee

### Deliverable 3 — `docs/reference/CVF_QUALITY_BENCHMARK_SUITE_CRITERIA_V2_FINAL_2026-05-09.md`

Updated candidate incorporating Deliverables 1 & 2, plus:

- L6 requirement raised to 3 provider families (or renamed + bounded)
- Adversarial family raised to 5–6 tasks (or explicitly limited claim boundary)
- Pre-registration section added (when analysis plan is frozen before any scoring)
- Negative control task family defined (a task family where CVF is expected to have zero advantage)
- Output Quality weight adjusted or dual-reviewer requirement added (to prevent judge-bias dominance)

---

## Stop Rules

Codex must stop and return to operator review if any of the following occur:

1. **Baseline confound unresolved:** CFG-A and CFG-B prompt definitions differ in anything other than governance overlay. Do not proceed with QBS-1 until this is locked.
2. **Sample size justified as "20 tasks is enough":** This requires power analysis with numbers, not assertion. Justification of MVP bounds is required, not skipped.
3. **"Material improvement" defined as vague:** Must be a number (e.g., "≥10% lift") or a protocol (e.g., "paired t-test p < 0.05"). Vague is not acceptable.
4. **Comparison to existing standards skipped:** Do not claim this is peer-comparable without showing how it differs from HELM/MT-Bench/AgentBench.
5. **Adversarial family remains 3 tasks:** Either raise to 5–6, or add explicit claim boundary ("adversarial robustness not claimed, only tested on 3 named patterns").

---

## Non-Claims

This review assesses the criteria document's methodological rigor only. It does not assess:

- Whether the specific axes (output quality, governance control, etc.) are the right ones to measure CVF's value — that is a substantive question for operator review.
- Whether a 20-task MVP is sufficient for CVF's business needs — that is a product/strategy decision.
- What the actual QBS-4 results will be — only the benchmark design can be assessed now.

---

## Open Questions for Codex Rebuttal

1. Why was sample size set to 20 tasks? What power analysis justifies this? (Or is MVP explicitly acknowledged as underpowered?)
2. What is the exact CFG-A prompt? How does it differ from CFG-B beyond governance overlay?
3. Why not extend HELM or MT-Bench rather than build a new benchmark?
4. Who is the intended reviewer for QBS-0 acceptance? (Operator only, or external benchmark committee?)
5. At what overhead ratio (cost CFG-B / cost CFG-A) should the benchmark recommend stopping the evaluation?
6. Should the L4/L5 claims be scoped as "promising, directional, not statistically significant" given the 20-task MVP?

---

## Verdict

**Conditional READY_FOR_REVIEW_WITH_MATERIAL_GAPS.**

The conceptual structure is sound. The claim hierarchy is disciplined. The overclaim guards are strong. But the statistical and methodological gaps are material and must be closed before QBS-1 implementation.

Current status blocks moving to "ACCEPTED_FOR_QBS_0" without the three deliverables above.

---

## Authorization Boundary

This review authorizes Codex to:
- File rebuttal against the 6 open questions
- Provide the three deliverables
- NOT begin QBS-1 until operator re-reviews the v2 criteria

Next step: Codex rebuttal → operator review → QBS-0 decision → QBS-1 roadmap.
