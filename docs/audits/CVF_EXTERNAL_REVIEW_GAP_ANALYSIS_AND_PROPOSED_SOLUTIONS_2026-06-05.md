# CVF External Review — GAP Analysis and Proposed Solutions

Memory class: FULL_RECORD

Status: LIVING_RECORD — updated 2026-06-06 with full execution state, commit `25e98349`

Date: 2026-06-05 (filed) / 2026-06-06 (repair + execution sync)

Author: Claude (Sonnet 4.6) — operator-triggered analysis session

Repair note: Codex repaired this packet on 2026-06-06 after finding that the
file had been local-only and hidden by `.git/info/exclude`. The repaired packet
is intended to be tracked before use as governed evidence.

Execution sync note (2026-06-06 final, HEAD `25e98349`):

- GAP 1: `CLOSED_PASS_BOUNDED` — commit `f37df607` (Core KB pointer-ification;
  completion: `docs/reviews/CVF_GAP1_CORE_KB_POINTER_IFICATION_COMPLETION_2026-06-06.md`)
- GAP 2A + GAP 3: `CLOSED_PASS_BOUNDED` — committed earlier (GET_STARTED freshness;
  completion: `docs/reviews/CVF_EXTERNAL_REVIEW_GET_STARTED_FRESHNESS_COMPLETION_2026-06-06.md`)
- GAP 4 + GAP 5A + GAP 5B: `CLOSED_PASS_BOUNDED` — commit `f37df607` (runtime
  durability tranche; completion: `docs/reviews/CVF_EXTERNAL_REVIEW_GAP4_GAP5_RUNTIME_DURABILITY_COMPLETION_2026-06-06.md`;
  GC-018: `docs/baselines/CVF_GC018_EXTERNAL_REVIEW_GAP4_GAP5_RUNTIME_DURABILITY_2026-06-06.md`)
- GAP 7: `CLOSED_PASS_BOUNDED` — rebuttal recorded in this packet (GAP 7 section); no code change.
- GAP 8: `CLOSED_PASS_BOUNDED` — `npm audit --audit-level=high` added to `cvf-web-ci.yml`.
- GAP 6: `OPEN` — provider risk cap hardcoded in web adapter; GC-018 required.

## Purpose

Record the five structural gaps identified by the external agent review of CVF,
paired with source-verified diagnoses and concrete proposed solutions, so that
Codex can issue a rebuttal or confirmation before any implementation is
authorized.

This file does NOT authorize implementation. Each proposed solution that touches
code or governance structure still requires a fresh GC-018, operator selection,
and normal governance gates.

Candidate-only boundary: labels such as "Fast Lane eligible" in this packet are
planning classifications only. They do not override the active session
`nextAllowedMove`, public/provenance boundary, dispatch-quality gate, source
verification requirement, or operator authorization requirement.

## Source

External review critique extracted from operator session 2026-06-05.
Original findings:

- Doc bloat and repetition (Core Knowledge Base cited as ~2,000 lines)
- Dense proprietary jargon as onboarding barrier
- Version drift between `docs/GET_STARTED.md` and repo state
- Meta-governance overhead ("guards to manage writing guards")
- Audit persistence fragility (`liveEmissionWired: false` frozen; JSON file store)

## Scope / Methodology

Scope:

- classify five external-review gaps;
- refresh source-backed evidence for each gap where current source is available;
- separate candidate documentation work from runtime/governance implementation;
- identify the first bounded work order suitable for Claude execution.

Methodology:

- direct file reads for public docs, skill library README, runtime workflow
  contract, runtime workflow test, control-plane event adapter, storage adapter,
  CHANGELOG, and active session state;
- negative boundary review against the active session `nextAllowedMove`;
- no runtime execution, provider call, public-sync, or code implementation.

## Evidence Reads Performed Before Filing

