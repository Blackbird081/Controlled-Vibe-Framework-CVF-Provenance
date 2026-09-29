# CVF TPGR-R7 Dual-Run Canary And Rollback Rehearsal Design

Memory class: governed-planning-assessment

docType: baseline

Status: COMPLETE_PENDING_REVIEW

Batch ID: TPGR-R7

Date: 2026-08-18

executionBaseHead: `d7b7157802deaf4e74044f13dd52682292bcfe92`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Responds to work order:
`docs/work_orders/CVF_AGENT_WORK_ORDER_TPGR_R7_DUAL_RUN_CANARY_AND_ROLLBACK_REHEARSAL_DESIGN_2026-08-18.md`

Paired baseline authority:
`docs/baselines/CVF_GC018_TPGR_R7_DUAL_RUN_CANARY_AND_ROLLBACK_REHEARSAL_DESIGN_2026-08-18.md`

## Purpose

Design, without executing, a strictly advisory dual-run comparison between
TPGR's proposed shadow routing and the existing phase-appropriate legacy gate
outcome, plus a paper (design-only) two-tier rollback rehearsal. This tranche
performs no canary execution, no selective command plan, and changes no
authority. TPGR remains advisory-only: it can never suppress, skip, reorder,
or shorten a legacy command, and the legacy gate bundle is always the
controlling outcome.

## Source / Predecessor Evidence

