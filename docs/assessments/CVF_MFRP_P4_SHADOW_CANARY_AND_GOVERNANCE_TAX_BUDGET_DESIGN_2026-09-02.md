# CVF MFRP-P4 Shadow Canary And Governance-Tax Budget Design

Memory class: governed-planning-assessment

docType: assessment

Status: REVISION_1_READY_FOR_INDEPENDENT_REVIEW

Date: 2026-09-02

Batch ID: MFRP-P4-D0

executionBaseHead: `f2dec40fd39ed04f4249b98b3fb32dac67e21fbb`

revisionOneBaseHead: `c1d1cbeef7b3c6bb979cabc982452dd14e48181c`

critiqueEvidenceCommit: `e79308d2cd5c0ff81e012c963428af3045ff990c`

revisionOneExecutionBaseHead: `7a3172acf8329d751bf30fea6b68b07aa64c5f85`

successorTrancheOpened: NO

## Purpose

Define the smallest useful MFRP shadow canary before any implementation or
activation. The canary measures both safety value and recurring governance
tax while preserving agent implementation autonomy. It observes returned
artifacts at phase boundaries; it does not prescribe prompts, reasoning,
roles, subagent topology, tool order, code structure or intermediate work.

This design is allowed to precede R1B so its cost and independence constraints
can bind R1B/P4 planning early. It does not waive the roadmap dependency:
actual P4 execution remains blocked until R1B actual-seam replay is separately
implemented, independently reviewed and accepted.

## Source / Predecessor Evidence

| Source | SHA-256 | Binding use |
|---|---|---|
| `docs/roadmaps/CVF_GCLH_MACHINE_FIRST_REVIEW_PREFLIGHT_ROADMAP_2026-09-01.md` | `4438fcce757dcbe9bb6041a025b36adf2a3d3350199000bd18fc2ed9f6c11a07` | P4 shadow-only mission, independent detector, metrics, rollback and cost budgets |
| `docs/assessments/CVF_MFRP_P3_R1_ACTUAL_SEAM_REPLAY_AND_COMMITTED_ORACLE_REDESIGN_2026-09-01.md` | `22a086d7742dbdaec5b887fd377890962ad34396953f48287ce865f743766011` | R1B/P4 dependency and actual-seam evidence boundary |
| `governance/compat/fixtures/mfrp_p3_r1a_r1_static_only_oracle.json` | `6aa32c3157092c974441c269d17e85aed20d5ba535479523eda5b64d23b3fbf2` | ratified 19-case, 18-family and seven-class expectation set |
| `docs/reviews/CVF_MFRP_P3_R1A_R1_STATIC_ONLY_ORACLE_CORRECTION_WORKER_RETURN_2026-09-02.md` | `32dabae39e0a4465b5e3a7ad4ba10e4cdf1aa7be7c20c1f6f8ba21f0ad87dee6` | independent `ORACLE_RATIFIED_BOUNDED` evidence and three honest P2 blind spots |
| `docs/reference/review_cost_control/CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md` | `7ead5cbde33d2012eaa58a9c161026454fe6133f7fe6e93facd975a2a0a4c8b1` | existing cost fields and single-pass review boundary; consume rather than duplicate |
| `docs/assessments/CVF_TPGR_R7_DUAL_RUN_CANARY_AND_ROLLBACK_REHEARSAL_DESIGN_2026-08-18.md` | `ca58d33e218e9c3160a49edb450eaf3f71454e0f5641e928a17b1d07615538ca` | advisory comparator and rollback precedent; no TPGR authority transfers to MFRP |
| `docs/reviews/CVF_MFRP_P4_SHADOW_CANARY_AND_GOVERNANCE_TAX_BUDGET_DESIGN_EXTERNAL_CRITIQUE_2026-09-02.md` | `a379503d642f40bb76ecbd868c4c86f816ac94a29b1616f8dfe0671df97b533d` | independent `REVISE_BEFORE_R1B` disposition and F-01 through F-08 corrections |

## Revision 1 Disposition

