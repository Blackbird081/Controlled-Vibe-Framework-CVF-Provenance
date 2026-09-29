# CVF TPGR-TV1 Tranche Value Admission Design

Memory class: governed-planning-assessment

docType: baseline

Status: COMPLETE_PENDING_REVIEW

Batch ID: TPGR-TV1

Date: 2026-08-26

executionBaseHead: `da1596bb400c6aaca3216bbd17cfcc34a9e4a4af`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Responds to work order:
`docs/work_orders/CVF_AGENT_WORK_ORDER_TPGR_TV1_TRANCHE_VALUE_ADMISSION_DESIGN_2026-08-26.md`

## Purpose

Define an additive, deterministic tranche admission and continuation value
contract for the existing TPGR standard. Decide field ownership across TPGR,
the work-order template, the review-cost standard, the router shadow output,
and the checker layer; specify a four-way decision algorithm; separate
remediation, external absorption, and app/project applicability; enumerate
hostile and boundary cases; and design a shadow-only rollout with an optional,
minimal TV2 manifest. This design implements no control and authorizes no
execution.

## Source / Predecessor Evidence

| Source | Identity | Authority use |
| --- | --- | --- |
| paired TV1 work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_TPGR_TV1_TRANCHE_VALUE_ADMISSION_DESIGN_2026-08-26.md` | worker contract, roadmap caps, write ownership |
| TPGR routing standard | `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md`; SHA-256 `f3884d43a91a9360f4166a564c29b32723578f713fd13e695ea43df2769f1d68` | existing owner for classification, profiles, escalation, T0 legacy interlock |
| Review Cost And Diminishing Return standard | `docs/reference/review_cost_control/CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md`; SHA-256 `32f4fe302a2a3d1f1f86ecff9e8d6520a6976c6e6c4b4c1b4fe02b5d9601a459` | existing owner for post-hoc review telemetry, stop-disposition vocabulary |
| accepted EAFR-R11 worker return | `docs/reviews/CVF_EAFR_R11_FINAL_RECONCILIATION_TRANCHE_VALUE_AND_RFR_DECISION_WORKER_RETURN_2026-08-26.md`; SHA-256 `f168fd21a849eb0408f4bd226cb48fcd9838d52c0e1a1bd9341c43df8d883715`; reviewer-accepted disposition `REVIEWER_ACCEPTED_CLOSED_BLOCKED_CONSOLIDATED_REPAIR_REQUIRED` | origin of the tranche-value learning recommendation and its evidence-shape proposal |
| accepted TPGR-R8 assessment | `docs/assessments/CVF_TPGR_R8_P0_P1_ALLOWLIST_DECISION_DESIGN_2026-08-23.md`; SHA-256 `4392429c04b0434740b315402b37b1109564e9ad3d614c571fc7a68c0547bcc3`; final disposition `HOLD_EMPTY_P0_ALLOWLIST_PENDING_OBSERVED_DUAL_RUN_EVIDENCE` | current TPGR-R8 hold state; interlock this design must preserve unchanged |
| RFR final reconciliation and roadmap closure | `docs/reviews/CVF_RFR_FINAL_RECONCILIATION_AND_ROADMAP_CLOSURE_2026-08-26.md`; SHA-256 `c5a0a70fda0ef08e887a357c3e38babd00c511cf7ab011adccd77b9cb4ec9f1d`; verdict `CLOSED_PASS_BOUNDED` | independent confirmation of the same routing gap from a second closed roadmap, corroborating R11's recommendation |
| canonical machine surfaces | `governance/compat/CVF_TASK_GOVERNANCE_ROUTE_REGISTRY.json`; `governance/compat/CVF_TASK_GOVERNANCE_ROUTE_MANIFEST.schema.json`; `governance/compat/route_task_governance.py`; `governance/compat/check_task_governance_route.py` | current TPGR machine owner set that any TV1 field addition must extend, not compete with |

## Scope / Methodology

Read the paired TV1 work order in full, the TPGR standard, the review-cost
standard, the accepted EAFR-R11 worker return's Tranche Admission And
Continuation Value Learning section, the accepted TPGR-R8 assessment, the
RFR final reconciliation review, the guard orientation index, the literal
format gotchas reference, and applicable checker sources
(`check_work_order_dispatch_quality.py`,
`check_dispatch_prompt_envelope.py`, `check_worker_return_quality_gate.py`,
`check_governed_artifact_checker_read_ahead.py`,
`check_task_governance_route.py`, `check_agent_operation_trace.py`,
`check_markdown_structural_completeness.py`). Recomputed all five pinned
input hashes at execution head; all matched exactly, zero drift. This
assessment proposes field ownership and a decision algorithm without editing
any existing standard, template, checker, router, or state file. Both
described outputs (this assessment and its paired worker return) are the
only files created; nothing was staged or committed.

## Findings / Position

### Owner And Field Placement

The tranche-value contract is one additive record family owned by the TPGR
standard, projected into four consumer surfaces rather than duplicated as
separate prose in each:

| Field group | Canonical owner | Projected into | Owner-edge rationale |
| --- | --- | --- | --- |
| eight TPGR classification dimensions (existing) | TPGR standard, unchanged | work-order manifest JSON (existing), router, checker | already owned; TV1 adds no new classification dimension |
| tranche-value record (new): outcome/consumer, severity, finding evidence state, root-cause identity, marginal value and its evidence state, cost/latency/quota envelope, consolidation key, stop condition, authority-sourced successor-cap reference and ordinal, decision reason, reviewer identity, freshness, override/appeal authority evidence | TPGR standard, new `## Tranche Admission And Continuation Value` section | work-order template (a documentary section reusing the record shape, not a new schema); existing route-manifest schema; router shadow output (an explanatory field only, per the existing Bundle Contract pattern); existing route checker (a future optional shape/read-ahead check only, not implemented here) | one record avoids the ten-tranche pattern the EAFR-R11 return observed, where every baseline hand-wrote its own Serious-Finding Gate and Successor Cap prose; TPGR is the correct owner because it already owns pre-dispatch classification and the T0 shadow-receipt pattern this record extends |
| four-way decision token (`CONTINUE_HIGH_VALUE`, `CONSOLIDATE`, `PARK_LOW_VALUE`, `STOP_NO_INCREMENTAL_VALUE`) | TPGR standard | work-order template (documentary decision field); router shadow output (explanatory `valueDisposition` field, non-authoritative) | distinct vocabulary from the Review Cost standard's five-token `stopDisposition` (`CONTINUE_NEW_CRITICAL_EVIDENCE`, `CONSOLIDATE_SINGLE_REPAIR`, `PARK_LOW_INCREMENTAL_VALUE`, `COMPLETE_REVIEW`, `REVIEW_COST_ESCALATION_REQUIRED`); no merge is proposed because the two vocabularies answer different questions at different times (see Applicability Separation and the cross-standard boundary below) |
| evidence-state vocabulary (`OBSERVED`, `HISTORICAL_BOUNDED`, `PROJECTED`, `UNKNOWN`) | TPGR standard, applied separately to finding evidence, marginal-value evidence, and each cost sub-field; not the Review Cost standard's existing per-round integer telemetry | none beyond TPGR; Review Cost's `valueDelta` free-text field remains its own, separate, post-hoc field | avoids inventing a second vocabulary while preventing a strong finding from being mistaken for strong economics, or vice versa; TPGR-R8 already established this exact four-token set in its Cost And Value table |

