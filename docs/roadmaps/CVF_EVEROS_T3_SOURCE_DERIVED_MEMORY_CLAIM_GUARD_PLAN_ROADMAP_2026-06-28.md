# CVF EVEROS-T3 Source-Derived Memory Claim Guard Plan Roadmap

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: roadmap

Date: 2026-06-28

Owner: Codex

Batch ID: EVEROS-T3

rawMemoryReleased=false

## Authorization / Decision

The operator approved continuing the EverOS absorption chain after EVEROS-T2
selected `EVEROS-T3 Source-Derived Memory Claim Guard Plan` as the next
highest-value bounded candidate.

Decision:
`CLOSED_PASS_BOUNDED_SOURCE_DERIVED_CLAIM_GUARD_PLAN_ONLY`

This roadmap converts the EVEROS-T1 contract and EVEROS-T2 owner-surface
reconciliation into a concrete future guard plan. It does not implement,
modify, or authorize a checker, runtime memory surface, generated aggregate,
derived index, route, provider/live proof, public-sync batch, adapter, package
activation, certification, OME runtime, or MPI-T6 runtime.

## Purpose

Close the planning gap between the CVF memory foundation doctrine and the
existing static memory-claim guards.

EVEROS-T1 already states that governed source surfaces remain authoritative and
that generated aggregates, graph views, semantic/vector views, metadata ledgers,
context packs, and cached summaries are derived and rebuildable. EVEROS-T2 then
mapped that doctrine to existing CVF owner surfaces and selected a small future
claim-language guard as the next useful candidate.

T3 records the exact guard shape before any implementation. The value is to
prevent future governed Markdown from treating derived views as source
authority, treating stale/degraded/conflicted views as safe to use, or treating
vector/graph/cache language as a live memory capability without source
verification.

## Scope / Target / Owner Boundary

Allowed T3 scope:

- define the future static guard's target claim classes;
- map those claim classes to existing T1/T2 source authority and current local
  guards;
- identify exemption boundaries for negative guardrail language and
  source-verified implementation packets;
- select a follow-on T4 implementation candidate, if the operator chooses to
  continue.

Forbidden T3 scope:

- no edits to `governance/compat/*.py`;
- no runtime implementation, database, vector store, graph store, semantic
  index, embedding/rerank path, watcher, daemon, route, or generated aggregate;
- no live/provider proof, public-sync, external adapter, package activation,
  certification, OME runtime, or MPI-T6 runtime;
- no claim that CVF currently has production vector memory, graph memory,
  durable memory access, external CLI/MCP memory access, or automatic prompt
  reinjection.

## Non-Goals

This roadmap does not:

- implement or edit a static guard;
- create tests, fixtures, or CI binding for a future guard;
- create a memory runtime, vector store, graph store, semantic index, database,
  watcher, daemon, route, generated aggregate, provider proof, public-sync
  batch, adapter, package activation, certification, or MPI-T6 runtime lane;
- claim derived views are source authority;
- claim stale, degraded, or conflicted derived views may be used without
  rebuild, denial, or source fallback;
- authorize prompt reinjection or raw memory release.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| EVEROS-T1 defines the source-derived replay contract | `docs/reference/memory_foundation/CVF_MEMORY_FOUNDATION_SOURCE_DERIVED_REPLAY_CONTRACT.md` | Source Authority Rule; Source And Derived Surface Classes; Derived View Rules | `cvf.memoryFoundation.sourceDerivedReplay.everosT1.v1` | memory foundation contract | VALUE_SET | ACCEPT |
| EVEROS-T2 selected the source-derived claim guard plan as the next candidate | `docs/reference/memory_foundation/CVF_MEMORY_FOUNDATION_OWNER_SURFACE_RECONCILIATION_MATRIX.md` | T2 Decision | `cvf.memoryFoundation.ownerSurfaceReconciliation.everosT2.v1` | owner-surface reconciliation matrix | VALUE_SET | ACCEPT |
| Memory foundation front door owns the stable reference family route | `docs/reference/memory_foundation/README.md` | Active References; Design Control Gate | `docs/reference/memory_foundation/` | memory foundation front door | EXISTS | ACCEPT |
| Current raw memory release invariant guard exists for changed governed Markdown | `governance/compat/check_raw_memory_release_invariant.py` | constants and diagnosis function | `RAW_RELEASE_FALSE_PATTERN`; `diagnose_raw_memory_release_invariant` | raw memory release invariant gate | EXISTS | ACCEPT |
| Current memory access overclaim guard exists and uses claim rules | `governance/compat/check_memory_access_claim.py` | `CLAIM_RULES`; `diagnose_memory_access_claims` | `CLAIM_RULES` | memory access claim gate | EXISTS | ACCEPT |
| T3 checker mutation is outside this roadmap | `docs/roadmaps/CVF_EVEROS_T3_SOURCE_DERIVED_MEMORY_CLAIM_GUARD_PLAN_ROADMAP_2026-06-28.md` | Authorization / Decision; Scope / Target / Owner Boundary | `CLOSED_PASS_BOUNDED_SOURCE_DERIVED_CLAIM_GUARD_PLAN_ONLY` | T3 roadmap | LITERAL_INVARIANT | ACCEPT |

