# CVF GC-018 Baseline - SOT3-T4 Truth Kernel Hardening

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-07-12

Baseline ID: GC018-SOT3-T4

## Purpose

Authorize one bounded no-commit implementation tranche for a CVF-owned,
deterministic Truth Kernel that consumes the accepted T2 Kernel request chain,
produces KernelDecision and TruthReceipt, and mints TruthReference only through
the complete eligible-acceptance resolution rule.

## Baseline Decision / Proposed Tranche

Create a new package at `EXTENSIONS/CVF_TRUTH_KERNEL/`. Enrich the existing
truth-foundation doctrine owner without duplicating it. Rewrite runtime and
schemas against T2. Direct import of the retained package is rejected.

## Target / Source

- Main roadmap: `docs/roadmaps/CVF_SOT_THREE_LAYER_ABSORPTION_ROADMAP_2026-07-12.md`.
- Contract authority: `docs/reference/sot_three_layer/CVF_SOT_THREE_LAYER_CONTRACT_CHAIN.md`.
- Negative authority: `docs/reference/sot_three_layer/CVF_SOT_THREE_LAYER_INVARIANTS_AND_NEGATIVE_CASES.md`.
- Doctrine owner: `docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_SOURCE_PROVENANCE_AND_VERIFICATION_CONTRACT.md`.
- Accepted upstream package boundary: `EXTENSIONS/CVF_REFINERY/`.
- Retained evidence: `.private_reference/legacy/CVF_SOT 10.07/CVF_Truth_Kernel_Patch`.

## Scope / Methodology

Build package metadata, strict TypeScript contracts, Draft 2020-12 schemas,
immutable local stores/resolvers, packet-bound evidence and obligation
verification, deterministic decisions, canonical receipt hashing, replay
protection, receipt revocation, and eligible TruthReference issuance. No AI,
agent, prompt, provider, network, database, monitor, adapter, or activation.

## Authorization / Decision

T3 closed at `fea7e2bba`; roadmap release `151812a07` permits T4 packet
authoring. Implementation begins only when this packet passes pre-dispatch.

## Non-Goals

- no Truth Flow or distribution lifecycle;
- no retained strict/relaxed/blocked mode compatibility;
- no runtime monitor, SOT index service, database, external verifier service,
  Guard Contract adapter, phase adapter, or caller-supplied authority boolean;
- no AI, agent, prompt, provider SDK, network, public-sync, or live proof;
- no package activation or production-readiness claim.

## Planned Artifact Manifest

| Output class | Exact root | Required contents |
|---|---|---|
| package | `EXTENSIONS/CVF_TRUTH_KERNEL/` | metadata, tsconfig, README |
| source | `EXTENSIONS/CVF_TRUTH_KERNEL/src/` | contracts, stores/resolvers, evaluator, receipt profile, reference issuer, exports |
| schemas | `EXTENSIONS/CVF_TRUTH_KERNEL/schemas/` | request, decision, receipt, reference, evidence, obligation, verification result |
| tests | `EXTENSIONS/CVF_TRUTH_KERNEL/tests/` | positive path, NC-02 through NC-08 plus NC-04A/04B, determinism, dependency boundary |
| worker return | `docs/reviews/CVF_SOT3_T4_WORKER_RETURN_2026-07-12.md` | exact manifest, proof, no-commit evidence |

## Source Verification Block