No parallel governance framework is created. Every field above is either an
extension of the existing TPGR manifest shape or a documentary projection of
it; no field is invented that duplicates a Review Cost standard field. The
review-cost standard remains the sole owner of post-hoc review telemetry
(`reviewRoundCount`, `stopDisposition`, `avoidableDelayClass`, and the rest);
TV1 does not touch that file or its checker.

**Cross-standard boundary (why two decision vocabularies do not merge):**
TPGR's four-way token answers "should this tranche be dispatched or
continued at all," decided once per tranche before or during work. Review
Cost's five-way `stopDisposition` answers "should this review round stop
repairing," decided repeatedly inside an already-open `completion_review`
artifact. EAFR-R11 through R7-R10 show both questions were answered by hand
in every baseline; TPGR-TV1 only closes the pre-dispatch half. A tranche
that TPGR marks `CONTINUE_HIGH_VALUE` still produces a review that
separately runs the existing Review Cost telemetry once it reaches
`completion_review` shape; the two contracts compose sequentially, they do
not overlap.

### Admission Schema

All fields below are additive to the TPGR manifest; none replaces an
existing TPGR field. Types are documentary (Markdown table shape), matching
the existing TPGR/Review-Cost pattern of Field/Value or Field/Shape tables;
no JSON schema file is created by this design.

