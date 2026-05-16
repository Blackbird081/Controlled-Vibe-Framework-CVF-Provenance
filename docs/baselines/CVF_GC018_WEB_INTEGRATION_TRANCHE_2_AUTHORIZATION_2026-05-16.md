# CVF GC-018 Web Integration Tranche 2 Authorization - 2026-05-16

Memory class: FULL_RECORD

Status: AUTHORIZATION GRANTED — EXECUTION PERMITTED

## Purpose

Grant GC-018 continuation authorization for Web Integration Tranche 2.
This packet is the operator-approval gate required before any Tranche 2
file is created or committed.

## Scope

Authorization covers exactly the three workstreams in the Tranche 2
proposal. It does not authorize Tranche 3 (OpenSpec intake, live QBS
display) or any new runtime contracts.

Authorized workstreams:

1. Artifact Export — live governance proof layer (new `proof.ts` +
   test; ≤ 10-line delta to `route.ts`; ≤ 15-line delta to
   `ArtifactExportPanel.tsx`)
2. Knowledge Vault Intake — promote to deep (`knowledge/intake/page.tsx`
   extended ≤ 350 LoC + new component test)
3. Work Transfer — promote to deep (`work-transfer/page.tsx` extended
   ≤ 400 LoC + new component test)

## Source

- Proposal:
  `docs/reviews/CVF_WEB_INTEGRATION_TRANCHE_2_PROPOSAL_2026-05-16.md`
- Tranche 1 closure (predecessor):
  `docs/reviews/CVF_WEB_INTEGRATION_TRANCHE_1_CLOSURE_2026-05-16.md`
- Tranche 1 authorization (predecessor):
  `docs/baselines/CVF_GC018_WEB_INTEGRATION_TRANCHE_1_AUTHORIZATION_2026-05-16.md`

## Decision

Authorization granted. Tranche 1 is closed with all criteria met.
Tranche 2 scope is bounded and all required API substrate exists in the
current `cvf-web` codebase.

## Evidence

Tranche 1 closure confirms:

- 83/83 tests green
- Three primitives shipped within LoC caps
- No SpecExport edits
- No new exception registry entries
- Claim boundary "HTML presentation candidate" preserved

Tranche 2 adds depth to existing surfaces using existing API endpoints.
No new runtime contracts, no new external integrations.

## Requirements

Authorized file changes (one commit per file):

### Workstream 1 — Artifact Export proof layer

| File | Action | Max LoC |
| --- | --- | ---: |
| `src/app/api/artifacts/export/proof.ts` | New | 200 |
| `src/app/api/artifacts/export/proof.test.ts` | New | — |
| `src/app/api/artifacts/export/route.ts` | Delta | +10 lines |
| `src/components/ArtifactExportPanel.tsx` | Delta | +15 lines |

All paths relative to
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/`.

### Workstream 2 — Knowledge Vault Intake deep

| File | Action | Max LoC |
| --- | --- | ---: |
| `src/app/(dashboard)/knowledge/intake/page.tsx` | Extend | 350 |
| `src/app/(dashboard)/knowledge/intake/page.test.tsx` | New | — |

### Workstream 3 — Work Transfer deep

| File | Action | Max LoC |
| --- | --- | ---: |
| `src/app/(dashboard)/work-transfer/page.tsx` | Extend | 400 |
| `src/app/(dashboard)/work-transfer/page.test.tsx` | New | — |

## Enforcement

Hard constraints (violation of any invalidates the tranche):

1. No edit to `SpecExport.tsx` — 20 lines to approved cap.
2. One commit per file.
3. GC-045 must pass on every committed Markdown file.
4. Governed file size check must pass — no new exception registry
   entries.
5. "Governed artifact generation" claim upgrade in closure note is
   conditional on live governance receipt being produced in a test
   run. If no live receipt, claim stays "HTML presentation candidate."
6. No new API routes — all API calls use existing endpoints.
7. No new runtime contracts.

## Related Artifacts

- `docs/reviews/CVF_WEB_INTEGRATION_TRANCHE_2_PROPOSAL_2026-05-16.md`
- `docs/reviews/CVF_WEB_INTEGRATION_TRANCHE_1_CLOSURE_2026-05-16.md`
- `docs/baselines/CVF_GC018_WEB_INTEGRATION_TRANCHE_1_AUTHORIZATION_2026-05-16.md`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/knowledge/intake/page.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/work-transfer/page.tsx`

## Claim Boundary

This authorization packet claims only that Tranche 2 is permitted to
proceed under the constraints above and that Tranche 1 is confirmed
closed. It does not upgrade the Artifact Export claim from "HTML
presentation candidate" to "governed artifact generation" — that
upgrade is conditional on the closure note. It does not authorize
Tranche 3 work. Closure requires a separate closure note at
`docs/reviews/CVF_WEB_INTEGRATION_TRANCHE_2_CLOSURE_2026-05-??.md`.
