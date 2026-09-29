# CVF MFRP-P4 Shadow Canary And Governance-Tax Budget Design External Critique

Memory class: governed-review

Status: INDEPENDENT_DESIGN_CRITIQUE_COMPLETE

docType: review_context

Date: 2026-09-02

Batch ID: MFRP-P4-D0

executionBaseHead: `c1d1cbeef7b3c6bb979cabc982452dd14e48181c`

successorTrancheOpened: NO

providerExecutionAuthority: FORBIDDEN

## Purpose

Independently review whether the MFRP-P4-D0 shadow-canary and governance-tax
budget design is safe, measurable, operationally affordable, and consistent
with the CVF principle that governance controls authority, evidence,
boundaries and outcomes rather than how agents reason, choose roles, decompose
work or use tools. This is a design review only; it produces a disposition and
findings, and authorizes no implementation.

## Scope / Target / Owner Boundary

Target: exactly one committed design artifact,
`docs/assessments/CVF_MFRP_P4_SHADOW_CANARY_AND_GOVERNANCE_TAX_BUDGET_DESIGN_2026-09-02.md`
at material commit `3ac41e8c7d9acd10d606b6e6304f66d8427ed9d9`.

Owner boundary:

- the MFRP roadmap remains the owner of P4 mission, independent-detector
  requirement, metrics and cost budgets;
- the MFRP-P3-R1 redesign remains the owner of the R1B seam contract and the
  R1A/R1B/P4 tranche boundary;
- the Review Cost standard remains the owner of review telemetry fields and
  their unavailability semantics;
- the ratified R1A-R1 oracle remains the owner of the case/family/class
  expectation set and the C07/C08/C18 blind-spot record;
- this review owns only its own findings and disposition; it owns no design
  content and amends no governed surface.

Out of scope by construction: R1B implementation, canary execution, P2
modification, any source/test/fixture/standard/roadmap/registry/hook/session
change, staging, committing, provider/API/live/network calls, and any
evaluation of agent reasoning, prompts, role selection, subagent topology,
tool order or intermediate drafts.

## Review Identity

| Field | Value |
|---|---|
| Review kind | independent design review, documentary only |
| Primary target | `docs/assessments/CVF_MFRP_P4_SHADOW_CANARY_AND_GOVERNANCE_TAX_BUDGET_DESIGN_2026-09-02.md` |
| Material design commit | `3ac41e8c7d9acd10d606b6e6304f66d8427ed9d9` |
| Execution base HEAD | `c1d1cbeef7b3c6bb979cabc982452dd14e48181c` |
| Reviewer role | independent reviewer; not the design author |
| Authority claimed | none over R1B, P4 execution, P2 owners or route authority |
| Provider/live calls | 0 |

## Identity Gate Results

| Check | Method | Result |
|---|---|---|
| current HEAD equals execution base | `git rev-parse HEAD` | `c1d1cbeef7b3c6bb979cabc982452dd14e48181c` MATCH |
| material commit is ancestor of HEAD | `git merge-base --is-ancestor 3ac41e8c7... HEAD` | ANCESTOR CONFIRMED |
| primary target SHA-256 | recomputed over worktree bytes | `cf5615388f58b6d49fa603a0679d70b22ba28ff175062f5a1973e4f17573d8df` MATCH |
| worktree clean before writing | `git status --short` | empty; clean |
| target is committed material, not regenerated | blob OID compare | worktree, `3ac41e8c7:<target>` and `HEAD:<target>` all resolve to blob `097269aaf87d5dfa5b14a8ccc2b01fc2bad244f3` |
| target unmodified since material commit | `git log 3ac41e8c7..HEAD -- <target>` | no commits touch the target |
| design-declared base consistency | `git rev-parse 3ac41e8c7^` | `f2dec40fd39ed04f4249b98b3fb32dac67e21fbb`, exactly the design's declared `executionBaseHead` |

Identity gate: PASS. `BLOCKED_IDENTITY_MISMATCH` does not apply.

Independent recomputation of the design's six pinned source hashes: all six
MATCH the values declared in its Source / Predecessor Evidence table
(roadmap, R1 redesign, ratified oracle fixture, R1A-R1 worker return, Review
Cost standard, TPGR-R7 design). No source drift.

## Sources Actually Read

Read in full:

- `docs/assessments/CVF_MFRP_P4_SHADOW_CANARY_AND_GOVERNANCE_TAX_BUDGET_DESIGN_2026-09-02.md` (343 lines, complete)

Read in relevant part, with the sections named:

- `docs/roadmaps/CVF_GCLH_MACHINE_FIRST_REVIEW_PREFLIGHT_ROADMAP_2026-09-01.md`: Work Plan tranche table (lines 316-330), Historical Replay And Hostile Test Matrix, P3-R1 Actual-Seam Correction, Metrics And Value Test, Rollback And Kill Conditions, Cost And Complexity Budgets, Acceptance Criteria (lines 332-463)
- `docs/assessments/CVF_MFRP_P3_R1_ACTUAL_SEAM_REPLAY_AND_COMMITTED_ORACLE_REDESIGN_2026-09-01.md`: Tranche Split And Authority Boundary, Actual P2 Seam Contract (lines 158-173), Safety Predicate Vocabulary, Source And Locator Binding, Freeze And Immutability Contract
- `docs/reference/review_cost_control/CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md`: Scope / Applies To, Required Fields (lines 121-151), Single-Pass Review Latency SOP
- `governance/compat/fixtures/mfrp_p3_r1a_r1_static_only_oracle.json`: parsed as data; 19 cases; three `NOT_REPRESENTABLE_BY_CURRENT_P2` confirmed as exactly C07, C08, C18
- `docs/assessments/CVF_TPGR_R7_DUAL_RUN_CANARY_AND_ROLLBACK_REHEARSAL_DESIGN_2026-08-18.md`: Comparator Record, rollback posture rows
- `governance/compat/agent_autorun_machine_verification.py`: `_machine_verification_object`, `_validate_receipt_integrity`, `RECEIPT_SCHEMA`
- `governance/compat/agent_automation_machine_verification_readout.py`: `read_receipt_readonly`, `build_machine_verification_readout`
- `governance/compat/run_agent_autorun_workflow_gate.py`: `_write_receipt`, `_receipt_path`
- `governance/compat/run_agent_automation_assist.py`: lines 609-610, 1116-1117

