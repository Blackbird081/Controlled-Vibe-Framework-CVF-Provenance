# CVF GC-018 - MPI-T6 Review Gate Hardening

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-22

docType: gc018_baseline

dispatchBaseHead: 603390b7

## Purpose

Authorize one bounded governance-control tranche before MPI-T6 is revised.
The current uncommitted MPI-T6 packet is retained as an external regression
sample. The tranche must make the earliest applicable reviewer gates reject
four defect classes observed in that sample:

1. unsupported exhaustive or negative filesystem claims;
2. closed GC-018 artifacts omitted from Machine Closure Package validation;
3. closed roadmap residue that still declares pending gates or a parked child;
4. provider-local interaction surfaces accepted as canonical authority.

## Source / Predecessor Evidence

| Source | Verified section or symbol | Disposition |
|---|---|---|
| operator instruction on 2026-06-22 | prioritize hardening and use Claude's MPI-T6 revision as the test | ACCEPT |
| `docs/reference/CVF_WORK_ORDER_CLOSURE_QUALITY_GATE_STANDARD_2026-05-28.md` | closed-equivalent evidence, reviewer conversion, residue rules | ACCEPT |
| `governance/compat/check_closure_packaging_preflight.py` | `ACTIVE_DOC_PREFIXES`, `STALE_CLOSED_PATTERNS`, `validate_doc` | ACCEPT |
| `governance/compat/check_machine_closure_package.py` | `_is_active_governed_doc`, `_is_closed_equivalent`, `validate_machine_closure_package` | ACCEPT |
| `governance/compat/check_agent_packet_authority_and_encoding.py` | `find_provider_specific_authority_violations`, `_run_check` | ACCEPT |
| current uncommitted MPI-T6 packet in the operator worktree | regression input only; not copied as authority | NOT_CVF_SOURCE |

## Decision / Baseline / Proposed Tranche

Decision: authorize bounded machine-gate hardening before MPI-T6 correction.

Baseline: reviewer-fast currently reports structural and encoding failures, but
does not machine-detect the false exhaustive directory claim, the provider-
local authority row, or the closed GC-018 Machine Closure Package omission.

Proposed tranche: modify only the three existing checker owners and their
focused tests, then prove that an MPI-T6-shaped regression fixture is rejected.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: bounded MPI-T6 review-gate hardening.

Protected paths:

- `governance/compat/check_closure_packaging_preflight.py`
- `governance/compat/test_check_closure_packaging_preflight.py`
- `governance/compat/check_machine_closure_package.py`
- `governance/compat/test_check_machine_closure_package.py`
- `governance/compat/check_agent_packet_authority_and_encoding.py`
- `governance/compat/test_check_agent_packet_authority_and_encoding.py`

Operator authorization: the operator explicitly prioritized CVF hardening
before Claude repairs MPI-T6 and designated that repair as the follow-on test.

Rollback boundary: revert only this tranche's checker and focused-test delta;
do not modify or discard the operator worktree's MPI-T6 artifacts.

## Scope Boundary

Allowed: the six protected checker/test paths above, this baseline, the matching
work order, worker return/completion evidence, and later session-sync surfaces.

Forbidden: editing Claude's MPI-T6 packet or roadmap, runtime/product source,
provider/live calls, public-sync, generated corpus registries, or unrelated
governance controls.

## Acceptance Criteria

- focused tests cover all four defect classes and safe counterexamples;
- existing checker behavior remains green;
- an MPI-T6-shaped fixture fails for the new semantic reasons;
- reviewer-fast and pre-closure gates pass on the hardening changed range;
- no claim is made that arbitrary prose semantics are universally verified.

## Evidence / Verification

Dispatch evidence requires the pre-dispatch autorun gate on the real changed
range. Implementation evidence requires focused pytest, an MPI-T6-shaped
negative regression fixture, reviewer-fast, committed diff/status evidence,
and pre-closure autorun results recorded in the completion review.

Implementation evidence pending reviewer conversion: focused pytest passed
41 tests, and the retained MPI-T6 sample triggered exhaustive-directory,
provider-local authority, missing Machine Closure Package, and decided-versus-
parked roadmap violations.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private governance hardening and regression evidence only.

## Current Runtime Freshness Verification

| Claim | Evidence | Disposition |
|---|---|---|
| Runtime behavior | N/A with reason: static governance checker/test tranche only; no runtime behavior is modified or claimed. | N/A with reason |
| Provider/live behavior | N/A with reason: no provider call, key, model, or live proof. | N/A with reason |
| Provider registry freshness | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts`; `PROVIDER_CAPABILITY_REGISTRY` exists but is not modified or consumed by this static checker tranche. | N/A with reason |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_MPI_T6_REVIEW_GATE_HARDENING_FOR_CODEX_2026-06-22.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_MPI_T6_REVIEW_GATE_HARDENING_COMPLETION_2026-06-22.md` | reviewer disposition and gate evidence | PASS |
| Roadmap state | N/A with reason: hardening precedes MPI-T6 roadmap repair. | N/A with reason | PASS |
| Registry JSON | N/A with reason: no registry change. | N/A with reason | PASS |
| Registry Markdown | N/A with reason: no registry change. | N/A with reason | PASS |
| External evidence digest | N/A with reason: operator worktree sample is regression input, not canonical external evidence. | N/A with reason | N/A with reason |
| System loop interlock | focused tests and reviewer-fast | 41 passed; 34/34 PASS | PASS |
| Session continuity | separate post-material session-sync | required following material commit | PASS |

## Claim Boundary

This authorization improves deterministic review gates for explicit textual
and repository-verifiable patterns. It does not prove general semantic truth,
repair MPI-T6, authorize runtime work, or claim universal agent correctness.
