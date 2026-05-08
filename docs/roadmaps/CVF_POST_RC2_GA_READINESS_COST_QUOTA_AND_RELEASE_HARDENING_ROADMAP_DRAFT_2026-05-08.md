<!-- Memory class: FULL_RECORD -->
# CVF Post-RC2 GA Readiness, Cost/Quota Guard, And Release Hardening Roadmap Draft

**Date:** 2026-05-08
**Status:** DRAFT FOR CLAUDE REVIEW — NOT AUTHORIZED FOR IMPLEMENTATION
**Branch basis:** `main` after RC2 Foundation + RC2 Pre-GA R/C5 push
**Purpose:** Define the remaining local-first work needed before a GA readiness
decision, with cost/quota control promoted ahead of additional live matrices.

## Executive Decision

Do **not** start GA packaging yet.

RC2 now has strong local-first evidence: CI1 static gate, R post-RC2 non-coder
regression, Web-triggered full live release gate, and CI2 protected workflow
implementation. The next work should be deliberately smaller and risk-ranked:

1. prove the protected hosted CI2 live gate after push;
2. install deeper cost/quota guardrails before any more high-volume live proof;
3. close the browser-visible redaction gap;
4. run DeepSeek confirmatory post-RC2 regression under the new budget controls;
5. only then write the GA readiness decision packet.

Managed/cloud state remains out of scope for this roadmap. Local JSONL remains
the default CVF runtime job store. Postgres/Supabase is a later optional managed
deployment track, not a blocker for local-first GA.

## Current Baseline

Already closed:

- CI1 static gate: `python scripts/run_cvf_static_ci_gate.py --json` PASS.
- R regression: `20/18` successful checks, 10/10 families, Alibaba-only.
- R2 role-bound repair: `2/2` checks.
- C5 Web-triggered full live release gate: Web job `full_live_release_gate`
  returned release gate 7/7 PASS.
- C5 deterministic fake-key redaction probe: covers stdout, stderr, returned
  job object, and persisted runtime state.
- CI2 workflow implementation:
  `.github/workflows/cvf-protected-live-release-gate.yml`.

Still open:

- CI2 has not yet produced a hosted GitHub Actions PASS artifact.
- Cost/quota control is still mostly warning + timeout/concurrency, not a
  budget policy with preflight estimates and blocking.
- C5.4 browser response and HAR/network redaction streams are not E2E-covered.
- DeepSeek post-RC2 regression remains unknown for the R matrix.
- GA readiness packet has not been written.

## Sequencing

| Order | Track | Purpose | Dependency |
|---:|---|---|---|
| 0 | CI2-H | Hosted protected live release gate proof | push complete |
| 1 | CQ | Cost/quota guard depth | before new live matrices |
| 2 | BR | Browser redaction closure | after CQ or in parallel if no live calls |
| 3 | DS | DeepSeek post-RC2 regression confirmation | CQ controls active |
| 4 | GA | GA readiness packet and decision | CI2-H + CQ + BR + DS |
| 5 | M | Optional managed state planning | separate later decision |

Track CQ is intentionally before DS. Additional live matrices should not run
until the operator can see and enforce budget posture.

---

## Track CI2-H — Hosted Protected Live Release Gate Proof

**Purpose:** Convert "CI2 implemented" into "CI2 hosted PASS".

### CI2-H0 — Environment And Secret Readiness

Verify GitHub environment and secrets without printing secret values:

- environment: `cvf-live-release-gate`;
- manual confirmation input: `RUN_LIVE_GATE`;
- one DashScope-compatible key configured through repository or organization
  secrets;
- optional DeepSeek key configured if DS follow-up will use hosted proof later.

**Artifact:**
`docs/reviews/CVF_CI2_HOSTED_LIVE_GATE_ENVIRONMENT_READINESS_2026-05-08.md`

### CI2-H1 — Manual Hosted Run

Run:

```text
CVF Protected Live Release Gate -> workflow_dispatch -> RUN_LIVE_GATE
```

Expected result:

- workflow completes successfully;
- uploaded artifact `cvf-protected-live-release-gate-result.json`;
- gate result is PASS;
- 7/7 release checks PASS.

**Artifact:**
`docs/reviews/CVF_CI2_HOSTED_LIVE_GATE_EVIDENCE_2026-05-08.md`

### CI2-H2 — Claim Sync

After hosted PASS only, update handoff/claim surfaces from:

> CI2 protected live release gate workflow is implemented pending hosted run.

to:

> CI2 protected live release gate has a hosted manual PASS artifact.

**Exit claim forbidden before H1 passes:**

- protected CI has passed;
- GitHub-hosted release proof is available;
- CI2 is release-quality evidence.

---

## Track CQ — Cost/Quota Guard Depth

**Purpose:** Prevent CVF live proof and Web-triggered operations from becoming
an uncontrolled spend/quota surface.

