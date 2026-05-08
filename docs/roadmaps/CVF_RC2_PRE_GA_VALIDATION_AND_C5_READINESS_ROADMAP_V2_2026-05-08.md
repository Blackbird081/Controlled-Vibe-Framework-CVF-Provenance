<!-- Memory class: FULL_RECORD -->
# CVF RC2 Pre-GA Validation And C5 Readiness Roadmap V2

**For:** Operator sign-off + Claude re-review before implementation  
**Date:** 2026-05-08  
**Status:** EXECUTED THROUGH CI2 IMPLEMENTATION — OPTIONAL MANAGED STATE DEFERRED
**Basis:** RC2 Foundation closure packet, Claude rebuttal, Codex response, operator clarification that CVF remains local-first and Supabase is optional managed depth  

## Executive Decision

Do **not** open GA yet.

RC2 Foundation is closed, but GA requires a post-hardening validation wave. The
next work should first install static CI guardrails, then prove that RC2 did
not regress the non-coder adoption paths, then implement C5 full live release
gate triggering from Web under strict controls. Optional managed/cloud state
planning remains separate and must not block the local-first RC/GA path.

CVF remains local-first:

```text
clone repository -> configure local provider key -> run CVF locally -> keep data local
```

The Web app is a local visual control and evidence surface for non-coders and
operators. It must not force developers to upload CVF data to a third-party
cloud. Supabase is only a possible deployment choice for a later optional
managed/shared CVF mode.

Recommended sequencing:

| Order | Track | Purpose | Dependency |
|---:|---|---|---|
| 1 | CI1 | Static/default CI guardrails with no secrets | none |
| 2 | R | Post-RC2 non-coder regression validation | CI1 preferred |
| 2a | C5.0/C5.1 | C5 threat model and control contract | may run in parallel with R |
| 3 | C5.2-C5.4 | Web-triggered full live release gate implementation and proof | R decision + C5.0/C5.1 accepted |
| 4 | CI2 | Protected live release gate CI | C5 stable |
| 5 | M | Optional managed adapter planning | separate operator decision |

Track M must not block local-first GA readiness.

## Execution Addendum — 2026-05-08

The V2 roadmap was subsequently authorized by Claude final authorization and
executed through the local-first GA-readiness tracks:

- CI1 static guardrails: CLOSED DELIVERED.
- R post-RC2 non-coder regression: CLOSED DELIVERED, `20/18` checks with all
  10 families covered on Alibaba; DeepSeek remains explicitly unknown.
- C5.0/C5.1 design: CLOSED DELIVERED.
- C5.2-C5.4 Web-triggered full live release gate: CLOSED DELIVERED, Web job
  `full_live_release_gate` returned release gate `7/7 PASS`.
- CI2 protected live release gate workflow: IMPLEMENTED, hosted run pending
  because the operator deferred push.
- M optional managed state/Postgres/Supabase planning: DEFERRED; local JSONL
  remains the default RC2 runtime job store.

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
- RC2 Claim N has not yet been repaired with a lowest-authorized role browser
  journey.
- C5 full live release gate cannot yet be triggered from Web.
- CI does not yet have a protected live release-gate lane.
- Runtime governance jobs use local JSONL state only. This is correct for RC2
  local-first but insufficient for optional managed/cloud multi-user hosting.
- Multi-tenant/org boundary is not complete for hosted CVF.
- Cost/quota controls are not yet a unified Web-triggered live gate guard.

### Explicit Local-First Boundary

The default CVF state model remains local files under the user's clone. Web
operations and evidence are local operator surfaces. Managed/cloud hosting is
optional and must be explicitly configured later.

Supabase/Postgres must not become the default persistence layer. If a managed
adapter is introduced later, local JSONL/file-backed operation remains the
default and must stay inspectable.

---

## Part 2 — Track CI1: Static CI Guardrails Before Regression

**Purpose:** Put non-secret checks around the tree before collecting post-RC2
regression evidence.

