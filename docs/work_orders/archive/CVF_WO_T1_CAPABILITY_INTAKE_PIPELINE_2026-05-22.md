# Work Order — T1 Capability Intake Pipeline + Complete Pack Artifact Set

Memory class: FULL_RECORD

Status: READY_FOR_IMPLEMENTATION

docType: work_order

Worker role: Codex (full Orchestrator → Reviewer → Implementer → Auditor chain)

Date dispatched: 2026-05-22

---

## Purpose

Build the missing Capability Intake Pipeline and the complete eight-artifact
certification format that the 17.05 Review CVF.md named as the largest current
gap. T1 ships the contract, the eight JSON schemas, the validator, and one
reference pack ported from an existing skill markdown. T1 is contract +
validator + reference only; no runtime change, no provider call, no receipt
envelope change, no memory wiring.

This work order resolves Codex blocking Finding 1 (V1 omitted `workflow.spec`
and `failure.recovery`) by certifying all eight artifacts in V2.

---

## Authority Chain

- Active roadmap (V2):
  `docs/roadmaps/CVF_REVIEW_CVF_PAIN_POINT_DELIVERY_GAP_ROADMAP_V2_2026-05-22.md`
- Predecessor audit:
  `docs/audits/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_GAP_AUDIT_2026-05-22.md`
- Codex blocking review:
  `docs/reviews/CVF_REVIEW_CVF_PAIN_POINT_DELIVERY_GAP_ROADMAP_CODEX_REVIEW_2026-05-22.md`
- Superseded V1 roadmap:
  `docs/roadmaps/CVF_REVIEW_CVF_PAIN_POINT_DELIVERY_GAP_ROADMAP_2026-05-22.md`
- Source review (original requirement):
  `.private_reference/legacy/CVF 17.05/Review CVF.md`
- GC-018 to be filed:
  `docs/baselines/CVF_GC018_T1_CAPABILITY_INTAKE_PIPELINE_2026-05-22.md`

---

## Agent Roles

- **Orchestrator (Codex):** File GC-018 baseline before any implementation
  file is created. Confirm write ownership boundaries from this work order.
- **Reviewer (Codex):** Confirm T1 stays contract + validator + reference
  only. No runtime change, no receipt envelope change, no live provider call,
  no public-sync update. Confirm none of the blocked-work classes is touched.
- **Implementer (Codex):** Write the guard markdown, eight JSON schemas,
  validator script, and one reference pack. Run validator offline only.
- **Auditor (Codex):** Verify evidence trace block, run governance hook
  chain, file completion review, and update active queue/state/handoff.

---

## Write Ownership

See "Write ownership (in scope)" under Scope below for the complete file
list. Codex must not modify any file outside that list. Any need to
touch a file outside write ownership triggers Return-to-Orchestrator.

---

## Scope / Target / Owner Boundary

### Write ownership (in scope)

- `governance/toolkit/05_OPERATION/CVF_CAPABILITY_INTAKE_PIPELINE_GUARD.md`
  (new) — the pipeline contract as governed surface text.
- `governance/schemas/skill-pack/` (new directory) containing eight JSON
  schemas:
  - `skill.meta.schema.json`
  - `risk.profile.schema.json`
  - `authority.scope.schema.json`
  - `execution.boundary.schema.json`
  - `receipt.schema.schema.json`
  - `workflow.binding.schema.json`
  - `workflow.spec.schema.json`
  - `failure.recovery.schema.json`
- `scripts/validate_skill_pack_certification.py` (new) — validator script.
- `EXTENSIONS/CVF_v1.5.2_SKILL_LIBRARY_FOR_END_USERS/_certified/strategy_analysis/`
  (new directory) — one reference pack containing the eight required
  artifacts plus a README pointing to the source markdown.
- `docs/baselines/CVF_GC018_T1_CAPABILITY_INTAKE_PIPELINE_2026-05-22.md`
  (new) — authorization baseline.
