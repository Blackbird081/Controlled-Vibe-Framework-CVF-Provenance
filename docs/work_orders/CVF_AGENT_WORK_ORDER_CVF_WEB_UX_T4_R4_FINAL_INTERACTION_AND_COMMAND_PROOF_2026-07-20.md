# CVF Agent Work Order - CVF Web UX T4 R4 Final Interaction And Command Proof

Memory class: governed-worker-dispatch

Status: REVIEWED_BLOCK_ACCEPTED_R5_REQUIRED

Batch ID: CVF-WEB-UX-T4-R4

Dispatch base head: `f8880597e`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: delegated browser-evidence worker

Reviewer/closer: independent reviewer/closer

Worker return path: `docs/reviews/CVF_WEB_UX_T4_R4_WORKER_RETURN_2026-07-20.md`

## Dispatch Prompt Envelope

Role: capture exactly three corrected interaction results and terminal command evidence.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_WEB_UX_T4_R4_FINAL_INTERACTION_AND_COMMAND_PROOF_2026-07-20.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: require the operator-provided final session-sync HEAD.

Current-time notes: R1-R3 accepted evidence is immutable. Start current cvf-web
on localhost:3000 and wait for Ready before capture.

Do-not-misread notes: exact target equality is mandatory. A step tab, onboarding
heading, script-created label, ACTIVE listener, PENDING check, or failing test
cannot receive PASS.

Required first actions: confirm clean worktree and exact HEAD; read `DESIGN.md`,
this packet, R3 review, target source, and worker-return checkers; run
pre-implementation; create any automation script only under the OS temporary
directory and delete it before return.

Return contract: produce exact R4 outputs, run and retain terminal checks, stop
Web, prove no listener, leave no scratch file, and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` without staging or commit.

## Purpose

Close only the non-terminal Home, Workspace, Knowledge, diagnostics, tests, and
teardown evidence left by R3. Do not repeat Preferences, accent, drawer, or the
full browser matrix.

## Authority Chain

Operator continuation -> active UX roadmap -> T4 -> R1/R2/R3 reviews -> this R4.

## Agent Roles

- Worker: three browser interactions and terminal command evidence; no commit.
- Reviewer/closer: recomputes all R4 evidence and decides final T4/roadmap closure.
- Session-sync steward: updates continuity only after reviewer decision.

## Write Ownership

Worker owns exactly the R4 matrix, R4 return, and fresh R4 evidence directory.
Automation scripts must remain outside the repository and be deleted.

## Dependency Release Evidence

| Dependency | Artifact | Material commit | Final disposition |
|---|---|---|---|
| R3 independent review | `docs/reviews/CVF_WEB_UX_T4_R3_BLOCKED_RETURN_REVIEW_2026-07-20.md` | N/A with reason: review and R4 dispatch share one material batch | `REVIEWED_BLOCK_ACCEPTED_R4_REQUIRED` |
| accepted predecessor evidence | R1-R3 evidence roots | reviewer material batch pending | immutable; reuse without recapture |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-WEB-UX-T4-R4 --title "CVF Web UX T4 R4 Final Interaction And Command Proof" --date 2026-07-20 --base f8880597e --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit Web evidence profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | added exact target equality, three-state evidence, non-live test command, post-stop proof, and temp-script boundary |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py` |
| docOnlyNewFields | `intermediateState`; `finalState`; `networkResponse`; `postStopListenerCount`; `temporaryScriptDisposition` |
| claimBoundary | dispatch provenance only; no interaction acceptance claim |

## Worker Autonomy / No-Question Rule

