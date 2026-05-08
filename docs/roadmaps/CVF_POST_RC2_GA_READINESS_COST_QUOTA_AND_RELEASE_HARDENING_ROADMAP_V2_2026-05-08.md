<!-- Memory class: FULL_RECORD -->
# CVF Post-RC2 GA Readiness, Cost/Quota Guard, And Release Hardening Roadmap V2

**Date:** 2026-05-08
**Status:** DRAFT V2 FOR CLAUDE RE-REVIEW - NOT AUTHORIZED FOR IMPLEMENTATION
**Branch basis:** `main` after RC2 Foundation + RC2 Pre-GA R/C5 push
**Purpose:** Define the remaining local-first work needed before a GA readiness
decision, with cost/quota control promoted ahead of additional live matrices.
**Supersedes draft:** `docs/roadmaps/CVF_POST_RC2_GA_READINESS_COST_QUOTA_AND_RELEASE_HARDENING_ROADMAP_DRAFT_2026-05-08.md`
**Claude rebuttal response:** `docs/reviews/CVF_POST_RC2_GA_READINESS_ROADMAP_CODEX_RESPONSE_TO_CLAUDE_2026-05-08.md`

## Executive Decision

Do **not** start GA packaging or implementation yet.

RC2 now has strong local-first evidence: CI1 static gate, R post-RC2 non-coder
regression, Web-triggered full live release gate, and CI2 protected workflow
implementation. The next work should be deliberately smaller and risk-ranked:

1. prove the protected hosted CI2 live gate after push, including metadata
   sanity and failure handling;
2. close browser-visible redaction streams with a deterministic fake-key probe;
3. install deeper local cost/quota guardrails before new high-volume live proof;
4. run DeepSeek smoke/sanity coverage under the new budget controls;
5. only then write the GA readiness decision packet.

Managed/cloud state remains out of scope for this roadmap. Local JSONL remains
the default CVF runtime job store. Postgres/Supabase is a later optional
managed deployment track, not a blocker for local-first GA.

## V2 Revision Summary

This V2 incorporates Claude's 15-point rebuttal:

- CI2-H now includes pre-run/pre-push GitHub environment and secrets metadata
  sanity checks, without reading or printing secret values.
- CI2-H now has an explicit hosted-run failure artifact and downstream block
  rule.
- CQ policy now defines time windows and per-provider lane budgets.
- CQ estimator now returns integer call estimates, not vague categories.
- CQ enforcement is server-side only; UI confirmation is informational.
- CQ verification now requires live under-budget proof plus mocked block,
  direct API block, owner override, and non-owner denial checks.
- BR fake-key proof must inject at the `runCommand` layer before redaction.
- DS is renamed from regression confirmation to smoke/sanity coverage unless
  expanded to N>=14.
- GA evidence now includes documentation currency and first-run trust signals.
- GA decision options now include `GA_LOCAL_FIRST_APPROVED_WITH_LIMITS`.
- Stop rules now cover policy-file secrets and impossible DS budget caps.
- Verification baseline now checks remote sync with `git fetch origin`.

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
- Browser response and HAR/network redaction streams are not E2E-covered.
- Cost/quota control is still mostly warning + timeout/concurrency, not a
  budget policy with preflight estimates and blocking.
- DeepSeek post-RC2 coverage remains unknown for the R matrix.
- GA readiness packet has not been written.

## Sequencing

| Order | Track | Purpose | Dependency |
|---:|---|---|---|
| 0 | CI2-H | Hosted protected live release gate proof | push complete; metadata sanity before hosted run |
| 1 | BR | Browser redaction closure | fully mocked, no live calls; can run after CI2-H scoping |
| 2 | CQ | Cost/quota guard depth | before new live matrices |
| 3 | DS | DeepSeek post-RC2 smoke/sanity coverage | CQ controls active |
| 4 | GA | GA readiness packet and decision | CI2-H + BR + CQ + DS |
| 5 | M | Optional managed state planning | separate later decision |

