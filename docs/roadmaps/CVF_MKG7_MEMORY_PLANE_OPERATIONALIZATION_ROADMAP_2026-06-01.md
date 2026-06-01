# CVF MKG7 Memory Plane Operationalization Roadmap

Memory class: FULL_RECORD

Status: PROPOSED

docType: roadmap

Date: 2026-06-01

## Purpose

Close the Memory plane as a real, bounded, governed system. MKG7 is the final
MKG-series roadmap: it operationalizes the bounded Memory runtime kernel
delivered in MKG1-MKG6 so that Memory can participate in governed execution as
advisory evidence, with deterministic lifecycle and retrieval attribution, a
readiness surface over the already-fail-closed durable write path, and a documented
derived-graph boundary — without raw Memory release, prompt reinjection,
graph-execution authority, or live-provider overclaim.

MKG7 starts from the committed MKG1-MKG6 result (commit `2ebc0b92` +
`6f825820`): manifest-backed Memory corpus reconciliation, owner-surface
triage, a deterministic LPF Memory runtime workflow chain, an LPF Memory
runtime subpath export, and an authenticated summary-only
`POST /api/memory/readout` route.

## Authorization / Decision

Authority:

- operator direction on 2026-06-01 to make Memory a real system and to deliver
  the final closing roadmap for the Memory plane;
- `docs/reviews/CVF_MKG_MEMORY_SYSTEM_TRANCHE_COMPLETION_2026-06-01.md`;
- `docs/roadmaps/CVF_MKG6_MEMORY_RUNTIME_READOUT_ROUTE_ROADMAP_2026-06-01.md`;
- `docs/work_orders/CVF_WO_MKG6_MEMORY_RUNTIME_READOUT_ROUTE_2026-06-01.md`;
- `docs/reference/CVF_WORKER_AUTONOMY_DISPATCH_PROMPT_STANDARD_2026-06-01.md`;
- `docs/reference/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md`;
- `docs/reference/CVF_WORK_ORDER_CLOSURE_QUALITY_GATE_STANDARD_2026-05-28.md`.

This roadmap authorizes planning only. Each tranche requires its own GC-018 and
work order before implementation.

## Current State (Source-Verified)

MKG1-MKG6 are committed (`git log`: `2ebc0b92 feat(memory): deliver bounded
memory runtime readout`, `6f825820 chore(session): sync memory tranche
handoff`). The MKG tranche completion review records MKG1-MKG6 closure.

### Already delivered runtime surfaces

