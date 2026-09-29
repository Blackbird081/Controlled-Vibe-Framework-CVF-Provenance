# CVF TPGR-R4 Shadow Interface And Claim Vocabulary Design

Memory class: governed-planning-assessment

docType: baseline

Status: COMPLETE_PENDING_REVIEW

Batch ID: TPGR-R4

Date: 2026-08-18

executionBaseHead: `aec3d4803fb46e86937dd12c31fc77d1f6e293d5`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Responds to work order:
`docs/work_orders/CVF_AGENT_WORK_ORDER_TPGR_R4_SHADOW_INTERFACE_AND_CLAIM_VOCABULARY_DESIGN_2026-08-18.md`

Paired baseline authority:
`docs/baselines/CVF_GC018_TPGR_R4_SHADOW_INTERFACE_AND_CLAIM_VOCABULARY_DESIGN_2026-08-18.md`

## Purpose

Design, without implementing, the smallest possible shadow interface that
binds accepted R3 archetype thresholds to CVF's existing S0-S8 knowledge-
absorption lifecycle by reference only, plus an exact eight-token claim
vocabulary that prevents cluster-level evidence from being laundered into
corpus-level absorption claims. This is design evidence and one disposition,
not implementation. It changes no standard, checker, registry, catalog,
hook, or source corpus.

## Source / Predecessor Evidence

