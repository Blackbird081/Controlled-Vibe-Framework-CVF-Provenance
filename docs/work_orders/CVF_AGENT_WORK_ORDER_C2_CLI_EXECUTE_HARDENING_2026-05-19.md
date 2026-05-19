# CVF Agent Work Order — C2: CLI Execute Hardening

Memory class: SUMMARY_RECORD

Status: CLOSED

GC-018 required: No — hardening delta of existing `cvf execute`; R0 scope.

## Purpose

Harden the existing `cvf execute` command in `CVF_ECO_v2.2_GOVERNANCE_CLI`
with a `--dry-run` flag, JSONL audit receipt persistence, and two new tests.
Closes the mock-only gap in Lane C: `cvf execute` exists and is mock-tested;
this delta adds verifiable dry-run capability and structured audit output.

## Authority Chain

`docs/roadmaps/CVF_RUNTIME_MATURITY_DELTA_ROADMAP_V2_2026-05-19.md` — C2
section. Codex rebuttal accepted; C2 starts from existing `execute.client.ts`.

## Agent Roles

- **Orchestrator** — dispatches work order; accepts completion packet.
- **Worker** — implements all tasks in governance repo CLI extension only;
  runs pre-flight before any code; files completion review upon closure.

## Scope

**Allowed scope:** `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/` only.

- Modified: `src/execute.client.ts` — add `buildDryRunOutput()`, `appendExecuteReceipt()`
- Modified: `src/command.registry.ts` — wire `--dry-run` and `--receipt` flags
- Modified: `tests/execute.client.test.ts` — add 2 new tests
- New evidence file: `docs/evidence/cvf-execute-receipts.jsonl` (created at runtime by `--receipt`, not manually)

**Forbidden scope:**

- Live provider call or HTTP integration test hitting real network
- New CLI commands beyond `execute` hardening
- Modifying `cli.ts`, `types.ts`, `governance-reliability-metrics.ts`
- Public-sync repo edits under this WO

## Required First Reads

1. `src/execute.client.ts` (189 lines) — full file, especially `executeGovernedTemplateCommand` and `buildCliReceipt`
2. `src/command.registry.ts` — execute command registration, flag list
3. `tests/execute.client.test.ts` (148 lines) — existing 5 tests
4. Roadmap C2 section — done criterion, line count constraints

## Write Ownership

Worker owns: `execute.client.ts`, `command.registry.ts`, `tests/execute.client.test.ts`.
Evidence JSONL is created at runtime, not manually. No other files.

## Pre-Flight Checks

Worker must verify before writing any code:

```text
1. Confirm execute.client.ts is 189 lines
2. Confirm tests/execute.client.test.ts is 148 lines with exactly 5 tests
3. Confirm buildDryRunOutput does NOT exist yet in execute.client.ts
4. Confirm appendExecuteReceipt does NOT exist yet in execute.client.ts
5. Confirm --dry-run flag is NOT registered in command.registry.ts
```

## Execution Plan

Task 1 → Task 2 → Task 3 in sequence. Tests must pass before closure.

### Task 1 — `execute.client.ts` additions

Add two functions after `buildCliReceipt`:

```typescript
export function buildDryRunOutput(
  payload: ExecuteRequestPayload,
  headers: Record<string, string>,
): Record<string, unknown> {
  const safeHeaders = { ...headers };
  delete safeHeaders['x-cvf-service-token'];
  delete safeHeaders['x-cvf-service-signature'];
  return {
    dryRun: true,
    templateId: payload.templateId,
    requestedRole: payload.requestedRole,
    endpoint: '[not sent]',
    payloadShape: Object.keys(payload),
    headerKeys: Object.keys(safeHeaders),
  };
}
```

```typescript
export function appendExecuteReceipt(
  receipt: Record<string, unknown>,
  receiptPath: string,
): void {
  const fs = require('node:fs');
  const path = require('node:path');
  const dir = path.dirname(receiptPath);
  if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
  const line = JSON.stringify({
    timestamp: new Date().toISOString().replace(/\.\d{3}Z$/, 'Z'),
    templateId: receipt['templateId'],
    requestedRole: receipt['requestedRole'],
    workflowId: receipt['workflowId'] ?? null,
    receiptBinding: receipt['receiptBinding'] ?? null,
  });
  fs.appendFileSync(receiptPath, line + '\n', 'utf8');
}
```