| Claimed item | Fact class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| doctrine already has an active owner | EXISTS | `docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_SOURCE_PROVENANCE_AND_VERIFICATION_CONTRACT.md` | Purpose; Scope / Target / Owner Boundary | `cvf.truthFoundation.sourceProvenanceVerification.tkgT1.v1` | truth-foundation reference contract | ACCEPT |
| fresh Kernel runtime owner is absent | EXISTS | `docs/reviews/CVF_SOT3_T1_OWNER_NOVELTY_MAP_2026-07-12.md` | CAP-05 | `NEW_OWNER_CANDIDATE` | T1 owner map | ACCEPT |
| request/decision/receipt/reference field sets and authority are canonical | VALUE_SET | `docs/reference/sot_three_layer/CVF_SOT_THREE_LAYER_CONTRACT_CHAIN.md` | sections 3 through 6 | `KernelEvaluationRequest`; `KernelDecision`; `TruthReceipt`; `TruthReference` | T2 contract chain | ACCEPT |
| canonical receipt profile and test vector exist | LITERAL_INVARIANT | `docs/reference/sot_three_layer/CVF_SOT_THREE_LAYER_CONTRACT_CHAIN.md` | TruthReceipt Receipt Hash Profile | `cvf.sotThreeLayer.receiptHash.v1` | T2 receipt contract | ACCEPT |
| empty evidence/results cannot accept | LITERAL_INVARIANT | `docs/reference/sot_three_layer/CVF_SOT_THREE_LAYER_INVARIANTS_AND_NEGATIVE_CASES.md` | Invariant 4; NC-02; NC-03 | `evidence_refs`; `verification_result_refs` | T2 negative contract | ACCEPT |
| complete decision-resolution chain controls reference issuance | LITERAL_INVARIANT | `docs/reference/sot_three_layer/CVF_SOT_THREE_LAYER_INVARIANTS_AND_NEGATIVE_CASES.md` | Invariant 6; NC-04A; NC-04B | `failed_obligations` | T2 negative contract | ACCEPT |
| retained strict mode passes empty results | RUNTIME_BEHAVIOR | `.private_reference/legacy/CVF_SOT 10.07/CVF_Truth_Kernel_Patch/EXTENSIONS/CVF_TRUTH_KERNEL/src/gates/strict-mode.ts` | `strictAllows` | `strictAllows` | retained prototype | ACCEPT |
| retained receipt is nondeterministic and hashes a different shape | RUNTIME_BEHAVIOR | `.private_reference/legacy/CVF_SOT 10.07/CVF_Truth_Kernel_Patch/EXTENSIONS/CVF_TRUTH_KERNEL/src/receipts/truth-receipt.ts` | `createTruthReceipt` | `new Date`; `chainHash` | retained prototype | ACCEPT |
| T3 Refinery is the accepted packet producer | EXISTS | `docs/reviews/CVF_SOT3_T3_COMPLETION_REVIEW_2026-07-12.md` | Machine Closure Package | `REFINERY_CORE_ACCEPTED_BOUNDED` | T3 completion review | ACCEPT |

## Required Invariants

1. Kernel accepts only a hash-matching READY_FOR_KERNEL RefineryPacket request.
2. Empty evidence or empty Kernel-produced verification results never accepts.
3. Evidence and obligations resolve to the same packet/source lineage.
4. Policy and rule versions equal the versions Kernel actually applies.
5. Decision, request, receipt, and reference records are immutable snapshots.
6. Every decision outcome receives a receipt; only an eligible accepting
   receipt can mint a TruthReference.
7. Receipt hashing reproduces the published 522-byte SHA-256 test vector and
   binds all authority-bearing fields under the canonical profile.
8. Receipt replay is rejected; supersession needs a new receipt identity and
   predecessor hash.
9. Reference issuance resolves receipt -> decision -> request and fails closed
   on missing records, mismatched bindings/versions/content, failed
   obligations, blocking verification, revoked receipt, or invalid dates.
10. No caller-supplied verification result, approval flag, or authority boolean
    can substitute for Kernel-owned evaluation.
11. No AI, agent, prompt, provider, network, monitor, or adapter dependency.

## Fail Conditions

Any empty-input accept, cross-packet evidence, stale/mismatched version,
partial receipt hash, replay, non-acceptance reference issuance, unresolved
record link, warning/blocking verification release, invalid UTC interval,
nondeterministic clock/ID, forbidden dependency, or out-of-scope path blocks closure.

## Verification / Evidence

