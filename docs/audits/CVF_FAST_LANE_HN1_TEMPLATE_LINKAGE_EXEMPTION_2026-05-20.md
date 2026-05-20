# CVF Fast Lane HN1 Template Linkage Exemption Audit

Memory class: FULL_RECORD

Status: FAST_LANE_READY_CLOSED

docType: audit

Date: 2026-05-20

---

## Purpose

Record the Fast-Lane disposition for the two currently unmapped template IDs
in the cvf-web template catalog and prevent the stale "118 unlinked templates"
claim from regenerating future work orders.

This audit is a GC-024 catalog/linkage hygiene action. It does not add skill
content, template content, runtime behavior, public claims, or a new
governance semantic.

---

## Source / Predecessor Evidence

- `docs/roadmaps/CVF_POST_PAIN_POINT_CLOSURE_HARDENING_ROADMAP_2026-05-20.md`
- `docs/reviews/CVF_POST_PAIN_POINT_CLOSURE_HARDENING_ROADMAP_CLAUDE_REBUTTAL_2026-05-20.md`
- `docs/work_orders/CVF_WO_HN1_TEMPLATE_LINKAGE_EXEMPTION_FAST_LANE_2026-05-20.md`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/data/skill-template-map.json`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates/development.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates/governance-enforcement.test.ts`
- `CLAUDE.md` GC-024 public catalog/linkage hygiene rule

Claude's rebuttal explicitly retracted the earlier 118-template figure. The
verified current inventory is 60 top-level template IDs, 58 mapped template
IDs, 2 unmapped template IDs, and 0 mapped-but-undefined IDs.

---

## Scope

In scope:

- Decide disposition for `individual_skills_folder`.
- Decide disposition for `vibe_workflow_folder`.
- Add an `exemptTemplateIds` section to `skill-template-map.json`.

Out of scope:

- New template or skill definitions.
- Runtime, guard, route, test, or skill content changes.
- Public-sync publication.
- GC-018.
- Reopening any Review-CVF A-H pain point.

---

## Protocol / Contract / Requirements

Contract:

- Only the two IDs `individual_skills_folder` and `vibe_workflow_folder` may
  receive a disposition in this audit.
- Existing `templateToSkillMap` entries must not be removed, reordered, or
  remapped.
- Any exemption must be represented as additive metadata under
  `exemptTemplateIds`.
- The JSON file must parse after the edit.

Requirements:

- Confirm the current inventory is 60/58/2/0.
- Confirm both IDs are folder-navigation surfaces, not runnable form
  templates.
- Confirm no runtime, route, guard, test, skill markdown, or public-sync file
  is modified.

---

## Pre-Flight Inventory Verification

| Check | Result |
| --- | --- |
| Top-level template IDs from `src/lib/templates/{business,technical,content,research,marketing,product,security,development,hr}.ts` | 60 |
| `templateToSkillMap` entries in `skill-template-map.json` | 58 |
| Defined IDs minus mapped IDs | 2 |
| Mapped-but-undefined IDs | 0 |
| Unmapped IDs | `individual_skills_folder`, `vibe_workflow_folder` |

Inventory matches the work order expected state: 60/58/2/0.

---

## Per-ID Disposition Table

| Template ID | Disposition | Evidence | Rationale |
| --- | --- | --- | --- |
| `individual_skills_folder` | `exempt` | `development.ts` defines `isFolder: true`; child templates reference `parentFolder: 'individual_skills_folder'`; governance test lists it in `FOLDER_TEMPLATE_IDS`. | Folder-navigation surface, not a runnable form template; child templates carry skill mappings. |
| `vibe_workflow_folder` | `exempt` | `development.ts` defines `isFolder: true`; child templates reference `parentFolder: 'vibe_workflow_folder'`; governance test lists it in `FOLDER_TEMPLATE_IDS`. | Folder-navigation surface, not a runnable form template; child templates carry skill mappings. |

No `map` disposition was selected because neither ID represents a runnable form
template. No `retire` disposition was selected because both folder IDs are
reachable parent surfaces for child templates.

---

## JSON Edit Summary

Added this top-level block to
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/data/skill-template-map.json`:

```json
"exemptTemplateIds": {
  "individual_skills_folder": {
    "reason": "Folder-navigation surface with isFolder=true; child templates carry skill mappings.",
    "exemptedAt": "2026-05-20",
    "exemptedBy": "HN1 Fast-Lane audit"
  },
  "vibe_workflow_folder": {
    "reason": "Folder-navigation surface with isFolder=true; child templates carry skill mappings.",
    "exemptedAt": "2026-05-20",
    "exemptedBy": "HN1 Fast-Lane audit"
  }
}
```

No `linkagePolicy` convention was added because no separate operator approval
was given for publishing the `_folder` convention as a general rule.

---

## Risk Classification

Risk: R0.

Reason:

- The edit is additive JSON metadata only.
- Existing `templateToSkillMap` entries were not changed.
- No runtime file, guard, route, test, template definition, skill markdown, or
  public-sync surface was modified.
- Rollback unit is the single `exemptTemplateIds` block.

---

## Verification

Static verification:

- `skill-template-map.json` parses successfully with Python `json.load`.
- Inventory remains 60/58/2/0.
- `git diff` shows only an additive `exemptTemplateIds` JSON block for HN1
  before documentation/session updates.

Governance verification:

- Pre-commit hook is required before closure.
- Pre-push hook is required before closure.

---

## Audit Decision

FAST LANE READY.

Disposition:

- `individual_skills_folder`: exempt.
- `vibe_workflow_folder`: exempt.
- 118-template figure: retracted as stale/wrong for current HEAD.

---

## Related Artifacts

- `docs/work_orders/CVF_WO_HN1_TEMPLATE_LINKAGE_EXEMPTION_FAST_LANE_2026-05-20.md`
- `docs/reviews/CVF_HN1_TEMPLATE_LINKAGE_EXEMPTION_CLOSURE_REVIEW_2026-05-20.md`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/data/skill-template-map.json`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates/development.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates/governance-enforcement.test.ts`

---

## Claim Boundary

This audit claims only that two folder-navigation template IDs are explicitly
exempted from skill-linkage mapping. It does not claim a complete public
catalog update, runtime governance change, new skill coverage, new template
coverage, release readiness, or any Review-CVF pain-point reopening.
