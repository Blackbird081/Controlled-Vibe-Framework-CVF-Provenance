# CVF Agent Work Order - Continuous Projection T4 Bounded Pilot And Closure

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: CVF-CONTINUOUS-PROJECTION-T4

dispatchBaseHead: `5f5c28b85`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

closureBaseHead: `REVIEWER_TO_SET`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: delegated worker through manual copy/paste

Reviewer/closer: Codex reviewer/closer

Worker return path: `docs/reviews/CVF_CONTINUOUS_PROJECTION_T4_WORKER_RETURN_2026-07-20.md`

## Dispatch Prompt Envelope

Role: delegated no-commit evidence worker for `CVF-CONTINUOUS-PROJECTION-T4`.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_CONTINUOUS_PROJECTION_T4_BOUNDED_PILOT_AND_CLOSURE_2026-07-20.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: capture current committed HEAD before any output and
require it to match the operator's dispatch note.

Current-time notes: artifact date is 2026-07-20; manual copy/paste is the only
authorized worker handoff.

Do-not-misread notes: no agent CLI/MCP, provider/API/account subscription,
browser, network, apply, public-sync mutation, retry, commit, push, or deploy.

Required first actions: read session front doors, guard orientation, literal
gotchas, paired baseline, this order, T3 closure, all three scripts/tests, and
policy; then capture HEAD, status, and remotes before creating output.

Return contract: produce exactly four Allowed outputs after one successful
scan, leave all unstaged and uncommitted, and return
`COMPLETE_PENDING_REVIEW`; on a stop condition return `BLOCKED_WITH_REASON`.

Revision: R3 reviewer repair after accepted outer-harness-timeout blocked return

Prior blocked executionBaseHead: `7dbdf3488`

Prior real-root scan invocation count: `1` in R2; consumed and not retried

R3 real-root scan invocation ceiling: `1` fresh invocation

R1 fixture evidence reused: `53/53`; `91/91`; `144/144`

## 1. Mission

Execute the final bounded Continuous Projection pilot without mutation: reuse
the accepted R1 T1/T2/T3 disposable-fixture evidence, perform exactly one T1 scan
over the real three-root state, generate one T2 review draft, measure the
receipt's review value and suspected errors, and return evidence for Codex
reviewer-owned audience assessment and closure.

## Purpose

Purpose is the bounded T4 mission above; this structural heading does not
expand scope.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-CONTINUOUS-PROJECTION-T4 --title "Continuous Projection T4 Bounded Pilot And Closure" --date 2026-07-20 --base 5f5c28b85 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "T3 closure commit e21199dfa REVIEWER_ACCEPTED_WITH_REPAIRS" --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker-return profile |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | Replaced generic fields with source-verified roots, one-scan sequencing, exact manifest, measurements, CLI/MCP prohibition, and reviewer ownership. |
| checkerReadAheadConfirmation | dispatch, scaffold, handoff, ADIF, structural, public-disposition, and worker-return checkers named below |
| docOnlyNewFields | four measurement fields listed under New Doc-Only Fields |
| claimBoundary | dispatch contract only; no scan result, provider action, mutation, or closure claim |

## 2. Authority Chain

- Operator instruction: 2026-07-20, finish T3/T4 but prohibit CLI/MCP until
  separately requested.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Active handoff: `AGENT_HANDOFF_V49_2026-07-20.md`.
- Roadmap: `docs/roadmaps/CVF_CONTINUOUS_PROJECTION_DRIFT_DETECTION_AND_REVIEW_PACKET_AUTOMATION_ROADMAP_2026-07-19.md`, T4.
- Dependency release: T3 completion review and commit `e21199dfa`.
- GC-018: `docs/baselines/CVF_GC018_CONTINUOUS_PROJECTION_T4_BOUNDED_PILOT_AND_CLOSURE_2026-07-20.md`.

Authority boundary: no source in this chain authorizes mutation, provider use,
agent CLI/MCP invocation, reviewer impersonation, or worker commit.

## 3. Agent Roles

- Dispatcher: Codex dispatch author.
- Worker: delegated implementation/evidence worker via operator copy/paste.
- Reviewer/closer: Codex reviewer/closer.
- Operator owns any later provider, CLI/MCP, public, push, or deployment release.

## 4. Scope

Allowed actions:

