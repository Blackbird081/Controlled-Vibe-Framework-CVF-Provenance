# CVF Lane C Execution Gateway Completion

Memory class: FULL_RECORD
Status: CLOSED - MOCK TESTED CLI CALLER

## Purpose

Close Lane C by adding a minimal `cvf execute` command surface to the existing
governance CLI while preserving the existing governed web execute route as the
single runtime path.

## Scope

Completed:

- added async `execute` command support to the governance CLI;
- added `GovernanceCLI.runAsync()` while keeping existing sync commands stable;
- added route-compatible payload construction;
- added service-token HMAC header construction;
- added compact CLI receipt JSON output;
- added mock HTTP tests;
- mirrored public-safe CLI source and tests into public-sync;
- updated the technical product catalog with bounded wording.

Not completed:

- live provider execution through the CLI;
- execute-route runtime changes;
- universal role override semantics.

## Source / Predecessor Evidence

- `docs/baselines/CVF_GC018_LANE_C_EXECUTION_GATEWAY_2026-05-19.md`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/execute.client.ts`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/tests/execute.client.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`

## Decision / Baseline / Proposed Tranche

Decision: Lane C is closed as a CLI caller implementation.

The implementation deliberately leaves
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
unchanged. The CLI posts to the existing route and returns a JSON envelope built
from the route response.

## Findings

The existing CLI was synchronous. Directly making all commands async would have
broken existing tests and caller expectations. The implementation therefore
adds:

- `GovernanceCLI.runAsync()` for HTTP commands;
- `CommandRegistry.executeAsync()` for async-capable handlers;
- a sync `execute --help` surface;
- a clear sync error for attempting HTTP execution through the sync runner.

The `--role` flag is preserved in the CLI request and receipt as
`requestedRole`. It does not override the execute route's existing
session/service-token role resolution.

## Recommendation

If a later tranche wants a shell-installed `cvf` binary, it should add an
explicit package `bin` entry and release wiring. Lane C intentionally stopped at
the library/command surface because that is enough for tests and orchestration
without inventing a packaging story.

## Risk / Corrective Action

Risk: users may assume `--role` overrides execute-route role enforcement.

Corrective action: the completion packet states `--role` is preserved as
`requestedRole` only. The route's session/service-token role resolution remains
authoritative.

## Evidence / Verification

Provenance CLI:

```powershell
npm test -- --run
```

Result: 4 test files passed, 47 tests passed.

```powershell
npx tsc --noEmit
```

Result: pass.

Public-sync path verification:

```powershell
Test-Path "EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/execute.client.ts"
Test-Path "EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/tests/execute.client.test.ts"
```

Result: both paths exist.

Public-sync test note: public-sync does not currently have installed
`node_modules` for this CLI package, so `vitest` and `tsc` were not runnable
there without installing dependencies. The same source was verified in the
provenance workspace where dependencies are installed.

## Claim Boundary

Lane C may be described as:

> `cvf execute` is implemented as a mock-tested CLI caller for the existing
> governed execute route.

Lane C must not be described as:

> `cvf execute` has live-proven provider execution, changes route governance,
> or broadens role permissions.
