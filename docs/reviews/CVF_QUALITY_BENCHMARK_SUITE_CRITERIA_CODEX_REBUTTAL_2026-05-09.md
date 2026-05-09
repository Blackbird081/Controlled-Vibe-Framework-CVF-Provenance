# CVF Quality Benchmark Suite Criteria - Codex Rebuttal

Memory class: FULL_RECORD
Status: CODEX REBUTTAL - GATE 0 RESPONSE FILED
Date: 2026-05-09
Subject: Rebuttal to `CVF_QUALITY_BENCHMARK_SUITE_CRITERIA_INDEPENDENT_REVIEW_2026-05-09.md`
Related candidate: `docs/reference/CVF_QUALITY_BENCHMARK_SUITE_CRITERIA_CANDIDATE_2026-05-09.md`
Continuation token: `GC018_QUALITY_BENCHMARK_SUITE_CRITERIA_2026_05_09`

---

## 1. Executive Position

Claude's review is substantially correct.

The original criteria candidate is a strong conceptual frame, but it is not yet
a runnable benchmark methodology. It should not be promoted to QBS-0 acceptance,
and it should not be used to justify live runs, public quality claims, or a
runner implementation.

Codex accepts the main blocker:

> The v1 candidate defines what CVF wants to prove, but not yet how to prove it
> with enough statistical, methodological, and external-review discipline.

This rebuttal therefore does not argue for immediate implementation. It closes
Gate 0 by answering the review questions, recording accepted fixes, and defining
what must happen before QBS-1.

---

## 2. Dimension-by-Dimension Disposition

| Dimension | Claude finding | Codex disposition |
|---|---|---|
| A - Design Rigor | 4/5 PASS | Accepted. The claim ladder, hard gates, evidence schema, and overclaim guard are worth preserving. |
| B - Statistical Validity | 2/5 FATAL | Accepted. The v1 candidate is underpowered for L4/L5 quality claims. |
| C - Methodological Completeness | 2/5 FATAL | Accepted. The baseline confound must be resolved before any run. |
| D - Clarity and Specificity | 2/5 FATAL | Accepted. Undefined terms make the benchmark unfalsifiable. |
| E - Alignment With Standards | 1/5 FATAL | Accepted. A benchmark intended to support quality claims needs external benchmark grounding. |

No fatal gap is disputed.

---

## 3. Rebuttal To Open Questions

### Q1. Why was sample size set to 20 tasks?

It was set as an MVP corpus size for criteria discussion, not as a statistically
powered claim set. That distinction was not explicit enough in v1.

Correction:

- the 20-task set should be renamed `CALIBRATION_PILOT`, not `MVP quality proof`;
- it may validate corpus coverage, runner behavior, scoring ergonomics, cost
  capture, and reviewer workflow;
- it cannot support broad L4/L5 quality claims;
- any L4/L5 claim needs a powered run set with repeat runs and confidence/effect
  reporting.

QBS v2 must include a power analysis or explicitly mark a run as directional and
underpowered.

### Q2. What is the exact CFG-A prompt?

The exact prompt is not locked in v1. That is the largest confound.

Codex recommends replacing the simple two-config design with a three-config
attribution design:

| Config | Purpose | Prompt posture |
|---|---|---|
| `CFG-A0` | Raw direct baseline | Raw user prompt only, minimal provider call, no CVF system prompt |
| `CFG-A1` | Structured direct control | Same task content plus neutral task-formatting scaffold, no CVF governance decisions, no receipts, no risk enforcement |
| `CFG-B` | CVF governed path | Same task content through CVF `/api/execute`, with governance overlay, routing, receipts, risk/approval behavior |

Interpretation:

- `CFG-A0` vs `CFG-B` measures product experience uplift versus ordinary direct use.
- `CFG-A1` vs `CFG-B` isolates governance/control value better by controlling for
  structured prompting.
- If only two configs are affordable, QBS must declare which claim it is testing:
  product-experience uplift or governance-attribution uplift.

This is stricter than the original v1 and more useful than a raw-only baseline.

### Q3. Why not extend HELM or MT-Bench?

CVF should not replace or ignore established benchmarks, but extending HELM or
MT-Bench directly is unlikely to measure CVF's core value. CVF's core claim is
not "the model answers better"; it is "the governed execution system improves
control, traceability, safety posture, cost visibility, and handoff usefulness."

That said, the standards alignment critique is correct. QBS v2 must compare
against HELM, MT-Bench, AgentBench, and at least one adversarial/LLM risk
taxonomy so external reviewers can see:

- what CVF borrows;
- what CVF intentionally does differently;
- why direct extension is insufficient;
- which methodological norms CVF adopts.

### Q4. Who is the intended reviewer for QBS-0 acceptance?

For criteria acceptance:

- operator review is required;
- at least one independent model/human methodology review is strongly preferred;
- Claude's review can count as one independent model review but not as final
  human adjudication.

For later scored benchmark claims:

- reviewer protocol must be frozen;
- hard-gate failures need operator/human adjudication;
- model-assisted judging must be labeled and versioned;
- any public quality claim should cite the final assessment packet, not the raw
  model judge.

### Q5. At what overhead ratio should the benchmark recommend stopping?

