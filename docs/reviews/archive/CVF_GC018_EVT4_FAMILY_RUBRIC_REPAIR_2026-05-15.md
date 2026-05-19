# CVF GC-018 — EVT-4 Family Rubric Repair

**Date:** 2026-05-15  
**Status:** EXECUTED - PARITY NOT MET  
**Scope:** Continue F-1 after template-family split and two-pass Phase 0 both
failed to meet parity.

## Authorization

User instructed Codex to run the roadmap autonomously using the available live
API keys and not stop after each intermediate step.

## Evidence Before Code Change

Latest Phase 0 two-pass evidence:

- `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_TWO_PASS_PHASE0_EVIDENCE_2026-05-15.json`
- Median `CFG-B - CFG-A = -0.16`.
- 20/20 final receipts.
- 20/20 expansion receipt pairs.
- 0 safety failures.
- Runtime two-pass not authorized because the registered `>= -0.05` rule was
  not met.

Reviewer rationales now repeatedly cite:

- Missing detailed actionable steps.
- Weak task fit for MVP scope and backlog triage.
- Personas lacking next actions and acceptance checks.
- Operator plans lacking sufficiently specific task descriptions and checks.
- Competitor/differentiation reviews lacking action steps.

## Allowed Work

- Repair only the underperforming family output rubrics/skeletons:
  `feature_prioritization`, `user_persona`, `operator_plan`, and
  `competitor_review`.
- Add exact sections that force implementation steps, verification signals,
  acceptance checks, and next actions.
- Keep governance, routing, QBS, hard gates, provider routing, and output
  validation unchanged.
- Run targeted tests, typecheck, lint, and live EVT-4 rerun.

## Exit Criteria

- [x] Targeted family templates contain actionability and verification sections.
- [x] Unit/template governance tests pass.
- [x] Live EVT-4 evidence is recorded.
- [x] Do not claim F-1 closure unless median `CFG-B - CFG-A >= -0.05` with
      20/20 receipts and 0 safety failures.

## Implementation

Updated targeted family output contracts:

- `feature_prioritization`: added feature detail cards, explicit MVP scope,
  implementation plan, and acceptance checks.
- `user_persona`: added jobs-to-be-done, journey/decision moments,
  product/marketing actions, and acceptance checks.
- `operator_plan`: added detailed timeline, operating checklist, richer
  first-72-hour structure, and acceptance checks.
- `competitor_review`: added competitor implications, differentiation action
  table, action plan, and validation checks.

No QBS, hard-gate, provider routing, output-validator, or production two-pass
runtime changes were made.

## Verification

- `npx vitest run src/lib/templates/governance-enforcement.test.ts src/lib/front-door-template-standard.test.ts src/lib/templates/index.test.ts src/lib/execute-prompt-contract.test.ts`
  PASS (42/42).
- `npx tsc --noEmit` PASS.
- `npm run lint` PASS with one pre-existing warning in
  `src/app/api/system/jobs/route.test.ts` for unused `_request`.

## Live Evidence

One-pass family-rubric repair:

- Evidence:
  `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_FAMILY_RUBRIC_REPAIR_EVIDENCE_2026-05-15.json`
- Summary:
  `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_FAMILY_RUBRIC_REPAIR_SUMMARY_2026-05-15.md`
- Result: 20/20 live receipts, 0 safety failures, median delta `-0.16`.

Rubric repair plus two-pass expansion:

- Evidence:
  `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_RUBRIC_TWO_PASS_EVIDENCE_2026-05-15.json`
- Summary:
  `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_RUBRIC_TWO_PASS_SUMMARY_2026-05-15.md`
- Result: 20/20 final receipts, 20/20 expansion receipt pairs, 0 safety
  failures, median delta `-0.16`.

## Conclusion

F-1 remains open. This tranche removed the worst outliers from the one-pass
run, but the median stayed fixed at `-0.16`. Combining the repaired family
rubrics with two-pass expansion also stayed at `-0.16`.

Current evidence says F-1 cannot be closed by more prompt/template/output-length
changes alone under the existing EVT-4 scoring setup. The next owner decision
should be one of:

- Define a sharper automated quality rubric and make closure depend on that
  rubric rather than a single LLM judge preference.
- Change the product claim from "quality parity" to a bounded safety/audit
  claim with a documented `-0.16` quality trade-off.
- Use a stronger provider/model lane for both CFG-A and CFG-B and
  preregister a new comparison.
