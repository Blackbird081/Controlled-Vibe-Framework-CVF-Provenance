# CVF GC-018 Baseline - SOT3-T0R Semantic Reconciliation

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: baseline

Date: 2026-07-12

Baseline ID: GC018-SOT3-T0R

Risk ceiling: HIGH_EVIDENCE_DOCS_ONLY

## Purpose

Authorize one no-commit external reviewer to convert the committed SOT3-T0
advisory evidence into a clear, source-backed architecture decision
recommendation before any CVF implementation or contract ratification.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind gc018-baseline --batch-id SOT3-T0R --title "Semantic Reconciliation" --date 2026-07-12 --base 0fbcadbc9 --stdout` |
| generatedProfile | GC-018 external semantic review |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | Filled source verification, corpus, external absorption, overlap, routing, blind-spot, evidence, fail-condition, and claim-boundary controls. |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_dispatch_scaffold_provenance.py` |
| docOnlyNewFields | `SOT3-T0R`; eight semantic decision axes |
| claimBoundary | Dispatch baseline provenance only; no architecture ratification or implementation. |

## Target / Source

Primary committed evidence:

- `docs/evidence/sot/sot3-t0-source-manifest.json`;
- `docs/reviews/CVF_SOT3_T0_EXTERNAL_SOURCE_PROCESSING_LEDGER_2026-07-12.md`;
- `docs/reviews/CVF_SOT3_T0_EXTERNAL_REVIEW_RETURN_2026-07-12.md`;
- `docs/reviews/CVF_SOT3_T0_PROCESS_FINDINGS_FOR_CODEX_2026-07-12.md`;
- `docs/corpus-intelligence/registry/entries/sot3-t0-retained-three-layer-advisory-scan.json`.

Retained source roots remain read-only:

- `.private_reference/legacy/CVF_SOT 10.07/CVF_Refinery_Patch`;
- `.private_reference/legacy/CVF_SOT 10.07/CVF_Truth_Kernel_Patch`;
- `.private_reference/legacy/CVF_SOT 10.07/CVF_Truth_Flow_Patch`.

## Scope / Methodology

Allowed:

- validate committed evidence without repeating file hashing;
- deeply re-read all 61 documentation files, every ABSORB and REJECT row, and
  all source files supporting disputed boundaries;
- challenge both Codex and prior Claude conclusions;
- decide the proposed layer topology, pipeline order, contract chain, and
  selective absorption boundary;
- create exactly three review outputs.

Forbidden:

- implementation, runtime/schema/test/guard/checker changes;
- direct import, package activation, provider/live proof, public-sync, commit,
  session/handoff mutation, or architecture ratification by the worker;
- claiming all 305 semantic dispositions accepted from first-line evidence;
- reopening file identity unless committed manifest drift is detected.

## Findings / Position

The evidence supports a three-layer hypothesis but does not yet constitute a
ratified CVF architecture. T0R must make the disagreements explicit and return
one recommendation that a CVF reviewer can accept, revise, or reject.

Required decision axes:

1. Refinery independent deterministic no-AI module boundary.
2. Source capture before normalization and continuous lineage.
3. Duplicate grouping before conflict evaluation.
4. Truth Kernel as sole trust-evaluation and receipt authority.
5. Truth Flow post-Kernel-only versus a separately named facade plus
   post-Kernel module.
6. Fail-closed empty-stage and empty-verification invariants.
7. One canonical cross-layer packet and receipt chain.
8. Absorb/adapt/defer/reject decisions before implementation sequencing.

## Baseline Decision

SOT3-T0R is authorized for semantic reconciliation and architecture
recommendation only. Implementation remains `NOT_AUTHORIZED` regardless of the
worker recommendation until CVF reviewer acceptance and a later fresh tranche.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`external semantic architecture reconciliation`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command:
`python governance/compat/run_adif_defect_resolver.py --task-class "external semantic architecture reconciliation" --role dispatcher --lifecycle-phase pre-dispatch --surface-selector docs/work_orders --risk-ceiling HIGH --max-results 20 --json`

