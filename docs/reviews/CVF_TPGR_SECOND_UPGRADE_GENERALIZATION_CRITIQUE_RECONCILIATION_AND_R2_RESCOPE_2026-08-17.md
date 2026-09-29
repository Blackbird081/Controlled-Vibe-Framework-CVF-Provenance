# CVF TPGR Second Upgrade Generalization Critique Reconciliation And R2 Rescope

Memory class: governed-planning-review

Status: REVISED_GENERALIZED_PLAN_PENDING_OPERATOR_DECISION

docType: review

Date: 2026-08-17

## Purpose

Reconcile the second independent critique against CVF authority and correct
the TPGR second-upgrade objective. The target is not one cheaper route for the
RSPB local corpus. The target is a reusable boundary in which existing CVF
absorption owners define how knowledge enters CVF and TPGR determines which
controls apply to the current stage, effect, evidence state, and claim risk.

## Target / Source

| Source | Identity | Authority use |
| --- | --- | --- |
| second external return | `docs/reviews/CVF_TPGR_SECOND_UPGRADE_GENERALIZATION_EXTERNAL_CRITIQUE_2026-08-17.md`; original SHA-256 `f27d420ccc1c56a7d62fa35c4fd4c8684b7ab0d99e7ff316bfe7185dbd9122db` | advisory input only |
| prior revised plan | `docs/reviews/CVF_TPGR_SECOND_UPGRADE_CRITIQUE_RECONCILIATION_AND_REVISED_PLAN_2026-08-17.md`; SHA-256 `3f4f922f083d499a6c8c908e6c30b564cb808e2dceeeebe14d885e129a513582` | governed planning source, modified by this reconciliation |
| TPGR T0 owner | `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md` | current routing authority; selective execution remains disabled |
| knowledge chain owner | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | current input-routing order and recorded universal-router gap |
| absorption owners | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md`; `docs/reference/external_agent_review/CVF_MIXED_ORIGIN_DERIVED_SYNTHESIS_ABSORPTION_STANDARD.md`; `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md` | current manifest, ledger, semantic, owner-map, adaptation, and blind-spot rules |
| corpus registry owner | `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md`; `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | current corpus registration and reusable scan-state evidence |

## Scope / Methodology

The reviewer read the critique, the prior plan, the canonical absorption and
TPGR owners, the relevant checker literals, and the generated corpus registry.
The registry was parsed directly rather than relying on the external count.
The review distinguishes verified repository facts from proposed architecture
and tests every proposal against cost control, authority non-duplication, and
claim precision.

No new source corpus was scanned. No authority, registry enum, checker,
catalog, hook, route, runtime, provider, public, deployment, or production
surface is changed by this plan.

## Findings / Position

The scope verdict `SPLIT_TPGR_AND_ABSORPTION_ARCHITECTURE` is accepted with
modification. It means separation of responsibility, not two new systems:

- existing absorption owners remain Layer A;
- TPGR remains Layer B and routes Layer A stages;
- one thin interface table may bind the two by reference inside the TPGR
  owner;
- no new absorption standard or parallel lifecycle is justified.

The recommendation `REVISE_R2_SCOPE_BEFORE_APPROVAL` is accepted. The prior
R2 is superseded by the generalized non-implementation assessment defined
below. It is not yet authorized.

## Independent Source Verification

