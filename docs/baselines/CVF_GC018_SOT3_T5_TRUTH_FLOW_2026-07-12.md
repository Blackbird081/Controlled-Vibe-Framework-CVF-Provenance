# CVF GC-018 Baseline - SOT3-T5 Post-Kernel Truth Flow

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-07-12

Baseline ID: GC018-SOT3-T5

## Purpose

Authorize one bounded no-commit implementation tranche for a CVF-owned,
deterministic Truth Flow package that consumes only Kernel-approved
`TruthReference` authority (per the accepted T2 contract chain and the
accepted T4 Truth Kernel runtime) and adds a strictly post-Kernel lifecycle:
routing, dose, distribution, consumption, feedback proposal, recall, and
retirement. No trust evaluation, no second `TruthReference` producer, no
direct `VERIFIED`-style transition without Kernel proof.

## Baseline Decision / Proposed Tranche

Create a new package at `EXTENSIONS/CVF_TRUTH_FLOW/`. This package is a new
owner candidate (T1 CAP-06, `NEW_OWNER_CANDIDATE`); it duplicates no existing
CVF owner. It never re-implements Refinery, never evaluates trust, and never
mints, forges, or restates `KernelDecision`, `TruthReceipt`, or
`TruthReference`. Direct import of the retained `CVF_Truth_Flow_Patch`
package is rejected.

## Target / Source

- Main roadmap: `docs/roadmaps/CVF_SOT_THREE_LAYER_ABSORPTION_ROADMAP_2026-07-12.md`.
- Contract authority (sections 6-8): `docs/reference/sot_three_layer/CVF_SOT_THREE_LAYER_CONTRACT_CHAIN.md`.
- Negative authority (Invariants 6-9; NC-04A, NC-04B, NC-09, NC-10, NC-11, NC-12): `docs/reference/sot_three_layer/CVF_SOT_THREE_LAYER_INVARIANTS_AND_NEGATIVE_CASES.md`.
- Owner reconciliation: `docs/reviews/CVF_SOT3_T1_OWNER_NOVELTY_MAP_2026-07-12.md`, CAP-06, CAP-07.
- Accepted upstream authority boundary: `EXTENSIONS/CVF_TRUTH_KERNEL/` (T4, `REVIEWER_ACCEPTED_AFTER_REPAIR`, material commit `6bf81979b`).
- Doctrine owner: `docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_SOURCE_PROVENANCE_AND_VERIFICATION_CONTRACT.md`.
- Retained evidence: `.private_reference/legacy/CVF_SOT 10.07/CVF_Truth_Flow_Patch`.

## Scope / Methodology

Build package metadata, strict TypeScript contracts for `DistributionPackage`
and `FeedbackProposal`, deterministic routing/dose/lifecycle engines, an
read-only Kernel authority consumer using the actual injected `TruthKernel`
instance and its ID-only `referenceState()` API, never a substitute resolver,
raw-snapshot lookup, or Kernel reimplementation),
recall/retirement transitions, and a proposal-only feedback path. No AI,
agent, prompt, provider, network, database, monitor, or activation.

## Authorization / Decision

T4 closed at `6bf81979b`; T4R1 current-reference authority repair closed at
`cda8fec64`; roadmap release `7dafc9185` permits T5 packet authoring.
Implementation begins only when this refreshed packet passes pre-dispatch.

## Non-Goals

- no trust evaluation, no second `KernelDecision`/`TruthReceipt`/
  `TruthReference` producer, no restatement of Kernel authority;
- no embedded or duplicate Refinery/`RefineryPacket` producer inside Flow;
- no direct `VERIFIED`-equivalent lifecycle transition without a resolved,
  eligible, non-expired, non-revoked `TruthReference`;
- no caller-supplied `truthKernelAccepted`-style boolean or string ID
  substituting for a bound `TruthReference`;