| Field | Type | Required | Default | Invalid states |
| --- | --- | --- | --- | --- |
| `outcomeConsumer` | free text naming the concrete downstream consumer of this tranche's output | required | none; missing value is invalid | empty, generic ("future work"), or a consumer with no named owner surface |
| `severity` | enum: `P0`, `P1`, `P2`, `P3`, `NONE` | required | none | a numeric severity outside this enum; a severity inferred from tranche count rather than evidence |
| `findingEvidenceState` | enum: `OBSERVED`, `HISTORICAL_BOUNDED`, `PROJECTED`, `UNKNOWN` | required | `UNKNOWN` when not asserted | any token outside the four-value enum; silently defaulting to `OBSERVED`; using economic evidence to label a finding observed |
| `rootCauseIdentity` | object with `relation` enum (`INDEPENDENT`, `DEPENDENT`, `DUPLICATE`, `UNKNOWN`), causal-invariant identity, owner surface, and evidence references; a first finding uses `INDEPENDENT` with its own source evidence | required | `UNKNOWN`, which cannot authorize continuation | a boolean; title-only or path-only identity; `INDEPENDENT` without evidence; `DEPENDENT`/`DUPLICATE` without a prior-record reference |
| `marginalValue` | free text stating the specific incremental value of the next tranche over stopping now | required | none; a missing value defaults the decision to `PARK_LOW_VALUE` per the Decision Algorithm | a bare number with no evidence-state label; a value that restates the finding instead of the marginal delta |
| `valueEvidenceState` | enum: `OBSERVED`, `HISTORICAL_BOUNDED`, `PROJECTED`, `UNKNOWN`, applied only to `marginalValue` | required | `UNKNOWN` | any token outside the four-value enum; copying `findingEvidenceState` without separate value evidence |
| `costEnvelope` | six sub-fields: `workerTime`, `reviewerTime`, `latency`, `tokenOrQuotaUsage`, `providerCallCost`, `opportunityCost`, each an evidence-state-labeled value (a concrete measure paired with `OBSERVED`/`HISTORICAL_BOUNDED`/`PROJECTED`, or the bare token `UNKNOWN`) | required, one row per sub-field | `UNKNOWN` per unmeasured sub-field | any sub-field presented as a bare number without an evidence-state label; `UNKNOWN` rendered as `0` |
| `consolidationKey` | free text or structured identity that groups this finding with any other finding sharing the same independent root cause | required | none | a consolidation key that matches an already-`STOP`-disposed or already-`CONSOLIDATE`-absorbed finding without citing that prior record (see Hostile Case 1/2/9) |
| `stopCondition` | free text naming the exact condition under which this tranche family stops accepting successors | required | `"no further successor after successor cap is reached"` when not otherwise specified | a stop condition that can never be met (unfalsifiable) |
| `successorAuthority` | object containing immutable roadmap/work-order authority reference, declared cap, and current successor ordinal; the values are read from that authority and are not selected by the candidate record | required | none; missing authority is invalid | caller-selected cap; ordinal not reconcilable to committed predecessors; cap increase without a fresh independently authorized roadmap |
| `decisionReason` | free text explaining why the four-way decision token below was selected, citing the specific field values that drove it | required | none | a decision reason that does not reference `severity`, `findingEvidenceState`, `valueEvidenceState`, or `marginalValue` |
| `reviewerIdentity` | role, artifact path, and immutable hash of the independent reviewer who confirmed the final record | required for every authoritative disposition; `NOT_YET_REVIEWED` means the result is shadow/candidate only | `NOT_YET_REVIEWED` | a reviewer identity with no artifact path or hash; treating an unreviewed decision as authority |
| `freshness` | captured-at time plus explicit expiry time (or `NO_EXPIRY_WITH_REASON`) | required | none | a record with no captured-at time; an expiry that has already passed and is still cited as current |
| `overrideAppealEvidence` | `NONE`, or an immutable governed operator-authority reference with operator identity, bounded scope, reason, capture/expiry, original computed token, and independent-review reference | required (may be `NONE`) | `NONE` | free-text identity alone; unbounded or expired authority; overwriting the computed token; override used to lower a risk floor or bypass a guard |

### Decision Algorithm

