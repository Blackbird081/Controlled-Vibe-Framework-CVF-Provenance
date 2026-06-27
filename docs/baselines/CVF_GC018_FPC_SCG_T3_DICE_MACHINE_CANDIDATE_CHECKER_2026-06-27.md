# CVF GC-018 Authorization Baseline - FPC-SCG-T3 DICE Machine-Candidate Checker

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: gc018

Date: 2026-06-27

Batch ID: FPC-SCG-T3

dispatchBaseHead: b64951d5

rawMemoryReleased: false

## Purpose

Authorize a bounded FPC-SCG-T3 material tranche to close FPC-T3-C02 by adding
a read-only governance checker for DICE/DIR machine-candidate coverage.

This baseline authorizes only the checker, focused tests, autorun/reviewer-fast
catalog wiring, FPC guidance update, work order, and completion review. It does
not authorize DICE runtime expansion, DIR runtime mutation, OCR/provider/live
proof, downstream adapter work, external app tree access, public-sync, generated
state mutation, Policy_Local, Document Translator, Model Gateway, Sandbox
Runtime, MPI-T6 runtime, package activation, certification decision, or
public/production/readiness claims.

## Authorization Decision

Operator direction on 2026-06-27 prioritized foundation-plane system-chain gaps
before downstream runtime or use-case work. FPC-SCG-T1 closed the P0 registry
visibility gap and FPC-SCG-T2 closed FPC-T3-C06. Active session state now points
to FPC-T3-C02 DICE machine-candidate coverage as the next P1 machine-check gap.

Decision: authorize Codex under `WORKER_MAY_COMMIT` to implement
`check_dice_machine_candidates.py`, add focused tests, wire it into the agent
autorun common catalog and reviewer-fast local governance catalog, update FPC
gap guidance, and close with a completion review.

## Decision