- local read-only source inspection;
- local Git status, remote, hash, and diff commands;
- the three existing disposable-fixture proof suites;
- exactly one supervised local-process invocation of the accepted T1 receipt
  script, launched once and observed through short manual polls of the same PID;
- one T2 draft invocation over the successful real receipt;
- writing exactly four Allowed outputs after the real scan completes;
- local Python governance gates.

Forbidden actions:

- Claude CLI, Codex CLI, any agent CLI, MCP tool/server, provider/API call,
  API key, account subscription, network request, browser, or fallback;
- a second real-root scan, including retry, relaunch, replacement PID, or a
  second process after timeout or failure;
- worker-authored `reviewerOwned=true` audience evidence;
- real-root T3 gate execution by the worker;
- apply/copy into public-sync, semantic edit, deletion, cleanup, commit, push,
  deploy, production action, scheduled job, or unattended loop; the R3 local
  process must remain under continuous same-worker supervision;
- modifying scripts, policy, tests, source, session state, roadmap, baseline,
  work order, public-sync, or cvf-web.

Risk ceiling: R3 read-only bounded scan with one supervised PID and fail-closed
stop. R3 is the final bounded recovery attempt; a further execution-envelope
failure returns to the reviewer without self-redispatch.

## Scope / Target / Owner Boundary

Target is one fixture-plus-real-root evidence pilot. The worker owns only the
four Allowed outputs. The reviewer owns audience evidence, real T3 gate run,
semantic disposition, commit, and closure.

## Write Ownership