| Source | Identity | Authority use |
| --- | --- | --- |
| paired baseline | `docs/baselines/CVF_GC018_TPGR_R4_SHADOW_INTERFACE_AND_CLAIM_VOCABULARY_DESIGN_2026-08-18.md` | complete execution authority for this design |
| paired work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_TPGR_R4_SHADOW_INTERFACE_AND_CLAIM_VOCABULARY_DESIGN_2026-08-18.md` | task manifest, Design Contract, Exact Claim Vocabulary, Required Hostile Cases, Allowed Final Dispositions |
| R3 assessment | `docs/assessments/CVF_TPGR_R3_ARCHETYPE_THRESHOLD_PROOF_DIVERGENCE_AND_ROLLBACK_FLOOR_DESIGN_2026-08-18.md` | Canonical Fact-Owner Map, Route Outcomes And Deterministic Precedence, Anti-Self-Downgrade Invariants, Dependency Invalidation Graph, R4 Candidate Delta Manifest, Final Disposition `PROCEED_TO_R4_SHADOW_INTERFACE_DESIGN` |
| R3 worker return | `docs/reviews/CVF_TPGR_R3_ARCHETYPE_THRESHOLD_PROOF_DIVERGENCE_AND_ROLLBACK_FLOOR_DESIGN_WORKER_RETURN_2026-08-18.md` | Independent Reviewer Addendum confirming the R3 evidence and one repaired per-worksheet field |
| generalized critique reconciliation | `docs/reviews/CVF_TPGR_SECOND_UPGRADE_GENERALIZATION_CRITIQUE_RECONCILIATION_AND_R2_RESCOPE_2026-08-17.md` | Conditional Lifecycle Route Graph (G0/C0/C1/C2/K0/K1/O1/V1/P1/D1), Scoped Claim Vocabulary Candidate, Generalized Architecture Boundary, Revised Delivery Sequence naming R4 |
| external critique (reconciled) | `docs/reviews/CVF_TPGR_SECOND_UPGRADE_GENERALIZATION_EXTERNAL_CRITIQUE_2026-08-17.md` | Semantic Completeness Vocabulary (S0-S8 stage mapping), Binding Rules, Three Strongest Future-Repository Failure Modes; `NOT_CVF_SOURCE` until reconciled, cited here only through the accepted reconciliation chain |
| R2G assessment | `docs/assessments/CVF_TPGR_R2G_GENERALIZED_ABSORPTION_ROUTING_FEASIBILITY_ASSESSMENT_2026-08-17.md` | Verified As-Is Layer A Owner Map, Conditional Lifecycle Interface Candidate (five-fact interface), Proposed Authority-Delta Manifest |
| TPGR routing standard | `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md` | Mandatory Classification enums, Mandatory Escalation rules, TPGR-T0 Legacy Full-Gate Interlock (shadow-only), Activation Rule |

## Scope / Methodology

The worker captured `executionBaseHead` = `aec3d4803fb46e86937dd12c31fc77d1f6e293d5`
via `git rev-parse HEAD` and confirmed a clean worktree
(`git status --short --untracked-files=all` returned no output) before any
edit. The worker read in full: the paired baseline, the paired work order,
`CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`, `CVF_SESSION_MEMORY.md`,
`AGENT_HANDOFF_V59_2026-08-11.md`, the guard orientation index, the
literal-format gotchas reference, the R3 assessment and its worker return
(including the Independent Reviewer Addendum), the generalized critique
reconciliation, the targeted Semantic Completeness Vocabulary and Binding
Rules sections of the external critique, the TPGR routing standard, and the
R2G assessment's Verified As-Is Layer A Owner Map and Conditional Lifecycle
Interface Candidate (the targeted Layer A owner sections cited by R3's
Canonical Fact-Owner Map). The worker also read the applicable
`governance/compat/check_*.py` checker sections listed in the Checker Source
Read-Ahead Block before authoring either output file.

Per the work order, this design uses R3's accepted thresholds and R2G's
Layer A owner map as the predecessor dataset. No new corpus scan, source
intake, network access, or re-derivation of any registry/catalog count was
performed. No standard, checker, registry, catalog, hook, or router is
modified by this assessment. No selective execution is authorized or
claimed; `selectiveExecutionAuthorized` remains `false` per the TPGR
standard, independently verified directly by `check_task_governance_route.py`
at this executionBaseHead (`COMPLIANT`, 0 violations, `Legacy gate
disposition: RUN_FULL_LEGACY_BUNDLE`).

## S0-S8 Reference Map To Existing CVF Owners

This is explicitly not a new lifecycle. Every stage below cites, by
reference only, the existing CVF-governed owner already verified in R2G's
Verified As-Is Layer A Owner Map and reused in R3's Canonical Fact-Owner
Map. No stage row restates a manifest, ledger, value matrix, origin graph,
owner map, or checker command inventory that already exists under that
owner. The S-numbering below aligns the reconciled external critique's
Semantic Completeness Vocabulary stage column with the reconciliation's own
Conditional Lifecycle Route Graph node identifiers, so a reader can trace
either vocabulary to the same one canonical owner.

| Stage | Route-graph node | What the stage means | Canonical CVF owner (by reference only) |
| --- | --- | --- | --- |
| S0 | G0 INPUT_IDENTIFIED | source identity, input class, scope, authority boundary known | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| S1 | C0/C1 CORPUS_REGISTERED / STRUCTURALLY_ENUMERATED | corpus registration; filesystem-backed manifest, hash, count reconciled | `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md` (GC-051); `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`; `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| S2 | C2 PROCESSING_LEDGER_RECONCILED | every manifest item has a terminal processing status | same core standard, `check_external_absorption_core.py` |
| S3 | K0 TRIAGE_CLASSIFIED | shallow/automated overlap-novelty triage pass | same core standard, `check_external_absorption_overlap_discipline.py` |
| S4 | K1 CLUSTER_SEMANTICALLY_READ | one named cluster substantively read; scope equals the listed files | same core standard; `docs/reference/external_agent_review/CVF_MIXED_ORIGIN_DERIVED_SYNTHESIS_ABSORPTION_STANDARD.md` for mixed-origin clusters |
| S5 | O1 OWNER_MAPPED | value has a target CVF owner, or an explicit `OWNER_SURFACE_NOT_FOUND` gap | same core standard's overlap/novelty and value-conversion lanes, `check_external_absorption_value_conversion.py` |
| S6 | V1 CVF_NATIVE_CONVERTED | a bounded capability is materialized as a governed CVF change in a named owner | the specific CVF owner surface the change lands in (e.g. a `docs/reference/` standard, a checker, a schema); no single blanket owner exists for S6, by design, since the target owner is always the receiving surface itself |
| S7 | P1 PROMOTION_REVIEWED | authority/runtime/public or other promotion review, under deterministic TPGR minimum | `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md` (TPGR-T0) plus the specific promotion-class owner (e.g. public-sync boundary, runtime/provider gate) |
| S8 | D1 DELTA_RECONCILED | pinned source identity changes; delta enumerated against the prior pin | the specific prior closure's own disposition trail, compared against the actual current live owner surface (never a cached copy); `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` for delta-ledger classification vocabulary |

Blind-spot and completeness cross-cutting owners apply across S1-S6 and are
not restated per stage: `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md`
(seven-gate discipline); `docs/reference/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_STANDARD_2026-06-01.md`;
`docs/reference/CVF_CORPUS_TO_KNOWLEDGE_MAP_RECONCILIATION_STANDARD_2026-06-01.md`.
Routing/control-selection across every stage is owned by the TPGR standard
itself (Layer B), never by this design.

This map introduces zero new owners. Every cell above already appears,
verbatim in substance, in R2G's Verified As-Is Layer A Owner Map or R3's
Canonical Fact-Owner Map; this section only adds the S-number-to-node
cross-reference so the shadow-interface field table below can cite a stage
identifier without re-deriving ownership.