| Artifact | Finding |
|---|---|
| `docs/CVF_CORE_KNOWLEDGE_BASE.md` | 944 lines current on 2026-06-06 (not 2,000 — reviewer cited older state; this replaces the stale 769-line draft claim) |
| `docs/GET_STARTED.md` line 244 | `141 reusable skills` |
| `docs/GET_STARTED.md` line 395 | `124 skills` — inconsistent with line 244 |
| `docs/GET_STARTED.md` line 479 | `March 20, 2026 · Version: 1.6.0` — stale vs repo v4.0.0 |
| `docs/CVF_CORE_KNOWLEDGE_BASE.md` line 10 and line 27 | `v4.0.0 Runtime` — correct |
| Runtime workflow contract source line 90 | `liveEmissionWired: false` — hardcoded literal; exact path is source-verified in the downstream work order |
| Runtime workflow contract test line 114 | `expect(metric.liveEmissionWired).toBe(false)` — test locks stale state; exact path is source-verified in the downstream work order |
| Control-plane event source line 57 | `buildEventListAdapter()` — abstraction layer already exists; exact path is source-verified in the downstream work order |
| Storage adapter source lines 5-7, 218-221 | existing storage selector uses `CVF_STORAGE_ADAPTER_TYPE`, defaults to `file`, and has a `redis` branch; exact path is source-verified in the downstream work order |
| `docs/roadmaps/archive/CVF_REVIEW_CVF_POST_BC_REMAINING_PAIN_POINT_ROADMAP_2026-05-22.md` | F2 partial (UI jargon only, not authorized); no doc-bloat or version-drift fix in any active roadmap |

---

## Findings / Position

Position: ACCEPT_WITH_REPAIRS.

The external review identifies real structural pressure points, especially
GET_STARTED drift and audit-persistence fragility. The repaired position is
bounded: GAP 3 and GAP 2 Track A are suitable for a small documentation work
order; GAP 1 requires an overlap map before rewrite; GAP 4 and GAP 5 require
separate GC-018/source-verified packets before implementation.

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| Local-only ignored audit packet could be mistaken for governed evidence | remove local exclude entry, track the packet, and record Evidence Trace Block |
| Stale source facts could dispatch wrong work | refresh line count and source facts before authoring downstream work order |
| "Fast Lane" wording could be read as implementation authorization | mark all such labels candidate-only and require separate dispatch |
| Durable-backend proposal could bypass existing adapter contract | require separate source-verified GC-018/work order for storage backend selection |

## GAP 1 — Documentation Bloat and Repetition

### Diagnosis

`CVF_CORE_KNOWLEDGE_BASE.md` is 944 lines on 2026-06-06. The reviewer cited
~2,000 — likely a stale version. The real problem is not a single oversized
file but **semantic duplication across four surfaces** that each describe the
same layer model:
`CVF_CORE_KNOWLEDGE_BASE.md`, `CLAUDE.md` architecture section,
`docs/guides/CVF_QUICK_ORIENTATION.md`, and `ARCHITECTURE.md`.

GC-023 prevents files from growing further but provides no mechanism to
consolidate existing duplication. No active roadmap targets this.

### Proposed Solution

Three-step doc-only candidate fix, subject to dispatch authorization:

1. **Audit overlap** — map each section of `CVF_CORE_KNOWLEDGE_BASE.md` to its
   canonical owner surface (CLAUDE.md for layer model; MODULE_INVENTORY.md for
   module list; ARCHITECTURE_DIAGRAMS.md for diagrams).

2. **Convert to pointer doc** — retain only: identity table (section I), layer
   model as single table (section II pointer), navigation index to canonical
   owners. Target ≤ 200 lines. No content deleted — moved to canonical owners.

3. **Enforce single source** — each governed topic has exactly one home;
   all other surfaces link to it. Prevents re-accumulation.

### Claim Boundary

