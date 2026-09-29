# CVF Task-Proportional Governance Second Upgrade Claude Critique

Memory class: governed-planning-review

Status: ADVISORY_INPUT_PENDING_RECONCILIATION

docType: external_critique

Date: 2026-08-30

## Purpose

Independently critique the TPGR second-upgrade plan for TPGR-U2-P0 —
challenge Models A through F against the actual registry, schema, router,
checker, and tests rather than restate the plan, and return a disposition per
required question so the operator can decide whether to proceed toward an
implementation baseline.

## Target / Source

Target: `docs/assessments/CVF_TASK_PROPORTIONAL_GOVERNANCE_SECOND_UPGRADE_EXTERNAL_CRITIQUE_PLAN_2026-08-17.md`,
hash-verified before reading (see Review Identity). Source authority for this
critique is direct inspection of the currently committed TPGR standard,
registry, schema, router, checker, and tests, plus the twelve other sources
named in the assignment's Required Authority And Implementation Sources list.

## Scope / Methodology

Read the full plan after exact hash verification, then read the mandatory
authority/implementation sources in full (standard, registry, schema, router,
checker, both test files, review-cost standard, corpus-scan-registry
standard, mixed-origin absorption standard, mixed-origin latency learning).
Answered each of the twelve required questions against the plan's own text
cross-checked against the actual machine sources, not against the plan's
self-description. During source verification, also located and read two
prior TPGR reviews already present in the repository (an earlier external
critique of this identical plan hash, and its CVF reconciliation) plus two
later worker-return status lines, to confirm current repository state before
finalizing a disposition. Did not modify the plan, standard, registry,
schema, router, checker, tests, roadmap, handoff, or session state. Did not
open TPGR-U2-P1 or RSPB-AI-T15. Made no provider/live/network/subagent calls
and no commits.

## Findings / Position

The plan's diagnosis and staged fail-closed posture are sound. Twelve
per-question dispositions below converge mostly on MODIFY: the checker
dependency graph (Model D) is under-costed against the actual size of
`governance/compat/`; `decisionUncertainty` (Model C) permits reviewer
self-downgrade by construction; and Model B's invalidation triggers do not
bind to checker-closure version, so a receipt can outlive the checker
hardening it should have been invalidated by. The single most important
finding is procedural rather than about the plan's content: this exact plan
hash already has a full external critique and CVF reconciliation committed
under `docs/reviews/CVF_TPGR_SECOND_UPGRADE_EXTERNAL_CRITIQUE_2026-08-17.md`
and its reconciliation, both dated 2026-08-17, and the repository already
contains a substantial committed follow-on sequence (`CVF_TPGR_R2G` through
`CVF_TPGR_R8`, and the `TV1`-`TV3` tranche-value chain accepted 2026-08-26)
that appears to be the executed result of that reconciliation. Treating the
2026-08-17 plan as the pending frontier, as this assignment's framing does,
does not match current repository state.

## Risk / Corrective Action

Primary risk: an operator or successor orchestrator treats this critique (or
the 2026-08-17 plan it targets) as the next actionable TPGR input without
first checking that the plan was already critiqued, reconciled, and largely
carried forward — risking re-litigation of an already-closed planning
decision or duplicate design work.

Corrective action: this critique states the staleness finding prominently
(Executive Verdict and Final Disposition) and recommends the operator
reconcile against current TPGR state (`CVF_SESSION_MEMORY.md`, the active
handoff, and `CVF_SESSION/ACTIVE_SESSION_STATE.json`) before treating either
critique as the next actionable input. This critique does not itself resolve
that reconciliation, since doing so is outside the bounded scope authorized
for this assignment (one review file, no roadmap/work-order authoring).

## Review Identity

- Target plan: `docs/assessments/CVF_TASK_PROPORTIONAL_GOVERNANCE_SECOND_UPGRADE_EXTERNAL_CRITIQUE_PLAN_2026-08-17.md`
- Expected SHA-256 (assignment): `6cc0cde0dd98b6dbc79aa9bd01357e24fcc4657860c67e5aa1ca7ec1c7882653`
- Computed SHA-256 (this review, via `certutil -hashfile ... SHA256`): `6cc0cde0dd98b6dbc79aa9bd01357e24fcc4657860c67e5aa1ca7ec1c7882653`
- Match: EXACT. No `BLOCKED_PLAN_DRIFT`.
- Reviewer: Claude (Sonnet 5), independent critique worker, TPGR-U2-P0 shared-workspace assignment.

## Executive Verdict