Revision 1 accepts F-01 through F-08 from the independent critique. The five
blocking findings are discharged here rather than deferred into a future work
order. The revisions disclose the two comparison objects, limit agreement to
consistency, establish order-of-record evidence, use one closed sampling
formula, and replace reviewer self-classification with a closed audit-input
manifest. They also name the one-off comparator owner, remove the unsupported
p95 gate, narrow the median diagnostic, and align `docType` with this path.

This correction changes no execution authority. R1B authoring, R1B execution
and P4 execution remain closed pending independent acceptance of Revision 1.

## Scope / Methodology

The design covers one documentary comparator contract, sampling rule,
independent-audit rule, cost ledger, thresholds and rollback posture. It
creates no runner, fixture, checker, hook, config switch, registry, receipt
family or provider integration. No canary is run by this tranche.

The canary unit is one observation pair already produced by ordinary project
work: (a) a committed phase-return artifact and its declared semantic evidence,
and (b) the associated autorun pass-receipt consumed by P2/AAF. They are
different artifacts with different semantics. The trusted outcome binds the
phase return; the machine outcome binds only the deterministic gate receipt.
The canary measures whether those identified records are compatible; it never
claims that both routes evaluated the same proposition.

CVF must not manufacture a task, repeat a phase, or require a second authoring
pass merely to fill a canary quota. The current trusted route remains
controlling and runs only when it would have run without the canary. The shadow
route consumes the existing associated receipt read-only after the trusted
record is immutable.

## Core Autonomy Boundary

CVF governs authority, source identity, evidence, outcome, cost and escalation
boundaries. The canary must never collect or score:

- chain-of-thought, hidden reasoning or prompt wording;
- role labels, single-agent versus multi-agent topology, or subagent count;
- tool-call order, implementation algorithm, work decomposition or coding
  style;
- intermediate drafts that were not offered as phase-return evidence;
- speed or brevity as a proxy for semantic quality.

The comparison boundary is the identified observation pair above, not a claim
that one common semantic object exists. Reviewer audit verifies compatibility
of the result, its declared evidence and the associated receipt; it does not
recreate work performed by the author or another role.

## Dependency And Opening Rule

This design may be independently reviewed now. P4 execution remains closed
until all of the following exist:

1. an accepted R1B actual-seam replay with a committed runner/result identity;
2. zero unexplained R1B divergence for representable zero-tolerance cases;
3. explicit retention of C07, C08 and C18 as uncovered P2 blind spots unless a
   separately authorized P2 hardening tranche changes that evidence;
4. a fresh P4 work order pinning the accepted R1B and this reviewed design;
5. a rollback rehearsal that does not assume a nonexistent production switch;
6. independent acceptance of this Revision 1 design, including its
   comparison-object and common-mode boundaries.

Neither R1B acceptance nor this design opens P4 automatically.

## Canary Population And Sampling

The observation window closes at the earlier of 20 eligible real returns or
30 calendar days. A smaller naturally occurring population is valid evidence
with declared phase coverage; missing phases remain `NOT_OBSERVED`, never a
reason to create artificial work or claim seven-phase adoption.

| Population class | Shadow machine run | Independent audit |
|---|---|---|
| known high-risk/live/public/destructive or zero-tolerance signal | once, advisory only | 100%; trusted route remains controlling |
| any machine/trusted-route divergence, identity drift, incomplete evidence or `UNCLASSIFIED` item | once | 100% |
| non-divergent consistency without those signals | once | audit the lowest `k` identity digests, where `k = min(4, max(1, ceil(0.20 * n)))` for `n >= 1` eligible records in the closed window; `k = 0` when `n = 0` |
| return outside the ordinary trusted route | none | none; canary does not create a new governance obligation |

The sampling identity is SHA-256 over repository-relative return path, Git blob
identity and controlling evidence-receipt identity, serialized as UTF-8 with
LF separators. Eligible non-divergent records are ordered by the resulting
lowercase hex digest. The single formula above determines sample size; digest
order only selects which `k` records. Sampling is reproducible and cannot be
selected by the author or reviewer after seeing the outcome.

There is no quota per phase and no quota by agent/role label. Phase is recorded
only to disclose which of `INTAKE`, `DESIGN`, `SPEC`, `WORK_ORDER`, `BUILD`,
`REVIEW` and `FREEZE` happened to be observed.

## Shadow Comparator Contract