Typecheck, build, focused negative tests, published receipt-vector equality,
repeated-run byte equality, dependency/forbidden scans, exact status/diff,
worker-return fast gate, file-size guard, and unchanged worker HEAD.

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | current `EXTENSIONS/`, T1 owner map, T2 contracts, truth-foundation owner, retained strict gate and receipt sources |
| Runtime behavior claimed | TARGET_ABSENT_AT_DISPATCH: no current CVF-owned `EXTENSIONS/CVF_TRUTH_KERNEL/` package exists |
| Helper/checker implementation claimed | N/A_WITH_REASON: no governance checker or hook mutation |
| Provider/live proof claimed | N/A_WITH_REASON: deterministic local package only |
| Public-sync claimed | N/A_WITH_REASON: private provenance packet only |
| Freshness disposition | PASS - current owner/runtime boundaries rechecked on 2026-07-12 |

## External Repository Absorption Entry Control

| Field | Value |
|---|---|
| Source type | retained legacy three-folder source family narrowed to Kernel evidence |
| Upstream or source-mirror disposition | LEGACY_REFERENCE_ONLY_WITH_REASON: operator-authored retained patch without verified upstream identity |
| Enumeration or manifest plan | reuse accepted T0 305-record manifest and enumerate retained Kernel folder with filesystem-backed command |
| Per-file terminal-ledger plan | T4 converts selected Kernel runtime value; T7 retains final 305-file reconciliation |
| Owner or overlap route | enrich truth-foundation doctrine; create only the absent Kernel runtime owner |
| Value-disposition route | ADAPT concepts; REJECT_DIRECT_IMPORT retained runtime and adapters |
| Claim boundary | bounded Kernel rewrite only; no full-corpus closure, Flow, provider, public, or activation claim |

## Mandatory Blind-Spot Control Block

- Source enumeration gate: reuse accepted T0 manifest and re-read every cited retained Kernel source.
- Owner-surface gate: T1 CAP-04/CAP-05 separates doctrine enrichment from new runtime ownership.
- Overlap gate: classify all retained value through the matrices below.
- Runtime/package gate: only the new local Kernel package is in scope; monitor,
  adapters, database, Flow, provider/live, and activation remain forbidden.
- Verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS.

## Corpus Completeness And Report Integrity

