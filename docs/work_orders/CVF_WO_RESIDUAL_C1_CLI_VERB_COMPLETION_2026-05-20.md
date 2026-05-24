# Work Order — Residual C1: CLI Verb Completion

Memory class: FULL_RECORD

Status: CLOSED

docType: work_order

Worker role: Codex (Implementer)

Orchestrator: Claude

Date dispatched: 2026-05-20

Predecessor:

- `docs/roadmaps/archive/CVF_REVIEW_CVF_RESIDUAL_CLOSURE_ROADMAP_2026-05-19.md` (Candidate C1, corrected after rebuttal)
- `docs/reviews/archive/CVF_REVIEW_CVF_RESIDUAL_CLOSURE_ROADMAP_CODEX_REBUTTAL_2026-05-19.md` (Codex: BLOCKING, corrected — GC-018 now required)

Rebuttal correction note: the roadmap originally marked C1 as `GC-018 required: No`.
Codex rebuttal identified this as an internal contradiction — adding five
canonical CLI verbs changes the public command surface and requires a GC-018
baseline naming each verb's backing source, input shape, error behavior,
and forbidden behaviors. This work order corrects that.

---

## Purpose

Register five new read-only CLI verbs in the CVF governance CLI to close the
gap between the 4 currently registered audit-task verbs and the 9 verbs
named in the 17.05 audit ask.

All five verbs are thin read-only wrappers over existing infrastructure. None
introduces mutation, network provider calls, or new auth paths.

---

## Scope / Target / Owner Boundary

In scope:

- Five new command registrations in
  `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts`.
- One GC-018 baseline naming each verb's backing source and forbidden behaviors.
- Five new Vitest test files (one per verb, 4–6 tests each, mock backends only).
- All existing CLI tests must continue to pass.

Out of scope:

- New runtime paths.
- Network provider calls of any kind.
- New auth or RBAC surfaces.
- Changes to any file outside `CVF_ECO_v2.2_GOVERNANCE_CLI/`.
- `cvf run` as a separate runtime — it is an alias only.

Constraint: each verb's `execute` (or `executeAsync`) handler must be read-only.
Any verb found to require mutation, network I/O, or auth during implementation
must be HELD and reported to the Orchestrator before proceeding.

---

## Per-Verb Backing Source (required in GC-018)

| Verb | Backing source | Forbidden |
|---|---|---|
| `cvf run <template>` | Alias to `cvf execute --template <template>`; delegates to existing `execute` handler; no new logic | New runtime path, mutation, provider call |
| `cvf skill list` | Read-only list of skill registry entries from existing skill index / registry file | Skill mutation, network fetch |
| `cvf skill show <id>` | Read-only detail view of one skill by ID from existing skill index | Skill mutation, network fetch |
| `cvf receipt show <id>` | Read-only inspection of an existing receipt artifact via `audit-memory-receipt.ts` output path | Receipt mutation, auth bypass |
| `cvf trace dump [--session <id>]` | Read-only dump of existing audit log JSONL, filtered by session if provided | Log mutation, new log creation |
| `cvf provider list` | Read-only listing of registered provider lanes from existing provider registry | Provider mutation, network call, key exposure |

---

## Deliverables

### Step C1.1 — GC-018 Baseline

File: `docs/baselines/CVF_GC018_C1_CLI_VERB_COMPLETION_2026-05-20.md`

Required sections: `## Status`, `## Source or Predecessor Evidence`,
`## Purpose / Decision / Baseline`, `## Scope or Proposed Tranche`,
`## Evidence / Required Evidence / Verification`, `## Claim Boundary`.

The baseline must:

- Include the per-verb table above (or equivalent structured content) showing
  each verb's backing source and forbidden behaviors.
- Confirm `cvf run` is an alias, not a new runtime.
- Confirm all five verbs are read-only.
- State that any verb requiring mutation or new I/O must be held and reported.

### Step C1.2 — Command Registrations

Extend `command.registry.ts` with five new command entries. Each entry must
have at minimum: `name`, `description`, `usage`, `execute` (or `executeAsync`).

`cvf run`:
- Name: `run`
- Maps to: existing `execute` handler with `--template` argument forwarding.
- Must not duplicate the `execute` implementation; must delegate to it.

`cvf skill list` and `cvf skill show`:
- Subcommand pattern consistent with existing CLI subcommand conventions.
- Read from the existing skill registry file (determine path from
  existing codebase; do not hardcode a new path).
- Output: plain table for `list`, detail block for `show`.

`cvf receipt show <id>`:
- Read from the `audit-memory-receipt.ts` output path.
- If a receipt with the given ID does not exist, exit with a clear error
  message and non-zero exit code.

`cvf trace dump [--session <id>]`:
- Read from the existing audit JSONL log.
- `--session` flag is optional; omitting it dumps all entries.
- Output: one JSON object per line (JSONL), or formatted table if
  `--format table` flag is added (consistent with existing `benchmark` output).

`cvf provider list`:
- Read from the existing provider registry.
- Output: plain table of provider names and their status.

### Step C1.3 — Test Files

One Vitest test file per verb (5 files). All tests use mock backends; no live
provider calls.

Naming convention: `tests/commands/cvf-run.test.ts`,
`tests/commands/cvf-skill.test.ts`, `tests/commands/cvf-receipt.test.ts`,
`tests/commands/cvf-trace.test.ts`, `tests/commands/cvf-provider.test.ts`.

Minimum 4 tests per file:

- Command registers successfully in `CommandRegistry`.
- Read path returns expected output shape for valid input.
- Missing / invalid input returns a clear error (non-zero exit).
- No mutation occurs (verify mock backend is never called with write methods).