## Shadow Interface Field Table

Eight fields, matching exactly the paired baseline's `docOnlyNewFields` list
and the work order's Design Contract. None is an active schema field; each
is a documentation-only candidate field this design proposes for a future
R5+ implementation. No field creates a second truth store: every "validation
source" column cites an owner already named in the S0-S8 map above.

| Field | Owner | Type | Allowed values | Who may assert it | Validation source | Missing/malformed behavior | Invalidation trigger |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `intakeStage` | the S0-S8 map row matching the current stage | enum | one of `S0`-`S8` (equivalently `G0`,`C0`,`C1`,`C2`,`K0`,`K1`,`O1`,`V1`,`P1`,`D1`) | worker proposes; independently recomputable from the actual evidence present, never accepted from worker declaration alone | the stage's own canonical owner checker (see S0-S8 map) | missing or out-of-enum value routes to `FULL_LAYER_A_REQUIRED` (never assumed as S0) | any change to the stage's owning standard/checker per the R3 Dependency Invalidation Graph |
| `claimToken` | this design's Exact Claim Vocabulary (below) | enum | exactly one of the eight tokens in the Exact Claim Vocabulary table | worker proposes; reviewer/owner confirms before it is current, mirroring R3's `WORKER_PROPOSES, OWNER_CONFIRMS` pattern | this design's token table; the underlying stage evidence the token claims to summarize | unknown, missing, or malformed token routes to `ESCALATE_FOR_REVIEW` at minimum (Hostile Case 5) | any redefinition of the eight-token table itself (R5+ only; this design defines it once) |
| `claimScopeRef` | the specific named file/cluster/corpus list the claim covers | reference (exact path list or corpus/cluster identifier) | a fully enumerated, exact scope reference; never an approximate or "et al." scope | worker proposes the scope it touched; independently countable from the diff or manifest, never taken on faith | the stage's manifest/ledger (S1/S2) or the named cluster list (S4) | missing scope routes to `FULL_LAYER_A_REQUIRED`/`ESCALATE_FOR_REVIEW` per Rule 2 (R3); scope exceeding evidence by even one file fails per Hostile Case 6 | any detected divergence between the declared scope and the independently recomputed scope |
| `evidenceRefs` | the specific receipt(s)/artifact path(s) the claim relies on | reference list | one or more existing governed artifact paths or checker-receipt identifiers already owned elsewhere | worker cites; never self-generates a receipt | the cited artifact/receipt's own existence and currency, independently re-read | missing or dangling reference routes to `ESCALATE_FOR_REVIEW`/`FULL_LAYER_A_REQUIRED` per the S0-S8 owner the reference should have come from | the cited artifact's own expiry per the R3 Dependency Invalidation Graph |
| `invalidatedBy` | the R3 Dependency Invalidation Graph's node-matching rule | reference (dependency-node identifier) | one dependency-node row from the R3 Dependency Invalidation Graph, or `NONE_CURRENTLY_KNOWN` | never worker-assertable as a final fact; only independently recomputable by re-running the graph's matching rule against current state | R3's Dependency Invalidation Graph (`docs/assessments/CVF_TPGR_R3_ARCHETYPE_THRESHOLD_PROOF_DIVERGENCE_AND_ROLLBACK_FLOOR_DESIGN_2026-08-18.md`) | unknown dependency state routes to `FULL_LAYER_A_REQUIRED` for the affected scope, per R3 Rule 6 | any change to the owning standard/checker/schema/catalog row the graph names |
| `reviewAuthority` | CVF reviewer/closer role (never the worker) | reference (role identifier) | `reviewer/closer`, `operator`, or a named CVF owner-confirmation role from the guard orientation Role Glossary | worker may name the applicable role; worker may never self-assign as the confirming authority for its own claim | `docs/reference/guard_orientation/README.md` Role Glossary | missing reviewer authority means the claim is not yet current-eligible, regardless of any other field | a role-glossary change (R5+ only) |
| `routeOutcome` | R3's Route Outcomes And Deterministic Precedence | enum | exactly one of `FULL_LAYER_A_REQUIRED`, `ESCALATE_FOR_REVIEW`, `LIGHT_ROUTE_ALLOWED` | never worker-assertable as final; the router/reviewer independently computes it from the other seven fields, mirroring R3's Route Outcomes precedence | R3's Route Outcomes And Deterministic Precedence section; `check_task_governance_route.py` for the underlying TPGR classification | missing or contradictory input facts force `FULL_LAYER_A_REQUIRED` or `ESCALATE_FOR_REVIEW`, never `LIGHT_ROUTE_ALLOWED` (R3 Rule 2) | any of the other seven fields becoming stale per their own invalidation trigger |
| `eligibilityState` | this shadow interface, as the single derived state summarizing whether the record currently licenses its claim | enum | `CURRENT`, `EXPIRED_HISTORICAL`, `NEVER_ELIGIBLE` | never worker-assertable; always derived deterministically from `routeOutcome`, `invalidatedBy`, and `reviewAuthority` confirmation state | this table's own derivation rule (below) | a record with any missing required field is `NEVER_ELIGIBLE` until repaired | any trigger that fires `invalidatedBy` moves `CURRENT` to `EXPIRED_HISTORICAL`, never to deletion (R3's historical-receipt-immutability rule) |

