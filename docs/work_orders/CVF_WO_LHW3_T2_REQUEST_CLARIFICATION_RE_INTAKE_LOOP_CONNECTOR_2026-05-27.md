# CVF Work Order — LHW3-T2 Request Clarification Re-Intake Loop Connector

Memory class: FULL_RECORD

Status: READY_FOR_DISPATCH

docType: work_order

Date: 2026-05-27

---

## Purpose

Implement LHW3-T2: a connector spec mapping each CB1 missing-signal class or
contamination flag into a standard clarification request packet that routes back
through the C8 intake loop. Closes the gap where CB1 identifies what is wrong
with a request and VI2 surfaces missing-signal detail, but no standard packet
defines how the clarification request is formed and re-enters intake.

Documentation-only tranche. No source code, runtime module, route, or provider
behavior is changed.

## Authority Chain

- LHW3 roadmap: `docs/roadmaps/CVF_LHW3_WORKFLOW_CONNECTOR_WAVE3_ROADMAP_2026-05-27.md`
- Fast Lane audit: `docs/reviews/CVF_LHW3_T2_FAST_LANE_AUDIT_2026-05-27.md` → FAST_LANE_READY
- LH1 ledger (`Human System Harness` trigger): `docs/reference/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
- CB1: `docs/reviews/CVF_CB1_CONTEXT_BUDGET_REQUEST_SHAPING_READOUT_COMPLETION_2026-05-25.md`
- VI2: `docs/reviews/CVF_VI2_ROUTE_REQUEST_CONTEXT_PROFILE_READOUT_COMPLETION_2026-05-25.md`
- C8: `docs/reviews/CVF_C8_PRODUCT_SKILL_PACK_SELECTION_READOUT_COMPLETION_2026-05-25.md`
- LHW3-T1 spec: `docs/reference/CVF_LHW3_OPERATIONAL_FAILURE_TREND_READOUT_CONNECTOR_SPEC_2026-05-27.md`

## Gate Condition — CHECK FIRST

Confirm T1 is `CLOSED_PASS` by reading:
`docs/reviews/CVF_LHW3_T1_*_COMPLETION_2026-05-27.md`

If T1 is not CLOSED_PASS, stop and report to Orchestrator.

## Agent Roles

Implementer writes spec (S1–S5) opening with the T1 foundation. Reviewer checks
CB1 signal class names verbatim, VI2 field names verbatim, C8 pack selection
vocabulary, boundary table honest, no runtime claim added, no `.ts` file touched,
S5 Source Verification complete. Auditor confirms T1 gate documented, Human
System Harness LH1 trigger recorded, no live routing or intake executor claimed.
No self-review.

## Scope

**Allowed:**

- `docs/reference/CVF_LHW3_REQUEST_CLARIFICATION_RE_INTAKE_LOOP_CONNECTOR_SPEC_2026-05-27.md`
  (new — primary deliverable)
- this work order (status update only)
- session continuity files

**Forbidden:** `EXTENSIONS/` (any file), `governance/contracts/` (any file),
any `.ts`/`.tsx`/`.js`/`.py` file, receipt envelope schema, public-sync repo.
Live clarification routing engine, intake executor, and automated loop re-entry
remain blocked.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. T1 completion (understand the trend-signal pattern T2 must complement)
4. `docs/reviews/CVF_CB1_CONTEXT_BUDGET_REQUEST_SHAPING_READOUT_COMPLETION_2026-05-25.md`
   — confirm CB1 signal classes: `budget_tier` values, `readiness` states,
   `missingSignals` array, `contaminationFlags`, `noiseFlags`,
   `nextAction` vocabulary
5. `docs/reviews/CVF_VI2_ROUTE_REQUEST_CONTEXT_PROFILE_READOUT_COMPLETION_2026-05-25.md`
   — confirm `requestContextReadout.missingSignals` field name and
   `requestContextReadout.readiness` field name
6. `docs/reviews/CVF_C8_PRODUCT_SKILL_PACK_SELECTION_READOUT_COMPLETION_2026-05-25.md`
   — confirm pack selection states: `no_certified_pack_match`, selected pack
   `packId` vocabulary
7. `docs/reference/CVF_LHW3_WORKFLOW_CONNECTOR_WAVE3_ROADMAP_2026-05-27.md`
   — confirm T2 deliverable shape

If any required file is missing, stop and report to Orchestrator.

## Deliverable — Connector Spec

File: `docs/reference/CVF_LHW3_REQUEST_CLARIFICATION_RE_INTAKE_LOOP_CONNECTOR_SPEC_2026-05-27.md`

Required sections:

### S1 — Purpose and claim boundary

- State what the connector is: a normative doc mapping CB1 missing-signal and
  contamination-flag outputs to standard clarification request packet types,
  with a loop re-entry standard for returning to C8 pack selection.
- State what it is not: not a CB1/VI2 runtime extension; not a live intake
  executor; not an automated routing engine.
- Explicit statement: "CB1 `cvf.productSkillPackRequestContext.v1` is the
  runtime authority for signal readout; VI2 `cvf.routeRequestContextProfile.vi2.v1`
  is the runtime authority for route-level missing-signal exposure. This
  connector extends those outputs to a standard clarification packet shape
  usable by Orchestrator and operators."

### S2 — CB1 signal class to clarification packet type mapping

Table columns: `CB1 signal class` | `CB1 field / value` | `Clarification packet type` |
`Minimum fields` | `Loop re-entry point`

Minimum rows:

- `missingSignals` non-empty → missing-context clarification packet
  → fields: actor, original packId, missingSignals list, returnPath=C8
- `contaminationFlags` non-empty → noisy-context clarification packet
  → fields: actor, original packId, contaminationFlags list, returnPath=C8
- `readiness=not_ready` (no missingSignals, no flags) → ambiguous-outcome
  clarification packet → fields: actor, original packId, goalStatement,
  returnPath=C8
- `no_certified_pack_match` (C8 outcome) → unmatched-request clarification
  packet → fields: actor, request summary, returnPath=C8 re-select

Use CB1 and VI2 field names verbatim. If a field name cannot be verified from
the CB1 or VI2 completion reviews, mark it `BLOCKED_SOURCE_NOT_FOUND`, stop,
and return to Orchestrator.

### S3 — Loop re-entry standard

Prose description (max 10 lines):

- How the clarification response closes the loop and returns to C8 intake:
  operator or agent receives the clarification packet, supplies the missing
  information, and re-submits to the C8 `cvf skill select` surface.
- What the receiving agent must confirm before re-entering: `missingSignals`
  resolved, `contaminationFlags` resolved, `no_certified_pack_match` re-tried
  with updated request.
- State explicitly: "The loop re-entry is manual or operator-triggered. This
  connector does not claim an automated clarification routing runtime."

### S4 — Runtime-enforcement boundary table

| Behavior | Current status | Future path |
| --- | --- | --- |
| CB1 missing-signal readout | Runtime (Governance CLI) | Stable |
| VI2 route-level missingSignals exposure | Runtime (cvf-web route) | Stable |
| C8 pack selection readout | Runtime (Governance CLI) | Stable |
| Signal-to-packet type mapping | Document-only | Future: clarification packet validator |
| Loop re-entry routing | Document-only | Future: intake loop executor |
| Automated clarification dispatch | Document-only | Future: operator notification surface |

Do not label any row "Runtime" unless a closed PASS tranche implements it.

### S5 — Source Verification Table (mandatory)

Required columns: `Claimed item` | `Source file` | `Verified path or symbol` |
`Owning interface/function/schema` | `Disposition`

Cover every CB1 field, VI2 field, and C8 vocabulary item cited in S2. Valid
dispositions are `ACCEPT`, `REJECT`, and `BLOCKED_SOURCE_NOT_FOUND`. If any
item cannot be source-verified, mark it `BLOCKED_SOURCE_NOT_FOUND`, stop, and
return to Orchestrator. No blocked, guessed, or confirm-later item may remain
in S2.

## Pre-Flight

- [ ] T1 CLOSED_PASS confirmed
- [ ] Working tree clean
- [ ] All required first reads done
- [ ] CB1 signal class / field names confirmed from CB1 completion review
- [ ] VI2 missingSignals field name confirmed from VI2 completion review

## Write Ownership

Implementer owns all new files. No file outside the Allowed list may be
modified.

## Execution Plan

1. Confirm T1 gate.
2. Read all required first reads.
3. Draft spec (S1–S5) with Source Verification Table.
4. Confirm no code file staged.
5. Reviewer perspective — record result.
6. Update session continuity (`lhw3_t2_complete`).
7. Commit: `docs(lhw3-t2): add request clarification re-intake loop connector spec`.
8. Write completion review; include T3 gate answer (see below).

Spec size guard: < 200 lines. Trim S3 prose if approaching 180 lines.

## Evidence Requirements

- Spec at target path with all 5 sections present
- S2 uses CB1 and VI2 vocabulary verbatim (no invented names)
- S3 explicitly states loop re-entry is manual/operator-triggered
- S4 boundary table present; no doc-only row labeled Runtime
- S5 Source Verification Table complete; no `BLOCKED_SOURCE_NOT_FOUND` rows
- No `.ts`/`.tsx`/`.js`/`.py` file in `git diff --name-only`
- Session continuity updated to `lhw3_t2_complete`
- Completion review written with T3 gate answer

## Acceptance Criteria

- [ ] Spec with all 5 sections created
- [ ] All 4 CB1 signal class combinations mapped to distinct packet types
- [ ] Loop re-entry standard explicitly states manual/operator-triggered
- [ ] S4 boundary table honest (no doc-only row labeled Runtime)
- [ ] S5 Source Verification Table complete with no `BLOCKED_SOURCE_NOT_FOUND` rows
- [ ] No code file in diff
- [ ] Session continuity updated

## Review Gate

Before committing: Reviewer perspective completed; all CB1 and VI2 field names
verbatim; S4 boundary table honest; S5 complete with no `BLOCKED_SOURCE_NOT_FOUND`
rows; no code file in diff.

## Closure Checklist

- [ ] T1 gate confirmed documented
- [ ] Spec created with all 5 sections
- [ ] S2 mapping table uses CB1 + VI2 vocabulary verbatim
- [ ] S3 manual/operator-triggered statement explicit
- [ ] S5 Source Verification Table complete; no `BLOCKED_SOURCE_NOT_FOUND` rows
- [ ] No code file in diff
- [ ] Session continuity updated
- [ ] Completion review with T3 gate answer written

## Return-To-Orchestrator Conditions

Stop and report to Orchestrator if:

- T1 gate is not CLOSED_PASS;
- any required first read file is missing or unreadable;
- a CB1 or VI2 field name cannot be confirmed from completion reviews;
- writing the connector requires adding a new CB1 signal class not in the
  existing vocabulary;
- spec exceeds 200 lines before S4 is complete.

## T3 Gate Output (required in completion review)

Answer explicitly: "Was a concrete spec-change workflow gap identified during
T2 work?"

- YES → describe gap in one sentence; T3 proceeds.
- NO → "No gap found. T3 proceeds per roadmap rationale."
  (T3 proceeds regardless — this output is informational.)

## Operator Checkpoint

operator.checkpoint.waiver: Low-risk documentation-only tranche gated by T1
CLOSED_PASS and source-verified CB1/VI2 field names; no operator checkpoint
required unless a conflict with CB1/VI2 vocabulary is discovered during
implementation.

## Claim Boundary

LHW3-T2 produces a documentation artifact. It does not claim CB1/VI2 runtime
extension, live clarification routing, automated intake re-entry, receipt
envelope extension, provider behavior, hosted readiness, production readiness,
or public release readiness.
