<!-- Memory class: FULL_RECORD -->
# CVF RC2 Pre-GA Validation And C5 Readiness Roadmap Draft

**For:** Claude critique before implementation  
**Date:** 2026-05-08  
**Status:** DRAFT — NOT AUTHORIZED FOR IMPLEMENTATION  
**Basis:** RC2 Foundation closure packet, Claude post-RC2 critique, operator clarification on local-first CVF and Web/Supabase boundaries  

## Executive Decision

Do **not** open GA yet.

RC2 Foundation is closed, but GA requires a separate post-hardening validation
wave. The next work should prove that RC2 Web operations did not regress the
non-coder adoption paths, then harden the C5 full live release-gate trigger
from Web, then wire release-quality evidence into CI/manual release operations.

Supabase is **not** the default CVF runtime state model. CVF remains
local-first for developers and operators who clone the repository and run the
framework on their own machine. Web exists primarily to make CVF visible and
operable for non-coders and local operators. Supabase/Postgres is only an
optional managed-deployment adapter for teams that explicitly choose cloud or
multi-user hosting.

Recommended order:

| Order | Track | Purpose |
|---:|---|---|
| 1 | R | Pre-GA regression validation after RC2 hardening |
| 2 | C5 | Full live release gate trigger from Web under strict controls |
| 3 | CI | Release-gate automation split into static/default and protected live gates |
| 4 | M | Optional managed adapter planning, local-first preserved |

Track M must not block the local-first RC/GA path.

---

## Part 1 — Current Truth Boundary

### Closed And Evidence-Backed

- RC2 Foundation Track A/B/C0-C4 is closed and pushed.
- Full CLI release gate has a standalone artifact:
  `docs/reviews/CVF_RC2_RELEASE_GATE_RESULT_2026-05-08.md`.
- Web governance operations C3/C4 have live provider evidence:
  `docs/reviews/CVF_RC2_C3_C4_LIVE_GOVERNANCE_EVIDENCE_2026-05-08.md`.
- Claim N and Claim D RC2 spot-checks exist:
  `docs/reviews/CVF_RC2_NONCODER_LIVE_SPOT_CHECK_2026-05-08.md`
  and `docs/reviews/CVF_RC2_DEVELOPER_LIVE_SPOT_CHECK_2026-05-08.md`.
- RC2 typecheck drift was resolved and filed:
  `docs/reviews/CVF_RC2_TYPECHECK_DRIFT_RESOLUTION_2026-05-08.md`.

### Still Not Proven After RC2

- W119/W122-W130 non-coder adoption paths have not been rerun as a post-RC2
  regression packet.
- C5 full live release gate cannot yet be triggered from Web.
- CI does not yet run the release gate as a protected, artifact-producing live
  release operation.
- Runtime jobs use local JSONL state only; this is correct for RC2 local-first,
  but not enough for a managed cloud or multi-user deployment.
- Multi-tenant/org boundary is not complete for a hosted CVF deployment.
- Cost/quota controls exist only as partial historical/product concepts, not
  as a unified Web-triggered live gate guard.

### Explicit Local-First Boundary

CVF's primary developer path is:

```text
clone repository -> configure local provider key -> run CVF locally -> keep data local
```

The Web app is not meant to force developers into someone else's cloud. Its
job is to make CVF understandable and controllable for non-coders and local
operators through visual status, evidence, and bounded governance operations.

Managed/cloud hosting is optional. Teams that need shared dashboards,
multi-user job history, org policy, or hosted audit retention may opt into a
cloud adapter later. That adapter must not weaken or replace local-first
operation.

---

## Part 2 — Track R: Pre-GA Non-Coder Regression Validation

**Purpose:** Prove that RC2 hardening did not regress the already-closed
non-coder adoption tranche.

**Status:** Candidate next track; requires GC-018 before implementation.

### R0 — Regression Scope Inventory

Inventory the exact prior claims and evidence boundaries from:

- W119 first-run readiness and evidence receipt visibility;
- W122 intent-first front door;
- W123 follow-up continuity;
- W124 clarification loop;
- W125 deliverable packs;
- W126 trusted-form routing;
- W127 adoption metrics;
- W128 rollout readout;
- W129 staged rollout;
- W130 evidence and pack export activation.

**Artifact:**
`docs/reviews/CVF_RC2_PRE_GA_NONCODER_REGRESSION_SCOPE_2026-05-08.md`

**Exit claim allowed:**

