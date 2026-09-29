# CVF TPGR-R5 Shadow Command Applicability And Receipt Invalidation Design

Memory class: governed-planning-assessment

docType: baseline

Status: COMPLETE_PENDING_REVIEW

Batch ID: TPGR-R5

Date: 2026-08-18

executionBaseHead: `e3893b37a391564521ad5dc0af90b5daea9b7e71`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Responds to work order:
`docs/work_orders/CVF_AGENT_WORK_ORDER_TPGR_R5_SHADOW_COMMAND_APPLICABILITY_AND_RECEIPT_INVALIDATION_DESIGN_2026-08-18.md`

Paired baseline authority:
`docs/baselines/CVF_GC018_TPGR_R5_SHADOW_COMMAND_APPLICABILITY_AND_RECEIPT_INVALIDATION_DESIGN_2026-08-18.md`

## Purpose

Design, without implementing, the smallest command-applicability and
receipt-invalidation contract that could make R4's accepted eight-field
shadow interface machine-checkable later, without creating a second command
catalog, receipt store, lifecycle, or router. This design binds every R4
field and claim token to CVF's single existing canonical command catalog by
reference only. This is design evidence and one disposition, not
implementation. It changes no standard, checker, registry, catalog, hook, or
source corpus.

## Source / Predecessor Evidence

| Source | Identity | Authority use |
| --- | --- | --- |
| paired baseline | `docs/baselines/CVF_GC018_TPGR_R5_SHADOW_COMMAND_APPLICABILITY_AND_RECEIPT_INVALIDATION_DESIGN_2026-08-18.md` | complete execution authority for this design |
| paired work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_TPGR_R5_SHADOW_COMMAND_APPLICABILITY_AND_RECEIPT_INVALIDATION_DESIGN_2026-08-18.md` | task manifest, Design Contract, Required Applicability Rows, Required Hostile Cases, Allowed Final Dispositions |
| R4 assessment | `docs/assessments/CVF_TPGR_R4_SHADOW_INTERFACE_AND_CLAIM_VOCABULARY_DESIGN_2026-08-18.md` | Shadow Interface Field Table (eight fields), Exact Claim Vocabulary (eight tokens), No Promotion By Aggregation rule, `CORPUS_SEMANTICALLY_ABSORBED` Proof Requirement, Escalation-Only Uncertainty Treatment, Upstream-Drift (S8) Handling, ten hostile cases, R5 Candidate Command/Receipt Invalidation Manifest, Final Disposition `PROCEED_TO_R5_SHADOW_COMMAND_AND_RECEIPT_INVALIDATION` |
| R4 worker return | `docs/reviews/CVF_TPGR_R4_SHADOW_INTERFACE_AND_CLAIM_VOCABULARY_DESIGN_WORKER_RETURN_2026-08-18.md` | Independent Reviewer Addendum confirming the corpus-semantic-proof repair, the stage-mapping repair, the freshness/route-closure repair, and the derived-state completeness repair, all binding on this design's reuse of R4's field/token definitions |
| R3 assessment | `docs/assessments/CVF_TPGR_R3_ARCHETYPE_THRESHOLD_PROOF_DIVERGENCE_AND_ROLLBACK_FLOOR_DESIGN_2026-08-18.md` | Route Outcomes And Deterministic Precedence, Proof Floors And Evidence-Expiry Rules, Dependency Invalidation Graph, A3/A4 Threshold Worksheets |
| R3 worker return | `docs/reviews/CVF_TPGR_R3_ARCHETYPE_THRESHOLD_PROOF_DIVERGENCE_AND_ROLLBACK_FLOOR_DESIGN_WORKER_RETURN_2026-08-18.md` | Independent Reviewer Addendum confirming R3 evidence |
| TPGR routing standard | `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md` | Mandatory Classification enums, Mandatory Escalation rules, TPGR-T0 Legacy Full-Gate Interlock (shadow-only), Activation Rule |
| canonical command catalog | `governance/compat/agent_autorun_command_catalog.py` | the single command-universe owner this design binds against by reference; `_common_commands`, `_pre_implementation_commands`, `PRE_PUSH_COMMANDS` |

## Scope / Methodology

The worker captured `executionBaseHead` = `e3893b37a391564521ad5dc0af90b5daea9b7e71`
via `git rev-parse HEAD` and confirmed a clean worktree
(`git status --short --untracked-files=all` returned no output) before any
edit. The worker read in full: the paired baseline, the paired work order,
`CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`, `CVF_SESSION_MEMORY.md`,
the guard orientation index, the literal-format gotchas reference, the R4
assessment and its worker return (including the Independent Reviewer
Addendum), the R3 assessment's Route Outcomes, Proof Floors, Dependency
Invalidation Graph, and A3/A4 worksheets sections, the TPGR routing
standard's Mandatory Classification, Mandatory Escalation, TPGR-T0 Legacy
Full-Gate Interlock, and Activation Rule sections, and
`governance/compat/agent_autorun_command_catalog.py` in full. The worker also
read the applicable `governance/compat/check_*.py` checker source listed in
the Checker Source Read-Ahead Block before authoring either output file.

Per the work order, this design uses R4's accepted eight-field interface and
eight-token vocabulary, and R3's accepted route/invalidation rules, as the
predecessor dataset. No new corpus scan, source intake, network access, or
re-derivation of any registry/catalog count was performed. No standard,
checker, registry, catalog, hook, or router is modified by this assessment.
No selective execution is authorized or claimed; `selectiveExecutionAuthorized`
remains `false` per the TPGR standard, independently verified directly by
`check_task_governance_route.py` at this executionBaseHead (`COMPLIANT`, 0
violations, `Legacy gate disposition: RUN_FULL_LEGACY_BUNDLE`).

## Current Owner Map

Exactly one canonical command catalog and the existing per-field/per-token
receipt and evidence owners already established by R2G/R3/R4. No second
catalog or store is proposed anywhere in this design.

| Owner class | Owner | Role in this design |
| --- | --- | --- |
| canonical command catalog | `governance/compat/agent_autorun_command_catalog.py` (`_common_commands`, `_pre_implementation_commands`, `PRE_PUSH_COMMANDS`) | the single command-universe owner every applicability row below cites; the runner selects the common commands plus the commands for the invoked phase, rather than executing every phase-specific list on every governed range |
| TPGR route computation | `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md`; `governance/compat/check_task_governance_route.py` | the sole owner of `taskGovernanceManifest`, profile minimums, and mandatory-escalation computation; this design adds no second routing manifest |
| corpus registration / structural enumeration / ledger | `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md` (GC-051); `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`; `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md`; `check_corpus_scan_registry.py`, `check_external_absorption_core.py` | owner for R4's `intakeStage` S0/S1/S2 rows and `claimToken` `SOURCE_REGISTERED`/`STRUCTURALLY_ENUMERATED`/`LEDGER_DISPOSITIONED` |
| overlap / novelty triage | same core standard; `check_external_absorption_overlap_discipline.py` | owner for `TRIAGE_CLASSIFIED` |
| cluster semantic read / mixed-origin | same core standard; `docs/reference/external_agent_review/CVF_MIXED_ORIGIN_DERIVED_SYNTHESIS_ABSORPTION_STANDARD.md`; `check_mixed_origin_derived_synthesis_absorption.py` | owner for `CLUSTER_SEMANTICALLY_READ` |
| value conversion / capability absorption | same core standard; `check_external_absorption_value_conversion.py` | owner for `CAPABILITY_ABSORBED` |
| blind-spot / corpus completeness / knowledge-map reconciliation | `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md`; `docs/reference/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_STANDARD_2026-06-01.md`; `docs/reference/CVF_CORPUS_TO_KNOWLEDGE_MAP_RECONCILIATION_STANDARD_2026-06-01.md`; `check_absorption_blindspot_control_presence.py`, `check_corpus_completeness_report_integrity.py`, `check_corpus_to_knowledge_map_reconciliation.py` | cross-cutting owner for the `CORPUS_SEMANTICALLY_ABSORBED` unread-file reconciliation and scope-total-equality proof requirement |
| upstream identity / delta accounting | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` delta-ledger vocabulary; the specific prior closure's own disposition trail; the actual current live owner surface | owner for `DELTA_ACCOUNTED` and the upstream-drift (S8) `invalidatedBy` rule |
| review authority / role confirmation | `docs/reference/guard_orientation/README.md` Role Glossary | owner for `reviewAuthority` |
| worker-return structural/semantic evidence | `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/run_worker_return_fast_gate.py` | owner for worker-return shape/semantic evidence that any future receipt cites as `evidenceRefs` |
| dependency invalidation precedence | R3's Dependency Invalidation Graph (`docs/assessments/CVF_TPGR_R3_ARCHETYPE_THRESHOLD_PROOF_DIVERGENCE_AND_ROLLBACK_FLOOR_DESIGN_2026-08-18.md`) | owner for `invalidatedBy` node matching, reused unchanged by this design |
| full legacy autorun bundle | `governance/compat/agent_autorun_command_catalog.py` as invoked by `governance/compat/run_agent_autorun_workflow_gate.py` and `governance/compat/run_local_governance_hook_chain.py` | owner for `RUN_FULL_LEGACY_BUNDLE`; every path/scope-family gate in `_common_commands` remains mandatory regardless of any candidate applicability row below |