Read as pointers only: `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`,
`CVF_SESSION_MEMORY.md`, `AGENT_HANDOFF_V59_2026-08-11.md`.

This review does not claim complete repository inspection. Findings below are
bounded to the paths and symbols named here.

## Design Understanding

The design defines a documentary, execution-blocked shadow canary. One real
phase-return artifact produced by ordinary project work is the canary unit.
The trusted (legacy/reviewer) route stays controlling throughout; a shadow
machine route consumes the same return read-only and produces an advisory
outcome. A comparator row records both outcomes plus identity, blind-spot and
cost fields. Divergence and high-risk returns receive 100% independent audit;
clean agreements receive a capped deterministic sample. Safety thresholds are
evaluated before cost thresholds. Passing thresholds does not activate a
lighter route; it only permits a separate P5 decision.

Verified fact: the design creates no runner, checker, hook, fixture, config
switch, registry or receipt family, and explicitly states no canary is run by
this tranche.

## Governance Boundary Assessment

The design's Core Autonomy Boundary section is, in my assessment, the
strongest part of the document and is correct on the CVF principle in the
mission.

Verified: the enumerated prohibitions cover chain-of-thought, prompt wording,
role labels, single-agent versus multi-agent topology, subagent count,
tool-call order, implementation algorithm, work decomposition, coding style,
intermediate drafts not offered as evidence, and speed/brevity as a quality
proxy. The stated comparison object is "the returned result plus its declared
evidence."

Verified: the comparator field list contains no agent-internal field. `phase`
is explicitly recorded for disclosure only, with "no quota per phase and no
quota by agent/role label," which removes the most obvious route by which a
phase or role metric could become a behavioral target.

Verified: the roadmap's Metrics And Value Test independently removed
focused-probe count and exception precision "because they can reward hidden
findings," and the design is consistent with that removal - it does not
reintroduce either.

Assessment of the incentive question asked in A3: the design mostly avoids
metrics that reward shorter reasoning or fewer findings. Two residual
pressures exist and are inference, not verified fact:

- the median/p95 duration ceilings apply to the machine path only, not to the
  reviewer, so they do not directly incentivize faster reviewing; but the
  `SIMPLIFY_CANARY_TAX_EXCEEDED` token fires partly on "clean-path audit
  exceeds its cap," which is an audit-volume trigger. A reviewer who wants to
  avoid firing that token has a weak incentive to classify a marginal return
  as clean agreement rather than as `EVIDENCE_INCOMPLETE`. F-04 addresses this.
- `duplicated semantic work` is counted "only when reviewer had to reconstruct
  work rather than assess returned evidence." That is the right definition,
  but it is reviewer-declared and has no independent test, so a reviewer under
  cost pressure can under-declare it. F-05 addresses this.

Neither residual pressure requires inspecting agent reasoning to fix.

Does the design create a second governance system? Stated explicitly, as
required: **no, not as written, but it is one unbounded step away from one.**
The design consumes the existing Review Cost owner, adds no reference family,
adds no receipt family and keeps the trusted route controlling. Those four
choices are what prevent a parallel system. The single largest threat to that
property is not in this document but in what a P4 work order might add on top
of it; F-06 and the corresponding mandatory correction bind that boundary.

## Duplicate-Work And Reviewer-Cost Assessment

Verified: the Independent Detector Boundary enumerates five bounded audit
checks (comparator identities, survival of limitations/not-checked scope and
`UNCLASSIFIED`, one source/authority binding, one declared hard obligation,
honest outcome classification, and whether machine output became authority).
It explicitly forbids repeating the phase, regenerating the deliverable,
rerunning every semantic decision, or inspecting agent reasoning.

Verified: `auditDisposition` is defined as "reviewer comparison result; never
a recreation of phase work."

Verified: `EVIDENCE_ENVELOPE_INSUFFICIENT` is defined so that a clean-agreement
audit that cannot be completed from returned evidence becomes a canary
finding rather than silent permission to redo the author's work. This is a
genuinely good control and directly answers the x2-latency risk in B2.

Reviewer-latency near x2 is bounded by construction for clean agreements: at
most four returns per window receive a five-check audit. For divergence and
high-risk returns the audit is 100%, which is correct - safety-driven cost is
supposed to be uncapped. The design correctly books that under
"safety investigation cost, recorded separately from clean-path tax."

B3, whether "zero duplicated semantic work" is operationally testable: **it is
not yet.** The measure is defined by reviewer self-declaration with no
observable discriminator between "assessed returned evidence" and
"reconstructed the work." A threshold of exactly 0 that depends on the
audited party's own classification is aspirational as written. F-05 is a
mandatory correction because this row is a promotion gate, not a soft metric.

## Same-Payload And Evidence-Binding Assessment

This section carries the most consequential finding in the review.

