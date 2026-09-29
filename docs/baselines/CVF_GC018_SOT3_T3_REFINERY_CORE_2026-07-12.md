# CVF GC-018 Baseline - SOT3-T3 Deterministic Refinery Core

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-07-12

Baseline ID: GC018-SOT3-T3

## Purpose

Authorize one bounded no-commit implementation tranche for an independent,
deterministic, no-AI CVF Refinery Core that consumes the accepted T2
`SourceEnvelope` contract and emits the accepted T2 `RefineryPacket` contract.

## Baseline Decision / Proposed Tranche

Create a new CVF-owned package at `EXTENSIONS/CVF_REFINERY/`. Adapt useful
deterministic concepts from the retained Refinery source, but rewrite the
pipeline and contracts against accepted T2 authority. Direct import is rejected.

## Target / Source

- Main roadmap: `docs/roadmaps/CVF_SOT_THREE_LAYER_ABSORPTION_ROADMAP_2026-07-12.md`.
- Contract authority: `docs/reference/sot_three_layer/CVF_SOT_THREE_LAYER_CONTRACT_CHAIN.md`.
- Negative cases: `docs/reference/sot_three_layer/CVF_SOT_THREE_LAYER_INVARIANTS_AND_NEGATIVE_CASES.md`.
- Retained input: `.private_reference/legacy/CVF_SOT 10.07/CVF_Refinery_Patch`.

## Scope / Methodology

Build package metadata, strict TypeScript types, deterministic pipeline,
normalization, schema validation, duplicate grouping, conflict detection,
quality/integrity results, transformation lineage, packet construction, and
focused fail-closed tests. No provider, AI, agent, prompt, or network dependency.

## Authorization / Decision

Operator explicitly instructed continuation of the three-folder absorption.
T0-T2 are accepted; roadmap commit `c897094d8` releases T3 packet authoring.
Implementation begins only after this packet passes pre-dispatch.

## Non-Goals

- no Truth Kernel or Truth Flow implementation;
- no direct retained-code copy or package activation outside the new package;
- no AI, agent, prompt, provider SDK, network, OCR, extraction, or semantic similarity;
- no public-sync, Web/UI, live proof, or production-readiness claim;
- no automatic authoritative-value selection from conflicts.

## Planned Artifact Manifest

| Output class | Exact root | Required contents |
|---|---|---|
| package | `EXTENSIONS/CVF_REFINERY/` | package metadata, tsconfig, README |
| source | `EXTENSIONS/CVF_REFINERY/src/` | contracts, pipeline, deterministic primitives, index |
| schemas | `EXTENSIONS/CVF_REFINERY/schemas/` | SourceEnvelope and RefineryPacket validation surfaces |
| tests | `EXTENSIONS/CVF_REFINERY/tests/` | positive, negative, determinism, no-AI proof |
| worker return | `docs/reviews/CVF_SOT3_T3_WORKER_RETURN_2026-07-12.md` | exact manifest, tests, no-commit evidence |

## Source Verification Block

| Claimed item | Fact class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| no current package owner exists | EXISTS | `docs/reviews/CVF_SOT3_T1_OWNER_NOVELTY_MAP_2026-07-12.md` | CAP-02/CAP-03 | `OWNER_SURFACE_NOT_FOUND` | T1 owner map | ACCEPT |
| RefineryPacket status vocabulary | VALUE_SET | `docs/reference/sot_three_layer/CVF_SOT_THREE_LAYER_CONTRACT_CHAIN.md` | RefineryPacket | `status`; `failure_tokens` | T2 contract chain | ACCEPT |
| zero-stage run blocks | LITERAL_INVARIANT | `docs/reference/sot_three_layer/CVF_SOT_THREE_LAYER_INVARIANTS_AND_NEGATIVE_CASES.md` | Invariant 3; NC-01 | `REFINERY_NO_STAGES_EXECUTED` | T2 negative-case contract | ACCEPT |
| retained engine defaults to empty stages | RUNTIME_BEHAVIOR | `.private_reference/legacy/CVF_SOT 10.07/CVF_Refinery_Patch/EXTENSIONS/CVF_REFINERY/src/pipeline/refinery-engine.ts` | `RefineryEngine.run` | `input.stages ?? []` | retained prototype | ACCEPT |
| retained package uses random UUID tooling | RUNTIME_BEHAVIOR | `.private_reference/legacy/CVF_SOT 10.07/CVF_Refinery_Patch/scripts/refinery/run_refinery.ts` | imports and packet construction | `randomUUID` | retained script | ACCEPT |
| target root is absent | EXISTS | `docs/reference/system_chain/gaps/entries/sot3_independent_refinery_owner_unresolved.json` | targetOwner | `NONE_WITH_REASON` | accepted GAP source | ACCEPT |

