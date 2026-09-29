# CVF GC-018 Authorization Baseline - FPC-SCG-T6 Interlock Expected-Chain Checker Extension

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: gc018

Date: 2026-06-27

Batch ID: FPC-SCG-T6

dispatchBaseHead: 372ba0e2

rawMemoryReleased: false

## Purpose

Authorize a bounded FPC-SCG-T6 material tranche to extend
`governance/compat/check_system_loop_interlock.py` so FPC-T3-C03 consumes the
source-verified expected-chain manifest closed by FPC-SCG-T5.

This baseline authorizes only checker-source comparison logic, a focused test,
FPC guidance update, this GC-018 baseline, the work order, and completion
review. It does not authorize system-loop registry mutation, manifest expansion,
runtime/MCP/CLI/IDE bridge implementation, provider/live proof, public-sync,
downstream use-case adapter work, DICE runtime expansion, generated
active-session mutation in the material commit, Model Gateway/Sandbox runtime
expansion, Policy_Local, Document Translator, MPI-T6 runtime, package
activation, certification decision, or public/production/readiness claims.

## Authorization Decision

Operator direction on 2026-06-27 prioritized foundation-plane system-chain gaps.
FPC-SCG-T5 closed the stable expected-chain manifest prerequisite for
FPC-T3-C03. The active next-move surfaces now point to FPC-SCG-T6 as the fresh
source-verified checker-extension tranche.

Decision: authorize Codex under `WORKER_MAY_COMMIT` to implement a narrow
expected-chain manifest comparison in the existing system-loop interlock checker
and close T6 without editing the registry or expanding the manifest.

## Decision

FPC-SCG-T6 is accepted as the bounded checker-extension tranche for FPC-T3-C03.
The baseline disposition is `CLOSED_PASS_BOUNDED` after the checker consumes the
manifest, the focused test passes, and governance gates pass.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| FPC-T3-C03 extends the existing system-loop checker instead of creating a new checker | `docs/reference/CVF_FPC_T3_FOUNDATION_CHECKER_TEMPLATE_COVERAGE_PLAN_2026-06-13.md` | `### FPC-T3-C03: Interlock Registry Coverage Checker Extension` | `check_system_loop_interlock.py` | FPC-T3 coverage plan | ACCEPT |
| Expected-chain manifest exists and names the future checker target | `docs/reference/CVF_FPC_T3_C03_INTERLOCK_EXPECTED_CHAIN_MANIFEST_2026-06-27.json` | `futureCheckerTarget` | `governance/compat/check_system_loop_interlock.py` | expected-chain manifest schema | ACCEPT |
| Future checker may compare expected ids against registry ids and matching status | `docs/reference/CVF_FPC_T3_C03_INTERLOCK_EXPECTED_CHAIN_MANIFEST_2026-06-27.json` | `futureCheckerMinimumRule` | `expectedChains[].expectedRegistryId` | expected-chain manifest schema | ACCEPT |
| Manifest rows declare expected automation level for the five eligible chains | `docs/reference/CVF_FPC_T3_C03_INTERLOCK_EXPECTED_CHAIN_MANIFEST_2026-06-27.json` | `expectedChains[]` | `expectedAutomationLevel` | expected-chain manifest schema | ACCEPT |
| System-loop registry contract uses stable connection ids, status, and automationLevel | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_STANDARD_2026-06-02.md` | `## Required Registry Fields` | `id`; `status`; `automationLevel` | system-loop interlock standard | ACCEPT |
| Current checker validates registry structure through `validate_registry` | `governance/compat/check_system_loop_interlock.py` | function definition | `validate_registry` | system-loop interlock checker | ACCEPT |
| Active guidance selects FPC-SCG-T6 as the next candidate | `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md` | `Recommended next work order candidate` | `FPC-SCG-T6 Interlock Registry Expected-Chain Checker Extension` | foundation-plane gap priority guidance | ACCEPT |

## New Files And Hook Wiring

| Path | Role | Source status |
|---|---|---|
| `governance/compat/check_system_loop_interlock.py` | consume expected-chain manifest and compare eligible rows against current registry | EXISTING_EDIT |
| `governance/compat/test_check_system_loop_interlock.py` | focused unit coverage for manifest comparison behavior | NEW_TEST |
| `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md` | record T6 closure and route next work to roadmap refresh/next tranche decision | EXISTING_EDIT |

No new hook wiring is required because `check_system_loop_interlock.py` is
already present in autorun and local hook chains.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: edit the existing GC-052 checker and add
one focused read-only test under `governance/compat/` for FPC-SCG-T6 only.

Protected paths:

- `governance/compat/check_system_loop_interlock.py`
- `governance/compat/test_check_system_loop_interlock.py`

Operator authorization: the operator instructed Codex to continue according to
the next move after FPC-SCG-T5, and active guidance selected FPC-SCG-T6 as the
next source-verified checker-extension tranche on 2026-06-27.