Track CQ is intentionally before DS. Additional live matrices should not run
until the operator can see and enforce budget posture.

Track BR is intentionally no-live-call. It may run before CQ because it uses a
fake key and mocked command output to verify redaction behavior, not provider
governance behavior.

---

## Track CI2-H - Hosted Protected Live Release Gate Proof

**Purpose:** Convert "CI2 implemented" into "CI2 hosted PASS", or record a
bounded hosted failure before any downstream claim depends on CI2.

### CI2-H0 - Environment And Secret Readiness

Verify GitHub environment and secrets metadata without printing secret values:

- environment: `cvf-live-release-gate`;
- manual confirmation input: `RUN_LIVE_GATE`;
- one DashScope-compatible key configured through repository, organization, or
  environment secrets;
- optional DeepSeek key configured only if DS follow-up will use hosted proof
  later.

**Artifact:**
`docs/reviews/CVF_CI2_HOSTED_LIVE_GATE_ENVIRONMENT_READINESS_2026-05-08.md`

### CI2-H0a - Pre-Run/Pre-Push Secrets Metadata Sanity

Before the hosted run, and before future pushes that claim CI2-H readiness,
run metadata-only checks such as:

```bash
gh api repos/{owner}/{repo}/environments/cvf-live-release-gate
gh api repos/{owner}/{repo}/environments/cvf-live-release-gate/secrets --jq '.secrets[].name'
```

Required assertions:

- environment exists;
- at least one accepted DashScope-compatible secret name is listed, such as
  `DASHSCOPE_API_KEY`, `ALIBABA_API_KEY`, `CVF_ALIBABA_API_KEY`, or
  `CVF_BENCHMARK_ALIBABA_KEY`;
- secret values are never fetched, printed, copied into artifacts, or committed;
- failure is recorded before making any hosted PASS claim.

**Artifact:**
`docs/reviews/CVF_CI2_HOSTED_LIVE_GATE_SECRET_METADATA_SANITY_2026-05-08.md`

### CI2-H1 - Manual Hosted Run

Run:

```text
CVF Protected Live Release Gate -> workflow_dispatch -> RUN_LIVE_GATE
```

Expected result:

- workflow completes successfully;
- uploaded artifact `cvf-protected-live-release-gate-result.json`;
- gate result is PASS;
- 7/7 release checks PASS;
- no raw provider key appears in logs or artifacts.

**Artifact:**
`docs/reviews/CVF_CI2_HOSTED_LIVE_GATE_EVIDENCE_2026-05-08.md`

### CI2-H1a - Hosted Run Failure Path

If CI2-H1 fails, do not silently retry into a PASS-only story.

Required failure handling:

- classify failure mode: missing secret, missing environment, quota exhausted,
  provider/network failure, workflow syntax failure, or unknown;
- capture run URL, job conclusion, relevant redacted log summary, and whether
  the lane failed closed;
- file a bounded failure artifact;
- block downstream tracks until either a re-run produces PASS or the operator
  explicitly defers CI2-H as a known limit.

**Artifact:**
`docs/reviews/CVF_CI2_HOSTED_LIVE_GATE_FAILURE_MODE_2026-05-08.md`

### CI2-H2 - Claim Sync

After hosted PASS only, update handoff/claim surfaces from:

> CI2 protected live release gate workflow is implemented pending hosted run.

to:

> CI2 protected live release gate has a hosted manual PASS artifact.

If CI2-H is deferred after failure, the claim must instead say:

> CI2 protected live release gate is implemented, but hosted PASS is deferred
> and is listed as a GA known limit.

**Exit claim forbidden before H1 passes:**

- protected CI has passed;
- GitHub-hosted release proof is available;
- CI2 is release-quality hosted evidence.

---

## Track BR - Browser Redaction Closure

**Purpose:** Close the remaining C5.4 browser-visible streams that the
deterministic unit probe intentionally left open.

