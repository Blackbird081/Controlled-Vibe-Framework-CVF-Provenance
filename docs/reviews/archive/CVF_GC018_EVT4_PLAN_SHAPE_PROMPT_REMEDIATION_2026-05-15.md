# CVF GC-018 — EVT-4 Plan-Shape Prompt Remediation

**Date:** 2026-05-15  
**Status:** EXECUTED - PARTIAL REMEDIATION ONLY  
**Scope:** Continue F-1 remediation after the depth-target EVT-4 run still failed parity.

## Authorization

User agreed to continue fixing F-1 after reviewing the 2026-05-14 handoff and
Codex's follow-up diagnosis.

## Root-Cause Finding Before Code Change

The latest live run
`docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_DEPTH_TARGET_EVIDENCE_2026-05-14.json`
improved median `CFG-B - CFG-A` from `-0.32` to `-0.16` but still failed the
preregistered `>= -0.05` rule.

Reviewer rationales show the remaining gap is concentrated in task-shape
mismatch:

- `Ops plan`, `Retention plan`: strategy template returns strategic analysis
  instead of implementation plan with tasks, metrics, and checkpoints.
- `Channel choice`: comparison is too general and lacks option-by-option
  activation steps and decision criteria.
- `FAQ plan`: documentation template returns a general guide instead of a real
  FAQ outline with concrete questions and answers.
- `Acceptance criteria`: documentation template returns operational guidance
  instead of testable criteria.

## Allowed Work

- Update the runtime prompt contract to add deterministic task-shape guidance
  for trusted non-coder templates when intent/input text asks for plan,
  comparison, prioritization, FAQ, or acceptance-criteria deliverables.
- Add unit tests proving the prompt contains those shape-specific requirements.
- Run targeted tests, typecheck, lint, and corrected live EVT-4 rerun if
  feasible.

## Boundaries

- No QBS rerun.
- No hard-gate or enforcement threshold change.
- No provider routing change.
- No output-validator change.
- No broad template registry rewrite.
- No raw API keys printed or committed.
- Do not claim quality parity unless the live evidence meets the registered
  rule.

## Exit Criteria

- [x] Plan-like prompts require timeline/action/owner/metric/acceptance-check
      detail.
- [x] FAQ prompts require concrete FAQ entries, not just how-to guidance.
- [x] Acceptance-criteria prompts require observable testable criteria.
- [x] Verification results and live evidence status are recorded.

## Implementation

Runtime code changed in
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-prompt-contract.ts`.

The prompt contract now:

- Treats trusted form output templates as minimum outlines, not compression
  targets.
- Gives trusted non-coder form templates a bounded operator-ready depth target.
- Adds task-shape guidance for plan, comparison, FAQ, acceptance-criteria,
  prioritization, and persona requests.
- Places task-shape guidance after the rendered template skeleton so it can
  override generic SWOT/risk/overview/documentation wrapper headings when those
  headings conflict with the requested deliverable shape.

Unit coverage was added in
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-prompt-contract.test.ts`.

## Live Evidence

- Plan-shape rerun:
  `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_PLAN_SHAPE_EVIDENCE_2026-05-15.json`
  and summary
  `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_PLAN_SHAPE_SUMMARY_2026-05-15.md`.
  Result: 20/20 live receipts, 0 safety failures, median delta `-0.16`.
- Shape-override rerun:
  `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_SHAPE_OVERRIDE_EVIDENCE_2026-05-15.json`
  and summary
  `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_SHAPE_OVERRIDE_SUMMARY_2026-05-15.md`.
  Result: 20/20 live receipts, 0 safety failures, median delta `-0.16`.

The preregistered `>= -0.05` decision rule was **not** met.

## Negative Experiments Not Retained

Two additional broad prompt attempts were tested and rejected:

- Operator-checks global footer instruction:
  `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_OPERATOR_CHECKS_SUMMARY_2026-05-15.md`.
- Trusted non-coder system appendix:
  `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_SYSTEM_APPENDIX_SUMMARY_2026-05-15.md`.

Both preserved live receipts and safety but worsened weak plan-like tasks such
as `Ops plan` and `Retention plan`. The runtime code intentionally does not
retain those broad instructions.

## Verification

- `node --check scripts/run_evt4_output_quality_ab.js` PASS.
- `npx vitest run src/lib/execute-prompt-contract.test.ts src/app/api/execute/route.test.ts`
  PASS (33/33).
- `npx tsc --noEmit` PASS.
- `npm run lint` PASS with one pre-existing warning in
  `src/app/api/system/jobs/route.test.ts` for unused `_request`.
- `git diff --check` PASS with Windows line-ending warnings for
  `AGENT_HANDOFF_V4_2026-05-12.md` and
  `scripts/run_evt4_output_quality_ab.js`.

## Result

F-1 is partially remediated but not closed. The measurable gap improved from
the original `-0.28` / corrected-template `-0.32` range to a stable `-0.16`,
but CVF-governed output quality still does not meet parity with the bare
provider for the EVT-4 frozen corpus.

Next F-1 work should use a fresh scope decision for template-specific contract
redesign or new trusted template families for plan/FAQ/acceptance-criteria
deliverables. Further broad global prompt text is not supported by the current
evidence.