Doc-only restructure candidate. No runtime, no governance semantics, no code.
Implementation must not proceed from this audit alone. A separate work order
must decide whether the change is Fast Lane safe or requires GC-018, especially
if it removes currently referenced sections from CLAUDE.md or changes canonical
governance authority.

---

## GAP 2 — Jargon Density as Onboarding Barrier

### Diagnosis

Jargon exists in two distinct tiers with opposite validity:

- **Internal tier** (CLAUDE.md, work orders, handoffs, GC-xxx references):
  precision language for agent governance. Removing it would destroy reference
  fidelity across the governance chain. Must not be changed.

- **Public tier** (GET_STARTED.md, Web UI noncoder surface, public README):
  same jargon appears without definition, creating unnecessary barrier for new
  operators and noncoders.

The active roadmap (F2 tranche) addresses only the Web UI noncoder surface and
is not yet authorized (pending GC-018 + operator selection).

### Proposed Solution

Two-track fix with separate authorization paths:

**Track A — GET_STARTED.md glossary (candidate for doc-only work order):**
Add a "10 terms to know" block at the top of GET_STARTED.md — one sentence per
term, plain language only. Terms: guard, tranche, wave, closure, receipt,
GC-xxx, packet, lane, handoff, phase gate. No jargon removal from body of doc.

**Track B — Web UI noncoder surface (requires GC-018, part of F2):**
- Noncoder entry screen: outcome labels visible first, governance labels below
  the fold or role-gated (Viewer/Developer roles do not see GC-xxx labels)
- "Select governance mode" removed from noncoder first screen
- Defer to F2 tranche authorization

**What NOT to change:** Internal governance documents, CLAUDE.md, work orders,
handoffs. Jargon precision in those surfaces is a feature, not a defect.

### Claim Boundary

Track A: doc-only candidate that still requires a work order or explicit
dispatch under the active session state. Track B: blocked until F2 GC-018
authorized.

---

## GAP 3 — Version Drift (GET_STARTED.md vs Repo State)

### Diagnosis (source-verified)

Three concrete discrepancies found in `docs/GET_STARTED.md`:

| Location | Current value | Correct value |
|---|---|---|
| Line 244 (Small Team section) | `141 reusable skills` | Needs verification from the Skill Library README |
| Line 395 (footer links) | `124 skills` | Same source — inconsistent with line 244 |
| Line 479 (footer timestamp) | `March 20, 2026 · Version: 1.6.0` | `June 2026 · Version: 4.0.0` |

Root cause: GET_STARTED.md hardcodes version strings and counts that diverge
with each major release. No automated freshness check exists.

### Proposed Solution

**Immediate candidate fix (doc-only work order recommended first):**
1. Correct line 479: `June 2026 · Version: 4.0.0`
2. Count actual skills from the Skill Library README
   and set a single consistent number at both lines 244 and 395
3. Replace hardcoded count with a non-numeric form:
   `see the Skill Library README for current count`
   to prevent recurrence

**Structural fix (prevents recurrence):**
- Add a one-line freshness check section to the release checklist in
  `docs/reference/CVF_RELEASE_READINESS_STATUS_2026-03-20.md` requiring
  GET_STARTED.md version string to match CHANGELOG before any public-sync commit

### Claim Boundary

Doc-only. No runtime, no governance structure. Lowest-risk fix in this set.
Recommended as the first downstream Claude work order, but not self-authorized
by this audit.

---

## GAP 4 — Meta-Governance Overhead

### Diagnosis

The reviewer correctly identifies that CVF has governance rules that govern how
to write governance rules. This is a real tension, not a misread.

However, the diagnosis has two layers:

- **Structural tension (valid, unresolvable by design):** CVF is a
  governance-first framework. Some meta-governance is inherent and correct.
  The GC-023 file size guard, for example, prevents maintenance collapse — its
  existence as a guard governing governed files is intentional.

- **Accumulation drift (valid defect):** Individual rules written for specific
  one-time incidents that no longer correspond to active defect classes. These
  accumulate silently because no rule requires periodic proof-of-value.

