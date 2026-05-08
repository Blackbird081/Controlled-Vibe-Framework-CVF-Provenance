<!-- Memory class: FULL_RECORD -->
# CVF RC2 Foundation Roadmap Draft: Productized Runtime + Web Control Surface

**For:** Claude rebuttal before execution  
**Date:** 2026-05-08  
**Status:** DRAFT FOR REVIEW — NOT AUTHORIZED FOR IMPLEMENTATION  
**Authority basis:** RC1 boundary after `v4.0.0-rc.1`, README/ARCHITECTURE claims, WPR-1 through WPR-4 closure state  

## Executive Decision

Do **not** open a GA roadmap yet.

Before CVF can honestly optimize non-coder UX or developer DX, two foundation
gaps must be closed:

1. **Productized runtime install:** a fresh clone must be diagnosable,
   configurable, and runnable with low friction.
2. **Web control surface:** CVF Web must expose the runtime's module health,
   provider readiness, governance gates, and evidence surfaces, not only the
   active non-coder `/api/execute` path.

This draft is a **foundation roadmap candidate**, not a GA/community adoption
roadmap. It should be challenged before any GC-018 authorization.

---

## Part 1 — Current Truth Boundary

### What RC1 Can Claim

- Public RC tag and GitHub Release exist: `v4.0.0-rc.1`.
- Core modules are present in the repository.
- The active governed AI path is live-proven.
- Trusted-form non-coder web flow is live-usable under the W149 evidence
  boundary.
- Mandatory release proof uses live provider API calls.

### What RC1 Must Not Claim

- CVF Web is a full operations console for every CVF runtime module.
- Fresh clone setup is zero-friction for ordinary community users.
- Every provider lane, extension, or legacy template has uniform runtime
  quality.
- The project is GA-ready.

---

## Part 2 — Roadmap Shape

**Code:** `RC2-F` (Release Candidate 2 Foundation), 7 waves.

Each wave requires a separate GC-018 authorization before implementation.
Execution should stop after each wave for closure decision and evidence review.

| Wave | Purpose | Primary Outcome |
|---|---|---|
| RC2-F0 | Foundation reality audit | Exact install/web-control gap baseline |
| RC2-F1 | One-command doctor | Clone readiness can be checked locally |
| RC2-F2 | Env + provider validation | Key/model/provider failures become explicit |
| RC2-F3 | Web runtime health surface | User sees system readiness in the browser |
| RC2-F4 | Module registry + facade contract | Web can enumerate core runtime modules |
| RC2-F5 | Governance gate/evidence web surface | Gates and evidence become inspectable from Web |
| RC2-F6 | Zero-friction setup path | New user can go clone → configured → first proof |

---

## Part 3 — Detailed Waves

### RC2-F0 — Foundation Reality Audit

**Why:** Avoid another speculative roadmap. Confirm the actual install and web
control gaps before changing code.

**Scope:**

1. Fresh clone smoke audit on at least one clean local path.
2. Record dependency expectations: Node, npm, Python, Playwright, provider keys,
   ports, writable state paths.
3. Map which runtime modules are currently web-visible vs CLI/doc-only:
   - Web/non-coder app
   - Guard contract
   - Phase governance runtime
   - Control Plane Foundation
   - Execution Plane Foundation
   - Governance Expansion Foundation
   - Learning Plane Foundation
   - Model Gateway
   - Policy Engine
   - Trust Sandbox
4. Produce a gap matrix:
   - `PRESENT`
   - `RUNNABLE_CLI_ONLY`
   - `WEB_VISIBLE_READ_ONLY`
   - `WEB_RUNNABLE`
   - `NOT_EXPOSED`
5. Decide whether RC2-F1 through RC2-F6 need reordering.

**Artifacts:**

- `docs/reviews/CVF_RC2_FOUNDATION_REALITY_AUDIT_2026-05-08.md`

**Verification:**

- No runtime changes.
- Audit findings classified as `MUST_FIX`, `ACCEPTED_BOUNDARY`, or `DEFERRED`.
- Release gate remains PASS if run.

**Boundary:** Audit only. No installer, Web UI, or runtime facade changes.

---

### RC2-F1 — One-Command Runtime Doctor

**Why:** A user should know whether their clone can run before they touch the
Web app.

**Scope:**

1. Add a single command such as:

   ```bash
   python scripts/cvf_doctor.py --json
   ```

2. Check:
   - OS and shell family
   - Node/npm availability
   - Python availability
   - key repo paths
   - `cvf-web` package availability
   - Playwright/browser readiness where applicable
   - common port availability
   - writable runtime/state paths
   - git hook availability
