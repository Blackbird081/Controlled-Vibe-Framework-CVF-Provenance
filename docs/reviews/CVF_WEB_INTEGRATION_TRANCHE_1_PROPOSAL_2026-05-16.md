# CVF Web Integration Tranche 1 Proposal - 2026-05-16

Memory class: FULL_RECORD

Status: proposal awaiting GC-018 authorization; not yet executed.

## Purpose

Record the rationale, scope, depth allocation, and acceptance criteria for
a bounded Web Integration tranche that wires three CVF 16.5 primitives into
`cvf-web` for the end-user audience. The tranche follows the runtime-
adoption tranche that closed all CVF 16.5 lanes as `runtime-owned` and is
the natural next step toward end-user-visible governed value.

## Scope

Documentation-only proposal. Implementation is gated behind a fresh GC-018
authorization packet. Scope includes:

- one **deep** primitive: Artifact Export
- two **placeholder** primitives: Knowledge Vault Intake, Agent Handoff UI
- new route segments under the dashboard with strict separation from
  existing oversized components
- vitest unit tests + Playwright mock E2E for the deep primitive
- governed artifact contract integration via the document artifact renderer
  runtime adopted at commit `41f37cc2`

Scope excludes:

- new runtime contracts or runtime ownership changes
- modifications to `SpecExport.tsx` (already at 1280 LoC under exception)
- modifications to other GC-023 exception files
- new external knowledge absorption
- live provider integration beyond the existing release-gate lane
- Tranche 2 work on the placeholder primitives

## Target

End-user audience consuming governed AI/agent output. Primary value:
"after governance passes, the user can download a clean governed
artifact (HTML/PDF/printable view) bound to the receipt."

## Findings

The surface audit
(`docs/audits/CVF_WEB_INTEGRATION_TRANCHE_1_SURFACE_AUDIT_2026-05-16.md`)
confirms three things:

1. Each proposed primitive has an adjacent existing surface; this is a
   delta tranche, not a from-zero build.
2. The runtime-adoption tranche from the same session published 10 runtime
   contracts the web surface can consume; Artifact Export consumes the
   document artifact renderer (`41f37cc2`).
3. `SpecExport.tsx` is at GC-023 hard threshold with an active exception;
   Artifact Export must land as a new sibling component, not as a
   SpecExport edit.

## Recommendation

Approve a fresh GC-018 candidate for Tranche 1 with the depth allocation
below. Defer Tranche 2 (deep work on the placeholders) until Tranche 1
ships and produces end-user feedback.

## Tranche 1 Depth Allocation

### Primitive 1 — Artifact Export (deep)

New artifacts:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` — new sibling component (NOT an edit to `SpecExport.tsx`)
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/artifacts/page.tsx` — new dashboard route segment
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts` — new API route that invokes the document artifact renderer contract
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx` — vitest unit test
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.test.ts` — API route test
- one Playwright mock E2E asserting the export panel renders and the
  generated artifact carries the governance receipt anchor

Acceptance criteria:

- new component stays under 700 LoC (soft threshold)
- new API route stays under 700 LoC
- governed artifact output carries `Memory class`, `Status`, `Claim Boundary`, and a receipt anchor
- no edit to `SpecExport.tsx`
- vitest run green; Playwright mock E2E green
- GC-045 automated check green
- governed file size check green
- public-surface scanner green when published

### Primitive 2 — Knowledge Vault Intake (placeholder)

New artifacts:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/knowledge/intake/page.tsx` — new route segment
- a short page that points at the existing knowledge governance page, the
  knowledge vault intake runtime contract (`060e16e7`), and a "coming
  soon" boundary statement

Acceptance criteria:

- new page stays under 200 LoC
- page links to the existing `/governance/knowledge/` surface for operator
  flows so it does not duplicate that page
- page declares its placeholder nature explicitly
- no new API route, no new component beyond the page itself

### Primitive 3 — Agent Handoff UI (placeholder)

