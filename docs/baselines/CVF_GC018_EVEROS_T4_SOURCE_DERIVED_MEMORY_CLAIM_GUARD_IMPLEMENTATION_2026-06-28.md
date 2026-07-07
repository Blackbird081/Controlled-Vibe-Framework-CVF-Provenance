# GC-018 EVEROS-T4 Source-Derived Memory Claim Guard Implementation

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: gc018_baseline

Date: 2026-06-28

Batch ID: EVEROS-T4

rawMemoryReleased=false

## Purpose

Authorize and close a bounded static-guard implementation that converts the
EVEROS-T3 source-derived memory claim guard plan into a narrow extension of the
existing memory access claim checker.

The implementation extends `governance/compat/check_memory_access_claim.py`
and its focused tests. It does not create runtime memory, generated aggregates,
derived indexes, databases, routes, provider/live proof, public-sync, adapters,
packages, certification, OME runtime, or MPI-T6 runtime.

## Decision / Baseline / Proposed Tranche

Decision: `CLOSED_PASS_BOUNDED`

Baseline: EVEROS-T3 selected the source-derived memory claim guard
implementation lane after EVEROS-T1/T2 established source authority and owner
surface doctrine.

Implemented tranche: extend the existing memory access claim checker with
source-derived claim classes from EVEROS-T3.

## Authority Chain

