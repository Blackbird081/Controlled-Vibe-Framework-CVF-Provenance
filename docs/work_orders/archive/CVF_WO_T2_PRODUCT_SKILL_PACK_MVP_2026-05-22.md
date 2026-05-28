# Work Order — T2 Product Skill Pack MVP (7 Certified Packs + Registry)

Memory class: FULL_RECORD

Status: READY_FOR_IMPLEMENTATION

docType: work_order

Worker role: Codex (full Orchestrator → Reviewer → Implementer → Auditor chain)

Date dispatched: 2026-05-22

---

## Purpose

Build the seven certified skill packs that deliver the noncoder-facing
Product Skill Pack System described in Review CVF.md pain points B and F.
T2 ships real governed pack artifacts that pass the T1 validator, plus the
registry JSON that surfaces them. T2 is packs + registry only; no UI
change, no runtime change, no receipt envelope change, no workflow
composition engine.

Pre-condition: T1 must be closed before T2 begins. T2 consumes the T1
schemas, validator, and reference pack as its certification contract.

---

## Authority Chain

- Active roadmap (V2):
  `docs/roadmaps/CVF_REVIEW_CVF_PAIN_POINT_DELIVERY_GAP_ROADMAP_V2_2026-05-22.md`
- Predecessor audit:
  `docs/audits/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_GAP_AUDIT_2026-05-22.md`
- T1 work order (pre-condition):
  `docs/work_orders/CVF_WO_T1_CAPABILITY_INTAKE_PIPELINE_2026-05-22.md`
- T1 completion review (must be filed before T2 starts):
  `docs/reviews/CVF_T1_CAPABILITY_INTAKE_PIPELINE_COMPLETION_2026-05-22.md`
- Source review (original requirement):
  `.private_reference/legacy/CVF 17.05/Review CVF.md`
- GC-018 to be filed:
  `docs/baselines/CVF_GC018_T2_PRODUCT_SKILL_PACK_MVP_2026-05-22.md`

---

## Agent Roles

- **Orchestrator (Codex):** Confirm T1 is closed (completion review
  filed, T1 validator PASS recorded). File GC-018 baseline before any
  pack artifact is created.
- **Reviewer (Codex):** Confirm T2 stays packs + registry only. No UI
  change, no workflow composition, no receipt envelope change, no live
  provider call, no public-sync update. Confirm none of the blocked-work
  classes is touched.
- **Implementer (Codex):** Create seven pack directories, populate each
  with the eight required artifacts, run the T1 validator on all seven,
  create the registry JSON.
- **Auditor (Codex):** Verify all seven packs PASS the validator, run
  governance hook chain, file completion review, update active
  queue/state/handoff.

---

## Write Ownership

See "Write ownership (in scope)" under Scope below for the complete file
list. Codex must not modify any file outside that list. Any need to
touch a file outside write ownership triggers Return-to-Orchestrator.

---

## Scope / Target / Owner Boundary

### Write ownership (in scope)

- `EXTENSIONS/CVF_v1.5.2_SKILL_LIBRARY_FOR_END_USERS/_certified/product_brief/`
  (new) — eight artifacts.
- `EXTENSIONS/CVF_v1.5.2_SKILL_LIBRARY_FOR_END_USERS/_certified/sop_generator/`
  (new) — eight artifacts.
- `EXTENSIONS/CVF_v1.5.2_SKILL_LIBRARY_FOR_END_USERS/_certified/strategy_analysis/`
  — already created by T1 as reference pack; T2 must not re-create or
  modify T1's reference pack. T2 uses it as a completed example only.
- `EXTENSIONS/CVF_v1.5.2_SKILL_LIBRARY_FOR_END_USERS/_certified/proposal_writer/`
  (new) — eight artifacts.
- `EXTENSIONS/CVF_v1.5.2_SKILL_LIBRARY_FOR_END_USERS/_certified/meeting_summarizer/`
  (new) — eight artifacts.
- `EXTENSIONS/CVF_v1.5.2_SKILL_LIBRARY_FOR_END_USERS/_certified/contract_review/`
  (new) — eight artifacts.
- `EXTENSIONS/CVF_v1.5.2_SKILL_LIBRARY_FOR_END_USERS/_certified/landing_page_builder/`
  (new) — eight artifacts.
- `governance/registries/cvf-certified-skill-pack-registry.json` (new)
  — the registry listing all seven packs with their certification status.