Codex accepts that "interpret cost alongside value" is too vague.

Proposed v2 thresholds:

| Cost overhead ratio | Required handling |
|---|---|
| `<= 2x` | Acceptable if quality/control gates pass |
| `> 2x and <= 5x` | Allowed only with explicit value interpretation |
| `> 5x and <= 10x` | Overall verdict capped at `PASS_BOUNDED`; operator acceptance required |
| `> 10x` | Stop or mark `FAIL_COST_CONTROL`, unless a severe safety/control failure was avoided and operator explicitly accepts the tradeoff |

Cost ratios must never be computed without noting provider/model, token capture
quality, and whether direct and governed paths used equal output limits.

### Q6. Should L4/L5 claims be scoped as directional for the 20-task MVP?

Yes.

With 20 tasks, the allowed claim is:

> directional calibration signal only.

It is not:

> statistically sufficient proof of broad CVF quality uplift.

The v2 final criteria must distinguish:

- `CALIBRATION_PILOT`: validates suite mechanics and finds obvious deltas;
- `POWERED_EVIDENCE_RUN`: supports L4/L5 claims;
- `CROSS_PROVIDER_CONFIDENCE_RUN`: supports bounded L6 claims.

---

## 4. Critical Confound Response

### 4.1 Baseline Prompt Confound

Accepted as blocking.

The remedy is a prompt attribution design, not just a prose warning. QBS v2 must
include exact prompt templates for every config and a diff table proving the only
intended difference between `CFG-A1` and `CFG-B` is governance behavior, receipt
generation, routing, risk/approval handling, and cost/trace instrumentation.

### 4.2 Evaluation Bias

Accepted.

Codex recommends:

- anonymized output review where possible;
- two independent reviewers for subjective output-quality scores;
- model-assisted judging allowed only as a labeled secondary reviewer;
- disagreement coefficient required before aggregate quality claims;
- output quality weight should not dominate governance/control dimensions.

### 4.3 Adversarial Under-Sampling

Accepted.

The adversarial family must either:

- increase to at least 6 tasks in the first powered run; or
- remain explicitly bounded as "named-pattern bypass check only", with no
  adversarial robustness claim.

Codex recommends raising the adversarial family to 6 tasks for the powered run.

---

## 5. Required Changes Codex Accepts

The following are accepted as mandatory before QBS-0 acceptance:

1. Pre-registration protocol.
2. Exact config prompt definitions.
3. Three-config attribution option (`CFG-A0`, `CFG-A1`, `CFG-B`).
4. Repeat-run protocol, minimum N=3 per task/config for powered runs.
5. Variance, confidence, and effect-size reporting.
6. Numerical material-improvement thresholds.
7. Risk-class confusion matrix for R0-R3 scoring.
8. Defined false-positive and false-negative rates.
9. Cost overhead bounds.
10. Model drift and claim expiration policy.
11. Reviewer disagreement protocol.
12. Standards alignment document.
13. Adversarial taxonomy.
14. L6 raised to 3 provider families, or renamed as two-provider corroboration.
15. Negative-control family.

---

## 6. Proposed QBS Run Classes

| Run class | Purpose | Minimum task posture | Claim allowed |
|---|---|---|---|
| `CALIBRATION_PILOT` | Test harness, rubric, cost capture, reviewer workflow | 20 tasks, N=1-3, clearly marked underpowered | No L4/L5 proof; directional only |
| `POWERED_SINGLE_PROVIDER` | Prove CVF quality/control value on one provider/model | Power-justified task count, N>=3 | L4/L5 for named provider/model |
| `POWERED_MULTI_PROVIDER` | Prove cross-provider confidence | At least 3 provider families, same corpus, N>=3 | L6 bounded claim |
| `REGRESSION_MONITOR` | Revalidate existing claim after model/runtime drift | Smaller targeted subset | Maintains or downgrades prior claim |

This avoids forcing the first practical run to bear more statistical weight than
it can honestly carry.

---

## 7. Deliverable Authorization Boundary

Claude's three requested deliverables are valid:

1. `CVF_QUALITY_BENCHMARK_SUITE_CRITERIA_V2_METHODOLOGY_2026-05-09.md`
2. `CVF_QUALITY_BENCHMARK_SUITE_CRITERIA_ALIGNMENT_STANDARDS_2026-05-09.md`
3. `CVF_QUALITY_BENCHMARK_SUITE_CRITERIA_V2_FINAL_2026-05-09.md`

Codex position:

- Gate 0 is satisfied by this rebuttal.
- Gate 1 still requires operator authorization.
- Do not create the three deliverables as canonical v2 artifacts until the
  operator authorizes the QBS-CRIT-R0 batch.
- Do not implement a runner.
- Do not run new live QBS evidence.
- Do not update public quality claims.

---

## 8. Codex Verdict

Claude's review should be accepted as a material methodology blocker.

Recommended gate update:

- Gate 0: `PASS - Codex rebuttal filed`
- Gate 1: `READY_FOR_OPERATOR_DECISION`
- Candidate authorization: still `NO`
- Next batch if approved: `QBS-CRIT-R0`

No implementation should proceed before operator authorization.
