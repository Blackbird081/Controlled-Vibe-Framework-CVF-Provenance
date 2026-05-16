# CVF GC-018 Web Integration Tranche 3 Authorization - 2026-05-16

Memory class: FULL_RECORD

Status: AUTHORIZATION GRANTED — EXECUTION PERMITTED

## Purpose

Grant GC-018 continuation authorization for Web Integration Tranche 3.
This packet is the operator-approval gate required before any Tranche 3
file is created or committed.

## Scope

Authorization covers exactly the three workstreams in the Tranche 3
proposal: home page quick-action cards, landing page feature callout,
and public README web workflows section. It does not authorize any new
routes, new API routes, new runtime contracts, or Tranche 4 work.

## Source

- Proposal:
  `docs/reviews/CVF_WEB_INTEGRATION_TRANCHE_3_PROPOSAL_2026-05-16.md`
- Tranche 2 closure (predecessor):
  `docs/reviews/CVF_WEB_INTEGRATION_TRANCHE_2_CLOSURE_2026-05-16.md`
- Tranche 2 authorization (predecessor):
  `docs/baselines/CVF_GC018_WEB_INTEGRATION_TRANCHE_2_AUTHORIZATION_2026-05-16.md`

## Decision

Authorization granted. Tranche 2 is closed with all criteria met and
claim upgraded to "governed artifact generation" as of 2026-05-16.
Tranche 3 scope is additive copy and navigation only with no new logic,
no new API surface, and all target files within governed LoC budgets.

## Evidence

Tranche 2 closure confirms:

- 97/97 tests green
- Proof layer operational; live receipt confirmed 2026-05-16
- Claim upgraded to "governed artifact generation"
- All three workstreams within LoC caps
- No SpecExport edits; no new exception registry entries

Target file headroom:

- `home/page.tsx` — 914 lines; hard limit 1000; 86 lines available; T3 uses ≤ 20
- `landing/page.tsx` — 216 lines; hard limit 1000; 784 lines available; T3 uses ≤ 40
- `README.md` (public-sync) — 443 lines; hard limit 1200; T3 uses ≤ 30

## Requirements

Authorized file changes:

### Workstream 1 — Home page quick-action cards

| File | Action | LoC delta cap |
| --- | --- | ---: |
| `src/app/(dashboard)/home/page.tsx` | Modify | +20 lines |

All paths relative to `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/`.

### Workstream 2 — Landing page feature callout

| File | Action | LoC delta cap |
| --- | --- | ---: |
| `src/app/(dashboard)/landing/page.tsx` | Modify | +40 lines |

### Workstream 3 — Public README web workflows section

| File | Action | LoC delta cap |
| --- | --- | ---: |
| `README.md` | Modify | +30 lines |

File path relative to public-sync repo root.

## Enforcement

Hard constraints (violation of any invalidates the tranche):

1. No edit to `SpecExport.tsx`.
2. No new routes, API routes, or runtime contracts.
3. No new test files — workstreams 1 and 2 are copy/navigation only.
4. GC-045 must pass on every committed Markdown file.
5. Governed file size check must pass — no new exception registry entries.
6. `home/page.tsx` must stay under 940 lines after changes.
7. Public README is English only.
8. Claim boundary: this tranche claims copy and navigation changes only.

## Related Artifacts

- `docs/reviews/CVF_WEB_INTEGRATION_TRANCHE_3_PROPOSAL_2026-05-16.md`
- `docs/reviews/CVF_WEB_INTEGRATION_TRANCHE_2_CLOSURE_2026-05-16.md`
- `docs/baselines/CVF_GC018_WEB_INTEGRATION_TRANCHE_2_AUTHORIZATION_2026-05-16.md`
- `docs/evidence/web-governance-path.md`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/home/page.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/landing/page.tsx`

## Claim Boundary

This authorization packet claims only that Tranche 3 is permitted to
proceed under the constraints above and that Tranche 2 is confirmed
closed. It does not authorize any new governance behavior or new
runtime capabilities. Closure requires a separate closure note at
`docs/reviews/CVF_WEB_INTEGRATION_TRANCHE_3_CLOSURE_2026-05-16.md`.