| Surface | File (verified) | Boundary |
| --- | --- | --- |
| Memory workflow chain | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-runtime-workflow-chain.ts` (218 lines) | local deterministic chain only |
| Memory runtime subpath export | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-runtime.ts` (26 lines) | narrow LPF re-export surface |
| Memory readout projection | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.ts` | summary-only HTTP projection |
| Memory readout route | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` (205 lines) | authenticated local route, returns `rawMemoryReleased:false` + `canReinject:false`, RAW_SENTINEL guard |
| Lifecycle policy (tier model) | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-lifecycle-policy.ts` (83 lines) | `evaluateLifecycleTransition`; tier-state machine working/episodic/semantic/procedural/expired/disputed/forgotten |
| Retrieval policy | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` (202 lines) | `evaluateRetrievalRequest`, `MemoryRetrievalResult` |
| Durable store | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` (456 lines) | `DurableMemoryStore` with **active `write()`** gated by provenance ≥ 0.7 and allowed lifecycle states |

### Verified facts that correct the prior draft

- `/api/execute/route.ts` is **858 lines** (hard limit 1000), not at threshold.
  Helper extraction before route growth remains the rule, but no emergency.
- A durable Memory **write path already exists AND already fails closed**
  (`DurableMemoryStore.write`, `durable-memory-store.ts:195`). The first branch
  (`durable-memory-store.ts:201`) denies the write unless
  `actorAuthorized === true` and `policyDecision === "allow"`, then further
  gates on runtime decision and `provenanceScore >= 0.7`
  (`MIN_PROVENANCE_SCORE`, line 98). The receipt is locked to `summaryOnly:true`,
  `canReinject:false`, `rawMemoryReleased:false`. So "persistence mutation
  disabled by default" was inaccurate in BOTH directions: the path is not
  disabled, but it is not an ungoverned exposure either. MKG7-T5 is therefore a
  **wiring/readiness** tranche — the gated store is not yet wired into a route
  or the runtime chain — not an emergency remediation of an open write hole.
- The readout/advisory surface enforces `canReinject:false`
  (`route.ts:203`). The internal tier policy returns `canReinject:true` for
  semantic/procedural tiers (`memory-lifecycle-policy.ts:44`). These are
  different layers. MKG7 scopes the `canReinject=false` invariant to the
  **readout and execution-advisory surfaces only**, and does not claim the
  internal tier flag is false.
- The LPF subpath export (`memory-runtime.ts`) does **not** currently re-export
  the lifecycle policy or durable store; only the chain, retrieval, gateway,
  event-hook, and actor-role types. T1/T2 may widen this export deliberately.

### Still missing (true gaps MKG7 closes)

- a formalized, source-verified Memory plane operational contract;
- deterministic readout-eligibility lifecycle decisions (distinct from the
  existing tier-state machine);
- bounded advisory Memory readout inside `/api/execute`;
- retrieval attribution (source, freshness, rank reason, exclusion reason)
  layered onto the existing retrieval result without raw content;
- a bounded readiness/wiring surface over the already-fail-closed durable write
  path, with regression tests that pin the existing deny branches;
- a documented derived-graph / semantic-region rebuildability boundary;
- a live-proof decision if Memory becomes part of a governance claim.

## Scope

In scope:

- define the operational Memory plane contract against current source;
- add deterministic readout-eligibility lifecycle decisions;
- wire a bounded advisory Memory readout into `/api/execute` if source and
  file-size guards allow;
- extend retrieval attribution on the existing retrieval result without raw
  content release;
- add a bounded readiness/wiring surface over the already-fail-closed durable
  write path, with regression tests pinning the existing deny branches;
- document the rebuildable derived-graph / semantic-region boundary and drift
  checks;
- run local deterministic route, TypeScript, and governance gates;
- prepare a live-proof tranche plan only if Memory behavior becomes a
  governance claim.

Out of scope:

- raw Memory content release;
- prompt injection or automatic reinjection into model prompts;
- autonomous (unauthorized) durable mutation;
- new graph persistence or graph-execution authority;
- provider routing changes;
- new role taxonomy;
- new receipt envelope fields unless source-verified and separately authorized;
- public-sync or public README claims;
- hosted readiness, production readiness, or cost optimization claims;
- editing frozen baseline layers or legacy source authority.

## Non-Goals

- do not claim Memory improves model quality without live/provider proof;
- do not claim Memory retrieval authority from derived graph views alone;
- do not convert advisory Memory output into execution-policy enforcement in
  this roadmap unless a later GC-018 explicitly authorizes it;
- do not add broad Memory tiers beyond the existing bounded kernel;
- do not claim the existing durable write path is disabled or ungoverned — it
  is present and already fails closed; T5 only adds readiness/wiring and
  regression coverage;
- do not use operator silence as approval for live proof, public-sync, or
  reinjection.

## Tranche Plan

| Tranche | Name | Goal | Primary outputs | Status |
| --- | --- | --- | --- | --- |
| MKG7-T1 | Operational Contract | Formalize the runtime contract from current source; name inputs, auth, surfaces, readout shape, forbidden fields, lifecycle states, advisory boundary | GC-018, work order, Memory Plane Operational Contract | PROPOSED |
| MKG7-T2 | Readout-Eligibility Lifecycle | Add deterministic readout-eligibility decisions distinct from the existing tier-state machine | new policy helper, focused tests | PROPOSED |
| MKG7-T3 | Execution Advisory Wire-In | Add bounded advisory Memory readout to `/api/execute` response, helper-first, guard-gated | helper, route tests | PROPOSED |
| MKG7-T4 | Retrieval Attribution | Extend the existing retrieval result with source/freshness/rank/exclusion attribution, no raw content | schema/helper delta, tests | PROPOSED |
| MKG7-T5 | Durable Write Readiness | Wire the already-fail-closed durable store into a bounded read-only/authorized surface; prove existing fail-closed behavior; no new mutation authority | adapter/wiring over existing store, fail-closed tests | PROPOSED |
| MKG7-T6 | Derived Graph Boundary | Document rebuildable graph/semantic-region boundary and drift checks | reference standard or review packet | PROPOSED |
| MKG7-T7 | Live Proof Decision | Decide whether a live/provider proof tranche is required; draft separately if yes | decision review, no live run by default | PROPOSED |

## Work Plan

| Step | Requirement | Output | Status |
| --- | --- | --- | --- |
| M7.0 | Open fresh GC-018 with source-verified Memory plane scope | MKG7 GC-018 baseline | PROPOSED |
| M7.1 | Dispatch T1 operational-contract work order against current source | source-verified contract and boundaries | PROPOSED |
| M7.2 | Implement deterministic readout-eligibility lifecycle decisions | policy helper and focused tests | PROPOSED |
| M7.3 | Decide and implement advisory route wire-in only if guards allow | route helper changes and tests | PROPOSED |
| M7.4 | Extend retrieval attribution without raw content | attribution helper/schema delta and tests | PROPOSED |
| M7.5 | Add readiness/wiring surface over already-fail-closed durable store | bounded read/authorized surface and deny-branch regression tests | PROPOSED |
| M7.6 | File derived-graph boundary packet | source-authority / rebuildability packet | PROPOSED |
| M7.7 | File live-proof decision and next roadmap if needed | decision packet | PROPOSED |

## Workstream Details

### MKG7-T1 Operational Contract

Formalize, from current source, a contract that names:

- Memory plane inputs (the `/api/memory/readout` request body fields:
  `operationId`, `sessionId`, `projectId`, `actorId`, `actorRole`, `scope`,
  `riskLevel`, `query`, `tokenBudget`, `candidates`, optional `policyDecision`,
  `containsSensitiveData`, `maxResults`);
- actor/session/project authorization signals (service-token verification via
  `verifyServiceTokenRequest`, session via `verifySessionCookie`);
- allowed route surfaces (`POST /api/memory/readout`, and the proposed advisory
  attachment point in `/api/execute`);
- returned readout shape (`memoryRuntimeReadout` projection +
  `rawMemoryReleased:false` + `canReinject:false`);
- forbidden fields (raw candidate `content`, anything triggering RAW_SENTINEL);
- lifecycle states, distinguishing the existing tier-state machine from the new
  readout-eligibility states added in T2;
- advisory-only execution boundary;
- required evidence receipts or existing receipt attachment points.

The contract must cite current source files with line/symbol evidence, not
memory summaries. It must explicitly state that the `canReinject=false`
invariant applies to the readout/advisory surface, and that the internal tier
policy's `canReinject` flag is a separate, non-prompt-assembly signal.

### MKG7-T2 Readout-Eligibility Lifecycle

Add a deterministic readout-eligibility policy, separate from the existing
`evaluateLifecycleTransition` tier-state machine, covering:

- `READOUT_ALLOWED`;
- `READOUT_DENIED`;
- `STALE_NEEDS_REFRESH`;
- `REVOKED`;
- `NO_AUTHORITY_SOURCE`;
- `OUT_OF_SCOPE_FOR_ACTOR`.

The policy must preserve, on the readout/advisory surface:

- `rawMemoryReleased=false`;
- `canReinject=false`;
- no prompt injection;
- no durable mutation as a side effect of readout.

T2 must source-verify `memory-lifecycle-policy.ts` and state how the new
eligibility states relate to the existing tier states without redefining them.

### MKG7-T3 Execution Advisory Wire-In

If source verification and file-size planning pass, wire a compact Memory
advisory object into the governed `/api/execute` response.

Required constraints:

- `/api/execute/route.ts` is currently 858 lines; any growth that approaches
  the 1000-line hard threshold must be preceded by helper extraction;
- route behavior must remain advisory unless a later roadmap authorizes
  enforcement;
- no live/provider claim unless the release gate with live proof is run;
- the advisory object reuses the existing readout projection contract; it must
  not introduce raw content or a reinjection path.

### MKG7-T4 Retrieval Attribution

Extend the existing `memory-retrieval-policy.ts` result
(`MemoryRetrievalResult`, `evaluateRetrievalRequest`) so it can answer:

- what authority source produced the summary;
- when it was generated or last refreshed;
- why it was selected;
- why other candidates were excluded;
- whether the result is stale, partial, or complete;
- which boundaries prevent raw content release.

T4 is a delta on the existing retrieval surface, not a new retrieval engine.
The attribution surface must be deterministic and testable without provider
calls.

### MKG7-T5 Durable Write Readiness

The durable store already exposes a `write()` (`durable-memory-store.ts:195`)
that **already fails closed**: it denies unless `actorAuthorized === true` and
`policyDecision === "allow"` (line 201), then gates on runtime decision and
`provenanceScore >= 0.7` (line 98), and locks the receipt to `summaryOnly:true`,
`canReinject:false`, `rawMemoryReleased:false`. T5 does NOT add new mutation
authority and does NOT change these semantics. T5 is readiness/wiring only:

- a bounded read-only or authorized-read surface over the existing store;
- regression tests that pin the existing fail-closed branches
  (`actorAuthorized` false → denied; `policyDecision !== "allow"` → denied;
  provenance below threshold → denied);
- tests proving the receipt invariants remain `summaryOnly:true`,
  `canReinject:false`, `rawMemoryReleased:false`.

T5 must source-verify the existing store interface and must not silently change
its current write semantics. Enabling a new write surface that mutates durable
state from a route requires a separate GC-018.

### MKG7-T6 Derived Graph Boundary

Document how graph, semantic-region, Palace, summary, cache, snapshot, and
retrieval views remain rebuildable derived views.

Required result:

- source authority stays primary;
- derived-view drift is detectable;
- graph lookup cannot overrule source authority;
- public or runtime claims require separate proof.

### MKG7-T7 Live Proof Decision

File a decision packet answering whether Memory now affects governed route
behavior enough to require live proof.

If yes, open a fresh GC-018 for live proof using:

```powershell
python scripts/run_cvf_release_gate_bundle.py --json
```

If no, record why the current tranche remains local deterministic evidence
only.

## Acceptance Criteria

| Criterion | Required result |
| --- | --- |
| Contract clarity | Memory plane contract names source-verified fields, owners, forbidden behaviors, advisory boundary, and the layer scope of `canReinject=false` |
| Readout-eligibility lifecycle | deterministic readout-eligibility decisions, distinct from the tier-state machine, covered by focused tests |
| Safety invariants | `rawMemoryReleased=false` and `canReinject=false` preserved across readout and execution-advisory surfaces |
| Execution integration | if implemented, Memory readout is advisory-only and tested through route helpers; route stays under the file-size threshold |
| Attribution | selected and excluded Memory candidates have non-raw source/freshness/rank/exclusion evidence layered on the existing retrieval result |
| Durable write readiness | regression tests pin the existing deny branches (unauthorized → denied, `policyDecision != allow` → denied, provenance below floor → denied); no new mutation authority added |
| Derived graph boundary | source authority and rebuildable derived views are explicitly separated |
| Maintainability | near-threshold source files are split or reduced before growth |
| Governance | work-order dispatch, autorun, structural, public-export, finding-learning, and file-size gates pass |

## Source Verification Block (Roadmap-Level)

| Claim | Verified path or symbol | Evidence |
| --- | --- | --- |
| MKG1-MKG6 committed | git log | `2ebc0b92`, `6f825820` |
| Readout route exists, summary-only | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` | `rawMemoryReleased:false` / `canReinject:false` at lines 202-203; RAW_SENTINEL at line 7/194 |
| Readout projection helper | `buildMemoryRuntimeReadout` | imported at route.ts:2; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.ts` |
| Tier lifecycle policy exists | `evaluateLifecycleTransition` | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-lifecycle-policy.ts:49` |
| Tier `canReinject` true for semantic/procedural | `transition` | `memory-lifecycle-policy.ts:44` |
| Retrieval policy exists | `evaluateRetrievalRequest`, `MemoryRetrievalResult` | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts:88,40` |
| Durable store write interface declared | `DurableMemoryStore.write` | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts:90` |
| Durable write fails closed without authorization | `write` deny branch | `durable-memory-store.ts:195,201` (`!input.actorAuthorized \|\| input.policyDecision !== "allow"` → `decision:"denied"`) |
| Durable write provenance floor | `MIN_PROVENANCE_SCORE` | `durable-memory-store.ts:98` (`0.7`) |
| Durable receipt invariants locked | `DurableMemoryReceipt` | `durable-memory-store.ts` (`summaryOnly:true`, `canReinject:false`, `rawMemoryReleased:false`) |
| Durable store factories | `createInProcessDurableMemoryStore`, `createFileBackedDurableMemoryStore` | `durable-memory-store.ts:100,106` |
| Subpath export omits lifecycle/durable | `memory-runtime.ts` | re-exports chain/retrieval/gateway/event-hook/actor-role only |
| execute route line count | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | 858 lines |

