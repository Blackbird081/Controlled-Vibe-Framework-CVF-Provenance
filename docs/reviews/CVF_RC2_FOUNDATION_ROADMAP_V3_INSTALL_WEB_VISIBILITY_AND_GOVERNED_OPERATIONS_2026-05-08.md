<!-- Memory class: FULL_RECORD -->
# CVF RC2 Foundation Roadmap V3: Install, Web Visibility, and Governed Operations

**For:** Operator sign-off + GC-018 candidate preparation  
**Date:** 2026-05-08  
**Status:** DRAFT V3 — NOT AUTHORIZED FOR IMPLEMENTATION  
**Basis:** V2 roadmap + Claude confirmation/refinements + operator requirement that Web-triggered governance operations must be established, not skipped  

## Executive Decision

Do **not** open a GA roadmap yet.

Do **not** defer Web-triggered governance operations indefinitely. They are a
real CVF completion requirement. The correct response to risk is to establish
the missing threat model, RBAC, allowlist, audit log, job boundary, failure-mode
contract, and evidence controls before enabling any Web-triggered governance
operation.

This V3 roadmap separates the work into three tracks:

| Track | Name | Purpose |
|---|---|---|
| A | Install Productization | Fresh clone becomes diagnosable and guided to first run |
| B | Web Runtime Visibility Console | Web can inspect runtime/module/provider/evidence state |
| C | Governed Web Operations Enablement | Web can safely trigger selected non-destructive governance operations |

Recommended execution for one engineer: **A -> B -> C**. Parallel execution is
possible only when ownership is clearly separated.

---

## Part 1 — Current Truth Boundary

### RC1 Can Claim

- Public RC tag and GitHub Release exist: `v4.0.0-rc.1`.
- Core modules are present in the repository.
- The active governed AI path is live-proven.
- Trusted-form non-coder Web flow is live-usable under the W149 evidence
  boundary.
- Release-quality governance proof uses live provider API calls.

### RC1 Must Not Claim

- CVF Web is a full runtime control console.
- Fresh clone setup is zero-friction for ordinary community users.
- Web can safely trigger governance jobs.
- The project is GA-ready.

---

## Part 2 — Track A: Install Productization

**Purpose:** A fresh Windows clone can be diagnosed, configured, and guided to
first governed run without guessing.

### A0 — Install Reality Audit

**Scope:**

1. Fresh clone smoke audit on a clean Windows path.
2. Record exact dependency expectations:
   - Node/npm
   - Python
   - Playwright/browser readiness
   - provider keys
   - ports
   - writable state paths
3. Classify install blockers:
   - `BLOCKER`
   - `WARNING`
   - `OPTIONAL`
   - `DEFERRED_PLATFORM`

**Artifact:** `docs/reviews/CVF_RC2_INSTALL_REALITY_AUDIT_2026-05-08.md`

**Exit claim allowed:** "Install blockers are classified from a fresh Windows
clone audit."

### A1 — Runtime Doctor + Provider Validation

**Scope:**

1. Add one command:

   ```bash
   python scripts/cvf_doctor.py --json
   ```

2. Add provider readiness check:

   ```bash
   python scripts/cvf_provider_check.py --provider alibaba --json
   ```

3. Classify failures:
   - missing Node/npm
   - unsupported Node version
   - missing Python
   - missing package install
   - port busy
   - Playwright browser missing
   - missing provider key
   - provider key present but live validation failed
4. Never print raw keys.

**Exit claim allowed:** "CVF clone and provider readiness are locally
diagnosable."

### A2 — Guided First-Run Setup

**Scope:**

1. Add a guided setup path:

   ```bash
   python scripts/cvf_setup.py
   ```

2. Orchestrate:
   - doctor checks
   - dependency guidance
   - env template creation
   - provider validation prompt
   - Web start guidance
   - first governed execution guidance
3. Publish a short "5-minute RC setup" guide.
4. Windows is the committed proof platform. macOS/Linux are documented as
   `DEFERRED_PLATFORM` until externally verified.

**Exit claim allowed:** "CVF has a guided, low-friction first-run path on
Windows."