| External claim | CVF evidence | Reviewer disposition |
| --- | --- | --- |
| generated registry has 170 corpora | direct JSON parse returns 170 entries | ACCEPT |
| entries occupy six corpus types | nonzero counts are CVF_EXTENSION 87, EXTERNAL_SOURCE 5, LEGACY_FOLDER 17, POLICY_DOCUMENT 18, PROJECT_SOURCE 37, TEST_CORPUS 6 | ACCEPT_WITH_PRECISION: seven types are allowed; COMPANY_DOCS currently has zero entries |
| lifecycle is proven in production | registry and guards prove governed use and machine-shaped evidence, not production effectiveness | REJECT_OVERCLAIM |
| chain map records a universal-router gap | Enforcement Gap explicitly says no one universal trigger/router enforces every relevant intake through the full chain | ACCEPT |
| RSPB registry entry covers 764 files | entry records 559 upstream plus 205 local through its prior-absorption evidence and `fileCount: 764` | ACCEPT |
| RSPB verdicts are gc047 complete, gc048 reconciled, gc050 not run | generated entry records `COMPLETE_VERIFIED`, `RECONCILED_VERIFIED`, `NOT_RUN` | ACCEPT |
| gc050 not run proves no semantic classification happened | the field proves only that GC-050 was not run; the entry also records semantic regions and findings | REJECT_OVERCLAIM |
| every source archetype must register in GC-051 | GC-051 applies to corpora; the chain map also supports bounded review/recommendation inputs that are not necessarily corpora | MODIFY |

## Reconciliation Matrix

| Proposal | Disposition | CVF correction |
| --- | --- | --- |
| Layer A / Layer B split | ACCEPT | TPGR routes existing owners and must not restate their semantics |
| thin stage contract inside TPGR | ACCEPT_WITH_MODIFICATION | call it an interface table under the existing TPGR owner, not a new owner |
| S0-S8 linear lifecycle | MODIFY | use a conditional route graph; small named inputs must not inherit corpus ceremony |
| add two corpus-type enums now | DEFER | first test whether existing types plus input metadata are sufficient; no enum change is authorized |
| five absorption archetypes | ACCEPT_WITH_MODIFICATION | retain five and add one downstream-project authority-boundary archetype |
| upstream commit change invalidates all S1/S2 evidence | MODIFY | preserve historical receipts; mark current eligibility stale and reconcile the delta from the earliest affected node |
| eight claim tokens | ACCEPT_WITH_MODIFICATION | align names with existing processing semantics and scope enforcement to new or changed completion claims |
| ban every bare use of absorbed | REJECT_AS_GLOBAL_RULE | require an exact scoped completion token; do not retroactively police descriptive prose or archives |
| A1 negative savings stops the program | MODIFY | first intake may contain unavoidable lifecycle cost; stop on duplicated ceremony or negative TPGR value, not on absence of inheritance savings |
| delete project adoption from scope | MODIFY | full downstream-project governance remains separate, but its source/authority boundary is a required R2 archetype |

## Generalized Architecture Boundary

Layer A owns knowledge intake semantics:

`input identification -> corpus accounting when applicable -> processing and
semantic review -> overlap/novelty -> CVF owner map -> CVF-native adaptation ->
promotion decision -> later delta reconciliation`.

Layer B owns control routing:

`actual task/effect/claim classification -> receipt freshness -> applicable
control closure -> monotonic escalation -> independent review -> fallback`.

The interface owns only five facts:

1. current lifecycle node;
2. valid predecessor receipt references;
3. exact claim requested;
4. actual target owner/effect class;
5. earliest invalidated node when evidence drifts.

It must not duplicate manifests, ledgers, value matrices, origin graphs, owner
maps, or checker command inventories already owned elsewhere.

## Conditional Lifecycle Route Graph

| Node | Applies when | Exit evidence | Licensed claim |
| --- | --- | --- | --- |
| G0 INPUT_IDENTIFIED | every intake | source identity, input class, scope, authority boundary | input is identified only |
| C0 CORPUS_REGISTERED | input is a reusable corpus | GC-051 entry or equivalent current registry reference | corpus identity is registered |
| C1 STRUCTURALLY_ENUMERATED | corpus or bounded folder accounting is required | manifest, hash recipe, count reconciliation | structural scope is enumerated |
| C2 PROCESSING_LEDGER_RECONCILED | file-level processing is required | terminal ledger plus unresolved/exclusion totals | processing ledger is reconciled; no full semantic claim |
| K0 TRIAGE_CLASSIFIED | prioritization is needed | ranked clusters and overlap/novelty hypotheses | candidates are triaged only |
| K1 CLUSTER_SEMANTICALLY_READ | a named cluster or item is selected | hashes plus substantive summary, use cases, value disposition, reviewer | named scope was semantically read |
| O1 OWNER_MAPPED | value may enter CVF | owner-fit result and dependency boundary | value has a target or explicit owner gap |
| V1 CVF_NATIVE_CONVERTED | governed CVF change exists | owner diff plus focused proof and routed checks | named capability is adapted into CVF |
| P1 PROMOTION_REVIEWED | authority/runtime/public or other promotion is requested | effect-specific review under deterministic TPGR minimum | only the exact approved promotion claim |
| D1 DELTA_RECONCILED | pinned source identity changes | added/changed/removed scope and impact map | delta is reconciled; unaffected historical evidence remains historical |

