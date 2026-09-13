# CVF Agent Work Order - QM Runtime Value R2

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

Date: 2026-09-14

Batch ID: QM-RUNTIME-VALUE-R2

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: d514711fa0386612bda11653be08fc639034b4c2

executionBaseHead: WORKER_MUST_CAPTURE_AT_START

closureBaseHead: N/A - worker does not commit

providerExecutionAuthority: FORBIDDEN

## Dispatch Prompt Envelope

Worker return path: `docs/reviews/CVF_QM_RUNTIME_VALUE_R2_WORKER_RETURN_2026-09-14.md`

completionReviewPath: `docs/reviews/CVF_QM_RUNTIME_VALUE_R2_COMPLETION_2026-09-14.md`

reviewerOwnedClosurePaths: `docs/reviews/CVF_QM_RUNTIME_VALUE_R2_COMPLETION_2026-09-14.md`; active-program/session continuity entries selected by Local after acceptance

Role: internal same-workspace source-evidence worker, relayed through the operator to Claude.
Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_QM_RUNTIME_VALUE_R2_2026-09-14.md`.
Paired authority: `docs/baselines/CVF_GC018_QM_RUNTIME_VALUE_R2_2026-09-14.md`.
Commit mode: `WORKER_MUST_NOT_COMMIT`.
executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`.
Required first actions: read startup/bootstrap/active handoff, this packet, the paired baseline, guard orientation, literal gotchas, and cited output/checker owners; capture full HEAD/status and verify mirror pin, branch/detached state, and clean status.
Current-time notes: 2026-09-14; repository and mirror observations must be captured again at worker start.
Do-not-misread notes: static source evidence only; no source execution, implementation, QM closure, program exit, successor, or repo substitution.
Return contract: write exactly the two owned evidence outputs, do not commit, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

This is an independent `INITIAL` QM lane inside active program
`DOMAIN-PILOT-THREE-REPO-2026-09`. It is not a successor to the stopped
three-repo residual-recovery chain. Do not close QM or the pilot, nominate a
different repo, or choose the next lane.

## Scope Selection And Dependency Release

Local selects this independent lane after accepted R1 closure at
`c3b38dffda7f00778803d2c976926064d8f86b15` and continuity at `d514711fa0386612bda11653be08fc639034b4c2`.
Accepted dependency: `docs/reviews/CVF_QM_RUNTIME_VALUE_R1_COMPLETION_2026-09-14.md`.
Existing residual owner: `docs/audits/CVF_THREE_REPO_RESIDUAL_RECOVERY_2026-09-13.json`.
R2 covers 27 new target blobs, disjoint from R1's 50 target blobs. A linked
test/caller reused from R1 is dependency evidence, not repeated target coverage.
R1's runtime candidates remain unimplemented. The stopped aggregate recovery
chain is not reopened; R2 has its own INITIAL source-evidence question set.
Read-ahead: `src/runs/run-store.ts` RunStore interface, `src/sessions/session-store.ts`
context envelope/interface prefix and `src/processes/process-registry.ts` interface
were inspected only to select scope. No runtime mechanism is pre-accepted.

## Mission

Recover practical runtime/use-case value from the pinned QM source in three
priority trees: `src/runs`, `src/sessions`, and `src/processes`. For each mechanism, establish its real source path from producer
through verification, non-test consumption, integration, tests, and failure
behavior; compare it with the actual existing CVF owner; then issue an
evidence-backed terminal disposition for this lane.

The objective is exhaustive accounting within the named trees, not a quota of
interesting findings. Existing CVF similarity must not erase a distinct QM
consumer, integration, test oracle, failure model, or operational recipe.

## Purpose

Give Local a complete, source-grounded decision packet for the highest-priority
QM runtime regions so Local can accept, defer, reject, or request correction
without repeating the worker's full read.

## Agent Roles