- `docs/baselines/CVF_GC018_T2_PRODUCT_SKILL_PACK_MVP_2026-05-22.md`
  (new) — authorization baseline.
- `docs/reviews/CVF_T2_PRODUCT_SKILL_PACK_MVP_COMPLETION_2026-05-22.md`
  (new) — completion review.
- `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` — update T2 entry status.
- `CVF_SESSION/ACTIVE_SESSION_STATE.json` — update `lastUpdated` and
  `t2ProductSkillPackMvp` field after closure.
- `AGENT_HANDOFF_V11_2026-05-21.md` — GC-020 sync entry.

### Out of scope (forbidden)

- Any change to `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/` files,
  including the UI, routes, or types.
- Any change to `GovernanceEvidenceReceipt` shape or `types.ts`.
- Any change to `EXTENSIONS/CVF_MODEL_GATEWAY/` files.
- Any live provider call. T2 is offline-only.
- Any change to T1 artifacts (schemas, validator, reference pack) unless
  a defect in T1 is discovered — in that case, Return-to-Orchestrator.
- Any workflow composition engine (that is T3).
- Any outcome quick action expansion (that is T3).
- Any registry surface-level UI integration (that is T3).
- Any provider method contract (that is T4).
- Any memory wiring (that is T5).
- Public-sync repository update.
- Maika, child-data, photo, or vision proof.

### Owner boundary

Codex executes Orchestrator → Reviewer → Implementer → Auditor in a
single session. Operator authorization is the GC-018 baseline filed at
dispatch time.

---

## Required First Reads

- `docs/roadmaps/CVF_REVIEW_CVF_PAIN_POINT_DELIVERY_GAP_ROADMAP_V2_2026-05-22.md`
- `docs/work_orders/CVF_WO_T1_CAPABILITY_INTAKE_PIPELINE_2026-05-22.md`
- `docs/reviews/CVF_T1_CAPABILITY_INTAKE_PIPELINE_COMPLETION_2026-05-22.md`
  (T1 pre-condition check — must exist and show PASS)
- `governance/schemas/skill-pack/` (all eight schemas authored by T1)
- `scripts/validate_skill_pack_certification.py` (authored by T1)
- `EXTENSIONS/CVF_v1.5.2_SKILL_LIBRARY_FOR_END_USERS/_certified/strategy_analysis/`
  (T1 reference pack — use as structural template)
- `EXTENSIONS/CVF_v1.5.2_SKILL_LIBRARY_FOR_END_USERS/SKILL_TEMPLATE.md`
- `.private_reference/legacy/CVF 17.05/Review CVF.md` (lines 466–525
  for noncoder outcome surface; lines 390–440 for product skill pack
  system)
- `governance/toolkit/05_OPERATION/CVF_GOVERNED_FILE_SIZE_GUARD.md`
- `docs/reference/CVF_MARKDOWN_STRUCTURAL_COMPLETENESS_STANDARD.md`

---

## Pre-Flight Checks

Before writing any pack artifact:

1. Confirm T1 completion review exists at
   `docs/reviews/CVF_T1_CAPABILITY_INTAKE_PIPELINE_COMPLETION_2026-05-22.md`
   with status `CLOSED_T1_INTAKE_PIPELINE_AND_REFERENCE_PACK`. If T1 is
   not closed, stop and report; do not proceed.
2. Confirm the eight schemas exist under `governance/schemas/skill-pack/`
   and the validator runs (`python scripts/validate_skill_pack_certification.py
   --help` or equivalent). If schemas or validator are missing, stop and
   report.
3. Confirm `_certified/` directory exists (created by T1). If it does
   not exist, stop and report — T1 must be closed first.
4. Confirm `governance/registries/` directory exists or can be created
   without conflict.
5. GC-023 pre-flight: new pack artifact JSON files should target under
   100 lines each. New pack markdown files should target under 200 lines
   each. The registry JSON should target under 300 lines.

---

## Execution Plan

T2 executes in nine sequential steps S-01 → S-09. Each step must
complete and produce its named artifact before the next step begins. If
any step fails verification, the Return-to-Orchestrator conditions apply.

## Implementation Steps

### S-01 — Confirm T1 pre-condition

