# CVF Adjustment 1 Inventory — Problem C: CLI Runtime

Memory class: SUMMARY_RECORD

Status: FILED — 2026-05-19. Pre-GC-018 factual inventory per
`docs/reviews/CVF_REVIEW_CVF_ASSESSMENT_AND_DIRECTION_2026-05-18.md`
Adjustment 1 requirement.

## Purpose

Record the factual pre-GC-018 inventory for Problem C so remaining CLI runtime
work is scoped to the actual gaps after Lane B/C/H delivery.

## Source

- `docs/reviews/CVF_REVIEW_CVF_ASSESSMENT_AND_DIRECTION_2026-05-18.md` §
  Adjustment 1 + corrected Problem C
- Live scan of `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/` performed
  2026-05-19 by coordinating agent (Claude)

## Scope / Target / Owner Boundary

Scope: Problem C only — CLI Runtime. Covers what exists in
`CVF_ECO_v2.2_GOVERNANCE_CLI` and what the corrected gap actually is.
Owner: Claude (reviewer role) per Adjustment 1 instruction.

## Findings

### What already exists

**`CVF_ECO_v2.2_GOVERNANCE_CLI` v2.2.0 — source files:**

| File | Lines | Role |
|---|---|---|
| `src/cli.ts` | 33 | Entry point, reads args, calls registry |
| `src/arg.parser.ts` | 63 | Parses CLI flags from process.argv |
| `src/types.ts` | 42 | `CLICommand` union type, `CLIArgs`, `CLIOutput`, `CLICommandHandler` |
| `src/command.registry.ts` | 271 | Command registration + `evaluate`, `execute`, `session`, `report`, `audit`, `status`, `help`, `version` |
| `src/execute.client.ts` | 187 | `cvf execute` — HTTP POST to `/api/execute`; sends `templateId`, `inputs`, `requestedRole`, HMAC-signed |

**Registered commands (`CLICommand` type):**
`evaluate` | `execute` | `session` | `report` | `audit` | `status` | `help` | `version`

**`cvf execute` specifically:**

- Usage: `cvf execute --template <id> --role <role> [--input <json>] [--endpoint <url>] [--verbose]`
- Wired in `command.registry.ts` line 117: `executeAsync: executeGovernedTemplateCommand`
- Sends POST to `/api/execute` on the web platform
- Lane B/C/H delivery added the governed-pack execute path end-to-end

**Tests:**

| File | Notes |
|---|---|
| `tests/arg.parser.test.ts` | arg parsing coverage |
| `tests/cli.test.ts` | CLI entry coverage |
| `tests/command.registry.test.ts` | command dispatch coverage |
| `tests/execute.client.test.ts` | HTTP execute client coverage |

4 test files total. Package has `scripts.check` (TypeScript check) and
`scripts.test`.

### What the actual gap is

The corrected problem map (assessment review, 2026-05-18) states:

> "Real gap: execution gateway (`cvf run/execute/trace`) does not exist."

After Lane B/C/H delivery, **`cvf execute` now exists and is wired** to
the governed execute route. The review's original Problem C claim
(`cvf run/execute/trace` does not exist) is now **partially resolved**:
`cvf execute` exists. What remains:

1. `cvf execute` currently has no `--stream` flag (adding this is Lane D).
2. `cvf benchmark governance` subcommand does not exist (Lane E).
3. No `cvf run` or `cvf trace` alias — not currently demand-gated on a
   named use case; not in scope for Lanes D–G.

### What "done" looks like for the next tranche

Lane E acceptance criterion: `cvf benchmark governance --input <path>`
subcommand registered in `command.registry.ts`, computes 4 governance
reliability metrics from a JSONL audit log, confirmed by unit tests.

Lane D adds `--stream` flag to `cvf execute`.

## Risk

None. Read-only inventory. No code changed.

## Decision / Recommendation / Disposition

Problem C: **PARTIALLY CLOSED** — `cvf execute` exists and is wired.
Remaining gap is `--stream` flag (Lane D) and `cvf benchmark governance`
subcommand (Lane E). No further `cvf run/trace` work authorized without
a new demand-gated GC-018.

## Claim Boundary

This packet is read-only inventory evidence. It does not authorize `cvf run`,
`cvf trace`, public claims, or runtime behavior beyond the lane work orders.