The algorithm returns exactly one of four tokens. Risk classification (the
existing TPGR eight-dimension manifest and its `P0_OBSERVE`-through-
`P4_CRITICAL` profile floor) is evaluated first and is never lowered by any
value field below. Value fields only ever narrow the decision toward
stopping, parking, or consolidating work; they never relax, skip, reorder,
or shorten the governance floor the risk classification already selected.

Pseudocode (documentary; no implementation is created by this design):

```text
function decideTrancheValue(record, committedAuthority):
    # Step 1: risk floor is fixed first and is immutable by this function.
    riskProfile = existingTpgrRouter.classify(record.classificationManifest)
    # riskProfile is P0_OBSERVE..P4_CRITICAL; this value is read-only here.

    # Step 2: validate the record and its immutable authority inputs.
    if any required field is missing or malformed:
        return PARK_LOW_VALUE   # incomplete candidate; never execution authority
    if record.successorAuthority does not match committedAuthority:
        return PARK_LOW_VALUE   # caller cannot select or raise its own cap
    if record.rootCauseIdentity.relation in (DEPENDENT, DUPLICATE) and
       its prior-record reference is valid and no new independent evidence exists:
        return STOP_NO_INCREMENTAL_VALUE   # see Hostile Case 2/9

    # Step 3: cap exhaustion blocks this roadmap, but does not mislabel a
    # source-backed serious finding as having no incremental value.
    if record.successorAuthority.currentOrdinal exceeds committedAuthority.cap:
        if record.severity in (P0, P1) and record.findingEvidenceState in
           (OBSERVED, HISTORICAL_BOUNDED):
            return CONSOLIDATE   # no execution here; new roadmap decision required
        return STOP_NO_INCREMENTAL_VALUE

    # Step 4: serious risk requires bounded handling, while high-value
    # continuation additionally requires independent value evidence.
    if record.severity in (P0, P1):
        if record.findingEvidenceState not in (OBSERVED, HISTORICAL_BOUNDED):
            return PARK_LOW_VALUE   # allegation not yet source-backed
        if record.rootCauseIdentity.relation == INDEPENDENT and
           record.valueEvidenceState in (OBSERVED, HISTORICAL_BOUNDED):
            return CONTINUE_HIGH_VALUE
        return CONSOLIDATE       # one bounded repair; economics may remain unknown

    # Step 5: P2/P3/NONE severity is value-led.
    if record.severity in (P2, P3, NONE):
        if record.rootCauseIdentity.relation == INDEPENDENT and
           record.marginalValue is well-evidenced and record.valueEvidenceState
           in (OBSERVED, HISTORICAL_BOUNDED):
            return CONTINUE_HIGH_VALUE
        if record.marginalValue exists and record.valueEvidenceState == PROJECTED:
            return PARK_LOW_VALUE   # projected value never authorizes CONTINUE
        return PARK_LOW_VALUE

    # Step 6: all other unknown/invalid states remain non-authoritative.
    return PARK_LOW_VALUE  # exhaustive fallback; never silently CONTINUE
```

The algorithm is deterministic for a fixed record plus committed authority.
It deliberately separates finding evidence from economic evidence: a
source-backed P0/P1 with unknown economics returns `CONSOLIDATE`, matching
EAFR-R11's rule that it cannot be parked for cost; an unverified P0/P1
allegation returns `PARK_LOW_VALUE` pending source proof and is not treated as
an established repair obligation. `CONTINUE_HIGH_VALUE` requires both an
independent root cause and observed or historical-bounded marginal value.
Unknown value on P2/P3/NONE never authorizes continuation. Every returned
token remains shadow-only until `reviewerIdentity` is complete.

### Applicability Separation

