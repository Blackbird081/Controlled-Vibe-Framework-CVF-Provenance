# CVF GC-018 Baseline - SOT3-T0 External Three-Layer Review

Memory class: FULL_RECORD

Status: HOLD_PENDING_CLEAN_DISPATCH_COMMIT

docType: baseline

Date: 2026-07-12

Baseline ID: GC018-SOT3-T0

Risk ceiling: HIGH_EVIDENCE_DOCS_ONLY

## Purpose

Authorize one bounded external-review worker to scan all 305 files in the
retained CVF Source of Truth three-layer corpus and return advisory
architecture evidence. The tranche creates only a source manifest, a
processing ledger, and an external review return.

## Target / Source

| Root | Files | Bytes | Root digest |
|---|---:|---:|---|
| `.private_reference/legacy/CVF_SOT 10.07/CVF_Refinery_Patch` | 133 | 160461 | `c7ace9ccbb470514bb9fea97527976a462146b5b220df88eadc6fdc38b88cbe2` |
| `.private_reference/legacy/CVF_SOT 10.07/CVF_Truth_Kernel_Patch` | 93 | 78007 | `73e4cc652f738d70428326a013de08fc65ce4edb553dcd3e4670eb8a46765497` |
| `.private_reference/legacy/CVF_SOT 10.07/CVF_Truth_Flow_Patch` | 79 | 78380 | `e7be38e77889f6280248fc4a6ceacf354a41c8f1c331fbb2a491e29f8a27858f` |

Authority inputs:

- operator instruction on 2026-07-12 to update the roadmap, prepare a
  synthesis packet, and dispatch an independent Claude scan;
- `docs/roadmaps/CVF_SOT_THREE_LAYER_ABSORPTION_ROADMAP_2026-07-12.md`;
- `docs/reviews/CVF_SOT3_T0_EXTERNAL_REVIEW_PACKET_2026-07-12.md`;
- current active session state and active handoff.

## Scope / Methodology

Allowed:

- read all files in the three retained roots;
- reproduce deterministic snapshot evidence;
- create one JSON source manifest;
- create one per-file processing ledger;
- create one evidence-backed external review return;
- run read-only builds and tests in isolated temporary copies when useful;
- inspect current CVF governed owner surfaces read-only for overlap analysis;
- repair only the three worker-owned output files for applicable gate shape.

Forbidden:

- edit any retained source file;
- edit roadmap, baseline, work order, review packet, current CVF runtime,
  schemas, tests, guards, checkers, registries, generated state, session state,
  or handoff;
- direct import or implementation;
- provider/live API proof, secrets, package activation, public-sync, push, or
  production-readiness claims;
- commit by the external-review worker.

## Findings / Position

The dispatcher expects that the three-layer model has value but the prototypes
require boundary and contract rewrite. This expectation is a falsifiable
review hypothesis, not a baseline verdict.

The review must test:

- Refinery as an independent deterministic no-AI core;
- Truth Kernel as the sole trust evaluation and receipt layer;
- Truth Flow as post-Kernel distribution/lifecycle or an explicitly separated
  orchestration facade;
- a single canonical chain of cross-layer contracts;
- selective absorption rather than full or direct import.

## Baseline Decision

Disposition: AUTHORIZED_IN_PRINCIPLE_HELD_FOR_CLEAN_DISPATCH

Release requires:

1. roadmap, packet, baseline, and work order in one clean governed dispatch
   commit;
2. no pre-existing protected dirty path in the dispatch range;
3. pre-dispatch autorun PASS on a real changed range;
4. external worker capture of a fresh `executionBaseHead`.

The current worktree contains a pre-existing operator modification to
`CVF_SESSION_MEMORY.md`. That path is excluded and must not be edited, staged,
or claimed by this dispatch.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`external agent review corpus scan`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command:
`python governance/compat/run_adif_defect_resolver.py --task-class "external agent review corpus scan" --role dispatcher --lifecycle-phase pre-dispatch --surface-selector docs/work_orders --risk-ceiling HIGH --max-results 20 --json`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Returned defect count | 0 |
| Disclosed defectIds | NONE_RETURNED |
| Baseline impact | no additional ADIF defect control returned for this exact query |

## Planned Worker Fulfillment Manifest

| Path | Required action | Purpose |
|---|---|---|
| `docs/evidence/sot/sot3-t0-source-manifest.json` | CREATE | exact three-root file records and root reconciliation |
| `docs/reviews/CVF_SOT3_T0_EXTERNAL_SOURCE_PROCESSING_LEDGER_2026-07-12.md` | CREATE | one body-read and advisory classification row per source file |
| `docs/reviews/CVF_SOT3_T0_EXTERNAL_REVIEW_RETURN_2026-07-12.md` | CREATE | cross-layer architecture critique and advisory disposition |

