# CVF HN1 Template Linkage Exemption Closure Review

Memory class: FULL_RECORD

Status: CLOSED

docType: review

Reviewer: Codex

Date: 2026-05-20

---

## Purpose

Close HN1 after applying the bounded Fast-Lane template-linkage exemption for
the two folder-navigation template IDs.

---

## Target

- Work order:
  `docs/work_orders/CVF_WO_HN1_TEMPLATE_LINKAGE_EXEMPTION_FAST_LANE_2026-05-20.md`
- Audit:
  `docs/audits/CVF_FAST_LANE_HN1_TEMPLATE_LINKAGE_EXEMPTION_2026-05-20.md`
- JSON surface:
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/data/skill-template-map.json`

---

## Scope / Methodology

Method:

1. Recomputed template-linkage inventory from current HEAD.
2. Inspected the two unmapped IDs in `development.ts`.
3. Confirmed both IDs are folder surfaces with `isFolder: true` and child
   templates attached through `parentFolder`.
4. Added an additive `exemptTemplateIds` metadata block.
5. Parsed the JSON after the edit.

---

## Findings

| Check | Result |
| --- | --- |
| Inventory | 60 top-level template IDs / 58 mapped / 2 unmapped / 0 mapped-but-undefined |
| Unmapped IDs | `individual_skills_folder`, `vibe_workflow_folder` |
| Disposition | Both exempt |
| JSON parse | PASS |
| `.ts` template files modified | No |
| Skill markdown or `skills-index.json` modified | No |
| Runtime / route / guard / test modified | No |
| Public-sync push | No |
| GC-018 filed | No |

The stale 118-template figure is not current-state evidence and must not be
used for future steering.

---

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| Future agents treat folder IDs as missing skill coverage | `exemptTemplateIds` now records both IDs as folder-navigation surfaces. |
| The stale 118-template number regenerates HN1/N3 work | Audit and closure review record the corrected 60/58/2/0 inventory. |
| Exemption becomes a broad `_folder` convention without review | No `linkagePolicy` convention was added in this tranche. |
| Public catalog overclaims skill coverage | No public-sync update or public claim was made. |

---

## Decision / Disposition

HN1 is closed as Fast-Lane hygiene.

The two folder-navigation IDs are explicitly exempted from skill-template
mapping. No broad `_folder` convention was added because the work order made
that optional and no separate operator approval was given for convention
publication.

Closure commit: pending at authoring time; sync through the active handoff
after commit.

---

## Claim Boundary

This closure confirms only the HN1 exemption decision and additive JSON
metadata. It does not authorize HN2, HN3, public catalog publication, runtime
changes, new skill/template content, or any A-H pain-point reopening.
