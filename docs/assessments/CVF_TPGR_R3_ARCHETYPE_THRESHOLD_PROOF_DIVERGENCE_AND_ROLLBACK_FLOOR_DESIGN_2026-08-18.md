# CVF TPGR-R3 Archetype Threshold Proof Divergence And Rollback Floor Design

Memory class: governed-planning-assessment

docType: baseline

Status: COMPLETE_PENDING_REVIEW

Batch ID: TPGR-R3

Date: 2026-08-18

executionBaseHead: `cdb18064ace9e92e3936640a0fdb6fe5e050116e`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Responds to work order:
`docs/work_orders/CVF_AGENT_WORK_ORDER_TPGR_R3_ARCHETYPE_THRESHOLD_PROOF_DIVERGENCE_AND_ROLLBACK_FLOOR_DESIGN_2026-08-18.md`

Paired baseline authority:
`docs/baselines/CVF_GC018_TPGR_R3_ARCHETYPE_THRESHOLD_PROOF_DIVERGENCE_AND_ROLLBACK_FLOOR_DESIGN_2026-08-18.md`

## Purpose

Pre-register per-archetype (A1-A6) proof floors, TPGR cost ceilings,
divergence tolerances, freshness invalidators, rollback triggers, and
anti-self-downgrade assertion ownership for Task-Proportional Governance
Routing (TPGR), before any implementation is authorized. This is design
evidence and one disposition, not implementation. It changes no standard,
checker, registry, catalog, hook, or source corpus.

## Source / Predecessor Evidence