> The post-RC2 non-coder regression surface is enumerated from prior closure
> artifacts.

**Exit claim forbidden:**

- No-regression.
- GA-ready.

### R1 — Representative Live Regression Matrix

Run a bounded but representative live browser matrix on the Alibaba lane.

Minimum coverage:

| Prior claim | Required post-RC2 check |
|---|---|
| W119 | non-coder can reach governed execution result with evidence receipt |
| W122 | intent-first routing reaches an audited trusted target |
| W123 | follow-up creates a continuation chain without losing evidence context |
| W124 | weak/short input enters clarification and recovers to a route |
| W125 | deliverable pack is generated and exportable |
| W126 | trusted-form route uses the trusted form subset correctly |
| W127/W128 | analytics/readout lanes update without corrupting evidence claims |
| W129/W130 | evidence export and pack export both fire in a live journey |

The matrix may be smaller than the full W149 40-form corpus, but it must cover
every non-coder capability family above. If any family fails, do not proceed to
C5.

**Artifact:**
`docs/reviews/CVF_RC2_PRE_GA_NONCODER_REGRESSION_EVIDENCE_2026-05-08.md`

**Exit claim allowed:**

> The representative W119/W122-W130 non-coder paths passed post-RC2
> regression on the live Alibaba lane.

**Exit claim forbidden:**

- Universal provider parity.
- Full 40-form replay, unless explicitly run.
- Non-coder stability beyond the tested matrix.

### R2 — Role-Bound Non-Coder Sanity Check

RC2 Claim N used an `admin` authenticated local browser session. This is
acceptable only as a post-hardening sanity check. R2 must add a role-bound
check for the non-coder-facing path.

Minimum requirement:

- run at least one live browser journey under the lowest role that is expected
  to use the non-coder flow in the current local Web model;
- verify that unauthorized Web governance operations remain blocked;
- verify that the non-coder path can still see the evidence receipt where the
  product claim says it can;
- record the role/auth mode explicitly.

**Artifact:**
`docs/reviews/CVF_RC2_PRE_GA_ROLE_BOUND_NONCODER_CHECK_2026-05-08.md`

**Exit claim allowed:**

> RC2 post-hardening non-coder sanity evidence includes a role-bound browser
> check.

**Exit claim forbidden:**

- Full enterprise RBAC proof.
- Managed multi-tenant authorization.

### R3 — Claim Sync And Pre-GA Decision

Update only claim surfaces that are affected by R1/R2 evidence:

- `AGENT_HANDOFF.md`;
- Claude transfer note if needed;
- public known-limits or release notes only if current public wording would
  overclaim.

**Artifact:**
`docs/reviews/CVF_RC2_PRE_GA_REGRESSION_DECISION_2026-05-08.md`

**Exit decisions:**

| Decision | Meaning |
|---|---|
| `PROCEED_TO_C5` | R1/R2 passed; Web full release-gate trigger may be planned |
| `REPAIR_REQUIRED` | regression found; repair before C5 |
| `SCOPE_REDUCED` | claim boundary must be narrowed before C5 |

---

## Part 3 — Track C5: Full Live Release Gate Trigger From Web

**Purpose:** Allow Web to trigger the full live release gate without turning the
browser into an arbitrary shell, cost sink, or secret leak.

**Status:** Separate high-rigor track; not part of RC2 C3/C4 closure.

### C5.0 — Threat Model Addendum

Extend the C0 threat model for full live release gate behavior.

Required additions:

- cost/quota exhaustion;
- long-running Playwright process lifecycle;
- provider key confused-deputy risk;
- concurrent trigger collision;
- stale job replay;
- partial gate output leakage;
- cancellation/orphan cleanup;
- artifact integrity and redaction.

**Artifact:**
`docs/reviews/CVF_C5_FULL_RELEASE_GATE_WEB_TRIGGER_THREAT_MODEL_2026-05-08.md`

### C5.1 — Cost, Timeout, And Rate-Limit Contract

Define the controls before implementation.

Minimum controls:

- one active full release gate per local workspace;
- owner/admin/operator only, according to C1 role matrix;
- explicit confirmation copy for live provider cost;
- configurable but bounded timeout;
- cooldown after success/failure;
- redacted output cap;
- hard block if live key is missing;
- hard block if preflight detects dirty or unsupported gate state where that
  would invalidate evidence.