**Exit claim forbidden:** "Zero friction for all environments."

---

## Part 3 — Track B: Web Runtime Visibility Console

**Purpose:** The browser can inspect CVF runtime readiness, module status,
provider readiness, and governance evidence before users run work.

### B0 — Module Runtime Classification Audit

**Scope:**

Inventory each core module:

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

Classify each module:

- `PRESENT_DOCS_ONLY`
- `HAS_RUNTIME_CODE`
- `RUNNABLE_CLI_ONLY`
- `WEB_VISIBLE_READ_ONLY`
- `WEB_RUNNABLE`
- `NOT_EXPOSED`

**Abort clause:** Do not build empty facades. If a module has no runnable code,
it may be listed as docs-only but must not be marked runnable or controllable.

**Artifact:** `docs/reviews/CVF_RC2_MODULE_RUNTIME_CLASSIFICATION_AUDIT_2026-05-08.md`

### B1 — Web Runtime Health Surface

**Scope:**

1. Add `GET /api/system/health`.
2. Add Web health panel/page under the existing dashboard/governance area.
3. Show:
   - app readiness
   - provider key status, secret-safe
   - configured provider/model pairs
   - storage/path readiness
   - gate availability
   - doctor result if available
4. Follow `DESIGN.md`.

**Exit claim allowed:** "CVF Web exposes runtime readiness status."

### B2 — Read-Only Module Registry

**Scope:**

1. Add module registry contract:
   - id
   - name
   - repo path
   - version/source marker
   - health status
   - exposed actions
   - evidence owner
   - Web exposure state
2. Add `GET /api/system/modules`.
3. Add Web module registry panel.
4. Any action marked `WEB_RUNNABLE` must have live proof through a Web surface.

**Exit claim allowed:** "CVF Web can enumerate core runtime modules and their
honest exposure state."

### B3 — Read-Only Governance Evidence + Gate State

**Scope:**

1. Add `GET /api/governance/evidence` or equivalent.
2. Show:
   - latest known release gate result
   - evidence receipt locations
   - provider lane readiness matrix link/status
   - policy snapshots where available
   - provider/model trace, secret-safe
   - approval ids where available
3. No job triggering in B3.

**Exit claim allowed:** "CVF Web exposes governance evidence and gate state for
inspection."

---

## Part 4 — Track C: Governed Web Operations Enablement

**Purpose:** Web-triggered governance operations are part of desired CVF runtime
maturity. They must be built through explicit controls, not avoided and not
shipped casually.

### C0 — Threat Model For Web-Triggered Governance Jobs

**Scope:**

1. Define allowed job classes:
   - read-only diagnostics
   - provider readiness validation
   - targeted non-destructive governance checks
   - release-gate dry readiness
2. Define forbidden job classes:
   - arbitrary shell commands
   - destructive file operations
   - git push/tag/release actions
   - secret printing
   - unbounded recursive scans initiated by unauthenticated users
3. Define attack surfaces:
   - command injection
   - secret exfiltration
   - resource exhaustion
   - privilege escalation
   - stale job replay
   - confused-deputy provider-key use
4. Define mitigations:
   - command allowlist
   - argument schema validation
   - RBAC check
   - job queue boundary
   - timeout/resource caps
   - structured log redaction
   - append-only audit log

**Artifact:** `docs/reviews/CVF_WEB_TRIGGERED_GOVERNANCE_THREAT_MODEL_2026-05-08.md`

**Exit claim allowed:** "Threat model for Web-triggered governance jobs is
defined."

### C1 — RBAC + Access Control Specification

**Dependency:** C0 must be closed. C1 and C2 may proceed in parallel and should
inform each other before C3 begins.

**Scope:**

1. Define roles for Web governance surfaces:
   - owner
   - admin
   - developer/operator
   - reviewer
   - viewer
2. Decide read vs trigger permissions:
   - health read
   - module registry read
   - evidence read
   - provider validation trigger
   - doctor trigger
   - targeted governance check trigger
   - release-gate dry readiness trigger
