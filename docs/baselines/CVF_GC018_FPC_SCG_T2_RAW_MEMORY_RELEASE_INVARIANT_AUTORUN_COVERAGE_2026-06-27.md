# CVF GC-018 Authorization Baseline - FPC-SCG-T2 Raw Memory Release Invariant Autorun Coverage

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: gc018

Date: 2026-06-27

Batch ID: FPC-SCG-T2

dispatchBaseHead: be06a4cb

rawMemoryReleased: false

## Purpose

Authorize a bounded FPC-SCG-T2 material tranche to close FPC-T3-C06 by adding
a static governance checker for memory-facing governed Markdown that lacks an
explicit `rawMemoryReleased=false` or `rawMemoryReleased: false` assertion.

This baseline authorizes only the checker, focused tests, reviewer-fast and
autorun catalog wiring, FPC guidance update, work order, and completion review.
It does not authorize runtime memory behavior changes, provider/live proof,
MCP/CLI route work, durable store mutation, public-sync, MPI-T6 runtime,
Policy_Local, Document Translator, Model Gateway, Sandbox Runtime, or public
readiness claims.

## Authorization Decision

Operator direction on 2026-06-27 prioritized foundation-plane system-chain gaps
before downstream runtime or use-case work. After FPC-SCG-T1 closed the P0
registry gap, active session state pointed to a fresh P1 machine-check coverage
tranche. FPC-T3-C06 is selected because it is independent, narrow, and protects
the Memory / Knowledge plane raw-memory boundary.

Decision: authorize Codex under `WORKER_MAY_COMMIT` to implement
`check_raw_memory_release_invariant.py`, add focused tests, wire it into the
agent autorun common catalog and reviewer-fast local governance catalog, update
the FPC gap guidance, and close with a completion review.

## Decision