Read T1 completion review. Confirm:
- Status is `CLOSED_T1_INTAKE_PIPELINE_AND_REFERENCE_PACK`.
- Eight schemas exist under `governance/schemas/skill-pack/`.
- Validator script exists at `scripts/validate_skill_pack_certification.py`.
- Reference pack at `_certified/strategy_analysis/` PASSes the validator.

If any check fails, file a return note and stop.

### S-02 — File GC-018 baseline

Create `docs/baselines/CVF_GC018_T2_PRODUCT_SKILL_PACK_MVP_2026-05-22.md`
declaring:

- Pre-condition: T1 closed (cite completion review path and status).
- Scope locked to write ownership above.
- Blocked-work classes touched: none.
- No override required.
- Acceptance criteria copied verbatim from V2 roadmap T2.
- Forbidden actions: any out-of-scope item from this work order.

### S-03 — Author six new packs

For each of the six new packs below, create a directory under
`EXTENSIONS/CVF_v1.5.2_SKILL_LIBRARY_FOR_END_USERS/_certified/<pack>/`
and populate it with eight artifacts plus a `README.md`:

| Pack | Domain | Risk level | Primary outcome |
| --- | --- | --- | --- |
| `product_brief` | product | R1 | Structured product brief document |
| `sop_generator` | operations | R1 | Standard operating procedure document |
| `proposal_writer` | business | R1 | Structured proposal document |
| `meeting_summarizer` | productivity | R0 | Meeting summary with action items |
| `contract_review` | legal | R2 | Contract review report with risk flags |
| `landing_page_builder` | marketing | R1 | Landing page copy and structure |

For each pack, the eight artifacts are:

- `skill.meta.json` — name, version, domain, difficulty, cvfVersion,
  description, provenance (all required fields per T1 schema).
- `risk.profile.json` — riskLevel (use table above), riskFactors[],
  mitigations[] (per T1 schema).
- `authority.scope.json` — allowedRoles[], allowedPhases[],
  authorityScope, autonomyMode (per T1 schema).
- `execution.boundary.json` — requiredInputs[], forbiddenActions[],
  auditHooks[], stopConditions[] (per T1 schema).
- `receipt.schema.json` — bindsTo must be the literal string
  `GovernanceEvidenceReceipt`; fieldsObserved[] must list only fields
  that already exist on the receipt envelope (per T1 schema). Do not
  propose new receipt fields here.
- `workflow.binding.json` — outcomeKey (must match one of the six
  outcomes in V2 roadmap T3), composedFrom[], policyRefs[] (per T1
  schema).
- `workflow.spec.md` — inputContract section, outputContract section,
  deterministicFixturePath pointer (per T1 schema; markdown).
- `failure.recovery.md` — failureModes[] section, recoveryActions[]
  section, rollbackPolicy section (per T1 schema; markdown).
- `README.md` — one-paragraph provenance note; name the primary source
  used to derive the pack content.

Content must be substantive and derived from the stated pack domain.
Pack content must not be placeholder text.

### S-04 — Run validator on all six new packs

Execute the T1 validator against each of the six new packs:

```bash
python scripts/validate_skill_pack_certification.py \
  EXTENSIONS/CVF_v1.5.2_SKILL_LIBRARY_FOR_END_USERS/_certified/product_brief
python scripts/validate_skill_pack_certification.py \
  EXTENSIONS/CVF_v1.5.2_SKILL_LIBRARY_FOR_END_USERS/_certified/sop_generator
python scripts/validate_skill_pack_certification.py \
  EXTENSIONS/CVF_v1.5.2_SKILL_LIBRARY_FOR_END_USERS/_certified/proposal_writer
python scripts/validate_skill_pack_certification.py \
  EXTENSIONS/CVF_v1.5.2_SKILL_LIBRARY_FOR_END_USERS/_certified/meeting_summarizer
python scripts/validate_skill_pack_certification.py \
  EXTENSIONS/CVF_v1.5.2_SKILL_LIBRARY_FOR_END_USERS/_certified/contract_review
python scripts/validate_skill_pack_certification.py \
  EXTENSIONS/CVF_v1.5.2_SKILL_LIBRARY_FOR_END_USERS/_certified/landing_page_builder
```

All six must return exit code 0 and PASS on all eight artifacts. Any
FAIL triggers Return-to-Orchestrator.

### S-05 — Run validator on T1 reference pack (regression check)

Execute the validator on `_certified/strategy_analysis/` to confirm the
T1 reference pack still PASSes after the new packs are added (no
accidental schema regression). Expected: PASS, exit code 0.