Each observed pair has one compact comparator row. Its owner is the one-off P4
worker-return artifact governed by the future P4 work order under
`docs/reviews/`; it is bounded tranche evidence, not a new reference family,
standard, registry, receipt family or persistent governance owner.

| Field | Rule |
|---|---|
| `phaseReturnIdentity` | repository-relative path, pre-shadow Git commit and blob identity of the semantic return |
| `receiptIdentity` | repository-relative receipt path, receipt digest and verifier/readout identity |
| `pairLinkageEvidence` | explicit evidence reference associating receipt with phase return; absence or ambiguity is `COMPARISON_OBJECT_MISMATCH` |
| `phase` | one canonical phase token or `UNCLASSIFIED` |
| `trustedOutcome` | actual controlling legacy/reviewer disposition with evidence reference |
| `machineOutcome` | advisory P2/AAF result over the associated autorun pass-receipt only; never a semantic review disposition |
| `samePayloadEvidence` | R1B evidence that validator and readout observed the identical in-memory receipt payload within one call chain; no phase-return/receipt identity claim |
| `trustedRecordOrderEvidence` | pre-shadow Git commit and blob proving the controlling trusted disposition was immutable before shadow readout generation or disclosure |
| `blindSpotDisposition` | C07/C08/C18 or another named unrepresented class remains visible |
| `divergenceClass` | one exact class from the table below |
| `auditReason` | high-risk, divergence, deterministic clean sample, or none |
| `auditDisposition` | reviewer comparison result; never a recreation of phase work |
| `costEvidence` | existing Review Cost values plus local command duration/count when available |
| `controllingOutcome` | always the trusted route during P4 shadow mode |

Allowed divergence classes:

- `ENVELOPE_CONSISTENT_WITH_TRUSTED`
- `MACHINE_STRICTER`
- `TRUSTED_ROUTE_STRICTER`
- `EVIDENCE_INCOMPLETE`
- `IDENTITY_OR_SOURCE_DRIFT`
- `COMPARISON_OBJECT_MISMATCH`
- `BLIND_SPOT_NOT_REPRESENTABLE`
- `UNEXPLAINED_DIVERGENCE`

`ENVELOPE_CONSISTENT_WITH_TRUSTED` means only that the mechanical receipt does
not contradict the trusted semantic disposition on fields both actually
represent. It is consistency evidence, never correctness, semantic equivalence
or route-replacement evidence. Missing, partial or weakly linked data cannot
be mapped to that class.

## Common-Mode And Independent-Detector Boundary

Both routes may miss the same defect. Therefore no consistency rate, including
100%, is a safety-success or correctness metric. Every canary decision must
enumerate classes not detectable by either compared route; the minimum set is
C07, C08 and C18. All such classes are excluded from safety denominators and
promotion claims.

For each sampled non-divergent record, the independent audit checks one
predeclared hard obligation directly against the immutable return and its
declared evidence. This invariant check is selected before machine disclosure
and does not rely on either route's outcome label. It is a bounded escape
detector, not a re-performance of the phase. Novel common-mode semantic defects
outside that invariant remain `NOT_DETECTED_WITH_CURRENT_EVIDENCE` and must be
disclosed. If the future P4 work order cannot name this independent invariant
and its evidence locator before execution, the roadmap's independent-detector
requirement remains undischarged and P4 cannot start.

## Independent Detector Boundary

The independent audit checks only:

1. comparator identities, pair linkage and trusted-record ordering evidence;
2. whether limitations, not-checked scope and `UNCLASSIFIED` items survived;
3. one source/authority binding and one declared hard obligation;
4. whether the trusted and machine outcomes were classified honestly;
5. whether immutable trusted disposition predates machine disclosure and
   whether any machine output was converted into review advice or authority.

The audit must not repeat the phase, regenerate the deliverable, rerun every
semantic decision, or inspect agent reasoning. Its closed input manifest is:

- the immutable phase-return blob;
- only evidence paths and authority sources declared by that return, at their
  pinned identities;
- the associated receipt and its verifier/readout identities;
- the predeclared hard-obligation locator; and
- the comparator row.

