# CVF ACEL G1 T3B Group 2 Source Creation Tooling Worker Return

Memory class: governed-worker-return

docType: review

Status: COMPLETE_PENDING_REVIEW

Batch ID: ACEL-G1-T3B-R2-ATOMIC-ROTATION-CONTRACT-CORRECTION

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: shared-workspace `INTERNAL_AGENT` correction worker

dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3B_R2_ATOMIC_ROTATION_CONTRACT_CORRECTION_2026-09-20.md`

Self-declared worker-return artifact: yes

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3B_R2_ATOMIC_ROTATION_CONTRACT_CORRECTION_2026-09-20.md`

independentProbeRequired: YES

independentProbeDisposition: PENDING_REVIEWER_EXECUTION

executionBaseHead: `d87a01115f1d37991bf90d2ac0cbcbf9c4e27362`

## Purpose

This is the R2 correction pass over the Group 2 tooling tranche. It replaces
the R1 supersession model, which Local's independent review
(`docs/reviews/CVF_ACEL_G1_T3B_R1_GROUP2_TOOLING_COHERENCE_CORRECTION_COMPLETION_2026-09-20.md`,
SHA-256 `64475b405e5f7886f2f9faecf6f50be13c95c8c7a6e5c1cd97260219630fe62e`)
found genuinely impossible to satisfy (T3B-R1-RV-1: the required prerequisite
state -- two simultaneously active versions -- is unreachable by the same
replay that must accept it; T3B-R1-RV-2: the closed decision-event schema had
no field durably naming a `SUPERSEDED` event's replacement version), with a
single atomic rotation event. It supersedes the prior version of this same
file; it is not a new artifact. This return does not authorize, and does not
claim, real Group 2 source creation, approval, activation, consumer wiring,
candidate admission, staging, commit, or any provider/live/public/deployment
effect.

## Scope / Methodology

Captured `executionBaseHead` via `git rev-parse HEAD` at the start of this R2
pass (`d87a01115f1d37991bf90d2ac0cbcbf9c4e27362`) and confirmed `git status
--short --untracked-files=all` showed exactly the eighteen pre-existing
uncommitted paths already present in the working tree at session start
(thirteen unrelated parked paths plus the five T3B outputs this worker owns),
with staging empty. Read the R2 work order in full, the R1 completion review
in full, the T2F Group 2 contract, the R1 worker return, and all five current
outputs in full before making any change, per the R2 packet's Required First
Reads.

Repaired the atomic rotation architecture across the exact five-path
manifest; created no sixth path; touched no parked path; confirmed
`scripts/acel_g1_party_a_group2_spec_writer.ps1` remains byte-identical
(disposition: `MATCH`; SHA-256
`226b081d20f7e1aaf0c0b672c0dd004ebd53bd0b2350ca87ac38e829c7cb62e6` before and
after this pass, per `sha256sum` in the Command Evidence section below) and its own
48/48 self-test still passes unmodified; never created, wrote to, or
otherwise touched either real Group 2
source path (`governance/sources/verification_authority_spec/SPEC_v1.json`
or `.../ACTIVATION_DECISIONS.jsonl`, both confirmed absent throughout and
after this pass); never used credentials, `runas`, or alternate-principal
execution.

Role: shared-workspace `INTERNAL_AGENT` correction worker. Phase: R2 hermetic
tooling correction only; real Party A/approver principal-separated execution
remains operator-only and did not occur. Decision owner: Local
orchestrator/reviewer.

## Target / Source

- R2 governing work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3B_R2_ATOMIC_ROTATION_CONTRACT_CORRECTION_2026-09-20.md`
- R1 completion review (two findings): `docs/reviews/CVF_ACEL_G1_T3B_R1_GROUP2_TOOLING_COHERENCE_CORRECTION_COMPLETION_2026-09-20.md`; SHA-256 `64475b405e5f7886f2f9faecf6f50be13c95c8c7a6e5c1cd97260219630fe62e`
- T2F Group 2 operational source contract (repaired in place): `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md`
- Five worker outputs (this batch, modified in place except the frozen spec writer, which is untouched and not part of this five-path manifest): listed in full in `## Changed Files` below.

## Findings / Position

Both R1 findings are addressed as follows.

**T3B-R1-RV-1 (CRITICAL, unreachable supersession state) -- RESOLVED.** The
contradictory "replacement must already be `ACTIVATED` before it can
supersede the still-active old version" prerequisite is removed entirely.
`docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md`'s
new `#### Atomic Rotation: Explicit Approval, Activation And Supersession
(T2F-R4-01)` subsection defines one atomic event: `SUPERSEDED(old,
replacement)` requires the active set be exactly `{old}` beforehand and, in
one state transition, removes `old` and adds `replacement`, never
materializing a two-active or zero-active intermediate state. Both
`scripts/acel_g1_approver_group2_decision_writer.ps1`'s `Get-DecisionHistoryState`
and `governance/compat/check_acel_g1_verification_authority_spec.py`'s
`validate_decision_history` implement this identically: ordinary `ACTIVATED`
requires an empty active set (never permitted while any version, including a
direct predecessor, is active); `SUPERSEDED` performs the atomic swap in one
step. The exact sequence the R1 review's admitted probe proved unreachable --
`APPROVED(v1) -> ACTIVATED(v1) -> APPROVED(v2) -> SUPERSEDED(v1,
replacement=v2)` -- now passes and ends with v2 as the sole active version
(PowerShell `T3B-08-V`/`T3B-08-W`; Python
`test_required_regression_1_atomic_rotation_ends_with_replacement_sole_active`).
A standalone ordinary `ACTIVATED(v2)` while v1 remains active still fails
closed (PowerShell `T3B-08-U`; Python
`test_required_regression_4_ordinary_activation_while_active_still_rejected`).
A replacement activated by rotation can itself later be superseded again,
rotating to v3 (PowerShell `T3B-R2-CHAINED-ROTATION`; Python
`test_replacement_can_itself_be_superseded_later`), and a later duplicate
ordinary `ACTIVATED(replacement)` is still rejected (PowerShell
`T3B-R2-DUP-ACTIVATE-REPLACEMENT`; Python
`test_duplicate_activation_of_replacement_after_rotation_rejected`).

**T3B-R1-RV-2 (HIGH, unbound durable replacement) -- RESOLVED.** The closed
`cvf.specDecisionEvent` preimage and durable record now include
`replacementSpecVersion` and `replacementRecomputedHashHex` as required,
always-present fields: both `null` for `APPROVED`/`REJECTED`/ordinary
`ACTIVATED`; both required non-null for `SUPERSEDED`, where
`replacementSpecVersion` must be a positive integer strictly greater than the
event's own `specVersion` and `replacementRecomputedHashHex` is the
independently recomputed raw-content hash of the replacement's own spec
file. `New-DecisionEventPreimage`'s new `Assert-ValidReplacementFieldPair`
guard and the Python `validate_replacement_field_pair` function enforce this
identically, including rejecting a one-null/one-non-null pair regardless of
event type. `Invoke-GroupTwoDecisionAppend` folds the proposed `SUPERSEDED`
event into a trial replay before ever appending, so the same atomic-swap
logic that later re-validates the file from genesis proves the rotation
legal beforehand. The `-ReplacementSpecVersion` PowerShell invocation
parameter is no longer discarded before hashing: it is threaded into
`New-DecisionEventRecord` and stored, hash-chained, in the durable record.

## Required Regression Coverage

| # | Class | PowerShell case(s) | Python case(s) |
|---|---|---|---|
| 1 | Positive: `APPROVED(v1)->ACTIVATED(v1)->APPROVED(v2)->SUPERSEDED(v1,replacement=v2)` passes, replay ends with v2 sole active | `T3B-08-V`, `T3B-08-W` | `test_required_regression_1_atomic_rotation_ends_with_replacement_sole_active` |
| 2a | Missing replacement fields | `T3B-R2-NEG-MISSING-REPLACEMENT-FIELDS` | `test_missing_replacement_fields_rejected` |
| 2b | One-null/one-non-null pair | `T3B-R2-NEG-ONE-NULL-ONE-NONNULL-A`/`-B` | `test_one_null_one_nonnull_replacement_fields_rejected`, `test_replacement_fields_on_approved_event_rejected` |
| 2c | Replacement equal/lower than old | `T3B-R2-NEG-REPLACEMENT-EQUAL`, `T3B-R2-NEG-REPLACEMENT-LOWER`, `T3B-R2-NEG-ASSERT-VALID-REPLACEMENT-NOT-GREATER` | `test_replacement_equal_to_old_rejected`, `test_replacement_lower_than_old_rejected` |
| 2d | Replacement never approved | `T3B-R2-NEG-REPLACEMENT-NEVER-APPROVED` | `test_replacement_never_approved_rejected` |
| 2e | Replacement already active / already superseded | `T3B-R2-NEG-REPLACEMENT-ALREADY-ACTIVE`, `T3B-R2-REPLACEMENT-ALREADY-ACTIVE-UNREACHABLE`, `T3B-R2-REPLACEMENT-ALREADY-ACTIVE-SOURCE-PRESENT`, `T3B-R2-NEG-REPLACEMENT-ALREADY-SUPERSEDED` | `test_replacement_already_superseded_and_already_active_guards_present_and_ordered` (both classes are structurally unreachable via legitimate sequential replay -- the unique-active invariant and strictly-increasing rotation numbering make two simultaneously-eligible candidates impossible to construct honestly; both guards' presence, correct field keying and correct check ordering are verified directly, and the reachable ground-truth outcome, `DECISION_MULTIPLE_ACTIVE_VERSIONS`, is proven by regression class 4) |
| 2f | Replacement spec file missing | `T3B-R2-NEG-REPLACEMENT-FILE-UNRESOLVED` | `test_replacement_spec_file_missing_rejected` |
| 2g | Replacement cited hash wrong | `T3B-R2-NEG-REPLACEMENT-HASH-MISMATCH` | `test_replacement_cited_hash_wrong_rejected` |
| 3 | Mutating/removing either durable field invalidates digest | `T3B-R2-NEG-TAMPER-REPLACEMENT-VERSION`, `T3B-R2-NEG-TAMPER-REPLACEMENT-HASH`, `T3B-R2-NEG-REPLACEMENT-FIELD-OMITTED` | `test_mutating_either_replacement_field_invalidates_digest` |
| 4 | Standalone ordinary `ACTIVATED(v2)` while v1 active still rejected | `T3B-08-U` | `test_required_regression_4_ordinary_activation_while_active_still_rejected` |
| 5 | Cross-language convergence on one identical event history | (writer functions exercised by the Python-side probe) | `test_cross_language_atomic_rotation_replay_converges` |

Regression class 2e's two sub-guards (`DECISION_SUPERSESSION_REPLACEMENT_ALREADY_ACTIVE`,
`DECISION_SUPERSESSION_REPLACEMENT_ALREADY_SUPERSEDED`) are proven present,
correctly field-keyed (current `activeVersions`/`active_versions` membership
for the active guard, never the historical-only `HasActivated`/`has_activated`
flag which never resets to `false`) and correctly ordered (already-superseded
checked before already-active, so an already-superseded candidate is never
misreported as merely already-active) by direct source inspection, because
constructing a genuinely legitimate sequential-replay fixture that reaches
either branch is structurally impossible: the unique-active invariant this
whole atomic rotation model enforces means only one version can ever be
active at a time, and rotation only ever assigns strictly increasing version
numbers, so an already-superseded candidate is always numerically smaller
than whatever is currently active. Both guards remain correctly-wired
defense-in-depth against a hand-tampered durable record.

## Failing-Before / Passing-After Regression Proof

| Finding | Regression case | Pre-R2 (R1) behavior | Post-R2 behavior |
|---|---|---|---|
| T3B-R1-RV-1 | PowerShell `T3B-08-V`/`T3B-08-W`; Python `test_required_regression_1_atomic_rotation_ends_with_replacement_sole_active` | The R1 guard required `-ReplacementSpecVersion` to already have its own prior `ACTIVATED` event before `SUPERSEDED` could be appended against the still-active old version; full-history replay independently rejects two simultaneously `ACTIVATED`-without-`SUPERSEDED` versions, so this prerequisite state could never be constructed. R1's own positive test (`T3B-08-V`/`T3B-08-W` at R1) instead built a history where v1 was ALREADY superseded before v2 activated, never exercising the real transition. | `SUPERSEDED` itself performs the old-to-replacement atomic swap; the replacement needs only a prior `APPROVED` event, never pre-activation. The exact `APPROVED(v1)->ACTIVATED(v1)->APPROVED(v2)->SUPERSEDED(v1,replacement=v2)` sequence now passes and replay ends with v2 as the sole active version. |
| T3B-R1-RV-2 | Python `test_mutating_either_replacement_field_invalidates_digest` | The R1 closed `cvf.specDecisionEvent` preimage contained only `decisionEventId`, `eventType`, `specVersion`, `recomputedHashHex`, `approverId`, `decidedAt`, `priorEntryHashHex`; `-ReplacementSpecVersion` existed only as a PowerShell invocation parameter, discarded before hashing/appending, so no durable field proved which replacement version a `SUPERSEDED` event was for. | `replacementSpecVersion`/`replacementRecomputedHashHex` are required closed-preimage fields on every event; tampering or removing either field after a valid event is built produces a digest mismatch or a missing-field rejection, proving the hash calculation genuinely depends on both fields. |

Test count delta: R1 return reported 48/48 (spec writer, unchanged),
63/63 (decision writer), 47/47 (Python). This R2 return reports 48/48 (spec
writer, byte-identical and unmodified), 74/74 (decision writer, +11 net
atomic-rotation cases replacing the non-discriminating R1 supersession
tests), 58/58 (Python, +11 net atomic-rotation cases). All originally-passing,
unaffected cases remain green.

## Risk / Corrective Action

| Risk | Corrective action taken |
|---|---|
| PowerShell parameter binding: a `[string]`-typed parameter passed `$null` from a caller silently coerces to an empty string (`""`), not actual `$null`, unlike an untyped parameter. `New-DecisionEventPreimage`/`New-DecisionEventRecord`'s initial `[AllowNull()][string] $ReplacementRecomputedHashHex` declaration therefore made every non-`SUPERSEDED` event fail the new pairing guard (`replacementSpecVersion` correctly null, `replacementRecomputedHashHex` incorrectly `""`), breaking the entire self-test at the very first genesis `APPROVED` event. | Removed the `[string]` type constraint (disposition: `MATCH`; now matching the existing untyped `$PriorEntryHashHex` pattern already used elsewhere in this file for the same reason), so `$null` stays `$null` through parameter binding. Re-ran the full self-test to confirm the fix and add no further type-coercion traps. |
| `DECISION_SUPERSESSION_REPLACEMENT_ALREADY_SUPERSEDED` was originally unreachable in both languages: `HasActivated`/`has_activated` is a historical "was ever activated" flag that never resets to `false` after a version is later superseded, so the already-active check (`if HasActivated`) always fired first for ANY previously-activated version, including an already-superseded one, masking the more specific already-superseded taxonomy id entirely. | Reordered both languages' checks to test `HasSuperseded`/`has_superseded` FIRST, then test current `activeVersions`/`active_versions` membership (not the historical flag) for the already-active case. Verified both branches are now independently reachable and correctly ordered by direct source inspection, since a genuinely legitimate sequential-replay fixture reaching either branch is structurally impossible (see `## Required Regression Coverage` above). |
| The R2 atomic-rotation Python test additions initially pushed `governance/compat/test_check_acel_g1_verification_authority_spec.py` to 1321 lines, exceeding the governed `python_test` hard line-count threshold (1200) with no approved exception. | Consolidated repeated fixture-construction boilerplate into shared `AtomicRotationTests` helper methods (`_v1_approved_activated`, `_v2_record`, `_approve_v2_from`, `_supersede`), merged three separate digest-tamper tests into one grouped test, and compressed the cross-language PowerShell probe-script generation, reducing the file to 1082 lines while preserving every required regression assertion. Confirmed `governed python automation size` passes after the reduction. |
| Several early attempts to construct hermetic fixtures for the already-active/already-superseded replacement guards produced internally inconsistent PowerShell test scenarios (e.g. citing a replacement version with no prior `APPROVED` event, or building an `ACTIVATED` event for a version while another was already active, which the ACTIVATED branch itself rejects before the intended guard is ever reached). | Iteratively corrected each fixture by tracing the exact guard-check order in the implementation, then, once confirming both target states are structurally unreachable via legitimate sequential replay (a mathematical consequence of the unique-active invariant and strictly-increasing rotation numbering), switched to direct source-presence and check-ordering verification for those two specific guards, which honestly and correctly proves they exist and are correctly wired without asserting a fixture that cannot legitimately exist. |
| The pre-implementation autorun gate reports `[FAIL] independent review probe admission` and `[FAIL] agent automation assist early diagnostics` for PRE-EXISTING unrelated worker-return docs (`CVF_ACEL_G1_T2A_...`, `CVF_ACEL_G1_T2B_...`, `CVF_ACEL_G1_T2_TASK_CLASS_CALIBRATION_OWNER_...`) among the thirteen parked paths. | Not repaired (out of allowed scope; those paths are explicitly forbidden to touch by the R2 work order's Allowed Scope / Forbidden Scope section). Disclosed here rather than silently worked around; confirmed present and unrelated to this worker's five paths both before and after this pass. |

## Decision / Disposition

Status: `COMPLETE_PENDING_REVIEW`.

Both R1-review findings (T3B-R1-RV-1, T3B-R1-RV-2) are corrected in place via
the atomic rotation model across the exact five-path manifest. The
PowerShell decision writer passes its full hermetic self-test (74/74,
including all atomic-rotation regression cases). The spec writer remains
byte-identical to its pre-R2 content (SHA-256
`226b081d20f7e1aaf0c0b672c0dd004ebd53bd0b2350ca87ac38e829c7cb62e6`, unchanged)
and its own self-test still passes unmodified (48/48). The Python checker and
its focused suite pass cleanly (58/58). `git diff --check` is clean; staging
is empty; both real Group 2 source paths remain absent throughout.

Real Group 2 source creation, approval, activation, consumer binding, and
candidate admission: `NOT_CLAIMED_AND_NOT_ATTEMPTED`.

Local orchestrator/reviewer next move: run the admitted independent atomic
rotation positive control and replacement-field mutation probes, evaluate the
five paths against the R2 atomic rotation contract, and accept/reject/repair.
This return does not self-accept, stage, or commit its own outputs.

## Claim Boundary

This return authorizes exactly the five Required Artifact Manifest paths as
corrected, uncommitted, hermetically self-tested tooling. It does not
authorize or claim: credential access; `runas` or alternate-principal
execution; creation of either real Group 2 source path
(`governance/sources/verification_authority_spec/SPEC_v1.json` or
`.../ACTIVATION_DECISIONS.jsonl`, both confirmed absent throughout and after
this work); spec approval or activation; consumer/T3E wiring; candidate
admission; staging; commit; or any provider/live, runtime, public-sync, or
deployment effect. All dispositions are subject to independent Local review.

## Review Dispatch Convergence And Invocation Budget Control

rootCauseClusterId: `acel-g1-t3b-group2-atomic-rotation`

reworkGeneration: 2

consolidatedDefectClassSweep: COMPLETE_ALL_KNOWN_DEPENDENCIES

productionBindingEvidence: N/A_NO_PRODUCTION_BINDING_PURE_OFFLINE_TOOLING_ONLY

adversarialRegressionDisposition: PASS_TARGETED_DEFECT_CLASS

successorTrancheOpened: NO

implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY

internalAgentInvocationCount: 1

externalAgentInvocationCount: 0

providerCallCount: 0

tokenOrQuotaUsage: NOT_AVAILABLE_WITH_REASON: no provider-neutral usage meter is available in this offline session

terminalReadinessVerdict: READY_FOR_REVIEW

## Core Guard Self-Protection Authorization

Operator authorization: the R2 governing work order
(`docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3B_R2_ATOMIC_ROTATION_CONTRACT_CORRECTION_2026-09-20.md`)
explicitly authorizes correction of the two named files below in its own
`## Core Guard Self-Protection Authorization` section. The other two
protected paths listed below
(`governance/compat/check_task_class_calibration_owner_evidence.py`,
`governance/compat/test_check_task_class_calibration_owner_evidence.py`) are
pre-existing untracked files from an unrelated prior task that this R2 worker
did not create, edit, or otherwise touch; they are listed here only because
the `governance/compat/*.py` protected-path pattern matches every Python file
under that directory currently present in the working tree, and the checker
requires every currently-matching protected path to be named, not only the
ones this worker modified.

Authorized guard-maintenance scope: bounded R2 correction of the Group 2
read-only checker and its focused test only (atomic rotation replay
semantics and both durable replacement fields); no hook/catalog/general-guard
changes and no modification to any other existing `governance/compat/*.py`
file.

Protected paths:

- `governance/compat/check_acel_g1_verification_authority_spec.py`
- `governance/compat/test_check_acel_g1_verification_authority_spec.py`
- `governance/compat/check_task_class_calibration_owner_evidence.py`
- `governance/compat/test_check_task_class_calibration_owner_evidence.py`

Rollback boundary: both R2-corrected files remain uncommitted until Local
accepts; rollback is deletion/reversion of only the five owned uncommitted
outputs to their pre-R2 (R1 worker return) content; the other two listed
protected paths belong entirely to the unrelated prior task and this worker
takes no action on them, has no rollback responsibility for them, and did not
modify them in any way.

## ADIF Defect Registry Disclosure

Dispatcher query for `CODE_CHANGE`/dispatcher/dispatch returned
`NONE_RETURNED` per the R2 work order. Worker rerun for
`CODE_CHANGE`/`worker`/`implementation`: no external ADIF registry query
mechanism is wired into this offline tooling tranche; self-found and
self-fixed defects are disclosed in full in `## Risk / Corrective Action`
above. Returned defects: NONE_RETURNED.

## Semantic Convergence Outcome

```json
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"acel-g1-t3b-r2-atomic-rotation-implementation-evidence","chainMode":"INITIAL","chainOrdinal":0,"predecessor":null,"blockerDelta":{"prior":[],"resolved":[],"retained":[],"new":["group2-tooling-r2-worker-evidence-pending-local-review"],"reopened":[],"current":["group2-tooling-r2-worker-evidence-pending-local-review"]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":0,"nonDecreasingBlockerTransitions":0},"claims":[{"claimId":"ACEL-G1-T3B-R2-ATOMIC-ROTATION","claimClass":"OTHER","proofClass":"NAMED_OBSERVABLE_PROOF","evidenceRef":"governance/compat/test_check_acel_g1_verification_authority_spec.py"}],"requiredDisposition":"CONTINUE_BOUNDED","successorScope":"INITIAL_BOUNDED"}
```

This block deliberately does NOT chain as a `SUCCESSOR` against the R2 work
order's own SCEC block
(`docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3B_R2_ATOMIC_ROTATION_CONTRACT_CORRECTION_2026-09-20.md`,
`requiredDisposition: STOP_REASSESS_ARCHITECTURE`), per Enforcement
Invariant 7 of `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md`:
"A predecessor at `STOP_REASSESS_ARCHITECTURE` cannot have another successor
in the same problem chain." The root
`acel-g1-t3b-group2-source-creation-tooling-problem` chain's escalation to
`STOP_REASSESS_ARCHITECTURE`/`INTEGRATED_ROOT_CONTRACT` remains open and
unresolved by this worker return; only Local's independent review and
closure decision may progress or close that chain. This block instead opens
a fresh, narrowly scoped `INITIAL` chain identifying this specific R2
implementation's own executable evidence as pending Local review -- a
distinct, subordinate problem identity, not a claim of root-chain
progression. The full, individually-evidenced per-finding proof for both
T3B-R1-RV-1 and T3B-R1-RV-2 is in `## Findings / Position`, `## Required
Regression Coverage` and `## Failing-Before / Passing-After Regression
Proof` above; those findings remain formally open in the root chain until
Local independently verifies and closes them there.

## Return-Time Closeability Recheck

closeabilityDisposition: CLOSEABLE

outsideAuthorityBlockers: NONE

nextRepairRoute: N/A with reason: no repair route is open within this
worker's allowed scope; the disclosed pre-existing gate failures
(independent review probe admission and agent automation assist early
diagnostics, both citing unrelated prior-task worker-return docs) are outside
this batch's five owned paths and outside the paths this work order permits
the worker to touch

workerRedispatchAllowed: NO

## Worker Experience Retrospective

WORKER_EXPERIENCE_RETRO:

frictionLevel: MEDIUM

frictionType: ENUM_OR_TOKEN_MISMATCH

observedStep: two real defects were caught during implementation rather than
by an independent reviewer: (1) a PowerShell `[string]`-typed nullable
parameter silently coerced caller-supplied `$null` to `""`, breaking the new
replacement-field pairing guard for every non-`SUPERSEDED` event; (2) the
`DECISION_SUPERSESSION_REPLACEMENT_ALREADY_SUPERSEDED` guard was originally
unreachable in both languages because the historical `HasActivated`/
`has_activated` flag (checked first, pre-fix) never resets to `false` after a
version is superseded, so the already-active check always fired first for
any previously-activated version.

preventiveControlCandidate: HELPER_DIAGNOSTIC

preventiveControlCandidateNote: (1) in PowerShell, prefer an untyped
`[AllowNull()] $Param` over `[AllowNull()][string] $Param` for any parameter
that must preserve a true `$null` through binding, since the typed form
silently coerces `$null` to an empty string. (2) when a state-machine field
tracks "was ever X" alongside a separate "is currently X" concept (here:
`HasActivated` historical vs. current `activeVersions` membership), order
guard checks from most-specific-terminal-state to least-specific, or key the
check on the precise current-state collection rather than the historical
flag, to avoid a broader historical condition silently masking a narrower,
more diagnostic one.

## Machine Closure Package

NOT_APPLICABLE_WITH_REASON: this is a worker-return artifact, not a closure
artifact. Machine closure packaging belongs to Local after the returned
evidence is reviewed and materially committed.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | internal governed input (no external intake) |
| Internal source | `docs/reviews/CVF_ACEL_G1_T3B_R1_GROUP2_TOOLING_COHERENCE_CORRECTION_COMPLETION_2026-09-20.md` |
| Chain map route | N/A with reason: direct internal review -> INTERNAL_AGENT correction -> Local review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | R2 work order and this worker return |
| Disposition | local first-party correction only |
| Claim boundary | no external source authority, corpus, remote implementation or provider claim |

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":"docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3B_R2_ATOMIC_ROTATION_CONTRACT_CORRECTION_2026-09-20.md"}
```

## Rescan Intelligence Hardening

- Original source artifact: N/A with reason: not applicable
- Predecessor intake artifact: N/A with reason: not applicable
- Delta ledger status: N/A with reason: not applicable
- Routing matrix status: N/A with reason: not applicable
- Semantic sampling status: N/A with reason: not applicable
- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

Reason: this worker return corrects five already-declared governed paths in
direct response to the R2 work order's Required Artifact Manifest; it is not
a corpus rescan or intake-refresh of a prior external or internal corpus.

### Original-Intake Delta Ledger

N/A with reason: not applicable; no delta categories apply
(`UNCHANGED_FROM_INTAKE`, `CHANGED_DISPOSITION`, `NEW_FINDING`,
`REMOVED_OR_REJECTED`) because there is no prior intake this return revises.

### Follow-Up Routing Matrix

N/A with reason: not applicable; no routing lane applies (`DO_NOW`,
`SEPARATE_RUNTIME_TRANCHE`, `STRATEGIC_OPERATOR_DECISION`, `OUT_OF_SCOPE`,
`RESOLVED_BY_DESIGN`) because this return is not a rescan.

### Semantic Sampling / Adversarial Review

N/A with reason: not applicable; no semantic sampling row applies
(`sampleId`, `source section`, `source claim`, `disposition checked`,
`adversarial challenge`, `verdict`) because this return is not a rescan.

## Corpus Completeness And Report Integrity

- Corpus task class: bounded named-source correction and focused test
  authoring; no repository-wide completeness claim.
- Corpus root: repo-local source files named in `## Target / Source`.
- Snapshot time: 2026-09-20 R2 worker execution at the recorded execution
  base.
- Enumeration command: filesystem-backed direct file reads and targeted `rg`
  queries over the named sources only.
- Manifest artifact or inline manifest: `## Target / Source` in this return.
- Manifest hash: N/A with reason: bounded named-source execution uses the
  inline inventory and does not generate a standalone corpus manifest.
- Processing ledger artifact or inline ledger: `## Target / Source` rows.
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED |
  BLOCKED_UNREADABLE.
- Reconciliation: manifest=inline Target/Source; ledger_terminal=READ; exclusions=all files outside the named bounded set; unresolved=0.
- Unresolved files: 0 within the named worker source set.
- Declared exclusions: all files outside the R2 work order's five-path
  manifest, including the thirteen parked paths and the frozen spec writer.
- Unreadable or unsupported files: 0 within the named worker source set.
- Aggregation check: N/A with reason: no aggregate is generated.
- Drift check: exact execution base, full status and parked-path isolation
  are recorded; no corpus aggregate is edited.
- Output traceability: source inventory, five-path manifest, command
  evidence and changed-files sections cross-reference this bounded
  execution.
- Adversarial verification: atomic rotation positive, replacement-field
  mutation negatives, digest-dependency negatives and cross-language
  convergence are recorded.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Finding-To-Governance Learning Disposition

- Defect class: `WORKER_EXECUTION_ERROR`
- Learning lane: `GOVERNANCE_CONTROL_PLANE`
- Disposition: `RULE_EXISTS`
- Next control action: the PowerShell typed-nullable-parameter coercion trap
  and the historical-vs-current-state guard-ordering trap are disclosed in
  `## Risk / Corrective Action` and `## Worker Experience Retrospective`
  above as reusable authoring cautions; a new general CVF rule is not
  justified from this single tranche, since both are language/design-level
  footguns rather than governance contract gaps. Recurrence in a future
  tranche would trigger machine-check elevation.
- Runtime/provider/cost learning lane: `N/A_WITH_REASON` -- this tranche is
  pure hermetic offline tooling correction with no provider, runtime, live,
  public, deployment, or cost-economics effect; every mention of
  "runtime"/"provider"/"cost"/"token" in this document (e.g.
  `providerCallCount: 0`, `tokenOrQuotaUsage: NOT_AVAILABLE_WITH_REASON`,
  `no runtime wrapper, proxy, or agent-control claim`) is a claim-boundary
  negation, never a runtime/provider/cost finding requiring its own lane.

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: replacing the two-active-state prerequisite
with one atomic rotation event would make the required v1-to-v2 sequence
pass where it previously could not; adding durable `replacementSpecVersion`/
`replacementRecomputedHashHex` fields would make the digest genuinely depend
on both; and PowerShell/Python replay would converge on the same final
state for one identical event history.

Evidence Comparison: exact match against all three predictions on final
implementation, with two real defects found and fixed during self-testing
(the PowerShell typed-nullable coercion trap, and the already-superseded
guard-ordering trap, both disclosed above) before reaching a clean pass.
Final observed evidence: spec writer 48/48 (byte-identical, unmodified);
decision writer 74/74; Python suite 58/58; cross-language convergence
confirmed; `git diff --check` clean; both real Group 2 source paths absent
throughout; staging empty.

Contradiction Or Gap Disposition: the R1-identified contract-level
contradiction (unreachable prerequisite state) is resolved by the atomic
rotation model; no new contract-level contradiction was found. Two
implementation-level gaps (PowerShell type coercion; guard-check ordering)
were found and resolved within this same worker pass without requiring
escalation.

Claim Update: T3B-R1-RV-1 CONFIRMED_RESOLVED; T3B-R1-RV-2
CONFIRMED_RESOLVED. Reports a hermetically self-tested, worker-complete R2
atomic rotation correction pending Local review; does not claim real Group 2
source creation, approval, activation, consumer binding, or candidate
admission.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/run_worker_return_fast_gate.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_semantic_convergence_control.py`; current Group 2 checker/test |
| literalTokensReviewed | required common groups (title, memory class, status, purpose, scope/target/owner boundary, claim/final/verification boundary); worker-return packet shape required terms (`Self-declared worker-return artifact: yes`, `Responds to work order:`, `dispatchWorkOrder:`, `independentProbeRequired: YES`); `executionBaseHead`; exact Checker Source Read-Ahead / Agent Operation Trace / Delta Execution Claim Boundary Control Block headings and field names; `WORKER_MUST_NOT_COMMIT` no-commit phrase; SCEC block schema fields and resolution-evidence hash binding |
| gateRunPurpose | confirm artifact structural conformance and worker-return packet shape before returning to Local; structural pass proves shape, not implementation correctness |
| claimBoundary | checker pass proves packet/structural shape only; it does not certify the T3B Group 2 tooling's technical correctness beyond the disclosed test evidence, which remains Local's independent review responsibility |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | shared-workspace `INTERNAL_AGENT` correction worker |
| Provider or surface | private CVF workspace only |
| Session or invocation | ACEL-G1-T3B-R2-ATOMIC-ROTATION-CONTRACT-CORRECTION worker execution, 2026-09-20 |
| Working directory | repository root |
| Command or tool surface | governed file reads, `pwsh -NoProfile -File` (both writer self-tests), `python -m py_compile`, `python governance/compat/test_check_acel_g1_verification_authority_spec.py`, `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation`, `python governance/compat/run_worker_return_fast_gate.py`, `git rev-parse HEAD`, `git status --short --untracked-files=all`, `git diff --check`, `git diff --cached --name-only`, `sha256sum` (spec-writer byte-identity confirmation) |
| Target paths | R2 work order, R1 completion review, T2F Group 2 contract, R1 worker return (all read-only); exactly the five worker output paths, modified in place |
| Allowed scope source | R2 work order's Required Artifact Manifest, Allowed Scope / Forbidden Scope, and Write Ownership sections |
| Before status evidence | HEAD `d87a01115f1d37991bf90d2ac0cbcbf9c4e27362`; `git status --short --untracked-files=all` showing exactly the thirteen pre-existing parked paths plus the five T3B outputs; staging empty; both real Group 2 source paths absent; spec-writer SHA-256 `226b081d20f7e1aaf0c0b672c0dd004ebd53bd0b2350ca87ac38e829c7cb62e6` |
| After status evidence | HEAD unchanged at `d87a01115f1d37991bf90d2ac0cbcbf9c4e27362`; exactly the same eighteen paths, none added or removed; staging empty; both real Group 2 source paths remain absent; spec-writer SHA-256 unchanged |
| Diff evidence | `git status --short --untracked-files=all` (reported in full below); `git diff --cached --name-only` (empty: nothing staged); `git diff --check` clean (one benign CRLF/LF line-ending advisory on the T2F contract, exit 0); `git diff --name-status` reports exactly one modified tracked path, `M docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` (the only committed file this worker edited; every other owned path is a modification to an already-untracked file, so it does not appear in a tracked-file diff) |
| Approval boundary | hermetic tooling correction and self-testing only |
| Claim boundary | no credential, alternate-principal execution, real source, activation, admission, live/runtime/public effect |
| Agent type | `INTERNAL_AGENT` worker |
| Invocation ID | `acel-g1-t3b-r2-atomic-rotation-contract-correction-worker-20260920` |
| Expected manifest | exactly the five Required Artifact Manifest paths |
| Actual changed set | exactly the same five paths, modified in place |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none occurred |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | Group 2 source-creation tooling R2 atomic rotation correction and hermetic validation only |
| claimDisposition | CLAIM_REJECTED for real source creation, approval, activation, consumer binding, admission, or any runtime/live/public/deployment effect |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no real Group 2 spec or decision record was produced; both real source paths remain absent |
| actionEvidence | ACTION_EVIDENCE_PRESENT: 48/48 spec-writer self-test cases (byte-identical, unmodified), 74/74 decision-writer self-test cases, 58/58 Python tests, all passing against disposable fixtures only |
| invocationBoundary | local filesystem reads/writes confined to disposable temp-directory sandboxes and the five declared worker output paths; no credential, `runas`, or alternate-principal invocation |
| interceptionBoundary | no runtime wrapper, proxy, or agent-control claim |
| claimLanguage | tooling corrected and hermetically re-tested pending Local review; Group 2 source remains not created |
| forbiddenExpansion | credentials, alternate-user execution, real Group 2 source, T3E, live/public/deployment remain out of scope and did not occur |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private principal-bound source tooling correction and not-yet-created
private source; no public-sync authority exists for this tranche.

## Changed Files

| Path | Change | Owner |
|---|---|---|
| `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | modified (T2F-R4-01 atomic rotation closed-schema and lifecycle repair) | worker |
| `scripts/acel_g1_approver_group2_decision_writer.ps1` | modified (atomic rotation build/validate/replay; replacement field guards) | worker |
| `governance/compat/check_acel_g1_verification_authority_spec.py` | modified (atomic rotation replay; replacement field validation) | worker |
| `governance/compat/test_check_acel_g1_verification_authority_spec.py` | modified (atomic-rotation positive/negative regressions; cross-language convergence) | worker |
| `docs/reviews/CVF_ACEL_G1_T3B_GROUP2_SOURCE_CREATION_TOOLING_WORKER_RETURN_2026-09-20.md` | modified (this file; R2 correction) | worker |

`scripts/acel_g1_party_a_group2_spec_writer.ps1` is accepted partial R1
evidence and was confirmed byte-identical throughout (disposition: `MATCH`;
not part of this five-path manifest). No other path in the repository was
created, edited,
deleted, or renamed by this worker. The thirteen pre-existing unrelated
uncommitted paths from prior tasks were left completely untouched.

## Command Evidence

Shell used: Bash tool (POSIX syntax) for `git`/`python`/`sha256sum`,
PowerShell (`pwsh`) for both writer self-tests.

```text
$ git rev-parse HEAD
d87a01115f1d37991bf90d2ac0cbcbf9c4e27362
Result: PASS (unchanged throughout this R2 pass)

$ python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 12d2d0d7437db746e4c4c038cf88eb881e03c23d --head HEAD
...
[FAIL] agent automation assist early diagnostics
[FAIL] independent review probe admission
  (both citing PRE-EXISTING unrelated worker-return docs / session-memory
  paths from prior-task parked paths, none citing this worker's five paths)
VIOLATION: pre-implementation blocked by 2 failing gate(s)
Result: PRE-EXISTING FAILURES, CONFIRMED UNRELATED TO THIS BATCH (identical
  category to the failure the R1 worker disclosed at the prior base)
```

```text
$ pwsh -NoProfile -File scripts/acel_g1_approver_group2_decision_writer.ps1
...
Self-test cases: 74 total, 74 passed, 0 failed.
Claim boundary: guard and state-machine behavior proven; no real Group 2 decision was appended.
Result: PASS (exit 0)

$ pwsh -NoProfile -File scripts/acel_g1_party_a_group2_spec_writer.ps1
...
Self-test cases: 48 total, 48 passed, 0 failed.
Claim boundary: guard behavior proven; no real Group 2 spec was created.
Result: PASS (exit 0; frozen file, unmodified, self-test unaffected)
```

```text
$ sha256sum scripts/acel_g1_party_a_group2_spec_writer.ps1
226b081d20f7e1aaf0c0b672c0dd004ebd53bd0b2350ca87ac38e829c7cb62e6  scripts/acel_g1_party_a_group2_spec_writer.ps1
Result: PASS (identical before and after this R2 pass)
```

```text
$ python -m py_compile governance/compat/check_acel_g1_verification_authority_spec.py governance/compat/test_check_acel_g1_verification_authority_spec.py
(no output; exit code 0)
Result: PASS

$ python governance/compat/test_check_acel_g1_verification_authority_spec.py
..........................................................
Ran 58 tests in 5.240s
OK
Result: PASS
```

```text
$ python governance/compat/run_worker_return_fast_gate.py
(reviewer-fast governance gate PASS after this document's SCEC resolution-
evidence hashes were recomputed against the corrected source files; any
finding outside this batch's five paths is a pre-existing condition from the
thirteen untouched parked paths, not a defect in this worker's five outputs)
```

```text
$ git diff --check
warning: in the working copy of 'docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md', LF will be replaced by CRLF the next time Git touches it
(exit 0; benign line-ending advisory only, not a whitespace-error violation)

$ git status --short --untracked-files=all
(exactly the thirteen pre-existing parked paths plus this worker's five
paths, nothing else)

$ git diff --cached --name-only
(no output; staging empty)
```

## No-Commit Statement

`WORKER_MUST_NOT_COMMIT honored`: this R2 worker pass did not run `git add`,
`git commit`, or any staging command at any point. Staging remains empty
(`git diff --cached --name-only` returns no output) and HEAD remains
unchanged at `d87a01115f1d37991bf90d2ac0cbcbf9c4e27362` (disposition MATCH
against the value captured before any edit in this pass). Only the five
Required Artifact Manifest paths were modified; no parked path, R2 dispatcher
path, or any other existing file was edited, deleted, or renamed, and no
sixth file was created. `scripts/acel_g1_party_a_group2_spec_writer.ps1`
remains byte-identical and was not touched. Neither real Group 2 source path
(`governance/sources/verification_authority_spec/SPEC_v1.json` or
`.../ACTIVATION_DECISIONS.jsonl`) was created at any point; both remain
absent. No credential, `runas`, or alternate-principal execution occurred.
Local reviewer/closer alone may stage, commit, or reject this return.

## git status --short --untracked-files=all

```text
 M docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md
?? EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.class.calibration.owner.contract.ts
?? EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/task.class.calibration.owner.contract.test.ts
?? docs/audits/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_2026-09-17.md
?? docs/audits/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_MANIFEST_2026-09-17.json
?? docs/audits/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_2026-09-17.md
?? docs/audits/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_MANIFEST_2026-09-17.json
?? docs/audits/CVF_ACEL_G1_T2_TASK_CLASS_CALIBRATION_OWNER_IMPLEMENTATION_2026-09-17.md
?? docs/reference/agent_system_skills/CVF_TASK_CLASS_CALIBRATION_OWNER_CONTRACT.md
?? docs/reviews/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_WORKER_RETURN_2026-09-17.md
?? docs/reviews/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_WORKER_RETURN_2026-09-17.md
?? docs/reviews/CVF_ACEL_G1_T2_TASK_CLASS_CALIBRATION_OWNER_IMPLEMENTATION_WORKER_RETURN_2026-09-17.md
?? docs/reviews/CVF_ACEL_G1_T3B_GROUP2_SOURCE_CREATION_TOOLING_WORKER_RETURN_2026-09-20.md
?? governance/compat/check_acel_g1_verification_authority_spec.py
?? governance/compat/check_task_class_calibration_owner_evidence.py
?? governance/compat/test_check_acel_g1_verification_authority_spec.py
?? governance/compat/test_check_task_class_calibration_owner_evidence.py
?? scripts/acel_g1_approver_group2_decision_writer.ps1
?? scripts/acel_g1_party_a_group2_spec_writer.ps1
```

Exactly the thirteen pre-existing parked paths plus this worker's five paths
(one now shown as modified -- the T2F contract, previously untracked at R1,
still untracked here since no commit has occurred across either round);
staging empty throughout.
