# CVF GC-018 — EVT-4 Template Family Split

**Date:** 2026-05-15  
**Status:** EXECUTED - EVIDENCE RECORDED, PARITY NOT MET  
**Scope:** Continue F-1 after prompt-contract remediation stabilized at median
`CFG-B - CFG-A = -0.16` but did not meet parity.

## Authorization

User instructed Codex to continue according to the roadmap after commit
`a1959a71`.

## Finding Before Code Change

The previous F-1 tranches eliminated or bounded the original suspected layers:

- Not QBS.
- Not hard gates.
- Not provider routing.
- Not output validator.
- Not only the all-documentation harness wrapper.
- Broad global prompt and system-prompt appendix experiments were negative.

The remaining evidence points to template-family mismatch. The frozen EVT-4
tasks ask for specific deliverables, but several are still routed through broad
legacy forms:

- Plan tasks through `strategy_analysis`.
- Decision/comparison tasks through `strategy_analysis`.
- FAQ and acceptance-criteria tasks through `documentation`.

## Allowed Work

- Add narrow trusted form families for explicit non-coder deliverable shapes:
  `operator_plan`, `decision_memo`, `faq_outline`, and
  `acceptance_criteria`.
- Add matching trusted-form routing entries with narrow activation patterns.
- Add unit coverage for routing, prompt rendering, and token budget inclusion.
- Update the EVT-4 harness to route frozen tasks to these specific families
  when the shape is explicit.
- Run targeted tests, typecheck, lint, and a live EVT-4 rerun if feasible.

## Boundaries

- No QBS rerun.
- No hard-gate or enforcement threshold change.
- No provider routing change.
- No output-validator change.
- No broad template registry rewrite outside the four bounded families.
- No raw API keys printed or committed.
- Do not claim quality parity unless live evidence meets the registered
  `>= -0.05` rule.

## Implementation

Runtime/template code changed:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates/business.ts`
  added `operator_plan` and `decision_memo`.
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates/content.ts`
  added `faq_outline` and `acceptance_criteria`.
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/trusted-form-corpus.ts`
  added bounded activation entries for the four new families.
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/data/skill-template-map.json`
  added mappings for the four new families and closed the pre-existing RULE-T4
  mapping drift for `meeting_notes`, `job_description`, and
  `performance_review`.
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-route-budget.ts`
  and `execute-prompt-contract.ts` now treat the new families as trusted
  non-coder templates.
- `scripts/run_evt4_output_quality_ab.js` now maps explicit EVT-4 frozen tasks
  to the new family IDs where applicable.

## Live Evidence

Evidence:
`docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_TEMPLATE_FAMILY_SPLIT_EVIDENCE_2026-05-15.json`

Summary:
`docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_TEMPLATE_FAMILY_SPLIT_SUMMARY_2026-05-15.md`

Result:

- Completed pairs: 20/20.
- CFG-B live receipts: 20.
- Safety failures: 0.
- Median normalized delta: `-0.16`.
- Decision rule met: `false`.

The family split did not close F-1. It also showed that exact template family
selection alone is insufficient: several remaining failures cite thin depth,
missing actionable detail, and weaker specificity, especially
`feature_prioritization`, `user_persona`, and `operator_plan` lanes.

## Verification

- `node --check scripts/run_evt4_output_quality_ab.js` PASS.
- `npx vitest run src/lib/trusted-form-corpus.test.ts src/lib/form-routing.test.ts src/lib/execute-prompt-contract.test.ts src/app/api/execute/route.test.ts`
  PASS (138/138).
- `npx vitest run src/lib/templates/governance-enforcement.test.ts src/lib/front-door-template-standard.test.ts src/lib/templates/index.test.ts src/lib/trusted-form-corpus.test.ts src/lib/form-routing.test.ts src/lib/execute-prompt-contract.test.ts src/app/api/execute/route.test.ts`
  PASS (169/169).
- `npx tsc --noEmit` PASS.
- `npm run lint` PASS with one pre-existing warning in
  `src/app/api/system/jobs/route.test.ts` for unused `_request`.

## Exit Criteria

- [x] New families exist as concrete form templates with exact output
      contracts.
- [x] `TRUSTED_FORM_MAP` has bounded activation patterns and tests.
- [x] EVT-4 harness maps explicit frozen tasks to the new families.
- [x] Verification and live evidence status are recorded.

## Result

F-1 remains open. This tranche proves that family split alone does not meet the
registered parity rule. The next bounded hypothesis should focus on the
underperforming family-specific output contracts and scoring rubrics:

- `feature_prioritization`: needs richer feature descriptions and
  implementation steps.
- `user_persona`: needs actionable next steps and acceptance checks.
- `operator_plan`: needs deeper phase detail and measurable checks.

Do not claim EVT-4 quality parity from this packet.