The plan itself is sound in diagnosis and posture, and this critique would
independently reach dispositions close to those already on record. But the
plan is not, in fact, awaiting its first critique. A full independent
external critique of this exact plan
(`docs/reviews/CVF_TPGR_SECOND_UPGRADE_EXTERNAL_CRITIQUE_2026-08-17.md`) and
its CVF reconciliation
(`docs/reviews/CVF_TPGR_SECOND_UPGRADE_CRITIQUE_RECONCILIATION_AND_REVISED_PLAN_2026-08-17.md`)
already exist, both dated 2026-08-17, both reachable from HEAD. Beyond that,
the TPGR program has already executed most of the revised delivery sequence
that critique produced: `CVF_TPGR_R2G` through `CVF_TPGR_R8` design worker
returns (2026-08-17 through 2026-08-23) and the `TV1`/`TV2`/`TV3` tranche-value
admission chain (2026-08-26, TV3 accepted at commit `3b3f944ff`) are committed
and, per their own status lines, `COMPLETE_PENDING_REVIEW`. The
`trancheValue` object this critique's own read of the schema and router shows
present, fully implemented, and tested is exactly the R4/TV1/TV2 output of
that already-accepted revised sequence. Treating the 2026-08-17 plan as the
current unreviewed frontier, as the assignment's framing does, is stale by
roughly two weeks of accepted governed work.

This critique therefore does two things: it answers all twelve required
questions independently, on the plan's own terms, largely converging with the
prior critique's dispositions; and it registers, as its own strongest
finding, that the assignment's premise — "obtain independent critique before
any implementation baseline or work order" — was already satisfied and acted
on before this session began, and any operator or orchestrator relying on
this plan file in isolation should be redirected to the current TPGR state
before authoring further roadmap.

Final disposition: **REVISE_BEFORE_IMPLEMENTATION_PLANNING** as an answer to
the plan on its own terms, with an explicit note that this disposition may
already be moot — see Finding 1 below and the Final Disposition section.

## Source Verification

| Source | Read depth | Disposition |
| --- | --- | --- |
| `docs/assessments/CVF_TASK_PROPORTIONAL_GOVERNANCE_SECOND_UPGRADE_EXTERNAL_CRITIQUE_PLAN_2026-08-17.md` | FULL (642 lines) | ACCEPT — hash verified exact before read |
| `AGENTS.md` | FULL | ACCEPT — authority hierarchy, startup contract |
| `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md` | FULL | ACCEPT — current TPGR-T0 standard, including the already-implemented Tranche Admission And Continuation Value section |
| `governance/compat/CVF_TASK_GOVERNANCE_ROUTE_REGISTRY.json` | FULL | ACCEPT — 8 dimensions, 5 profiles, 10 bundles, protected-path minimums confirmed as described in the plan |
| `governance/compat/CVF_TASK_GOVERNANCE_ROUTE_MANIFEST.schema.json` | FULL | ACCEPT — closed-shape manifest plus optional 14-field `trancheValue` |
| `governance/compat/route_task_governance.py` | FULL (446 lines) | ACCEPT — router already implements bundle selection, contradiction checks, and the trancheValue decision precedence described in the standard; `selectiveExecutionAuthorized` hardcoded `False` everywhere |
| `governance/compat/check_task_governance_route.py` | FULL (210 lines) | ACCEPT — activation checker, hash-verified successor-authority resolution seam |
| `governance/compat/test_route_task_governance.py` | FULL (420 lines) | ACCEPT — router test coverage including trancheValue decision matrix |
| `governance/compat/test_check_task_governance_route.py` | FULL (120 lines) | ACCEPT — checker test coverage including authority resolution |
| `docs/reference/review_cost_control/CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md` | FULL | ACCEPT — single-pass review SOP, stop-disposition vocabulary, dispatch-convergence control |
| `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md` | FULL | ACCEPT — corpus registry rules governing reuse of prior scan state |
| `docs/reference/external_agent_review/CVF_MIXED_ORIGIN_DERIVED_SYNTHESIS_ABSORPTION_STANDARD.md` | FULL | ACCEPT — origin classes, evidence reuse controls (`manifestLedgerReuse`, `defaultValuePosture`, etc.) that Model A/B draw on |
| `docs/reviews/CVF_MIXED_ORIGIN_ABSORPTION_LATENCY_AND_VALUE_PRESERVATION_LEARNING_2026-08-16.md` | FULL | ACCEPT — the learning the plan cites as its cost-defect precedent |
| `docs/reviews/CVF_TPGR_SECOND_UPGRADE_EXTERNAL_CRITIQUE_2026-08-17.md` | FULL (334 lines) — targeted, not in the mandatory list, read to verify current repository state before finalizing this critique | ACCEPT — a prior full critique of the identical plan hash already exists |
| `docs/reviews/CVF_TPGR_SECOND_UPGRADE_CRITIQUE_RECONCILIATION_AND_REVISED_PLAN_2026-08-17.md` | TARGETED (first ~80 lines) — sufficient to confirm reconciliation disposition and independent re-verification of the prior critique's checker counts | ACCEPT |
| `docs/reviews/CVF_TPGR_R8_P0_P1_ALLOWLIST_DECISION_DESIGN_WORKER_RETURN_2026-08-23.md`, `CVF_TPGR_TV3_TERMINAL_TWO_COMPARISON_PILOT_WORKER_RETURN_2026-08-26.md` | TARGETED (status line + commit only) | ACCEPT — confirms `COMPLETE_PENDING_REVIEW` status and existence of committed follow-on work |
| `governance/compat` checker count / autorun catalog wiring | Not independently recomputed by this review; relied on the prior critique's and reconciliation's already-verified counts (193 checkers, 79 catalog-wired, 114 catalog-unwired) since re-deriving them would duplicate existing accepted evidence with no new decision value | DOCUMENTATION_ONLY_WITH_REASON |
| Full 205-file local corpus | NOT READ — plan requires only citation as reusable evidence, not re-enumeration; consistent with `CVF_CORPUS_SCAN_REGISTRY_STANDARD` Rule 1 (inherit `SCANNED`/`DEEP_CLASSIFIED` state, do not re-scan) | N/A_BY_DESIGN |

