# CVF GC-018 Lane F Noncoder UX

Memory class: SUMMARY_RECORD
Status: AUTHORIZED

## Purpose

Authorize Lane F to add a small outcome-first entry surface on the cvf-web home
page so non-coder users can start three already-governed packs without
browsing the full template catalog.

## Scope

In scope:

- add `OutcomeQuickActions`;
- create
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/OutcomeQuickActions.tsx`;
- add unit tests in
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/OutcomeQuickActions.test.tsx`;
- render the component in
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/home/page.tsx`
  above the existing template browser section;
- wire button selection to existing template selection flow with the canonical
  template IDs `app_builder_complete`, `documentation`, and
  `strategy_analysis`.

Out of scope:

- adding a page route;
- changing API routes;
- changing auth, RBAC, or runtime policy;
- editing template definitions or governed pack definitions;
- claiming full outcome-first UX redesign or live execution proof from the
  quick-action buttons.

## Source / Predecessor Evidence

- `docs/roadmaps/CVF_NEXT_PHASE_ROADMAP_LANE_D_E_F_G_2026-05-19.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_LANE_F_NONCODER_UX_2026-05-19.md`
- `docs/reviews/CVF_REVIEW_CVF_ASSESSMENT_AND_DIRECTION_2026-05-18.md`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/home/page.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/app_builder_complete/workflow.spec.md`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/documentation/workflow.spec.md`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/strategy_analysis/workflow.spec.md`

## Source-Fidelity Pass

Pre-flight checks confirmed:

- `OutcomeQuickActions` does not already exist in `cvf-web/src/`;
- the three governed pack directories exist under `src/lib/governed-packs/`;
- canonical template definitions exist for:
  - `app_builder_complete` in `src/lib/templates/development.ts`;
  - `documentation` in `src/lib/templates/content.ts`;
  - `strategy_analysis` in `src/lib/templates/business.ts`;
- `home/page.tsx` already exposes `handleSelectTemplate(template)` and the
  browse view template browser section;
- `home/page.tsx` line count before edit is 931, so the integration must stay
  below the GC-023 hard threshold and avoid unrelated expansion.

## Decision / Baseline / Proposed Tranche

Decision: implement Lane F as a bounded R0 UI tranche.

Exact component:

```text
OutcomeQuickActions
```

Exact component path:

```text
EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/OutcomeQuickActions.tsx
```

Exact template IDs:

```text
app_builder_complete
documentation
strategy_analysis
```

Exact integration point:

```text
cvf-web home browse view, after the knowledge/artifact action links and before
the existing template browser section containing CategoryTabs and TemplateCard.
```

Risk ceiling: R0, because the change is a static client-side UI shortcut into
already-existing template selection behavior. It does not alter provider calls,
runtime policy, API routes, RBAC, or template contracts.

## Rule

Lane F may claim:

> The cvf-web home page renders three bilingual outcome quick-action buttons
> wired to the existing governed pack template IDs and unit-tested at the
> component boundary.

Lane F must not claim:

> A full outcome-first UX redesign, new server-side personalization, new
> governed pack behavior, or live execution proof was delivered by this lane.

## Evidence / Verification

Required web commands:

```powershell
npm run build
npm run lint
npm run test:run -- src/components/OutcomeQuickActions.test.tsx
```

Run in:

```text
EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web
```

Repository guard:

```powershell
python governance/compat/run_local_governance_hook_chain.py --hook pre-commit
```

## Tranche Closure Checklist

- `OutcomeQuickActions.tsx` exists and stays under 200 lines.
- Component renders the three governed pack template IDs.
- Button clicks call `onSelectTemplate(templateId)` with the correct ID.
- Vietnamese and English labels render.
- Home page renders the component above the existing template browser.
- No template definitions are modified.
- No API route, auth, RBAC, or new page route is changed.
- Web build, lint, and targeted unit test pass or any inherited blocker is
  recorded honestly.
- Current governance hook chain passes without bypassing hooks.

## Claim Boundary

This authorization covers only the outcome quick-action UI shortcut and its
home-page wiring into existing template selection. It is not a live governance
behavior claim and does not substitute for the mandatory live governance proof
required for release-quality governance assertions.