Each tranche work order must produce its own, finer Source Verification Block
before implementation, citing source files, symbols, and line/section evidence.
`ACCEPT` rows must not treat MKG completion prose as source authority when
runtime source exists.

## Required Work Orders

MKG7 must not be dispatched as one broad worker assignment. Create separate
work orders:

- `CVF_WO_MKG7_T1_MEMORY_PLANE_OPERATIONAL_CONTRACT_2026-06-01.md`;
- `CVF_WO_MKG7_T2_MEMORY_READOUT_ELIGIBILITY_LIFECYCLE_2026-06-01.md`;
- `CVF_WO_MKG7_T3_MEMORY_EXECUTION_ADVISORY_WIREIN_2026-06-01.md`;
- `CVF_WO_MKG7_T4_MEMORY_RETRIEVAL_ATTRIBUTION_2026-06-01.md`;
- `CVF_WO_MKG7_T5_MEMORY_DURABLE_WRITE_GOVERNANCE_2026-06-01.md`;
- `CVF_WO_MKG7_T6_MEMORY_DERIVED_GRAPH_BOUNDARY_2026-06-01.md`;
- `CVF_WO_MKG7_T7_MEMORY_LIVE_PROOF_DECISION_2026-06-01.md`.

Each work order must include:

- Source Verification Block;
- Roadmap-to-Work-Order Trace Matrix;
- Worker Autonomy / No-Question Rule;
- Work-Order Fulfillment Manifest;
- Allowed Scope and Forbidden Scope;
- Closure Diff Gate;
- Public Export Disposition;
- Claim / Final / Verification Boundary.