FPC-SCG-T2 is accepted as the bounded implementation tranche for FPC-T3-C06.
The baseline disposition is `CLOSED_PASS_BOUNDED` after focused tests and
governance gates pass.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Active guidance lists FPC-T3-C06 as a P1 machine-check gap | `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md` | `P1 - Machine-Check Coverage Gap` | `FPC-T3-C06` | foundation-plane gap priority guidance | ACCEPT |
| FPC-T3-C06 requires memory-facing artifacts to carry `rawMemoryReleased=false` | `docs/reference/CVF_FPC_T3_FOUNDATION_CHECKER_TEMPLATE_COVERAGE_PLAN_2026-06-13.md` | `### FPC-T3-C06: Memory rawMemoryReleased=false Autorun Check` | `rawMemoryReleased` | FPC-T3 coverage plan | ACCEPT |
| Existing MPI-T5 checker blocks `rawMemoryReleased=true` overclaims but does not require false assertions for every memory-facing artifact | `governance/compat/check_memory_access_claim.py` | `CLAIM_RULES` | `raw_memory_or_reinjection_permitted` | memory access claim gate | ACCEPT |
| Existing MPI-T5 focused test covers `rawMemoryReleased: true` as an overclaim | `governance/compat/test_check_memory_access_claim.py` | `test_raw_memory_release_detected` | `raw_memory_or_reinjection_permitted` | memory access claim focused tests | ACCEPT |
| Memory plane map records MPI-T5 checker as running static claim guard | `docs/reference/CVF_MEMORY_PLANE_MAP.md` | `### Memory Access Claim Checker` | `check_memory_access_claim.py` | Memory Plane map | ACCEPT |
| Runtime readout projection declares false raw-memory and reinjection fields | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.ts` | `buildMemoryRuntimeReadout` projection fields | `rawMemoryReleased` | memory runtime readout projection | ACCEPT |
| Memory readout route response declares false raw-memory and reinjection fields | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` | response body fields | `rawMemoryReleased` | memory readout route | ACCEPT |
| Durable memory store receipt declares false raw-memory and reinjection fields | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | receipt fields | `rawMemoryReleased` | durable memory store | ACCEPT |
| Memory context package evidence declares false raw-memory and reinjection fields | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-context-packager.ts` | package evidence fields | `rawMemoryReleased` | memory context packager | ACCEPT |
| Agent autorun catalog already carries range-aware common governance commands | `governance/compat/agent_autorun_command_catalog.py` | `_common_commands` | `GateCommand` | agent autorun command catalog | ACCEPT |
| Reviewer-fast local governance catalog already carries memory-related static checks | `governance/compat/local_governance_hook_catalog_reviewer_fast.py` | `REVIEWER_FAST_CHECKS` | `memory access claim` | reviewer-fast hook catalog | ACCEPT |

## New Files And Hook Wiring

| Path | Role | Source status |
|---|---|---|
| `governance/compat/check_raw_memory_release_invariant.py` | new read-only static checker | NEW_IN_THIS_TRANCHE |
| `governance/compat/test_check_raw_memory_release_invariant.py` | focused tests for the new checker | NEW_IN_THIS_TRANCHE |
| `governance/compat/agent_autorun_command_catalog.py` | autorun common command wiring | EXISTING_EDIT |
| `governance/compat/local_governance_hook_catalog_reviewer_fast.py` | reviewer-fast command wiring | EXISTING_EDIT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Query: `python governance/compat/run_adif_defect_resolver.py --task-class work-order-authoring --role dispatcher --phase pre-dispatch --json`

Returned defects: ADIF-0001, ADIF-0002, ADIF-0006, ADIF-0007

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

## Expected Result / Prediction

Expected result: a narrow read-only checker can close FPC-T3-C06 without
runtime mutation by failing changed governed Markdown that discusses
memory-write, raw-memory, reinjection, retrieval-facing, or promotion surfaces
without an explicit false raw-memory-release assertion.

## Evidence Comparison

Actual evidence is evaluated in the completion review. The tranche may close
only if focused tests pass, the checker passes on the changed range, and the
autorun/reviewer-fast wiring is present.

## Contradiction Or Gap Disposition

MPI-T5 already blocks explicit raw-memory-release overclaims. That is necessary
but not sufficient for FPC-T3-C06 because C06 requires a positive false
assertion on memory-facing governed artifacts. This tranche closes that narrower
remaining gap.

## Claim Update

After closure, C06 moves from P1 candidate to bounded machine-check coverage.
Remaining P1 candidates are FPC-T3-C02, FPC-T3-C05, and FPC-T3-C03, with P2
runtime/use-case/provider/public/MPI-T6 lanes still parked.

## Core Guard Self-Protection Authorization

This tranche intentionally modifies governance guard surfaces to close a
foundation-plane machine-check gap.

Protected paths:

- `governance/compat/check_raw_memory_release_invariant.py`
- `governance/compat/test_check_raw_memory_release_invariant.py`
- `governance/compat/agent_autorun_command_catalog.py`
- `governance/compat/local_governance_hook_catalog_reviewer_fast.py`

Authorization boundary: read-only static checker, focused tests, and hook/autorun
catalog wiring only. No destructive command, runtime mutation, provider call, or
public-sync is authorized.

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | `governance/compat/check_raw_memory_release_invariant.py`; `governance/compat/test_check_raw_memory_release_invariant.py`; `governance/compat/agent_autorun_command_catalog.py`; `governance/compat/local_governance_hook_catalog_reviewer_fast.py` |
| Runtime behavior claimed | N/A_WITH_REASON: no product runtime, provider route, Web route, CLI/MCP adapter, durable store, or Learning Plane runtime behavior is changed |
| Helper/checker implementation claimed | PASS: new read-only static checker and focused tests are the only implementation claim |
| Provider/live proof claimed | N/A_WITH_REASON |
| Provider registry surfaces | N/A_WITH_REASON: no provider-selection, provider-routing, provider-registry, or live-governance claim is made |
| Public-sync claimed | N/A_WITH_REASON |
| Freshness disposition | PASS - checker-only FPC-T3-C06 coverage |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance foundation-plane checker tranche. Public-sync is not
authorized.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_FPC_SCG_T2_RAW_MEMORY_RELEASE_INVARIANT_AUTORUN_COVERAGE_FOR_CODEX_2026-06-27.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_FPC_SCG_T2_RAW_MEMORY_RELEASE_INVARIANT_AUTORUN_COVERAGE_COMPLETION_2026-06-27.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Checker source | `governance/compat/check_raw_memory_release_invariant.py` | focused tests pass | PASS |
| Focused tests | `governance/compat/test_check_raw_memory_release_invariant.py` | pytest pass | PASS |
| Autorun wiring | `governance/compat/agent_autorun_command_catalog.py` | common range command added | PASS |
| Reviewer-fast wiring | `governance/compat/local_governance_hook_catalog_reviewer_fast.py` | reviewer-fast command added | PASS |
| FPC guidance | `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md` | C06 disposition updated | PASS |
| Roadmap state | `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md` | P1 guidance updated; no roadmap file changed | PASS |
| Registry JSON | BLOCKED with reason: FPC-SCG-T2 is checker-only and does not edit GC-052 registry JSON | N/A | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason: no registry Markdown companion is edited in this tranche | N/A | BLOCKED with reason |
| External evidence digest | N/A with reason: no external evidence or provider proof used | N/A | N/A with reason |
| System loop interlock | `governance/compat/check_system_loop_interlock.py` | registry checker remains pass with no registry edit | PASS |
| Session continuity | reviewer-owned post-material sync | pending separate session-sync after material commit | PASS |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Raw-memory invariant checker exists | `governance/compat/check_raw_memory_release_invariant.py` | new checker created | PASS |
| Focused tests exist | `governance/compat/test_check_raw_memory_release_invariant.py` | new focused tests created | PASS |
| Autorun command present | `raw memory release invariant` | added to `_common_commands` | PASS |
| Reviewer-fast command present | `raw memory release invariant` | added to `REVIEWER_FAST_CHECKS` | PASS |
| Runtime mutation | none | no runtime/source route or durable store path in changed set | PASS |

## Claim Boundary

FPC-SCG-T2 adds static governance coverage for changed governed Markdown. It
does not prove live runtime memory behavior, provider behavior, MCP/CLI route
behavior, durable persistence behavior, public readiness, production readiness,
autonomous mutation safety, or MPI-T6 runtime value.