- `docs/reviews/CVF_T1_CAPABILITY_INTAKE_PIPELINE_COMPLETION_2026-05-22.md`
  (new) — completion review.
- `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` — update T1 entry status.
- `CVF_SESSION/ACTIVE_SESSION_STATE.json` — update `lastUpdated` and
  `t1CapabilityIntakePipeline` field after closure.
- `AGENT_HANDOFF_V11_2026-05-21.md` — GC-020 sync entry.

### Out of scope (forbidden)

- Any change to `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts`
  or any route file.
- Any change to `GovernanceEvidenceReceipt` shape.
- Any live provider call. T1 is offline-only.
- Any change to existing skill markdown files in
  `EXTENSIONS/CVF_v1.5.2_SKILL_LIBRARY_FOR_END_USERS/business_analysis/`
  (port reads from, does not modify).
- Any change to provider adapters, route, persistence, or memory wiring.
- Any change to existing audit-memory readout.
- Public-sync repository update.
- Maika, child-data, photo, or vision proof.
- Workflow composition engine (that is T3).
- Outcome quick action expansion (that is T3).
- Additional certified packs beyond the single reference (those are T2).

### Owner boundary

Codex executes Orchestrator → Reviewer → Implementer → Auditor in a single
session. Operator authorization is the GC-018 baseline filed at dispatch
time.

---

## Required First Reads

- `docs/roadmaps/CVF_REVIEW_CVF_PAIN_POINT_DELIVERY_GAP_ROADMAP_V2_2026-05-22.md`
- `docs/audits/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_GAP_AUDIT_2026-05-22.md`
- `docs/reviews/CVF_REVIEW_CVF_PAIN_POINT_DELIVERY_GAP_ROADMAP_CODEX_REVIEW_2026-05-22.md`
- `.private_reference/legacy/CVF 17.05/Review CVF.md` (lines 466–525 for
  capability intake; lines 500–508 for the artifact list)
