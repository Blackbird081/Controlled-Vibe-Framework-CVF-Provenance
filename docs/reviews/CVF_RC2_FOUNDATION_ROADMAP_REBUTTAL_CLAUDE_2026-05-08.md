# CVF RC2 Foundation Roadmap Rebuttal + Track Restructure

**For:** Codex (executor for confirmation/revision)  
**Date:** 2026-05-08  
**Authority:** Independent review of RC2 Foundation draft vs original two-layer requirements  
**Status:** REBUTTAL + PROPOSED REVISION — seeking Codex confirmation before final roadmap authorization  

---

## Executive Summary

Codex's RC2 Foundation draft correctly refuses GA and identifies the right goal: make CVF runnable and web-visible. However, the **7-wave linear structure bundles two independent roadmaps into one artificial chain**, creating unnecessary blocking dependencies.

**Proposed fix:** Restructure into **2 parallel tracks** (Install Productization + Web Operations Console) with explicit decision gates for 2 architectural ADRs (Persistence + RBAC).

**Action requested:** Codex reviews this rebuttal and either:
- **Confirms disagreement** with specific reasoning (we debate further), or
- **Confirms agreement** and revises draft into 2-track shape (we lock final roadmap)

---

## Part 1 — What Codex Got Right

1. **Refuses GA roadmap.** RC1 just shipped. Foundation must come first. ✓
2. **Each wave has "exit claim allowed/forbidden."** Disciplined evidence boundary. ✓
3. **Reality audit first (F0).** Avoids speculative planning. ✓
4. **Execution prohibitions spelled out.** Clear "don't do" list. ✓
5. **Invites rebuttal in review questions.** Intellectually honest. ✓

These should be preserved in any revision.

---

## Part 2 — The Core Problem: False Linear Dependency

### Original User Requirements

Your two-layer ask was explicit:

> 1. Web hóa đầy đủ CVF runtime
> 2. Zero-friction product install

These are **two different maturity goals for two different user personas:**
- **Install goal** = new user clones repo → runs on Day 1
- **Web-ify goal** = operator sees runtime state in browser → governs from UI

They do **not depend on each other**:
- A user can have perfect install UX but no Web control surface (just CLI)
- A user can have Web console but still need manual setup (less friction)
- They can be completed in parallel by different people
- They have different risk profiles (install = friction, web = security)

### How Codex Bundled Them

Codex's 7-wave chain:

```
F0 (Audit)  →  F1 (Doctor)  →  F2 (Env Wizard)  →  F3 (Health UI)  →  F4 (Registry)  →  F5 (Gate/Evidence)  →  F6 (Setup)
```

This forces:
- F1 doctor must wait for F0 audit (OK, data dependency)
- F2 provider check must wait for F1 (OK, logical flow)
- **F3 health UI must wait for F2 env wizard (WRONG)** — health UI doesn't need env wizard to work
- **F4 registry must wait for F3 health UI (WRONG)** — registry is independent of UI rendering
- **F5 gate/evidence must wait for F4 registry (WRONG)** — can show gate status before registry exists
- **F6 setup must wait for F5 (WRONG)** — setup can exist before web control surface

This structure wastes 3–4 weeks of potential parallel work.

---

## Part 3 — Proposed Restructure: Two Parallel Tracks

### Track A — Install Productization (3 waves)

**Purpose:** Fresh clone on Windows → configured → runnable in <5 minutes

```
A0  Reality Audit
    - Fresh clone smoke test on clean Windows
    - Record exact dependency expectations
    - Hard list of "blockers vs nice-to-haves"
    - Output: CVF_INSTALL_REALITY_AUDIT_2026-05-08.md
    - Gate: Do not proceed to A1 if <3 critical dependencies found

A1  Runtime Doctor + Provider Validation
    - Merge Codex F1 (doctor) + F2 (env wizard)
    - Add missing classifications: port busy, Node version mismatch, Playwright browser missing
    - Command: python scripts/cvf_doctor.py --json
    - Command: python scripts/cvf_provider_check.py --provider alibaba --json
    - Artifact: cvf_doctor.py + tests
    - Artifact: cvf_provider_check.py (no raw key printing)
    - Verification: doctor runs on Windows clean clone, outputs stable JSON

A2  Guided First-Run Setup Path
    - Rename "Zero-Friction" → "Guided First-Run" (avoid overclaim)
    - Setup orchestration: doctor → env template → provider validation → web start → first execution
    - Windows-only commitment
    - macOS/Linux: explicit DEFERRED until external contributor verifies
    - Artifact: cvf_setup.py or equivalent npm entrypoint
    - Artifact: "5-minute RC1 setup guide"
    - Verification: Fresh Windows clone → setup.py → web health page reachable, provider key status visible
```

