# CVF Source Of Truth Three-Layer Absorption Roadmap

Memory class: FULL_RECORD

Status: PROPOSED_T1_OWNER_RECONCILIATION_DISPATCH

docType: roadmap

Date: 2026-07-12

Roadmap ID: SOT3

Operator intent: assess and selectively absorb the retained three-layer Source
of Truth design into CVF without direct import or a one-hundred-percent
absorption claim.

## Purpose

Turn the retained `CVF_SOT 10.07` source family into a governed, selective,
CVF-native three-layer architecture:

1. CVF Refinery prepares source-bound data without creating truth.
2. CVF Truth Kernel evaluates what may be treated as trusted.
3. CVF Truth Flow distributes verified references through a governed lifecycle.

The first action is an independent external review of the complete three-folder
corpus and this roadmap. No implementation tranche may start from the current
prototype code.

## Target / Source

Retained private source roots:

- `.private_reference/legacy/CVF_SOT 10.07/CVF_Refinery_Patch`
- `.private_reference/legacy/CVF_SOT 10.07/CVF_Truth_Kernel_Patch`
- `.private_reference/legacy/CVF_SOT 10.07/CVF_Truth_Flow_Patch`

Current deterministic snapshot:

| Layer | Files | Directories | Bytes | Aggregate manifest SHA-256 |
|---|---:|---:|---:|---|
| Refinery | 133 | 44 | 160461 | `c7ace9ccbb470514bb9fea97527976a462146b5b220df88eadc6fdc38b88cbe2` |
| Truth Kernel | 93 | 39 | 78007 | `73e4cc652f738d70428326a013de08fc65ce4edb553dcd3e4670eb8a46765497` |
| Truth Flow | 79 | 17 | 78380 | `e7be38e77889f6280248fc4a6ceacf354a41c8f1c331fbb2a491e29f8a27858f` |
| Total | 305 | N/A with reason: nested directories overlap only within their own roots | 316848 | N/A with reason: each root retains a separate digest |

The retained folders are reference input, not CVF authority and not runtime
dependencies.

## Scope / Methodology

The roadmap uses five evidence stages:

1. deterministic source enumeration and body-read accounting;
2. independent architecture critique;
3. cross-layer contract reconciliation;
4. CVF owner and novelty reconciliation;
5. bounded implementation only after fresh tranche authorization.

Every source item must receive an `ABSORB`, `ADAPT`, `DEFER`, `REJECT`,
`BLOCK`, or `NO_NEW_VALUE` disposition before final closeout.

## Findings / Position

Initial dispatcher position for independent challenge:

`THREE_LAYER_MODEL_CONFIRMED_WITH_ROLE_SPLIT_AND_CONTRACT_REWRITE`

```text
Raw or extracted record
        |
        v
SourceEnvelope
        |
        v
CVF Refinery Core
        |
        v
RefineryPacket - unverified candidate material
        |
        v
CVF Truth Kernel
        |
        v
Kernel evaluation output and receipt reference
(semantic trust requires separate source-backed authorization)
        |
        v
CVF Truth Flow
        |
        v
Scoped distribution to application, human, workflow, agent, or tool
```

CVF Core governs policy, identity, permission, risk, review, freeze, audit, and
execution boundaries around all three layers.

## Layer Boundary Decisions To Validate

| Layer | Proposed ownership | Must not own | Initial disposition |
|---|---|---|---|
| Refinery | source envelope, normalization, schema validation, duplicate grouping, conflict detection, quality, integrity, lineage, RefineryPacket | truth approval, AI inference, agent behavior, prompt logic, provider integration, final routing | independent deterministic module candidate |
| Truth Kernel | evidence admission, obligation evaluation, provenance, verification, authority decision, receipt, truth reference | raw-source cleanup, recipient routing, execution approval | contract-first rewrite candidate |
| Truth Flow | register, route, information dose, distribute, consume, observe, feedback proposal, recall, retire | duplicate Refinery implementation, truth creation, direct trust-state mutation, execution approval | post-Kernel lifecycle module candidate |

