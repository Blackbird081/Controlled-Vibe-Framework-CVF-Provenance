# CVF GC-018 — EVT-4 Deliverable Contract Remediation

**Date:** 2026-05-15  
**Status:** EXECUTED - PARTIAL REMEDIATION ONLY  
**Scope:** Continue F-1 after task-shape guidance stabilized EVT-4 at `-0.16` but did not meet parity.

## Authorization

User instructed Codex to continue after the 2026-05-15 F-1 partial
remediation result.

## Root-Cause Finding Before Code Change

The retained task-shape prompt contract improved the corrected-template
quality gap to `-0.16`, but did not meet the preregistered `>= -0.05` rule.

The remaining weak tasks still align with generic template skeletons:

- `Ops plan` and `Retention plan` are routed through `strategy_analysis`, whose
  rendered skeleton still centers SWOT/risk/recommendation sections.
- `Channel choice` and `Launch options memo` need a decision/comparison memo,
  not a general strategy analysis packet.
- `FAQ plan` and `Acceptance criteria` are routed through `documentation`, whose
  rendered skeleton still centers an operational documentation packet.

The likely residual cause is not safety, routing, QBS, hard gates, provider
choice, or output validation. It is the mismatch between the requested
deliverable shape and the primary rendered output contract.

## Allowed Work

- Add a bounded deliverable-contract resolver inside the execution prompt
  contract.
- When a clear task shape is detected, use an exact shape-specific output
  contract as the primary contract instead of the generic trusted-form skeleton.
- Keep the existing template skeleton as fallback only when no clear shape is
  detected.
- Add unit tests for plan, comparison, FAQ, acceptance criteria,
  prioritization, and normal fallback behavior.
- Run targeted tests, typecheck, lint, and a live EVT-4 rerun if feasible.

## Boundaries

- No QBS rerun.
- No hard-gate or enforcement threshold change.
- No provider routing change.
- No output-validator change.
- No UI change.
- No full template registry rewrite.
- No raw API keys printed or committed.
- Do not claim quality parity unless live evidence meets the registered rule.

## Exit Criteria

- [x] Plan tasks receive a plan-first output contract, not SWOT-first.
- [x] FAQ tasks receive FAQ entries as the primary contract, not documentation
      wrapper headings.
- [x] Acceptance-criteria tasks keep the documentation skeleton with explicit
      observable/testable criteria guidance. A primary replacement contract was
      tested and rejected because it did not improve the corpus.
- [x] Decision/comparison tasks receive an option-by-option matrix and
      decision rule as the primary contract.
- [x] Verification and live evidence status are recorded.

## Implementation Retained

Runtime code changed in
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-prompt-contract.ts`.

The retained implementation:

- Resolves bounded trusted non-coder deliverable shapes from template id,
  intent, and form inputs.
- Applies a primary replacement contract only for FAQ, decision/comparison,
  and true plan requests.
- Keeps acceptance-criteria, prioritization, and persona requests on their
  original template skeletons with shape guidance only, because live evidence
  showed primary replacement contracts hurt those lanes.
- Keeps the previously proven `700-1100` trusted-form depth target; a deeper
  target was tested and rejected.

Unit coverage was updated in
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-prompt-contract.test.ts`.

## Live Evidence

- Broad deliverable-contract run:
  `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_DELIVERABLE_CONTRACT_EVIDENCE_2026-05-15.json`
  and summary
  `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_DELIVERABLE_CONTRACT_SUMMARY_2026-05-15.md`.
  Result: 20/20 live receipts, 0 safety failures, median delta `-0.16`.
  Not retained as-is because it worsened checklist/SOP/persona/prioritization
  tasks.
- Scoped deliverable-contract run:
  `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_SCOPED_DELIVERABLE_CONTRACT_EVIDENCE_2026-05-15.json`
  and summary
  `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_SCOPED_DELIVERABLE_CONTRACT_SUMMARY_2026-05-15.md`.
  Result: 20/20 live receipts, 0 safety failures, median delta `-0.16`.
  This is the retained runtime posture because it improves the original weak
  strategy plan/comparison lanes without worsening the median.
- Deep scoped-contract run:
  `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_DEEP_SCOPED_CONTRACT_EVIDENCE_2026-05-15.json`
  and summary
  `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_DEEP_SCOPED_CONTRACT_SUMMARY_2026-05-15.md`.
  Result: 20/20 live receipts, 0 safety failures, median delta `-0.16`.
  Not retained because the 1100-1600 token target and extra anti-thin-section
  instruction worsened plan/persona/checklist tasks.

The preregistered `>= -0.05` decision rule remains **not met**.

## Verification

- `node --check scripts/run_evt4_output_quality_ab.js` PASS.
- `npx vitest run src/lib/execute-prompt-contract.test.ts src/app/api/execute/route.test.ts`
  PASS (34/34).
- `npx tsc --noEmit` PASS.
- `npm run lint` PASS with one pre-existing warning in
  `src/app/api/system/jobs/route.test.ts` for unused `_request`.
- `git diff --check` PASS with Windows line-ending warnings for
  `AGENT_HANDOFF_V4_2026-05-12.md` and
  `scripts/run_evt4_output_quality_ab.js`.

## Result

F-1 remains partially remediated and evidence-bounded. The retained code fixes
the strongest residual shape mismatch for FAQ, comparison, and plan requests,
but the EVT-4 corpus still stabilizes around median `-0.16`, not parity.

Further F-1 work should stop treating this as a prompt-only problem. The next
scoped hypothesis should be either:

- Split the trusted form corpus into dedicated task families such as
  `operator_plan`, `decision_memo`, `faq_outline`, and `acceptance_criteria`;
  or
- Rework the EVT-4 CFG-B harness to route frozen tasks directly to those new
  families and rerun a fresh preregistered comparison.

Do not claim quality parity from this packet.
