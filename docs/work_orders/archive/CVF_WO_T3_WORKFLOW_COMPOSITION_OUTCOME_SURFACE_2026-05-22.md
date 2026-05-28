# Work Order — T3 Workflow Composition + Outcome Surface

Memory class: FULL_RECORD

Status: READY_FOR_IMPLEMENTATION

docType: work_order

Worker role: Codex (full Orchestrator → Reviewer → Implementer → Auditor chain)

Date dispatched: 2026-05-22

---

## Purpose

Wire the workflow composition layer and expand the noncoder outcome
surface to six governed outcomes backed by the T2 certified packs. T3
delivers the `WorkflowComposition` interface, the six-outcome registry,
the expanded `OutcomeQuickActions` component, and an optional
`workflowComposition` field on `GovernanceEvidenceReceipt`. This last
item requires the `new_receipt_envelopes` blocked-work-class override.
If the override is not granted, T3 ships the composition contract and
outcome surface without the receipt field; the receipt field becomes a
separate demand-gated candidate.

Pre-condition: T2 must be closed before T3 begins.

---

## Authority Chain

- Active roadmap (V2):
  `docs/roadmaps/CVF_REVIEW_CVF_PAIN_POINT_DELIVERY_GAP_ROADMAP_V2_2026-05-22.md`
- Predecessor audit:
  `docs/audits/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_GAP_AUDIT_2026-05-22.md`
- T2 work order (pre-condition):
  `docs/work_orders/CVF_WO_T2_PRODUCT_SKILL_PACK_MVP_2026-05-22.md`
- T2 completion review (must be filed before T3 starts):
  `docs/reviews/CVF_T2_PRODUCT_SKILL_PACK_MVP_COMPLETION_2026-05-22.md`
- Source review (original requirement):
  `.private_reference/legacy/CVF 17.05/Review CVF.md`
- GC-018 to be filed:
  `docs/baselines/CVF_GC018_T3_WORKFLOW_COMPOSITION_OUTCOME_SURFACE_2026-05-22.md`

---

## Agent Roles

- **Orchestrator (Codex):** Confirm T2 is closed. File GC-018 baseline
  before any implementation file is created. The GC-018 must explicitly
  state whether the `new_receipt_envelopes` override is granted (with
  operator confirmation) or whether T3 ships the split scope (no receipt
  field). Operator must provide confirmation of override status before
  Orchestrator proceeds past GC-018.
- **Reviewer (Codex):** Confirm T3 stays composition + outcome surface
  only. No provider method change, no memory wiring, no new provider
  adapters. Confirm receipt field is only added if override is confirmed
  in GC-018.
- **Implementer (Codex):** Author `WorkflowComposition` interface, the
  six-entry outcome-to-workflow registry, the expanded
  `OutcomeQuickActions` component, and (if override granted) the receipt
  field extension. Write UI unit tests for the new component state.
- **Auditor (Codex):** Run `npm run test:run` and TypeScript check for
  `cvf-web`, run governance hook chain, file completion review, update
  active queue/state/handoff.

---

## Blocked-Work Override Requirement

T3 touches one blocked-work class:

- **`new_receipt_envelopes`** — adding an optional `workflowComposition`
  field to `GovernanceEvidenceReceipt`.

The GC-018 baseline must record one of:

1. **Override granted:** Operator has explicitly confirmed
   `new_receipt_envelopes` override for this specific field. Codex may
   then add the optional `workflowComposition` field to the receipt type
   in `types.ts`.
2. **Override not granted (split scope):** T3 ships composition contract
   and outcome surface without the receipt field. The receipt field is
   declared a separate demand-gated candidate in the GC-018. No change
   to `GovernanceEvidenceReceipt` or `types.ts`.

Operator confirmation of override status is required **before** the
Orchestrator role proceeds past S-02 (GC-018). This is an Operator
Checkpoint (see below).

---

## Scope / Target / Owner Boundary