Verified from source, not inferred: in
`governance/compat/agent_automation_machine_verification_readout.py`,
`read_receipt_readonly` loads one JSON file inside the repo boundary, calls
`_validate_receipt_integrity(payload)`, and returns `(valid, payload, reason)`.
`run_agent_automation_assist.py` lines 1116-1117 then pass that same `payload`
object into `build_machine_verification_readout(valid, payload, reason)`.
Same-payload identity therefore holds structurally within one call chain,
because one single in-memory object is passed to both seams.

Verified: the R1 redesign's Actual P2 Seam Contract (lines 160-173) requires
the R1B runner to build a receipt, mutate it in memory, call the validator on
the mutated payload, then call the readout "on that exact observation." R1B's
same-payload proof is therefore a property of a **synthetic replay loop over
constructed receipts**.

Verified: `RECEIPT_SCHEMA = "cvf.autorun.pass-receipt.v3"`, and receipts are
written by `run_agent_autorun_workflow_gate.py::_write_receipt` at
`_receipt_path(phase, receipt_dir)`. A receipt attests that a set of
deterministic gate commands passed for a phase/base/head/command-manifest
envelope. It is a gate-run artifact.

The gap: the design's canary unit is "one real phase-return artifact already
produced by ordinary project work" - in CVF practice a `docs/reviews/*.md`
worker return and its declared evidence. The machine seam does not consume
that artifact. It consumes an autorun pass-receipt JSON. These are different
objects with different semantics: the receipt says deterministic gates passed;
the phase return asserts a semantic disposition.

Consequence: `machineOutcome` is defined as "advisory P2/AAF result from the
same return/evidence object," but for a real phase return there is currently
no P2 route that evaluates that return. The available machine outcome is a
readout over the associated gate receipt. Unless the comparator explicitly
declares that `trustedOutcome` and `machineOutcome` range over **different
objects with different semantics**, `EXACT_AGREEMENT` will be recorded for
pairs that were never comparing the same claim.

Answering C3 directly: **yes, part of the design depends on proof R1B has not
implemented, and more importantly on proof R1B is not scoped to produce.**
R1B proves same-payload identity for synthetic replay cases. It does not
establish that a real phase return and its gate receipt are the same evidence
object. The design's `samePayloadEvidence` field asserts "R1B-proven identity"
and therefore overstates what an accepted R1B will deliver for this canary's
actual unit. This is F-01, blocking.

C2, identity binding sufficiency: the `returnIdentity` triple (path, Git blob
identity, evidence-receipt identity) is strong and does prevent comparing two
regenerated or normalized payloads, because a Git blob OID is content-addressed
and any regeneration changes it. That part is sound. The defect is not weak
identity; it is that the two identities bound together belong to two different
kinds of object.

## Safety, False-Confidence And Blind-Spot Assessment

Verified and correct: the design states R1A-R1 established C07, C08 and C18 as
not representable by current P2, that they "remain outside machine recall
denominators and are never counted as PASS," and that "a canary that looks
efficient only by excluding these blind spots cannot pass." I independently
parsed the ratified oracle and confirm exactly three
`NOT_REPRESENTABLE_BY_CURRENT_P2` cases, and they are exactly C07, C08, C18.
D3 is satisfied.

Verified and correct: `BLIND_SPOT_NOT_REPRESENTABLE` is a first-class
divergence class, so a blind spot cannot be silently absorbed into
`EXACT_AGREEMENT`. The rule "missing or partial data cannot be mapped to
`EXACT_AGREEMENT`" is present and correct, and directly answers D2 for
`EVIDENCE_INCOMPLETE`.

Verified and correct: `controllingOutcome` is "always the trusted route during
P4 shadow mode," and the threshold table includes "machine closure where
trusted route blocks | 0." Together these answer D1 at the authority level: a
mechanical PASS cannot become authorization while shadow mode holds.

D4, whether clean agreement can reward both routes being wrong the same way:
**yes, and this is unaddressed.** I searched the design for any
correlated-failure, common-mode or detector-independence control and found
none. The structure makes this material rather than theoretical:

- `EXACT_AGREEMENT` is the expected dominant class;
- clean agreements receive at most four audits per window;
- the audit's five checks verify identity, survival of limitations, one source
  binding, one hard obligation and honest classification - none of which
  re-derives the semantic question both routes may have answered wrongly;
- the roadmap requires that "the route being replaced cannot be the only
  escape detector," which is about detector independence, and the design cites
  that requirement without discharging it.

The specific failure mode: a class of defect that the trusted reviewer
systematically misses and that current P2 cannot represent produces
`EXACT_AGREEMENT` on every observation, and the canary reports clean agreement
as evidence of machine-route safety. This is F-02, blocking. It is a design
gap, not an implementation detail, because the promotion gates read agreement
as a safety signal.

Stating the required explicit judgment: **yes, a proposed metric can create
false confidence.** The clean-agreement rate, as currently defined, measures
inter-route consistency and is capable of being read as correctness. The
oracle's own three blind spots demonstrate that consistency and correctness
come apart precisely where P2 lacks representation.

## Independent Detection And Rollback Assessment

Verified: rollback triggers for `ROLLBACK_SHADOW` are any failed safety
threshold, machine advice influencing authority, sampling selected after
seeing outcomes, or inability to disable the route without changing the
trusted result. Three of the four are detectable from the comparator ledger
and the trusted route's own record, independently of the shadow route's
self-report. That satisfies E1 for those three.

E5, whether any stop condition is detectable only by the mechanism it stops:
one is. "Machine advice influences authority" is a claim about whether a
reviewer's disposition was contaminated by the advisory machine output. The
comparator's own `auditDisposition` is written by that same reviewer. There is
no independent artifact establishing that the trusted disposition was reached
without reference to the machine outcome. In the current design the shadow
output is visible in the same ledger the reviewer fills in. F-03 records this
as blocking, with a cheap correction: order-of-record separation, so the
trusted disposition is committed before the machine outcome is revealed for
that return.

