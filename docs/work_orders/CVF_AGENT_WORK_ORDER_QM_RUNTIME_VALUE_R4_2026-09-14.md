# CVF Agent Work Order - QM Runtime Value R4

Memory class: governed-worker-dispatch

docType: work_order

Status: CLOSED_PASS_BOUNDED

Date: 2026-09-14

Batch ID: QM-RUNTIME-VALUE-R4

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: fd231762b9cae0bc425e5fa61ac5fd9799ff5bff

executionBaseHead: WORKER_MUST_CAPTURE_AT_START

closureBaseHead: N/A - worker does not commit

providerExecutionAuthority: FORBIDDEN

## Dispatch Prompt Envelope

Historical HOLD: R4 repair was parked for EVIDENCE-READINESS-T1. Local released it in continuity commit 7271f4f10 under operator instruction; this review reconciles the stale dispatch status.
Local accepts bounded R4 evidence with one explicit supplementary-test exception: test/agent-tools.test.ts is PARTIAL_READ (213/3237 lines), outside fullyReadTests; its remainder remains unknown. All other selected test reads retain the full-read requirement. No runtime or whole-repository closure.
Two current worker outputs remain unaccepted and frozen; no findings are closed.

Worker return path: `docs/reviews/CVF_QM_RUNTIME_VALUE_R4_WORKER_RETURN_2026-09-14.md`

completionReviewPath: `docs/reviews/CVF_QM_RUNTIME_VALUE_R4_COMPLETION_2026-09-14.md`

reviewerOwnedClosurePaths: `docs/reviews/CVF_QM_RUNTIME_VALUE_R4_COMPLETION_2026-09-14.md`; active-program/session continuity entries selected by Local after acceptance

