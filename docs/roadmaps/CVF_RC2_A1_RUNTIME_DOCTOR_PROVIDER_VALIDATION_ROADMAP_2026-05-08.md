<!-- Memory class: FULL_RECORD -->
# CVF RC2-A1 Runtime Doctor + Provider Validation Roadmap

> Authorization: `docs/baselines/CVF_GC018_RC2_A1_RUNTIME_DOCTOR_PROVIDER_VALIDATION_AUTHORIZATION_2026-05-08.md`
> Track: RC2 Foundation / A — Install Productization
> Status: CLOSED DELIVERED

## Purpose

Turn the A0 install audit findings into concrete, secret-safe diagnostics that
new users and future setup automation can run before starting CVF Web.

## Checkpoints

| CP | Work |
|---|---|
| CP0 | GC-018 authorization and A1 scope lock |
| CP1 | Track `cvf-web/.env.example` so fresh clones have an env template |
| CP2 | Add `scripts/cvf_doctor.py --json` |
| CP3 | Add `scripts/cvf_provider_check.py --provider <lane> --json [--live] [--no-local-env]` |
| CP4 | Verify doctor/provider classifications and live provider validation |
| CP5 | Publish closure and handoff sync |

## Exit Criteria

- Doctor emits stable JSON and human output.
- Provider check emits stable JSON and never prints raw keys.
- Missing provider keys are classified as `MISSING_KEY`.
- Present keys can be classified without live calls.
- Live validation is opt-in through `--live`.
- Alibaba and DeepSeek live validation pass on configured local keys.

## Closure Result

RC2-A1 closed on 2026-05-08.

Closure:
`docs/reviews/CVF_RC2_A1_RUNTIME_DOCTOR_PROVIDER_VALIDATION_CLOSURE_DECISION_2026-05-08.md`