**Artifact:**
`docs/reviews/CVF_C5_RELEASE_GATE_COST_TIMEOUT_RATE_LIMIT_CONTRACT_2026-05-08.md`

### C5.2 — Web Job Type Implementation

Add a new allowlisted job type only after C5.0 and C5.1 close:

```text
full_live_release_gate
```

The implementation must run the canonical command:

```bash
python scripts/run_cvf_release_gate_bundle.py --json
```

Implementation requirements:

- no free-form argv from the browser;
- cwd locked to repository root;
- live key presence checked without printing key values;
- status transitions persisted;
- stdout/stderr redacted before persistence or UI display;
- artifact reference captured when the run completes;
- cancellation/orphan handling tested.

**Exit claim allowed:**

> CVF Web can trigger the full live release gate through an allowlisted job
> type under bounded controls.

### C5.3 — Web Operations UI Upgrade

Update `/governance/operations` with:

- full release gate action visible only to authorized roles;
- explicit live-provider/cost warning;
- current running gate status;
- disabled state while another gate is active;
- redacted result summary;
- evidence artifact link/reference;
- clear distinction between dry readiness and live proof.

Follow `DESIGN.md` before implementation.

### C5.4 — C5 Live Evidence Packet

Run C5 from the Web UI, not CLI only.

Required proof:

- at least one successful Web-triggered full live release gate;
- blocked unauthorized attempt;
- missing-key or invalid-preflight behavior if safely testable without printing
  secrets;
- audit trail includes request, running, success/failure, and evidence refs;
- output redaction verified.

**Artifact:**
`docs/reviews/CVF_C5_WEB_TRIGGERED_FULL_RELEASE_GATE_EVIDENCE_2026-05-08.md`

**Exit claim allowed:**

> CVF Web can trigger a full live release gate under RBAC, timeout, rate, cost,
> redaction, and audit controls.

**Exit claim forbidden:**

- Arbitrary Web-triggered governance jobs.
- Public hosted control plane.
- GA-ready, unless Track R and Track CI also close.

---

## Part 4 — Track CI: Release Gate Automation

**Purpose:** Make release-quality proof repeatable without weakening secret
handling or forcing every contributor to have live provider keys.

**Status:** Candidate track after C5 or in parallel only if implementation is
strictly non-overlapping.

### CI0 — CI Gate Design

Define two lanes:

| Lane | Trigger | Secret requirement | Purpose |
|---|---|---|---|
| `static_pr_gate` | pull request / push | none | build, typecheck, unit/static governance checks |
| `protected_live_release_gate` | manual dispatch / scheduled / protected branch | live provider secret | release-quality proof |

Live governance claims must never be inferred from `static_pr_gate`.

**Artifact:**
`docs/reviews/CVF_RELEASE_GATE_CI_DESIGN_2026-05-08.md`

### CI1 — Static CI Gate

Wire non-secret checks into CI:

- Web build;
- TypeScript check;
- secrets scan;
- docs governance check;
- unit/static governance checks.

### CI2 — Protected Live Release Gate

Wire the canonical release command into a protected/manual job:

```bash
python scripts/run_cvf_release_gate_bundle.py --json
```

Requirements:

- use repository/organization secrets;
- fail closed when the live key is absent;
- upload redacted JSON/artifact summary;
- never print raw keys;
- label output as live release evidence, not generic CI success.

**Artifact:**
`docs/reviews/CVF_PROTECTED_LIVE_RELEASE_GATE_CI_EVIDENCE_2026-05-08.md`

### CI3 — Claim Sync

Update claim surfaces only after the first successful protected live CI run.

**Exit claim allowed:**

> CVF has a protected CI lane for release-quality live governance proof.

**Exit claim forbidden:**

- Every PR proves live governance.
- CI can run live proof without configured secrets.

---

## Part 5 — Track M: Optional Managed Runtime Adapter Planning

**Purpose:** Prepare for teams that explicitly want hosted/shared CVF while
preserving local-first operation as the default.

**Status:** Deferred planning track. Do not mix into R/C5/CI unless operator
explicitly authorizes it.

### M0 — Storage Adapter Boundary

Introduce a storage boundary only when needed:

```text
RuntimeJobStore
  -> FileBackedRuntimeJobStore   # default local-first adapter
  -> SupabaseRuntimeJobStore     # optional managed adapter
```

Rules:

- file-backed JSONL remains the default;
- Supabase/Postgres is opt-in;
- no local developer must upload CVF job/evidence data to a third-party cloud;
- adapter selection must be explicit through configuration;
- local evidence format must remain inspectable.

