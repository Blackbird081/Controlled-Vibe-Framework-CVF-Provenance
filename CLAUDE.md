# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Session Memory Front Door

Before material governed work in a new or resumed session, read
`CVF_SESSION_MEMORY.md`, then resolve
`CVF_SESSION/ACTIVE_SESSION_STATE.json`.

Do not treat archived handoffs under `CVF_SESSION/handoffs/archive/` or any
versioned root handoff as current until the active state registry points to it.
State or internally confirm the active session mode, active handoff path,
required first reads, blocked work classes, and next allowed move before
continuing.

## Mandatory Startup Acknowledgment

Before material governed work in any new or resumed session, state to the
operator or record in the active handoff/session state one concise startup
acknowledgment naming current mode, active handoff, next allowed move, and any
parked operator checkpoint.

Suggested format:

`Startup acknowledged: current mode=<mode>; active handoff=<handoff>; next allowed move=<summary>; parked checkpoint=<none|summary>.`

This is a soft-accountability requirement only. It does not claim runtime
auto-load, universal tool support, MCP availability, or hidden cross-agent
memory transfer. Trivial direct answers may keep the confirmation internal, but
roadmap, implementation, review, live run, commit, handoff, or public-sync work
must satisfy it first.

## What This Repository Is

**Controlled Vibe Framework (CVF)** is a governance-first control plane for AI-assisted software development. It is not a code library — it is a governance framework with executable controls, process standards, and multi-layer architecture (L0–L5). The core workflow is: `INTAKE → DESIGN → BUILD → REVIEW → FREEZE`.

**Current branch:** `cvf-next` (development). **Main branch:** `main` (production).

## Mandatory Live Run Diagnostics

Before rerunning any failed, partial, timed-out, empty-output, or ambiguous live
provider/API-key/service-token/CLI/MCP/browser proof, follow:

`docs/reference/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`

Record a secret-safe diagnostic with stage, class, retryability, user action,
provider/model when known, HTTP status/latency when available, receipt/trace
when available, and a safe human-readable message. Do not print raw API keys,
signed headers, bearer tokens, or unredacted provider request bodies.

For benchmark evidence with multiple events per live call, report both
call-level pass rate and event-model metric denominator.

## Mandatory Knowledge Absorption Blind-Spot Control

This applies to **all agents** (Claude, Codex, Gemini, or any future agent)
executing work that absorbs, reopens, scopes, or implements knowledge from
`.private_reference/legacy/`, archived absorption packets, external capability
sources, Review-CVF pain points, memory, graph, workflow, CLI/MCP/tool,
provider, benchmark, context, or non-coder outcome surfaces.

Before implementation, the agent must produce a Blind-Spot Control Block per
the binding standard:

`docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`

The control block must be included in the GC-018 packet or work order, with
all seven gates executed and a verdict of `CLEAR`, `PARTIAL`, or `BLOCKED`.
Tranches with `BLOCKED` verdict cannot proceed. Operator may grant a one-off
exception, which must be recorded in the GC-018 packet itself.

Do not bypass this standard by claiming "the folder was already audited," "the
summary is enough," "another agent already reviewed it," or any of the other
rationalizations in the standard's Do-Not-Bypass List.

For LHW connector waves, do not use bare `rejected: requires live route`
wording when a family is excluded only because the current wave is doc-only.
Use:

`rejected from this LHW wave (doc-only scope) - requires live route; eligible for separate live-proof roadmap post-LHW.`

This is a scope label, not a value judgment on the worker or source family.
`abtop` and `gridex` may be live-testable when API/key paths exist, but live
route execution belongs in a separate live-proof roadmap after LHW connector
absorption of remaining `PARTIALLY_ABSORBED` LH1 families is complete.

## Mandatory Work Order Source Verification

Before authoring or dispatching a CVF work order, follow the canonical template:

`docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`

If the work order names runtime/source fields, interfaces, functions, schema
keys, receipt fields, diagnostic classes, role values, route states,
template/pack IDs, policy enums, config keys, CLI/MCP tool names, existing
source paths, or MA1 section references, it must include a Source Verification
Table with source file plus verified line/section.

Use current runtime source or canonical contracts before completion reviews,
handoffs, or memory summaries. Search the repo for every named token. If a
token appears only in the draft work order, dispatch is blocked unless it is
explicitly listed as a new documentation-only field with no runtime claim.

