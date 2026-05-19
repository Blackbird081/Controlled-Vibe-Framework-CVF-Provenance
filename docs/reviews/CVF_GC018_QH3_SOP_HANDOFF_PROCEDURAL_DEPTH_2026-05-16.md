# CVF GC-018 Review - QH-3 SOP/Handoff Procedural Depth

Date: 2026-05-16

Status: APPROVED FOR BOUNDED IMPLEMENTATION

Parent roadmap:

- `docs/roadmaps/archive/CVF_NONCODER_OUTPUT_QUALITY_HARDENING_ROADMAP_2026-05-15.md`

Recent tranche:

- `docs/reviews/archive/CVF_QH1_QH2_NONCODER_OUTPUT_HARDENING_RESULT_2026-05-15.md`

Parent F-1 boundary:

- `docs/reviews/archive/CVF_F1_OUTPUT_QUALITY_PARITY_CLOSURE_NOT_MET_2026-05-15.md`
- `docs/reviews/archive/CVF_F1_DIMINISHING_RETURNS_STOP_RULE_2026-05-15.md`

## 1. Decision

Proceed with QH-3 as bounded product deliverable hardening for SOP,
documentation, handoff, onboarding checklist, and operator-plan outputs.

This is not F-1 parity tuning and must not be treated as a reason to reopen
global prompt/model/token-budget work.

## 2. Authorized Scope

Implementation may update:

- trusted non-coder checklist/documentation deliverable contract;
- `documentation` template metadata and output skeleton;
- `operator_plan` template metadata and output skeleton;
- prompt-contract tests proving procedural depth.

Expected QH-3 behavior:

- Output provides step-by-step procedure, not just a summary.
- Each major step has owner/role, action, required artifact or field, done
  signal, and acceptance check.
- Decision branches are explicit.
- QA checks are separated from execution steps.
- Common failure modes include detection signal, recovery action, and escalation
  rule.
- Handoff checklist states what must be true before work is passed on.

## 3. Non-Goals

Do not:

- claim F-1 output-quality parity;
- claim full EVT-4 no-degrade from this tranche;
- raise the DeepSeek `deepseek-v4-pro` trusted non-coder cap above `3072`;
- add runtime two-pass expansion;
- add hidden rubric retries or generalized output validators;
- rerun full EVT-4 merely to chase reviewer/provider variance;
- change public-facing repository content from the provenance workspace.

## 4. Evidence Plan

Before closure:

- Targeted unit tests prove QH-3 procedural sections are present.
- Typecheck/lint stay clean aside from known pre-existing warnings.
- Focused live governed check covers QH-3 lanes with receipts:
  - EVT4-07 builder handoff;
  - EVT4-12 SOP draft;
  - optionally EVT4-08 ops plan if runtime budget allows.

Full EVT-4 is deferred until the next meaningful product tranche is complete
unless a regression appears in focused QH-3 evidence that requires rollback.

## 5. Closure Standard

Close QH-3 only if:

- the change is narrower than broad family-contract reshaping;
- governance receipt behavior is retained on focused live evidence;
- safety failures remain `0`;
- the active V5 handoff records the result honestly.
