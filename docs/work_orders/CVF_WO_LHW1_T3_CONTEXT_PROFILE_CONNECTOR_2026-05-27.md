# CVF Work Order — LHW1-T3 Context Profile Connector

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-05-27

---

## Purpose

Implement LHW1-T3: a connector between non-coder context capture,
route/profile readouts, and the workflow packet — with clear compaction
and relevance rules drawn from the caveman/GoClaw legacy sources.

This work order authorizes a documentation-only tranche. No source code,
runtime module, route, or provider behavior is changed.

## Authority Chain

- Operator authorized LHW1 roadmap on 2026-05-27.
- Roadmap:
  `docs/roadmaps/CVF_LHW1_LEGACY_WORKFLOW_CONNECTOR_ABSORPTION_ROADMAP_2026-05-27.md`
- Fast Lane audit:
  `docs/reviews/CVF_LHW1_T3_FAST_LANE_AUDIT_2026-05-27.md`
  → Decision: FAST_LANE_READY (pre-conditions: T1 CLOSED_PASS, T2
  CLOSED_PASS, concrete context gap identified)
- T1 work order:
  `docs/work_orders/CVF_WO_LHW1_T1_PRODUCT_SKILL_PACK_WORKFLOW_CONNECTOR_2026-05-27.md`
- T2 work order:
  `docs/work_orders/CVF_WO_LHW1_T2_WORKFLOW_CHAIN_STATE_CONNECTOR_2026-05-27.md`
- VI2 authority:
  `docs/reviews/CVF_VI2_ROUTE_REQUEST_CONTEXT_PROFILE_READOUT_COMPLETION_2026-05-25.md`
- VI3 authority:
  `docs/reviews/CVF_VI3_AGENTMEMORY_CAPTURE_RECORD_READOUT_COMPLETION_2026-05-25.md`
- LH1 ledger (caveman/GoClaw dispositions):
  `docs/reference/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`

## Gate Conditions — MUST CHECK ALL BEFORE STARTING

```
Gate 1 — T1 status: read docs/reviews/CVF_LHW1_T1_*_COMPLETION_2026-05-27.md
         Verdict must be: CLOSED_PASS

Gate 2 — T2 status: read docs/reviews/CVF_LHW1_T2_*_COMPLETION_2026-05-27.md
         Verdict must be: CLOSED_PASS

Gate 3 — Context gap: read T2 completion note section "T3 Gate Output"
         Answer must be: YES with a named gap
```

If any gate fails, stop immediately. Do not implement T3.
If Gate 3 is NO (no context gap found), T3 is deferred — record this in
session continuity and mark the roadmap `CLOSED_PASS_BOUNDED`.

## Required First Reads

After confirming all three gates:

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `docs/reviews/CVF_LHW1_T2_WORKFLOW_CHAIN_STATE_CONNECTOR_COMPLETION_2026-05-27.md`
   — read the named context gap; T3 spec must address it specifically.
4. `docs/reference/CVF_LHW1_WORKFLOW_CHAIN_STATE_CONNECTOR_SPEC_2026-05-27.md`
   — T2 deliverable; T3 connector must be compatible with T2 phase
   vocabulary and role assignment fields.
5. `docs/reviews/CVF_VI2_ROUTE_REQUEST_CONTEXT_PROFILE_READOUT_COMPLETION_2026-05-25.md`
   — understand the `cvf.routeRequestContextProfile.vi2.v1` readout
   field names. T3 must reuse these names; do not invent new ones.
6. `docs/reviews/CVF_VI3_AGENTMEMORY_CAPTURE_RECORD_READOUT_COMPLETION_2026-05-25.md`
   — understand the `cvf.agentMemoryCaptureRecord.vi3.v1` fields,
   especially `canReinject=false` and `rawMemoryReleased=false` bindings.