The external review must attempt to disprove or narrow these proposed
boundaries rather than merely restating them.

## Cross-Layer Contract Plan

The stack requires one canonical contract chain:

| Contract | Producer | Consumer | Required boundary |
|---|---|---|---|
| `SourceEnvelope` | governed intake adapter | Refinery | source identity exists before normalization and remains in lineage |
| `RefineryPacket` | Refinery | Truth Kernel | structurally eligible is not trusted or canonical |
| `KernelEvaluationRequest` | Kernel adapter | Truth Kernel | binds complete packet content and requested verification mode |
| `KernelDecision` and `TruthReceipt` | Truth Kernel | Truth Flow and CVF guards | fail-closed, packet-bound, issuer-bound, replay-aware |
| `TruthReference` | Truth Kernel | Truth Flow | scoped, versioned, time-bounded, supersession-aware |
| `DistributionRequest` and `DistributionPackage` | Truth Flow | governed consumer | receipt-bound, route-bound, dose-bound, TTL-bound |
| `FeedbackProposal` | Truth Flow | human or governed owner | proposal only; no silent truth or source-score rewrite |

Contract names are roadmap design labels. They are not claims that matching
runtime symbols already exist in current CVF.

## Refinery No-AI Core Invariant

The proposed Refinery Core is a pure deterministic module:

```text
Raw
-> Source Envelope
-> Normalize
-> Schema
-> Duplicate
-> Conflict
-> Quality and Integrity
-> Evidence Candidate
-> RefineryPacket
```

It contains no AI, agent, prompt, provider SDK, network dependency, or authority
decision. OCR, extraction, semantic classification, and AI similarity may be
upstream adapters only. Their output must enter through `SourceEnvelope` and
remain untrusted.

## Known Prototype Gaps Requiring Independent Review

| Area | Source-backed initial observation | Review question |
|---|---|---|
| Refinery engine | default stage input can be an empty array | can the default run emit a misleading ready packet without the intended pipeline? |
| Refinery normalization | date and unit helpers exist but are not fully bound to the default engine | which functions are reusable and which need replacement? |
| Determinism | generated IDs and timestamps vary | what injected clock and identifier contract is required? |
| Conflict and duplicate semantics | missing fields, wildcard scopes, invalid dates, and group-level overlap can misclassify candidates | what fail-closed semantics should control grouping? |
| Kernel receipt | empty result arrays can reach a non-fail status and receipt binding is incomplete | what minimum evidence and content binding are mandatory? |
| Kernel schema | truth packet allows extra properties | should the shared packet boundary be closed or explicitly extensible? |
| Flow topology | documentation alternates between a post-Kernel layer and an orchestrator placed before Kernel | should Flow be a facade, a post-Kernel module, or two separately named surfaces? |
| Flow embedded refinery | Flow defines a second incompatible RefineryPacket | what code and schema must be removed or relocated? |
| Flow lifecycle | caller-controlled transitions can promote to VERIFIED without receipt proof | what state transition evidence is mandatory? |
| Flow publish gate | booleans and a string receipt ID are trusted without receipt verification | what binding belongs in Flow versus CVF guards? |

## Non-Goals

- no direct import of retained TypeScript, schemas, rules, guards, or scripts;
- no one-hundred-percent absorption target;
- no implementation during SOT3-T0;
- no AI, agent, prompt, or provider capability inside Refinery Core;
- no provider/live proof during architecture review;
- no current CVF runtime, checker, package, registry, or generated-state mutation;
- no public-sync, release, or production-readiness claim;
- no external reviewer authority over CVF semantics.

## Authorization / Decision

SOT3-T0R is reviewer-accepted at material commit `ae7d53385`. Authorization is
now limited to SOT3-T1 owner and novelty reconciliation planning/dispatch.
SOT3-T2 through SOT3-T7 remain proposal rows and require fresh authorization.
Current decision: map every accepted capability group to an existing owner,
explicit new-owner candidate, defer, or rejection before contract work.

## Design Control Gate