Total new test count: approximately 20–30 tests.

Existing CLI tests must all continue to pass after this change.

### Step C1.4 — Closure Review

File: `docs/reviews/CVF_C1_CLI_VERB_COMPLETION_CLOSURE_REVIEW_2026-05-20.md`

Required structure: Purpose, Target, Scope/Methodology, Findings,
Decision/Disposition, Claim Boundary.

The closure review must confirm:

- GC-018 authorized before any command was registered.
- Five verbs registered in `command.registry.ts`.
- All five are read-only; no mutation, network call, or auth path introduced.
- 5 new test files, all PASS.
- Existing CLI tests remain PASS (`npm test` in `CVF_ECO_v2.2_GOVERNANCE_CLI`).
- `npm run check` PASS.
- Pre-commit and pre-push hooks PASS.

---

## Acceptance Criteria

All of the following must be true before this work order is CLOSED:

- [ ] GC-018 baseline exists and is AUTHORIZED with per-verb backing-source
      table.
- [ ] Five new command entries in `command.registry.ts`.
- [ ] `cvf run` delegates to existing `execute` handler; no new runtime path.
- [ ] All five verbs verified read-only (no mutation, no network, no auth).
- [ ] 5 new test files, minimum 4 tests each, all PASS.
- [ ] Existing CLI tests remain PASS.
- [ ] `npm test` PASS in `CVF_ECO_v2.2_GOVERNANCE_CLI`.
- [ ] `npm run check` PASS.
- [ ] Pre-commit and pre-push hooks PASS.
- [ ] Closure review filed confirming all above.

---

## Forbidden Actions

- Do NOT implement any verb that requires mutation, network I/O, or a new
  auth path. Hold and report instead.
- Do NOT add new runtime semantics to `cvf run` beyond argument forwarding.
- Do NOT shadow or override an existing command name.
- Do NOT add provider API calls to any test (mock backends only).
- Do NOT change files outside `CVF_ECO_v2.2_GOVERNANCE_CLI/`.

---

## Authority Chain

- Authorized by: Codex rebuttal correction (C1: BLOCKING → GC-018 now required); roadmap corrected 2026-05-20
- Roadmap: `docs/roadmaps/archive/CVF_REVIEW_CVF_RESIDUAL_CLOSURE_ROADMAP_2026-05-19.md` (REBUTTAL_ACCEPTED)
- Orchestrator: Claude; Worker: Codex; Operator approval required for GC-018

---

## Agent Roles

- Worker (Codex): GC-018, command registrations, test files, closure review
- Orchestrator (Claude): reviews closure review; must approve GC-018 before implementation

---

## Required First Reads

1. `docs/roadmaps/archive/CVF_REVIEW_CVF_RESIDUAL_CLOSURE_ROADMAP_2026-05-19.md` — C1 scope and per-verb mapping
2. `docs/reviews/archive/CVF_REVIEW_CVF_RESIDUAL_CLOSURE_ROADMAP_CODEX_REBUTTAL_2026-05-19.md` — C1 BLOCKING finding and required corrections
3. `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts` — current registered commands
4. `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/` — scan for existing skill registry, receipt, audit-log, provider registry access patterns

---

## Pre-Flight Checks

- [ ] Read `command.registry.ts` to confirm current 9 registered commands and no naming conflicts
- [ ] Identify backing source file for each verb (skill registry, receipt path, audit log path, provider registry)
- [ ] Confirm `npm test` baseline PASS before starting implementation
- [ ] GC-018 must be AUTHORIZED before any command is registered

---

## Write Ownership

May create or modify only files under `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/`, plus:

- `docs/baselines/CVF_GC018_C1_CLI_VERB_COMPLETION_2026-05-20.md` (new)
- `docs/reviews/CVF_C1_CLI_VERB_COMPLETION_CLOSURE_REVIEW_2026-05-20.md` (new)

---

## Execution Plan

1. File GC-018 baseline with per-verb backing-source table (Step C1.1) — AUTHORIZED before Step C1.2
2. Add five command registrations to `command.registry.ts` (Step C1.2)
3. Create five test files, one per verb (Step C1.3)
4. File closure review (Step C1.4)

---

## Evidence Requirements

- GC-018 AUTHORIZED with per-verb backing-source table and forbidden behaviors
- Five new entries in `command.registry.ts`, all verified read-only
- 5 new test files (minimum 4 tests each), all PASS
- Existing CLI tests remain PASS
- `npm test` PASS, `npm run check` PASS

---

## Review Gate

Stop and return to Orchestrator before registering any verb if:

- The verb's backing source cannot be identified in the working tree
- Implementing a verb would require mutation, network I/O, or new auth logic

---

## Closure Checklist

- [ ] GC-018 AUTHORIZED with per-verb table
- [ ] 5 new command entries in `command.registry.ts`
- [ ] All 5 verbs confirmed read-only (no mutation, no network, no auth)
- [ ] 5 new test files, all PASS
- [ ] Existing CLI tests remain PASS
- [ ] `npm test` PASS, `npm run check` PASS
- [ ] Pre-commit and pre-push hooks PASS
- [ ] Closure review filed

---

## Return-To-Orchestrator Conditions

Return if: any verb requires mutation or new I/O; GC-018 cannot be authorized due to scope inflation; hook failure outside this scope.

---

## Claim Boundary

This work order covers five read-only CLI verbs + GC-018 + tests + closure
review only. It does not authorize new runtime paths, new provider execution,
new auth surfaces, or any change outside the governance CLI extension.