### S-06 — Author registry

Create `governance/registries/cvf-certified-skill-pack-registry.json`:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "registryVersion": "1.0.0",
  "lastUpdated": "2026-05-22",
  "certifiedPacks": [
    {
      "id": "strategy_analysis",
      "path": "EXTENSIONS/CVF_v1.5.2_SKILL_LIBRARY_FOR_END_USERS/_certified/strategy_analysis",
      "domain": "business",
      "riskLevel": "R1",
      "status": "certified",
      "certifiedAt": "2026-05-22",
      "tranche": "T1_reference"
    },
    { "id": "product_brief", ... },
    { "id": "sop_generator", ... },
    { "id": "proposal_writer", ... },
    { "id": "meeting_summarizer", ... },
    { "id": "contract_review", ... },
    { "id": "landing_page_builder", ... }
  ]
}
```

Each entry requires: `id`, `path`, `domain`, `riskLevel`, `status`
(`"certified"`), `certifiedAt` (date), `tranche` (`"T2"` for the six
new packs; `"T1_reference"` for strategy_analysis).

### S-07 — Governance hook chain

Run:

```bash
python governance/compat/check_markdown_structural_completeness.py --base HEAD --head HEAD --enforce
python governance/compat/check_governed_file_size.py --enforce
```

Both must report COMPLIANT.

### S-08 — File completion review

Create
`docs/reviews/CVF_T2_PRODUCT_SKILL_PACK_MVP_COMPLETION_2026-05-22.md`
including:

- Memory class FULL_RECORD, status `CLOSED_T2_PRODUCT_SKILL_PACK_MVP`.
- Authority chain citing V2 roadmap, T1 completion review, GC-018
  baseline, and this work order.
- Evidence trace block: validator stdout for all seven packs (six new +
  one T1 regression), hook chain results.
- Findings: PASS or FAIL per acceptance criterion.
- Risk / corrective action.
- Claim boundary copied from V2 roadmap T2.

### S-09 — Update active session and commit

Update in this order:

1. `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` — update T2 entry status to
   `CLOSED_T2_PRODUCT_SKILL_PACK_MVP` with `completionPath` and
   `baselinePath`.
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json` — add `t2ProductSkillPackMvp`
   field with closure summary; update `lastUpdated`; do not change
   `currentMode` or `freezePosture`.
3. `AGENT_HANDOFF_V11_2026-05-21.md` — append GC-020 sync entry citing
   the closure commit SHA.

Single commit message:

```text
feat(t2): close product skill pack MVP — 7 certified packs + registry

Authority: docs/roadmaps/CVF_REVIEW_CVF_PAIN_POINT_DELIVERY_GAP_ROADMAP_V2_2026-05-22.md
GC-018: docs/baselines/CVF_GC018_T2_PRODUCT_SKILL_PACK_MVP_2026-05-22.md
Completion: docs/reviews/CVF_T2_PRODUCT_SKILL_PACK_MVP_COMPLETION_2026-05-22.md

Closes T2 from the Review-CVF pain-point delivery gap roadmap V2:
- 6 new certified packs: product_brief, sop_generator, proposal_writer,
  meeting_summarizer, contract_review, landing_page_builder
- Each pack: 8 artifacts validated against T1 schemas (PASS all)
- T1 reference pack regression check: PASS
- Certified skill pack registry at governance/registries/

Boundary: packs + registry only. No UI change, no runtime change,
no receipt envelope change, no workflow composition, no live provider
call, no public-sync update.
```

---

## Evidence Requirements

Every closure claim in the T2 completion review must be backed by:

- Validator stdout for each of the seven packs (six new + T1
  regression check), captured verbatim.
- Output of `check_markdown_structural_completeness.py --enforce`.
- Output of `check_governed_file_size.py --enforce`.
- Local governance hook chain pre-commit and pre-push results.
- The closure commit SHA.

No live provider call, no network request, no release-gate output is
required for T2 evidence.

---

## Acceptance Criteria

Closure requires **all** of:

1. GC-018 baseline filed and cited; T1 pre-condition confirmed therein.
2. All six new packs created with eight artifacts each.
3. All seven packs (six new + T1 reference) PASS the T1 validator
   (exit code 0, all eight artifacts PASS per pack).
4. Registry JSON filed with seven entries; `status: "certified"` for
   all.
