# CVF W140-T1 UI Execution Lifecycle Diagnostic Roadmap

> Authorization: `docs/baselines/CVF_GC018_W140_T1_UI_EXECUTION_LIFECYCLE_DIAGNOSTIC_AUTHORIZATION_2026-05-08.md`  
> Wave ID: W140  
> Status: CLOSED

## Problem

W137 and W138 both left Alibaba at 10/12 accepted in the repeated browser UI
matrix, while W139 direct API diagnostics proved Alibaba 12/12 and DeepSeek 6/6
accepted. The remaining blocker is the browser UI lifecycle for late repeated
journeys.

## Checkpoints

| CP | Status | Work |
|---|---:|---|
| CP0 | COMPLETE | GC-018 authorization and scope lock |
| CP1 | COMPLETE | Added browser lifecycle capture to Alibaba UI matrix |
| CP2 | COMPLETE | Ran 12-journey Alibaba UI diagnostic: 10/12 accepted |
| CP3 | COMPLETE | Classified failures as `execute_request_not_sent` caused by wizard routing |
| CP4 | COMPLETE | Published continuation decision |

## Evidence Rules

Evidence must not include raw provider keys. Page text and response body capture
must be bounded to diagnostic snippets and error metadata, not full generated
outputs.

## Closure Target

## Closure Evidence

- Continuation decision:
  `docs/reviews/CVF_W140_CONTINUATION_DECISION_2026-05-08.md`
- Alibaba UI lifecycle matrix:
  `docs/reviews/CVF_W140_UI_EXECUTION_LIFECYCLE_ALIBABA_EVIDENCE_2026-05-08.json`

W140 closes as diagnostic evidence only. The next tranche is W141 trusted-form
versus wizard routing disambiguation.