| Dimension | Remediation / finding repair (primary initial scope) | External repository absorption | App / project delivery slices |
| --- | --- | --- | --- |
| Common invariant | risk floor is set first and is never relaxed by value; unknown value never authorizes continuation; a successor cap bounds the chain | same | same |
| Outcome/consumer | a specific fail-closed control, guard, or governance record | a specific CVF owner surface (doctrine, package, runtime, or checker) that absorbs external value | a specific user-facing capability or vertical slice |
| Independent root cause | a distinct defect/finding, as in the EAFR R1-R11 chain | a distinct external source item or cluster, as already scoped by TPGR's Absorption Cost Rule | a distinct backlog item or slice, not yet TPGR-governed |
| Marginal value evidence source | reviewer-confirmed source re-inspection, as EAFR-R11 performed against current runtime files | the existing absorption disposition ledger (`absorb`/`adapt`/`defer`/`reject`) already required by the guard-orientation task-class row for external source intake | user/business outcome evidence, not yet defined by any current CVF owner |
| Existing TPGR/Review-Cost coverage today | none pre-dispatch (the exact gap EAFR-R11 and this RFR closure both independently found) | partial: TPGR's Absorption Cost Rule already governs corpus scale and full-read proof, but not continuation value after intake | none; project delivery is presently ungoverned by TPGR or Review Cost |
| TV1 disposition | **in scope**: this design's schema and algorithm are written and validated against this class first | **out of scope for TV1**: named here only as a future consumer; no field, checker, or roadmap tranche is authorized for it by this design | **out of scope for TV1**: named here only as a future consumer; same boundary |
| Named future consumer and required evidence before extending | n/a (already the TV1 scope) | a future TV2/TV3 candidate would need: at least one closed absorption roadmap producing an absorption disposition ledger, reviewer confirmation that the ledger's `defer`/`reject`/`no_new_value` groups were value-audited (per guard-orientation's known absorption-audit failure pattern), and independent evidence that the four-way token adds value beyond the existing ledger disposition | a future TV2/TV3 candidate would need: a CVF-governed project-delivery roadmap or work-order class that does not yet exist, a defined "user outcome" evidence field, and independent predecessor acceptance before this design's schema is reused there |

These three classes are explicitly not three implementation tranches. TV1
designs the shared schema and algorithm once, proves it against the
remediation class where EAFR-R11 supplied concrete before/after evidence, and
leaves the other two classes as named future consumers pending their own
independent predecessor acceptance, per the work order's Roadmap-To-Work-
Order Trace Matrix and the roadmap's TV1-TV3 cap.

### Hostile And Boundary Cases

