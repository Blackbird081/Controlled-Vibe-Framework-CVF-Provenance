# Work Order — HN1: Template-Skill Linkage Exemption (Fast-Lane under GC-024)

Memory class: FULL_RECORD

Status: CLOSED

docType: work_order

Worker role: Codex (Implementer)

Orchestrator: Claude

Date dispatched: 2026-05-20

Predecessor:

- `docs/roadmaps/CVF_POST_PAIN_POINT_CLOSURE_HARDENING_ROADMAP_2026-05-20.md` (REBUTTAL_FILED_NON_BLOCKING_WITH_SCOPE_REFINEMENT)
- `docs/reviews/CVF_POST_PAIN_POINT_CLOSURE_HARDENING_ROADMAP_CLAUDE_REBUTTAL_2026-05-20.md` (Claude verdict on HN1: NON_BLOCKING_AS_FAST_LANE_HYGIENE — collapse to single Fast-Lane audit)
- `CLAUDE.md` GC-024 BINDING rule (catalog and linkage hygiene)
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/data/skill-template-map.json` (current 58-entry templateToSkillMap)
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates/{business,technical,content,research,marketing,product,security,development,hr}.ts` (60 top-level Template IDs)

Authority chain: Claude rebuttal on HN1 collapsed the candidate from a
full multi-step roadmap into a single Fast-Lane audit under GC-024
catalog hygiene. No GC-018 is required. Operator approval is sufficient.

---

## Purpose

Resolve the only template-skill linkage coverage gap currently present in
the cvf-web template catalog by deciding the disposition of exactly two
unmapped Template IDs (`individual_skills_folder`, `vibe_workflow_folder`),
optionally codifying a `_folder` non-skill-surface convention, and
recording a Fast-Lane audit packet so future agents do not regenerate the
stale "118 unlinked templates" claim.

This work order is documentation/policy maintenance only. It does NOT
deliver new code, new tests, new skill content, new template content, new
runtime behavior, or new governance semantics.

---

## Scope / Target / Owner Boundary

In scope:

- Read and decide the disposition class for the two unmapped Template IDs:
  - `individual_skills_folder`
  - `vibe_workflow_folder`
- Apply exactly one of the three allowed classes per ID:
  - `map` — link to an existing skill in
    `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/public/data/skills-index.json`
  - `exempt` — record an explicit non-skill-surface reason
  - `retire` — remove the template definition (only if the template is
    unreachable from the wizard UI; verify before retiring)
- Update `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/data/skill-template-map.json`
  by adding an `exemptTemplateIds` section if any ID is classified as
  `exempt`. Schema:
  ```json
  "exemptTemplateIds": {
    "<templateId>": {
      "reason": "<one short sentence>",
      "exemptedAt": "2026-05-20",
      "exemptedBy": "HN1 Fast-Lane audit"
    }
  }
  ```
- If both IDs end in `_folder` and both are classified as `exempt`,
  optionally record the convention rule "templates whose ID ends in
  `_folder` are non-skill surfaces by convention" in the same JSON file
  under a new `linkagePolicy` key (string field). This convention is
  optional — Operator decides during the audit.
- File the Fast-Lane audit packet at
  `docs/audits/CVF_FAST_LANE_HN1_TEMPLATE_LINKAGE_EXEMPTION_2026-05-20.md`
  (governance repo).
- Add no other code, test, or content changes.

Out of scope (forbidden):

- Adding any new template definition.
- Adding any new skill definition.
- Modifying any `.ts` file under `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates/`.
- Modifying any file under `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/public/data/`.
- Modifying any runtime route, guard, registry, or hook file.
- Reopening N3 dead-reference framing.
- Public-sync push or public catalog update from this tranche unless
  Operator separately approves the `_folder` convention publication.
- Reopening any A–H Review-CVF pain point.
- Filing GC-018.
- Modifying the public-sync `.gitignore`.

Owner boundary:

- This work order touches only the governance repo.
- It modifies at most one JSON file
  (`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/data/skill-template-map.json`)
  and creates two new docs (audit packet + closure review).

---

## Per-ID Decision Table (must be filled in audit packet)

| Template ID | Suggested class | Required evidence |
| --- | --- | --- |
| `individual_skills_folder` | `exempt` (likely) | Confirm the template renders a folder-navigation surface, not a wizard. Source: `src/lib/templates/*.ts` definition + any caller in `src/components/` or `src/app/`. |
| `vibe_workflow_folder` | `exempt` (likely) | Confirm the template renders a workflow-folder surface, not a wizard. Source: same as above. |

