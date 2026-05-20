# CVF Web Integration Tranche 2 Proposal - 2026-05-16

Memory class: FULL_RECORD

Status: PROPOSAL — awaiting execution; GC-018 authorization granted at
`docs/baselines/CVF_GC018_WEB_INTEGRATION_TRANCHE_2_AUTHORIZATION_2026-05-16.md`

## Purpose

Define scope, depth allocation, and acceptance criteria for Web
Integration Tranche 2. Tranche 1 shipped Artifact Export (deep) plus
two functional placeholders (Knowledge Vault Intake, Work Transfer).
Tranche 2 promotes both placeholders to deep primitives, adds a live
governance proof layer to Artifact Export, and completes the end-user
web integration roadmap.

## Scope

Tranche 2 is a **deep tranche** across three workstreams:

1. **Artifact Export — live governance proof layer**
   Add a release-gate bundle check to the existing export flow so the
   "HTML presentation candidate" claim can be upgraded to "governed
   artifact generation" in a future closure note. This workstream does
   not change `ArtifactExportPanel.tsx` or the API route logic; it
   adds a proof integration layer only.

2. **Knowledge Vault Intake — promote to deep**
   Convert `knowledge/intake/page.tsx` from a preview-and-pointer
   page into a functional intake form that submits to the existing
   `/api/admin/knowledge/collections` API substrate, shows a receipt
   on success, and links the receipt to the Artifact Export flow.

3. **Work Transfer — promote to deep**
   Convert `work-transfer/page.tsx` from a client-side validator demo
   into a page that reads recent work transfer records from the
   existing `/api/admin/audit` endpoints, presents them in a read-only
   list, and allows the user to export a selected record as an HTML
   review packet via `ArtifactExportPanel`.

Scope excludes:

- Any edit to `SpecExport.tsx` (still at approved cap, 20 lines
  remaining)
- New runtime contracts or runtime ownership changes
- New provider integrations beyond the existing release-gate lane
- Tranche 3 work (live QBS score display, OpenSpec packet intake)

## Target

End-user and operator audience. Primary value: "after Tranche 2, the
user can submit new knowledge for review, see recent work transfers
with context, and export any reviewed artifact as a governed HTML
packet with a live governance receipt."

## Source

- Tranche 1 closure:
  `docs/reviews/CVF_WEB_INTEGRATION_TRANCHE_1_CLOSURE_2026-05-16.md`
- Tranche 1 surface audit:
  `docs/audits/CVF_WEB_INTEGRATION_TRANCHE_1_SURFACE_AUDIT_2026-05-16.md`
- Document artifact renderer spec:
  `docs/reference/CVF_GOVERNED_DOCUMENT_ARTIFACT_RENDERING_SPEC_2026-05-16.md`
- Knowledge vault intake contract: commit `060e16e7`
- Agent boundary delegation contract: commit `cb201fa7`
- Existing API substrate:
  `/api/admin/knowledge/collections/*` (intake)
  `/api/admin/audit`, `/api/admin/audit-feed` (work transfer history)

## Findings

Tranche 1 closure confirms three surfaces are live in `cvf-web`:

- `ArtifactExportPanel.tsx` (498 LoC) — 340+ lines of headroom remain
  before soft threshold; adding a `governanceReceipt` badge is a
  ≤15-line delta.
- `knowledge/intake/page.tsx` (166 LoC) — 184 lines of headroom to
  the 350-LoC cap; submit + receipt flow fits within that budget.
- `work-transfer/page.tsx` (184 LoC) — 216 lines of headroom to the
  400-LoC cap; audit history panel + export pre-population fits.

Existing API substrate required by each workstream is confirmed
present:

- `/api/admin/knowledge/collections` — collections CRUD (intake
  substrate)
- `/api/admin/audit`, `/api/admin/audit-feed` — audit event feed
  (work transfer history substrate)
- `/api/governance/evaluate` — governance evaluate endpoint (proof
  layer substrate)

No new runtime contracts needed. No new API routes needed.

## Decision

Promote both placeholders to deep, add live proof layer to Artifact
Export. Defer Tranche 3 (OpenSpec intake, live QBS display) until
Tranche 2 ships and end-user feedback is collected.

## Depth Allocation

### Workstream 1 — Artifact Export live proof layer

New artifacts:

- `src/app/api/artifacts/export/proof.ts` — release-gate bundle
  integration module; calls governance evaluate endpoint and attaches
  a `governanceReceipt` field to the export response when a live run
  is available; no-ops gracefully in local/mock mode
- `src/app/api/artifacts/export/proof.test.ts` — unit test covering
  live path and no-op path

Changes to existing files:

- `src/app/api/artifacts/export/route.ts` — import `proof.ts` and
  attach `governanceReceipt` to response when present (≤ 10 line
  delta; stays well within 700 LoC)
- `src/components/ArtifactExportPanel.tsx` — display
  `governanceReceipt` badge when present in API response (≤ 15 line
  delta; stays well within 700 LoC)

Acceptance criteria:

- `proof.ts` ≤ 200 LoC
- When a live governance receipt is present, export HTML includes a
  `governance-receipt` section and the UI shows a "Governed" badge
- When no live receipt is available (local/mock), export proceeds
  normally with "HTML presentation candidate" claim unchanged