Verified and correct: rollback is defined as "stop producing/consuming shadow
comparator rows and continue the existing trusted route unchanged," it
preserves evidence, and it requires no provider or external effect. The design
explicitly refuses to claim a runtime config switch exists and requires a P4
implementation to prove its actual local rollback mechanism before the first
observation. This matches the TPGR-R7 precedent, which likewise recorded that
a config-switch flip is "never a claimed config-switch flip unless a current
CVF-owned source proves one exists (none does)." E3 and E4 are satisfied.

E2, whether the two tokens are executable decision tokens: `ROLLBACK_SHADOW`
has clear evidence requirements. `SIMPLIFY_CANARY_TAX_EXCEEDED` is weaker  - 
one of its four triggers is "reviewer work becomes a second execution of the
phase," which inherits the untestable-duplication problem in F-05, and another
depends on latency ratios that are usually unpopulable per F-07.

## Governance-Tax Budget Assessment

Verified and correct on separation: the ledger explicitly books existing
trusted-route duration as "unavoidable baseline; never counted as canary cost
or saving," shadow machine duration and extra commands as "recurring marginal
governance tax," clean-agreement audit minutes as "recurring sampling tax,"
and divergence/high-risk diagnosis minutes as "safety investigation cost,
recorded separately from clean-path tax." This is exactly the separation F
asks for, and it correctly prevents safety cost from being misread as normal
governance tax.

Verified and correct on honesty: "no projected saving is an observed saving,"
and the explicit statement that during shadow mode P4 "cannot claim that a
legacy review was actually avoided." This is the single most important
anti-overclaim sentence in the document.

Verified and correct: "provider calls and token/quota must remain zero for
machine execution," consistent with the roadmap's "no provider call in P0-P4."

Verified, supporting the design: machine-path duration evidence is genuinely
obtainable. `_write_receipt` records `totalDurationSeconds` and per-check
`durationSeconds`. The digest preimage in `_machine_verification_object` is
deliberately "duration-free," so recording duration does not disturb receipt
identity. The machine side of the ratio is well founded.

Verified, against the design: the trusted side is not. The Review Cost
standard's Required Fields contain no duration distribution of any kind. I
searched it for `p95`, `percentile`, `median`, `duration`, `per-return` and
`distribution` and found no occurrence. Its only temporal field is
`elapsedReviewMinutes`, which is one of exactly two fields permitted to be
`NOT_AVAILABLE_WITH_REASON`, and its scope is per completion-review artifact
declaring `docType: completion_review` - not per phase return.

Measured, not inferred: across `docs/reviews/*.md`, `elapsedReviewMinutes`
resolves to a number in 17 occurrences across 16 files, and to
`NOT_AVAILABLE_WITH_REASON` in 119 occurrences across 112 files. Numeric
availability is 12.5%.

Consequence for F1 and F7: the "median at most 10%" and "p95 at most 20%"
gates have a well-defined numerator and an empirically unpopulable
denominator. At a 20-return window with ~12.5% availability, the expected
number of trusted-route durations is about 2-3, which cannot support a median
and certainly cannot support a p95. A p95 over at most 20 observations is not
a meaningful statistic even at full availability; it degenerates to
approximately the maximum.

Mitigating and to the design's credit: the "cost evidence availability" row
already states that missing duration evidence "is disclosed and blocks a
cost-saving claim, not the safety observation," and both ratio rows are
conditioned "when both are available." So the design fails safe here - the
gates simply will not fire rather than firing wrongly. That is why F-07 is
recorded as non-blocking for safety while still being a mandatory correction
for honesty: a promotion gate that is designed never to evaluate should be
stated as such rather than presented as an operative ceiling.

F5, small-sample honesty: partially satisfied. The design is honest that a
smaller natural population is valid with declared coverage and that missing
phases stay `NOT_OBSERVED`. It is not honest about statistical power: it
attaches a p95 to a window whose maximum is 20 returns without qualification.

F6, whether the design optimizes for "faster review/fewer findings" as a
success proxy: no, and this is explicit. Safety gates precede cost gates, and
"all divergences/high-risk signals receive full audit." The Risk / Corrective
Action section names the exact hazard: "optimizing measured latency by hiding
findings."

F8, whether 20 returns / 30 days suffices for a bounded decision: yes for a
bounded, explicitly non-representative decision, and the design does not claim
phase representativeness - it forbids manufacturing work to fill quota and
marks unobserved phases `NOT_OBSERVED`. That is the correct posture.

## R1B/P4 Sequencing Assessment

Verified: design authoring may precede R1B. The design states this and bounds
it - "This design is allowed to precede R1B so its cost and independence
constraints can bind R1B/P4 planning early. It does not waive the roadmap
dependency."

Verified: the roadmap's Work Plan states "P4 requires accepted R1B replay," and
the design's Dependency And Opening Rule reproduces this with five conjunctive
conditions, including a fresh P4 work order and a rollback rehearsal that does
not assume a nonexistent production switch. It closes with "Neither R1B
acceptance nor this design opens P4 automatically."

Verified by targeted search: I scanned every occurrence of permissive verbs
(`may`, `must`, `shall`, `activate`, `authorize`, `enable`, `proceed`, `open`)
co-occurring with `R1B`, `P4`, `P5`, `activat`, `authoriz` or `route`. Every
hit is closing rather than opening. The strongest permissive sentence,
"Passing these thresholds does not activate a lighter route. It only permits a
separate P5 decision to consider which deterministic checks, if any, may
replace repeated deterministic reviewer work," is correctly bounded by "does
not activate," "separate," and "if any."

