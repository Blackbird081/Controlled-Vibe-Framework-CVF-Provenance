# CVF DARA-T2 Architecture Readiness Admission Implementation Review

Memory class: governed-review

Status: REJECTED_RETURN_TO_DESIGN

docType: review

Date: 2026-09-07

Batch ID: DARA-T2-IMPLEMENTATION-REVIEW-R1

providerExecutionAuthority: FORBIDDEN

Review route: MULTI_AGENT_MULTI_ROLE

Independent review claimed: YES - external implementation worker returned to a separate Codex reviewer role.

## Purpose

Evaluate the DARA-T2 worker return and exact implementation delta without
recreating worker implementation, decide whether the material is commit-ready,
and preserve causal evidence for the DARA and CVF-foundation roadmap.

## Target / Source

| Artifact | Frozen reviewer input | Result |
|---|---|---|
| external worker return supplied for DARA-T2 review | filename `CVF_DARA_T2_ARCHITECTURE_READINESS_ADMISSION_IMPLEMENTATION_WORKER_RETURN_2026-09-06.md`; SHA-256 `EC426641EC5F699F7F9E57BB31CBA4CFDC25F5A28918B85E4C8CA5F48C8523CD` | uncommitted worker evidence read once; content findings reproduced below |
| ten implementation paths in the work-order manifest | working-tree diff hash-object `f86be219710813f8bd39164c06416dae0a81d972` | inspected; not edited by reviewer |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_DARA_T2_ARCHITECTURE_READINESS_ADMISSION_IMPLEMENTATION_2026-09-06.md` | dispatch commit `ab3b2025ab96b6f9fcbb9f05fa839125739fa3ec` | acceptance contract |
| `docs/assessments/CVF_DARA_T1_ARCHITECTURE_READINESS_CONTRACT_DESIGN_2026-09-06.md` | accepted T1 owner/chain/test contract | implementation authority |

## Scope / Methodology

The reviewer consumed the worker's manifest, command ledger, hostile-test
mapping, causal counters, and disclosed blockers. Review work was limited to:

- exact changed-set and no-commit reconciliation;
- worker-return fast gate;
- the two size guards named by the worker's open blockers;
- source inspection of the new applicability, row-identity, and semantic-review
  binding logic;
- two already-existing tests selected because their assertions contradicted
  T1; and
- one ephemeral row-identity probe covering four T1-required invariants.

No worker source/test/template file was edited. No broad unit suite,
pre-implementation bundle, provider call, runtime proof, or worker
implementation was recreated.

## Reviewer Dependency Matrix

| Area | Evidence consumed | Result | Reviewer action |
|---|---|---|---|
| exact manifest | status/diff and worker trace | PASS | none |
| no worker commit | HEAD remains `01c1420f6f19fe0caae572eb09d8da8e8d6f8576` | PASS | none |
| reviewer non-duplication | targeted checks only | PASS | none |
| mandatory file-size gates | direct current guard output | FAIL | return to design |
| applicability fail-closed | source line and HT-02 test | FAIL | consolidated finding R1-01 |
| immutable semantic review binding | source line and HT-01 test | FAIL | consolidated finding R1-02 |
| complete architecture chain | source inspection and one row probe | FAIL | consolidated finding R1-03 |
| evidence/status integrity | worker command table and terminal claim | FAIL | consolidated finding R1-04 |
| upstream manifest feasibility | worker disclosure plus T1 exact-path interlock | FAIL_UPSTREAM | consolidated finding R1-05 |

## Findings / Position

### DARA-T2-R1-01 - applicable work orders can bypass DARA by omitting the declaration

`governance/compat/check_work_order_dispatch_quality_range.py:765` returns an
empty issue list whenever the declaration is absent. The added test
`test_ht02_no_declaration_at_all_is_not_applicable` explicitly accepts that
fail-open behavior, and the targeted reviewer run passed it. T1 and the work
order instead require applicable external HIGH/CRITICAL or authority-expanding
design-bearing work to fail when the declaration or matrix row is missing.

Disposition: `WORKER_CONTRACT_EXECUTION_DEFECT`; machine coverage would be
fail-open if accepted.

### DARA-T2-R1-02 - semantic review commit is presence-only and accepts a fabricated identity

The validator checks current working-tree review bytes and requires only a
non-empty `architectureSemanticReviewCommit`. It does not require a full Git
SHA, prove ancestor status, load the review blob from that commit, or bind the
declared file SHA to committed bytes. HT-01 passes with the fabricated value
`0123456789abcdef0123456789abcdef01234567`, confirmed by the targeted reviewer
run. This violates T1's immutable path/commit/file-hash acceptance binding.

Disposition: `WORKER_CONTRACT_EXECUTION_DEFECT`; false acceptance is possible.

### DARA-T2-R1-03 - row identity validation omits required closed-chain invariants

The implementation validates selected owner/implementation/producer/export/
composition/consumer pairs, but does not resolve or constrain `trustSource`,
the context-carrier path/field pair, dated literal `evidenceOutputPath`,
`rollbackPaths` containment, or archive/provider-private authority. A targeted
ephemeral probe supplied a missing trust source, missing carrier, outside-root
rollback path, and undated non-review output; the validator returned `[]`.

Disposition: `WORKER_CONTRACT_EXECUTION_DEFECT`; the T1 closed chain is only
partially machine-enforced.

### DARA-T2-R1-04 - terminal readiness and PASS labels contradict recorded failures

The return uses `COMPLETE_PENDING_REVIEW` although its mandatory
pre-implementation gate and both size-policy owners remain failed. It labels
220/221 and 120/122 results as PASS and declares 16/16 hostile families pass,
although HT-15 explicitly requires the selected P4-C1 tests to pass. A
pre-existing or environmental cause may justify `KNOWN_FAILURE_WITH_REASON`,
but it cannot convert a non-zero failing test run into PASS or satisfy the work
order's all-commands-pass return condition.

Disposition: `EVIDENCE_INTERPRETATION_ERROR` plus worker return contract breach.

### DARA-T2-R1-05 - the dispatcher froze an infeasible exact manifest

The worker correctly disclosed three upstream conflicts: the work-order
template requires rotation or a 50-line shrink, the dispatch scaffold exceeds
its hard limit, and the frozen test file requires net delta at or below zero
and directs new tests to a dedicated file. Current guard evidence confirms all
three affected destinations. T1 explicitly says to return to design before
adding any production/checker/helper path, so a reviewer cannot authorize a
split path or exception locally and the worker cannot repair this within the
current exact manifest.

Disposition: `ORCHESTRATOR_PACKET_GAP`; this is not charged to the worker.

## Risk / Corrective Action

Accepting now would install a gate that can be bypassed by declaration omission,
can accept a nonexistent semantic-review commit, and does not validate multiple
required chain identities. It would also commit three active maintainability
violations and normalize failing commands as PASS.

Do not spend external invocation 2 on code repair yet. First, an orchestrator
must amend T1/T2 architecture with exact split/rotation paths and a feasible
size disposition. That amendment must also freeze the missing applicability
detection, committed-blob review binding, and full-chain validation cases.
Only then may one consolidated worker rework be dispatched within the existing
ceiling.

## Decision / Disposition

Reviewer verdict:

`REJECTED_RETURN_TO_DESIGN`

Commit disposition:

`NO_COMMIT_REVIEW`

External invocation disposition:

`HOLD_REMAINING_INVOCATION_1_OF_2`

The implementation remains uncommitted. DARA-T3 and WP-ARCH-003 remain parked.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Existing owner | Disposition | Next control action |
|---|---|---|---|---|---|
| absent declaration bypasses applicability | `WORKER_EXECUTION_ERROR` | `GOVERNANCE_CONTROL_PLANE` | DARA validator and hostile tests | `MACHINE_CHECK_CANDIDATE` | add inference/blocked-ambiguity cases before rework |
| fabricated commit satisfies review binding | `WORKER_EXECUTION_ERROR` | `GOVERNANCE_CONTROL_PLANE` | DARA semantic-review validator | `MACHINE_CHECK_CANDIDATE` | bind full ancestor commit and committed blob hash |
| five chain invariants are presence-only | `WORKER_EXECUTION_ERROR` | `GOVERNANCE_CONTROL_PLANE` | DARA row-identity validator | `MACHINE_CHECK_CANDIDATE` | add negative cases for every omitted identity |
| failing commands labeled PASS and COMPLETE | `EVIDENCE_INTERPRETATION_ERROR` | `GOVERNANCE_CONTROL_PLANE` | worker-return evidence contract | `DESIGN_REVIEW_REQUIRED` | require terminal status to reconcile with command exit state |
| exact manifest conflicts with size policy | `ORCHESTRATOR_PACKET_GAP` | `GOVERNANCE_CONTROL_PLANE` | DARA T1/T2 design and dispatch | `DESIGN_REVIEW_REQUIRED` | pre-authorize exact split/rotation paths before rework |

No new ADIF entry is opened in this review. These findings are retained as
DARA evidence candidates for later roadmap/ADIF reconciliation after the
orchestrator fixes the root contract.

Runtime/provider/cost learning lane: N/A_WITH_REASON: this review made zero
provider or live calls and found governance admission/evidence defects only;
token metering absence was already disclosed by the worker and is not promoted
to a runtime behavior claim here.

## Reviewer Non-Duplication And Cost Disposition

reviewRoundCount: 1

workerRepairTurnCount: 5

newRootCauseCountThisRound: 5

dependentFindingCountThisRound: 3

providerCallCount: 0

materialCommitCount: 0

continuityCommitCount: 0

elapsedReviewMinutes: NOT_AVAILABLE_WITH_REASON: no trusted elapsed-time meter is exposed to this reviewer

tokenOrQuotaUsage: NOT_AVAILABLE_WITH_REASON: no provider-neutral token meter is exposed to this reviewer

valueDelta: one bounded review found three executable fail-open classes, one evidence-status contradiction, and one upstream manifest-feasibility cluster before commit

stopDisposition: REVIEW_COST_ESCALATION_REQUIRED

preRepairAuditDisposition: COMPLETE_BEFORE_FIRST_REPAIR

commitPlanDisposition: NO_COMMIT_REVIEW

latencyDisposition: WITHIN_FAST_PATH_TARGET

avoidableDelayClass: GATE_DISCOVERY_LOOP

reviewerWorkBoundary: EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION

Duplicate deterministic reruns: 0 broad suites; two named existing tests and
one four-field row probe were admitted by explicit source contradictions.

## Epistemic Process Block

### Expected Result / Prediction

A complete T2 should make every applicable dispatch declare and satisfy the
matrix, bind acceptance to immutable committed review evidence, validate the
full T1 chain, and pass mandatory repository gates.

### Evidence Comparison

The worker supplied substantial implementation and useful causal evidence,
but direct source and targeted checks show declaration, commit identity, and
five chain fields remain fail-open. Current size guards independently confirm
the worker's upstream manifest-feasibility disclosure.

### Contradiction Or Gap Disposition

The five findings are consolidated in this review. R1-05 requires return to
design before R1-01 through R1-04 can be safely redispatched as one repair.

### Claim Update

DARA-T2 is not implemented or commit-ready. The tranche is now a high-value
evidence sample showing both dispatcher architecture debt and worker execution
gaps under the non-duplicative review model.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | review headings, finding classes, learning dispositions, cost fields, trace labels, private export disposition, claim boundary |
| gateRunPurpose | confirm the completed reviewer artifact after semantic findings were established |
| claimBoundary | reviewer-fast conformance cannot convert rejected implementation into acceptance |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External-agent returned output |
| Chain map route | governed worker return -> local source/evidence review -> consolidated disposition |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | DARA roadmap, T1 design, T2 work order, and this review |
| Disposition | retain source-backed findings; reject unsupported PASS/readiness labels |
| Claim boundary | external return is evidence input, not CVF authority or implementation acceptance |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex reviewer only |
| Provider or surface | local private CVF workspace |
| Session or invocation | DARA-T2 reviewer round 1, 2026-09-07 |
| Working directory | repository root |
| Command or tool surface | git status/diff, worker-return read, reviewer-fast, two size guards, source reads, two named unit tests, one ephemeral row probe, apply_patch for this review only |
| Target paths | worker return, ten implementation paths read-only, and this reviewer-owned disposition |
| Allowed scope source | operator assigned Codex reviewer role and submitted `COMPLETE_PENDING_REVIEW` return |
| Before status evidence | HEAD `01c1420f6f19fe0caae572eb09d8da8e8d6f8576`; exact eleven worker paths plus two pre-existing parked paths |
| After status evidence | implementation untouched; one reviewer-owned rejection artifact added; no stage or commit |
| Diff evidence | worker diff hash-object `f86be219710813f8bd39164c06416dae0a81d972`; review file excluded from that hash |
| Approval boundary | evidence evaluation and reviewer disposition only |
| Claim boundary | no implementation repair, work-order amendment, external redispatch, commit, provider/live/public action |
| Agent type | reviewer |
| Invocation ID | `dara-t2-review-r1-2026-09-07` |
| Expected manifest | this reviewer-owned completion disposition only |
| Actual changed set | this review plus preserved worker and parked pre-existing worktree changes |
| Manifest delta | MATCH for reviewer-owned change |
| Deletion or rename disposition | N/A with reason: reviewer deleted or renamed nothing |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private rejected implementation review; no public-sync authority.

## Claim Boundary

This review rejects the current DARA-T2 implementation and records one
consolidated finding set. It does not repair worker code, amend the frozen
manifest, consume the remaining external invocation, accept T2, open T3,
resume WP-ARCH-003, change MFRP, commit, publish, deploy, or claim runtime or
production readiness.
