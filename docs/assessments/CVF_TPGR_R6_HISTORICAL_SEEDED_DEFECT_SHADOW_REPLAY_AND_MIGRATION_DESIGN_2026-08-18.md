# CVF TPGR-R6 Historical Seeded-Defect Shadow Replay And Migration Design

Memory class: governed-planning-assessment

docType: baseline

Status: COMPLETE_PENDING_REVIEW

Batch ID: TPGR-R6

Date: 2026-08-18

executionBaseHead: `8f195c6ea9c73688ce1391d94f97df2fa572497b`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Responds to work order:
`docs/work_orders/CVF_AGENT_WORK_ORDER_TPGR_R6_HISTORICAL_SEEDED_DEFECT_SHADOW_REPLAY_AND_MIGRATION_DESIGN_2026-08-18.md`

Paired baseline authority:
`docs/baselines/CVF_GC018_TPGR_R6_HISTORICAL_SEEDED_DEFECT_SHADOW_REPLAY_AND_MIGRATION_DESIGN_2026-08-18.md`

## Purpose

Independently shadow-replay the accepted R3-R5 routing design against
governed historical A1-A6 evidence and seeded defects, then design a
fail-closed, non-promoting migration of historical evidence into the R4/R5
field model. This exposes whether the design catches known failures and
preserves the A3 reuse saving without weakening any current guard. This is
documentary/manual shadow evaluation only, not implementation. It changes no
standard, checker, registry, catalog, hook, or source corpus, and creates no
executable fixture, receipt, or selective-execution behavior.

## Source / Predecessor Evidence

| Source | Identity | Authority use |
| --- | --- | --- |
| paired baseline | `docs/baselines/CVF_GC018_TPGR_R6_HISTORICAL_SEEDED_DEFECT_SHADOW_REPLAY_AND_MIGRATION_DESIGN_2026-08-18.md` | complete execution authority for this design |
| paired work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_TPGR_R6_HISTORICAL_SEEDED_DEFECT_SHADOW_REPLAY_AND_MIGRATION_DESIGN_2026-08-18.md` | task manifest, Replay And Migration Contract, Required Historical Replay Cases, Required Seeded Defect And Negative Cases, Acceptance Thresholds |
| R2G assessment | `docs/assessments/CVF_TPGR_R2G_GENERALIZED_ABSORPTION_ROUTING_FEASIBILITY_ASSESSMENT_2026-08-17.md` | A1-A6 archetype worksheets and Verified As-Is Layer A Owner Map used as H1-H6 fixture authority |
| R3 assessment | `docs/assessments/CVF_TPGR_R3_ARCHETYPE_THRESHOLD_PROOF_DIVERGENCE_AND_ROLLBACK_FLOOR_DESIGN_2026-08-18.md` | A1-A6 Threshold Worksheets, Route Outcomes And Deterministic Precedence, Proof Floors, Dependency Invalidation Graph, Hostile Test Design Matrix |
| R3 worker return | `docs/reviews/CVF_TPGR_R3_ARCHETYPE_THRESHOLD_PROOF_DIVERGENCE_AND_ROLLBACK_FLOOR_DESIGN_WORKER_RETURN_2026-08-18.md` | Independent Reviewer Addendum confirming R3 evidence |
| R4 assessment | `docs/assessments/CVF_TPGR_R4_SHADOW_INTERFACE_AND_CLAIM_VOCABULARY_DESIGN_2026-08-18.md` | Shadow Interface Field Table (eight fields), Exact Claim Vocabulary (eight tokens), No Promotion By Aggregation rule, `CORPUS_SEMANTICALLY_ABSORBED` Proof Requirement, ten hostile cases |
| R4 worker return | `docs/reviews/CVF_TPGR_R4_SHADOW_INTERFACE_AND_CLAIM_VOCABULARY_DESIGN_WORKER_RETURN_2026-08-18.md` | Independent Reviewer Addendum repairing corpus-semantic-proof, stage-mapping, freshness/route-closure, and derived-state completeness |
| R5 assessment | `docs/assessments/CVF_TPGR_R5_SHADOW_COMMAND_APPLICABILITY_AND_RECEIPT_INVALIDATION_DESIGN_2026-08-18.md` | R4 Invariant-To-Command Applicability Matrix, Receipt Ownership Table (six candidate fields), Identity-Binding Contract, Invalidation Precedence, Re-Earning Rule, False-Positive Boundary, twelve hostile cases |
| R5 worker return | `docs/reviews/CVF_TPGR_R5_SHADOW_COMMAND_APPLICABILITY_AND_RECEIPT_INVALIDATION_DESIGN_WORKER_RETURN_2026-08-18.md` | Independent Reviewer Addendum repairing `receiptOwnerRef` identity-binding, phase-aware cost boundary, and worker evidence consistency |
| TPGR routing standard | `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md` | Mandatory Classification, Mandatory Escalation, TPGR-T0 Legacy Full-Gate Interlock, Activation Rule, Rollback |
| canonical command catalog | `governance/compat/agent_autorun_command_catalog.py` | the single command-universe owner cited for cost separation |

## Scope / Methodology

The worker captured `executionBaseHead` = `8f195c6ea9c73688ce1391d94f97df2fa572497b`
via `git rev-parse HEAD` and confirmed a clean worktree
(`git status --short --untracked-files=all` returned no output) before any
edit. The worker read in full: the paired baseline, the paired work order,
`CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`, `CVF_SESSION_MEMORY.md`,
the active handoff it names, the guard orientation index, the literal-format
gotchas reference, the R2G assessment's six archetype worksheets and Verified
As-Is Layer A Owner Map, the R3 assessment in full (Route Outcomes, A1-A6
Worksheets, Proof Floors, Cost Ceilings, Dependency Invalidation Graph,
Hostile Test Design Matrix) and its worker return's Independent Reviewer
Addendum, the R4 assessment in full and its worker return's Independent
Reviewer Addendum, the R5 assessment in full and its worker return's
Independent Reviewer Addendum, the TPGR routing standard's Mandatory
Classification, Mandatory Escalation, legacy interlock, Activation Rule, and
Rollback sections, and `governance/compat/agent_autorun_command_catalog.py`
in full. The worker also read the applicable `governance/compat/check_*.py`
checker sections listed in the Checker Source Read-Ahead Block before
authoring either output file.

This replay is documentary and manual only. No new corpus scan, source
intake, network access, or re-derivation of any registry/catalog count was
performed. No standard, checker, registry, catalog, hook, or router is
created or modified by this design. No test fixture, script, checker,
receipt, schema, registry field, or catalog row is created. No selective
execution is authorized or claimed; `selectiveExecutionAuthorized` remains
`false` per the TPGR standard, independently verified directly by
`check_task_governance_route.py` at this executionBaseHead (`COMPLIANT`, 0
violations, `Legacy gate disposition: RUN_FULL_LEGACY_BUNDLE`).

Replay method: for each of H1-H6, the worker independently re-derived
`observedShadowRoute` by applying R3's Route Outcomes precedence and R4/R5's
field/token/applicability rules to the objective facts recorded in the cited
R2G/R3 worksheet, without looking at the worksheet's own stated route outcome
first, then compared the independently derived route against the worksheet's
recorded route outcome and against the archetype's historical disposition.
Any mismatch between the independently derived route and either predecessor
value is disclosed verbatim in the worksheet's Mismatches field, never
silently reconciled.

## Exact Historical Fixture Inventory

One governed case per archetype, each preserving source commit/path and
accepted historical disposition, per the work order's Replay And Migration
Contract item 1.

| Case | Archetype | Source document | Source commit (assessment `executionBaseHead`) | Accepted historical disposition |
| --- | --- | --- | --- | --- |
| H1 | A1 new upstream corpus | R2G A1 worksheet, citing `docs/audits/CVF_EAIC_KR_R1_CVF_23_07_EXTERNAL_REPOSITORY_INTAKE_AUDIT_2026-07-23.md` | R2G `c18f6907f1ccee5e9f459611de780dbfc126c561`; R3 confirms via `cdb18064ace9e92e3936640a0fdb6fe5e050116e` | `COMPLETE_VERIFIED` corpus verdict; 231 files (18 Conversation-Resilient Governance + 213 Interaction Projection); `PASS` on R2G's A1 acceptance bar |
| H2 | A2 mixed-origin synthesis | R2G A2 worksheet, citing `docs/audits/CVF_RSPB_AI_T0_DUAL_CORPUS_INTAKE_AUDIT_2026-08-15.md` | R2G `c18f6907f1ccee5e9f459611de780dbfc126c561` | `Corpus verdict: COMPLETE_VERIFIED`; 764 files (559 upstream + 205 local proposal); source audit's own top-level disposition is `STOP_COST_EXCEEDS_VALUE`, superseded in decision framing per its own Supersession Notice (`SUPERSEDED_IN_DECISION_BY_MODS_T0_CORRECTION`), which this replay preserves verbatim and does not re-litigate |
| H3 | A3 accepted-corpus cluster | R2G A3 worksheet, citing `docs/reviews/CVF_RSPB_AI_T11_CAPABILITY_WORKSPACE_PROFILE_AND_BOOTSTRAP_POLICY_BUNDLE_VALIDATION_KERNEL_COMPLETION_2026-08-17.md` (T7/T11 named-cluster cycle) | R2G `c18f6907f1ccee5e9f459611de780dbfc126c561` | `REVIEWER_ACCEPTED_PENDING_CLOSER` per R2G's own Tertiary Risk disclosure; T11 review-cost telemetry `reviewRoundCount: 1`, `latencyDisposition: WITHIN_FAST_PATH_TARGET` |
| H4 | A4 upstream delta | R2G A4 worksheet, citing `docs/audits/CVF_PPMCP_R1_PINNED_UPSTREAM_AND_LEGACY_DELTA_REINTAKE_2026-07-25.md` | R2G `c18f6907f1ccee5e9f459611de780dbfc126c561` | 107-file re-intake (98 upstream + 9 legacy); aggregate manifest digest `7deb1ef3b1...`; `DELTA_RECONCILED` narrowed claim; direct import rejected for all 24 tool implementations |
| H5 | A5 advisory item | R2G A5 worksheet, citing `docs/reviews/CVF_TPGR_SECOND_UPGRADE_GENERALIZATION_EXTERNAL_CRITIQUE_2026-08-17.md`; reconciled critique chain via `docs/reviews/CVF_TPGR_SECOND_UPGRADE_GENERALIZATION_CRITIQUE_RECONCILIATION_AND_R2_RESCOPE_2026-08-17.md` | R2G `c18f6907f1ccee5e9f459611de780dbfc126c561` | `ADVISORY_INPUT_PENDING_RECONCILIATION`, never CVF authority by itself; reconciled into R2G/R3/R4/R5 as design input only |
| H6 | A6 downstream project source | R2G A6 worksheet, citing GC-051 Rule 5 (`docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md`) and `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | R2G `c18f6907f1ccee5e9f459611de780dbfc126c561` | `CORPUS_REGISTERED` for project scope path only, explicitly not a CVF-authority promotion claim; 37 `PROJECT_SOURCE` entries recomputed by R2G |