- `EXTENSIONS/CVF_v1.5.2_SKILL_LIBRARY_FOR_END_USERS/SKILL_TEMPLATE.md`
- `EXTENSIONS/CVF_v1.5.2_SKILL_LIBRARY_FOR_END_USERS/business_analysis/01_strategy_analysis.skill.md`
  (the source for the reference port)
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts`
  (read-only — to confirm receipt envelope shape is not changed)
- `governance/toolkit/05_OPERATION/CVF_GOVERNED_FILE_SIZE_GUARD.md`
- `docs/reference/CVF_MARKDOWN_STRUCTURAL_COMPLETENESS_STANDARD.md`

---

## Pre-Flight Checks

Before writing any implementation file:

1. Confirm the V2 roadmap is committed at the project HEAD and cited by
   the GC-018 baseline.
2. Confirm the predecessor audit and Codex blocking review are committed
   and citable.
3. Confirm `governance/schemas/` directory exists or can be created
   without conflict. If a `governance/schemas/` directory already exists
   with unrelated content, place skill-pack schemas under a clearly named
   `skill-pack/` subdirectory.
4. Confirm `_certified/` directory does not yet exist under the skill
   library extension. If it does (unlikely), report back before
   proceeding.
5. GC-023 pre-flight: no file under write ownership should exceed its
   class threshold. New files are unconstrained but should aim for
   under 500 lines per JSON schema and under 600 lines for the guard
   markdown.

---

## Execution Plan

T1 executes in eleven sequential steps S-01 → S-11 below. Each step
must complete and produce its named artifact before the next step
begins. If any step fails verification, the Return-to-Orchestrator
conditions below apply.

## Implementation Steps

### S-01 — File GC-018 baseline

Create `docs/baselines/CVF_GC018_T1_CAPABILITY_INTAKE_PIPELINE_2026-05-22.md`
declaring:

- Scope locked to write ownership above.
- Blocked-work classes touched: none.
- No override required.
- Acceptance criteria copied verbatim from V2 roadmap T1.
- Forbidden actions: any out-of-scope item from this work order.

### S-02 — Author the pipeline guard

Create `governance/toolkit/05_OPERATION/CVF_CAPABILITY_INTAKE_PIPELINE_GUARD.md`
defining:

- The pipeline: intake → normalization → risk audit → policy binding →
  certification → workflow mapping → governed runtime.
- The eight per-pack artifacts required for certification.
- Boundary: T1 covers contract and validator only; runtime governed
  execution is downstream.
- Reference to V2 roadmap as authority.

### S-03 — Author eight JSON schemas

For each artifact, create a JSON Schema Draft 2020-12 file under
`governance/schemas/skill-pack/`:

| File | Required fields (minimum) |
| --- | --- |
| `skill.meta.schema.json` | `name`, `version`, `domain`, `difficulty`, `cvfVersion`, `description`, `provenance` |
| `risk.profile.schema.json` | `riskLevel` (R0–R3), `riskFactors[]`, `mitigations[]` |
| `authority.scope.schema.json` | `allowedRoles[]`, `allowedPhases[]`, `authorityScope`, `autonomyMode` |
| `execution.boundary.schema.json` | `requiredInputs[]`, `forbiddenActions[]`, `auditHooks[]`, `stopConditions[]` |
| `receipt.schema.schema.json` | `bindsTo` (must be the string literal `GovernanceEvidenceReceipt`), `fieldsObserved[]` |
| `workflow.binding.schema.json` | `outcomeKey`, `composedFrom[]`, `policyRefs[]` |
| `workflow.spec.schema.json` | `inputContract`, `outputContract`, `deterministicFixturePath` |
| `failure.recovery.schema.json` | `failureModes[]`, `recoveryActions[]`, `rollbackPolicy` |

Each schema must declare `$schema`, `$id`, `title`, `type: "object"`,
`required`, and `additionalProperties: false`.

### S-04 — Author validator script

Create `scripts/validate_skill_pack_certification.py`:

- Accepts a positional directory argument (the candidate pack directory).
- Loads all eight schemas from `governance/schemas/skill-pack/`.
- For each expected artifact filename, validates against its schema.
- Emits a deterministic JSON result to stdout:

  ```json
  {
    "pack": "<dir>",
    "result": "PASS",
    "artifacts": [
      { "name": "skill.meta.json", "result": "PASS" },
      { "name": "workflow.spec.md", "result": "FAIL", "reason": "..." }
    ]
  }
  ```
- Exit code 0 on PASS, exit code 1 on FAIL.
- No network call. No live provider call. No external HTTP.
- Pure Python stdlib + `jsonschema` if already available; if not, declare
  the dependency and stop, do not silently install.

### S-05 — Port reference pack

Create
`EXTENSIONS/CVF_v1.5.2_SKILL_LIBRARY_FOR_END_USERS/_certified/strategy_analysis/`
with eight artifacts:

- `skill.meta.json`
- `risk.profile.json`
- `authority.scope.json`
- `execution.boundary.json`
- `receipt.schema.json`
- `workflow.binding.json`
- `workflow.spec.md` (markdown with required structural sections)
- `failure.recovery.md` (markdown with required structural sections)
- `README.md` (provenance pointer to
  `business_analysis/01_strategy_analysis.skill.md`)

Content must be derived from the existing `01_strategy_analysis.skill.md`
governance block. Receipt schema must bind to the existing
`GovernanceEvidenceReceipt` shape without proposing any envelope change.

### S-06 — Run validator on reference pack

Execute the validator against the reference pack. Expected: PASS on all
eight artifacts, exit code 0.

### S-07 — Run negative tests

For each of the eight artifacts, create a deliberate violation copy in a
temp directory (do not commit), run the validator, and confirm each
violation produces a distinct named rejection reason. Record the eight
distinct reason strings in the completion review.

### S-08 — Governance hook chain

Run:

```bash
python governance/compat/check_markdown_structural_completeness.py --base HEAD --head HEAD --enforce
python governance/compat/check_governed_file_size.py --enforce
```

Both must report COMPLIANT.

### S-09 — File completion review

Create
`docs/reviews/CVF_T1_CAPABILITY_INTAKE_PIPELINE_COMPLETION_2026-05-22.md`
including:

- Memory class FULL_RECORD, status `CLOSED_T1_INTAKE_PIPELINE_AND_REFERENCE_PACK`.
- Authority chain citing the V2 roadmap, audit, Codex review, GC-018
  baseline, and this work order.
- Evidence trace block: validator stdout for reference pack, validator
  stderr for each negative test, hook chain results.
- Findings: PASS or FAIL per acceptance criterion.
- Risk / corrective action.
- Claim boundary copied from V2 roadmap T1.

### S-10 — Update active session

Update in this order:

1. `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` — add T1 entry as
   `CLOSED_T1_INTAKE_PIPELINE_AND_REFERENCE_PACK` with `completionPath`
   and `baselinePath` pointing at the filed artifacts.
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json` — add
   `t1CapabilityIntakePipeline` field with the closure summary; update
   `lastUpdated`; do not change `currentMode` or `freezePosture`.