| # | Case | Expected decision | Governance floor | Evidence preserved | Re-entry / appeal rule |
| --- | --- | --- | --- | --- | --- |
| 1 | Duplicate root cause: a new record proves the same causal invariant and owner surface as a prior disposed record | `STOP_NO_INCREMENTAL_VALUE` | unchanged; no P0/P1 finding is silently dropped, only the duplicate admission is stopped | both records preserved verbatim; `rootCauseIdentity.relation` is `DUPLICATE` with the immutable prior-record reference | re-entry requires new source-backed evidence proving an independent causal mechanism, plus independent review |
| 2 | Renamed duplicate: the same causal mechanism reappears under a different `outcomeConsumer`, title, or source path | `STOP_NO_INCREMENTAL_VALUE` | unchanged | both records preserved; identity reconciles owner, violated invariant, causal mechanism, and evidence references rather than relying on title or file location alone | same as Case 1; neither title similarity nor source-location identity alone decides admission |
| 3 | No consumer: `outcomeConsumer` is missing or generic ("future work", "TBD") | `PARK_LOW_VALUE` by the explicit Step 2 schema-validation branch | unchanged | the incomplete record is preserved with the missing field flagged | re-entry requires a concrete named consumer before the record is re-evaluated |
| 4 | Documentation-only churn: the tranche would only reformat or reword existing accepted evidence with no new finding | `STOP_NO_INCREMENTAL_VALUE` | unchanged | the churn proposal is preserved as a record so a future agent does not re-propose the same non-finding | re-entry requires a genuine new finding, not a rewording of the same accepted evidence |
| 5 | Projected savings presented as the sole marginal-value justification, with no `OBSERVED`/`HISTORICAL_BOUNDED` evidence | `PARK_LOW_VALUE` if severity is P2/P3/NONE, `CONSOLIDATE` if severity is P0/P1 (never `CONTINUE_HIGH_VALUE` on projected-only value, per Decision Algorithm Step 4/5) | unchanged | the projected estimate is preserved labeled `PROJECTED`, never promoted to `OBSERVED` | re-entry requires observed or historical-bounded evidence superseding the projection |
| 6 | Unknown quota/cost envelope on an otherwise well-evidenced P2 finding | `PARK_LOW_VALUE`; unknown cost never blocks parking, only blocks continuation | unchanged | the record is preserved with `costEnvelope` sub-fields explicitly `UNKNOWN`, never defaulted to zero | re-entry requires at least the `workerTime`/`reviewerTime` sub-fields resolved to a concrete evidence-stated value |
| 7 | Serious, source-backed P0/P1 finding with unknown economics (cost/latency/quota and `valueEvidenceState` all `UNKNOWN`) | `CONSOLIDATE` (Decision Algorithm Step 4); a proved P0/P1 is never parked or stopped for unknown cost alone | unchanged; full governance floor applies to one bounded repair | finding proof and unknown economic fields are preserved separately; the consolidated repair must measure cost when feasible | the consolidation decision requires independent review; execution still needs its own authorized bounded successor |
| 8 | Successor-cap exhaustion: a fourth successor is proposed after three tranches and the cap is read from committed roadmap authority | `CONSOLIDATE` for a source-backed P0/P1 with reason `CAP_EXHAUSTED_NEW_ROADMAP_REQUIRED`, otherwise `STOP_NO_INCREMENTAL_VALUE` | unchanged; no fourth tranche executes and a serious finding is not falsely labeled valueless | all prior records and the proposal are preserved; the proposal records committed cap authority and `CAP_EXHAUSTED` | re-entry requires a fresh, independently authorized roadmap with its own cap; the candidate record cannot raise the exhausted cap |
| 9 | Conflicting value evidence: two reviewers disagree on `valueEvidenceState` or `marginalValue` for the same record | `CONSOLIDATE` if a source-backed P0/P1 finding is independently established, else `PARK_LOW_VALUE` pending reconciliation; conflicting evidence is never silently resolved by picking the more favorable label | unchanged | both conflicting assessments are preserved verbatim, side by side, per the same pattern TPGR-R8's Hostile Case H-A7 uses for contradictory comparator state | re-entry requires explicit source-authority reconciliation between the two assessments plus one fresh independent review |
| 10 | Stale decision: a record's `freshness.expiresAt` has passed, or `freshness` is missing/malformed | `PARK_LOW_VALUE`; the expired record is invalid for authority and its finding/value evidence is not silently relabeled | unchanged | the expired record is preserved labeled expired, not deleted | re-entry requires source re-verification, a fresh capture, and independent review; timestamp-only renewal is forbidden |
| 11 | Scope widening: a tranche proposes to extend its `outcomeConsumer` or `consolidationKey` beyond what the originating roadmap authorized | `STOP_NO_INCREMENTAL_VALUE` for the widened portion; the originally authorized scope is unaffected and evaluated on its own record | unchanged; widened scope is treated the same as TPGR-R8's Hostile Case H-A5 (widened task/path scope selects `P1_FULL_LEGACY_REQUIRED`) | both the original and widened manifests are preserved | re-entry requires a fresh dispatch and full proof for the exact widened identity, not an amendment to the original record |
| 12 | Operator override: an operator seeks `CONTINUE_HIGH_VALUE` despite a computed park/stop token | the computed token remains unchanged; an override becomes authoritative only through an immutable governed authority reference with bounded scope/expiry and independent-review confirmation | unchanged; an override cannot lower a risk floor, waive a guard, raise an exhausted cap, or authorize selective execution | original token, operator authority, reason, scope, expiry, and reviewer confirmation are preserved side by side | re-entry occurs only after the governed override and independent review are valid; operator identity as free text is insufficient |

Hostile/boundary coverage: 12/12 designed cases fail safe (no case authorizes
governance-floor reduction, silent duplication, self-selected cap authority,
or an unbounded successor chain).

### Cost And Evidence Semantics

Only `OBSERVED`, `HISTORICAL_BOUNDED`, `PROJECTED`, and `UNKNOWN` are used,
reusing the exact vocabulary TPGR-R8's Cost And Value table already
established. `costEnvelope` separates six sub-fields, each independently
evidence-stated: `workerTime`, `reviewerTime`, `latency`,
`tokenOrQuotaUsage`, `providerCallCost`, `opportunityCost`. Missing
telemetry for any sub-field is recorded as the bare token `UNKNOWN`; it is
never rendered as `0`, never averaged with observed sub-fields, and never
summed into a total that would make an unknown component look like zero
cost. `providerCallCost` and `opportunityCost` are UNKNOWN by design for
every TV1-scope remediation record in this design's worked examples, because
no provider/live/network measurement is authorized by this design or its
paired work order.

### Rollout, Rollback, And TV2 Manifest