The worker may write the four Allowed paths only, and only after the real scan
finishes. Temporary scan output stays outside all target roots. Staging and
commit are forbidden.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`, maxResults=`100`

Returned defects: ADIF-0001; ADIF-0002; ADIF-0006; ADIF-0007; ADIF-0014; ADIF-0015; ADIF-0016; ADIF-0017; ADIF-0020; ADIF-0021; ADIF-0024; ADIF-0028; ADIF-0029; ADIF-0031; ADIF-0033; ADIF-0039; ADIF-0043; ADIF-0044

## 5. Required First Reads

- paired T4 GC-018 baseline;
- T3 completion review;
- R2 blocked pilot ledger and worker return;
- `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0043.md`;
- `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0044.md`;
- T1, T2, and T3 scripts plus their three focused test scripts;
- `scripts/cvf_projection_policy.json`;
- T1 synopsis and timeout branch for the local timeout diagnostic shape;
- governed artifact literal-format gotchas and guard orientation index.

## 6. Pre-Flight Checks

Before any output file is created:

```powershell
git rev-parse --short HEAD
git status --porcelain
git remote get-url origin
git -C ..\Controlled-Vibe-Framework-CVF-public-sync status --porcelain
git -C ..\Controlled-Vibe-Framework-CVF-public-sync remote get-url origin
Test-Path EXTENSIONS\CVF_v1.6_AGENT_PLATFORM\cvf-web
Test-Path scripts\cvf_projection_policy.json
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <dispatchHead> --head HEAD
```

Expected: exact dispatch HEAD, both Git roots clean, provenance/public remotes
match policy, required roots exist, and pre-implementation passes. Otherwise
return `BLOCKED_WITH_REASON` without scanning.

## 6A. Source-Fidelity Pass

### Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| T4 dependency is released | `docs/reviews/CVF_CONTINUOUS_PROJECTION_T3_COMPLETION_REVIEW_2026-07-20.md` | Decision and Next Allowed Move | T4 packet authoring | T3 reviewer closure | ACCEPT |
| T1 accepts four roots/policy inputs plus optional receipt path and timeout | `scripts/get_cvf_projection_drift_receipt.ps1` | parameter block and synopsis | ProvenanceRoot; PublicSyncRoot; CvfWebRoot; PolicyPath; ReceiptOutputPath; ScanTimeoutSeconds | script parameter interface | ACCEPT |
| T1 emits receipt JSON to stdout when ReceiptOutputPath is omitted | `scripts/get_cvf_projection_drift_receipt.ps1` | ReceiptOutputPath parameter documentation and receipt output branch | ReceiptOutputPath | script output interface | ACCEPT |
| T1 requires a supplied receipt path to be contained under process CWD and outside every read-only root | `scripts/get_cvf_projection_drift_receipt.ps1` | lines 612-619 containment branch | Assert-PathContainment; Test-PathContained | receipt output containment | ACCEPT |
| T1 timeout maximum is 3600 seconds | `scripts/get_cvf_projection_drift_receipt.ps1` | ScanTimeoutSeconds parameter and timeout branch | ScanTimeoutSeconds | T1 child-process wrapper | ACCEPT |
| T1 success schema is 1.0.0 with 16 rows and no-write confirmation | `scripts/get_cvf_projection_drift_receipt.ps1` | success receipt construction | schemaVersion; rows; noTargetWriteConfirmation | T1 receipt schema | ACCEPT |
| T2 consumes ReceiptPath and emits stdout-only draft | `scripts/get_cvf_projection_review_packet.ps1` | synopsis and parameter block | ReceiptPath | T2 drafter interface | ACCEPT |
| T2 draft remains review-required and non-authorizing | `scripts/get_cvf_projection_review_packet.ps1` | output construction | draftStatus; authorizesDecision | T2 draft schema | ACCEPT |
| T3 requires reviewer-owned evidence | `scripts/get_cvf_projection_audience_gate.ps1` | synopsis and validation contract | AudienceEvidencePath; reviewerOwned | T3 gate interface | ACCEPT |
| real public-sync root is the sibling clone | `docs/reviews/CVF_CONTINUOUS_PROJECTION_T0_THREE_ROOT_DRIFT_CONTRACT_LEDGER_2026-07-20.md` | Root Identity table | PublicSyncRoot | T0 accepted root contract | ACCEPT |
| policy declares exact provenance/public remotes | `scripts/cvf_projection_policy.json` | expectedRemotes | provenanceRemote; publicRemote | projection policy | ACCEPT |

### New Doc-Only Fields

| Field | Owner | Purpose |
|---|---|---|
| suspectedFalsePositiveCount | T4 ledger | worker suspicion only; reviewer decides |
| suspectedMissedDriftCount | T4 ledger | bounded manual cross-check count |
| preparationMinutes | T4 ledger | local worker effort telemetry |
| packetUsefulnessDisposition | T4 ledger | provisional evidence utility assessment |

### Current Runtime Freshness Verification

The dispatch author re-read all three current script interfaces, the policy,
and T3 closure at HEAD `5f5c28b85`. No proposed runtime field is represented
as existing source. No agent CLI/MCP adapter is present or authorized here.

## 6B. Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification | Status |
|---|---|---|---|---|
| disposable three-root fixture | Execution Phase A | ledger fixture totals | direct suite output | PASS |
| one reviewer-authorized real-root scan | Execution Phase B | real receipt | receipt schema and root evidence | PASS |
| false positives | Measurement | row-level ledger | reviewer confirmation | PASS |
| missed drift | Measurement | 16-row cross-check | reviewer confirmation | PASS |
| reviewer effort | Measurement | preparation and later review minutes | completion review | PASS |
| packet usefulness | Measurement | provisional usefulness rows | reviewer decision | PASS |
| no automatic semantic mutation | Forbidden scope | status/diff/no-write evidence | before/after root checks | PASS |

## 6C. Worker Autonomy / No-Question Rule

Proceed autonomously only inside Allowed scope. Repair formatting defects in
the ledger/return and rerun local gates. Stop for dirty roots, wrong HEAD or
remote, failed fixture suite, timeout, real scan error, malformed receipt,
forbidden-path need, or any request for CLI/MCP/provider/browser/network use.
Do not retry the real scan and do not ask the operator to waive the stop.

## Required Artifact Manifest

Allowed paths, exactly:

| Required artifact | Path | Success-run disposition | Blocked-run disposition |
|---|---|---|---|
| Real-root receipt | `docs/reviews/evidence/CVF_CONTINUOUS_PROJECTION_T4_REAL_ROOT_RECEIPT_2026-07-20.json` | REQUIRED | OMIT |
| Review draft | `docs/reviews/evidence/CVF_CONTINUOUS_PROJECTION_T4_REAL_ROOT_REVIEW_DRAFT_2026-07-20.json` | REQUIRED | OMIT |
| Pilot ledger | `docs/reviews/CVF_CONTINUOUS_PROJECTION_T4_BOUNDED_PILOT_LEDGER_2026-07-20.md` | REQUIRED | REQUIRED |
| Worker return | `docs/reviews/CVF_CONTINUOUS_PROJECTION_T4_WORKER_RETURN_2026-07-20.md` | REQUIRED | REQUIRED |

Work-Order Fulfillment Manifest: four required artifacts; every other path is
forbidden. On a blocked real scan, the two JSON success artifacts must be
absent and only the ledger plus worker return may exist.

## 8. Execution Instructions

## Execution Plan

Execute Phases A through D below in order. A failed phase blocks every later
phase. Phase B has a one-invocation ceiling and no retry.

### Phase A - Reuse R1 Disposable Fixture Pilot

Do not rerun the three fixture suites. Reuse the committed R1 blocked-return
evidence because no T1/T2/T3 script or test source changed after that run:
`53/53`, `91/91`, and `144/144`, all with zero failures. Verify with
`git diff --name-only 5b929dad9..HEAD -- scripts/` that the range is empty.
Any script-path delta blocks Phase B and returns `BLOCKED_WITH_REASON`.

### Phase B - Single Supervised Real-Root Receipt Process

R2 proved that a synchronous worker tool call is not a valid execution
envelope: its outer command ceiling terminated the scan near 180 seconds,
before the script's 3600-second bound. R3 therefore launches exactly one hidden
local `powershell.exe` process and manually polls that same PID through separate
short tool calls. This is supervised local execution, not a scheduled job,
unattended loop, agent CLI/MCP call, provider call, or retry.

Before launch, create one unique disposable directory under `%TEMP%`, outside
all three target roots. Reserve four paths there: stdout, stderr, PID metadata,
and a launch sentinel. Do not supply `-ReceiptOutputPath`; redirect process
stdout and stderr to their two reserved files. Resolve the script and all four
input paths to absolute paths before launch.

Launch once with PowerShell `Start-Process -WindowStyle Hidden -PassThru`, set
the working directory to the provenance root, and pass the same T1 arguments
as R2, including `-ScanTimeoutSeconds 3600`. Persist the returned PID, process
start time, absolute command target, stdout path, stderr path, and
`scanInvocationCount=1` to the metadata path, then create the launch sentinel.
The launch call must return immediately; it must not synchronously wait for the
scan.

Poll only the persisted PID. Each poll must be a separate bounded local command
that returns within 60 seconds and records elapsed time plus one of `RUNNING` or
`EXITED`. Do not launch another process if metadata or the sentinel already
exists. Do not use a scheduled task, job, daemon, watcher, autonomous retry, or
sleep longer than 45 seconds. The worker must remain present and supervise the
same process until it exits or until the worker can no longer continue safely.

When the process exits, read stdout and stderr once. A valid schema `1.0.0`
receipt with 16 rows and empty errors is the only success condition. Because a
detached Windows process exit code is not durable across separate worker shell
calls, the exit-code diagnostic may be `NOT_AVAILABLE_WITH_REASON` if the
process has already left the process table; receipt structure and errors remain
authoritative. Empty, malformed, or error-bearing stdout blocks Phase C.

If supervision cannot continue, enumerate descendants of the persisted PID,
stop only that exact process tree with native PowerShell process controls,
verify no matching process remains, and return `BLOCKED_WITH_REASON`. Never
relaunch. In every failure case classify stage, class, retryability, user
action, elapsed time, exit-code availability, diagnostic code, and safe
message. R3 is the final bounded recovery attempt; do not propose or execute R4.

### Phase C - Persist And Draft

Only after success, join the captured stdout lines with the platform newline
and write UTF-8 without BOM to the first Allowed JSON path. Run T2 once against that path and persist stdout exactly to the second
Allowed JSON path. Validate JSON parsing, identity linkage, 16 rows,
reconciliation, empty errors, and all no-authority fields.

### Phase D - Measurement Ledger

For each of 16 receipt rows record disposition, evidence locator, suspected
false-positive status, suspected missed-drift status, and reviewer question.
Record fixture totals, scan elapsed time, preparation minutes, root statuses,
receipt/draft hashes, decisions enabled, decisions still blocked, and explicit
absence of worker-owned audience judgment.

## 9. Evidence And Negative Cases

Required proof includes exact start/end HEAD; both roots' start/pre-scan/
post-scan/final status; exact remotes; fixture totals; scan count one; elapsed
time; receipt and draft hashes; 16-row reconciliation; no-write literal;
providerCallCount=0; agentCliCallCount=0; mcpCallCount=0; browserCallCount=0;
and exact four-path final manifest.

Fail closure for missing fields, string-coerced booleans/numbers, schema or
identity mismatch, unknown disposition, nonempty errors, target write, dirty
root, second scan, worker audience evidence, or any forbidden action.

## Evidence Requirements

Evidence must use exact command, result, root, hash, receipt, and manifest
facts from section 9. Narrative confidence is not a substitute.

## Acceptance Criteria

- Committed R1 fixture totals are reused only if `5b929dad9..HEAD` contains no script-path delta.
- Real-root T1 launch count equals one, with one persisted PID and no relaunch.
- Every poll targets that PID and returns within 60 seconds; the scan remains
  supervised by the same worker until success or fail-closed teardown.
- Receipt and draft satisfy accepted schemas and identities.
- All 16 rows receive a bounded worker cross-check without semantic verdict.
- Provider, agent CLI, MCP, browser, network, mutation, stage, and commit
  counters remain zero.
- Final pending manifest equals the four Allowed paths.

## Verification Commands

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/test_cvf_projection_drift_receipt.ps1
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/test_cvf_projection_review_packet.ps1
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/test_cvf_projection_audience_gate.ps1
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/check_governed_file_size.py --enforce
git status --short
git diff --name-status
```