**Status:** Candidate first track; requires GC-018 before implementation.

### CI1.0 — Static CI Design

Define a default CI lane that requires no provider keys and makes no live
governance claim.

Minimum checks:

- Web build;
- TypeScript check;
- secrets scan;
- docs governance check;
- unit/static governance checks already available in the repository.

**Artifact:**
`docs/reviews/CVF_STATIC_CI_GATE_DESIGN_2026-05-08.md`

**Exit claim allowed:**

> CVF has a proposed static CI gate for non-secret regression protection.

**Exit claim forbidden:**

- CI proves live governance.
- PRs can run release-quality proof without live provider secrets.

### CI1.1 — Static CI Implementation

Wire the non-secret checks into CI. This track must not require provider keys,
must not run live provider calls, and must not modify runtime behavior.

**Artifact:**
`docs/reviews/CVF_STATIC_CI_GATE_EVIDENCE_2026-05-08.md`

**Exit claim allowed:**

> CVF has a default static CI lane that protects build, type, secret-scan, docs,
> and static/unit checks.

---

## Part 3 — Track R: Pre-GA Non-Coder Regression Validation

**Purpose:** Prove that RC2 hardening did not regress the already-closed
non-coder adoption tranche.

**Status:** Candidate track after CI1; requires GC-018 before implementation.

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

Minimum coverage and run count:

| Family | Prior claim | Required post-RC2 check | Minimum passes |
|---|---|---|---:|
| first value | W119 | non-coder can reach governed execution result with evidence receipt | 2 |
| intent routing | W122 | intent-first routing reaches an audited trusted target | 2 |
| continuity | W123 | follow-up creates a continuation chain without losing evidence context | 2 |
| clarification | W124 | weak/short input enters clarification and recovers to a route | 2 |
| deliverable pack | W125 | deliverable pack is generated and exportable | 2 |
| trusted form | W126 | trusted-form route uses the trusted form subset correctly | 2 |
| metrics | W127 | browser-local analytics lanes update for the tested journey | 2 |
| readout | W128 | non-coder health/readout does not overstate low-data evidence | 2 |
| rollout signal | W129 | enabled rollout flags do not block the tested non-coder path | 1 |
| export activation | W130 | evidence export and pack export both fire in a live journey | 1 |

Minimum total: **N >= 18 live successful checks** across the table above.

The matrix may be smaller than the full W149 40-form corpus, but it must cover
every non-coder capability family above. The artifact must list every actual
run, role/auth mode, provider lane, prompt/template, result, receipt state,
export state where applicable, and failure classification.

If any family fails, do not proceed to C5.2-C5.4.

DeepSeek boundary:

- Alibaba is the required lane for R1.
- DeepSeek is optional confirmatory coverage.
- If DeepSeek is not run, the R1 artifact must explicitly state:
  `DeepSeek post-RC2 regression status unknown; this evidence applies to the Alibaba lane only.`

**Artifact:**
`docs/reviews/CVF_RC2_PRE_GA_NONCODER_REGRESSION_EVIDENCE_2026-05-08.md`

**Exit claim allowed:**

> The representative W119/W122-W130 non-coder paths passed post-RC2 regression
> on the live Alibaba lane with N >= 18 successful checks.

**Exit claim forbidden:**

- Universal provider parity.
- DeepSeek post-RC2 regression pass unless DeepSeek is actually run.
- Full 40-form replay unless explicitly run.
- Non-coder stability beyond the tested matrix.

### R2 — Role-Bound Non-Coder Evidence Repair

RC2 Claim N used an `admin` authenticated local browser session. R2 repairs
that weakness with two separate browser checks.

#### R2a — Positive Observer-Role Journey

Use the minimum role that the current Web model claims may use the non-coder
path. The artifact must name the role and auth mode.

Required result:

- open the non-coder-facing entry path;
- submit an intent-first or trusted-form journey;
- receive governed result;
- see governance evidence receipt;
- prove that receipt visibility is not dependent on `admin`.

