# CVF Work Order — LHW2-T3 Tool Approval MA1 Handoff Connector

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-05-27

---

## Purpose

Implement LHW2-T3: a connector spec mapping each TA1 tool approval state to its
MA1 transfer packet outcome. Closes the gap where TA1 outputs a detailed approval
state (pending, blocked, satisfied-but-not-executable, etc.) but no connector
defines how that state routes into a governance handoff packet for the
Orchestrator or Auditor to act on.

Documentation-only tranche. No source code, runtime module, route, or provider
behavior is changed. `runtimeExecutionAuthorized=false` is preserved throughout.

## Authority Chain

- LHW2 roadmap: `docs/roadmaps/CVF_LHW2_WORKFLOW_CONNECTOR_COMPLETION_ROADMAP_2026-05-27.md`
- Fast Lane audit: `docs/reviews/CVF_LHW2_T3_FAST_LANE_AUDIT_2026-05-27.md` → FAST_LANE_READY
- LH1 ledger (`pancake-pos-mcp` trigger): `docs/reference/archive/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
- TA1: `docs/reviews/archive/CVF_TA1_TOOL_ACTION_APPROVAL_READOUT_COMPLETION_2026-05-25.md`
- W3: `docs/reviews/CVF_W3_TOOL_MCP_DATABASE_ACTION_TAXONOMY_COMPLETION_2026-05-24.md`
- MA1 standard: `docs/reference/CVF_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_STANDARD_2026-05-26.md`
  (read full sections 0–9)
- LHW1-T2 boundary table: `docs/reference/CVF_LHW1_WORKFLOW_CHAIN_STATE_CONNECTOR_SPEC_2026-05-27.md`
  (S7 row: "Role assignment enforcement — doc-only → Future: role-gate in /api/execute")

## Gate Conditions — MUST CHECK ALL BEFORE STARTING

```text
Gate 1 — T1 status: read docs/reviews/CVF_LHW2_T1_*_COMPLETION_2026-05-27.md
         Verdict must be: CLOSED_PASS

Gate 2 — T2 status: read docs/reviews/CVF_LHW2_T2_*_COMPLETION_2026-05-27.md
         Verdict must be: CLOSED_PASS