MA1 section references must match
`docs/reference/CVF_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_STANDARD_2026-05-26.md`
exactly. Do not invent MA1 labels such as `Input Package`, `Purpose`, or
`Return Protocol`.

---

## Commands

### Web UI (`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/`)

```bash
npm run dev           # Dev server at localhost:3000
npm run build         # Production build
npm run lint          # ESLint (max-warnings=0, must be clean)
npm run test          # Unit tests (Vitest, watch mode)
npm run test:run      # Tests once
npm run test:coverage # Coverage report
npm run test:e2e      # Playwright E2E tests
```

### Guard Contract SDK (`EXTENSIONS/CVF_GUARD_CONTRACT/`)

```bash
npm test              # Vitest run
npm run test:watch    # Watch mode
npm run check         # TypeScript type check
```

### Conformance & Automation Scripts (Python, from repo root)

```bash
python scripts/run_cvf_cross_extension_conformance.py
python scripts/run_cvf_conformance_release_gate.py
python scripts/rotate_cvf_conformance_trace.py
```

### Workspace Bootstrap (PowerShell)

```powershell
# Creates a new project sibling workspace (do NOT develop inside CVF root)
powershell -ExecutionPolicy Bypass -File .\scripts\new-cvf-workspace.ps1 `
  -WorkspaceRoot "D:\CVF-Workspace" -ProjectName "My-Project"
```

---

## Architecture

### Layer Model (L0 → L5)

| Layer | Module | Role |
|---|---|---|
| L0 (Foundation) | `CVF_v3.0_CORE_GIT_FOR_AI` | AI Commit, Artifact Staging, Ledger, Process Model |
| L1 (Core) | `v1.0/`, `v1.1/` | Phases, Governance (FROZEN baselines — do not modify) |
| L1.5 (Dev Governance) | `CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL` | Hardened runtime, deterministic orchestration |
| L2 (Tools) | `CVF_ECO_v1.0`–`v1.4` | Validation, NL Policy, LLM Risk Engine, RAG Pipeline |
| L2.5 (Safety Runtime) | `CVF_v1.7`–`v1.9` | Reasoning Gate, Entropy Guard, Mutation Sandbox, Execution Recording |
| L3 (Platform) | `CVF_v1.6_AGENT_PLATFORM` | Web UI (Next.js), Agent Tools, Template Marketplace |
| L4 (Safety UI) | `CVF_v1.7.2` | Risk visualization, Policy simulation, Domain map |
| L5 (Adapter Hub) | `CVF_v1.7.3` | LLM/Runtime/Tool/Memory/Policy contracts |

### Authority Hierarchy

```
ECOSYSTEM/doctrine/          ← L0 Supreme layer (FROZEN — never touch)
    ↓ governs
ECOSYSTEM/operating-model/   ← L3 Operational model for humans
    ↓ governs
governance/ + docs/ + EXTENSIONS/  ← Engineering implementation
    ↓ verified by
tests/ + governance/compat/  ← Conformance verification
    ↓ evidenced in
docs/reviews/ + CHANGELOG    ← Audit trail
```

### Key Directory Purposes

- **`ECOSYSTEM/`** — Meta layer (WHY & WHAT). `doctrine/` is FROZEN supreme governance. `operating-model/` is VOM for human operators.
- **`EXTENSIONS/`** — All 36+ implementation modules. Each versioned module is self-contained with its own tests.
- **`governance/toolkit/05_OPERATION/`** — 34 operational guard files. These are the enforcement contracts.
- **`docs/`** — Engineering documentation hub: `concepts/`, `guides/`, `reference/`, `reviews/`, `roadmaps/`, `baselines/`.
- **`v1.0/`, `v1.1/`** — Frozen baseline layers. **Do not modify.**
- **`scripts/`** — 72 Python/PowerShell automation scripts for conformance, governance, and workspace management.
- **`tools/`** — CLI utilities: skill validation, skill search, security scanning.

### Web UI Stack (`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/`)

- Next.js 16.1.6, React 19.2.3, TypeScript 5, TailwindCSS 4
- Zod 4 for validation, React Hook Form 7
- NextAuth.js 5 (beta) for RBAC (Owner/Admin/Developer/Reviewer/Viewer)
- Vitest for unit tests, Playwright for E2E
- Deployed via Netlify (config: `netlify.toml`)

### Landing Page Component Architecture (`src/app/landing/`)

The `/landing` route is a standalone public page split into dedicated components (GC-023 compliance, each <200 lines):

```
landing/
  page.tsx                       # Shell: imports + bilingual state (lang: 'vi'|'en')
  components/
    HeroVisualizer.tsx            # Animated chat conversation (client, cycling)
    SocialProof.tsx               # Avatar strip + brand logos
    TestimonialCards.tsx          # 3 cards mint/sky/pink + star ratings
    TemplateShowcase.tsx          # 4 template cards with hover-lift
    InsideVibCode.tsx             # Pathway cards 2×2 + tab switcher (client)
    WorkflowVisualizer.tsx        # CVF pipeline reveal + accordion (client)
