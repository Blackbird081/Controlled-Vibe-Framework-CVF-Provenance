# CVF GC-018 Baseline - MPA-AI-T0 Local Memory Poisoning Absorption Intake

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Date: 2026-08-27

Batch ID: MPA-AI-T0

Dispatch base head: 8bda197b14337e229fa29dddbbdb39608e09e3d2

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: CVF operator

Reviewer owner: CVF reviewer/closer

Worker target: current CVF agent in a bounded no-commit semantic-intake role

Mixed-origin derived synthesis: REQUIRED

artifactClass: PROVENANCE_BACKED_DERIVED_SYNTHESIS_CANDIDATE

authorityStatus: NON_AUTHORITATIVE_UNTIL_REVIEWED

External absorption core: REQUIRED

rawMemoryReleased=false

## Purpose

Authorize a single-pass, source-verified intake of the operator-supplied local
memory-poisoning packet. Determine whether its four proposed capability
clusters expose serious, current, non-duplicate CVF gaps whose value exceeds
implementation, review, latency, and maintenance cost. This baseline does not
authorize implementation.

## Decision

Open MPA-AI-T0 as a documentation-only, no-commit semantic intake. Preserve
all current CVF owners and require a fresh operator decision for any successor.

## Evidence Requirements

Closure requires 50 terminal ledger rows, primary-paper verification for used
research claims, current-owner comparison for every retained cluster, an exact
value/cost decision, and passing provider-free governance gates.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind source-intake --batch-id MPA-AI-T0 --title "Local Memory Poisoning Mixed-Origin Absorption Intake" --date 2026-08-27 --base 8bda197b14337e229fa29dddbbdb39608e09e3d2 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | source-intake plus WORKER_MUST_NOT_COMMIT profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced stubs with verified local identity, 50-file receipt, mixed-origin controls, owner/value gates, and exact output ownership |
| checkerReadAheadConfirmation | external absorption, mixed-origin, blind-spot, corpus integrity, knowledge reconciliation, task routing, dispatch envelope, scaffold provenance, registry, and public export checker sources reviewed |
| docOnlyNewFields | `localSourceIdentity`; `paperVerificationBoundary`; `valueGateDecision` |
| claimBoundary | dispatch evidence only; no implementation, runtime, provider, public, deployment, or production claim |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`external-knowledge-absorption`, role=`dispatcher`, lifecyclePhase=`dispatch`.