3. Decide whether unauthenticated local mode is allowed and under what warning.
4. Decide audit fields for every trigger attempt.

**Artifact:** `docs/reviews/CVF_WEB_GOVERNANCE_RBAC_SPEC_2026-05-08.md`

**Exit claim allowed:** "RBAC and access boundary for non-destructive
Web-triggered governance operations is specified."

### C2 — Persistence + Audit Log ADR

**Dependency:** C0 must be closed. C1 and C2 may proceed in parallel and should
inform each other before C3 begins.

**Scope:**

1. Decide persistence mechanism:
   - file-backed JSONL
   - SQLite
   - PostgreSQL
   - in-memory only for dev
2. Define persisted data:
   - job id
   - job type
   - requester role
   - start/end timestamps
   - status
   - redacted output summary
   - evidence artifact path
   - provider lane metadata, never raw key
3. Define retention and local privacy boundary.

**Default recommendation:** JSONL is sufficient for RC2 unless the first Web UI
requires complex query/filter behavior. SQLite can be selected if query UI is
in-scope and tested.

**Artifact:** `docs/reviews/CVF_WEB_GOVERNANCE_JOB_PERSISTENCE_ADR_2026-05-08.md`

**Exit claim allowed:** "Persistence and audit log boundary is decided."

### C3 — Allowlisted Non-Destructive Governance Job Runner

**Dependencies:** C0, C1, and C2 must be closed.

**Scope:**

1. Implement a minimal allowlisted runner with no free-form command execution.
2. Candidate jobs:
   - `cvf_doctor`
   - `provider_check`
   - `docs_governance_check`
   - `release_gate_dry_readiness`
3. Full live release gate is **not** in C3. It is separated into C5.
4. Add job lifecycle:
   - queued
   - running
   - succeeded
   - failed
   - timed_out
   - blocked_by_policy
   - orphaned
5. Add a failure-mode contract and tests for:
   - malformed allowlist match input
   - subprocess exit code outside expected set
   - concurrent job trigger behavior: queue dedupe or serial execution
   - job runner crash/restart behavior: orphan detection and cleanup
   - timeout state recovery
   - redaction failure behavior: fail closed

All failure modes must have defined state recovery. No untested code paths may
be treated as production-ready.

**Exit claim allowed:** "CVF Web can trigger selected allowlisted
non-destructive governance jobs under audit."

**Exit claim forbidden:** "CVF Web can run arbitrary operations."

### C4 — Web Operations UI For Governed Jobs

**Dependency:** C3 must be closed.

**Scope:**

1. Add job trigger controls only for roles authorized by C1.
2. Add job status and audit trail views.
3. Add copy/export for redacted evidence summary.
4. Add clear warnings when live provider key is required for validation jobs.
5. Add tests for:
   - unauthorized trigger blocked
   - authorized trigger audited
   - raw key redaction
   - timeout handling
   - allowed job only
   - concurrent trigger behavior

**Exit claim allowed:** "CVF Web provides governed operation controls for a
bounded allowlisted non-destructive job set."

**Exit claim forbidden:** "CVF Web fully controls every CVF runtime module."

### C5 — Full Live Release Gate Trigger Enablement

**Status:** Separate high-rigor wave. It is not part of C3/C4.

**Why:** Full live release gate from Web is the highest-risk Web-triggered
operation because it can run real provider calls, consume quota/cost, run for
minutes, expose long output streams, and touch broad governance surfaces.

**Dependencies:**

- C3 and C4 closed with evidence.
- Additional cost/timeout cap specification.
- Separate live-provider interaction threat review.
- Rate limiter for repeated runs.
- Audit and redaction controls proven under long-running output.

**Artifact:** `docs/reviews/CVF_WEB_OPERATIONS_FULL_RELEASE_GATE_ENABLEMENT_C5_2026-05-08.md`

**Exit claim allowed:** "CVF Web can trigger full release gate under
cost/timeout/rate controls."

**Exit claim forbidden:** "Full release gate is just another Web job."

---

## Part 5 — Final Claim Gates

### Claim A: Guided First Run

Allowed only after A0-A2 close with evidence.

Final wording:

> CVF has a guided, low-friction first-run path on Windows from fresh clone to
> first governed run.

### Claim B: Web Runtime Visibility

Allowed only after B0-B3 close with evidence.

Final wording:

> CVF Web exposes runtime readiness, module status, provider readiness, and
> governance evidence for operator inspection.

### Claim C: Governed Web Operations

Allowed only after C0-C4 close with evidence.

Final wording:

> CVF Web can trigger selected allowlisted non-destructive governance operations
> (diagnostics, validation, evidence inspection) under RBAC, audit logging,
> redaction, timeout, and evidence controls.

### Claim D: Full Live Release Gate From Web

Allowed only after C5 closes with evidence.

Final wording:

> CVF Web can trigger the full live release gate under separate live-provider
> cost, timeout, rate-limit, redaction, and audit controls.

Still forbidden unless separately proven:

- "CVF Web can run arbitrary jobs."
- "CVF Web fully replaces CLI/operator workflows."
- "Every runtime module is Web-controllable."
- "Zero friction for all users and platforms."
- "GA-ready."

---

## Part 6 — Execution Order

Recommended graph:

```text
A0 -> A1 -> A2

B0 -> B1 -> B2 -> B3

C0 -> (C1 || C2) -> C3 -> C4 -> C5
```

Recommended single-engineer order:

```text
A0 -> A1 -> A2 -> B0 -> B1 -> B2 -> B3 -> C0 -> (C1/C2) -> C3 -> C4 -> C5
```

Parallelism:

- A0 and B0 may run in parallel after authorization.
- C0 may begin after B0 identifies real module/job surfaces.
- C1 and C2 may run in parallel after C0.
- C3 waits for C0, C1, and C2.

Stop rules:

- Each checkpoint needs GC-018 authorization before implementation.
- Any governance behavior claim must use live provider proof when relevant.
- Any Web-triggered operation must fail closed when prerequisites are missing.

---

## Part 7 — Execution Prohibitions

1. Do not call this GA.
2. Do not add new provider lanes.
3. Do not broaden public claims beyond evidence.
4. Do not run arbitrary shell commands from Web.
5. Do not print or commit raw API keys.
6. Do not mark docs-only modules as runnable.
7. Do not implement Web-triggered jobs before threat model, RBAC, persistence,
   audit log, allowlist, timeout, redaction, and failure-mode boundaries are
   approved.
8. Do not include full live release gate in C3/C4.
9. Do not redesign CVF visual identity outside `DESIGN.md`.

---

## Part 8 — Operator Scope Check

This V3 contains 14 checkpoints:

- Track A: A0-A2 = 3 checkpoints
- Track B: B0-B3 = 4 checkpoints
- Track C: C0-C5 = 6 checkpoints, with C1/C2 parallelizable
- Operator sign-off / GC-018 candidate = 1 governance step before execution

If this is too large for a single RC2 foundation tranche, the preferred trim is
to keep A0-A2, B0-B3, and C0-C4, while leaving C5 as a named post-RC2
high-rigor continuation. Do **not** remove C0-C4 if the goal is real CVF Web
operations maturity.

---

## Part 9 — Review Questions For Claude

1. Does V3 apply all four refinements from the confirmation file?
2. Should C5 remain in RC2 as a checkpoint, or be named but scheduled
   post-RC2?
3. Is JSONL still acceptable as the default C2 recommendation?
4. Are the final claim wordings now sufficiently bounded?
5. Is the single-engineer order acceptable if no parallel execution is used?

---

## Operator Summary

| Item | Decision |
|---|---|
| GA roadmap | Not opened |
| Install productization | Track A |
| Web runtime visibility | Track B |
| Web-triggered non-destructive operations | Track C0-C4 |
| Full live release gate from Web | C5 separate high-rigor wave |
| Risk treatment | Establish controls; do not skip the capability |
| Authorization | Not granted by this draft |
| First likely execution | A0 reality audit |

**End of V3 draft.** This version preserves the operator requirement that
Web-triggered governance jobs must be completed, while separating full live
release-gate triggering into its own high-rigor wave.