`eligibilityState` derivation rule (stated once here; not a ninth field, a
computed view of the other eight): a record is `CURRENT` only when all eight
fields are present, mutually consistent, owner-verified, and current;
`routeOutcome` was computed (not self-declared); `reviewAuthority`
confirmation exists; and no `invalidatedBy` node has fired since
confirmation. A record whose `invalidatedBy` node fires after being
`CURRENT` becomes `EXPIRED_HISTORICAL`, preserved as immutable evidence per
R3's Proof Floors And Evidence-Expiry Rules, never rewritten or deleted. A
record that never had a valid `routeOutcome`/`reviewAuthority` pair is
`NEVER_ELIGIBLE` and was never current.

This eight-field table is smaller than and references Layer A: it contains
zero manifest rows, zero ledger rows, zero value-conversion lanes, and zero
owner-map rows of its own. Every "validation source" cell points outward to
an existing owner. No field in this table proposes a new registry, ledger,
or truth store; the table itself is not implemented by this design and
remains a documentation-only candidate pending R5+ authorization.

## Exact Claim Vocabulary

Exactly eight tokens, taken verbatim from the work order's Exact Claim
Vocabulary table (itself reconciled from the external critique's Semantic
Completeness Vocabulary through the accepted R2G/R3 chain). No token is
invented, renamed, or reworded from the work order's table.

| Token | Minimum meaning (positive implication) | Forbidden implication |
| --- | --- | --- |
| `SOURCE_REGISTERED` | identity and scope known | any reading occurred |
| `STRUCTURALLY_ENUMERATED` | manifest/hash/count reconciled | any file was substantively read |
| `LEDGER_DISPOSITIONED` | every item has terminal disposition | every file was substantively understood |
| `TRIAGE_CLASSIFIED` | overlap/novelty triage completed | value confirmed or materialized |
| `CLUSTER_SEMANTICALLY_READ` | exact named cluster substantively read | repository-level understanding |
| `CAPABILITY_ABSORBED` | bounded capability materialized in a named CVF owner | repository absorbed |
| `CORPUS_SEMANTICALLY_ABSORBED` | every substantive file read and reconciled into owners | N/A; this is the highest corpus semantic claim and has no forbidden-implication ceiling above it |
| `DELTA_ACCOUNTED` | upstream change enumerated against pinned prior | delta absorbed or semantically resolved |

Each token maps to exactly one bounded stage expression from the reference map
above (a single stage except for the explicitly compound corpus expression):
`SOURCE_REGISTERED`->S0, `STRUCTURALLY_ENUMERATED`->S1,
`LEDGER_DISPOSITIONED`->S2, `TRIAGE_CLASSIFIED`->S3,
`CLUSTER_SEMANTICALLY_READ`->S4, `CAPABILITY_ABSORBED`->S6,
`CORPUS_SEMANTICALLY_ABSORBED`->S4-through-S6 repeated across every
in-scope item with explicit unread-file reconciliation (see below),
`DELTA_ACCOUNTED`->S8. A token asserted for a stage its `claimScopeRef` does
not actually cover is malformed per the shadow interface field table's
`claimToken` row and routes to `ESCALATE_FOR_REVIEW` at minimum.

### No Promotion By Aggregation

Cluster receipts never imply corpus absorption, no matter how many cluster
receipts accumulate. `CLUSTER_SEMANTICALLY_READ` is a scope-bound token: its
`claimScopeRef` is the exact named cluster, and it never sums. Ten, one
hundred, or every existing `CLUSTER_SEMANTICALLY_READ` receipt for a given
corpus, taken together, license only ten (or one hundred, or N) separate
scope-bound claims - never one `CORPUS_SEMANTICALLY_ABSORBED` claim. The
only path to `CORPUS_SEMANTICALLY_ABSORBED` is the explicit proof
requirement below, evaluated once, directly, never derived by counting
cluster receipts.