### BR0 - Browser Fake-Key Test Design

Design a no-live-call test that uses the fake key:

```text
test_invalid_cvf_redaction_probe_20260508
```

Required design constraints:

- no real provider key is used;
- no live provider call is made;
- mock injection MUST happen at the `runCommand` layer before the redaction
  pipeline runs;
- the `runCommand` mock returns fake-key-bearing stdout/stderr, for example:

```text
stdout: "provider_key=test_invalid_cvf_redaction_probe_20260508"
stderr: "ALIBABA_API_KEY=test_invalid_cvf_redaction_probe_20260508"
```

Forbidden design:

- mocking the API response after redaction;
- serving a pre-redacted response body directly to the browser;
- treating API-response-layer mocks as redaction proof.

### BR1 - Browser Response Probe

Trigger a mocked `full_live_release_gate` result through the API/UI route so
the browser receives a job response after normal redaction processing.

Required assertions:

- fake key absent from browser-visible `/api/system/jobs` response body;
- `[REDACTED]` or the canonical redaction token is present where the fake key
  was injected;
- returned job object remains structurally useful to the Web UI.

### BR2 - HAR/Network Probe

Capture network traffic for the browser fake-key run.

Required assertions:

- fake key absent from HAR/network capture;
- response payload remains redacted;
- persisted runtime state remains redacted.

**Artifact:**
`docs/reviews/CVF_C5_BROWSER_REDACTION_6_STREAM_EVIDENCE_2026-05-08.md`

**Exit claim allowed:**

> C5 redaction positive proof covers stdout, stderr, returned job object,
> persisted runtime state, browser-visible response, and HAR/network capture.

**Exit claim forbidden:**

- browser redaction is closed if the fake key is injected after redaction;
- redaction proof used a real provider key;
- BR proves live provider governance behavior.

---

## Track CQ - Cost/Quota Guard Depth

**Purpose:** Prevent CVF live proof and Web-triggered operations from becoming
an uncontrolled spend/quota surface.

### CQ0 - Cost/Quota Threat Model

Document operator risks:

- repeated CI2 manual dispatch;
- repeated Web `full_live_release_gate` clicks;
- DeepSeek/Alibaba regression matrix expansion;
- accidental live calls during local testing;
- quota exhaustion causing false regressions;
- cost spike without local audit trail;
- direct API bypass of Web confirmation;
- owner override misuse;
- policy file accidentally containing secrets.

**Artifact:**
`docs/reviews/CVF_COST_QUOTA_GUARD_THREAT_MODEL_2026-05-08.md`

### CQ1 - Local Budget Policy Contract

Define a local-first policy file:

```text
.cvf/config/cost-quota-policy.json
```

The operator-specific policy file is local-only by default. A committed example
file may exist, but the active policy must not contain provider keys, tokens, or
machine-specific secrets.

Required schema shape:

```json
{
  "version": 1,
  "windowMode": "rolling_24h",
  "globalDailyLiveCallLimit": 120,
  "providerLanes": {
    "alibaba": {
      "dailyLiveCallLimit": 100,
      "perJobLiveCallLimit": {
        "full_live_release_gate": 20,
        "provider_check": 2
      }
    },
    "deepseek": {
      "dailyLiveCallLimit": 30,
      "perJobLiveCallLimit": {
        "deepseek_post_rc2_smoke": 8,
        "deepseek_post_rc2_confirmation": 14
      }
    }
  },
  "cooldownSeconds": {
    "full_live_release_gate": 300
  },
  "requireOwnerOverrideAboveLimit": true,
  "auditMode": "append_only_jsonl"
}
```

Allowed `windowMode` values:

- `rolling_24h` - preferred default for local-first operator safety;
- `utc_calendar_day` - acceptable if documented in the evidence artifact.

Required fields:

| Field | Purpose |
|---|---|
| `windowMode` | defines the budget time boundary explicitly |
| `globalDailyLiveCallLimit` | whole-installation upper bound |
| `providerLanes.*.dailyLiveCallLimit` | per-provider call cap |
| `providerLanes.*.perJobLiveCallLimit.*` | per-job cap by provider |
| `cooldownSeconds.*` | minimum delay between repeated expensive jobs |
| `requireOwnerOverrideAboveLimit` | controls whether override is required |
| `auditMode` | append-only local audit by default |

**Artifact:**
`docs/reviews/CVF_COST_QUOTA_LOCAL_POLICY_CONTRACT_2026-05-08.md`

### CQ2 - Runtime Estimate And Preflight

Add a deterministic estimator before live jobs launch.

The estimator must produce integer call estimates:

```typescript
interface LiveCallEstimate {
  jobType: string;
  providerLane: 'alibaba' | 'deepseek' | 'mixed';
  expectedLiveCallCount: number;
  estimateConfidence: 'high' | 'low';
  estimateBasis: string;
  policyWindowMode: 'rolling_24h' | 'utc_calendar_day';
}
```

Minimum estimate coverage:

- `full_live_release_gate`: fixed release bundle estimate plus live E2E count;
- `provider_check`: one live provider readiness call;
- `deepseek_post_rc2_smoke`: planned N count;
- `deepseek_post_rc2_confirmation`: planned N count if separately authorized;
- manual override reason when over threshold.

The estimator does not need exact dollar pricing for local-first GA readiness.
It must enforce live-call budgets and record estimated impact.

**Runtime targets:**

- `web-governance-jobs.ts`;
- `/api/system/jobs`;
- Governance Operations UI;
- local runtime audit writer.

**Artifact:**
`docs/reviews/CVF_COST_QUOTA_PREFLIGHT_EVIDENCE_2026-05-08.md`

### CQ3 - Server-Side Enforcement And Web Operator UX

The Web UI may show a confirmation dialog for operator experience, but the
enforcement contract is server-side only.

Server-side preflight in the Web job path and `/api/system/jobs` MUST block
over-limit jobs regardless of UI state. A direct API call that bypasses the UI
must hit the same server gate.

Before a live job runs, Web should show:

- job class;
- provider lane;
- estimated live call impact;
- current window usage;
- configured cap;
- cooldown state;
- warning if near cap;
- block reason if over cap;
- owner/admin override path if allowed.

The UI confirmation is informational. It is not a budget control by itself.

**Artifact:**
`docs/reviews/CVF_COST_QUOTA_WEB_OPERATOR_EVIDENCE_2026-05-08.md`

### CQ4 - Audit Trail

Append cost/quota decision events to local runtime audit, without raw keys:

- estimate requested;
- estimate allowed or blocked;
- live job launched;
- usage counter incremented;
- cooldown block;
- owner override used;
- non-owner override denied;
- direct API bypass blocked;
- policy validation failed.

Override audit events must include:

- role;
- reason;
- timestamp;
- job ID;
- provider lane;
- estimated live call count;
- no raw provider key.

Default audit storage remains local JSONL. No cloud store is introduced.

**Artifact:**
`docs/reviews/CVF_COST_QUOTA_AUDIT_EVIDENCE_2026-05-08.md`

### CQ5 - Verification

Required checks:

- one live `full_live_release_gate` run under budget is allowed;
- under-budget live run increments the usage counter in audit;
- over-budget attempted run with a temporary zero-cap policy is blocked before
  provider call;
- direct API over-budget attempt is blocked before provider call;
- repeated full gate before cooldown is blocked;
- owner over-budget override is allowed when policy permits it and records
  `override_used`;
- non-owner over-budget override is blocked and records `override_denied`;
- provider check estimate is recorded as an integer;
- no raw provider key appears in cost/quota policy, audit, logs, or artifacts;
- static CI gate PASS.

No live provider call is required for over-limit blocking tests. The live call
requirement applies only to the under-budget allow path.

**Exit claim allowed:**