| Control | Requirement | Dispatch state |
|---|---|---|
| Scope boundary | all three retained folders, complete file accounting, architecture critique only | PASS |
| Non-goals | direct import, implementation, provider/live, public, and readiness claims forbidden | PASS |
| Lane split | external review precedes contract ratification and implementation | PASS |
| Source verification | work order cites current paths, sections, symbols, and snapshot evidence | REQUIRED |
| Claim boundary | external output remains advisory | PASS |
| Acceptance criteria | source accounting, cross-layer map, contradictions, and dispositions observable | PASS |
| Verification evidence | manifest arithmetic, body-read ledger, review report, and no-commit evidence | REQUIRED |
| Dispatch readiness | paired GC-018 and source-verified work order must pass pre-dispatch | HOLD_PENDING_GATES |

## Tranche Plan

| Tranche | Objective | Required output | Release condition |
|---|---|---|---|
| SOT3-T0 | independent full-corpus architecture review | external-review packet, 305-file manifest/ledger, cross-layer critique, advisory return | exact corpus reconciliation and reviewer return without implementation |
| SOT3-T0R | recover advisory evidence into a clear pre-implementation architecture decision recommendation | semantic reconciliation matrix, explicit three-layer decision recommendation, no-commit worker return | every disputed boundary decided or visibly blocked; implementation remains unauthorized |
| SOT3-T1 | CVF owner and novelty reconciliation | owner map and absorb/adapt/defer/reject ledger | every capability group has an owner or explicit owner decision |
| SOT3-T2 | canonical inter-layer contracts | SourceEnvelope, RefineryPacket, Kernel evaluation/receipt, TruthReference, distribution and feedback specifications | no duplicate packet or lifecycle authority |
| SOT3-T3 | independent Refinery Core | deterministic package, schemas, tests, fixtures, no-AI dependency proof | default pipeline cannot bypass required stages and negative tests fail closed |
| SOT3-T4 | Truth Kernel hardening | packet-bound verification, obligation, provenance, receipt, release, and freshness contracts | empty, cross-packet, warning-release, replay, and invalid-date cases fail closed |
| SOT3-T5 | post-Kernel Truth Flow | routing, dose, distribution, consumption, feedback proposal, recall and retirement | no embedded Refinery or direct VERIFIED transition without Kernel proof |
| SOT3-T6 | three-layer vertical slice | internal, project, and market-source scenario across all contracts | end-to-end evidence preserves source, scope, conflict, receipt, route, and lifecycle |
| SOT3-T7 | semantic value audit and closeout | complete conversion ledger and parked-value index reconciliation | all 305 source items terminal and unresolved value equals zero |

SOT3-T1 through SOT3-T7 remain unauthorized implementation or mutation lanes
until their own fresh GC-018 baseline and work order exist.

## Work Plan

1. Release the SOT3-T0 packet from a clean governed dispatch commit.
2. Receive complete manifest, ledger, and advisory external return.
3. Classify atomic returned observations through the external-finding workflow.
4. Decide whether SOT3-T1 owner reconciliation should proceed.
5. Keep every implementation tranche on HOLD until its own authorization.

## Acceptance Criteria

- AC-01: all 305 retained files are deterministically accounted for.
- AC-02: README and TREEVIEW surfaces are reviewed before implementation files.
- AC-03: the absence of a root Truth Kernel TREEVIEW is recorded as an entry-surface gap, not an unread-file excuse.
- AC-04: every cross-layer packet mismatch is listed with both source surfaces.
- AC-05: Refinery Core no-AI invariant is accepted, revised, or rejected with evidence.
- AC-06: Flow orchestrator-versus-post-Kernel ambiguity receives a recommended resolution.
- AC-07: direct import remains rejected.
- AC-08: implementation tranches remain gated behind fresh authorization.
- AC-09: external output is classified through the CVF external-finding absorption workflow.
- AC-10: final closeout has no unresolved source item or hidden value-bearing deferment.

## Verification / Evidence