Worker performs the bounded static audit and owns only the return artifacts.
Local is dispatcher, reviewer, closer, commit steward, continuity owner, and
final absorption decision owner. The operator relays this packet. External
agents have no role in source-level execution or final decisions.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "QM-RUNTIME-VALUE-R2",
  "requestedProfile": "P3_ELEVATED",
  "classification": {
    "taskKind": "EXTERNAL_ABSORPTION",
    "authorityImpact": "USES_EXISTING_OWNER",
    "externalEffect": "NONE",
    "dataSensitivity": "PRIVATE_REPO",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "BOUNDED_CLUSTER",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "OWNER_COMPOSITION"
  },
  "pathFamilies": [
    "AGENT_HANDOFF_V60_2026-09-08.md",
    "CVF_SESSION_MEMORY.md",
    "CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json",
    "CVF_SESSION/state/entries/nextAllowedMove.json",
    "CVF_SESSION/ACTIVE_SESSION_STATE.json",
    "CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json",

    "docs/baselines/CVF_GC018_QM_RUNTIME_VALUE_R2_2026-09-14.md",
    "docs/work_orders/CVF_AGENT_WORK_ORDER_QM_RUNTIME_VALUE_R2_2026-09-14.md",
    "docs/audits/CVF_QM_RUNTIME_VALUE_R2_2026-09-14.json",
    "docs/reviews/CVF_QM_RUNTIME_VALUE_R2_WORKER_RETURN_2026-09-14.md",
    ".private_reference/source_mirrors/yc-software__qm/"
  ],
  "claims": ["Static pinned-source runtime-value evidence only"],
  "requiredProof": [
    "Immutable exact-pin corpus manifest",
    "Producer verifier consumer integration and test traces",
    "Per-item terminal value dispositions"
  ],
  "operatorCheckpoints": ["Explicit scope exit only"],
  "forbiddenEffects": [
    "Worker commit",
    "Source execution",
    "Network",
    "Provider calls",
    "Public writes",
    "Implementation"
  ],
  "sourceEvidence": {
    "selectedFilesFullyRead": true,
    "corpusReceiptRef": null,
    "completenessClaimChanged": false
  }
}
```

## Worker Autonomy / No-Question Rule

Proceed autonomously through all in-scope evidence. Resolve routine choices by
the packet and cited authority. Do not pause for the operator to say `next` or
ask which hypothesis to inspect first. If a stop condition occurs, preserve
completed evidence and return `BLOCKED_WITH_REASON`; do not widen scope or
substitute another repository.

## Authority Chain

Operator instruction to finish the three-repo absorption program -> `AGENTS.md`
-> `CVF_SESSION/state/entries/activeExternalAbsorptionProgram.json` ->
`docs/reviews/CVF_EXTERNAL_LOCAL_ABSORPTION_PROGRAM_CONTINUITY_HARDENING_2026-09-13.md`
-> paired GC-018 baseline -> this work order.

## Parent Program Contract Binding

| Field | Required value |
| --- | --- |
| programId | `DOMAIN-PILOT-THREE-REPO-2026-09` |
| sourceId | `yc-software__qm` |
| source state | `INCOMPLETE` |
| nextActionClass | `CONTINUE_ACTIVE_PROGRAM` |
| expansionAllowed | `false` |
| exitDisposition | `RETAIN_ACTIVE_PROGRAM` |
| chainBoundary | `INDEPENDENT_PER_SOURCE_LANES_ONLY` |

Any conflict with these values is a stop condition. Worker output cannot mutate
them or serve as self-acceptance evidence.

## External/Local Coordination Binding

```json
{
  "contractId": "cvf.external-local-absorption-coordination@1",
  "invariants": {
    "externalRole": "ADVISORY_RESEARCH_AND_PATTERN_MAPPING",
    "externalContext": "PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ",
    "localRole": "SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION",
    "finalDecisionOwner": "LOCAL",
    "localCoverageBasis": "SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST",
    "externalEvidenceAuthority": "INPUT_NOT_PRIVATE_CVF_PROOF"
  },
  "contractSha256": "92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c",
  "parentArtifact": "docs/reviews/CVF_EXTERNAL_LOCAL_ABSORPTION_PROGRAM_CONTINUITY_HARDENING_2026-09-13.md"
}
```

## Source And Immutable Boundary

| Field | Required value |
| --- | --- |
| sourceId | `yc-software__qm` |
| mirror | `.private_reference/source_mirrors/yc-software__qm/` |
| required HEAD | `51bf455ea414a58f70274284ce212142518e556a` |
| checkout | record branch/detached state; clean and unchanged before/after |
| source access | local static Git/file reads only |
| upstream fetch/network | forbidden |

Do not reset, checkout, clean, fetch, install, build, test, import, execute, or
modify anything in the mirror. A mismatch or dirty mirror yields
`BLOCKED_WITH_REASON` with secret-safe evidence.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Active program keeps QM next and incomplete | continuity | `CVF_SESSION/state/entries/activeExternalAbsorptionProgram.json` | `value` | `nextSourceId`, `sourceStates`, `expansionAllowed` | `cvf.externalAbsorptionProgramContinuity.v1` | ACCEPT |
| Local owns detailed source verification and final absorption decision | governance | `docs/reference/external_agent_review/CVF_CROSS_WORKSPACE_DOMAIN_FUNNEL_ABSORPTION_METHOD.md` | two-step agreement and program continuity | Local/external role split | canonical method | ACCEPT |
| Program exit is machine constrained | governance implementation | `docs/reviews/CVF_EXTERNAL_LOCAL_ABSORPTION_PROGRAM_CONTINUITY_HARDENING_2026-09-13.md` | decision and validation | continuity checker binding | existing checker owner | ACCEPT |
| QM pin is registered | provenance | `.private_reference/source_mirrors/INDEX.md` | `yc-software__qm` row | exact mirror and commit | source mirror registry | ACCEPT |

These rows establish dispatch authority and provenance only. Worker findings
must add pinned source evidence; this table does not pre-accept runtime value.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`, bootstrap read model, and named active handoff.
2. This work order and paired GC-018 baseline.
3. `docs/reference/guard_orientation/README.md` and literal-format gotchas.
4. Active-program state and its continuity-hardening review.
5. Domain-funnel method, corpus completeness/report integrity standard, and
   corpus-to-knowledge-map reconciliation standard.
6. Mirror `INDEX.md`, prior three-repo audits/reviews only where they contain QM
   claims, then the exact pinned source/test blobs required by this packet.

Do not read full session history by default and do not use provider memory as
canonical evidence.

## Pre-Flight Checks