Rollback boundary: if FPC-SCG-T6 is rejected, remove only the T6 checker
extension, focused test, guidance update, and T6 execution artifacts. Do not
revert FPC-SCG-T5 material commit `fbd98f61` or session-sync commit `372ba0e2`.

Scope boundary: this authorization does not extend to registry mutation,
manifest expansion, runtime/product source, provider/live proof, public-sync,
generated active-session state, downstream adapter work, or MPI-T6 runtime.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Query: `python governance/compat/run_adif_defect_resolver.py --task-class work-order-authoring --role dispatcher --phase pre-dispatch --json`

Returned defects: ADIF-0001, ADIF-0002, ADIF-0006, ADIF-0007

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

## Expected Result / Prediction

Expected result: a narrow checker extension can close the FPC-T3-C03 machine
coverage gap by validating every manifest row marked
`ELIGIBLE_FOR_EXPECTED_CHAIN_CHECK` against registry `connections[].id`,
`status`, and `automationLevel`.

## Evidence Comparison

Actual evidence is evaluated in the completion review. The tranche may close
only if the system-loop checker passes, the focused pytest passes, the registry
JSON remains unchanged, the manifest JSON remains unchanged, and governance
gates pass.

## Contradiction Or Gap Disposition

The previous T5 gap was "manifest present; checker extension still missing."
T6 resolves that gap by making the existing checker consume the manifest. Any
future expansion beyond the five source-verified expected chains requires a
later manifest update and fresh source verification.

## Claim Update

After closure, FPC-T3-C03 moves from "manifest present; checker extension
eligible" to "manifest-backed checker extension closed bounded." No runtime,
registry mutation, provider, public-sync, or use-case claim is added.

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | `governance/compat/check_system_loop_interlock.py`; `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json`; `docs/reference/CVF_FPC_T3_C03_INTERLOCK_EXPECTED_CHAIN_MANIFEST_2026-06-27.json` |
| Runtime behavior claimed | N/A_WITH_REASON: no product runtime, provider route, Web route, CLI/MCP adapter, OCR/provider call, retrieval behavior, downstream adapter behavior, or registry behavior is changed |
| Helper/checker implementation claimed | PASS: existing checker now compares eligible expected-chain manifest rows against registry id/status/automationLevel |
| Provider/live proof claimed | N/A_WITH_REASON |
| Provider registry surfaces | PASS: `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` and `PROVIDER_CAPABILITY_REGISTRY` are accounted-for, out-of-scope, and untouched; no provider-selection, provider-routing, provider-registry, or live-governance claim is made |
| Public-sync claimed | N/A_WITH_REASON |
| Freshness disposition | PASS - FPC-T3-C03 manifest-backed checker coverage |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance foundation-plane checker-extension tranche.
Public-sync is not authorized.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_FPC_SCG_T6_INTERLOCK_EXPECTED_CHAIN_CHECKER_EXTENSION_FOR_CODEX_2026-06-27.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_FPC_SCG_T6_INTERLOCK_EXPECTED_CHAIN_CHECKER_EXTENSION_COMPLETION_2026-06-27.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Checker source | `governance/compat/check_system_loop_interlock.py` | expected-chain manifest comparison added | PASS |
| Focused test | `governance/compat/test_check_system_loop_interlock.py` | pytest passes | PASS |
| FPC guidance | `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md` | T6 disposition and next decision updated | PASS |
| Roadmap state | `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md` | P1 guidance updated; no roadmap file changed | PASS |
| Registry JSON | BLOCKED with reason: T6 consumes but does not edit GC-052 registry JSON | N/A | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason: no registry Markdown companion is edited in this tranche | N/A | BLOCKED with reason |
| Manifest JSON | BLOCKED with reason: T6 consumes but does not edit the T5 expected-chain manifest | N/A | BLOCKED with reason |
| System loop interlock | `governance/compat/check_system_loop_interlock.py` | checker passes with manifest comparison enabled | PASS |
| External evidence digest | N/A with reason: no external evidence or provider proof used | N/A | N/A with reason |
| Session continuity | reviewer-owned post-material sync | pending separate session-sync after material commit | PASS |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Eligible manifest rows checked | all `ELIGIBLE_FOR_EXPECTED_CHAIN_CHECK` rows | checker helper iterates eligible rows | PASS |
| Registry id comparison | required | helper fails missing expected id | PASS |
| Status comparison | required | helper fails status mismatch | PASS |
| automationLevel comparison | required | helper fails automationLevel mismatch | PASS |
| Registry mutation | none | registry path unchanged | PASS |
| Manifest mutation | none | manifest path unchanged | PASS |

## Claim Boundary

FPC-SCG-T6 records only manifest-backed structural checker coverage for the
existing system-loop registry. It does not mutate the registry, expand the
manifest, prove runtime/provider behavior, authorize public-sync, certify
semantic correctness, or certify public/production readiness.