- root-specific file counts, byte totals, and aggregate digests;
- one manifest record and one processing-ledger row per source file;
- source-backed cross-layer mismatch matrix;
- explicit external dissent and strongest alternative architecture;
- current CVF owner paths checked before novelty claims;
- no-commit and changed-set evidence from the external worker;
- CVF reviewer classification before any roadmap or implementation action.

## Fail Conditions

- any source folder or file is silently excluded;
- README/TREEVIEW interpretation substitutes for source-body review;
- prototype tests are treated as CVF runtime proof;
- external reviewer opinion is treated as CVF authority;
- an implementation, package activation, guard change, provider call, or public action occurs in SOT3-T0;
- Refinery receives AI, agent, prompt, or provider ownership without a new operator decision;
- Flow keeps a second canonical RefineryPacket without explicit architecture disposition;
- a roadmap or review claims complete absorption while unresolved ledger rows remain.

## External Repository Absorption Entry Control

| Field | Value |
|---|---|
| Source type | retained legacy three-folder source family |
| Upstream or source-mirror disposition | `LEGACY_REFERENCE_ONLY_WITH_REASON`: operator-authored retained patch with no verified upstream repository identity |
| Enumeration or manifest plan | recursive direct filesystem enumeration including ignored files, one record per relative path |
| Per-file terminal-ledger plan | one body-read row per source item, initially reviewer-pending |
| Owner or overlap route | SOT3-T1 maps accepted value to existing CVF owner surfaces or records an owner decision |
| Value-disposition route | absorb, adapt, defer, reject, block, or no-new-value with reviewer audit |
| Claim boundary | source evaluation only; no direct import or implementation authority |

## Mandatory Blind-Spot Control Block

| Field | Disposition |
|---|---|
| Trigger source | ignored retained legacy source roots |
| Control disposition | APPLICABLE |
| Corpus completeness section | PRESENT |
| Completeness trigger model | exact three-root manifests and per-file body-read ledger |
| Blind-spot prevention action | path-set equality, digest reproduction, and reviewer-pending semantic classification |
| Residual gap | independent external critique and later CVF owner decisions remain open |
| Blind-spot verdict | PARTIAL_PENDING_EXTERNAL_REVIEW |

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | the three literal retained roots in Target / Source |
| Enumeration command | direct recursive filesystem enumeration per literal root |
| Manifest artifact or inline manifest | planned `docs/evidence/sot/sot3-t0-source-manifest.json` |
| Processing ledger artifact or inline ledger | planned `docs/reviews/CVF_SOT3_T0_EXTERNAL_SOURCE_PROCESSING_LEDGER_2026-07-12.md` |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | inline Overlap And Novelty Classification table in this roadmap |
| Unresolved items | 305 before external review |
| Completion claim boundary | roadmap evidence only; no absorption, runtime, or readiness proof |

## Corpus Completeness And Report Integrity

