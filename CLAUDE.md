# CLAUDE.md

Provider-local operating guidance for Claude Code (claude.ai/code) in this
repository.

## Authority Boundary

`CLAUDE.md` is `NOT_CVF_SOURCE`. It is a provider-local execution aid, not CVF
source of truth, and must never be cited as canonical authority in Source
Authority tables, Source Verification ACCEPT rows, corpus manifests, closure
proof, or roadmap/work-order evidence.

Canonical CVF authority lives in `AGENTS.md`, the canonical routing index
`docs/reference/CVF_AGENT_INSTRUCTION_CARRIER_ROUTING_INDEX_2026-08-11.md`,
standards under `docs/reference/`, and governed roadmaps, baselines, work
orders, reviews, registries and checkers. Read `AGENTS.md` for the governing
rules; this file only records how to operate the repository as a provider.

Any fact learned here must be re-verified against a CVF-governed surface before
use as evidence.

## Session Startup

Before material governed work in a new or resumed session, read the compact
front door `CVF_SESSION_MEMORY.md`, then its bootstrap read model
`CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`, then the active handoff
those surfaces name. Resolve the full state registry
`CVF_SESSION/ACTIVE_SESSION_STATE.json` only as a targeted lookup, when a
current fact is missing, contradictory, or the task explicitly requires
historical evidence.

State one concise startup acknowledgment naming current mode, active handoff,
next allowed move, and any parked operator checkpoint, per the startup contract
in `AGENTS.md`.

Do not treat archived handoffs under `CVF_SESSION/handoffs/archive/` as current
until the active state registry points to them.

## Governance Rules Routing

Every mandatory governance rule is owned by a CVF-governed surface, not by this
file. Resolve owners through `AGENTS.md` and the routing index. Two carrier
bindings are required directly here by existing machine readers:

- `governance/compat/check_corpus_completeness_report_integrity.py`
- `governance/compat/check_corpus_to_knowledge_map_reconciliation.py`

Before claiming a complete scan, inventory, or "all files read", satisfy the
corpus completeness standard. Before claiming a corpus-derived knowledge map or
retrieval readiness, satisfy the reconciliation standard. Bare `rg --files` is
not completeness evidence; use `rg --files --hidden --no-ignore`.

## Commands

Web UI (`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/`):

```bash
npm run dev           # Dev server at localhost:3000
npm run build         # Production build
npm run lint          # ESLint (max-warnings=0, must be clean)
npm run test:run      # Unit tests once (Vitest)
npm run test:coverage # Coverage report
npm run test:e2e      # Playwright E2E tests
```

Guard Contract SDK (`EXTENSIONS/CVF_GUARD_CONTRACT/`):

```bash
npm test              # Vitest run
npm run check         # TypeScript type check
```

Conformance and automation (Python, from repo root):

```bash
python scripts/run_cvf_cross_extension_conformance.py
python scripts/run_cvf_conformance_release_gate.py
```

Workspace bootstrap (PowerShell) - creates a sibling project workspace; do not
develop inside the CVF root:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\new-cvf-workspace.ps1 `
  -WorkspaceRoot "D:\CVF-Workspace" -ProjectName "My-Project"
```

## Architecture Pointers

Layer model L0-L5, module inventory, and authority hierarchy are documented in
CVF-governed surfaces rather than restated here:

| Topic | Owner |
|---|---|
| Architectural map | `docs/CVF_CORE_KNOWLEDGE_BASE.md` |
| Module inventory | `docs/reference/CVF_MODULE_INVENTORY.md` |
| Governance control matrix | `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md` |
| Architecture decisions | `docs/CVF_ARCHITECTURE_DECISIONS.md` |
| New to CVF | `docs/guides/CVF_QUICK_ORIENTATION.md` |
| Cheat sheet | `docs/CHEAT_SHEET.md` |
| UI / Web design contract | `DESIGN.md` |

Frozen layers `v1.0/` and `v1.1/` and `ECOSYSTEM/doctrine/` must not be
modified. The CVF root is maintenance-only; user projects are siblings.

## Web UI Notes

Next.js App Router: never read `localStorage` in a `useState()` initializer, as
it causes hydration mismatch; initialize with a static default and apply
`localStorage` in `useEffect`. In `globals.css`, Google Fonts `@import url(...)`
must appear before `@import "tailwindcss"`.

The `App onboarding/` folder at repo root holds the official UI design mockups;
consult the matching file before redesigning a platform page.

## Repository And Public-Sync Boundary

This workspace is the private provenance repository. Run `git remote -v` before
any push intended for the public repository.

When syncing to the public-sync clone, never copy `AGENT_HANDOFF*.md`,
`docs/baselines/`, `docs/reviews/`, or `docs/roadmaps/`. Use an explicit file
list; never `git add -A` or copy whole directories. Public-sync requires
separate authorization.

Every delivered capability tranche must update the public technical catalog
before closing, per the public catalog update rule in the governed catalog
surface. Verify every new or modified path from the public-sync clone before
committing there.

## Claim Boundary

This file is provider-local operating guidance only. It defines no governance
semantics, overrides no canonical standard or machine checker, and makes no
runtime, live-proof, deployment, public-sync, or production readiness claim.
Historical pre-compaction text is preserved as evidence at
`docs/reference/archive/CLAUDE_FULL_PRE_T2B_2026-08-11.md`, which is
`NOT_ACTIVE_AUTHORITY`.