FPC-SCG-T3 is accepted as the bounded implementation tranche for FPC-T3-C02.
The baseline disposition is `CLOSED_PASS_BOUNDED` after focused tests and
governance gates pass.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Active guidance selects FPC-T3-C02 as the recommended next P1 candidate | `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md` | `Recommended next work order candidate` | `FPC-SCG-T3 DICE Machine-Candidate Checker` | foundation-plane gap priority guidance | ACCEPT |
| FPC-T3-C02 target checker was absent in the original coverage plan | `docs/reference/CVF_FPC_T3_FOUNDATION_CHECKER_TEMPLATE_COVERAGE_PLAN_2026-06-13.md` | `Checker Inventory Snapshot` | `check_dice_machine_candidates.py` | FPC-T3 coverage plan | ACCEPT |
| FPC-T3-C02 purpose is DICE-MC-01 through DICE-MC-10 ownership invariants | `docs/reference/CVF_FPC_T3_FOUNDATION_CHECKER_TEMPLATE_COVERAGE_PLAN_2026-06-13.md` | `### FPC-T3-C02: check_dice_machine_candidates.py` | `DICE-MC-01` | FPC-T3 coverage plan | ACCEPT |
| DICE focused tests already define DICE-MC-01 through DICE-MC-10 markers | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_control_envelope.py` | module header and `test_DICE_MC_*` functions | `DICE-MC-01` | DICE-T1 focused test suite | ACCEPT |
| DICE envelope has a bounded local deterministic claim boundary | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_control_envelope.py` | `CLAIM_BOUNDARY` | `CLAIM_BOUNDARY` | DICE-T1 envelope module | ACCEPT |
| DICE envelope builds the control envelope through one owner function | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_control_envelope.py` | function definition | `build_document_intelligence_control_envelope` | DICE-T1 envelope module | ACCEPT |
| DIR owns authorization gate and downstream capability literals | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | literal type definitions | `AuthorizationGate`; `DownstreamCapability` | DIR-T1 router module | ACCEPT |
| DIR owns scan-route-to-authorization-gate mapping | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | mapping definition | `SCAN_ROUTE_TO_AUTHORIZATION_GATE` | DIR-T1 router module | ACCEPT |
| Autorun catalog supports adding range-aware static gates | `governance/compat/agent_autorun_command_catalog.py` | `_common_commands` | `_range_command` | agent autorun command catalog | ACCEPT |
| Reviewer-fast catalog supports adding range-aware static gates | `governance/compat/local_governance_hook_catalog_reviewer_fast.py` | `REVIEWER_FAST_CHECKS` | `raw memory release invariant` | reviewer-fast hook catalog | ACCEPT |

## New Files And Hook Wiring

| Path | Role | Source status |
|---|---|---|
| `governance/compat/check_dice_machine_candidates.py` | new read-only range-aware checker | NEW_IN_THIS_TRANCHE |
| `governance/compat/test_check_dice_machine_candidates.py` | focused tests for the new checker | NEW_IN_THIS_TRANCHE |
| `governance/compat/agent_autorun_command_catalog.py` | autorun common command wiring | EXISTING_EDIT |
| `governance/compat/local_governance_hook_catalog_reviewer_fast.py` | reviewer-fast command wiring | EXISTING_EDIT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Query: `python governance/compat/run_adif_defect_resolver.py --task-class work-order-authoring --role dispatcher --phase pre-dispatch --json`

Returned defects: ADIF-0001, ADIF-0002, ADIF-0006, ADIF-0007

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

## Expected Result / Prediction

Expected result: a narrow read-only checker can close FPC-T3-C02 without DICE
runtime mutation by detecting changed DICE/DIR paths, verifying DICE-MC-01
through DICE-MC-10 marker coverage, and running the existing focused DICE suite
when those paths change.

## Evidence Comparison

Actual evidence is evaluated in the completion review. The tranche may close
only if focused checker tests pass, the DICE focused suite passes, the new
checker passes on the changed range, and autorun/reviewer-fast wiring is present.

## Contradiction Or Gap Disposition

DICE-T1 already had focused tests, but FPC-T3-C02 recorded that these
invariants were not visible to autorun or reviewer-fast local governance. This
tranche closes that visibility gap without changing DICE runtime behavior.

## Claim Update

After closure, C02 moves from P1 candidate to bounded machine-check coverage.
Remaining P1 candidates are FPC-T3-C05 and FPC-T3-C03, with C05 preferred next
because C01 exists and C03 still needs a stable expected-chain manifest.

## Core Guard Self-Protection Authorization

This tranche intentionally modifies governance guard surfaces to close a
foundation-plane machine-check gap.

Protected paths:

- `governance/compat/check_dice_machine_candidates.py`
- `governance/compat/test_check_dice_machine_candidates.py`
- `governance/compat/agent_autorun_command_catalog.py`
- `governance/compat/local_governance_hook_catalog_reviewer_fast.py`

Authorization boundary: read-only static checker, focused tests, and hook/autorun
catalog wiring only. No destructive command, runtime mutation, provider call,
external app tree access, OCR execution, downstream adapter work, or public-sync
is authorized.

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_control_envelope.py`; `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_control_envelope.py`; `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py`; `governance/compat/check_dice_machine_candidates.py`; `governance/compat/test_check_dice_machine_candidates.py` |
| Runtime behavior claimed | N/A_WITH_REASON: no product runtime, provider route, Web route, CLI/MCP adapter, OCR/provider call, retrieval behavior, or downstream adapter behavior is changed |
| Helper/checker implementation claimed | PASS: new read-only static checker and focused tests are the only implementation claim |
| Provider/live proof claimed | N/A_WITH_REASON |
| Provider registry surfaces | PASS: current provider registry surfaces `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` and `PROVIDER_CAPABILITY_REGISTRY` are not changed; no provider-selection, provider-routing, provider-registry, or live-governance claim is made |
| Public-sync claimed | N/A_WITH_REASON |
| Freshness disposition | PASS - checker-only FPC-T3-C02 coverage |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance foundation-plane checker tranche. Public-sync is not
authorized.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_FPC_SCG_T3_DICE_MACHINE_CANDIDATE_CHECKER_FOR_CODEX_2026-06-27.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_FPC_SCG_T3_DICE_MACHINE_CANDIDATE_CHECKER_COMPLETION_2026-06-27.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Checker source | `governance/compat/check_dice_machine_candidates.py` | focused tests pass | PASS |
| Focused checker tests | `governance/compat/test_check_dice_machine_candidates.py` | pytest pass | PASS |
| DICE focused suite | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_control_envelope.py` | pytest pass | PASS |
| Autorun wiring | `governance/compat/agent_autorun_command_catalog.py` | common range command added | PASS |
| Reviewer-fast wiring | `governance/compat/local_governance_hook_catalog_reviewer_fast.py` | reviewer-fast command added | PASS |
| FPC guidance | `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md` | C02 disposition updated | PASS |
| Roadmap state | `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md` | P1 guidance updated; no roadmap file changed | PASS |
| Registry JSON | BLOCKED with reason: FPC-SCG-T3 is checker-only and does not edit GC-052 registry JSON | N/A | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason: no registry Markdown companion is edited in this tranche | N/A | BLOCKED with reason |
| System loop interlock | `governance/compat/check_system_loop_interlock.py` | registry checker remains pass with no registry edit | PASS |
| External evidence digest | N/A with reason: no external evidence or provider proof used | N/A | N/A with reason |
| Session continuity | reviewer-owned post-material sync | pending separate session-sync after material commit | PASS |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| DICE machine-candidate checker exists | `governance/compat/check_dice_machine_candidates.py` | new checker created | PASS |
| Focused checker tests exist | `governance/compat/test_check_dice_machine_candidates.py` | new focused tests created | PASS |
| DICE-MC markers covered | `DICE-MC-01` through `DICE-MC-10` | marker diagnostics and DICE focused suite pass | PASS |
| Autorun command present | `DICE machine-candidate coverage` | added to `_common_commands` | PASS |
| Reviewer-fast command present | `DICE machine-candidate coverage` | added to `REVIEWER_FAST_CHECKS` | PASS |
| Runtime mutation | none | no DICE/DIR runtime source path changed | PASS |

## Claim Boundary

FPC-SCG-T3 adds local governance visibility for existing DICE-MC focused
coverage. It does not prove document correctness, extraction accuracy, OCR
quality, provider behavior, downstream use-case readiness, public readiness,
production readiness, cost, speed, or MPI-T6 runtime value.