Returned defects: NONE_RETURNED

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| advisory corpus contains 305 verified file hashes | VALUE_SET | `docs/evidence/sot/sot3-t0-source-manifest.json` | top-level fileCount and records | `fileCount` | SOT3-T0 manifest | ACCEPT |
| T0 return rejects work-order closure and accepts advisory input | VALUE_SET | `docs/reviews/CVF_SOT3_T0_EXTERNAL_REVIEW_RETURN_2026-07-12.md` | Decision / Disposition | `REJECT_WORK_ORDER_CLOSURE_ACCEPT_ADVISORY_INPUT` | CVF reviewer disposition | ACCEPT |
| SOT3 registry status is partial | VALUE_SET | `docs/corpus-intelligence/registry/entries/sot3-t0-retained-three-layer-advisory-scan.json` | status and nextScanRecommendation | `status` | corpus registry entry | ACCEPT |
| roadmap contains T0R before implementation lanes | VALUE_SET | `docs/roadmaps/CVF_SOT_THREE_LAYER_ABSORPTION_ROADMAP_2026-07-12.md` | Tranche Plan | `SOT3-T0R` | SOT3 roadmap | ACCEPT |
| worker may not commit | VALUE_SET | archive-qualified contract citation: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | WORKER_MUST_NOT_COMMIT rule | `WORKER_MUST_NOT_COMMIT` | Agent Handoff Contract | ACCEPT |

## External Repository Absorption Entry Control

| Field | Value |
|---|---|
| Source type | retained legacy three-folder source family plus committed advisory evidence |
| Upstream or source-mirror disposition | LEGACY_REFERENCE_ONLY_WITH_REASON: operator-authored retained patch without verified upstream identity |
| Enumeration or manifest plan | reuse committed 305-record manifest; no hash rescan unless drift appears |
| Per-file terminal-ledger plan | audit documentation and disputed/high-value rows; retain all other rows reviewer-pending |
| Owner or overlap route | T0R recommends owner boundaries; CVF reviewer decides |
| Value-disposition route | absorb, adapt, defer, reject, block, or no-new-value |
| Claim boundary | architecture recommendation only; no direct import or implementation |

## Mandatory Blind-Spot Control Block

| Field | Disposition |
|---|---|
| Trigger source | committed partial SOT3 scan and retained roots |
| Control disposition | APPLICABLE |
| Corpus completeness section | PRESENT |
| Completeness trigger model | 61 documentation files plus every ABSORB/REJECT and disputed contract source |
| Blind-spot prevention action | challenge prior conclusions, identify unsupported rows, and keep unaudited rows pending |
| Residual gap | final CVF reviewer acceptance remains open |
| Blind-spot verdict | PARTIAL_PENDING_T0R_EXECUTION |

## Corpus Completeness And Report Integrity

