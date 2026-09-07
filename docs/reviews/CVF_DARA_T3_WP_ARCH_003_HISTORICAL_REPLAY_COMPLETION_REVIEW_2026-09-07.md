# CVF DARA-T3 WP-ARCH-003 Historical Replay Completion Review

Memory class: governed-review

Status: REJECTED_RETURN_TO_DESIGN_REWORK_AUTHORIZED_PENDING_DISPATCH

docType: review

Date: 2026-09-07

Batch ID: DARA-T3-WP-ARCH-003-HISTORICAL-REPLAY-REVIEW

providerExecutionAuthority: FORBIDDEN

Review route: MULTI_AGENT_MULTI_ROLE

Independent review claimed: YES - the operator-relayed external worker returned
to a separate Codex orchestrator/reviewer.

## Purpose

Evaluate the exact-five DARA-T3 worker return without recreating its
implementation, determine whether the claimed historical-replay result is
decision-grade, and freeze one consolidated finding set before any rework.

## Target / Source

| Artifact | Frozen reviewer input | Result |
|---|---|---|
| replay fixture | `governance/compat/fixtures/dara_t3_wp_arch_003_historical_replay.json`; SHA-256 `bc21813ea83bf3b96f9099298c5d7435da0c1501b264b5c4bd08f122ae16f55f` | 7 sources, 3 raw cases and 10 seeded labels are present |
| replay helper | `governance/compat/dara_t3_historical_replay.py`; SHA-256 `8b516694c87c0ec83ec3545d71acc4618dd6377a1980fe15d329a52e0054cb52` | raw declaration check is executable; seeded evaluation is not |
| focused tests | `governance/compat/test_dara_t3_historical_replay.py`; SHA-256 `6e67dd63cd947dc7064ae8398b58f66e51c05afd348cfbbdeaa95e1d349dc003` | 19/19 pass but encode the same seeded tautology |
| replay ledger | `docs/reviews/CVF_DARA_T3_WP_ARCH_003_HISTORICAL_REPLAY_LEDGER_2026-09-07.md`; SHA-256 `8defe904eab7fd59edc7736c9e6de20d487f55fed77d434e020363042a1dd03d` | final hash exists; required pre/post ledger identity proof is absent |
| worker return | `docs/reviews/CVF_DARA_T3_WP_ARCH_003_HISTORICAL_REPLAY_WORKER_RETURN_2026-09-07.md`; SHA-256 `b4480ca94e4f308be13abd0202bfe8ffe743cf6dd9c92a1e4e4867bd58f9f1d3` | exact-five and no-commit evidence is valid; terminal replay claim is rejected |

executionBaseHead: `b23f0b7db8b24993f999ba38d9f445b89a06fa76`

Prior finding set digest:
`88aabb6fcc1043945efde94d0010f67c508bf0fdffc883ace2406a9ad260b63d`

## Scope / Methodology

The reviewer consumed the worker's hashes, command evidence, exact changed-set
evidence and focused results. Independent work was limited to recomputing the
seven source hashes through the helper, rerunning the focused tests and
worker-return fast gate, inspecting the seeded evaluation path, and one
contradiction-driven adversarial probe. No broad suite, implementation repair,
provider call, live proof or duplicate case-by-case reconstruction was run.

The adversarial probe replaced every seeded `sourceFinding` and `note` with
`NO DEFECT DATA`. All seeded outputs and the terminal
`REPLAY_BLOCKS_AVOIDABLE_INVOCATIONS` verdict remained identical.

## Reviewer Dependency Matrix

| Area | Evidence consumed | Result | Reviewer action |
|---|---|---|---|
| execution anchor | HEAD and worker return | PASS | accept `b23f0b7db8b24993f999ba38d9f445b89a06fa76` |
| exact manifest | Git status and paired baseline | PASS | preserve the same five paths for rework |
| source identity | helper output | PASS | 7/7 hashes match; do not refresh source hashes |
| raw replay | helper output and source declarations | PASS_BOUNDED | retain the three raw earliest-stop cases |
| seeded replay | helper lines 168-194 | FAIL | require structured defect inputs evaluated by real accepted validators |
| error accounting | helper lines 208-216 | FAIL | derive false positives, false negatives and zero-tolerance misses from observed versus expected results |
| freeze integrity | ledger and return freeze sections | FAIL_EVIDENCE | require explicit pre-run and post-run fixture/ledger hashes with byte identity |
| structural gates | 19/19 focused and 67/67 reviewer-fast | PASS_STRUCTURE_ONLY | do not treat structural PASS as semantic acceptance |
| quota | first DARA-T3 external assignment consumed 1/1 | EXHAUSTED_UNDER_OLD_PACKET | operator instruction opens one consolidated rework with ceiling raised to 2 |

