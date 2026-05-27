# CVF Work Order — LHW4-T3 Noncoder Friction Advisory Packet Connector

Memory class: FULL_RECORD

Status: READY_FOR_DISPATCH

docType: work_order

Date: 2026-05-27

---

## Purpose

Implement LHW4-T3: a connector spec turning LHW3-T1 trend signals and CB1
advisory readout into a plain-language friction advisory packet for non-coders.
Closes the gap where LHW3-T1 maps failure trends and CB1 identifies missing
signals, but no connector defines the advisory packet that tells a non-coder
what is wrong and what to try next — without exposing technical field names.

Documentation-only tranche. No source code, runtime module, route, or provider
behavior is changed. The advisory packet does not block workflow execution.

## Authority Chain

- LHW4 roadmap: `docs/roadmaps/CVF_LHW4_WORKFLOW_CONNECTOR_WAVE4_ROADMAP_2026-05-27.md`
- Fast Lane audit: `docs/reviews/CVF_LHW4_T3_FAST_LANE_AUDIT_2026-05-27.md` → FAST_LANE_READY
- LH1 ledger (`AI-first vs Human-first` trigger): `docs/reference/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
- LHW3-T1 spec: `docs/reference/CVF_LHW3_OPERATIONAL_FAILURE_TREND_READOUT_CONNECTOR_SPEC_2026-05-27.md`
- CB1: `docs/reviews/CVF_CB1_CONTEXT_BUDGET_REQUEST_SHAPING_READOUT_COMPLETION_2026-05-25.md`
- C8: `docs/reviews/CVF_C8_PRODUCT_SKILL_PACK_SELECTION_READOUT_COMPLETION_2026-05-25.md`
- LHW3-T2 spec: `docs/reference/CVF_LHW3_REQUEST_CLARIFICATION_RE_INTAKE_LOOP_CONNECTOR_SPEC_2026-05-27.md`

## Gate Conditions — CHECK FIRST

```text
Gate 1 — T1 status: CLOSED_PASS
Gate 2 — T2 status: CLOSED_PASS
```

Read `docs/reviews/CVF_LHW4_T1_*_COMPLETION_2026-05-27.md` and
`docs/reviews/CVF_LHW4_T2_*_COMPLETION_2026-05-27.md`.

If either gate is not CLOSED_PASS, stop and report to Orchestrator.

## Agent Roles

Implementer writes spec (S1–S5) using LHW3-T1 signal labels and CB1 field
names verbatim. Reviewer checks signal labels verbatim, CB1 `recommendedNextAction`
vocabulary verbatim, plain-language advisory text non-technical, advisory-only
(no blocking) explicit, S5 Source Verification complete. Auditor confirms both
gates documented, `AI-first vs Human-first` LH1 trigger recorded, no workflow
blocking claimed. No self-review.

## Scope

**Allowed:**

- `docs/reference/CVF_LHW4_NONCODER_FRICTION_ADVISORY_PACKET_CONNECTOR_SPEC_2026-05-27.md`
  (new — primary deliverable)
- this work order (status update only)
- LHW4 roadmap (status update to `CLOSED_PASS_BOUNDED` after T3 closes)
- session continuity files

**Forbidden:** `EXTENSIONS/` (any file), `governance/contracts/` (any file),
any `.ts`/`.tsx`/`.js`/`.py` file, receipt envelope schema, public-sync repo.
Live friction scoring, UX enforcement, and workflow blocking remain blocked.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. T1 and T2 completions (understand the chain both tranches establish)
4. `docs/reference/CVF_LHW3_OPERATIONAL_FAILURE_TREND_READOUT_CONNECTOR_SPEC_2026-05-27.md`
   — confirm LHW3-T1 trend signal labels: `overconstraint signal`,
   `provider instability signal`, `underspecification signal`,
   `degraded-output or drift signal`, `audit gap signal`; confirm S3
   advisory-only constraint
5. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-request-context-readout.ts`
   and `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/product-outcome.runtime.ts`
   — confirm `recommendedNextAction`, `readiness`, `missingSignals`,
   `contaminationFlags`, and `noiseFlags` field names and values
6. `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/product-outcome.runtime.ts`
   — confirm `no_certified_pack_match` token
7. `docs/reference/CVF_LHW3_REQUEST_CLARIFICATION_RE_INTAKE_LOOP_CONNECTOR_SPEC_2026-05-27.md`
   — confirm S2 clarification packet type tokens used in the re-intake loop;
   the T3 advisory packet must point to the T2 loop as the next action path
8. `docs/roadmaps/CVF_LHW4_WORKFLOW_CONNECTOR_WAVE4_ROADMAP_2026-05-27.md`
   — confirm T3 deliverable shape

If any required file is missing, stop and report to Orchestrator.

## Pre-Dispatch Source Verification Block