3. `AGENT_HANDOFF_V11_2026-05-21.md` — append GC-020 sync entry citing
   the closure commit SHA.

### S-11 — Commit

Single commit message:

```text
feat(t1): close capability intake pipeline contract and reference pack

Authority: docs/roadmaps/CVF_REVIEW_CVF_PAIN_POINT_DELIVERY_GAP_ROADMAP_V2_2026-05-22.md
GC-018: docs/baselines/CVF_GC018_T1_CAPABILITY_INTAKE_PIPELINE_2026-05-22.md
Completion: docs/reviews/CVF_T1_CAPABILITY_INTAKE_PIPELINE_COMPLETION_2026-05-22.md

Closes T1 from the Review-CVF pain-point delivery gap roadmap V2:
- Capability Intake Pipeline guard
- 8 JSON schemas under governance/schemas/skill-pack/
- Validator script scripts/validate_skill_pack_certification.py
- Reference pack ported from strategy_analysis skill markdown
- Validator PASS on reference pack, distinct rejection reason per artifact
  on negative tests

Boundary: contract + validator + reference pack only. No runtime change,
no provider call, no receipt envelope change, no memory wiring, no
public-sync update, no UI change.
```

---

## Evidence Requirements

Every closure claim in the T1 completion review must be backed by an
evidence trace block citing:

- Validator stdout for the reference pack (captured verbatim).
- Validator stderr (or rejection JSON) for each of the eight negative
  tests (captured verbatim).
- Output of `python governance/compat/check_markdown_structural_completeness.py --base HEAD --head HEAD --enforce`.
- Output of `python governance/compat/check_governed_file_size.py --enforce`.
- Local governance hook chain pre-commit and pre-push results.
- The eight distinct negative-test rejection reason strings.
- The closure commit SHA.

No live provider call, no network request, no release-gate output is
required for T1 evidence.

---

## Acceptance Criteria

Closure requires **all** of:

1. GC-018 baseline filed and cited.
2. Pipeline guard markdown filed with required structural sections.
3. All eight JSON schemas filed; each declares
   `additionalProperties: false`.
4. Validator script filed, runs offline, returns deterministic JSON,
   exits 0 on PASS, 1 on FAIL.
5. Reference pack PASSes validator (eight artifacts PASS, exit 0).
6. Eight distinct negative-test rejection reasons recorded in completion
   review.
7. No file outside write ownership modified.
8. `GovernanceEvidenceReceipt` shape unchanged.
9. Markdown structural completeness: COMPLIANT.
10. File size guard: COMPLIANT.
11. Local governance hook chain: PASS (pre-commit and pre-push).
12. Completion review filed with all required sections.
13. Active queue, active state, and handoff updated with the closure
    commit SHA.

---

## Review Gate