This is a graph, not a mandatory linear ceremony. A returned review may route
from G0 directly to finding classification. A small named-file input may route
G0 -> K1 -> O1 without GC-051 when it is not a reusable corpus. A new upstream
corpus uses C0-C2 before semantic claims. An accepted corpus cluster inherits
C0-C2 and starts at K1 when receipts are fresh. D1 routes back only to the
earliest affected node.

## Scoped Claim Vocabulary Candidate

| Token | Exact boundary |
| --- | --- |
| `INPUT_IDENTIFIED` | identity and authority boundary known; no reading claim |
| `CORPUS_REGISTERED` | reusable corpus has a current registry reference |
| `STRUCTURALLY_ENUMERATED` | bounded filesystem/source manifest reconciled |
| `PROCESSING_LEDGER_RECONCILED` | all in-scope rows have terminal processing outcomes; not full semantic comprehension |
| `TRIAGE_CLASSIFIED` | shallow or automated prioritization completed |
| `CLUSTER_SEMANTICALLY_READ` | exact listed cluster substantively read |
| `CAPABILITY_ADAPTED_INTO_CVF` | bounded value materialized in a named CVF owner |
| `CORPUS_SEMANTICALLY_RECONCILED` | explicit proof that no substantive in-scope item remains semantically unresolved |
| `DELTA_RECONCILED` | source delta accounted against a pinned predecessor |

R2 must test these tokens against existing verdict/status vocabularies before
any standard change. New or changed completion claims would carry one exact
token plus scope reference. General descriptive prose is not a completion
claim, and historical artifacts are not retroactively rewritten.

## Generalized R2 Feasibility Assessment

R2 becomes a non-implementation assessment over existing governed evidence.
It creates one assessment artifact but does not mutate the assessed standards,
registry, router, checkers, catalogs, or source corpora.

Required archetypes:

| Archetype | Evidence posture | Question R2 must answer |
| --- | --- | --- |
| A1 new upstream corpus | no inherited intake receipt | can TPGR route existing first-intake controls without adding duplicate ceremony? |
| A2 mixed-origin local synthesis | provenance-backed, owner-agent co-designed | can claim-specific evidence and local-first semantic review be preserved? |
| A3 accepted-corpus cluster | fresh reusable corpus evidence | does the RSPB seven-file case remove repeated work without weakening semantic review? |
| A4 upstream delta | pinned predecessor plus changed source identity | can the earliest affected node be found without invalidating unrelated history? |
| A5 small named item/file set | not necessarily a reusable corpus | is the minimum route materially cheaper than corpus intake while remaining source-bound? |
| A6 downstream project source boundary | existing PROJECT_SOURCE evidence | can project knowledge be used without promoting the project to CVF authority or claiming full project-governance activation? |

Use existing historical evidence or read-only fixtures. R2 does not authorize a
network clone, new intake, registry mutation, or implementation.

For each archetype measure separately:

- unavoidable Layer A evidence cost;
- current legacy guard command count and wall time;
- proposed TPGR classification/metadata overhead;
- inherited versus refreshed evidence;
- controls selected, always retained, and conditionally omitted;
- recurring maintenance cost per relevant owner/catalog change;
- escalation rate and possible material false-negative class;
- net cost attributable to TPGR, separated from necessary semantic-intake work.