No owner class above is newly created by this design. Every row cites an
existing CVF-governed standard, schema, or checker already verified current
at this `executionBaseHead`. This design's six documentation-only candidate
fields (below) are annotations that reference these owners; they persist no
independent state.

## R4 Invariant-To-Command Applicability Matrix

Every row below covers one of the eight R4 interface fields, one of the
eight R4 claim tokens, no-promotion-by-aggregation, corpus semantic proof,
uncertainty escalation, or upstream drift, with none omitted. Applicability enum is exactly `ALWAYS`,
`CONDITIONAL`, or `NOT_APPLICABLE_WITH_REASON`. Many rows reuse the same
canonical command owner (many-to-one), consistent with the work order's
preference against assuming one command per field.

### Eight Interface Fields

| R4 field | Applicability | Canonical command owner (by reference) | Rationale |
| --- | --- | --- | --- |
| `intakeStage` | `CONDITIONAL` | corpus scan registry (`check_corpus_scan_registry.py`), external absorption core (`check_external_absorption_core.py`), overlap discipline, mixed-origin, value conversion - selected by which S0-S8 stage the record claims | activation predicate: a record asserts a specific `intakeStage` value; required input/evidence: the stage's own canonical owner checker output re-parsed at claim time, never worker declaration; false-positive exclusion: prose describing the S0-S8 map in general terms (no specific record asserting a stage) is not a claim; failure route: missing/out-of-enum `intakeStage` routes to `FULL_LAYER_A_REQUIRED`; invalidation trigger: any change to the stage's owning standard/checker per the R3 Dependency Invalidation Graph |
| `claimToken` | `CONDITIONAL` | the specific token's owner row below (per-token table) | activation predicate: a record asserts one of the eight exact tokens; required input/evidence: the token's own proof requirement (per-token table) satisfied by current owner evidence; false-positive exclusion: a table cell or prose sentence explaining what a token means, without a `claimToken:`-shaped assertion line binding it to a `claimScopeRef`, is descriptive, not asserted; failure route: unknown/missing/malformed token routes to `ESCALATE_FOR_REVIEW` at minimum (R4 Hostile Case 5); invalidation trigger: any redefinition of the eight-token table itself (out of scope for any tranche through R5) |
| `claimScopeRef` | `CONDITIONAL` | the stage's manifest/ledger owner (S1/S2) or the named-cluster list owner (S4); no independent command of its own | activation predicate: a `claimToken` is asserted (scope only matters relative to a token); required input/evidence: the exact enumerated scope, independently countable from the diff or manifest the token's owner already produces; false-positive exclusion: an approximate or descriptive scope mention with no asserted token is not a scope claim; failure route: missing scope routes to `FULL_LAYER_A_REQUIRED`/`ESCALATE_FOR_REVIEW` per R3 Rule 2; scope exceeding evidence by even one file fails per R4 Hostile Case 6; invalidation trigger: any detected divergence between declared and independently recomputed scope |
| `evidenceRefs` | `CONDITIONAL` | the cited artifact/receipt's own owner surface, re-read directly (no new evidence-index command) | activation predicate: a claim cites one or more evidence paths; required input/evidence: each cited path must exist and remain current at claim-verification time; false-positive exclusion: a citation used only as background context, not as the proof basis for a specific `claimToken`, is not an evidence-ref claim; failure route: missing or dangling reference routes to `ESCALATE_FOR_REVIEW`/`FULL_LAYER_A_REQUIRED` per the S0-S8 owner the reference should have come from; invalidation trigger: the cited artifact's own expiry per the R3 Dependency Invalidation Graph |
| `invalidatedBy` | `ALWAYS` | R3's Dependency Invalidation Graph, re-run directly against current repository state (no independent command; the graph's matching rule is evaluated by re-reading the named owner surfaces) | this field must always be evaluated for any current-eligible record; it is never optional once a record claims `eligibilityState: CURRENT` | 
| `reviewAuthority` | `ALWAYS` | `docs/reference/guard_orientation/README.md` Role Glossary | a claim's confirming role must always be checked against the fixed Role Glossary enum before the claim can be current-eligible; a worker can never self-assign as its own confirming authority |
| `routeOutcome` | `ALWAYS` | `check_task_governance_route.py`; R3's Route Outcomes And Deterministic Precedence | the route is always independently computed from the other seven fields; it is never worker-assertable as final under any condition |
| `eligibilityState` | `ALWAYS` | this design's own derivation rule (R4-stated), evaluated against `routeOutcome`, `invalidatedBy`, and `reviewAuthority` confirmation state - no independent command; a pure function over already-owned facts | a derived view must always be recomputed, never cached or worker-declared, because it is the single field most exposed to stale-receipt survival |

