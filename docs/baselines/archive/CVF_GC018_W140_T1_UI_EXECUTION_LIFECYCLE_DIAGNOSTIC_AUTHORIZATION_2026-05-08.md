# CVF GC-018 - W140-T1 Authorization

> Date: 2026-05-08  
> Tranche: W140-T1 - UI Execution Lifecycle Diagnostic  
> Status: AUTHORIZED

## Decision

**AUTHORIZED.** W140-T1 may begin immediately.

W140 is authorized because W139 proved the trusted-form matrix works through
direct authenticated `/api/execute` calls: Alibaba 12/12 accepted and DeepSeek
6/6 accepted. The remaining instability is therefore bounded to the browser UI
execution lifecycle, not the server/provider route capability.

## Scope Lock

W140 is limited to:

- Running the Alibaba 12-journey trusted-form matrix through the browser UI.
- Capturing `/api/execute` request lifecycle events:
  request started, response observed, request finished, and request failed.
- Capturing ProcessingScreen/result visibility state and bounded page text at
  timeout.
- Publishing a continuation decision that identifies whether W141 should target
  UI submission, browser fetch lifecycle, or ProcessingScreen/result handoff.

W140 must not:

- Change product runtime behavior.
- Add new trusted forms or provider behavior.
- Treat diagnostic evidence as a release-quality stability claim.
- Print or commit raw provider keys.

## Closure Criteria

W140 can close as diagnostic when it records the Alibaba UI lifecycle matrix and
publishes a continuation decision with the observed failure class.