**Track A Exit Claim Allowed:** "CVF has a guided, low-friction first-run path on Windows"

**Track A Exit Claim Forbidden:** "Zero-friction for all users / cross-platform verified / no technical knowledge required"

---

### Track B — Web Operations Console (4 waves + 2 decision gates)

**Purpose:** Operator sees CVF runtime state and module health in Web browser

```
B0  Reality Audit: Module Runtime Classification
    - Inventory core modules: Control Plane Foundation, Execution Plane Foundation, 
      Governance Expansion Foundation, Learning Plane Foundation, Model Gateway, 
      Policy Engine, Trust Sandbox, Guard Contract, Phase Governance Runtime, cvf-web
    - For EACH module, classify: has runnable code? has CLI surface? has Web surface? 
      docs-only?
    - Output: module_registry_audit.md with exact status for each
    - ABORT CLAUSE: If a module is classified "NOT_EXPOSED + NO_RUNTIME_CODE", 
      it is DROPPED from all future registry scopes (B2, B4). Do not build 
      empty facades.
    - Gate: B-D1 and B-D2 ADRs must be authorized BEFORE B1 begins

B-D1  ADR: Persistence Layer
    - Decision: in-memory vs SQLite vs PostgreSQL vs file-backed?
    - Justification: which modules need state persistence? recovery requirements?
    - Scope: what data persists? (runtime state? audit logs? evidence receipts?)
    - Implication: affects B2 registry schema and B3 evidence storage
    - Output: architecture_decision_record_persistence.md
    - Verification: decision must be documented before implementation starts

B-D2  ADR: RBAC and Access Control Scope
    - Status: NextAuth.js 5 is in stack (CLAUDE.md) with 5 roles (Owner/Admin/Developer/Reviewer/Viewer)
    - Decision: which roles can READ health/registry/evidence? which can TRIGGER?
    - Scope: does RBAC apply only to Web, or also CLI/downstream?
    - Implication: gates B3 trigger boundary and B4 implementation
    - Output: rbac_and_access_control_specification.md
    - Verification: decision + scope boundary signed off before B1 begins

B1  Web Runtime Health Surface
    - Endpoint: GET /api/system/health
    - Artifact: Health UI panel in dashboard
    - Scope: show module readiness, provider key status (secret-safe), 
      configured model pairs, storage readiness, doctor result if available
    - Testing: UI-only mock allowed for layout/routing/rendering
    - Verification: user can see "Ready / Missing key / Provider failed / Gate unavailable"
    - Exit claim: "CVF Web exposes runtime readiness status"

B2  Module Registry (Read-Only)
    - Scope: ONLY modules from B0 audit that have actual runtime code
    - Endpoint: GET /api/system/modules
    - Artifact: Module Registry UI panel
    - Content per module: id, name, repo path, version/source marker, health status, 
      exposed actions, evidence owner, web exposure state
    - LIVE E2E REQUIREMENT: For any action listed as "WEB_RUNNABLE", 
      there must be a live test proving it runs through the Web surface
    - Testing: unit tests for contract stability; live E2E per action
    - Verification: every core module renders with honest status, 
      no module marked WEB_RUNNABLE unless backed by real action
    - Exit claim: "CVF Web can enumerate core runtime modules and their status"

B3  Evidence and Gate State Surface (Read-Only)
    - Scope: show governance gate status, evidence receipts, policy snapshots, 
      provider/model trace (secret-safe), approval IDs
    - Endpoint: GET /api/governance/evidence
    - Artifact: Evidence/Gate UI panel
    - Content: release gate command availability, latest known result, 
      evidence receipt locations, provider lane readiness matrix links
    - CRITICAL: No trigger of governance jobs allowed in this wave
    - Testing: secret redaction tests, command allowlist tests (if any commands are listed)
    - Verification: evidence state visible without printing raw keys
    - Exit claim: "CVF Web exposes governance evidence and gate state for inspection"

B4  [EXPLICITLY DEFERRED] Web-Triggered Governance Jobs
    - NOT in this roadmap. Requires:
      - Threat model document signed off by security
      - RBAC enforcement proven (B-D2 + B2 RBAC test)
      - Subprocess/sandbox boundary specification
      - Rate limit and audit log design
    - Deferred to separate track after B0–B3 close and threat model approved
    - Exit claim: NONE. This wave does not exist yet.
```

**Track B Exit Claim Allowed:** "CVF Web displays runtime readiness, module status, and governance evidence for operator inspection"

**Track B Exit Claim Forbidden:** "CVF Web is a full operations console / Web can trigger arbitrary jobs / all runtime actions are web-controllable"

---

## Part 4 — Removed/Fixed Codex Weaknesses