**Rollout (shadow-only):** the tranche-value record and four-way decision
are documentary fields added to a future TPGR standard revision and
projected into the work-order template as an optional new section. The full
legacy gate bundle continues to run unchanged, exactly as TPGR-T0 already
mandates (`selectiveExecutionAuthorized: false`,
`legacyGateDisposition: RUN_FULL_LEGACY_BUNDLE`). No router, checker, or hook
behavior changes at TV1; the router shadow output only gains an explanatory
field, following the existing Bundle Contract's "every omitted bundle
carries a machine reason" pattern.

**Rollback:** because TV1 itself edits no standard, template, checker,
router, or state file, there is no TV1 rollback surface; rollback applies
only to a future TV2 shadow implementation, which would be reverted by
removing the added optional section/field from the standard and template and
retaining the legacy full gate, mirroring the TPGR standard's own existing
Rollback section pattern ("remove the TPGR checker from command catalogs and
retain the legacy full gate... never roll back by accepting an invalid
manifest or by silently authorizing selective execution").

**Optional TV2 manifest (named, not created or authorized here):**

| Candidate surface | Purpose | Test requirement | Rollback |
| --- | --- | --- | --- |
| `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md` (a future revision) | add the `## Tranche Admission And Continuation Value` section documented above as an optional, additive section | none at TV1; a TV2 tranche would need focused review confirming the section does not alter any existing classification, profile, or escalation rule | revert the added section; retain the standard's current content unchanged |
| `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` (a future revision) | add an optional tranche-value section mirroring the TPGR record shape, for dispatchers who choose to declare it | none at TV1; a TV2 tranche would need confirmation that omitting the section remains valid for work orders that do not use it | revert the added section |
| `governance/compat/CVF_TASK_GOVERNANCE_ROUTE_MANIFEST.schema.json` and existing `route_task_governance.py` | add one optional closed-shape record and emit an explanatory, non-authoritative `valueDispositionExplanation`; no competing schema or decision owner | extend existing schema/router tests with valid, missing-field, invalid-enum, authority-cap, and explanatory-output cases | remove the optional record and explanatory output; existing manifest behavior remains unchanged |
| existing `check_task_governance_route.py` | validate a declared optional record through the existing TPGR checker; omitted records remain valid | extend `test_check_task_governance_route.py` for declared/omitted/invalid record shapes and confirmation that selective execution remains false | remove only the optional-record validation branch; do not add or delete a parallel checker |

This manifest is named for future reference only. TV1 authorizes none of
these four owner-aligned rows; each requires its own independently reviewed TV2 work
order and predecessor acceptance of this TV1 design, per the roadmap's
TV1-TV3 cap and the "TV2/TV3 only after independent review and demonstrated
value" boundary already fixed by the roadmap and this work order's
Dependency Release Evidence table (`TV2/TV3 | roadmap successor cap |
independent predecessor acceptance required | NOT_AUTHORIZED`).

**TPGR-R8 P0 hold interlock:** this design does not touch, reference as
authority, or in any way loosen the TPGR-R8 `HOLD_EMPTY_P0_ALLOWLIST_
PENDING_OBSERVED_DUAL_RUN_EVIDENCE` disposition. TPGR-R8's P0/P1 allowlist
question (whether a specific C1-C6 identity may skip to a lighter execution
route) is orthogonal to TV1's question (whether a tranche should be
dispatched or continued at all). A future `CONTINUE_HIGH_VALUE` disposition
under this design never converts into TPGR-R8 `P0_CANDIDATE_ONLY`
eligibility, and TPGR-R8's fail-closed six-of-six `P1_FULL_LEGACY_REQUIRED`
result remains completely unchanged by this design.

## Evidence / Verification