Returned defects: NONE_RETURNED.

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class external-knowledge-absorption --role dispatcher --lifecycle-phase dispatch --risk-ceiling HIGH --max-results 20 --json` |
| Returned defect count | 0 |
| Returned defects | none |
| Disclosed defectIds | none |
| Dispatch impact | no registered ADIF defect changes this bounded intake route |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_absorption_blindspot_control_presence.py`; `governance/compat/check_mixed_origin_derived_synthesis_absorption.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_corpus_to_knowledge_map_reconciliation.py`; `governance/compat/check_source_mirror_migration.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/route_task_governance.py`; `governance/compat/check_corpus_scan_registry.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | External Repository Absorption Entry Control; Mandatory Blind-Spot Control Block; External Absorption Core; Corpus Completeness And Report Integrity; Knowledge System Reconciliation; Mixed-Origin Derived Synthesis Provenance; Absorption Decision Vector; System-Chain Value Review; Absorption Efficiency And Provenance Reuse; External Knowledge Intake Routing; Public Export Disposition |
| gateRunPurpose | confirm dispatch shape after authoring; gates are not used as first source discovery |
| claimBoundary | read-ahead covers dispatch and T0 evidence shape only, not semantic correctness or implementation |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| local packet identity and proposed four clusters | derived synthesis | `.private_reference/legacy/CVF 13.08/CVF_MEMORY_POISONING_ABSORPTION/README.md` | Purpose; four approved absorptions | packet root | local mixed-origin packet | ACCEPT |
| operator/external-agent origin and no Git upstream | provenance | `.private_reference/legacy/CVF 13.08/CVF_MEMORY_POISONING_ABSORPTION/SOURCE_BASIS.md` | Research input; CVF owner/source observations | source basis | operator-supplied local source | ACCEPT |
| source manifest integrity | immutable inventory | `.private_reference/legacy/CVF 13.08/CVF_MEMORY_POISONING_ABSORPTION/PACKET_MANIFEST.json` | complete `files` array | 49 declared files, self excluded | packet manifest | ACCEPT |
| implementation is not pre-authorized | authority boundary | `.private_reference/legacy/CVF 13.08/CVF_MEMORY_POISONING_ABSORPTION/CLAIM_BOUNDARY.md` | Claims requiring implementation and tests | packet claim boundary | current CVF authority | ACCEPT |
| current retrieval trust is ranking metadata | runtime source | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` | lines 56-57; candidate admission and ranking | `auditTrust`; `isValidAuditTrust` | Memory Foundation runtime | ACCEPT |
| omitted durable provenance defaults to one | runtime source | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | line 249 | `input.provenanceScore ?? 1` | durable memory store | ACCEPT |
| integrity is not truth | governance doctrine | `docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_SOURCE_PROVENANCE_AND_VERIFICATION_CONTRACT.md` | Integrity Is Not Truth | truth foundation contract | Truth Foundation | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| governed path collision | all planned MPA-AI-T0 baseline, work-order, audit, review, manifest, and ledger paths were absent before authoring | PASS |
| exact prior lane | `rg -n "MPA-AI-T0|CVF_MEMORY_POISONING_ABSORPTION" docs CVF_SESSION governance` found only the new scan-open registry entry | PASS |
| topic overlap | current Memory and Truth owners contain related trust/provenance doctrine, so every proposal requires field-level owner reconciliation | ENRICH_EXISTING_OR_NO_NEW_VALUE |
| collision decision | open T0 intake only; do not create a roadmap or implementation lane before the value decision | ACCEPT |

## External Repository Absorption Entry Control

| Field | Value |
| --- | --- |
| Source type | operator-supplied copied local folder produced through operator and external-agent exchange; not a GitHub repository |
| Upstream or source-mirror disposition | no repository mirror applies; paper-attributed claims require targeted primary-paper verification, while current CVF claims require current local owner verification |
| Enumeration or manifest plan | independent 50-file filesystem manifest plus verification of the source-supplied 49-file self-excluding manifest |
| Per-file terminal-ledger plan | one terminal semantic row for each of 50 files |
| Owner or overlap route | Memory Foundation, Truth Foundation/SOT3, Context, Action revalidation, evaluation/benchmark, or missing-owner decision |
| Value-disposition route | ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE, package/runtime/checker candidate, or serious fresh-roadmap candidate |
| Claim boundary | documentation-only intake; no direct import, source execution, runtime mutation, provider/live call, public sync, deployment, or production authority |

## Mandatory Blind-Spot Control Block

Packet summaries, filenames, proposed approvals, and hashes are not semantic
completion evidence. Every retained cluster must cite current CVF owner source
and primary-paper evidence where it relies on a research claim. Every file must
end in a terminal ledger state, including duplicates and rejected work-order or
implementation instructions.

## External Absorption Core

| Field | Value |
| --- | --- |
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | `.private_reference/legacy/CVF 13.08/CVF_MEMORY_POISONING_ABSORPTION/` |
| Enumeration command | recursive filesystem-backed `Get-ChildItem -LiteralPath <corpusRoot> -Recurse -Force -File` |
| Manifest artifact or inline manifest | `docs/audits/CVF_MPA_AI_T0_LOCAL_MEMORY_POISONING_MANIFEST_2026-08-27.json` |
| Processing ledger artifact or inline ledger | `docs/audits/CVF_MPA_AI_T0_LOCAL_MEMORY_POISONING_FILE_LEDGER_2026-08-27.json` |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | `docs/reference/memory_foundation/`; `docs/reference/truth_foundation/`; `docs/reference/CVF_MEMORY_PLANE_MAP.md`; final T0 audit inline owner table |
| Unresolved items | 50 semantic classifications at dispatch |
| Completion claim boundary | inventory and dispatch only; no semantic completion or implementation claim |

