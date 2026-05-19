# CVF Non-Coder Output Quality Hardening Roadmap

Date: 2026-05-15

Status: IMPLEMENTED - BOUNDED PRODUCT HARDENING COMPLETE, FULL EVT-4 STILL MIXED

Parent closure:

- `docs/reviews/CVF_F1_OUTPUT_QUALITY_PARITY_CLOSURE_NOT_MET_2026-05-15.md`
- `docs/reviews/CVF_EVT4_BOUNDED_VALUE_CLAIM_2026-05-15.md`
- `docs/reviews/CVF_F1_DIMINISHING_RETURNS_STOP_RULE_2026-05-15.md`

Latest tranche evidence:

- `docs/reviews/CVF_GC018_QH1_QH2_NONCODER_OUTPUT_HARDENING_2026-05-15.md`
- `docs/reviews/CVF_QH1_QH2_NONCODER_OUTPUT_HARDENING_RESULT_2026-05-15.md`
- `docs/reviews/CVF_GC018_QH3_SOP_HANDOFF_PROCEDURAL_DEPTH_2026-05-16.md`
- `docs/reviews/CVF_QH3_SOP_HANDOFF_PROCEDURAL_DEPTH_RESULT_2026-05-16.md`
- `docs/reviews/CVF_GC018_QH4_QH5_ROADMAP_COMPLETION_2026-05-16.md`
- `docs/reviews/CVF_QH_ROADMAP_COMPLETION_RESULT_2026-05-16.md`

## 0. Purpose

Convert the EVT-4 output-quality tax into targeted product work for non-coder
deliverables.

This is not F-1 parity tuning. It is a product hardening roadmap focused on
where users feel pain:

- unclear MVP scope;
- vague pricing recommendations;
- SOP/handoff outputs that are not procedural enough;
- personas that do not translate into product/marketing actions;
- decision memos that do not tell the operator what to do first.

## 1. Binding Boundary

This roadmap inherits the F-1 stop rule.

Do not:

- reopen broad F-1 prompt micro-tuning;
- raise the DeepSeek `deepseek-v4-pro` trusted non-coder cap above `3072`;
- add runtime two-pass expansion;
- rerun EVT-4 just to chase reviewer variance;
- claim output-quality parity unless a later registered run actually meets the
  frozen rule.

EVT-4 is a regression benchmark only. Each implementation tranche must have a
specific user-facing product change before EVT-4 is rerun.

## 2. Bounded Claim To Carry Forward

CVF governance preserved live receipts and safety on EVT-4, but a measurable
output-quality tax remains on several non-coder deliverable families.

This is a product-quality backlog, not a governance release blocker.

## 3. Work Tracks

### Track QH-1 — MVP Scope And Backlog Actionability

Implementation status: implemented 2026-05-15 as a scope-first deliverable
contract. EVT-4 target lanes improved or stayed bounded, but full-corpus
regression remains mixed; do not claim output-quality parity or full
no-degrade.

User pain:

- Feature-prioritization outputs can over-index on scoring matrices.
- Non-coders need a crisp scope decision and next operational/build action.

Target families:

- `feature_prioritization`
- MVP scope
- backlog triage

Product change direction:

- Make the final user-visible deliverable lead with:
  - `Do now / MVP`
  - `Do next`
  - `Defer`
  - first validation/build step
  - owner/role
  - acceptance check
- The scoring matrix becomes support evidence, not the primary answer.

Exit criteria:

- Unit tests prove the generated prompt/deliverable contract includes the scope
  decision before scoring evidence.
- One focused live non-coder journey produces a receipt and an operator-ready
  MVP scope.
- EVT-4 is not rerun until this is implemented as a product-level behavior, not
  just a one-line prompt hint.

### Track QH-2 — Pricing Recommendation Actionability

Implementation status: implemented 2026-05-15 as a concrete pricing
recommendation contract. Pricing tiers improved strongly in the full EVT-4
regression and pilot pricing stayed stable on CFG-B score, but full-corpus
regression remains mixed; do not claim output-quality parity or full
no-degrade.

User pain:

- Pricing outputs can be too broad and theoretical.
- Non-coders need concrete tiers or a concrete pilot decision.

Target families:

- `pricing_strategy`
- pilot pricing
- freemium vs paid-only decisions

Product change direction:

