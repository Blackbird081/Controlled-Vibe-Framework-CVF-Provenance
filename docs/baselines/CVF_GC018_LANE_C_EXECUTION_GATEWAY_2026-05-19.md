# CVF GC-018 Lane C Execution Gateway

Memory class: SUMMARY_RECORD
Status: AUTHORIZED

## Purpose

Authorize Lane C to add a minimal CLI execution gateway that calls the existing
governed `/api/execute` web route and returns receipt JSON.

The CLI is a caller. It is not a replacement runtime and does not change
governance logic inside the execute route.

## Scope

In scope:

- add an async `execute` command surface to the existing governance CLI;
- accept `--template <id>`, `--role <role>`, optional `--input <json>`,
  optional `--endpoint <url>`, optional provider/model flags, and `--verbose`;
- POST to `<endpoint>/api/execute`;
- sign service-token requests when `CVF_SERVICE_TOKEN` or `--token` is present;
- print a JSON receipt envelope to CLI output;
- prove behavior with mock HTTP unit tests and TypeScript validation.

Out of scope:

- modifying `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`;
- adding new route middleware;
- changing provider routing;
- changing role-permission runtime semantics;
- claiming live governance proof from mock tests.

## Source / Predecessor Evidence

- `docs/work_orders/CVF_AGENT_WORK_ORDER_LANE_BCH_2026-05-19.md`
- `docs/roadmaps/CVF_NEXT_PHASE_ROADMAP_LANE_B_C_H_2026-05-19.md`
- `docs/reviews/CVF_LANE_B_WORKFLOW_PACKAGING_COMPLETION_2026-05-19.md`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/cli.ts`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`

## Decision / Baseline / Proposed Tranche

Decision: implement Lane C as an async governance CLI caller.

Chosen approach:

- extend the existing CLI with `execute`;
- keep legacy sync command behavior for existing commands;
- add `GovernanceCLI.runAsync()` for commands that perform HTTP I/O;
- sign service-token calls with the same HMAC header contract used by the web
  route;
- return a compact CLI receipt containing request template/role, governance
  receipt, workflow ID, step traces, receipt binding, role permission, and
  provider routing.

## Rule

Lane C may claim:

> `cvf execute` is implemented as a CLI caller for the existing governed execute
> route and is mock-tested for request construction and receipt output.

Lane C must not claim:

> live provider proof, new runtime enforcement, or role semantics beyond what
> `/api/execute` already enforces.

## Claim Boundary

This baseline authorizes only a CLI caller and mocked receipt-output proof. It
does not authorize a live provider execution claim.

## Allowed And Forbidden Requirements

Allowed:

- add CLI files and tests;
- use mock HTTP tests for CLI request/response behavior;
- update public-safe catalog rows after public-sync path verification;
- rely on existing service-token auth headers.

Forbidden:

- editing execute route governance logic for Lane C;
- printing raw service tokens or provider keys;
- claiming `--role` overrides execute-route session/service-token role
  resolution;
- claiming live governance proof unless the mandatory live gate or a targeted
  live proof is run with operator-supplied keys.

## Exceptions

None. Any route wiring or runtime enforcement changes belong to a separate
authorized tranche.

## Enforcement Surface

Verification must include:

- CLI tests for help, argument parsing, request construction, HMAC header
  construction, and mocked receipt JSON;
- TypeScript validation for the CLI extension;
- public-sync `Test-Path` validation for catalog-cited CLI files.

## Evidence / Verification

Expected commands:

```powershell
npm test -- --run
npx tsc --noEmit
```

Run in:

```text
EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI
```

Live release gate is not required for Lane C unless the CLI result is used as a
release-quality governance claim.

## Claim / Final / Verification Boundary

Final boundary: Lane C is a CLI caller and mock-tested request/receipt surface.
Verification is limited to CLI unit tests, TypeScript checks, and catalog path
verification. Live provider execution remains outside this baseline.