## Worker Autonomy / No-Question Rule

Assigned workers must repair allowed-scope guard failures and rerun gates
without asking the operator whether to continue.

Escalate to the operator only for:

- scope expansion;
- claim-boundary change;
- live/provider proof;
- secret or quota use;
- public-sync or push;
- destructive or irreversible actions;
- touching forbidden paths;
- releasing a `HOLD_*` prerequisite;
- changing risk level or enforcement authority;
- any change to the existing durable write semantics, or any new route that
  mutates durable state.

## Source Verification Requirements

Before implementation, each work order must source-verify any named:

- route path;
- TypeScript function, type, or field;
- receipt field;
- actor role;
- risk or lifecycle enum;
- policy result;
- package export;
- file path;
- test command.

`ACCEPT` rows must cite source files, symbols, and line or section evidence.
Do not treat MKG completion prose as source authority when runtime source
exists.

## Verification / Evidence

Required phase gates, with `<baseHead>` captured before each tranche (the
roadmap-creation baseHead is `6f825820`):

```powershell
python governance/compat/check_work_order_dispatch_quality.py --base <baseHead> --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base <baseHead> --head HEAD
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <baseHead> --head HEAD
python governance/compat/check_governed_file_size.py --enforce
python governance/compat/check_public_export_disposition.py --base <baseHead> --head HEAD --enforce
python governance/compat/check_finding_to_governance_learning.py --base <baseHead> --head HEAD --enforce
```