#### R2b — Negative Blocked-Role Operation Attempt

Use an unauthenticated or otherwise blocked role according to the C1 matrix.

Required result:

- attempt a governance operation that the role must not trigger;
- receive 401/403 or equivalent policy block;
- no governance operation is executed;
- no privileged receipt or audit export is exposed.

**Artifact:**
`docs/reviews/CVF_RC2_PRE_GA_ROLE_BOUND_NONCODER_CHECK_2026-05-08.md`

**Exit claim allowed:**

> RC2 post-hardening non-coder sanity evidence includes separate positive
> lowest-authorized receipt visibility and negative blocked-operation checks.

**Exit claim forbidden:**

- Full enterprise RBAC proof.
- Managed multi-tenant authorization.

### R3 — Claim Sync And Pre-GA Decision

Update claim surfaces affected by R1/R2 evidence in both directions:

- repair any overclaim contradicted by R1/R2;
- repair underclaim where RC2 added visible capability that public docs do not
  mention;
- update `AGENT_HANDOFF.md`;
- update Claude transfer note if needed;
- update README, GET_STARTED, known-limits, or release notes only when the
  current user-facing documentation would mislead users by overclaiming or by
  omitting a now-visible RC2 capability.

Examples of underclaim to check:

- local Web operations console;
- intent-first non-coder flow;
- trusted-form route;
- governance evidence receipt UI.

**Artifact:**
`docs/reviews/CVF_RC2_PRE_GA_REGRESSION_DECISION_2026-05-08.md`

**Exit decisions:**

| Decision | Meaning |
|---|---|
| `PROCEED_TO_C5_IMPLEMENTATION` | R1/R2 passed; C5.2-C5.4 may proceed |
| `REPAIR_REQUIRED` | regression found; repair before C5.2 |
| `SCOPE_REDUCED` | claim boundary must be narrowed before C5.2 |

---

## Part 4 — Track C5: Full Live Release Gate Trigger From Web

**Purpose:** Allow Web to trigger the full live release gate without turning the
browser into an arbitrary shell, cost sink, or secret leak.

**Status:** Separate high-rigor track. C5.0/C5.1 may run in parallel with
Track R because they are design artifacts. C5.2-C5.4 must wait for the R3
decision and accepted C5.0/C5.1 artifacts.

### C5.0 — Threat Model Addendum

Extend the C0 threat model for full live release gate behavior.

Required additions:

- cost/quota exhaustion;
- long-running Playwright process lifecycle;
- provider key confused-deputy risk;
- concurrent trigger collision;
- stale job replay;
- partial gate output leakage;
- deterministic secret redaction verification;
- cancellation/orphan cleanup;
- artifact integrity and redaction.

**Artifact:**
`docs/reviews/CVF_C5_FULL_RELEASE_GATE_WEB_TRIGGER_THREAT_MODEL_2026-05-08.md`

### C5.1 — Cost, Timeout, And Rate-Limit Contract

Define the controls before implementation.

Minimum controls:

- one active full release gate at a time on this local CVF installation;
- owner/admin/operator only, according to C1 role matrix;
- explicit confirmation copy for live provider cost;
- configurable but bounded timeout;
- cooldown after success/failure;
- redacted output cap;
- deterministic fake-key redaction probe in C5.4;
- hard block if live key is missing;
- hard block if preflight detects dirty or unsupported gate state where that
  would invalidate evidence.

When multi-tenant scope is added in Track M2, extend the "one active full gate"
rule to workspace/org-scoped rate limits. Do not use workspace/org language in
C5 local implementation before M2 formalizes it.

**Artifact:**
`docs/reviews/CVF_C5_RELEASE_GATE_COST_TIMEOUT_RATE_LIMIT_CONTRACT_2026-05-08.md`

### C5.2 — Web Job Type Implementation