Stop or narrow the design when any of these holds:

- the interface duplicates Layer A evidence rather than referencing it;
- deterministic classification cannot distinguish corpus and item routes;
- metadata maintenance plus escalation cost exceeds removed irrelevant-guard
  cost for an activation candidate;
- a repeated/reuse route produces no bounded savings after maintenance;
- any material false negative, authority contamination, or completion-claim
  laundering appears;
- selective command closure cannot be maintained from one canonical catalog.

A1 is not required to show inheritance savings. It must show that TPGR adds no
duplicate intake ceremony and correctly preserves every first-intake control.

## R2 Deliverables And Exit

R2 must return:

1. an as-is Layer A owner map with no duplicated proposed owner;
2. the conditional lifecycle interface candidate;
3. six archetype route/cost worksheets;
4. claim-vocabulary compatibility and migration assessment;
5. checker/catalog applicability feasibility using the canonical command
   universe;
6. an exact proposed authority-delta manifest, still unimplemented;
7. one disposition: `PROCEED_TO_THRESHOLD_DESIGN`,
   `NARROW_TO_RECEIPT_REUSE_ONLY`, `REVISE_ARCHITECTURE`, or
   `STOP_TPGR_SECOND_UPGRADE`.

R2 passes only if the router remains smaller than the lifecycle it routes,
does not create a second truth store, and demonstrates a positive bounded case
for at least the repeated/reuse routes without weakening any always-on or
effect-triggered control.

## Revised Delivery Sequence

| Stage | Work | Authorization state |
| --- | --- | --- |
| R0 | first critique and checker-cost reconciliation | complete |
| R1 | generalization critique and this CVF reconciliation | complete when materially committed |
| R2G | generalized six-archetype non-implementation feasibility assessment | pending operator decision |
| R3 | pre-register per-archetype proof, cost, divergence, and rollback floors | unauthorized |
| R4 | shadow interface/claim vocabulary design | unauthorized |
| R5 | shadow command applicability and receipt invalidation | unauthorized |
| R6 | historical plus seeded-defect replay | unauthorized |
| R7 | dual-run canary and rollback rehearsal | unauthorized |
| R8 | exact P0/P1 allowlist decision | unauthorized |
| R9 | separate P2 decision | unauthorized |

Full downstream-project governance adoption, P3/P4 narrowing, T15, and all
runtime/provider/live/public/deployment work remain outside this decision.

## Risk / Corrective Action

Primary risk: replacing one over-governed absorption workflow with a new
universal stage machine would recreate the same cost in a different schema.

Corrective action: treat the lifecycle as conditional routes, reference current
owners, and measure TPGR overhead separately from unavoidable semantic work.

Secondary risk: a valid ledger or one understood cluster becomes a false
repository-completion claim.

Corrective action: bind every new completion claim to one scoped token and
evidence reference; never infer corpus-level semantic reconciliation from the
number of cluster receipts.

## Decision Requested From Operator

Choose exactly one:

- `APPROVE_GENERALIZED_R2_FEASIBILITY_ASSESSMENT`;
- `MODIFY_GENERALIZED_R2_PLAN`; or
- `REJECT_TPGR_SECOND_UPGRADE`.