Any read, command or evidence source outside that manifest, or any regeneration
or semantic re-execution command, records `AUDIT_INPUT_SCOPE_EXCEEDED` and one
duplicated-semantic-work occurrence. This is observable from the audit command
trace and actual input manifest; it is not a reviewer opinion about effort.

A sampled non-divergent audit that cannot be completed from this closed input
set is itself a canary finding:
`EVIDENCE_ENVELOPE_INSUFFICIENT`; it is not permission to redo the author's
work silently.

The ordinary trusted disposition must already exist as a Git commit/blob before
the shadow readout is generated or revealed. That pre-shadow identity is
written to `trustedRecordOrderEvidence`. A missing or non-ancestor identity is
`ORDER_OF_RECORD_UNPROVEN` and returns `ROLLBACK_SHADOW`; no reviewer assertion
can substitute for it. This reuses the ordinary material commit; the canary
must not demand an extra commit. A return without that existing record is
ineligible rather than a reason to add governance work.

## Governance-Tax Ledger

Reuse the Review Cost owner for provider calls, token/quota availability,
review rounds, commits and elapsed review minutes. The canary adds only
ephemeral comparison measurements that change the P4 decision:

| Measure | Treatment |
|---|---|
| existing trusted-route duration/commands | unavoidable baseline; never counted as canary cost or saving |
| shadow machine duration and extra command count | recurring marginal governance tax |
| sampled non-divergent audit minutes | recurring sampling tax |
| divergence/high-risk diagnosis minutes | safety investigation cost, recorded separately from clean-path tax |
| cache hit/miss and reused receipt count | evidence-reuse observation, never proof of safety by itself |
| provider calls and token/quota | must remain zero for machine execution; unavailable reviewer token data stays explicitly unavailable |
| duplicated semantic work | count `AUDIT_INPUT_SCOPE_EXCEEDED` events from actual input/command manifests; threshold does not inspect reasoning or rely on reviewer self-classification |

No projected saving is an observed saving. During shadow mode the trusted route
still controls, so P4 can establish safety and marginal cost but cannot claim
that a legacy review was actually avoided.

## Tax Budget And Promotion Thresholds

Safety gates are evaluated before cost. A canary is ineligible for promotion
unless all safety rows pass.

| Gate | Threshold |
|---|---|
| zero-tolerance escape | 0 |
| machine closure where trusted route blocks | 0 |
| unexplained divergence | 0 |
| hidden limitation, not-checked scope or `UNCLASSIFIED` item | 0 |
| provider/live/network call caused by canary | 0 |
| extra shadow command | at most one per eligible return; consume existing receipts where valid |
| sampled non-divergent independent audit | exactly `k = min(4, max(1, ceil(0.20 * n)))` lowest-digest records for `n >= 1`; zero for `n = 0` |
| duplicated semantic work on sampled non-divergent records | 0 observable `AUDIT_INPUT_SCOPE_EXCEEDED` events; any occurrence requires evidence-envelope correction before promotion |
| common-mode disclosure | minimum C07/C08/C18 plus every newly observed undetectable class; consistency rate excluded from correctness and safety-success claims |
| independent invariant detector | one predeclared hard obligation and evidence locator per sampled record; missing locator blocks P4 execution |
| machine-path median duration diagnostic | no more than 10% of trusted-route median only when at least five same-unit paired durations already exist; expected usually inapplicable because Review Cost permits trusted duration to be unavailable |
| cost evidence availability | missing duration/token evidence is disclosed and blocks a cost-saving claim, not the safety observation |

The median row is a conditional cost diagnostic, not a safety or promotion
gate. It cannot require new reviewer timing collection, and no cost-saving
claim may rest on it when unavailable. No p95 statistic is used in this
20-return window.

Passing the remaining thresholds does not prove correctness or activate a
lighter route. It only permits a separate P5 decision to consider which
deterministic checks, if any, may replace repeated deterministic reviewer work.

## Blind-Spot Treatment

R1A-R1 established that C07, C08 and C18 are not representable by current P2.
They remain outside machine recall denominators and are never counted as PASS.

- C07 verifier self-attestation remains independently controlled.
- C08 earlier-batch verifier/shared-dependency drift remains bound to H0 source
  identity evidence rather than inferred from one payload.
