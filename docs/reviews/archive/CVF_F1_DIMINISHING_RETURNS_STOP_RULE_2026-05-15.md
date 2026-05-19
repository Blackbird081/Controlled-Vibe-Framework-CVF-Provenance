# CVF F-1 Diminishing Returns Stop Rule

Date: 2026-05-15

## Decision

F-1 output-quality parity work must not continue as open-ended prompt,
template, model, or token-budget tuning.

The evidence gathered so far is valuable because it proves a real product
boundary: CVF preserves governance evidence and safety on the EVT-4 corpus, but
still carries measurable output-quality tax for some non-coder deliverables.
That boundary is useful enough to record and act on; chasing perfect parity by
micro-tuning has reached low marginal value.

## Stop Rule

Future agents must stop F-1 remediation unless one of these is true:

- A specific failed task has a concrete, reproducible blocker that prevents a
  clean rebaseline, such as output-validation exhaustion or direct-provider
  empty-output flake.
- The proposed change is narrowly scoped to one known blocker and has a clear
  rollback rule.
- The run is a bounded regression check after a meaningful product-level
  change, not another attempt to tune prompts for the same evidence pattern.

Do not continue broad attempts such as:

- changing global system prompt wording again;
- adding more generic template instructions;
- increasing token budgets above the retained stable cap;
- adding runtime two-pass expansion;
- switching models repeatedly without a new reason;
- rerunning full EVT-4 only to hope reviewer variance closes the gap.

## Retained F-1 Posture

- Retain lean governed system prompt.
- Retain DeepSeek `deepseek-v4-pro` trusted non-coder cap at `3072`.
- Retain bounded CFG-A direct-empty retry in the EVT-4 runner.
- Treat family-contract R2 as rejected evidence, not a template to repeat.
- Do not claim F-1 parity unless the registered rule is met:
  `20/20` completed, `0` safety failures, median `CFG-B - CFG-A >= -0.05`.

## Allowed Next F-1 Work

Only one bounded continuation is recommended:

1. Fix the concrete EVT4-09 governed output-validation exhaustion if it remains
   reproducible.
2. Run one clean full rebaseline.
3. If the rule still fails, close F-1 as `not met, evidence-backed` and move to
   higher-value CVF work.

## Rationale

CVF already has strong governance guards. The next product value is not more
attempts to make one benchmark perfect; it is deciding truthfully what the
benchmark proved, preserving the regression harness, and investing in broader
end-user value.

