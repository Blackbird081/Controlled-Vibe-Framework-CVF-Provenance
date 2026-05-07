# CVF GC-018 — W134-T1 Authorization

> Date: 2026-05-07  
> Tranche: W134-T1 — Pre-AI-Call HTTP 400 Root Cause Fix  
> Status: AUTHORIZED

## Decision

**AUTHORIZED.** W134-T1 may begin immediately.

W134 is authorized because W133 closed with the classified blocker
`noncoder_pre_ai_call_http400_non_documentation_forms`: documentation journeys
can reach live provider execution, while the trusted non-documentation form
subset returns HTTP 400 before useful noncoder acceptance can be measured.

## Scope Lock

W134 is limited to:

- Capturing `/api/execute` HTTP 400 response bodies for trusted form journeys.
- Identifying the exact pre-AI rejection path.
- Fixing the narrow root cause without widening the trusted form corpus.
- Re-running targeted and stability evidence on Alibaba and DeepSeek lanes.
- Publishing a continuation decision and release-gate result.

W134 must not:

- Add new trusted form templates.
- Overstate noncoder runtime stability before the 12-journey and 6-journey
  live matrices pass.
- Treat mock UI checks as governance behavior proof.
- Print or commit raw provider keys.

## Closure Criteria

W134 can close as delivered only when:

- `responseBody` evidence identifies the pre-AI 400 path.
- The root cause is fixed with targeted regression coverage.
- Alibaba 12-journey matrix reaches at least 8 accepted journeys.
- DeepSeek 6-journey confirmatory matrix reaches at least 3 accepted journeys.
- `python scripts/run_cvf_release_gate_bundle.py --json` passes with live
  governance E2E enabled.