## Corpus Completeness And Report Integrity

- Corpus task class: operator-supplied local mixed-origin folder intake.
- Corpus root: `.private_reference/legacy/CVF 13.08/CVF_MEMORY_POISONING_ABSORPTION/`.
- Snapshot time: 2026-08-27T00:00:00+07:00.
- Enumeration command: filesystem-backed recursive `Get-ChildItem -LiteralPath <corpusRoot> -Recurse -Force -File`.
- Manifest artifact or inline manifest: `docs/audits/CVF_MPA_AI_T0_LOCAL_MEMORY_POISONING_MANIFEST_2026-08-27.json`.
- Manifest hash: `7bcdc612aaf99e7323de9b1236474c1e9ebf8a6b326d3e19ada649a1b57f9e10`.
- Processing ledger artifact or inline ledger: `docs/audits/CVF_MPA_AI_T0_LOCAL_MEMORY_POISONING_FILE_LEDGER_2026-08-27.json`.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.
- Reconciliation: manifest=50; ledger_terminal=50; exclusions=0; unresolved=50 at dispatch.
- Unresolved files: 50.
- Declared exclusions: none.
- Unreadable or unsupported files: none during byte hashing.
- Aggregation check: source packet 49 declared plus self-excluded packet manifest equals 50 observed files.
- Drift check: source-declared hashes match 49/49; semantic review pending.
- Output traceability: final audit must cite source path, ledger row, paper evidence when applicable, and current CVF owner.
- Adversarial verification: reviewer must inspect every retained/high-risk group and sample duplicate/no-value groups.
- Corpus verdict: PARTIAL

## Knowledge System Reconciliation

- Knowledge task class: local synthesis to current CVF owner reconciliation.
- Source manifest: `docs/audits/CVF_MPA_AI_T0_LOCAL_MEMORY_POISONING_MANIFEST_2026-08-27.json`.
- Source manifest hash: `7bcdc612aaf99e7323de9b1236474c1e9ebf8a6b326d3e19ada649a1b57f9e10`.
- Enumeration safety: direct filesystem reads only; no packet code or command execution.
- Intake registry or ledger: MPA-AI-T0 ledger and corpus registry entry.
- Authority assets: current CVF sources for CVF facts; primary paper for paper facts; local pack as secondary synthesis.
- Derived views: final absorption audit, owner map, value decision, and worker return.
- Semantic region ledger: five declared regions; all remain deferred at dispatch.
- Region reconciliation: assets=50; mapped=0; deferred=50; unmapped=0.
- Orphan or unmapped assets: none at dispatch because every item is visibly deferred.
- Cross-region links: source claim to local proposal to current CVF owner.
- Drift check: PASS for path/hash receipt only.
- Rebuildability check: exact root, enumeration rule, paths, bytes, hashes, manifest, and ledger are recorded.
- Retrieval boundary: local documentation and registry lookup only.
- Adversarial verification: pending T0 semantic review.
- Knowledge-map verdict: PARTIAL

## Mixed-Origin Derived Synthesis Provenance

| Input or concept | Origin class | Evidence basis | Claim type | Validation method | Current CVF owner | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| four selected absorption themes | OPERATOR_AGENT_CO_DESIGNED | local packet README and source basis | design proposal | full file reading plus owner reconciliation | existing Memory/Truth/Context/Action/evaluation owners | evaluate |
| paper-attributed findings | UPSTREAM_REPOSITORY_BACKED | arXiv identifier carried by source basis | research claim | targeted primary-paper verification | none; evidence input only | verify |
| CVF owner observations | CVF_PUBLIC_DERIVED | local packet source basis | current-CVF claim | current private-provenance source inspection | named current CVF owners | refresh |
| combined contracts, fixtures, and plans | MIXED_ORIGIN | complete 50-file local packet | derived synthesis | terminal ledger and capability-cluster review | existing owners or missing-owner decision | classify |

## Absorption Decision Vector