## Required Invariants

1. At least one configured stage must execute; zero stages yields `BLOCKED` and
   `REFINERY_NO_STAGES_EXECUTED`.
2. IDs and timestamps come from injected deterministic dependencies.
3. Input objects are not mutated.
4. Unknown values remain unknown; normalization never invents data.
5. Duplicate grouping is non-destructive and scope-aware.
6. Unresolved conflicts never select an authoritative value.
7. Required integrity and lineage evidence cannot be empty for
   `READY_FOR_KERNEL`.
8. Non-empty failure tokens require `REVIEW_REQUIRED` or `BLOCKED`.
9. Refinery output never contains a truth/approval/canonical claim.
10. Package dependency graph contains no AI, agent, prompt, provider, or network dependency.

## Fail Conditions

Any direct import, default empty pipeline, nondeterministic global clock/UUID,
truth claim, conflict auto-resolution, missing required lineage/integrity,
forbidden dependency, failing negative test, or out-of-scope path blocks closure.

## Verification / Evidence

Typecheck, build, focused tests, repeated-run byte equality, dependency scan,
forbidden-token scan, exact status/diff, worker-return fast gate, and no commit.

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | `EXTENSIONS/CVF_REFINERY/`; `docs/reviews/CVF_SOT3_T1_OWNER_NOVELTY_MAP_2026-07-12.md`; `docs/reference/system_chain/gaps/entries/sot3_independent_refinery_owner_unresolved.json`; retained engine and script cited in Source Verification |
| Runtime behavior claimed | TARGET_ABSENT_AT_DISPATCH: repository path/status checks confirm no current CVF-owned `EXTENSIONS/CVF_REFINERY/` package; this packet proposes its bounded creation |
| Helper/checker implementation claimed | N/A_WITH_REASON: no governance helper, checker, or hook implementation is authorized |
| Provider/live proof claimed | N/A_WITH_REASON: deterministic local package only |
| Public-sync claimed | N/A_WITH_REASON: private provenance packet only |
| Freshness disposition | PASS - target absence and retained prototype behavior were rechecked on 2026-07-12; implementation proof remains worker/reviewer-owned |

## External Repository Absorption Entry Control

| Field | Value |
|---|---|
| Source type | retained legacy three-folder source family, narrowed in T3 to the Refinery folder and accepted T0-T2 evidence |
| Upstream or source-mirror disposition | LEGACY_REFERENCE_ONLY_WITH_REASON: operator-authored retained patch without verified upstream identity; no clone or mirror is required |
| Enumeration or manifest plan | reuse `docs/evidence/sot/sot3-t0-source-manifest.json` and the accepted 305-record T0 processing evidence; T3 re-reads only selected Refinery sources cited by the packet |
| Per-file terminal-ledger plan | no new corpus-wide terminal reclassification in T3; T7 owns final 305-file reconciliation |
| Owner or overlap route | use accepted T1 owner/novelty map and T2 contracts; create only the independent Refinery package candidate |
| Value-disposition route | ADAPT deterministic concepts; REJECT direct prototype runtime, nondeterministic IDs, and AI/provider surfaces |
| Claim boundary | bounded T3 CVF-native rewrite only; no whole-corpus closure, direct import, Kernel, Flow, provider/live, or public claim |

## Mandatory Blind-Spot Control Block

- Source enumeration gate: reuse the accepted 305-record T0 manifest and re-read
  every retained Refinery source named by the T3 packet before implementation.
- Owner-surface gate: compare the implementation target against the accepted T1
  owner/novelty map and current T2 owner surfaces before creating files.
