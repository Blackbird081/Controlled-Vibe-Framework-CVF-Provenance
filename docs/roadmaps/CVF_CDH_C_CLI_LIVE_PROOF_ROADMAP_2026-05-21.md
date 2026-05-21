# CVF CDH-C CLI Live Proof Roadmap

Memory class: FULL_RECORD

Status: READY_FOR_IMPLEMENTATION

docType: roadmap

Date: 2026-05-21

---

## Purpose

Prove the existing `cvf execute` CLI path with a live HTTP call, demonstrate
JSONL receipt persistence, and surface at least one operator diagnostic error
path to close the CDH-C live-proof gap.

---

## Authorization

Authorized by:

- CDH-C delta rebuttal:
  `docs/reviews/CVF_CDH_C_DELTA_CODEX_REBUTTAL_2026-05-20.md`
- CDH delta meta-roadmap:
  `docs/roadmaps/CVF_CDH_DELTA_META_ROADMAP_2026-05-20.md`
- C2 prior closure:
  `docs/reviews/CVF_C2_CLI_EXECUTE_HARDENING_COMPLETION_2026-05-19.md`

This roadmap requires a fresh CDH-C GC-018 before implementation begins.

---

## Why

The CDH-C rebuttal confirmed that `cvf execute` and `cvf run` already exist
and local CLI tests pass. The remaining gap is **live proof**: no evidence
exists of a real HTTP call from the CLI to `/api/execute` returning a
governed receipt. Without this proof, CVF cannot claim a working CLI
governance path to operators or external reviewers.

A second gap is **receipt persistence observability**: the JSONL receipt
log path exists in code but has not been demonstrated with a real invocation
showing the log file on disk after execution.

A third gap is **operator diagnostics**: there is no documented or tested
path for an operator to diagnose a misconfigured endpoint, bad service token,
or missing pack — the errors that will actually occur in day-one use.

---

## Scope

In scope:

- Live `cvf execute` invocation against the running CVF web endpoint.
- Redacted proof output showing HTTP 200, governed receipt, decision ALLOW.
- JSONL receipt log file on disk after invocation (redacted path shown).
- Operator diagnostics: at least one error path tested (bad endpoint or
  missing token), with a clear error message surfaced to the CLI user.
- GC-018 baseline for this tranche.
- Completion review.

Out of scope:

- Adding a new execute command or new CLI flag.
- New provider/runtime semantics.
- Installability or packaging.
- Public-sync update (bounded private proof only).
- Any claim that CDH-C proves broad CLI stability.

---

## Non-Goals

- Proving all providers via CLI (only the existing authorized provider lane).
- Proving SSE streaming via CLI.
- Proving multi-agent orchestration via CLI.
- Modifying `command.registry.ts` or `execute.client.ts` structure beyond
  diagnostic improvements.

---

## Work Plan

| Step | Artifact | Owner |
| --- | --- | --- |
| C-01 | File GC-018 baseline | Codex/Orchestrator |
| C-02 | Run live `cvf execute` against CVF endpoint; capture redacted output | Codex/Implementer |
| C-03 | Verify JSONL receipt file on disk; record redacted file path + first line structure | Codex/Implementer |
| C-04 | Test one diagnostic error path; record CLI error message | Codex/Implementer |
| C-05 | File completion review with evidence trace block | Codex/Auditor |
| C-06 | Update active queue/state/handoff | Codex/Auditor |

---

## Acceptance Criteria

- [ ] GC-018 baseline filed.
- [ ] Live `cvf execute` invocation: HTTP 200, `success=true`, decision
      `ALLOW`, receipt id present, non-mock output.
- [ ] JSONL receipt log file exists on disk after invocation (redacted).
- [ ] At least one operator diagnostic error path tested and surfaced.
- [ ] Completion review filed with full evidence trace block.
- [ ] No new command, flag, provider semantics, or public-sync update.

---

## Verification / Evidence

All claims must be backed by:

- Redacted command output (no raw API keys).
- Receipt id and trace id in the evidence trace block.
- JSONL log file path (redacted, not raw content).
- CLI error message text for the diagnostic path.

---

## Claim Boundary

This roadmap closes only a live-proof and diagnostic hardening delta for the
existing `cvf execute` CLI path. It does not prove broad CLI stability, all-
provider CLI parity, SSE streaming, multi-agent orchestration, or any public
product capability beyond what the evidence trace block explicitly records.