Repair allowed-scope checker failures directly. Return blocked for missing exact
target, unavailable browser, failing required check, listener residue,
forbidden-scope need, or source contradiction.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`web-ui-browser-audit`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "web-ui-browser-audit" --role dispatcher --lifecycle-phase pre-dispatch` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | packet supplies local fail-closed target and result controls |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | dispatch status; source verification; handoff; worker return; closure conversion |
| gateRunPurpose | confirmation and evidence after packet source verification; not first discovery |
| claimBoundary | checker PASS authorizes evidence execution only |

## Roadmap-to-Work-Order Trace Matrix

| Roadmap requirement | R4 control | Evidence required | Fail condition |
|---|---|---|---|
| primary Home action | dismiss onboarding, activate exact `Tao PRD`, bind form-specific result | screenshot plus form h1/label | generic form or onboarding anchor |
| advanced disclosure | record false-true-false | intermediate and final DOM states | only one transition |
| journey action | activate exact `Bien soan` action | exact name, response status, visible result/error | step tab or script label |
| diagnostics | classify unique classes truthfully | terminal diagnostic ledger | warning relabeled as auth |
| verification | non-live focused tests and teardown | command records with terminal output | failure, pending, or active listener |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Home outcome action uses accessible title | LITERAL_INVARIANT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/OutcomeQuickActions.tsx` | lines 100-111 | `aria-label` | `OutcomeQuickActions` | ACCEPT |
| selected Home outcome renders DynamicForm | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app` | child `(dashboard)/home/page.tsx`, lines 284-290 and 582-589 | `handleOutcomeQuickAction` | `HomePage` | ACCEPT |
| DynamicForm has a form-specific h1 | LITERAL_INVARIANT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/DynamicForm.tsx` | lines 116-165 | `localizedTemplate` | `DynamicForm` | ACCEPT |
| Workspace details uses native open state | LITERAL_INVARIANT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app` | child `(dashboard)/workspace/page.tsx`, lines 167-176 | `advanced-detail` | `WorkspacePage` | ACCEPT |
| compile action exact text is `Bien soan` | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app` | child `(dashboard)/governance/knowledge/page.tsx`, lines 47-59 and 256-258 | `compile` | `KnowledgeGovernancePage` | ACCEPT |
| unauthenticated compile produces visible error | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app` | child `(dashboard)/governance/knowledge/page.tsx`, lines 148-171 and 230 | `setError` | `KnowledgeGovernancePage` | ACCEPT |
| compile route returns 401 when unauthenticated | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/governance/knowledge/compile/route.ts` | lines 12-24 | `POST` | compile route | ACCEPT |
| provider-free suite excludes live tests | LITERAL_INVARIANT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | scripts section; `test:run` value excludes live tests | `scripts` | npm package | ACCEPT |

## New Doc-Only Fields

| Field | Purpose | Claim boundary |
|---|---|---|
| `intermediateState` | retain state after first activation | R4 DOM evidence |
| `finalState` | retain state after second activation | R4 DOM evidence |
| `networkResponse` | bind action to exact route/status | sampled local request |
| `postStopListenerCount` | prove teardown after process stop | R4 process session |
| `temporaryScriptDisposition` | prove no repo scratch residue | R4 worker environment |

## Evidence Reuse And Encoding Plan

verificationMode: REUSE_PRIOR_VERIFICATION

priorVerificationArtifact: `docs/reviews/CVF_WEB_UX_T4_R3_BLOCKED_RETURN_REVIEW_2026-07-20.md`

priorVerificationAnchor: accepted R1-R3 responsive, Preferences, accent, and drawer evidence

freshRecomputeRequired: three interactions, diagnostics, commands, predecessor
integrity, tests, Ready/stop/no-listener, exact manifest

unicodePathHandling: retain exact UTF-8 rendered Vietnamese accessible names

extractedTextAuthority: rendered text is observed evidence; current source remains authority

## Required First Reads

Read `DESIGN.md`, this packet, R3 review, target source, package scripts, and
worker-return checker sources before browser execution.

## Pre-Flight Checks

- require clean worktree and exact supplied execution base;
- verify R4 output paths do not exist;
- hash R1-R3 evidence before work;
- run pre-implementation before Web start;
- do not load provider keys or invoke live proof;
- put browser automation only under `$env:TEMP` and record its deletion.

