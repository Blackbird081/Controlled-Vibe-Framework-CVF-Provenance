# CVF GC-018 Baseline - SOT3-T4R1 Kernel Current-Reference Authority Repair

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-07-12

Baseline ID: GC018-SOT3-T4R1

## Purpose

Authorize one bounded no-commit repair tranche closing a source-verified gap
in the accepted T4 Truth Kernel package: `TruthKernel.referenceState()` and
`computeReferenceState()` currently accept caller-supplied `isRevoked`/
`isSuperseded` booleans instead of deriving effective `TruthReference` state
from Kernel-owned stores. This blocks SOT3-T5 dispatch (Codex pre-dispatch
review, 2026-07-12) because no injected Flow-side resolver can satisfy NC-11
(`DistributionPackage.routing_decision` must not derive from a caller-supplied
boolean) while the authoritative state derivation itself is caller-supplied
one layer upstream.

## Baseline Decision / Proposed Tranche

Repair `EXTENSIONS/CVF_TRUTH_KERNEL/` in place. Add Kernel-owned direct
reference-revocation and supersession-link stores plus a read-time resolver
that first resolves the caller's `reference_id` to the immutable stored
reference, then derives `REVOKED`, `SUPERSEDED`, and `EXPIRED` from Kernel
stores only. This replaces the caller-supplied object and boolean parameters.
No new package, no Truth Flow work, no
public contract field change (`TruthReference`'s field set and
`reference_state` vocabulary are unchanged; only the derivation mechanism
changes from caller-supplied to store-derived).

## Target / Source

- Blocking finding: Codex pre-dispatch review of SOT3-T5, 2026-07-12 (recorded
  in-place on `docs/baselines/CVF_GC018_SOT3_T5_TRUTH_FLOW_2026-07-12.md` and
  `docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_T5_TRUTH_FLOW_2026-07-12.md`,
  `Status: HOLD_UNTIL_T4_CURRENT_REFERENCE_AUTHORITY`).
- Contract authority: `docs/reference/sot_three_layer/CVF_SOT_THREE_LAYER_CONTRACT_CHAIN.md`, section 6 (`TruthReference`, Precedence rule).
- Negative authority: `docs/reference/sot_three_layer/CVF_SOT_THREE_LAYER_INVARIANTS_AND_NEGATIVE_CASES.md`, Invariant 6; NC-09; NC-10.
- Accepted T4 package under repair: `EXTENSIONS/CVF_TRUTH_KERNEL/` (T4, `REVIEWER_ACCEPTED_AFTER_REPAIR`, material commit `6bf81979b`).
- T4 completion review: `docs/reviews/CVF_SOT3_T4_COMPLETION_REVIEW_2026-07-12.md`.

## Scope / Methodology

Add `referenceRevocations` and `supersessions` stores to `KernelStores`
(direct reference revocation and reference-to-reference supersession link).
Keep receipt revocation resolvable through `TruthReference.receipt_id`. Replace
`computeReferenceState(reference, stores, nowUtcIso, isRevoked, isSuperseded)`
with a store-only resolver `computeCurrentReferenceState(referenceId, stores,
nowUtcIso)` that resolves the immutable stored reference and derives all three
dynamic states from stores; keep the
existing expiry-derivation and precedence logic
(`REVOKED > SUPERSEDED > EXPIRED > ACTIVE`) unchanged. Update
`TruthKernel.referenceState()` to accept only `(referenceId, nowUtcIso)`. Add
direct `revokeReference()` and validated `supersedeReference()` Kernel methods.
No AI,
agent, prompt, provider, network, database, monitor, or adapter.

## Authorization / Decision

T4 material commit `6bf81979b` is accepted; this repair operates on that
accepted package to close a specific source-verified gap before T5 may be
refreshed and redispatched. This baseline does not reopen any other T4
finding (R1-R12, already repaired and accepted). Implementation begins only
when this packet passes pre-dispatch.

## Non-Goals

- no Truth Flow implementation, package, or resolver;
- no change to `TruthReference`'s public field set or `reference_state`
  vocabulary (`ACTIVE`/`SUPERSEDED`/`REVOKED`/`EXPIRED` unchanged);