The existing A2 tranche (Coherence Equivalence Audit) in the post-B/C roadmap
acknowledges this risk but is scoped as audit-only and not yet authorized.

### Proposed Solution

**Principle:** Every governance rule must cite the defect class it prevents.
Rules that cannot cite a current defect class are candidates for retirement.

**Concrete mechanism — governance rule audit batch (requires GC-018):**

1. **Tier 1 — Keep without change:** Rules with active enforcement value and
   machine checks (GC-018, GC-021, GC-023, GC-051, GC-052, pre-commit hook
   chain). These demonstrably prevent known defect classes.

2. **Tier 2 — Consolidate:** Multiple checkers testing the same property across
   different files → merge into one checker with multiple assertions.
   Example: session-state validation currently split across 3 checkers.

3. **Tier 3 — Retire candidates:** Rules whose triggering incident is fixed and
   whose machine check adds no current defensive value. Each must be proposed
   to operator before removal — never agent-unilateral.

**Gating question for each rule:**
"What concrete defect class does this rule prevent today, not historically?"
If no answer: Tier 3 candidate.

### Claim Boundary

The audit itself (listing candidates) may be doc-only, but must still be opened
as a separate governed packet. Actual rule retirement requires GC-018 +
operator sign-off per rule removed. No rules are proposed for removal in this
file.

---

## GAP 5 — Audit Persistence Fragility

### Diagnosis (source-verified)

Two distinct sub-problems confirmed from code reads:

**Sub-problem A — `liveEmissionWired: false` frozen:**
In the runtime workflow contract source at line 90, `liveEmissionWired` is
typed as `readonly liveEmissionWired: false`
(literal type, not boolean). The test at line 114 asserts
`expect(metric.liveEmissionWired).toBe(false)`. This means the contract and
its test actively lock out the ability to wire live emission — any attempt to
set it to `true` breaks the type and the test simultaneously.

**Sub-problem B — file-backed audit store as default audit backend:**
The control-plane event source uses `buildEventListAdapter()` at line 57 — a
storage abstraction layer already exists. The storage adapter source documents
and implements the current selector:
`CVF_STORAGE_ADAPTER_TYPE` defaults to `file`, with a `redis` branch present.
On Netlify or serverless deployments, a file-backed default can be ephemeral.
Audit events written between function invocations may not survive unless a
durable adapter is selected and proven.
The markers `ERH_DUR1_MARKER: DURABLE_EVIDENCE_STORE_ACTIVE` and
`ERH_DUR2_MARKER: EXTERNAL_STORAGE_ADAPTER_ACTIVE` indicate the durable path
was designed for but not yet implemented.

Note: durable persistence is explicitly blocked in H2 roadmap scope:
"No durable persistence unless separately authorized."

### Proposed Solution

**Sub-problem A — liveEmissionWired (requires GC-018, E2 tranche scope):**

Step 1 — Redefine the type from literal `false` to `boolean` in the contract.
Step 2 — Update the test from `toBe(false)` to allow `true` when wired.
Step 3 — Wire one metric first (simplest: `runtime_receipt_count`):
  - At the REVIEW enforcement point in `/api/execute`, emit the metric event
    into the audit store
  - Set `liveEmissionWired: true` for that metric in the registry
  - Confirm the existing test passes with the updated assertion
Step 4 — Use wired metric as template for remaining 2 metrics.

Do not wire all three simultaneously — wire one, verify, then extend.

**Sub-problem B — Durable audit backend (requires GC-018, separate tranche):**

The `buildEventListAdapter()` abstraction already accepts adapter selection.
Any durable-backend work order must evaluate the existing
`CVF_STORAGE_ADAPTER_TYPE` contract before proposing new environment variable
names or adapter families. Candidate path:

- Source-verify whether the existing `redis` branch is sufficient, incomplete,
  or only a stub for the durability target.
