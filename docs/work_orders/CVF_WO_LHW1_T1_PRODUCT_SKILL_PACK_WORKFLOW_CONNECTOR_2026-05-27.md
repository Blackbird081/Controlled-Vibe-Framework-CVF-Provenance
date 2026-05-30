# CVF Work Order — LHW1-T1 Product Skill Pack Workflow Connector

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-05-27

---

## Purpose

Implement LHW1-T1: a canonical connector spec that turns a certified CVF
product skill pack into a non-coder workflow chain.

This work order authorizes a documentation-only tranche. No source code,
runtime module, route, or provider behavior is changed.

## Retroactive Source Verification Addendum

This work order is closed, but future reuse or amendment must satisfy the
2026-05-27 Mandatory Work Order Source Verification rule.

T1 references existing source-contract vocabulary from W1/WR1, MA1,
`GovernanceEvidenceReceipt`, V3 diagnostics, W3/TA1 action taxonomy, and the
C7A certified pack inventory. A successor or amended work order must include a
Source Verification Table before implementation whenever it instructs a worker
to use concrete field names, type names, receipt fields, diagnostic classes,
role values, route states, pack IDs, policy enums, source paths, or schema keys.

Required columns:

| Claimed item | Source file | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|

`ACCEPT` requires direct source or canonical-contract verification. `REJECT`
must record the corrected symbol when known. `BLOCKED_SOURCE_NOT_FOUND` returns
the work order to Orchestrator. Guessed names, stale memory-only vocabulary,
placeholder source paths, and "confirm later" language are not allowed.

## Authority Chain

- Operator directed legacy knowledge absorption continuation on 2026-05-27.
- Roadmap: `docs/roadmaps/CVF_LHW1_LEGACY_WORKFLOW_CONNECTOR_ABSORPTION_ROADMAP_2026-05-27.md`
- Fast Lane audit: `docs/reviews/CVF_LHW1_T1_FAST_LANE_AUDIT_2026-05-27.md`
  → Decision: FAST_LANE_READY
- LH1 Closeout Ledger reopen trigger: met — C7A/C8/Human System Harness
  partially absorbed; operator demand present.
- Knowledge Absorption Blind-Spot verdict: CLEAR (recorded in roadmap).

## Required First Reads

