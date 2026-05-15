# CVF GC-018 Review - QH-4/QH-5 Roadmap Completion

Date: 2026-05-16

Status: APPROVED FOR BOUNDED IMPLEMENTATION

Parent roadmap:

- `docs/roadmaps/CVF_NONCODER_OUTPUT_QUALITY_HARDENING_ROADMAP_2026-05-15.md`

Previous tranche:

- `docs/reviews/CVF_QH3_SOP_HANDOFF_PROCEDURAL_DEPTH_RESULT_2026-05-16.md`

Parent F-1 boundary:

- `docs/reviews/CVF_F1_OUTPUT_QUALITY_PARITY_CLOSURE_NOT_MET_2026-05-15.md`
- `docs/reviews/CVF_F1_DIMINISHING_RETURNS_STOP_RULE_2026-05-15.md`

## 1. Decision

Proceed with the remaining roadmap tracks as one bounded completion tranche:

- QH-4: persona-to-action bridge.
- QH-5: decision memo activation steps.

This is product deliverable hardening only. It does not reopen F-1 and does
not authorize broad prompt, model, provider, or token-budget tuning.

## 2. Authorized Scope

Implementation may update:

- trusted non-coder persona deliverable contract;
- trusted non-coder decision/comparison deliverable contract;
- `user_persona` template metadata and output skeleton;
- `decision_memo` template metadata and output skeleton;
- prompt-contract tests proving QH-4/QH-5 structure.

Expected QH-4 behavior:

- Every persona includes trigger, objection, decision criteria, and success
  signal.
- Every persona maps to product, marketing/support, and onboarding or
  activation actions.
- Every persona has a first experiment and acceptance check.

Expected QH-5 behavior:

- Decision memos include recommendation first enough for an operator to start.
- Every option is compared on common criteria.
- The output includes first activation step in the next 24-72 hours, decision
  rule, switch/rollback trigger, risks, assumptions, and acceptance checks.

## 3. Non-Goals

Do not:

- claim output-quality parity unless the registered EVT-4 rule is actually met;
- claim full no-degrade if full EVT-4 is mixed;
- raise the retained DeepSeek `deepseek-v4-pro` trusted non-coder cap above
  `3072`;
- add runtime two-pass expansion;
- add hidden rubric retries or generalized output validators;
- rerun full EVT-4 merely to chase reviewer/provider variance;
- push public-facing claim changes from the provenance workspace.

## 4. Evidence Plan

Before closure:

- Targeted unit tests prove QH-4/QH-5 contracts are present.
- Typecheck/lint stay clean aside from known pre-existing warnings.
- Focused live governed check covers:
  - EVT4-04, EVT4-10, EVT4-17 for QH-4;
  - EVT4-02 and EVT4-13 for QH-5.
- Run full EVT-4 once after QH-4/QH-5 implementation as the roadmap completion
  regression benchmark.

## 5. Closure Standard

Close the roadmap only if:

- QH-4 and QH-5 product contracts are implemented and tested;
- focused live evidence has receipts and no safety failures;
- full EVT-4 result is recorded honestly;
- the active handoff tells future agents not to continue tuning unless a fresh
  roadmap supersedes the stop rule.