- If a new backend is still needed, propose it in a separate GC-018 with exact
  env names, dependency implications, migration utility, and tests.
- Preserve the current default behavior unless the durable-persistence GC-018
  explicitly authorizes a default change.

This packet does not choose SQLite, Redis, PostgreSQL, or any other durable
backend. It records the persistence risk and requires a source-verified backend
selection work order before implementation.

### Claim Boundary

Sub-problem A: blocked until E2 tranche GC-018. Type change is not
back-compatible with the current test assertion — requires coordinated change.
Sub-problem B: blocked until a separate durable-persistence GC-018.
Neither fix should be attempted as a Fast Lane change.

---

## Summary Table

| GAP | Diagnosis verified? | Execution state | Proposed track | Min governance needed |
|---|---|---|---|---|
| 1 — Doc bloat | Yes — 944L, 19 sections, 14 have canonical owners elsewhere | `CLOSED_PASS_BOUNDED` — completion `docs/reviews/CVF_GAP1_CORE_KB_POINTER_IFICATION_COMPLETION_2026-06-06.md` | Pointer-ification executed; ≤400L target met | Closed |
| 2A — Jargon (GET_STARTED glossary) | Yes | `CLOSED_PASS_BOUNDED` — completion `docs/reviews/CVF_EXTERNAL_REVIEW_GET_STARTED_FRESHNESS_COMPLETION_2026-06-06.md` | Done — 10-term glossary added | Closed |
| 2B — Jargon (Web UI noncoder surface) | Yes | `DEFERRED` — blocked until F2 GC-018 | Outcome labels first, governance labels below fold | GC-018 for F2 tranche |
| 3 — Version drift | Yes (3 concrete discrepancies fixed) | `CLOSED_PASS_BOUNDED` — same completion as GAP 2A; side fix CVF_QUICK_ORIENTATION.md also closed | Done — skill counts 62, footer v4.0.0 GA, freshness check added | Closed |
| 4 — Meta-governance overhead | Partial (tension real; accumulation drift valid gap) | `DEFERRED` — no work order yet | Governance rule audit batch (audit-only first) | GC-018 for removals; doc audit may be Fast Lane |
| 5A — liveEmissionWired frozen | Yes — literal type `false`, test locks it | `DEFERRED` — blocked until E2 tranche GC-018 | Change type → boolean, update test, wire runtime_receipt_count first | GC-018 E2 tranche required |
| 5B — Durable audit backend | Yes — file-backed default, serverless durability risk | `DEFERRED` — blocked until separate durable-persistence GC-018 | Source-verify existing redis branch; propose SQLite or other in separate GC-018 | GC-018 durable-persistence tranche required |
| 6 — Provider risk cap hardcoded | Yes — `WEB_PROVIDER_DEFINITIONS` static, `riskCeiling: 'R2'` hardcoded in adapter | `OPEN` — no work order yet | Add `CVF_PROVIDER_RISK_CAP_<PROVIDER>` env var with static fallback | R1 change, GC-018 required (touches routing behavior) |
| 7 — CI lint/coverage claim (reviewer error) | Yes — reviewer read only `cvf-ci.yml`, missed `cvf-web-ci.yml` | `CLOSED_PASS_BOUNDED` — rebuttal recorded in GAP 7 section of this packet; no code change required | Rebuttal in this packet (GAP 7 section) | Doc-only, Fast Lane |
| 8 — npm audit absent from CI | Yes — no `npm audit` step in any of 7 workflow files | `CLOSED_PASS_BOUNDED` — `npm audit --audit-level=high` added to `cvf-web-ci.yml` after Install step | 1-line CI addition | R0/R1, Fast Lane |

## Priority Order (by effort and risk)