| Threshold | Result |
| --- | --- |
| 100% field ownership and decision paths deterministic | PASS: every field in the Admission Schema names exactly one canonical owner (TPGR) and its projection surfaces; the Decision Algorithm is a total function over the schema with an exhaustive fallback (`PARK_LOW_VALUE`) so no input reaches an undefined branch |
| four and only four decisions | PASS: `CONTINUE_HIGH_VALUE`, `CONSOLIDATE`, `PARK_LOW_VALUE`, `STOP_NO_INCREMENTAL_VALUE`; the algorithm returns no fifth token |
| at least 12/12 hostile cases fail safe | PASS: 12/12 designed in the Hostile And Boundary Cases table, each with an expected decision, preserved governance floor, preserved evidence, and re-entry rule |
| 100% risk-floor preservation | PASS: Decision Algorithm Step 1 reads the existing TPGR risk classification read-only and no later step lowers it; every hostile case's "Governance floor" column states "unchanged" |
| explicit remediation/absorption/project separation | PASS: Applicability Separation table names the common invariant and per-class differences, with absorption and project delivery marked out of TV1 scope and given named future-consumer requirements |
| one canonical record; no competing governance owner | PASS: Owner And Field Placement table routes every field to the existing TPGR standard, with explicit non-merge rationale against the Review Cost standard's separate `stopDisposition` vocabulary |
| maximum roadmap successor count remains three with no TV4 | PASS: Hostile Case 8 reads the cap from committed authority and authorizes no fourth tranche; a source-backed serious finding is consolidated into a new-roadmap decision rather than falsely labeled valueless |
| projected/unknown cost never represented as observed savings | PASS: Cost And Evidence Semantics section states unknown telemetry is never rendered as zero, and Hostile Case 5 forces `PARK_LOW_VALUE`/`CONSOLIDATE`, never `CONTINUE_HIGH_VALUE`, on projected-only value |
| TV2 manifest is minimal, shadow-only, and optional | PASS: four named candidate rows, each additive/optional, each requiring its own independent review; none created or authorized here |
| exact two outputs, unchanged HEAD, empty staging, no external effect | PASS: this assessment and its paired worker return are the only two files created; verified via `git status --short --untracked-files=all` and `git diff --cached --name-only` in the paired worker return's Command Evidence |
| exactly one allowed final disposition | PASS: see Decision below |

## Risk / Corrective Action

The primary risk in this design was letting the four-way value decision
implicitly weaken the existing TPGR risk floor, for example by allowing a
low-marginal-value P0/P1 to be parked for cost. Corrective action: Decision
Algorithm Step 1 fixes the risk profile before any value field is read, and
Step 4 forces `CONSOLIDATE` rather than cost-driven parking whenever a P0/P1
finding is source-backed but its economics are unknown. An unverified
allegation remains parked pending finding evidence, so severity text alone
does not manufacture a repair obligation. A second risk was inventing a competing decision
vocabulary that duplicates the Review Cost standard's `stopDisposition`;
corrective action was the explicit Cross-Standard Boundary subsection
distinguishing pre-dispatch admission (TPGR-TV1's question) from in-review
stop control (the existing Review Cost standard's question), so the two
never need to be reconciled into one token set. A third risk was silently
letting a duplicate or renamed finding re-enter through a new
`outcomeConsumer` label; corrective action was defining root-cause identity
through owner, violated invariant, causal mechanism, and evidence references,
not title or source-path identity alone. Reviewer repair also binds caps and
overrides to immutable governed authority and extends only the existing TPGR
schema/router/checker owner set.

## Decision

`DESIGN_COMPLETE_PROCEED_TO_TV2_SHADOW_IMPLEMENTATION`

## Final Disposition

`PROCEED_TO_TV2_SHADOW_IMPLEMENTATION`

Rationale: the owner map is complete with no competing governance surface;
the four-way decision algorithm is deterministic and risk-floor-preserving
in every one of 12 designed hostile cases; the remediation/absorption/
project applicability split is explicit with absorption and project
delivery correctly held out of TV1 scope; the optional TV2 manifest is
minimal (four named surfaces, each additive and independently testable) and
strictly shadow-only, preserving `RUN_FULL_LEGACY_BUNDLE` and the TPGR-R8 P0
hold unchanged. This disposition recommends, but does not authorize, a
future independently reviewed TV2 shadow-implementation work order; per this
work order's Operator Checkpoint section, TV2/TV3, implementation, and any
owner-surface edit require a fresh post-review operator decision, which this
design does not grant.

## Claim Boundary

This is a documentation-only tranche-value admission design. It creates no
standard revision, template revision, checker, router change, registry,
schema file, hook, CI wiring, or runtime plan. It edits no existing TPGR
standard, work-order template, review-cost standard, router, or checker
file. It authorizes no TV2/TV3 implementation, no TPGR-R9, no selective
execution, no change to the TPGR-R8 P0 hold, and no provider/network/live,
public-sync, deployment, or destructive effect. The `PROCEED_TO_TV2_SHADOW_
IMPLEMENTATION` disposition is a worker recommendation only; it is not
implementation authority and does not itself dispatch, authorize, or
schedule any successor tranche.