## Findings / Position

### DARA-T3-R1-01 - seeded results copy expectations instead of evaluating defects

`evaluate_seeded_case` assigns `actualViolationClass` from
`expectedViolationClass`, assigns the actual earliest stop from the expected
earliest stop, and sets `matched = True`. The fixture contains prose labels and
citations but no structured candidate packet or matrix that an accepted DARA
validator can evaluate. Consequently the ten seeded rows do not test whether a
known dispatcher-created defect would escape.

Disposition: `ORCHESTRATOR_PACKET_GAP`. The original work order required
expected/actual comparison but did not explicitly require independent
structured stimulus and observed validator output.

### DARA-T3-R1-02 - false-positive and zero-tolerance accounting is tautological

`false_positive_count` is a constant zero. Seeded false negatives are derived
from `matched`, which is always true, while zero-tolerance success only checks
whether the expected label belongs to a constant allowlist. Removing all
seeded defect evidence leaves the claimed verdict unchanged. T3-A05 and T3-A06
therefore fail.

Disposition: `MACHINE_GATE_GAP`. Focused tests confirm serialization and label
membership but do not prove sensitivity to defect-bearing input.

### DARA-T3-R1-03 - ledger freeze identity is not demonstrated

T3-A07 required both fixture and ledger hashes before the first replay and
unchanged afterward. The pre-replay freeze table contains fixture, helper and
test hashes but no ledger hash. The worker return provides only one final
ledger hash and narrows the claim to unchanged expectation content. That is
not byte-identity evidence for the ledger required by the work order.

Disposition: `EVIDENCE_INTERPRETATION_ERROR`. Rework must record external
pre-run and post-run hashes for both frozen artifacts without embedding or
self-referentially changing the ledger hash.

## Risk / Corrective Action

Do not commit or accept the current exact-five worker material. One
consolidated R1 rework may modify only the same five paths. It must preserve the
seven frozen source identities and the valid raw cases, replace seeded labels
with structured validator inputs, compute observed outcomes independently from
expected fields, add metamorphic/adversarial sensitivity tests, and produce
external pre/post byte hashes for fixture and ledger.

The operator explicitly authorized manual relay to Claude for this repair.
The rework remains `WORKER_MUST_NOT_COMMIT`, moves the same parent assignment
from external count 1 to ceiling 2, and is the final admitted external repair
under this packet. No third invocation is automatic.

## Decision / Disposition

Reviewer verdict: `RETURN_TO_DESIGN`

Commit disposition: `NO_COMMIT_WORKER_MATERIAL`

Rework disposition: `ONE_CONSOLIDATED_REWORK_AUTHORIZED_PENDING_COMMITTED_PACKET`

External invocation disposition: `COUNT_1_CEILING_RAISED_TO_2_BY_OPERATOR`

Next role: orchestrator authors, validates and commits one bounded R1 baseline
and work order; operator manually relays that committed packet to Claude.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Existing owner | Disposition | Next control action |
|---|---|---|---|---|---|
| seeded expected values were presented as observed validator output | `ORCHESTRATOR_PACKET_GAP` | `GOVERNANCE_CONTROL_PLANE` | DARA work order and replay contract | `TEMPLATE_UPDATED` | R1 packet requires structured stimulus and independent observation |
| constant-zero and membership-only metrics passed focused tests | `MACHINE_GATE_GAP` | `GOVERNANCE_CONTROL_PLANE` | focused replay test module | `MACHINE_CHECK_CANDIDATE` | add metamorphic tests that remove or invert defect-bearing input |
| ledger freeze claim lacked pre/post byte identity | `EVIDENCE_INTERPRETATION_ERROR` | `GOVERNANCE_CONTROL_PLANE` | worker return evidence contract | `TEMPLATE_UPDATED` | require external hash receipt captured before and after replay |

No new ADIF entry is opened by this review. The three findings are consolidated
into the R1 repair packet first; recurrence after that repair is the escalation
condition.

Runtime/provider/cost learning lane: N/A_WITH_REASON: the findings concern a
provider-free local replay measurement and its evidence contract; no runtime
behavior, provider output or cost-economics observation was produced.