| Authority | Evidence | Disposition |
|---|---|---|
| Operator approval | operator said `tiep tuc` after EVEROS-T3 closure | ACCEPT |
| EVEROS-T3 roadmap | `docs/roadmaps/CVF_EVEROS_T3_SOURCE_DERIVED_MEMORY_CLAIM_GUARD_PLAN_ROADMAP_2026-06-28.md` | ACCEPT |
| Existing checker | `governance/compat/check_memory_access_claim.py` | ACCEPT |
| Existing focused tests | `governance/compat/test_check_memory_access_claim.py` | ACCEPT |
| Guard orientation | `docs/reference/guard_orientation/README.md` | ACCEPT |
| Literal-format gotchas | `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | ACCEPT |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| EVEROS-T3 selected T4 implementation | `docs/roadmaps/CVF_EVEROS_T3_SOURCE_DERIVED_MEMORY_CLAIM_GUARD_PLAN_ROADMAP_2026-06-28.md` | Recommended Next Tranche | `EVEROS-T4 Source-Derived Memory Claim Guard Implementation` | EVEROS-T3 roadmap | VALUE_SET | ACCEPT |
| Memory access claim checker owns claim rules | `governance/compat/check_memory_access_claim.py` | claim rule definitions | `CLAIM_RULES` | memory access claim checker | EXISTS | ACCEPT |
| Memory access claim checker owns applicability prefixes | `governance/compat/check_memory_access_claim.py` | applicable prefixes | `APPLICABLE_PREFIXES` | memory access claim checker | EXISTS | ACCEPT |
| Memory access checker diagnostics entrypoint exists | `governance/compat/check_memory_access_claim.py` | diagnosis function | `diagnose_memory_access_claims` | memory access claim checker | EXISTS | ACCEPT |
| Focused unit test module exists | `governance/compat/test_check_memory_access_claim.py` | unittest classes | `TestMemoryAccessClaimTruePositives`; `TestMemoryAccessClaimTrueNegatives` | memory access claim checker tests | EXISTS | ACCEPT |

## Planned Artifact Manifest

| Artifact | Role | Status |
|---|---|---|
| `governance/compat/check_memory_access_claim.py` | static checker implementation | UPDATED |
| `governance/compat/test_check_memory_access_claim.py` | focused tests | UPDATED |
| `docs/baselines/CVF_GC018_EVEROS_T4_SOURCE_DERIVED_MEMORY_CLAIM_GUARD_IMPLEMENTATION_2026-06-28.md` | GC-018 closure baseline | CREATED |
| `docs/reviews/CVF_EVEROS_T4_SOURCE_DERIVED_MEMORY_CLAIM_GUARD_IMPLEMENTATION_COMPLETION_2026-06-28.md` | completion review and protected-path authorization | CREATED |

## Execution Plan

| Step | Action | Evidence |
|---|---|---|
| 1 | Read startup, guard orientation, literal gotchas, T3 roadmap, checker, and tests | startup acknowledgment and source reads |
| 2 | Extend existing checker instead of creating a parallel checker | changed checker path |
| 3 | Add focused true-positive and true-negative tests | changed test path |
| 4 | Add protected-path authorization and closure review | completion review |
| 5 | Run focused tests and governance gates | Gate Evidence |
| 6 | Commit material change, then sync active handoff separately | commit log and handoff marker |

## Roadmap-To-Guard Trace Matrix

| EVEROS-T3 planned class | T4 implementation route | Status |
|---|---|---|
| `derived_view_as_source_authority` | `CLAIM_RULES` rule with generated/runtime source citation allowance | PASS |
| `stale_or_conflicted_view_safe_to_use` | `CLAIM_RULES` hard-fail rule | PASS |
| `derived_view_runtime_capability` | `CLAIM_RULES` rule with generated/runtime source citation allowance | PASS |
| `retrieval_result_allows_reinjection` | `CLAIM_RULES` hard-fail rule | PASS |
| roadmap applicability | `APPLICABLE_PREFIXES` includes `docs/roadmaps/` | PASS |
| negative guardrail exemption | `GUARDRAIL_CONTEXT_MARKERS` includes guard-target language | PASS |

## Evidence / Verification

| Evidence item | Result |
|---|---|
| Focused unit tests | PASS: `python -m unittest governance.compat.test_check_memory_access_claim` |
| Static checker stays read-only | PASS: focused read-only implementation test |
| Runtime/provider/public boundary | PASS: no runtime/source route/provider/public surface changed |
| Protected-path authorization | PASS: completion review lists protected checker/test paths |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`guard-checker-maintenance`, role=`dispatch-author`, lifecyclePhase=`dispatch`

Query:

```text
python governance/compat/run_adif_defect_resolver.py --task-class guard-checker-maintenance --role dispatch-author --lifecycle-phase dispatch
```

Returned defects: NONE_RETURNED

## Acceptance Criteria

| Criterion | Required result | Status |
|---|---|---|
| Existing checker is extended, not duplicated | `check_memory_access_claim.py` updated | PASS |
| T3 claim classes have tests | focused tests cover four new classes | PASS |
| Guardrail prose is not self-flagged | negative guardrail test passes | PASS |
| Roadmaps are in scope | roadmap path applicability test passes | PASS |
| Runtime/provider/public/adapter scope remains closed | Claim Boundary excludes all such work | PASS |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External repo or copied folder |
| Chain map route | External repo or copied folder -> Root/folder lifecycle classification plus absorption map when retained -> CVF-owned reference contract -> ABSORB, ADAPT, DEFER, REJECT, or BLOCK |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | `docs/baselines/CVF_GC018_EVEROS_T4_SOURCE_DERIVED_MEMORY_CLAIM_GUARD_IMPLEMENTATION_2026-06-28.md` |
| Disposition | ADAPT EVEROS-T3 source-derived doctrine into an existing CVF static checker |
| Claim boundary | external materials remain inputs; T4 modifies only CVF-owned checker/test surfaces |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | `governance/compat/check_memory_access_claim.py` | may use as local static guard output only | focused tests and autorun gates | N/A with reason: no runtime adapter | `STATIC_GUARD_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future public-safe or adapter readout | no external interface, CLI, MCP, or public behavior is created | T4 claim boundary | separate GC-018/source-verified work order required | `DEFERRED_WITH_REASON` |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Escalation state | Next control action |
|---|---|---|---|---|
| EVEROS-T3 machine-check candidate was implementable inside an existing checker | RULE_GAP | GOVERNANCE_CONTROL_PLANE | RESOLVED_BY_STATIC_GUARD | keep using focused checker tests for future memory claim guard changes |
| Runtime/provider/cost learning is not applicable to this static-guard tranche | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | T4 made no live behavior, provider output, cost, token, or latency finding |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Completion or reviewer artifact | `docs/reviews/CVF_EVEROS_T4_SOURCE_DERIVED_MEMORY_CLAIM_GUARD_IMPLEMENTATION_COMPLETION_2026-06-28.md` | completion review exists in changed set | PASS |
| Work order status | no worker-dispatch work order in T4 | T4 is a single-agent bounded implementation closure | N/A with reason |
| Roadmap state | `docs/roadmaps/CVF_EVEROS_T3_SOURCE_DERIVED_MEMORY_CLAIM_GUARD_PLAN_ROADMAP_2026-06-28.md` | T3 Status: CLOSED_PASS_BOUNDED | PASS |
| Registry JSON | no GC-051 registry JSON mutation authorized | changed set excludes GC-051 registry JSON | BLOCKED with reason: T4 is static checker/test hardening only |
| Registry Markdown | no GC-051 registry Markdown mutation authorized | changed set excludes GC-051 registry Markdown | BLOCKED with reason: T4 is static checker/test hardening only |
| External evidence digest | EverOS external evidence already converted by T0-T3; T4 cites CVF-owned surfaces only | External Knowledge Intake Routing | N/A with reason |
| System loop interlock | N/A with reason: no loop/interlock surface changed | Claim Boundary | N/A with reason |
| Session continuity | active handoff marker planned after material commit | separate handoff-sync commit required | PASS |

## Acceptance Receipt Assertion Matrix

| Query ID | Receipt artifact | JSON path | Required value | Observed value | Status |
|---|---|---|---|---|---|
| EVEROS-T4-Q1 | focused unittest output | N/A with reason: terminal command | 20 tests pass | 20 tests pass | PASS |
| EVEROS-T4-Q2 | `CLAIM_RULES` | N/A with reason: Python source | T3 claim classes represented | represented | PASS |
| EVEROS-T4-Q3 | `APPLICABLE_PREFIXES` | N/A with reason: Python source | roadmaps in scope | roadmaps in scope | PASS |
| EVEROS-T4-Q4 | Public Export Disposition | N/A with reason: Markdown section | DEFERRED_PRIVATE_ONLY | DEFERRED_PRIVATE_ONLY | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance static checker hardening. Public wording requires a
separate public-sync decision.

## Claim Boundary

This baseline closes only bounded static checker/test hardening. It does not
implement or authorize runtime memory, generated aggregates, derived indexes,
databases, graph stores, vector stores, embeddings, rerank, watcher, daemon,
route behavior, provider/live proof, public-sync, CLI/MCP adapter, package
activation, certification, OME runtime, or MPI-T6 runtime.
