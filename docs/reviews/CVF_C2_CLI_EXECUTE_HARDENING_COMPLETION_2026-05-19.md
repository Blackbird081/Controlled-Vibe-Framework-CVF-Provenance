# CVF C2 CLI Execute Hardening Completion

Memory class: FULL_RECORD

Status: CLOSED

Reviewer / Worker: Codex

Date: 2026-05-19

---

## Purpose

Record implementation and verification evidence for C2: harden the existing
`cvf execute` gateway with dry-run output and structured receipt persistence.

---

## Scope / Target / Owner Boundary

In scope:

- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/execute.client.ts`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/tests/execute.client.test.ts`

Out of scope:

- Live HTTP integration tests.
- New CLI commands.
- Provider/runtime behavior.
- Public-sync repository changes.

---

## Target / Source Under Review

Work order:

- `docs/work_orders/CVF_AGENT_WORK_ORDER_C2_CLI_EXECUTE_HARDENING_2026-05-19.md`

Roadmap:

- `docs/roadmaps/CVF_RUNTIME_MATURITY_DELTA_ROADMAP_V2_2026-05-19.md`

Implemented paths:

- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/execute.client.ts`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/tests/execute.client.test.ts`

---

## Scope / Methodology

Method:

1. Verified existing execute client and test shape before editing.
2. Added `--dry-run` handling before any `fetch()` call.
3. Added `appendExecuteReceipt()` JSONL persistence for successful receipts.
4. Updated execute command help/usage for `--dry-run` and `--receipt`.
5. Added targeted unit tests for dry-run redaction and JSONL receipt shape.

No raw service tokens were printed.

---

## Findings / Position

Position: C2 is implemented and locally verified.

Findings:

1. `buildDryRunOutput()` redacts `x-cvf-service-token` and
   `x-cvf-service-signature` from reported header keys.
2. `executeGovernedTemplateCommand()` returns dry-run output without calling
   HTTP when `--dry-run` is set.
3. `appendExecuteReceipt()` creates parent directories and appends one JSONL
   receipt line with timestamp, template, role, workflow, and binding fields.
4. Existing execute behavior remains covered by the expanded test suite.

---

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| Secret header leakage in dry-run output | Dry-run output removes service token and signature keys |
| Receipt path directory missing | `appendExecuteReceipt()` creates the directory recursively |
| Work-order fixture count was stale | Completion evidence records current suite size: 62 total tests, 10 execute-client tests |

---

## Evidence / Verification

### CLI Tests

Command:

```powershell
npm test
```

Run in:

```text
EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI
```

Result:

```text
Test Files  5 passed (5)
Tests       62 passed (62)
```

`tests/execute.client.test.ts` now contains 10 passing tests.

Verdict: PASS.

### Type Check

Command:

```powershell
npm run check
```

Run in:

```text
EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI
```

Result:

```text
tsc --noEmit
```

Verdict: PASS.

### Line Counts

Command:

```powershell
(Get-Content src/execute.client.ts).Count
(Get-Content tests/execute.client.test.ts).Count
```

Result:

```text
208
191
```

Verdict: PASS.

### Dry-Run Redaction And JSONL Shape

Evidence:

- Dry-run tests assert HTTP is not called and `x-cvf-service-token` is absent
  from `headerKeys`.
- JSONL test writes a temporary line and asserts `templateId`,
  `requestedRole`, `workflowId`, `receiptBinding`, and string timestamp shape.

Verdict: PASS.

---

## Acceptance Criteria

| Criterion | Status | Evidence |
| --- | --- | --- |
| `buildDryRunOutput` added; `execute.client.ts` <= 220 lines | PASS | 208 lines |
| `appendExecuteReceipt` added; `execute.client.ts` <= 220 lines | PASS | 208 lines |
| `--dry-run` and `--receipt` wired | PASS | Command registry and execute client updated |
| Execute-client tests pass | PASS | 10 execute-client tests, 62 total tests |
| `npm run check` passes | PASS | `tsc --noEmit` PASS |
| Token absent from dry-run header keys | PASS | Unit assertion |

---

## Decision / Recommendation / Disposition

Disposition: **CLOSED**.

C2 closes the requested CLI hardening delta. Runtime/live provider behavior was
not modified and no live HTTP integration claim is made.

---

## Claim Boundary

C2 may be described as:

> The existing `cvf execute` CLI path now supports dry-run inspection and JSONL
> receipt persistence with passing local unit and type checks.

C2 must not be described as:

> a new command, a live HTTP/provider integration proof, or a public repository
> release.