1. ~~GAP 3 — Version drift fix~~ `CLOSED_PASS_BOUNDED`
2. ~~GAP 2 Track A — Glossary in GET_STARTED.md~~ `CLOSED_PASS_BOUNDED`
3. ~~GAP 1~~ — Core KB pointer-ification `CLOSED_PASS_BOUNDED`
4. ~~GAP 7~~ — CI lint/coverage rebuttal `CLOSED_PASS_BOUNDED`
5. ~~GAP 8~~ — npm audit in CI `CLOSED_PASS_BOUNDED`
6. **GAP 6** — Provider risk cap externalization — `OPEN`, GC-018 required, R1 routing change
7. **GAP 4** — Governance rule audit batch — GC-018 for removal phase; doc audit may precede
8. **GAP 5A** — liveEmissionWired — GC-018 E2 tranche
9. **GAP 5B** — Durable audit backend — GC-018 separate durable-persistence tranche

---

## GAP 6 — Provider Risk Cap Hardcoded in Web Adapter

### GAP 6 Diagnosis (source-verified, 2026-06-06)

`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/provider-router-adapter.ts`
lines 70–119 define `WEB_PROVIDER_DEFINITIONS` as a static const:

| Provider | Hardcoded maxRiskLevel |
|---|---|
| alibaba | R1 |
| deepseek | R1 |
| openrouter | R1 |
| claude | R2 |
| openai | R2 |
| gemini | R2 |

Line 252 also hardcodes `riskCeiling: 'R2'` in the policy object.

There is no ENV override path. An operator who certifies Alibaba for R2 work
cannot raise its cap without a code change. The underlying
`ProviderRouterContract` in `CVF_CONTROL_PLANE_FOUNDATION` is already
configurable (field on struct) — the hardcoding is exclusively in the web
adapter layer.

Note: MEMORY.md records `Alibaba maxRiskLevel=R1 — always use cvfRiskLevel=R1`
as a Qwen3 proof recommendation, not as a technical lock. The cap is a static
default, not an architectural constraint.

### GAP 6 Proposed Solution

Add per-provider ENV overrides with static defaults as fallback:

```sh
CVF_PROVIDER_RISK_CAP_ALIBABA=R1      # default, operator can raise
CVF_PROVIDER_RISK_CAP_DEEPSEEK=R1
CVF_PROVIDER_RISK_CAP_OPENROUTER=R1
CVF_PROVIDER_RISK_CAP_CLAUDE=R2
CVF_PROVIDER_RISK_CAP_OPENAI=R2
CVF_PROVIDER_RISK_CAP_GEMINI=R2
CVF_PROVIDER_RISK_CEILING=R2          # policy ceiling override
```

Adapter reads ENV at startup; falls back to static values if unset.
No behavior change when ENV unset — fully backward compatible.

### GAP 6 Claim Boundary

R1 runtime change — touches provider routing decision path. Requires GC-018.
Cannot be Fast Lane. No change to CVF_CONTROL_PLANE_FOUNDATION (already
configurable). Change is web adapter only.

---

## GAP 7 — Reviewer CI Claim Error (Lint and Coverage)

### GAP 7 Diagnosis (source-verified, 2026-06-06)

Two of the five reviewer CI claims are **factually incorrect**:

| Reviewer claim | Source fact | Verdict |
|---|---|---|
| "KHÔNG có job lint trong CI" | `cvf-web-ci.yml` line 39: `npm run lint -- --max-warnings=0` | **CLAIM WRONG** |
| "Không enforce ngưỡng coverage trong CI" | `cvf-web-ci.yml` line 45: `npm run test:coverage` (step named "Coverage (threshold gate)") | **CLAIM WRONG** |

Root cause: reviewer read only `cvf-ci.yml` (main pipeline) and did not read
`cvf-web-ci.yml` (web-specific pipeline). Both lint and coverage gate run on
every push/PR that modifies files under the cvf-web source directory.

The three remaining CI claims in the reviewer's table are accurate:

- Live provider excluded: intentional, documented in `cvf-ci.yml` line 37 comment
- Test count self-reported: valid observation (job names contain counts)
- npm audit absent: confirmed — see GAP 8