Verified: `successorTrancheOpened: NO`, and the Claim Boundary denies canary
execution, R1B/P4 implementation, P2 modification, trusted-authority change,
new telemetry/reference family, lighter-route activation, downstream change and
all provider/live/public/deploy/production action.

G3 finding: I identify **no wording that accidentally opens R1B implementation,
P4 execution or route-authority changes.** This section is clean.

## Practical Operability

H1, ledger populability: partially. `returnIdentity`, `phase`, `trustedOutcome`,
`blindSpotDisposition`, `divergenceClass`, `auditReason`, `auditDisposition` and
`controllingOutcome` are populable from existing return and receipt evidence
without new paperwork. `machineOutcome` and `samePayloadEvidence` are not, for
the object-mismatch reason in F-01. `costEvidence` is populable on the machine
side and mostly unpopulable on the trusted side per F-07.

H2, determinism: the identity construction is deterministic and well specified
 -  SHA-256 over repository-relative return path, Git blob identity and
controlling evidence-receipt identity, UTF-8 with LF separators, ordered by
lowercase hex digest. Selection genuinely cannot be gamed after seeing
outcomes, because the digest is fixed by content that predates classification.

However the sample size rule is not deterministic. The text reads
"deterministic 20% sample, maximum four; if at least two clean agreements
exist, audit the two lowest identity digests." These are two different rules
that disagree for most populations. Worked arithmetic over the clean-agreement
count n:

| n | 20% of n | "two lowest" rule | cap |
|---|---|---|---|
| 2 | 0.4 | 2 | 4 |
| 3 | 0.6 | 2 | 4 |
| 5 | 1.0 | 2 | 4 |
| 10 | 2.0 | 2 | 4 |
| 15 | 3.0 | 2 | 4 |
| 20 | 4.0 | 2 | 4 |

The two rules agree only at n=10. Rounding for non-integer results is
unspecified. At n=20 the rules differ by a factor of two, and the threshold
table separately caps clean-agreement audit at "at most 20% and at most four,"
which the "two lowest" rule would under-run. F-04 is blocking on this ground
alone: an ambiguous sample size makes the `SIMPLIFY_CANARY_TAX_EXCEEDED`
trigger non-evaluable.

H3, controls that add cost without independent detection value: I recommend
deleting or downgrading two. The p95 ceiling adds a statistic that a 20-return
window cannot support and whose denominator is 87.5% unavailable; the median
ceiling alone carries the same intent at lower cost. The `phase` field is
retained for disclosure only and is cheap, so it should stay. I found no other
field that fails the cost/detection test.

## Findings