## Per-Question Dispositions

### Q1 — Does separating `originClass`/`intakeStage` from `taskKind` preserve provenance while preventing permanent over-classification?

**MODIFY.** The separation is the correct fix for the concrete defect the
plan names: today `taskKind: EXTERNAL_ABSORPTION` alone drives
`P1_LIGHT`/`P2_BOUNDED` minimums regardless of whether the material is a
seven-file CVF-native conversion from an already-accepted 205-file corpus or
a brand-new external repository. Coupling risk to provenance-that-never-decays
is exactly the over-classification bug described in the Problem Statement.
However, six `originClass` values is more than the routing logic needs:
`REUSED_ACCEPTED_CORPUS`, `PROVENANCE_BACKED_DERIVED_SYNTHESIS`, and
`MIXED_ORIGIN` all resolve to the same operational answer — "accepted
evidence exists, inherit it, do not re-run intake ceremony" — under Model B's
own inheritance rule. A field with values that never produce a different
route is classification debate with no control payoff.

Concrete alternative: collapse to four routing-relevant values (`CVF_NATIVE`,
`NEW_EXTERNAL_SOURCE`, `ACCEPTED_DERIVED`, `UNRESOLVED`), and keep the finer
distinction (mixed vs. co-designed vs. reused) as free-text provenance
metadata that must still exist (Mixed-Origin standard already requires this
via its Origin Classes table) but does not gate the router.

### Q2 — Are the evidence bindings and invalidation triggers sufficient?

**MODIFY.** The eight triggers cover the obvious stale-reuse paths: hash
drift, scope expansion, unresolved provenance, owner movement, new
completeness/absence claims, unreadable evidence, reviewer-named uncertainty,
and changed-paths-exceed-manifest. This is a reasonable floor. One material
gap: nothing in the trigger list invalidates a receipt when the *checker* that
produced it changes. Model D lists "checker source hash" as a cache input for
individual checker records but Model B's own invalidation-trigger list never
references it. A cluster whose selected-file receipt shows `PASS` under
checker version N remains inheritable after checker version N+1 is deployed
specifically to catch a newly discovered defect class — silently defeating
the hardening. This is not hypothetical: the plan's own precedent document
(the mixed-origin latency learning) is itself a checker-hardening event; under
Model B as written, receipts issued before that hardening would still have
inherited cleanly through it.

Concrete alternative: add a ninth trigger — "checker-closure version digest
producing this receipt has changed" — and bind every inheritance receipt to
that digest, not only to source-file hashes.

### Q3 — Which always-on core checks are unnecessary, and which missing invariant could cause a material false negative?

**MODIFY.** Five of the six proposed always-on items are correctly cheap and
correctly always-on (manifest/schema validation, diff-vs-authorized-path
reconciliation, protected-path/external-effect escalation, checker-inventory
freshness, phase receipt integrity). None should be cut; none is
unnecessary. Item 5 is the actual defect, not an omission: "no-secret/
no-destructive-boundary check **when those detectors can inspect the changed
material safely**" is a self-cancelling escape hatch on the single most
safety-critical always-on item. It directly contradicts Design Principle 7
("safety... boundaries remain fail-closed") and undermines Model F's own
"secret value present" trigger, which presumes the detector this clause can
disable actually ran.

Failure scenario: a change touches a binary asset, a minified bundle, or a
large generated file that a detector treats as "not safely inspectable," the
secret scan is skipped rather than escalated, and a credential ships in
exactly the file class most likely to hide one.

Missing invariant: nothing in the always-on core independently verifies that
a manifest's declared `pathFamilies` actually covers every diff-changed path
for authority-surface prefixes (`AGENTS.md`, `docs/reference/`,
`governance/compat/`, schemas/registries/hooks). The existing checker
(`_uncovered_paths` in `check_task_governance_route.py`) does this today for
work orders it inspects, but the plan's Model D framing treats
diff-reconciliation as a single generic item rather than naming the
authority-surface case as a distinct, unconditional invariant a self-
downgraded manifest cannot evade.

### Q4 — Can the checker dependency graph be maintained without becoming a second high-cost governance system? Smallest reliable schema?