| Decision axis | Decision | Evidence | Cost boundary |
| --- | --- | --- | --- |
| Knowledge absorption | PENDING_T0 | 50-file manifest and four capability clusters | retain only verified non-duplicate value |
| Direct import | REJECT | local packet is non-authoritative synthesis | CVF-native adaptation only |
| Runtime activation | DEFER | no implementation or live evidence | fresh work order and tests required |
| Authority promotion | DEFER | current CVF owners remain canonical | independent review and operator selection required |

## System-Chain Value Review

| Chain component | Evidence path | Existing CVF owner/gap | Value disposition | Readiness disposition | Next action |
| --- | --- | --- | --- | --- | --- |
| epistemic admission | `01_MEMORY_EPISTEMIC_ADMISSION/` | Memory Foundation and retrieval policy | pending owner delta | design candidate only | verify current seam |
| retrieval traceability | `02_RETRIEVAL_TRUTH_TRACEABILITY/` | Memory and Truth Foundations | pending owner delta | design candidate only | verify field-level overlap |
| adversarial provenance evaluation | `03_ADVERSARIAL_TRUST_PROVENANCE_EVAL/` | memory tests and evaluation owners | pending test delta | test candidate only | verify scenarios |
| utility under attack | `04_UTILITY_UNDER_ATTACK/` | benchmark/evaluation owner to locate | possible new evaluation delta | schema/fixture candidate only | verify metrics and cost |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
| --- | --- | --- | --- | --- | --- |
| epistemic admission | decision-bearing memory eligibility concept | DOCTRINE_ADAPTED | `docs/reference/memory_foundation/` | verify exact current gap | no runtime mutation |
| retrieval traceability | evidence/truth reference fields | PACKAGE_CANDIDATE | current Memory and Truth contracts | field-level owner comparison | no direct import |
| adversarial trust scenarios | negative semantic test candidates | CHECKER_CANDIDATE | current memory tests/evaluation owner | retain only uncovered cases | no checker wiring |
| utility-under-attack metrics | benchmark trade-off candidate | RUNTIME_CANDIDATE | existing evaluation/benchmark owner or gap | value/cost decision first | no execution |
| packet work orders and authority prose | external process material | REJECT_DIRECT_IMPORT | current CVF dispatch authority | classify as duplicate/input only | no authority transfer |
| duplicate guidance | already-owned semantics | NO_PACKAGE_OR_RUNTIME_VALUE | named current owner | close with evidence | no package/runtime value |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| stored/retrieved is not true | `docs/reference/memory_foundation/`; `docs/reference/truth_foundation/` | CONFIRMED_EXISTING | likely doctrine duplicate | verify and close duplicate rows |
| omitted provenance defaults to one | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | NEW_FINDING | possible fail-open epistemic default | assess severity and consumer reach |
| retrieval truth-reference binding | `docs/reference/memory_foundation/`; `docs/reference/truth_foundation/` | ENRICH_EXISTING | possible field/seam delta | source and owner reconciliation |
| utility-under-attack benchmark | OWNER_SURFACE_NOT_FOUND | OWNER_SURFACE_NOT_FOUND | possible new benchmark methodology | locate owner before retention |
| local implementation/work orders | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`; `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/` | REJECT_DIRECT_IMPORT | no authority transfer | retain as proposal evidence only |

## Absorption Efficiency And Provenance Reuse

manifestLedgerReuse: REUSE_IF_FRESH
semanticReviewUnit: CAPABILITY_CLUSTER
defaultValuePosture: PRESERVE_UNTIL_CONTRADICTED
additionalValueProbe: SKIP_UNLESS_NAMED_GAP
latencyBudget: SINGLE_PASS_BOUNDED
intakePriority: LOCAL_SYNTHESIZED_PACK_FIRST
localSemanticInspection: FILE_AND_USE_CASE_CONTENT_REQUIRED
mappingAction: DIRECT_WORK_ORDER_FOR_HIGH_FIT_CLUSTERS
deliverySequence: WORK_ORDER_THEN_WORKER_THEN_INDEPENDENT_REVIEWER
namePatternInference: FORBIDDEN_AS_VALUE_DISPOSITION
upstreamConsultation: TARGETED_FOR_PROVENANCE_OR_GAP

## Rescan Intelligence Hardening

- Original source artifact: operator-supplied local folder
  `.private_reference/legacy/CVF 13.08/CVF_MEMORY_POISONING_ABSORPTION`.
- Predecessor intake artifact: none for this exact folder; current CVF memory,
  truth, retrieval, provenance, evaluation, and utility owners are comparison
  surfaces, not predecessor intake proof.
- Delta ledger status: `PARTIAL`; dispatch records expected categories and the
  worker must replace them with source-read evidence.
- Routing matrix status: `DO_NOW` for bounded intake; all runtime or
  implementation effects use `SEPARATE_RUNTIME_TRANCHE` or remain out of scope.
- Semantic sampling status: dispatch samples top-level provenance and claim
  boundaries; worker must sample every semantic cluster after full read.
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Delta category | Dispatch evidence |
|---|---|
| UNCHANGED_FROM_INTAKE | Existing CVF contracts already separate similarity from evidence and restrict raw-memory reinjection; worker must verify exact overlap. |
| CHANGED_DISPOSITION | Any source proposal retained after verification must be adapted to the current owner instead of imported as legacy text. |
| NEW_FINDING | Candidate omitted-provenance/default-trust risk requires consumer-reach, severity, duplicate, and primary-source verification. |
| REMOVED_OR_REJECTED | Source instructions, universal claims, direct imports, and implementation effects are rejected from T0. |

### Follow-Up Routing Matrix

| Routing lane | Disposition |
|---|---|
| DO_NOW | Reconcile 50 files, fully read them, verify the cited paper, compare current owners, and issue one value decision. |
| RESOLVED_BY_DESIGN | Record source concepts already controlled by current CVF contracts as overlap rather than reopening work. |
| STRATEGIC_OPERATOR_DECISION | Present any source-backed, serious, non-duplicate, net-positive successor candidate for operator selection. |
| SEPARATE_RUNTIME_TRANCHE | Any code, runtime policy, provider/live proof, deployment, or public-sync change. |
| OUT_OF_SCOPE | Executing source instructions, direct import, secret/account use, and claims of universal memory-poisoning protection. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| MPA-AI-T0-RS1 | `SOURCE_BASIS.md` | packet derives from paper `arXiv:2608.21230` plus synthesis | DO_NOW | Is the local packet itself sufficient empirical evidence? | FAIL_AS_PRIMARY_EVIDENCE - verify paper directly |
| MPA-AI-T0-RS2 | `CLAIM_BOUNDARY.md` | packet does not prove production readiness | OUT_OF_SCOPE | Could intake imply deployed protection? | PASS - dispatch forbids runtime and production claims |
| MPA-AI-T0-RS3 | `OWNER_MAPPING.md` | concepts map onto several current CVF owners | DO_NOW | Are filename mappings proof of novelty or value? | FAIL_AS_VALUE_EVIDENCE - require exact owner comparison |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External repo or copied folder |
| Chain map route | local folder receipt to semantic ledger to paper/current-owner verification to overlap/value decision |
| Matching local-view guard | `governance/compat/check_external_absorption_core.py`; `governance/compat/check_mixed_origin_derived_synthesis_absorption.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_corpus_to_knowledge_map_reconciliation.py`; `governance/compat/check_absorption_blindspot_control_presence.py`; `governance/compat/check_corpus_scan_registry.py`; `governance/compat/check_task_governance_route.py` |
| Owner surface | paired work order, final T0 audit, worker return, and corpus registry entry |
| Disposition | ADAPT only verified non-duplicate value; REJECT direct import; DEFER implementation |
| Claim boundary | no implementation, runtime, provider/live, public, deployment, or production behavior |

## Claim Boundary

This baseline authorizes inventory reconciliation, full local source reading,
targeted primary-paper verification, current-owner comparison, and a bounded
value decision. It authorizes no source execution, implementation, dependency,
runtime/provider/account use, live proof, public sync, deployment, production,
or direct import.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance intake; no public-sync batch is authorized.