| ID | Severity | Observation | Evidence | Consequence | Required correction |
|---|---|---|---|---|---|
| F-01 | BLOCKING | The canary unit is a real phase return, but the only current machine seam consumes an autorun pass-receipt JSON; `machineOutcome` and `samePayloadEvidence` presume a P2 route over the phase return that does not exist and that R1B is not scoped to create | `read_receipt_readonly` and `build_machine_verification_readout` in `governance/compat/agent_automation_machine_verification_readout.py`; `run_agent_automation_assist.py:1116-1117`; `RECEIPT_SCHEMA = "cvf.autorun.pass-receipt.v3"` and `_write_receipt`/`_receipt_path` in `run_agent_autorun_workflow_gate.py`; R1 redesign Actual P2 Seam Contract lines 160-173; design lines 48-52, 118-119 | `EXACT_AGREEMENT` can be recorded for a trusted disposition and a machine readout that were never evaluating the same claim, producing structurally meaningless agreement statistics | State explicitly that `trustedOutcome` and `machineOutcome` range over different objects, define which artifact each binds, and either restrict the comparator to returns with a controlling gate receipt or add an explicit `COMPARISON_OBJECT_MISMATCH` disposition. Correct `samePayloadEvidence` to claim only what R1B proves: validator/readout same-payload identity within one call chain over a receipt |
| F-02 | BLOCKING | No correlated-failure or detector-independence control exists; clean agreement is treated as a safety signal while the audit's five checks cannot re-derive the semantic question both routes may have answered identically wrongly | Design Independent Detector Boundary lines 139-153 and threshold table lines 180-192 contain no common-mode clause; searched for `both`, `correlat`, `common.mode`, `independence` with no governing hit; roadmap line 418-420 requires "the route being replaced cannot be the only escape detector"; oracle blind spots C07/C08/C18 demonstrate consistency and correctness diverging | A defect class the trusted reviewer systematically misses and current P2 cannot represent yields `EXACT_AGREEMENT` on every observation and is reported as clean-agreement safety evidence; false confidence at promotion | Add an explicit common-mode clause stating that agreement is evidence of consistency, never of correctness; require the promotion record to name which defect classes neither route can detect (at minimum C07, C08, C18) and to exclude them from any safety claim; require at least one escape detector not derived from either compared route, or record that the roadmap's independent-detector requirement is not yet discharged |
| F-03 | BLOCKING | The stop condition "machine advice influences authority" is detectable only from artifacts written by the party whose independence is in question; the shadow outcome and the reviewer's disposition share one ledger with no ordering constraint | Design lines 213-215 (`ROLLBACK_SHADOW` triggers) and comparator fields `trustedOutcome`/`machineOutcome`/`auditDisposition` at lines 117-123; no ordering or blinding rule anywhere in the document | A contaminated trusted disposition is unfalsifiable from the record, so the stop condition cannot fire on evidence; this is the one stop condition detectable only by the mechanism it is meant to stop | Require order-of-record separation: the trusted disposition and its evidence reference must be recorded and immutable before the machine outcome for that return is revealed or written, with the ordering itself evidenced (for example by separate commits or an append-only sequence). Without this, delete the trigger rather than keep an unfalsifiable one |
| F-04 | BLOCKING | The clean-agreement sample size is specified by two rules that disagree for every n except 10, with unspecified rounding | Design line 95: "deterministic 20% sample, maximum four; if at least two clean agreements exist, audit the two lowest identity digests" versus threshold row line 188 "at most 20% and at most four"; worked arithmetic in Practical Operability above | Sample size is non-deterministic despite the design asserting determinism; the `SIMPLIFY_CANARY_TAX_EXCEEDED` trigger "clean-path audit exceeds its cap" becomes non-evaluable, and audit volume can be argued after the fact | Replace with one closed formula, for example `k = min(4, max(1, ceil(0.20 * n)))` for n >= 1, and state the ordering rule (lowest k digests) as selection only, not as sample size. Ensure the threshold row and the sampling row cite one single shared formula |
| F-05 | BLOCKING | "Duplicated semantic work = 0" is a promotion gate but is defined only by reviewer self-classification with no observable discriminator | Design ledger row line 169 ("count only when reviewer had to reconstruct work rather than assess returned evidence") and threshold row line 189 ("0; any occurrence requires evidence-envelope correction before promotion") | A hard zero gate that depends on the audited party's own judgment is not operationally testable; B3 fails, and the same weakness propagates into the `SIMPLIFY_CANARY_TAX_EXCEEDED` trigger "reviewer work becomes a second execution of the phase" | Define an observable proxy, for example: duplicated semantic work is recorded whenever the audit consumed any source beyond the return, its declared evidence and the comparator identities. Make the enumerated audit input set closed, so exceeding it is observable rather than self-declared |
| F-06 | NON-BLOCKING | The design asserts a future P4 ledger "may carry these fields without creating a new reference family" but does not name the owning surface that will carry them | Design line 110-111; roadmap Cost And Complexity Budgets line 425-426 ("no new reference family unless P1 proves a required field cannot live in an existing owner"); Review Cost standard scope is `docType: completion_review` artifacts only, and contains none of the comparator fields | Without a named owner the comparator plausibly becomes a new reference family at P4 implementation time, which is the precise mechanism by which a second governance system would appear | Name the intended owning surface for comparator rows in the P4 work order, or state explicitly that no existing owner can carry them and that the roadmap's new-reference-family exception must be argued separately |
| F-07 | NON-BLOCKING | The median/p95 duration ceilings have an obtainable numerator and an empirically unpopulable denominator, and a p95 is not supportable at a 20-return window | Review Cost Required Fields lines 121-151 contain no duration distribution (searched `p95`, `percentile`, `median`, `duration`, `distribution`: no occurrence); `elapsedReviewMinutes` is numeric in 17 occurrences across 16 files and `NOT_AVAILABLE_WITH_REASON` in 119 across 112 files (12.5% availability); machine side is available via `totalDurationSeconds`/`durationSeconds` in `_write_receipt` | Two stated promotion ceilings will almost never evaluate; presenting them as operative ceilings overstates the design's measurement capability, though the "when both are available" conditioning makes the failure mode safe rather than wrong | Delete the p95 ceiling as unsupportable at this window size; retain the median ceiling but restate it as conditional and expected-usually-inapplicable, with an explicit statement that trusted-route duration is unavailable by default under the Review Cost owner and that no cost-saving claim may rest on it |
| F-08 | NON-BLOCKING | `docType: baseline` is declared on an artifact under `docs/assessments/` whose Status is `DESIGN_ONLY_READY_FOR_INDEPENDENT_REVIEW`, while the paired-baseline convention elsewhere in MFRP uses `docs/baselines/` for dispatch baselines | Design lines 5-7; compare MFRP-P3-R1A-R1 baseline at `docs/baselines/CVF_GC018_MFRP_P3_R1A_R1_STATIC_ONLY_ORACLE_CORRECTION_2026-09-02.md` | Low risk of a future reader treating a design assessment as dispatch authority; no current checker failure (reviewer-fast passes 67/67) | Recommend confirming `docType` is intended, or aligning it with the assessment convention. No action required before R1B |

Blocking findings: 5 (F-01 through F-05). Non-blocking: 3 (F-06, F-07, F-08).

## Mandatory Corrections Before R1B

These bind the separately authored R1B/P4 work order. They do not require
reopening or amending the reviewed design commit; they may be discharged in
the P4 work order that pins this design.

1. **Comparison-object disclosure (F-01).** Declare that `trustedOutcome` and
   `machineOutcome` bind different artifacts with different semantics, name
   the artifact each binds, and add an explicit mismatch disposition. Restate
   `samePayloadEvidence` to claim only validator/readout same-payload identity
   within one call chain over a receipt, which is what R1B actually proves.
2. **Common-mode clause (F-02).** State that agreement evidences consistency,
   never correctness; require the promotion record to enumerate defect classes
   neither route can detect (minimum C07, C08, C18) and exclude them from
   safety claims; either supply an escape detector independent of both
   compared routes or record that the roadmap's independent-detector
   requirement remains undischarged.
3. **Order-of-record separation (F-03).** Require the trusted disposition to be
   recorded immutably before the machine outcome for that return is revealed
   or written, with the ordering itself evidenced. Otherwise delete the
   "machine advice influences authority" trigger rather than retain an
   unfalsifiable stop condition.
4. **Single closed sampling formula (F-04).** Replace the two conflicting
   sampling rules with one formula and specify rounding; make the sampling row
   and the threshold row cite that identical formula.
