# CVF External Review — GAP Analysis and Proposed Solutions

Memory class: FULL_RECORD

Status: FILED_FOR_CODEX_REBUTTAL_REPAIRED_FOR_GOVERNED_INTAKE

Date: 2026-06-05

Author: Claude (Sonnet 4.6) — operator-triggered analysis session

Repair note: Codex repaired this packet on 2026-06-06 after finding that the
file had been local-only and hidden by `.git/info/exclude`. The repaired packet
is intended to be tracked before use as governed evidence.

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

| GAP | Diagnosis verified? | Roadmap exists? | Proposed track | Min governance needed |
|---|---|---|---|---|
| 1 — Doc bloat | Partial (944L not 2000L; duplication likely but needs overlap map) | No | Pointer-ification + single source | Separate doc work order; GC-018 if authority changes |
| 2 — Jargon | Yes (two tiers — internal valid, public barrier) | F2 partial (UI only) | Glossary candidate + F2 (GC-018) | Work order for Track A; GC-018 for Track B |
| 3 — Version drift | Yes (3 concrete discrepancies found) | No | Immediate string fix + release checklist | First Claude work order recommended |
| 4 — Meta-governance | Partial (tension real; accumulation drift valid gap) | A2 audit-only | Governance rule audit batch | GC-018 for removals |
| 5 — Audit persistence | Yes (liveEmissionWired literal; file-backed default durability risk) | No | liveEmissionWired (E2) + durable backend selection | GC-018 required both |

## Priority Order (by effort and risk)

1. GAP 3 — Version drift fix (30 min, first Claude work order candidate)
2. GAP 2 Track A — Glossary in GET_STARTED.md (2 hr, same small doc work order if source-verified)
3. GAP 1 — Doc pointer-ification (1 day, separate packet after overlap map)
4. GAP 4 — Governance rule audit batch (2–3 days, GC-018 for removal phase)
5. GAP 5A — liveEmissionWired type + wire one metric (1 day, GC-018 E2 scope)
6. GAP 5B — Durable audit backend selection/implementation (3–5 days, GC-018 separate durable persistence tranche)

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
