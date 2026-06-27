# CVF Guard Binding Catalog-Aware Checker Hardening Roadmap

Memory class: active-roadmap
Status: CLOSED_PASS_BOUNDED
Owner: Codex reviewer/closer multi-role
Date: 2026-06-26

## Purpose

Refactor guard-binding validation so checkers can verify runner wiring through command catalog modules instead of requiring literal checker-path marker strings inside large runner files.

## Scope

In scope:

- Add a shared guard-binding catalog resolver.
- Update binding-sensitive checkers to inspect effective runner text plus catalog module text.
- Remove temporary marker constants from the two orchestration runners.
- Preserve existing hook and autorun behavior.

Out of scope:

- Package instance creation.
- Certification decision.
- Generated-index mutation.
- Resolver mutation.
- Web runtime change.
- CLI/MCP adapter change.
- Provider/live proof.
- Public-sync or push.

## Authorization

Operator authorized immediate checker upgrade and front-door/handoff maintainability work before the next tranche. This roadmap covers only the material checker/catalog-binding part; session compaction is intentionally split into a later session-maintenance commit.

## Non-Goals

No checker semantics are weakened. The only admissible behavior change is that a guard path may satisfy binding evidence when it is present in a catalog module loaded by the runner.

## Design Control Gate

Design control decision: APPROVED_FOR_NARROW_MATERIAL_BATCH.

The existing orchestration catalog refactor moved command definitions out of runner files. The follow-on checker hardening keeps the machine guard model aligned with that source layout instead of preserving non-runtime marker constants.

## Work Plan

| Tranche | Work | Status |
|---|---|---|
| GBCA-T0 | Add catalog-aware binding helper | CLOSED_PASS |
| GBCA-T1 | Convert direct runner binding checks | CLOSED_PASS |
| GBCA-T2 | Convert required-marker checks that target runners | CLOSED_PASS |
| GBCA-T3 | Remove marker constants from runner files | CLOSED_PASS |
| GBCA-T4 | Run targeted gates and closure proof | CLOSED_PASS |

## Acceptance Criteria

| Criterion | Disposition |
|---|---|
| Binding checkers can find guard commands in catalog modules | PASS |
| Runner marker constants are removed | PASS |
| Orchestration runner size stays below exception pressure | PASS |
| Targeted guard-binding gates pass | PASS |
| No runtime, Web, provider, package, resolver, generated-index, public-sync, or push mutation | PASS |

## Verification

| Command | Result |
|---|---|
| `python -m py_compile ...` | PASS |
| `python governance/compat/check_agent_handoff_boundary.py --base f73546c5 --head HEAD --enforce` | PASS |
| `python governance/compat/check_agent_workspace_design.py --base f73546c5 --head HEAD --enforce` | PASS |
| `python governance/compat/check_agent_workspace_runtime_boundary.py --base f73546c5 --head HEAD --enforce` | PASS |
| `python governance/compat/check_agent_workspace_state.py --base f73546c5 --head HEAD --enforce` | PASS |
| `python governance/compat/check_markdown_structural_completeness.py --base f73546c5 --head HEAD --enforce` | PASS after packet-shape repairs |
| `python governance/compat/check_work_order_dispatch_quality.py --base f73546c5 --head HEAD --enforce` | PASS after packet-shape repairs |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| runtimeMutation | N/A with reason: no runtime file changed |
| providerRegistrySurface | N/A with reason: `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` and `PROVIDER_CAPABILITY_REGISTRY` are outside this material scope |
| webMutation | N/A with reason: no Web file changed |
| liveProviderProof | N/A with reason: no provider behavior claim made |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_GUARD_BINDING_CATALOG_AWARE_CHECKER_HARDENING_FOR_CODEX_2026-06-26.md` | `Status: CLOSED_PASS` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_GUARD_BINDING_CATALOG_AWARE_CHECKER_HARDENING_COMPLETION_2026-06-26.md` | `Status: CLOSED_PASS` | PASS |
| Roadmap state | this roadmap | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | N/A with reason | No registry JSON changed | N/A with reason |
| Registry Markdown | N/A with reason | No registry Markdown changed | N/A with reason |
| External evidence digest | N/A with reason | No external evidence used | N/A with reason |
| System loop interlock | N/A with reason | No system loop runtime changed | N/A with reason |
| Session continuity | N/A with reason | Session sync is split into a later commit | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Assertion | Receipt |
|---|---|
| Material code refactor is source-bounded | Targeted guard commands listed in Verification |
| Runners no longer carry marker constants | `rg -n "CATALOG_BINDING_MARKERS" governance/compat` returns no material runner marker |
| Session compaction is separate | Not included in this roadmap commit |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private governance hardening only. No public-sync authorization was granted.

## Claim Boundary

CLOSED_PASS_BOUNDED means the catalog-aware binding path is implemented and tested for known binding-sensitive checkers. It does not claim comprehensive semantic review of every checker in `governance/compat`.
