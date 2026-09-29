# CVF Task-Proportional Governance Second Upgrade External Critique

Memory class: governed-planning-review

Status: ADVISORY_INPUT_PENDING_RECONCILIATION

docType: external_critique

Date: 2026-08-17

External return SHA-256:
`4f3a02c2ca95028e2109f5c37f4311b755bd33dd81b2ea812917e6ff5dff588a`

Reviewer normalization: the external return is preserved semantically. The
CVF reviewer added the required governed-review wrapper, authority boundary,
trace, and encoding exception, replaced two rescan-trigger phrases with
equivalent "repeat scan" wording, and normalized two bare equivalence phrases
without changing their meaning. The hash above identifies the pre-review
external return; the committed artifact has a different post-normalization
hash.

## Purpose

Preserve the independent external critique of the TPGR second-upgrade plan as
advisory evidence pending CVF reconciliation.

## Target / Source

Target: the committed TPGR second-upgrade external-critique plan at
`b6bee448ce4ccc69b5969315d00255ca9100f1be`.

Source: external reviewer output returned by the operator. It is
`NOT_CVF_SOURCE` until each accepted fact is independently verified against a
CVF-governed surface.

## Scope / Methodology

The external reviewer read the full plan and selected machine surfaces, then
answered the twelve requested critique questions. The reviewer did not perform
a complete repository checker-usage audit, inspect the full local corpus, or
authorize implementation.

## Findings / Position

External disposition: `REVISE_BEFORE_IMPLEMENTATION_PLANNING`. The critique
identifies checker-mapping cost, uncertainty self-downgrade, and stale receipt
reuse after checker hardening as the three strongest risks.

## Risk / Corrective Action

Risk: promoting advisory measurements or design recommendations directly into
CVF authority would bypass source verification and independent reconciliation.

Corrective action: preserve this critique as advisory evidence and record all
accepted, modified, and rejected recommendations in a separate CVF-governed
reconciliation before any implementation decision.

# Independent External Critique

## Artifact Verification
- path: `docs/assessments/CVF_TASK_PROPORTIONAL_GOVERNANCE_SECOND_UPGRADE_EXTERNAL_CRITIQUE_PLAN_2026-08-17.md`
- expected commit: `b6bee448ce4ccc69b5969315d00255ca9100f1be`
- expected SHA-256: `6cc0cde0dd98b6dbc79aa9bd01357e24fcc4657860c67e5aa1ca7ec1c7882653`
- verification status: VERIFIED
- limitations: MATCH: computed SHA-256 matches exactly. Blob at `b6bee448c` is `344a32faa4fe2be0fd78c7d95050b4f5b9959a86`, the same blob at current HEAD `e063df90b`, so the file is unmodified between the expected commit and working tree; `git status` is clean. Note HEAD is *not* `b6bee448c` — it is one commit ahead (`e063df90b sync(cvf): await TPGR external critique`), which does not touch this artifact. Full 642-line artifact read. Additionally read `route_task_governance.py`, `CVF_TASK_GOVERNANCE_ROUTE_REGISTRY.json`, `agent_autorun_command_catalog.py`, and the TPGR standard to test the plan's premises against machine reality; did not read the full 205-file corpus, the mixed-origin absorption standard body, or all 193 checkers. No file was modified, staged, or committed. No work order, T15, or provider/live action was opened.

## Executive Position

The plan is genuinely good on the diagnosis and on fail-closed posture: separating provenance from task stage is the correct core insight, and the staged shadow→replay→canary→progressive-activation sequence is the right shape. But it under-costs its central mechanism and over-builds its schema. Verification found the decisive fact the plan does not state: the repository has **193 checkers in `governance/compat/`, of which only 79 are wired into the autorun catalog — 114 are already orphans** — and `GateCommand` is a two-field dataclass (`name`, `command`) carrying zero applicability metadata. Model D therefore is not "annotating an existing map"; it is building the repository's first checker applicability system, across a 193-node surface, from nothing. That is the plan's dominant hidden cost and its most likely failure point. Model D's per-checker record (ten fields, including a full dependency edge set) is unmaintainable at that scale and should be cut to a five-field record with dependencies expressed as coarse *groups*, not per-checker edges. Model A's `originClass` has six values where three carry routing weight, and Model B's seven evidence types exceed what actually gates a decision. The plan also leaves two real holes: nothing invalidates inherited evidence on checker-version change beneath a receipt, and `decisionUncertainty` is a reviewer-assigned field that a self-interested router can set to `LOW` — self-downgrade by construction. Finally, P6 (absorption + project-governance adoption) is scope the critique cannot responsibly bless now and should be deferred out of this sequence entirely. Net: the design is sound in principle, materially under-specified in cost and anti-self-downgrade controls, and needs one revision pass before implementation planning. Final disposition is **REVISE_BEFORE_IMPLEMENTATION_PLANNING**.

## Per-Question Disposition