- Overlap gate: classify retained value as CONFIRMED_EXISTING, ENRICH_EXISTING,
  OWNER_SURFACE_NOT_FOUND, NEW_FINDING, REJECT_DIRECT_IMPORT, or NO_NEW_VALUE.
- Runtime/package gate: only the new deterministic Refinery package is in scope;
  Kernel, Flow, package activation, AI, agent, prompt, provider, network,
  public-sync, Web, and production claims remain forbidden.
- Verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS.

## Corpus Completeness And Report Integrity

- Corpus task class: bounded implementation from a previously accepted retained
  three-folder absorption corpus.
- Corpus root: `.private_reference/legacy/CVF_SOT 10.07/`.
- Snapshot time: 2026-07-12 local dispatch session.
- Enumeration command: `rg --files --hidden --no-ignore ".private_reference/legacy/CVF_SOT 10.07/CVF_Refinery_Patch"`; reconcile selected paths against `docs/evidence/sot/sot3-t0-source-manifest.json`.
- Manifest artifact or inline manifest: accepted 305-record SOT3-T0 manifest.
- Manifest hash: retained from accepted T0 evidence; no new whole-corpus hash claim.
- Processing ledger artifact or inline ledger: accepted T0/T0R evidence plus the
  T3 value-conversion and overlap tables below.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE
- Reconciliation: manifest=305; ledger_terminal=0; exclusions=305; unresolved=0. T3 does not reopen corpus-wide terminal classification because final per-file reconciliation remains T7-owned.
- Unresolved files: 0 within the bounded T3 selected source facts.
- Declared exclusions: Truth Kernel, Truth Flow, retained AI/provider/runtime
  adapters, generated dependencies, and all files not needed for the T3 rewrite.
- Unreadable or unsupported files: none known at dispatch.
- Aggregation check: T3 proves one bounded Refinery owner implementation, not
  complete absorption of all three folders.
- Drift check: worker reopens every cited retained and canonical source at start.
- Output traceability: every adapted value maps to the new package or an explicit
  rejection/exclusion row.