- no direct feedback mutation of a `TruthReceipt`, `TruthReference`, evidence
  record, or source score;
- no runtime monitor, SOT-index/database service, adapter, Guard Contract
  adapter, phase-governance adapter, Web/UI, or activation;
- no AI, agent, prompt, provider SDK, network, public-sync, or live proof;
- no package activation or production-readiness claim.

## Planned Artifact Manifest

| Output class | Exact root | Required contents |
|---|---|---|
| package | `EXTENSIONS/CVF_TRUTH_FLOW/` | metadata, tsconfig, README |
| source | `EXTENSIONS/CVF_TRUTH_FLOW/src/` | `DistributionPackage`/`FeedbackProposal` contracts, Kernel-reference resolver, routing engine, dose engine, lifecycle engine, feedback engine, recall/retirement, exports |
| schemas | `EXTENSIONS/CVF_TRUTH_FLOW/schemas/` | distribution package, feedback proposal |
| tests | `EXTENSIONS/CVF_TRUTH_FLOW/tests/` | positive path, NC-09, NC-10, NC-11, NC-12, no-second-Refinery boundary, no-second-Kernel-authority boundary, determinism |
| worker return | `docs/reviews/CVF_SOT3_T5_WORKER_RETURN_2026-07-12.md` | exact manifest, proof, no-commit evidence |

## Source Verification Block