## Execution Plan

1. Start current-source Web on localhost:3000 and retain actual Ready output.
2. Dismiss onboarding by its visible dismiss action before Home interaction.
3. Keyboard-focus the button whose accessible name equals `Tao PRD`; press
   Enter; capture the resulting DynamicForm with its form-specific h1 and at
   least one form label.
4. On `/workspace`, focus the exact advanced summary; record false, press Enter,
   record true, press Enter again, and record final false. Capture the open state.
5. On `/governance/knowledge`, fill the content textarea, select only the enabled
   button whose normalized text equals `Bien soan`, press Enter, record the exact
   compile-route response, and capture the visible artifact or exact error text.
6. Classify the React missing-key warning as a retained source warning, not auth.
7. Run focused provider-free tests with `npm run test:run --` and exact test paths;
   do not run or summarize live tests as PASS.
8. Run file-size and worker-fast, update command evidence, then rerun worker-fast
   after the final update so no field remains pending.
9. Stop the Web process; only afterward record zero listeners on port 3000.
10. Delete the temporary automation script, verify exact scope, and return with
    unchanged HEAD and nothing staged.

Text Encoding Exception: exact rendered Vietnamese UI anchors are required in
R4 evidence; all other authored control prose remains ASCII-first.

## Required Browser Evidence

Create exactly three screenshots:

- `home-tao-prd-form-result.png`;
- `workspace-advanced-open.png`;
- `knowledge-compile-terminal.png`.

Create exactly five JSON files:

- `captures.json`;
- `interaction-trace.json`;
- `diagnostics.json`;
- `commands.json`;
- `predecessor-integrity.json`.

## Interaction Evidence Contract

Home must retain exact accessible target, onboarding-dismissed state, form h1,
one form label, screenshot hash, and terminal verdict.

Workspace must retain `beforeState=false`, `intermediateState=true`, and
`finalState=false`, with the same focused summary before both Enter presses.

Knowledge must retain exact action text equality, enabled state, request URL
`/api/governance/knowledge/compile`, response status, and visible artifact or
visible `Unauthorized: please login.` error. A step-tab label, generic 401 from
another route, or `compile_attempted` is not evidence.

## Allowed Scope

- `docs/reviews/CVF_WEB_UX_T4_R4_FINAL_INTERACTION_ACCEPTANCE_MATRIX_2026-07-20.md`
- `docs/reviews/CVF_WEB_UX_T4_R4_WORKER_RETURN_2026-07-20.md`
- `docs/reviews/evidence/CVF_WEB_UX_T4_R4_LOCALHOST_2026-07-20/`

## Forbidden Scope

Every other repository path, including scratch scripts, Web source/tests,
R1-R3 evidence, roadmap, session, dependencies, lockfiles, hosted/deploy/public,
provider/live, production, and continuous-projection surfaces.

## Evidence Requirements

- exactly three screenshots and five JSON files;
- exact target and visible result evidence for all three scenarios;
- terminal diagnostic classification with no false auth mapping;
- unchanged R1-R3 predecessor hashes;
- actual Ready and post-stop zero-listener evidence;
- exact git manifest, unchanged HEAD, nothing staged, no scratch files;
- focused provider-free tests, file-size, and worker-fast PASS with no pending row.

## Verification Commands

From the cvf-web package, run:

`npm run test:run -- src/components/OutcomeQuickActions.test.tsx src/components/DynamicForm.test.tsx "src/app/(dashboard)/workspace/page.test.tsx" "src/app/(dashboard)/governance/knowledge/page.test.tsx"`

Then run file-size, worker-fast, final HEAD/status/diff/cached-diff, predecessor
hash comparison, temp-script deletion check, process stop, and port check.

Required worker-return gate command:

`python governance/compat/run_worker_return_fast_gate.py`

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | reviewed R3 evidence and current source |
| Scope classification | final evidence repair only |
| Intake role | browser-evidence worker |
| Reviewer role | independent reviewer/closer |
| Routing decision | WORKER_MUST_NOT_COMMIT |
| Public route | DEFERRED_PRIVATE_ONLY |
| canonical route mode | SINGLE_AGENT_SINGLE_ROLE |
| selected role route | R4 worker to reviewer closure conversion |
| escalation condition | missing exact target/result, failing check, or forbidden-path need |
| risk sensitivity | MEDIUM: final roadmap acceptance evidence |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | NOT_APPLICABLE_WITH_REASON: no outside artifact promoted |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | R4 evidence and independent review |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | no external authority or hosted-equivalence claim |

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

## Agent Handoff Contract Control Block

| Field | Value |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | delegated evidence worker to independent reviewer/closer |
| phase | implementation |
| baseHeadFor(phase) | dispatchBaseHead=f8880597e; executionBaseHead=OPERATOR_PROVIDED_FINAL_SESSION_SYNC_HEAD; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | exact new R4 Allowed Scope |
| traceScope(phase, actor) | process, browser, three interactions/images, diagnostics, commands, hashes, tests, gates, return |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | all predecessor evidence and source immutable |
| nextMoveSurfaces | reviewer decides final T4/roadmap closure; session steward syncs continuity |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_WEB_UX_T4_COMPLETION_2026-07-20.md` |
| reviewerOwnedClosurePaths | final completion review; active UX roadmap; material commit |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |
| conversionRule | reviewer recomputes R4 and combines only accepted predecessor evidence |
| failureRoute | truthful block; any source repair requires separate authorization |

## Worker Output Checker Read-Ahead Mandate

Before writing each output, read its checker source and derive exact headings,
trace fields, claim boundary, corpus/rescan handling, no-commit evidence, and
Machine Closure Package shape.

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| R4 final interaction matrix | create three terminal rows |
| R4 worker return | create full-gate return with actual commands |
| R4 evidence directory | create exactly three PNG and five JSON files |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_WEB_UX_T4_R4_WORKER_RETURN_2026-07-20.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Web/UI Claim Boundary

| Field | Value |
|---|---|
| DESIGN.md read | required before browser execution |
| UI claim boundary | current-source localhost evidence only; no hosted or production-readiness claim |

## Agent Operation Trace Block

| Field | Required worker evidence |
|---|---|
| Actor | delegated R4 browser-evidence worker |
| Provider or surface | current-source localhost browser |
| Agent type | evidence worker |
| Session or invocation | R4 worker session |
| Invocation ID | actual ID or N/A with reason |
| Working directory | repo root and cvf-web package |
| Command or tool surface | git, Next, browser automation, tests, hashes, gates |
| Intent | close final three interaction and command evidence gaps |
| Inputs | R4 order, R3 review, DESIGN.md, target source |
| Target paths | exact R4 Allowed Scope |
| Allowed scope source | this work order |
| Expected manifest | matrix, return, exactly eight evidence files |
| Before status evidence | clean worktree and supplied HEAD |
| Actions | start, dismiss, focus, activate, assert, capture, test, stop, verify |
| Outputs | terminal R4 interaction and command evidence |
| Evidence | PNG, JSON, visible anchors, responses, commands, hashes |
| After status evidence | exact status, unchanged HEAD, zero listeners, no scratch |
| Actual changed set | exact final manifest |
| Manifest delta | NONE or truthful blocked explanation |
| Deletion or rename disposition | N/A with reason: no repository deletion or rename authorized |
| Approval boundary | no source, predecessor, session, commit, hosted, public, provider, or production authority |
| Diff evidence | status, diff, cached diff, HEAD before/after |
| Claim boundary | current-source localhost R4 evidence only |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | deterministic localhost interaction and command evidence |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT - no provider receipt authorized |
| actionEvidence | ACTION_EVIDENCE_PRESENT only through target-bound browser interactions |
| invocationBoundary | local Next, browser, and provider-free test processes |
| interceptionBoundary | no provider, hosted, production, or external-service interception |
| claimLanguage | R4 records only directly observed current-source states |
| forbiddenExpansion | source repair, hosted freshness, live governance, deploy, public, provider, production |

## Foundation Storage Layout Block

NOT_APPLICABLE_WITH_REASON: R4 creates review evidence only; no foundation,
registry, runtime store, or generated aggregate is created.

## Acceptance Criteria

- [ ] Home result is bound to DynamicForm h1 and a form label after onboarding dismissal.
- [ ] Workspace records false-to-true-to-false on the same summary target.
- [ ] Knowledge uses exact action text and retains its exact response plus visible result/error.
- [ ] Three screenshots and five JSON files exist with matching hashes.
- [ ] Diagnostics are terminal and truthfully classified.
- [ ] R1-R3 hashes are unchanged.
- [ ] Focused `test:run`, file-size, and final worker-fast pass with no pending row.
- [ ] Server Ready and post-stop zero-listener evidence are retained.
- [ ] Only exact R4 scope is present; no scratch, staged change, or HEAD movement.

## Review Gate

Reviewer inspects all three images at original resolution, recomputes hashes,
verifies targets/results against source, checks command output and teardown,
and reruns reviewer/pre-closure gates before T4 and roadmap closure.

## Closure Checklist

- [ ] Three interaction rows terminal.
- [ ] Diagnostics and commands terminal.
- [ ] Predecessor integrity and exact scope terminal.
- [ ] Reviewer decision recorded.
- [ ] T4 and roadmap closure reconciled only if all acceptance criteria pass.

## Return-To-Orchestrator Conditions

Return blocked for missing exact target, generic/script result, failing test or
gate, listener residue, predecessor drift, scratch residue, or forbidden need.

## Operator Checkpoint

No checkpoint is needed for evidence execution. Any source, hosted, deploy,
public, provider, or production action requires new authorization.

## Current Runtime Freshness Verification

| Surface | Verification | Required disposition |
|---|---|---|
| current Web source | exact worker HEAD and localhost Ready | PASS or BLOCKED |
| interaction semantics | exact source-bound targets/results | PASS or BLOCKED |
| predecessor evidence | before/after hashes | PASS or BLOCKED |
| hosted runtime | not invoked | N/A with reason |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | dispatch-ready | PASS |
| Completion or reviewer artifact | reviewer completion | pending R4 | N/A with reason |
| Roadmap state | active UX roadmap | T4-R4 dispatch-ready | PASS |
| Registry JSON | corpus aggregate | no mutation authorized | N/A with reason |
| Registry Markdown | paired registry | no mutation authorized | N/A with reason |
| External evidence digest | R4 hashes | worker to create | N/A with reason |
| System loop interlock | no loop mutation | evidence-only | N/A with reason |
| Session continuity | final session-sync HEAD | operator supplies | PASS |

## Acceptance Receipt Assertion Matrix

| Query ID | Receipt artifact | JSON path | Required value | Observed value | Status |
|---|---|---|---|---|---|
| R4-AR-01 | `interaction-trace.json` | Home | form-specific anchor | pending | N/A with reason |
| R4-AR-02 | `interaction-trace.json` | Workspace | false-true-false | pending | N/A with reason |
| R4-AR-03 | `interaction-trace.json` | Knowledge | exact action/response/visible result | pending | N/A with reason |
| R4-AR-04 | `commands.json` | terminal commands | no pending/failure/listener | pending | N/A with reason |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: R4 is private localhost evidence. Hosted, deploy, and public lanes are
outside this packet.

## Claim Boundary

This packet authorizes only fresh R4 localhost interaction and command evidence.
It does not authorize Web source mutation, hosted equivalence, deployment,
public export, provider/live calls, production action, or closure.
