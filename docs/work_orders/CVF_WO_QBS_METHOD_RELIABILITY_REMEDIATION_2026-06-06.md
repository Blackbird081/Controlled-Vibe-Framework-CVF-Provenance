# CVF WO QBS Method Reliability Remediation

Memory class: POINTER_RECORD

Status: BACKLOG_SOURCE_VERIFIED

## Purpose

Repair benchmark reliability and corpus-power boundaries before another public
quality claim is made from QBS evidence.

## Authority Chain

- Operator P1-P5 remediation request, 2026-06-06.
- QBS independent review and rerun remediation history.
- Active handoff: `AGENT_HANDOFF_V16_2026-06-06.md`.

## Objective

Repair the benchmark-method claim boundary around reviewer reliability and the
48-task corpus before any renewed public quality claim.

## Agent Roles

Orchestrator owns benchmark claim policy. Implementer owns methodology and
checker updates. Reviewer validates statistics, corpus power, and F-1 stop-rule
compatibility.

## Required First Reads

- `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`
- `docs/reviews/archive/CVF_QBS_PUBLIC_METHODOLOGY_INDEPENDENT_REVIEW_2026-05-09.md`
- `docs/reviews/archive/CVF_QBS_PUBLIC_METHODOLOGY_CODEX_REBUTTAL_2026-05-09.md`
- `docs/reviews/archive/CVF_QBS_RERUN_REMEDIATION_PROPOSAL_2026-05-11.md`
- `docs/reviews/CVF_F1_OUTPUT_QUALITY_PARITY_CLOSURE_NOT_MET_2026-05-15.md`

## Pre-Flight Checks

- `rg -n "kappa|48-task|aggregate-only|quality parity" docs/benchmark docs/reviews scripts`
- confirm no broad F-1 tuning is reopened;
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base <baseHead> --head HEAD`.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| 48-task corpus supports aggregate comparison only | `docs/reviews/archive/CVF_QBS_PUBLIC_METHODOLOGY_INDEPENDENT_REVIEW_2026-05-09.md` | lines 88-95 | `48-task corpus` | QBS methodology review | ACCEPT |
| Ordinal reviewer statistic should be ordinal alpha or weighted kappa at 0.60 | `docs/reviews/archive/CVF_QBS_PUBLIC_METHODOLOGY_INDEPENDENT_REVIEW_2026-05-09.md` | lines 237-243 | `quadratic-weighted Cohen's kappa` | QBS methodology review | ACCEPT |
| Prior rebuttal accepted aggregate-only claim boundary | `docs/reviews/archive/CVF_QBS_PUBLIC_METHODOLOGY_CODEX_REBUTTAL_2026-05-09.md` | line 42 | `aggregate-only rule` | QBS rebuttal | ACCEPT |
| Later proposal lowered aggregate kappa gate to 0.55 | `docs/reviews/archive/CVF_QBS_RERUN_REMEDIATION_PROPOSAL_2026-05-11.md` | lines 584-587, 695-704 | `aggregate kappa` | QBS rerun proposal | ACCEPT_WITH_CONFLICT |
| Later proposal withdrew per-family kappa threshold | `docs/reviews/archive/CVF_QBS_RERUN_REMEDIATION_PROPOSAL_2026-05-11.md` | lines 584, 700-704 | `per-family kappa` | QBS rerun proposal | ACCEPT |

## Required Remediation

1. Restore the public quality-claim gate to ordinal alpha or quadratic-weighted
   kappa >= 0.60 unless a new independent methodology review approves a lower
   gate.
2. Keep the 48-task corpus claim boundary aggregate-only.
3. Treat per-family rows as diagnostics unless a separately powered family
   corpus exists.
4. Add an explicit no-parity claim boundary aligned with the F-1 stop rule.
5. Add reviewer calibration anchors before any new live benchmark run.

## Forbidden Scope

- Do not reopen broad F-1 prompt/template/model/token tuning.
- Do not claim output-quality parity from the existing QBS evidence.
- Do not publish family-level effects from the 48-task corpus.

## Write Ownership

Allowed after release: QBS methodology docs, claim ladder docs, benchmark
checker scripts, calibration packets, and focused benchmark receipts.

Forbidden without new authority: runtime prompt tuning, model/token budget
changes, public quality claims, and full live benchmark reruns.

## Execution Plan

1. Reconcile the 0.60 independent-review gate with later 0.55 proposal.
2. Update methodology and claim ladder to keep aggregate-only power boundaries.
3. Add or update checker logic for reviewer agreement reporting.
4. Add reviewer calibration anchors.
5. Run a bounded benchmark only after method gates pass.

## Evidence Requirements

- updated methodology or claim ladder diff;
- reviewer calibration receipt;
- agreement report with aggregate ordinal reliability statistic;
- corpus power statement;
- live/provider run evidence only after the methodology gate is repaired.

## Acceptance Criteria

- Public quality claims require ordinal reliability >= 0.60 or a new
  independent-review waiver.
- 48-task evidence is labeled aggregate-only.
- Per-family rows are diagnostics unless a powered family corpus exists.
- F-1 stop rule remains intact.

## Review Gate

Reviewer must reject benchmark closure if agreement statistics are below the
claim gate and the artifact still asks for public quality lift or parity.

## Closure Checklist

- [x] Backlog packet source facts verified.
- [ ] Methodology/claim ladder updated.
- [ ] Calibration evidence produced.
- [ ] Agreement checker/report updated.
- [ ] Autorun and benchmark-specific gates passed.

## Return-To-Orchestrator Conditions

Return if the team wants to lower the 0.60 public gate, reopen broad F-1 tuning,
or publish family-level claims without an expanded powered corpus.

## operator.checkpoint.waiver

Required before live benchmark rerun, public quality claim, corpus expansion
budget, or any change to the F-1 stop-rule boundary.

## Claim Boundary

This packet authorizes benchmark-method remediation planning. It does not claim
quality parity, product quality lift, or benchmark-family power.
