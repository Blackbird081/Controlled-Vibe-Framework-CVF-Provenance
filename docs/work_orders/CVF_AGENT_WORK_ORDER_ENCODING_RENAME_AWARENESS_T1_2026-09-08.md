# CVF Agent Work Order - Encoding Rename Awareness T1

Memory class: governed-worker-dispatch

docType: work_order

## Dispatch Prompt Envelope

Role: internal governance implementation worker; the orchestrator/reviewer owns
acceptance and commits.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_ENCODING_RENAME_AWARENESS_T1_2026-09-08.md`.

Paired baseline: `docs/baselines/CVF_GC018_ENCODING_RENAME_AWARENESS_T1_2026-09-08.md`.

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: capture the exact clean committed HEAD immediately before the
first edit and use it for every worker-range command.

Current-time notes: operator-authorized bounded packet on 2026-09-08 after
ROLE-SOT-MH-T1 closed at `docs/work_orders/CVF_AGENT_WORK_ORDER_ROLE_SOT_MH_T1_DISPATCH_COORDINATION_AND_DEPENDENCY_DISCOVERY_MACHINE_HARDENING_2026-09-08.md` commit `94c4922c29390ac6f362a6a56a71b3e5054926ae`. Local machine hardening only; external invocation count
remains zero.

Do-not-misread notes: make the encoding gate rename-aware. Do not normalize
historical Unicode, do not weaken detection of genuinely added non-ASCII text,
do not touch the commit-choreography helper, and do not add hook or autorun
wiring.

Return contract: return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` in `docs/reviews/CVF_ENCODING_RENAME_AWARENESS_T1_WORKER_RETURN_2026-09-08.md` with full status, staging state and the exact owned-path manifest; do not stage or commit.

Required first actions: read the startup surfaces, guard orientation, literal
gotchas, the paired baseline and this packet; capture HEAD and full status;
require a clean worktree and empty staging; recompute every Source Pin Contract
hash; then run pre-implementation.

Status: CLOSED_PASS_BOUNDED

Batch ID: ENCODING-RENAME-T1

Date: 2026-09-08

Dispatch base head: `39be75a7cff4fc9acdbf3dd129254ddb164947d0`

dispatchBaseHead: `39be75a7cff4fc9acdbf3dd129254ddb164947d0`

executionBaseHead: WORKER_MUST_CAPTURE_AT_START

closureBaseHead: `d46a55d2b`

Commit mode: WORKER_MUST_NOT_COMMIT

providerExecutionAuthority: FORBIDDEN

Worker return path: `docs/reviews/CVF_ENCODING_RENAME_AWARENESS_T1_WORKER_RETURN_2026-09-08.md`

successorTrancheOpened: NO

EPISTEMIC_PROCESS_NA_WITH_REASON: dispatch packet defining scope, ownership and
required proof; the worker return carries the evidence comparison.


## Purpose

Make the agent packet authority and encoding gate rename-aware so a renamed
governed file no longer reports its pre-existing non-ASCII text as newly added,
while genuinely new non-ASCII text still fails.

## 1. Mission

Derive newly added lines from rename-aware Git provenance so a renamed governed
file no longer reports its pre-existing non-ASCII text as newly added, while
genuinely new non-ASCII text still fails.

## 2. Authority Chain

