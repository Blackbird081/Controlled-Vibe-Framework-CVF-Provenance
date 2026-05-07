<!-- Memory class: FULL_RECORD -->
# CVF W151-T1 Trusted Form Test Maintainability Roadmap

> Authorization: `docs/baselines/CVF_GC018_W151_T1_TRUSTED_FORM_TEST_MAINTAINABILITY_AUTHORIZATION_2026-05-08.md`
> Wave ID: W151
> Status: CLOSED DELIVERED

## Purpose

W150 split trusted-form corpus data from router behavior. W151 completes the
same maintainability cleanup on test coverage by separating corpus activation
coverage from route integration behavior.

## Checkpoints

| CP | Work |
|---|---|
| CP0 | GC-018 authorization and no-behavior-change scope lock |
| CP1 | Add data-driven trusted-form activation corpus test |
| CP2 | Reduce `form-routing.test.ts` to router/integration coverage |
| CP3 | Run targeted routing verification |
| CP4 | Run lint/build/release gate |
| CP5 | Closure packet + handoff update |

## Claim Boundary

W151 may claim test maintainability improvement only. It does not alter the
trusted-form corpus, routing semantics, or W149 live value baseline.

## Closure Result

W151 closed on 2026-05-08. Activation coverage moved to a data-driven corpus
test, `form-routing.test.ts` dropped from 731 to 153 lines, targeted tests pass
131/131, and the release gate bundle passed.

Closure decision:
`docs/reviews/CVF_W151_CLOSURE_DECISION_2026-05-08.md`.
