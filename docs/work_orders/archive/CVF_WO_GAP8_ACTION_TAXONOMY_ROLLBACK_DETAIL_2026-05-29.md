# CVF Work Order — Gap 8 Action Taxonomy Per-Action Rollback Detail

Memory class: FULL_RECORD

Status: CLOSED_PASS

docType: work_order

Date: 2026-05-29

---

## Purpose

Implement CVF 25.05 Gap 8 remaining portion: add per-action rollback detail
spec for each `ToolActionSideEffect` value in W3's tool-action taxonomy.

W3 (`cvf.toolActionTaxonomy.w3.v1`) already provides a boolean gate:
`rollbackRequired` is computed and `rollbackDeclared` is checked at dispatch.
What is missing is a **per-action rollback detail record** that specifies, for
each side-effect category, the minimum rollback evidence required, the rollback
steps, and the escalation path when rollback is not possible.

Source: CVF 25.05 Gop_y.md Gap 8 — "Action taxonomy is partially covered by
W3/TA1/LHW connector waves, but per-action rollback detail (what evidence is
needed, what steps apply, what escalation applies per side-effect category) is
not specified. Governance Auditors cannot verify rollback quality from the
current boolean gate alone."

This work order is **DEMAND_GATED** — operator must explicitly authorize
before implementation begins.

---

## Authority Chain

- CVF 25.05 review: `.private_reference/legacy/CVF 25.05/CLAUDE_REVIEW_OF_GOP_Y_2026-05-25.md`
  — Gap 8 section
- W3 contract: `governance/contracts/tool-action-taxonomy.ts`
  — `ToolActionSideEffect` (line 16), `rollbackDeclared` (line 93),
    `rollbackRequired` (line 118)
- TA1 readout: `governance/contracts/tool-action-taxonomy.ts`
  — `buildToolActionApprovalReadout()` with `rollback_plan` evidence type
- PD roadmap: `docs/roadmaps/CVF_PRODUCT_DEPTH_ROADMAP_2026-05-29.md`
  — Gap 8 row: PARTIALLY_CLOSED

---

## Gap Analysis

### What W3 already provides

- `rollbackRequired: boolean` — computed from `sideEffect` and
  `mutationCaptureRequired`
- `rollbackDeclared?: boolean` — caller must supply; gate blocks if missing
- `rollback_plan` approval evidence type — listed in `ToolActionApprovalEvidence`
- Gate logic: blocks execution if `rollbackRequired && !rollbackDeclared`

### What is missing (Gap 8 remainder)

No spec defines, per `ToolActionSideEffect` value:
- **Minimum rollback evidence**: what artifact proves rollback is possible
- **Rollback steps**: ordered steps specific to the side-effect category
- **Escalation path**: what to do when rollback cannot be performed
- **Rollback time bound**: how long rollback evidence must be retained

Without this, `rollbackDeclared=true` is an unverifiable claim — callers can
pass it without understanding what rollback actually requires per action type.

---

## Agent Roles

Implementer writes connector spec (S1–S5). Reviewer checks: all 15
`ToolActionSideEffect` values individually row-covered in S2; no aggregate
rows; `runtimeExecutionAuthorized=false` explicit; no W3 runtime modification
claimed. Auditor confirms CVF 25.05 Gap 8 cited and advisory-only posture
preserved. No self-review.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `governance/contracts/tool-action-taxonomy.ts` — confirm all 15
   `ToolActionSideEffect` values at line 16; confirm `rollbackDeclared` at
   line 93, `rollbackRequired` at line 118, `rollback_plan` at line 79
4. `.private_reference/legacy/CVF 25.05/CLAUDE_REVIEW_OF_GOP_Y_2026-05-25.md`
   — confirm Gap 8 section: per-action rollback detail not specified
5. `docs/roadmaps/CVF_PRODUCT_DEPTH_ROADMAP_2026-05-29.md`
   — confirm Gap 8 row: PARTIALLY_CLOSED

## Scope

**Allowed (Phase A — documentation connector only):**

- `docs/reference/CVF_GAP8_ACTION_TAXONOMY_ROLLBACK_DETAIL_SPEC_2026-05-29.md`
  (new — connector spec, 5 sections S1–S5)
- `docs/reviews/CVF_GAP8_ACTION_TAXONOMY_ROLLBACK_DETAIL_FAST_LANE_AUDIT_2026-05-29.md`
  (new)
- `docs/reviews/CVF_GAP8_ACTION_TAXONOMY_ROLLBACK_DETAIL_COMPLETION_2026-05-29.md`
  (new)
- this work order (status update only)
- session continuity files