3. Emit machine-readable JSON and human-readable summary.
4. Do **not** require provider keys for basic readiness.
5. Return non-zero only for real blockers, not optional live-provider absence.

**Artifacts:**

- `scripts/cvf_doctor.py`
- Targeted tests for doctor classification
- README/deploy-guide link updates

**Verification:**

- Unit/targeted tests pass.
- `python scripts/cvf_doctor.py --json` produces stable JSON.
- Existing release gate still PASS.

**Exit claim allowed:** "CVF clone readiness is locally diagnosable."

**Exit claim forbidden:** "CVF is zero-friction installed."

---

### RC2-F2 — Env Wizard + Provider Key Validation

**Why:** Provider/key/model failures are currently too easy to confuse with CVF
runtime failures.

**Scope:**

1. Add secret-safe env readiness logic:
   - detect `.env.local` presence
   - detect provider key variable presence without printing values
   - validate model/provider pair using a minimal live call when explicitly
     requested
2. Add a CLI wizard candidate such as:

   ```bash
   python scripts/cvf_configure.py
   python scripts/cvf_provider_check.py --provider alibaba --json
   ```

3. Accept aliases already recognized by release gate:
   - `DASHSCOPE_API_KEY`
   - `ALIBABA_API_KEY`
   - `CVF_ALIBABA_API_KEY`
   - `CVF_BENCHMARK_ALIBABA_KEY`
4. Include DeepSeek validation if `DEEPSEEK_API_KEY` is supplied.
5. Do not store, print, or commit raw keys.

**Artifacts:**

- Provider readiness helper module or script
- Tests for missing/malformed/present key classification
- Docs update for local setup

**Verification:**

- Missing keys report `MISSING_KEY`, not generic failure.
- Bad live validation reports provider/model-specific failure without leaking
  secret values.
- Release-quality governance proof still uses
  `python scripts/run_cvf_release_gate_bundle.py --json`.

**Exit claim allowed:** "Provider readiness is explicitly diagnosable."

**Exit claim forbidden:** "All provider lanes are certified."

---

### RC2-F3 — Web Runtime Health Surface

**Why:** The browser should show whether CVF is ready before a non-coder or dev
tries a governed execution.

**Scope:**

1. Add a Web health/readiness endpoint, for example:
   - `GET /api/system/health`
2. Add a Web surface under an existing dashboard/governance area:
   - module readiness summary
   - provider key status, secret-safe
   - configured provider/model pairs
   - storage/path readiness
   - release gate availability
   - last local doctor result if available
3. Follow `DESIGN.md` visual contract.
4. This surface is allowed to use mock/static checks only for UI structure, but
   must clearly label non-live statuses.

**Artifacts:**

- Health API route
- Runtime Health UI panel/page
- Targeted UI tests

**Verification:**

- UI mock tests prove rendering/state labels.
- Live governance claims still require provider-backed proof.

**Exit claim allowed:** "CVF Web exposes runtime readiness."

**Exit claim forbidden:** "CVF Web controls the full runtime."

---

### RC2-F4 — Module Registry + Runtime Facade Contract

**Why:** Full Web control requires a stable module vocabulary before adding
buttons that run things.

**Scope:**

1. Define a module registry contract:
   - module id
   - display name
   - repo path
   - version/source marker if available
   - health status
   - exposed actions
   - evidence owner
   - web exposure state
2. Include core modules at minimum:
   - `cvf-web`
   - `guard-contract`
   - `phase-governance-runtime`
   - `control-plane-foundation`
   - `execution-plane-foundation`
   - `governance-expansion-foundation`
   - `learning-plane-foundation`
   - `model-gateway`
   - `policy-engine`
   - `trust-sandbox`
3. Expose read-only registry through Web.
4. Do not invent module capabilities that cannot be verified from repo state.

**Artifacts:**

- Runtime module registry module
- `GET /api/system/modules`
- Web module registry panel
- Tests for stable module contract

**Verification:**

- Registry contract tests pass.
- Web renders all core modules with honest exposure state.
- No module is marked `WEB_RUNNABLE` unless backed by a real action.

**Exit claim allowed:** "CVF Web can enumerate core runtime modules."

**Exit claim forbidden:** "All modules are fully web-controlled."

---

### RC2-F5 — Governance Gate + Evidence Web Surface

**Why:** Governance is CVF's product center. Users need to see gate/evidence
state without reading CLI logs.

**Scope:**

1. Expose gate status and evidence references in Web:
   - release gate command availability
   - latest known gate result if present
   - evidence receipt locations
   - provider lane readiness matrix links/status
2. Add a safe job boundary for running selected checks from Web, if feasible:
   - start job
   - job status
   - output summary
   - artifact link
3. Live governance jobs must fail closed if no live key is available.
4. Do not run arbitrary shell commands from Web.

