# CVF Web Integration Tranche 3 Proposal — End-User Discovery Surface

Memory class: FULL_RECORD

Status: PROPOSED

## Purpose

Expose the Web Integration T1+T2 deliverables (Knowledge Vault Intake,
Artifact Export with governed receipt, Work Transfer) to the end-user
and non-coder audience. T1 and T2 built the routes and components; T3
makes them discoverable from the first screen a new user sees.

## Scope

Three workstreams, all within existing files, no new routes, no new API
routes:

1. **Home page quick-action cards** — add two quick-action entries to
   `home/page.tsx` linking to `/knowledge/intake` and `/artifacts`.
2. **Landing page feature callout** — add a "What you can do today"
   section or extend the existing feature list in
   `(dashboard)/landing/page.tsx` to mention governed artifact export
   and knowledge intake.
3. **README update** — add a "Web Workflows" section to the public-sync
   `README.md` describing the three new end-user workflows with their
   route paths and what non-coders can do with them.

No changes to `SpecExport.tsx`, `QuickStart.tsx` (onboarding tour is
not in scope — its test coverage is independent and adding tour steps
would require test additions that may push file sizes), or any API
routes.

## Source

Prior art:

- T1 closure: `docs/reviews/CVF_WEB_INTEGRATION_TRANCHE_1_CLOSURE_2026-05-16.md`
- T2 closure: `docs/reviews/CVF_WEB_INTEGRATION_TRANCHE_2_CLOSURE_2026-05-16.md`
- Sidebar already links to all three routes (confirmed in `Sidebar.tsx`)
- Public evidence: `docs/evidence/web-governance-path.md` — governed
  artifact generation claim confirmed 2026-05-16

## Findings

The routes exist and are functional. The sidebar navigates to them.
But the home page (first screen post-login) has no quick-action entry
for either Knowledge Intake or Artifact Export. The landing page has
no feature callout for governed artifact generation. The public README
does not mention any of the three web workflows. End users who do not
explore the sidebar will not discover these features.

## Decision

Pending GC-018 authorization. This proposal is PROPOSED only.

## Workstream Detail

### Workstream 1 — Home page quick-action cards

**File:** `src/app/(dashboard)/home/page.tsx` — currently 914 lines
(soft advisory; hard limit 1000; not in exception registry)

**Change:** Add ≤ 20 lines — two quick-action card entries for
Knowledge Intake and Artifact Export in the existing quick-actions
grid. Must stay under 940 lines total (20-line budget).

**Acceptance criteria:**

- Quick-action card for `/knowledge/intake` visible on home page
- Quick-action card for `/artifacts` visible on home page
- Bilingual EN/VI labels
- `home/page.tsx` stays under 940 lines
- No new test file required (UI layout change, no new logic branch)

### Workstream 2 — Landing page feature callout

**File:** `src/app/(dashboard)/landing/page.tsx` — currently 216 lines
(well under soft 700 / hard 1000 for `frontend_component`)

**Change:** Add ≤ 40 lines — a "New: Governed Workflows" callout block
listing Knowledge Intake, Artifact Export (with receipt), and Work
Transfer with brief descriptions and links. Bilingual EN/VI.

**Acceptance criteria:**

- Landing page shows callout for all three governed workflows
- Links to `/knowledge/intake`, `/artifacts`, `/work-transfer`
- Bilingual EN/VI copy
- `landing/page.tsx` stays under 260 lines
- No new test file required (static copy block, no logic)

### Workstream 3 — Public README web workflows section

**File:** `README.md` in public-sync repo — currently 443 lines
(governed `active_markdown`, soft 900 / hard 1200)

**Change:** Add ≤ 30 lines — a "Web Workflows" section after the
existing feature list, describing the three end-user workflows, their
routes, and what non-coders can do (submit knowledge, export governed
HTML packets, review transfer history).

**Acceptance criteria:**

- README has "Web Workflows" section
- Three workflows described: Knowledge Intake, Artifact Export, Work
  Transfer
- `README.md` stays under 480 lines
- English only (public-sync README is English-only per prior decision)

## Risk

Low. All changes are additive copy + navigation only. No logic changes.
No new routes. The only GC-023 risk is `home/page.tsx` at 914/1000 —
budget is 86 lines; this change uses ≤ 20.

## Related Artifacts

- `docs/baselines/CVF_GC018_WEB_INTEGRATION_TRANCHE_3_AUTHORIZATION_2026-05-16.md`
- `docs/reviews/CVF_WEB_INTEGRATION_TRANCHE_2_CLOSURE_2026-05-16.md`
- `docs/evidence/web-governance-path.md`

## Claim Boundary

This proposal claims only that the workstream scope is correct, the
file budgets are within governed limits, and the change is additive
copy/navigation only. It does not claim UI visual correctness or that
the landing page constitutes a governed artifact on its own.