**MODIFY — this is the plan's largest real cost, and the plan under-states it.**
Verification against `agent_autorun_command_catalog.py` (independently
confirmed by both this review and the prior 2026-08-17 critique/reconciliation
pair) shows the repository holds far more `governance/compat/check_*.py`
files than the autorun catalog wires in — the reconciliation independently
re-verified 193 total files against 79 catalog-referenced filenames, and
narrowed "114 orphans" (the prior external critique's word) to "114
catalog-unwired," since absence from the autorun catalog does not by itself
prove a checker is unused elsewhere. Either framing produces the same cost
conclusion: Model D's proposed per-checker record (ID, command, path
families, artifact types, claim/content triggers, lifecycle phases,
prerequisite and downstream checker IDs, protected owners, five-part cache
input, skip-reason vocabulary, full-bundle escalation conditions — ten-plus
fields including bidirectional dependency edges) is not "annotate an
existing map." `GateCommand` today is a two-field dataclass with zero
applicability metadata. Model D is proposing to build the repository's first
checker-applicability system from nothing, across a three-figure checker
surface, and P2's stated exit criterion ("every legacy command is mapped,
explicitly global, or blocked with an owner; no silent orphan checker")
requires resolving the unwired/unclear-usage checkers before P2 can close —
turning one stage of a seven-stage sequence into a standalone governance
project.

Smallest reliable representation: a five-field record extending the existing
`GateCommand` dataclass — `checkerId`, `command`, `appliesTo` (path globs +
artifact types), `phases`, `group` — with dependency ordering expressed as a
small (roughly half a dozen) partial order over coarse groups
(structure/governance-compat/absorption/code/state-security/runtime-live/
public-release) rather than per-checker bidirectional edges. Default every
unmapped or ambiguous-usage checker to the most conservative group
(always-selected) rather than gating P2 exit on individually adjudicating
every one of them. This keeps closure computation correct (selected groups
plus everything ordered before them) without an O(n²) edge-maintenance
burden or a P2 stage that cannot close on its own stated terms.

### Q5 — Are the full-bundle escalation triggers too broad or too narrow?

**MODIFY (narrow addition, one clause tightened).** The nine listed triggers
are well matched to the registry's own `P4_CRITICAL` minimums and the
self-referential "router/checker/hook/generator changes force full bundle"
trigger is exactly the right invariant against self-selective verification of
the thing being changed. Not too broad as a set. Two refinements: first,
nothing fires on *repeated* escalation or divergence for the same route
class over time, which risks alert fatigue turning a fail-closed signal into
routine noise that reviewers learn to wave through. Second,
`decisionUncertainty: HIGH/BLOCKED` is load-bearing for escalation while
being a free-form reviewer-assigned value with no floor — see Q7; a trigger
the routed party can set to avoid firing is a soft control, not a hard one,
and should not be removed but should be restructured as ratchet-only.

### Q6 — Bounded equivalence threshold before P0/P1 and P2 selective activation?

**MODIFY.** The plan correctly refuses a universal-equivalence claim and
correctly keeps P3/P4 on full legacy execution through initial activation —
this is the right default and should not change. But its stated exit
criteria are qualitative where a threshold needs to be quantitative: P3 exits
on "no unexplained material false negative" and P4 exits on "operator-
approved evidence threshold achieved" with no stated floor, which means the
threshold can be set after seeing results rather than before. Concrete
alternative, pre-registered before any replay begins: (a) a minimum-N
distinct-historical-tranche coverage floor per activating task class,
including at least one defect-bearing case; (b) a zero-tolerance 100% seeded-
defect recall floor specifically for authority/secret/destructive/
irreversible/unauthorized-path categories, with every miss in other
categories individually explained; (c) a zero-unexplained-divergence floor
for the dual-run canary, where "explained" requires a reviewer other than the
author. Equivalence claims should be scoped per task class and per checker-
inventory version, and should expire when either changes.

### Q7 — How should semantic reviewer judgment interact with deterministic routing without silent downgrade or automatic over-escalation?

**MODIFY — the plan's most under-specified control.** `decisionUncertainty`
is a routing-bearing field (`LOW`/`MEDIUM`/`HIGH`/`BLOCKED`) with no stated
assignment procedure and no verification, gating whether Model F's
uncertainty-based full-bundle trigger fires. The party whose review cost goes
down when uncertainty reads `LOW` is the party assigning it. Design Principle
6 states unknown classification escalates and never silently reduces
verification, but `LOW` is a *positive* confidence claim, not "unknown," and
nothing in the plan checks it against evidence. Under ordinary schedule
pressure this deflates to a constant `LOW`, and the uncertainty trigger
becomes decorative while receipts falsely record that uncertainty was
assessed. Concrete alternative: make the field ratchet-only — a reviewer may
raise the route (escalate with a stated reason) but no deterministic field
computed from the manifest/diff may be lowered by a reviewer-supplied value.
Restructuring `decisionUncertainty` from a four-value confidence scale into
an optional `escalationRequest` flag (present = escalate with reason, absent
= deterministic route stands) removes the downward path structurally rather
than by policy.