### `CORPUS_SEMANTICALLY_ABSORBED` Proof Requirement

This is the highest corpus semantic claim and carries the strictest proof
floor in this vocabulary. A `CORPUS_SEMANTICALLY_ABSORBED` claim is valid
only when both of the following hold simultaneously, evaluated at claim
time, never inherited from an earlier partial state:

1. **Explicit unread-file reconciliation.** An accounting of every file in
   the corpus's registered scope that was NOT substantively read, with
   owner-confirmed evidence that each excluded file is non-substantive for the
   claim, or a prior `CLUSTER_SEMANTICALLY_READ` receipt that already covers it
   and remains `CURRENT`. A bare terminal label such as `NO_NEW_VALUE` is not
   proof of substantive reading and cannot qualify an unread file by itself;
   it counts only when its own current evidence proves either prior semantic
   review or a valid non-substantive exclusion. This mechanically generalizes
   the existing blind-spot Gate 7 cross-check to files, per the external
   critique's Binding Rule 2, reconciled through R2G/R3.
2. **Scope-total equality.** The claimed scope count (the number of files
   the `CORPUS_SEMANTICALLY_ABSORBED` claim asserts as covered) must equal
   the evidence scope count (the sum of files independently accounted for as
   substantively read, owner-confirmed as a valid non-substantive exclusion,
   or covered by a still-`CURRENT` `CLUSTER_SEMANTICALLY_READ` receipt)
   exactly. A terminal ledger disposition without that evidence contributes
   zero to this semantic evidence count. A claimed count of 764
   against an evidence count of 763 is not `CORPUS_SEMANTICALLY_ABSORBED`;
   it remains `LEDGER_DISPOSITIONED` at most, with the one-file gap named
   explicitly.

A claim missing either requirement is malformed and routes to
`ESCALATE_FOR_REVIEW` per Hostile Case 10, never silently downgraded to a
weaker token by the claimant; the reviewer/owner determines the actual
current token, if any, that the evidence supports.

### Escalation-Only Uncertainty Treatment

Mirroring R3's Rule 3 and Anti-Self-Downgrade Invariants, any uncertainty
signal in this interface can only escalate to a stricter route
(`LIGHT_ROUTE_ALLOWED` -> `ESCALATE_FOR_REVIEW` -> `FULL_LAYER_A_REQUIRED`),
never justify a lighter one. Concretely: if a worker or any input declares
low uncertainty, high confidence, or low authority impact for a claim whose
`claimToken`, `claimScopeRef`, or `invalidatedBy` field is missing,
malformed, or contradicted by independently observable evidence, that
declaration is discarded entirely, not averaged or partially honored, and
the route computed from the objective fields stands or worsens.

**Negative proof that worker input cannot select a lighter route.** Every
field in the Shadow Interface Field Table above that could plausibly be used
to justify a lighter route (`claimToken`, `routeOutcome`, `eligibilityState`)
is explicitly marked `never worker-assertable as final` or requires
independent recomputation/confirmation in its "who may assert it" column.
There is no field in this eight-field table through which a worker
declaration alone can set `routeOutcome` to `LIGHT_ROUTE_ALLOWED` or
`eligibilityState` to `CURRENT`; both are always derived from independently
verifiable state (the S0-S8 map's canonical owner evidence, the
Dependency Invalidation Graph, and reviewer confirmation), never from a
worker's stated confidence or self-report. This closes exactly the
self-downgrade surface the reconciled external critique's failure mode 1
(stage-claim laundering at scale) and R3's Threshold Precedence Rule 3
identify, using the same mechanism R3 already established: uncertainty
changes the *evaluation direction* (toward stricter), never the base
evaluation logic.

### Upstream-Drift (S8) Handling

This directly addresses the paired baseline's Stop Condition on S8 upstream
identity drift and the reconciled critique's failure mode 2 (upstream drift
with live inherited receipts). The hazard: an upstream source's identity
(commit/pin) changes, but the specific files a route selected still
hash-match their receipt's recorded hashes, because those particular files
happened not to change even though the surrounding source moved on. A
receipt that checks only per-file hash stability would report "fresh" while
the claim's actual meaning has silently gone stale.

Binding rule: **source-identity change always invalidates dependent
eligibility, independent of and regardless of selected-file hash
stability.** Concretely:

- `invalidatedBy` for any record whose `claimScopeRef` traces back to a
  pinned upstream source must be recomputed whenever that source's pinned
  identity (commit/mirror hash) changes, not only when a selected file's own
  hash changes;