`execute.client.ts` must stay ≤ 220 lines after additions.

### Task 2 — `command.registry.ts` wiring

In the `execute` command `executeAsync` handler:

1. Check `args.flags['dry-run'] === true` → call `buildDryRunOutput(payload, headers)` → return as success output, skip HTTP.
2. After successful execute, check `args.flags['receipt'] === true` → call `appendExecuteReceipt(receipt, receiptFilePath)` where `receiptFilePath` defaults to `docs/evidence/cvf-execute-receipts.jsonl` relative to cwd.

Update usage string:

```text
cvf execute --template <id> --role <role> [--input <json>] [--endpoint <url>] [--dry-run] [--receipt] [--verbose]
```

### Task 3 — Two new tests in `execute.client.test.ts`

Add after the existing 5 tests:

```typescript
it("dry-run returns payload shape without making HTTP call", async () => {
  const payload = buildExecutePayload({
    command: "execute",
    flags: { template: "documentation", role: "BUILDER" },
    positional: [],
  });
  const headers = buildServiceHeaders(undefined, JSON.stringify(payload));
  const output = buildDryRunOutput(payload, headers);
  expect(output.dryRun).toBe(true);
  expect(output.templateId).toBe("documentation");
  expect(Array.isArray(output.payloadShape)).toBe(true);
  expect((output.headerKeys as string[]).includes('x-cvf-service-token')).toBe(false);
});

it("appendExecuteReceipt writes a valid JSONL line", async () => {
  const { mkdtempSync, readFileSync, rmSync } = await import("node:fs");
  const { join } = await import("node:path");
  const tmpDir = mkdtempSync("cvf-receipt-test-");
  const receiptPath = join(tmpDir, "evidence", "test-receipts.jsonl");
  const fakeReceipt = {
    templateId: "documentation",
    requestedRole: "BUILDER",
    workflowId: "wf-001",
    receiptBinding: "rb-001",
  };
  appendExecuteReceipt(fakeReceipt, receiptPath);
  const line = JSON.parse(readFileSync(receiptPath, "utf8").trim());
  expect(line.templateId).toBe("documentation");
  expect(typeof line.timestamp).toBe("string");
  rmSync(tmpDir, { recursive: true });
});
```

`tests/execute.client.test.ts` must stay ≤ 220 lines. Run `npm test` — all 7
tests must pass. Run `npm run check` — must pass.

## Acceptance Criteria

- [ ] `buildDryRunOutput` added; `execute.client.ts` ≤ 220 lines
- [ ] `appendExecuteReceipt` added; `execute.client.ts` ≤ 220 lines
- [ ] `--dry-run` and `--receipt` wired in `command.registry.ts`
- [ ] 7 tests PASS (5 existing + 2 new); `tests/execute.client.test.ts` ≤ 220 lines
- [ ] `npm run check` PASS
- [ ] `buildDryRunOutput` output confirms `x-cvf-service-token` absent from headerKeys

## Evidence Requirements

Completion review must include:

1. `npm test` output: 7 tests PASS.
2. `npm run check` output: PASS.
3. `execute.client.ts` line count ≤ 220.
4. `tests/execute.client.test.ts` line count ≤ 220.
5. Sample `buildDryRunOutput` output showing `x-cvf-service-token` absent.
6. JSONL line shape from `appendExecuteReceipt` test.

## Review Gate

Orchestrator reviews completion packet. No closure without 7-test PASS and
`npm run check` PASS in evidence.

## Closure Checklist

- [ ] All acceptance criteria verified with evidence
- [ ] Completion review filed in CVF `docs/reviews/`
- [ ] GC-020 handoff HEAD SHA updated after commit

## Return-To-Orchestrator Conditions

Return immediately if:

- `execute.client.ts` would exceed 220 lines — report line count and stop
- `npm run check` fails after additions — do not commit
- Any of the existing 5 tests breaks — fix before adding new tests

## Target repo

`Controlled-Vibe-Framework-CVF` (governance/provenance repo).
`EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/` only.

## Claim Boundary

C2 covers `--dry-run` and `--receipt` hardening of the existing `cvf execute`
command. It does not add a new command, modify other CLI commands, implement
live HTTP integration, or touch the public-sync repo.