## Existing Guard Coverage

| Existing guard | Current coverage | T3 gap decision |
|---|---|---|
| `governance/compat/check_raw_memory_release_invariant.py` | requires `rawMemoryReleased=false` on memory-facing governed Markdown under its applicable prefixes | covered; T3 preserves this invariant |
| `governance/compat/check_memory_access_claim.py` | flags live external-agent read access, scan-registry route overclaims, production/live graph/vector/durable memory access, raw release/reinjection, and index replacing canonical authority | covered for broad memory-access overclaims |
| T1 source-derived replay contract | documents source authority, derived surface classes, stale/degraded/conflicted states, retrieval receipts, rebuild receipts, and reinjection denial | source doctrine, not a machine guard |
| T2 owner-surface matrix | maps doctrine to current owner surfaces and selects a T3 candidate | plan input, not implementation |
| T3 plan | defines the narrower guard target for derived-view authority and stale-use claim language | implementation deferred to T4 |

## Planned Guard Claim Classes

Future guard candidate id:
`cvf.memoryFoundation.sourceDerivedClaimGuard.everosT4.candidate`

| Claim class | Description | Desired handling |
|---|---|---|
| `derived_view_as_source_authority` | changed governed Markdown says a generated aggregate, graph view, semantic/vector view, metadata ledger, context pack, or cached summary is truth, source authority, or proof by itself | flag unless the wording is negative guardrail language or the packet cites a source-verified implementation contract that narrows the claim |
| `stale_or_conflicted_view_safe_to_use` | changed governed Markdown says a stale, degraded, or conflicted derived view may still answer, route, authorize, certify, or dispatch without rebuild, denial, or source fallback | flag unless the wording records a denial/rebuild rule |
| `derived_view_runtime_capability` | changed governed Markdown turns vector, graph, cache, semantic, or metadata-index language into a live runtime memory capability without source verification | flag unless a current runtime/source path is source-verified in the same artifact |
| `retrieval_result_allows_reinjection` | changed governed Markdown treats retrieval presence, similarity, graph relation, or cache hit as authorization for prompt reinjection or raw memory release | flag because current T1 and local guards keep raw release and reinjection false |

## Planned Guard Exemptions

| Exemption | Reason | Required evidence |
|---|---|---|
| Negative guardrail language | docs must be able to state what is forbidden | sentence or nearby paragraph uses terms such as `must not`, `does not authorize`, `overclaim`, `flag`, `reject`, or `fail condition` |
| Source-verified implementation packet | future runtime/source work may add a narrower true claim | Source Verification Block cites the owning implementation file, route, schema, or generated-source layout and names the verified symbol |
| Documentation-only future candidate | a roadmap may describe a candidate without claiming it already exists | claim boundary states implementation is deferred and no checker/source mutation is included |
| Existing raw-release false invariant | current raw-release and reinjection claims stay forbidden | `rawMemoryReleased=false` remains present and no positive raw release or reinjection claim is made |

## Work Plan

| Step | Output | Status |
|---|---|---|
| T3.1 | Read startup, active handoff, guard orientation, literal-format gotchas, T1 contract, T2 matrix, and current memory claim checkers | PASS |
| T3.2 | Map current guard coverage against T1/T2 doctrine | PASS |
| T3.3 | Define future claim classes and exemptions | PASS |
| T3.4 | Keep implementation out of T3 and select T4 as the possible implementation lane | PASS |
| T3.5 | Commit the T3 roadmap, then sync the active handoff separately | PASS |

## Design Control Gate

| Design control | Handling | Verdict |
|---|---|---|
| Source authority preserved | T3 routes all truth claims back to T1/T2 and current source verification | PASS |
| Guard overlap respected | T3 does not duplicate raw-release and broad memory-access guard coverage | PASS |
| Implementation restraint | T3 records a plan only; no checker file is changed | PASS |
| External input boundary | EverOS remains absorbed doctrine, not CVF source authority | PASS |
| Public/provenance boundary | no public export or public-sync is claimed | PASS |
| Next-move clarity | T4 is a possible implementation candidate only after operator approval | PASS |

## Acceptance Criteria

| ID | Criterion | Disposition |
|---|---|---|
| AC1 | T3 reads and cites T1/T2 source-owned memory foundation surfaces | PASS |
| AC2 | T3 defines concrete claim classes for derived-view authority and stale-use overclaims | PASS |
| AC3 | T3 distinguishes existing guard coverage from the future candidate gap | PASS |
| AC4 | T3 records exemption boundaries so future implementation does not flag negative guardrail prose | PASS |
| AC5 | T3 does not edit or authorize checker/runtime/provider/public/adapter/package surfaces | PASS |
| AC6 | T3 selects a single possible next lane: EVEROS-T4 implementation candidate | PASS |

## Verification / Evidence