5. **Observable duplication test (F-05).** Define duplicated semantic work by a
   closed, enumerated audit input set so that exceeding it is observable
   rather than reviewer-declared.

Non-blocking recommendations, explicitly distinguished from the above: name the
comparator's owning surface (F-06); delete the p95 ceiling and restate the
median ceiling as conditional and usually inapplicable (F-07); confirm the
`docType` declaration (F-08).

## Final Disposition

`REVISE_BEFORE_R1B`

Reasoning. The design's direction is sound and should not be rejected. Its
autonomy boundary is correct and unusually well drawn; its safety-before-cost
ordering, blind-spot retention, no-observed-saving honesty, evidence-preserving
rollback and refusal to assume a config switch are all correct; and its
sequencing language is clean, with no wording that opens R1B, P4 or any route
authority. `REJECT_CANARY_DIRECTION` would be wrong.

`ACCEPT_CANARY_DESIGN_BOUNDED` would also be wrong, because five findings are
blocking and three of them (F-01, F-02, F-03) concern whether the canary can
produce a meaningful safety signal at all rather than how efficiently it runs.
A canary whose two compared outcomes may range over different objects, whose
dominant clean-agreement metric cannot distinguish consistency from
correctness, and whose contamination stop condition is unfalsifiable is not yet
suitable as the governing input to an R1B work order.

All five blocking findings are correctable in the P4 work order without
redesigning the canary and without any implementation work.

This disposition authorizes nothing. It does not authorize R1B implementation,
P4 execution, canary observation, P2 modification or route-authority change.

## Risk / Corrective Action

The dominant risk this review identifies is false confidence rather than
overt failure. A canary that reports high clean-agreement rates reads as
evidence that the machine route is safe, when the same number is also
consistent with both routes sharing a blind spot. The corrective action is
F-02's common-mode clause plus explicit enumeration of undetectable defect
classes in any promotion record, so that agreement is never presented as
correctness.

The second risk is a comparison that is not a comparison: F-01's object
mismatch would let the ledger accumulate agreement statistics over pairs that
never evaluated the same claim. The corrective action is explicit
comparison-object disclosure before any comparator row is produced, not a
later reinterpretation of collected rows.

The third risk is a stop condition that cannot fire. F-03's contamination
trigger and F-05's duplication gate both depend on self-classification by the
party being constrained. The corrective actions are order-of-record separation
and a closed audit input set; where neither is adopted, the honest action is
to delete the unfalsifiable trigger rather than retain it as apparent safety.

A residual risk this review accepts rather than corrects: the 20-return window
cannot establish phase representativeness, and the design already says so. No
correction is required because the design does not claim otherwise.

The corrective actions above are recorded for the P4 work order. This review
performs none of them and amends no governed surface.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_equivalence_claim_evidence.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | the exact operation-trace section marker required by its checker and that section's seventeen row labels; learning-disposition `DEFECT_CLASSES`, `LANES`, `DISPOSITIONS` and `GENERALIZABLE_PROMOTION_DISPOSITIONS` vocabularies read directly from the checker source rather than guessed; epistemic four-part section markers; equivalence-claim phrase/disposition proximity rule; markdown common-element set (purpose, scope/target/owner boundary); ASCII-only encoding constraint; public export disposition heading |
| gateRunPurpose | confirm this review artifact is structurally compatible after source-led correction of six real gate failures found on first run; the gate was run before and after each correction round |
| claimBoundary | checker conformance proves document shape only; it cannot validate any finding, the disposition, the design's safety, or R1B/P4 readiness |

## Epistemic Process Block

### Expected Result / Prediction

Before reading the design I expected the main risks of a shadow canary to be
cost-shaped: a sampling regime that quietly doubles reviewer work, and metrics
that reward faster or thinner review. I predicted the governance-boundary
section would be the weakest part, because "observe outcomes, not reasoning"
is easy to state and hard to hold once metrics are attached.

### Evidence Comparison

That prediction was wrong in an informative way. The autonomy boundary is the
strongest section of the document and holds under adversarial reading: the
comparator carries no agent-internal field, phase is disclosure-only, and the
roadmap's own removal of focused-probe count and exception precision is
respected rather than reintroduced. Reviewer-cost doubling is also genuinely
bounded, by the four-return clean-agreement cap plus the
`EVIDENCE_ENVELOPE_INSUFFICIENT` rule.

The real defects sat one layer lower, in what the canary compares and in what
agreement proves. Reading `read_receipt_readonly`, `_write_receipt` and the R1
seam contract together showed that the machine seam consumes an autorun
pass-receipt while the declared canary unit is a phase return (F-01). Searching
the design for a common-mode or detector-independence clause returned no
governing hit, while the ratified oracle's own three blind spots demonstrate
that route agreement and correctness come apart exactly where P2 lacks
representation (F-02). Both were reachable only by checking the design against
executable source rather than against its own internal consistency.

Measuring `elapsedReviewMinutes` availability (17 numeric versus 119
unavailable occurrences) converted a suspicion about the duration ceilings
into a quantified fact, and changed my disposition on F-07 from blocking to
non-blocking, because the design's "when both are available" conditioning
makes the gate fail safe rather than fail wrong.

### Contradiction Or Gap Disposition

Five blocking findings are recorded rather than resolved here; a design review
cannot repair them. F-01, F-02 and F-03 concern whether the canary can emit a
meaningful safety signal at all, which is why the disposition is
`REVISE_BEFORE_R1B` rather than bounded acceptance. No finding was softened to
reach acceptance, and no unverified claim was promoted to fact: inference about
incentive pressure and correlated-failure likelihood is labeled as inference in
the body.