Every other path is forbidden to the worker.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| three-layer roadmap starts with independent review | VALUE_SET | `docs/roadmaps/CVF_SOT_THREE_LAYER_ABSORPTION_ROADMAP_2026-07-12.md` | Tranche Plan | `SOT3-T0` | SOT3 roadmap | ACCEPT |
| review packet requires complete three-root critique | VALUE_SET | `docs/reviews/CVF_SOT3_T0_EXTERNAL_REVIEW_PACKET_2026-07-12.md` | Review Objective; Target / Source | `SOT3-T0-ERP` | external review packet | ACCEPT |
| Refinery engine permits empty default stages | RUNTIME_BEHAVIOR | `.private_reference/legacy/CVF_SOT 10.07/CVF_Refinery_Patch/EXTENSIONS/CVF_REFINERY/src/pipeline/refinery-engine.ts` | line 58 | `run` | `RefineryEngine` | ACCEPT |
| Flow defines a second Refinery packet status | VALUE_SET | `.private_reference/legacy/CVF_SOT 10.07/CVF_Truth_Flow_Patch/EXTENSIONS/CVF_TRUTH_FLOW/src/refinery/refinery-engine.ts` | lines 9-14 | `RefineryPacket` | embedded Flow refinery engine | ACCEPT |
| Flow lifecycle permits ready-to-verified transition | VALUE_SET | `.private_reference/legacy/CVF_SOT 10.07/CVF_Truth_Flow_Patch/EXTENSIONS/CVF_TRUTH_FLOW/src/lifecycle/lifecycle-engine.ts` | line 14 | `READY_FOR_VERIFICATION` | `allowed` transition map | ACCEPT |
| Kernel receipt status derives from result-array searches | RUNTIME_BEHAVIOR | `.private_reference/legacy/CVF_SOT 10.07/CVF_Truth_Kernel_Patch/EXTENSIONS/CVF_TRUTH_KERNEL/src/receipts/truth-receipt.ts` | lines 26-30 | `verification_results` | `createTruthReceipt` | ACCEPT |
| Kernel truth packet schema allows extra fields | VALUE_SET | `.private_reference/legacy/CVF_SOT 10.07/CVF_Truth_Kernel_Patch/EXTENSIONS/CVF_TRUTH_KERNEL/schemas/truth.packet.schema.json` | line 6 | `additionalProperties` | truth packet JSON schema | ACCEPT |
| external output remains advisory | LITERAL_INVARIANT | `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_REVIEW_PACKET_TEMPLATE.md` | Absorption Instruction | `External output is advisory` | external review packet template | ACCEPT |

## External Repository Absorption Entry Control

| Field | Value |
|---|---|
| Source type | retained legacy three-folder source family |
| Upstream or source-mirror disposition | `LEGACY_REFERENCE_ONLY_WITH_REASON`: operator-authored retained patch without verified upstream repository identity |
| Enumeration or manifest plan | direct recursive enumeration including ignored files and per-file SHA-256 |
| Per-file terminal-ledger plan | one row per source-relative path with body-read status and advisory classification |
| Owner or overlap route | external worker proposes candidates; CVF reviewer owns acceptance |
| Value-disposition route | absorb, adapt, defer, reject, block, or no-new-value |
| Claim boundary | evidence and critique only; no direct import or implementation |

## Mandatory Blind-Spot Control Block

| Field | Disposition |
|---|---|
| Trigger source | ignored retained legacy source roots |
| Control disposition | APPLICABLE |
| Corpus completeness section | PRESENT |
| Completeness trigger model | exact 305-file manifest and one ledger row per record |
| Blind-spot prevention action | root digest reproduction, path-set equality, unreadable accounting, and reviewer-pending semantic state |
| Residual gap | final CVF value and owner decisions remain reviewer-owned |
| Blind-spot verdict | PARTIAL_PENDING_EXTERNAL_REVIEW |

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | the three literal roots in Target / Source |
| Enumeration command | direct recursive filesystem enumeration per literal root |
| Manifest artifact or inline manifest | planned `docs/evidence/sot/sot3-t0-source-manifest.json` |
| Processing ledger artifact or inline ledger | planned `docs/reviews/CVF_SOT3_T0_EXTERNAL_SOURCE_PROCESSING_LEDGER_2026-07-12.md` |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | inline Overlap And Novelty Classification table in this baseline |
| Unresolved items | 305 before worker execution |
| Completion claim boundary | baseline authorization only; no absorption, implementation, or readiness proof |

## Corpus Completeness And Report Integrity