### M1 — Supabase/Postgres Managed Adapter Candidate

Supabase is a reasonable candidate for hosted/shared CVF because it can provide:

- Postgres persistence;
- row-level security;
- org/workspace scoping;
- audit retention;
- managed dashboard queryability.

But Supabase must be treated as optional product depth, not RC2/GA local proof.

Required planning artifacts:

- schema ADR;
- RLS policy design;
- migration/rollback plan;
- local-to-managed export/import boundary;
- secret handling plan;
- evidence retention and deletion policy.

### M2 — Multi-Tenant / Org Boundary

Before any managed deployment claim:

- every runtime job must have `orgId` and `workspaceId` or an explicit
  `local_only` scope;
- evidence, jobs, knowledge, approvals, and cost usage must be partitioned;
- role checks must include org membership;
- cross-org read/write attempts must be tested and blocked.

### M3 — Cost/Quota Guard For Managed And C5 Paths

Cost/quota guard should cover:

- per-run estimate where practical;
- daily/monthly budget threshold;
- per-role trigger limit;
- provider lane cooldown;
- warning before live gate execution;
- hard block after configured budget cap;
- audit events for warning, block, override, and reset.

The C5 local path may implement a bounded version first. Managed cost/quota
guard can expand later with persistent org-level usage.

### M4 — Public Learning Loop And Extension SDK

Defer ecosystem expansion until the local and managed control boundaries are
clean.

Minimum later requirements:

- public issue triage SLO;
- contributor onboarding metric;
- extension author boundary tests;
- plugin/extension SDK examples;
- compatibility policy for third-party extensions;
- explicit rule that external plugins do not become governance authority.

---

## Part 6 — Suggested Execution Plan

### Immediate Next Roadmap

Create a narrower implementation roadmap after Claude critique:

```text
CVF_RC2_R1_PRE_GA_NONCODER_REGRESSION_REPLAY_ROADMAP_2026-05-08.md
```

Do not begin C5 until R1/R2 evidence is filed.

### Then C5

Create:

```text
CVF_RC2_C5_FULL_LIVE_RELEASE_GATE_FROM_WEB_ROADMAP_2026-05-08.md
```

C5 should be implemented only after the C5.0/C5.1 design artifacts are
accepted.

### Then CI

Create:

```text
CVF_RELEASE_GATE_CI_INTEGRATION_ROADMAP_2026-05-08.md
```

CI may begin earlier only if it touches CI files and docs, not C5 runtime code.

### Later Managed Option

Create only if the operator chooses managed/cloud productization:

```text
CVF_MANAGED_RUNTIME_STATE_AND_SUPABASE_ADAPTER_ROADMAP_2026-05-08.md
```

This roadmap must state that local JSONL/file-backed operation remains the
default and that Supabase is optional.

---

## Part 7 — Global Stop Rules

Stop and ask for operator decision if:

- a step would require uploading local CVF data to a cloud service by default;
- a Web control requires free-form command execution;
- a live governance claim would be backed only by mock/UI evidence;
- a release gate run cannot access a live provider key;
- raw API keys would appear in logs, artifacts, browser output, or CI output;
- C5 attempts to bypass R1/R2 post-RC2 regression evidence;
- Supabase work starts before local-first adapter boundaries are documented.

---

## Part 8 — Claude Review Questions

Ask Claude to critique these exact points:

1. Is Track R sufficient to prove post-RC2 non-coder no-regression without
   rerunning the entire historical corpus?
2. Is R2 strong enough to repair the earlier RC2 Claim N admin-role weakness?
3. Are the C5 controls enough before allowing Web to trigger the full live
   release gate?
4. Should CI integration happen before or after C5, given the need to avoid
   mixing runtime changes with workflow changes?
5. Does Track M preserve the operator's local-first boundary clearly enough?
6. Is Supabase correctly framed as optional managed adapter rather than default
   CVF state?
7. Are any claims still too strong for the evidence proposed here?

---

## Claim Boundary

Allowed after this draft is accepted:

> CVF has a proposed post-RC2 Pre-GA validation and C5 readiness roadmap for
> external critique.

Still forbidden after this draft:

- Post-RC2 no-regression is proven.
- C5 is implemented.
- Web can trigger the full live release gate.
- Release gate CI is implemented.
- CVF is GA-ready.
- Supabase is the default CVF persistence layer.