> CVF has local-first cost/quota guardrails for Web-triggered live governance
> jobs, with integer preflight estimates, server-side blocking, cooldown,
> override audit, and local usage trail.

**Exit claim forbidden:**

- exact provider billing reconciliation;
- cloud FinOps dashboard;
- multi-tenant quota enforcement;
- universal cost accuracy;
- UI confirmation alone is a budget guard.

---

## Track DS - DeepSeek Post-RC2 Smoke/Sanity Coverage

**Purpose:** Reduce the R evidence boundary from Alibaba-only to bounded
Alibaba + DeepSeek smoke/sanity evidence after cost/quota controls exist.

### DS0 - Scope

Do not replay the full W149 corpus unless separately authorized.

Minimum suggested smoke/sanity scope:

| Family | Minimum DeepSeek checks |
|---|---:|
| first value + receipt | 1 |
| intent routing | 1 |
| continuity | 1 |
| clarification | 1 |
| deliverable pack | 1 |
| trusted form | 1 |
| export/readout/metrics sanity | 2 combined |

Minimum total for smoke/sanity: **N >= 8** successful checks.

If the claim needs to say "regression confirmation", the minimum must rise to
**N >= 14** successful checks, with approximately two checks per selected
family. Otherwise the artifact must use smoke/sanity wording only.

If CQ policy sets a cap lower than N>=8, the test is not runnable as scoped and
must stop for operator decision rather than silently lowering the evidence bar.

### DS1 - Live Run

Run under cost/quota guard:

- DeepSeek provider lane;
- explicit run count;
- receipt state;
- failure classification;
- budget estimate and final usage audit reference.

**Artifact:**
`docs/reviews/CVF_DEEPSEEK_POST_RC2_SMOKE_COVERAGE_2026-05-08.md`

**Exit claim allowed if N>=8 passes:**

> DeepSeek has bounded post-RC2 smoke/sanity coverage for the selected
> non-coder families. This is not a full regression confirmation.

**Exit claim allowed if N>=14 passes and family coverage supports it:**

> DeepSeek has bounded post-RC2 regression confirmation for the selected
> non-coder families.

**Exit claim forbidden after N>=8 only:**

- DeepSeek regression confirmation;
- full DeepSeek parity with Alibaba;
- full 40-form DeepSeek replay;
- DeepSeek cost/performance equivalence.

---

## Track GA - GA Readiness Packet

**Purpose:** Make a final bounded decision: GA, GA with known limits, RC3, or
hold.

### GA0 - Evidence Index

Index:

- RC1 publication;
- RC2 Foundation;
- RC2 Pre-GA R/C5;
- CI1 static;
- CI2 hosted PASS or explicit CI2-H known-limit deferral;
- BR redaction closure;
- CQ guard;
- DS smoke/sanity coverage, DS confirmation, or explicit DS boundary.

**Artifact:**
`docs/reviews/CVF_GA_READINESS_EVIDENCE_INDEX_2026-05-08.md`

### GA0a - Documentation Currency Audit

Verify public/user-facing trust signals:

- README mentions current RC2 capabilities, including Web operations,
  intent-first flow, evidence receipt, and local-first posture;
- GET_STARTED is reproducible for a Day-1 user;
- `new-cvf-workspace.ps1` succeeds end-to-end on a clean Windows machine;
- optional macOS/Linux bootstrap is either verified or explicitly listed as
  not covered;
- public examples work from a fresh clone or are marked as archived;
- app onboarding and design references match shipped UI;
- docs do not imply Supabase/Postgres is required for local-first CVF.

**Artifact:**
`docs/reviews/CVF_GA_DOCUMENTATION_CURRENCY_AUDIT_2026-05-08.md`

### GA1 - Known Limitations Refresh

Refresh limitations in tiers.

#### Hard Limits (Architecture)

- Local-first only by default; managed/cloud mode is optional and deferred.
- Single-machine JSONL runtime state is the default.
- Multi-tenant hosted posture is not GA.