```

If either gate fails, stop immediately. Do not implement T3.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. T1 completion (understand loop connector foundation)
4. T2 completion (understand packet structure pattern T3 must follow)
5. `docs/reviews/archive/CVF_TA1_TOOL_ACTION_APPROVAL_READOUT_COMPLETION_2026-05-25.md`
   — confirm the 6 TA1 approval states and `runtimeExecutionAuthorized=false` binding
6. `docs/reviews/CVF_W3_TOOL_MCP_DATABASE_ACTION_TAXONOMY_COMPLETION_2026-05-24.md`
   — confirm W3 action risk classes that feed TA1 input
7. `docs/reference/CVF_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_STANDARD_2026-05-26.md`
   — sections 0–9; identify which sections apply to approval request vs block notification
8. `governance/contracts/tool-action-taxonomy.ts`
   — read-only to confirm TA1 approval state names; do NOT modify

If any required file is missing, stop and report to Orchestrator.

## Scope

**Allowed:**

- `docs/reference/CVF_LHW2_TOOL_APPROVAL_MA1_HANDOFF_CONNECTOR_SPEC_2026-05-27.md`
  (new — primary deliverable)
- this work order (status update only)
- session continuity files

**Forbidden:** `EXTENSIONS/` (any file), `governance/contracts/` (any file),
`tool-action-taxonomy.ts`, any `.ts`/`.tsx`/`.js`/`.py` file, receipt envelope
schema, public-sync repo. MCP bridge, transport, database runtime, and approval
ticket persistence remain permanently blocked for this tranche.

## Deliverable — Connector Spec

File: `docs/reference/CVF_LHW2_TOOL_APPROVAL_MA1_HANDOFF_CONNECTOR_SPEC_2026-05-27.md`

Required sections:

### S1 — Purpose and claim boundary

- State what the connector is: a normative doc mapping TA1 approval states to
  MA1 transfer packet outcomes.
- State what it is not: not a TA1/W3 runtime extension; not a tool execution
  authority; not an approval persistence mechanism.
- Explicit statement: "`runtimeExecutionAuthorized=false` is preserved from W3
  and TA1. This connector does not grant any form of execution authority.
  Approval state in a packet is a governance signal, not an execution trigger."

### S2 — TA1 approval state to MA1 packet mapping

One row per TA1 approval state. Columns:
`TA1 state` | `Packet type` | `When issued` | `Required MA1 sections (R/O/N/A)` |
`Minimum packet fields` | `Next role action`

Minimum rows:

- `not_required` — no packet needed; advance immediately
- `pending_approval` — approval request packet; R: ##0, ##1, ##2, ##3, ##4,
  ##7, ##8, ##9; who approves, what evidence is missing, which role receives packet
- `satisfied_but_not_executable` — readiness-confirmed packet; R: ##0, ##1,
  ##2, ##8, ##10; note: execution remains gated; what additional gate is pending
- `blocked_before_approval` — block notification packet; R: ##0, ##1, ##2,
  ##3, ##8, ##10; stop condition, safe message, corrective action
- `blocked_by_policy` — policy block packet; R: ##0, ##1, ##2, ##7, ##8,
  ##10; Auditor must confirm; escalation path
- `incomplete_approval` — missing-evidence packet; R: ##0, ##1, ##2, ##3,
  ##4, ##7; list missing evidence fields; which role resolves

Use TA1 approval state names verbatim. Reference MA1 section numbers and names
from the canonical standard (##0 through ##10) — do not re-define MA1 structure.

### S3 — Source Verification Table (mandatory)

Required columns: `Claimed field` | `Source file` | `Verified field path` |
`Owning interface/function` | `Disposition`

Cover every TA1 approval state name cited in S2 and the MA1 section-number
contract used in S2. Valid dispositions are `ACCEPT`, `REJECT`, and
`BLOCKED_SOURCE_NOT_FOUND`. If any state name or MA1 section reference cannot
be source-verified against `tool-action-taxonomy.ts` or the canonical MA1
standard, mark Disposition as `BLOCKED_SOURCE_NOT_FOUND`, stop, and return to
Orchestrator. No blocked, guessed, inferred, or confirm-later state may remain
in S2.

### S4 — Demand-gated items

Explicitly state what T3 does NOT absorb:

- `pancake-pos-mcp` approval transport and business tool runtime: remains
  PARTIALLY_ABSORBED per LH1; reopen only for MCP approval proof with runtime GC-018.
- Persisted approval tickets or approval queue: demand-gated; not in scope.
- Live tool/MCP/database execution proof: demand-gated; requires dedicated
  execution tranche.
- `CLI-Anything` sandboxed execution integration: demand-gated; not in scope.

### S5 — Runtime-enforcement boundary table

| Behavior | Current status | Future path |
| --- | --- | --- |
| W3 tool action risk classification | Runtime (governance/contracts) | Stable |
| TA1 approval state readout | Runtime (governance/contracts) | Stable |
| MA1 transfer packet format | Document standard | Future: MA1 schema validator |
| Approval request packet routing | Document-only | Future: approval request queue |
| Block notification delivery | Document-only | Future: governed notification surface |
| Execution gate enforcement | Document-only | Future: role-gate in /api/execute |

Do not label any row "Runtime" unless a closed PASS tranche implements it.

## Pre-Flight

- [ ] Gate 1: T1 CLOSED_PASS confirmed
- [ ] Gate 2: T2 CLOSED_PASS confirmed
- [ ] Working tree clean
- [ ] All required first reads done
- [ ] TA1 approval state names confirmed from `tool-action-taxonomy.ts`

## Agent Roles

Implementer confirms both gates, writes spec (S1–S5), populates Source
Verification Table, updates session continuity. Reviewer checks TA1 state names
verbatim, MA1 section refs correct, demand-gated items listed, `runtimeExecutionAuthorized=false`
preserved, no `.ts` file touched. Auditor confirms gates documented, `pancake-pos-mcp`
LH1 trigger recorded, no execution authority granted, LHW2 roadmap closure
prepared. No self-review.

## Write Ownership

Implementer owns all new files. No file outside the Allowed list may be modified.

## Execution Plan

1. Check both gates. If either fails → stop and report to Orchestrator.
2. Read all required first reads.
3. Draft spec (S1–S5) with Source Verification Table.
4. Confirm no code file staged.
5. Reviewer perspective — record result.
6. Update session continuity (`lhw2_t3_complete`).
7. Update LHW2 roadmap `Status` to `CLOSED_PASS_BOUNDED`.
8. Commit: `docs(lhw2-t3): add tool approval MA1 handoff connector spec`.
9. Write completion review.

Spec size guard: < 200 lines. Trim S4 prose if approaching 180 lines.

## Review Gate

Before committing: Reviewer perspective completed; all gate conditions documented;
`runtimeExecutionAuthorized=false` confirmed; demand-gated items listed; Source
Verification Table complete; no code file in diff.

## Acceptance Criteria

- [ ] Both gate conditions confirmed and documented
- [ ] All 6 TA1 approval states mapped to distinct packet outcomes
- [ ] MA1 sections marked R/O/N/A per packet type
- [ ] Source Verification Table present with no `BLOCKED_SOURCE_NOT_FOUND` rows
- [ ] Demand-gated items explicitly listed in S4
- [ ] `runtimeExecutionAuthorized=false` stated explicitly
- [ ] Runtime boundary table present and honest
- [ ] No code file in diff
- [ ] LHW2 roadmap status updated to `CLOSED_PASS_BOUNDED`
- [ ] Session continuity updated

## Evidence Requirements

- Spec at target path with all 5 sections present
- Both gate conditions confirmed and documented in completion review
- All 6 TA1 approval states mapped to distinct packet outcomes in S2
- MA1 sections marked R/O/N/A per packet type using canonical section numbers
- S3 Source Verification Table complete; no `BLOCKED_SOURCE_NOT_FOUND` rows
- Demand-gated items explicitly listed in S4
- `runtimeExecutionAuthorized=false` stated explicitly in S1
- S5 boundary table present; no doc-only row labeled Runtime
- No `.ts`/`.tsx`/`.js`/`.py` file in `git diff --name-only`
- LHW2 roadmap status updated to `CLOSED_PASS_BOUNDED`
- Session continuity updated to `lhw2_t3_complete`
- Completion review written

## Closure Checklist

- [ ] Gate 1 (T1 CLOSED_PASS) confirmed and documented
- [ ] Gate 2 (T2 CLOSED_PASS) confirmed and documented
- [ ] Spec created with all 5 sections
- [ ] All 6 TA1 approval states mapped with MA1 sections R/O/N/A
- [ ] S3 Source Verification Table complete; no `BLOCKED_SOURCE_NOT_FOUND` rows
- [ ] Demand-gated items listed in S4
- [ ] `runtimeExecutionAuthorized=false` explicit
- [ ] S5 boundary table honest; no doc-only row labeled Runtime
- [ ] No code file in diff
- [ ] LHW2 roadmap updated to `CLOSED_PASS_BOUNDED`
- [ ] Session continuity updated

## Return-To-Orchestrator Conditions

Stop and report to Orchestrator if:

- either gate condition is not met;
- any required first read file is missing or unreadable;
- a TA1 approval state name cannot be confirmed from `tool-action-taxonomy.ts`
  without modifying it;
- writing the connector requires extending TA1 with a new approval state not
  in the existing 6-state vocabulary;
- writing the connector requires modifying `tool-action-taxonomy.ts`;
- spec exceeds 200 lines before S4 is complete.

## Operator Checkpoint

operator.checkpoint.waiver: Low-risk documentation-only tranche gated by T1
and T2 CLOSED_PASS pre-conditions; no operator checkpoint required unless a
conflict with TA1 TypeScript vocabulary or LHW2 roadmap closure is discovered.

## Claim Boundary

LHW2-T3 produces a documentation artifact. It does not claim TA1/W3 runtime
extension, tool/MCP/database execution authority, approval ticket persistence,
MCP bridge or transport, route-level enforcement, receipt envelope extension,
provider behavior, hosted readiness, production readiness, or public release
readiness.

After T3 closes, LHW2 is `CLOSED_PASS_BOUNDED`. No further LHW2 tranche is
authorized without a fresh roadmap and GC-018.