### Write ownership (in scope — base scope, applies regardless of override)

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflow-composition/`
  (new directory) containing:
  - `WorkflowComposition.ts` — TypeScript interface and types.
  - `outcome-workflow-registry.ts` — six-entry registry mapping outcome
    keys to their `WorkflowComposition` objects.
  - `index.ts` — re-export.
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/OutcomeQuickActions.tsx`
  — expand from existing stub to include all six outcomes backed by the
  registry. Must respect the existing component contract (no auth/RBAC
  change, no new route, no new API call).
- Test files under
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflow-composition/__tests__/`
  — unit tests for registry completeness and component rendering.
- `docs/baselines/CVF_GC018_T3_WORKFLOW_COMPOSITION_OUTCOME_SURFACE_2026-05-22.md`
  (new).
- `docs/reviews/CVF_T3_WORKFLOW_COMPOSITION_OUTCOME_SURFACE_COMPLETION_2026-05-22.md`
  (new).
- `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` — update T3 entry status.
- `CVF_SESSION/ACTIVE_SESSION_STATE.json` — update `lastUpdated` and
  `t3WorkflowCompositionOutcomeSurface` field.
- `AGENT_HANDOFF_V11_2026-05-21.md` — GC-020 sync entry.

### Write ownership (in scope — override scope, only if `new_receipt_envelopes` override granted)

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts` —
  add one optional field `workflowComposition?: WorkflowCompositionSummary`
  to `GovernanceEvidenceReceipt`. No other change to this file.

### Out of scope (forbidden)

- Any change to `route.ts` or any API route file.
- Any change to provider adapters (`CVF_MODEL_GATEWAY/`).
- Any live provider call. T3 is offline-only.
- Any memory wiring (that is T5).
- Any provider method contract (that is T4).
- Any change to auth/RBAC, new routes, new API endpoints.
- Public-sync repository update.
- Maika, child-data, photo, or vision proof.
- Any receipt envelope change if the override is not granted (split
  scope applies).

---

## Required First Reads

- `docs/roadmaps/CVF_REVIEW_CVF_PAIN_POINT_DELIVERY_GAP_ROADMAP_V2_2026-05-22.md`
- `docs/work_orders/CVF_WO_T2_PRODUCT_SKILL_PACK_MVP_2026-05-22.md`
- `docs/reviews/CVF_T2_PRODUCT_SKILL_PACK_MVP_COMPLETION_2026-05-22.md`
  (T2 pre-condition check — must exist and show CLOSED)
- `governance/registries/cvf-certified-skill-pack-registry.json`
  (authored by T2 — source of truth for seven pack IDs and outcomeKeys)
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts`
  (read current `GovernanceEvidenceReceipt` shape — read-only unless
  override granted)
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/`
  (read existing `OutcomeQuickActions` stub and component patterns)
- `.private_reference/legacy/CVF 17.05/Review CVF.md` (lines 466–525
  for noncoder outcome surface design)
- `governance/toolkit/05_OPERATION/CVF_GOVERNED_FILE_SIZE_GUARD.md`
- `docs/reference/CVF_MARKDOWN_STRUCTURAL_COMPLETENESS_STANDARD.md`

---

## Pre-Flight Checks

Before writing any implementation file:

1. Confirm T2 completion review exists with status
   `CLOSED_T2_PRODUCT_SKILL_PACK_MVP`. If T2 is not closed, stop.
2. Read the certified skill pack registry and confirm all seven packs are
   present with `status: "certified"`. Confirm each pack's `outcomeKey`
   maps to one of the six outcomes in V2 roadmap T3.
3. Read the current `GovernanceEvidenceReceipt` type in `types.ts`.
   Record the current field count and all field names before any edit.
4. Confirm the `new_receipt_envelopes` override decision is recorded in
   the GC-018 baseline (Operator Checkpoint required before S-02 closes).
5. GC-023 pre-flight: `types.ts` current line count must be checked
   before any edit. If adding one field would exceed the approved max,
   open a new wrapper type file instead and import it.
6. GC-023 pre-flight: `OutcomeQuickActions.tsx` current line count must
   be checked. If expansion would exceed the GC-023 threshold, split
   into sub-components (e.g., `OutcomeQuickActionsGrid.tsx`).

