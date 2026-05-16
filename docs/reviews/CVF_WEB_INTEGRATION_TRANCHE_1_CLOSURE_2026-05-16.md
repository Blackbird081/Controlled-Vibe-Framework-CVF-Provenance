# CVF Web Integration Tranche 1 Closure - 2026-05-16

Memory class: FULL_RECORD

Status: CLOSED — ALL ACCEPTANCE CRITERIA MET

## Purpose

Record the closure of Web Integration Tranche 1 against the acceptance
criteria in the GC-018 authorization packet. Confirm test results, route
decisions, and claim boundaries. Hand off to Tranche 2.

## Scope

Closure covers exactly the three primitives authorized in
`docs/baselines/CVF_GC018_WEB_INTEGRATION_TRANCHE_1_AUTHORIZATION_2026-05-16.md`:
Artifact Export (deep), Knowledge Vault Intake (placeholder), Work
Transfer / Agent Handoff UI (placeholder).

## Source

- Authorization:
  `docs/baselines/CVF_GC018_WEB_INTEGRATION_TRANCHE_1_AUTHORIZATION_2026-05-16.md`
- Proposal (amended):
  `docs/reviews/CVF_WEB_INTEGRATION_TRANCHE_1_PROPOSAL_2026-05-16.md`
- Surface audit:
  `docs/audits/CVF_WEB_INTEGRATION_TRANCHE_1_SURFACE_AUDIT_2026-05-16.md`
- Implementation commit: `e72e5fa1` (public-sync repo)

## Decision

Tranche 1 is closed. All hard constraints and per-primitive acceptance
criteria are met. The tranche is eligible for Tranche 2 handoff.

## Evidence

### Test results

`npm run test:run` — **83 passed, 0 failed** (15 test files; 1 file
skipped — live OpenAI lane, intentionally skipped in local run).

Playwright mock E2E: `artifact-export-panel.spec.ts` — 2 scenarios
(EN export flow + VI language check). Passes against mock config.

### Per-primitive acceptance criteria

#### Primitive 1 — Artifact Export (deep)

| Criterion | Result |
| --- | --- |
| `ArtifactExportPanel.tsx` ≤ 700 LoC | 498 LoC ✓ |
| `artifacts/page.tsx` ≤ 700 LoC | 120 LoC ✓ |
| `api/artifacts/export/route.ts` ≤ 700 LoC | 279 LoC ✓ |
| HTML only; no PDF/PNG/PPTX | ✓ — boundary stated in UI + API |
| `Memory class`, `Status`, `Claim Boundary`, receipt anchor in output | ✓ — all four present in generated HTML |
| Vitest unit tests green | 3 API cases + 4 component cases ✓ |
| Playwright mock E2E green | 2 scenarios ✓ |
| No edit to `SpecExport.tsx` | ✓ confirmed |
| Governed file size check green | ✓ — no new exception registry entries |
| Claim: "HTML presentation candidate" only | ✓ — UI pills read "HTML / Candidate" |

Route implements markdown-lite parser + HTML builder + SHA-256 source
hash inline — satisfies "implements renderer" not "consumes runtime
service."

#### Primitive 2 — Knowledge Vault Intake (placeholder)

| Criterion | Result |
| --- | --- |
| `knowledge/intake/page.tsx` ≤ 200 LoC | 166 LoC ✓ |
| No new API route | ✓ |
| Placeholder boundary declared | ✓ — amber boundary banner: "This page prepares intake notes only." |
| Pointer to Artifact Export path | ✓ — UI guidance to send output to Artifact Export |
| Bilingual EN/VI | ✓ |

#### Primitive 3 — Work Transfer (placeholder)

| Criterion | Result |
| --- | --- |
| `work-transfer/page.tsx` ≤ 300 LoC | 184 LoC ✓ |
| Reads from existing validator | ✓ — `validateHandoff` imported from `src/lib/agent-handoff-validator.ts` |
| No new API route | ✓ — validator called client-side |
| Degrades gracefully when no live data | ✓ — defaults to demo input; ALLOW/WARN/BLOCK rendered live |
| Placeholder boundary declared | ✓ — amber banner: "This page checks whether the next step has enough context. It is not final proof by itself." |
| Bilingual EN/VI | ✓ |

### Route naming deviation — `/agent-handoff` → `/work-transfer`

The authorization packet named the route `/agent-handoff`. The
implementation uses `/work-transfer` with label "Work Transfer /
Chuyển giao công việc."

Reason: the public-surface gate blocks path segments containing
"handoff" as an internal-governance term not suitable for public
consumer-facing routes. The rename is a valid public-surface
adaptation. The validator imported is the same
`src/lib/agent-handoff-validator.ts`; only the route segment and UI
label differ.

This deviation is accepted. Future auditors can trace the naming gap
via this note.

### Claim boundary preserved

Tranche 1 claims "HTML presentation candidate" only. No committed
file, commit message, or UI string claims "governed artifact generation
proof." Live-governance proof remains deferred to a future tranche
that explicitly adds release-gate bundle coverage.

### End-user feedback

Not yet collected. Tranche 1 shipped the surfaces; structured end-user
feedback collection is planned as input to Tranche 2 scope decisions.

## Requirements

No open items remain for Tranche 1. Tranche 2 requirements are captured
in `docs/reviews/CVF_WEB_INTEGRATION_TRANCHE_2_PROPOSAL_2026-05-16.md`.

## Related Artifacts

- `docs/baselines/CVF_GC018_WEB_INTEGRATION_TRANCHE_1_AUTHORIZATION_2026-05-16.md`
- `docs/reviews/CVF_WEB_INTEGRATION_TRANCHE_1_PROPOSAL_2026-05-16.md`
- `docs/audits/CVF_WEB_INTEGRATION_TRANCHE_1_SURFACE_AUDIT_2026-05-16.md`
- `docs/reviews/CVF_WEB_INTEGRATION_TRANCHE_2_PROPOSAL_2026-05-16.md`
- `docs/baselines/CVF_GC018_WEB_INTEGRATION_TRANCHE_2_AUTHORIZATION_2026-05-16.md`

## Claim Boundary

This closure note claims only that Tranche 1 acceptance criteria are
met as of 2026-05-16, that tests are green (83/83 passed), and that
the `/work-transfer` route naming deviation is accepted. It does not
claim live-governance proof, does not claim "governed artifact
generation," and does not authorize any Tranche 2 work beyond what the
companion GC-018 authorization permits.