Capture workspace HEAD/status; confirm both owned outputs' starting existence;
verify exact mirror HEAD, branch/detached state, clean status, and registered pin;
generate the three-tree manifest; record deterministic test-search commands;
and stop before writing if any authority, pin, or ownership condition conflicts.

## Exact Corpus Scope

Build the target manifest from every Git blob under `src/runs/`,
`src/sessions/`, and `src/processes/` at the required immutable pin.
Dispatcher verified 27 blobs: runs=18, sessions=6, processes=3;
bytes=210770. Filesystem-backed `rg --files --hidden --no-ignore`
reconciled with `git ls-tree -r --long` at dispatch, with zero path differences.
Normalized path/blob manifest SHA-256: `9fab809cb263c7cc38ff707a1bc794c692730ebbc918767821919a3dd0a21709`.
Recipe: repo-relative forward-slash path, TAB, lowercase blob SHA; code-point
sort of whole rows, UTF-8 without BOM, LF separators and exactly one final LF.
Worker independently verifies membership/pin, then records one terminal row
per blob: path, blob SHA, byte size, content class, actual depth and status.
Every target source blob is FULL_READ; chunk large files through their end.
Do not infer full reads from filenames, setup code or test headings.

Selected tests: deterministic path/symbol/constructor/error searches; record
commands, exact roots, result paths/counts, inclusion/exclusion reasons and
immutable test blob SHA. Every selected test must be fully read. Current test
ledger has exactly one row per selected path, with blobShaAtPin, read scope,
assertion evidence and limitations. Keep partial/superseded reads in readHistory.
Reconcile selected unique paths=current terminal paths; partial=0 is required
for readiness. A test assertion read is not an executed test result.

Reuse R1's accepted audit for auth/identity/credential/sandbox context and its
already-read linked tests when immutable identity and depth match. Record
REUSED_FULL_READ evidence source/hash explicitly; do not double-count reads.
Read direct callers/imports in core, harness, API, wiring or persistence only
as necessary to resolve a target mechanism; record dependency paths, pin/blob,
read spans and what they establish. This does not expand the target corpus.
All other QM regions remain INCOMPLETE for separate Local accounting.

## Required Hypothesis Rechecks

These are source-derived questions, not accepted findings:

1. Run enqueue deduplication, claim/heartbeat/lease ownership, stale-worker
   completion and memory/Postgres differences (RunStore interface).
2. Retry/error attempt budgets, reaper/requeue/park behavior, graceful drain,
   cancellation/withdrawal and task protection across actual callers.
3. Session sequence/history/context-window/prompt-envelope storage, sharing,
   scope access, restart behavior and memory/Postgres differences.
4. Process registration, TTL/liveness, reaping/reconciliation and cleanup:
   connect the registry to actual sandbox/orchestrator consumers using R1.
5. Run activity, signals and turn stream: producer/consumer subscription,
   delivery ordering, disconnect/reconnect and incomplete/duplicate events.
6. Cross-component lifecycle mismatches, loss/duplication/cleanup failure,
   missing consumers/tests and adverse paths. Distinguish source-guaranteed,
   asserted-by-test and unknown behavior; prove neither concurrency nor
   restart guarantees merely from method names or a happy-path test.

Discover additional mechanisms from the full target ledger; do not force a
fixed record count or presume a new CVF runtime owner is needed.

## Mechanism And Use-Case Evidence Contract

For every candidate or no-new-value conclusion, record:

| Field | Required evidence |
| --- | --- |
| mechanismId / useCaseId | stable ID unique in this audit |
| user/agent outcome | concrete operational outcome |
| source pin | exact required QM commit |
| producer | path, symbol, line/section, blob SHA |
| verifier | validation/authz/check path and failure result |
| non-test consumer | path and invocation/consumption link, or explicit missing evidence |
| integration link | route/service/CLI/runtime path joining producer to consumer |
| tests | path, case/assertion, what it proves and does not prove |
| failure semantics | error, retry, cleanup, denial, fallback, or propagation behavior |
| source-native status | whether QM itself wires and uses the mechanism |
| CVF comparison owner | governed CVF path/symbol/section, or `OWNER_NOT_FOUND` with bounded negative search |
| delta beyond CVF | specific reusable behavior, oracle, fixture, recipe, or missing link |
| practical benefit | expected CVF outcome and affected consumer |
| evidence confidence | `HIGH`, `MEDIUM`, or `LOW` with reason |
| terminal value disposition | one allowed value below |
| next action / trigger | concrete action or reopen trigger |

Allowed terminal value dispositions for each item:

- `CONFIRMED_EXISTING_NO_ADDITION`
- `ADAPT_CANDIDATE`
- `DEFER_WITH_TRIGGER`
- `REJECT_NO_ACTIONABLE_VALUE`
- `BLOCKED_WITH_REASON`

`ADAPT_CANDIDATE` is a reviewer input, not permission to copy or implement.
`CONFIRMED_EXISTING_NO_ADDITION` requires a cited existing CVF owner and a
comparison of consumer, integration, tests, and failure semantics. A shared
pattern name is insufficient.

## CVF Comparison Discipline

