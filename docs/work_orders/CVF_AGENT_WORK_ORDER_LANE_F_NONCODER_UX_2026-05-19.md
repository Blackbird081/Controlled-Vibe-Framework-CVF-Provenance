# CVF Agent Work Order — Lane F: Noncoder UX

Memory class: POINTER_RECORD

Status: CLOSED_WITH_INHERITED_FULL_SUITE_BLOCKERS — Codex implemented the
bounded UI lane and filed completion evidence on 2026-05-19.
Prerequisite: Lane E must be closed before Lane F begins.

## Purpose

Dispatch Codex to implement Lane F (Noncoder UX) as defined in
`docs/roadmaps/CVF_NEXT_PHASE_ROADMAP_LANE_D_E_F_G_2026-05-19.md`.

Lane F adds an `OutcomeQuickActions` component to the web UI home page with
3 outcome quick-action buttons that pre-fill and launch the 3 governed packs
from Lane B without requiring the user to browse the template list.

## Source

- `docs/roadmaps/CVF_NEXT_PHASE_ROADMAP_LANE_D_E_F_G_2026-05-19.md` — lane F spec
- `docs/reviews/CVF_REVIEW_CVF_ASSESSMENT_AND_DIRECTION_2026-05-18.md` —
  Problem F: outcome-first UX gap
- `AGENT_HANDOFF_V9_2026-05-18.md` — active session posture
- `CVF_SESSION/ACTIVE_SESSION_STATE.json` — current mode

## 1. Mission

Add 3 outcome quick-action buttons (`Create Product Brief`, `Generate SOP`,
`Analyze Strategy`) to the home page above the template browser.

Success means: a user landing on the home page sees 3 prominent outcome
buttons; clicking any button immediately enters the execute flow with the
correct governed pack template pre-filled; bilingual (vi/en) labels work;
component unit tests pass.

## 2. Authority Chain

- Operator instruction: 2026-05-19 — implement Lane D/E/F/G in sequence
- Roadmap: `docs/roadmaps/CVF_NEXT_PHASE_ROADMAP_LANE_D_E_F_G_2026-05-19.md`
- Decision pack: `docs/reviews/CVF_MULTI_AGENT_DECISION_PACK_REVIEW_CVF_NEXT_PHASE_2026-05-18.md`
- Active session: `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- Active handoff: `AGENT_HANDOFF_V9_2026-05-18.md`
- Prerequisite: Lane E completion packet filed and reviewed

## 3. Agent Roles

- Orchestrator / dispatcher: operator and coordinating agent (Claude)
- Implementer: Codex
- Reviewer: Claude
- Operator approval required for: adding a new page route, changing template
  categories, any auth/RBAC change

## 4. Required First Reads

Before filing GC-018:

1. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/home/page.tsx`
   — full current home page; understand `handleTryTemplate`, `workflowState`,
   and `lang` prop usage before writing new component
2. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/` —
   the 3 packs from Lane B; note their `templateId` values
3. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates/index.ts` —
   confirm `app_builder_complete`, `documentation`, `strategy_analysis`
   template IDs exist and their `fields` definitions
4. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/` — existing
   component patterns; `OutcomeQuickActions` must follow the same style
5. `CLAUDE.md` → Landing Page Component Architecture section — GC-023 rule:
   each new component must be <200 lines; no localStorage in useState initializer
6. `governance/compat/CVF_GOVERNED_FILE_SIZE_EXCEPTION_REGISTRY.json` —
   line limits for `home/page.tsx` and any touched files

Anti-duplication grep:

```powershell
rg -n "OutcomeQuick|quick.action|quickAction" EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/
rg -n "app_builder_complete|strategy_analysis|documentation" EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/home/page.tsx
```

## 5. Pre-Flight Checks

```powershell
python governance/compat/check_active_session_state.py --enforce
python governance/compat/check_markdown_structural_completeness.py
python governance/compat/check_docs_governance_compat.py
Test-Path "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/home/page.tsx"
Test-Path "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/app_builder_complete/workflow.spec.md"
(Get-Content "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/home/page.tsx").Count
git status --short
```

Check line count of `home/page.tsx` before edit. If adding import and
component usage would breach GC-023 soft threshold, split accordingly.

## 6. GC-018 Requirements

Before implementation, file:

```
docs/baselines/CVF_GC018_LANE_F_NONCODER_UX_2026-05-19.md
```

The GC-018 must record:

- exact component name: `OutcomeQuickActions`
- exact file path: `cvf-web/src/components/OutcomeQuickActions.tsx`
- exact 3 templateIds used (from Lane B governed packs)
- exact integration point in home page
- R0 risk statement (UI component only, no runtime change)
- explicit no-new-route, no-RBAC-change boundary
- acceptance criteria
- Tranche Closure Checklist

## 7. Write Ownership

Allowed scope:

```
EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/OutcomeQuickActions.tsx  (NEW)
EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/OutcomeQuickActions.test.tsx (NEW)
EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/home/page.tsx       (MODIFY — import and render OutcomeQuickActions)
docs/baselines/CVF_GC018_LANE_F_NONCODER_UX_2026-05-19.md                          (NEW)
docs/reviews/CVF_LANE_F_NONCODER_UX_COMPLETION_2026-05-19.md                       (NEW)
```

Forbidden scope:

```
EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates/     (do not modify template definitions)
EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/           (no API route changes)
EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/   (no new page routes)
```

Write mode: create OutcomeQuickActions component and test; modify home page
to import and render it; create GC-018 and completion packet.

## 8. Execution Plan

1. Read `home/page.tsx` fully. Note `handleTryTemplate(template, prefilled)`
   signature. Note `lang` prop availability. Note current line count.
   Grep for existing quick-action or outcome-button pattern.
   Stop if: `OutcomeQuickActions` already exists.

2. Identify the 3 templateIds from governed pack `workflow.spec.md` files
   (e.g., `app_builder_complete`, `documentation`, `strategy_analysis`).
   Confirm these IDs exist in the canonical templates directory with
   `rg -n "id:.*app_builder|id:.*documentation|id:.*strategy" src/lib/templates`.
   Stop if: any templateId does not exist — report to reviewer.

3. Create `OutcomeQuickActions.tsx` (<200 lines, GC-023):
   - Props: `lang: 'vi' | 'en'`, `onSelectTemplate: (templateId: string) => void`
   - 3 button cards, each with: outcome icon, bilingual outcome title, short
     bilingual description
   - Bilingual labels:
     * `app_builder_complete`: vi "Tạo Product Brief" / en "Create Product Brief"
     * `documentation`: vi "Tạo SOP" / en "Generate SOP"
     * `strategy_analysis`: vi "Phân tích chiến lược" / en "Analyze Strategy"
   - Tailwind styling: consistent with existing home page card style
   - No localStorage, no useEffect for initialisation — static default

4. Integrate into `home/page.tsx`:
   - Import `OutcomeQuickActions`
   - Render above the existing template browser section
   - Wire `onSelectTemplate` to call `handleSelectTemplate` (or equivalent)
     with the correct template object looked up from `templates`
   - Pass `lang` from existing page state

5. Write `OutcomeQuickActions.test.tsx`:
   - renders 3 buttons
   - clicking each button calls `onSelectTemplate` with correct templateId
   - renders vi labels when `lang='vi'` and en labels when `lang='en'`
   Use Vitest + React Testing Library following existing test patterns.

6. Run `npm run build` to confirm no TypeScript errors.
   Run `npm run lint` — must be clean (max-warnings=0).
   Run `npm test` — all tests pass.

7. File GC-018 baseline. File completion packet. Update GC-020.

## 9. Evidence Requirements

```powershell
Test-Path "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/OutcomeQuickActions.tsx"
(Get-Content "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/OutcomeQuickActions.tsx").Count
rg -n "OutcomeQuickActions" EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/home/page.tsx
npm run build       # must succeed
npm run lint        # must be clean
npm test            # all pass
python governance/compat/run_local_governance_hook_chain.py --hook pre-commit
```

Evidence Trace Block required for each claim in completion packet.

## 10. Acceptance Criteria

- [ ] `OutcomeQuickActions.tsx` exists and is under 200 lines (GC-023)
- [ ] Component renders 3 outcome buttons for `app_builder_complete`,
      `documentation`, `strategy_analysis`
- [ ] Clicking a button calls the correct templateId handler
- [ ] Bilingual labels work correctly for vi and en
- [ ] Component is rendered on home page above template browser
- [ ] No new template categories created; uses only existing governed pack IDs
- [ ] `npm run build` succeeds — no TypeScript errors
- [ ] `npm run lint` passes — no warnings
- [ ] Component unit tests pass
- [ ] No API route or auth changes
- [ ] GC-023 line limit respected for all modified files
- [ ] Current governance pre-commit hook chain passes without bypassing hooks

## 11. Review Gate

Reviewer: Claude.

Reviewer checks:
- Component is under 200 lines
- TemplateIds match existing governed packs from Lane B
- No route changes, no auth changes
- Build and lint pass
- All acceptance criteria evidenced

## 12. Closure Checklist

- [ ] GC-018 filed and referenced
- [ ] All acceptance criteria PASS
- [ ] Evidence Trace Block present
- [ ] Current governance hook chain passes without bypassing hooks
- [ ] GC-020 handoff updated
- [ ] Public catalog: consider adding "outcome-first home page quick actions"
      as a UI capability row with `defined, unit-tested` status
- [ ] Reviewer disposition: NO_BLOCKING_FINDING or operator waiver

## 13. Return-To-Orchestrator Conditions

Stop and escalate if:

- `OutcomeQuickActions` already exists
- Any of the 3 templateIds does not exist in the canonical
  `src/lib/templates/` directory
- `home/page.tsx` would exceed GC-023 hard threshold after modification
- Build or lint fails and cannot be fixed within lane scope
- Any API or auth change is needed to make the buttons work

## Claim Boundary

Lane F closes with: 3 outcome quick-action buttons rendered on home page,
wired to correct governed pack templateIds — `defined, unit-tested`

Not claimed: full outcome-first UX redesign, new page route, server-side
personalization, marketing-copy pack behavior, live execution proof from UI.