Add a new allowlisted job type only after C5.0/C5.1 are accepted and R3 returns
`PROCEED_TO_C5_IMPLEMENTATION`:

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
- cancellation/orphan handling tested;
- deterministic fake-key redaction probe supported by test harness or manual
  evidence path.

**Exit claim allowed:**

> CVF Web can trigger the full live release gate through an allowlisted job type
> under bounded local controls.

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
- missing-key behavior, using a key-absent environment or equivalent safe
  fixture;
- invalid-key behavior with deterministic redaction probe;
- audit trail includes request, running, success/failure, and evidence refs;
- output redaction verified before UI display and persistence.

#### Redaction Positive Test

Use an obviously fake API key value, for example:

```text
test_invalid_cvf_redaction_probe_20260508
```

The evidence must verify that this exact value does not appear in:

- stdout;
- stderr;
- JSON result artifact;
- persisted Web job state;
- browser-visible API response;
- HAR/network capture or equivalent browser evidence.

The fake-key probe must fail closed with an expected invalid-provider-key or
provider-auth error. The failure is acceptable only if the key value is absent
from every recorded output.

**Artifact:**
`docs/reviews/CVF_C5_WEB_TRIGGERED_FULL_RELEASE_GATE_EVIDENCE_2026-05-08.md`

**Exit claim allowed:**

> CVF Web can trigger a full live release gate under RBAC, timeout, rate, cost,
> redaction, and audit controls.

**Exit claim forbidden:**

- Arbitrary Web-triggered governance jobs.
- Public hosted control plane.
- GA-ready unless Track R, C5, and the applicable CI tracks also close.

---

## Part 5 — Track CI2: Protected Live Release Gate Automation

**Purpose:** Make release-quality proof repeatable without forcing every PR or
contributor to have live provider keys.

**Status:** Candidate track after C5.2-C5.4 are stable.

### CI2.0 — Protected Live Release Gate Design

Define a protected/manual/scheduled lane:

| Lane | Trigger | Secret requirement | Purpose |
|---|---|---|---|
| `protected_live_release_gate` | manual dispatch / scheduled / protected branch | live provider secret | release-quality proof |

Live governance claims must never be inferred from CI1 static checks.

**Artifact:**
`docs/reviews/CVF_PROTECTED_LIVE_RELEASE_GATE_CI_DESIGN_2026-05-08.md`

### CI2.1 — Protected Live Release Gate Implementation

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

### CI2.2 — Claim Sync

Update claim surfaces only after the first successful protected live CI run.

**Exit claim allowed:**

> CVF has a protected CI lane for release-quality live governance proof.

**Exit claim forbidden:**

- Every PR proves live governance.
- CI can run live proof without configured secrets.

---

## Part 6 — Track M: Optional Managed Runtime Adapter Planning

**Purpose:** Prepare for teams that explicitly want hosted/shared CVF while
preserving local-first operation as the default.

**Status:** Deferred planning track. Do not mix into R/C5/CI unless operator
explicitly authorizes it.

### M0 — Runtime Job Store Interface Extraction

Before any managed adapter exists:

1. Enumerate every RC2 runtime job state write and read path.
2. Formalize the intentional contract as `RuntimeJobStore`.
3. Refactor current JSONL behavior into `FileBackedRuntimeJobStore` as a
   no-behavior-change local-first implementation.
4. Preserve `.cvf/runtime/web-governance-jobs.jsonl` as the default local
   persistence path.
5. Verify existing C3/C4 job evidence and Web operations behavior still pass.

Initial shape:

```text
RuntimeJobStore
  -> FileBackedRuntimeJobStore   # default local-first adapter
  -> PostgresRuntimeJobStore     # optional managed adapter, later
```

Rules:

- file-backed JSONL remains the default;
- Postgres/Supabase is opt-in;
- no local developer must upload CVF job/evidence data to a third-party cloud;
- adapter selection must be explicit through configuration;
- local evidence format must remain inspectable.

### M1 — Postgres Managed Adapter Candidate

