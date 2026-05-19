# CVF GC-018 — EVT-4 Prompt Contract Remediation

**Date:** 2026-05-14  
**Status:** APPROVED BY USER FOR EXECUTION  
**Scope:** F-1 runtime prompt-contract remediation for trusted non-coder form output quality.

## Authorization

User authorized proceeding from F-1. The template-payload diagnostic rerun proved
that the original EVT-4 result was partly affected by a hard-coded
`documentation` harness payload, but the corrected live run still failed the
decision rule: median `CFG-B - CFG-A = -0.32`, 20/20 live receipts, 0 safety
failures.

## Root-Cause Finding Before Code Change

The remaining quality gap is not caused by output validation: corrected CFG-B
outputs pass live execution and validation, but reviewer rationales repeatedly
cite missing detailed steps, specificity, metrics, and acceptance checks.

The remaining gap is in the runtime template prompt contract:

- `buildExecutionPrompt()` tells the provider to follow `outputTemplate` "more
  strongly than generic sectioning advice."
- Some trusted-form skeletons are intentionally terse and omit the EVT-4 task's
  requested "assumptions, concrete next steps, and acceptance checks."
- The model treats those skeletons as a compression target instead of a minimum
  outline, especially for `strategy_analysis`, `feature_prioritization`,
  `user_persona`, and `documentation`.

## Allowed Work

- Update `src/lib/execute-prompt-contract.ts` so template skeletons are treated
  as minimum structure, not maximum depth.
- Require task-specific detail, assumptions, concrete next actions, and
  acceptance checks when the intent asks for an actionable non-coder output.
- Add/update unit coverage for the prompt contract.
- Rerun targeted tests and a live corrected EVT-4 evidence run if feasible.
- Preserve all original and diagnostic evidence files.

## Boundaries

- No QBS rerun.
- No hard-gate or enforcement threshold change.
- No provider routing change.
- No `output-validator` change.
- No template registry rewrite.
- No raw API keys printed or committed.
- Any claim must remain scoped to the EVT-4 R0/R1 corpus and the reviewer mode.

## Exit Criteria

- [x] Prompt contract states that output templates are minimum outlines, not
      compression targets.
- [x] Unit tests prove trusted form prompts preserve template headings while
      requiring depth/acceptance checks.
- [x] Corrected live evidence is generated:
      `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_PROMPT_CONTRACT_EVIDENCE_2026-05-14.json`
      and
      `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_DEPTH_TARGET_EVIDENCE_2026-05-14.json`.

## Post-Run Result

The prompt-contract remediation improved the corrected median delta from
`-0.32` to `-0.16`, with 20/20 CFG-B live receipts and 0 safety failures. It
did not satisfy the preregistered `>= -0.05` decision rule. The remaining gap is
concentrated in plan-like tasks routed through generic analysis/documentation
families (`Ops plan`, `Channel choice`, `Retention plan`, `FAQ plan`,
`Acceptance criteria`), where reviewer rationale still cites missing
task-specific implementation steps, metrics, and acceptance checks.