New artifacts:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/agent-handoff/page.tsx` — new route segment
- a short page that consumes `validateHandoff` from the existing validator
  (`src/lib/agent-handoff-validator.ts`) and renders the last few
  handoffs read-only

Acceptance criteria:

- new page stays under 300 LoC
- page reads from existing validator; does not introduce a new validator
  surface
- no new API route; data is sourced from existing audit data exposed by
  current admin/audit endpoints
- page declares its placeholder nature explicitly

## Hard Constraints

1. **No edit to `SpecExport.tsx`.** Already at GC-023 hard threshold.
2. **One commit per file.** Selective rollback preserved if any primitive drifts.
3. **GC-045 must pass** on every committed Markdown file.
4. **Governed file size must pass** on every committed source file.
5. **Audit-trail files stay out-of-scope** as in Tier 1/2/3 of the public
   Markdown program.
6. **No claim drift.** Existing component contracts, audit-receipt shapes,
   and provider-routing fields must be preserved verbatim.
7. **Live-governance proof is not required for Tranche 1** because
   Tranche 1 does not claim runtime governance enforcement; it claims
   governed artifact production via the already-adopted document artifact
   renderer contract.

## Risk

**Risk 1 — Scope creep into SpecExport.** The natural temptation is to
"just add a function" to `SpecExport.tsx`. Mitigation: the hard constraint
above plus a code-review requirement that any diff touching
`SpecExport.tsx` invalidates the tranche.

**Risk 2 — Placeholder pages drift into deep features.** Knowledge Vault
Intake and Agent Handoff UI must remain placeholders. Mitigation: explicit
LoC caps (200 and 300) plus a single GC-018 acceptance criterion that the
placeholder pages do not introduce new API routes.

**Risk 3 — Test infra overload.** Tranche 1 ships 3 new test files
(component, API, Playwright mock). Mitigation: tests must be small and
focused. Playwright mock E2E is one scenario, not a suite.

**Risk 4 — End-user feedback dependency.** The recommended next step
after Tranche 1 is end-user feedback before any Tranche 2 deep work.
Mitigation: closure note must capture either a feedback summary or an
explicit "not collected" note, mirroring the Tier 1 read-test pattern.

## Acceptance Criteria

- A fresh GC-018 authorization packet exists at
  `docs/baselines/CVF_GC018_WEB_INTEGRATION_TRANCHE_1_AUTHORIZATION_2026-05-??.md`.
- The audit at
  `docs/audits/CVF_WEB_INTEGRATION_TRANCHE_1_SURFACE_AUDIT_2026-05-16.md`
  is referenced.
- All new files satisfy the per-primitive acceptance criteria above.
- All tests green: `npm run test:run`, `npm run test:e2e -- --config=playwright.config.mock.ts`.
- All new Markdown passes GC-045 automated check.
- Governed file size check is green; no new entries added to the exception registry.
- Closure note exists at
  `docs/reviews/CVF_WEB_INTEGRATION_TRANCHE_1_CLOSURE_2026-05-??.md`.
- Public-surface scanner is green when published to public-sync.

## Verification

Required local checks for this tranche:

```bash
cd EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web
npm run test:run
npm run test:e2e -- --config=playwright.config.mock.ts
cd ../../..
python governance/compat/check_markdown_structural_completeness.py \
  --base origin/main --head HEAD --all-changed --enforce
python governance/compat/check_governed_file_size.py --enforce
```

## Related Artifacts

- `docs/audits/CVF_WEB_INTEGRATION_TRANCHE_1_SURFACE_AUDIT_2026-05-16.md`
- `docs/baselines/CVF_GC018_MODEL_GATEWAY_RUNTIME_AUTHORIZATION_2026-05-16.md`
- `docs/baselines/CVF_16_5_LIVING_INTEGRATION_CLASSIFICATION_SUMMARY_2026-05-16.md`
- `docs/reference/CVF_GOVERNED_DOCUMENT_ARTIFACT_RENDERING_SPEC_2026-05-16.md`
- `docs/reference/CVF_LEGACY_16_5_EXTERNAL_KNOWLEDGE_ABSORPTION_MAP_2026-05-16.md`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/SpecExport.tsx` (out-of-scope; hard constraint)
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/agent-handoff-validator.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/governance/knowledge/page.tsx`

## Claim Boundary

This proposal claims only that Tranche 1 is justified, scoped, and ready
for GC-018 authorization. It does not authorize execution. It does not
claim runtime governance enforcement. It does not extend the CVF 16.5
absorption authority beyond what the runtime-adoption tranche already
landed. Execution requires operator approval of a fresh GC-018
authorization packet, completion of the per-primitive acceptance criteria,
and publication of the closure note before public push.