- `proof.test.ts` covers both paths
- Governed file size check green; no new exception registry entries

### Workstream 2 — Knowledge Vault Intake (deep)

Changes to existing file:

- `src/app/(dashboard)/knowledge/intake/page.tsx` — extend the
  existing 166-LoC page with a submit button that POSTs to
  `/api/admin/knowledge/collections`, shows a success receipt with
  collection ID, and links to Artifact Export; stays ≤ 350 LoC

New artifacts:

- `src/app/(dashboard)/knowledge/intake/page.test.tsx` — vitest
  component test covering form submit, success receipt render, and
  error state

Acceptance criteria:

- Page stays ≤ 350 LoC after extension
- Submit calls `/api/admin/knowledge/collections` with correct payload
- Success receipt displays collection ID and links to Artifact Export
- Error state shown when API returns non-2xx
- Bilingual EN/VI preserved
- No new API route (uses existing substrate)
- Component test green

### Workstream 3 — Work Transfer (deep)

Changes to existing file:

- `src/app/(dashboard)/work-transfer/page.tsx` — add a read-only
  history panel that fetches recent records from `/api/admin/audit`,
  renders them in a list (timestamp, action, actor), and offers an
  "Export as HTML" button that pre-populates `ArtifactExportPanel`
  with the selected record; stays ≤ 400 LoC

New artifacts:

- `src/app/(dashboard)/work-transfer/page.test.tsx` — vitest component
  test covering history fetch, empty state, and export pre-population

Acceptance criteria:

- Page stays ≤ 400 LoC after extension
- History panel fetches from existing `/api/admin/audit`; empty state
  shown when no records returned
- "Export as HTML" pre-populates `ArtifactExportPanel` without
  navigation — panel appears inline below the selected record
- Bilingual EN/VI preserved
- No new API route
- Component test green

## Hard Constraints

1. **No edit to `SpecExport.tsx`.** Still at 1280 lines against
   `approvedMaxLines: 1300`.
2. **One commit per file.** Selective rollback preserved.
3. **GC-045 must pass** on every committed Markdown file.
4. **Governed file size must pass** — no new exception registry entries.
5. **Claim boundary upgrade is conditional.** Artifact Export may only
   claim "governed artifact generation" in the closure note if a live
   governance receipt is actually attached in a test run. If the proof
   layer is present but no live receipt is produced in CI, the claim
   stays "HTML presentation candidate."
6. **No new runtime contracts.** All API calls must use existing
   endpoints already in the `cvf-web` API tree.

## Risk

**Risk 1 — Knowledge intake API substrate gap.** The
`/api/admin/knowledge/collections` route exists but its request schema
may not match the intake form fields exactly. Mitigation: read the
route before building the form; adapt field names to match existing
schema rather than changing the API.

**Risk 2 — Audit endpoint shape.** The `/api/admin/audit` endpoint
returns a feed but the exact record shape is not confirmed. Mitigation:
read `admin/audit/route.ts` before building the history panel; render
only the fields that are present.

**Risk 3 — Live proof integration brittleness.** The proof layer
must no-op cleanly in local/mock mode. Mitigation: proof module is
imported conditionally; if governance evaluate returns a non-2xx or
times out, export proceeds without `governanceReceipt`.

**Risk 4 — LoC budget.** Promoting two 166-LoC and 184-LoC pages to
deep may push them past the soft threshold if scope creeps. Mitigation:
explicit LoC caps (350 and 400); if a page would exceed its cap a new
sibling component must be extracted instead.

## Acceptance Criteria

- All new and modified files satisfy the per-workstream criteria above.
- All tests green: `npm run test:run`.
- Governed file size check green.
- GC-045 passes on all new Markdown files.
- Closure note exists at
  `docs/reviews/CVF_WEB_INTEGRATION_TRANCHE_2_CLOSURE_2026-05-??.md`
  with explicit statement of whether "governed artifact generation"
  claim is unlocked or deferred.
- Public-surface scanner green when published to public-sync.

## Verification

```bash
cd EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web
npm run test:run
cd ../../..
python governance/compat/check_governed_file_size.py --enforce
python governance/compat/check_markdown_structural_completeness.py \
  --base origin/main --head HEAD --all-changed --enforce
```

## Related Artifacts

- `docs/reviews/CVF_WEB_INTEGRATION_TRANCHE_1_CLOSURE_2026-05-16.md`
- `docs/baselines/CVF_GC018_WEB_INTEGRATION_TRANCHE_2_AUTHORIZATION_2026-05-16.md`
- `docs/audits/CVF_WEB_INTEGRATION_TRANCHE_1_SURFACE_AUDIT_2026-05-16.md`
- `docs/reference/CVF_GOVERNED_DOCUMENT_ARTIFACT_RENDERING_SPEC_2026-05-16.md`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/knowledge/intake/page.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/work-transfer/page.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx`

## Claim Boundary

This proposal claims only that Tranche 2 is scoped, justified, and
ready for execution under the GC-018 authorization. It does not claim
that any file has been implemented, does not upgrade Artifact Export
from "HTML presentation candidate" to "governed artifact generation"
(that upgrade is conditional on live proof in the closure note), and
does not authorize Tranche 3 work. Execution requires completion of all
per-workstream acceptance criteria and publication of the closure note.