- Corpus task class: SOT3 semantic reconciliation from committed advisory evidence.
- Corpus root: committed T0 evidence plus three retained roots.
- Snapshot time: 2026-07-12 dispatch.
- Enumeration command: filesystem-backed direct file reads using the committed manifest.
- Manifest artifact or inline manifest: `docs/evidence/sot/sot3-t0-source-manifest.json`.
- Manifest hash: per-file SHA-256 records; original aggregate algorithm remains unspecified.
- Processing ledger artifact or inline ledger: committed SOT3-T0 processing ledger.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE
- Reconciliation: manifest=305; ledger_terminal=305; exclusions=0; unresolved=0
- Unresolved files: 0 file identities; semantic acceptance remains open.
- Declared exclusions: no file exclusion; non-disputed low-value rows remain reviewer-pending.
- Unreadable or unsupported files: none.
- Aggregation check: 305 file identities already verified and registry-backed.
- Drift check: compare current file hashes only if source drift is observed.
- Output traceability: T0R rows cite committed evidence and retained source paths.
- Adversarial verification: prior Codex and Claude conclusions are hypotheses, not authority.
- Corpus verdict: PARTIAL

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | committed SOT3-T0 evidence and retained three-layer roots |
| Enumeration command | filesystem-backed direct file reads from committed manifest targets |
| Manifest artifact or inline manifest | `docs/evidence/sot/sot3-t0-source-manifest.json` |
| Processing ledger artifact or inline ledger | `docs/reviews/CVF_SOT3_T0_EXTERNAL_SOURCE_PROCESSING_LEDGER_2026-07-12.md` |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | planned `docs/reviews/CVF_SOT3_T0R_SEMANTIC_RECONCILIATION_MATRIX_2026-07-12.md` |
| Unresolved items | architecture and owner decisions remain pending |
| Completion claim boundary | recommendation only; no runtime or readiness proof |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| layer doctrine | prepare/evaluate/distribute separation | DOCTRINE_ADAPTED | T0R recommendation | decide exact topology | no implementation |
| Refinery module | deterministic preparation | PACKAGE_CANDIDATE | later T3 candidate | decide boundary first | no package activation |
| Kernel module | trust evaluation and receipts | RUNTIME_CANDIDATE | later T4 candidate | decide invariants first | no runtime change |
| Flow module | routing and lifecycle | RUNTIME_CANDIDATE | later T5 candidate | decide post-Kernel ownership | no runtime change |
| fail-closed cases | enforcement use cases | CHECKER_CANDIDATE | later contract-test lane | recommend tests only | no checker wiring |
| duplicate Flow refinery | incompatible ownership | REJECT_DIRECT_IMPORT | negative evidence | decide rejection explicitly | no direct import |
| low-value scaffolding | context only | NO_PACKAGE_OR_RUNTIME_VALUE | retained provenance | keep pending or reject with reason | no runtime/package action |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| truth doctrine | `docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_SOURCE_PROVENANCE_AND_VERIFICATION_CONTRACT.md` | ENRICH_EXISTING | general SOT stack is broader | reconcile |
| skill truth packet | `docs/reference/agent_system_skills/CVF_SKILL_SOURCE_OF_TRUTH_PACKET_STANDARD.md` | ENRICH_EXISTING | vertical slice only | preserve compatibility |
| independent Refinery | OWNER_SURFACE_NOT_FOUND | OWNER_SURFACE_NOT_FOUND | proposed new owner | recommend, do not create |
| post-Kernel Flow | OWNER_SURFACE_NOT_FOUND | OWNER_SURFACE_NOT_FOUND | proposed new owner | recommend, do not create |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | committed advisory evidence -> T0R external semantic critique -> CVF reviewer decision -> later fresh implementation tranche if authorized |
| Matching local-view guard | `governance/compat/check_external_absorption_core.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py` |
| Owner surface | paired T0R baseline and work order |
| Disposition | ADAPT through independent semantic reconciliation |
| Claim boundary | no external recommendation becomes CVF authority directly |

## Verification / Evidence

- source citations for every decision axis;
- explicit dissent against both prior reviewers;
- coverage table for 61 docs and every ABSORB/REJECT row;
- one recommended topology and one strongest alternative;
- unresolved decisions listed as blockers, never hidden;
- exactly three worker outputs and unchanged HEAD.

## Checker Source Read-Ahead Block

| Field | Disposition |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py` |
| literalTokensReviewed | Purpose; Target / Source; Scope / Methodology; Findings / Position; Baseline Decision; Source Verification Block; External Absorption Core; Corpus Completeness And Report Integrity; PARTIAL; DISPATCH_READY |
| gateRunPurpose | confirm exact dispatch shape after checker review |
| claimBoundary | checker conformance does not decide architecture correctness |

## Acceptance Criteria

- [ ] all eight decision axes receive explicit recommendations;
- [ ] all 61 documentation files receive meaningful semantic coverage;
- [ ] every ABSORB and REJECT row is independently audited;
- [ ] strongest alternative architecture is presented;
- [ ] implementation remains NOT_AUTHORIZED;
- [ ] exactly three outputs and no worker commit.

## Fail Conditions

- broad agreement without citations or dissent;
- runtime, contract, schema, guard, or checker implementation;
- hidden unresolved decision;
- treating T0 advisory dispositions as already accepted;
- worker commit or extra output.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private retained source and pre-implementation architecture review.

## Claim Boundary

This baseline authorizes only the T0R semantic reconciliation and decision
recommendation. It does not authorize architecture ratification,
implementation, package activation, provider/live proof, public-sync, commit,
release, or production readiness.