---

## Execution Plan

T3 executes in ten sequential steps S-01 → S-10.

## Implementation Steps

### S-01 — Confirm T2 pre-condition

Read T2 completion review and registry. Confirm both exist and are
consistent. If any check fails, file a return note and stop.

### S-02 — File GC-018 baseline (with override decision)

Create `docs/baselines/CVF_GC018_T3_WORKFLOW_COMPOSITION_OUTCOME_SURFACE_2026-05-22.md`
declaring:

- Pre-condition: T2 closed (cite completion review and registry paths).
- Scope locked to write ownership above.
- Blocked-work class: `new_receipt_envelopes`.
- Override status: GRANTED or NOT_GRANTED (must be filled in by
  Orchestrator after operator confirmation).
- If NOT_GRANTED: document split-scope boundary (no `types.ts` change;
  receipt field is a separate demand-gated candidate).
- Acceptance criteria copied verbatim from V2 roadmap T3.
- Forbidden actions: any out-of-scope item from this work order.

### S-03 — Author WorkflowComposition interface

Create `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflow-composition/WorkflowComposition.ts`
defining:

```typescript
export interface WorkflowComposition {
  outcomeKey: string;
  packIds: string[];
  policyRefs: string[];
  inputContract: string;
  outputContract: string;
  deterministicFixturePath: string;
}

// Summary shape used in receipt (only present if new_receipt_envelopes override granted)
export interface WorkflowCompositionSummary {
  outcomeKey: string;
  packIds: string[];
  compositionVersion: string;
}
```

Types must match V2 roadmap T3 spec. Do not add fields beyond what is
specified here.

### S-04 — Author outcome-workflow registry

Create `outcome-workflow-registry.ts` with six entries mapping outcome
keys to `WorkflowComposition` objects:

| Outcome key | Pack(s) | Output |
| --- | --- | --- |
| `create_prd` | `product_brief` | Product requirements document |
| `generate_sop` | `sop_generator` | Standard operating procedure |
| `review_contract` | `contract_review` | Contract review report |
| `build_landing_page` | `landing_page_builder` | Landing page copy |
| `summarize_meeting` | `meeting_summarizer` | Meeting summary |
| `create_proposal` | `proposal_writer` | Proposal document |

Each entry must include `outcomeKey`, `packIds`, `policyRefs`,
`inputContract`, `outputContract`, and `deterministicFixturePath`.
`deterministicFixturePath` must point to a plausible fixture location
(e.g., `tests/fixtures/workflow/<outcomeKey>.fixture.json`) — the
fixture file itself is not required at T3 time, only the path binding.

### S-05 — Expand OutcomeQuickActions component

Update `OutcomeQuickActions.tsx` to render all six outcome buttons backed
by the registry. Requirements:

- Each button/card must display the outcome label and call to action.
- Component must render correctly with all six outcomes visible.
- No new API call, no new route, no auth/RBAC change.
- Must pass TypeScript check.
- If file would exceed GC-023 threshold after expansion, split to a
  sub-component before expanding.

### S-06 — Add receipt field (override scope only)

If and only if `new_receipt_envelopes` override is GRANTED in GC-018:

Edit `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts`
to add:

```typescript
workflowComposition?: WorkflowCompositionSummary;
```

to the `GovernanceEvidenceReceipt` interface. Import
`WorkflowCompositionSummary` from the composition lib. No other change
to `types.ts`. Confirm field count before and after.

If override is NOT_GRANTED: skip this step entirely. Do not add the
field. Record the skip in the completion review.

### S-07 — Write unit tests

Create tests under `cvf-web/src/lib/workflow-composition/__tests__/`:

- `outcome-workflow-registry.test.ts` — verify all six outcomes are
  present in the registry; verify each entry has required fields; verify
  `packIds` reference valid pack IDs from the T2 registry.
- `OutcomeQuickActions.test.tsx` — verify all six outcome labels render;
  verify no broken imports.