All six rows are verifiable from the two named predecessor assessments
(R2G's A1-A6 worksheets and R3's A1-A6 Threshold Worksheets) plus the R2G/R3
worker returns' Independent Reviewer Addenda that independently confirmed
this same evidence. No named historical fixture in this inventory required
invention; none is blocked.

## H1-H6 Replay Worksheets

Each worksheet independently derives `observedShadowRoute` from R3's Route
Outcomes precedence and R4/R5's field rules applied to the objective facts in
the cited worksheet, then compares it against the predecessor's own recorded
route outcome (`expectedRoute`) and the archetype's historical disposition.

### H1 - A1 new upstream corpus

| Field | Value |
| --- | --- |
| replayCaseId | H1 |
| fixtureClass | A1_NEW_UPSTREAM_CORPUS |
| Historical outcome | `COMPLETE_VERIFIED`; full first-intake floor (GC-051 registration, C1 structural enumeration, C2 ledger reconciliation, blind-spot Gates 1-3) applied to 231 files; zero inheritance claimed |
| Objective facts | dual source (pinned mirror plus copied legacy folder), no prior GC-051 registry row, full manifest and two terminal file ledgers present |
| Inherited/refreshed evidence | none inherited (A1 is the no-inheritance case by design); all evidence freshly produced in the source audit |
| expectedRoute (R3 worksheet's own stated route outcome) | `FULL_LAYER_A_REQUIRED` |
| observedShadowRoute (independently derived) | `FULL_LAYER_A_REQUIRED` - applying R3 Rule 1 (no prior receipt exists, so no lighter route is reachable regardless of file count) and R3's A1 Divergence Tolerance (zero tolerance; any missing manifest/ledger row forces the full route) to the objective facts above yields the same outcome as R3's own worksheet |
| Mismatches | none between `expectedRoute` and `observedShadowRoute`; none between either route value and the historical `COMPLETE_VERIFIED` disposition, since `COMPLETE_VERIFIED` is a Layer A corpus verdict, not itself a TPGR route token, and `FULL_LAYER_A_REQUIRED` is exactly the route this design would assign to any input needing that verdict |
| Layer A cost | full 231-file enumeration/hash/ledger; unavoidable per R2G and R3, never counted as TPGR savings |
| TPGR comparison overhead | one classification manifest plus one routing receipt (PROJECTED; no live TPGR receipt exists for H1) |
| Escalation cost | N/A; H1 does not escalate, it routes directly to `FULL_LAYER_A_REQUIRED` as its default posture |
| Replay verdict | PASS - the design correctly preserves the full first-intake floor and claims no inheritance saving for A1, matching the work order's required posture for H1 |

### H2 - A2 mixed-origin synthesis

| Field | Value |
| --- | --- |
| replayCaseId | H2 |
| fixtureClass | A2_MIXED_ORIGIN_SYNTHESIS |
| Historical outcome | `Corpus verdict: COMPLETE_VERIFIED` for the 764-file dual corpus; dual-manifest separation control verified (upstream never cited as proof of proposal claims); adversarial full-read of four highest-risk safety-bypass files; the source audit's own top-level value/cost disposition is `STOP_COST_EXCEEDS_VALUE`/superseded, preserved verbatim, not re-litigated here |
| Objective facts | 559-file pinned upstream mirror plus 205-file local proposal folder; `.private_reference/legacy/` classification retained; zero `ADAPTED` rows promoting proposal material to CVF source |
| Inherited/refreshed evidence | manifest/ledger hashes (upstream `74ef4330d0...`; proposal `c51ed5055e...`) are available for reuse by a later cluster review without re-enumeration; the adversarial-sample evidence itself is not re-inheritable without fresh re-verification |
| expectedRoute (R3 worksheet's own stated route outcome) | `FULL_LAYER_A_REQUIRED` until reusable receipts and owner mapping are current; may relax only for a later named-cluster reuse subcase that itself resolves to an A3-shaped K1 entry |
| observedShadowRoute (independently derived) | `FULL_LAYER_A_REQUIRED` - applying R3 Rule 2 (missing/contradictory owner facts cannot select `LIGHT_ROUTE_ALLOWED`) and R3's A2 Divergence Tolerance (zero tolerance on origin-separation controls) to the dual-origin, no-prior-receipt facts above yields the same outcome as R3's own worksheet; dual-origin separation and selected-cluster semantic reading are preserved, matching the work order's required H2 posture |
| Mismatches | none between `expectedRoute` and `observedShadowRoute`; none against the historical `COMPLETE_VERIFIED` ledger-completeness verdict, since that verdict licenses `STRUCTURALLY_ENUMERATED`/`LEDGER_DISPOSITIONED` claims only, never `CLUSTER_SEMANTICALLY_READ` for the full corpus, consistent with R4's forbidden-implication column for those tokens |
| Layer A cost | full 764-file enumeration/hashing/ledger plus adversarial full-reads of four highest-risk files and two self-declaring foundation files; unavoidable, never counted as TPGR savings |
| TPGR comparison overhead | one classification manifest (PROJECTED; no live TPGR receipt exists for H2) |
| Escalation cost | N/A for the base route; a later named-cluster reuse subcase would separately incur A3-shaped escalation cost, not measured here |
| Replay verdict | PASS - dual-origin separation and selected-cluster semantic reading are preserved; the work order's required H2 posture is met and the source audit's own supersession framing is preserved without being overridden |

### H3 - A3 accepted-corpus cluster

| Field | Value |
| --- | --- |
| replayCaseId | H3 |
| fixtureClass | A3_ACCEPTED_CORPUS_CLUSTER |
| Historical outcome | `REVIEWER_ACCEPTED_PENDING_CLOSER` for the T11 named-cluster completion review; review-cost telemetry `reviewRoundCount: 1`, `latencyDisposition: WITHIN_FAST_PATH_TARGET`; no full-corpus re-enumeration performed |
| Objective facts | seven-file-scale named cluster composed from an already-accepted corpus (T7/T11 pure Guard Contract kernel); K1 entry inherits C0-C2 from the corpus's existing accepted receipts |
| Inherited/refreshed evidence | T7 owner projection and prior accepted contract surface inherited unchanged; only the new T11 file set (bundle validator module, focused test file, two barrel exports, one hash-only system-chain map refresh) was fresh |
| expectedRoute (R3 worksheet's own stated route outcome) | `LIGHT_ROUTE_ALLOWED` only with current accepted receipts and exact named scope; `ESCALATE_FOR_REVIEW` on any owner/hash/freshness ambiguity |
| observedShadowRoute (independently derived) | `ESCALATE_FOR_REVIEW` - the exact named scope is evidenced, but the cited completion review remains `REVIEWER_ACCEPTED_PENDING_CLOSER` and this replay did not reconstruct the full identity-bound C0-C2 currency chain required by R5. R3 selects escalation on any owner/hash/freshness ambiguity; a condition that still requires future verification cannot select the light route now. |
| Mismatches | disclosed strict-route divergence: R3's worksheet permits `LIGHT_ROUTE_ALLOWED` only after current accepted receipts and exact scope are both proven. Exact scope is present, but current receipt identity is not. The observed replay therefore takes the worksheet's explicit `ESCALATE_FOR_REVIEW` branch. This preserves the historical bounded-reuse evidence without laundering it into current route eligibility. |
| Layer A cost | the underlying corpus's own C0-C2 floor, already paid once; zero re-enumeration of the full corpus for the T11 cluster |
| TPGR comparison overhead | near-zero marginal cost (PROJECTED; no live TPGR receipt exists for H3); this is the one required positive bounded case per the work order |
| Escalation cost | UNKNOWN/PROJECTED for the current replay: independent reconstruction of the identity-bound receipt chain is still required and was not measured. The source review's one bounded repair round remains Layer A review cost, not TPGR escalation cost. |
| Replay verdict | PASS_WITH_DISCLOSED_STRICT_ROUTE - H3 proves the historical bounded-reuse value without repeating full-corpus enumeration or inheriting semantic understanding of a new cluster, while current eligibility fails closed to `ESCALATE_FOR_REVIEW` until receipt freshness and identity are independently re-earned. |

### H4 - A4 upstream delta

| Field | Value |
| --- | --- |
| replayCaseId | H4 |
| fixtureClass | A4_UPSTREAM_DELTA |
| Historical outcome | `DELTA_RECONCILED`; aggregate manifest digest independently recomputed and matched exactly (`7deb1ef3b1...`); delta ledger separates `UNCHANGED_FROM_INTAKE`, `CHANGED_DISPOSITION`, `NEW_FINDING`, `REMOVED_OR_REJECTED`; direct import rejected for all 24 tool implementations |
| Objective facts | 107-file bounded re-intake (98-file pinned-upstream mirror plus 9 retained legacy interpretation files) compared against a prior `PARTIALLY_ABSORBED` disposition trail; all 107 files read in full, no sampling |
| Inherited/refreshed evidence | 6 of 9 legacy files inherited unchanged disposition (`CONFIRMED_EXISTING`); 2 legacy files required fresh comparison due to real narrow deltas; the entire 98-file upstream mirror was freshly compared since it had never been compared before (0% inherited for that portion) |
| expectedRoute (R3 worksheet's own stated route outcome) | `FULL_LAYER_A_REQUIRED` for the affected delta scope; D1 node licenses only `DELTA_RECONCILED`, never a broader claim |
| observedShadowRoute (independently derived) | `FULL_LAYER_A_REQUIRED` for the affected delta scope - applying R3 Rule 5 (cost thresholds cannot omit required semantic reading) and R5's Invalidation Precedence level 1 (source-identity change invalidates independent of file-hash stability) to the upstream-commit-change fact yields the same outcome as R3's own worksheet; the earliest-affected-node principle (re-deriving which sub-claims are `UNCHANGED_FROM_INTAKE` from the actual current owner surface, not from memory of the prior closure) is preserved |
| Mismatches | none between `expectedRoute` and `observedShadowRoute`; none against the historical `DELTA_RECONCILED` disposition, since that token is the D1 ceiling claim this design's route also converges on for the reconciled scope |
| Layer A cost | full 107-file re-read plus field-by-field comparison against the actual current owner surface (not stale documentation); unavoidable, never counted as TPGR savings |
| TPGR comparison overhead | one delta-reconciliation classification (PROJECTED; no live TPGR receipt exists for H4) |
| Escalation cost | N/A; H4 routes directly to `FULL_LAYER_A_REQUIRED` for the affected scope as its default posture, with the 6-of-9 already-settled legacy sub-claims correctly not re-litigated |
| Replay verdict | PASS - delta-scope re-read and earliest-node invalidation are preserved; the work order's required H4 posture is met |

### H5 - A5 advisory item

| Field | Value |
| --- | --- |
| replayCaseId | H5 |
| fixtureClass | A5_ADVISORY_ITEM |
| Historical outcome | `ADVISORY_INPUT_PENDING_RECONCILIATION`; explicit Claim Boundary in the source critique states it must not be cited as canonical authority in Source Authority tables, Source Verification ACCEPT rows, corpus manifests, closure proof, or roadmap/work-order evidence; reconciled through R2G/R3/R4/R5 as design input only, never promoted to CVF authority by itself |
| Objective facts | one named operator-provided external critique document, not a corpus; explicit `Input type` canonical token (`operator-provided external comparison, critique, or recommendation`); `Rescan Intelligence Hardening: NOT_APPLICABLE_WITH_REASON`; `Corpus Completeness And Report Integrity: NOT_APPLICABLE_WITH_REASON` |
| Inherited/refreshed evidence | none required; the document was read directly and dispositioned without GC-051 registration, consistent with the Conditional Lifecycle Route Graph's stated exception for non-reusable small named inputs |
| expectedRoute (R3 worksheet's own stated route outcome) | `ESCALATE_FOR_REVIEW` on any authority or reuse ambiguity (work order default); otherwise the cheapest legitimate `LIGHT_ROUTE_ALLOWED` case in the R3 matrix |
| observedShadowRoute (independently derived) | `ESCALATE_FOR_REVIEW` - because H5's fixture is itself the external critique whose authority status was, by design, ambiguous until independently reconciled by R2G/R3/R4/R5; applying R3's Anti-Self-Downgrade Invariant (file count cannot override authority impact) to a single-document input whose content plausibly reads as proposing CVF authority changes yields escalation, not the lighter route, exactly as R3's own worksheet's Hostile Example already demonstrates for this same fixture |
| Mismatches | none between `expectedRoute` and `observedShadowRoute`; this is the intended fail-closed behavior R3's own worksheet documents for its own primary evidence, not a defect |
| Layer A cost | minimal: one document read, source-verified against named canonical standards; no corpus-scale ceremony invoked |
| TPGR comparison overhead | effectively zero beyond the existing External Knowledge Intake Routing table already required by the chain map |
| Escalation cost | one reconciliation cycle (already completed and closed via the R2G reconciliation review); not separately re-measured by this replay |
| Replay verdict | PASS - the advisory authority boundary is preserved with near-zero extra ceremony beyond the mandatory escalation itself, matching the work order's required H5 posture |

### H6 - A6 downstream project source

| Field | Value |
| --- | --- |
| replayCaseId | H6 |
| fixtureClass | A6_DOWNSTREAM_PROJECT_SOURCE |
| Historical outcome | `CORPUS_REGISTERED` for the project scope path only; GC-051 Rule 5 explicitly separates registration from authority promotion; 37 `PROJECT_SOURCE` entries independently recomputed by R2G via direct JSON parse of the current generated registry |
| Objective facts | project-owned source trees registered as `PROJECT_SOURCE` corpus-type entries; each entry carries its own `scopePaths`; project findings are cross-referenced against CVF framework findings, not merged into CVF authority |
| Inherited/refreshed evidence | scope-path inheritance across repeated project reads under the same registered entry; the registry does not currently express automatic drift detection for project sources as a distinct rule |
| expectedRoute (R3 worksheet's own stated route outcome) | `FULL_LAYER_A_REQUIRED` when project corpus scanning is claimed; registration-before-scan is mandatory exactly as for any other corpus type, with no lighter-weight rule |
| observedShadowRoute (independently derived) | `FULL_LAYER_A_REQUIRED` - applying R3's A6 zero-tolerance authority-promotion boundary and R4 Hostile Case 9 (project source cited as CVF authority routes to `FULL_LAYER_A_REQUIRED`, citation void) to the objective facts above yields the same outcome as R3's own worksheet; registration never promotes project material to CVF authority under this replay |
| Mismatches | none between `expectedRoute` and `observedShadowRoute`; none against the historical `CORPUS_REGISTERED` disposition |
| Layer A cost | one registry entry per project scope; unavoidable minimum already in force |
| TPGR comparison overhead | none identified beyond the same routing receipt every other corpus-type entry would receive |
| Escalation cost | N/A for a clean registration-before-scan case; a hostile authority-promotion attempt would separately escalate, evaluated below in the Seeded Defect Matrix |
| Replay verdict | PASS - registration never promotes project material to CVF authority; the work order's required H6 posture is met and no schema change is proposed |

## Historical Fixture Coverage Summary

6/6 historical fixtures replayed. Five select their predecessor's direct
route token; H3 selects the predecessor worksheet's explicit strict branch,
`ESCALATE_FOR_REVIEW`, because current receipt identity was not proven. This
route divergence is disclosed and preserves the historical A3 reuse evidence
without converting it into current light-route eligibility. No historical
outcome was rewritten; H2's source-level `STOP_COST_EXCEEDS_VALUE`/
superseded framing is preserved verbatim, not overridden.

## Seeded-Defect Matrix (Twelve R5 Hostile Cases)

All twelve R5 hostile cases are seeded and resolved without modifying any
source file, per the work order's Required Seeded Defect And Negative Cases
section. Each row states the expected detection, the actual shadow
determination this replay independently derives, the route, preserved
historical evidence, invalidation scope, and pass/fail. Case numbering
matches the R5 assessment's own Hostile Cases table exactly.

| # | Seeded scenario (from R5) | Expected detection | Actual shadow determination | Route | Preserved evidence | Invalidation scope | Pass/Fail |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | a worker marks a costly command `NOT_APPLICABLE_WITH_REASON` to obtain a lighter route | worker-authored disposition treated as `WORKER_PROPOSES` only | detected: the disposition is discarded as a route input per R3's `WORKER_PROPOSES, OWNER_CONFIRMS` pattern | `ESCALATE_FOR_REVIEW` | worker's proposed reason retained for reviewer diagnosis, licenses no route | none beyond the single record | PASS |
| 2 | a checker changes semantics but filename/command row stay stable | semantic dependency closure re-compared, not just path | detected: `receiptOwnerRef`'s checker semantic-dependency closure (per R5's Identity-Binding Contract) is re-derived and found mismatched | `FULL_LAYER_A_REQUIRED` for every claim depending on that closure | pre-change evidence preserved as `historicalDisposition` | scoped to claims whose evidence depended on the specific checker | PASS |
| 3 | a catalog row is removed while an old receipt still cites it | command-catalog membership re-checked at claim-verification time | detected: the stable row key no longer exists in the current catalog | `FULL_LAYER_A_REQUIRED` for the affected claim | old receipt's `historicalDisposition` preserved as immutable evidence | scoped to the specific claim citing the removed row | PASS |
| 4 | upstream identity changes while selected file hashes stay stable | identity-drift detection independent of file-hash comparison | detected: R5 Invalidation Precedence level 1 fires on pinned-identity change alone | `FULL_LAYER_A_REQUIRED` for the affected delta scope; `eligibilityState` moves `CURRENT` to `EXPIRED_HISTORICAL` | pre-drift receipts preserved as historical evidence | scoped to the delta scope only | PASS |
| 5 | a bare `NO_NEW_VALUE` ledger label offered as corpus semantic proof | label alone contributes zero to scope-total-equality count | detected: R4's reviewer-repaired corpus semantic proof rule requires current proof of prior review or owner-confirmed exclusion, not a bare label | `ESCALATE_FOR_REVIEW` | the `LEDGER_DISPOSITIONED`-level evidence the label actually supports remains valid at its own stage | scoped to the `CORPUS_SEMANTICALLY_ABSORBED` claim only | PASS |
| 6 | ten cluster receipts aggregated into a corpus claim | No Promotion By Aggregation rule rejects the aggregation | detected: aggregation is never a licensed path to `CORPUS_SEMANTICALLY_ABSORBED` under R4's rule | `ESCALATE_FOR_REVIEW`; aggregated claim rejected outright | the ten underlying `CLUSTER_SEMANTICALLY_READ` receipts remain valid as ten separate scope-bound claims | none beyond the rejected aggregate claim | PASS |
| 7 | a historical archived document containing a claim token triggers current enforcement | archived-path/status exclusion applied per False-Positive Boundary | detected: the document sits under an archived path/status, so its token is not a live claim | preservation of unaffected current state with explicit reason; no enforcement fires | archived document's content remains valid evidence of what it stated when archived | none; explicitly excluded from enforcement | PASS |
| 8 | descriptive prose or a code fence explaining a token is mistaken for an asserted claim | assertion-shaped-structure requirement (populated `claimScopeRef` inside a claim-eligible document) | detected: neither prose nor a code fence carries a populated `claimScopeRef`, so no claim is asserted | preservation of unaffected current state with explicit reason | surrounding document's own actual claims, if any, independently evaluated on their own merits | none; explicitly excluded from enforcement | PASS |
| 9 | a receipt has every field but its review authority changed | confirming review artifact identity re-checked, not just the role label | detected: R5 Invalidation Precedence level 6 fires on the identity-bound confirming review artifact mismatch even though the role label alone still reads as valid | `FULL_LAYER_A_REQUIRED` (or `ESCALATE_FOR_REVIEW` if the change is itself ambiguous); `eligibilityState` moves to `EXPIRED_HISTORICAL` | the receipt's other seven fields remain historical evidence, license no current claim without valid confirming authority | scoped to the specific claim whose confirming review changed | PASS |
| 10 | a stale receipt is copied into a new artifact with a new timestamp | Re-Earning Rule: copying does not re-earn eligibility | detected: the copy inherits `EXPIRED_HISTORICAL` status from its source evidence, the new timestamp is not itself evidence | `FULL_LAYER_A_REQUIRED`, or the pre-existing `EXPIRED_HISTORICAL` state is simply carried forward, never upgraded to `CURRENT` | both original and copy remain historical evidence of what was claimed and when | none beyond the copy itself | PASS |
| 11 | one dependency fact is unknown and the worker declares low uncertainty | Escalation-Only Uncertainty Treatment discards the declaration entirely | detected: the low-uncertainty declaration is discarded, not averaged or partially honored | `ESCALATE_FOR_REVIEW` | any other independently verified fields on the same record remain visible for reviewer diagnosis, license no claim on their own | none beyond the single record | PASS |
| 12 | receipt invalidation cascades beyond the earliest affected scope | Invalidation Precedence "earliest affected node controls" rule bounds `invalidationScope` | detected: `invalidationScope` is bounded to exactly the earliest affected node's own scope, per R5's binding rule | preservation of every unaffected current sub-claim with explicit reason | the affected node's own scope is fully invalidated; everything outside it remains `CURRENT` with explicit reason | scoped to exactly the earliest affected node; not expanded | PASS |

12/12 material seeded-defect cases detected. Zero false negatives. None
selected `LIGHT_ROUTE_ALLOWED`.

## Reviewer-Repair Seeded Cases (Three Additional)

Per the work order's Replay And Migration Contract item 3, three additional
cases seeded beyond the twelve R5 hostile cases: unbound receipt identity,
incorrect phase-cost accounting, and contradictory gate evidence. These
mirror the exact three reviewer-repaired defects independently found and
fixed across the R4 and R5 worker return Independent Reviewer Addenda, now
seeded as forward-looking replay cases against the accepted (post-repair)
design rather than the original pre-repair drafts.

| # | Seeded scenario | Expected detection | Actual shadow determination | Route | Preserved evidence | Invalidation scope | Pass/Fail |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 13 | unbound receipt identity: `receiptOwnerRef` is asserted as a bare path/section pointer with no owner-identity, checker semantic-dependency-closure, catalog-row, or confirming-review-artifact identity attached | R5's Identity-Binding Contract requires the full ordered reference set (owner blob identity, checker semantic dependency closure, stable command-row key plus serialized arguments, confirming review artifact identity), not a bare path | detected: a bare path/section pointer fails the Identity-Binding Contract's explicit requirement that "a bare path match never proves currency"; freshness is unknown when the semantic dependency closure cannot be enumerated | `FULL_LAYER_A_REQUIRED` for the affected claim, per the Identity-Binding Contract's own fail-closed rule | the bare-path receipt is retained as `historicalDisposition` evidence of what was asserted, but licenses no current claim | scoped to the specific claim with the unbound identity | PASS |
| 14 | incorrect phase-cost accounting: a pre-push-only command (for example the local pre-push governance hook chain) is charged as cost against a pre-implementation-phase replay case | R5's reviewer-repaired phase-aware cost boundary: the legacy bundle is explicitly phase-selected, not a blanket union of every phase's command list | detected: `governance/compat/agent_autorun_command_catalog.py`'s `PRE_PUSH_COMMANDS` tuple is disjoint from the common/pre-implementation command tuples; a pre-push-only command charged to a pre-implementation fixture is a phase-boundary violation, independently verifiable by checking which tuple the command's name appears in; the mischarged cost cell is rejected and cost is recomputed using only the common plus pre-implementation command tuples for a pre-implementation-phase claim | N/A (this is a cost-accounting correction, not an eligibility route); if presented as claim evidence, the mischarged cost cell routes the surrounding claim to `ESCALATE_FOR_REVIEW` under R3 Rule 5 (cost thresholds cannot omit or misstate required evidence) | the corrected cost cell is recorded; the mischarged original cell is disclosed as a seeded-case artifact, not silently dropped | scoped to the single mischarged cost cell | PASS |
| 15 | contradictory gate evidence: a worker summary states first-pass fast-gate success while the detailed Command Evidence section discloses a first-run FAIL and a second-run PASS | R4/R5's Anti-Self-Downgrade Invariants applied to self-reported summaries: an independently observable command-evidence record controls over a worker's own summary | detected: comparing the summary claim ("first-and-only PASS") against the Command Evidence section's own recorded sequence (FAIL then PASS) surfaces the contradiction directly, exactly as the R5 worker return's own Independent Reviewer Addendum found and repaired for this exact defect class | `ESCALATE_FOR_REVIEW`; the summary is discarded as a route input in favor of the independently observable command-evidence record | both the (corrected) summary and the full command-evidence sequence, including the first-run failure, are preserved and disclosed, never overwritten with a final-only summary | scoped to the specific worker return's own summary/evidence-consistency claim | PASS |

15/15 total material seeded-defect cases (twelve R5 hostile plus three
reviewer-repair) detected. Zero false negatives.

## False-Positive Replay Matrix (Six Classes)

Per R5's own False-Positive Boundary section and the work order's Replay And
Migration Contract item 4, each of the six declared false-positive classes is
replayed against a concrete illustrative instance and confirmed to raise zero
enforcement activation.

| Class | Illustrative instance replayed | Expected activation | Observed activation | Pass/Fail |
| --- | --- | --- | --- | --- |
| descriptive prose | a sentence in this design's own Exact Historical Fixture Inventory section explaining what `COMPLETE_VERIFIED` means, without a populated `claimScopeRef` binding it to a specific record | zero (definition, not a claim) | zero; no populated `claimScopeRef` accompanies any bare mention of the token in prose throughout this document | PASS |
| taxonomy tables | this design's own Seeded-Defect Matrix and False-Positive Replay Matrix tables, whose row labels use scenario/class names as row keys, not as populated claim records | zero (taxonomy, not assertion) | zero; every table in this document uses the token/class name as a row label or column value describing a scenario, never as a `claimToken:`-shaped field inside a populated claim record | PASS |
| archived history | the R2G assessment's own citation of `docs/audits/CVF_RSPB_AI_T0_DUAL_CORPUS_INTAKE_AUDIT_2026-08-15.md`, whose own status carries `SUPERSEDED_IN_DECISION_BY_MODS_T0_CORRECTION` | zero (archived/superseded status excludes current enforcement) | zero; this replay's H2 worksheet explicitly preserves the superseded framing as historical evidence without treating it as a live current claim | PASS |
| code fences | the literal-format gotchas reference's own illustrative code-fence examples (for example gotcha 23's illustrated field-name prose), referenced but not reproduced as a live claim in this document | zero (illustrative syntax, not assertion) | zero; this document contains no fenced code block asserting a `claimToken` against a populated `claimScopeRef` | PASS |
| quoted examples | R3's own worksheet Hostile Example rows (for example A1's "a worker claims `LIGHT_ROUTE_ALLOWED` for a small first-intake corpus" example), quoted by reference in this design's H1-H5 worksheets as illustrative framing | zero (hypothetical framing marks the token as illustrative) | zero; every quoted hostile-example reference in this document is explicitly framed as an illustration of a rule, not as a live claim about this document's own subject matter | PASS |
| incomplete draft artifacts | a hypothetical draft work order whose `Status:` field reads `DRAFT` and whose prose happens to contain a claim-token name | zero (non-claim-eligible status excludes currency) | zero; this replay does not encounter or create any incomplete draft artifact carrying a claim token, and no `DRAFT`/`DISPATCH_READY`-status document is treated as claim-eligible anywhere in this design | PASS |

0/6 declared false-positive classes activated.

## Migration Table (Fourteen Fields, All Six H1-H6 Fixtures)

Per the work order's Replay And Migration Contract item 5, this table covers
all eight R4 fields and all six R5 candidate fields for every one of the six
H1-H6 fixtures. Historical evidence is referenced, never rewritten; no cell
below synthesizes `CURRENT` without genuine identity evidence, per R5's
Identity-Binding Contract and Re-Earning Rule. Migration dispositions use
only the five exact tokens required by the work order:
`MIGRATABLE_CURRENT_WITH_IDENTITY`, `NEEDS_FRESH_EVIDENCE`,
`HISTORICAL_ONLY`, `NOT_APPLICABLE_WITH_REASON`, `BLOCKED_CONTRADICTORY_EVIDENCE`.

Because no R4/R5 field has ever been machine-populated for any of H1-H6 (no
live TPGR receipt has been attached to any archetype through R5), every field
below is evaluated against the identity-binding standard R5 requires: a
`MIGRATABLE_CURRENT_WITH_IDENTITY` disposition is reachable only when the
full R5 Identity-Binding Contract reference set (owner blob identity, checker
semantic-dependency closure, stable command-row identity, confirming review
artifact identity) can be independently reconstructed from the cited source
document today. Where that full reference set cannot be reconstructed from
prose alone (which is the case for every H1-H6 fixture, since none was
authored with R5's identity-binding fields in mind), the disposition is
`NEEDS_FRESH_EVIDENCE`, not a guessed `CURRENT` match, per the work order's
Replay And Migration Contract item 7.

### R4 Fields (Eight)

| R4 field | H1 (A1) | H2 (A2) | H3 (A3) | H4 (A4) | H5 (A5) | H6 (A6) |
| --- | --- | --- | --- | --- | --- | --- |
| `intakeStage` | `NEEDS_FRESH_EVIDENCE` - S0-S2 facts are present in prose (registration, manifest, ledger) but no identity-bound stage receipt exists to migrate as `CURRENT` | `NEEDS_FRESH_EVIDENCE` - same reasoning; S0-S2 facts present, no identity-bound receipt | `NEEDS_FRESH_EVIDENCE` - K1 stage facts present in the T11 completion review, but the review's own status is `REVIEWER_ACCEPTED_PENDING_CLOSER`, not a closed identity-bound receipt | `NEEDS_FRESH_EVIDENCE` - D1/S8 facts present (delta ledger complete), no identity-bound receipt | `HISTORICAL_ONLY` - G0/K1 facts present for a non-reusable small named item; A5's own posture explicitly does not require a corpus-stage receipt, so there is nothing further to migrate beyond the historical record itself | `NEEDS_FRESH_EVIDENCE` - C0 registration fact present in the current live registry (not stale), but no identity-bound intake-stage receipt for this specific replay exists |
| `claimToken` | `HISTORICAL_ONLY` - the source audit's `COMPLETE_VERIFIED` verdict maps to `STRUCTURALLY_ENUMERATED`/`LEDGER_DISPOSITIONED` per R4's token table, but this design does not synthesize a live `claimToken` assertion the source document never made | `HISTORICAL_ONLY` - same reasoning; the audit's own status (`SUPERSEDED_IN_DECISION_BY_MODS_T0_CORRECTION`) additionally forecloses treating any token here as current | `NEEDS_FRESH_EVIDENCE` - `CLUSTER_SEMANTICALLY_READ` is the token the T11 review's evidence would support, but the review's `REVIEWER_ACCEPTED_PENDING_CLOSER` status means the confirming-review identity leg of R5's Identity-Binding Contract is not yet closed | `HISTORICAL_ONLY` - `DELTA_ACCOUNTED` is the token the audit's evidence supports as a historical fact; no live claim is asserted by this design | `HISTORICAL_ONLY` - no claim token applies; A5 items do not carry a corpus-semantic claim token under R4's vocabulary | `HISTORICAL_ONLY` - `SOURCE_REGISTERED` is the token the registry entry's evidence supports as a historical/current registration fact, but registration alone is not promoted to any higher-stage token here |
| `claimScopeRef` | `HISTORICAL_ONLY` - 231 files exactly enumerated in the source audit's own manifest; the scope reference itself is a stable historical fact, reusable as a citation, not as a live migrated claim | `HISTORICAL_ONLY` - 764 files exactly enumerated (559 + 205); same reasoning | `HISTORICAL_ONLY` - the exact named seven-file-scale T11 cluster list is stable and citable | `HISTORICAL_ONLY` - 107 files exactly enumerated (98 + 9); same reasoning | `HISTORICAL_ONLY` - one named document; scope is trivially exact | `HISTORICAL_ONLY` - the registered `scopePaths` entry is the stable scope reference |
| `evidenceRefs` | `HISTORICAL_ONLY` - the source audit path itself is the evidence reference; it exists and is citable today | `HISTORICAL_ONLY` - same reasoning, plus the audit's own supersession notice must be cited alongside it, never omitted | `NEEDS_FRESH_EVIDENCE` - the T11 completion review exists and is citable, but its own pending-closer status means a downstream evidenceRef citing it as final proof would itself be provisional | `HISTORICAL_ONLY` - the source audit path is citable and current | `HISTORICAL_ONLY` - the critique document and its reconciliation review are both citable | `HISTORICAL_ONLY` - the registry JSON path and the specific entry are citable |
| `invalidatedBy` | `NEEDS_FRESH_EVIDENCE` - R3's Dependency Invalidation Graph node (GC-051/core-standard row) must be independently re-run against current repository state at migration time, not inherited from R2G's original read | `NEEDS_FRESH_EVIDENCE` - same reasoning, plus the mixed-origin standard's own row | `NEEDS_FRESH_EVIDENCE` - the underlying corpus's own upstream C0-C2 receipts must be traced fresh per R3's graph, since T7/T11 receipt currency is exactly the kind of fact that expires from the earliest affected node, not a static historical property | `NEEDS_FRESH_EVIDENCE` - the specific CVF owner surface the delta was compared against must be re-diffed fresh at migration time, per R3's A4 "actual current owner surface, not a cached copy" rule | `NEEDS_FRESH_EVIDENCE` - the chain map's own `Input type` enum and checker must be re-checked fresh | `NEEDS_FRESH_EVIDENCE` - GC-051 Rule 5 text and the `PROJECT_SOURCE` schema must be re-checked fresh |
| `reviewAuthority` | `NEEDS_FRESH_EVIDENCE` - no explicit `reviewer/closer` role-confirmation record was captured in R4-field shape for the original A1 audit; the role can be inferred from the audit's own review history but not migrated as an identity-bound R5-shaped confirming-review-artifact reference without fresh construction | `NEEDS_FRESH_EVIDENCE` - same reasoning | `NEEDS_FRESH_EVIDENCE` - the T11 review's own reviewer role is named in its completion review, but its `REVIEWER_ACCEPTED_PENDING_CLOSER` status means the closer confirmation leg is not yet closed | `NEEDS_FRESH_EVIDENCE` - same reasoning as H1 | `NEEDS_FRESH_EVIDENCE` - the reconciliation review names a reviewer role, but not in R5's identity-bound confirming-review-artifact shape | `NEEDS_FRESH_EVIDENCE` - same reasoning |
| `routeOutcome` | `HISTORICAL_ONLY` - this replay's own H1 worksheet independently computed `FULL_LAYER_A_REQUIRED`; that computed value is itself new evidence produced by this R6 design, not a migrated historical fact, and is recorded in the worksheet above, not re-asserted here as a migrated field | `HISTORICAL_ONLY` - same reasoning, referencing the H2 worksheet | `HISTORICAL_ONLY` - same reasoning, referencing the H3 worksheet, with the freshness condition disclosed | `HISTORICAL_ONLY` - same reasoning, referencing the H4 worksheet | `HISTORICAL_ONLY` - same reasoning, referencing the H5 worksheet | `HISTORICAL_ONLY` - same reasoning, referencing the H6 worksheet |
| `eligibilityState` | `NOT_APPLICABLE_WITH_REASON` - no R4-shaped record has ever existed for H1 to carry an `eligibilityState`; there is nothing to migrate a state for, only a route to newly derive (done above) | `NOT_APPLICABLE_WITH_REASON` - same reasoning | `NOT_APPLICABLE_WITH_REASON` - same reasoning | `NOT_APPLICABLE_WITH_REASON` - same reasoning | `NOT_APPLICABLE_WITH_REASON` - same reasoning | `NOT_APPLICABLE_WITH_REASON` - same reasoning |

### R5 Candidate Fields (Six)

| R5 field | H1 (A1) | H2 (A2) | H3 (A3) | H4 (A4) | H5 (A5) | H6 (A6) |
| --- | --- | --- | --- | --- | --- | --- |
| `commandApplicability` | `HISTORICAL_ONLY` - R5's own applicability matrix already classifies the relevant catalog owners for A1-shaped `intakeStage`/`claimToken` rows as `CONDITIONAL`; that classification is a static design fact reusable by citation, not a per-fixture migrated state | `HISTORICAL_ONLY` - same reasoning for A2-shaped rows | `HISTORICAL_ONLY` - same reasoning for A3-shaped `CLUSTER_SEMANTICALLY_READ` row | `HISTORICAL_ONLY` - same reasoning for A4-shaped `DELTA_ACCOUNTED` row | `HISTORICAL_ONLY` - same reasoning; A5 activates minimal applicability rows per R5's own matrix | `HISTORICAL_ONLY` - same reasoning for A6-shaped `SOURCE_REGISTERED` row |
| `receiptOwnerRef` | `NEEDS_FRESH_EVIDENCE` - the full R5 Identity-Binding Contract reference set (owner blob identity, checker semantic-dependency closure, stable command-row identity, confirming review artifact identity) cannot be reconstructed from the H1 source audit's prose alone; a bare path citation is explicitly insufficient per R5's own rule | `NEEDS_FRESH_EVIDENCE` - same reasoning | `NEEDS_FRESH_EVIDENCE` - same reasoning, compounded by the pending-closer status | `NEEDS_FRESH_EVIDENCE` - same reasoning | `NEEDS_FRESH_EVIDENCE` - same reasoning | `NEEDS_FRESH_EVIDENCE` - same reasoning |
| `invalidationEvent` | `NOT_APPLICABLE_WITH_REASON` - no invalidation has fired for H1's evidence as of this replay's executionBaseHead; there is no event to migrate | `NOT_APPLICABLE_WITH_REASON` - same reasoning | `NOT_APPLICABLE_WITH_REASON` - same reasoning | `NOT_APPLICABLE_WITH_REASON` - same reasoning; the delta itself was the reconciliation of a prior invalidation, already closed by the D1 disposition | `NOT_APPLICABLE_WITH_REASON` - same reasoning | `NOT_APPLICABLE_WITH_REASON` - same reasoning |
| `invalidationScope` | `NOT_APPLICABLE_WITH_REASON` - no invalidation event exists to scope | `NOT_APPLICABLE_WITH_REASON` - same reasoning | `NOT_APPLICABLE_WITH_REASON` - same reasoning | `NOT_APPLICABLE_WITH_REASON` - same reasoning | `NOT_APPLICABLE_WITH_REASON` - same reasoning | `NOT_APPLICABLE_WITH_REASON` - same reasoning |
| `recomputeFromNode` | `NOT_APPLICABLE_WITH_REASON` - no expired eligibility exists to re-earn from a node | `NOT_APPLICABLE_WITH_REASON` - same reasoning | `NOT_APPLICABLE_WITH_REASON` - same reasoning | `NOT_APPLICABLE_WITH_REASON` - same reasoning | `NOT_APPLICABLE_WITH_REASON` - same reasoning | `NOT_APPLICABLE_WITH_REASON` - same reasoning |
| `historicalDisposition` | `HISTORICAL_ONLY` - the source audit's own recorded `COMPLETE_VERIFIED` verdict and file counts are preserved verbatim as the immutable historical record; this replay cites, never rewrites, that record | `HISTORICAL_ONLY` - the source audit's own recorded verdict, counts, and supersession notice are preserved verbatim | `HISTORICAL_ONLY` - the T11 completion review's own recorded verdict and pending-closer status are preserved verbatim | `HISTORICAL_ONLY` - the source audit's own recorded delta ledger and rejection of direct import are preserved verbatim | `HISTORICAL_ONLY` - the critique's own recorded advisory disposition is preserved verbatim | `HISTORICAL_ONLY` - the registry's own recorded entry count and type distribution are preserved verbatim |

No cell in either table asserts `MIGRATABLE_CURRENT_WITH_IDENTITY` for any
of the six fixtures, because none of H1-H6 was ever authored with R5's
identity-binding fields in mind, and inventing that identity now would
violate the work order's explicit prohibition on migration-created `CURRENT`
claims without genuine identity evidence. This is disclosed as an honest
finding, not smoothed over: the migration design is proven fail-closed on
this exact axis (zero synthesized `CURRENT` claims), which is precisely the
acceptance threshold the work order sets, not a gap in this design's
completeness.

R4 fields reconciled: 8/8 (every field has an explicit disposition for every
fixture). R5 candidate fields reconciled: 6/6 (same). 14/14 fields x 6
fixtures = 84/84 cells populated, zero blank.

## A3 Bounded Reuse Demonstration

Per the work order's Replay And Migration Contract item 9, H3's replay
worksheet above demonstrates bounded receipt reuse: the T11 named-cluster
review inherited the T7 owner projection and prior accepted contract surface
unchanged, re-reading only the seven-file-scale named scope (bundle validator
module, its focused test file, contracts barrel export, root barrel export,
one hash-only system-chain map refresh) rather than re-enumerating the full
underlying corpus. Zero full-corpus enumeration was repeated. Zero semantic
understanding of a "new cluster" was inherited without fresh reading - only
the exact named T11 file set was freshly read; every fact about files outside
that named set was cited from the corpus's own existing accepted receipts,
never assumed. The one disclosed condition (H3's `REVIEWER_ACCEPTED_PENDING_
CLOSER` status) does not weaken this demonstration; it is exactly the kind of
honest freshness disclosure R5's Re-Earning Rule requires rather than a
silent assumption of currency.

## Cost Accounting (Layer A Versus TPGR Versus Escalation Versus Identity-Comparison)

| Cost category | H1 | H2 | H3 | H4 | H5 | H6 |
| --- | --- | --- | --- | --- | --- | --- |
| Layer A evidence cost (never counted as TPGR savings) | OBSERVED: full 231-file enumeration/hash/ledger | OBSERVED: full 764-file enumeration/hash/ledger plus adversarial full-reads | OBSERVED: the underlying corpus's own C0-C2 floor, already paid once; zero full-corpus re-enumeration for T11 | OBSERVED: full 107-file re-read plus field-by-field live-surface comparison | OBSERVED: one document read plus source-verification against named standards | OBSERVED: one registry entry per project scope |
| TPGR comparison overhead | PROJECTED: one classification manifest plus one routing receipt; no live receipt exists | PROJECTED: one classification manifest; no live receipt exists | PROJECTED: near-zero marginal cost; no live receipt exists | PROJECTED: one delta-reconciliation classification; no live receipt exists | PROJECTED: near-zero, already the cheapest route without TPGR | PROJECTED: none beyond the existing routing receipt every corpus-type entry would receive |
| Escalation cost | N/A (direct route, no escalation) | N/A (direct route, no escalation) | UNKNOWN/PROJECTED: escalation would fire only if a freshness check failed; not measured because no live check has run | N/A (direct route, no escalation) | OBSERVED: one reconciliation cycle, already completed via the R2G reconciliation review | N/A (direct route for a clean case); UNKNOWN/PROJECTED for an authority-promotion-attempt case (see Seeded Defect Matrix H6-adjacent reasoning) |
| `identityComparisonCost` (R5's own required cost field) | UNKNOWN/PROJECTED: no live `receiptOwnerRef` identity comparison has ever been performed for H1; per R5's own Cost Proof section, "R5 has no live receipt telemetry, so the marginal identity-comparison cost is UNKNOWN/PROJECTED," which this replay reuses unchanged rather than inventing a number | UNKNOWN/PROJECTED: same reasoning | UNKNOWN/PROJECTED: same reasoning; this is the archetype where identity comparison matters most (freshness of the underlying corpus receipts) and is exactly the unmeasured cost this replay must not hide | UNKNOWN/PROJECTED: same reasoning | UNKNOWN/PROJECTED: same reasoning | UNKNOWN/PROJECTED: same reasoning |
| Full legacy autorun bundle | ALWAYS mandatory per TPGR-T0's Legacy Full-Gate Interlock, regardless of any route above; not reduced by this replay for any fixture | same | same | same | same | same |

Every UNKNOWN/PROJECTED cell above is labeled as such and not treated as a
saving. No cell in this table counts unavoidable Layer A evidence toward
TPGR savings. No cell charges a phase-inapplicable command (for example a
`PRE_PUSH_COMMANDS` entry) against a pre-implementation-phase fixture; this
directly resolves Seeded Case 14 above by construction, not merely by
detection.

## Zero-Edit R7 Candidate Manifest

Per the work order's Replay And Migration Contract item 10, the following
paths and sections are named as exact candidate targets for a future R7+
tranche only. None is edited, drafted, or scaffolded by this design.

| Candidate path | Candidate change | Justifying evidence | Authorization state |
| --- | --- | --- | --- |
| a new `governance/compat/check_shadow_replay_migration.py` (candidate name only; file does not exist) | machine-check the migration-table disposition rules (five exact tokens, zero synthesized `CURRENT`) against any future governed artifact that asserts a migration row | Migration Table section above | UNAUTHORIZED; R7+ must specify exact detection regexes and false-positive controls before any checker is drafted, exactly as R5's own R6 Candidate Manifest already flagged the sibling command-applicability/receipt-invalidation checkers for this same treatment |
| `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md` | evaluate (not adopt) whether a "Dual-Run Canary Reference" section should be added, naming this R6 replay's H1-H6 coverage and the migration table's field/token reconciliation by reference, for a future R7 dual-run advisory comparison | this design's H1-H6 Replay Worksheets and Migration Table sections | UNAUTHORIZED; requires R7+ and independent review |
| a new dual-run advisory comparison harness (candidate name only; no file exists) | compare a live TPGR shadow route against the existing full legacy-gate outcome for a real governed range, strictly advisory and non-blocking, per the work order's R7 framing | this design's Cost Accounting section's `UNKNOWN`/`PROJECTED` identity-comparison-cost gap, which only live telemetry can resolve | UNAUTHORIZED; R7 must define exact advisory-only non-blocking mechanics, a rollback rehearsal design, and negative tests proving the comparison cannot become enforcing before any implementation is authorized |
| any `governance/compat/check_*.py` file | none proposed by this design | no fixture, seeded case, or false-positive class in this replay identified a checker gap requiring a new or modified checker | NOT_PROPOSED |
| a new registry, receipt store, lifecycle standard, or second command catalog | none proposed | this design performs manual/documentary replay only, using the existing R3/R4/R5 field/token/graph/catalog definitions unchanged, with no second truth store | NOT_PROPOSED |

No path above is edited by this worker. This table exists to satisfy the
work order's requirement for a zero-edit R7 candidate manifest, not to
pre-approve any future change.

## Acceptance Threshold Reconciliation

Each threshold from the work order's Acceptance Thresholds section,
reconciled against this replay's actual evidence above:

| Threshold | Required | Observed | Met? |
| --- | --- | --- | --- |
| historical fixture coverage | 6/6 | 6/6 (H1-H6 above) | YES |
| material seeded-defect recall | 100%; false negatives: 0 | 15/15 detected (twelve R5 hostile plus three reviewer-repair); 0 false negatives | YES |
| declared false-positive class activations | 0/6 | 0/6 | YES |
| unknown/missing/contradictory facts routed light | 0 | 0; H3's missing current identity selects `ESCALATE_FOR_REVIEW`, and every UNKNOWN/PROJECTED cost cell and `NEEDS_FRESH_EVIDENCE` migration cell routes away from `LIGHT_ROUTE_ALLOWED`/`MIGRATABLE_CURRENT_WITH_IDENTITY` | YES |
| authority contamination or completion-claim laundering | 0 | 0; H2's superseded framing and H3's pending-closer status are both preserved and disclosed, never laundered into a stronger claim | YES |
| migration-created or upgraded `CURRENT` claims without identity | 0 | 0; zero `MIGRATABLE_CURRENT_WITH_IDENTITY` cells anywhere in the 84-cell migration table | YES |
| R4 fields reconciled | 8/8 | 8/8 x 6 fixtures = 48/48 cells populated | YES |
| R5 candidate fields reconciled | 6/6 | 6/6 x 6 fixtures = 36/36 cells populated | YES |
| A3 repeats of full-corpus enumeration absent a corpus-level invalidator | 0 | 0; H3 explicitly avoided full-corpus re-enumeration | YES |
| Layer A evidence counted as TPGR savings | 0 | 0; every Layer A cost cell in the Cost Accounting table is explicitly separated from TPGR/escalation/identity-comparison cells | YES |
| phase-inapplicable command cost charged to a fixture | 0 | 0; Seeded Case 14 demonstrates detection and the Cost Accounting table's construction avoids the error by design | YES |
| all mismatches disclosed; no historical outcome rewritten | required | H3's strict-route divergence and H2's superseded framing are explicitly disclosed; no historical disposition was rewritten to force agreement | YES |
| full phase-appropriate legacy bundle remains mandatory | required | confirmed in the Cost Accounting table's final row and independently verified by the required preflight gate commands below | YES |

All twelve acceptance thresholds are met. No threshold miss exists that would
forbid the proceed disposition.

## Evidence / Verification

Before dispatch, both worker outputs were required to pass routing and
dispatch gates; the pre-implementation autorun gate and the TPGR shadow-route
checker (`COMPLIANT`, 0 violations, `Legacy gate disposition:
RUN_FULL_LEGACY_BUNDLE`) were both run as required preflight, before any
edit, at `executionBaseHead`. During execution, this design records source
sections, replay worksheets, seeded-defect and false-positive matrices, the
fourteen-field migration table, cost accounting, and the no-commit boundary
directly in its own tables above and in the paired worker return's Command
Evidence section. Reviewer acceptance of this evidence, including
independent re-derivation of at least one case from each archetype and every
material seeded-defect class per the work order's Review Gate, remains a
separate, independent step owned by the reviewer/closer.

## Findings / Position

The accepted R3-R5 design reproduces the required fail-closed behavior across
all six archetypes (H1-H6), with zero unexplained mismatches: H3 takes the
explicit strict route because receipt freshness is unproven, while H2's
supersession framing is preserved rather than silently smoothed. The design
catches all fifteen required material seeded-defect cases (the twelve R5
hostile cases plus the three reviewer-repair cases this replay adds) with
zero false negatives, and correctly declines to activate on any of the six
false-positive classes. The A3 bounded-reuse case is preserved without
repeating full-corpus enumeration or inheriting unearned semantic
understanding. The fourteen-field migration table is fully reconciled across
all six fixtures (84/84 cells) with zero synthesized `CURRENT` claims -
every fixture instead resolves to `NEEDS_FRESH_EVIDENCE` or `HISTORICAL_ONLY`
for any field whose full R5 identity-binding evidence cannot be
reconstructed from the fixture's original prose, which this design treats as
the correct fail-closed outcome, not a completeness gap. Cost accounting
keeps every unavoidable Layer A evidence cost separated from TPGR/escalation/
identity-comparison cost, and every unmeasured cell is labeled
`UNKNOWN`/`PROJECTED` rather than claimed as a saving, consistent with R3
Rule 6 and R5's own Cost Proof section. All twelve of the work order's
Acceptance Thresholds are independently met.

## Risk / Corrective Action

Primary risk: the migration table's uniform `NEEDS_FRESH_EVIDENCE`
disposition for `receiptOwnerRef` and most other R5-shaped fields across all
six fixtures could be read as this design failing to demonstrate any
concrete migration path, rather than correctly demonstrating the fail-closed
boundary the work order requires. Corrective action: a future R7+ reader
must not treat the absence of `MIGRATABLE_CURRENT_WITH_IDENTITY` rows as a
defect in this design; it is the intended, evidence-driven outcome given
that R5's identity-binding fields did not exist when H1-H6's source
documents were authored. Any future tranche seeking to demonstrate a live
`MIGRATABLE_CURRENT_WITH_IDENTITY` migration must construct that identity
evidence fresh, from a document authored with R5's fields in mind, not
retrofit it onto H1-H6.

Secondary risk: H3's `REVIEWER_ACCEPTED_PENDING_CLOSER` status, disclosed
throughout this replay as the reason for `ESCALATE_FOR_REVIEW`, could be misread by a
future reader as this design casting doubt on T11's acceptance. Corrective
action: this replay does not re-litigate T11's acceptance; it only declines
to treat "pending closer" prose as equivalent to a fully closed,
identity-bound receipt for R5's stricter migration purposes, which is a
narrower and more conservative claim than re-opening T11 itself.

Tertiary risk: this design's Zero-Edit R7 Candidate Manifest names a future
dual-run advisory comparison harness whose exact non-blocking mechanics are
not yet specified. Corrective action: any R7+ implementation must define
negative tests proving the comparison cannot become enforcing before
implementation, per the manifest row's own authorization-state note, and
must not treat this design's naming of the candidate as pre-approval.

## Decision

`PROCEED_TO_R7_DUAL_RUN_CANARY_AND_ROLLBACK_REHEARSAL_DESIGN`

## Final Disposition

`PROCEED_TO_R7_DUAL_RUN_CANARY_AND_ROLLBACK_REHEARSAL_DESIGN`

Rationale: all six required historical archetypes (H1-H6) were independently
replayed against governed evidence with zero fabricated fixtures and zero
rewritten historical outcomes; all fifteen required seeded-defect cases
(twelve from R5 plus three reviewer-repair cases) were detected with zero
false negatives and none selected `LIGHT_ROUTE_ALLOWED`; all six declared
false-positive classes correctly raised zero activation; the fourteen-field
migration table is fully reconciled across all six fixtures with zero
synthesized `CURRENT` claims, correctly routing every field lacking full
identity evidence to `NEEDS_FRESH_EVIDENCE` or `HISTORICAL_ONLY`; the A3
bounded-reuse case is preserved without repeating full-corpus enumeration;
cost accounting separates Layer A, TPGR, escalation, and identity-comparison
cost with every unmeasured cell honestly labeled `UNKNOWN`/`PROJECTED`; and
every one of the work order's twelve Acceptance Thresholds is independently
met with no miss. This satisfies the paired baseline's Design Contract and
Stop Conditions and the work order's Acceptance Criteria. The next authorized
step is R7 (dual-run canary and rollback rehearsal design), which remains
unauthorized by this design and requires a fresh operator decision and
governed dispatch.

## Claim Boundary

This design is a documentation-only, non-implementation historical
seeded-defect shadow replay and migration design evidence artifact over
existing governed evidence. It does not implement any checker, receipt,
fixture, script, registry field, or catalog row; does not modify any
standard, checker, registry, catalog, hook, or router; does not intake or
register any new source corpus; does not authorize selective execution
(`selectiveExecutionAuthorized` remains `false` per the TPGR standard,
independently verified at this executionBaseHead); and does not open
R7-R9, T15, or any runtime, provider/live, public-sync, deployment, or
production action. The `PROCEED_TO_R7_DUAL_RUN_CANARY_AND_ROLLBACK_
REHEARSAL_DESIGN` disposition authorizes only a future operator decision to
open R7 under a fresh governed dispatch; it does not itself authorize R7
work.