Before commit (step S-11), Codex acting in Reviewer role must
independently confirm:

1. No file outside the declared write ownership has been modified.
2. `GovernanceEvidenceReceipt` shape is unchanged (no field added,
   removed, or retyped).
3. No new dependency was introduced into the project Python environment
   beyond what was already installed.
4. The reference pack content is derived from the source markdown only
   and does not introduce new governance semantics.
5. No file under `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/` was
   modified.
6. No file under `EXTENSIONS/CVF_MODEL_GATEWAY/` was modified.
7. No file under any provider adapter, route, or audit-memory module
   was modified.
8. None of the active session state blocked-work classes is touched.

If any review gate item fails, do not commit; trigger
Return-to-Orchestrator instead.

---

## Closure Checklist

Before the auditor marks T1 closed, all of these must be ticked off in
the completion review:

- [ ] GC-018 baseline filed at the expected path.
- [ ] All eight JSON schemas filed with `additionalProperties: false`.
- [ ] Validator script filed and runs offline (`python scripts/validate_skill_pack_certification.py <path>`).
- [ ] Reference pack PASSes validator (exit 0, all eight artifacts PASS).
- [ ] Eight distinct negative-test rejection reasons recorded.
- [ ] Pipeline guard markdown filed with required structural sections.
- [ ] Markdown structural completeness gate: COMPLIANT.
- [ ] Governed file size guard: COMPLIANT.
- [ ] Local governance hook chain pre-commit: PASS.
- [ ] Local governance hook chain pre-push: PASS.
- [ ] Active review queue updated with T1 closure status.
- [ ] Active session state updated with `t1CapabilityIntakePipeline` field.
- [ ] Handoff updated with GC-020 sync entry and closure SHA.
- [ ] Completion review filed at the expected path with all required
      sections.

---

## Operator Checkpoint

Operator authorized T1 dispatch on 2026-05-22 by directing the creation
of this work order from V2 roadmap. No further operator checkpoint is
required during T1 execution because T1 carries no blocked-work
override.

If T1 encounters a Return-to-Orchestrator condition, the operator must
be consulted before the work order is reopened with a revised scope.

---

## Return-to-Orchestrator Conditions

Return this work order to the Orchestrator (do not close) if **any**:

- The reference pack cannot be ported cleanly from the source markdown
  without modifying the source.
- A required schema cannot be satisfied by content derived from the
  source markdown alone.
- The validator requires a dependency (e.g., `jsonschema`) that is not
  already installed in the project Python environment.
- Any acceptance criterion fails and the cause is unclear within
  bounded debug time.
- Any out-of-scope file change would be necessary to make T1 close.

When returning, file a return note at
`docs/reviews/CVF_T1_CAPABILITY_INTAKE_PIPELINE_RETURN_2026-05-22.md`
naming the blocker and the smallest scope that would unblock T1.

---

## Forbidden Patterns (Anti-Pattern Guardrails from V2)

T1 closure must not occur via any of:

- **Closure by rejection alone.** T1 cannot close by arguing one or more
  artifacts duplicate an existing surface. T1 is scoped to build them.
- **Closure by scope redefinition.** T1 cannot close by removing
  artifacts from the required eight.
- **Implicit scope inflation.** T1 cannot quietly add work beyond write
  ownership. Any addition requires a fresh GC-018 amendment.

T1 is **explicitly exempt** from the "contract-only closure" prohibition
because V2 scopes T1 as contract + validator + reference. Downstream
tranches (T2–T5) carry the runtime delivery.

---

## Claim Boundary

This work order authorizes only the construction of:

- The capability intake pipeline guard.
- The eight JSON schemas.
- The validator script.
- One reference pack.
- The GC-018 baseline, completion review, and active-session updates.

It does not authorize any runtime change, any receipt envelope change,
any provider semantics change, any memory wiring, any UI change, any
live provider call, any public-sync update, any release claim, any
freeze lift, or any Maika/child-data/photo/vision claim.