- C18 high-risk/live/public/destructive authority always stays on the trusted
  conservative route because current P2 carries no such authority field.

A canary that looks efficient only by excluding these blind spots cannot pass.

## Rollback And Stop Conditions

Return `ROLLBACK_SHADOW` and preserve all evidence when any safety threshold
fails, trusted record order is unproven, machine advice is disclosed before the
trusted disposition becomes immutable, sampling is selected after seeing
outcomes, or the route cannot be disabled without changing the trusted result.

Return `SIMPLIFY_CANARY_TAX_EXCEEDED` when sampled audit exceeds the single
formula, more than one marginal machine command is added, an extra packet is
demanded per phase, or `AUDIT_INPUT_SCOPE_EXCEEDED` is recorded. The conditional
median diagnostic cannot fire this token when its paired evidence is absent.

Rollback means stop producing/consuming shadow comparator rows and continue
the existing trusted route unchanged. This design does not claim a runtime
config switch exists. A P4 implementation must prove its actual local rollback
mechanism before the first canary observation.

## Acceptance Criteria

The design is acceptable only if an independent reviewer confirms:

- canary execution is still blocked by R1B and a fresh P4 work order;
- trusted review remains controlling throughout shadow mode;
- no synthetic phase work or per-phase packet is required;
- audit selection is deterministic and bounded;
- reviewer audit evaluates results without recreating author work;
- the semantic phase return and mechanical pass-receipt are disclosed as
  different objects and weak linkage is fail-closed;
- the trusted disposition is immutable before shadow readout disclosure;
- consistency is never represented as correctness or route equivalence;
- the audit input/command manifest makes duplicated semantic work observable;
- all three current P2 blind spots remain explicit;
- safety thresholds precede cost thresholds;
- governance-tax measures separate unavoidable baseline, clean-path tax and
  safety-investigation cost;
- no projected saving is presented as observed;
- rollback preserves evidence and requires no provider or external effect.

## Evidence / Verification

This design binds the ratified oracle and its independent review by exact file
SHA-256, retains the roadmap's R1B-before-P4-execution dependency, reuses the
existing Review Cost owner and draws only the advisory comparator/rollback
pattern from TPGR-R7. Gate PASS on this file proves document compatibility,
not canary safety, cost value, R1B acceptance or P4 readiness.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| P4 mission and stop rules | governed roadmap | `docs/roadmaps/CVF_GCLH_MACHINE_FIRST_REVIEW_PREFLIGHT_ROADMAP_2026-09-01.md` | Work Plan; Metrics And Value Test; Rollback And Kill Conditions; Cost And Complexity Budgets | MFRP-P4 shadow canary | MFRP roadmap | ACCEPT |
| R1B execution prerequisite | governed design | `docs/assessments/CVF_MFRP_P3_R1_ACTUAL_SEAM_REPLAY_AND_COMMITTED_ORACLE_REDESIGN_2026-09-01.md` | Tranche Split; Actual P2 Seam Contract; Acceptance And Stop Conditions | R1B before actual P4 | MFRP R1 design | ACCEPT |
| oracle coverage and blind spots | ratified machine data and review | `docs/reviews/CVF_MFRP_P3_R1A_R1_STATIC_ONLY_ORACLE_CORRECTION_WORKER_RETURN_2026-09-02.md` | independent review; feasibility reconciliation | C07, C08, C18 | ratified R1A-R1 evidence | ACCEPT |
| cost-field ownership | canonical standard | `docs/reference/review_cost_control/CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md` | Required Fields; Single-Pass Review Latency SOP | review-cost telemetry | Review Cost owner | ACCEPT |
| advisory comparison precedent | accepted documentary design | `docs/assessments/CVF_TPGR_R7_DUAL_RUN_CANARY_AND_ROLLBACK_REHEARSAL_DESIGN_2026-08-18.md` | Comparator Record; Rollback Rehearsal; Cost And Value | shadow-only comparison pattern | TPGR-R7 evidence only | ACCEPT |
| F-01 through F-08 critique | independent governed review | `docs/reviews/CVF_MFRP_P4_SHADOW_CANARY_AND_GOVERNANCE_TAX_BUDGET_DESIGN_EXTERNAL_CRITIQUE_2026-09-02.md` | Findings; Mandatory Corrections Before R1B; Final Disposition | Revision 1 correction set | critique evidence only; no execution authority | ACCEPT |