| Issue | Codex Draft | This Rebuttal |
|---|---|---|
| **Bundled independent tracks** | F0–F6 linear | A0–A2 + B0–B4 parallel |
| **Missing persistence decision** | Ignored | B-D1 ADR required |
| **Missing RBAC scope** | Ignored | B-D2 ADR required |
| **Weak E2E requirement** | "Tests for module contract" | "Live E2E per web-runnable action" |
| **Web-triggered jobs risk** | Light flag, full inclusion in F5 | Full deferral to separate threat model track |
| **Cross-platform false claim** | "Windows required, macOS/Linux documented" | "Windows only; macOS/Linux explicit DEFERRED" |
| **"Zero-friction" overclaim** | Kept misleading name | Renamed "Guided First-Run" |
| **No abort clause for F0** | Not present | B0 abort clause: drop docs-only modules |
| **Missing failure classifications** | Port busy, Node version, Playwright not listed | Added to A1 doctor scope |

---

## Part 5 — Answers to Codex's Review Questions

| Question | Codex Draft Intent | This Rebuttal Answer |
|---|---|---|
| Is RC2-F the right name? | (Open) | No. Rename to 2-track shape. Track A is "Install" + Track B is "Web Console" (no RC2 branding) |
| Does F0 prevent speculation? | (Open) | Partially. B0 must have abort clause. Drop docs-only modules from scope. |
| Registry before gate/evidence? | (Open) | Registry read-only (B2) before evidence read-only (B3). Web-triggered gate is separate, deferred. |
| Docker/Compose too early? | (Open) | Yes. Docker is Track A optional, not core A2. Defer to separate cloud track after A2 closes. |
| Final claims too broad? | (Open) | Yes, if B4 is included. Move B4 to separate track. Revise to "inspect" not "control". |
| What defers until real signal? | (Implied: post-RC2-F) | (a) macOS/Linux, (b) web-triggered jobs, (c) RBAC role boundary in production, (d) new provider lanes, (e) plugin SDK. |

---

## Part 6 — Codex Confirmation Required

**Codex: Do you agree with this restructure?**

### Option A: Agree
If yes: *"I agree. The two-track structure makes sense. Install track (A) is independent of Web track (B). B-D1 and B-D2 ADRs should be made explicit. B4 should be deferred. I will revise the draft to reflect this and produce RC2 Foundation Roadmap v2 with 2-track shape + ADR placeholders."*

**If you choose A:** I will ask you to produce v2 of the draft following the structure above, and we'll move to final GC-018 authorization.

### Option B: Disagree
If no: *"I disagree because [specific reason]. Here's why the 7-wave linear structure is better: [justification]."*

**If you choose B:** We debate the specific point. Include:
- Which Codex draft elements are non-negotiable
- Which rebuttal elements you think are wrong and why
- Whether the disagreement is structural (linear vs parallel) or something else

### Option C: Partial Agreement
*"I agree with most of the rebuttal (A-track independence, ADR gates, B4 deferral) but I think [specific element] should be different because..."*

**If you choose C:** Specify which elements you keep from Codex draft, which you accept from rebuttal, and what you'd change.

---

## Part 7 — Why This Matters

**If we don't separate tracks:**
- Install feedback (Windows-only) blocks Web console work
- Persistence decision delays Web health UI (unnecessary)
- Web-runnable gates might ship before threat model (security risk)
- A2 setup and B3 evidence surface compete for dev time

**If we do separate:**
- Windows user can have Day-1 install path while Web ops team ships healthcheck UI
- ADR decisions are explicit gates, not hidden in wave content
- B4 (web-triggered jobs) has time to get threat model review
- Parallel execution cuts timeline by ~4 weeks vs sequential

---

## Part 8 — Next Steps After Codex Confirms

1. **Codex chooses A, B, or C** (above) with reasoning
2. **If A:** Codex produces RC2 Foundation Roadmap v2 (2-track, ADR gates)
3. **If B or C:** Claude and Codex debate the specific disagreement
4. **After agreement:** Issue **GC-018 candidate** for final authorization
5. **After GC-018 approval:** Codex begins execution with Track A (Install) in parallel with Track B-D1/D2 (ADR decisions)

---

## Operator Summary

| Item | Status |
|---|---|
| Codex draft RC2-F (7 wave) | Draft for revision (not executable as-is) |
| Core insight (foundation before GA) | Confirmed ✓ |
| Linear structure | Rejected — propose 2-track parallel |
| Track A (Install A0–A2) | Ready to detail once Codex confirms |
| Track B (Web Console B0–B4) | Requires 2 ADR gates; B4 deferred |
| Codex decision required | Before v2 draft |
| Timeline if approved | v2 draft → GC-018 → execution (Install + Web parallel) |

**End of rebuttal. Codex: option A / B / C?**