```

All landing components receive `lang: 'vi' | 'en'` as prop from page.tsx state. Never read `localStorage` in a `useState()` initializer in Next.js App Router — it causes hydration mismatch. Always initialize with a static default then apply `localStorage` in `useEffect`.

**CSS rule:** Google Fonts `@import url(...)` must appear **before** `@import "tailwindcss"` in `globals.css`, otherwise the CSS optimizer emits a warning and the font may not load.

### App Onboarding Design Reference (`App onboarding/`)

The `App onboarding/` folder at repo root contains HTML/JSX mockups that are the **official UI design reference** for all platform pages. When redesigning any page inside the app, consult the matching file first:

| File | Covers |
|---|---|
| `cvf-pages-landing.jsx` | About CVF / landing tab |
| `cvf-pages-home.jsx` | Home — template gallery |
| `cvf-pages-workspace.jsx` | Skills, Skill Search, Help, Docs |
| `cvf-pages-ai.jsx` | AI Agent, Multi-Agent, Tools, Simulation, Knowledge |
| `cvf-pages-platform.jsx` | History, Analytics, Marketplace, Governance, Safety |
| `cvf-pages-account.jsx` | User profile, Settings, AI Usage |
| `cvf-sidebar.jsx` | Navigation sidebar structure |
| `cvf-theme.jsx` | Design tokens, shared icons (57+), reusable components |

These files use inline React styles — when porting to the Next.js app, translate to Tailwind classes. The design tokens in `cvf-theme.jsx` (`makeTheme`) map to the app's `indigo-600` accent and `gray-950` dark background.

---

## Governance Controls to Know

**Fast Lane (GC-021):** Low-risk work can bypass full governance with a Fast Lane audit. Check `docs/reference/CVF_FAST_LANE_AUDIT_TEMPLATE.md`.

**Continuation Governance (GC-018):** Agent handoff and stopping rules. See `docs/reference/CVF_GC018_CONTINUATION_CANDIDATE_TEMPLATE.md`.

**Memory Classification (GC-022):** Records are classified as FULL / SUMMARY / POINTER. See `docs/reference/CVF_MEMORY_RECORD_CLASSIFICATION.md`.

**File Size Guard (GC-023):** All governed source, test, frontend, and markdown files have hard line-count thresholds. Policy: `governance/toolkit/05_OPERATION/CVF_GOVERNED_FILE_SIZE_GUARD.md`. Exception registry: `governance/compat/CVF_GOVERNED_FILE_SIZE_EXCEPTION_REGISTRY.json`. **Before adding tests, code, or continuity text to any existing file:** (1) check the current line count, (2) check the exception registry for that file's `approvedMaxLines` and `requiredFollowup`, (3) if the file is near its hard threshold, rotate/archive/split it or materially shrink it in the same batch, (4) if adding would exceed the limit, create a dedicated file instead. Do not compress prose merely to fit under the guard. Front doors and handoffs must open a compact pointer/successor/archive when they approach threshold. The pre-commit hook (`.githooks/pre-commit` → `governance/compat/run_local_governance_hook_chain.py`) automatically enforces this at every `git commit` — no manual run needed.

**Latest-Closure Continuity Gate:** Before claiming any connector wave closed, run the autorun `pre-closure` gate and ensure the highest closed LHW wave in `CVF_SESSION/ACTIVE_SESSION_STATE.json` is also named in `nextAllowedMove`, `CVF_SESSION_MEMORY.md` `Next Allowed Move`, and the active handoff. Stale lower-wave text such as LHW6/LHW8 after LHW9 closure blocks closure even when specs pass.

**Closure Finality Gate:** A closed-equivalent work order, roadmap, Fast Lane audit, completion, or connector spec must not retain `| OPEN |` table rows, unchecked `- [ ]` checklist items, stale roadmap `WORK_ORDER_READY`/`HOLD until` residue, or `Status: ACTIVE` paired with pass/approve disposition.

**Risk Model:** R0 (Safe) → R3 (Dangerous). All changes are classified before execution.

---

## CI/CD

GitHub Actions (`.github/workflows/`):
- **`cvf-ci.yml`** — Main pipeline: Guard Contract tests (Vitest) + MCP ECO v2.5 tests (71) + Web UI TypeScript check. Requires all-pass gate.
- **`cvf-web-ci.yml`** — Web changes: Python conformance check → Lint → Build → Unit tests → Coverage gate.
- **`cvf-extensions-ci.yml`** — Extensions CI for EXTENSIONS/ changes.

---

## Workspace Isolation Rule

The CVF root is **maintenance-only**. User projects must be created as **sibling directories**, not inside this repo. Use `scripts/new-cvf-workspace.ps1` to bootstrap new projects correctly.

---

## Public-Sync Rule (CRITICAL)

When syncing changes from this governance repo to `Controlled-Vibe-Framework-CVF-public-sync`, the following artifact classes must **never** be copied or pushed to the public repo:

| Pattern | Class |
|---|---|
| `AGENT_HANDOFF*.md` | Internal Codex execution briefs |
| `docs/baselines/` | GC-018 authorization records |
| `docs/reviews/` | Internal audit and review records |
| `docs/roadmaps/` | Internal implementation roadmaps and Codex specs |

These are enforced by `.gitignore` in the public-sync repo. When performing a manual sync (copy files then commit), always use an explicit file list — never `git add -A` or copy entire directories. Only copy: source code, test files, and curated public documentation (`ARCHITECTURE.md`, `CONTRIBUTING.md`, `README.md`, `PROVENANCE.md`, `docs/guides/`, `docs/concepts/`, `docs/reference/` where appropriate).

---

## Public Catalog Update Rule (GC-024 candidate) — BINDING

**Every agent that delivers a new capability tranche must update the
public technical catalog before closing the tranche.**

Public catalog location (public-sync repo):
`docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md`

### Why this rule exists

CVF v4.0.0 delivered 130+ W-series tranches but did not surface them in
the public catalog. An external reviewer in 2026-05-17 concluded that
CVF's CLI, benchmark, and Skill/Provider/Memory foundations did not
exist — because the catalog did not mention them. **The 3 factual errors
in Review CVF.md are a documentation failure, not a reviewer failure.**
This rule prevents recurrence.

### What must be updated

1. **New proven capability** → add a row to the capability table with
   `proven` status and a verified evidence path.
2. **New or significantly extended extension** → add or update the
   extension inventory row (R2 section when added).
3. **Row status upgrade** (`roadmap` → `partially absorbed` → `proven`)
   → update the row and replace with a concrete evidence link.
4. **New delivery tranche at GA/RC level** → update the Delivery History
   Summary paragraph (R3 section when added) with the tranche name and
   date.

### Verification before every public-sync commit

Run `Test-Path` on **every new or modified path** in the catalog from
the public-sync clone, not the governance repo. Copying provenance paths
without re-verification in public-sync is the N-1 failure mode — it has
caused broken links before.

### Sections delivered (GC-018 authorized and complete — 2026-05-19)

All three catalog enrichment sections are now present in the public
catalog (public-sync commit `08ffda44`):

- R1 — "What CVF Can Do Today" (5 outcomes, each with verified evidence path)
- R2 — Key Extensions inventory table (8 extensions, plain-language)
- R3 — "Maturity and Delivery History" paragraph (v4.0.0 GA, 130+ tranches)

Authorization: `docs/baselines/CVF_GC018_CATALOG_FIRST_CLASS_GOVERNED_ARTIFACT_2026-05-18.md`
Test-Path: 15/15 PASS (verified in public-sync clone before commit)

Future catalog updates follow the Update Rule above. Any new
section additions require a fresh GC-018.

---

## Key Reference Documents

| Purpose | Document |
|---|---|
| New to CVF | `docs/guides/CVF_QUICK_ORIENTATION.md` |
| Getting started (VN + EN) | `docs/GET_STARTED.md` |
| Architectural map | `docs/CVF_CORE_KNOWLEDGE_BASE.md` |
| Current release status | `docs/reference/CVF_RELEASE_READINESS_STATUS_2026-03-20.md` |
| Module inventory | `docs/reference/CVF_MODULE_INVENTORY.md` |
| Governance control matrix | `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md` |
| Architecture decisions | `docs/CVF_ARCHITECTURE_DECISIONS.md` |
| Cheat sheet | `docs/CHEAT_SHEET.md` |