If either ID is classified as `map`:

- The target skill ID must exist in `skills-index.json` (verify with grep).
- Add the mapping under `templateToSkillMap` with the existing schema
  shape (`domain` + `skillId`).

If either ID is classified as `retire`:

- Confirm the template is unreachable from the wizard UI (grep for the
  ID in `src/components/`, `src/app/`, and any wizard or
  template-selection surface).
- Out of scope: actual retirement (deletion of the template definition)
  belongs to a separate work order. This tranche only records the
  decision, NOT the deletion.

---

## Deliverables

### Step HN1.1 — Pre-Flight Inventory Verification

Confirm Claude's verified inventory still holds at HEAD:

1. Run a static scan of `src/lib/templates/{business,technical,content,research,marketing,product,security,development,hr}.ts` and count top-level Template IDs.
2. Read `skill-template-map.json` and count `templateToSkillMap` entries.
3. Compute the difference set: defined IDs minus mapped IDs.

Expected (per Claude rebuttal): 60 defined / 58 mapped / 2 unmapped /
0 mapped-but-undefined. The 2 unmapped IDs must be exactly
`individual_skills_folder` and `vibe_workflow_folder`.

If the inventory does NOT match, stop and return to Orchestrator. Do NOT
file an audit packet against a different inventory.

Record the inventory in the audit packet under "Pre-Flight Inventory
Verification".

### Step HN1.2 — Per-ID Disposition Decision

For each of the two unmapped IDs:

1. Locate the template definition in `src/lib/templates/*.ts`.
2. Read the definition's `category`, `name`, `description`, and any
   visible UI flags.
3. Grep for the ID across `src/components/`, `src/app/`, and any
   wizard / selector surface to verify reachability.
4. Choose one disposition class: `map`, `exempt`, or `retire`.
5. Record the choice + evidence in the audit packet under
   "Per-ID Disposition Table".

If a third unmapped ID is discovered, stop and return to Orchestrator —
this work order is scoped to exactly two IDs.

### Step HN1.3 — Apply Exemption Schema (only if any ID is `exempt`)

If at least one ID is classified as `exempt`:

1. Open `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/data/skill-template-map.json`.
2. Add a top-level key `exemptTemplateIds` (object) with one sub-object
   per exempted ID using the schema in the In-scope section above.
3. If both IDs end in `_folder` AND both are exempted AND Operator
   approves the convention during the audit, add a top-level key
   `linkagePolicy` with the value:
   `"templates whose ID ends in '_folder' are non-skill surfaces by convention; record an exemption per ID in exemptTemplateIds"`.
4. Do NOT change any existing keys. Do NOT reorder existing entries.
5. Validate the JSON parses cleanly after the edit (e.g.,
   `python -c "import json; json.load(open('...'))"`).

If neither ID is `exempt`, skip Step HN1.3.

### Step HN1.4 — Fast-Lane Audit Packet

File: `docs/audits/CVF_FAST_LANE_HN1_TEMPLATE_LINKAGE_EXEMPTION_2026-05-20.md`

Required sections (per `docs/reference/CVF_FAST_LANE_AUDIT_TEMPLATE.md`):

- Purpose
- Source / Predecessor Evidence
- Scope (exactly two ID decisions, optional convention)
- Pre-Flight Inventory Verification (the Step HN1.1 table)
- Per-ID Disposition Table (the Step HN1.2 result)
- JSON Edit Summary (if Step HN1.3 ran; show the added key block
  verbatim)
- Risk Classification (R0, JSON schema additive change)
- Decision / Disposition
- Claim Boundary

The audit packet must explicitly:

- Cite GC-024 BINDING rule + Claude rebuttal as the authorization for
  skipping GC-018.
- Confirm no source code, test, route, guard, or skill content was
  modified.
- Confirm the 118-template figure from earlier Claude notes is
  retracted; the verified inventory is 60/58/2/0.

### Step HN1.5 — Closure Review

File: `docs/reviews/CVF_HN1_TEMPLATE_LINKAGE_EXEMPTION_CLOSURE_REVIEW_2026-05-20.md`

Required structure: Purpose, Target, Scope/Methodology, Findings,
Decision/Disposition, Claim Boundary.

The closure review must confirm:

- Pre-flight inventory verified to match expected 60/58/2/0.
- Both unmapped IDs received a disposition decision recorded in the
  audit packet.