| Evidence item | Command or artifact | Required result |
|---|---|---|
| Startup and current state | `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `AGENT_HANDOFF_V25_2026-06-28.md` | active handoff and T2 next candidate confirmed |
| T1 source authority | `docs/reference/memory_foundation/CVF_MEMORY_FOUNDATION_SOURCE_DERIVED_REPLAY_CONTRACT.md` | source-derived replay doctrine confirmed |
| T2 selection | `docs/reference/memory_foundation/CVF_MEMORY_FOUNDATION_OWNER_SURFACE_RECONCILIATION_MATRIX.md` | T3 candidate confirmed |
| Current guard overlap | `governance/compat/check_memory_access_claim.py`; `governance/compat/check_raw_memory_release_invariant.py` | existing coverage confirmed |
| T3 material gate | focused governance and autorun gates over base `6772bb6b` and `HEAD` | PASS before material commit |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External repo or copied folder |
| Chain map route | External repo or copied folder -> Root/folder lifecycle classification plus absorption map when retained -> CVF-owned reference contract -> ABSORB, ADAPT, DEFER, REJECT, or BLOCK |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | `docs/roadmaps/CVF_EVEROS_T3_SOURCE_DERIVED_MEMORY_CLAIM_GUARD_PLAN_ROADMAP_2026-06-28.md` |
| Disposition | ADAPT the EverOS-derived T1/T2 doctrine into a CVF-owned future guard plan |
| Claim boundary | external materials remain inputs; this roadmap cites CVF-owned T1/T2 surfaces and current local guards |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | this roadmap plus T1/T2 memory foundation references | may use for future source-verification and guard implementation planning | Source Verification Block and Planned Guard Claim Classes | N/A with reason: roadmap only | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future public-safe or adapter readout | no external interface, CLI, MCP, or public behavior is created | deferred by this roadmap | separate GC-018/source-verified work order required | `DEFERRED_WITH_REASON` |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Escalation state | Next control action |
|---|---|---|---|---|
| Derived-view authority and stale-use language is not fully covered by current static guards | RULE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | consider EVEROS-T4 Source-Derived Memory Claim Guard Implementation |
| Runtime/provider/cost learning is not applicable to this documentation-only roadmap | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | T3 made no live behavior, provider output, cost, token, or latency finding |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Completion or reviewer artifact | this roadmap | Status: CLOSED_PASS_BOUNDED | PASS |
| Work order status | no worker-dispatch work order in T3 | T3 is a single-agent roadmap plan closure | N/A with reason |
| Roadmap state | `docs/roadmaps/CVF_EVEROS_T3_SOURCE_DERIVED_MEMORY_CLAIM_GUARD_PLAN_ROADMAP_2026-06-28.md` | Status: CLOSED_PASS_BOUNDED | PASS |
| Registry JSON | no GC-051 registry JSON mutation authorized | changed set excludes GC-051 registry JSON | BLOCKED with reason: T3 is memory-foundation roadmap planning only |
| Registry Markdown | no GC-051 registry Markdown mutation authorized | changed set excludes GC-051 registry Markdown | BLOCKED with reason: T3 is memory-foundation roadmap planning only |
| External evidence digest | EverOS external evidence already converted by T0/T1/T2; T3 cites CVF-owned surfaces only | External Knowledge Intake Routing | N/A with reason |
| System loop interlock | N/A with reason: no loop/interlock surface changed | Claim Boundary | N/A with reason |
| Session continuity | active handoff marker planned after material commit | separate handoff-sync commit required | PASS |

## Acceptance Receipt Assertion Matrix

| Query ID | Receipt artifact | JSON path | Required value | Observed value | Status |
|---|---|---|---|---|---|
| EVEROS-T3-Q1 | this roadmap | N/A with reason: Markdown roadmap | T3 plan closed | T3 plan closed | PASS |
| EVEROS-T3-Q2 | Planned Guard Claim Classes | N/A with reason: Markdown table | derived-view authority and stale-use overclaims defined | defined | PASS |
| EVEROS-T3-Q3 | Claim Boundary | N/A with reason: Markdown section | no implementation authorized | no implementation authorized | PASS |
| EVEROS-T3-Q4 | Public Export Disposition | N/A with reason: Markdown section | DEFERRED_PRIVATE_ONLY | DEFERRED_PRIVATE_ONLY | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is a private provenance memory-foundation planning roadmap.
Public wording requires a separate public-sync decision.

## Recommended Next Tranche

Recommended next lane:
`EVEROS-T4 Source-Derived Memory Claim Guard Implementation`

T4 should be opened only if the operator wants to convert this plan into a
small checker or dispatch-quality extension. T4 must include a fresh GC-018,
source verification, tests, core-guard self-protection authorization for any
changed `governance/compat/*.py` path, and a bounded false-positive test set.

## Claim Boundary

This roadmap closes only the source-derived memory claim guard plan. It does
not implement or authorize runtime memory, generated aggregates, derived
indexes, databases, graph stores, vector stores, embeddings, rerank, watcher,
daemon, route behavior, provider/live proof, public-sync, CLI/MCP adapter,
package activation, certification, checker mutation, OME runtime, or MPI-T6
runtime.