## Epistemic Process Block

### Expected Result / Prediction

A useful canary can obtain independent escape detection without doubling
semantic review or constraining agent implementation behavior.

### Evidence Comparison

The roadmap requires an independent detector and safety-first rollback, while
R1A-R1 exposes three machine blind spots and Review Cost forbids reviewer
work-by-drip. The critique showed that phase returns and pass-receipts are
different objects, consistency is not correctness, order must be evidenced,
and audit scope must be observable. Revision 1 uses a closed input manifest,
pre-shadow Git identity, one fixed sample formula and one predeclared invariant
without auditing every return twice.

### Contradiction Or Gap Disposition

P4 cannot yet produce observed safety or cost results because Revision 1 is not
independently accepted, R1B is not accepted and no canary has run. The current
P2 route evaluates a pass-receipt, not the phase return. All thresholds remain
design requirements; none is reported as achieved.

### Claim Update

Revision 1 may be independently reviewed before R1B. R1B authoring remains
closed until that review accepts the corrections, and canary execution remains
dependent on accepted R1B evidence and a separate P4 work order.

## Risk / Corrective Action

The primary risk is false confidence from treating cross-object consistency as
correctness. The correction is explicit object disclosure, a common-mode
inventory and a bounded invariant detector. The second risk is turning safety
sampling into a permanent second review. The correction is one closed sampling
formula and an observable input/command boundary; all divergences and high-risk
signals still receive full audit.

## Decision / Disposition

`CANARY_DESIGN_REVISION_1_READY_FOR_INDEPENDENT_REVIEW_R1B_RETAINED`

The next action is independent review of Revision 1 against F-01 through F-08.
R1B authoring, R1B execution and P4 execution remain separate operator
checkpoints; none is opened here.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | assessment source/decision/evidence heading groups; checker-read-ahead four fields; assessment path applicability; epistemic four-part markers; public disposition heading |
| gateRunPurpose | confirmation evidence that the canary design is structurally compatible after source-led authoring, not first discovery of design semantics |
| claimBoundary | source read-ahead and gate compatibility only; no canary execution, effectiveness, cost saving or activation is proven |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | CVF canary designer/orchestrator |
| Provider or surface | local private provenance repository |
| Session or invocation | MFRP-P4-D0 Revision 1 after independent critique, 2026-09-02 |
| Working directory | repository root |
| Command or tool surface | governed reads, hash recomputation, text search, apply_patch and local governance gates |
| Target paths | `docs/assessments/CVF_MFRP_P4_SHADOW_CANARY_AND_GOVERNANCE_TAX_BUDGET_DESIGN_2026-09-02.md` |
| Allowed scope source | operator instructed canary handling before the next implementation tranche |
| Before status evidence | Revision authoring began at `c1d1cbeef`; critique was preserved at `e79308d2c`; correction checkpoint `7a3172acf` is the final execution base |
| After status evidence | one modified design; committed critique unchanged; no implementation or runtime path |
| Diff evidence | exactly one modified design after critique evidence commit |
| Approval boundary | design the canary first; no R1B/P4 execution or activation |
| Claim boundary | repository-local documentary design only |
| Agent type | designer/orchestrator |
| Invocation ID | `mfrp-p4-d0-shadow-canary-design-revision-1-2026-09-02` |
| Expected manifest | `docs/assessments/CVF_MFRP_P4_SHADOW_CANARY_AND_GOVERNANCE_TAX_BUDGET_DESIGN_2026-09-02.md` |
| Actual changed set | `docs/assessments/CVF_MFRP_P4_SHADOW_CANARY_AND_GOVERNANCE_TAX_BUDGET_DESIGN_2026-09-02.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private design-only canary planning with no public-sync authorization.

## Claim Boundary

This assessment defines a future shadow-canary contract only. It does not run
a canary, implement R1B/P4, modify P2, alter trusted review authority, create a
new telemetry/reference family, activate a lighter route, change downstream
workspaces or authorize provider/live/network/public/deploy/production action.