## Reviewer Non-Duplication And Cost Disposition

reviewRoundCount: 1

workerRepairTurnCount: 0

newRootCauseCountThisRound: 2

dependentFindingCountThisRound: 1

providerCallCount: 0

materialCommitCount: 0

continuityCommitCount: 0

elapsedReviewMinutes: NOT_MEASURED_WITH_REASON: no trusted reviewer timer is bound to this artifact

tokenOrQuotaUsage: NOT_AVAILABLE_WITH_REASON: no provider-neutral token meter is exposed

valueDelta: one semantic replay defect, one dependent metric defect and one evidence defect identified with one focused rerun and one adversarial probe

stopDisposition: CONSOLIDATE_SINGLE_REPAIR

preRepairAuditDisposition: COMPLETE_BEFORE_FIRST_REPAIR

commitPlanDisposition: NO_COMMIT_WORKER_MATERIAL

latencyDisposition: WITHIN_FAST_PATH_TARGET

avoidableDelayClass: GATE_DISCOVERY_LOOP

reviewerWorkBoundary: EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`architecture-readiness historical replay review`,
role=`reviewer`, lifecyclePhase=`pre-closure`.

Returned defects: NONE_RETURNED

## Epistemic Process Block

### Expected Result / Prediction

The returned helper should independently evaluate each raw and seeded input
against accepted DARA behavior and compare observed output with frozen
expectations.

### Evidence Comparison

Raw declaration cases are evaluated. Seeded cases instead copy their expected
fields into actual fields; a defect-evidence removal probe leaves their output
and terminal verdict unchanged. The ledger also lacks the required pre-run
hash.

### Contradiction Or Gap Disposition

The terminal success claim is contradicted by the helper implementation and
cannot be repaired through reviewer prose. One bounded code/evidence rework is
required.

### Claim Update

The exact-five packet is structurally compliant and its raw-case result is
promising, but DARA-T3 effectiveness is unproven. No T3 success outcome or
downstream activation is accepted.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_review_cost_control.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | review status, defect classes, learning lanes/dispositions, review-cost scalar fields, trace labels and private export disposition |
| gateRunPurpose | confirm review artifact structure after the semantic finding set was frozen |
| claimBoundary | machine conformance cannot accept the replay or replace reviewer judgment |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External-agent returned output |
| Chain map route | committed work order -> operator relay -> exact-five pending return -> local independent review -> bounded rework packet |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_review_cost_control.py` |
| Owner surface | DARA roadmap, paired T3 baseline/work order and this review |
| Disposition | retain valid hashes/raw evidence; reject the seeded effectiveness conclusion |
| Claim boundary | returned material is evidence input, not acceptance authority |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex orchestrator/reviewer |
| Provider or surface | local private CVF workspace |
| Session or invocation | DARA-T3 first-return review, 2026-09-07 |
| Working directory | repository root |
| Command or tool surface | governed reads, Git inspection, SHA-256, focused pytest, replay helper, worker-return fast gate and one local adversarial probe |
| Target paths | exact-five pending worker paths plus this reviewer-owned review |
| Allowed scope source | active DARA-T3 review boundary and operator instruction to prepare one Claude worker repair packet |
| Before status evidence | HEAD and execution base `b23f0b7db8b24993f999ba38d9f445b89a06fa76`; exact five untracked worker paths |
| After status evidence | worker paths unchanged; reviewer review added separately |
| Diff evidence | `git status --short --untracked-files=all`; no staged worker material |
| Approval boundary | review and one bounded R1 dispatch only |
| Claim boundary | no replay acceptance, WP implementation, DARA-T4, provider/live, public-sync, deployment or production action |
| Agent type | orchestrator/reviewer |
| Invocation ID | `dara-t3-r1-review-2026-09-07` |
| Expected manifest | one reviewer-owned review artifact |
| Actual changed set | this review only in the review commit |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance review and dispatch authority; no public-sync
authority.

## Claim Boundary

This review rejects the seeded historical-replay effectiveness claim while
preserving valid source-hash, raw-case, exact-five and no-commit evidence. It
authorizes only preparation of one bounded same-parent R1 repair packet for
operator manual relay. It does not accept or implement `WP-ARCH-003`, open
DARA-T4, invoke Claude or any provider, expose credentials, publish, deploy,
push or claim production readiness.