**Forbidden (Phase A):** `governance/contracts/tool-action-taxonomy.ts`
runtime changes, new `ToolActionSideEffect` values, new `rollback_plan`
enforcement beyond the existing boolean gate, any `.ts`/`.tsx`/`.js`/`.py`
file, receipt envelope schema, public-sync repo.

**Phase B (separate work order, DEMAND_GATED):** Wire rollback detail records
into `evaluateToolAction()` as a per-category advisory output. Requires a
fresh GC-018 and explicit operator authorization.

---

## Pre-Dispatch Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface | Disposition |
| --- | --- | --- | --- | --- | --- |
| `ToolActionSideEffect` type | `governance/contracts/tool-action-taxonomy.ts` | line 16 | `ToolActionSideEffect` | W3 contract | ACCEPT |
| `rollbackDeclared` field | `governance/contracts/tool-action-taxonomy.ts` | line 93 | `rollbackDeclared` | `ToolActionRequest` | ACCEPT |
| `rollbackRequired` field | `governance/contracts/tool-action-taxonomy.ts` | line 118 | `rollbackRequired` | `ToolActionEvaluation` | ACCEPT |
| `rollback_plan` evidence type | `governance/contracts/tool-action-taxonomy.ts` | line 79 | `rollback_plan` | `ToolActionApprovalEvidence` | ACCEPT |
| `TOOL_ACTION_TAXONOMY_VERSION` | `governance/contracts/tool-action-taxonomy.ts` | line 6 | `TOOL_ACTION_TAXONOMY_VERSION` | W3 contract | ACCEPT |

New doc-only fields:

| New doc-only field | Purpose | Runtime claim blocked? |
| --- | --- | --- |
| `rollbackDetailAdvisoryType` | Names the per-action rollback detail advisory | Yes |
| `minimumRollbackEvidence` | Lists required rollback evidence per side-effect | Yes |
| `rollbackSteps` | Ordered rollback steps per side-effect category | Yes |
| `rollbackEscalationPath` | Escalation if rollback cannot be performed | Yes |
| `rollbackTimeBoundAdvisory` | How long rollback evidence must be retained | Yes |

---

## Deliverable — Connector Spec

File: `docs/reference/CVF_GAP8_ACTION_TAXONOMY_ROLLBACK_DETAIL_SPEC_2026-05-29.md`

S2 design: map `ToolActionSideEffect` → `rollbackDetailAdvisoryType` +
`minimumRollbackEvidence` + `rollbackSteps` + `rollbackEscalationPath`:

| `sideEffect` | `rollbackDetailAdvisoryType` | `minimumRollbackEvidence` | `rollbackEscalationPath` |
| --- | --- | --- | --- |
| `read_only` | `rollback_not_required` | None | N/A |
| `local_write` | `rollback_via_file_restore` | Pre-write snapshot path or git-trackable diff | Restore from snapshot; if missing, escalate to Reviewer |
| `workspace_mutation` | `rollback_via_workspace_restore` | Workspace state snapshot or git stash reference | Restore snapshot; if unrestorable, escalate to Orchestrator |
| `external_mutation` | `rollback_via_external_undo` | External system undo endpoint or manual reversal evidence | Contact external system owner; escalate to Orchestrator if unavailable |
| `install` | `rollback_via_uninstall` | Package name + version + uninstall command | Run uninstall; if broken state, escalate to Orchestrator |
| `network_egress` | `rollback_not_possible_advisory` | Sent-data log; no recall possible | Mark as IRREVERSIBLE; require explicit human acknowledgment before dispatch |
| `database_read` | `rollback_not_required` | None | N/A |
| `database_write` | `rollback_via_transaction_or_backup` | Transaction ID or pre-write backup reference | Rollback transaction; if committed, restore from backup; escalate if backup missing |
| `database_export` | `rollback_via_export_deletion` | Export file path + deletion confirmation | Delete exported file; if distributed, escalate to Orchestrator |
| `database_schema_mutation` | `rollback_via_migration_down` | Down-migration script reference | Run down-migration; if irreversible, escalate to Orchestrator |
| `database_recovery` | `rollback_advisory_only` | Recovery operation log | Recovery ops generally idempotent; log and escalate if unexpected state |
| `database_admin` | `rollback_via_admin_reversal` | Admin operation log + reversal command | Run reversal; if cannot revert, escalate to human DBA |
| `destructive` | `rollback_not_possible_advisory` | Pre-destruction backup reference required | IRREVERSIBLE without backup; require explicit human authorization before dispatch |
| `privileged` | `rollback_via_privilege_revocation` | Privilege grant log + revocation command | Revoke privilege; escalate to security team if revocation fails |
| `unknown` | `rollback_detail_unavailable` | Manual review required | Block until side-effect is reclassified; escalate to Reviewer |