### Q1
- Disposition: ACCEPT (with reduction)
- Rationale: This is the plan's strongest idea and it is correct. Today `taskKind: EXTERNAL_ABSORPTION` maps to `P1_LIGHT` in the registry while `sourceScale: CORPUS` maps to `P2_BOUNDED` — provenance is doing risk work that belongs to effect, which is exactly why a small CVF-native conversion inherits intake ceremony forever. Orthogonalizing lineage from current-work-being-done fixes the root cause. But six `originClass` values is over-modelling: does a field value change a routing decision? `REUSED_ACCEPTED_CORPUS` and `PROVENANCE_BACKED_DERIVED_SYNTHESIS` route identically (both are "accepted evidence exists, inherit it"), and `MIXED_ORIGIN` routes identically to whichever component is strictest.
- Failure mode: (a) Over-modelling: reviewers argue whether a cluster is `MIXED_ORIGIN` or `PROVENANCE_BACKED_DERIVED_SYNTHESIS` when both produce the same bundle — new ceremony, zero control value. (b) `intakeStage: I2_CVF_NATIVE_CONVERSION` becomes a laundering stage: an agent declares I2 on material whose selected files were never actually read at I1, and the plan's own text then legitimately routes it light. The I1→I2 transition has no gate.
- Concrete alternative: Collapse `originClass` to `CVF_NATIVE`, `EXTERNAL_UNACCEPTED`, `ACCEPTED_DERIVED`, `UNRESOLVED` (fail-closed). Keep finer lineage as free-text `provenanceRef`, not a routable field. Gate I1→I2: `intakeStage: I2` accepted only when `evidenceInheritance.selectedCluster` carries a full-read receipt whose file hashes match current disk; otherwise falls back to I1.
- Required evidence before implementation: Deterministic classification test showing a stable matching `(originClass, intakeStage, profile)` tuple across repeated runs on the same manifest; negative test proving an I2 manifest without a valid matching-hash cluster read receipt is rejected.

### Q2
- Disposition: MODIFY
- Rationale: The eight Model B triggers are well chosen and cover the obvious stale-reuse paths. Hash-binding to content rather than paths is the right foundation. Two gaps are material. First, there is no time-based freshness rule — the plan says evidence must be "within its freshness policy" but never defines one. Second, and worse: checker-version drift beneath a receipt does not invalidate it. Model D lists "checker source hash" as a cache input, but the Model B invalidation trigger list never mentions it. A cluster receipt recorded PASS under checker v1 remains inheritable after that checker is strengthened to v2.
- Failure mode: A checker is hardened in response to a real discovered defect. Clusters carrying pre-hardening receipts inherit their old PASS and are never re-examined under the stronger guard. The repository silently retains exactly the defect class the hardening was written to catch — invisibly, because no bound hash changed.
- Concrete alternative: Add two triggers. (1) Checker-closure version drift: bind each inheritance receipt to a version digest of the checker-closure that produced it; any source-hash change in that closure drops the receipt to `DELTA_REFRESHED` and re-runs only the changed closure. (2) Bounded freshness horizon expressed as commit-reachability from an `issuedAtCommit` field (deterministic, replay-safe) rather than wall-clock TTL (non-deterministic, fake-expiry-prone).
- Required evidence before implementation: Seeded test where a checker's source is modified and every receipt inheriting that checker transitions out of `INHERITED_FRESH` automatically; test proving an owner-file edit invalidates dependent cluster receipts without over-invalidating unrelated ones.

### Q3
- Disposition: MODIFY
- Rationale: Five of six always-on core items are correctly cheap and always-on: manifest/schema validation, diff-vs-authorized-path reconciliation, protected-path/external-effect escalation, checker-inventory freshness, phase receipt integrity. Item 5 is the defect: "no-secret/no-destructive-boundary check **when those detectors can inspect the changed material safely**" — a self-cancelling escape hatch on the single most safety-critical always-on item, contradicting the plan's own Design Principle 7 and undermining the Model F "secret value present" trigger, which depends on the detector this clause can disable.
- Failure mode: A change touching binary, generated, minified, or large-file material is judged not "safely inspectable," the secret detector is skipped, and a credential ships in exactly the material class most likely to hide one.
- Concrete alternative: Delete the conditional. Restate: the check runs on every changed path; a path a detector cannot inspect is reported `UNINSPECTABLE` and escalates to full bundle — never treated as clean. Also add one missing invariant to the core: a diff-derived (never manifest-declared) authority-surface touch detector for `AGENTS.md`, the routing index, `docs/reference/` standards, `governance/compat/`, schemas, registries, hooks — Model F depends on this but nothing independently checks a self-downgraded manifest that omits the declaration.
- Required evidence before implementation: Wall-time measurement proving the six-item core runs in a small fixed budget; negative test where a manifest omits an authority-path declaration and the diff-derived detector escalates anyway.