Search the smallest governed CVF owner surfaces that can test each claim.
Record search query and roots. Cite canonical standards/runtime/source/tests,
not provider memory. Separate these questions:

- Does CVF describe the pattern?
- Does CVF implement or own the behavior?
- Does a real CVF consumer invoke it?
- Does CVF carry equivalent validation, failure semantics, and test evidence?
- Does QM contribute a useful integration or oracle even when the abstraction exists?

If the owner search is inconclusive, use `BLOCKED_WITH_REASON` or
`DEFER_WITH_TRIGGER`; do not convert absence of proof into novelty.

## Required Outputs And Write Ownership

Worker may create or replace exactly:

1. `docs/audits/CVF_QM_RUNTIME_VALUE_R2_2026-09-14.json`
2. `docs/reviews/CVF_QM_RUNTIME_VALUE_R2_WORKER_RETURN_2026-09-14.md`

The JSON audit is the structured evidence source. The Markdown return summarizes
it and reports validation. Do not edit this packet, its baseline, mirrors,
INDEX, runtime/product source, tests, governance, session state, handoff, SOT,
other audits/reviews, or any external-agent folder. Do not create convenience
scripts or temporary files inside the repository.

## Write Ownership

Exact worker-owned paths are the JSON audit and Markdown worker return listed
above. All other repository paths are read-only. The worker must report the
actual changed set and a `MATCH` or `MISMATCH` comparison to this two-path
manifest.

## Audit Shape

The JSON must contain at least:

- schema/version, batch ID, program binding, source identity and pin evidence;
- before/after repository and mirror state;
- exact target manifest and read-depth ledger;
- deterministic test discovery ledger and fully read test set;
- hypothesis outcomes;
- mechanism/use-case records with every evidence-contract field;
- CVF owner searches and comparison results;
- disposition counts and ID lists that reconcile to all reported items;
- exclusions, unknowns, contradictions, and remaining QM regions;
- validation commands/results and claim boundary.

Use JSON-valid strings and arrays. Do not embed an unbounded source dump.

## Execution Plan

1. Complete startup and pre-flight checks.
2. Generate and reconcile the immutable three-tree blob manifest.
3. Fully read target code and discover/read directly relevant tests.
4. Trace every mechanism through producer, verifier, consumer, integration,
   tests, and failures; run bounded CVF owner searches.
5. Assign one terminal per-item disposition and reconcile all counts/IDs.
6. Write the JSON audit, derive the Markdown return, validate both, and recheck
   workspace/mirror state without committing.

## Evidence Requirements

Evidence must be path-, symbol-, pin-, and blob-specific. Counts need commands
and reconciliation. Negative searches need query and roots. Missing consumers,
owners, tests, or links remain explicit. Separate observed source behavior from
inference and from proposed CVF adaptation. Preserve contradictions and adverse
findings with the same detail as promising candidates.

## Acceptance Criteria

The return is reviewable only when the exact pin and mutation boundary hold;
all target blobs and selected tests reconcile; every value record satisfies the
evidence contract and has one terminal disposition; all prior hypotheses have
outcomes; remaining QM scope is explicit; JSON parses; and the fast return gate
passes. `COMPLETE_PENDING_REVIEW` means evidence complete for review, not accepted.

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The Markdown return must include:

- `Status: COMPLETE_PENDING_REVIEW` or `Status: BLOCKED_WITH_REASON`;
- exact HEAD/status before and after;
- exact mirror pin/status before and after;
- output paths and hashes;
- corpus/test ledger reconciliation;
- mechanism disposition table with IDs and counts;
- material contradictions and retained unknowns;
- explicit statement that QM and the parent program remain open;
- commands run and exit results;
- confirmation of zero commits and zero unauthorized mutations.

Do not label the return `ACCEPTED_REVIEW`, `CLOSED_PASS_BOUNDED`, or equivalent.
Only Local may review, accept, update program state, select implementation, or
issue the next independent lane.

## Intake Role Routing Decision