- If exemption schema was applied, JSON parses cleanly and only
  `skill-template-map.json` was modified.
- No code/test/runtime/skill/content change.
- No public-sync push (unless Operator separately approved the `_folder`
  convention publication, which would require a separate N1-style
  catalog tranche).
- Pre-commit and pre-push hooks PASS on the governance repo.

---

## Acceptance Criteria

All of the following must be true before this work order is CLOSED:

- [x] Pre-flight inventory matches expected 60/58/2/0 (or stop-and-return
      condition was correctly triggered).
- [x] Both unmapped IDs (`individual_skills_folder`, `vibe_workflow_folder`)
      have a disposition recorded in the audit packet.
- [x] If exemption applied: `skill-template-map.json` parses cleanly with
      `exemptTemplateIds` (and optional `linkagePolicy`) added.
- [x] Fast-Lane audit packet filed at
      `docs/audits/CVF_FAST_LANE_HN1_TEMPLATE_LINKAGE_EXEMPTION_2026-05-20.md`.
- [x] Closure review filed at
      `docs/reviews/CVF_HN1_TEMPLATE_LINKAGE_EXEMPTION_CLOSURE_REVIEW_2026-05-20.md`.
- [x] No `.ts` file modified; no skill/template content added; no runtime
      route touched.
- [x] No public-sync push.
- [x] No GC-018 filed.
- [x] No A–H pain-point reopen.
- [x] Pre-commit hook PASS (11/11).
- [x] Pre-push hook PASS (43/43).
- [x] Handoff GC-020 HEAD SHA synced after closure commit.

---

## Forbidden Actions

- Do NOT add or remove any template definition.
- Do NOT add or remove any skill definition.
- Do NOT modify any `.ts` file under `src/lib/templates/`.
- Do NOT modify `skills-index.json`.
- Do NOT touch any runtime route, guard, hook, or registry.
- Do NOT modify the public-sync repo.
- Do NOT use `git add -A` or `git add .`.
- Do NOT classify any ID as `retire` and then delete the template
  definition (deletion belongs to a separate work order).
- Do NOT discover a third unmapped ID and try to handle it — return to
  Orchestrator instead.
- Do NOT bundle HN2 or HN3 work into this tranche.
- Do NOT reopen any A–H Review-CVF pain point.
- Do NOT file GC-018.

---

## Authority Chain

- Authorized by: Claude rebuttal verdict NON_BLOCKING_AS_FAST_LANE_HYGIENE
  on HN1 candidate, 2026-05-20.
- Predecessor roadmap:
  `docs/roadmaps/CVF_POST_PAIN_POINT_CLOSURE_HARDENING_ROADMAP_2026-05-20.md`.
- Binding rule: GC-024 in `CLAUDE.md` (catalog/linkage hygiene).
- Orchestrator: Claude; Worker: Codex; Operator approval required for the
  optional `_folder` convention publication only.

---

## Agent Roles

- Worker (Codex): pre-flight inventory, per-ID disposition decision,
  optional JSON schema edit, Fast-Lane audit packet, closure review.
- Orchestrator (Claude): reviews closure review; confirms inventory
  retraction recorded; verifies no scope inflation.

---

## Required First Reads

1. `docs/reviews/CVF_POST_PAIN_POINT_CLOSURE_HARDENING_ROADMAP_CLAUDE_REBUTTAL_2026-05-20.md` —
   HN1 verdict + verified inventory + retraction note.
2. `docs/roadmaps/CVF_POST_PAIN_POINT_CLOSURE_HARDENING_ROADMAP_2026-05-20.md` —
   HN1 framing.
3. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/data/skill-template-map.json` —
   current 58-entry `templateToSkillMap`.
4. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates/index.ts` —
   aggregator import pattern.
5. The two template files that define the unmapped IDs (locate with grep
   `individual_skills_folder` and `vibe_workflow_folder`).
6. `docs/reference/CVF_FAST_LANE_AUDIT_TEMPLATE.md` — audit packet
   structural template.
7. `CLAUDE.md` GC-024 BINDING rule section.

---

## Pre-Flight Checks

- [ ] Governance repo working tree CLEAN before starting.
- [ ] Confirm audit packet path
      `docs/audits/CVF_FAST_LANE_HN1_TEMPLATE_LINKAGE_EXEMPTION_2026-05-20.md`
      does NOT yet exist.