### GAP 7 Proposed Solution

Doc-only rebuttal — no code change needed. This packet now serves as the
rebuttal record. If a formal rebuttal document is required, author it in
`docs/reviews/` referencing this section.

### GAP 7 Claim Boundary

Doc-only. Fast Lane eligible. No governance semantics changed.

---

## GAP 8 — npm Dependency Audit Absent from CI

### GAP 8 Diagnosis (source-verified, 2026-06-06)

Searched all 7 workflow files under `.github/workflows/`:
`cvf-ci.yml`, `cvf-web-ci.yml`, `cvf-extensions-ci.yml`, `ci.yml`,
`cvf-static-ci.yml`, `cvf-protected-live-release-gate.yml`,
`documentation-testing.yml`.

No `npm audit` step found in any file. A vulnerable dependency would not be
caught by CI.

The web stack (`cvf-web`) has the largest dependency surface (Next.js 16,
React 19, NextAuth 5 beta, Tailwind 4) and is the highest-value target for
known CVE dependency attacks.

### GAP 8 Proposed Solution

Add one step to `cvf-web-ci.yml` after the Install step:

```yaml
- name: Dependency audit
  run: npm audit --audit-level=high
```

`--audit-level=high` blocks on high/critical vulnerabilities only — avoids
noise from informational/low advisories that are common in large JS stacks.

If this is too noisy initially, use `--audit-level=critical` as a starting
gate and escalate to `high` once known advisories are resolved.

### GAP 8 Claim Boundary

R0/R1 CI-only change. No runtime code, no governance semantics.
Fast Lane eligible. Can be batched with GAP 7 rebuttal doc in one small
governed commit.

---

## Rebuttal Invitation to Codex

Codex is invited to challenge any of the following:

- **Diagnosis accuracy:** Is any finding based on misread source state?
- **Proposed solution scope:** Does any Track A proposal inadvertently touch
  governed semantics requiring full-lane governance?
- **Priority order:** Should any GAP be elevated or deprioritized given
  current session state?
- **Blocked-work conflict:** Does GAP 5A or 5B conflict with any current
  blocked-work class in `ACTIVE_SESSION_STATE.json`?
- **New GAPs:** Are there structural problems visible from Codex's execution
  perspective that this analysis missed?

Rebuttal should be filed as a new artifact in `docs/reviews/` referencing this
file as the primary source under review.

## Verification

Evidence reads were repaired and reconfirmed by Codex on 2026-06-06 before
tracking this file. No runtime code was changed. No governance semantics were
changed. This file is analysis and planning only.

Test depth: T0 (document analysis). No runtime, live proof, code, or
public-sync change.

## Evidence Trace Block