**Artifacts:**

- Gate/evidence API route or job abstraction
- Web gate/evidence panel
- Tests for secret redaction and command allowlist

**Verification:**

- Unit tests prove allowlisted commands only.
- Web UI cannot print raw API keys.
- Full release gate remains PASS.

**Exit claim allowed:** "Governance gate and evidence state are inspectable
from CVF Web."

**Exit claim forbidden:** "The full release gate can always run from Web on any
machine."

---

### RC2-F6 — Zero-Friction Setup Path

**Why:** After diagnostics, provider validation, health UI, module registry, and
evidence surfaces exist, CVF can offer a practical guided setup path.

**Scope:**

1. Add one canonical setup path:

   ```bash
   python scripts/cvf_setup.py
   ```

   or a clearly equivalent npm entrypoint.

2. Setup should orchestrate:
   - doctor checks
   - dependency install guidance
   - env file creation from template
   - provider validation prompt
   - web start instructions
   - first governed execution guidance
3. Add optional Docker/Compose path only if it can be tested honestly.
4. Add a short "5-minute RC setup" guide.
5. Add cross-platform smoke verification:
   - Windows required
   - macOS/Linux at least documented until externally verified

**Artifacts:**

- Setup orchestrator
- Short setup guide
- Smoke tests or scripted proof
- README quick-start update

**Verification:**

- Fresh-clone setup smoke passes on Windows.
- User can reach Web health page.
- User can identify missing provider key without reading code.
- With a live key, user can run first governed execution.
- Release gate remains PASS.

**Exit claim allowed:** "CVF has a guided setup path from clone to first
governed run."

**Exit claim forbidden:** "CVF is frictionless for every environment."

---

## Part 4 — Final RC2 Foundation Exit Criteria

The two target claims become allowed only when all conditions below are met.

### Claim A: "CVF Web is a runtime control surface"

Allowed only if:

- Web exposes module registry for all listed core modules.
- Web exposes runtime health and provider readiness.
- Web exposes governance gate/evidence status.
- At least one governed check/action is runnable or inspectable through a
  safe allowlisted path.
- Evidence and secret redaction are tested.

Still forbidden unless separately proven:

- "Every CVF runtime action is web-runnable."
- "Web fully replaces CLI/operator workflows."

### Claim B: "CVF is productized for fresh clone usage"

Allowed only if:

- One-command doctor exists.
- Setup path exists.
- Provider readiness is explicit.
- Web health page tells the user what is missing.
- Fresh-clone smoke proof exists.
- Live governed execution proof still passes with real provider key.

Still forbidden unless externally proven:

- "Zero friction for all community users."
- "Works identically on Windows/macOS/Linux."
- "No technical setup knowledge required."

---

## Part 5 — Execution Prohibitions

Codex/Claude must not do the following under this roadmap:

1. Do not call this GA.
2. Do not add new provider lanes unless RC2-F2 explicitly scopes validation for
   already-supported lanes.
3. Do not broaden public claims beyond evidence.
4. Do not turn Web into arbitrary command execution.
5. Do not print or commit raw API keys.
6. Do not redesign CVF visual identity outside `DESIGN.md`.
7. Do not rewrite WPR-1 through WPR-4 artifacts unless a direct inconsistency is
   found.
8. Do not claim community validation until external issues/PRs/feedback exist.

---

## Part 6 — Suggested Verification Commands

Baseline checks:

```bash
git status
git log --oneline -5
python scripts/run_cvf_release_gate_bundle.py --json
```

Future candidate checks:

```bash
python scripts/cvf_doctor.py --json
python scripts/cvf_provider_check.py --provider alibaba --json
```

Web checks must distinguish:

- UI-only mock checks: allowed for layout/routing/status rendering.
- Governance behavior claims: require live provider API proof.

---

## Part 7 — Review Questions for Claude

1. Is `RC2-F` the right name, or should this be a non-versioned foundation track?
2. Does RC2-F0 sufficiently prevent speculative planning?
3. Should module registry be read-only first, or should gate/evidence surface
   come before it?
4. Is Docker/Compose too early for RC2-F6?
5. Are the final allowed claims still too broad?
6. What should be explicitly deferred until real community signal arrives?

---

## Operator Summary

| Item | Decision |
|---|---|
| GA roadmap | Do not open yet |
| Foundation track | Draft for rebuttal |
| Main objective | Make CVF runnable, diagnosable, and web-visible |
| Execution authorization | Not granted by this file |
| First executable wave if approved | RC2-F0 reality audit |
| Risk if skipped | UX/DX work will mask setup/runtime-control gaps |

**End of draft.** Claude should rebut this before Codex performs any RC2-F
implementation.
