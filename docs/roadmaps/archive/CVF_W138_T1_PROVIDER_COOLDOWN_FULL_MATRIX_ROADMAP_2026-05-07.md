# CVF W138-T1 Provider Cooldown Full Matrix Roadmap

> Authorization: `docs/baselines/CVF_GC018_W138_T1_PROVIDER_COOLDOWN_FULL_MATRIX_AUTHORIZATION_2026-05-07.md`  
> Wave ID: W138  
> Status: CLOSED_CONTINUED

## Problem

W137 improved Alibaba from W134's 9/12 accepted to 10/12 accepted, but the same
late-matrix `documentation` and `strategy_analysis` execute-route timeouts
recurred under a 1500ms inter-journey delay.

## Checkpoints

| CP | Status | Work |
|---|---:|---|
| CP0 | COMPLETE | GC-018 authorization and scope lock |
| CP1 | COMPLETE | Added provider-cooldown full-matrix spec |
| CP2 | COMPLETE | Alibaba 12-journey matrix with longer cooldown ran: 10/12 accepted, target not met |
| CP3 | COMPLETE | DeepSeek 6-journey confirmatory matrix: 6/6 accepted |
| CP4 | COMPLETE | Published continuation decision |
| CP5 | NOT_RUN | Release gate skipped because CP2 target failed |

## Evidence Rules

Evidence must record cooldown duration, HTTP status, response body availability,
receipt presence, and diagnostic subcodes without printing raw provider keys.

## Closure Evidence

- Continuation decision:
  `docs/reviews/CVF_W138_CONTINUATION_DECISION_2026-05-07.md`
- Alibaba cooldown matrix:
  `docs/reviews/CVF_W138_PROVIDER_COOLDOWN_STABILITY_ALIBABA_EVIDENCE_2026-05-07.json`
- DeepSeek cooldown matrix:
  `docs/reviews/CVF_W138_PROVIDER_COOLDOWN_STABILITY_DEEPSEEK_EVIDENCE_2026-05-07.json`

W138 continued to W139 because 7500ms provider cooldown did not change the
late Alibaba timeout pattern.