| Field | Disposition |
| --- | --- |
| Intake summary | Operator request to continue the active three-repository program by dispatching Claude on QM runtime-value recovery |
| Scope classification | Bounded static source audit with exactly two worker-owned output paths |
| Risk sensitivity | Private source evidence; no provider, live, secret, public-sync, production, or upstream execution |
| canonical route mode | `MULTI_AGENT_SINGLE_ROLE` |
| selected role route | Internal worker produces evidence; Local orchestrator/reviewer makes decisions and closes |
| Worker role | Pinned QM mirror and two owned outputs; evidence production only |
| Reviewer role | Private CVF owners, review, closure, commit, and continuity |
| External-agent role | `NOT_INVOKED`; no source-runtime or final authority |
| Escalation condition | Stop and return `BLOCKED_WITH_REASON` on a stated stop condition; operator checkpoint only for explicit program scope exit |
| Disposition | ACCEPT |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | Local author/reviewer/closer; internal evidence worker |
| phase | QM bounded source audit then independent Local review |
| baseHeadFor(phase) | dispatchBaseHead=d514711fa0386612bda11653be08fc639034b4c2; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | dispatch pair; then exactly two worker outputs; then Local review/continuity |
| traceScope(phase, actor) | exact commands, hashes, mirror state, and changed set for each actor |
| commitOwner(phase) | Local closer; worker forbidden |
| crossBatchIsolation | one active QM lane; no concurrent repository mutation |
| nextMoveSurfaces | active-program state and Local-owned completion/continuity only after review |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF
activeLaneOwner: internal QM evidence worker after committed dispatch
laneOwnedPaths: exactly the two worker-owned output paths; mirror read-only
dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE
laneReleaseEvidence: terminal worker return and exact changed-set reconciliation

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_QM_RUNTIME_VALUE_R2_COMPLETION_2026-09-14.md` |
| reviewerOwnedClosurePaths | exact worker outputs, completion review, and separately authorized continuity paths |
| closureOwner | Local reviewer/closer |
| workerCommitPermission | FORBIDDEN |

Local reviewer will sample high-value and adverse cases, verify manifest/count
reconciliation, test at least one owner-match and one novelty/defer conclusion,
confirm pin and mutation boundaries, and run applicable M5/M10/safety/M20 gates.
Local will not adopt worker self-assessment as closure evidence.

An accepted return may close only `QM-RUNTIME-VALUE-R2`. QM remains
`INCOMPLETE` until all remaining repository regions and accepted/deferred/
rejected values are terminally accounted. The parent program remains active
until all three source states are terminal or the operator records an explicit
governed scope-exit decision.

## Review Gate

Local reviews M5/M10/safety/M20 evidence: corpus reconciliation, one positive
candidate, one no-addition/defer/reject item, source-to-consumer trace, owner
comparison, pin/status, and exact changed paths. Any contradiction triggers a
bounded targeted check, not a duplicate full audit.

## Gate-To-Role Closeability Contract

closeabilityContractVersion: cvf.gate-role-closeability@1.0.0
closeabilityDisposition: CLOSEABLE
implementationTopologyPolicy: EXACT_PATHS_WITH_NO_FORESEEABLE_SPLIT
foreseeableFileSplitDisposition: NOT_REQUIRED_UNDER_SIZE_BUDGET
returnTimeRecheck: REQUIRED_BEFORE_REPAIR

| gateId | mustPassBy | repairOwner | repairPhase | mutationSurface | topology | commitOwner | commitPhase | dependsOn |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| authorization_review | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired dispatch documents | EXACT_PATHS | closer | DISPATCH_COMMIT | NONE |
| pre_dispatch_gate | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired dispatch documents | EXACT_PATHS | closer | DISPATCH_COMMIT | authorization_review |
| dispatch_continuity | IMPLEMENTATION | session-sync-steward | IMPLEMENTATION | `AGENT_HANDOFF_V60_2026-09-08.md` material-SHA marker plus active program and current authority | EXACT_PATHS | session-sync-steward | DISPATCH_CONTINUITY_COMMIT | pre_dispatch_gate |
| pre_implementation_autorun | IMPLEMENTATION | worker | IMPLEMENTATION | exact worker-owned outputs | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| source_identity_license | WORKER_RETURN | worker | IMPLEMENTATION | audit and return | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_implementation_autorun |
| inventory_depth_value | WORKER_RETURN | worker | IMPLEMENTATION | audit and return | EXACT_PATHS | closer | MATERIAL_COMMIT | source_identity_license |
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | audit and return | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity, inventory_depth_value |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | worker return | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| worker_return_fast | REVIEW | worker | WORKER_RETURN | exact worker-owned outputs | EXACT_PATHS | closer | MATERIAL_COMMIT | adif_integrity |
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | worker outputs and completion review | EXACT_PATHS | closer | MATERIAL_COMMIT | worker_return_fast |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | REVIEW | exact reviewed material set | EXACT_PATHS | closer | MATERIAL_COMMIT | reviewer_fast |
| terminal_completion_review | PRE_MATERIAL_COMMIT | reviewer | REVIEW | completionReviewPath | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | Local continuity paths | EXACT_PATHS | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL | exact reviewed ranges | EXACT_PATHS | closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

## Closure Checklist

- Worker status and output hashes present.
- JSON parses and all counts/IDs reconcile.
- Mirror and workspace boundaries remain valid.
- No worker commit or unauthorized path mutation exists.
- Reviewer completion artifact records accepted, rework, deferred, or blocked.
- Active program remains or changes only through Local-owned continuity evidence.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` when all criteria and gates pass. Return
`BLOCKED_WITH_REASON` with completed partial evidence and the exact stop
condition otherwise. Never self-close, self-accept, or issue a successor.

## Operator Checkpoint

No routine operator checkpoint is parked. Operator input is required only for
an explicit scope-exit decision or a contradiction that changes the authorized
three-repository program. Local otherwise reviews and continues autonomously.

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: QM-RUNTIME-VALUE-R2
reviewRoundCount: 0
priorFindingSetDigest: NOT_APPLICABLE_INITIAL_DISPATCH
dependencyAuditDisposition: COMPLETE_INITIAL_ACCEPTANCE_MATRIX
reworkFindingDisposition: NOT_APPLICABLE_INITIAL_DISPATCH
newIndependentCriticalEvidence: NONE
regressionGuardDisposition: BASELINE_NEGATIVE_TESTS_PLANNED
cumulativeExternalInvocationCount: 0
externalInvocationCeiling: 0
usageAvailability: NOT_APPLICABLE_INTERNAL_AGENT
quotaAdmissionDisposition: NOT_APPLICABLE_INTERNAL_AGENT
nextDispatchDisposition: INITIAL_DISPATCH
rootCauseClusterId: NOT_APPLICABLE_INITIAL_DISPATCH
reworkGeneration: 0
consolidatedDefectClassSweep: COMPLETE_INITIAL_ACCEPTANCE_MATRIX
successorTrancheOpened: NO
implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY
preExecutionReviewAdmission: NOT_REQUIRED_BEFORE_EXECUTION
preExecutionReviewTrigger: NONE
nextRoutineReviewBoundary: WORKER_RETURN
reviewerWorkBoundary: EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION

## Semantic Convergence Outcome

Standard: `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md`

```json
{
  "schemaVersion": "cvf.semanticConvergenceControl.v1",
  "problemKey": "QM-RUNTIME-VALUE-R2",
  "chainMode": "INITIAL",
  "chainOrdinal": 0,
  "predecessor": null,
  "blockerDelta": {
    "prior": [],
    "resolved": [],
    "retained": [],
    "new": [],
    "reopened": [],
    "current": []
  },
  "resolutionEvidence": {},
  "counters": {
    "partialReadyClosures": 0,
    "reviewerScopeExpansions": 0,
    "sameClaimCorrections": 0,
    "nonDecreasingBlockerTransitions": 0
  },
  "claims": [],
  "requiredDisposition": "CONTINUE_BOUNDED",
  "successorScope": "INITIAL_BOUNDED"
}
```

This independent lane has no predecessor. Do not bind it to the stopped
aggregate recovery chain or use that chain's blocker count as this lane's
closure evidence.

## Validation Requirements

Before return:

1. parse the audit with Python JSON tooling;
2. verify only the two owned paths changed relative to captured start state;
3. recheck workspace and mirror HEAD/status;
4. run applicable document/audit checks that do not execute upstream source;
5. record command, exit code, and concise result for every validation;
6. leave both output files uncommitted for Local review.

No live governance claim is made, so the release-quality provider gate is not
applicable. Do not invoke it merely to populate evidence.

## Verification Commands

- `python -m json.tool docs/audits/CVF_QM_RUNTIME_VALUE_R2_2026-09-14.json`
- `python governance/compat/run_worker_return_fast_gate.py`
- `git status --short --untracked-files=all`
- `git rev-parse HEAD`
- `git -C .private_reference/source_mirrors/yc-software__qm rev-parse HEAD`
- `git -C .private_reference/source_mirrors/yc-software__qm status --short`

## Stop Conditions