7. `docs/reference/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
   — sections: `caveman` (DEFER_DEMAND_GATED) and `Workflow GoClaw`
   (PARTIALLY_ABSORBED). Read the remaining trigger text for both.
   T3 may absorb the compaction/relevance concepts from these sources
   as advisory guidelines — it does not re-open the demand-gate for
   full runtime caveman implementation.

Do not scope from summaries alone. If any file above is missing, stop.

## Scope / Target / Owner Boundary

### Allowed owner files

- `docs/reference/CVF_LHW1_CONTEXT_PROFILE_CONNECTOR_SPEC_2026-05-27.md`
  (new — primary deliverable)
- this work order (status update only)
- session continuity files

### Forbidden

- `EXTENSIONS/` — any file
- `governance/contracts/` — any file
- `route-request-context-readout.ts` — not modified
- `audit-memory-receipt.ts` — not modified
- `route.ts` or any `/api/execute` file — not modified
- any `.ts`, `.tsx`, `.js`, `.py` file
- caveman full runtime budgeting engine — DEFER_DEMAND_GATED, not opened
- raw memory reinjection of any kind
- provider route behavior changes
- LLM-based context scoring
- public-sync repo
- any hosted or production surface

## Deliverables

### Deliverable 1 — Context profile connector spec

File:
`docs/reference/CVF_LHW1_CONTEXT_PROFILE_CONNECTOR_SPEC_2026-05-27.md`

The spec must contain all of the following sections:

### Section 1 — Purpose, named context gap, and claim boundary

- Open with the specific context gap identified in T2 (quote it from
  the T2 completion note).
- State what the connector does: maps non-coder context capture fields
  to the workflow packet without overbuilding memory or blocking the route.
- State what it does not do: no raw memory reinjection, no provider route
  behavior change, no LLM scoring, no caveman runtime engine.
- State: "`canReinject: false` is preserved from VI3 and M1/M2 boundaries.
  This connector does not relax that constraint."

### Section 2 — Context capture field mapping

A table mapping non-coder input fields to their workflow packet destination.
Columns: `Input field` | `Source surface` | `Workflow packet field` | `Compaction rule`.

Minimum rows to cover:

- User goal / outcome request → intake context → `workflowSpec.phases[intake].inputs`
- Skill pack selected → C8 readout → `packId` in T1 connector record
- Readiness signals (from VI2 `requestContextReadout`) → route readout → intake phase context profile
- Missing signals (from VI2 `missingSectors` if present) → intake → `workflowSpec.phases[intake].successCriteria` gap note
- Session role (from VI3 `captureRecord.sessionRole`) → audit capture → T2 phase-role assignment field

Use VI2 field names verbatim. If a VI2 field name is uncertain,
state "confirm field name against `route-request-context-readout.ts`"
rather than inventing a name.

### Section 3 — Compaction and relevance rules

Guidelines drawn from caveman / Workflow GoClaw legacy sources (LH1
ledger disposition: PARTIALLY_ABSORBED / DEFER_DEMAND_GATED).

Rules are advisory — they guide how a future implementer should filter
context before injecting it into a workflow packet, not how the route
currently works.

Required rules at minimum:

1. **Relevance rule:** Only context fields with a direct mapping to a
   workflow packet field (Section 2 table) are included in the handoff.
   Fields that do not map to any packet field are dropped at intake.
2. **Compaction rule:** If a context field exceeds 500 characters, it
   must be summarized to a single sentence before being placed in the
   workflow packet. The raw value is not passed downstream.
3. **Noise filter rule:** Repeated, contradictory, or out-of-scope
   signals (e.g. references to other projects, unrelated providers, or
   prior session state) are excluded from the current workflow packet.
4. **Missing-signal rule:** If a required context field is absent, the
   intake phase records it as a `successCriteria` gap — the phase does
   not advance to `design_ready` until the gap is resolved or explicitly
   waived by the Orchestrator.
5. **Memory boundary rule:** No field from this connector may be marked
   `canReinject: true`. Context flows forward into the workflow packet;
   it does not flow back into the provider prompt as raw memory.

Note which rules are derived from `caveman` (budget/relevance filtering)
and which from `Workflow GoClaw` (session classification and context
cache) per the LH1 ledger.

### Section 4 — Context-to-workflow handoff mapping

Describe (in prose) how the mapped fields flow from intake through the
T2 state connector phases:

- At `intake_pending`: which context fields must be present before
  the phase can advance.
- At `design_ready`: which fields are passed to the Implementer's input
  package (reference T2 MA1 `## 4. Input Package` field).
- At `build_running`: which context fields remain relevant; which are
  dropped as stale.
- At `review_pending`: which context fields the Reviewer needs to
  evaluate the output (e.g. original user goal for outcome alignment).
- At `freeze_ready`: which context fields are archived in the receipt.

This section is prose description. No cvf-web or route file is modified.

### Section 5 — What remains demand-gated

Explicitly state what was NOT absorbed in T3 (per LH1 ledger triggers):

- `caveman` full runtime context budget engine: remains DEFER_DEMAND_GATED;
  reopen only when request-context budget/readout quality is a concrete
  proven need.
- `Workflow GoClaw` full session classification runtime: remains
  PARTIALLY_ABSORBED; reopen only for context profile packaging after
  selector/memory traffic exists.
- Any LLM-based scoring of context relevance: not in scope.
- Raw memory reinjection: permanently blocked per M1/M2/VI3.

This section closes the LHW1 absorption loop for T3 scope.

### Deliverable 2 — If T3 is deferred (Gate 3 = NO)

If no concrete context gap was identified in T2, do not create the spec.
Instead, do all of the following:

- Update this work order status to `DEFERRED_NO_GAP_FOUND`.
- Update session continuity to reflect `lhw1_t3_deferred`.
- Mark roadmap `CLOSED_PASS_BOUNDED` (T1+T2 completed; T3 deferred).
- Write a one-paragraph note in the active handoff explaining the deferral.

### Deliverable 3 — Session continuity update

If T3 proceeds: update session continuity to `lhw1_t3_complete`.
If T3 deferred: update session continuity to `lhw1_t3_deferred` and
roadmap to `CLOSED_PASS_BOUNDED`.

## Pre-Flight

- [ ] Gate 1: T1 `CLOSED_PASS` confirmed
- [ ] Gate 2: T2 `CLOSED_PASS` confirmed
- [ ] Gate 3: named context gap present in T2 completion note
- [ ] working tree clean; all required first reads done
- [ ] VI2 field names confirmed from VI2 completion review

## Agent Roles

Implementer confirms all 3 gates, writes spec, updates session continuity.
Reviewer checks gap is addressed, VI2/VI3 field names correct, compaction
rules sourced from caveman/GoClaw, `canReinject: false` preserved, no `.ts`
file touched. Auditor confirms gates documented, demand-gated items remain
gated, no new runtime claim, roadmap closed. No self-review.

## Write Ownership

Implementer owns all new files. Reviewer and Auditor hold read + review
rights only. No file outside the Allowed list in the Scope section may be
modified by any role.

## Execution Plan

1. Check gates 1-3. If any fails → Deliverable 2 (deferred path) and stop.
2. Read all required first reads.
3. Draft spec (Sections 1-5) opening with the named context gap from T2.
4. Confirm no code file staged.
5. Reviewer perspective — record result.
6. Update session continuity (`lhw1_t3_complete` or `lhw1_t3_deferred`).
7. Update LHW1 roadmap `Status` to `CLOSED_PASS_BOUNDED`.
8. Commit:
   - T3 complete: `docs(lhw1-t3): add context profile connector spec`
   - T3 deferred: `docs(lhw1-t3): defer context profile connector — no gap found`
9. Write completion review (or deferral note).

Spec size guard: < 200 lines. Trim Section 4 prose if approaching 180 lines.

## Review Gate

Before committing: Reviewer perspective completed; all 3 gate conditions
documented; `canReinject: false` confirmed; demand-gated items listed;
no code file in diff.

## Closure Checklist

- [ ] All 3 gate conditions confirmed and documented
- [ ] Named context gap addressed in spec (or deferral documented)
- [ ] Compaction/relevance rules present with legacy source attribution
- [ ] `canReinject: false` stated explicitly
- [ ] No code file in diff
- [ ] LHW1 roadmap status updated to `CLOSED_PASS_BOUNDED`
- [ ] Session continuity updated

## Evidence Requirements

Spec at target path; all 3 gate conditions documented; context field mapping
table present; compaction rules sourced from caveman/GoClaw; `canReinject: false`
explicit; no code file in diff; LHW1 roadmap updated; completion review written.
If T3 deferred: deferral note present in handoff; roadmap marked
`CLOSED_PASS_BOUNDED`.

## Acceptance Criteria

- [ ] All 3 gate conditions confirmed and documented
- [ ] Named context gap addressed in spec (or deferral documented)
- [ ] Context field mapping table covers minimum 5 rows
- [ ] All 5 compaction/relevance rules present with legacy source attribution
- [ ] Demand-gated items (caveman runtime, GoClaw runtime, LLM scoring) listed
- [ ] `canReinject: false` stated explicitly
- [ ] No `.ts`/`.tsx`/`.js`/`.py` file in diff
- [ ] LHW1 roadmap status updated to `CLOSED_PASS_BOUNDED`
- [ ] Session continuity updated

## Return-To-Orchestrator Conditions

Stop and report to Orchestrator if:

- any gate condition is not met;
- VI2 field names cannot be confirmed without reading `route-request-context-readout.ts`
  (in that case: Implementer may read the file to confirm names but must
  not modify it; record the confirmed field names in the completion note);
- writing the connector requires re-opening the caveman runtime demand-gate;
- spec exceeds 200 lines before Section 4 is complete.

## Operator Checkpoint

No operator checkpoint required unless:

- T3 reveals a conflict between VI2 field names and the context gap
  described in T2 (escalate);
- the roadmap closure at `CLOSED_PASS_BOUNDED` needs operator confirmation
  before session state is updated.

## Claim Boundary

LHW1-T3 produces a context profile connector specification document. It does
not claim caveman runtime context budgeting, Workflow GoClaw session
classification runtime, LLM-based context scoring, raw memory reinjection,
VI2/VI3 implementation changes, hosted readiness, production readiness, or
public release readiness.

If T3 is deferred, LHW1 closes at T1+T2 (CLOSED_PASS_BOUNDED) — this is
a valid and complete outcome. Deferred T3 does not indicate a failure.