Every existing signal label, runtime field, selection status, and clarification
packet token must be verified before implementation. Completion reviews may
support closure status only.

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| LHW3-T1 trend signal labels | `docs/reference/CVF_LHW3_OPERATIONAL_FAILURE_TREND_READOUT_CONNECTOR_SPEC_2026-05-27.md` | lines 46-52 | `overconstraint signal`, `provider instability signal`, `underspecification signal`, `degraded-output or drift signal`, `audit gap signal` | LHW3-T1 trend mapping | ACCEPT |
| VI2 route context fields | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-request-context-readout.ts` | lines 7-35, 193-198 | `readiness`, `missingSignals`, `noiseFlags`, `contaminationFlags`, `recommendedNextAction` | `RouteRequestContextReadout` | ACCEPT |
| C8 request context fields | `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/product-outcome.runtime.ts` | lines 45-52, 79-93, 330-343 | `readiness`, `missingSignals`, `contaminationFlags`, `noiseFlags`, `recommendedNextAction` | `ProductSkillPackRequestContextReadout` | ACCEPT |
| C8 no-match token | `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/product-outcome.runtime.ts` | lines 45, 270, 274 | `no_certified_pack_match` | `ProductSkillPackSelectionStatus` / selection reason | ACCEPT |
| LHW3-T2 clarification packet types | `docs/reference/CVF_LHW3_REQUEST_CLARIFICATION_RE_INTAKE_LOOP_CONNECTOR_SPEC_2026-05-27.md` | lines 47-50 | `missing_context_clarification_packet`, `noisy_context_clarification_packet`, `ambiguous_outcome_clarification_packet`, `unmatched_request_clarification_packet` | LHW3-T2 re-intake loop | ACCEPT |

New doc-only fields proposed by this work order: `advisoryId`,
`advisoryType`, `signalSource`, `plainLanguageMessage`,
`suggestedNextStep`, `nextStepLoopRef`, and `advisoryBlocking`.
These must be labeled documentation-only in the connector spec.

## Deliverable — Connector Spec

File: `docs/reference/CVF_LHW4_NONCODER_FRICTION_ADVISORY_PACKET_CONNECTOR_SPEC_2026-05-27.md`

Required sections:

### S1 — Purpose and claim boundary

- State what the connector is: a normative doc mapping LHW3-T1 trend signals
  and CB1 advisory readout into a plain-language friction advisory packet for
  non-coders — a human-readable record of what friction was detected and what
  to try next.
- State what it is not: not a LHW3-T1/CB1 runtime extension; not a live
  friction scoring engine; not a workflow blocker.
- Explicit statement: "This connector does not block workflow execution. The
  advisory packet is a non-blocking governance record. An operator or agent
  may read it to improve their next request, but ignoring it does not prevent
  a workflow from running."

### S2 — Trend signal + CB1 signal to advisory packet type mapping

Table columns: `LHW3-T1 trend signal` | `CB1 field / value` |
`Advisory packet type` | `Plain-language message template` | `Suggested next step`

Minimum rows:

- `overconstraint signal` + `policyViolationRate` high → **Overconstraint Advisory**
  → "CVF declined this action because it doesn't match the current safety
  rules." → "Try a lower-risk request or contact your administrator to adjust
  the policy."
- `underspecification signal` + `missingSignals` non-empty → **Missing Context Advisory**
  → "Your request is missing some information CVF needs to match a workflow."
  → "Add the missing details and try again." (reference LHW3-T2 re-intake loop)
- `provider instability signal` + `retryCount` high → **Provider Instability Advisory**
  → "CVF had trouble reaching the AI provider." → "Wait a moment and try again,
  or ask your administrator about provider status."
- `degraded-output or drift signal` + `humanCorrectionCount` high → **Output Drift Advisory**
  → "The AI output needed human corrections recently." → "Review the output
  carefully and provide more specific instructions next time."
- `no_certified_pack_match` (C8 outcome) → **No Match Advisory**
  → "CVF could not find a workflow that matches your request." → "Try rephrasing
  your goal or use the clarification option." (reference LHW3-T2 re-intake loop)

All signal labels must be used verbatim from LHW3-T1 and CB1/C8 fields must be
source-verified. Plain-language
message templates are documentation examples — implementers may adjust wording
but must preserve the signal source and next-step link.

### S3 — Advisory packet minimum fields

Prose + field list (max 10 lines):

Every friction advisory packet must contain:

- `advisoryId`: unique token
- `advisoryType`: one of `overconstraint` | `missing_context` | `instability` |
  `output_drift` | `no_match`
- `signalSource`: the LHW3-T1 trend signal label or C8 outcome that triggered
  the advisory
- `plainLanguageMessage`: non-technical human-readable message
- `suggestedNextStep`: one-sentence action for the operator or non-coder
- `nextStepLoopRef`: optional reference to LHW3-T2 clarification packet type
  when applicable
- `advisoryBlocking`: always `false`

State explicitly: "These fields are documentation-only minimum requirements.
`advisoryBlocking=false` is invariant. The advisory packet does not extend
`GovernanceEvidenceReceipt` or any existing receipt envelope."

### S4 — Runtime-enforcement boundary table

| Behavior | Current status | Future path |
| --- | --- | --- |
| LHW3-T1 trend signal computation | Document-only (LHW3-T1) | Future: trend aggregator |
| CB1 missing-signal readout | Runtime (Governance CLI) | Stable |
| C8 pack selection no-match | Runtime (Governance CLI) | Stable |
| Signal-to-advisory-type mapping | Document-only | Future: friction advisory engine |
| Plain-language message rendering | Document-only | Future: operator-facing UI |
| Advisory packet dispatch | Document-only | Future: notification surface |

Do not label any row "Runtime" unless a closed PASS tranche implements it.

After T3 is CLOSED_PASS: update LHW4 roadmap Status to `CLOSED_PASS_BOUNDED`.

### S5 — Source Verification Table (mandatory)

Required columns: `Claimed item` | `Source file` | `Verified line/section` |
`Verified path or symbol` | `Owning interface/function/schema` | `Disposition`

Cover every LHW3-T1 signal label, CB1/C8 field name, and C8 vocabulary item cited
in S2 and S3. Valid dispositions are `ACCEPT`, `REJECT`, and
`BLOCKED_SOURCE_NOT_FOUND`. No blocked, guessed, or confirm-later item may
remain in S2.

## Pre-Flight

- [ ] T1 CLOSED_PASS confirmed
- [ ] T2 CLOSED_PASS confirmed
- [ ] Working tree clean
- [ ] All required first reads done
- [ ] LHW3-T1 trend signal labels confirmed from LHW3-T1 spec
- [ ] CB1/C8 `recommendedNextAction` vocabulary confirmed from source files

## Write Ownership

Implementer owns all new files. No file outside the Allowed list may be
modified.

## Execution Plan

1. Confirm T1 + T2 gates.
2. Read all required first reads.
3. Draft spec (S1–S5) with Source Verification Table.
4. Confirm no code file staged.
5. Reviewer perspective — record result.
6. Update LHW4 roadmap → `CLOSED_PASS_BOUNDED`.
7. Update session continuity (`lhw4_t3_complete`).
8. Commit: `docs(lhw4-t3): add noncoder friction advisory packet connector spec`.
9. Write completion review.

Spec size guard: < 200 lines. Trim S3 prose if approaching 180 lines.

## Evidence Requirements

- Spec at target path with all 5 sections present
- Both gates (T1 + T2) documented as CLOSED_PASS
- S2 maps minimum 5 signal combinations to advisory packet types
- `advisoryBlocking=false` explicit in S1 and S3
- S4 boundary table present; no doc-only row labeled Runtime
- S5 Source Verification Table complete; no `BLOCKED_SOURCE_NOT_FOUND` rows
- LHW4 roadmap updated to `CLOSED_PASS_BOUNDED`
- No `.ts`/`.tsx`/`.js`/`.py` file in `git diff --name-only`
- Session continuity updated to `lhw4_t3_complete`
- Completion review written

## Acceptance Criteria

- [ ] Spec with all 5 sections created
- [ ] S2 covers minimum 5 signal-to-advisory-type combinations
- [ ] `advisoryBlocking=false` invariant explicit in S1 and S3
- [ ] S5 Source Verification Table complete; no `BLOCKED_SOURCE_NOT_FOUND` rows
- [ ] S4 boundary table honest; no doc-only row labeled Runtime
- [ ] LHW4 roadmap updated to `CLOSED_PASS_BOUNDED`
- [ ] No code file in diff
- [ ] Session continuity updated

## Review Gate

Before committing: Reviewer perspective completed; all LHW3-T1 signal tokens
and CB1 field names verbatim; `advisoryBlocking=false` explicit; S5 complete;
no code file in diff; LHW4 roadmap updated.

## Closure Checklist

- [ ] T1 gate confirmed documented
- [ ] T2 gate confirmed documented
- [ ] Spec created with all 5 sections
- [ ] S2 advisory mapping uses LHW3-T1 + CB1 vocabulary verbatim
- [ ] `advisoryBlocking=false` explicit
- [ ] S5 Source Verification Table complete; no `BLOCKED_SOURCE_NOT_FOUND` rows
- [ ] S4 boundary table honest; no doc-only row labeled Runtime
- [ ] LHW4 roadmap updated to `CLOSED_PASS_BOUNDED`
- [ ] No code file in diff
- [ ] Session continuity updated
- [ ] Completion review written

## Return-To-Orchestrator Conditions

Stop and report to Orchestrator if:

- T1 or T2 gate is not CLOSED_PASS;
- any required first read file is missing;
- a LHW3-T1 signal token or CB1 field name cannot be confirmed from source;
- writing the connector requires adding a new trend signal not in LHW3-T1;
- the advisory packet requires blocking workflow execution;
- spec exceeds 200 lines before S4 is complete.

## Operator Checkpoint

operator.checkpoint.waiver: Low-risk documentation-only tranche gated by T1 +
T2 CLOSED_PASS and source-verified LHW3-T1/CB1/C8 vocabulary; no operator
checkpoint required unless a workflow-blocking requirement or new signal token
is discovered during implementation.

## Claim Boundary

LHW4-T3 produces a documentation artifact. It does not claim LHW3-T1/CB1 runtime
extension, live friction scoring, UX enforcement, workflow blocking, receipt
envelope extension, provider behavior, hosted readiness, production readiness,
or public release readiness.
