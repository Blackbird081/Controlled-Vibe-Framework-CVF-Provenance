# CVF GC-018 Review - QH-1/QH-2 Non-Coder Output Hardening

Date: 2026-05-15

Status: APPROVED FOR BOUNDED IMPLEMENTATION

Parent roadmap:

- `docs/roadmaps/CVF_NONCODER_OUTPUT_QUALITY_HARDENING_ROADMAP_2026-05-15.md`

Parent closure and boundary:

- `docs/reviews/CVF_F1_OUTPUT_QUALITY_PARITY_CLOSURE_NOT_MET_2026-05-15.md`
- `docs/reviews/CVF_EVT4_BOUNDED_VALUE_CLAIM_2026-05-15.md`
- `docs/reviews/CVF_F1_DIMINISHING_RETURNS_STOP_RULE_2026-05-15.md`

## 1. Decision

Proceed with the first bounded non-coder output-quality hardening tranche:

- QH-1: MVP scope and backlog actionability.
- QH-2: Pricing recommendation actionability.

This is product deliverable hardening, not a reopening of F-1 output-quality
parity work.

## 2. Authorized Scope

Implementation may update the trusted non-coder deliverable contract for:

- `feature_prioritization`
- MVP scope and backlog triage prompts
- `pricing_strategy`
- pilot pricing and freemium/paid-only pricing prompts

Expected product behavior:

- Feature-prioritization output leads with the scope decision:
  - `Do now / MVP`
  - `Do next`
  - `Defer`
  - first validation/build step
  - owner/role
  - acceptance check
- The scoring matrix supports the scope decision instead of replacing it.
- Pricing output includes concrete tiers or pricing options, target user per
  option, included limits/features, price anchors or relative bands when exact
  prices are not supplied, first pricing experiment, and risk/validation checks.
- Assumptions must be labeled. Unsupported exact prices must not be fabricated.

## 3. Non-Goals

Do not:

- claim F-1 output-quality parity;
- reopen broad prompt/template/model/token-budget tuning;
- increase the trusted non-coder DeepSeek `deepseek-v4-pro` cap above `3072`;
- add runtime two-pass expansion;
- add hidden rubric retries or generalized output validators;
- rerun EVT-4 as an optimization loop;
- push public-facing claim changes from the provenance workspace.

## 4. Files In Scope

Expected code/test surface:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-prompt-contract.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-prompt-contract.test.ts`

Template definitions may be updated only if needed to keep the user-visible
form contract aligned with the bounded QH-1/QH-2 behavior.

## 5. Required Evidence

Before closure:

- Targeted unit tests prove the QH-1 and QH-2 output contracts are present.
- A focused live governed check produces receipts for the changed lanes.
- EVT-4 is rerun once as a regression benchmark after the product change.

EVT-4 interpretation:

- Compare against the retained final stop-rule baseline:
  - Median delta `-0.08`
  - `20/20` completed
  - `20/20` CFG-B receipts
  - `0` safety failures
- Passing or improving the benchmark does not by itself reopen or satisfy F-1.
- Regression findings become product-roadmap evidence, not prompt-tuning
  authorization.

## 6. Closure Standard

Close QH-1/QH-2 only if:

- the implemented contracts are narrower than the rejected broad R2 reshaping;
- governance receipt behavior is retained;
- test evidence is recorded in the active V5 handoff;
- any remaining quality gap is stated honestly as future QH roadmap work.
