# CVF Web Integration Tranche 1 Surface Audit - 2026-05-16

Memory class: FULL_RECORD

Status: AUDIT COMPLETE - PROPOSAL READY

## Purpose

Inventory the existing `cvf-web` surface, primitives, API routes, components,
and GC-023 size posture so the Web Integration Tranche 1 proposal can target
delta extensions rather than from-zero implementations.

## Scope

Surface inventory and gap analysis for the three primitives the operator
selected for end-user audience:

- Artifact Export (deep)
- Knowledge Vault Intake (placeholder)
- Agent Handoff UI (placeholder)

This audit does not authorize implementation. It records what exists and
what each primitive needs to extend.

## Target

`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/` — the Next.js 16 / React 19
control surface that already hosts dashboard pages, admin pages, governance
pages, reports, knowledge governance, and approvals.

## Methodology

Read directory structure, count lines for components likely to be touched,
spot-check existing primitives nearest each proposed surface, and check
GC-023 exception registry status for affected files.

## Source

Primary source: the `cvf-web` Next.js workspace at
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/`. Secondary sources: the
CVF 16.5 runtime-adoption commits `8fb1f038`..`a0224426` and the
governed document artifact rendering spec at
`docs/reference/CVF_GOVERNED_DOCUMENT_ARTIFACT_RENDERING_SPEC_2026-05-16.md`.

## Protocol

For each proposed primitive, the audit (a) finds the nearest existing
surface in `cvf-web`, (b) counts lines against the GC-023 thresholds, (c)
checks the exception registry, and (d) names the runtime contract the
primitive would consume from the 10 adopted in this session.

## Findings

### Existing surfaces nearest each primitive

| Proposed primitive | Closest existing surface | LoC |
| --- | --- | ---: |
| Artifact Export | `src/components/SpecExport.tsx` (existing export component) | 1280 |
| Artifact Export | `src/app/reports/compliance/page.tsx` (compliance report) | 173 |
| Knowledge Vault Intake | `src/app/(dashboard)/governance/knowledge/page.tsx` | 380 |
| Knowledge Vault Intake | `src/app/api/admin/knowledge/collections/route.ts` (API) | (existing API) |
| Agent Handoff UI | `src/lib/agent-handoff-validator.ts` (validator) | 283 |
| Agent Handoff UI | No existing dashboard page (gap) | n/a |

### GC-023 size posture for components likely touched

| File | LoC | Class | Soft | Hard | Status |
| --- | ---: | --- | ---: | ---: | --- |
| `SpecExport.tsx` | 1280 | `frontend_component` | 700 | 1000 | ACTIVE_EXCEPTION (in registry) |
| `governance/knowledge/page.tsx` | 380 | `frontend_component` | 700 | 1000 | within soft |
| `reports/compliance/page.tsx` | 173 | `frontend_component` | 700 | 1000 | within soft |
| `agent-handoff-validator.ts` | 283 | `general_source` | 700 | 1000 | within soft |

Critical: `SpecExport.tsx` already exceeds the hard threshold and carries an
exception. Tranche 1 must NOT add code to that file. Artifact Export must
land as a new sibling component, not as a SpecExport extension.

### Test infrastructure

- Vitest configured (`vitest.config.ts`)
- Playwright configured with two configs (`playwright.config.ts`, `playwright.config.mock.ts`)
- Component-level tests exist (`SpecExport.test.tsx`, `AppBuilderWizard.test.tsx`)
- `agent-handoff-validator.test.ts` exists for the handoff validator

This is a healthy baseline. New primitives can ship with unit + mock E2E,
and the live-governance E2E lane is already wired for the release-gate
bundle.

### API route patterns

The `src/app/api/` tree already has:

- `admin/audit`, `admin/audit-feed`
- `admin/knowledge/collections/*` (vault intake API surface partly exists)
- `approvals/*`
- `reports/compliance/*` (referenced by reports page)

This means Knowledge Vault Intake has a partial API substrate already; only
the public-facing intake form and receipt UI need delta. Artifact Export
needs a new `/api/artifacts/export/...` family. Agent Handoff UI can read
the validator output via a new `/api/agent-handoff/...` family or by
embedding the validator client-side.

### Runtime adoption from this session

Codex's session adopted 10 runtime contracts that the web surfaces can wire
to:

| Adopt commit | Contract |
| --- | --- |
| `8fb1f038` | model gateway runtime primitives |
| `c124581e` | controlled memory runtime |
| `029f9ebb` | tool call trace sandbox |
| `cb201fa7` | agent boundary delegation |
| `b152b162` | MCP business adapter |
| `fb348ba1` | observability delta signal |
| `060e16e7` | knowledge vault intake |
| `41f37cc2` | document artifact renderer |
| `9e392aef` | OpenSpec change adapter |
| `a0224426` | governed skill evolution loop |

The Artifact Export deep primitive should consume the document artifact
renderer contract (`41f37cc2`). Knowledge Vault Intake placeholder should
point at the knowledge vault intake contract (`060e16e7`). Agent Handoff
UI placeholder should consume the agent boundary delegation contract
(`cb201fa7`).

## Risk

- **SpecExport size constraint.** `SpecExport.tsx` has `approvedMaxLines:
  1300` in the exception registry and is already at 1280 lines — only 20
  lines remain before the approved cap is breached. Any edit risks a GC-023
  violation immediately. Mitigation: new sibling component
  `ArtifactExportPanel.tsx` plus a new route, not an edit to SpecExport.
- **Knowledge governance page complexity.** The existing knowledge page
  already mixes compile/maintain/refactor flows; adding intake there risks
  audience confusion. Mitigation: separate route segment for non-coder
  intake under `/(dashboard)/knowledge/intake/` rather than nesting under
  `governance/`.
- **No dashboard page for agent handoff.** Building a deep agent-handoff
  dashboard is out of scope for Tranche 1. Mitigation: placeholder is a
  read-only "what would appear here" page that consumes the validator and
  shows last 5 handoffs from existing audit data.
- **Live governance proof requirement.** Any primitive that claims
  governance behavior on the public surface must run against the live
  release-gate bundle. Tranche 1 does not claim governance enforcement —
  only "governed artifact export" which is already covered by the
  document artifact renderer contract.

## Decision

Surface audit confirms Tranche 1 is feasible as a delta tranche, not a
from-zero implementation. Each primitive has at least one adjacent existing
surface and one adopted runtime contract to consume.

Recommended primitive depth allocation:

- Artifact Export: deep (new component + new route + new API + tests)
- Knowledge Vault Intake: placeholder (new route segment, pointer to
  governed intake contract, no new API)
- Agent Handoff UI: placeholder (new route segment, read-only handoff
  visibility from existing validator, no new API)

## Verification

Commands used during this audit:

```bash
find src/app -name "page.tsx"
find src/app/api -name "route.ts"
wc -l <component>
grep -rln 'SpecExport|ArtifactExport' src/components
```

## Related Artifacts

- `docs/baselines/CVF_GC018_MODEL_GATEWAY_RUNTIME_AUTHORIZATION_2026-05-16.md`
- `docs/baselines/CVF_16_5_LIVING_INTEGRATION_CLASSIFICATION_SUMMARY_2026-05-16.md`
- `docs/reference/CVF_GOVERNED_DOCUMENT_ARTIFACT_RENDERING_SPEC_2026-05-16.md`
- `governance/compat/CVF_GOVERNED_FILE_SIZE_EXCEPTION_REGISTRY.json`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/SpecExport.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/governance/knowledge/page.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/agent-handoff-validator.ts`

## Claim Boundary

This audit claims only that the inventory above reflects the current
`cvf-web` state as of 2026-05-16 and that the recommended depth allocation
fits the existing surface. It does not authorize implementation, does not
claim a primitive will pass live-governance proof, and does not commit to
landing all three primitives in a single tranche if any one of them needs
additional time.