Stop and return bounded evidence if the mirror is dirty or off pin; required
source is unreadable; corpus totals cannot reconcile; output ownership is
insufficient; source execution or network access appears necessary; or a
governed authority contradicts this packet. Do not repair the mirror, widen
scope, edit another path, substitute another repository, or wait for the
operator to choose a different task.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`EXTERNAL_ABSORPTION`, role=`ORCHESTRATOR`, lifecyclePhase=`DISPATCH`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class EXTERNAL_ABSORPTION --role ORCHESTRATOR --lifecycle-phase DISPATCH --json`.

Returned defects: NONE_RETURNED
Result on 2026-09-14: `items=[]`, `totalCandidates=0`, `truncated=false`.

## Negative Search And Collision Discipline

Before dispatch, Local verified that the exact two target output paths and the
paired packet paths did not already exist. Worker must recheck the two owned
output paths and report whether it creates or replaces them. Same-token QM
history is expected and is evidence input, not a naming collision.

## Current Runtime Freshness Verification

`runtimeClaimPresent=NO`; `runtimeMutationAuthorized=NO`;
`freshnessVerificationMode=NOT_APPLICABLE_WITH_REASON`. This lane audits pinned
source semantics and does not claim current CVF runtime/provider behavior.

## External Repository Absorption Entry Control

| Field | Value |
| --- | --- |
| Source type | external repository pinned in a local ignored source mirror |
| Upstream or source-mirror disposition | read-only exact pin `51bf455ea414a58f70274284ce212142518e556a`; no fetch or mutation |
| Enumeration or manifest plan | exact-pin `git ls-tree` for three named source trees plus a separate linked-test ledger |
| Per-file terminal-ledger plan | every target blob receives `READ`, `SKIPPED_WITH_REASON`, `DEFERRED`, or `BLOCKED_UNREADABLE` plus read depth |
| Owner or overlap route | bounded private-CVF owner search per mechanism |
| Value-disposition route | Local reviews item dispositions; worker cannot accept or implement |
| Claim boundary | static evidence recovery only; no source copy, execution, implementation, or absorption acceptance |

## Overlap And Novelty Classification

Classify every mechanism independently as exact existing coverage, useful
source-specific delta, deferred value, rejected value, or blocked evidence.
Comparison must cover the consumer, integration, tests, and failure semantics;
pattern-name similarity alone cannot establish no-new-value, and external
shortlists cannot limit Local source-derived coverage.

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| Each discovered QM mechanism | `OWNER_SURFACE_NOT_FOUND` until the worker records an exact owner | `OWNER_SURFACE_NOT_FOUND` | Consumer, integration, tests, failures, and operational recipe remain to compare | Worker replaces with an allowed evidence-backed classification and item disposition |
| Program coordination contract | `docs/reference/external_agent_review/CVF_CROSS_WORKSPACE_DOMAIN_FUNNEL_ABSORPTION_METHOD.md` | `CONFIRMED_EXISTING` | No new coordination owner is needed | Reuse owner while auditing source-derived value |

## Mandatory Blind-Spot Control Block

The three-tree manifest is exhaustive within scope. Required blind-spot checks
cover non-test consumers, integration links, adverse/failure paths, provider
differences, lifecycle/cleanup, test oracles, and prior residual hypotheses.
Uninspected QM directories remain explicit and cannot inherit this lane's
disposition. UNKNOWN is never converted to no value.

## Corpus Completeness And Report Integrity

- Corpus task class: bounded pinned-source semantic audit.
- Corpus root: three exact QM source trees at the required commit.
- Snapshot time: worker captures UTC start/end at the immutable pin.
- Enumeration command: filesystem-backed `rg --files --hidden --no-ignore <three mirror paths>`, reconciled to `git ls-tree -r --full-tree <pin> -- <three paths>` for immutable blob identity.
- Manifest artifact or inline manifest: worker-owned JSON audit.
- Manifest hash: worker computes from normalized path/blob rows.
- Processing ledger artifact or inline ledger: worker-owned JSON audit.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.
- Reconciliation: dispatch state `manifest=27; ledger_terminal=0; exclusions=0; unresolved=27`; worker must reach `manifest=27; ledger_terminal=27; exclusions=0; unresolved=0` and reconcile all depth buckets.
- Declared exclusions: all QM paths outside three target trees, except directly linked tests in their separate ledger.
- Unresolved files: 27 at dispatch; worker records each individually until unresolved=0; none may disappear from counts.
- Unreadable or unsupported files: worker records individually; none may disappear from counts.
- Aggregation check: unique path/blob rows and item IDs reconcile without cross-unit addition.
- Drift check: exact pin and clean mirror before/after.
- Output traceability: audit JSON to Markdown return and Local completion review.
- Adversarial verification: enumeration is not semantic absorption; test names are not behavior proof.
- Corpus verdict: PARTIAL - exhaustive only for the named trees, not all QM.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | `External repo or copied folder` |
| Chain map route | active Local per-source runtime-value recovery |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | `docs/reference/external_agent_review/CVF_CROSS_WORKSPACE_DOMAIN_FUNNEL_ABSORPTION_METHOD.md` |
| Disposition | per item only; `ADAPT`, `DEFER`, `REJECT`, `BLOCK`, or existing/no-addition |
| Claim boundary | Work-order routing only; no source value or absorption is accepted here |

## Checker Source Read-Ahead Block

| Field | Evidence |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_external_knowledge_intake_routing.py` |
| literalTokensReviewed | dispatch status, commit mode, return status, program markers, SCEC initial sentinel |
| gateRunPurpose | dispatch confirmation, not source discovery |
| claimBoundary | validates packet structure only |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind source-intake --batch-id QM-RUNTIME-VALUE-R2 --title "QM Run Session Process Lifecycle" --date 2026-09-14 --base d514711fa --commit-mode WORKER_MUST_NOT_COMMIT --dependency docs/reviews/CVF_QM_RUNTIME_VALUE_R1_COMPLETION_2026-09-14.md --include-worker-return-skeleton --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --review-round-count 0 --scec-problem-key QM-RUNTIME-VALUE-R2 --scec-chain-mode INITIAL --scec-chain-ordinal 0 --scec-required-disposition CONTINUE_BOUNDED --scec-successor-scope INITIAL_BOUNDED --stdout` |
| generatedProfile | source-intake, no-commit, INITIAL |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Reused R1 dispatch contract structure; replaced scope, hypotheses and base; corrected gate CLI and output reconciliation requirements from accepted R1 closure |
| checkerReadAheadConfirmation | Prior R1 reviewed literals and current scaffold/source-intake, review-cost, closeability and corpus requirements consumed |
| docOnlyNewFields | exact R2 27-blob boundary and R1 evidence reuse |
| claimBoundary | dispatch only; no semantic/source-runtime acceptance |

## Foundation Storage Layout Block

Use existing `docs/baselines`, `docs/work_orders`, `docs/audits`, and
`docs/reviews` families. No new foundation owner, folder, registry, or layout
migration is authorized. The existing mirror INDEX remains provenance owner.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Local author; delegated worker after relay |
| Agent type | orchestrator author / internal evidence worker |
| Provider or surface | Codex local authoring; internal worker execution |
| Session or invocation | `QM-RUNTIME-VALUE-R2` |
| Invocation ID | worker must capture its local invocation/session identifier or `UNAVAILABLE_WITH_REASON` |
| Working directory | repository root |
| Command or tool surface | static Git and filesystem reads; worker-return fast gate |
| Target paths | paired packet and Local-only exact continuity manifest above; worker later owns exactly two evidence outputs |
| Allowed scope source | operator instruction to continue until all three repos are handled; paired baseline |
| Before status evidence | clean worktree at `d514711fa0386612bda11653be08fc639034b4c2` before Local authoring; worker recaptures at start |
| After status evidence | Local authoring changes paired dispatch docs; worker later reports exact owned delta |
| Diff evidence | `git status --short --untracked-files=all`; worker records output hashes |
| Expected manifest | docs/work_orders/CVF_AGENT_WORK_ORDER_QM_RUNTIME_VALUE_R2_2026-09-14.md; docs/baselines/CVF_GC018_QM_RUNTIME_VALUE_R2_2026-09-14.md; AGENT_HANDOFF_V60_2026-09-08.md; CVF_SESSION_MEMORY.md; CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json; CVF_SESSION/state/entries/nextAllowedMove.json; CVF_SESSION/ACTIVE_SESSION_STATE.json; CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json; worker phase separately limited to the two outputs |
| Actual changed set | docs/work_orders/CVF_AGENT_WORK_ORDER_QM_RUNTIME_VALUE_R2_2026-09-14.md; docs/baselines/CVF_GC018_QM_RUNTIME_VALUE_R2_2026-09-14.md; AGENT_HANDOFF_V60_2026-09-08.md; CVF_SESSION_MEMORY.md; CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json; CVF_SESSION/state/entries/nextAllowedMove.json; CVF_SESSION/ACTIVE_SESSION_STATE.json; CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json |
| Manifest delta | worker must record `MATCH` or list exact mismatch and stop |
| Approval boundary | worker may execute this static audit after packet commit |
| Claim boundary | no implementation, source execution, or program exit |

## Delta Claim Boundary

This packet adds dispatch authority and an evidence contract. It does not add
QM behavior to CVF and does not prove any candidate valuable or already owned.

## Claim Boundary

Authorized result: a bounded, reviewable source-evidence packet for the three
named QM trees. Unauthorized claims include complete QM absorption, complete
three-repo absorption, implementation readiness without Local review, external
authority, provider/live behavior, public export, deployment, or production.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance work order with no public artifact or sync scope.

## Output Acceptance Lessons From R1

Before writing outputs, read each applicable checker source. Both outputs must
be internally consistent, including nested mechanism fields, hypotheses,
unknowns, history, disposition counts and Markdown projections. Audit hashes
are computed after the final content edit; preserve old hashes as history.
Use real current-state rows, not appended duplicates or placeholder success.
The final return includes the actual no-argument fast-gate command, exit code,
final receipt and preserved failure history. A gate PASS is structural evidence,
not semantic acceptance. Do not treat F-number examples as the whole scope.
Full R1 return source may be reused as a shape reference, never as R2 evidence.
Required literal sections include Target / Source, Corpus Completeness And
Report Integrity, Knowledge System Reconciliation, Mandatory Blind-Spot Control
Block, External Repository Absorption Entry Control, External/Local Coordination
Binding, Overlap And Novelty Classification, Return-Time Closeability Recheck,
Semantic Convergence Outcome and generation-0 convergence self-proof.
Before return additionally run the three bounded checks below, because the
fast gate alone did not expose these R1 pre-commit requirements:

- `python governance/compat/check_absorption_blindspot_control_presence.py --base d514711fa0386612bda11653be08fc639034b4c2 --head HEAD --enforce`
- `python governance/compat/check_corpus_completeness_report_integrity.py --base d514711fa0386612bda11653be08fc639034b4c2 --head HEAD --enforce`
- `python governance/compat/check_corpus_to_knowledge_map_reconciliation.py --base d514711fa0386612bda11653be08fc639034b4c2 --head HEAD --enforce`

These are additive checks, not a substitute for the required fast gate. On
outside-authority failures, return BLOCKED_WITH_REASON; never edit checkers or
protected state. Tool-owned ignored gate receipts are allowed side effects;
no additional authored script/output file is authorized.

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: bounded new QM source-evidence lane; no legacy
foundation owner/workflow-chain migration or package admission.

## Mixed Protected-Path Atomicity Authorization

Disposition: AUTHORIZED_EXACT_MANIFEST

Atomicity reason: publish the R2 dispatch authority and its currentAuthority
fingerprints/next-move together; worker owns none of the continuity paths.
A dedicated post-material continuity commit records the known dispatch SHA.
Rollback boundary: revert the exact R2 dispatch projection together; preserve
accepted R1 closure and the open three-repository program.
Exact changed manifest:

- `docs/work_orders/CVF_AGENT_WORK_ORDER_QM_RUNTIME_VALUE_R2_2026-09-14.md`
- `docs/baselines/CVF_GC018_QM_RUNTIME_VALUE_R2_2026-09-14.md`
- `AGENT_HANDOFF_V60_2026-09-08.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`

## Core Guard Self-Protection Authorization

Operator authorization: operator requested the next worker assignment after
Local closed R1. Standing Local orchestrator mandate owns same-program dispatch
and its exact authority/continuity projection, with no new source implementation.
Authorized scope: current R2 baseline/work-order hashes, handoff and next move.
Protected paths:

- `AGENT_HANDOFF_V60_2026-09-08.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`

Rollback boundary: revert R2 dispatch projection only. Do not change checkers,
hooks, provider credentials, public state, runtime code or source mirrors.
Worker edits only its two evidence outputs after committed dispatch.