| Source | Identity | Authority use |
| --- | --- | --- |
| paired baseline | `docs/baselines/CVF_GC018_TPGR_R3_ARCHETYPE_THRESHOLD_PROOF_DIVERGENCE_AND_ROLLBACK_FLOOR_DESIGN_2026-08-18.md` | complete execution authority for this design |
| paired work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_TPGR_R3_ARCHETYPE_THRESHOLD_PROOF_DIVERGENCE_AND_ROLLBACK_FLOOR_DESIGN_2026-08-18.md` | task manifest, Archetype Threshold Matrix, Threshold Precedence rules, Hostile Test Design Matrix, Measurement Protocol, acceptance criteria |
| R2G assessment | `docs/assessments/CVF_TPGR_R2G_GENERALIZED_ABSORPTION_ROUTING_FEASIBILITY_ASSESSMENT_2026-08-17.md` | predecessor A1-A6 evidence dataset; Layer A owner map; conditional lifecycle interface candidate; disposition `PROCEED_TO_THRESHOLD_DESIGN` |
| R2G worker return | `docs/reviews/CVF_TPGR_R2G_GENERALIZED_ABSORPTION_ROUTING_FEASIBILITY_ASSESSMENT_WORKER_RETURN_2026-08-17.md` | Independent Reviewer Addendum correcting checker counts to 193/79/114 |
| R2G reconciliation and rescope | `docs/reviews/CVF_TPGR_SECOND_UPGRADE_GENERALIZATION_CRITIQUE_RECONCILIATION_AND_R2_RESCOPE_2026-08-17.md` | Conditional Lifecycle Route Graph, Scoped Claim Vocabulary Candidate, Generalized Architecture Boundary |
| TPGR routing standard | `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md` | Mandatory Classification enums, Mandatory Escalation rules, TPGR-T0 Legacy Full-Gate Interlock (shadow-only) |
| external critique | `docs/reviews/CVF_TPGR_SECOND_UPGRADE_EXTERNAL_CRITIQUE_2026-08-17.md` | reconciled advisory risk input on self-downgrade, stale-receipt survival across checker hardening, and rollback tiering; `NOT_CVF_SOURCE` until reconciled |

## Scope / Methodology

The worker captured `executionBaseHead` = `cdb18064ace9e92e3936640a0fdb6fe5e050116e`
and confirmed a clean worktree (`git status --short --untracked-files=all`
returned no output) before any edit. The worker read in full: the paired
baseline, the paired work order, `CVF_SESSION_MEMORY.md`, the bootstrap read
model, `AGENT_HANDOFF_V59_2026-08-11.md`, the guard orientation index, the
literal-format gotchas reference, the R2G reconciliation review, the R2G
assessment (all six archetype worksheets and every supporting section), the
R2G worker return (including its Independent Reviewer Addendum), the TPGR
routing standard, and the external critique. The worker also read the
applicable `governance/compat/check_*.py` checker sources listed in the
Checker Source Read-Ahead Block before authoring either output file.

Per the Measurement Protocol, this design uses R2G's A1-A6 evidence as the
predecessor dataset. No new corpus scan, source intake, network access, or
re-derivation of R2G's registry/catalog counts was performed. Where this
design cites the checker-count evidence, it uses the R2G worker return's
Independent Reviewer Addendum's corrected figures verbatim: 193 `check_*.py`
files, 80 pre-implementation command rows, 79 direct checker invocations, one
wrapper (`run_agent_automation_assist.py`), and 114 checker files not
directly referenced by that phase's command rows.

No standard, checker, registry, catalog, hook, or router is modified by this
assessment. No selective execution is authorized or claimed;
`selectiveExecutionAuthorized` remains `false` per the TPGR standard, verified
directly by `check_task_governance_route.py` at this executionBaseHead
(`COMPLIANT`, 0 violations, `Legacy gate disposition: RUN_FULL_LEGACY_BUNDLE`).

## Canonical Fact-Owner Map

One canonical fact-owner map. No second truth store is created; every row
below cites an existing CVF-governed owner by reference, consistent with the
R2G reconciliation's Generalized Architecture Boundary (Layer A owns
knowledge-intake semantics; Layer B/TPGR owns control routing by reference
only).

| Fact | Canonical owner | Worker-assertable? | Evidence class |
| --- | --- | --- | --- |
| corpus registration / scope path | `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md` (GC-051); `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | NOT_WORKER_ASSERTABLE - registry entry must exist and be current | OBSERVED when a registry entry is independently re-parsed |
| structural enumeration / manifest / hash | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | NOT_WORKER_ASSERTABLE - manifest/hash must be independently recomputed, not declared | OBSERVED when recomputed against current disk state |
| terminal processing ledger status | same core standard | NOT_WORKER_ASSERTABLE - ledger rows are machine-checked, not self-declared | OBSERVED via `check_external_absorption_core.py` |
| overlap / novelty classification | same core standard | WORKER_PROPOSES, OWNER_CONFIRMS - worker may propose a classification; reviewer/owner confirms before it is current | PROJECTED until reviewer confirmation |
| mixed-origin provenance separation | `docs/reference/external_agent_review/CVF_MIXED_ORIGIN_DERIVED_SYNTHESIS_ABSORPTION_STANDARD.md` | NOT_WORKER_ASSERTABLE - dual-manifest separation is machine-checked | OBSERVED via `check_mixed_origin_derived_synthesis_absorption.py` |
| seven-gate blind-spot discipline | `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md` | NOT_WORKER_ASSERTABLE | OBSERVED via `check_absorption_blindspot_control_presence.py` |
| corpus completeness / report integrity | `docs/reference/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_STANDARD_2026-06-01.md` | NOT_WORKER_ASSERTABLE | OBSERVED via `check_corpus_completeness_report_integrity.py` |
| corpus-to-knowledge-map reconciliation | `docs/reference/CVF_CORPUS_TO_KNOWLEDGE_MAP_RECONCILIATION_STANDARD_2026-06-01.md` | NOT_WORKER_ASSERTABLE | OBSERVED via `check_corpus_to_knowledge_map_reconciliation.py` |
| external intake input-type routing | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | WORKER_DECLARES canonical `Input type` token only; chain-map route itself is fixed by the chain map, not the worker | OBSERVED via `check_external_knowledge_intake_routing.py` |
| routing/control-selection classification (`taskKind`, `authorityImpact`, `externalEffect`, `dataSensitivity`, `reversibility`, `sourceScale`, `delegation`, `novelty`) | `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md` (TPGR-T0) | WORKER_DECLARES the manifest; router (`route_task_governance.py`) independently computes the route; a self-downgraded manifest that omits a real authority/effect touch is a diff-derived detection gap this design must not create | OBSERVED via `check_task_governance_route.py`; router output is authoritative over worker self-declaration |
| `decisionUncertainty` (this design's proposed threshold field) | reviewer-owned policy or evidence-conflict derivation only, per Threshold Precedence Rule 3 | NOT_WORKER_ASSERTABLE - never a worker-controlled downgrade input | PROPOSED design invariant; not yet a machine-checked field |
| checker-closure version / source-hash freshness | filesystem state of `governance/compat/check_*.py` at time of receipt versus at time of reuse | NOT_WORKER_ASSERTABLE - must be independently recomputed | OBSERVED when recomputed; UNKNOWN as a machine-bound receipt field, since no such field exists in any current registry schema |
| authority impact / material doctrine change | the specific CVF owner surface named by the change (e.g. `AGENTS.md`, a `docs/reference/` standard, a checker, a schema, a registry) | NOT_WORKER_ASSERTABLE - authority impact is determined by which owner surface is touched, never by worker self-report of triviality | OBSERVED via diff-derived path-family detection, not manifest declaration |
| evidence freshness (age/staleness of a prior receipt) | the specific predecessor artifact's own commit/hash plus current HEAD state of anything it depends on | NOT_WORKER_ASSERTABLE - freshness is a comparison between two independently observable states, not a worker opinion | OBSERVED when both states are independently read |
| source scale (`NAMED_FILES` / `BOUNDED_CLUSTER` / `CORPUS`) | the actual file/path set touched, independently countable | WORKER_DECLARES the manifest value; independently verifiable by counting the diff | OBSERVED |

No row above proposes a new registry, lifecycle, command catalog, or truth
store. Every "canonical owner" column cites a CVF standard, schema, or
checker that already exists at this `executionBaseHead`.

## Route Outcomes And Deterministic Precedence

Exactly three route outcomes, in fixed evaluation order (each outcome is
evaluated only if the prior one is not triggered):

1. `FULL_LAYER_A_REQUIRED` - selected first. Any archetype whose objective
   input facts are missing, contradictory, owner-unverified, show material
   authority impact, or touch an always-on/effect-triggered Layer A control
   routes here regardless of file count or worker cost preference (Threshold
   Precedence Rule 1). This is the safe default and the default fail-closed
   posture for A1, A2, A4, and A6 per the work order's Archetype Threshold
   Matrix.
2. `ESCALATE_FOR_REVIEW` - selected second, only when `FULL_LAYER_A_REQUIRED`
   is not triggered but a named ambiguity exists: owner/hash/freshness
   ambiguity (A3), authority or reuse ambiguity (A5), or any evidence
   conflict/contradiction the worker cannot resolve from existing canonical
   owners (Threshold Precedence Rule 2, Rule 3).
3. `LIGHT_ROUTE_ALLOWED` - selected last, only when every objective input
   fact is present, owner-verified, current, and consistent, and no
   always-on Layer A control is omitted from the cost denominator (Threshold
   Precedence Rule 5).

Precedence is deterministic and monotonic: an archetype may only move toward
a stricter outcome as new facts appear, never from a stricter outcome to a
lighter one without a fresh independent owner confirmation (mirrors the TPGR
standard's "Escalation is monotonic... may not self-downgrade after
dispatch"). Missing or contradictory owner facts cannot select
`LIGHT_ROUTE_ALLOWED` under any circumstance (Rule 2).

## Threshold Precedence And Fail-Closed Rules (Binding Constraints)

The following six rules from the paired work order are hard constraints on
every threshold in this design; no archetype worksheet below violates any of
them:

1. Authority/materiality and external-effect escalation overrides file
   count, reversibility, and worker cost preference.
2. Missing or contradictory owner facts cannot select `LIGHT_ROUTE_ALLOWED`.
3. `decisionUncertainty` is derived from evidence conflicts or reviewer-owned
   policy, never accepted as a worker-controlled downgrade input.
4. Any relevant source/schema/checker/catalog change expires current route
   eligibility from the earliest affected dependency node; historical
   receipt evidence remains immutable.
5. Cost thresholds cannot omit required semantic reading or always-on Layer A
   controls from the denominator.
6. A route with unknown maintenance cost cannot claim positive net value; it
   must remain projected and carry an escalation or measurement requirement.

## Anti-Self-Downgrade Invariants (Binding Constraints)

From the paired baseline, also binding on every threshold below:

- `decisionUncertainty`, authority impact, evidence freshness, and source
  scale cannot be accepted solely from the executing worker's declaration.
- Missing, malformed, contradictory, or owner-unverified facts route to
  `ESCALATE_FOR_REVIEW` or `FULL_LAYER_A_REQUIRED`, never the light route.
- A small file count cannot override material authority impact.
- A prior receipt remains historical evidence but loses current eligibility
  from the earliest affected node when a relevant source, schema, checker, or
  command-catalog dependency changes.
- No threshold may omit an always-on or effect-triggered Layer A control.

These invariants directly reconcile the external critique's three strongest
failure modes (Q4/Q7/Q2 in the external critique): the checker-mapping cost
basis, `decisionUncertainty` self-downgrade, and stale-receipt survival
across checker hardening. This design addresses each below in the per-
archetype freshness-dependency fields and in the Dependency Invalidation
Graph, without adopting the critique's unreconciled schema-field proposals
as CVF authority (the critique remains `NOT_CVF_SOURCE`; only the already-
accepted R2G reconciliation and this design's own reasoning are cited as
authority).

## A1-A6 Threshold Worksheets

### A1 - New upstream corpus (first intake, no inherited receipt)

| Field | Value |
| --- | --- |
| Objective input facts | source identity (pinned mirror/copied folder), authority boundary, file count, corpus registration state |
| Fact owner | GC-051 registry (`docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md`); `CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` for manifest/ledger |
| Route outcome | `FULL_LAYER_A_REQUIRED` (matches the work order's Archetype Threshold Matrix default) |
| Minimum proof floor | full hidden/no-ignore structural enumeration, per-file terminal processing ledger, GC-051 registration, blind-spot Gates 1-3, source-mirror migration control if applicable, before any TPGR classification is eligible to be recorded at all |
| Maximum TPGR cost ceiling | one classification manifest plus one routing receipt only; TPGR must add zero duplicate intake ceremony on top of the mandatory first-intake floor (per R2G's A1 worksheet, this ceiling was not exceeded in the observed 231-file case) |
| Divergence tolerance | zero tolerance: any missing manifest, unreconciled hash, or incomplete ledger row forces `FULL_LAYER_A_REQUIRED`, never a lighter route, because A1 is by definition the no-inheritance case |
| Freshness invalidators | upstream commit change; manifest hash drift; any change to `CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` or `check_external_absorption_core.py`; any blind-spot standard/checker hardening |
| Rollback trigger / safe route | any post-registration discovery that the manifest or ledger is incomplete rolls back to `FULL_LAYER_A_REQUIRED` at C1 (structural enumeration), never silently to a lighter route; historical partial receipts remain as evidence but lose current eligibility |
| Assertion ownership | worker may declare `sourceScale: CORPUS` and `authorityImpact` per the TPGR manifest fields; worker may NOT self-declare `CORPUS_REGISTERED`, `STRUCTURALLY_ENUMERATED`, or `PROCESSING_LEDGER_RECONCILED` - those require the actual GC-051 entry and core-standard checker evidence to exist |
| Evidence labels | OBSERVED: R2G's 231-file A1 case (`COMPLETE_VERIFIED`); PROJECTED: any future live A1 TPGR receipt, since none exists yet |
| Unresolved uncertainty | UNKNOWN: no machine-bound TPGR receipt yet proves recurring routing-maintenance cost for a future A1 intake; this cannot relax `FULL_LAYER_A_REQUIRED` and remains a future measurement requirement under Rule 6 |
| Hostile example | a worker claims `LIGHT_ROUTE_ALLOWED` for a "small" first-intake corpus citing only file count; per Rule 1 and the Anti-Self-Downgrade Invariants, a small file count cannot override the fact that no inherited receipt exists, so this fails closed to `FULL_LAYER_A_REQUIRED` regardless of size |

### A2 - Mixed-origin local synthesis (provenance-backed, owner-agent co-designed)

| Field | Value |
| --- | --- |
| Objective input facts | dual-origin file counts (upstream mirror vs. local proposal), manifest/ledger hashes, adversarial-sample coverage, `.private_reference/legacy/` classification state |
| Fact owner | `CVF_MIXED_ORIGIN_DERIVED_SYNTHESIS_ABSORPTION_STANDARD.md`; `CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Route outcome | `FULL_LAYER_A_REQUIRED` until reusable receipts and owner mapping are current (work order default); may relax only for a later named-cluster reuse subcase that itself resolves to A3-shaped K1 entry |
| Minimum proof floor | full dual-manifest enumeration/hash for both origins; terminal ledger for all files; adversarial full-read of the highest-risk cluster (not sampled); dual-manifest separation control verified (upstream never cited as proof of proposal claims) |
| Maximum TPGR cost ceiling | one classification manifest; TPGR adds no second full-corpus pass; a later cluster review of the same corpus may route directly to K1 using existing manifest/ledger receipts instead of re-enumerating, per R2G's A2 worksheet, but semantic reading of the selected cluster is never inherited |
| Divergence tolerance | zero tolerance on origin-separation controls; any single `ADAPTED` row promoting proposal-folder material to CVF source without an explicit owner-fit resolution forces escalation |
| Freshness invalidators | either mirror's commit drift; any change to the mixed-origin standard or its checker; any change to the adversarial-sampling requirement in the blind-spot standard |
| Rollback trigger / safe route | any detected origin-separation violation (proposal material cited as upstream-verified fact, or vice versa) rolls back immediately to `FULL_LAYER_A_REQUIRED`; the corpus's manifest/ledger receipts remain valid historical evidence for file-count/hash purposes but the specific violating claim is void |
| Assertion ownership | worker may declare `novelty: OWNER_COMPOSITION`; worker may NOT self-declare that a `NO_NEW_VALUE`/`REJECTED` group requires no further semantic reading - that determination stays with the terminal ledger and adversarial-sample evidence already recorded, not a fresh worker opinion |
| Evidence labels | OBSERVED for R2G's 764-file A2 case's own measured facts; PROJECTED for any future TPGR-routed reuse of that corpus, since no such reuse has yet occurred |
| Unresolved uncertainty | UNKNOWN: the maintenance cost and exact admission boundary for a future A2 named-cluster reuse have not been measured; until an exact subcase independently satisfies the A3 proof floor, A2 remains `FULL_LAYER_A_REQUIRED` |
| Hostile example | a worker declares `decisionUncertainty: LOW` for a mixed-origin cluster while the terminal ledger shows unresolved `NO_NEW_VALUE` rows still under dispute; per Rule 3 and Anti-Self-Downgrade Invariants, `decisionUncertainty` is never worker-declarable as a downgrade input, so this fails closed to `ESCALATE_FOR_REVIEW` |

### A3 - Accepted-corpus cluster (fresh reusable receipts)

| Field | Value |
| --- | --- |
| Objective input facts | named cluster file list, source corpus identity, corpus's own C0-C2 receipt currency, prior owner-projection state |
| Fact owner | the corpus's own GC-051 entry plus `CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md`; the specific prior accepted work-order/worker-return/completion-review cycle that produced the receipt |
| Route outcome | `LIGHT_ROUTE_ALLOWED` only with current accepted receipts and exact named scope (work order default); `ESCALATE_FOR_REVIEW` on any owner/hash/freshness ambiguity |
| Minimum proof floor | the underlying corpus's C0-C2 receipts must be current (not expired per the Dependency Invalidation Graph below); the named cluster's own file set must be exactly and explicitly listed; independent reviewer diff audit before first edit remains always-on |
| Maximum TPGR cost ceiling | near-zero marginal TPGR cost is the target and the one required positive bounded case per R2G's Measurement Protocol; observed R2G ceiling: one bounded reviewer repair round, focused-test regression, reviewer-fast, pre-commit - no additional TPGR-specific ceremony beyond the existing work-order/worker-return/completion-review cycle |
| Divergence tolerance | zero tolerance on scope drift: if the named cluster's actual file set diverges even by one file from the exact registered scope, the route is not eligible until re-verified; this is the archetype most exposed to quiet scope creep because its whole value proposition depends on an exact, narrow, named list |
| Freshness invalidators | T7/owner-surface change; contract hash drift; any hardening to a checker in the closure that produced the original corpus receipt (see Dependency Invalidation Graph); underlying corpus GC-051 entry re-registration or status change |
| Rollback trigger / safe route | any hash mismatch between the named cluster's current file contents and the receipt's recorded hashes rolls back to `ESCALATE_FOR_REVIEW`; if the underlying corpus receipt itself is stale, rolls back further to `FULL_LAYER_A_REQUIRED` for the affected scope only, not the entire corpus |
| Assertion ownership | worker may declare the named file list and propose `CLUSTER_SEMANTICALLY_READ`; worker may NOT self-declare that the underlying corpus's C0-C2 receipts remain current - freshness must be independently recomputed against the Dependency Invalidation Graph, not asserted |
| Evidence labels | OBSERVED for R2G's A3 review-cost telemetry (`reviewRoundCount: 1`, `WITHIN_FAST_PATH_TARGET`); PROJECTED for any TPGR-specific overhead delta, since no TPGR receipt was actually attached to that review |
| Unresolved uncertainty | UNKNOWN: no current machine field binds a cluster receipt to relevant owner/checker versions, so recurring freshness-maintenance cost is unmeasured; reviewer recomputation remains mandatory and ambiguity routes to `ESCALATE_FOR_REVIEW` |
| Hostile example | a worker reuses a corpus's accepted receipts for a "new" cluster whose file list quietly includes two files outside the original named scope, citing the corpus's overall freshness; per the exact-named-scope requirement and Rule 2, this fails closed to `ESCALATE_FOR_REVIEW` because the actual touched scope was never owner-verified |

### A4 - Upstream delta (pinned predecessor, changed source identity)

| Field | Value |
| --- | --- |
| Objective input facts | prior pinned predecessor identity, changed source commit/identity, delta ledger classification (`UNCHANGED_FROM_INTAKE`, `CHANGED_DISPOSITION`, `NEW_FINDING`, `REMOVED_OR_REJECTED`) |
| Fact owner | the specific prior closure's own disposition trail plus the current live owner surface the delta is compared against (never the owner surface as it stood at the prior closure) |
| Route outcome | `FULL_LAYER_A_REQUIRED` for the affected delta scope (work order default); the D1 node licenses only `DELTA_RECONCILED`, never a broader claim |
| Minimum proof floor | full re-read of every file in the delta scope (a terminal ledger row alone is explicitly not full-read proof per the TPGR standard); field-by-field re-comparison against the actual current owner surface; earliest-affected-node identification |
| Maximum TPGR cost ceiling | one delta-reconciliation classification only; TPGR must not reduce the mandatory full re-verification of the delta scope itself - R2G's A4 worksheet found the dominant cost is the mandatory full delta re-verification, and TPGR correctly does not attempt to reduce it |
| Divergence tolerance | zero tolerance on scope boundary: only the sub-claims already `CONFIRMED_EXISTING` under a still-current comparison may be treated as settled; every sub-claim touched by the delta, or downstream of an earliest-affected node, requires fresh comparison |
| Freshness invalidators | any further upstream commit change beyond the one already reconciled; any change to the specific CVF owner surface the delta was compared against |
| Rollback trigger / safe route | rolls back to `FULL_LAYER_A_REQUIRED` from the earliest affected node only; unaffected historical evidence (settled sub-claims from before that node) remains historical and is not re-invalidated, per Rule 4 |
| Assertion ownership | worker may propose which sub-claims are `UNCHANGED_FROM_INTAKE`; worker may NOT self-declare the earliest affected node without independently re-deriving it from the actual current owner surface, not from memory of the prior closure's narrative |
| Evidence labels | OBSERVED for the completed R2G A4 audit (107-file re-intake); PROJECTED for how a TPGR receipt would formally express "earliest affected node," since D1 is not yet implemented as a machine node |
| Unresolved uncertainty | UNKNOWN: D1 has no implemented machine representation for the earliest affected node or its maintenance cost; the affected delta scope therefore retains `FULL_LAYER_A_REQUIRED` until a future governed design validates that representation |
| Hostile example | a worker inherits a prior delta's disposition trail wholesale, asserting `DELTA_RECONCILED` for the full 107-file scope while only having freshly compared 6 of 9 previously-settled legacy files and skipping the 98-file upstream mirror comparison entirely; this fails closed to `FULL_LAYER_A_REQUIRED` for the unreconciled 98-file portion, per Rule 5 (cost thresholds cannot omit required semantic reading) |

### A5 - Small named advisory item (not a reusable corpus)

| Field | Value |
| --- | --- |
| Objective input facts | one named document identity, its `Input type` canonical token, whether it is being cited as advisory or as authority |
| Fact owner | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md`; the item's own explicit Claim Boundary/Authority Boundary section |
| Route outcome | `ESCALATE_FOR_REVIEW` on any authority or reuse ambiguity (work order default); otherwise the cheapest legitimate `LIGHT_ROUTE_ALLOWED` case in this matrix, per R2G's A5 finding that the existing ceremony floor already works without TPGR |
| Minimum proof floor | source verification of every named CVF standard the item references; an explicit, unambiguous Claim Boundary or Authority Boundary statement that the item is advisory only until independently reconciled |
| Maximum TPGR cost ceiling | effectively zero beyond the existing External Knowledge Intake Routing table already required by the chain map; a routing receipt confirming the skip of GC-051/manifest/ledger machinery was correct, not a new capability |
| Divergence tolerance | zero tolerance on authority-boundary violation: any citation of the item as canonical authority in a Source Authority table, Source Verification ACCEPT row, corpus manifest, closure proof, or roadmap/work-order evidence is an immediate escalation trigger, not a divergence to be tolerated |
| Freshness invalidators | a re-issued or corrected version of the same document; any change to the chain map's canonical `Input type` enum |
| Rollback trigger / safe route | if the item is later found cited as authority anywhere, rolls back to `ESCALATE_FOR_REVIEW` and the citation must be corrected; the item's own advisory content remains valid evidence of what it said, but not of CVF authority |
| Assertion ownership | worker may declare the canonical `Input type` token; worker may NOT self-declare `authorityImpact: NONE` when the item's content could plausibly be read as changing CVF authority - that determination requires the item's own explicit Claim Boundary plus reviewer confirmation |
| Evidence labels | OBSERVED - R2G's A5 case (the external critique itself, prior to this R3 tranche) was processed exactly this way under current rules, with no TPGR receipt attached |
| Unresolved uncertainty | UNKNOWN: no machine receipt proves that an advisory item's authority boundary remains unambiguous after later citation or revision; reviewer confirmation remains required and ambiguity routes to `ESCALATE_FOR_REVIEW` |
| Hostile example | a worker treats a small advisory critique's recommendations as pre-approved because "it is just one file"; per the Anti-Self-Downgrade Invariants, file count is explicitly barred from overriding authority impact, so any content that reads as changing CVF authority forces `ESCALATE_FOR_REVIEW` regardless of the one-file scale (this is exactly the disposition the R2G/R3 reconciliation chain itself already enforces on the external critique used as A5's own primary evidence) |

### A6 - Downstream project source (PROJECT_SOURCE boundary)

| Field | Value |
| --- | --- |
| Objective input facts | project scope path, existing `PROJECT_SOURCE` registry entry (or its absence), whether project findings are being cross-referenced or merged into CVF authority |
| Fact owner | GC-051 Rule 5 (`docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md`); `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` |
| Route outcome | `FULL_LAYER_A_REQUIRED` when project corpus scanning is claimed (work order default); registration-before-scan is mandatory exactly as for any other corpus type, with no lighter-weight rule |
| Minimum proof floor | GC-051 registration-before-scan for the exact `scopePaths`; explicit cross-reference (not merge) of any CVF-relevant finding against CVF's own findings |
| Maximum TPGR cost ceiling | one registry entry per project scope; no capability beyond the existing routing receipt every other corpus-type entry would receive |
| Divergence tolerance | zero tolerance on the authority-promotion boundary: project material is never eligible for treatment as CVF authority; any route that would treat project material as promoting CVF authority must escalate, never fast-route, regardless of how small or clean the project material appears |
| Freshness invalidators | project source-tree change under an already-registered `scopePaths` entry; the current registry schema has no automatic drift-detection field for project sources distinct from other corpus types, so this remains a manual/process invalidator, not yet machine-bound |
| Rollback trigger / safe route | any detected authority-promotion attempt (project finding treated as CVF-owner fact without cross-reference) rolls back to `FULL_LAYER_A_REQUIRED`; the registry entry itself remains valid registration evidence |
| Assertion ownership | worker may declare `dataSensitivity: PRIVATE_REPO` (or as the project declares) and `authorityImpact: NONE` for pure project-source reads; worker may NOT self-declare that a project finding is cross-reference-complete - that remains an owner/reviewer confirmation |
| Evidence labels | OBSERVED for the recomputed 37-entry `PROJECT_SOURCE` count from R2G; PROJECTED for how a TPGR receipt would mark the authority-boundary distinction machine-readably, since no such field exists in the current registry schema |
| Unresolved uncertainty | UNKNOWN: the current registry has no project-specific automatic drift detector, so freshness and recurring maintenance cost remain manual and unmeasured; unknown drift keeps the affected project scope on `FULL_LAYER_A_REQUIRED` |
| Hostile example | a worker presents a downstream project's own documentation as CVF canonical authority in a Source Authority table, citing the project's `PROJECT_SOURCE` registration as sufficient; per GC-051 Rule 5 (registration is not authority promotion) and this design's Divergence Tolerance for A6, this fails closed to `FULL_LAYER_A_REQUIRED`/escalation, and the citation is void regardless of registration currency |

## Proof Floors And Evidence-Expiry Rules

A proof floor is the minimum machine-checked evidence that must exist,
independently of worker declaration, before an archetype's route outcome is
eligible. Proof floors never replace Layer A semantic owners; they cite the
owner's own checker output as the floor. Evidence expires (per Rule 4) from
the earliest affected dependency node when any of the following changes:

- the specific standard or checker that produced the receipt's evidence
  (source-hash drift in that checker file);
- the specific schema or registry entry the receipt depends on;
- the specific command-catalog row that would invoke the checker for that
  receipt's evidence class;
- the actual current owner surface content the receipt was compared against
  (for D1/A4, this is the live source, not a cached copy).

Historical receipt evidence remains immutable: an expired receipt is not
deleted or rewritten; it is marked as no-longer-current for routing purposes
while remaining valid evidence of what it recorded at the time.

## Per-Archetype TPGR Cost Ceilings And Maintenance Assumptions

| Archetype | One-time design cost | Per-task routing cost | Recurring maintenance | Escalation cost | Unavoidable Layer A cost (never in TPGR's numerator) |
| --- | --- | --- | --- | --- | --- |
| A1 | this R3 worksheet plus a future R4 interface field set | one classification manifest, one routing receipt | low; GC-051 schema changes propagate via the existing generator | full re-registration if escalated | full first-intake enumeration/hash/ledger (231-file R2G case) |
| A2 | this R3 worksheet | one classification manifest | low; dual-manifest separation control already exists | full corpus-scope re-review if origin-separation violated | full dual-origin enumeration/hash/ledger plus adversarial full-reads (764-file R2G case) |
| A3 | this R3 worksheet | near-zero marginal cost (the one required positive case) | low; T7/T11-style composition already regression-tested | scope re-verification if named-cluster drift detected | the underlying corpus's own C0-C2 floor, already paid once |
| A4 | this R3 worksheet | one delta-reconciliation classification | low; delta re-intake is the designed recurring case | full re-comparison of the affected scope if further drift | full delta-scope re-read and field-by-field comparison (107-file R2G case) |
| A5 | this R3 worksheet | near-zero; existing chain-map table already required | near-zero | full source-verification re-check if authority ambiguity found | one document read and source-verification against named standards |
| A6 | this R3 worksheet | one registry entry per project scope | low; registry entry maintenance only | full escalation if authority-promotion attempted | GC-051 registration-before-scan, already in force |

Per Rule 6, any cell above with UNKNOWN or unmeasured recurring maintenance
(the "live TPGR receipt" case for every archetype, since no TPGR receipt has
ever been attached to a routed task) remains PROJECTED and cannot claim
positive net value; it carries the explicit measurement requirement recorded
in the Observed/Projected/Unknown table below, consistent with R2G's own
Observed/Projected/Unknown Evidence Summary.

## Divergence Tolerances And Fail-Closed Escalation

Divergence, for this design, means an observed mismatch between the current
independently-verifiable state of an objective input fact and the state a
route decision was based on. Every archetype worksheet above states its own
divergence tolerance; the shared cross-archetype rule is:

- zero tolerance on authority-boundary and origin-separation divergence
  (A2, A5, A6): any such divergence is an immediate escalation trigger, never
  a matter of degree;
- zero tolerance on scope-boundary divergence (A3, A4): the named/affected
  scope must be exact, not approximate;
- zero tolerance on missing-inheritance-floor divergence (A1): first intake
  has no divergence budget because it has no prior receipt to diverge from.

There is no archetype in this design where a nonzero divergence tolerance is
proposed. This is a deliberate, conservative design choice consistent with
Rule 1 (materiality overrides cost preference) and the Anti-Self-Downgrade
Invariants: a design that tolerated small divergences would create exactly
the self-downgrade surface the external critique flagged as the plan's
"Self-downgrade through `decisionUncertainty`" failure mode. Any future R4+
tranche that proposes a nonzero divergence tolerance for any archetype must
treat that proposal itself as a stop-condition-adjacent change requiring
independent review, not a default assumption of this design.

## Rollback Triggers And Restored Safe Route

Two-tier rollback structure, informed by (but not adopting as CVF authority)
the reconciled critique's Q10 tiering concept, applied here as this design's
own proposed invariant:

- **Immediate full-scope rollback** (any archetype): any detected authority
  contamination, completion-claim laundering, missing/contradictory
  owner-unverified fact accepted as light-routed, or worker self-declaration
  of `decisionUncertainty`/authority impact/evidence freshness/source scale
  being treated as sufficient on its own. Restored safe route:
  `FULL_LAYER_A_REQUIRED` for the affected scope, full legacy gate bundle per
  TPGR-T0 (`RUN_FULL_LEGACY_BUNDLE`), and reviewer re-confirmation before any
  future light routing of the same scope.
- **Scoped rollback** (single archetype or single named cluster): any
  archetype-specific freshness invalidator fires (see each worksheet's
  Freshness Invalidators row and the Dependency Invalidation Graph below).
  Restored safe route: roll back only to the earliest affected dependency
  node for that scope; unaffected historical receipts and unaffected
  archetypes/clusters remain at their current eligibility, per Rule 4.

In every case, rollback restores the full safe route (never a partial or
"slightly lighter" fallback) and retains historical receipts as immutable
evidence, per the Anti-Self-Downgrade Invariants and Rule 4.

## Dependency Invalidation Graph

This graph lets a reviewer decide relevant-versus-unrelated checker/catalog
changes without enumerating all 193 checker files individually, per
Measurement Protocol step 7. It groups checkers by the Layer A owner
standard/story they gate, using the same standards already cited in the
Canonical Fact-Owner Map and the R2G Layer A owner map; it does not create a
new grouping registry, and it reuses the existing `sourceScale`/path-family
signal already in the TPGR manifest rather than inventing per-checker edges
(a design choice this assessment records as deliberately narrower than the
critique's unreconciled per-checker-record proposal, to avoid recreating the
critique's own Q4 concern inside this design).

| Dependency node | What changing it invalidates | Archetypes affected | Detection method |
| --- | --- | --- | --- |
| GC-051 corpus registry standard or `check_corpus_scan_registry.py` | any receipt whose route outcome depended on a `CORPUS_REGISTERED` fact | A1, A2, A4, A6 | re-run the named checker against the specific registry entry; compare status before/after the standard/checker change |
| `CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` or its checker family (manifest/ledger/overlap/value-conversion) | any receipt whose route outcome depended on `STRUCTURALLY_ENUMERATED` or `PROCESSING_LEDGER_RECONCILED` | A1, A2, A4 | re-run the affected checker against the specific manifest/ledger; a hardening that adds a new required field invalidates receipts missing that field |
| `CVF_MIXED_ORIGIN_DERIVED_SYNTHESIS_ABSORPTION_STANDARD.md` or its checker | any receipt whose route outcome depended on dual-origin separation | A2 | re-run `check_mixed_origin_derived_synthesis_absorption.py` against the specific cluster |
| `CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md` or its checker | any receipt whose route outcome depended on Gate 1-3 (always-on) or Gates 4-7 (conditional) evidence | A1, A2 | re-run `check_absorption_blindspot_control_presence.py`; a hardening from Gate-N to Gate-N+1 as always-on invalidates any receipt that only satisfied the prior always-on set |
| the specific CVF owner surface a delta was compared against (any file under the actual current owner path named in an A4 delta) | the D1 `DELTA_RECONCILED` claim for that specific delta scope only | A4 (scoped to the specific delta) | direct diff of the owner surface between the receipt's comparison time and now |
| the accepted corpus's own upstream C0-C2 receipts (for A3's inherited corpus) | the A3 named-cluster's `LIGHT_ROUTE_ALLOWED` eligibility, cascading from whichever upstream node expired | A3 | trace the corpus's own registry/manifest/ledger currency before trusting an A3 K1 entry |
| `CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` or its checker, or the canonical `Input type` enum | any A5 receipt's routing correctness | A5 | re-run `check_external_knowledge_intake_routing.py` |
| GC-051 Rule 5 text itself, or the `PROJECT_SOURCE` corpus-type schema | any A6 receipt's registration-before-scan claim | A6 | re-check the specific `scopePaths` entry against current Rule 5 text |
| `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md`, `route_task_governance.py`, `check_task_governance_route.py`, or the manifest schema | every archetype's routing classification itself (not the underlying Layer A evidence, but the router's interpretation of it) | A1-A6 (all) | re-run `check_task_governance_route.py --enforce`; per the TPGR standard's own self-referential Mandatory Escalation rule, any router/checker/generator/hook change forces at least `P3_ELEVATED`, which is stricter than any light route this design proposes |
| an unrelated checker with no path-family or standard-owner overlap with the archetype's fact-owner row | nothing for that archetype | none directly, but the always-on `check_task_governance_route.py` and legacy full-gate bundle still execute regardless (TPGR-T0 shadow interlock) | confirm via the Canonical Fact-Owner Map that the changed checker's owning standard does not appear in that archetype's row before concluding "unrelated" |

This graph resolves relevance by matching a changed checker/standard/catalog
path against the specific fact-owner row(s) it governs, not by enumerating
all 193 files. A checker outside every fact-owner row in the Canonical
Fact-Owner Map is, by this design's own reasoning, not a relevant
invalidator for any archetype - but it remains covered by the always-on
TPGR-T0 legacy full-gate interlock regardless, since selective execution
remains unauthorized.

## Hostile Test Design Matrix

| # | Hostile scenario | Expected route outcome | Why (binding rule) |
| --- | --- | --- | --- |
| 1 | one-file input with material doctrine authority impact | `FULL_LAYER_A_REQUIRED` or `ESCALATE_FOR_REVIEW` (never light) | Rule 1: authority/materiality overrides file count; Anti-Self-Downgrade Invariant: small file count cannot override material authority impact |
| 2 | many-file corpus with complete structural receipts but no semantic receipt | `FULL_LAYER_A_REQUIRED` for the semantic-reading portion; `STRUCTURALLY_ENUMERATED`/`PROCESSING_LEDGER_RECONCILED` may be cited, but `CLUSTER_SEMANTICALLY_READ` is never inferred from ledger completeness alone | R2G's own claim-vocabulary finding: "READ does not mean fully understood"; Rule 5 (cost thresholds cannot omit required semantic reading) |
| 3 | worker declares low uncertainty while owner evidence conflicts | `ESCALATE_FOR_REVIEW`; the worker's `decisionUncertainty: LOW` declaration is discarded, not honored | Rule 3 and Anti-Self-Downgrade Invariants: `decisionUncertainty` is never a worker-controlled downgrade input; the underlying evidence conflict is dispositive, not the worker's stated confidence |
| 4 | current receipt generated before a relevant checker hardening | route eligibility expires from the earliest affected node; falls back to `FULL_LAYER_A_REQUIRED` or `ESCALATE_FOR_REVIEW` for the affected scope | Rule 4; Dependency Invalidation Graph row matching the hardened checker's owning standard |
| 5 | unrelated checker change that must not invalidate the receipt | route eligibility is preserved; no rollback | Dependency Invalidation Graph's relevance-matching rule: a changed checker outside every fact-owner row for that archetype is not a relevant invalidator |
| 6 | reused cluster with source hash drift | `ESCALATE_FOR_REVIEW`, escalating to `FULL_LAYER_A_REQUIRED` for the drifted files if the drift is material | A3 worksheet's zero divergence tolerance on scope drift; Rule 4 |
| 7 | mixed-origin cluster whose provenance edge is missing | `FULL_LAYER_A_REQUIRED`; missing provenance is a missing objective input fact | Rule 2: missing or contradictory owner facts cannot select `LIGHT_ROUTE_ALLOWED`; A2 worksheet's dual-manifest separation requirement |
| 8 | project source presented as CVF canonical authority | `FULL_LAYER_A_REQUIRED`/escalation; the citation itself is void | A6 worksheet's zero-tolerance authority-promotion boundary; GC-051 Rule 5 (registration is not authority promotion) |
| 9 | cost estimate excludes required semantic reading | the cost estimate itself is rejected as a valid proof floor; route recomputed with semantic reading restored to the denominator | Rule 5: cost thresholds cannot omit required semantic reading or always-on Layer A controls from the denominator |
| 10 | light-route metadata is missing, malformed, unknown, or contradictory | `ESCALATE_FOR_REVIEW` or `FULL_LAYER_A_REQUIRED`, never `LIGHT_ROUTE_ALLOWED` | Rule 2 and Anti-Self-Downgrade Invariants; mirrors the TPGR standard's own rule that "Unknown values, missing fields, contradictions... produce `REJECTED_ESCALATED`" |

## Decision Table For Missing / Malformed / Conflicting Data

| Data condition | Route outcome | Rationale |
| --- | --- | --- |
| all objective input facts present, owner-verified, current, consistent | `LIGHT_ROUTE_ALLOWED` (only if the archetype's own default posture permits it, e.g. A3/A5) | full proof floor met |
| any single objective input fact missing | `FULL_LAYER_A_REQUIRED` or `ESCALATE_FOR_REVIEW` per archetype default | Rule 2 |
| any objective input fact malformed (wrong type, out of enum range) | `FULL_LAYER_A_REQUIRED` or `ESCALATE_FOR_REVIEW` per archetype default; treated identically to missing | mirrors TPGR standard's "Unknown values, missing fields, contradictions... produce `REJECTED_ESCALATED`" |
| two facts contradict each other (e.g. registry says registered, worker manifest says unregistered) | `ESCALATE_FOR_REVIEW` at minimum, escalating to `FULL_LAYER_A_REQUIRED` if the contradiction touches authority | Rule 3 (evidence conflicts drive escalation, not worker declaration) |
| a fact is present but its freshness cannot be determined (unknown dependency state) | `FULL_LAYER_A_REQUIRED` for the affected scope until freshness is independently established | Rule 6 (unknown maintenance/freshness cannot claim positive net value) |
| worker-declared field conflicts with independently observable state | the independently observable state controls; worker declaration is discarded | Anti-Self-Downgrade Invariants |

## Observed / Projected / Unknown Evidence Summary

| Evidence class | Label | Basis |
| --- | --- | --- |
| R2G's A1-A6 archetype evidence (file counts, verdicts, dispositions) | OBSERVED | direct full reads of the R2G assessment's worksheets, carried forward per the Measurement Protocol, not re-derived |
| checker/catalog counts (193 files, 80 command rows, 79 direct invocations, 1 wrapper, 114 not directly referenced) | OBSERVED | R2G worker return's Independent Reviewer Addendum, used verbatim per the Measurement Protocol's explicit instruction |
| this design's proof floors, cost ceilings, and divergence tolerances | PROPOSED design invariant | reasoned from R2G evidence and the paired baseline's Threshold Design Contract; not yet implemented or machine-checked |
| whether a live TPGR router would enforce these exact thresholds automatically | UNKNOWN | no TPGR receipt has been attached to any archetype yet, and this design's proof floors are not yet expressed as machine-checked fields; consistent with R2G's own "UNKNOWN" label on the same underlying question |
| recurring maintenance cost of the Dependency Invalidation Graph over time | UNKNOWN | the graph is a design candidate only; no maintenance history exists, mirroring R2G's own treatment of the conditional lifecycle interface candidate |
| whether the external critique's unreconciled schema proposals (five-field checker record, escalation-only uncertainty flag) would reduce or increase this design's maintenance cost if later adopted | UNKNOWN, and out of scope | the critique remains `NOT_CVF_SOURCE`; this design neither adopts nor rejects those specific schema proposals, and only cites the critique's risk framing (self-downgrade, stale-receipt survival) as already-reconciled input via the R2G reconciliation chain |

## R4 Candidate Delta Manifest (Zero Current Edits)

The following paths are named as exact candidate edit targets for a future
R4+ tranche only. None is edited, drafted, or scaffolded by this design.

| Candidate path | Candidate change | Justifying evidence | Authorization state |
| --- | --- | --- | --- |
| `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md` | add a "Threshold Design Reference" section citing this R3 design's route-outcome precedence, proof floors, and Dependency Invalidation Graph by reference | this design's Route Outcomes And Deterministic Precedence and Dependency Invalidation Graph sections | UNAUTHORIZED; requires R4+ and independent review |
| `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md` (manifest schema) | evaluate (not adopt) adding a `decisionUncertainty`-equivalent field structured as escalation-only (present=escalate, absent=deterministic route stands), per this design's Anti-Self-Downgrade treatment | this design's Route Outcomes section and Divergence Tolerances section; the reconciled external-critique risk framing | UNAUTHORIZED; R4+ shadow-interface design would need to specify the exact field shape and a negative test proving no downward path exists |
| any `governance/compat/check_*.py` file | none proposed by this design | no A1-A6 worksheet in this design identified a checker gap requiring a new or modified checker | NOT_PROPOSED |
| a new registry, lifecycle standard, or command catalog | none proposed | this design explicitly reuses the existing Canonical Fact-Owner Map with no second truth store, per the Acceptance Criteria | NOT_PROPOSED |

No path above is edited by this worker. This table exists to satisfy the
work order's requirement for an R4 candidate delta manifest with zero
current edits, not to pre-approve any future change.

## Evidence / Verification

Before dispatch, both worker outputs were required to pass routing and
dispatch gates; the pre-implementation autorun gate and the TPGR
shadow-route checker (`COMPLIANT`, 0 violations) were both run as required
preflight, before any edit, at `executionBaseHead`. During execution, this
design records source sections, evidence labels, and the no-commit boundary
directly in its own tables above and in the paired worker return's Command
Evidence section. Reviewer acceptance of this evidence remains a separate,
independent step owned by the reviewer/closer.

## Risk / Corrective Action

Primary risk: a future R4+ implementation of the Dependency Invalidation
Graph could quietly grow into a second per-checker record with per-checker
edges, recreating the exact O(n-squared) maintenance cost the reconciled
critique warned against in its Q4 finding. Corrective action: any R4+ implementation
must be reviewed against exactly the group-level, fact-owner-row-matching
shape this design uses (matching a changed path against the Canonical
Fact-Owner Map's existing owner rows), not a new per-checker dependency
schema; a design that adds per-checker bidirectional edges should be treated
as a stop-condition-adjacent change even if this design did not observe one.

Secondary risk: the zero-divergence-tolerance posture across every archetype
in this design is conservative by construction and may prove more expensive
in practice than a calibrated nonzero tolerance would be. Corrective action:
this design deliberately defers that calibration to a future measurement-
gated tranche (per Rule 6, a route with unknown maintenance cost cannot claim
positive net value); any future proposal to introduce a nonzero divergence
tolerance must carry its own replay/measurement evidence, not be adopted by
default.

Tertiary risk: this design's proof floors and cost ceilings are PROPOSED
design invariants, not yet machine-checked fields. A future reader must not
cite this design as having implemented, activated, or machine-enforced any
threshold; it remains a design proposal pending R4+ authorization.

## Decision

`PROCEED_TO_R4_SHADOW_INTERFACE_DESIGN`

## Final Disposition

`PROCEED_TO_R4_SHADOW_INTERFACE_DESIGN`

Rationale: every archetype (A1-A6) now has an explicit proof floor, TPGR cost
ceiling, divergence tolerance, freshness-invalidation dependency, rollback
trigger, and assertion-ownership boundary that traces to an existing CVF
canonical owner, with no second truth store proposed. The three route
outcomes have deterministic, monotonic precedence. No threshold in this
design permits worker-controlled self-downgrade of `decisionUncertainty`,
authority impact, evidence freshness, or source scale; every hostile
scenario in the work order's required matrix resolves to a fail-closed
outcome under the binding Threshold Precedence and Anti-Self-Downgrade
rules. The Dependency Invalidation Graph resolves relevant-versus-unrelated
checker/catalog changes without enumerating all 193 checker files, addressing
the reconciled external critique's stale-receipt-survival concern without
adopting any unreconciled critique schema as authority. Numeric thresholds
with inadequate current evidence (recurring maintenance cost, live-router
equivalence) remain explicit PROJECTED/UNKNOWN measurement gates rather than
invented certainty, per Rule 6. This satisfies the paired baseline's
Threshold Design Contract and the work order's Acceptance Criteria. The next
authorized step is R4 (shadow interface/claim vocabulary design), which
remains unauthorized by this design and requires a fresh operator decision
and governed dispatch.

## Claim Boundary

This design is a documentation-only, non-implementation threshold-design
evidence artifact over existing governed evidence. It does not implement
TPGR routing, does not modify any standard, checker, registry, catalog, hook,
or router, does not intake or register any new source corpus, does not
authorize selective execution (`selectiveExecutionAuthorized` remains
`false` per the TPGR standard, independently verified at this
executionBaseHead), and does not open R4-R9, T15, or any runtime,
provider/live, public-sync, deployment, or production action. The
`PROCEED_TO_R4_SHADOW_INTERFACE_DESIGN` disposition authorizes only a future
operator decision to open R4 under a fresh governed dispatch; it does not
itself authorize R4 work.