## Review Gate

Codex reviewer reads all outputs and source inputs, recomputes schema,
identity, root, negative-case, measurement, range, and commit-plan evidence in
one audit, authors reviewer-owned audience evidence, and runs the real T3 gate.

## Return Conditions

Return `COMPLETE_PENDING_REVIEW` only for a successful one-scan run with four
valid outputs and passing worker-return fast gate. Otherwise return
`BLOCKED_WITH_REASON` with no scan retry.

## Return-To-Orchestrator Conditions

Return immediately for wrong HEAD/remote, dirty root, failed fixture suite,
timeout, nonzero real scan, malformed receipt/draft, forbidden-path need, or
any need for CLI/MCP/provider/browser/network/mutation authority. Do not retry.

## 10. Worker Return Contract

Return status is `COMPLETE_PENDING_REVIEW` only after all four outputs exist
and local worker-return fast gate passes. Otherwise return
`BLOCKED_WITH_REASON`. Report actual pending status; do not claim a clean
worktree. Include Checker Source Read-Ahead, Agent Operation Trace, Delta
Execution Claim Boundary, Public Export Disposition, External Knowledge Intake
Routing, Rescan Intelligence Hardening, Corpus Completeness And Report
Integrity, Finding-To-Governance Learning Disposition, Epistemic Process,
Changed Files, Command Evidence, and No-Commit Statement.

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intake summary | final read-only fixture and real-root evidence pilot |
| scope classification | local bounded execution evidence |
| risk sensitivity | R3; one fresh supervised PID; fail closed; zero external services |
| escalation condition | any stop condition or need outside Allowed scope |
| selected role route | no-commit worker -> independent reviewer/closer |
| mode | `MULTI_AGENT_MULTI_ROLE` |
| execution-lane authority | manual operator copy/paste only |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | local T1/T2/T3 scripts | read-only local execution; no semantic authority | receipt, draft, ledger | repository scripts only | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | none released | operator prohibition; no invocation or adapter authority | zero-call counters and action log | separate future operator-approved work order required | `DEFERRED_WITH_REASON` |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | dispatcher -> no-commit worker -> reviewer/closer -> session-sync steward |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | dispatchBaseHead=`5f5c28b85`; executionBaseHead=`WORKER_MUST_CAPTURE_AT_START`; closureBaseHead=`REVIEWER_TO_SET` |
| changedSetScope(phase) | two dispatch paths; exactly four worker paths; reviewer-owned closure paths; continuity separately |
| traceScope(phase, actor) | each actor reports only its commands and evidence |
| commitOwner(phase) | worker=`WORKER_MUST_NOT_COMMIT`; reviewer owns material; session steward owns continuity |
| crossBatchIsolation | clean start required; unrelated changes block execution |
| nextMoveSurfaces | reviewer/session steward updates roadmap and continuity from committed T4 completion evidence |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_CONTINUOUS_PROJECTION_T4_COMPLETION_REVIEW_2026-07-20.md` |
| reviewerOwnedClosurePaths | audience evidence JSON; real-root T3 gate JSON; completion review; paired baseline; this work order; roadmap |
| closureOwner | Codex reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_CONTINUOUS_PROJECTION_T4_WORKER_RETURN_2026-07-20.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The worker return must include Purpose, Scope / Methodology, Findings / Position,
Risk / Corrective Action, Claim Boundary, Agent Operation Trace Block,
Delta Execution Claim Boundary Control Block, Public Export Disposition,
executionBaseHead, and git status --short.

Conditional sections must include External Knowledge Intake Routing,
Rescan Intelligence Hardening, Corpus Completeness And Report Integrity,
Finding-To-Governance Learning Disposition, Epistemic Process Block, and
Machine Closure Package, or an explicit N/A with reason / NOT_APPLICABLE_WITH_REASON.

Also include Changed Files, Command Evidence, and No-Commit Statement.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex reviewer and redispatch author |
| Provider or surface | local private provenance workspace |
| Session or invocation | T4 R3 outer-harness-timeout review and packet repair, 2026-07-21 |
| Working directory | repository root |
| Command or tool surface | governed reads; apply_patch; local Python checkers and gates; Git status |
| Target paths | T4 work order, roadmap, R2 pilot ledger, R2 worker return, ADIF-0044, and ADIF entries README |
| Allowed scope source | operator instruction plus accepted T4 R2 blocked return at `7dbdf3488` |
| Before status evidence | clean worktree at HEAD `7dbdf3488` before the worker updated its two blocked-return outputs |
| After status evidence | exactly six R3 reviewer-repair and learning paths pending before commit |
| Diff evidence | `git status --short` and exact staged manifest before commit |
| Approval boundary | accept R2 blocked return, repair the execution envelope, record reusable learning, and prepare manual copy/paste R3 redispatch only |
| Claim boundary | one R2 invocation interrupted by its parent harness; no successful scan, provider, CLI/MCP, target mutation, or public claim |
| Agent type | reviewer and dispatcher |
| Invocation ID | `cvf-continuous-projection-t4-r3-redispatch-2026-07-21` |
| Expected manifest | T4 work order, roadmap, R2 pilot ledger, R2 worker return, ADIF-0044, and ADIF entries README |
| Actual changed set | same six R3 reviewer-repair and learning paths |
| Manifest delta | MATCH |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | bounded local fixture and one real-root read-only scan |
| claimDisposition | CLAIM_REJECTED: no execution-control or interception claim |
| receiptEvidence | `CLAIM_REJECTED_NO_RECEIPT`: pending worker receipt; no result claimed at dispatch |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: dispatch author ran no T4 scan or mutation |
| invocationBoundary | future manual local script invocation only |
| interceptionBoundary | no wrapper/proxy control over Claude, CLI, MCP, or provider |
| claimLanguage | dispatch-ready means packet accepted, not pilot passed |
| forbiddenExpansion | agent CLI/MCP, provider, browser, mutation, public-sync, push, deployment, production |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | NOT_APPLICABLE_WITH_REASON: no external knowledge is absorbed |
| Matching local-view guard | N/A with reason: current repository source is authority |
| Owner surface | paired T4 baseline and work order |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | manual worker routing does not promote provider output to CVF authority |

## Operator Checkpoint

The operator explicitly authorized T4 packet creation and prohibited CLI/MCP
until another direct request. The operator will manually copy/paste the
committed work order to the worker.

## Closure Checklist

- [ ] Exact execution base and clean roots verified.
- [ ] R1 fixture totals are reused only after an empty script-path delta check.
- [ ] Exactly one real-root PID is launched and no replacement PID appears.
- [ ] Short polls supervise that PID until completion or exact-tree teardown.
- [ ] Receipt and draft integrity are proven.
- [ ] Row-level metrics are recorded without semantic overclaim.
- [ ] No worker-owned audience evidence or real-root T3 run occurs.
- [ ] No CLI/MCP/provider/browser/network/mutation action occurs.
- [ ] Exactly four outputs remain unstaged and HEAD unchanged.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | DISPATCH_READY; ACCEPT; source columns; exact ADIF query; handoff fields; worker-return markers; Allowed manifest |
| gateRunPurpose | confirm T4 packet compliance as dispatch evidence, not discover requirements |
| claimBoundary | structural checks do not prove a real-root scan or semantic quality |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance evidence only; public-sync mutation is forbidden.

## Claim Boundary

This work order authorizes one manual no-commit worker to run local fixture
proof and exactly one real-root read-only T1 scan. It does not authorize any
agent CLI/MCP call, provider/API/account use, retry, reviewer impersonation,
automatic semantic mutation, public-sync, commit, push, deploy, production,
browser, network, scheduled, or unattended action.