- Corpus task class: retained SOT three-layer full-corpus architecture review.
- Corpus root: the three roots listed in Target / Source.
- Snapshot time: 2026-07-12 local dispatch-authoring session.
- Enumeration command: direct recursive `Get-ChildItem` per literal root.
- Manifest artifact or inline manifest: planned SOT3-T0 JSON manifest and processing ledger.
- Manifest hash: three root-specific SHA-256 values in Target / Source.
- Processing ledger artifact or inline ledger: planned external-review source ledger.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE
- Reconciliation: manifest=305; ledger_terminal=0 at roadmap authoring; exclusions=0; unresolved=305
- Unresolved files: 305
- Declared exclusions: none.
- Unreadable or unsupported files: none observed during dispatcher scan.
- Aggregation check: 133 plus 93 plus 79 equals 305 files; total bytes equal 316848.
- Drift check: SOT3-T0 worker must reproduce all root-specific counts, bytes, and digests.
- Output traceability: source-root ID, relative path, file digest, and body-read status.
- Adversarial verification: build/test results and earlier dispatcher conclusions cannot substitute for independent file-body critique.
- Corpus verdict: PARTIAL

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| three-layer doctrine | separation of preparation, trust evaluation, and distribution | `DOCTRINE_ADAPTED` | SOT3-T2 contract family | independent critique then owner reconciliation | no implementation in T0 |
| Refinery package | deterministic preparation primitives | `PACKAGE_CANDIDATE` | SOT3-T3 | rewrite after contract ratification | no direct import |
| Truth Kernel package | evidence, obligation, provenance, verification, receipt primitives | `RUNTIME_CANDIDATE` | SOT3-T4 | hardening design after T2 | no current runtime mutation |
| Truth Flow package | routing, dose, distribution, lifecycle, feedback primitives | `RUNTIME_CANDIDATE` | SOT3-T5 | remove duplicated upstream ownership first | no current runtime mutation |
| prototype guards and scripts | enforcement use cases | `CHECKER_CANDIDATE` | future governance owner decision | classify only | no checker wiring |
| duplicated or conflicting packet definitions | architecture evidence | `REJECT_DIRECT_IMPORT` | SOT3-T1 and T2 | preserve as negative evidence | no package activation |
| duplicate historical or non-reusable material | possible context only | `NO_PACKAGE_OR_RUNTIME_VALUE` | retained provenance only | require body-read reason before final disposition | no runtime or package action |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| general Truth Kernel doctrine | `docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_SOURCE_PROVENANCE_AND_VERIFICATION_CONTRACT.md` | ENRICH_EXISTING | retained package is broader than the bounded doctrine already adapted | external critique and SOT3-T1 mapping |
| skill-specific truth packets | `docs/reference/agent_system_skills/CVF_SKILL_SOURCE_OF_TRUTH_PACKET_STANDARD.md` | ENRICH_EXISTING | current owner is a vertical slice, not the general three-layer stack | preserve compatibility requirement |
| independent Refinery Core | OWNER_SURFACE_NOT_FOUND | OWNER_SURFACE_NOT_FOUND | no current general RefineryPacket owner found | validate in SOT3-T1 before creating owner |
| post-Kernel distribution lifecycle | OWNER_SURFACE_NOT_FOUND | OWNER_SURFACE_NOT_FOUND | no current shared Truth Flow owner found | validate in SOT3-T1 before creating owner |
| retained prototype implementations | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/receipt-binding.contract.ts` | REJECT_DIRECT_IMPORT | incompatible packet and trust boundaries | rewrite only after contract ratification |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | legacy source family |
| Chain map route | retained corpus -> bounded external-review packet -> independent full scan -> returned-output absorption workflow -> CVF owner reconciliation -> separately authorized implementation |
| Matching local-view guard | `governance/compat/check_absorption_blindspot_control_presence.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_corpus_completeness_report_integrity.py` |
| Owner surface | this roadmap until SOT3-T2 ratifies shared contracts |
| Disposition | ADAPT through independent critique and selective CVF-native rewrite |
| Claim boundary | roadmap and review planning only; no runtime, provider, public, or production claim |

## Checker Source Read-Ahead Block

| Field | Disposition |
|---|---|
| applicableCheckersRead | `governance/compat/check_absorption_blindspot_control_presence.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_roadmap_closure_freshness.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py` |
| literalTokensReviewed | Target / Source; Scope / Methodology; Findings / Position; External Repository Absorption Entry Control; Mandatory Blind-Spot Control Block; Corpus Completeness And Report Integrity; External Absorption Value Conversion Matrix; Overlap And Novelty Classification; External Knowledge Intake Routing; PARTIAL; PROPOSED_EXTERNAL_REVIEW_FIRST |
| gateRunPurpose | confirm exact authored evidence and literal shape after pre-write checker review |
| claimBoundary | checker-shape evidence does not prove semantic correctness or future implementation behavior |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this roadmap evaluates private retained source. A public-safe projection
requires a separate public-sync decision after CVF-native contracts exist.

## Claim Boundary

This roadmap authorizes planning and the SOT3-T0 external-review dispatch only.
It does not authorize direct import, contract ratification, runtime or checker
implementation, package activation, provider/live proof, public-sync, release,
or production readiness. External-review output remains advisory until CVF
classifies it through the governed absorption workflow.