### CQ0 — Cost/Quota Threat Model

Document operator risks:

- repeated CI2 manual dispatch;
- repeated Web `full_live_release_gate` clicks;
- DeepSeek/Alibaba regression matrix expansion;
- accidental live calls during local testing;
- quota exhaustion causing false regressions;
- cost spike without local audit trail.

**Artifact:**
`docs/reviews/CVF_COST_QUOTA_GUARD_THREAT_MODEL_2026-05-08.md`

### CQ1 — Local Budget Policy Contract

Define a local-first policy file, likely:

```text
.cvf/config/cost-quota-policy.json
```

Required fields:

| Field | Purpose |
|---|---|
| `dailyLiveCallLimit` | max live provider calls per local day |
| `perJobLiveCallLimit.full_live_release_gate` | cap per full gate job |
| `perJobLiveCallLimit.deepseek_regression` | cap per DS matrix job |
| `cooldownSeconds.full_live_release_gate` | minimum delay between full gates |
| `requireOwnerOverrideAboveLimit` | block or require explicit override |
| `auditMode` | append-only local audit by default |

Default policy should be conservative, local, and editable by the operator.

**Artifact:**
`docs/reviews/CVF_COST_QUOTA_LOCAL_POLICY_CONTRACT_2026-05-08.md`

### CQ2 — Runtime Estimate And Preflight

Add a deterministic estimator before live jobs launch.

Minimum estimates:

- `full_live_release_gate`: expected check bundle and live E2E count category;
- `provider_check`: one live provider readiness call;
- `deepseek_post_rc2_regression`: planned matrix count;
- manual override reason when over threshold.

The estimator does not need exact dollar pricing for GA readiness. It must at
least enforce live-call budgets and record estimated impact.

**Runtime targets:**

- `web-governance-jobs.ts`;
- `/api/system/jobs`;
- Governance Operations UI.

**Artifact:**
`docs/reviews/CVF_COST_QUOTA_PREFLIGHT_EVIDENCE_2026-05-08.md`

### CQ3 — Web Operator UX

Before a live job runs, Web must show:

- job class;
- estimated live call impact;
- current daily/session usage;
- configured cap;
- warning if near cap;
- block reason if over cap;
- owner/admin override path if allowed.

For RC2/Pre-GA, a simple confirmation affordance is acceptable if the policy
check is server-side and audit-backed.

**Artifact:**
`docs/reviews/CVF_COST_QUOTA_WEB_OPERATOR_EVIDENCE_2026-05-08.md`

### CQ4 — Audit Trail

Append cost/quota decision events to local runtime audit, without raw keys:

- estimate requested;
- estimate allowed/blocked;
- live job launched;
- usage counter incremented;
- override used, if any.

Default audit storage remains local JSONL. No cloud store is introduced.

**Artifact:**
`docs/reviews/CVF_COST_QUOTA_AUDIT_EVIDENCE_2026-05-08.md`

### CQ5 — Verification

Required checks:

- under-limit full gate allowed;
- over-limit full gate blocked;
- repeated full gate before cooldown blocked;
- provider check estimate recorded;
- no raw provider key appears in cost/quota audit;
- static CI gate PASS;
- no live provider call is required for over-limit blocking tests.

Optional live proof:

- one live full gate under the policy after CQ controls are installed.

**Exit claim allowed:**

> CVF has local-first cost/quota guardrails for Web-triggered live governance
> jobs, with preflight estimates, blocking, and audit trail.

**Exit claim forbidden:**

- exact provider billing reconciliation;
- cloud FinOps dashboard;
- multi-tenant quota enforcement;
- universal cost accuracy.

---

## Track BR — Browser Redaction Closure

**Purpose:** Close the remaining C5.4 browser-visible streams that the
deterministic unit probe intentionally left open.

### BR0 — Browser Fake-Key Test Design

Design a test that uses the fake key:

```text
test_invalid_cvf_redaction_probe_20260508
```

It must not use a real provider key and must not run a live provider call.

### BR1 — Browser Response Probe

Trigger a mocked `full_live_release_gate` result through the API/UI route so
the browser receives a job response containing redacted stdout/stderr.

Required assertion:

- fake key absent from browser-visible `/api/system/jobs` response body;
- `[REDACTED]` present where the fake key was injected.

### BR2 — HAR/Network Probe

Capture network traffic for the browser fake-key run.

Required assertion:

- fake key absent from HAR/network capture;
- response payload remains redacted.

**Artifact:**
`docs/reviews/CVF_C5_BROWSER_REDACTION_6_STREAM_EVIDENCE_2026-05-08.md`

**Exit claim allowed:**

> C5 redaction positive proof covers stdout, stderr, returned job object,
> persisted runtime state, browser-visible response, and HAR/network capture.

---

## Track DS — DeepSeek Post-RC2 Regression Confirmation

