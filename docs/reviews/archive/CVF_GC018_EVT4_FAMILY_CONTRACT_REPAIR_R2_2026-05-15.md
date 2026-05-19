# GC-018 — EVT-4 Family Contract Repair R2

Date: 2026-05-15

## Decision

Proceed with a bounded EVT-4/F-1 remediation that changes trusted non-coder
output contracts for the weak DeepSeek `deepseek-v4-pro` lanes only.

## Trigger Evidence

- `CVF_EVT4_DEEPSEEK_V4_PRO_LEAN_PROMPT_3072_RERUN_*`
- Completed 19/20 pairs; no CFG-B timeout; 0 safety failures.
- Median normalized delta remained `-0.12`, below the registered `>= -0.05`
  rule.
- Reviewer rationales repeatedly cited:
  - pricing outputs too broad and missing concrete tiers/actions;
  - feature-prioritization outputs too matrix-heavy and weak on MVP scope;
  - persona outputs missing product/marketing feature suggestions;
  - documentation/handoff outputs missing procedural or implementation detail.

## Authorized Scope

- Strengthen `buildExecutionPrompt()` family contracts for:
  - `pricing_strategy`
  - `feature_prioritization`
  - `user_persona`
  - checklist/documentation handoff/SOP shapes
  - operator plans
- Keep provider routing, hard gates, safety filters, output validator, and
  reviewer protocol unchanged.
- Keep DeepSeek V4 Pro trusted non-coder token budget at `3072`; do not return
  to `4096` because live evidence showed timeout instability.

## Boundaries

- No QBS rerun.
- No hard-gate or enforcement threshold change.
- No runtime two-pass production feature.
- No public repository push from this provenance workspace.
- Do not claim F-1 closure unless a later live run completes 20/20, has 0 safety
  failures, and median delta is `>= -0.05`.

## Result

The R2 contract repair was tested and rejected.

- Evidence:
  `docs/assessments/CVF_EVT4_DEEPSEEK_V4_PRO_FAMILY_CONTRACT_R2_EVIDENCE_2026-05-15.json`
- Summary:
  `docs/assessments/CVF_EVT4_DEEPSEEK_V4_PRO_FAMILY_CONTRACT_R2_SUMMARY_2026-05-15.md`
- Completed: 19/20; one CFG-A direct-provider empty-output failure.
- CFG-B receipts: 19.
- Safety failures: 0.
- Median delta: `-0.16`.

Because R2 worsened the retained lean-prompt/3072 signal (`-0.12`), the runtime
family-contract changes were reverted. Keep this packet as evidence that broad
family contract reshaping should not be the next F-1 path.