Role: internal same-workspace source-evidence worker, relayed through the operator.
Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_QM_RUNTIME_VALUE_R4_2026-09-14.md`.
Paired authority: `docs/baselines/CVF_GC018_QM_RUNTIME_VALUE_R4_2026-09-14.md`.
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

Accepted R1 material: c3b38dffda7f00778803d2c976926064d8f86b15.
Accepted R2 material: e081c2eb6e2dfbb218e646609258d04fa3e1f8d4.
Accepted R3 material: bc914729c149ddc1f5d3d22c62eaab9b1d2769aa.
Accepted dependency: `docs/reviews/CVF_QM_RUNTIME_VALUE_R3_COMPLETION_2026-09-14.md`.
Existing residual owner: `docs/audits/CVF_THREE_REPO_RESIDUAL_RECOVERY_2026-09-13.json`.
R4 has 19 memory targets, disjoint from R1/R2/R3 target paths. Reuse prior
linked-test evidence only after exact blob and full-read provenance checks.
Read-ahead: Git/file inventory, preliminary test-path search and upstream diff
for primitives, agent-tools and async cancellation. No target semantic read or
mechanism acceptance is claimed by dispatch.

## Mission

Recover runtime/use-case value from every blob under `src/memory`.
Trace each mechanism through producer, verifier, non-test consumer, integration,
tests and failures; compare against real CVF owners. Include bench.ts and all
provider/strategy adapters. Account for adverse findings and operational recipes
without a quota of promising candidates.

## Purpose

Give Local a complete, source-grounded decision packet for the highest-priority
QM runtime regions so Local can accept, defer, reject, or request correction
without repeating the worker's full read.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| INTERNAL_AGENT | Paired work order and two evidence outputs | Static inspection and pending return | Exact manifest and authority | Internal relay; no adapter needed | CONTRACT_ONLY |
| EXTERNAL_AGENT_CLI_MCP | No external interface selected | No CLI/MCP or provider invocation | Private owner comparison requires local inspection | No external consumer requirement; adapter deferred | N/A_WITH_REASON |

## Agent Roles

Worker performs the bounded static audit and owns only the return artifacts.
Local is dispatcher, reviewer, closer, commit steward, continuity owner, and
final absorption decision owner. The operator relays this packet. External
agents have no role in source-level execution or final decisions.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "QM-RUNTIME-VALUE-R4",
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
    ".private_reference/source_mirrors/INDEX.md",
    "AGENT_HANDOFF_V60_2026-09-08.md",
    "CVF_SESSION_MEMORY.md",
    "CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json",
    "CVF_SESSION/state/entries/nextAllowedMove.json",
    "CVF_SESSION/ACTIVE_SESSION_STATE.json",
    "CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json",

    "docs/baselines/CVF_GC018_QM_RUNTIME_VALUE_R4_2026-09-14.md",
    "docs/work_orders/CVF_AGENT_WORK_ORDER_QM_RUNTIME_VALUE_R4_2026-09-14.md",
    "docs/audits/CVF_QM_RUNTIME_VALUE_R4_2026-09-14.json",
    "docs/reviews/CVF_QM_RUNTIME_VALUE_R4_WORKER_RETURN_2026-09-14.md",
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
    "selectedFilesFullyRead": false,
    "corpusReceiptRef": null,
    "completenessClaimChanged": false
  },
  "initialIntakeAdmission": {
    "stage": "INITIAL_ACQUISITION_SURVEY",
    "plannedReceiptPath": "docs/audits/CVF_QM_RUNTIME_VALUE_R4_2026-09-14.json",
    "acceptanceDisposition": "NO_ABSORPTION_ACCEPTANCE",
    "nextStageAuthority": "SEPARATE_REVIEWED_WORK_ORDER",
    "unknownEvidencePolicy": "PRESERVE_UNKNOWN"
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
| required HEAD | `361a6c0095dcd3d156aca91353f3ffba0bb8b69b` |
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
generate the memory-tree manifest; record deterministic test-search commands;
and stop before writing if any authority, pin, or ownership condition conflicts.

## Exact Corpus Scope

Fully read all 19 blobs at `361a6c0095dcd3d156aca91353f3ffba0bb8b69b`; Git blob bytes=86253.
Manifest SHA-256: `5fb76f1a20a702dfcf25ad38ace8f6f68491cff8f2791919b5a8c820de20bcfc`.
Recipe: repo-relative forward-slash path + TAB + lowercase blob SHA; code-point
sorting; UTF-8 without BOM, LF joins, exactly one final LF. Git/file membership
matches with zero differences. Sizes are Git bytes, not CRLF checkout bytes.

| Target path | blobShaAtPin | Git blob bytes |
| --- | --- | --- |
| src/memory/bench.ts | 1bbfa2d66a26e5a8d7b4cf6a25b2effe299ae7b8 | 5796 |
| src/memory/mcp-memory-provider.ts | 5b756abb2dbda81eb378cab32da794f40214e9c0 | 3243 |
| src/memory/memorable/capture.ts | 660f67c9a29556ecec0d39bcf55c5ad154e4b25f | 4533 |
| src/memory/memorable/config.ts | 5b2b9148ad96c1dbb101a32e64b9e2be814938fd | 3880 |
| src/memory/memorable/inject.ts | 55bf1821b5fea2d8088b9476fe672ea40685d942 | 2625 |
| src/memory/memorable/provider.ts | b58bb2b9a9caf3cc9f664ac4a21504c3b1b62778 | 3376 |
| src/memory/memorable/relay.ts | b4cd958e6d92819efa8d3513463da7eb4f2671ed | 2535 |
| src/memory/memory-service.ts | eaa9c446c3a431711e753e9735c68eae09671efd | 6918 |
| src/memory/notebook.ts | 27e3fc0b4419f2613addd7a00eeea319187d8a9d | 948 |
| src/memory/policy.ts | faddf2b52e3e43fbc0ab0392de871db158016118 | 1222 |
| src/memory/postgres-memory-service.ts | a432e8871eff50b2183941e7f6dddff1de980922 | 6726 |
| src/memory/provider-config.ts | 64c9b6b5eb305a9c841466642c1f70ae313a0e11 | 7602 |
| src/memory/provider-factory.ts | 875d95ad01e93eacf7ded2e4031d102abd1cedd2 | 3323 |
| src/memory/provider-router.ts | 32434883da4b86da8c32ed438caa2ab29a13d93f | 5431 |
| src/memory/strategies/agent-only.ts | c973145b5e0663de6c32750969456d02619095d0 | 788 |
| src/memory/strategies/consolidation.ts | e28321c84655e45a0e5aaf1aca54fddc57fa7368 | 7685 |
| src/memory/strategies/per-turn.ts | 9db5d581723438555db0c08323066d95294ecc40 | 6602 |
| src/memory/strategies/scratch-promote.ts | 216c0a4004ce39788aedfd734271044e1ffdc334 | 9901 |
| src/memory/strategy.ts | 184e971eea88d515329f43f6a450fc812815b938 | 3119 |

Keep target, test and dependency ledgers separate. Fully read each selected test;
record exact blob, total lines and contiguous read spans. Partial/history reads
never belong in fullyReadTests. Prior accepted R1/R2/R3 evidence may be reused
as REUSED_FULL_READ only with old/new blob match, cited artifact and full-read
provenance. Changed caller blobs invalidate caller conclusions independently.

Preliminary command: `git -C .private_reference/source_mirrors/yc-software__qm grep -l src/memory HEAD -- test`.
Its 36 paths are a discovery seed, not a complete direct-import/test count.
Search imports, exported symbols, aliases, constructors, method surfaces,
factory wiring, strategy hooks and failure paths across tracked test locations,
including plugin/package tests where applicable. Record query, regex mode,
result paths, selected/excluded paths and evidence-backed reasons. Fixture-only
requires alias-aware call-site inspection; a single zero-hit grep is insufficient.
Reconcile candidate = selected + justified excluded, using unique path sets.

Trace necessary callers in core, resolution, tools, harness, wiring, API and stores.
Mandatory current-pin dependency reads: memory-read path in src/tools/primitives.ts,
its src/harness/agent-tools.ts caller and src/util/async.ts withAbort.
Inspect test/read-cancellation.test.ts and test/util-async.test.ts assertions.
Distinguish stopping an await from stopping the backend operation.
Record dependency spans/blobs; all other regions remain INCOMPLETE.
No upstream source, tests, built-in reproduction probes, skills or packages execute.

## Required Hypothesis Rechecks

Questions, not accepted findings:

1. H1: Identity and access boundaries across org, scope, agent, conversation and
   personal/shared memory; actual authorization callers and isolation tests.
2. H2: Local versus PostgreSQL persistence, write ordering, concurrency, deletion,
   reset and failure propagation; distinguish raw SQL from API-level proof.
3. H3: Agent-only, per-turn, consolidation and scratch-promote strategies: capture,
   promotion, truncation, timing, replay and information-loss paths.
4. H4: Provider config/factory/router and MCP adapter: selection precedence,
   invalid config, unreachable backend, fallback, timeout and partial results.
5. H5: Memorable capture/inject/relay lifecycle: access controls, asynchronous
   completion, retries, cleanup and what reaches production prompts/turns.
6. H6: Consumer composition, cancellation and error masking. Inspect new withAbort
   memory-read behavior; distinguish wait cancellation from backend cancellation.
   Check stale/lost/cross-scope memory and missing test oracles.

Use differentiated practicalBenefit statements and label SOURCE_TRACE,
TEST_ASSERTION_READ or INFERRED_FROM_SOURCE. No executed upstream proof.

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

1. `docs/audits/CVF_QM_RUNTIME_VALUE_R4_2026-09-14.json`
2. `docs/reviews/CVF_QM_RUNTIME_VALUE_R4_WORKER_RETURN_2026-09-14.md`

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
2. Generate and reconcile the immutable memory-tree blob manifest.
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

Required return sections and fields: Purpose; Scope / Methodology; Findings / Position; Risk / Corrective Action; Claim Boundary; Agent Operation Trace Block; Delta Execution Claim Boundary Control Block; Public Export Disposition; executionBaseHead; git status --short.
Conditional sections remain explicit: External Knowledge Intake Routing; Rescan Intelligence Hardening; Corpus Completeness And Report Integrity; Finding-To-Governance Learning Disposition; Epistemic Process Block; Machine Closure Package. Use N/A with reason when a conditional obligation does not apply; do not remove eligibility markers.


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
| Intake summary | Operator request to continue the active three-repository program by dispatching the internal worker on QM runtime-value recovery |
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
| baseHeadFor(phase) | dispatchBaseHead=fd231762b9cae0bc425e5fa61ac5fd9799ff5bff; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
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
| completionReviewPath | `docs/reviews/CVF_QM_RUNTIME_VALUE_R4_COMPLETION_2026-09-14.md` |
| reviewerOwnedClosurePaths | exact worker outputs, completion review, and separately authorized continuity paths |
| closureOwner | Local reviewer/closer |
| workerCommitPermission | FORBIDDEN |

Local reviewer will sample high-value and adverse cases, verify manifest/count
reconciliation, test at least one owner-match and one novelty/defer conclusion,
confirm pin and mutation boundaries, and run applicable M5/M10/safety/M20 gates.
Local will not adopt worker self-assessment as closure evidence.

An accepted return may close only `QM-RUNTIME-VALUE-R4`. QM remains
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
parentAssignmentId: QM-RUNTIME-VALUE-R4
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
  "problemKey": "QM-RUNTIME-VALUE-R4",
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

- `python -m json.tool docs/audits/CVF_QM_RUNTIME_VALUE_R4_2026-09-14.json`
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
| Upstream or source-mirror disposition | read-only exact pin `361a6c0095dcd3d156aca91353f3ffba0bb8b69b`; no fetch or mutation |
| Enumeration or manifest plan | exact-pin `git ls-tree` for the memory source tree plus a separate linked-test ledger |
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

The memory-tree manifest is exhaustive within scope. Required blind-spot checks
cover non-test consumers, integration links, adverse/failure paths, provider
differences, lifecycle/cleanup, test oracles, and prior residual hypotheses.
Uninspected QM directories remain explicit and cannot inherit this lane's
disposition. UNKNOWN is never converted to no value.

## Corpus Completeness And Report Integrity

- Corpus task class: bounded pinned-source semantic audit.
- Corpus root: the QM memory tree at the required commit.
- Snapshot time: worker captures UTC start/end at the immutable pin.
- Enumeration command: filesystem-backed `rg --files --hidden --no-ignore <mirror>/src/memory`, reconciled to `git ls-tree -r --full-tree <pin> -- src/memory` for immutable blob identity.
- Manifest artifact or inline manifest: worker-owned JSON audit.
- Manifest hash: worker computes from normalized path/blob rows.
- Processing ledger artifact or inline ledger: worker-owned JSON audit.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.
- Reconciliation: dispatch state `manifest=19; ledger_terminal=0; exclusions=0; unresolved=19`; worker must reach `manifest=19; ledger_terminal=19; exclusions=0; unresolved=0` and reconcile all depth buckets.
- Declared exclusions: all QM paths outside the memory tree, except directly linked tests in their separate ledger.
- Unresolved files: 19 at dispatch; worker records each individually until unresolved=0; none may disappear from counts.
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
| scaffoldHelperCommand | NOT_RUN_WITH_REASON: build_dispatch_packet_scaffold.py; reused accepted R3 packet structure instead |
| generatedProfile | source-intake, no-commit, INITIAL |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | Replaced pin, scope, hypotheses and base; removed closure evidence; added exact memory manifest and cancellation delta |
| checkerReadAheadConfirmation | Current dispatch-quality, closeability, intake/freshness constants and role standards read |
| docOnlyNewFields | 19 memory targets and six questions |
| claimBoundary | Dispatch structure only; no accepted source value |

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
| Session or invocation | `QM-RUNTIME-VALUE-R4` |
| Invocation ID | worker must capture its local invocation/session identifier or `UNAVAILABLE_WITH_REASON` |
| Working directory | repository root |
| Command or tool surface | static Git and filesystem reads; worker-return fast gate |
| Target paths | paired packet and Local-only exact continuity manifest above; worker later owns exactly two evidence outputs |
| Allowed scope source | operator instruction to continue until all three repos are handled; paired baseline |
| Before status evidence | clean worktree at `fd231762b9cae0bc425e5fa61ac5fd9799ff5bff` before Local authoring; worker recaptures at start |
| After status evidence | Local authoring changes paired dispatch docs; worker later reports exact owned delta |
| Diff evidence | `git status --short --untracked-files=all`; worker records output hashes |
| Expected manifest | .private_reference/source_mirrors/INDEX.md; docs/work_orders/CVF_AGENT_WORK_ORDER_QM_RUNTIME_VALUE_R4_2026-09-14.md; docs/baselines/CVF_GC018_QM_RUNTIME_VALUE_R4_2026-09-14.md; AGENT_HANDOFF_V60_2026-09-08.md; CVF_SESSION_MEMORY.md; CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json; CVF_SESSION/state/entries/nextAllowedMove.json; CVF_SESSION/ACTIVE_SESSION_STATE.json; CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json; worker phase separately limited to the two outputs |
| Actual changed set | .private_reference/source_mirrors/INDEX.md; docs/work_orders/CVF_AGENT_WORK_ORDER_QM_RUNTIME_VALUE_R4_2026-09-14.md; docs/baselines/CVF_GC018_QM_RUNTIME_VALUE_R4_2026-09-14.md; AGENT_HANDOFF_V60_2026-09-08.md; CVF_SESSION_MEMORY.md; CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json; CVF_SESSION/state/entries/nextAllowedMove.json; CVF_SESSION/ACTIVE_SESSION_STATE.json; CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json |
| Manifest delta | worker must record `MATCH` or list exact mismatch and stop |
| Approval boundary | worker may execute this static audit after packet commit |
| Claim boundary | no implementation, source execution, or program exit |

## Delta Claim Boundary

This packet adds dispatch authority and an evidence contract. It does not add
QM behavior to CVF and does not prove any candidate valuable or already owned.

## Claim Boundary

Authorized result: a bounded, reviewable source-evidence packet for the QM memory tree. Unauthorized claims include complete QM absorption, complete
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
R1/R2 returns may be reused as shape references; R3 evidence reuse requires the exact-blob and full-read checks specified above.
Required literal sections include Target / Source, Corpus Completeness And
Report Integrity, Knowledge System Reconciliation, Mandatory Blind-Spot Control
Block, External Repository Absorption Entry Control, External/Local Coordination
Binding, Overlap And Novelty Classification, Return-Time Closeability Recheck,
Semantic Convergence Outcome and generation-0 convergence self-proof.
Before return additionally run the three bounded checks below, because the
fast gate alone did not expose these R1 pre-commit requirements:

- `python governance/compat/check_absorption_blindspot_control_presence.py --base fd231762b9cae0bc425e5fa61ac5fd9799ff5bff --head HEAD --enforce`
- `python governance/compat/check_corpus_completeness_report_integrity.py --base fd231762b9cae0bc425e5fa61ac5fd9799ff5bff --head HEAD --enforce`
- `python governance/compat/check_corpus_to_knowledge_map_reconciliation.py --base fd231762b9cae0bc425e5fa61ac5fd9799ff5bff --head HEAD --enforce`

These are additive checks, not a substitute for the required fast gate. On
outside-authority failures, return BLOCKED_WITH_REASON; never edit checkers or
protected state. Tool-owned ignored gate receipts are allowed side effects;
no additional authored script/output file is authorized.

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: bounded new QM source-evidence lane; no legacy
foundation owner/workflow-chain migration or package admission.

## Mixed Protected-Path Atomicity Authorization

Disposition: AUTHORIZED_EXACT_MANIFEST

Atomicity reason: publish the R4 dispatch authority and its currentAuthority
fingerprints/next-move together; worker owns none of the continuity paths.
A dedicated post-material continuity commit records the known dispatch SHA.
Rollback boundary: revert the exact R4 dispatch projection together; preserve
accepted R1/R2/R3 closures and the open three-repository program.
Exact changed manifest:

- `.private_reference/source_mirrors/INDEX.md`

- `docs/work_orders/CVF_AGENT_WORK_ORDER_QM_RUNTIME_VALUE_R4_2026-09-14.md`
- `docs/baselines/CVF_GC018_QM_RUNTIME_VALUE_R4_2026-09-14.md`
- `AGENT_HANDOFF_V60_2026-09-08.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`

## Core Guard Self-Protection Authorization

Operator authorization: operator requested the next worker assignment after
Local closed R3. Standing Local orchestrator mandate owns same-program dispatch
and its exact authority/continuity projection, with no new source implementation.
Authorized scope: current R4 baseline/work-order hashes, handoff and next move.
Protected paths:

- `AGENT_HANDOFF_V60_2026-09-08.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`

Rollback boundary: revert R4 dispatch projection only. Do not change checkers,
hooks, provider credentials, public state, runtime code or source mirrors.
Worker edits only its two evidence outputs after committed dispatch.

## Upstream Freshness Preflight

```json
[
  {
    "schemaVersion": "cvf.upstream-freshness.v1",
    "sourceUrl": "https://github.com/yc-software/qm.git",
    "observedAt": "2026-09-14T05:19:17.351511+00:00",
    "manifestFrozenAt": "2026-09-14T05:23:49.229026+00:00",
    "defaultBranch": "refs/heads/main",
    "observedHead": "361a6c0095dcd3d156aca91353f3ffba0bb8b69b",
    "selectedPin": "361a6c0095dcd3d156aca91353f3ffba0bb8b69b",
    "previousPin": "59cf6554faadcd06494782190c3ecae1829dd381",
    "selectionReason": "",
    "deltaSummary": "One new commit; 21 changed paths: 15 web-ui paths, 3 src paths, 3 test paths. Memory target tree and root LICENSE unchanged. primitives and agent-tools pass/check AbortSignal; async adds withAbort. Changed memory-read cancellation consumer is mandatory R4 dependency evidence. Other changes inventoried, not semantically accepted. Prior R1-R3 conclusions remain bound to their original pins.",
    "lsRemoteOutput": "ref: refs/heads/main\tHEAD\n361a6c0095dcd3d156aca91353f3ffba0bb8b69b\tHEAD\n"
  }
]
```

Local ran git ls-remote --symref, fetched the observed commit with hooks disabled,
read the src delta, then checked out the selected detached pin. No source execution.
MIT LICENSE blob: 1bb48c345739f58481c3770d4fafdf702d1523e0.
Worker cannot fetch/repin. Offline receipt validation is separate from the live
ls-remote observation recorded above.

## R2 Review Lessons Applied

Differentiate practical benefit for positive, adverse and deferred findings. Do not classify every non-adopted record as adverse/N/A. Record exact owner-search commands; bound negative claims to searched scope. Test names do not prove assertions; raw database writes are distinct from API concurrency tests. Reconcile dependent fields, hypotheses, counts and Markdown in one sweep before return.

## External Absorption Core

| Field | Value |
|---|---|
| Standard | docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md |
| Input root or repository | .private_reference/source_mirrors/yc-software__qm at the selected pin above; 19 targets only |
| Enumeration command | git ls-tree -r HEAD -- src/memory; reconcile with rg --files --hidden --no-ignore |
| Manifest artifact or inline manifest | Inline exact target table and digest above |
| Processing ledger artifact or inline ledger | docs/audits/CVF_QM_RUNTIME_VALUE_R4_2026-09-14.json; planned worker evidence; pending |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | docs/audits/CVF_QM_RUNTIME_VALUE_R4_2026-09-14.json cvfOwnerSearches; no CVF implementation admitted |
| Unresolved items | 19 target rows pending worker evidence |
| Absorption maturity | SOURCE_RECONCILED |
| Named runtime consumer | N/A_NO_RUNTIME_VALUE_WITH_REASON: no CVF runtime candidate admitted |
| Integration evidence | N/A_NO_RUNTIME_VALUE_WITH_REASON: static evidence closure only |
| Use proof | N/A_NO_RUNTIME_VALUE_WITH_REASON: no runtime proof authorized |
| Operator checkpoint | Source audit authorized; runtime implementation and proof require a separate work order |
| Absorption completion status | ABSORPTION_NOT_COMPLETE |
| Completion claim boundary | SOURCE_RECONCILED describes the frozen inventory only; no completed reading, value acceptance, or runtime integration is claimed |

## External Absorption Value Conversion Matrix

These are dispatch routing decisions, not accepted source-value findings. The worker must replace pending assessments with evidence in its return; no candidate is admitted here.

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| R4 doctrine opportunity | Not assessed; no doctrine adaptation authorized | DOCTRINE_ADAPTED | No doctrine change selected | Report evidence and proposed disposition for reviewer | No doctrine or runtime edits |
| R4 package opportunity | Not assessed; no package candidate admitted | PACKAGE_CANDIDATE | No owner selected by closure | Separate work order required | No package creation |
| R4 runtime opportunity | R4 mechanisms not yet assessed | RUNTIME_CANDIDATE | No owner selected by closure | Separate work order required | No runtime implementation or execution |
| R4 checker opportunity | No checker candidate admitted | CHECKER_CANDIDATE | No owner selected by closure | Separate testable gap required | No checker implementation |
| Upstream code copying | Direct import is outside this audit authorization | REJECT_DIRECT_IMPORT | No import destination | Preserve source citations only | No upstream code copied into CVF runtime |
| R4 no-value outcome | Not concluded; requires bounded comparative evidence | NO_PACKAGE_OR_RUNTIME_VALUE | No target selected | Worker substantiates any no-value outcome | No repository-wide rejection inferred |

## Local Reviewer Closure Receipt

Accepted bounded with the explicit partial supplementary-test exception recorded in docs/reviews/CVF_QM_RUNTIME_VALUE_R4_COMPLETION_2026-09-14.md. No runtime or three-repo closure.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | docs/work_orders/CVF_AGENT_WORK_ORDER_QM_RUNTIME_VALUE_R4_2026-09-14.md | CLOSED_PASS_BOUNDED; historical HOLD preserved in Git; released at 7271f4f10 | PASS |
| Completion or reviewer artifact | docs/reviews/CVF_QM_RUNTIME_VALUE_R4_COMPLETION_2026-09-14.md | bounded evidence and explicit scope exception accepted by Local | PASS |
| Roadmap state | N/A | standalone work order; no dedicated roadmap transition | N/A with reason: parent program remains open |
| Registry JSON | CVF_SESSION/state/entries/activeExternalAbsorptionProgram.json | all three sourceStates INCOMPLETE, retained unchanged | PASS |
| Registry Markdown | docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md | existing registry retained unchanged; bounded evidence stored in paired audit; no new package or runtime admission | PASS |
| External evidence digest | docs/audits/CVF_QM_RUNTIME_VALUE_R4_2026-09-14.json | sha256:ad6d8c7e4c7f58428035104f55aead5bad169dd4e34b24fa0410e37e5b034d7b | PASS |
| System loop interlock | N/A | no runtime or loop transition | N/A with reason: static evidence only |
| Session continuity | CVF_SESSION/state/entries/nextAllowedMove.json | retain QM next; material SHA recorded after material commit | N/A with reason: dedicated post-material synchronization |


## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
| --- | --- | --- | --- |
| Audit identity | accepted current bytes | ad6d8c7e4c7f58428035104f55aead5bad169dd4e34b24fa0410e37e5b034d7b | PASS |
| Test ledger | exact identities and honest spans | 38 full, 1 partial, 2 exclusions = 41; all 39 identities match | PASS |
| Scope decision | disclose exception | one supplementary partial test accepted with unknown remainder | PASS |
| Program | remain open | all three source states INCOMPLETE | PASS |


## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | Packet authority and bounded evidence requirements only |
| claimDisposition | CLAIM_REJECTED: no live execution-control claim from this packet |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT |
| actionEvidence | CLAIM_REJECTED_NO_ACTION |
| invocationBoundary | Explicit task scope and named role ownership |
| interceptionBoundary | No interception proved by a work order |
| claimLanguage | Source evidence or synthetic proof as expressly scoped |
| forbiddenExpansion | Universal enforcement, provider/live, CLI activation and public deployment |
