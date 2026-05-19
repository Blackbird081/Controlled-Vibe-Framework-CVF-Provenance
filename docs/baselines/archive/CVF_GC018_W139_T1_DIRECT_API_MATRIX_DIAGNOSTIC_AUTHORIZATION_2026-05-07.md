# CVF GC-018 — W139-T1 Authorization

> Date: 2026-05-07  
> Tranche: W139-T1 — Direct API Matrix Diagnostic  
> Status: AUTHORIZED

## Decision

**AUTHORIZED.** W139-T1 may begin immediately.

W139 is authorized because W137 and W138 both reproduced the same late Alibaba
UI-matrix `execute_route_timeout` pattern, while direct targeted W136 proof
passed. A direct `/api/execute` matrix is needed to isolate the failure domain.

## Scope Lock

W139 is limited to:

- Running the trusted-form 12-journey sequence through authenticated direct
  `/api/execute` calls on Alibaba.
- Running the first 6 journeys through direct `/api/execute` calls on DeepSeek.
- Capturing HTTP status, receipt decision, output-validation metadata, elapsed
  time, and diagnostic class.
- Publishing a continuation decision that identifies whether W140 should target
  UI/browser lifecycle or server/provider lifecycle.

W139 must not:

- Change product runtime behavior.
- Add new trusted forms.
- Treat diagnostic direct API evidence as browser UI stability proof.
- Print or commit raw provider keys.

## Closure Criteria

W139 can close as diagnostic when it records both direct API lanes and publishes
a continuation decision.