### Eight Claim Tokens

| R4 token | Applicability | Canonical command owner (by reference) | Rationale |
| --- | --- | --- | --- |
| `SOURCE_REGISTERED` | `CONDITIONAL` | `check_corpus_scan_registry.py`; GC-051 registry JSON | activation predicate: a record asserts source identity/scope is known for a named corpus; required input/evidence: a current GC-051 registry entry for that exact scope; false-positive exclusion: a corpus mentioned in prose without a registration claim is not asserted; failure route: missing/stale registry entry routes to `FULL_LAYER_A_REQUIRED`; invalidation trigger: registry entry re-registration, removal, or GC-051 standard/checker change |
| `STRUCTURALLY_ENUMERATED` | `CONDITIONAL` | `check_external_absorption_core.py` manifest/hash evidence | activation predicate: a record asserts manifest/hash/count reconciliation; required input/evidence: an independently recomputed manifest matching the claimed count; false-positive exclusion: a stated intent to enumerate, without a produced manifest, is not asserted; failure route: unreconciled manifest/hash routes to `FULL_LAYER_A_REQUIRED`; invalidation trigger: any change to the core standard/checker or a filesystem-state drift in the claimed scope |
| `LEDGER_DISPOSITIONED` | `CONDITIONAL` | `check_external_absorption_core.py` terminal ledger evidence | activation predicate: a record asserts every manifest item has a terminal disposition; required input/evidence: a current ledger with zero non-terminal rows for the claimed scope; false-positive exclusion: a partial or in-progress ledger mention is not asserted; failure route: any non-terminal row routes to `FULL_LAYER_A_REQUIRED`; invalidation trigger: core standard/checker change, or a ledger row's disposition being superseded |
| `TRIAGE_CLASSIFIED` | `CONDITIONAL` | `check_external_absorption_overlap_discipline.py` | activation predicate: a record asserts overlap/novelty triage completed; required input/evidence: a current overlap-discipline classification for every ledger item in scope; false-positive exclusion: an unclassified or "pending triage" mention is not asserted; failure route: incomplete triage routes to `FULL_LAYER_A_REQUIRED`/`ESCALATE_FOR_REVIEW`; invalidation trigger: overlap-discipline standard/checker change |
| `CLUSTER_SEMANTICALLY_READ` | `CONDITIONAL` | `check_mixed_origin_derived_synthesis_absorption.py` for mixed-origin clusters; the core standard's cluster-scope evidence otherwise | activation predicate: a record asserts one exact named cluster was substantively read; required input/evidence: `claimScopeRef` enumerates the exact cluster file list, independently countable; false-positive exclusion: per No Promotion By Aggregation (below), this token never sums across clusters into a broader claim; failure route: scope exceeding the read evidence routes to `ESCALATE_FOR_REVIEW` (R4 Hostile Case 6); invalidation trigger: any file in the named cluster changing, or the corpus's own C0-C2 receipts expiring |
| `CAPABILITY_ABSORBED` | `CONDITIONAL` | `check_external_absorption_value_conversion.py`; the specific receiving CVF owner surface itself (S6 has no single blanket owner by design, per R4's Risk section) | activation predicate: a record asserts a bounded capability materialized in a named CVF owner; required input/evidence: the specific receiving owner surface's own current state showing the change landed; false-positive exclusion: a proposed-but-not-materialized capability is not asserted; failure route: unmaterialized or unverifiable landing routes to `FULL_LAYER_A_REQUIRED`; invalidation trigger: the receiving owner surface's own subsequent change |
| `CORPUS_SEMANTICALLY_ABSORBED` | `CONDITIONAL` | `check_corpus_completeness_report_integrity.py`; `check_corpus_to_knowledge_map_reconciliation.py`; `check_absorption_blindspot_control_presence.py` jointly, per R4's Proof Requirement (explicit unread-file reconciliation plus exact scope-total equality) | activation predicate: a record asserts the highest corpus semantic claim; required input/evidence: both R4 Proof Requirement conditions satisfied simultaneously at claim time from current owner evidence, never inherited from a partial state; false-positive exclusion: a bare `NO_NEW_VALUE` terminal label contributes zero to the semantic evidence count (R4's reviewer-repaired rule); failure route: either condition unmet routes to `ESCALATE_FOR_REVIEW` (R4 Hostile Case 10), never silently downgraded by the claimant; invalidation trigger: any single file in the claimed scope losing its `CURRENT` cluster-read status, or a scope-count mismatch appearing |
| `DELTA_ACCOUNTED` | `CONDITIONAL` | the core standard's delta-ledger classification vocabulary; the actual current live owner surface (never a cached copy), per R3's A4 worksheet | activation predicate: a record asserts upstream change enumerated against a pinned prior; required input/evidence: a fresh delta classification comparing the current live owner surface, not the surface as it stood at the prior closure; false-positive exclusion: citing the prior closure's disposition trail alone, without a fresh live-surface comparison, is not asserted; failure route: unreconciled delta scope routes to `FULL_LAYER_A_REQUIRED` for the affected scope (R3 A4 default); invalidation trigger: any further upstream identity change beyond the one already reconciled |

### Cross-Cutting Invariants

| Invariant | Applicability | Canonical command owner (by reference) | Rationale |
| --- | --- | --- | --- |
| no-promotion-by-aggregation | `ALWAYS` | no independent command; this is a pure evaluation rule over `CLUSTER_SEMANTICALLY_READ` receipts already owned by the core/mixed-origin standards above | must always be evaluated whenever multiple `CLUSTER_SEMANTICALLY_READ` receipts exist for one corpus, to prevent silent promotion to `CORPUS_SEMANTICALLY_ABSORBED`; this is not conditional because the aggregation hazard exists any time two or more scope-bound receipts share a corpus, regardless of how the claim is phrased |
| corpus semantic proof | `ALWAYS` | `CORPUS_SEMANTICALLY_ABSORBED` Proof Requirement owners (above) | must always gate any `CORPUS_SEMANTICALLY_ABSORBED` assertion; there is no lighter-weight path |
| uncertainty escalation | `ALWAYS` | no independent command; a pure evaluation rule applied to every field's "who may assert it" column in R4's Shadow Interface Field Table | must always discard a worker's declared uncertainty/confidence as a route input; this is unconditional because R4's Escalation-Only Uncertainty Treatment applies to every field, not a subset |
| upstream drift (S8) | `CONDITIONAL` | the core standard's delta-ledger vocabulary plus independent upstream-identity comparison (pinned commit/mirror hash), separate from and in addition to file-level hash checks | activation predicate: a record's `claimScopeRef` traces back to a pinned upstream source; required input/evidence: the upstream source's current pinned identity, independently re-read, compared against the identity recorded at claim time; false-positive exclusion: a record whose scope never traced to a pinned upstream source (a purely local artifact) is not subject to this invariant; failure route: identity change routes affected records' `eligibilityState` from `CURRENT` to `EXPIRED_HISTORICAL` immediately, even if selected-file hashes are stable (R4 Hostile Case 3); invalidation trigger: the upstream pinned identity's own change, evaluated independently of file-hash comparison |