- no change to `TruthReceipt`, `KernelDecision`, `KernelEvaluationRequest`
  contracts, receipt hash profile, or admission/evaluation/issuance logic
  already accepted at T4 closure;
- no adapter, activation, monitor, database/SOT-index service, Web/UI;
- no AI, agent, prompt, provider SDK, network, public-sync, or live proof;
- no production-readiness claim.

## Planned Artifact Manifest

| Output class | Exact root | Required contents |
|---|---|---|
| store | `EXTENSIONS/CVF_TRUTH_KERNEL/src/stores/kernel-stores.ts` | add `referenceRevocations` and `supersessions` stores |
| engine | `EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/revocation.ts` | receipt-id and direct-reference revocation resolution |
| engine | `EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/reference-issuer.ts` | replace caller-object/flag resolver with store-derived `computeCurrentReferenceState`; add validated `supersedeReference` |
| public API | `EXTENSIONS/CVF_TRUTH_KERNEL/src/kernel.ts` | `referenceState()` takes only `(referenceId, nowUtcIso)`; new `revokeReference()` and `supersede()` methods |
| exports | `EXTENSIONS/CVF_TRUTH_KERNEL/src/index.ts` | export new public result/rejection types only; keep the store-dependent resolver internal |
| tests | `EXTENSIONS/CVF_TRUTH_KERNEL/tests/` | revocation, supersession, expiry, precedence, missing reference, stale-ACTIVE-snapshot cases |
| worker return | `docs/reviews/CVF_SOT3_T4R1_WORKER_RETURN_2026-07-12.md` | exact manifest, proof, no-commit evidence |

## Source Verification Block