- Adversarial verification: worker must prove that empty stages, random IDs,
  conflict auto-selection, and truth claims cannot pass.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS - accepted T0 manifest is
  reused; T3 is intentionally limited to the Refinery capability subset.

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | `.private_reference/legacy/CVF_SOT 10.07/CVF_Refinery_Patch` plus accepted T1/T2 CVF authority |
| Enumeration command | read the accepted `docs/evidence/sot/sot3-t0-source-manifest.json`, then enumerate and re-read selected Refinery sources with `rg --files --hidden --no-ignore` and `Get-Content -LiteralPath` |
| Manifest artifact or inline manifest | accepted `docs/evidence/sot/sot3-t0-source-manifest.json`; planned T3 package manifest in worker return |
| Processing ledger artifact or inline ledger | accepted T0/T0R processing evidence plus the overlap and value-conversion matrices in this baseline |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | `docs/reviews/CVF_SOT3_T1_OWNER_NOVELTY_MAP_2026-07-12.md`; new candidate `EXTENSIONS/CVF_REFINERY/` |
| Unresolved items | zero dispatch-blocking T3 owner/source items; T7 retains final corpus reconciliation |
| Completion claim boundary | bounded T3 deterministic package only; no whole-corpus, Kernel, Flow, direct import, provider/live, public, or production claim |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| Three-layer boundary and RefineryPacket contract | `docs/reference/sot_three_layer/` | CONFIRMED_EXISTING | T2 already owns canonical field, status, and failure semantics | Implement against T2 without duplicating doctrine. |
| Independent deterministic Refinery runtime owner | `docs/reviews/CVF_SOT3_T1_OWNER_NOVELTY_MAP_2026-07-12.md` | OWNER_SURFACE_NOT_FOUND | CVF has no current package owner | Create only `EXTENSIONS/CVF_REFINERY/`. |
| Deterministic normalization, duplicate, conflict, integrity, and lineage primitives | OWNER_SURFACE_NOT_FOUND | NEW_FINDING | useful implementation concepts need a CVF-native strict rewrite | Adapt concepts with injected clock/ID and fail-closed tests. |
| Empty-stage prototype and random UUID construction | OWNER_SURFACE_NOT_FOUND | REJECT_DIRECT_IMPORT | prototype can fail open or become nondeterministic | Reject behavior and add negative/determinism tests. |
| AI, agent, prompt, provider, OCR, extraction, and network surfaces | OWNER_SURFACE_NOT_FOUND | NO_NEW_VALUE | outside the operator-defined deterministic Refinery boundary | Exclude from package and dependency graph. |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| Retained deterministic pipeline concepts | staged normalization, schema, duplicate, conflict, quality, integrity, lineage, and packet construction | DOCTRINE_ADAPTED | `EXTENSIONS/CVF_REFINERY/` | Rewrite against accepted T2 contracts and prove the negative matrix. | New T3 package only. |
| Accepted T2 SourceEnvelope and RefineryPacket semantics | canonical input/output and fail-closed lifecycle | DOCTRINE_ADAPTED | `docs/reference/sot_three_layer/` and T3 package types | Implement exact compatibility; do not redefine authority. | No Kernel or Flow implementation. |
| Retained empty-stage default | omission can execute zero stages | REJECT_DIRECT_IMPORT | T3 engine and NC-01 tests | Required default pipeline plus explicit zero-stage block. | No fail-open compatibility mode. |
| Retained random UUID construction | nondeterministic packet identity | REJECT_DIRECT_IMPORT | injected deterministic dependency interface | Require injected clock and ID factory. | No global clock or random UUID. |
| Retained AI/provider/agent adapters | implementation outside deterministic input cleaning | NO_PACKAGE_OR_RUNTIME_VALUE | explicit package exclusions and dependency scan | Do not copy, install, or expose. | No AI, agent, prompt, provider, or network dependency. |
| Independent Refinery package identity | bounded reusable package owner for the accepted T3 capability | PACKAGE_CANDIDATE | `EXTENSIONS/CVF_REFINERY/` | Create package metadata and exports, subject to reviewer acceptance. | No registry activation or cross-package integration. |
| Future contract-drift or forbidden-dependency guard | possible repeated-defect prevention after implementation evidence exists | CHECKER_CANDIDATE | future `governance/compat/` packet only | Record no checker implementation in T3; require a fresh source-verified work order if repeated defects justify it. | No checker or hook mutation. |
| Future Kernel/Flow integration | downstream use of accepted packet | RUNTIME_CANDIDATE | roadmap T4-T6 only after T3 acceptance | Keep dependency-held. | Not authorized by T3. |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | legacy source family |
| Chain map route | retained SOT3 corpus -> accepted T0/T0R manifest and semantics -> accepted T1 owner map -> accepted T2 contracts -> bounded T3 CVF-native Refinery rewrite |
| Matching local-view guard | `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_absorption_blindspot_control_presence.py`; `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | new `EXTENSIONS/CVF_REFINERY/` package candidate governed by accepted T2 contracts |
| Disposition | ADAPT deterministic Refinery value and REJECT_DIRECT_IMPORT retained prototype behavior |
| Claim boundary | selective T3 rewrite only; no direct import, whole-corpus closure, Kernel, Flow, provider/live, public-sync, or production claim |

External absorption core: REQUIRED

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind gc018-baseline --batch-id SOT3-T3 --title "Deterministic Refinery Core" --date 2026-07-12 --base 5510412e8 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | bounded TypeScript package baseline |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | Added retained-source verification, T2 invariants, package manifest, deterministic and no-AI controls. |
| checkerReadAheadConfirmation | structural, dispatch-quality, core-guard, external-intake, worker-return and file-size checkers |
| docOnlyNewFields | deterministic dependency injection boundary |
| claimBoundary | dispatch baseline only; no package implementation proof |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defectIds: ADIF-0001, ADIF-0002, ADIF-0007, ADIF-0014, ADIF-0015,
ADIF-0016, ADIF-0017, ADIF-0020, ADIF-0021, ADIF-0024.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | DISPATCH_READY; Source Verification Block; Planned Artifact Manifest; Public Export Disposition |
| gateRunPurpose | confirm source-derived packet fidelity before implementation |
| claimBoundary | gate PASS does not prove Refinery correctness |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance implementation tranche; no public-sync authorization.

## Claim Boundary

This baseline authorizes only the bounded T3 package after pre-dispatch. It
does not authorize Kernel, Flow, vertical-slice, provider/live, or public work.