- until the affected delta scope has completed fresh semantic re-verification,
  `DELTA_ACCOUNTED` is the only token that may be newly asserted after an
  upstream identity change, and only for the delta scope itself (mirroring
  R3's A4 worksheet: `D1` licenses only `DELTA_RECONCILED`/`DELTA_ACCOUNTED`,
  never a broader claim). Later-stage tokens may be re-earned only from fresh
  evidence through their own canonical owners; they are never inherited from
  the expired receipt;
- `CLUSTER_SEMANTICALLY_READ` and `CAPABILITY_ABSORBED` claims whose
  `claimScopeRef` sits inside a source that has since drifted move from
  `CURRENT` to `EXPIRED_HISTORICAL` `eligibilityState` immediately upon
  detecting the identity change, even if every one of their selected files
  still hash-matches;
- this is a stale-corpus problem where the *sample* is unchanged but the
  *source* has moved on; the fix binds `invalidatedBy` to the upstream
  identity as its own independent fact, separate from and in addition to
  file-level hash checks, so identity drift alone is sufficient to
  invalidate, per Hostile Case 3.

This rule is stated as a design invariant on the `invalidatedBy` field's
validation source, using the R3 Dependency Invalidation Graph's own
"the specific CVF owner surface a delta was compared against" row and A4
worksheet as its existing authority. No new invalidation mechanism is
proposed; the rule only makes explicit that upstream-identity comparison is
  a required, independent input to `invalidatedBy`, not an input that
file-hash comparison alone can satisfy.

## Hostile Cases And Decision Tables

Ten cases exactly as required by the work order. Each resolves to a named
fail-closed route and preserves historical receipt evidence without
preserving current eligibility, per R3's historical-receipt-immutability
rule (an expired or void claim's evidence is retained as a record of what
was claimed and when, never deleted or rewritten).

| # | Hostile scenario | Resolved route | Preserved evidence | Why (binding rule) |
| --- | --- | --- | --- | --- |
| 1 | ten cluster receipts are aggregated into a corpus claim | `ESCALATE_FOR_REVIEW`; the aggregated `CORPUS_SEMANTICALLY_ABSORBED` claim is rejected outright | the ten underlying `CLUSTER_SEMANTICALLY_READ` receipts remain valid as exactly what they are: ten scope-bound cluster claims | No Promotion By Aggregation section; the reconciled critique's failure mode 1 |
| 2 | ledger completeness is cited as semantic understanding | `ESCALATE_FOR_REVIEW`; `LEDGER_DISPOSITIONED` cannot be read as `CLUSTER_SEMANTICALLY_READ` or `CAPABILITY_ABSORBED` | the `LEDGER_DISPOSITIONED` receipt remains valid at its own S2 stage | Exact Claim Vocabulary's forbidden-implication column for `LEDGER_DISPOSITIONED`; R3 Hostile Test #2 |
| 3 | upstream commit changes while selected file hashes stay stable | `FULL_LAYER_A_REQUIRED` for the affected delta scope; `eligibilityState` moves `CURRENT` -> `EXPIRED_HISTORICAL` for every affected record; pending fresh semantic re-verification, only `DELTA_ACCOUNTED` for the delta scope may be newly asserted | the pre-drift receipts remain historical evidence of what was true before the identity change | Upstream-Drift (S8) Handling section above; R3 A4 route floor |
| 4 | worker declares low uncertainty or low authority impact | the declaration is discarded and cannot establish `LIGHT_ROUTE_ALLOWED`; if the lighter result depends on that declaration, the named fail-closed route is `ESCALATE_FOR_REVIEW`; otherwise objective fields are recomputed under normal R3 precedence | the worker's declaration itself is recorded as a discarded input, not deleted from the record, but never used to compute the route | Escalation-Only Uncertainty Treatment section; negative proof above |
| 5 | claim token is unknown, missing, or malformed | `ESCALATE_FOR_REVIEW`; a token outside the exact eight-token enum is treated identically to a missing token | any other valid fields on the same record remain visible for reviewer diagnosis, but license no claim on their own | Shadow Interface Field Table's `claimToken` row; mirrors TPGR standard's "Unknown values, missing fields... produce `REJECTED_ESCALATED`" |
| 6 | claim scope exceeds evidence scope by one file | `ESCALATE_FOR_REVIEW`; the claim is malformed regardless of how small the excess is | the evidence scope's own valid coverage (N-1 files) remains valid at whatever token that smaller scope actually supports | Scope-Total Equality requirement; `claimScopeRef` row's "missing/malformed behavior" |
| 7 | owner changes after receipt creation | `FULL_LAYER_A_REQUIRED` for the affected scope because the owner fact is stale; `eligibilityState` moves to `EXPIRED_HISTORICAL` for any claim whose `evidenceRefs` or S6 owner target no longer matches current state | the receipt remains historical evidence of the claim as it stood against the prior owner | R3 Rule 1 and Rule 4 (owner-unverified facts take the full route; evidence expires from the earliest affected node); `invalidatedBy` row |
| 8 | `OWNER_GAP` is used to auto-create a new CVF owner | `FULL_LAYER_A_REQUIRED`; auto-creation is not a licensed action of this interface under any token | the `OWNER_GAP` finding itself remains recorded as an open gap requiring an explicit authority decision | reconciled critique's failure mode 3 (architecture dilution through owner-gap accumulation); this design proposes zero new owners and zero auto-creation mechanism |
| 9 | project source is cited as CVF authority | `FULL_LAYER_A_REQUIRED`; the citation is void | the project source's own `PROJECT_SOURCE` registration (if any) remains valid registration evidence, but grants no authority-citation license | mirrors R3's A6 worksheet zero-tolerance authority-promotion boundary; GC-051 Rule 5 (registration is not authority promotion) |
| 10 | corpus claim omits unread-file reconciliation | `ESCALATE_FOR_REVIEW`; `CORPUS_SEMANTICALLY_ABSORBED` cannot be asserted without the explicit unread-file accounting | any valid lower-stage tokens the same evidence actually supports (e.g. `LEDGER_DISPOSITIONED`) remain valid at their own stage | `CORPUS_SEMANTICALLY_ABSORBED` Proof Requirement section, item 1 |