- Corpus task class: bounded T4 implementation from accepted SOT3 corpus.
- Corpus root: `.private_reference/legacy/CVF_SOT 10.07/CVF_Truth_Kernel_Patch`.
- Snapshot time: 2026-07-12 local dispatch session.
- Enumeration command: `rg --files --hidden --no-ignore ".private_reference/legacy/CVF_SOT 10.07/CVF_Truth_Kernel_Patch"`.
- Manifest artifact or inline manifest: accepted `docs/evidence/sot/sot3-t0-source-manifest.json`.
- Manifest hash: retained from accepted T0 evidence; no new whole-corpus claim.
- Processing ledger artifact or inline ledger: overlap and conversion matrices in this baseline.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE
- Reconciliation: manifest=305; ledger_terminal=0; exclusions=305; unresolved=0. Final corpus reconciliation remains T7-owned.
- Unresolved files: 0 within selected T4 source facts.
- Declared exclusions: monitors, databases, adapters, Flow, generated/vendor files, AI/provider surfaces.
- Unreadable or unsupported files: none known at dispatch.
- Aggregation check: T4 proves one bounded runtime owner, not full three-folder closure.
- Drift check: worker reopens all cited authority and retained sources.
- Output traceability: every adapted concept maps to package output or explicit rejection.
- Adversarial verification: empty arrays, cross-packet refs, replay, version/hash mismatch, and broken resolution are tested.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS - T4 is limited to the Kernel capability subset.

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | retained Kernel folder plus accepted T1-T3 CVF authority |
| Enumeration command | `rg --files --hidden --no-ignore ".private_reference/legacy/CVF_SOT 10.07/CVF_Truth_Kernel_Patch"` |
| Manifest artifact or inline manifest | `docs/evidence/sot/sot3-t0-source-manifest.json` plus Planned Artifact Manifest table in this baseline |
| Processing ledger artifact or inline ledger | Overlap And Novelty Classification and External Absorption Value Conversion Matrix tables in this baseline; worker return adds implementation ledger |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | truth-foundation doctrine owner plus new `EXTENSIONS/CVF_TRUTH_KERNEL/` candidate |
| Unresolved items | zero T4 dispatch blockers; T7 retains corpus closure |
| Completion claim boundary | bounded T4 Kernel package only |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| source/provenance/evidence/obligation doctrine | `docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_SOURCE_PROVENANCE_AND_VERIFICATION_CONTRACT.md` | ENRICH_EXISTING | T2 adds concrete runtime bindings and receipt/reference contracts | Implement without duplicating doctrine. |
| Kernel request/decision/receipt/reference runtime | OWNER_SURFACE_NOT_FOUND | OWNER_SURFACE_NOT_FOUND | no current general runtime owner | Create bounded package. |
| retained strict gate and receipt code | OWNER_SURFACE_NOT_FOUND | REJECT_DIRECT_IMPORT | empty arrays pass, clock is global, receipt/profile differs | Rewrite and add negative tests. |
| retained verifier/registry concepts | `docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_SOURCE_PROVENANCE_AND_VERIFICATION_CONTRACT.md` | NEW_FINDING | useful deterministic concepts require packet-bound CVF rewrite | Adapt only contract-aligned concepts. |
| monitors, adapters, database/SOT-index service | OWNER_SURFACE_NOT_FOUND | NO_NEW_VALUE | outside bounded T4 value | Exclude and retain separate authorization boundary. |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| truth-foundation doctrine | provenance/evidence/obligation/verification minimums | DOCTRINE_ADAPTED | existing truth-foundation owner and T4 package contracts | implement exact T2 runtime bindings | no duplicate doctrine owner |
| independent Kernel identity | exclusive decision/receipt/reference producer | PACKAGE_CANDIDATE | `EXTENSIONS/CVF_TRUTH_KERNEL/` | create package subject to review | no activation |
| evaluation and issuance engine | deterministic packet-bound trust evaluation | RUNTIME_CANDIDATE | new package source | implement bounded local runtime | no provider/network/database |
| future static overclaim checks | possible repeated-defect enforcement | CHECKER_CANDIDATE | future governance packet only | no checker in T4 | no hook mutation |
| retained strict gate/receipt/adapters | fail-open or incompatible implementation | REJECT_DIRECT_IMPORT | CVF-native rewrite only | reject direct copy | no compatibility layer |
| monitor/database/Flow implementation | outside T4 | NO_PACKAGE_OR_RUNTIME_VALUE | later explicit lane only | keep excluded | no monitor, SOT index, or Flow |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | legacy source family |
| Chain map route | retained SOT3 corpus -> accepted T0-T3 evidence/contracts -> bounded T4 CVF-native Kernel rewrite |
| Matching local-view guard | `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_absorption_blindspot_control_presence.py`; `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | existing truth-foundation doctrine plus new Kernel runtime candidate |
| Disposition | ADAPT contract-aligned value and REJECT_DIRECT_IMPORT prototype runtime |
| Claim boundary | T4 rewrite only; no Flow, provider/live, public-sync, or production claim |

External absorption core: REQUIRED

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind gc018-baseline --batch-id SOT3-T4 --title "Truth Kernel Hardening" --date 2026-07-12 --base bbae4a92b --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | bounded TypeScript package baseline |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | Added T2 Kernel contracts, owner split, retained-source rejection, negative matrix, absorption controls. |
| checkerReadAheadConfirmation | dispatch, structural, absorption, handoff, worker-return, file-size checkers |
| docOnlyNewFields | deterministic local resolver/store interfaces |
| claimBoundary | dispatch baseline only; no runtime proof |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defectIds: ADIF-0001, ADIF-0002, ADIF-0006, ADIF-0007,
ADIF-0014, ADIF-0015, ADIF-0016, ADIF-0017, ADIF-0020, ADIF-0021, ADIF-0024.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_absorption_blindspot_control_presence.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | DISPATCH_READY; Source Verification Block; External Absorption Core; Overlap And Novelty Classification; Public Export Disposition |
| gateRunPurpose | confirm source-derived packet fidelity before implementation |
| claimBoundary | gate PASS does not prove Kernel correctness |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance implementation tranche; no public-sync authorization.

## Claim Boundary

This baseline authorizes only bounded T4 implementation after pre-dispatch. It
does not authorize Flow, vertical slice, provider/live, public, or activation work.