Before writing a single line of the connector spec, read these files in order:

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `docs/reference/archive/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
   — confirm C7A/C8 disposition and remaining trigger.
4. `docs/reviews/archive/CVF_C7A_PRODUCT_SKILL_PACK_TOP10_COMPLETION_2026-05-25.md`
   — understand the 10 certified packs and their metadata shape.
5. `docs/reviews/archive/CVF_C8_PRODUCT_SKILL_PACK_SELECTION_READOUT_COMPLETION_2026-05-25.md`
   — understand the selection readout and CB1 context budget pattern.
6. `docs/roadmaps/CVF_MA1_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_ROADMAP_2026-05-26.md`
   — understand role-transfer packet fields before writing T2-adjacent
   state connector fields (needed in T1 schema definition as forward-compat
   stubs only, not implementation).
7. `docs/roadmaps/CVF_LHW1_LEGACY_WORKFLOW_CONNECTOR_ABSORPTION_ROADMAP_2026-05-27.md`
   — confirm candidate screen, deliverables, and claim boundary.

Do not scope from summaries alone. If a referenced completion review is
missing, stop and report to Orchestrator before proceeding.

## Scope / Target / Owner Boundary

### Allowed owner files

- `docs/reference/CVF_LHW1_PRODUCT_SKILL_PACK_WORKFLOW_CONNECTOR_SPEC_2026-05-27.md`
  (new — primary deliverable)
- this work order (status update only)
- session continuity files (`CVF_SESSION_MEMORY.md`,
  `CVF_SESSION/ACTIVE_SESSION_STATE.json`, active handoff)

### Forbidden

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/` — any file
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/governance/` — any file
- `governance/contracts/` — any file
- `/api/execute` route
- receipt envelope schema
- skill pack registry TypeScript
- any `.ts`, `.tsx`, `.js`, `.py` file
- public-sync repo
- any hosted or production surface

## Deliverables

### Deliverable 1 — Connector spec

File: `docs/reference/CVF_LHW1_PRODUCT_SKILL_PACK_WORKFLOW_CONNECTOR_SPEC_2026-05-27.md`

The spec must contain all of the following sections:

**Section 1 — Purpose and scope boundary**
- What the connector is (turns a certified skill pack into a workflow
  chain readable by a non-coder or an agent).
- What it is not (not a runtime scheduler, not a live provider call,
  not a memory reinject mechanism).

**Section 2 — Required fields: Skill Pack Metadata**

At minimum:
- `packId` — unique identifier (string, matches registry key)
- `packName` — human-readable English name
- `packVersion` — semver string
- `outcomeFamily` — top-level outcome (e.g. `product`, `marketing`)
- `certificationStatus` — `certified | experimental | deprecated`
- `nonCoderSummary` — one sentence describing what a non-coder gets

**Section 3 — Required fields: Workflow Spec**

At minimum:
- `workflowId` — string
- `phases` — ordered list: each phase has `name`, `role`, `inputs`,
  `outputs`, `successCriteria`
- `phaseTransitions` — list of valid `from → to` pairs (maps to W1
  state machine vocabulary: `intake_pending → design_ready →
  build_running → review_pending → freeze_ready → completed`)
- `recoveryCheckpoint` — which phase can be restored if interrupted
  (maps to WR1 pattern)

**Section 4 — Required fields: Execution Policy**

At minimum:
- `maxRiskLevel` — `R0 | R1 | R2 | R3`
- `requiresLiveProvider` — boolean
- `requiresReviewerGate` — boolean and at which phase
- `blockedActions` — list of action classes that cannot be executed
  within this workflow (maps to W3/TA1 vocabulary)

**Section 5 — Required fields: Review Checklist**

At minimum:
- `reviewerRoles` — list of roles that must approve (maps to MA1
  packet role lanes: Orchestrator, Reviewer, Implementer, Auditor)
- `dissent handling` — what happens when a reviewer dissents
- `evidenceRequired` — minimum evidence before marking `freeze_ready`

**Section 6 — Required fields: Receipt Schema**

At minimum:
- `receiptRequired` — boolean
- `receiptFields` — list of fields expected in the governance evidence
  receipt (reference existing `GovernanceEvidenceReceipt` field names
  where applicable; do not invent new receipt envelope fields)
- `canReinject` — must be hardcoded `false`

**Section 7 — Required fields: Failure Recovery**

At minimum:
- `failureClasses` — list of expected failure classes (maps to V3
  `ExecutionDiagnosticClass` vocabulary where applicable)
- `recoveryActions` — per failure class: `retry | escalate | hold |
  abort`
- `userVisibleMessage` — non-technical message pattern for non-coders

**Section 8 — Mapping from web template/spec export surfaces**

Describe (in prose, not code) how the current cvf-web template
selector and spec export surfaces map to connector fields:
- which connector field a non-coder would fill via the UI
- which field comes from the skill pack registry automatically
- which field requires governance review before population

This is a mapping description only. No cvf-web file is modified.

**Section 9 — Example connector records**

Provide at least two complete connector records using the fields
defined above. Use these certified packs as examples:
- `product_brief` (pack from C7A top-10)
- one other from the C7A registry (agent's choice)

Each record must be valid against all required fields in sections 2-7.

### Deliverable 2 — Session continuity update

Update `CVF_SESSION/ACTIVE_SESSION_STATE.json` and active handoff to
reflect `lhw1_t1_complete` after commit.

## Allowed / Forbidden Scope Summary

| Action | Allowed |
|---|---|
| Create connector spec markdown file | YES |
| Update session state + handoff | YES |
| Modify any `.ts` or `.tsx` file | NO |
| Modify cvf-web routes or components | NO |
| Change receipt envelope schema | NO |
| Modify skill pack registry TypeScript | NO |
| Call a live provider | NO |
| Add to public-sync repo | NO |

## Pre-Flight Checks

Before starting implementation:

- [ ] working tree is clean (`git status` → nothing staged or modified)
- [ ] active session state resolves to this work order as next allowed move
- [ ] LH1 closeout ledger reopen trigger confirmed (C7A/C8 PARTIALLY_ABSORBED)
- [ ] all required first reads completed

## Agent Roles

| Role | Responsibility |
|---|---|
| Implementer | Reads required sources; writes connector spec and example records; updates session continuity; opens commit |
| Reviewer | Verifies spec contains all 7 required field sections; verifies examples are complete; verifies no code file is touched; verifies canReinject=false |
| Auditor | Confirms Fast Lane decision is recorded; confirms LH1 ledger trigger; confirms no runtime claim in the spec |

The Implementer must not self-review. If operating solo, complete
Implementer work, then switch to Reviewer perspective explicitly and
record the review result in the completion note before closing.

## Write Ownership

Implementer owns all new files. Reviewer and Auditor hold read + review
rights only. No file outside the Allowed list in the Scope section may be
modified by any role.

## Execution Plan

1. Read all required first reads (section above).
2. Draft `docs/reference/CVF_LHW1_PRODUCT_SKILL_PACK_WORKFLOW_CONNECTOR_SPEC_2026-05-27.md`
   with sections 1-9 above.
3. Confirm connector spec satisfies all deliverable requirements.
4. Confirm no code file is staged.
5. Switch to Reviewer perspective; record review result.
6. Update `CVF_SESSION/ACTIVE_SESSION_STATE.json` and active handoff.
7. Commit with message: `docs(lhw1-t1): add product skill pack workflow connector spec`.
8. Record completion in `docs/reviews/CVF_LHW1_T1_PRODUCT_SKILL_PACK_WORKFLOW_CONNECTOR_COMPLETION_2026-05-27.md`.

## Review Gate

Before committing:
- Reviewer perspective completed (Implementer switches role explicitly).
- All Acceptance Criteria confirmed checked.
- No `.ts`/`.tsx`/`.js`/`.py` file in diff.

## Evidence Requirements

Required before closure:

- connector spec file exists at target path;
- spec contains all 9 sections;
- at least 2 complete example records;
- `canReinject: false` appears in every example record;
- no `.ts`, `.tsx`, `.js`, `.py` file appears in `git diff --name-only`;
- session continuity files updated;
- completion review file exists.

Live proof: not applicable — no live behavior is asserted in T1.

## Closure Checklist

- [ ] Connector spec created with all 9 sections
- [ ] Example records present with `canReinject: false`
- [ ] No code file in diff
- [ ] Session continuity updated
- [ ] Completion review written
- [ ] Work order status updated to `CLOSED_PASS_BOUNDED`

## File Size Guard (GC-023)

- Target file is a new markdown file.
- Hard limit for new governed markdown: 300 lines.
- If the connector spec with examples exceeds 250 lines, split into:
  - `CVF_LHW1_PRODUCT_SKILL_PACK_WORKFLOW_CONNECTOR_SPEC_2026-05-27.md`
    (spec only, sections 1-8)
  - `CVF_LHW1_PRODUCT_SKILL_PACK_WORKFLOW_CONNECTOR_EXAMPLES_2026-05-27.md`
    (section 9 examples)
- Register the split in the exception registry if either file
  exceeds 200 lines.

## Acceptance Criteria

- [ ] Connector spec file created with all 9 required sections
- [ ] At least 2 complete example records using C7A certified packs
- [ ] `canReinject: false` in every example record
- [ ] Phase vocabulary matches W1/WR1 state machine standard
- [ ] MA1 role lanes referenced correctly in review checklist section
- [ ] W3/TA1 blocked-action vocabulary referenced in execution policy
- [ ] Mapping to web surfaces is prose description only — no code change
- [ ] No `.ts`, `.tsx`, `.js`, `.py` file in diff
- [ ] Session continuity updated
- [ ] Completion review file written

## T2/T3 Gate

After this work order closes PASS:

- Orchestrator reviews whether the connector shape is useful and
  concrete.
- If yes: T2 (Workflow Chain State Connector) may be dispatched with
  a fresh Fast Lane audit referencing T1's connector spec as its
  authority source.
- If no: T2 is deferred. Operator checkpoint required before
  reopening.

T2 and T3 are NOT authorized by this work order. Do not implement them
in this tranche.

## Return-To-Orchestrator Conditions

Stop and report to Orchestrator if any of the following occur:

- a required first read file is missing or corrupt;
- writing the connector spec would require modifying a TypeScript file;
- any field in the spec requires a live provider call to validate;
- Candidate 7 external skill ingestion is needed to produce an example;
- the spec grows beyond 300 lines before sections 1-7 are complete.

## Operator Checkpoint

No operator checkpoint is required unless:

- the Implementer discovers that the connector shape conflicts with
  an existing runtime contract (escalate immediately); or
- T2 dispatch is being considered (requires Orchestrator review of T1
  outcome first).

## Claim Boundary

LHW1-T1 produces a canonical connector specification document. It does
not claim runtime workflow enforcement, external skill ingestion,
MCP/tool action execution, memory reinjection, hosted readiness,
production readiness, or public release readiness.