- Corpus task class: retained SOT three-layer external architecture review.
- Corpus root: three literal roots in Target / Source.
- Snapshot time: 2026-07-12.
- Enumeration command: direct recursive `Get-ChildItem` per literal root.
- Manifest artifact or inline manifest: planned `docs/evidence/sot/sot3-t0-source-manifest.json`.
- Manifest hash: three root-specific digests in Target / Source.
- Processing ledger artifact or inline ledger: planned external source processing ledger.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE
- Reconciliation: manifest=305; ledger_terminal=0 at dispatch authoring; exclusions=0; unresolved=305
- Unresolved files: 305.
- Declared exclusions: none.
- Unreadable or unsupported files: none known.
- Aggregation check: 305 files and 316848 bytes.
- Drift check: worker reproduces all three root snapshots before body review.
- Output traceability: root ID, source-relative path, digest, size, body-read status.
- Adversarial verification: README/TREEVIEW, tests, and dispatcher findings cannot substitute for full body reads.
- Corpus verdict: PARTIAL

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| three-layer doctrine | separation of preparation, trust evaluation, and distribution | DOCTRINE_ADAPTED | SOT3-T2 candidate | independent review first | no implementation |
| Refinery primitives | deterministic preparation | PACKAGE_CANDIDATE | SOT3-T3 candidate | classify only | no direct import |
| Kernel primitives | evidence, obligation, provenance, verification, receipt | RUNTIME_CANDIDATE | SOT3-T4 candidate | compare owners | no runtime mutation |
| Flow primitives | routing, dose, lifecycle, feedback | RUNTIME_CANDIDATE | SOT3-T5 candidate | remove duplicated ownership | no runtime mutation |
| prototype guards | enforcement use cases | CHECKER_CANDIDATE | future owner decision | record only | no checker wiring |
| incompatible source implementations | negative integration evidence | REJECT_DIRECT_IMPORT | SOT3-T2 | preserve mismatch facts | no package activation |
| duplicate or non-reusable material | context only | NO_PACKAGE_OR_RUNTIME_VALUE | retained provenance | require body-read reason | no runtime or package action |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| truth doctrine | `docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_SOURCE_PROVENANCE_AND_VERIFICATION_CONTRACT.md` | ENRICH_EXISTING | broader retained concepts require review | map exact delta |
| skill truth packets | `docs/reference/agent_system_skills/CVF_SKILL_SOURCE_OF_TRUTH_PACKET_STANDARD.md` | ENRICH_EXISTING | vertical slice is not general owner proof | preserve compatibility check |
| independent Refinery | OWNER_SURFACE_NOT_FOUND | OWNER_SURFACE_NOT_FOUND | owner remains unratified | worker searches; reviewer decides |
| post-Kernel Flow | OWNER_SURFACE_NOT_FOUND | OWNER_SURFACE_NOT_FOUND | owner remains unratified | worker searches; reviewer decides |
| prototype receipt paths | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/receipt-binding.contract.ts` | REJECT_DIRECT_IMPORT | incompatible binding semantics | adaptation only |

## Verification / Evidence

- root-specific count, bytes, and digest reproduction;
- 305 unique manifest records and 305 matching processing rows;
- source-backed layer and contract findings;
- explicit dissent and alternative architecture;
- actual three-path worker changed set;
- unchanged worker HEAD and no-commit statement;
- required component and worker-return gate evidence.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | retained corpus -> bounded review packet -> external advisory return -> CVF finding absorption workflow |
| Matching local-view guard | `governance/compat/check_absorption_blindspot_control_presence.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_corpus_completeness_report_integrity.py` |
| Owner surface | paired roadmap, packet, baseline, and work order |
| Disposition | ADAPT only after independent critique and CVF reviewer acceptance |
| Claim boundary | no runtime, provider, public, package, checker, or production claim |

## Checker Source Read-Ahead Block

| Field | Disposition |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_absorption_blindspot_control_presence.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | Purpose; Target / Source; Scope / Methodology; Findings / Position; Authorization / Decision; Source Verification Block; External Repository Absorption Entry Control; Mandatory Blind-Spot Control Block; Corpus Completeness And Report Integrity; External Knowledge Intake Routing; PARTIAL |
| gateRunPurpose | confirm the baseline's bounded authorization and exact evidence shape after checker review |
| claimBoundary | gate shape does not prove future worker completeness or semantic correctness |

## Acceptance Criteria

- [ ] worker reproduces all three source snapshots;
- [ ] manifest contains exactly 305 unique source records;
- [ ] ledger contains exactly one row for every manifest record;
- [ ] README and TREEVIEW claims are compared against implementation;
- [ ] cross-layer packet and lifecycle mismatches are source-cited;
- [ ] external return contains evidence-backed dissent and alternative architecture;
- [ ] every capability group receives an advisory disposition;
- [ ] worker touches only the three planned outputs;
- [ ] worker HEAD remains unchanged;
- [ ] external return remains pending CVF review.

## Fail Conditions

- source snapshot drift is silently accepted;
- any readable file lacks a body-read ledger row;
- review relies only on filenames, README, TREEVIEW, or tests;
- external output claims CVF authority or readiness;
- worker edits a forbidden path or commits;
- direct import, implementation, provider/live, public, package, checker, or
  generated-state action occurs;
- routine gate repair requires a path outside the three worker-owned outputs.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: the baseline authorizes review of private retained source only.

## Claim Boundary

This baseline authorizes a no-commit external-review evidence tranche after a
clean dispatch commit and passing pre-dispatch gate. It does not authorize
direct import, contract ratification, implementation, provider/live proof,
public-sync, release, or production readiness.
