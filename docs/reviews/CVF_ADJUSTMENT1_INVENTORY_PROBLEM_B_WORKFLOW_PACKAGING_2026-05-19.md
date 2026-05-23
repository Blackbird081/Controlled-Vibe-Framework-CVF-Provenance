# CVF Adjustment 1 Inventory — Problem B: Workflow Packaging

Memory class: SUMMARY_RECORD

Status: FILED — 2026-05-19. Pre-GC-018 factual inventory per
`docs/reviews/archive/CVF_REVIEW_CVF_ASSESSMENT_AND_DIRECTION_2026-05-18.md`
Adjustment 1 requirement.

## Purpose

Record the factual pre-GC-018 inventory for Problem B so downstream work does
not reopen already delivered workflow-packaging scope or duplicate Lane B
governed pack work.

## Source

- `docs/reviews/archive/CVF_REVIEW_CVF_ASSESSMENT_AND_DIRECTION_2026-05-18.md` §
  Adjustment 1
- Live scan of `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/`
  performed 2026-05-19 by coordinating agent (Claude)

## Scope / Target / Owner Boundary

Scope: Problem B only — Skill → Product Capability / Workflow Packaging.
Owner: Claude (reviewer role) per Adjustment 1 instruction.
Not in scope: problems C, D, H (covered in separate inventory files).

## Findings

### What already exists

**Template system:**

| Path | Lines | Notes |
|---|---|---|
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates/index.ts` | 201 | Template registry; 5 export groups |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates/development.ts` | — | Contains `app_builder_complete` (id) at line 60 |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates/content.ts` | — | Contains `documentation` (id) at line 16 |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates/business.ts` | — | Contains `strategy_analysis` (id) at line 16 |

**Governed packs (Lane B delivery — all 3 exist):**

| Pack | Files | workflow.spec.md | execution.policy.json | receipt.schema.json |
|---|---|---|---|---|
| `app_builder_complete` | 3 | 66 lines | 35 lines | 88 lines |
| `documentation` | 3 | 66 lines | 35 lines | 88 lines |
| `strategy_analysis` | 3 | 66 lines | 35 lines | 88 lines |

All 3 packs are under:
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/`

**GC-018 baseline filed:**
`docs/baselines/CVF_GC018_LANE_B_WORKFLOW_PACKAGING_2026-05-19.md`

**Template unit tests:** 2 test files under
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates/`
(`index.test.ts`, `governance-enforcement.test.ts`).
No per-pack unit tests (the pack files are JSON/Markdown, not TypeScript).

### What the actual gap is

Lane B is complete. All 3 governed packs have `workflow.spec.md`,
`execution.policy.json`, and `receipt.schema.json`. The remaining gap
is the **home-page UX surface** (Lane F): the 3 packs are not surfaced
as first-class outcome buttons on the home page. The packaging gap is
closed; the discoverability gap is in Lane F.

### What "done" looks like for the next tranche

Lane F acceptance criterion: `OutcomeQuickActions` component renders 3
buttons on home page, each wired to the correct governed pack templateId
(`app_builder_complete`, `documentation`, `strategy_analysis`), confirmed
by component unit tests passing.

## Risk

None. This is a read-only inventory. Lane B is closed; no new packaging
work is authorized here.

## Decision / Recommendation / Disposition

Problem B packaging: **CLOSED** — all 3 governed packs delivered in Lane B.
Remaining UX gap: tracked in Lane F work order
(`docs/work_orders/CVF_AGENT_WORK_ORDER_LANE_F_NONCODER_UX_2026-05-19.md`).

## Claim Boundary

This packet is read-only inventory evidence. It does not authorize new
packaging work, public claims, or runtime behavior changes.