`PostgresRuntimeJobStore` is the technology-neutral adapter name. Supabase is a
possible deployment choice for that adapter, not the public interface name.

Supabase can be considered because it provides:

- hosted Postgres persistence;
- row-level security;
- auth integration;
- managed dashboard queryability;
- operational convenience for teams that choose hosted/shared CVF.

But Supabase must remain optional product depth, not RC2/GA local proof.

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

## Part 7 — Suggested Execution Plan

### Step 1 — Static CI

Create:

```text
CVF_STATIC_CI_GATE_ROADMAP_2026-05-08.md
```

This is non-secret and may run before R.

### Step 2 — R Regression

Create:

```text
CVF_RC2_R1_PRE_GA_NONCODER_REGRESSION_REPLAY_ROADMAP_2026-05-08.md
```

R1/R2 must close before C5.2-C5.4 implementation.

### Step 2a — C5 Design In Parallel

Create:

```text
CVF_RC2_C5_FULL_RELEASE_GATE_THREAT_MODEL_AND_CONTROL_CONTRACT_ROADMAP_2026-05-08.md
```

C5.0/C5.1 may run while R executes because they are design-only. They do not
authorize C5 runtime implementation.

### Step 3 — C5 Implementation

Create:

```text
CVF_RC2_C5_FULL_LIVE_RELEASE_GATE_FROM_WEB_ROADMAP_2026-05-08.md
```

C5.2-C5.4 may begin only after:

- R3 returns `PROCEED_TO_C5_IMPLEMENTATION`;
- C5.0/C5.1 are accepted;
- no open regression requires repair first.

### Step 4 — Protected Live CI

Create:

```text
CVF_PROTECTED_LIVE_RELEASE_GATE_CI_ROADMAP_2026-05-08.md
```

CI2 should reuse the canonical release command and align with C5 evidence
controls.

### Step 5 — Optional Managed State

Create only if the operator chooses managed/cloud productization:

```text
CVF_MANAGED_RUNTIME_STATE_AND_POSTGRES_ADAPTER_ROADMAP_2026-05-08.md
```

This roadmap must state that local JSONL/file-backed operation remains the
default and that Supabase is optional deployment infrastructure.

---

## Part 8 — Global Stop Rules

Stop and ask for operator decision if:

- a step would require uploading local CVF data to a cloud service by default;
- a Web control requires free-form command execution;
- a live governance claim would be backed only by mock/UI evidence;
- a release gate run cannot access a live provider key when live proof is
  required;
- raw API keys appear in logs, artifacts, browser output, or CI output;
- C5.2-C5.4 attempts to bypass R1/R2 post-RC2 regression evidence;
- Supabase work starts before local-first adapter boundaries are documented;
- a redaction positive test cannot be run deterministically with a fake key.

---

## Part 9 — Claude Re-Review Questions

Ask Claude to critique these exact points:

1. Does CI1-before-R improve evidence quality without mixing runtime concerns?
2. Is R1's N >= 18 Alibaba matrix a sufficient bounded regression proof, or
   should it be labeled smoke-only?
3. Does R2 now repair the admin-role Claim N weakness through separate
   positive and negative role journeys?
4. Are C5.0/C5.1 safe to run in parallel with R while blocking C5.2+?
5. Is the C5.4 fake-key redaction probe strong enough?
6. Does `PostgresRuntimeJobStore` plus optional Supabase deployment preserve
   local-first and avoid vendor lock-in?
7. Are public-doc underclaim checks in R3 scoped narrowly enough?

---

## Claim Boundary

Allowed after this V2 draft is accepted:

> CVF has a revised post-RC2 Pre-GA validation and C5 readiness roadmap that
> addresses critique points on evidence specification, sequencing, and control
> verification.

Still forbidden after this V2 draft:

- Post-RC2 no-regression is proven.
- C5 is implemented.
- Web can trigger the full live release gate.
- Release gate CI is implemented.
- CVF is GA-ready.
- Supabase is the default CVF persistence layer.