#### Current Scope Limits (May Expand Later)

- DeepSeek N>=8 is smoke/sanity coverage, not full regression confirmation.
- Cost/quota guard counts provider calls, not exact dollar billing.
- Browser redaction closure covers specified streams only.
- Provider parity boundaries remain explicit.

#### Operator-Controlled Limits (Configurable)

- Live-call caps are controlled by `.cvf/config/cost-quota-policy.json`.
- Cooldown timing is configurable.
- Owner override may be enabled or disabled by local policy.

**Artifact:**
`docs/reviews/CVF_GA_KNOWN_LIMITATIONS_REFRESH_2026-05-08.md`

### GA2 - Decision Packet

Decision options:

| Decision | Meaning |
|---|---|
| `GA_LOCAL_FIRST_APPROVED` | local-first GA may publish; all roadmap evidence requirements pass without material known limits |
| `GA_LOCAL_FIRST_APPROVED_WITH_LIMITS` | local-first GA may publish with explicit known-limits register for partial coverage |
| `RC3_REQUIRED` | one or more release-facing blockers remain |
| `HOLD_FOR_MANAGED_MODE` | operator chooses hosted/managed as GA requirement |

**Artifact:**
`docs/reviews/CVF_GA_READINESS_DECISION_2026-05-08.md`

---

## Deferred Track M - Optional Managed State

Not part of this roadmap's implementation.

Future work may define:

- `RuntimeJobStore` interface;
- `FileBackedRuntimeJobStore` as default local implementation;
- `PostgresRuntimeJobStore` as optional managed adapter;
- Supabase as one possible Postgres deployment option;
- tenant/org boundary and RLS only for managed mode.

This must not block local-first GA unless the operator explicitly changes the
product requirement from local-first to hosted/managed.

## Stop Rules

Stop and ask for operator decision if:

- CI2 hosted run fails and no failure-mode artifact is filed;
- CI2 hosted run fails and the operator has not explicitly chosen PASS retry or
  known-limit deferral;
- cost/quota policy cannot block over-limit live jobs server-side;
- direct API over-budget bypass is not blocked;
- owner override or non-owner denial cannot be audited;
- `.cvf/config/cost-quota-policy.json` contains a raw provider key, auth token,
  or any value matching secrets-scan patterns;
- DS lane budget cap is lower than the selected evidence minimum, making the
  test impossible;
- redaction browser/HAR probe reveals the fake key;
- BR mock injection occurs after redaction;
- DS run consumes more live quota than planned;
- any artifact would imply Supabase/Postgres is required for local-first CVF;
- any GA packet would claim provider parity or hosted multi-tenant readiness
  without evidence.

## Verification Baseline For This Roadmap

Before implementation:

```bash
git fetch origin
git status --short --branch
# assert the branch line does not show "behind"
python scripts/run_cvf_static_ci_gate.py --json
```

For any governance behavior claim:

```bash
python scripts/run_cvf_release_gate_bundle.py --json
```

Mock mode is allowed only for BR fake-key browser redaction tests because those
tests assert redaction behavior, not live provider governance behavior.

## Claude Re-Review Questions

1. Does V2 close the critical evidence-definition gaps for CI2-H and BR?
2. Is CQ now strict enough for local-first GA without requiring dollar-pricing?
3. Are CQ override and direct API bypass checks sufficient?
4. Is DS smoke/sanity wording acceptable for N>=8, with N>=14 reserved for
   confirmation?
5. Is GA documentation currency audit scoped to the right public trust signals?
6. Is `GA_LOCAL_FIRST_APPROVED_WITH_LIMITS` the right middle decision state?
7. Does V2 preserve local-first CVF while keeping Supabase/Postgres deferred?

## Authorization State

This V2 is not implementation authorization.

Required next step:

- Claude re-review and operator authorization for GC-018 scoping.

Forbidden next step:

- implementing CQ/BR/DS/GA tracks directly from this draft without
  authorization.