| Level | Artifact |
|---|---|
| Operator authorization | operator direction on 2026-09-08 to open encoding and GC-020 hardening as two separate bounded packets |
| Paired baseline | `docs/baselines/CVF_GC018_ENCODING_RENAME_AWARENESS_T1_2026-09-08.md` |
| Canonical standard | `docs/reference/CVF_TEXT_ENCODING_AND_SYMBOL_DISCIPLINE_STANDARD_2026-06-07.md` |
| Defect binding | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0011.md` |
| Predecessor closure | ROLE-SOT-MH-T1 `CLOSED_PASS_BOUNDED` at `94c4922c29390ac6f362a6a56a71b3e5054926ae` |

## 3. Agent Roles

| Role | Responsibility | Limit |
|---|---|---|
| Operator | authorizes this exact packet and retains expansion checkpoints | no implementation role implied |
| Dispatcher | fixes sources, exact scope, cases, stop rules and rollback | does not edit worker-owned material after dispatch |
| Worker | implements and verifies exact owned paths | no stage, commit, scope expansion or external effect |
| Reviewer/closer | evaluates returned evidence, performs bounded allowed-scope repair if justified, and commits accepted material | does not recreate implementation or broaden claims |

## 4. Scope

In scope: rename-aware provenance for the encoding gate, its focused tests, the
encoding standard, and the ADIF-0011 promotion after proof.

Out of scope: the commit-choreography helper and every GC-020 concern, which are
governed by `docs/work_orders/CVF_AGENT_WORK_ORDER_GC020_POST_COMMIT_SHA_SYNCHRONIZATION_T1_2026-09-08.md`.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`encoding gate hardening`, role=`worker`,
lifecyclePhase=`pre-commit`. Returned defects: ADIF-0011, the matching active
entry, which is an owned path in this tranche. No new ADIF entry is required.

## 5. Required First Reads

| Source | Reason |
|---|---|
| `CVF_SESSION_MEMORY.md` | current mode and next allowed move |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | bootstrap facts |
| `AGENT_HANDOFF_V60_2026-09-08.md` | active handoff |
| `docs/reference/guard_orientation/README.md` | applicable role and task guards |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | known gate traps |
| `docs/baselines/CVF_GC018_ENCODING_RENAME_AWARENESS_T1_2026-09-08.md` | paired baseline |
| `governance/compat/check_agent_packet_authority_and_encoding.py` | owned checker source |
| `governance/compat/test_check_agent_packet_authority_and_encoding.py` | owned focused tests |
| `docs/reference/CVF_TEXT_ENCODING_AND_SYMBOL_DISCIPLINE_STANDARD_2026-06-07.md` | canonical encoding policy |
| `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0011.md` | existing defect binding |

## 6. Pre-Flight Checks

Capture the full `executionBaseHead`; require an empty
`git status --short --untracked-files=all` and empty staging; prove that
dispatch `39be75a7cff4fc9acdbf3dd129254ddb164947d0` is an ancestor of HEAD;
recompute every Source Pin Contract hash; and run pre-implementation. Stop
before edits on drift or any unexpected path.

## 6C. Worker Autonomy / No-Question Rule

Proceed autonomously inside Write Ownership. Repair routine in-scope failures
after reading the failing checker source. Return `BLOCKED_WITH_REASON` for any
needed path expansion, source contradiction, maintainability violation, registry
mutation, hook or autorun change.

## 6F. Near-Threshold Owner Maintainability Plan

At dispatch base the owned checker is 567 lines against a 1000-line hard
threshold for `python_checker`, and the owned test file is 265 lines against a
1200-line hard threshold for `python_test`. Neither enters the near-hard band.
The worker must keep rename provenance inside the existing module rather than
opening a new helper module. If the checker would exceed 900 lines, stop and
return `BLOCKED_WITH_REASON` rather than splitting an owner not listed here.

## 6G. Work-Order Fulfillment Manifest

The Required Artifact Manifest is the complete fulfillment manifest. Exactly
those five paths may be pending at worker return; any sixth path is blocking.

## Required Artifact Manifest

| Artifact | Required worker action |
|---|---|
| `governance/compat/check_agent_packet_authority_and_encoding.py` | MODIFY with rename-aware provenance only |
| `governance/compat/test_check_agent_packet_authority_and_encoding.py` | MODIFY with positive, negative, malformed-input and regression cases |
| `docs/reference/CVF_TEXT_ENCODING_AND_SYMBOL_DISCIPLINE_STANDARD_2026-06-07.md` | MODIFY existing owner semantics |
| `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0011.md` | MODIFY only after executable proof passes |
| `docs/reviews/CVF_ENCODING_RENAME_AWARENESS_T1_WORKER_RETURN_2026-09-08.md` | CREATE complete no-commit evidence return |

## Forbidden Path Manifest

- `scripts/cvf_commit_tranche.py` and every GC-020 surface;
- `AGENTS.md`, `CVF_SESSION/`, the active handoff, roadmaps, this packet and its
  paired baseline;
- the work-order template, dispatch scaffold and active-window registry;
- hook, autorun, command-catalog and exception-registry surfaces;
- any other `governance/compat/check_*.py` owner.

## Forbidden Scope

- no new checker entrypoint or guard wiring;
- no hook, autorun or command-catalog change;
- no broad Unicode normalization of historical or unrelated files;
- no weakening of non-ASCII detection for genuinely added text;
- no Git worktree creation or removal, stash, checkout, reset or path isolation;
- no provider, live, network, credential, package install, public sync, push,
  deployment, runtime or production action;
- no staging or commit.

## Source Pin Contract

| Source | Expected SHA-256 |
|---|---|
| `governance/compat/check_agent_packet_authority_and_encoding.py` | `db7e488344d9e41191e8042a081d5df831f0ac9c14c7f4b07622cc4848e1a89a` |
| `governance/compat/test_check_agent_packet_authority_and_encoding.py` | `037ebdcd7ea091991c6f81cea935c3a8d156a54ed70478adfe40458ea6af4b94` |
| `docs/reference/CVF_TEXT_ENCODING_AND_SYMBOL_DISCIPLINE_STANDARD_2026-06-07.md` | `c51a1eef1d69c5537467a87c32804bb007ed22aa629c05839d4344e3fd1880dd` |
| `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0011.md` | `32e84a218429a3a4b7bc2bb5169bc1ddd57e679cb762ce7f1decd4010316ae6f` |
| `governance/compat/CVF_ACTIVE_WINDOW_REGISTRY.json` | `a5261b674cab6b112a8e45d0df9a2efa1d159a070656d985cbb4db5a70f9e866` |

## 7. Write Ownership

Modify exactly:

1. `governance/compat/check_agent_packet_authority_and_encoding.py`
2. `governance/compat/test_check_agent_packet_authority_and_encoding.py`
3. `docs/reference/CVF_TEXT_ENCODING_AND_SYMBOL_DISCIPLINE_STANDARD_2026-06-07.md`
4. `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0011.md`

Create exactly:

5. `docs/reviews/CVF_ENCODING_RENAME_AWARENESS_T1_WORKER_RETURN_2026-09-08.md`

All five paths remain unstaged and uncommitted at worker handoff.

## 7A. Protected-Path Authorization Carrier

Two owned paths are protected `governance/compat/*.py` files. The Core Guard
Self-Protection Authorization block below names both explicitly.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: make the existing encoding gate
rename-aware and extend its existing focused tests.

Protected paths:

- `governance/compat/check_agent_packet_authority_and_encoding.py`
- `governance/compat/test_check_agent_packet_authority_and_encoding.py`

Operator authorization: the operator authorized rename-aware encoding
enforcement as one of two separate bounded packets, with ROLE-SOT-MH-T1 closed at
`docs/work_orders/CVF_AGENT_WORK_ORDER_ROLE_SOT_MH_T1_DISPATCH_COORDINATION_AND_DEPENDENCY_DISCOVERY_MACHINE_HARDENING_2026-09-08.md`
commit `94c4922c29390ac6f362a6a56a71b3e5054926ae`.

Rollback boundary: revert only accepted ENCODING-RENAME-T1 material. Preserve
ROLE-SOT-MH-T1 at `94c4922c2`, ROLE-SOT-EVIDENCE-T0 at `6bcdeaca8`, the RABA
park at `0767a16e5` and P4-C1 at `b9bdba712`.

Dispatch-authoring protected path, owned by the dispatch author rather than the
implementation worker:

- `governance/compat/CVF_ACTIVE_WINDOW_REGISTRY.json`

The dispatch author added exactly two additive `BINDING_REFERENCE_ACTIVE_WINDOW`
entries during authoring so the dated canonical standard this tranche must edit
is exempt from stale-dated archive pressure. No existing registry entry was
modified or removed. The implementation worker does not own this path and must
not mutate it.

Not authorized: hook, autorun, command-catalog, registry, session-state,
active-handoff, template, scaffold, commit-helper, provider/live, public-sync,
push, deploy or production changes.

## Dated Owner Dependency Discovery

| Owned dated reference path | Classification | Registry evidence | Disposition |
|---|---|---|---|
| `docs/reference/CVF_TEXT_ENCODING_AND_SYMBOL_DISCIPLINE_STANDARD_2026-06-07.md` | `BINDING_REFERENCE_ACTIVE_WINDOW` | registry entry id `text_encoding_and_symbol_discipline_standard_active_reference` in `governance/compat/CVF_ACTIVE_WINDOW_REGISTRY.json`; registered during dispatch authoring, so the implementation worker neither owns nor mutates the registry | ACCEPT |

The undated ADIF-0011 entry is outside this dated-owner table. Registration was
completed during dispatch authoring. The implementation worker does not own the
registry, must not mutate it, and inherits the binding classification as a
settled precondition.

## Shared Worktree Coordination

| Field | Value |
|---|---|
| sharedWorktreeCoordinationMode | `EXPLICIT_LANE_HANDOFF` |
| activeLaneOwner | ENCODING-RENAME-T1 internal no-commit worker from execution anchor capture until returned status evidence |
| laneOwnedPaths | exactly the five Write Ownership paths |
| dispatcherMutationBoundary | `NO_MUTATION_WHILE_LANE_ACTIVE` |
| laneReleaseEvidence | worker return records final full status and empty staging; reviewer explicitly accepts control of the paths before any isolation or commit |

This is a packet-contract declaration. It does not intercept Git or filesystem
operations and does not prove that concurrent writes were technically prevented.

## Protocol / Contract / Requirements

### Rename provenance

Preserve both source and destination from `git diff --name-status -z -M`, or an
equivalently lossless parser, so quoting, spaces and non-ASCII path names cannot
corrupt the source and destination fields. Do not reduce an `R100 old new`
record to destination-only provenance. Determine newly added lines by comparing
the destination against the correct source blob, or by using an unrestricted
rename-aware diff that preserves pairing. A pathspec limited to the destination
alone must not be the sole provenance source, because Git cannot pair blobs
under that restriction.

### Below-threshold move semantics

Git decides whether a move is a rename. This packet does not second-guess that
decision and does not reconstruct provenance Git did not establish.

- When Git reports `R` or `C`, use its source and destination provenance.
- When Git reports a delete plus an add because similarity fell below the rename
  threshold, the source relationship is not established by the name-status
  evidence. Do not invent one.
- Selected behavior, frozen for this tranche: treat the destination as an
  ordinary added file under existing enforcement. Newly added non-ASCII in it
  fails exactly as any other added file would.
- The packet must never claim historical provenance is known in this case.

### Required behavior

- A pure rename carrying historical non-ASCII text produces zero newly-added
  non-ASCII violations.
- A rename plus newly introduced non-ASCII reports only the newly introduced
  lines.
- Rename-with-modification, ordinary additions, ordinary modifications and
  deletions are each handled explicitly.
- A below-threshold move is treated as an ordinary added destination, never as a
  reconstructed rename.
- Paths containing spaces and paths containing non-ASCII characters both resolve
  to the correct source and destination.
- Malformed name-status records, missing source blobs, binary files and decode
  failures each produce a deterministic diagnostic.
- Fail closed only where evidence is genuinely unavailable. Converting all
  historical destination lines into additions is not acceptable fail-closed
  behavior.
- Untracked and provenance-unknown files keep their existing fail-closed
  handling.
- Existing Text Encoding Exception behavior is unchanged.

### Documentation

Update the encoding standard with the rename-provenance rule and restate the
prohibition on broad Unicode normalization. Update ADIF-0011 to record the
rename-aware behavior only after the focused proof passes, preserving its
historical evidence.

## Focused Case Matrix

Required focused test names, each proven with real Git provenance in an isolated
temporary repository:

1. `test_pure_rename_with_historical_unicode_reports_no_violation`
2. `test_rename_with_new_unicode_reports_only_new_line`
3. `test_rename_with_ascii_only_edit_passes`
4. `test_new_file_with_unicode_without_exception_fails`
5. `test_existing_file_newly_added_unicode_fails`
6. `test_below_threshold_move_is_treated_as_ordinary_added_destination`
7. `test_below_threshold_move_does_not_claim_historical_provenance`
8. `test_rename_path_with_spaces_resolves_source_and_destination`
9. `test_rename_path_with_non_ascii_name_resolves_source_and_destination`
10. `test_malformed_name_status_record_fails_closed`
11. `test_missing_source_blob_produces_deterministic_diagnostic`
12. `test_decode_failure_produces_deterministic_diagnostic`
13. `test_binary_rename_is_classified_without_text_violation`
14. `test_text_encoding_exception_behavior_is_unchanged`
15. `test_untracked_file_retains_fail_closed_behavior`

## 8. Execution Plan

1. Capture execution identity, verify pins, run pre-implementation.
2. Implement rename-aware provenance in the existing checker module.
3. Add the focused cases above.
4. Update the encoding standard.
5. Update ADIF-0011 only after the focused proof passes.
6. Write the worker return last, rerun gates, leave staging empty.

### Worker Trace Requirement

The worker return must carry a complete Agent Operation Trace Block including
`Deletion or rename disposition` and `git diff --name-status` diff evidence.

## 9. Evidence Requirements

Return exact start and final HEAD, full status, staging state, recomputed
hashes, focused counts, Python size result, ADIF integrity result, the
worker-return fast result, the exact five-path manifest, and explicit
no-commit and no-external-effect evidence.

## 10. Acceptance Criteria

All focused cases pass; the prior encoding suite passes; the Python size guard
passes with no touched near-hard growth; the changed set is exactly five paths;
staging is empty; ADIF-0011 truthfully records the rename-aware behavior; and
the reviewer can evaluate the return without recreating implementation.

## 11. Review Gate

Reviewer applies `EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION`.
Bounded reruns require a named contradiction, expected information gain and a
cost reason.

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_ENCODING_RENAME_AWARENESS_T1_COMPLETION_2026-09-08.md` (create only if machine closure or a material reviewer finding requires it) |
| reviewerOwnedClosurePaths | the exact five worker paths plus bounded in-scope repairs; session surfaces only in a separate continuity commit |
| closureOwner | internal orchestrator/reviewer |
| workerCommitPermission | FORBIDDEN |

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intake summary | operator request on 2026-09-08 to resume rename-aware encoding enforcement as its own bounded packet |
| scope classification | bounded blast radius: exactly five allowed-scope changed paths, one existing checker owner and its focused tests |
| risk sensitivity | low; no provider, live, secret, public-sync, production or readiness surface is touched by this repository-local pre-commit checker |
| selected role route | route mode `MULTI_AGENT_MULTI_ROLE` |
| role separation basis | dispatcher authors, internal no-commit worker implements, reviewer/closer accepts and commits |
| escalation condition | worker must stop and return `BLOCKED_WITH_REASON` on any sixth path, registry mutation need, hook or autorun change, or operator checkpoint |
| externalAgentDisposition | NOT_ROUTED_EXTERNAL; external invocation remains unauthorized for this packet |
| adapterBoundary | no adapter, CLI or MCP surface is opened by this tranche |

## Evidence Requirements

Return exact start and final HEAD, full status, staging state, recomputed
hashes, focused counts, the governed Python size result, the worker-return fast
result, the exact owned-path manifest, and explicit no-commit and
no-external-effect evidence.

## Closure Checklist

- [x] all focused cases pass
- [x] prior suites for the owned surfaces pass
- [x] governed Python size guard passes with no touched near-hard growth
- [x] changed set matches the Required Artifact Manifest exactly
- [x] staging is empty and no commit was made by the worker
- [x] worker return carries complete packet-shape evidence
- [x] reviewer accepts before any commit

## Operator Checkpoint

The operator authorized this exact bounded packet on 2026-09-08. Any scope
expansion, hook or autorun wiring, registry mutation, provider/live/public or
deployment step requires a fresh operator checkpoint before it may proceed.

## External Knowledge Intake Routing

| Row | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | N/A with reason: no external input was received or consumed while authoring this packet |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | N/A with reason: no external material entered this tranche |
| Disposition | N/A with reason: nothing to absorb, adapt, defer or reject |
| Claim boundary | all inputs were repository-local governed surfaces read at the dispatch base |

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| foundationImpact | NOT_APPLICABLE_WITH_REASON: this tranche hardens one existing checker and its focused tests; it creates, splits, relocates or refactors no durable governance foundation file |
| storageLocation | no durable governance foundation file is created, split, relocated or refactored |
| indexUpdateDisposition | NOT_APPLICABLE_WITH_REASON: no foundation index row is added or moved |
| claimBoundary | records storage-layout impact only; asserts no runtime or retrieval behavior |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this packet | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ENCODING_RENAME_AWARENESS_T1_COMPLETION_2026-09-08.md` | reviewer acceptance | PASS |
| Paired baseline | the paired GC-018 baseline | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Owned implementation | Required Artifact Manifest rows | material commit `d46a55d2b`; focused suite 40/40 | PASS |
| Worker return | the packet worker-return path | worker-return fast and pre-commit gates | PASS |
| Roadmap state | N/A with reason: no roadmap row is opened | N/A with reason | N/A with reason |
| Registry JSON | `governance/compat/CVF_CORPUS_SCAN_REGISTRY.json` | GC-051 aggregate drift check confirms source aggregate aligned; no tranche mutation required | PASS |
| Registry Markdown | `docs/reference/CVF_CORPUS_SCAN_REGISTRY.md` | GC-051 aggregate drift check confirms projection aligned; no tranche mutation required | PASS |
| External evidence digest | N/A with reason: no external evidence consumed | N/A with reason | N/A with reason |
| System loop interlock | encoding standard and ADIF-0011 | policy and learning bindings | PASS |
| Session continuity | active continuity surfaces | separate continuity commit | N/A with reason: material-first choreography |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| Rename-aware enforcement | material commit `d46a55d2b`; focused suite 40/40 | PASS |
| Worker no-commit boundary | target staging empty and HEAD unchanged at handoff | PASS |
| Reviewer acceptance | completion review records `CLOSED_PASS_BOUNDED` | PASS |
| External or provider receipt | N/A with reason: repository-local checker only | N/A_WITH_REASON |

## Evidence Reuse And Encoding Plan

- verificationMode: RECOMPUTE_REQUIRED
- recomputeReason: all Source Pin Contract hashes and owner line counts were recomputed by direct source read at the dispatch base commit because the prior dependency-discovery report contained a false finding, so no earlier session value may be carried forward
- priorVerificationArtifact: N/A with reason: no prior verification artifact is reused as evidence
- priorVerificationAnchor: N/A with reason: no prior verification anchor is reused
- freshRecomputeRequired: true
- unicodePathHandling: literal repo-root paths only, read with UTF-8-safe readers; this packet introduces no Unicode path segment
- extractedTextAuthority: N/A with reason
- externalEvidenceDisposition: N/A with reason: no external evidence or source bundle is consumed
- encodingPlan: ASCII-only authoring for this packet
- claimBoundary: records reuse and encoding intent only; asserts no worker gate result

## Semantic Convergence And Escalation Control

```json
{
  "schemaVersion": "cvf.semanticConvergenceControl.v1",
  "problemKey": "encoding-rename-provenance-t1",
  "chainMode": "INITIAL",
  "chainOrdinal": 0,
  "predecessor": null,
  "blockerDelta": {"prior": [], "resolved": [], "retained": [], "new": [], "reopened": [], "current": []},
  "resolutionEvidence": {},
  "counters": {"partialReadyClosures": 0, "reviewerScopeExpansions": 0, "sameClaimCorrections": 0, "nonDecreasingBlockerTransitions": 0},
  "claims": [{"claimId": "ENCODING-RENAME-T1-DISPATCH-PACKET", "claimClass": "DOCUMENTATION_ONLY", "proofClass": "PROPOSAL_ONLY_NO_RUNTIME_READINESS", "evidenceRef": "docs/baselines/CVF_GC018_ENCODING_RENAME_AWARENESS_T1_2026-09-08.md"}],
  "requiredDisposition": "CONTINUE_BOUNDED",
  "successorScope": "INITIAL_BOUNDED"
}
```

This packet is dispatch documentation only. It authorizes work and carries no
executable proof of its own; the worker return supplies that proof.

## Review-Dispatch Convergence Control

Review-Dispatch Convergence Control: REQUIRED

- dispatchKind: INITIAL
- dispatchSurface: INTERNAL_AGENT
- parentAssignmentId: ENCODING-RENAME-T1
- reviewRoundCount: 0
- priorFindingSetDigest: NOT_APPLICABLE_INITIAL_DISPATCH
- dependencyAuditDisposition: COMPLETE_INITIAL_ACCEPTANCE_MATRIX
- reworkFindingDisposition: NOT_APPLICABLE_INITIAL_DISPATCH
- newIndependentCriticalEvidence: NONE
- regressionGuardDisposition: BASELINE_NEGATIVE_TESTS_PLANNED
- cumulativeExternalInvocationCount: 0
- externalInvocationCeiling: 0
- usageAvailability: NOT_APPLICABLE_INTERNAL_AGENT
- quotaAdmissionDisposition: NOT_APPLICABLE_INTERNAL_AGENT
- nextDispatchDisposition: INITIAL_DISPATCH
- rootCauseClusterId: NOT_APPLICABLE_INITIAL_DISPATCH
- reworkGeneration: 0
- consolidatedDefectClassSweep: COMPLETE_INITIAL_ACCEPTANCE_MATRIX
- successorTrancheOpened: NO
- implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY
- preExecutionReviewAdmission: NOT_REQUIRED_BEFORE_EXECUTION
- preExecutionReviewTrigger: NONE
- nextRoutineReviewBoundary: WORKER_RETURN
- reviewerWorkBoundary: EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION
- latencyDisposition: BOUNDED_LOCAL_AUTHORING
- avoidableDelayClass: NONE_OBSERVED

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: <!--archive-name-exception-->`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | dispatcher -> internal no-commit worker -> reviewer/closer -> session-sync steward |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | dispatchBaseHead=`39be75a7cff4fc9acdbf3dd129254ddb164947d0`; executionBaseHead=captured by the worker at its actual start; closureBaseHead=set by the reviewer |
| changedSetScope(phase) | dispatch pair now; the exact owned paths during execution; material then continuity at closure |
| traceScope(phase, actor) | each actor records only its phase-local changes and inherited concurrent HEAD movement separately |
| commitOwner(phase) | reviewer/closer for accepted material; session-sync steward for continuity; worker commit forbidden |
| crossBatchIsolation | explicit lane handoff with dispatcher mutation forbidden on worker-owned paths while the lane is active |
| sharedWorktreeCoordinationMode | `EXPLICIT_LANE_HANDOFF` |
| activeLaneOwner | ENCODING-RENAME-T1 internal no-commit worker from execution anchor capture until returned status evidence |
| laneOwnedPaths | exactly the Required Artifact Manifest paths |
| dispatcherMutationBoundary | `NO_MUTATION_WHILE_LANE_ACTIVE` |
| laneReleaseEvidence | worker return records final full status and empty staging; reviewer explicitly accepts control before any isolation or commit |
| nextMoveSurfaces | reviewer disposition, material commit, then separate active continuity projection |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch author (packet authoring only) |
| Provider or surface | local workspace; no provider or network surface used |
| Session or invocation | ENCODING-RENAME-T1 dispatch authoring, 2026-09-08 |
| Working directory | repository root |
| Command or tool surface | local file authoring; `git`; local `governance/compat` checkers |
| Target paths | this work order, its paired baseline and the dispatch-author return |
| Allowed scope source | operator authorization on 2026-09-08 for two separate bounded packets |
| Before status evidence | clean worktree; `git status --short` empty; empty staging at `39be75a7cff4fc9acdbf3dd129254ddb164947d0` |
| After status evidence | five pending documentation paths; staging empty; HEAD unchanged |
| Diff evidence | `git diff --name-status` and `git status --short --untracked-files=all` recorded in the dispatch-author return |
| Approval boundary | packet authoring only; no implementation, staging or commit |
| Claim boundary | authorizes bounded work; claims no implementation or runtime behavior |
| Agent type | dispatch author |
| Invocation ID | cvf-encoding-rename-t1-dispatch-authoring-2026-09-08 |
| Expected manifest | five documentation paths |
| Actual changed set | five documentation paths |
| Manifest delta | MATCH |
| Deletion or rename disposition | no deletion, rename or path move occurred |

## Current Runtime Freshness Verification

Verified at dispatch base `39be75a7cff4fc9acdbf3dd129254ddb164947d0` on
2026-09-08 by direct source read. Every owner line count, absent-path claim and
registry classification in this packet was recomputed at that base rather than
carried from an earlier session. No runtime, provider or live surface was
contacted.

## Verification Commands

```powershell
$executionBaseHead = git rev-parse HEAD
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base $executionBaseHead --head HEAD
python -m pytest governance/compat/test_check_agent_packet_authority_and_encoding.py -q
python governance/compat/check_python_automation_size.py --enforce
python governance/compat/check_adif_entry_integrity.py --enforce
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git diff --name-status
git diff --cached --name-status
git status --short --untracked-files=all
```

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_ENCODING_RENAME_AWARENESS_T1_WORKER_RETURN_2026-09-08.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required terms: Purpose; Target / Source; Scope / Methodology; Findings /
Position; Risk / Corrective Action; Claim Boundary; Checker Source Read-Ahead
Block; Agent Operation Trace Block; Delta Execution Claim Boundary Control
Block; Public Export Disposition; executionBaseHead; git status --short.

Conditional terms: External Knowledge Intake Routing; Rescan Intelligence
Hardening; Corpus Completeness And Report Integrity; Finding-To-Governance
Learning Disposition; Epistemic Process Block; Machine Closure Package.

Use `N/A with reason` for every non-applicable conditional block.

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"ENCODING-RENAME-T1","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"PURE_LOCAL_IMPLEMENTATION","authorityImpact":"ENRICHES_EXISTING_OWNER","externalEffect":"NONE","dataSensitivity":"PRIVATE_REPO","reversibility":"GIT_REVERSIBLE","sourceScale":"BOUNDED_CLUSTER","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"KNOWN_PATTERN"},"pathFamilies":["governance/compat","docs/reference","docs/reviews","docs/baselines","docs/work_orders"],"claims":["rename-aware encoding provenance for changed governed paths"],"requiredProof":["pure-rename positive case","rename-plus-new-Unicode negative case","malformed and missing-blob fail-closed cases","focused tests","independent review"],"operatorCheckpoints":["scope expansion","hook or autorun change","runtime or external effect"],"forbiddenEffects":["template or scaffold growth","hook or autorun wiring","runtime or provider execution","public sync","worker commit"],"sourceEvidence":{"selectedFilesFullyRead":true,"corpusReceiptRef":"N/A with reason: bounded named control cluster","completenessClaimChanged":false}}
```

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id ENCODING-RENAME-T1 --title "Encoding Rename Awareness T1" --date 2026-09-08 --base 39be75a7cff4fc9acdbf3dd129254ddb164947d0 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | protected-governance no-commit dispatch profile |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | Reason for NOT_USED_WITH_REASON: the whole packet was authored directly from the canonical work-order template using the accepted ROLE-SOT-MH-T1 packet pair as structural reference. The helper command is recorded for provenance only and was not executed, so no scaffold file was generated or modified. |
| checkerReadAheadConfirmation | Applicable dispatch-quality, scaffold-provenance, structural, routing, size, self-protection and export checkers were read before authoring. |
| docOnlyNewFields | rename-provenance packet fields only; no runtime field |
| claimBoundary | Scaffold provenance proves authoring origin only, not implementation correctness. |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_python_automation_size.py`; `governance/compat/check_adif_entry_integrity.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | `_parse_name_status`; `_added_lines`; `AddedLine`; `ENCODING_EXTENSIONS`; `ENCODING_PATH_PREFIXES`; `EXCEPTION_MARKERS`; `RAW_PREIMAGE_ARCHIVE_ENCODING_EXCEPTIONS`; ADIF `enforcementLevel`, `checkerBindings` and `promotionState`; size classes `python_checker` and `python_test` |
| gateRunPurpose | confirm this packet pair satisfies dispatch-quality, scaffold-provenance, size and structural gates before worker dispatch |
| claimBoundary | records consulted checker sources and literal tokens only; asserts no worker gate result |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | one rename-aware provenance control plus focused regressions and owner documentation |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT - pre-dispatch autorun receipt recorded by the dispatch author |
| actionEvidence | ACTION_EVIDENCE_PRESENT - packet pair authored and validated at dispatch base |
| invocationBoundary | zero external, provider, live or network invocations |
| interceptionBoundary | no Git or filesystem interception is implemented or claimed |
| claimLanguage | bounded checker claims only; no readiness, runtime or production language |
| forbiddenExpansion | no hook, autorun, registry, template, scaffold, session or commit-helper mutation; no sixth path |

## Review-Cost Telemetry

- rootCauseClusterId: ENCODING-RENAME-PROVENANCE
- reworkGeneration: 0
- consolidatedDefectClassSweep: COMPLETE_ALL_KNOWN_DEPENDENCIES
- productionBindingEvidence: none; repository-local pre-commit checker only
- adversarialRegressionDisposition: PASS_TARGETED_DEFECT_CLASS
- successorTrancheOpened: NO
- implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY
- internalAgentInvocationCount: 0
- externalAgentInvocationCount: 0
- providerCallCount: 0
- tokenOrQuotaUsage: 0
- terminalReadinessVerdict: READY_FOR_REVIEW
- reviewerWorkBoundary: reviewer owns acceptance, bounded in-scope repair and all commits

## 13. Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` for any required sixth path, source contradiction,
maintainability violation, registry mutation need, hook or autorun change, or
any case where rename provenance cannot be resolved without expanding scope.

## Rollback Boundary

Revert only accepted ENCODING-RENAME-T1 material: the checker, its tests, the
encoding standard, ADIF-0011 and the packet worker return. Preserve every other
lane and commit.

## Claim Boundary

This packet authorizes one bounded encoding-gate hardening tranche. It claims no
implementation completion, no runtime or provider behavior, no GC-020 change and
no public-sync, deployment or production readiness.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Private provenance dispatch material. No public-sync artifact or public claim is
authorized by this work order.