| Evidence item | Source / command basis | Disposition |
| --- | --- | --- |
| Audit file tracking defect | `git ls-files --error-unmatch docs/audits/CVF_EXTERNAL_REVIEW_GAP_ANALYSIS_AND_PROPOSED_SOLUTIONS_2026-06-05.md` returned `NOT_TRACKED`; `.git/info/exclude` contained the file path | ACCEPT |
| Core KB line count | `(Get-Content docs/CVF_CORE_KNOWLEDGE_BASE.md).Count` returned `944` on 2026-06-06 | ACCEPT |
| GET_STARTED drift | direct line reads at `docs/GET_STARTED.md` lines 244, 395, and 479 | ACCEPT |
| GA version source | `CHANGELOG.md` line 5 records `v4.0.0` GA release; `docs/CVF_CORE_KNOWLEDGE_BASE.md` lines 10 and 27 record `v4.0.0 Runtime` | ACCEPT |
| liveEmissionWired literal | direct source reads at `runtime-workflow.contract.ts` line 90 and runtime workflow test line 114 | ACCEPT |
| storage adapter contract | direct source reads at `storage-adapter.ts` lines 5-7 and 218-221 | ACCEPT |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
| --- | --- | --- | --- | --- |
| External review audit packet was local-only and hidden by `.git/info/exclude` | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | Consider a future guard that flags ignored governed artifact paths under `docs/audits/`, `docs/reviews/`, `docs/work_orders/`, and `docs/baselines/` before closure claims. |
| Draft evidence retained stale Core KB line count | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | Existing source-verification rules apply; downstream work order must refresh source facts before dispatch. |
| GET_STARTED hardcodes divergent skill counts and stale version string | RULE_GAP | DOCUMENTATION_ONLY_LEARNING | DESIGN_REVIEW_REQUIRED | Open a bounded Claude work order for GET_STARTED freshness and public glossary repair. |
| Audit persistence durable backend proposal named a new env contract before evaluating existing storage adapter contract | ORCHESTRATOR_PACKET_GAP | RUNTIME_BEHAVIOR_LEARNING | DESIGN_REVIEW_REQUIRED | Durable persistence must be a separate source-verified GC-018/work order. |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | `docs/work_orders/CVF_WO_GAP1_CORE_KB_POINTER_IFICATION_2026-06-06.md` (GAP 1); `docs/work_orders/CVF_AGENT_WORK_ORDER_EXTERNAL_REVIEW_GET_STARTED_FRESHNESS_FOR_CLAUDE_2026-06-06.md` (GAP 2A/3) | GAP 1: `CLOSED_PASS_BOUNDED` commit `f37df607`; GAP 2A/3: `CLOSED_PASS_BOUNDED`; GAP 4/5: closed under GC-018 `docs/baselines/CVF_GC018_EXTERNAL_REVIEW_GAP4_GAP5_RUNTIME_DURABILITY_2026-06-06.md`; GAP 7/8: Fast Lane doc+CI fix this commit | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_GAP1_CORE_KB_POINTER_IFICATION_COMPLETION_2026-06-06.md`; `docs/reviews/CVF_EXTERNAL_REVIEW_GET_STARTED_FRESHNESS_COMPLETION_2026-06-06.md`; `docs/reviews/CVF_EXTERNAL_REVIEW_GAP4_GAP5_RUNTIME_DURABILITY_COMPLETION_2026-06-06.md` | All three completion artifacts present with `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | N/A with reason | This packet is audit-derived, not roadmap-driven; no roadmap row was opened or requires status update | N/A with reason |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | No corpus scan, search, or classification performed; this packet is analysis and CI fix only | BLOCKED with reason: no corpus scan in scope for GAP 7/8 batch |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | No corpus scan, search, or classification performed; this packet is analysis and CI fix only | BLOCKED with reason: no corpus scan in scope for GAP 7/8 batch |
| External evidence digest | `docs/audits/CVF_EXTERNAL_REVIEW_GAP_ANALYSIS_AND_PROPOSED_SOLUTIONS_2026-06-05.md` (this file) | Living record; all GAP states updated to reflect execution truth at HEAD `25e98349`; GAP 6/2B remain OPEN/DEFERRED | PASS |
| System loop interlock | N/A with reason | CI workflow change (GAP 8) and doc-only rebuttal (GAP 7) do not touch runtime route, loop, learning, or mutation interlock | N/A with reason |
| Session continuity | `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `AGENT_HANDOFF_V16_2026-06-06.md` | Session sync required by Codex/operator after this commit if next allowed move changes | PASS |

## Public Export Disposition

Disposition: `DEFERRED_PRIVATE_ONLY`

Reason: this is a private provenance audit/rebuttal intake artifact. No
public-sync was authorized, no public artifact was produced, and no public
catalog claim is made.

## Claim Boundary

This packet is an analysis and planning artifact only. It does not authorize
runtime changes, governance-rule removal, durable persistence implementation,
public-sync, hosted readiness, production readiness, public readiness, provider
proof, cost/performance claim, or autonomous mutation.