5. No file outside write ownership modified.
6. `GovernanceEvidenceReceipt` shape unchanged.
7. No workflow composition, no UI change, no receipt envelope change,
   no live provider call.
8. Markdown structural completeness: COMPLIANT.
9. File size guard: COMPLIANT.
10. Local governance hook chain: PASS (pre-commit and pre-push).
11. Completion review filed with all required sections.
12. Active queue, active state, and handoff updated with the closure
    commit SHA.

---

## Review Gate

Before commit (step S-09), Codex acting in Reviewer role must
independently confirm:

1. No file outside the declared write ownership has been modified.
2. `GovernanceEvidenceReceipt` shape is unchanged.
3. All seven packs PASS the T1 validator (no FAIL artifacts).
4. The registry contains exactly seven entries with `status: "certified"`.
5. No file under `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/` was
   modified.
6. No file under `EXTENSIONS/CVF_MODEL_GATEWAY/` was modified.
7. No live provider call was made during T2 execution.
8. None of the active session state blocked-work classes is touched.

If any review gate item fails, do not commit; trigger
Return-to-Orchestrator instead.

---

## Closure Checklist

Before the auditor marks T2 closed, all of these must be ticked off in
the completion review:

- [ ] T1 pre-condition confirmed (T1 completion review status CLOSED,
      schemas exist, validator runs).
- [ ] GC-018 baseline filed at the expected path.
- [ ] Six new certified packs created, each with eight artifacts.
- [ ] All seven packs PASS the T1 validator (exit 0, all artifacts PASS).
- [ ] Registry JSON filed with seven entries.
- [ ] No `GovernanceEvidenceReceipt` change.
- [ ] Markdown structural completeness gate: COMPLIANT.
- [ ] Governed file size guard: COMPLIANT.
- [ ] Local governance hook chain pre-commit: PASS.
- [ ] Local governance hook chain pre-push: PASS.
- [ ] Active review queue updated with T2 closure status.
- [ ] Active session state updated with `t2ProductSkillPackMvp` field.
- [ ] Handoff updated with GC-020 sync entry and closure SHA.
- [ ] Completion review filed at the expected path with all required
      sections.

---

## Operator Checkpoint

Operator authorized T2 dispatch on 2026-05-22 by directing the creation
of this work order from V2 roadmap. No further operator checkpoint is
required during T2 execution because T2 carries no blocked-work override.

T2 has one external dependency: T1 must be closed before any T2 pack
artifact is created. If Codex is executing T1 → T2 sequentially without
operator check-in, the Orchestrator role must verify T1 closure before
proceeding.

If T2 encounters a Return-to-Orchestrator condition, the operator must
be consulted before the work order is reopened with a revised scope.

---

## Return-to-Orchestrator Conditions

Return this work order to the Orchestrator (do not close) if **any**:

- T1 is not closed when T2 begins.
- A pack cannot be populated with substantive content without modifying
  the source markdown or an out-of-scope file.
- Any pack FAIL on the T1 validator that cannot be resolved by fixing
  the pack artifact itself (i.e., a schema defect in T1 is suspected).
- Any acceptance criterion fails and the cause is unclear within
  bounded debug time.
- Any out-of-scope file change would be necessary to make T2 close.

When returning, file a return note at
`docs/reviews/CVF_T2_PRODUCT_SKILL_PACK_MVP_RETURN_2026-05-22.md`
naming the blocker and the smallest scope that would unblock T2.

---

## Forbidden Patterns (Anti-Pattern Guardrails from V2)

T2 closure must not occur via any of:

- **Closure by rejection alone.** T2 cannot close by arguing a pack
  duplicates an existing skill markdown.
- **Closure by scope redefinition.** T2 cannot close by reducing the
  seven packs to fewer.
- **Contract-only closure.** T2 cannot close by delivering a registry
  JSON without the underlying pack artifacts validated.
- **Implicit scope inflation.** T2 cannot quietly add packs beyond the
  seven named. Any addition requires a fresh GC-018 amendment.

---

## Claim Boundary

This work order authorizes only the construction of:

- Six new certified packs under `_certified/`.
- The certified skill pack registry.
- The GC-018 baseline, completion review, and active-session updates.

It does not authorize any UI integration, any workflow composition, any
receipt envelope change, any provider method contract, any memory wiring,
any live provider call, any public-sync update, any release claim, any
freeze lift, or any Maika/child-data/photo/vision claim.