Key invariant: "This spec defines advisory rollback detail for Orchestrators.
It does not modify `evaluateToolAction()` runtime behavior. Phase B wiring is
DEMAND_GATED. `runtimeExecutionAuthorized=false`."

---

## Roadmap-To-Work-Order Trace Matrix

| Requirement | Section | Output artifact | Verification | Status |
| --- | --- | --- | --- | --- |
| Per-action rollback detail per `ToolActionSideEffect` | S2 | Mapping table covering all 15 values | Reviewer confirms no aggregate rows | CLOSED |
| Source W3 symbols verbatim | S5 | Source Verification rows | Symbol matches line numbers | CLOSED |
| `runtimeExecutionAuthorized=false` explicit | S1, S3 | Invariant statement | grep check | CLOSED |
| CVF 25.05 Gap 8 cited | S1 | Explicit in Purpose | Auditor checks | CLOSED |
| No `.ts` file in diff | Scope | — | Gate check | CLOSED |

---

## Pre-Flight

- [x] Operator authorization received
- [x] Fresh GC-018 waived — operator authorized directly 2026-05-29
- [x] Working tree clean
- [x] All 15 `ToolActionSideEffect` values confirmed from `governance/contracts/tool-action-taxonomy.ts` line 16

## Write Ownership

Implementer owns all new files. No file outside Allowed list may be modified.
`governance/contracts/tool-action-taxonomy.ts` is read-only reference for this
Phase A work order.

## Execution Plan

1. Receive operator authorization and fresh GC-018.
2. Confirm all 15 `ToolActionSideEffect` values from source line 16.
3. Draft connector spec (S1–S5); verify < 250 lines.
4. Run Fast Lane audit.
5. Run governance gates with captured `baseHead`.
6. Update session continuity; update PD roadmap Gap 8 row.
7. Commit.
8. Write completion review.

## Evidence Requirements

- Spec < 250 lines
- All 15 `ToolActionSideEffect` values individually row-covered in S2
- W3 source symbols individually row-verified in S5
- `runtimeExecutionAuthorized=false` explicit
- CVF 25.05 Gap 8 cited
- No code file in diff
- Operator authorization + GC-018 present before dispatch

## Review Gate

All 15 `ToolActionSideEffect` values individually covered; W3 source symbols
verified; `runtimeExecutionAuthorized=false`; no runtime W3 change; spec < 250
lines; no code file; operator authorization + GC-018 present.

## Return-To-Orchestrator Conditions

Stop if: operator authorization missing; cannot confirm all 15 `ToolActionSideEffect`
values from source; connector requires W3 runtime modification; spec > 250 lines
before S4.

## Operator Checkpoint

Operator authorization received 2026-05-29. GC-018 waived — operator authorized directly.

---

## Acceptance Criteria

- [x] Spec with all 5 sections; < 250 lines (121 lines)
- [x] All 15 `ToolActionSideEffect` values individually row-covered in S2
- [x] `runtimeExecutionAuthorized=false` explicit; no W3 runtime change claimed
- [x] CVF 25.05 Gap 8 cited in S1
- [x] W3 source symbols (`rollbackDeclared`, `rollbackRequired`, `rollback_plan`)
  individually row-verified in S5
- [x] No `.ts`/`.tsx`/`.js`/`.py` file in diff
- [x] Operator authorization received 2026-05-29

Fail conditions:
- Runtime enforcement of rollback detail added without Phase B authorization
- `ToolActionSideEffect` values aggregated in S2
- No operator authorization before dispatch

---

## Closure Checklist

- [x] Operator authorization received 2026-05-29
- [x] Fresh GC-018 waived — operator authorized directly
- [x] Spec with all 5 sections
- [x] S2 covers all 15 `ToolActionSideEffect` values individually
- [x] `runtimeExecutionAuthorized=false` explicit
- [x] S5 complete; no aggregate rows
- [x] No code file in diff
- [x] Fast Lane audit created
- [x] Session continuity updated
- [x] PD roadmap Gap 8 row updated to CLOSED_PASS on Phase A closure

---

## Sequencing

Phase A (this work order): documentation connector spec only. No runtime change.
Phase B (separate, DEMAND_GATED): wire rollback detail into `evaluateToolAction()`
as per-category advisory output. Requires fresh GC-018 + operator authorization.

## Claim Boundary

This work order is a planning record. It does not authorize implementation,
modify W3 runtime behavior, change the `rollbackDeclared` gate logic, or
claim any rollback capability is currently enforced beyond the existing boolean
gate. Gap 8 Phase A closure claim: documentation connector spec only.