Run `npm run test:run` — all tests must PASS.

### S-08 — TypeScript check

Run `npm run build` or equivalent TypeScript check for `cvf-web`. Must
complete without errors.

### S-09 — Governance hook chain

Run:

```bash
python governance/compat/check_markdown_structural_completeness.py --base HEAD --head HEAD --enforce
python governance/compat/check_governed_file_size.py --enforce
```

Both must report COMPLIANT.

### S-10 — File completion review, update session, commit

Create
`docs/reviews/CVF_T3_WORKFLOW_COMPOSITION_OUTCOME_SURFACE_COMPLETION_2026-05-22.md`
including:

- Memory class FULL_RECORD, status
  `CLOSED_T3_WORKFLOW_COMPOSITION_OUTCOME_SURFACE`.
- Override decision recorded: GRANTED or NOT_GRANTED.
- If NOT_GRANTED: document receipt field as separate demand-gated
  candidate.
- Evidence trace: `npm run test:run` output (excerpt showing new tests
  PASS), TypeScript check output, hook chain results.
- Findings: PASS or FAIL per acceptance criterion.
- Claim boundary.

Update active session (queue, state, handoff) and commit with message:

```text
feat(t3): close workflow composition + noncoder outcome surface

Authority: docs/roadmaps/CVF_REVIEW_CVF_PAIN_POINT_DELIVERY_GAP_ROADMAP_V2_2026-05-22.md
GC-018: docs/baselines/CVF_GC018_T3_WORKFLOW_COMPOSITION_OUTCOME_SURFACE_2026-05-22.md
Completion: docs/reviews/CVF_T3_WORKFLOW_COMPOSITION_OUTCOME_SURFACE_COMPLETION_2026-05-22.md

Closes T3 from the Review-CVF pain-point delivery gap roadmap V2:
- WorkflowComposition interface + outcome-workflow registry (6 entries)
- OutcomeQuickActions expanded to 6 outcomes
- new_receipt_envelopes override: [GRANTED|NOT_GRANTED]
- [If GRANTED: workflowComposition? field added to GovernanceEvidenceReceipt]
- [If NOT_GRANTED: receipt field deferred to demand-gated candidate]
- Unit tests PASS, TypeScript check PASS

Boundary: composition + outcome surface only. No provider method change,
no memory wiring, no new routes, no auth change, no public-sync update.
```

---

## Evidence Requirements

Every closure claim must be backed by:

- T2 completion review path and status (pre-condition).
- Override decision from GC-018 (GRANTED or NOT_GRANTED).
- `npm run test:run` output (relevant test file lines).
- TypeScript check output (no errors).
- Hook chain COMPLIANT output.
- If override GRANTED: `GovernanceEvidenceReceipt` field count before
  and after (must differ by exactly +1).
- Closure commit SHA.

---

## Acceptance Criteria

Closure requires **all** of:

1. T2 pre-condition confirmed (completion review CLOSED, registry with
   seven packs).
2. GC-018 filed with explicit override decision.
3. `WorkflowComposition` interface and registry authored with six entries.
4. `OutcomeQuickActions` expanded to six outcomes.
5. If override GRANTED: one optional field added to
   `GovernanceEvidenceReceipt`; no other `types.ts` change.
6. If override NOT_GRANTED: `types.ts` unchanged; receipt field declared
   demand-gated in GC-018 and completion review.
7. Unit tests authored and PASS.
8. TypeScript check: no errors.
9. No file outside write ownership modified (per override scope).
10. Markdown structural completeness: COMPLIANT.
11. File size guard: COMPLIANT.
12. Local governance hook chain: PASS.
13. Completion review filed with all required sections.
14. Active queue, state, and handoff updated with closure SHA.

---

## Review Gate

Before commit, Codex acting in Reviewer role must independently confirm:

1. Override decision in GC-018 matches the implementation (field added
   iff GRANTED; unchanged iff NOT_GRANTED).