| Claimed item | Fact class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| T4 Kernel is accepted and closed | EXISTS | `docs/reviews/CVF_SOT3_T4_COMPLETION_REVIEW_2026-07-12.md` | Machine Closure Package | `TRUTH_KERNEL_CORE_ACCEPTED_BOUNDED` | T4 completion review | ACCEPT |
| Flow post-Kernel lifecycle owner is absent | EXISTS | `docs/reviews/CVF_SOT3_T1_OWNER_NOVELTY_MAP_2026-07-12.md` | CAP-06 | `NEW_OWNER_CANDIDATE` | T1 owner map | ACCEPT |
| Flow-embedded Refinery is rejected | EXISTS | `docs/reviews/CVF_SOT3_T1_OWNER_NOVELTY_MAP_2026-07-12.md` | CAP-07 | `REJECT_DIRECT_IMPORT` | T1 owner map | ACCEPT |
| DistributionPackage and FeedbackProposal field sets and authority are canonical | VALUE_SET | `docs/reference/sot_three_layer/CVF_SOT_THREE_LAYER_CONTRACT_CHAIN.md` | sections 7 and 8 | `DistributionPackage`; `FeedbackProposal` | T2 contract chain | ACCEPT |
| distribution requires a valid, non-expired, non-revoked TruthReference | LITERAL_INVARIANT | `docs/reference/sot_three_layer/CVF_SOT_THREE_LAYER_INVARIANTS_AND_NEGATIVE_CASES.md` | Invariant 8; NC-09; NC-10 | `reference_state`; `valid_until_utc` | T2 negative contract | ACCEPT |
| Flow cannot publish from caller-supplied booleans | LITERAL_INVARIANT | `docs/reference/sot_three_layer/CVF_SOT_THREE_LAYER_INVARIANTS_AND_NEGATIVE_CASES.md` | Invariant 7; NC-11 | `routing_decision` | T2 negative contract | ACCEPT |
| feedback is proposal-only and cannot mutate authority directly | LITERAL_INVARIANT | `docs/reference/sot_three_layer/CVF_SOT_THREE_LAYER_INVARIANTS_AND_NEGATIVE_CASES.md` | Invariant 9; NC-12 | `no_direct_mutation_flag`; `review_status` | T2 negative contract | ACCEPT |
| TruthReference precedence and state model Flow must read, not derive | LITERAL_INVARIANT | `docs/reference/sot_three_layer/CVF_SOT_THREE_LAYER_CONTRACT_CHAIN.md` | section 6, Precedence rule | `reference_state` | T2 contract chain | ACCEPT |
| accepted Kernel TruthReference type and revocation/state resolvers exist for Flow to consume by reference | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_TRUTH_KERNEL/src/types/truth-reference.ts` | `TruthReference` interface | `reference_state` | accepted T4 Kernel package | ACCEPT |
| accepted Kernel exposes the authoritative ID-only state-read method | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_TRUTH_KERNEL/src/kernel.ts` | `TruthKernel.referenceState` | `referenceState` | `TruthKernel` | ACCEPT - `(referenceId, nowUtcIso)` resolves Kernel-owned stores and returns a typed result |
| issued TruthReference stores an ACTIVE snapshot and effective state is evaluated at read time | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/reference-issuer.ts` | `issueReference`; `computeCurrentReferenceState` | `reference_state`; `computeCurrentReferenceState` | accepted T4R1 Kernel package | ACCEPT - raw issuance snapshot is not current-state authority |
| Kernel public API resolves current state without caller authority flags | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_TRUTH_KERNEL/src/kernel.ts` | `TruthKernel.referenceState` | `referenceState` | accepted T4R1 Kernel package at `cda8fec64` | ACCEPT |
| Kernel internal resolver derives stored revocation, supersession, and expiry evidence | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/reference-issuer.ts` | `computeCurrentReferenceState` | `computeCurrentReferenceState` | accepted T4R1 Kernel package at `cda8fec64` | ACCEPT |
| Kernel resolves receipt and direct-reference revocation | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/revocation.ts` | `isReferenceEffectivelyRevoked` | `isReferenceEffectivelyRevoked` | accepted T4R1 Kernel package at `cda8fec64` | ACCEPT |
| retained publish gate trusts a caller-supplied boolean instead of a bound TruthReference | RUNTIME_BEHAVIOR | `.private_reference/legacy/CVF_SOT 10.07/CVF_Truth_Flow_Patch/EXTENSIONS/CVF_TRUTH_FLOW/src/routing/publish-gate.ts` | `PublishGateInput.truthKernelAccepted` | `evaluatePublishGate` | retained prototype | ACCEPT |
| retained source-score feedback path mutates directly instead of proposing | RUNTIME_BEHAVIOR | `.private_reference/legacy/CVF_SOT 10.07/CVF_Truth_Flow_Patch/EXTENSIONS/CVF_TRUTH_FLOW/src/feedback/source-score.ts` | `updateSourceScore` | `updateSourceScore` | retained prototype | ACCEPT |
| retained lifecycle uses a caller-controlled composite state machine promoting to VERIFIED without a receipt check, and duplicates a RefineryPacket boundary Refinery already owns | RUNTIME_BEHAVIOR | `.private_reference/legacy/CVF_SOT 10.07/CVF_Truth_Flow_Patch/EXTENSIONS/CVF_TRUTH_FLOW/src/lifecycle/lifecycle-engine.ts` | `LifecycleEngine.transition` | `LifecycleState`; `allowed` | retained prototype | ACCEPT |
| accepted T3 Refinery package exists as the sole upstream packet producer Flow must not duplicate | EXISTS | `EXTENSIONS/CVF_REFINERY/` | `src/`, `schemas/`, `tests/` directories present | N/A - directory existence only | accepted T3 Refinery package | ACCEPT |

## Required Invariants

1. Flow never produces `KernelDecision`, `TruthReceipt`, or `TruthReference`;
   it only reads an already-issued, Kernel-resolved `TruthReference` by
   reference.
2. Flow never produces a second `RefineryPacket` or duplicates Refinery
   normalization/dedupe/conflict logic.
3. `DistributionPackage.routing_decision` derives only from the actual
   `TruthKernel.referenceState()` result for a bound reference ID at the action
   evaluation time; a raw issuance snapshot, caller-supplied state/boolean, or
   string ID never substitutes (Invariant 7, NC-11).