- [ ] Confirm closure review path
      `docs/reviews/CVF_HN1_TEMPLATE_LINKAGE_EXEMPTION_CLOSURE_REVIEW_2026-05-20.md`
      does NOT yet exist.
- [ ] Confirm pre-flight inventory matches 60/58/2/0. If not, stop and
      return to Orchestrator.

---

## Write Ownership

May create only:

- `docs/audits/CVF_FAST_LANE_HN1_TEMPLATE_LINKAGE_EXEMPTION_2026-05-20.md` (new)
- `docs/reviews/CVF_HN1_TEMPLATE_LINKAGE_EXEMPTION_CLOSURE_REVIEW_2026-05-20.md` (new)

May modify only:

- `docs/work_orders/CVF_WO_HN1_TEMPLATE_LINKAGE_EXEMPTION_FAST_LANE_2026-05-20.md`
  (status/checklist closure sync only)
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/data/skill-template-map.json`
  (additive schema fields only; no removal, no reordering)
- `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` (queue item update after closure)
- `CVF_SESSION/ACTIVE_SESSION_STATE.json` (nextAllowedMove update after
  closure)
- `AGENT_HANDOFF_V10_2026-05-19.md` (status line + GC-020 HEAD SHA sync)

No other files may be created or modified in either repo.

---

## Execution Plan

1. Pre-flight checks (Section: Pre-Flight Checks).
2. Pre-flight inventory verification (Step HN1.1).
3. Per-ID disposition decision (Step HN1.2).
4. Apply exemption schema if needed (Step HN1.3).
5. File Fast-Lane audit packet (Step HN1.4).
6. File closure review (Step HN1.5).
7. Update queue + session state + handoff.
8. Commit + GC-020 sync.

---

## Evidence Requirements

- Inventory match recorded (60/58/2/0).
- Per-ID disposition table complete (2 IDs, 1 class each, evidence
  cited).
- If exemption applied: JSON parse PASS recorded.
- Audit packet cites GC-024 BINDING and Claude rebuttal as authorization.
- Closure review cites the audit packet + commit SHA.

---

## Review Gate

Stop and return to Orchestrator if:

- Pre-flight inventory does not match 60/58/2/0.
- A third unmapped ID is found.
- Either ID requires `map` and the target skill ID does NOT exist in
  `skills-index.json`.
- The Operator denies the `_folder` convention AND both IDs require
  exemption — in which case the audit must record per-ID reason only,
  not the convention.
- The exemption schema edit would touch any existing key besides adding
  the new top-level field(s).

---

## Non-Goals

- HN2 inventory or owner map.
- HN3 runtime maturity work.
- New template content.
- New skill content.
- Public-sync catalog update (unless Operator separately approves the
  convention publication).
- Reopening any A–H pain point.

---

## Work Plan

Sequential:

1. Pre-flight checks.
2. Inventory verification (Step HN1.1).
3. Per-ID disposition (Step HN1.2).
4. Optional JSON edit (Step HN1.3).
5. Audit packet (Step HN1.4).
6. Closure review (Step HN1.5).
7. Queue + session-state + handoff update.
8. Commit using HEREDOC commit message; do not amend.

If any review-gate condition fires, stop and report to Orchestrator
before proceeding.

---

## Closure Checklist

- [x] Pre-flight inventory matches 60/58/2/0.
- [x] Per-ID disposition recorded for both IDs.
- [x] JSON edits (if any) parse cleanly.
- [x] Audit packet filed.
- [x] Closure review filed.
- [x] No `.ts` modified; no skill/template content added.
- [x] No public-sync push.
- [x] No GC-018.
- [x] No A–H pain-point reopen.
- [x] Session state + handoff + queue updated.
- [x] Pre-commit + pre-push hooks PASS.

---

## Return-To-Orchestrator Conditions

Return if:

- Inventory mismatch (anything other than 60/58/2/0).
- Third unmapped ID found.
- `map` disposition required but target skill ID missing.
- JSON edit would require modifying existing keys.
- Hook failure outside this scope.

---

## Claim Boundary

This work order covers a single Fast-Lane disposition decision for two
unmapped Template IDs, an optional `_folder` convention codification,
an audit packet, and a closure review. It does not authorize new code,
new tests, new policy, new GC-018, downstream work orders, template
deletion, skill content additions, runtime changes, or public catalog
expansion. It does not preempt HN2 or HN3 and does not reopen any A–H
Review-CVF pain point.