2. No route file, API endpoint, or auth/RBAC file was modified.
3. No provider adapter or `CVF_MODEL_GATEWAY/` file was modified.
4. No live provider call was made.
5. If override GRANTED: `types.ts` change is exactly one optional field
   added; no other type was changed.
6. All six outcomes are present in the registry and in the component.
7. `npm run test:run` passed with zero failures.
8. None of the active session state blocked-work classes other than
   `new_receipt_envelopes` (if override granted) is touched.

---

## Closure Checklist

- [ ] T2 pre-condition confirmed.
- [ ] GC-018 filed with explicit override decision (GRANTED or NOT_GRANTED).
- [ ] `WorkflowComposition.ts` authored.
- [ ] `outcome-workflow-registry.ts` authored with six entries.
- [ ] `OutcomeQuickActions.tsx` expanded to six outcomes.
- [ ] Receipt field added to `types.ts` iff override GRANTED (or
      explicitly skipped iff NOT_GRANTED, with demand-gated note).
- [ ] Unit tests authored and PASS.
- [ ] TypeScript check: no errors.
- [ ] Markdown structural completeness gate: COMPLIANT.
- [ ] Governed file size guard: COMPLIANT.
- [ ] Local governance hook chain pre-commit: PASS.
- [ ] Local governance hook chain pre-push: PASS.
- [ ] Active review queue updated with T3 closure status.
- [ ] Active session state updated with `t3WorkflowCompositionOutcomeSurface` field.
- [ ] Handoff updated with GC-020 sync entry and closure SHA.
- [ ] Completion review filed with all required sections.

---

## Operator Checkpoint

**This work order has one mandatory Operator Checkpoint.**

Before the Orchestrator proceeds past S-02 (GC-018), the operator must
explicitly confirm the `new_receipt_envelopes` override status:

- **GRANTED:** The operator authorizes adding `workflowComposition?` to
  `GovernanceEvidenceReceipt`. The GC-018 must record this authorization
  with the operator's confirmation statement.
- **NOT_GRANTED:** The operator confirms T3 ships split scope. The
  receipt field is a separate demand-gated candidate. The GC-018 must
  record this boundary.

Operator confirmation alone (e.g., "proceed") is not sufficient. The
GC-018 must record the override status explicitly. If the operator does
not confirm override status before S-02, Codex must pause and request
clarification.

If T3 encounters a Return-to-Orchestrator condition, the operator must
be consulted before the work order is reopened.

---

## Return-to-Orchestrator Conditions

Return this work order to the Orchestrator (do not close) if **any**:

- T2 is not closed when T3 begins.
- Operator does not confirm override status before GC-018 is filed.
- `OutcomeQuickActions.tsx` cannot be expanded within GC-023 limits
  without a structural refactor that would touch files outside write
  ownership.
- Any acceptance criterion fails and the cause is unclear within
  bounded debug time.
- Any out-of-scope file change would be necessary to make T3 close.

When returning, file a return note at
`docs/reviews/CVF_T3_WORKFLOW_COMPOSITION_OUTCOME_SURFACE_RETURN_2026-05-22.md`
naming the blocker.

---

## Forbidden Patterns (Anti-Pattern Guardrails from V2)

T3 closure must not occur via any of:

- **Closure by rejection.** T3 cannot close by arguing the outcome
  surface already exists in a different form.
- **Closure by scope redefinition.** T3 cannot close by shipping fewer
  than six outcomes.
- **Contract-only closure.** T3 cannot close by delivering the
  interface types without the expanded `OutcomeQuickActions` component.
- **Implicit scope inflation.** T3 cannot add new routes, auth changes,
  or provider calls beyond what is specified.

---

## Claim Boundary

This work order authorizes only:

- The `WorkflowComposition` interface and six-entry registry.
- The expanded `OutcomeQuickActions` component.
- The optional receipt field (only if `new_receipt_envelopes` override
  is explicitly granted).
- The GC-018 baseline, completion review, and active-session updates.

It does not authorize any provider method contract, any memory wiring,
any new route, any new provider, any live provider call, any public-sync
update, any release claim, any freeze lift, or any
Maika/child-data/photo/vision claim.