4. `DistributionPackage` creation with an empty `truth_references` collection,
   or with any referenced `TruthReference.reference_state` not `ACTIVE` at
   creation time, fails closed (Invariant 8, NC-09, NC-10).
5. `reference_state` is read from the injected actual `TruthKernel` instance,
   whose state-read applies precedence (`REVOKED > SUPERSEDED >
   EXPIRED > ACTIVE`) at the supplied action time; Flow computes no competing
   supersession/revocation/expiry flag of its own and does not trust the raw
   issuance snapshot as current state.
6. Information dose, routing, and consumption are recipient/role/task/phase
   scoped and TTL-bound (`expiry_utc`); package lifecycle uses only
   `PENDING_ACKNOWLEDGEMENT`, `ACKNOWLEDGED`, `EXPIRED`, `WITHDRAWN`.
7. Before every routing, delivery, acknowledgement, or consumption action,
   Flow re-resolves every bound reference at that action time and fails closed
   unless all effective states are `ACTIVE`; creation-time acceptance is not
   reusable current-state authority.
8. Recall and retirement use only the T2-valid
   `PENDING_ACKNOWLEDGEMENT -> WITHDRAWN` transition. `ACKNOWLEDGED`, `EXPIRED`,
   and `WITHDRAWN` remain terminal; T5 creates no post-acknowledgement recall
   state and never mutates the underlying Kernel record.
9. `FeedbackProposal` never mutates a `TruthReceipt`, `TruthReference`,
   evidence record, or source score directly; only an `ACCEPTED` proposal may
   trigger a separate, governed mutation action outside this package's scope
   (Invariant 9, NC-12).
10. Every Flow-local state transition is a deterministic, immutable-snapshot
    append; no global clock/random source is read inside `src/`.
11. No AI, agent, prompt, provider, network, monitor, or adapter dependency.

## Resolved Prerequisite Evidence

T4R1 closed at `cda8fec64`. `TruthKernel.referenceState(referenceId,
nowUtcIso)` now resolves immutable Kernel stores, applies receipt/direct
reference revocation, supersession, expiry, and typed missing-record failure.
T5 must call this public method on the actual Kernel instance before every
authority-bearing action; it must not introduce a substitute resolver.

## Fail Conditions

Any Flow-side truth minting, second Refinery/Kernel authority, raw/stale
reference snapshot accepted as current authority, missing action-time
re-resolution, empty or non-`ACTIVE` `truth_references` at distribution, caller-supplied
approval-boolean routing, direct feedback mutation, direct
`VERIFIED`-equivalent transition without a resolved eligible
`TruthReference`, nondeterministic clock/ID, forbidden dependency, or
out-of-scope path blocks closure.

## Verification / Evidence

Typecheck, build, focused negative tests (NC-09, NC-10, NC-11, NC-12 plus a
no-second-Refinery and no-second-Kernel-authority boundary test), dependency/
forbidden scans, exact status/diff, worker-return fast gate, file-size guard,
and unchanged worker HEAD.

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | current `EXTENSIONS/`, T1 owner map, T2 contracts, accepted T4 Kernel package, retained Flow prototype |
| Runtime behavior claimed | TARGET_ABSENT_AT_DISPATCH: no current CVF-owned `EXTENSIONS/CVF_TRUTH_FLOW/` package exists |
| Helper/checker implementation claimed | N/A_WITH_REASON: no governance checker or hook mutation |
| Provider/live proof claimed | N/A_WITH_REASON: deterministic local package only |
| Public-sync claimed | N/A_WITH_REASON: private provenance packet only |
| Freshness disposition | PASS - current owner/runtime boundaries rechecked on 2026-07-12 |

## External Repository Absorption Entry Control