### Q4
- Disposition: MODIFY (strongest reservation in this critique)
- Rationale: Measured facts: `governance/compat/` contains 193 `check_*.py` checkers; `agent_autorun_command_catalog.py` (531 lines) references 79 of them; 114 are orphans, never wired into the autorun catalog. `GateCommand` is `@dataclass(frozen=True)` with exactly two fields (`name`, `command`) — no applicability, path-family, phase, or dependency metadata to build on anywhere. Model D asks each checker record to declare ten things including bidirectional prerequisite/downstream edges — O(n²)-shaped over ~193 nodes, and redundant (both directions must stay in sync). The plan's P2 exit criterion ("no silent orphan checker") means adjudicating an owner and applicability for 114 currently-orphaned checkers before P2 can exit — a substantial governance project budgeted as one stage among seven.
- Failure mode: (a) P2 stalls on 114 orphan adjudications; the map goes stale relative to checkers that keep changing; drift-detection fires constantly, forcing full bundle routinely — all the maintenance cost of selective routing, none of the savings. (b) Bidirectional edge drift: `A.downstream=[B]` and `B.prerequisite=[A]` disagree after a refactor; closure computation silently under-selects a genuinely required prerequisite — a direct material-false-negative path.
- Concrete alternative: (1) Cut the record to five fields: `checkerId`, `command`, `appliesTo`, `phases`, `group` — drop per-checker prerequisite/downstream edges. (2) Express dependencies as a partial order over ~7 coarse groups (`STRUCTURE`, `GOVERNANCE_COMPAT`, `ABSORPTION`, `CODE`, `STATE_SECURITY`, `RUNTIME_LIVE`, `PUBLIC_RELEASE`); closure = matched groups plus all groups ordered before them. Genuine producer/consumer pairs stay unidirectional on the consumer and should number in single digits. (3) Do not gate P2 exit on adjudicating all 114 orphans — default every unmapped checker to `group: GOVERNANCE_COMPAT, appliesTo: *` (always-selected; safer than today's "runs nowhere," and adds no selective omission for the 79 wired ones). Extend the existing `GateCommand` dataclass rather than creating a parallel inventory file.
- Required evidence before implementation: A worked prototype mapping the 79 currently-wired checkers under the five-field schema, with measured authoring time and stated per-checker-change maintenance cost. If mapping 79 is not boundedly feasible, reject Model D rather than scale it to 193.

### Q5
- Disposition: ACCEPT (with one addition and one narrowing)
- Rationale: The nine Model F triggers are well constructed and complete against the registry's own `P4_CRITICAL` minimums. The self-referential trigger (router/checker/generator/hook changes force full bundle) is exactly right, and the Evaluation Matrix's "no self-selective verification of the router/checker being changed" is a sharp, correct invariant. One trigger is missing: nothing fires on repeated escalation or repeated divergence over time for a route class, so a wrongly-mapped class just escalates constantly and everyone learns to treat escalation as routine noise. One is too broad: `decisionUncertainty: HIGH/BLOCKED` is load-bearing for escalation while being a reviewer-assigned free choice (see Q7) — a trigger the routed party can set themselves is not a control.
- Failure mode: Alert fatigue converts a fail-closed control into a rubber stamp; a real escalation is waved through as "the usual." Separately, `decisionUncertainty: LOW` self-assignment bypasses the uncertainty trigger entirely.
- Concrete alternative: Add a tenth trigger — a route class escalating/diverging in more than N of its last M runs loses selective eligibility until its mapping is re-reviewed. Do not remove the uncertainty trigger; make it ratchet-only (see Q7). State explicitly that all triggers evaluate against the diff, not only the declared manifest.
- Required evidence before implementation: Replay evidence showing trigger firing rates per task class; a trigger firing on nearly every run is mis-scoped and must be caught before activation.

### Q6
- Disposition: MODIFY
- Rationale: The plan correctly refuses universal equivalence claims and correctly keeps P3/P4 on full legacy execution during initial activation. But exit criteria are qualitative where they must be quantitative: P3 exits on "no unexplained material false negative" and P4 exits on "operator-approved evidence threshold achieved" with no stated floor — the threshold can be set to whatever is convenient when activation is desired. The plan also conflates detection equivalence (selective finds what full finds) with sample sufficiency (enough cases were run for that to mean anything) and only ever measures the first.
- Failure mode: Activation on a small, unrepresentative replay set — zero divergence across a handful of clean historical tranches (because they contained no defects) is recorded as equivalence evidence; the route activates and the first real defect in that class is missed.
- Concrete alternative: Require three floors, pre-registered before replay begins: (a) coverage floor — minimum N distinct historical tranches per activating class; (b) seeded-defect recall floor — 100% recall in authority/secret/destructive/irreversible/unauthorized-path categories, no tolerance, every miss in other categories individually explained and mapped to a fix; (c) divergence floor — zero unexplained divergences, "explained" requiring review by someone other than the author. State equivalence as per-task-class, per-checker-inventory-version.
- Required evidence before implementation: Pre-registered thresholds recorded in the TPGR owner before P3 replay runs — thresholds chosen after seeing results are not thresholds.

### Q7
- Disposition: MODIFY (plan's most under-specified control)
- Rationale: `decisionUncertainty: LOW|MEDIUM|HIGH|BLOCKED` is a routing-bearing field with no stated assignment procedure, no evidence binding, and no verification. The field that gates escalation is set by the party whose cost is reduced by setting it low. Design Principle 6 says unknown classification escalates and never silently reduces verification — but `LOW` is a positive confidence claim, not "unknown," and nothing checks it.
- Failure mode: Uncertainty deflation under schedule pressure — every task routed `LOW` because it's faster and nothing contradicts it; the uncertainty dimension becomes a constant; Model F's uncertainty trigger never fires while receipts falsely record that uncertainty was assessed.
- Concrete alternative: Make uncertainty ratchet-only and asymmetric. (1) A reviewer may raise profile freely with a one-line reason. (2) A reviewer may never lower a profile any deterministic dimension assigned — `decisionUncertainty` becomes escalation-only, structurally incapable of downgrading. (3) Restructure as an optional escalation flag (absent = deterministic route stands; present = escalate with reason) rather than a four-value confidence scale — simpler and structurally ungameable downward. (4) Independent-review triggers stay driven by `changeImpact`/`claimClasses`, never by self-assessed confidence.
- Required evidence before implementation: Negative test proving no combination of reviewer-supplied fields produces a profile lower than the deterministic floor; shadow telemetry on escalation-flag usage.

### Q8
- Disposition: ACCEPT (with one strengthening)
- Rationale: The eight-step 205-file route is well judged. The key distinction — "reuse corpus accounting, not selected-file understanding" — is exactly right, and the explicit copy/paste prohibition directly addresses architecture-dilution risk. The reservation: step 2 ("fully read the substantive selected files") is an unverifiable attestation, identical in kind to the I2 laundering risk in Q1. The router's `sourceEvidence.selectedFilesFullyRead` is currently a self-declared boolean with nothing binding the claim to evidence.
- Failure mode: Cluster selection degenerates into skim-and-adapt; `selectedFilesFullyRead: true` is declared, conversion happens from headings/file names, semantic value in file bodies is lost — the exact copy/paste failure the plan forbids, arriving through the attestation channel. Because the corpus receipt is inherited, nothing else would catch it.
- Concrete alternative: Bind the read claim to content — require the cluster read receipt to carry, per selected file, a content hash computed at read time (self-evidencing, and doubles as the Q2 invalidation binding). Require a short per-file value disposition (adopt/adapt/reject-with-reason); an "adopt" with no CVF-owner mapping is a copy/paste smell requiring resolution.
- Required evidence before implementation: A worked example on the seven-file cluster showing read receipts with matching hashes and per-file value dispositions, independently reviewed, with measured total cost.

### Q9
- Disposition: MODIFY
- Rationale: The P3 case list covers a good spread of risk tranches and defect types, but every seeded defect targets the work being reviewed — none targets the routing system itself. The failure modes that actually kill selective-execution designs (mis-mapping, stale caches, closure gaps) would not be caught by a suite that only seeds defects a correctly-functioning router would catch.
- Failure mode: P3 passes cleanly, activation proceeds, and the first production miss comes from a checker mapped to the wrong path family — a defect class P3 never simulated.
- Concrete alternative: Add six router-targeting cases: (1) mis-mapped checker — narrow `appliesTo` to exclude a path family it guards, seed a defect there, prove drift/closure machinery catches it; (2) stale-receipt attack — valid-hash receipt whose checker closure has since changed source hash, prove non-inheritance; (3) manifest-omission attack — diff touching `governance/compat/` with a manifest declaring only `docs/`, prove triggers are diff-derived; (4) uncertainty-deflation attack — authority-touching change declared `LOW`, prove the ratchet holds; (5) I2 laundering attack — I2 manifest with no valid cluster read receipt, prove fallback to I1; (6) orphan-checker diagnostic case. Also add rename-heavy and multi-owner historical tranches.
- Required evidence before implementation: All six router-targeting cases specified with expected outcomes stated before P3 executes.

### Q10
- Disposition: MODIFY
- Rationale: Rollback is the plan's thinnest area relative to its importance. P4/P5 mention automatic fallback and operator override, but no enumerated rollback signal list, no stated blast radius, and no re-activation procedure exist. A rollback control that is not enumerated and rehearsed will not work under pressure — the only time it is needed.
- Failure mode: A divergence appears in one class; with blast radius undefined, response is debated ad hoc while selective routing continues elsewhere, including classes sharing the same root cause — rollback happens late and partially, or over-broadly destroys confidence for a narrow well-understood cause.
- Concrete alternative: Two explicit tiers. Tier 1 (immediate global rollback): any production material false negative; any missed fail-closed-category defect; checker-inventory/closure corruption; router self-modification outside the governance-maintenance route; receipt-integrity failure; or ambiguity about which tier applies (default to Tier 1). Tier 2 (class-scoped): divergence confined to one class; escalation-rate breach; checker-inventory version bump (automatic). Re-activation only through the full P3/P4 evidence path. Rollback rehearsed once during P4 canary; config-only, no deploy required.
- Required evidence before implementation: A rehearsed rollback demonstration during canary with measured time-to-full-bundle; written confirmation rollback requires no code change.

### Q11
- Disposition: MODIFY (several concrete cuts)
- Rationale: Real ceremony in four places. (a) Model D's ten-field record over 193 checkers — the largest cost in the plan (quantified in Q4). (b) Model B's `provenance` and `decision` evidence types don't change routing — audit metadata inside a routing structure. (c) The telemetry block's eight metric families, several of which (repeated-read counts, packet counts by phase) require new instrumentation to measure a cost nobody disputes. (d) P6 is a second program bolted onto this one with an unfalsifiable exit criterion. Conversely, the dual-run canary, seeded-defect suite, and always-on core are high control value and should not be cut.
- Failure mode: A governance system that costs more to maintain than the ceremony it removed, with the cost distributed across every future change rather than concentrated and visible.
- Concrete alternative: Cut (a) per Q4. Move `provenance`/`decision` to a non-routing `auditRefs` field. Cut telemetry to three decision-gating metrics: selected/skipped/escalated counts, wall time, divergence result. Defer P6 out of this sequence entirely as a separate future proposal.
- Required evidence before implementation: A single-page cost model (estimated maintenance minutes per change vs. estimated savings) on the seven-file cluster and one mid-size tranche; if savings do not clearly exceed maintenance, do not proceed regardless of elegance.

### Q12
- Disposition: MODIFY → REVISE_BEFORE_IMPLEMENTATION_PLANNING
- Rationale: The diagnosis, fail-closed posture, staged sequence, and 205-file absorption route are sound and need no redesign. Three defects are decision-changing: the Model D cost basis understated against measured 193/79/114 reality; `decisionUncertainty` permitting self-downgrade by construction; and inherited evidence not invalidating on checker-version drift. Each has a bounded, concrete fix.
- Failure mode: Proceeding as-is produces a selective-execution system with an unmaintainable mapping layer, an escalation path defeated by a self-assigned field, and receipts that survive the checker hardenings meant to invalidate them.
- Concrete alternative: One bounded revision pass applying the fixes above, then re-review — plan-level only, no implementation, no T15.
- Required evidence before implementation: Revised plan plus the Q4 79-checker prototype and the pre-registered Q6 thresholds.

## Strongest Three Failure Modes

1. **The checker dependency graph becomes the cost it was built to remove.** (Highest severity — threatens the program's entire value proposition.) 193 checkers, 79 wired, 114 orphaned, zero existing applicability metadata, and a proposed ten-field bidirectional-edge record. P2's exit criterion requires adjudicating all 114 orphans. The realistic outcome is that mapping maintenance plus drift-induced fail-closed escalations consume the entire saving. Mitigation: five-field record, group-based ordering, orphans defaulted to always-selected, extend `GateCommand`, mandatory pre-implementation cost model on 79 real checkers.

2. **Self-downgrade through `decisionUncertainty`.** (High — silently disables the design's main semantic escalation path.) A routing-bearing, escalation-gating field assigned by the party whose cost falls when it is set `LOW`, with no evidence binding. Deflates to a constant `LOW` under normal pressure; Model F's uncertainty trigger never fires; receipts falsely record assessment occurred. Mitigation: ratchet-only field, restructured as an escalation-only flag, negative test proving no downward path exists.

3. **Stale receipt inheritance across checker hardening.** (High — inverts the intended safety property at the worst moment.) Invalidation triggers bind to content hashes only; a strengthened checker's prior PASS remains inheritable indefinitely, silently retaining exactly the defect class the hardening addressed. Same structural gap covers I2-laundering and attested-full-read paths. Mitigation: bind receipts to checker-closure version digest, gate I2 on hash-matching read receipts, make `selectedFilesFullyRead` self-evidencing via read-time hashes.

## Proposed Minimal Schema Changes

Principle: a field earns its place only if a different value produces a different route; everything else is `auditRefs`.

`sourceContext` reduced to four fields:
- `originClass`: `CVF_NATIVE`, `EXTERNAL_UNACCEPTED`, `ACCEPTED_DERIVED`, `UNRESOLVED` (6→4 values; merges reused-corpus/provenance-backed/mixed-origin, all of which route identically)
- `intakeStage`: unchanged shape, but I2 gated on a valid hash-matching cluster read receipt
- `evidenceState`: unchanged — all five values drive distinct routes
- `ownerFit`: unchanged — all five values drive distinct routes; `UNKNOWN`/`CONFLICT` fail-closed
- `decisionUncertainty` removed as a scale; replaced by optional `escalationRequest: {reason}` — present escalates, absent leaves the deterministic route standing, no downward direction exists

`evidenceInheritance` reduced to four types:
- `corpusReceipt` (manifest path + hash + file count; folds in ledger hash)
- `clusterReadReceipt` (per-file path + read-time content hash — self-evidencing)
- `ownerMapReceipt` (owner paths + current hashes + ownerFit)
- `checkerClosureVersion` (closure digest over selected checkers' source hashes — new, closes the Q2 gap)
- `provenance` and `decision` moved to non-routing `auditRefs`

Kept unchanged from Model C: `changeImpact` (5 values), `claimClasses`, `lifecyclePhase` (7 values), and "profile is the maximum of all applicable minimums."

Two required global invariants: (1) triggers and impact detection computed from the diff, manifest used only for cross-checking; (2) no reviewer-supplied field may lower any deterministic floor.

## Checker Dependency Graph Assessment

- Minimum viable checker record (five fields, extending `GateCommand`): `checkerId`, `command`, `appliesTo` (path globs + artifact types), `phases`, `group`. Drop `prerequisite`/`downstream`/`protectedOwners`/`skipReasonVocabulary`/`fullBundleEscalationConditions` — these are global router policy or belong in the always-on protected-path detector, not per-checker data.
- Dependency closure: ~7 groups (`STRUCTURE`, `GOVERNANCE_COMPAT`, `ABSORPTION`, `CODE`, `STATE_SECURITY`, `RUNTIME_LIVE`, `PUBLIC_RELEASE`) with a declared partial order; closure = matched groups plus everything ordered before them plus the always-on core. Rare genuine producer/consumer pairs declared unidirectionally on the consumer only, expected in the single digits.
- Drift/freshness rule: inventory version digest over every checker's source hash plus group order; any change bumps the digest, invalidates caches bound to the prior digest, forces the governance-maintenance route, and auto-rolls-back (Tier 2) task classes whose equivalence evidence predates the digest.
- Cache invalidation rule: reuse only when checker source hash, group-order digest, changed-path digest, and bound evidence-receipt digests are all identical and the checker explicitly declares receipt-reuse support — opt-in, not opt-out.
- Orphan-checker handling: the 114 unwired checkers default to `group: GOVERNANCE_COMPAT, appliesTo: *` (always-selected) — safer than today, and not a P2 exit gate. A checker referenced but absent from disk, or a group referenced but undeclared, is a fail-closed inventory error.
- Maintenance-cost risks: glob drift under renames (mitigated by rename-heavy P3 case); new checkers landing ungrouped (mitigated by always-selected default); contested group order (mitigated by small group count + governance-maintenance route requirement); residual risk that even five fields over 193 checkers proves too much — hence the mandatory 79-checker prototype before commitment.

## Activation And Equivalence Assessment

No claim of universal equivalence is made or should be made; equivalence is per-task-class, per-checker-inventory-version, and expires when either changes.

- Historical replay standard: pre-registered coverage floor (N distinct tranches per class, including at least one defect-bearing historical case), rename-heavy and multi-owner tranches included, every divergence classified by a non-author reviewer.
- Seeded-defect acceptance threshold: 100% recall, zero tolerance, for authority/secret/destructive/irreversible/unauthorized-path/router-self-modification categories — a single miss disqualifies activation. High stated threshold for non-safety categories with every miss individually explained. Suite must include the six router-targeting adversarial cases from Q9.
- Dual-run divergence rule: selective results advisory only during canary, never gate a commit. Any full-detects/selective-misses divergence triggers immediate Tier 1 rollback with required root cause before resumption. Selective-over-selects divergence is recorded, not a failure.
- Task classes eligible for first activation: `P0_OBSERVE` read-only; `P1_LIGHT` docs-only under unchanged existing owner; `P1_LIGHT` pure-local implementation under unchanged existing owner with no authority/secret/runtime/public/destructive/irreversible claim. Only these three.
- Task classes that must continue full legacy bundle: anything touching authority surfaces, `governance/compat/`, schemas, registries, hooks, generators, the router itself; `P2_BOUNDED` until P0/P1 runs clean in production for a bounded period; all `P3_ELEVATED`/`P4_CRITICAL`; every secret/credential/regulated/live/public-write/destructive/irreversible class; any `UNRESOLVED` origin or `CONFLICT`/`UNKNOWN` owner-fit.
- Immediate rollback triggers: Tier 1 (global) — production material false negative, missed fail-closed-category defect, closure corruption, router self-modification outside governance-maintenance route, receipt-integrity failure, or tier ambiguity (defaults to Tier 1). Tier 2 (class-scoped) — single-class divergence, escalation-rate breach, checker-inventory version bump (automatic). Rollback config-only, rehearsed once during canary.

## 205-File Absorption Assessment

- When manifest/ledger may be reused: whenever no Model B trigger fires and the checker closure that produced the receipt is unchanged — cited as accounting evidence, never re-enumerated. Endorsed without qualification; repeating the scan of 205 files to convert seven of them is pure waste.
- Depth of read required for a selected cluster: full and substantive — bodies not headings, plus use cases, plus current CVF owner and direct dependencies. Corpus accounting is inherited; selected-file understanding is never inherited. Self-evidenced via per-file read-time content hashes in the cluster receipt.
- Triggers forcing refresh: the eight Model B triggers plus checker-closure version drift; refresh is delta-scoped to what the trigger implicates, not corpus-wide, unless the trigger is corpus-root/manifest-hash level.
- Preserving knowledge value without mis-owner copy/paste: enforce via a checkable per-file value disposition (adopt/adapt/reject-with-reason) in the cluster receipt; every "adopt" must name a target CVF owner, and an unmapped or new-owner "adopt" requires explicit reviewer resolution.
- Routing for the seven profile/policy files: `originClass: ACCEPTED_DERIVED`, `intakeStage: I2_CVF_NATIVE_CONVERSION`, `evidenceState: INHERITED_FRESH` for corpus accounting plus a fresh `clusterReadReceipt` over all seven files, `ownerFit` against the existing owner, `changeImpact: LOCAL_LEAF` or `OWNER_COMPOSITION`. Recompute only the seven hashes; full substantive read; owner + direct-dependency inspection; focused proof over the routed closure; independent semantic review. Not required: a repeated 205-file scan, ledger re-adjudication, fresh external-repository intake ceremony. I2-gated: without a valid hash-matching read receipt for all seven, falls back to I1 — a good first canary case because it is small enough to dual-run cheaply.

## Ceremony And Cost Audit

KEEP: Model A provenance/stage separation (reduced 4+4 values) — removes root cause of over-classification, low cost. Model B hash-bound inheritance (reduced to 4 types) — makes reuse safe, low-moderate cost. Model C deterministic dimensions + max-of-minimums — anti-downgrade spine, already implemented, very low cost. Model F full-bundle triggers plus escalation-rate addition — the fail-closed backstop, low cost. Always-on core with the secret-check conditional deleted — fixed low cost. P3 replay + seeded defects plus six router-targeting cases — high but non-recurring cost, irreplaceable value. P4 dual-run canary plus rollback rehearsal — temporary cost by construction. 205-file inheritance route — very low cost, the concrete saving motivating the program.

SIMPLIFY: Model D checker record 10→5 fields, per-checker edges→group order — removes the O(n²) edge-maintenance burden, the plan's single largest hidden cost, while retaining full closure correctness. `decisionUncertainty` scale→optional escalation flag — control value increases (self-downgrade becomes structurally impossible) while cost decreases. Telemetry 8 metric families→3 — retains everything decision-gating, drops instrumentation for undisputed facts. P2 exit: drop "no silent orphan checker," default orphans to always-selected — removes 114 blocking adjudications while increasing coverage versus today.

REMOVE: `evidenceInheritance.provenance`/`.decision` as routing types — zero routing value, move to `auditRefs`. `originClass` values that route identically (`REUSED_ACCEPTED_CORPUS`/`PROVENANCE_BACKED_DERIVED_SYNTHESIS`/`MIXED_ORIGIN`) — zero routing value, classification-debate cost. The always-on secret check's "when detectors can inspect safely" conditional — negative control value, a credible secret-exposure path. A separate parallel checker-inventory file — no value over extending `GateCommand`, and is itself the second governance system Q4 warns against.

DEFER: P6 (absorption + project-governance adoption) — real but unmeasurable value until P0–P5 produce evidence, unfalsifiable exit criterion, inflates current approval surface; route to a separate future proposal. P2 selective activation — larger share of the saving but premature before P0/P1 production evidence; gate on a bounded clean-running period. Narrowing P3/P4 below full bundle — highest risk in the design; the plan already defers this correctly, keep deferred. Orphan-checker applicability adjudication — incremental value; opportunistic background work, never a gate.

## Recommended Revised Delivery Sequence

Planning (no machine change): R0 reconcile this critique in a separate CVF review artifact; R1 revise the plan applying the agreed fixes (schema reductions, uncertainty ratchet, checker-closure invalidation, always-on secret fix, two-tier rollback, P6 deferral) — TPGR-T0 unchanged, `selectiveExecutionAuthorized` still false; R2 cost-model prototype on the 79 currently-wired checkers under the five-field schema — decision gate, reject Model D here if infeasible; R3 pre-register replay/recall/divergence thresholds in the TPGR owner before any replay runs.

Shadow implementation (full legacy execution continues throughout): R4 taxonomy + receipt contract — amend the existing TPGR owner, implement the I2 gate and uncertainty ratchet, deterministic classification tests; R5 checker inventory as an extension of `GateCommand` — add `appliesTo`/`phases`/`group`, orphans default to always-selected, emit but do not execute a selective plan.

Proof: R6 historical replay + seeded defects including the six router-targeting adversarial cases and the seven-file cluster, pre-registered thresholds must be met; R7 dual-run canary, selective advisory only, starting with the seven-file cluster class, rollback rehearsed here.

Activation: R8 P0/P1 progressive activation only, allowlisted per task class and per checker-inventory version; R9 P2 consideration only after P0/P1 runs clean in production for a bounded period, via independent acceptance — P3/P4 remain full-gate.

Rollback (standing, not a phase, live from R7 onward): Tier 1 global and Tier 2 class-scoped triggers as specified; ambiguity defaults to Tier 1; re-activation only through the full R6/R7 path; rollback config-only and rehearsed.

## Final Disposition

`REVISE_BEFORE_IMPLEMENTATION_PLANNING`

The design's core insight and fail-closed posture are sound and should survive. Three decision-changing defects — the understated Model D cost basis against the measured 193-checker/114-orphan reality, self-downgrade via `decisionUncertainty`, and receipt survival across checker hardening — must be corrected in the plan before any implementation baseline or work order is authored. Each has a bounded, concrete fix specified above; none requires redesign.

## Authority Boundary

- This critique is advisory input only.
- It is not CVF authority and must not be cited as canonical authority in Source Authority tables, Source Verification ACCEPT rows, corpus manifests, closure proof, or roadmap/work-order evidence. Any fact here must be re-verified against a CVF-governed surface before use as evidence.
- It does not authorize implementation of TPGR-U2 or any part of it.
- It does not authorize selective gate execution; `selectiveExecutionAuthorized` remains `false`.
- It does not open RSPB-AI-T15 or any feature tranche.
- Operator and the CVF reviewer/orchestrator must reconcile this critique in a governed review artifact before any further decision.
- No file was modified, staged, or committed in producing this critique beyond this review artifact itself; no work order was created; no provider/live, network, public-sync, deployment, destructive, or production action was taken.

## Process Notes

- The expected commit supplied for verification (`b6bee448c`) is not HEAD; HEAD is `e063df90b`. The artifact blob is byte-identical at both commits, so verification passed, but the identity circulated to future reviewers should be confirmed against the intended reference point.
- The finding most worth reconciling first is the 193/79/114 checker measurement. It is not stated in the plan, and it changes the cost basis of Model D — the plan's largest component — from "annotate an existing map" to "build the first applicability system across 193 nodes." The R2 prototype gate exists specifically so that discovery, if it goes badly, costs one bounded pass rather than a whole implementation tranche.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | common review headings; trace labels; public disposition; local encoding-exception marker |
| gateRunPurpose | structural admission of advisory evidence only |
| claimBoundary | no recommendation is promoted by structural compliance |

## Text Encoding Exception

Unicode exception: evidence fidelity. The em dashes and arrows in the external
reviewer's prose are retained as a bounded evidence quote from the returned
critique. No invisible or control characters are authorized.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - this external critique makes no
  new complete-corpus claim and did not inspect or change the accepted
  205-file manifest or ledger.

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE_ADVISORY.

Expected Result / Prediction: independent review should identify hidden cost,
self-downgrade, freshness, activation, and rollback weaknesses before any
implementation planning begins.

Evidence Comparison: the external reviewer compared the plan with selected
current TPGR and autorun machine surfaces and returned measured checker/catalog
counts plus twelve question-level dispositions.

Contradiction Or Gap Disposition: every external fact remains subject to CVF
re-verification. The adjacent reconciliation records where terminology or
recommended solutions were narrowed.

Claim Update: none in this advisory file. Only the CVF reconciliation may
change the proposed plan.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | external reviewer, then CVF reviewer/orchestrator for structural normalization |
| Provider or surface | operator-returned advisory file in the private provenance repository |
| Session or invocation | TPGR second-upgrade external critique and reconciliation intake, 2026-08-17 |
| Working directory | repository root |
| Command or tool surface | entire critique read, SHA-256, Git identity checks, CVF machine-source verification, structural normalization |
| Target paths | this external critique only before reconciliation authoring |
| Allowed scope source | operator returned the critique for CVF review and decision |
| Before status evidence | clean continuity HEAD `e063df90b`; this critique was the sole untracked path at reviewer intake |
| After status evidence | advisory content retained with governed wrapper; reconciliation remains separate |
| Diff evidence | exact untracked/changed path and external-return hash |
| Approval boundary | advisory intake and structural normalization only |
| Claim boundary | no TPGR implementation, selective execution, T15, runtime/provider/live, public, deploy, or production |
| Agent type | external reviewer plus CVF reviewer/orchestrator |
| Invocation ID | `tpgr-second-upgrade-external-critique-20260817` |
| Expected manifest | this critique plus `docs/reviews/CVF_TPGR_SECOND_UPGRADE_CRITIQUE_RECONCILIATION_AND_REVISED_PLAN_2026-08-17.md` |
| Actual changed set | exact same two review paths |
| Manifest delta | zero |
| Deletion or rename disposition | N/A with reason: no deletion or rename authorized |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private advisory critique and reconciliation evidence; no public sync
is authorized.

## Claim Boundary

This file is external advisory input, not CVF authority. Structural admission
does not accept its measurements, terminology, thresholds, implementation
sequence, or recommendations. It authorizes no implementation, selective gate
execution, T15, runtime/provider/live, public sync, deployment, or production.