- Deliver:
  - tier names or pricing options;
  - target user per tier;
  - included limits/features;
  - price anchors or relative bands when exact prices are not supplied;
  - first pricing experiment;
  - risk and validation checks.

Exit criteria:

- Pricing output is publishable/testable by an operator without another
  strategy pass.
- Assumptions are labeled; unsupported exact prices are not fabricated.

### Track QH-3 — SOP And Handoff Procedural Depth

Implementation status: implemented 2026-05-16 as a procedural runbook and
operator-plan hardening tranche. Focused live evidence retained receipts and
safety, improved builder handoff, recovered ops plan to final stop-rule
baseline CFG-B score, and kept SOP draft stable versus QH-1/QH-2. Do not claim
output-quality parity or full EVT-4 no-degrade.

User pain:

- Documentation/handoff can be clear but not procedural enough.
- Non-coders need steps, branches, QA checks, and escalation paths.

Target families:

- `documentation`
- SOP draft
- builder handoff
- onboarding checklist

Product change direction:

- Deliver:
  - step-by-step procedure;
  - decision branches;
  - required artifacts/fields/assets;
  - QA checks;
  - common failure modes;
  - escalation rules;
  - handoff acceptance checklist.

Exit criteria:

- SOP/handoff outputs let an operator execute or review the workflow without
  developer interpretation.
- Existing safety/audit behavior remains unchanged.

### Track QH-4 — Persona-To-Action Bridge

Implementation status: implemented 2026-05-16 as a persona-to-action packet.
Focused QH-4/QH-5 evidence retained receipts and safety and met the focused
decision rule, but full EVT-4 completion regression remains mixed. Do not claim
output-quality parity or full EVT-4 no-degrade.

User pain:

- Personas can be descriptive but not actionable enough.
- Non-coders need persona-linked product, marketing, support, or onboarding
  actions.

Target families:

- `user_persona`
- buyer/end-user personas
- research-note synthesis

Product change direction:

- Deliver:
  - each persona's trigger, objection, decision criteria, and success signal;
  - product/support/marketing action per persona;
  - first experiment;
  - acceptance check for whether the persona is usable.

Exit criteria:

- Every persona has at least one concrete action and one measurable validation
  signal.

### Track QH-5 — Decision Memo Activation Steps

Implementation status: implemented 2026-05-16 as a decision activation memo.
Focused QH-4/QH-5 evidence retained receipts and safety and met the focused
decision rule, but full EVT-4 completion regression remains mixed. Do not claim
output-quality parity or full EVT-4 no-degrade.

User pain:

- Decision memos can compare options but leave the operator unsure what to do
  first.

Target families:

- `decision_memo`
- channel choice
- launch options

Product change direction:

- Deliver:
  - option comparison using common criteria;
  - recommendation;
  - first activation step;
  - decision rule for when to switch;
  - risk and assumption checks.

Exit criteria:

- The operator can start the recommended path within 24-72 hours.

## 4. Measurement Plan

Use two measurement levels:

1. Focused product checks per track:
   - unit tests for contract structure;
   - one live governed journey with receipt;
   - manual/automated assertion that the expected operator artifacts are
     present.
2. EVT-4 regression benchmark:
   - run only after a meaningful product-level tranche;
   - compare against the retained final stop-rule baseline;
   - do not use reruns as tuning loops.

Retained benchmark baseline:

- `docs/assessments/CVF_EVT4_DEEPSEEK_V4_PRO_FINAL_STOP_RULE_REBASELINE_SUMMARY_2026-05-15.md`
- Median delta `-0.08`.
- `20/20` completed.
- `20/20` CFG-B receipts.
- `0` safety failures.

## 5. First Recommended Tranche

Start with QH-1 and QH-2.

Reason:

- MVP scope/backlog and pricing are repeated negative lanes.
- They map directly to high-value non-coder decisions.
- They can be improved as product deliverable design without reopening global
  F-1 tuning.

Required before implementation:

- Fresh GC/review note for the selected tranche.
- Explicit statement that EVT-4 is regression-only and F-1 parity remains
  closed unless a later run truly meets the registered rule.

## 6. Non-Goals

- No claim that governance improves output quality today.
- No generalized output-quality validator or hidden rubric retry.
- No runtime two-pass expansion.
- No provider/model shopping as a substitute for product work.
- No public repo claim changes from the provenance workspace.