### Claim Update

The canary direction is sound and should proceed; its comparison object,
agreement semantics, contamination detectability, sampling determinism and
duplication test must be corrected in the separately authored P4 work order
before R1B work is dispatched against this design.

## Finding-To-Governance Learning Disposition

| Field | Value |
|---|---|
| findingsRaised | 8 (F-01 through F-08); 5 blocking, 3 non-blocking |
| defectClass | `RULE_GAP` for F-01, F-02, F-03 and F-05 (the design contract omits a required disclosure, independence, ordering or testability rule); `ORCHESTRATOR_PACKET_GAP` for F-04 and F-06 (packet-level specification ambiguity to be closed in the P4 work order); `DOCUMENTATION_ONLY` residue for F-07 and F-08 |
| learningLane | `GOVERNANCE_CONTROL_PLANE` for F-01 through F-06; `COST_ECONOMICS_LEARNING` for F-07 |
| disposition | `DESIGN_REVIEW_REQUIRED` - all eight findings return to the design/work-order layer for correction before R1B dispatch |
| next action | Author the MFRP-P4 work order pinning this design and discharging the five mandatory pre-R1B corrections; do not dispatch R1B implementation against the design until they are discharged. |
| newOwnerRequired | NO |
| newStandardRequired | NO |
| newCheckerRequired | NO |
| dispositionRationale | All eight findings are corrigible inside the separately authored MFRP-P4 work order that will pin this design. None requires a new governance owner, standard, checker, hook or reference family; proposing one would itself risk the second-governance-system failure mode this review flags in F-06. |
| existingOwnersSufficient | MFRP roadmap (P4 mission, independent detector, cost budgets); MFRP-P3-R1 redesign (R1B seam contract and tranche boundary); Review Cost standard (telemetry fields and their explicit unavailability semantics); the ratified R1A-R1 oracle (blind-spot set C07/C08/C18) |
| generalizableFindingPromotion | `N/A_WITH_REASON`: the reusable lesson below is recorded as bounded review evidence for the P4 work order only. Promoting it to a CVF-wide rule, template, standard or machine check is deliberately not proposed, because a single unreviewed dual-route design is insufficient evidence for a control-plane rule, and adding one here would enact the second-governance-system growth this review flags in F-06. Any promotion requires a separately authorized tranche. |
| generalizableLesson | A dual-route comparator must state which object each route evaluates before it may report agreement, and must state that agreement evidences consistency rather than correctness. Recorded as review evidence, not as an adopted control. |
| learningStorage | recorded in this governed CVF repository artifact, which is the authoritative record for this lesson |
| deferredToWorkOrder | the five mandatory pre-R1B corrections listed above |

## Claim Boundary

This is a documentary design review only. It ran no canary, implemented no
R1B, executed no replay, modified no source, test, fixture, standard, roadmap,
registry, hook or session state, staged nothing and committed nothing. It made
zero provider, live, network or credential calls.

Verified facts in this review are limited to: the identity-gate computations;
the six pinned source hashes; the parsed contents of the ratified oracle; the
named sections of the five governed documents listed under Sources Actually
Read; and the named symbols in the four Python files listed there. Statements
about incentive pressure, correlated failure likelihood and future P4
implementation behavior are inference and are labeled as such in the text.

This review does not claim complete repository inspection. It does not
evaluate agent reasoning, prompts, role selection, subagent topology, tool
order or intermediate drafts, and it did not request access to any of them.
Gate PASS on this file proves document compatibility only; it does not ratify
the design, prove canary safety or establish P4 readiness.

Acceptance semantics are explicit: no disposition in this review may be read
as opening R1B or P4. A separately authored, operator-governed work order
remains required.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | independent reviewer |
| Provider or surface | local private provenance repository |
| Session or invocation | MFRP-P4-D0 independent design review, 2026-09-02 |
| Working directory | repository root |
| Command or tool surface | `git rev-parse`, `git merge-base`, `git log`, `git show`, `git status`, read-only file reads, SHA-256 recomputation, text search, JSON parse, `run_local_governance_hook_chain.py --hook reviewer-fast` |
| Target paths | created exactly one: `docs/reviews/CVF_MFRP_P4_SHADOW_CANARY_AND_GOVERNANCE_TAX_BUDGET_DESIGN_EXTERNAL_CRITIQUE_2026-09-02.md` |
| Allowed scope source | operator instruction to independently review MFRP-P4-D0, design review only |
| Before status evidence | HEAD `c1d1cbeef7b3c6bb979cabc982452dd14e48181c`; `git status --short` empty; output path absent |
| After status evidence | one new untracked review file; no tracked file modified; nothing staged; no commit |
| Diff evidence | `git diff --name-status` empty; `git diff --cached --name-status` empty |
| Approval boundary | design review only; no R1B, P4, canary execution, source or session change |
| Claim boundary | documentary review; no runtime, provider, public or production claim |
| Agent type | independent reviewer |
| Invocation ID | `mfrp-p4-d0-independent-design-review-2026-09-02` |
| Expected manifest | `docs/reviews/CVF_MFRP_P4_SHADOW_CANARY_AND_GOVERNANCE_TAX_BUDGET_DESIGN_EXTERNAL_CRITIQUE_2026-09-02.md` |
| Actual changed set | `docs/reviews/CVF_MFRP_P4_SHADOW_CANARY_AND_GOVERNANCE_TAX_BUDGET_DESIGN_EXTERNAL_CRITIQUE_2026-09-02.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename in this review |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private CVF governance-foundation design review; no public-sync
authorization exists or is requested.