Approval authorizes only creation of the R2G assessment/work order and local
read-only measurements against existing evidence. It does not authorize R3-R9,
rule/checker/registry/catalog changes, source intake, selective execution,
T15, runtime, provider/live, public, deployment, or production action.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_rescan_intelligence_hardening.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_finding_to_governance_learning.py` |
| literalTokensReviewed | review headings; checker-read-ahead fields; intake-routing rows; compact non-scan corpus and repeat-scan dispositions; epistemic fields; trace labels; finding-learning enum; public disposition |
| gateRunPurpose | confirm the reconciliation and rescope satisfy governed-review evidence shape after substantive source review |
| claimBoundary | planning reconciliation only; no selective-execution or implementation proof |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | advisory critique -> independent CVF verification -> accepted/modified/rejected reconciliation -> operator decision |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | existing TPGR, chain-map, corpus-registry, mixed-origin, core, and blind-spot owners |
| Disposition | ACCEPT_WITH_MODIFICATION_FOR_GENERALIZED_R2 |
| Claim boundary | no external conclusion becomes authority without this CVF disposition and later authorized owner change |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON
- N/A with reason: this review verifies named governed sources and aggregates
  the current registry; it performs no scan, rescan, intake refresh, or corpus
  absence claim.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - this planning review makes no
  new complete-corpus claim and does not modify the accepted RSPB manifest,
  ledger, registry entry, or any other corpus evidence.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next action |
| --- | --- | --- | --- | --- |
| prior R2 overfit one accepted-corpus cell | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | require six-archetype R2G before implementation planning |
| lifecycle/router ownership was not explicit | RULE_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | test a thin interface-by-reference; do not create a new standard |
| semantic completion vocabulary is ambiguous | DOCUMENTATION_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | assess scoped tokens and migration cost in R2G |

Cost/latency learning disposition: N/A_WITH_REASON - this planning review
defines measurements but reports no runtime, provider, token, latency, or
empirical cost result.

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE_PLANNING.

Expected Result / Prediction: a thin interface over existing absorption owners
should generalize to future repositories while TPGR removes only irrelevant
controls and preserves semantic work.

Evidence Comparison: direct registry aggregation confirms 170 entries and the
RSPB facts; canonical standards confirm a general lifecycle and a universal-
router gap. They do not establish production effectiveness, mandatory corpus
registration for every item, or universal semantic completion.

Contradiction Or Gap Disposition: accept the architecture split and broader
R2; modify lifecycle linearity, delta invalidation, claim enforcement, enum
changes, and stop logic as recorded above.

Claim Update: the prior R2 request is superseded. The only proposed next move
is operator approval, modification, or rejection of R2G.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | CVF reviewer/orchestrator |
| Provider or surface | local private provenance repository |
| Session or invocation | TPGR second-upgrade generalization reconciliation, 2026-08-17 |
| Working directory | repository root |
| Command or tool surface | full critique read, governed source reads, JSON aggregation, checker-source read-ahead, apply patch, reviewer gates, Git |
| Target paths | external generalization critique plus this reconciliation/rescope |
| Allowed scope source | operator requested reconciliation of the second critique and a reusable future-repository absorption design |
| Before status evidence | HEAD `532e4bd81bc4e927cbaa46b2f9a44bee18551a93`; one untracked external critique |
| After status evidence | normalized critique and independently verified generalized R2 plan pending gates and material commit |
| Diff evidence | exact changed-path reconciliation required before commit |
| Approval boundary | critique preservation and plan rescope only |
| Claim boundary | no authority implementation, source intake, selective execution, T15, runtime, provider/live, public, deployment, destructive, or production action |
| Agent type | reviewer/orchestrator |
| Invocation ID | `tpgr-second-upgrade-generalization-reconciliation-20260817` |
| Expected manifest | the external critique and this reconciliation/rescope |
| Actual changed set | required to equal the expected material manifest before commit |
| Manifest delta | required to be zero |
| Deletion or rename disposition | N/A with reason: no deletion or rename authorized |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private governance planning and advisory reconciliation; public-sync
is not authorized.

## Decision / Disposition

`REVISE_R2_SCOPE_BEFORE_APPROVAL_ACCEPTED_WITH_CVF_MODIFICATIONS`

## Claim Boundary

This artifact verifies and revises a planning proposal. It does not prove that
the existing lifecycle is effective in production, declare any corpus fully
semantically reconciled, activate claim tokens, change a CVF owner, authorize
R2G, enable selective execution, open T15, or permit source intake, runtime,
provider/live, public, deployment, destructive, irreversible, or production
work.