| Field | Value |
|---|---|
| Source type | retained legacy three-folder source family narrowed to Flow evidence |
| Upstream or source-mirror disposition | LEGACY_REFERENCE_ONLY_WITH_REASON: operator-authored retained patch without verified upstream identity |
| Enumeration or manifest plan | reuse accepted T0 305-record manifest and enumerate retained Flow folder with filesystem-backed command |
| Per-file terminal-ledger plan | T5 converts selected Flow lifecycle/routing/dose/feedback value; T7 retains final 305-file reconciliation |
| Owner or overlap route | create only the absent post-Kernel Flow lifecycle owner; reject the embedded Refinery duplicate |
| Value-disposition route | ADAPT routing/dose/lifecycle/feedback concepts; REJECT_DIRECT_IMPORT retained runtime, publish-gate boolean, source-score mutation, and embedded Refinery |
| Claim boundary | bounded Flow rewrite only; no full-corpus closure, monitor, database, adapter, provider, public, or activation claim |

## Mandatory Blind-Spot Control Block

- Source enumeration gate: reuse accepted T0 manifest (79 Flow files,
  78380 bytes, digest `e7be38e77889f6280248fc4a6ceacf354a41c8f1c331fbb2a491e29f8a27858f`)
  and re-read every cited retained Flow source before implementation.
- Owner-surface gate: T1 CAP-06 (`NEW_OWNER_CANDIDATE`) and CAP-07
  (`REJECT_DIRECT_IMPORT`) separate the new lifecycle owner from the rejected
  embedded-Refinery duplicate.
- Overlap gate: classify all retained value through the matrices below.
- Runtime/package gate: only the new local Flow package is in scope; monitor,
  adapters, database/SOT-index, provider/live, Web/UI, and activation remain
  forbidden.
- Verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS.

## Corpus Completeness And Report Integrity