| Claimed item | Fact class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| `computeReferenceState` accepts caller-supplied `isRevoked`/`isSuperseded` | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/reference-issuer.ts` | lines 168-179 | `computeReferenceState`; `isRevoked`; `isSuperseded` | accepted T4 Kernel package | ACCEPT |
| `TruthKernel.referenceState()` forwards caller-supplied flags unchanged | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_TRUTH_KERNEL/src/kernel.ts` | lines 142-149 | `referenceState`; `isRevoked`; `isSuperseded` | accepted T4 Kernel package | ACCEPT |
| revocation is keyed only by `receipt_id`, with no direct reference-revocation path | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/revocation.ts` | lines 18-40 | `revokeReceipt`; `isReceiptRevoked`; `currentReceiptStatus` | accepted T4 Kernel package | ACCEPT |
| no direct reference-revocation or supersession-link store exists in `KernelStores` | EXISTS | `EXTENSIONS/CVF_TRUTH_KERNEL/src/stores/kernel-stores.ts` | lines 18-27 | `KernelStores` | accepted T4 Kernel package | ACCEPT |
| `TruthReference` carries `receipt_id` and no supersession field | VALUE_SET | `EXTENSIONS/CVF_TRUTH_KERNEL/src/types/truth-reference.ts` | lines 8-16 | `TruthReference` | accepted T4 Kernel package | ACCEPT |
| `ImmutableStore` supports insert/get/has/all with deep-clone snapshots, suitable for a new supersession store | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_TRUTH_KERNEL/src/stores/immutable-store.ts` | lines 8-30 | `ImmutableStore` | accepted T4 Kernel package | ACCEPT |
| no existing test exercises revocation, supersession, expiry, or precedence via the store path | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_TRUTH_KERNEL/tests/reference-integrity.test.ts` | lines 49-59 | `describe("TruthReference integrity resolution")` | accepted T4 Kernel package tests | ACCEPT - only hash-mismatch and missing-verification-result cases exist |
| T2 precedence rule Kernel must implement store-side | LITERAL_INVARIANT | `docs/reference/sot_three_layer/CVF_SOT_THREE_LAYER_CONTRACT_CHAIN.md` | section 6, Precedence rule | `reference_state` | T2 contract chain | ACCEPT |
| Invariant 6 / NC-09 / NC-10 require Kernel-derived, not caller-derived, dynamic state | LITERAL_INVARIANT | `docs/reference/sot_three_layer/CVF_SOT_THREE_LAYER_INVARIANTS_AND_NEGATIVE_CASES.md` | Invariant 6; NC-09; NC-10 | `reference_state` | T2 negative contract | ACCEPT |

## Required Invariants

1. `computeCurrentReferenceState` accepts a `reference_id`, resolves the
   immutable stored reference, and takes no caller-supplied reference object,
   `isRevoked`, or `isSuperseded` authority input.
2. Revocation is resolvable both through the reference's `receipt_id` link to
   `stores.revocations` and through a Kernel-owned direct-reference revocation
   record; either cause reads `REVOKED` without any caller flag.
3. Supersession is resolvable via a Kernel-owned `supersessions` store. A
   supersession insert requires distinct existing references, identical
   `scope`, and a superseding reference whose `valid_from_utc` is strictly
   later; self-links, cross-scope links, older/equal links, and duplicate
   supersession records fail closed.
4. Precedence remains exactly `REVOKED > SUPERSEDED > EXPIRED > ACTIVE`,
   evaluated in that order, unchanged from the T2 contract.
5. Expiry remains derived from `valid_until_utc` compared to the supplied
   `nowUtcIso` read-time argument; no independent stored expiry flag.
6. A reference resolved a second time after its underlying receipt is
   revoked, or after a newer reference for the same scope is recorded via
   `supersede()`, must report the updated state; the original issuance-time
   `ACTIVE` snapshot is never treated as durable current-state authority.
7. Missing reference IDs, missing bound receipts, and invalid timestamps fail
   closed with typed resolution results, never exceptions or default `ACTIVE`.
8. `TruthReference`'s public field set and `reference_state` vocabulary are
   unchanged; only the derivation mechanism changes.
9. No AI, agent, prompt, provider, network, monitor, or adapter dependency.

## New Doc-Only Fields

| Proposed item | Intended owner | Dispatch status |
|---|---|---|
| `ReferenceStateResolutionResult`; `ReferenceStateResolutionReason` | T4R1 Kernel engine/public type export | NEW_RUNTIME_SURFACE_TO_IMPLEMENT |
| `ReferenceRevocationRecord`; `ReferenceSupersessionRecord` | `KernelStores` | NEW_RUNTIME_SURFACE_TO_IMPLEMENT |
| typed reference revocation/supersession rejection tokens | T4R1 Kernel engine/public type export | NEW_RUNTIME_SURFACE_TO_IMPLEMENT |

## Fail Conditions

Any caller-supplied reference object or revocation/supersession authority flag
remaining in a public Kernel state-read signature, any reference reading
`ACTIVE` after its receipt/reference is revoked or after a valid supersession
record exists, any invalid supersession link being accepted, any
precedence-order deviation, any stale cached-snapshot read replacing a fresh
store-derived read, forbidden dependency, or out-of-scope path blocks
closure.

## Verification / Evidence

Typecheck, build, focused tests for revocation, supersession, expiry,
precedence (all four states independently and in combination), missing
reference, and stale-ACTIVE-snapshot rejection; full existing T4 suite
re-run to confirm no regression (6 suites/33 tests baseline); dependency
scan; exact status/diff; worker-return fast gate; file-size guard; unchanged
worker HEAD.

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | current `EXTENSIONS/CVF_TRUTH_KERNEL/src/kernel.ts`, `src/engine/reference-issuer.ts`, `src/engine/revocation.ts`, `src/stores/kernel-stores.ts`, `src/stores/immutable-store.ts`, `src/types/truth-reference.ts`, `tests/reference-integrity.test.ts` |
| Runtime behavior claimed | TARGET_PRESENT_WITH_GAP: caller-supplied `isRevoked`/`isSuperseded` parameters confirmed present at both call sites listed in the Source Verification Block |
| Helper/checker implementation claimed | N/A_WITH_REASON: no governance checker or hook mutation |
| Provider/live proof claimed | N/A_WITH_REASON: deterministic local package only |
| Public-sync claimed | N/A_WITH_REASON: private provenance packet only |
| Freshness disposition | PASS - current gap rechecked directly against source on 2026-07-12, matching Codex's pre-dispatch finding |

## Repair Scope Control Block

This tranche is a bounded in-place repair of an already-accepted CVF-native
package (`EXTENSIONS/CVF_TRUTH_KERNEL/`, material commit `6bf81979b`). It
performs no retained-corpus enumeration, no external-repository intake, and
no knowledge absorption action, so the absorption-entry, blind-spot,
completeness, and intake-routing control families do not apply to this
artifact class. The triggering evidence is a same-session Codex pre-dispatch finding
against already-accepted CVF source, re-verified directly against current
`EXTENSIONS/CVF_TRUTH_KERNEL/` source in the Source Verification Block above,
not an external or retained corpus read.

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| caller-supplied revocation/supersession flags | `EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/reference-issuer.ts` | CONFIRMED_EXISTING | replace with store-derived resolution; same file, same owner | repair in place |
| revocation store keyed by `receipt_id` | `EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/revocation.ts` | CONFIRMED_EXISTING | extend resolution path from a `TruthReference.receipt_id` link; no new store needed for revocation | repair in place |
| supersession link | `EXTENSIONS/CVF_TRUTH_KERNEL/src/stores/kernel-stores.ts` (owner absent) | OWNER_SURFACE_NOT_FOUND | no current store or record type for reference-to-reference supersession | add `supersessions` store to `KernelStores`, same owner package |

## Dependency-Closure Matrix

| Dependency layer | Source evidence | T4R1 obligation | Disposition |
|---|---|---|---|
| T2 contract chain, `TruthReference` section 6 | `docs/reference/sot_three_layer/CVF_SOT_THREE_LAYER_CONTRACT_CHAIN.md` | precedence and field set must remain exactly as specified | ACCEPT |
| T2 invariants, Invariant 6 / NC-09 / NC-10 | `docs/reference/sot_three_layer/CVF_SOT_THREE_LAYER_INVARIANTS_AND_NEGATIVE_CASES.md` | dynamic state must be Kernel-derived, not caller-derived | ACCEPT |
| T4 accepted package (`kernel.ts`, `reference-issuer.ts`, `revocation.ts`, `kernel-stores.ts`) | source re-read 2026-07-12, cited above | repair only the caller-flag gap; no other accepted T4 behavior changes | ACCEPT |
| Codex pre-dispatch finding on SOT3-T5 | in-place `HOLD_UNTIL_T4_CURRENT_REFERENCE_AUTHORITY` status on both T5 packet files | this repair is the exact closing condition named by the reviewer | ACCEPT |
| proposed T4R1 artifacts | Planned Artifact Manifest above | store/engine/API changes plus tests, no runtime yet | PLANNED |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind gc018-baseline --batch-id SOT3-T4R1 --title "Kernel Current-Reference Authority Repair" --date 2026-07-12 --base 1bf21dcee --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | bounded TypeScript package repair baseline |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | Hand-authored from the GC-018 template directly, following the T4/T5 baselines' proven section shape. Added the caller-flag repair scope, revocation/supersession source verification, and repair-specific dependency-closure matrix. |
| checkerReadAheadConfirmation | dispatch, structural, handoff, worker-return, file-size checkers |
| docOnlyNewFields | proposed `ReferenceStateResolutionResult`, `ReferenceStateResolutionReason`, `ReferenceRevocationRecord`, `ReferenceSupersessionRecord`, and supersession/revocation rejection tokens; none exists before this repair |
| claimBoundary | dispatch baseline only; no runtime proof |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defectIds: ADIF-0001, ADIF-0002, ADIF-0006, ADIF-0007,
ADIF-0014, ADIF-0015, ADIF-0016, ADIF-0017, ADIF-0020, ADIF-0021, ADIF-0024.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_dispatch_scaffold_provenance.py` |
| literalTokensReviewed | DISPATCH_READY; Source Verification Block; Dependency-Closure Matrix; Public Export Disposition; NOT_APPLICABLE_WITH_REASON |
| gateRunPurpose | confirm source-derived packet fidelity before implementation |
| claimBoundary | gate PASS does not prove repair correctness |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance repair tranche; no public-sync authorization.

## Claim Boundary

This baseline authorizes only a bounded T4 repair after pre-dispatch. It
does not authorize T5 implementation, T6-T7, vertical slice, provider/live,
public, adapter, or activation work. It does not reopen any other T4 finding
already accepted at material commit `6bf81979b`.