Focused tests are finalized per work order, but must include LPF tests for
Memory policy/chain/store changes and cvf-web tests for route/readout changes.

Live/provider proof is not required unless MKG7-T7 authorizes a live tranche.
If authorized, use the release-quality live governance bundle and do not print
raw secrets.

## Risk Register

| Risk | Control |
| --- | --- |
| Memory overclaimed as production behavior | Keep claim boundary local/advisory until live proof exists |
| Raw content leakage | RAW_SENTINEL guard plus forbidden-field assertions in tests |
| Reinjection by accident | Preserve `canReinject=false` on readout/advisory surfaces; no prompt-assembly changes without separate GC-018 |
| Worker rebuilds existing modules | Delta-only tranche framing plus per-work-order Source Verification Block |
| Existing durable write path misdescribed as new, disabled, or ungoverned | T5 pins the already-fail-closed `write()` with regression tests; a new mutating route requires separate GC-018 |
| Route file exceeds maintainability threshold | Extract helpers before route growth; current count is 858/1000 |
| Derived graph treated as source authority | Enforce source-authority versus rebuildable-view boundary |
| Worker asks routine guard questions | Worker Autonomy / No-Question Rule plus dispatch-quality gate |
| Public/private boundary drift | Public Export Disposition remains `DEFERRED_PRIVATE_ONLY` unless public-sync evidence exists |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: MKG7 is a private provenance roadmap. No public-sync remote, public
repository commit, hosted proof, public artifact path, or public README claim
is included.

## Claim Boundary

This roadmap authorizes planning for Memory plane operationalization only. It
does not by itself authorize live/provider proof, public-sync, prompt
injection, Memory reinjection, raw Memory release, graph mutation or
graph-execution authority, changes to the existing durable write semantics,
new durable-mutating routes, production readiness, hosted readiness,
public readiness, or autonomous mutation.
