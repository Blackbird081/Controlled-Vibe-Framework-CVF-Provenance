# Work Order — CDH-C CLI Live Proof

Memory class: FULL_RECORD

Status: READY_FOR_IMPLEMENTATION

docType: work_order

Worker role: Codex

Date dispatched: 2026-05-21

---

## Purpose

Prove the existing `cvf execute` CLI path with a live HTTP call to the CVF
endpoint, demonstrate JSONL receipt persistence, and surface at least one
operator diagnostic error path.

---

## Authority Chain

- CDH-C delta rebuttal:
  `docs/reviews/archive/CVF_CDH_C_DELTA_CODEX_REBUTTAL_2026-05-20.md`
- CDH-C roadmap:
  `docs/roadmaps/CVF_CDH_C_CLI_LIVE_PROOF_ROADMAP_2026-05-21.md`
- C2 prior closure:
  `docs/reviews/archive/CVF_C2_CLI_EXECUTE_HARDENING_COMPLETION_2026-05-19.md`
- GC-018 to be filed:
  `docs/baselines/CVF_GC018_CDH_C_CLI_LIVE_PROOF_2026-05-21.md`

---

## Agent Roles

- Orchestrator: Codex files GC-018 and confirms scope before proceeding.
- Reviewer: Codex reviews its own rebuttal boundary before implementation.
- Implementer: Codex runs live CLI invocation and records evidence.
- Auditor: Codex verifies evidence trace block and closes the packet.

---

## Scope / Target / Owner Boundary

In scope:

- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/execute.client.ts`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts`
- Live `cvf execute` invocation output (redacted).
- JSONL receipt log file (redacted path and first-line structure).
- One diagnostic error path (bad endpoint or missing token).
- `docs/baselines/CVF_GC018_CDH_C_CLI_LIVE_PROOF_2026-05-21.md`
- `docs/reviews/CVF_CDH_C_CLI_LIVE_PROOF_COMPLETION_2026-05-21.md`
- Active queue/state/handoff updates.

Out of scope:

- New CLI command or flag.
- Provider/runtime semantics changes.
- SSE streaming, multi-agent orchestration.
- Installability or packaging.
- Public-sync update.
- Any change to `execute.client.ts` structure beyond diagnostic surfacing.

---

## Required First Reads

- `docs/reviews/archive/CVF_CDH_C_DELTA_CODEX_REBUTTAL_2026-05-20.md`
- `docs/reviews/archive/CVF_C2_CLI_EXECUTE_HARDENING_COMPLETION_2026-05-19.md`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/execute.client.ts`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`

---

## Pre-Flight Checks

- Confirm `cvf execute` is registered in `command.registry.ts` (exact
  registration line must be cited in evidence).
- Confirm CVF web endpoint is reachable at the operator-configured URL.
- Confirm live provider key is available without printing raw value.
- Confirm no prior CDH-C live proof GC-018 exists for this date.
- Run `python governance/compat/check_markdown_structural_completeness.py
  --base HEAD --head HEAD --enforce` — must be COMPLIANT before staging.

---

## Write Ownership

Permitted writes:

| File | Change |
| --- | --- |
| `docs/baselines/CVF_GC018_CDH_C_CLI_LIVE_PROOF_2026-05-21.md` | New GC-018 baseline |
| `docs/reviews/CVF_CDH_C_CLI_LIVE_PROOF_COMPLETION_2026-05-21.md` | Completion review |
| `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` | Update cdh-c-delta status |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Update nextAllowedMove |
| `AGENT_HANDOFF_V10_2026-05-19.md` | GC-020 sync |
| `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/execute.client.ts` | Diagnostic surfacing only if needed |

No other files may be modified.

---

## Execution Plan

1. File `CVF_GC018_CDH_C_CLI_LIVE_PROOF_2026-05-21.md` (C-01).
2. Run `cvf execute` against CVF endpoint with an authorized governed
   template; capture redacted output (C-02).
3. Verify JSONL receipt log exists on disk; record redacted file path and
   first-line structure (C-03).
4. Trigger one diagnostic error path (bad endpoint URL or missing service
   token); record the CLI error message shown to the operator (C-04).
5. File `CVF_CDH_C_CLI_LIVE_PROOF_COMPLETION_2026-05-21.md` with evidence
   trace block (C-05).
6. Update active queue/state/handoff (C-06).
7. Run governance checks (C-07):
   `python governance/compat/check_markdown_structural_completeness.py --base HEAD --head HEAD --enforce`
   `python governance/compat/check_docs_governance_compat.py --base HEAD --head HEAD --enforce`

---

## Evidence Requirements

| Claim | Required evidence |
| --- | --- |
| Live invocation success | HTTP 200, `success=true`, decision ALLOW, receipt id, trace id — all in evidence trace block |
| No mock fallback | Output shows `evidenceMode: live` or equivalent, no `mock_fallback` flag |
| JSONL receipt on disk | Redacted file path + first-line key structure (no raw secrets) |
| Diagnostic path works | CLI error message text for the triggered error case |
| No new command surface | `command.registry.ts` diff shows no new `register()` call |
| Registration confirmed | Exact registration line for `cvf execute` cited |

---

## Acceptance Criteria

- [ ] GC-018 baseline filed.
- [ ] Live `cvf execute`: HTTP 200, `success=true`, decision ALLOW, receipt
      id present, non-mock output, `evidenceMode: live`.
- [ ] JSONL log file confirmed on disk (redacted).
- [ ] Diagnostic error path: CLI error message recorded.
- [ ] No new command, flag, or provider semantics.
- [ ] Governance checks exit 0.
- [ ] Completion review filed.
- [ ] Active queue `cdh-c-delta` status updated.

---

## Review Gate

Close only after C-07 governance checks exit 0 and all evidence trace block
rows are filled with real (not placeholder) values.

---

## Closure Checklist

- [ ] GC-018 filed.
- [ ] Live invocation run and output captured.
- [ ] JSONL log confirmed.
- [ ] Diagnostic error path tested.
- [ ] Completion review filed.
- [ ] Queue/state/handoff updated.
- [ ] Governance checks PASS.

---

## Return-To-Orchestrator Conditions

Return to Orchestrator (do not close) if:

- CVF endpoint is unreachable and live invocation cannot be completed.
- Live output contains a raw API key or secret that cannot be redacted.
- The invocation requires a new CLI command or new provider semantics.
- Any governance check exits non-zero.

---

## Operator Checkpoint

Checkpoint required: operator must confirm that the CVF web endpoint is
running and accessible (local or tunnel) before Codex proceeds to step C-02.
If the endpoint is not available, Codex must return to Orchestrator rather
than substituting a dry-run as live proof.

---

## Claim Boundary

This work order closes only a live-proof and diagnostic hardening delta for
the existing `cvf execute` CLI path. It does not prove broad CLI stability,
all-provider CLI parity, SSE streaming, multi-agent orchestration, or any
public product capability.