### Q8 — Does the accepted 205-file corpus route still inspect enough content to absorb and adapt coherently?

**ACCEPT (with one strengthening).** The eight-step route is well judged, and
"reuse corpus accounting, not selected-file understanding" is exactly the
right distinction — it directly implements the Mixed-Origin standard's
`manifestLedgerReuse: REUSE_IF_FRESH` /
`localSemanticInspection: FILE_AND_USE_CASE_CONTENT_REQUIRED` split, and the
explicit bulk-copy/paste prohibition (step and closing paragraph) correctly
guards against architecture dilution. The one soft spot: step 2 ("fully read
the substantive selected files") is an attestation with nothing binding the
claim to evidence — the router's `sourceEvidence.selectedFilesFullyRead` is
today a plain boolean (confirmed by direct read of
`SOURCE_EVIDENCE_KEYS`/`validate_manifest` in `route_task_governance.py`).
Nothing distinguishes "read the file bodies" from "read the file names and
inferred the content." Concrete strengthening: require a per-selected-file
read-time content hash in the cluster evidence record (which doubles as a
Q2 invalidation binding), so the full-read claim is self-evidencing rather
than self-reported.

### Q9 — Which historical replay or seeded adversarial cases are missing from P3?

**MODIFY.** The named case list (seven-file profile/policy example, pure
local contract clusters, governance-checker changes, continuity-only changes,
provider/live work, public-release work) covers a reasonable spread of
*target-work* risk classes, and the seeded-defect list (source drift,
unauthorized paths, owner conflict, schema mismatch, fail-open behavior,
secret exposure, closure mismatch) covers a reasonable spread of *defect*
classes. But every case targets the work being reviewed; none targets the
router itself. A suite that only seeds defects a correctly functioning router
would already catch cannot expose mis-mapping, stale-cache, or closure-gap
defects in the router's own logic — exactly the class of defect that would
kill a selective-execution system in production. Missing: a mis-mapped-
checker case (narrow a checker's `appliesTo` to wrongly exclude a path family
it should guard, seed a real defect there, confirm the gap is caught rather
than silently missed); a stale-receipt-after-checker-change case (Q2); a
manifest-omission case (diff touches `governance/compat/` while the manifest
declares only `docs/`, confirm escalation is diff-derived and not manifest-
trusting); and an uncertainty-deflation case (an authority-touching change
manually declared `LOW`, confirm the Q7 ratchet holds).

### Q10 — What rollback signal should immediately restore the full legacy bundle?

**MODIFY.** Rollback is the plan's thinnest section relative to its
importance. P4/P5 mention automatic fallback and operator override but name
no enumerated signal list, no stated blast radius, and no re-activation
procedure — an unrehearsed, unenumerated rollback path will not work well
under the pressure of an actual incident, which is the only time it matters.
Concrete alternative: two explicit tiers. Tier 1 (immediate, global,
default-on-ambiguity): any material false negative reaching production, any
missed fail-closed-category defect (authority/secret/destructive/
irreversible/unauthorized-path), checker-inventory or closure corruption, or
router self-modification outside the governance-maintenance route. Tier 2
(class-scoped): divergence confined to one task class, or an automatic
checker-inventory version bump. Re-activation only through the full P3/P4
evidence path, never by unilateral operator override alone. Rollback itself
should be config-only (no code change, no deploy) and rehearsed at least once
during the P4 canary stage, not left as an untested assumption.

### Q11 — Where does the plan introduce ceremony whose cost exceeds its control value?

**MODIFY (concrete cuts, not a wholesale rejection).** Four concentrations of
low-payoff ceremony: (a) Model D's ten-plus-field per-checker record over a
three-figure checker surface — the single largest cost in the whole plan,
addressed in Q4; (b) Model B's `provenance` and `decision` evidence types,
which record audit trail but do not change which route or bundle is chosen —
these belong in a non-routing audit-reference field, not the routing
structure; (c) the eight-metric-family telemetry block, several of whose
items (repeated-read counts, packet counts by lifecycle phase) require new
instrumentation to measure costs nobody in the plan actually disputes; (d)
TPGR-U2-P6 (absorption + project-governance adoption) is effectively a
second program appended to this one, with an exit criterion ("documented
examples and independent review show consistent routing without authority
dilution") that cannot be evaluated until P0–P5 have already produced real
evidence — it inflates the current decision surface without adding a
decision the operator can actually make today. None of this undercuts the
plan's genuinely high-value ceremony: the staged shadow→replay→canary→
progressive-activation sequence, the dual-run canary itself, and the always-
on core (once the Q3 clause is fixed) are exactly the right amount of
process for a change to fail-closed governance execution.

### Q12 — Final disposition

**REVISE_BEFORE_IMPLEMENTATION_PLANNING** — see Final Disposition section
below for the qualification that this disposition may already have been
executed on.

## Strongest Three Failure Modes

1. **The checker applicability map becomes the cost it was meant to remove.**
   (file: `governance/compat/route_task_governance.py`; representative line:
   the bundle-selection block at
   [route_task_governance.py:344-369](governance/compat/route_task_governance.py#L344-L369),
   where bundle selection today is a handful of simple boolean rules with no
   per-checker metadata at all.) Failure scenario: Model D's ten-plus-field,
   bidirectional-edge checker record is authored across the full
   `governance/compat/` surface; maintaining prerequisite/downstream edge
   pairs in sync as checkers are added, renamed, or refactored consumes more
   reviewer time than the selective execution it enables saves, and any
   drift between `A.downstream=[B]` and `B.prerequisite=[A]` silently
   under-selects a genuinely required checker — a direct false-negative path
   introduced by the routing system itself rather than by the work it
   routes.

2. **`decisionUncertainty` self-downgrade.** (file:
   `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md`,
   Model C's `decisionUncertainty` dimension, cross-referenced against
   Design Principle 6's "unknown classification... never silently reduces
   verification.") Failure scenario: an authority-touching or safety-
   relevant change is manually declared `decisionUncertainty: LOW` by the
   same party whose review burden shrinks if the full-bundle uncertainty
   trigger in Model F does not fire; nothing in the plan's validation logic
   (unlike, for comparison, the already-implemented hash-verified
   `successorAuthority` resolution seam in
   [check_task_governance_route.py:31-86](governance/compat/check_task_governance_route.py#L31-L86))
   checks the claim against independent evidence, so the escalation trigger
   is defeated exactly when it is needed most.

3. **Stale receipt inheritance across checker hardening.** (cross-reference:
   `docs/reviews/CVF_MIXED_ORIGIN_ABSORPTION_LATENCY_AND_VALUE_PRESERVATION_LEARNING_2026-08-16.md`,
   the plan's own cited precedent for a checker being hardened in response to
   a discovered gap.) Failure scenario: a checker is strengthened to catch a
   newly discovered defect class; a cluster's inheritance receipt, bound only
   to content hashes and not to checker-closure version, continues to be
   treated as `INHERITED_FRESH` after the hardening, so the repository
   silently retains exactly the defect class the hardening was written to
   close — invisibly, because no bound hash the plan currently defines
   actually changed.

## Proposed Minimal Schema/Routing Changes

- `originClass`: reduce from six to four routing-relevant values
  (`CVF_NATIVE`, `NEW_EXTERNAL_SOURCE`, `ACCEPTED_DERIVED`, `UNRESOLVED`);
  demote finer provenance distinctions to non-routing metadata already
  required by the Mixed-Origin standard's Origin Classes table.
- `evidenceInheritance`: add a `checkerClosureVersion` binding (digest over
  the source hashes of every checker in the selected route's dependency
  closure) as a new required field and a new Model B invalidation trigger;
  move `provenance` and `decision` evidence types to a non-routing audit
  reference rather than the routing-relevant evidence set.
- `decisionUncertainty`: replace the four-value scale with an optional
  `escalationRequest: {reason}` flag — present escalates, absent leaves the
  deterministically computed route standing; no reviewer-supplied field may
  lower a deterministic floor.
- Checker inventory (Model D): extend the existing `GateCommand` dataclass
  with `appliesTo`, `phases`, `group` (five fields total including the
  existing `name`/`command`); express dependency as a small partial order
  over coarse groups rather than per-checker bidirectional edges; default
  unmapped/ambiguous checkers to the most conservative always-selected group
  rather than gating P2 exit on adjudicating every one.
- Always-on core item 5: delete the "when those detectors can inspect the
  changed material safely" conditional; an uninspectable path escalates to
  full bundle rather than being treated as clean.

## Always-On-Core Recommendation

Keep five of six items exactly as proposed (manifest/schema validation,
diff-vs-authorized-path reconciliation, protected-path/external-effect
escalation, checker-inventory/dependency-graph freshness, phase receipt
integrity). Fix item 6 (secret/destructive boundary) to remove the
self-cancelling inspectability conditional — an uninspectable path is a
full-bundle trigger, never a pass. Add one additional always-on item: an
unconditional diff-derived (not manifest-declared) check that any changed
path under a protected-path prefix (`AGENTS.md`, `docs/reference/`,
`governance/compat/`, `.github/workflows/`, schemas/registries/hooks/router
itself) is reflected in the manifest's declared classification — this is
close to, but not identical to, what `_uncovered_paths` in
`check_task_governance_route.py` already does for work orders; the
recommendation is to make that specific authority-surface check an explicit,
independently-testable always-on item rather than an incidental effect of
general reconciliation.

## Full-Bundle Escalation Recommendation

The nine listed Model F triggers are not too broad; keep them as written.
Add a tenth: a task-class-scoped escalation/divergence-rate trigger (a class
escalating or diverging in more than a stated fraction of its recent runs
loses selective eligibility pending re-review of its mapping), to prevent
alert fatigue from converting the existing triggers into routine noise.
Restructure (do not remove) the `decisionUncertainty`-based trigger per Q7 so
it cannot be defeated by the party it constrains.

## Equivalence And Activation Threshold

Adopt three pre-registered floors, fixed before any P3 replay begins rather
than chosen after seeing results: a minimum distinct-historical-tranche
coverage floor per activating task class (including at least one
defect-bearing historical case); a zero-tolerance 100% seeded-defect recall
floor for authority/secret/destructive/irreversible/unauthorized-path
categories, with every miss outside those categories individually explained;
and a zero-unexplained-divergence floor for the P4 dual-run canary, where
"explained" requires review by someone other than the change's author.
Equivalence claims are scoped per task class and per checker-inventory
version and expire when either changes — this directly answers the plan's
own instruction to avoid unsupported claims of universal equivalence.

## Historical Replay And Seeded-Defect Matrix

In addition to the plan's named cases (seven-file profile/policy cluster,
pure local contract clusters, governance-checker changes, continuity-only
changes, provider/live work, public-release work) and seeded defects (source
drift, unauthorized paths, owner conflict, schema mismatch, fail-open
behavior, secret exposure, closure mismatch), add router-targeting cases:
mis-mapped-checker (narrowed `appliesTo` excluding a path family it should
guard, with a real seeded defect placed there); stale-receipt-after-checker-
change (a receipt issued under a superseded checker version, confirming
non-inheritance once the Q2 fix lands); manifest-omission
(diff touches a protected-path prefix while the manifest under-declares its
classification, confirming the escalation is diff-derived); and
uncertainty-deflation (an authority-touching change manually declared `LOW`,
confirming the Q7 ratchet cannot be talked down).

## Rollback Policy

Two explicit tiers rather than an undifferentiated "automatic fallback."
Tier 1 (immediate, global, and the default whenever tier is ambiguous):
production material false negative, a missed fail-closed-category defect,
checker-inventory/closure corruption, or router self-modification outside
the governance-maintenance route. Tier 2 (class-scoped): divergence confined
to one task class, an escalation-rate breach, or an automatic checker-
inventory version bump. Re-activation requires re-passing the full P3/P4
evidence path, never a unilateral operator override alone. Rollback itself
must be config-only (no code change, no redeploy) and rehearsed at least
once during the P4 canary stage so it is proven to work before it is needed
under pressure.

## Cost/Ceremony Objections

The plan's largest unaccounted cost is the Model D checker-applicability
system (Q4/Q11): building applicability metadata from nothing across the
full `governance/compat/` surface is a governance project in its own right,
not an annotation pass, and its current P2 exit criterion ("no silent orphan
checker") cannot close without first resolving checker usage/ownership for
every currently catalog-unwired file. Secondary ceremony with low payoff:
routing-inert evidence types (`provenance`, `decision`) inside the routing
schema; a telemetry block with metric families that require new
instrumentation to measure undisputed facts; and TPGR-U2-P6, whose exit
criterion cannot be evaluated with evidence that does not yet exist. None of
these findings argue against the plan's staged activation discipline, its
dual-run canary, or its always-on core, all of which are proportionate to
the risk of changing execution behavior in a fail-closed governance system.

## Absorption-Specific Objections

The accepted 205-file corpus route (Q8) is sound in structure — reusing
corpus accounting while requiring full substantive reads of selected files
is exactly the right split under the Mixed-Origin standard's
`manifestLedgerReuse`/`localSemanticInspection` controls, and the bulk-
copy/paste prohibition is explicit and correctly placed. The one gap is that
"fully read the substantive selected files" is currently an unverifiable
attestation (`sourceEvidence.selectedFilesFullyRead: boolean`), identical in
kind to the self-downgrade risk in Q7: nothing distinguishes a genuine
content read from a skim-and-infer conversion that declares the same
boolean. Binding the claim to per-file read-time content hashes closes this
without adding a new re-scan obligation, and it simultaneously supplies the
checker-closure/content binding Q2 needs.

## Final Disposition

`REVISE_BEFORE_IMPLEMENTATION_PLANNING` as a direct answer to the twelve
questions on the plan's own terms.

**With the qualification that this disposition is very likely stale as a
practical operator decision.** This session's own required reading turned up
a full external critique of this exact plan hash
(`docs/reviews/CVF_TPGR_SECOND_UPGRADE_EXTERNAL_CRITIQUE_2026-08-17.md`,
dated 2026-08-17, disposition `REVISE_BEFORE_IMPLEMENTATION_PLANNING`) and its
CVF reconciliation
(`docs/reviews/CVF_TPGR_SECOND_UPGRADE_CRITIQUE_RECONCILIATION_AND_REVISED_PLAN_2026-08-17.md`,
disposition `ACCEPT_REVISE_BEFORE_IMPLEMENTATION_PLANNING`), both already
committed to this repository. Both reach conclusions materially convergent
with this review — the same three decision-changing issues (checker-mapping
cost, `decisionUncertainty` self-downgrade, checker-hardening receipt
staleness) were already identified and reconciled there. Beyond that, the
repository already contains a substantial committed sequence that appears to
be the executed outcome of that reconciliation: `CVF_TPGR_R2G` through
`CVF_TPGR_R8` design worker returns (2026-08-17 through 2026-08-23) and the
`TV1`/`TV2`/`TV3` tranche-value admission chain (2026-08-26, accepted at
commit `3b3f944ff`), all `COMPLETE_PENDING_REVIEW`, plus a fully implemented
and tested `trancheValue` mechanism in the current router, checker, and
schema — which is not present in the 2026-08-17 plan this assignment treats
as the pending frontier. An operator or orchestrator instruction that relies
on this 2026-08-17 plan in isolation, without first checking
`CVF_SESSION_MEMORY.md` and the active handoff for TPGR's actual current
state, risks re-litigating an already-closed planning decision or duplicating
already-committed design work. This review answers the assignment as given;
it does not itself authorize any next TPGR action, and recommends the
operator reconcile against current TPGR state (`AGENT_HANDOFF_V59_2026-08-11.md`
and `CVF_SESSION/ACTIVE_SESSION_STATE.json`) before treating either this
critique or the 2026-08-17 one as the next actionable input.

## Claim Boundary

This critique is advisory input only. It is not CVF authority and must not
be cited as canonical authority in Source Authority tables, Source
Verification ACCEPT rows, corpus manifests, closure proof, or roadmap/work-
order evidence. Any fact stated here must be independently re-verified
against a CVF-governed surface before use as evidence. It does not amend the
active TPGR standard, registry, schema, router, checker, hook, or autorun
catalog; does not authorize selective gate execution
(`selectiveExecutionAuthorized` remains `false` throughout every source this
review read); does not open TPGR-U2-P1, RSPB-AI-T15, or any implementation
work order; and does not authorize runtime, provider/live, credentials,
network access, public sync, deployment, or destructive action. It grants no
implementation authorization.

## Checker Source Read-Ahead Block

| Field | Evidence |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py` |
| conditionalTriggersReviewed | governed review artifact, external critique, non-ASCII source-fidelity text, operation trace |
| literalTokensReviewed | `Checker Source Read-Ahead Block`; `Text Encoding Exception`; `Agent Operation Trace Block`; `Public Export Disposition`; `Claim Boundary` |
| gateRunPurpose | confirmation and evidence after direct checker-source read; not first discovery of required structure |
| claimBoundary | read-ahead confirms required packet shape only and does not promote this advisory critique to CVF authority |
| disposition | PASS: required blocks are present; this advisory critique opens no implementation authority |

## Text Encoding Exception

Bounded exception under
`docs/reference/CVF_TEXT_ENCODING_AND_SYMBOL_DISCIPLINE_STANDARD_2026-06-07.md`:
non-ASCII text in this external critique is retained for source fidelity to the
worker's Vietnamese-language analysis and quoted review context. It is not an
invisible-character, protocol-literal, or runtime claim.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | independent critique worker (shared-workspace, TPGR-U2-P0) |
| Provider or surface | Claude Code, local private provenance repository |
| Session or invocation | TPGR-U2-P0 second-upgrade critique, 2026-08-30 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | `certutil -hashfile` (SHA-256 verification); Read on plan and twelve required sources plus targeted reads of two prior TPGR reviews; `git log`, `git status --short` for changed-set and prior-work confirmation; Write for this review file only |
| Target paths | this review file only |
| Allowed scope source | operator/orchestrator work-order instructions for TPGR-U2-P0 critique |
| Before status evidence | plan hash verified exact match before any content was read; pre-existing dirty worktree (170 changed paths per `git status --short`) preserved untouched, none of it authored or touched by this review |
| After status evidence | exactly one new file created: this review |
| Diff evidence | `git status --short` before and after this review's authoring shows only this one new untracked path added to the pre-existing dirty worktree |
| Approval boundary | critique and planning-decision input only |
| Claim boundary | no TPGR implementation, selective execution, TPGR-U2-P1, RSPB-AI-T15, runtime/provider/live, public sync, deployment, destructive action, or commit |
| Agent type | independent critique worker |
| Invocation ID | `tpgr-u2-p0-claude-critique-20260830` |
| Expected manifest | one review file: `docs/reviews/CVF_TASK_PROPORTIONAL_GOVERNANCE_SECOND_UPGRADE_CLAUDE_CRITIQUE_2026-08-30.md` |
| Actual changed set | same one file |
| Manifest delta | zero |
| Provider/live/network/subagent calls | zero |
| Commits | zero |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private planning critique; public sync is not authorized by this
assignment and was not attempted.
