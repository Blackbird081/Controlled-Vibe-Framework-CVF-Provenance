# CVF W139-T1 Direct API Matrix Diagnostic Roadmap

> Authorization: `docs/baselines/CVF_GC018_W139_T1_DIRECT_API_MATRIX_DIAGNOSTIC_AUTHORIZATION_2026-05-07.md`  
> Wave ID: W139  
> Status: CLOSED

## Problem

W137 and W138 show the same late Alibaba UI-matrix timeout pattern even with
provider cooldown. W136 direct targeted proof passed, so the failure domain is
still ambiguous.

## Checkpoints

| CP | Status | Work |
|---|---:|---|
| CP0 | COMPLETE | GC-018 authorization and scope lock |
| CP1 | COMPLETE | Added direct `/api/execute` matrix diagnostic spec |
| CP2 | COMPLETE | Alibaba direct 12-journey matrix: 12/12 accepted |
| CP3 | COMPLETE | DeepSeek direct 6-journey confirmatory matrix: 6/6 accepted |
| CP4 | COMPLETE | Published continuation decision |

## Evidence Rules

Evidence must not include raw provider keys. Response body capture should be
bounded to diagnostic metadata and errors, not full generated outputs.

## Closure Evidence

- Continuation decision:
  `docs/reviews/CVF_W139_CONTINUATION_DECISION_2026-05-07.md`
- Alibaba direct matrix:
  `docs/reviews/CVF_W139_DIRECT_API_MATRIX_ALIBABA_EVIDENCE_2026-05-07.json`
- DeepSeek direct matrix:
  `docs/reviews/CVF_W139_DIRECT_API_MATRIX_DEEPSEEK_EVIDENCE_2026-05-07.json`

W139 closes as diagnostic evidence. The next tranche is W140 browser/UI
lifecycle diagnostics.
