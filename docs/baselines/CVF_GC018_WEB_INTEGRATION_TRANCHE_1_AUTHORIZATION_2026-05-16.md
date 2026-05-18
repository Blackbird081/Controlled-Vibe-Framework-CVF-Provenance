# CVF GC-018 Web Integration Tranche 1 Authorization - 2026-05-16

Memory class: SUMMARY_RECORD

Status: AUTHORIZATION GRANTED — EXECUTION PERMITTED

## Purpose

Grant GC-018 continuation authorization for the Web Integration Tranche 1
implementation. This packet is the operator-approval gate required before
any Tranche 1 file is created or committed.

## Scope

Authorization covers exactly the artifacts listed in the depth allocation
below. It does not authorize Tranche 2 work, runtime contract changes, or
any edit to files listed as out-of-scope.

Authorized primitives:

- Artifact Export (deep) — new component + new route segment + new API
  route + vitest unit tests + Playwright mock E2E
- Knowledge Vault Intake (placeholder) — new route segment only
- Agent Handoff UI (placeholder) — new route segment only

## Source

- Proposal:
  `docs/reviews/CVF_WEB_INTEGRATION_TRANCHE_1_PROPOSAL_2026-05-16.md`
  (amended 2026-05-16, five defects resolved)
- Surface audit:
  `docs/audits/CVF_WEB_INTEGRATION_TRANCHE_1_SURFACE_AUDIT_2026-05-16.md`
  (amended 2026-05-16, SpecExport cap corrected)
- Runtime adoption baseline:
  `docs/baselines/CVF_GC018_MODEL_GATEWAY_RUNTIME_AUTHORIZATION_2026-05-16.md`
- Document artifact renderer spec:
  `docs/reference/CVF_GOVERNED_DOCUMENT_ARTIFACT_RENDERING_SPEC_2026-05-16.md`

## Decision

Authorization granted subject to all hard constraints and acceptance
criteria enumerated in the proposal. The amended proposal is the
controlling scope document.

## Evidence

Surface audit confirms delta feasibility: each primitive has an adjacent
existing surface and the test infrastructure (Vitest + Playwright) is
already in place. The amended proposal resolves all five cross-review
defects:

1. Artifact Export implements an HTML renderer per the document artifact
   renderer spec boundary — it does not consume an existing runtime service.
2. Tranche 1 claims "HTML presentation candidate" only, not "governed
   artifact generation proof." Live-governance proof is deferred to a
   future tranche.
3. PDF/PNG/PPTX are explicitly out of scope; HTML only; browser print
   preview is acceptable.
4. SpecExport has `approvedMaxLines: 1300` with 1280 current lines (20
   remaining). No edits to `SpecExport.tsx` are permitted under any
   circumstances.
5. Agent Handoff UI renders validator demo or audit-filtered candidates
   when present; degrades gracefully to schema + "no live handoffs" when
   no live endpoint is available.

## Requirements

Authorized artifacts (one commit per file):

### Artifact Export (deep)

| File | Max LoC |
| --- | ---: |
| `src/components/ArtifactExportPanel.tsx` | 700 |
| `src/app/(dashboard)/artifacts/page.tsx` | 700 |
| `src/app/api/artifacts/export/route.ts` | 700 |
| `src/components/ArtifactExportPanel.test.tsx` | — |
| `src/app/api/artifacts/export/route.test.ts` | — |
| One Playwright mock E2E scenario | — |

All paths are relative to
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/`.

### Knowledge Vault Intake (placeholder)

| File | Max LoC |
| --- | ---: |
| `src/app/(dashboard)/knowledge/intake/page.tsx` | 200 |

### Agent Handoff UI (placeholder)

| File | Max LoC |
| --- | ---: |
| `src/app/(dashboard)/agent-handoff/page.tsx` | 300 |

## Enforcement

Hard constraints (violation of any invalidates the tranche):

1. No edit to `SpecExport.tsx` — 20 lines to approved cap.
2. One commit per file — selective rollback preserved.
3. GC-045 must pass on every committed Markdown file.
4. Governed file size check must pass — no new exception registry entries.
5. Artifact Export output is HTML only; no PDF/PNG/PPTX.
6. Tranche 1 closure note must state "HTML presentation candidate" — not
   "governed artifact generation."
7. Placeholder pages must not introduce new API routes.
8. No edit to other GC-023 exception files.

## Related Artifacts

- `docs/reviews/CVF_WEB_INTEGRATION_TRANCHE_1_PROPOSAL_2026-05-16.md`
- `docs/audits/CVF_WEB_INTEGRATION_TRANCHE_1_SURFACE_AUDIT_2026-05-16.md`
- `docs/reference/CVF_GOVERNED_DOCUMENT_ARTIFACT_RENDERING_SPEC_2026-05-16.md`
- `governance/compat/CVF_GOVERNED_FILE_SIZE_EXCEPTION_REGISTRY.json`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/SpecExport.tsx` (out-of-scope)
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/agent-handoff-validator.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/governance/knowledge/page.tsx`

## Claim Boundary

This authorization packet claims only that Tranche 1 is permitted to
proceed under the constraints above, that the proposal has been reviewed
and amended, and that the operator has granted execution authorization.
It does not claim that any file has been implemented, does not claim
"governed artifact generation," and does not extend the CVF 16.5
absorption authority. Closure requires a separate closure note at
`docs/reviews/CVF_WEB_INTEGRATION_TRANCHE_1_CLOSURE_2026-05-??.md`.