**Purpose:** Reduce the R evidence boundary from Alibaba-only to bounded
Alibaba + DeepSeek confirmation after cost/quota controls exist.

### DS0 — Scope

Do not replay the full W149 corpus unless separately authorized. Use a bounded
DeepSeek matrix covering the same capability families as R, at a lower count if
cost/quota policy requires it.

Minimum suggested scope:

| Family | Minimum DeepSeek checks |
|---|---:|
| first value + receipt | 1 |
| intent routing | 1 |
| continuity | 1 |
| clarification | 1 |
| deliverable pack | 1 |
| trusted form | 1 |
| export/readout/metrics sanity | 2 combined |

Minimum total: **N >= 8** successful checks, unless CQ policy sets a lower
operator-approved cap. If lower, the artifact must say it is a smoke check, not
a regression confirmation.

### DS1 — Live Run

Run under cost/quota guard:

- DeepSeek provider lane;
- explicit run count;
- receipt state;
- failure classification;
- budget estimate and final usage audit reference.

**Artifact:**
`docs/reviews/CVF_DEEPSEEK_POST_RC2_REGRESSION_CONFIRMATION_2026-05-08.md`

**Exit claim allowed if N >= 8 passes:**

> DeepSeek has bounded post-RC2 regression confirmation for the selected
> non-coder families.

**Exit claim forbidden:**

- full DeepSeek parity with Alibaba;
- full 40-form DeepSeek replay;
- DeepSeek cost/performance equivalence.

---

## Track GA — GA Readiness Packet

**Purpose:** Make a final bounded decision: GA, RC3, or hold.

### GA0 — Evidence Index

Index:

- RC1 publication;
- RC2 Foundation;
- RC2 Pre-GA R/C5;
- CI1 static;
- CI2 hosted PASS;
- CQ guard;
- BR redaction closure;
- DS confirmation or explicit DS boundary.

**Artifact:**
`docs/reviews/CVF_GA_READINESS_EVIDENCE_INDEX_2026-05-08.md`

### GA1 — Known Limitations Refresh

Refresh limitations:

- local-first only;
- optional managed state deferred;
- no default Supabase/Postgres;
- multi-tenant hosted posture not GA;
- cost/quota is local guard, not exact billing;
- provider parity boundaries.

**Artifact:**
`docs/reviews/CVF_GA_KNOWN_LIMITATIONS_REFRESH_2026-05-08.md`

### GA2 — Decision Packet

Decision options:

| Decision | Meaning |
|---|---|
| `GA_LOCAL_FIRST_APPROVED` | local-first GA may publish |
| `RC3_REQUIRED` | one or more release-facing blockers remain |
| `HOLD_FOR_MANAGED_MODE` | operator chooses hosted/managed as GA requirement |

**Artifact:**
`docs/reviews/CVF_GA_READINESS_DECISION_2026-05-08.md`

---

## Deferred Track M — Optional Managed State

Not part of this roadmap's implementation.

Future work may define:

- `RuntimeJobStore` interface;
- `FileBackedRuntimeJobStore` as default local implementation;
- `PostgresRuntimeJobStore` as optional managed adapter;
- Supabase as one possible Postgres deployment option;
- tenant/org boundary and RLS only for managed mode.

This must not block local-first GA unless the operator explicitly changes the
product requirement from local-first to hosted/managed.

---

## Stop Rules

Stop and ask for operator decision if:

- CI2 hosted run fails because secrets/environment are unavailable;
- cost/quota policy cannot block over-limit live jobs server-side;
- redaction browser/HAR probe reveals the fake key;
- DS regression consumes more live quota than planned;
- any artifact would imply Supabase/Postgres is required for local-first CVF;
- any GA packet would claim provider parity or hosted multi-tenant readiness
  without evidence.

## Verification Baseline For This Roadmap

Before implementation:

```bash
git status --short --branch
python scripts/run_cvf_static_ci_gate.py --json
```

For any governance behavior claim:

```bash
python scripts/run_cvf_release_gate_bundle.py --json
```

Mock mode is allowed only for BR fake-key browser redaction tests because those
tests assert redaction behavior, not live provider governance.

## Claude Re-Review Questions

1. Is CQ correctly promoted ahead of DS and GA?
2. Is CI2-H scoped narrowly enough to avoid overclaiming hosted proof before a
   manual run completes?
3. Is CQ's call-count guard sufficient for local-first GA, or must dollar-price
   estimation be mandatory before GA?
4. Does BR close the C5.4 gap without requiring a real provider key?
5. Is DS N >= 8 a reasonable bounded confirmation, or should DeepSeek require a
   larger post-RC2 matrix?
6. Does the roadmap preserve the operator's local-first principle and keep
   Supabase/Postgres deferred?
7. Are the GA decision options strict enough to prevent premature GA?