- Corpus task class: bounded T5 implementation from accepted SOT3 corpus.
- Corpus root: `.private_reference/legacy/CVF_SOT 10.07/CVF_Truth_Flow_Patch`.
- Snapshot time: 2026-07-12 local dispatch session.
- Enumeration command: `rg --files --hidden --no-ignore ".private_reference/legacy/CVF_SOT 10.07/CVF_Truth_Flow_Patch"`.
- Manifest artifact or inline manifest: accepted `docs/evidence/sot/sot3-t0-source-manifest.json`.
- Manifest hash: retained from accepted T0 evidence; no new whole-corpus claim.
- Processing ledger artifact or inline ledger: overlap and conversion matrices in this baseline.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE
- Reconciliation: manifest=305; ledger_terminal=0; exclusions=305; unresolved=0. Final corpus reconciliation remains T7-owned.
- Unresolved files: 0 within selected T5 source facts.
- Declared exclusions: monitors, databases, adapters, embedded Refinery, generated/vendor files, AI/provider surfaces.
- Unreadable or unsupported files: none known at dispatch.
- Aggregation check: T5 proves one bounded runtime owner, not full three-folder closure.
- Drift check: worker reopens all cited authority and retained sources.
- Output traceability: every adapted concept maps to package output or explicit rejection.
- Adversarial verification: empty/non-active reference collections, caller-supplied booleans, direct feedback mutation, and embedded-Refinery duplication are tested.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS - T5 is limited to the Flow capability subset.

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | retained Flow folder plus accepted T1-T4 CVF authority |
| Enumeration command | `rg --files --hidden --no-ignore ".private_reference/legacy/CVF_SOT 10.07/CVF_Truth_Flow_Patch"` |
| Manifest artifact or inline manifest | `docs/evidence/sot/sot3-t0-source-manifest.json` plus Planned Artifact Manifest table in this baseline |
| Processing ledger artifact or inline ledger | Overlap And Novelty Classification and External Absorption Value Conversion Matrix tables in this baseline; worker return adds implementation ledger |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | new `EXTENSIONS/CVF_TRUTH_FLOW/` candidate, strictly post-Kernel |
| Unresolved items | zero T5 dispatch blockers; T7 retains corpus closure |
| Completion claim boundary | bounded T5 Flow package only |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| post-Kernel routing/dose/distribution/consumption/observation/recall/retirement | OWNER_SURFACE_NOT_FOUND | OWNER_SURFACE_NOT_FOUND | no current general Flow lifecycle owner | Create bounded package (T1 CAP-06). |
| Flow-embedded Refinery (`refinery-engine.ts` and siblings) | `EXTENSIONS/CVF_REFINERY/` (accepted T3 sole producer) | REJECT_DIRECT_IMPORT | second, incompatible `RefineryPacket` producer | Exclude entirely; do not port. |
| `publish-gate.ts` caller-supplied boolean | `docs/reference/sot_three_layer/CVF_SOT_THREE_LAYER_CONTRACT_CHAIN.md`, `DistributionPackage` section | REJECT_DIRECT_IMPORT | `routing_decision` must derive from a bound `TruthReference`, not a boolean | Rewrite gate against Kernel-resolved reference only. |
| `source-score.ts` direct mutation | `docs/reference/sot_three_layer/CVF_SOT_THREE_LAYER_CONTRACT_CHAIN.md`, `FeedbackProposal` section | REJECT_DIRECT_IMPORT | direct authority-store mutation bypasses proposal review | Rewrite as proposal-only path. |
| `lifecycle-engine.ts` composite `LifecycleState` (including `VERIFIED`) | T2 contract chain, `TruthReference`/`DistributionPackage` sections | REJECT_DIRECT_IMPORT | conflates Refinery/Kernel/Flow-owned states into one caller-controlled machine; `VERIFIED` is reachable without receipt proof | Rewrite as a `DistributionPackage`-scoped status vocabulary only (`PENDING_ACKNOWLEDGEMENT`/`ACKNOWLEDGED`/`EXPIRED`/`WITHDRAWN`); no Flow-local "VERIFIED" token. |
| routing/dose/distribution/consumption concepts (routing policy, information dose, context profile) | OWNER_SURFACE_NOT_FOUND | NEW_FINDING | useful deterministic concepts require `TruthReference`-bound CVF rewrite | Adapt only contract-aligned concepts into `DistributionPackage` fields. |
| monitors, adapters (`guard-contract-adapter.ts`, `phase-governance-adapter.ts`, `truth-kernel-adapter.ts`), database/SOT-index service | OWNER_SURFACE_NOT_FOUND | NO_NEW_VALUE | outside bounded T5 value | Exclude and retain separate authorization boundary. |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| T2/T4 authority chain | Kernel-issued, resolvable `TruthReference` | DOCTRINE_ADAPTED | `EXTENSIONS/CVF_TRUTH_FLOW/` reads accepted Kernel exports only | implement read-only reference resolution | no Kernel logic duplicated |
| independent Flow identity | exclusive `DistributionPackage`/`FeedbackProposal` producer | PACKAGE_CANDIDATE | `EXTENSIONS/CVF_TRUTH_FLOW/` | create package subject to review | no activation |
| routing/dose/lifecycle/feedback engines | deterministic post-Kernel distribution and proposal-only feedback | RUNTIME_CANDIDATE | new package source | implement bounded local runtime | no provider/network/database |
| retained publish-gate/source-score/lifecycle-engine/embedded-Refinery | fail-open, direct-mutation, or duplicate-authority implementation | REJECT_DIRECT_IMPORT | CVF-native rewrite only | reject direct copy | no compatibility layer |
| no-second-Refinery / no-second-Kernel-authority boundary test | possible repeated-defect enforcement (Flow-side authority minting) | CHECKER_CANDIDATE | future governance packet only | no checker in T5; worker adds a focused package test instead | no hook mutation |
| monitor/database/adapter implementation | outside T5 | NO_PACKAGE_OR_RUNTIME_VALUE | later explicit lane only | keep excluded | no monitor, SOT index, or adapter |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | legacy source family |
| Chain map route | retained SOT3 corpus -> accepted T0-T4 evidence/contracts/runtime -> bounded T5 CVF-native Flow rewrite |
| Matching local-view guard | `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_absorption_blindspot_control_presence.py`; `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | new post-Kernel Flow runtime candidate only |
| Disposition | ADAPT contract-aligned value and REJECT_DIRECT_IMPORT prototype runtime |
| Claim boundary | T5 rewrite only; no monitor, database, adapter, provider/live, public-sync, or production claim |

External absorption core: REQUIRED

## Dependency-Closure Matrix

| Dependency layer | Source evidence | T5 obligation | Disposition |
|---|---|---|---|
| retained README/TREEVIEW (Truth Flow folder) | `.private_reference/legacy/CVF_SOT 10.07/CVF_Truth_Flow_Patch/README.md`, `TREEVIEW.md` | scope only, no direct import | CLOSED_VIA_T0/T0R |
| T1 owner map | `docs/reviews/CVF_SOT3_T1_OWNER_NOVELTY_MAP_2026-07-12.md`, CAP-06/CAP-07 | create new Flow owner; reject embedded Refinery | ACCEPT |
| T2 contracts/invariants/negative cases | `docs/reference/sot_three_layer/CVF_SOT_THREE_LAYER_CONTRACT_CHAIN.md` sections 6-8; invariants file, Invariants 6-9, NC-04A/B, NC-09 through NC-12 | bind every T5 artifact field/status/transition to these exact contracts | ACCEPT |
| T4/T4R1 Kernel runtime/schema/tests | `EXTENSIONS/CVF_TRUTH_KERNEL/src/types/truth-reference.ts`, `src/index.ts`, `src/kernel.ts`, `src/engine/reference-issuer.ts`, `src/engine/revocation.ts`; closure `cda8fec64` | T5 calls the actual `TruthKernel.referenceState(referenceId, nowUtcIso)` before each action and never implements a substitute resolver | ACCEPT |
| proposed T5 artifacts | Planned Artifact Manifest above | package/source/schemas/tests/worker-return, no runtime yet | PLANNED |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind gc018-baseline --batch-id SOT3-T5 --title "Post-Kernel Truth Flow" --date 2026-07-12 --base 1bf21dcee --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | bounded TypeScript package baseline |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | Hand-authored from the GC-018 template directly, following the T4 baseline's proven section shape (T4 passed pre-dispatch 75/75 with the same template). Added T2 Flow contracts, owner split, retained-source rejection, negative matrix, absorption controls, Dependency-Closure Matrix. |
| checkerReadAheadConfirmation | dispatch, structural, absorption, handoff, worker-return, file-size checkers |
| docOnlyNewFields | deterministic local Flow engine interfaces only; Kernel authority uses existing `TruthKernel` and `ReferenceStateResolutionResult` exports from `cda8fec64` |
| claimBoundary | dispatch baseline only; no runtime proof |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defectIds: ADIF-0001, ADIF-0002, ADIF-0006, ADIF-0007,
ADIF-0014, ADIF-0015, ADIF-0016, ADIF-0017, ADIF-0020, ADIF-0021, ADIF-0024.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_absorption_blindspot_control_presence.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_adif_defect_registry_disclosure.py` |
| literalTokensReviewed | DISPATCH_READY; Source Verification Block; External Absorption Core; Overlap And Novelty Classification; Public Export Disposition; Dependency-Closure Matrix |
| gateRunPurpose | confirm source-derived packet fidelity before implementation |
| claimBoundary | gate PASS does not prove Flow correctness |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance implementation tranche; no public-sync authorization.

## Claim Boundary

This baseline authorizes only bounded T5 implementation after pre-dispatch. It
does not authorize T6-T7, vertical slice, monitor, database/SOT-index,
adapter, provider/live, public, Web/UI, or activation work.