| Source | Identity | Authority use |
| --- | --- | --- |
| paired baseline | `docs/baselines/CVF_GC018_TPGR_R7_DUAL_RUN_CANARY_AND_ROLLBACK_REHEARSAL_DESIGN_2026-08-18.md` | complete execution authority for this design |
| paired work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_TPGR_R7_DUAL_RUN_CANARY_AND_ROLLBACK_REHEARSAL_DESIGN_2026-08-18.md` | task manifest, Design Contract, Required Canary Design Cases, Required Mismatch Classes, Acceptance Thresholds |
| R3 assessment | `docs/assessments/CVF_TPGR_R3_ARCHETYPE_THRESHOLD_PROOF_DIVERGENCE_AND_ROLLBACK_FLOOR_DESIGN_2026-08-18.md` | Route Outcomes And Deterministic Precedence, Threshold Precedence Rules, Anti-Self-Downgrade Invariants, A1-A6 Threshold Worksheets, Rollback Triggers And Restored Safe Route, Dependency Invalidation Graph |
| R5 assessment | `docs/assessments/CVF_TPGR_R5_SHADOW_COMMAND_APPLICABILITY_AND_RECEIPT_INVALIDATION_DESIGN_2026-08-18.md` | Receipt Ownership Table, Identity-Binding Contract, Invalidation Precedence, Re-Earning Rule, False-Positive Boundary |
| R6 assessment | `docs/assessments/CVF_TPGR_R6_HISTORICAL_SEEDED_DEFECT_SHADOW_REPLAY_AND_MIGRATION_DESIGN_2026-08-18.md` | H1-H6 Replay Worksheets (H3's disclosed strict-route divergence), Seeded-Defect Matrix, False-Positive Replay Matrix, Migration Table, Cost Accounting, Zero-Edit R7 Candidate Manifest, Final Disposition `PROCEED_TO_R7_DUAL_RUN_CANARY_AND_ROLLBACK_REHEARSAL_DESIGN` |
| R6 worker return | `docs/reviews/CVF_TPGR_R6_HISTORICAL_SEEDED_DEFECT_SHADOW_REPLAY_AND_MIGRATION_DESIGN_WORKER_RETURN_2026-08-18.md` | Independent Reviewer Addendum: H3 repaired from `LIGHT_ROUTE_ALLOWED` to `ESCALATE_FOR_REVIEW` because current C0-C2 receipt identity was not proven; this repair is binding on R7's C3 case |
| TPGR routing standard | `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md` | Mandatory Classification, Mandatory Escalation, TPGR-T0 Legacy Full-Gate Interlock, Activation Rule, Rollback |
| canonical command catalog | `governance/compat/agent_autorun_command_catalog.py` | the single legacy command-universe owner cited for phase-aware cost separation (`_common_commands`, `_pre_implementation_commands`, `PRE_PUSH_COMMANDS`) |

## Scope / Methodology

The worker captured `executionBaseHead` = `d7b7157802deaf4e74044f13dd52682292bcfe92`
via `git rev-parse HEAD` and confirmed a clean worktree
(`git status --short --untracked-files=all` returned no output) before any
edit. The worker ran the two required preflight commands
(`run_agent_autorun_workflow_gate.py --phase pre-implementation` and
`check_task_governance_route.py --enforce`) before the first edit, both
`COMPLIANT`. The worker then read, in full unless a targeted section was
named: `AGENTS.md`, `docs/reference/guard_orientation/README.md`,
`docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`,
the paired R7 baseline and work order, the TPGR routing standard, R3's
deterministic-precedence and rollback-floor sections, R5's identity-binding,
invalidation, and cost sections, R6 in full including the reviewer-corrected
H3 route and its Zero-Edit R7 Candidate Manifest, R6's worker return
Independent Reviewer Addendum, and `governance/compat/agent_autorun_command_
catalog.py` in full as the single legacy command-universe owner (read only;
not duplicated here). The worker also read the applicable
`governance/compat/check_*.py` checker sections listed in the Checker Source
Read-Ahead Block before authoring either output file, using
`check_markdown_structural_completeness.py`'s own `docs/assessments/` ->
`baseline` and `docs/reviews/` -> `review` structural-group mappings as the
literal shape source, not the dispatch packet checklist alone.

This design is documentary and manual only. No live TPGR receipt exists for
any case below; no canary, selective command plan, harness, fixture,
checker, schema, receipt, registry field, or catalog row is created. The
legacy phase-appropriate gate bundle is always the controlling outcome; TPGR
output is compared against it for advisory diagnostic purposes only and
never substitutes for it.

## Comparator Record

Documentary schema, at minimum the following fields, per the paired work
order's Design Contract. No field below is implemented, persisted, or given
a runtime schema by this design; it names the fields a future R8+
implementation would populate on an existing evidence artifact, exactly as
R5's Receipt Ownership Table already does for its own six candidate fields.

| Field | Definition | Currency rule |
| --- | --- | --- |
| `canaryCaseId` | one of C1-C6 below | static per case |
| `taskArchetype` | A1-A6 per the TPGR standard's archetype vocabulary | static per case |
| `lifecyclePhase` | the specific autorun phase (`common`, `pre-implementation`, `pre-push`) the comparison is evaluated at, per `agent_autorun_command_catalog.py`'s own phase-disjoint tuples | must match the actual phase the legacy command belongs to; a phase mismatch is Mismatch Class 3 below |
| `sourceIdentity` | the pinned upstream commit/mirror hash or the specific file identity the case concerns, per R5's Invalidation Precedence level 1 | re-derived fresh at comparison time, never cached |
| `diffIdentity` | the exact `git diff --name-status <base>..<head>` range the comparison covers | re-derived fresh; a stale range is Mismatch Class 3 |
| `commandCatalogIdentity` | the stable command-row key plus serialized arguments plus catalog blob identity, per R5's Identity-Binding Contract item 3 | re-derived fresh against the current catalog, never assumed stable from a filename match |
| `checkerIdentity` | the checker entry path plus its semantic-dependency-closure identity, per R5's Invalidation Precedence level 4 | re-derived fresh; a same-path semantic change is Mismatch Class 4 |
| `confirmingReviewIdentity` | the identity-bound confirming review artifact path, role, and immutable artifact identity, per R5's Identity-Binding Contract item 4 | re-derived fresh; a bare role label alone never suffices |
| `legacyObservedOutcome` | the actual pass/fail/violation-count result of running the full phase-appropriate legacy bundle | OBSERVED only when a live legacy command actually ran; otherwise the cell is `NOT_YET_RUN`, never fabricated |
| `legacyEvidenceRef` | the specific command output, receipt path, or `.cvf/runtime/autorun-receipts/*.json` reference proving `legacyObservedOutcome` | must be an actual artifact reference, never a description |
| `tpgrAdvisoryOutcome` | the shadow route TPGR's classification manifest would independently derive for the same case, applying R3's Route Outcomes precedence and R5's applicability/invalidation rules | PROJECTED unless a live TPGR receipt exists; no live receipt exists for any C1-C6 case in this design |
| `tpgrEvidenceRef` | the specific classification manifest, worksheet, or routing-receipt reference proving `tpgrAdvisoryOutcome` | must be an actual artifact reference or explicitly `PROJECTED_NO_RECEIPT`, never fabricated |
| `comparisonDisposition` | exactly one of: `EXACT_AGREEMENT`, `ADVISORY_STRICTER`, `ADVISORY_LIGHTER`, `UNKNOWN_PARTIAL`, `CONTRADICTION` | derived by comparing `legacyObservedOutcome` against `tpgrAdvisoryOutcome`; never assumed |
| `controllingOutcome` | always `legacyObservedOutcome` in R7 | fixed; TPGR output never controls |
| `mismatchClass` | one of the six classes below, or `NONE` for exact agreement | derived, never worker-declared as a downgrade |
| `earliestAffectedNode` | the specific R3 Dependency Invalidation Graph node (or R5 Invalidation Precedence level) where the mismatch originates | re-derived by walking the graph top-to-bottom per R3/R5's earliest-affected-node rule, never assumed to be the whole scope |
| `preservedEvidence` | the immutable historical record of both sides' outcomes at comparison time | never deleted or rewritten, per R3 Rule 4 and R5's historical-immutability rule |
| `rollbackTier` | `TIER_1_GLOBAL` or `TIER_2_CLASS_SCOPED`, or `NOT_TRIGGERED` | ambiguity always promotes Tier 2 to Tier 1, per the hard rule below |
| `rollbackFromNode` | the specific node/scope rollback restores to | bounded to the earliest affected node's own scope for Tier 2; global for Tier 1 |
| `rollbackTrigger` | the specific condition that fired the rollback | must cite an objective fact, never a worker preference |
| `rollbackAction` | the design-time state transition performed | legacy-only advisory-off posture; never a claimed config-switch flip unless a current CVF-owned source proves one exists (none does; see Rollback Rehearsal) |
| `reEntryRequirement` | the full R6 replay plus R7 comparison/rehearsal proof required before the affected identity is eligible again | copying a receipt or changing a timestamp never satisfies this |
| `observedCost` | cost actually measured from a completed run | labeled `OBSERVED` only when true |
| `projectedCost` | cost estimated but not yet measured | labeled `PROJECTED`; never presented as a saving |

Never call a projected or documentary value observed. A copied timestamp,
path match, or role label is never identity currency, per R5's
Identity-Binding Contract and Re-Earning Rule, both reused unchanged here.

## Required Canary Design Cases (C1-C6)

All six cases are paper/design comparisons only. No canary is run and no
selective plan is executed. Each case independently derives
`tpgrAdvisoryOutcome` from R3's Route Outcomes precedence and R5's
applicability/invalidation rules applied to the archetype's own R3
Threshold Worksheet, then states the required posture and the comparator
disposition this design would assign if a live legacy result existed at
each of `EXACT_AGREEMENT`, `ADVISORY_STRICTER`, and `ADVISORY_LIGHTER`.

### C1 - A1 new upstream corpus

| Field | Value |
| --- | --- |
| canaryCaseId | C1 |
| taskArchetype | A1 new upstream corpus |
| Required posture | both routes retain full first-intake floor |
| tpgrAdvisoryOutcome (independently derived) | `FULL_LAYER_A_REQUIRED`, per R3's A1 worksheet Route Outcome and its zero divergence tolerance (no prior receipt exists, so no lighter route is reachable regardless of file count) |
| legacyObservedOutcome (design-time expectation) | the full first-intake floor (GC-051 registration, structural enumeration, ledger reconciliation, blind-spot Gates 1-3) is unavoidable and phase-appropriate regardless of TPGR; `NOT_YET_RUN` until a live case exists |
| Comparator disposition if legacy result matches TPGR | `EXACT_AGREEMENT`; both routes select the full floor |
| Comparator disposition if a worker-authored shortcut is offered | `ADVISORY_LIGHTER` from a rogue proposal is rejected outright: A1's zero divergence tolerance means any lighter TPGR proposal for A1 is itself evidence of a defect in the classification manifest, not a legitimate comparator state, and routes to Mismatch Class 1 |
| Rollback posture | Tier 1 if the lighter proposal already influenced any executed command; Tier 2 (class-scoped to A1) only if caught before any command selection, and only when the affected class and dependency closure are exact and independently proven |

### C2 - A2 mixed-origin synthesis

| Field | Value |
| --- | --- |
| canaryCaseId | C2 |
| taskArchetype | A2 mixed-origin synthesis |
| Required posture | dual-origin and semantic-reading controls remain mandatory |
| tpgrAdvisoryOutcome (independently derived) | `FULL_LAYER_A_REQUIRED` until reusable receipts and owner mapping are current, per R3's A2 worksheet; dual-origin separation and adversarial-sample full-reads are never reduced by a TPGR classification |
| legacyObservedOutcome (design-time expectation) | full dual-manifest enumeration/hashing plus adversarial full-reads of the highest-risk cluster; `NOT_YET_RUN` until a live case exists |
| Comparator disposition if legacy result matches TPGR | `EXACT_AGREEMENT` |
| Comparator disposition if TPGR proposes skipping the adversarial full-read because a `NO_NEW_VALUE` label exists | `ADVISORY_LIGHTER`, rejected: per R4's reviewer-repaired corpus-semantic-proof rule (cited via R6's Seeded Case 5), a bare label never substitutes for the adversarial-sample evidence itself; this is Mismatch Class 1 |
| Rollback posture | Tier 1 if origin-separation was actually violated in an executed step; otherwise Tier 2 scoped to A2 only when the specific violating claim, and nothing beyond it, is exactly identified |

### C3 - A3 accepted-corpus cluster

| Field | Value |
| --- | --- |
| canaryCaseId | C3 |
| taskArchetype | A3 accepted-corpus cluster |
| Required posture | historical reuse value preserved, but H3 stays `ESCALATE_FOR_REVIEW` until current identity is earned |
| tpgrAdvisoryOutcome (independently derived) | `ESCALATE_FOR_REVIEW` - reapplying R3's A3 worksheet (`LIGHT_ROUTE_ALLOWED` only with current accepted receipts and exact named scope; `ESCALATE_FOR_REVIEW` on any owner/hash/freshness ambiguity) and R6's reviewer-repaired H3 route (current C0-C2 receipt identity not independently reconstructed) to the same fixture class yields the identical strict outcome; this design does not relitigate or soften the R6 reviewer repair |
| legacyObservedOutcome (design-time expectation) | the underlying corpus's own C0-C2 floor is already paid once; the named cluster's own scope requires independent reviewer diff audit before first edit regardless of TPGR; `NOT_YET_RUN` until a live case exists |
| Comparator disposition if legacy result matches TPGR's escalation | `EXACT_AGREEMENT` (both sides require reviewer escalation) |
| Comparator disposition if TPGR proposes `LIGHT_ROUTE_ALLOWED` for C3 | `ADVISORY_LIGHTER`, rejected outright by design: this is the exact case the R6 Independent Reviewer Addendum repaired; any future C3 comparator that computes a light route without independently reconstructing the full R5 Identity-Binding Contract reference set is itself a defect in the comparator, not a legitimate advisory state, and is Mismatch Class 1 plus Mismatch Class 3 (stale/unbound identity) simultaneously |
| Rollback posture | Tier 1 always for a confirmed C3 light-route defect, because a wrongly light-routed A3 case risks laundering unearned currency across the one archetype whose entire value proposition depends on exact scope and identity; Tier 2 is never available for C3 identity-boundary failures specifically, distinct from the general class-scoped allowance |

C3 is the one case in this design where a design-time hard override applies:
regardless of any future computed comparator state, a `LIGHT_ROUTE_ALLOWED`
or `EXACT_AGREEMENT`-with-light-route outcome for H3-class evidence is
treated as a comparator defect requiring Tier 1 rollback, not as a
legitimate lighter advisory finding, per the binding R6 reviewer repair.

### C4 - A4 upstream delta

| Field | Value |
| --- | --- |
| canaryCaseId | C4 |
| taskArchetype | A4 upstream delta |
| Required posture | earliest-node full verification controls affected scope |
| tpgrAdvisoryOutcome (independently derived) | `FULL_LAYER_A_REQUIRED` for the affected delta scope, per R3's A4 worksheet and R5's Invalidation Precedence level 1 (source-identity change invalidates independent of file-hash stability); the D1 node licenses only `DELTA_RECONCILED`, never a broader claim |
| legacyObservedOutcome (design-time expectation) | full re-read of every file in the delta scope, field-by-field comparison against the actual current owner surface (never a cached copy); `NOT_YET_RUN` until a live case exists |
| Comparator disposition if legacy result matches TPGR | `EXACT_AGREEMENT` |
| Comparator disposition if TPGR proposes treating settled sub-claims outside the delta scope as also requiring re-verification | `ADVISORY_STRICTER`, permitted as advisory input but never mandatory: TPGR may flag extra caution, but the legacy result (only the actually-affected scope requires re-verification, per R3's zero-tolerance scope-boundary rule) remains controlling; the stricter flag is recorded as advisory-only diagnostic context, not enforced |
| Comparator disposition if TPGR proposes narrowing the delta scope below the actual affected scope | `ADVISORY_LIGHTER`, rejected: this is Mismatch Class 1, since narrowing a re-verification scope is functionally equivalent to skipping required semantic reading (R3 Rule 5) |
| Rollback posture | Tier 2 scoped to the specific delta identity only, when the earliest affected node is exactly and independently proven per R3's Dependency Invalidation Graph; escalates to Tier 1 if the affected scope cannot be exactly bounded |

### C5 - A5 advisory item

| Field | Value |
| --- | --- |
| canaryCaseId | C5 |
| taskArchetype | A5 advisory item |
| Required posture | authority ambiguity escalates; small size never downgrades |
| tpgrAdvisoryOutcome (independently derived) | `ESCALATE_FOR_REVIEW` on any authority or reuse ambiguity, per R3's A5 worksheet and its Anti-Self-Downgrade Invariant that file count cannot override authority impact; otherwise the cheapest legitimate `LIGHT_ROUTE_ALLOWED` case in the matrix only when authority is unambiguous |
| legacyObservedOutcome (design-time expectation) | source verification of every named CVF standard the item references, plus an explicit Claim Boundary/Authority Boundary statement; `NOT_YET_RUN` until a live case exists |
| Comparator disposition if legacy result matches TPGR | `EXACT_AGREEMENT` |
| Comparator disposition if TPGR proposes a light route because the item is "just one file" | `ADVISORY_LIGHTER`, rejected: per the Anti-Self-Downgrade Invariants (file count barred from overriding authority impact), this is Mismatch Class 1 |
| Comparator disposition if TPGR escalates a genuinely unambiguous, already-reconciled advisory item out of excess caution | `ADVISORY_STRICTER`, permitted as advisory-only noise, never blocking; the legacy result (escalation only where ambiguity is real) remains controlling |
| Rollback posture | Tier 1 if any advisory item was ever cited as authority (immediate full-scope rollback per R3's Rollback Triggers, reused unchanged); otherwise Tier 2 scoped to the single named item when authority ambiguity is exactly and independently resolved |

### C6 - A6 downstream project source

| Field | Value |
| --- | --- |
| canaryCaseId | C6 |
| taskArchetype | A6 downstream project source |
| Required posture | registration never promotes project evidence to CVF authority |
| tpgrAdvisoryOutcome (independently derived) | `FULL_LAYER_A_REQUIRED` when project corpus scanning is claimed, per R3's A6 worksheet; registration-before-scan is mandatory with no lighter-weight rule, and any route that would treat project material as promoting CVF authority must escalate |
| legacyObservedOutcome (design-time expectation) | GC-051 registration-before-scan for the exact `scopePaths`; explicit cross-reference (not merge) of any CVF-relevant finding; `NOT_YET_RUN` until a live case exists |
| Comparator disposition if legacy result matches TPGR | `EXACT_AGREEMENT` |
| Comparator disposition if TPGR proposes citing a registered project entry as CVF authority evidence | `ADVISORY_LIGHTER` in effect (a laundering attempt dressed as agreement), rejected outright: per GC-051 Rule 5 and R3's A6 zero-tolerance authority-promotion boundary, this is Mismatch Class 1 and simultaneously a contamination event requiring Tier 1 rollback regardless of any other field |
| Rollback posture | Tier 1 always for any detected authority-promotion attempt, per R3's Rollback Triggers "immediate full-scope rollback" category, reused unchanged; Tier 2 is never available for an A6 authority-promotion violation specifically |

### C1-C6 Coverage Summary

6/6 archetypes covered. Every case's `tpgrAdvisoryOutcome` is independently
re-derived from R3/R5's own precedence rules applied fresh to the archetype's
worksheet, not copied from R6's H1-H6 historical replay values (R6 replayed
historical fixtures; R7 designs the forward-looking dual-run comparator
mechanics against the same archetypes). C3 explicitly preserves the binding
R6 reviewer repair: `ESCALATE_FOR_REVIEW` until current identity is earned,
never treated as settled or light-routed.

## Required Mismatch Classes (Six)

For each class: detection, controlling outcome, evidence preservation,
rollback tier/scope, operator visibility, and re-entry proof. No mismatch may
silently become agreement.

### Mismatch Class 1 - TPGR advisory is lighter than the legacy outcome

| Field | Value |
| --- | --- |
| Detection | `tpgrAdvisoryOutcome` selects a weaker route token than `legacyObservedOutcome`'s actual evidence requirement, per R3's fixed three-outcome precedence order (`FULL_LAYER_A_REQUIRED` > `ESCALATE_FOR_REVIEW` > `LIGHT_ROUTE_ALLOWED`) |
| Controlling outcome | `legacyObservedOutcome` always; the lighter TPGR value is discarded as a route input, never merged or averaged |
| Evidence preservation | both the lighter TPGR proposal and the actual legacy outcome are preserved verbatim as `preservedEvidence`; the lighter proposal is retained as a diagnostic artifact for reviewer inspection, never deleted |
| Rollback tier/scope | Tier 1 if any executed command was ever skipped, reordered, or shortened because of the lighter proposal; Tier 2 scoped to the specific case only if caught before any command was affected and the affected class/scope is exact |
| Operator visibility | recorded in the comparator's `comparisonDisposition: ADVISORY_LIGHTER` field with the discarded proposal attached; not silently corrected without disclosure |
| Re-entry proof | full R6 replay plus R7 comparison/rehearsal proof for the affected identity; a corrected timestamp or copied receipt never qualifies |

### Mismatch Class 2 - TPGR advisory is stricter than the legacy outcome

| Field | Value |
| --- | --- |
| Detection | `tpgrAdvisoryOutcome` selects a stronger route token than `legacyObservedOutcome`'s actual evidence requirement |
| Controlling outcome | `legacyObservedOutcome` always; the stricter TPGR value is recorded as advisory-only diagnostic context, never used to add enforcement in R7 |
| Evidence preservation | both values preserved verbatim; the stricter flag is retained as future threshold-tuning input, not enforced retroactively |
| Rollback tier/scope | `NOT_TRIGGERED` by a stricter-only mismatch on its own, because no legacy command was suppressed, reordered, or skipped; if a stricter proposal is mistakenly enforced anyway (adding a command the legacy bundle did not require), that enforcement action itself triggers Tier 1, since it is an unauthorized TPGR-controlled execution change |
| Operator visibility | recorded as `comparisonDisposition: ADVISORY_STRICTER`; visible for future threshold calibration, not actioned in R7 |
| Re-entry proof | not applicable unless the stricter value was wrongly enforced, in which case the same full R6/R7 re-entry proof requirement applies to the affected identity |

### Mismatch Class 3 - identity is missing/stale (receipt owner, checker closure, catalog row, or confirming-review identity)

| Field | Value |
| --- | --- |
| Detection | any of the four Identity-Binding Contract legs (owner blob identity, checker semantic-dependency closure, stable command-row identity, confirming review artifact identity, per R5) cannot be independently reconstructed, or a reconstructed value does not match the recorded `receiptOwnerRef`-equivalent reference |
| Controlling outcome | `legacyObservedOutcome` always; `tpgrAdvisoryOutcome` for the affected claim is treated as `UNKNOWN_PARTIAL`, never as `CURRENT`, per R5's "a bare path match never proves currency" rule |
| Evidence preservation | the incomplete/stale identity reference is preserved as `historicalDisposition`; it licenses no current claim, per R5's Re-Earning Rule |
| Rollback tier/scope | Tier 2 scoped to the earliest affected node if the missing/stale leg is exactly and independently isolated; promotes to Tier 1 if the affected scope cannot be exactly bounded, or if the missing identity is the confirming-review leg (review-authority changes affect trust in the whole comparator, per R5 Invalidation Precedence level 6) |
| Operator visibility | recorded with the specific missing/stale leg named (owner blob, checker closure, catalog row, or confirming review), never a generic "identity issue" label |
| Re-entry proof | full R6 replay plus R7 comparison/rehearsal proof for the affected identity, starting from the `recomputeFromNode` value per R5's Re-Earning Rule |

### Mismatch Class 4 - checker or catalog semantics drift while names remain stable

| Field | Value |
| --- | --- |
| Detection | the checker's semantic-dependency closure (imported policy/schema/config surfaces) changes even though the checker's filename and command-row key stay stable, per R5's Invalidation Precedence level 4; independently verified by comparing the closure's current identities against those recorded at comparison time, never by filename comparison alone |
| Controlling outcome | `legacyObservedOutcome` always; any `tpgrAdvisoryOutcome` computed before the drift is marked `EXPIRED_HISTORICAL` for current eligibility, never silently carried forward as `CURRENT` |
| Evidence preservation | the pre-drift comparator state is preserved as `historicalDisposition`; the drift event itself is recorded as `invalidationEvent` |
| Rollback tier/scope | Tier 2 scoped to exactly the claims whose evidence depended on the specific drifted checker's semantics, per R5's earliest-affected-node rule; promotes to Tier 1 if the drift's blast radius across dependent claims cannot be exactly enumerated |
| Operator visibility | recorded with the specific checker path and the fact that filename/command-row stability masked the semantic change, so a reviewer does not mistake filename stability for currency |
| Re-entry proof | full R6 replay plus R7 comparison/rehearsal proof for the affected identity, re-deriving the closure fresh from the current checker source |

### Mismatch Class 5 - either comparison side times out, is partial, malformed, or unavailable

| Field | Value |
| --- | --- |
| Detection | `legacyObservedOutcome` or `tpgrAdvisoryOutcome` cannot be fully populated (a command did not complete, output was malformed, or a required field is missing) |
| Controlling outcome | if the legacy side is unavailable, the phase-appropriate legacy bundle has simply not yet been run and no comparison exists yet (`NOT_YET_RUN`, not a comparator disposition); if the TPGR side is unavailable, the comparator records `comparisonDisposition: UNKNOWN_PARTIAL`, never `EXACT_AGREEMENT` or any agreement-adjacent value, per the acceptance threshold that zero unknown/partial results may be treated as agreement |
| Evidence preservation | whatever partial output exists is preserved verbatim, labeled partial; a truncated or malformed record is never padded or inferred into a complete one |
| Rollback tier/scope | Tier 1, because an unavailable or malformed comparison side means the affected scope cannot be exactly bounded (the ambiguity-promotes-to-Tier-1 rule applies directly) |
| Operator visibility | recorded explicitly as `UNKNOWN_PARTIAL` with the specific missing/malformed component named |
| Re-entry proof | full R6 replay plus R7 comparison/rehearsal proof for the affected identity; a re-run that merely retries without diagnosing the original timeout/malformation cause does not by itself qualify unless the retry itself produces genuinely fresh, complete, owner-verified evidence |

### Mismatch Class 6 - evidence sources contradict each other or the worker summary

| Field | Value |
| --- | --- |
| Detection | comparing an independently observable record (command output, receipt file, gate log) against a worker's own narrative summary surfaces a contradiction, exactly as R6's Seeded Case 15 (contradictory gate evidence) already demonstrates for this defect class; the independently observable record always controls over a self-reported summary, per R4/R5's Anti-Self-Downgrade Invariants applied to self-reported summaries |
| Controlling outcome | `legacyObservedOutcome` always; the contradicted worker summary is discarded as a route/comparator input in favor of the independently observable record |
| Evidence preservation | both the (corrected) summary and the full independently-observable evidence, including any first-run failure, are preserved and disclosed, never overwritten with a final-only summary, per this work order's own explicit instruction |
| Rollback tier/scope | Tier 1, because a contradiction between evidence sources means the actual current state cannot be trusted without independent re-verification, and the affected scope of the contradiction cannot be assumed bounded until re-verified |
| Operator visibility | recorded as `comparisonDisposition: CONTRADICTION` with both conflicting records shown side by side, never silently reconciled toward the more favorable one |
| Re-entry proof | full R6 replay plus R7 comparison/rehearsal proof for the affected identity, plus an explicit reconciliation record showing which source was authoritative and why |

### Mismatch Class Coverage Summary

6/6 mismatch classes defined with deterministic detection, controlling
outcome, evidence preservation, rollback tier/scope, operator visibility, and
re-entry proof. No class permits `UNKNOWN_PARTIAL` or `CONTRADICTION` to
resolve to `EXACT_AGREEMENT`. No class permits `ADVISORY_LIGHTER` to control
execution.

## Rollback Rehearsal

Rollback is a design-time state transition back to legacy-only advisory-off
posture. No current CVF-owned source proves that a runtime config switch
exists to toggle TPGR advisory participation on or off; this design does not
claim one exists. The rehearsed transition below is a paper/documentary
state change in how a future governed artifact would record TPGR's
participation status, not an executable mechanism. Re-entry after any
rollback requires the full R6 replay plus R7 comparison/rehearsal proof for
the affected identity; copying a receipt or changing a timestamp never
qualifies, per the Re-Earning Rule reused unchanged from R5.

Hard rule applied consistently throughout this rehearsal: ambiguity always
promotes Tier 2 to Tier 1. Any rehearsal row below whose affected class or
dependency closure cannot be exactly and independently proven is Tier 1 by
default, never Tier 2.

### Tier 1 - Global Rollback Scenarios (four required, four provided)

| # | Scenario | Trigger | Scope | Restored safe route | Preserved evidence | Re-entry requirement |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | Unknown scope: a comparator mismatch is detected but the affected identity's earliest-affected node cannot be exactly bounded by the Dependency Invalidation Graph | any Mismatch Class 3-6 event whose blast radius is not exactly enumerable | global (all archetypes, all in-flight comparator claims) | `FULL_LAYER_A_REQUIRED` for every affected scope, full legacy bundle per TPGR-T0 (`RUN_FULL_LEGACY_BUNDLE`), reviewer re-confirmation before any future light routing | every claim's state at the moment of rollback preserved verbatim as `historicalDisposition` | full R6 replay plus R7 comparison/rehearsal proof for every affected identity; reviewer must independently re-bound the scope before any narrower re-entry is even considered |
| G2 | Cross-class contamination: an A6-class authority-promotion attempt, or a C3-class light-route defect, is detected and its evidence has already been cited in a claim touching a different archetype | Mismatch Class 1 combined with an authority-boundary violation (C3 or C6 specifically, per those cases' hard-override rows above) | global, because contamination by definition crosses the single-archetype boundary that Tier 2 requires to stay scoped | full-scope rollback to `FULL_LAYER_A_REQUIRED`; any downstream claim that cited the contaminated evidence is also marked `EXPIRED_HISTORICAL` | the contaminated claim and every downstream citation of it preserved verbatim, with the contamination path disclosed | full R6 replay plus R7 comparison/rehearsal proof for every touched identity, not just the originating one |
| G3 | Command suppression risk: any comparator state, however derived, is about to cause an executed step to skip, reorder, or shorten a legacy command | any Mismatch Class 1 event where the lighter proposal has already influenced command selection, or any attempted use of `tpgrAdvisoryOutcome` as if it were `controllingOutcome` | global, because a suppression risk that reaches command execution is a TPGR-standard-level interlock violation (`selectiveExecutionAuthorized` must remain `false`), not a single-archetype issue | immediate restoration of `RUN_FULL_LEGACY_BUNDLE` for the current and all pending phases; the suppressed/reordered/shortened command is re-run in full before any further progress | the suppression attempt itself preserved as evidence, including which command and phase were affected | full R6 replay plus R7 comparison/rehearsal proof; additionally, an explicit independent confirmation that `check_task_governance_route.py --enforce` reports `Selective execution authorized: false` before any future TPGR participation resumes |
| G4 | Comparator integrity failure: the comparator's own identity-binding references (owner blob, checker closure, catalog row, or confirming review identity) are found to be internally inconsistent across two or more cases, suggesting a defect in the comparator design itself rather than in one case | two or more Mismatch Class 3 or Class 4 events in unrelated cases within the same review cycle, or any single event where the comparator's own schema (not the underlying evidence) is implicated | global, because a comparator-design-level defect cannot be assumed bounded to the cases where it happened to be observed | full-scope rollback; the comparator design itself (this assessment's Comparator Record schema) is flagged for reviewer re-audit before any case is re-evaluated against it | every case's raw evidence preserved verbatim, independent of the comparator's own derived fields, so a corrected comparator can be re-applied to unchanged raw evidence | full R6 replay plus R7 comparison/rehearsal proof for every case evaluated under the suspect comparator version, plus independent reviewer sign-off on the comparator schema correction itself |

### Tier 2 - Class-Scoped Rollback Scenarios (three required, three provided)

Tier 2 is allowed only when the affected class and dependency closure are
exact and independently proven. Each row below states the specific proof
condition that keeps it at Tier 2 rather than promoting to Tier 1.

| # | Scenario | Trigger | Scope | Restored safe route | Preserved evidence | Re-entry requirement | Why Tier 2 (not Tier 1) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | A4 delta-scope invalidation: the specific CVF owner surface a delta was compared against changes | R5 Invalidation Precedence level 2 (owner surface) fires for a single, exactly identified A4 delta scope | the specific delta scope only, per R3's A4 worksheet rollback trigger ("rolls back to `FULL_LAYER_A_REQUIRED` from the earliest affected node only") | `FULL_LAYER_A_REQUIRED` for the affected delta scope; unaffected historical sub-claims from before that node remain historical, per R3 Rule 4 | the pre-invalidation delta ledger preserved verbatim | full R6 replay plus R7 comparison/rehearsal proof for the affected delta identity only | the affected scope is exactly the diffable delta boundary, independently re-derivable by direct diff of the owner surface, per R3's Dependency Invalidation Graph detection method for this exact node |
| S2 | A3 named-cluster scope drift: the named cluster's actual file set is found to include exactly one file outside the originally registered scope, and no other case or archetype cites that file | R3's A3 worksheet hostile example scenario, confirmed to be isolated to the single named cluster | the specific named cluster only | `ESCALATE_FOR_REVIEW` for the affected cluster (matching R3's own A3 rollback trigger for scope-drift); the underlying corpus's own C0-C2 receipts remain valid if unaffected | the pre-drift named-scope list preserved verbatim, with the drifted file flagged | full R6 replay plus R7 comparison/rehearsal proof for the affected cluster identity; per the C3 hard-override rule above, this scenario can never resolve directly back to `LIGHT_ROUTE_ALLOWED` without independently reconstructing the full R5 Identity-Binding Contract reference set first | the drifted file is exactly named and independently confirmed to be cited by no other claim; if that confirmation cannot be made exactly, this promotes to Tier 1 (G2) instead |
| S3 | A5 single-item authority re-check: a re-issued or corrected version of one named advisory document is published, and the chain map's canonical `Input type` enum is unchanged | R3's A5 worksheet freshness invalidator ("a re-issued or corrected version of the same document") fires for exactly one named item | the single named advisory item only | `ESCALATE_FOR_REVIEW` for the specific item until the reconciliation chain re-confirms its advisory boundary, per R3's A5 rollback trigger | the pre-reissue advisory content preserved verbatim as historical evidence of what it said at that time | full R6 replay plus R7 comparison/rehearsal proof for the specific item identity | the affected item is a single named document with no corpus-scale ripple, and the chain map's own enum is independently confirmed unchanged, which is the exact condition R3's A5 worksheet requires for a scoped (not global) response |

### Rollback Rehearsal Coverage Summary

4/4 required Tier 1 global scenarios rehearsed (unknown scope, cross-class
contamination, command suppression risk, comparator integrity failure). 3/3
required Tier 2 class-scoped scenarios rehearsed (A4 delta, A3 named-cluster
drift, A5 single-item re-check), each with an explicit proof condition
justifying why it did not promote to Tier 1. 100% of ambiguous-scope rows in
this rehearsal default to Tier 1: every Tier 2 row above states the exact
condition required to stay scoped, and every condition's failure mode is
explicitly routed to a Tier 1 scenario (G2 or G4) in the same row or the
scenario immediately above it.

## Negative-Test Design (Specified, Not Implemented)

Ten negative-test designs, per the paired work order's Design Contract item
8. No test, fixture, script, checker, config, or harness is created by this
design; each row states what a future R8+ implementation would need to
prove, and the expected outcome.

| # | Negative-test design | Expected outcome |
| --- | --- | --- |
| N1 | Feed the comparator a case where `tpgrAdvisoryOutcome` is lighter than a known `legacyObservedOutcome`, then assert no legacy command was skipped, reordered, or shortened as a result | assertion holds: `controllingOutcome` always equals `legacyObservedOutcome`; the lighter proposal is discarded as a route input, matching Mismatch Class 1's controlling-outcome rule above |
| N2 | Feed the comparator a case where `tpgrAdvisoryOutcome` is stricter than `legacyObservedOutcome`, then assert no additional enforcement command was added to the phase-appropriate legacy bundle | assertion holds: the stricter value is recorded as advisory-only diagnostic context per Mismatch Class 2; `NOT_TRIGGERED` rollback state unless the stricter value is wrongly enforced |
| N3 | Feed the comparator a case where `tpgrAdvisoryOutcome` is `UNKNOWN_PARTIAL` (a required field could not be populated), then assert `comparisonDisposition` never resolves to `EXACT_AGREEMENT` | assertion holds: Mismatch Class 5's controlling-outcome rule explicitly forbids `UNKNOWN_PARTIAL` or malformed data resolving to agreement |
| N4 | Feed the comparator an H3-class C3 case whose receipt identity cannot be independently reconstructed, then assert the case never resolves to `LIGHT_ROUTE_ALLOWED` regardless of how confident the input evidence appears | assertion holds: C3's hard-override rule treats any such resolution as a comparator defect requiring Tier 1 rollback, not a legitimate lighter finding |
| N5 | Feed the comparator two cases with identical filenames/command-row keys but different underlying checker semantic-dependency closures, then assert the drift is detected despite filename stability | assertion holds: Mismatch Class 4's detection method explicitly compares the closure's identities, never filename alone, mirroring R5's own Invalidation Precedence level 4 resolution of the identical R5 Hostile Case 2 |
| N6 | Feed the comparator a case whose affected class/scope cannot be exactly bounded, then assert the rollback tier resolves to Tier 1, never Tier 2 | assertion holds: the ambiguity-promotes-to-Tier-1 rule is applied as a hard default throughout the Rollback Rehearsal section; every Tier 2 row above states the exact bounding condition, and its absence is explicitly routed to Tier 1 |
| N7 | Trigger a Tier 1 or Tier 2 rollback, then assert every prior historical claim's `historicalDisposition` remains byte-identical before and after the rollback | assertion holds: rollback moves only the live `eligibilityState`/`comparisonDisposition` view; the underlying historical record is never deleted or rewritten, per R3 Rule 4 and R5's historical-immutability rule, both reused unchanged throughout this design |
| N8 | Attempt re-entry for an `EXPIRED_HISTORICAL`/rolled-back identity by copying its prior evidence references into a new artifact with a new timestamp, then assert re-entry is refused | assertion holds: per the Re-Earning Rule reused unchanged from R5, a copied receipt with a new timestamp never re-earns eligibility; only fresh, independently owner-verified re-derivation starting at the correct node succeeds |
| N9 | Feed a fully-populated comparator record (all fields present, `comparisonDisposition: EXACT_AGREEMENT`) into a hypothetical downstream consumer, then assert it cannot be interpreted or serialized as an execution plan, selective command list, or command-suppression instruction | assertion holds: the Comparator Record schema carries no field representing an executable action; `controllingOutcome` is always the legacy result, and no field in the schema authorizes skipping, reordering, or selecting a subset of legacy commands |
| N10 | Feed the comparator a case at a specific autorun phase (for example `pre-implementation`), then assert the legacy bundle selected for comparison is exactly that phase's commands from `_common_commands` plus `_pre_implementation_commands`, never a `PRE_PUSH_COMMANDS` entry mischarged against a pre-implementation case, and never a truncated subset of the phase-appropriate bundle | assertion holds: `agent_autorun_command_catalog.py`'s phase-disjoint tuples (`_common_commands`, `_pre_implementation_commands`, `PRE_PUSH_COMMANDS`) are the single command-universe owner; this directly reuses R6's Seeded Case 14 resolution (phase-aware cost boundary) and extends it to bundle-selection completeness, not merely cost accounting |

### Negative-Test Coverage Summary

10/10 negative-test designs specified with an expected outcome. No test,
fixture, script, checker, config, or harness is implemented by this design.

## Cost And Value

Cost categories separated per the paired work order's Design Contract item
7: unavoidable legacy execution, TPGR classification, identity comparison,
dual-run comparison, mismatch diagnosis, rollback rehearsal, and maintenance
cost. All R7 values are documentary/projected unless backed by an already
observed historical value from R2G/R3/R5/R6; no projected saving authorizes
activation.

| Cost category | C1 (A1) | C2 (A2) | C3 (A3) | C4 (A4) | C5 (A5) | C6 (A6) |
| --- | --- | --- | --- | --- | --- | --- |
| Unavoidable legacy execution (never counted as TPGR savings) | OBSERVED via R6's H1: full 231-file enumeration/hash/ledger, reused as historical evidence, not re-measured here | OBSERVED via R6's H2: full 764-file enumeration/hashing plus adversarial full-reads, reused as historical evidence | OBSERVED via R6's H3: the underlying corpus's own C0-C2 floor, already paid once; zero full-corpus re-enumeration | OBSERVED via R6's H4: full 107-file re-read plus field-by-field live-surface comparison | OBSERVED via R6's H5: one document read plus source-verification | OBSERVED via R6's H6: one registry entry per project scope |
| TPGR classification cost | PROJECTED: one classification manifest plus one routing receipt; no live receipt exists for C1 | PROJECTED: one classification manifest; no live receipt exists | PROJECTED: near-zero marginal cost; no live receipt exists | PROJECTED: one delta-reconciliation classification; no live receipt exists | PROJECTED: near-zero, already the cheapest route without TPGR | PROJECTED: none beyond the existing routing receipt every corpus-type entry would receive |
| Identity comparison cost (R5's `identityComparisonCost`) | UNKNOWN/PROJECTED: no live `receiptOwnerRef`-equivalent identity comparison has ever been performed for C1; reused unchanged from R5's Cost Proof and R6's Cost Accounting, not re-measured here | UNKNOWN/PROJECTED: same reasoning | UNKNOWN/PROJECTED: same reasoning; C3 is the case where identity comparison matters most and is exactly the unmeasured cost this design must not hide | UNKNOWN/PROJECTED: same reasoning | UNKNOWN/PROJECTED: same reasoning | UNKNOWN/PROJECTED: same reasoning |
| Dual-run comparison cost (new to R7) | PROJECTED: one comparator-record population per case; no live dual-run has ever executed, so this cell has no observed value to draw from | PROJECTED: same reasoning | PROJECTED: same reasoning, plus the C3 hard-override check adds one additional deterministic comparison step | PROJECTED: same reasoning | PROJECTED: same reasoning | PROJECTED: same reasoning |
| Mismatch diagnosis cost (new to R7) | PROJECTED: applies only if a mismatch is actually detected; `N/A` for a clean `EXACT_AGREEMENT` case | PROJECTED: same reasoning | PROJECTED: same reasoning, structurally higher expected cost given C3's hard-override rule, but still unmeasured | PROJECTED: same reasoning | PROJECTED: same reasoning | PROJECTED: same reasoning |
| Rollback rehearsal cost (new to R7; this design's own paper rehearsal) | OBSERVED: this design itself performed the paper rehearsal (see Rollback Rehearsal section); the cost of authoring G1-G4/S1-S3 is the only rehearsal cost actually incurred so far, and it is a one-time design cost, not a per-case recurring cost | same one-time design cost, not per-case | same | same | same | same |
| Maintenance cost | UNKNOWN/PROJECTED: no live TPGR receipt has ever existed for any archetype, so recurring maintenance cost of keeping the comparator's identity references current is unmeasured, per R3's Per-Archetype Cost Ceilings table reused unchanged | UNKNOWN/PROJECTED: same reasoning | UNKNOWN/PROJECTED: same reasoning | UNKNOWN/PROJECTED: same reasoning | UNKNOWN/PROJECTED: same reasoning | UNKNOWN/PROJECTED: same reasoning |
| Full legacy autorun bundle | ALWAYS mandatory per TPGR-T0's Legacy Full-Gate Interlock, regardless of any comparator outcome above; not reduced by this design for any case | same | same | same | same | same |

No cell in this table counts unavoidable legacy execution toward TPGR
savings. No cell presents a projected value as an observed saving. Every
UNKNOWN/PROJECTED cell carries the explicit measurement requirement that only
a live TPGR receipt (none exists) could resolve, consistent with R3 Rule 6
and R5's Cost Proof section, both reused unchanged here. The one genuinely
OBSERVED new-to-R7 cost is this design's own paper rollback rehearsal
authoring cost, which is a one-time design cost, not a per-case recurring
cost, and is not claimed as a saving of any kind.

## Zero-Edit R8 P0/P1 Allowlist-Decision Candidate Manifest

Per the paired work order's Design Contract item 9. No path below is edited,
drafted, or scaffolded by this worker.

| Candidate path | Candidate change | Justifying evidence | Authorization state |
| --- | --- | --- | --- |
| a new `governance/compat/check_dual_run_comparator_shape.py` (candidate name only; file does not exist) | machine-check the Comparator Record schema's field presence and `comparisonDisposition`/`rollbackTier` enum values against any future governed artifact that asserts a comparator row | this design's Comparator Record and Required Mismatch Classes sections | UNAUTHORIZED; R8 must specify exact detection regexes, false-positive controls, and the P0/P1 allowlist boundary before any checker is drafted, exactly as R6's own Zero-Edit R7 Candidate Manifest already flagged this same treatment for the sibling migration/comparator checkers |
| `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md` | evaluate (not adopt) whether a "P0/P1 Allowlist Decision" section naming a narrow, reviewer-confirmed set of always-`EXACT_AGREEMENT` historical cases as P0 (candidate for a future lighter route) versus every other case as P1 (remains full-bundle) should be added, citing this R7 design's C1-C6 coverage by reference | this design's C1-C6 cases and their comparator dispositions | UNAUTHORIZED; requires R8 and independent review; no case in this design is proposed as P0 by this worker |
| a new dual-run comparator harness (candidate name only; no file exists) | actually execute a live TPGR shadow route against a live legacy-gate outcome for a real governed range, strictly advisory and non-blocking | this design's Cost And Value table's UNKNOWN/PROJECTED identity-comparison and dual-run-comparison cost gaps, which only live telemetry can resolve | UNAUTHORIZED; R8 must define the exact P0/P1 allowlist decision criteria, an activation gate distinct from this design's paper rehearsal, and negative tests proving the harness cannot become enforcing before any implementation is authorized |
| any `governance/compat/check_*.py` file | none proposed by this design | no case, mismatch class, or rollback scenario in this design identified a checker gap requiring a new or modified checker | NOT_PROPOSED |
| a new registry, receipt store, lifecycle standard, config switch, or second command catalog | none proposed | this design performs manual/documentary comparison and paper rehearsal only, using the existing R3/R5/R6 field/token/graph/catalog definitions unchanged, with no second truth store and no claimed config switch | NOT_PROPOSED |

No path above is edited by this worker. This table exists to satisfy the
work order's requirement for a zero-edit R8 candidate manifest, not to
pre-approve any future change.

## Acceptance Threshold Reconciliation

Each threshold from the paired work order's Acceptance Thresholds section,
reconciled against this design's actual evidence above.

| Threshold | Required | Observed | Met? |
| --- | --- | --- | --- |
| design cases reconciled | 6/6 archetypes | 6/6 (C1-C6 above) | YES |
| advisory-lighter outcomes controlling execution | 0 | 0; every case's Comparator disposition table shows `ADVISORY_LIGHTER` proposals discarded, never controlling | YES |
| legacy commands suppressed, reordered, or skipped | 0 | 0; `controllingOutcome` is always `legacyObservedOutcome` across every case, mismatch class, and negative-test design | YES |
| unknown or partial comparator results treated as agreement | 0 | 0; Mismatch Class 5 explicitly forbids this, and N3 specifies the negative test proving it | YES |
| stale or unbound identity treated as current | 0 | 0; Mismatch Class 3 and C3's hard-override rule explicitly forbid this, and N4 specifies the negative test proving it | YES |
| mismatch classes with deterministic disposition | 6/6 | 6/6 (Mismatch Classes 1-6 above, each with detection/controlling-outcome/evidence/rollback/visibility/re-entry) | YES |
| Tier 1 rollback scenarios rehearsed | at least 4 | 4 (G1-G4) | YES |
| Tier 2 rollback scenarios rehearsed | at least 3 | 3 (S1-S3) | YES |
| ambiguous rollback scope defaults to Tier 1 | 100% | 100%; every Tier 2 row's proof condition failure mode is explicitly routed to a Tier 1 scenario | YES |
| re-entry without full R6/R7 proof path | 0 | 0; every mismatch class and rollback scenario row states the full R6/R7 re-entry requirement, and N8 specifies the negative test proving copied receipts never qualify | YES |
| costs counted as savings before observation | 0 | 0; every Cost And Value cell is explicitly labeled OBSERVED, PROJECTED, or UNKNOWN/PROJECTED, and none of the PROJECTED/UNKNOWN cells is presented as a saving | YES |
| selective execution remains unauthorized | required | confirmed by the required preflight `check_task_governance_route.py --enforce` run (`Selective execution authorized: false`), independently re-verified below | YES |
| all ten negative-test designs have expected outcomes | 10/10 | 10/10 (N1-N10 above) | YES |
| exact two-path manifest and no commit | required | exactly this assessment and the paired worker return; no `git add`/`git commit`/staging command run by this worker | YES |

All fourteen acceptance thresholds are met. No threshold miss exists that
would forbid the proceed disposition.

## Evidence / Verification

Before any edit, both required preflight commands were run at
`executionBaseHead`: `run_agent_autorun_workflow_gate.py --phase
pre-implementation` (`COMPLIANT`) and `check_task_governance_route.py
--enforce` (`COMPLIANT`, `Selective execution authorized: false`, `Legacy
gate disposition: RUN_FULL_LEGACY_BUNDLE`, `Violations: 0`). During
authoring, this design records C1-C6 comparator cases, six mismatch classes,
the Tier 1/Tier 2 rollback rehearsal, ten negative-test designs, cost
separation, the zero-edit R8 manifest, and the acceptance-threshold
reconciliation directly in its own tables above and in the paired worker
return's Command Evidence section. Reviewer acceptance of this evidence,
including independent recomputation of at least one case from each archetype
and every mismatch class per the work order's Review Gate, remains a
separate, independent step owned by the reviewer/closer.

## Findings / Position

All six required canary design cases (C1-C6) are independently derived from
R3's Route Outcomes precedence and R5's identity-binding/invalidation rules
applied fresh to each archetype's own R3 Threshold Worksheet, with C3
explicitly preserving the binding R6 reviewer repair (`ESCALATE_FOR_REVIEW`
until current identity is earned, treated as a hard comparator-defect
override rather than a soft preference). All six required mismatch classes
have deterministic detection, controlling-outcome, evidence-preservation,
rollback-tier, operator-visibility, and re-entry-proof rules; none permits
`ADVISORY_LIGHTER` to control execution or `UNKNOWN_PARTIAL`/`CONTRADICTION`
to resolve to agreement. The rollback rehearsal provides four Tier 1 global
scenarios and three Tier 2 class-scoped scenarios, each Tier 2 row stating
the exact proof condition required to avoid promotion to Tier 1, with the
ambiguity-promotes-to-Tier-1 rule applied as a hard default throughout. Ten
negative-test designs are specified (not implemented) with expected outcomes
tracing directly to the comparator, mismatch, and rollback rules above. Cost
accounting separates unavoidable legacy execution, TPGR classification,
identity comparison, dual-run comparison, mismatch diagnosis, rollback
rehearsal, and maintenance cost, with every unmeasured cell explicitly
labeled UNKNOWN/PROJECTED and none presented as an observed saving. All
fourteen of the work order's Acceptance Thresholds are independently met;
none is missed. Rollback itself is honestly scoped as a design-time state
transition with no claimed config switch, since no current CVF-owned source
proves one exists. The design therefore selects the proceed disposition
`PROCEED_TO_R8_P0_P1_ALLOWLIST_DECISION_DESIGN`, one of the four exact tokens
the paired baseline and work order allow, distinct from R6's own
forward-pointing `PROCEED_TO_R7_DUAL_RUN_CANARY_AND_ROLLBACK_REHEARSAL_
DESIGN` token, which this design does not reuse.

## Risk / Corrective Action

Primary risk: a future reader could mistake the Cost And Value table's
uniform UNKNOWN/PROJECTED identity-comparison and dual-run-comparison cells
for a design gap rather than the intended honest disclosure that no live
TPGR receipt has ever existed for any archetype. Corrective action: this
section states explicitly that these cells cannot be resolved by design
alone; only a future live receipt (out of scope for R7 and for any R8
design-only tranche) could convert them to OBSERVED, and no projected value
in this design is treated as a saving that would authorize activation.

Secondary risk: C3's hard-override rule (any light-route resolution for
H3-class evidence is treated as a comparator defect requiring Tier 1
rollback) is deliberately more conservative than the general Mismatch Class
1 rule for other archetypes. A future reader could read this asymmetry as an
inconsistency rather than a deliberate, binding preservation of the R6
reviewer repair. Corrective action: the C3 case section and the Tier 2 S2
row both state explicitly why this asymmetry exists and cite the exact
Independent Reviewer Addendum finding it preserves; a future R8+ tranche must
not relax this override without an independent reviewer decision citing
fresh, current, R5-shaped identity evidence for the H3-class corpus, not a
cost or convenience argument.

Tertiary risk: the Zero-Edit R8 Candidate Manifest names a P0/P1 allowlist
decision concept without proposing which specific historical cases, if any,
would ever qualify as P0. Corrective action: this is intentional; per the
manifest row's own authorization-state note, R7 does not pre-select any case
as P0, and any future R8 tranche must independently justify each P0
candidate against fresh, current evidence rather than treating this design's
mere naming of the concept as a pre-approval of any specific case.

## Decision

`PROCEED_TO_R8_P0_P1_ALLOWLIST_DECISION_DESIGN`

## Final Disposition

`PROCEED_TO_R8_P0_P1_ALLOWLIST_DECISION_DESIGN`

Rationale: all six required canary design cases (C1-C6) are independently
derived from governed R3/R5 precedence rules with zero fabricated evidence
and the binding R6 reviewer repair on C3 explicitly preserved as a hard
comparator-defect override; all six required mismatch classes have
deterministic, fail-closed dispositions with zero paths to silent agreement
or TPGR-controlled execution; the rollback rehearsal meets both the Tier 1
(4) and Tier 2 (3) floors with the ambiguity-promotes-to-Tier-1 rule applied
100% of the time; all ten negative-test designs have traceable expected
outcomes; cost accounting honestly separates observed, projected, and unknown
values with zero projected savings claimed as observed; and every one of the
work order's fourteen Acceptance Thresholds is independently met with no
miss. This satisfies the paired baseline's Design Contract and Stop
Conditions and the work order's Acceptance Criteria. The next authorized step
is R8 (P0/P1 allowlist decision design), which remains unauthorized by this
design and requires a fresh operator decision and governed dispatch.

## Claim Boundary

This design is a documentation-only, non-implementation dual-run canary and
rollback rehearsal design evidence artifact over existing governed evidence.
It does not implement any checker, receipt, fixture, script, registry field,
or catalog row; does not modify any standard, checker, registry, catalog,
hook, or router; does not intake or register any new source corpus; does not
authorize selective execution (`selectiveExecutionAuthorized` remains
`false` per the TPGR standard, independently verified at this
executionBaseHead); does not run any real canary or selective command plan;
does not claim a config switch exists for toggling TPGR participation; and
does not open R8-R9, T15, or any runtime, provider/live, public-sync,
deployment, or production action. The
`PROCEED_TO_R8_P0_P1_ALLOWLIST_DECISION_DESIGN` disposition authorizes only a
future operator decision to open R8 under a fresh governed dispatch; it does
not itself authorize R8 work.