### Required Applicability Rows (Work-Order Minimum Set)

| Required row | Applicability | Canonical command owner | Rationale |
| --- | --- | --- | --- |
| task route classification | `ALWAYS` | `check_task_governance_route.py` | every governed work order with a `DISPATCH_READY`/`READY`/`ACTIVE`/`APPROVED_FOR_EXECUTION` status must carry a routing manifest per the TPGR Activation Rule; this is unconditional |
| worker-return structural/semantic evidence | `ALWAYS` | `check_worker_return_quality_gate.py`; `check_markdown_structural_completeness.py`; `run_worker_return_fast_gate.py` | every worker-return artifact this design's future receipts would cite as `evidenceRefs` must pass these checkers; unconditional for any worker-return-shaped evidence source |
| corpus registration, ledger, blind-spot, knowledge-map reconciliation | `CONDITIONAL` | `check_corpus_scan_registry.py`; `check_external_absorption_core.py`; `check_absorption_blindspot_control_presence.py`; `check_corpus_to_knowledge_map_reconciliation.py` | activation predicate: a claim touches `SOURCE_REGISTERED` through `CORPUS_SEMANTICALLY_ABSORBED`; required input/evidence: the four owners' current joint output for the claimed scope; false-positive exclusion: a claim scoped to a single named file with no corpus registration claim does not activate this row; failure route: any owner returning non-current or absent evidence routes to `FULL_LAYER_A_REQUIRED`; invalidation trigger: any of the four owning standards/checkers changing |
| claim vocabulary/no-aggregation detection candidate | `CONDITIONAL` | no command exists today (R4's own R5 Candidate Manifest names `check_shadow_interface_claim_vocabulary.py` as `UNAUTHORIZED`, candidate-name-only); until authorized, this row's canonical owner is the reviewer's own direct re-application of R4's No Promotion By Aggregation text | activation predicate: a claim asserts or implies a `claimToken`; required input/evidence: reviewer re-derivation of the token's proof requirement directly from R4's Exact Claim Vocabulary section (no machine command exists yet); false-positive exclusion: descriptive prose about the vocabulary itself, without a `claimToken:`-shaped assertion, does not activate; failure route: absent a future checker, any claim of this class routes to `ESCALATE_FOR_REVIEW` until a human reviewer confirms it, never to `LIGHT_ROUTE_ALLOWED` by default; invalidation trigger: authorization and creation of the named future checker (R6+ only) |
| upstream identity and selected-file hash comparison | `CONDITIONAL` | the core standard's delta-ledger vocabulary plus independent upstream-identity comparison, as in the upstream-drift cross-cutting row above | activation predicate: a claim's scope traces to a pinned upstream source; required input/evidence: both the pinned-identity comparison and the selected-file hash comparison, evaluated as two independent facts, never one standing in for the other; false-positive exclusion: a purely local claim with no upstream pin does not activate; failure route: identity drift alone (even with stable file hashes) routes to `FULL_LAYER_A_REQUIRED` for the delta scope; invalidation trigger: either fact changing independently |
| owner/checker/catalog freshness | `ALWAYS` | R3's Dependency Invalidation Graph, applied against current filesystem state of every named standard/checker/catalog row | every current-eligible claim must always have its owner/checker/catalog freshness re-checked before `eligibilityState` can be `CURRENT`; this is the mechanism that prevents stale-receipt survival across checker hardening |
| full legacy autorun bundle | `ALWAYS` | `governance/compat/agent_autorun_command_catalog.py` via `run_agent_autorun_workflow_gate.py` / `run_local_governance_hook_chain.py` | per TPGR-T0's Legacy Full-Gate Interlock, every command in `_common_commands` (and the phase-specific pre-implementation/pre-push commands) remains mandatory regardless of any applicability row above; no row in this matrix reduces this bundle |
| non-applicable families with explicit reason | `NOT_APPLICABLE_WITH_REASON` | N/A | see the dedicated Non-Applicable Families table below |

### Non-Applicable Families (Explicit Reasons)

| Family | Applicability | Reason |
| --- | --- | --- |
| a second command catalog or discovery mechanism | `NOT_APPLICABLE_WITH_REASON` | the work order and paired baseline both forbid a second catalog; `governance/compat/agent_autorun_command_catalog.py` remains the sole command-universe owner for every row above |
| a new receipt persistence store, schema, or generator | `NOT_APPLICABLE_WITH_REASON` | the six documentation-only candidate fields (Receipt Ownership Table, below) are annotations on existing governed artifacts, never a new store; R4's own Risk section already flags this as a stop-condition-adjacent hazard for any future implementation |
| selective/light-route command omission | `NOT_APPLICABLE_WITH_REASON` | TPGR-T0's Legacy Full-Gate Interlock keeps `selectiveExecutionAuthorized: false` and `RUN_FULL_LEGACY_BUNDLE` mandatory through this tranche; no applicability row above authorizes skipping any catalog command |
| runtime, provider/live, public-sync, deployment, or production command binding | `NOT_APPLICABLE_WITH_REASON` | out of scope per the work order's Claim Boundary and this design's own Delta Execution Claim Boundary Control Block; no catalog command in this class is bound to any R4 field or token by this design |

Every family above is a deliberate exclusion, not an unexamined gap: each was
evaluated against the eight fields, eight tokens, and cross-cutting
invariants and found to have no applicable binding under this design's
one-catalog constraint.

## Receipt Ownership Table

Exactly the six documentation-only candidate fields named in the paired
baseline's `docOnlyNewFields` list and the work order's Design Contract item
4. None is implemented, persisted, or given a schema by this design.

| Candidate field | Owner (annotation target) | Populated from | Invalidated by | Never independently persisted because |
| --- | --- | --- | --- | --- |
| `commandApplicability` | the specific R4 field/token row it annotates, in the applicability matrix above | the applicability matrix's own `ALWAYS`/`CONDITIONAL`/`NOT_APPLICABLE_WITH_REASON` value for that row, re-derived at claim time | any change to the row's canonical command owner (catalog row addition/removal/semantic change) | it restates only what the matrix above already states; a future implementation should annotate an existing artifact's own claim row, not create a parallel index |
| `receiptOwnerRef` | an identity-bound reference set for the existing evidence owner, catalog membership, and confirming review evidence | the applicability matrix's "canonical command owner" column plus the exact identities defined in the Identity-Binding Contract below | any mismatch in the referenced semantic dependency closure, command row, or confirming review artifact | it is carried with the existing claim/evidence record and points into existing governed surfaces; it is not a new registry of owners |
| `invalidationEvent` | R3's Dependency Invalidation Graph node that fired, if any | direct re-application of R3's graph-matching rule against current repository state | superseded automatically each time the graph is re-run; the event itself is a point-in-time fact, not a stored row | the graph is already the owner; this field only names which of its existing nodes fired for a specific claim, it does not extend the graph |
| `invalidationScope` | the exact `claimScopeRef` (or sub-scope) affected by the fired `invalidationEvent`, per the Invalidation Precedence rule (below) | the earliest affected node's own scope boundary, never a broader scope by default | any correction to the earliest-affected-node determination itself | scope is derived from the precedence rule applied to already-owned facts, not tracked as independent state |
| `recomputeFromNode` | the specific dependency-graph node identifier from which fresh evidence must be re-derived before re-earning current eligibility | R3's Dependency Invalidation Graph, read at the earliest affected node | superseded whenever a fresh, owner-verified re-derivation from that node succeeds and produces new evidence | it names a starting point for re-verification; it is not itself proof and carries no independent authority |
| `historicalDisposition` | the specific expired or void claim's own prior `routeOutcome`/`eligibilityState` pair, preserved as immutable evidence | the claim's own record at the moment `invalidatedBy` fired, per R3's historical-receipt-immutability rule | never invalidated itself; historical evidence is immutable by design (only `eligibilityState` on the live view moves to `EXPIRED_HISTORICAL`, the historical record is not rewritten) | it is a preserved snapshot of a fact that already existed, not a new live-state field requiring its own freshness tracking |

All six fields describe how an existing owned fact would be annotated onto
an existing governed artifact in a future R6+ implementation; none proposes
a query surface, index, generator, or lifecycle of its own. This satisfies
the paired baseline's Design Contract item on receipt ownership without
creating "a second command catalog, receipt store, lifecycle, or router."

### Identity-Binding Contract

`receiptOwnerRef` is not a bare path and a timestamp is never an identity.
For design purposes it is an ordered reference set carried by the existing
claim/evidence artifact and containing, as applicable:

1. the normalized owner path and owner symbol/section plus the immutable Git
   blob identity (or an equivalently exact content digest) observed when the
   evidence was accepted;
2. the checker entry path plus the identities of every repository-local
   imported policy/schema/config surface in the checker's semantic dependency
   closure that can change its verdict for this evidence class;
3. the stable command-row key, serialized command/arguments, and catalog blob
   identity observed when the receipt was accepted; and
4. the confirming review artifact path, confirming role, and immutable review
   artifact identity, not merely the role name from the Role Glossary.

The current values are compared with those recorded identities before a claim
can remain `CURRENT`. If the semantic dependency closure cannot be enumerated
or any required recorded identity is absent, freshness is unknown and the
affected scope routes to `FULL_LAYER_A_REQUIRED`; a bare path match never
proves currency. This adds no catalog or store: the reference set is proposed
metadata on the already-existing claim/evidence artifact, and R6 must replay
whether it can be derived without duplicating Layer A evidence.

## Invalidation Precedence

Exactly the six-level order required by the work order. Earliest affected
node controls; historical evidence remains immutable; current eligibility
expires. This precedence is evaluated top-to-bottom; the first level at
which a change is detected is the earliest affected node for that claim, and
invalidation scope never expands past what that node's own scope covers.

1. **Source identity** - the pinned upstream commit/mirror hash, or (for a
   purely local claim) the specific file identity the claim was made about.
   Reused unchanged from R4's Upstream-Drift (S8) Handling section: identity
   change invalidates independent of and regardless of selected-file hash
   stability.
2. **Owner surface** - the specific CVF owner surface (a `docs/reference/`
   standard, a schema, a registry entry, or the receiving surface for an S6
   `CAPABILITY_ABSORBED` claim) the claim's evidence was compared against.
   Reused from R3 Rule 4 and R3 A4's "the actual current owner surface, not
   a cached copy" rule. Detection compares the current owner identity with
   the identity recorded in `receiptOwnerRef`; a current path alone is not
   sufficient.
3. **Schema/registry** - the specific registry entry (for example a GC-051
   entry) or schema the claim's manifest/ledger evidence depends on.
4. **Checker semantics** - the specific `governance/compat/check_*.py` file's
   semantic dependency closure, independent of whether its filename or
   command row changed. Detection compares the checker and every verdict-
   affecting repository-local imported policy/schema/config identity recorded
   in `receiptOwnerRef`; if that closure is unknown or incomplete, freshness
   fails closed. This directly resolves R5 Hostile Case 2: a same-path checker
   semantic change is detected even when command-catalog membership is stable.
5. **Command-catalog membership** - whether the same stable row key and
   serialized command/arguments recorded in `receiptOwnerRef` still exist in
   the current catalog and belong to the invoked phase. This directly
   resolves R5 Hostile Case 3 (a catalog row is removed while an old receipt
   still cites it): removal or mutation at this level invalidates the affected
   claim even though the checker file itself may still exist on disk.
6. **Review authority** - whether the confirming role remains valid and the
   identity-bound confirming review artifact recorded in `receiptOwnerRef`
   still represents the current accepted disposition, including any later
   reviewer correction or revocation.
   This directly resolves R5 Hostile Case 9 (a receipt has every field but
   its review authority changed): a change at this level invalidates even
   when every other field is unchanged.

Binding rules for this precedence, mirroring R3 Rule 4 and the R4 historical-
immutability rule:

- **Earliest affected node controls.** Evaluation proceeds top-to-bottom;
  the invalidation fires at the first (lowest-numbered) level where a change
  is detected, and `invalidationScope` is bounded to exactly what that
  level's own scope covers, never expanded to unrelated evidence at a lower
  precedence level that was not itself affected. This directly resolves R5
  Hostile Case 12 (invalidation cascades beyond the earliest affected scope
  and needlessly reopens unrelated evidence): a level-4 checker-semantics
  change invalidates only claims whose evidence depended on that specific
  checker's semantics, not every claim anywhere in the corpus.
- **Historical evidence remains immutable.** Whatever the claim's record
  stated at the moment of firing is preserved verbatim as
  `historicalDisposition`; it is never deleted or rewritten, per R3's
  historical-receipt-immutability rule and R4's Hostile Cases 3/7 preserved-
  evidence columns.
- **Current eligibility expires.** Only the live `eligibilityState` view
  moves from `CURRENT` to `EXPIRED_HISTORICAL` (never `NEVER_ELIGIBLE`,
  since the claim was once validly current); the underlying preserved record
  is not touched.
- **An unbound identity is not current.** A path-only owner reference, a role
  name without its confirming review artifact, or a catalog command without
  its stable row identity cannot establish freshness and therefore cannot
  support `CURRENT` eligibility.

## Re-Earning Rule

Later claims become current only from fresh canonical-owner evidence
produced after the invalidating event; no stale receipt revival, and no
worker declaration can restore eligibility, under any circumstance.

- A claim whose `eligibilityState` is `EXPIRED_HISTORICAL` can return to
  `CURRENT` only by a fresh, independently owner-verified re-derivation
  starting at the `recomputeFromNode` value, producing genuinely new
  evidence (a new manifest re-read, a new ledger reconciliation, a new
  reviewer confirmation, or equivalent), never by re-asserting the old
  `evidenceRefs` unchanged.
- Copying an expired claim's fields into a new artifact with a new
  timestamp does not re-earn eligibility, because the underlying owner
  evidence the copy points to is still the same stale evidence; only a
  fresh, independently re-verified owner check re-earns it. This directly
  resolves R5 Hostile Case 10 (a stale receipt is copied into a new artifact
  with a new timestamp): the timestamp is not itself evidence, and the copy
  inherits `EXPIRED_HISTORICAL` status from its source evidence, not
  `CURRENT` status from its new authoring date.
- A worker's own declaration that a field is "still fine" or "re-verified"
  is discarded exactly as R4's Escalation-Only Uncertainty Treatment already
  discards worker-declared uncertainty; only independently observable owner
  state re-earns eligibility. This directly resolves R5 Hostile Case 1 (a
  worker marks a costly command `NOT_APPLICABLE_WITH_REASON` to obtain a
  lighter route): a worker-authored `NOT_APPLICABLE_WITH_REASON` disposition
  on any applicability row is not itself proof; it is treated as a proposed
  classification pending independent reviewer confirmation against the
  matrix above, exactly as R3's `WORKER_PROPOSES, OWNER_CONFIRMS` pattern
  already requires for overlap/novelty classification.
- Re-earning one field does not re-earn a sibling field at a different
  precedence level; each level's evidence must be independently fresh.

## False-Positive Boundary

Design-only detection surfaces (no regex or code is specified; this
describes what a future R6+ checker would need to distinguish, per the work
order's instruction to design the surface without implementing it).

| Surface | Boundary rule | Why it is not an asserted claim |
| --- | --- | --- |
| descriptive prose | a sentence explaining what a `claimToken` or `intakeStage` value means, without an accompanying `claimScopeRef` binding it to a specific enumerated scope | a definition is not a claim about any particular file set; this mirrors R4's own Exact Claim Vocabulary table, which itself contains every token name without asserting any of them |
| tables explaining tokens | a table (such as the Exact Claim Vocabulary table, or this design's own applicability matrix) whose row labels are the token/field names themselves, used as column headers or row keys rather than as values inside a populated claim record | the table's function is taxonomy, not assertion; a future checker's detection surface must distinguish a taxonomy table (token name as row label) from a claim record (token name as a field value inside a record that also has a populated `claimScopeRef`) |
| archived history | a claim token appearing inside a file under an `/archive/` path segment, or a file whose own status marks it historical/superseded | R4 Hostile Case 7 (a historical archived document containing a claim token triggers current enforcement) requires this exclusion explicitly; an archived document's claim tokens describe what was true when archived, not a current assertion |
| code fences | a claim token appearing inside a fenced code block (` ``` `) illustrating example syntax, JSON shape, or a command's expected output | code fences are illustrative, not assertive; this mirrors gotcha 5 in the literal-format gotchas reference (a backtick-quoted heading example is not the real heading) applied to claim tokens instead of headings |
| quoted examples | a claim token appearing inside a hostile-case description, a worked example, or a "for instance" illustration explicitly framed as hypothetical | the surrounding framing (a hostile-case number, an "e.g." marker, or equivalent) marks the token as illustrative rather than a live assertion about the document's own subject matter |
| incomplete draft artifacts | a claim token appearing in a file whose own `Status:` field is not a claim-eligible status (for example `DISPATCH_READY`, `DRAFT`, or any status other than a status this design's future implementation would define as claim-bearing) | R4's own eligibility model already ties currency to `reviewAuthority` confirmation; a draft with no confirming review cannot be `CURRENT` regardless of what tokens its prose contains |

The common design principle across all six rows: a future detection surface
must require an assertion-shaped structure (a token bound to a populated,
enumerated `claimScopeRef` inside a document whose status is claim-eligible
and whose location is not archived) before treating any token occurrence as
a live claim. Bare substring presence of a token name is never sufficient by
itself, mirroring the literal-format gotchas reference's own repeated lesson
that naive substring/heading matching produces false positives (gotchas 5,
21, 22, 35 in `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`).
This directly resolves R5 Hostile Case 8 (descriptive prose or a code fence
explaining a token is mistaken for an asserted claim).

## Cost Proof

Candidate routing must not add duplicate command discovery or replay on top
of unavoidable Layer A evidence. This section separates always-on legacy
bundle cost from projected future selective value, per the work order's
Design Contract item 8.

### Always-On Legacy Bundle Cost (Unavoidable, Never Reduced By This Design)

Per TPGR-T0's Legacy Full-Gate Interlock, the current runner executes the
complete catalog bundle applicable to the invoked lifecycle phase: the common
commands plus that phase's additional command list. It does not execute every
other phase-specific list on every governed range. For this review the full
pre-implementation phase bundle is the unavoidable bundle regardless of any
applicability row in this design.
This design's applicability matrix adds zero new command invocations to that
bundle: every "canonical command owner" cited above is a command that
already runs as part of `_common_commands` today, independent of whether
this design exists. `RUN_FULL_LEGACY_BUNDLE` remains the mandatory
disposition per the Verification Commands section and the paired baseline's
own Stop Conditions.

### Projected Future Selective Value (Not Authorized By This Design)

If a future, separately authorized R6+ tranche implemented a real
`commandApplicability` field and its `CONDITIONAL` activation predicates as a
machine-checked receipt, the only value this design projects is: a future
selective-execution decision (still requiring its own TPGR-T2/T4 equivalence
evidence per the Legacy Full-Gate Interlock) could route a claim's
verification directly to the specific `CONDITIONAL` row's already-existing
canonical command owner, instead of re-discovering which of the roughly
eighty catalog commands applies by re-reading this design's matrix manually
each time. This is a routing-time-saving projection only, is `UNKNOWN` and
unmeasured (no such receipt has ever been attached to a routed task, exactly
as R3's Per-Archetype Cost Ceilings table records for every archetype), and
under R3 Rule 6 cannot claim positive net value; it remains `PROJECTED` and
carries an explicit future measurement requirement, not an assumption this
design relies on for its own disposition.

### No Duplicate Discovery Or Replay

No row in the R4 Invariant-To-Command Applicability Matrix invents a second
discovery mechanism: every "canonical command owner" cell names an existing
`GateCommand` row, standard section, or graph node already present in the
catalog, R3's Dependency Invalidation Graph, or R4's field/token tables. No
row proposes re-running a command that a `CONDITIONAL` predicate's own owner
does not already run as part of the unavoidable Layer A evidence its stage
requires. This satisfies the paired baseline's Stop Condition: "exceeds the
existing Layer A evidence cost it is meant to route."

Identity comparison is not declared free. Reading the recorded/current owner,
semantic-dependency, catalog-row, and review-artifact identities is candidate
routing overhead, while rerunning an applicable Layer A checker remains Layer A
evidence cost. R5 has no live receipt telemetry, so the marginal identity-
comparison cost is `UNKNOWN`/`PROJECTED`; R6 must replay it across the six
archetypes and must revise or stop if it duplicates discovery/replay or exceeds
the Layer A evidence cost. R5 therefore proves only that it introduces no new
command invocation today, not that a future implementation has zero cost.

## Hostile Cases

All twelve cases exactly as required by the work order. Each resolves to a
named, deterministic route: `FULL_LAYER_A_REQUIRED`, `ESCALATE_FOR_REVIEW`,
or preservation of an unaffected current sub-claim with an explicit reason.
No case selects `LIGHT_ROUTE_ALLOWED`.

| # | Hostile scenario | Resolved route | Preserved evidence | Why (binding rule) |
| --- | --- | --- | --- | --- |
| 1 | a worker marks a costly command `NOT_APPLICABLE_WITH_REASON` to obtain a lighter route | `ESCALATE_FOR_REVIEW`; the worker-authored disposition is treated as `WORKER_PROPOSES` only, never `OWNER_CONFIRMS` | the worker's proposed reason is recorded for reviewer diagnosis but licenses no route on its own | Re-Earning Rule (worker declaration cannot restore or grant eligibility); R3's `WORKER_PROPOSES, OWNER_CONFIRMS` pattern; Anti-Self-Downgrade Invariants |
| 2 | a checker changes semantics but its filename and command row remain stable | `FULL_LAYER_A_REQUIRED` for every claim whose evidence depended on that checker's semantic dependency closure; unknown closure also fails closed | pre-change evidence remains historical (`historicalDisposition`), preserved as what was true before the semantic change | Invalidation Precedence level 4 plus the Identity-Binding Contract; bare path/row stability cannot prove semantic currency |
| 3 | a command-catalog row is removed while an old receipt still cites it | `FULL_LAYER_A_REQUIRED` for any claim whose `receiptOwnerRef` pointed to the removed row | the old receipt's `historicalDisposition` remains immutable evidence of what it once cited | Invalidation Precedence level 5 (command-catalog membership); Re-Earning Rule (no stale receipt revival) |
| 4 | upstream identity changes while selected file hashes remain stable | `FULL_LAYER_A_REQUIRED` for the affected delta scope; affected records' `eligibilityState` moves `CURRENT` -> `EXPIRED_HISTORICAL` immediately | pre-drift receipts remain historical evidence of what was true before the identity change | Invalidation Precedence level 1 (source identity), reused unchanged from R4's Upstream-Drift (S8) Handling section and R4 Hostile Case 3 |
| 5 | a bare `NO_NEW_VALUE` ledger label is offered as corpus semantic proof | `ESCALATE_FOR_REVIEW`; the label contributes zero to the scope-total-equality count | the `LEDGER_DISPOSITIONED`-level evidence the label actually supports remains valid at its own stage | `CORPUS_SEMANTICALLY_ABSORBED` token row's proof requirement, reused unchanged from R4's reviewer-repaired corpus semantic proof rule |
| 6 | ten cluster receipts are aggregated into a corpus claim | `ESCALATE_FOR_REVIEW`; the aggregated `CORPUS_SEMANTICALLY_ABSORBED` claim is rejected outright | the ten underlying `CLUSTER_SEMANTICALLY_READ` receipts remain valid as exactly what they are: ten separate scope-bound claims | no-promotion-by-aggregation cross-cutting invariant, reused unchanged from R4's No Promotion By Aggregation section |
| 7 | a historical archived document containing a claim token triggers current enforcement | preservation of the unaffected current state with explicit reason: the archived document's token is not a live claim and enforcement does not fire | the archived document's content remains valid evidence of what it stated when archived | False-Positive Boundary "archived history" row; R4 Hostile Case 7 |
| 8 | descriptive prose or a code fence explaining a token is mistaken for an asserted claim | preservation of the unaffected current state with explicit reason: prose/code-fence occurrences lack the assertion-shaped structure (populated `claimScopeRef` inside a claim-eligible document) required to be a live claim | the surrounding document's own actual claims (if any) remain independently evaluated on their own merits | False-Positive Boundary "descriptive prose" and "code fences" rows |
| 9 | a receipt has every field but its review authority changed | `FULL_LAYER_A_REQUIRED` (or `ESCALATE_FOR_REVIEW` if the change is itself ambiguous) for the affected claim; `eligibilityState` moves to `EXPIRED_HISTORICAL` | the receipt's other seven fields remain historical evidence of what was recorded, but license no current claim without a valid confirming authority | Invalidation Precedence level 6 plus the identity-bound confirming review artifact; a role label alone cannot establish current authority |
| 10 | a stale receipt is copied into a new artifact with a new timestamp | `FULL_LAYER_A_REQUIRED` (or the receipt's pre-existing `EXPIRED_HISTORICAL` state is simply carried forward, never upgraded to `CURRENT`) | both the original and the copy remain historical evidence of what was claimed and when; the copy's new timestamp is not itself evidence | Re-Earning Rule (copying does not re-earn eligibility); R5 Hostile Case 10 resolution above |
| 11 | one dependency fact is unknown and the worker declares low uncertainty | `ESCALATE_FOR_REVIEW`; the worker's low-uncertainty declaration is discarded entirely, not averaged or partially honored | any other independently verified fields on the same record remain visible for reviewer diagnosis, but license no claim on their own | R4's Escalation-Only Uncertainty Treatment and negative proof, reused unchanged; R3 Rule 3 |
| 12 | receipt invalidation cascades beyond the earliest affected scope and needlessly reopens unrelated evidence | preservation of every unaffected current sub-claim with explicit reason: `invalidationScope` is bounded to exactly the earliest affected node's own scope, per the Invalidation Precedence "earliest affected node controls" rule | the affected node's own scope is fully invalidated as required; everything outside that scope remains `CURRENT` with the explicit reason that no evidence at a lower precedence level was actually touched | Invalidation Precedence "earliest affected node controls" binding rule; R3 Rule 4 (evidence expires from the earliest affected node, not globally) |

## Zero-Edit R6 Candidate Manifest

The following paths and sections are named as exact candidate targets for a
future R6+ tranche only. None is edited, drafted, or scaffolded by this
design.

| Candidate path | Candidate change | Justifying evidence | Authorization state |
| --- | --- | --- | --- |
| a new `governance/compat/check_shadow_command_applicability.py` (candidate name only; file does not exist) | machine-check the `commandApplicability` value against the applicability matrix above for any governed artifact that asserts a `claimToken` with a populated `claimScopeRef` | R4 Invariant-To-Command Applicability Matrix section; False-Positive Boundary section | UNAUTHORIZED; R6+ must specify exact detection regexes and re-validate the false-positive boundary before any checker is drafted, exactly as R4's own R5 Candidate Manifest already flagged for this same candidate name |
| a new `governance/compat/check_shadow_receipt_invalidation.py` (candidate name only; file does not exist) | machine-check the Invalidation Precedence order and the Re-Earning Rule against any claim whose `invalidatedBy`/`eligibilityState` fields are populated | Invalidation Precedence section; Re-Earning Rule section | UNAUTHORIZED; R6+ must show this does not duplicate R3's Dependency Invalidation Graph's own matching logic, and must define exact node-identifier matching before any checker is drafted |
| `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md` | evaluate (not adopt) whether the Receipt Ownership Table's six fields should be added to the standard's own "Shadow Interface Reference" candidate section already named by R4's R5 Candidate Manifest | Receipt Ownership Table section; R4's own equivalent candidate row | UNAUTHORIZED; requires R6+ and independent review |
| `governance/compat/agent_autorun_command_catalog.py` | none proposed; this design explicitly binds to the catalog by reference only and adds zero rows | Current Owner Map section; Cost Proof "No Duplicate Discovery Or Replay" subsection | NOT_PROPOSED |
| any other `governance/compat/check_*.py` file | none proposed by this design | no field, token, or invariant in the applicability matrix identified a checker gap outside the two candidate rows above | NOT_PROPOSED |
| a new registry, receipt store, lifecycle standard, or second command catalog | none proposed | this design explicitly reuses the existing single canonical catalog and existing per-field/per-token owners with no second truth store, per the Acceptance Criteria and the Non-Applicable Families table above | NOT_PROPOSED |

No path above is edited by this worker. This table exists to satisfy the
work order's requirement for a zero-edit R6 candidate manifest, not to
pre-approve any future change.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - N/A with reason: this design
  reuses R3's Proof Floors, R4's field/token evidence, and the existing
  command catalog as committed evidence fixtures cited by reference; it
  performs no new corpus scan, registration, or enumeration, and creates or
  changes no corpus manifest, ledger, or completeness verdict of its own.

## Evidence / Verification

Before dispatch, both worker outputs were required to pass routing and
dispatch gates; the pre-implementation autorun gate and the TPGR shadow-route
checker (`COMPLIANT`, 0 violations) were both run as required preflight,
before any edit, at `executionBaseHead`. During execution, this design
records source sections, evidence labels, and the no-commit boundary
directly in its own tables above and in the paired worker return's Command
Evidence section. Reviewer acceptance of this evidence remains a separate,
independent step owned by the reviewer/closer.

## Risk / Corrective Action

Primary risk: a future R6+ implementation of `commandApplicability` could
quietly grow into a full second index mapping every claim to every command,
recreating exactly the "second command catalog" this design explicitly
rejects. Corrective action: any R6+ implementation must be reviewed against
this design's own constraint that `commandApplicability` is an annotation on
an existing claim record pointing at an existing catalog row, never an
independent index with its own query surface; a design that proposes a
standalone applicability database should be treated as a stop-condition-
adjacent change even if this design did not observe one.

Secondary risk: the False-Positive Boundary section is deliberately
non-executable (no regex or code, per the work order's instruction). A
future R6+ checker author could implement a boundary that is narrower or
broader than intended here, reproducing the exact "plausible prose then gate
failure" pattern the literal-format gotchas reference documents. Corrective
action: any R6+ checker draft must be reviewed against each of the six rows
in the False-Positive Boundary table with a concrete positive and negative
test case per row before the checker is considered complete, not merely
against the aggregate hostile-case table.

Tertiary risk: the Invalidation Precedence's six-level order is itself a new
design artifact (not a verbatim restatement of R3's Dependency Invalidation
Graph, though it is built entirely from R3/R4 material). A future reader
could mistake it for an existing R3 mechanism rather than this design's own
synthesis. Corrective action: this design's own Source / Predecessor
Evidence table and inline citations throughout the Invalidation Precedence
section already attribute each level to its specific R3/R4 origin; any
future implementation should preserve those citations rather than treating
the six-level list as freestanding.

## Hostile-Case Coverage Reconciliation

Twelve hostile cases required, twelve hostile cases resolved above, each to
exactly one of `FULL_LAYER_A_REQUIRED`, `ESCALATE_FOR_REVIEW`, or an
explicit-reason preservation of an unaffected current sub-claim. Zero cases
resolve to `LIGHT_ROUTE_ALLOWED`. Eight interface fields evaluated in the
applicability matrix, matching R4's eight-field table exactly. Eight claim
tokens evaluated, matching R4's eight-token vocabulary exactly. Six
documentation-only candidate fields evaluated in the Receipt Ownership
Table, matching the paired baseline's `docOnlyNewFields` list exactly. One
canonical command catalog cited throughout; zero new catalogs, stores,
lifecycles, or routers proposed anywhere in this design.

## Decision

`PROCEED_TO_R6_SHADOW_REPLAY_AND_MIGRATION_DESIGN`

## Final Disposition

`PROCEED_TO_R6_SHADOW_REPLAY_AND_MIGRATION_DESIGN`

Rationale: the R4 Invariant-To-Command Applicability Matrix cites every one
of R4's eight interface fields, eight claim tokens, and the no-promotion-by-
aggregation/corpus-semantic-proof/uncertainty-escalation/upstream-drift
cross-cutting invariants to the single existing canonical command catalog or
an existing standard/graph owner, with zero new catalogs, stores,
lifecycles, or routers proposed; the Receipt Ownership Table binds all six
documentation-only candidate fields to existing owners as annotations, never
as independent state; the six-level Invalidation Precedence resolves the
paired baseline's Stop Conditions on checker-semantics-versus-filename
stability (level 4) and catalog-row removal (level 5) explicitly; the
Re-Earning Rule closes the stale-receipt-revival surface with an explicit
negative proof mirroring R4's own worker-declaration exclusion; the
False-Positive Boundary names six concrete detection surfaces without
writing implementation code, as the work order requires; the Cost Proof
separates the unavoidable, unreduced always-on legacy bundle from an
explicitly `PROJECTED` and `UNKNOWN` future selective-value estimate, adding
zero duplicate command discovery; and all twelve required hostile cases
resolve to a named fail-closed route, with none silently selecting
`LIGHT_ROUTE_ALLOWED`. This satisfies the paired baseline's Design Contract
and Stop Conditions and the work order's Acceptance Criteria. The next
authorized step is R6 (shadow replay and migration design), which remains
unauthorized by this design and requires a fresh operator decision and
governed dispatch.

## Claim Boundary

This design is a documentation-only, non-implementation command-
applicability and receipt-invalidation design evidence artifact over
existing governed evidence. It does not implement any command, checker,
receipt field, or registry; does not modify any standard, checker, registry,
catalog, hook, or router; does not intake or register any new source corpus;
does not authorize selective execution (`selectiveExecutionAuthorized`
remains `false` per the TPGR standard, independently verified at this
executionBaseHead); and does not open R6-R9, T15, or any runtime,
provider/live, public-sync, deployment, or production action. The
`PROCEED_TO_R6_SHADOW_REPLAY_AND_MIGRATION_DESIGN` disposition authorizes
only a future operator decision to open R6 under a fresh governed dispatch;
it does not itself authorize R6 work.