### Decision Table For Missing / Malformed / Contradictory Facts

| Data condition | Resolved route | Rationale |
| --- | --- | --- |
| all eight interface fields present, owner-verified, current, and mutually consistent | `LIGHT_ROUTE_ALLOWED` only if `routeOutcome` independently computes to it via R3's precedence | full proof floor met; no field required worker-only assertion |
| any single interface field missing | `FULL_LAYER_A_REQUIRED` or `ESCALATE_FOR_REVIEW` per the field's own "missing/malformed behavior" column | R3 Rule 2, inherited unchanged |
| interface field malformed (wrong enum value, dangling reference) | treated identically to missing | mirrors TPGR standard's missing-vs-malformed equivalence |
| two facts contradict (e.g. `claimToken` says `CLUSTER_SEMANTICALLY_READ` but `claimScopeRef` cites a file outside the receipt's ledger) | `ESCALATE_FOR_REVIEW` at minimum, escalating to `FULL_LAYER_A_REQUIRED` if the contradiction touches an owner/authority fact | R3 Rule 3 (evidence conflicts drive escalation, not worker declaration) |
| a field is present but its freshness (`invalidatedBy` state) cannot be determined | `FULL_LAYER_A_REQUIRED` for the affected scope until freshness is independently established | R3 Rule 6 (unknown maintenance/freshness cannot claim positive net value) |
| worker-declared field conflicts with independently observable state | the independently observable state controls; the worker declaration is discarded, not reconciled toward | Anti-Self-Downgrade Invariants (inherited from R3, restated here for this interface) |

## R5 Candidate Command/Receipt Invalidation Manifest (Zero Current Edits)

The following paths and sections are named as exact candidate targets for a
future R5+ tranche only. None is edited, drafted, or scaffolded by this
design.

| Candidate path | Candidate change | Justifying evidence | Authorization state |
| --- | --- | --- | --- |
| `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md` | add a "Shadow Interface Reference" section naming this R4 design's eight-field table and eight-token vocabulary by reference, alongside the existing "Layer A Interface" candidate R2G already named | this design's Shadow Interface Field Table and Exact Claim Vocabulary sections; R2G's Proposed Authority-Delta Manifest row for the same standard | UNAUTHORIZED; requires R5+ and independent review |
| `governance/compat/CVF_TASK_GOVERNANCE_ROUTE_REGISTRY.json` | evaluate (not adopt) whether `claimToken` should become a registry-recognized enum alongside the existing eight classification dimensions | Shadow Interface Field Table's `claimToken` row | UNAUTHORIZED; a schema/registry change requires `P3_ELEVATED` per the TPGR standard's own Rollback section |
| a new `governance/compat/check_shadow_interface_claim_vocabulary.py` (candidate name only; file does not exist) | machine-check the eight-token enum, the no-aggregation rule, and the `CORPUS_SEMANTICALLY_ABSORBED` proof requirement on any governed artifact that asserts a `claimToken` | Exact Claim Vocabulary section, No Promotion By Aggregation section, `CORPUS_SEMANTICALLY_ABSORBED` Proof Requirement section | UNAUTHORIZED; R5+ command/receipt-invalidation design must specify exact detection regexes and false-positive controls before any checker is drafted |
| `governance/compat/check_external_absorption_core.py` | evaluate (not adopt) whether `invalidatedBy`'s upstream-identity-drift rule should be surfaced as a new receipt field on the existing manifest/ledger schema | Upstream-Drift (S8) Handling section | UNAUTHORIZED; R5+ must show this does not duplicate the core standard's own manifest schema |
| any other `governance/compat/check_*.py` file | none proposed by this design | no field in the Shadow Interface Field Table or Exact Claim Vocabulary section identified a checker gap outside the two rows above | NOT_PROPOSED |
| a new registry, lifecycle standard, or command catalog | none proposed | this design explicitly reuses the S0-S8 reference map and R3's Canonical Fact-Owner Map with no second truth store, per the Acceptance Criteria | NOT_PROPOSED |

No path above is edited by this worker. This table exists to satisfy the
work order's requirement for a zero-edit R5 candidate manifest, not to
pre-approve any future change.

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

Primary risk: a future R5+ implementation of the eight-field shadow
interface could quietly grow into a full second schema with its own
generator, storage, and query surface, recreating exactly the "new registry,
lifecycle standard, or command catalog" this design explicitly rejects.
Corrective action: any R5+ implementation must be reviewed against this
design's own constraint that every field's validation source is an existing
owner (never a new store), and a design that proposes persisting these eight
fields anywhere other than as annotations on an existing governed artifact
should be treated as a stop-condition-adjacent change even if this design
did not observe one.

Secondary risk: the `CORPUS_SEMANTICALLY_ABSORBED` proof requirement's
scope-total-equality rule is exact-match by design, which may prove
operationally brittle (a single miscount blocks the claim entirely).
Corrective action: this design deliberately keeps the rule exact rather than
tolerant, consistent with R3's zero-divergence-tolerance posture on
scope-boundary facts; any future proposal to introduce a tolerance band must
carry its own replay/measurement evidence, not be adopted by default.

Tertiary risk: the S0-S8 reference map's S6 row (`V1 CVF_NATIVE_CONVERTED`)
has no single blanket owner, unlike every other stage, because the
receiving CVF surface varies per capability. A future reader must not treat
this as an owner gap; it is a deliberate design choice reflecting that S6's
owner is always the specific surface the change lands in, and this design's
own Shadow Interface Field Table's `evidenceRefs`/`invalidatedBy` fields
already require citing that specific surface per claim, not a generic S6
owner.

## Decision

`PROCEED_TO_R5_SHADOW_COMMAND_AND_RECEIPT_INVALIDATION`

## Final Disposition

`PROCEED_TO_R5_SHADOW_COMMAND_AND_RECEIPT_INVALIDATION`

Rationale: the S0-S8 reference map cites every stage to an existing
CVF-governed owner with zero new owners proposed; the eight-field shadow
interface is strictly smaller than Layer A (it restates no manifest,
ledger, value matrix, origin graph, or owner map, and every validation
source column points outward); the eight claim tokens are used exactly as
specified in the work order with no invented token or reworded meaning; no
promotion by aggregation is possible under the No Promotion By Aggregation
rule; `CORPUS_SEMANTICALLY_ABSORBED` requires both explicit unread-file
reconciliation and exact scope-total equality; uncertainty is escalation-
only with an explicit negative proof that no field in the interface can be
set to a lighter route by worker declaration alone; S8 upstream-identity
drift invalidates dependent eligibility independent of and regardless of
selected-file hash stability; and all ten required hostile cases resolve to
a named fail-closed route while preserving historical receipt evidence
without preserving current eligibility. This satisfies the paired baseline's
Design Contract and Stop Conditions and the work order's Acceptance
Criteria. The next authorized step is R5 (shadow command applicability and
receipt invalidation), which remains unauthorized by this design and
requires a fresh operator decision and governed dispatch.

## Claim Boundary

This design is a documentation-only, non-implementation shadow-interface and
claim-vocabulary design evidence artifact over existing governed evidence.
It does not implement any interface field, checker, or command; does not
modify any standard, checker, registry, catalog, hook, or router; does not
intake or register any new source corpus; does not authorize selective
execution (`selectiveExecutionAuthorized` remains `false` per the TPGR
standard, independently verified at this executionBaseHead); and does not
open R5-R9, T15, or any runtime, provider/live, public-sync, deployment, or
production action. The `PROCEED_TO_R5_SHADOW_COMMAND_AND_RECEIPT_INVALIDATION`
disposition authorizes only a future operator decision to open R5 under a
fresh governed dispatch; it does not itself authorize R5 work.
