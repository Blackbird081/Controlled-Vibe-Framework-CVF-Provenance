<!-- Text Encoding Exception: exact Vietnamese UI labels are required evidence. -->
# CVF Agent Work Order - CVF Web UX T4 R5 Screenshot State Binding Repair

Memory class: governed-worker-dispatch

Status: CLOSED_PASS_BOUNDED

Batch ID: CVF-WEB-UX-T4-R5

Dispatch base head: `ce5ff64fb`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: delegated browser-evidence worker

Reviewer/closer: independent reviewer/closer

Worker return path: `docs/reviews/CVF_WEB_UX_T4_R5_WORKER_RETURN_2026-07-20.md`

## Dispatch Prompt Envelope

Role: repair only the three R4 screenshots whose pixels contradict their JSON.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_WEB_UX_T4_R5_SCREENSHOT_STATE_BINDING_REPAIR_2026-07-20.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: require the operator-provided final session-sync HEAD.

Current-time notes: R1-R4 evidence is immutable. Start current cvf-web source on
localhost:3000 and wait for Ready. Use a real visible browser or browser subagent
and visually reopen every saved PNG before returning.

Do-not-misread notes: DOM metadata is not a substitute for the saved pixels.
Any onboarding overlay, blur layer, hidden target, mismatched hash, or missing
visible anchor makes that capture fail.

Required first actions: confirm clean worktree and exact HEAD; read `DESIGN.md`,
the R4 review, this packet, target source, and worker-return checkers; run
pre-implementation; keep browser automation only under the OS temporary folder.

Return contract: produce only the R5 outputs, stop Web, prove no listener, delete
temporary automation, and return `COMPLETE_PENDING_REVIEW` or
`BLOCKED_WITH_REASON` without staging or commit.

## Purpose

Replace no source and redo no accepted R4 command work. Capture three fresh
screenshots that visibly show the exact Home, Workspace, and Knowledge terminal
states, with post-write hash and overlay-absence evidence bound to each image.

## Authority Chain

Operator continuation -> active UX roadmap -> T4 -> R4 review -> this R5.

## Agent Roles

- Worker: current-source localhost capture and screenshot integrity only.
- Reviewer/closer: opens every PNG, recomputes hashes, and decides T4 closure.
- Session-sync steward: updates continuity only after reviewer decision.

## Write Ownership

Worker owns exactly the R5 matrix, R5 return, and fresh R5 evidence directory.
All automation remains outside the repository and is deleted before return.

## Dependency Release Evidence

| Dependency | Artifact | Material commit | Final disposition |
|---|---|---|---|
| R4 independent review | `docs/reviews/CVF_WEB_UX_T4_R4_BLOCKED_RETURN_REVIEW_2026-07-20.md` | N/A with reason: review and R5 dispatch share the current material batch | `REVIEWED_BLOCK_ACCEPTED_R5_REQUIRED` |
| accepted predecessor subset | R1-R4 evidence roots | material commit pending reviewer stewardship | immutable; reuse without recapture |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-WEB-UX-T4-R5 --title "CVF Web UX T4 R5 Screenshot State Binding Repair" --date 2026-07-20 --base ce5ff64fb --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit Web evidence profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | narrowed output to visible screenshot state, post-write hash, overlay absence, and visual reopen |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py` |
| docOnlyNewFields | `onboardingStorageValue`; `overlayCount`; `postWriteSha256`; `visualReopenVerdict` |
| claimBoundary | dispatch provenance only; no interaction acceptance claim |

## Worker Autonomy / No-Question Rule

Repair allowed-scope checker failures directly. Return blocked for unavailable
visible-browser inspection, missing exact target, persistent overlay, failing
hash comparison, forbidden-scope need, active listener, or source contradiction.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`web-ui-browser-audit`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "web-ui-browser-audit" --role dispatcher --lifecycle-phase pre-dispatch` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | packet supplies pixel-to-metadata binding and overlay fail conditions locally |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | dispatch status; source verification; handoff; worker return; closure conversion; exact output manifest |
| gateRunPurpose | confirmation after direct review of the R4 contradiction and current source |
| claimBoundary | checker PASS authorizes capture only; it does not prove image content |

## Roadmap-to-Work-Order Trace Matrix

| Roadmap requirement | R5 control | Evidence required | Fail condition |
|---|---|---|---|
| primary Home action | show the DynamicForm result without overlay | visible h1 and form label in PNG | wizard, blur, or missing label |
| advanced disclosure | show Workspace details open without overlay | visible summary plus expanded content | collapsed or obscured panel |
| journey terminal action | show exact Knowledge 401 result without overlay | visible error and compile page context | hidden or unrelated 401 |
| browser acceptance truth | bind metadata to saved bytes | post-write SHA256 and visual reopen verdict | mismatch or metadata-only PASS |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| onboarding completion is persisted | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/hooks/useModals.ts` | lines 20-30 | `handleOnboardingComplete` | `useModals` | ACCEPT |
| onboarding dismiss label is visible | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/OnboardingWizard.tsx` | labels block and dismiss button | `LABELS` | `OnboardingWizard` | ACCEPT |
| Home action exposes an accessible title | LITERAL_INVARIANT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/OutcomeQuickActions.tsx` | lines 100-111 | `aria-label` | `OutcomeQuickActions` | ACCEPT |
| Home form title is source-declared | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates/development.ts` | line 61 | `name` | development template catalog | ACCEPT |
| Workspace advanced disclosure exists | LITERAL_INVARIANT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app` | child `(dashboard)/workspace/page.tsx`, lines 167-176 | `advanced-detail` | `WorkspacePage` | ACCEPT |
| Knowledge compile action text is source-declared | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app` | child `(dashboard)/governance/knowledge/page.tsx`, lines 47-59 | `compile` | `KnowledgeGovernancePage` | ACCEPT |
| unauthenticated compile response text is source-declared | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/governance/knowledge/compile/route.ts` | lines 12-24 | `POST` | compile route | ACCEPT |

## New Doc-Only Fields

| Field | Purpose | Claim boundary |
|---|---|---|
| `onboardingStorageValue` | prove persistent context dismissal state | sampled local browser context |
| `overlayCount` | prove onboarding heading and blocking overlay are absent at capture | sampled rendered DOM |
| `postWriteSha256` | bind record to exact saved PNG bytes | R5 evidence file |
| `visualReopenVerdict` | record manual or browser-subagent inspection of saved PNG | R5 visual acceptance only |

## Evidence Reuse And Encoding Plan

verificationMode: REUSE_PRIOR_VERIFICATION

priorVerificationArtifact: `docs/reviews/CVF_WEB_UX_T4_R4_BLOCKED_RETURN_REVIEW_2026-07-20.md`

priorVerificationAnchor: accepted R1-R4 responsive, interaction, command, test, and teardown subsets

freshRecomputeRequired: three visible PNGs, their metadata and hashes, predecessor integrity, Ready and teardown

unicodePathHandling: retain exact UTF-8 Vietnamese visible labels and use literal paths

extractedTextAuthority: current source is authority; rendered text and pixels are sampled evidence

## Required First Reads

Read `DESIGN.md`, this packet, the R4 review, `useModals.ts`,
`OnboardingWizard.tsx`, the three target surfaces, and worker-return checkers.

## Pre-Flight Checks

- require clean worktree and the supplied execution base;
- verify R5 output paths do not exist;
- hash the entire R1-R4 evidence trees before work;
- run pre-implementation before Web start;
- do not load provider keys or invoke live proof;
- create browser automation only under `$env:TEMP` and delete it before return.

## Execution Plan

1. Start current-source Web on localhost:3000 and retain actual Ready output.
2. Open one persistent visible browser context. Dismiss the wizard using its
   visible `Bỏ qua giới thiệu` action and verify local storage contains
   `cvf_onboarding_complete=true`.
3. For Home, activate the exact `Tạo PRD` button. Before saving the image, assert
   the onboarding heading is absent, no blocking onboarding overlay is visible,
   and the form heading plus first form label are visible.
4. For Workspace, keep the same context, open exact `advanced-detail`, assert it
   remains open, assert overlay absence, and save the visible expanded panel.
5. For Knowledge, keep the same context, fill content, activate only the exact
   enabled `Biên soạn` action, wait for its compile response and visible error,
   assert overlay absence, and save the terminal page.
6. After each image write, compute SHA256, store it in both capture and integrity
   records, reopen the saved PNG in a visible browser/image viewer, and record
   `PASS` only if the claimed anchor is visible in the saved pixels.
7. Run file-size and worker-fast, stop Web, prove zero listeners, delete the temp
   script, verify exact scope and unchanged HEAD, then return.

## Required Browser Evidence

Create exactly three PNG files:

- `home-tao-prd-form-result.png`;
- `workspace-advanced-open.png`;
- `knowledge-compile-terminal.png`.

Create exactly four JSON files:

- `captures.json`;
- `screenshot-integrity.json`;
- `commands.json`;
- `predecessor-integrity.json`.

## Screenshot Integrity Contract

Every screenshot row must retain route, viewport, exact target, exact visible
anchor, `onboardingStorageValue=true`, `overlayCount=0`, post-write file size,
post-write SHA256, and `visualReopenVerdict=PASS`. The SHA256 in
`captures.json` must equal the value independently recomputed after the final
write. A screenshot taken before the final navigation or after a reload that
reopens onboarding fails.

## Allowed Scope

- `docs/reviews/CVF_WEB_UX_T4_R5_SCREENSHOT_STATE_BINDING_MATRIX_2026-07-20.md`
- `docs/reviews/CVF_WEB_UX_T4_R5_WORKER_RETURN_2026-07-20.md`
- `docs/reviews/evidence/CVF_WEB_UX_T4_R5_LOCALHOST_2026-07-20/`

## Forbidden Scope

Every other repository path, including Web source/tests, R1-R4 evidence,
roadmap, session, dependencies, lockfiles, hosted/deploy/public, provider/live,
production, continuous projection, and repository scratch scripts.

## Evidence Requirements

- exactly three PNG and four JSON files;
- all three images visibly free of onboarding and blur overlays;
- image-visible anchor, storage value, overlay count, byte size, hash, and visual
  reopen evidence for every PNG;
- unchanged predecessor evidence hashes;
- actual Ready and post-stop zero-listener evidence;
- exact git manifest, unchanged HEAD, nothing staged, and no scratch files;
- file-size and final worker-fast PASS with no pending row.

## Verification Commands

Run file-size, worker-fast, final HEAD/status/diff/cached-diff, predecessor hash
comparison, temp-script deletion check, process stop, and port check.

Required worker-return command:

`python governance/compat/run_worker_return_fast_gate.py`

## Acceptance Criteria

- [x] Home PNG visibly shows the DynamicForm heading and a form label with no overlay.
- [x] Workspace PNG visibly shows expanded advanced detail with no overlay.
- [x] Knowledge PNG visibly shows the exact unauthorized result with no overlay.
- [x] Each final PNG has matching post-write hashes in both JSON records.
- [x] Each saved PNG was visually reopened and truthfully classified.
- [x] R1-R4 evidence is unchanged and Web source is untouched.
- [x] Web is stopped, port 3000 has no listener, and temp automation is deleted.
- [x] Worker-fast and file-size pass with actual terminal results.
- [x] HEAD is unchanged, nothing is staged, and changed set equals Allowed Scope.

## Review Gate

The independent reviewer must open all three PNGs at original resolution,
recompute every SHA256 from disk, compare those values with both JSON records,
and confirm that each claimed anchor is visibly present while the onboarding
overlay is absent. JSON agreement without matching pixels fails review.

## Closure Checklist

- [x] Exact R5 manifest contains one matrix, one return, three PNGs, and four JSON files.
- [x] All three image hashes recompute exactly.
- [x] All three saved images visibly show their route-specific terminal state.
- [x] No onboarding heading, wizard, blur, or blocking overlay appears in any PNG.
- [x] Predecessor evidence and Web source remain unchanged.
- [x] File-size and worker-fast are terminal PASS.
- [x] Web is stopped, port 3000 is clear, and no scratch automation remains.
- [x] Reviewer closes T4 bounded through the required completion review.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only when every R5 acceptance criterion is met
and retained evidence is terminal. Return `BLOCKED_WITH_REASON` before claiming
PASS if visible-browser inspection is unavailable, any saved PNG still contains
onboarding, any hash differs, any required command fails, or repair would need a
forbidden path.

## Operator Checkpoint

N/A with reason: the operator already authorized continued tranche execution
through roadmap completion. R5 creates only private localhost evidence and does
not cross a deploy, public-sync, provider/live, production, or source-mutation
checkpoint.

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | R4 review and current source |
| Scope classification | screenshot-state binding repair only |
| Intake role | browser-evidence worker |
| Reviewer role | independent reviewer/closer |
| Routing decision | WORKER_MUST_NOT_COMMIT |
| Public route | DEFERRED_PRIVATE_ONLY |
| canonical route mode | SINGLE_AGENT_SINGLE_ROLE |
| selected role route | R5 worker to reviewer closure conversion |
| escalation condition | persistent overlay, missing anchor, unavailable visible inspection, or forbidden-path need |
| risk sensitivity | MEDIUM: final roadmap visual acceptance evidence |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | NOT_APPLICABLE_WITH_REASON: no outside artifact promoted |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | R5 evidence and independent review |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | no external authority or hosted-equivalence claim |

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

## Agent Handoff Contract Control Block

| Field | Value |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | delegated evidence worker to independent reviewer/closer |
| phase | implementation |
| baseHeadFor(phase) | dispatchBaseHead=ce5ff64fb; executionBaseHead=OPERATOR_PROVIDED_FINAL_SESSION_SYNC_HEAD; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | exact new R5 Allowed Scope |
| traceScope(phase, actor) | browser context, overlay state, visible targets, final PNG bytes, hashes, visual reopen, process teardown |
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
| conversionRule | reviewer opens every R5 PNG and independently recomputes hashes before combining accepted predecessor evidence |
| failureRoute | truthful block; any Web source repair requires separate authorization |

## Worker Output Checker Read-Ahead Mandate

Before writing each output, read its checker source and derive exact headings,
trace fields, claim boundary, corpus handling, no-commit evidence, and Machine
Closure Package shape.

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| R5 screenshot-state matrix | create three terminal pixel-bound rows |
| R5 worker return | create full-gate return with actual commands |
| R5 evidence directory | create exactly three PNG and four JSON files |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_WEB_UX_T4_R5_WORKER_RETURN_2026-07-20.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Web/UI Claim Boundary

| Field | Value |
|---|---|
| DESIGN.md read | required before browser execution |
| UI claim boundary | current-source localhost screenshots only; no hosted or production-readiness claim |

## Agent Operation Trace Block

| Field | Required worker evidence |
|---|---|
| Actor | delegated R5 browser-evidence worker |
| Provider or surface | current-source localhost visible browser |
| Agent type | evidence worker |
| Session or invocation | R5 worker session |
| Invocation ID | actual ID or N/A with reason |
| Working directory | repo root and cvf-web package |
| Command or tool surface | git, Next, visible browser, image viewer, hashes, gates |
| Intent | repair three screenshot-to-state contradictions |
| Inputs | R5 order, R4 review, DESIGN.md, target source |
| Target paths | exact R5 Allowed Scope |
| Allowed scope source | this work order |
| Expected manifest | matrix, return, exactly seven evidence files |
| Before status evidence | clean worktree and supplied HEAD |
| Actions | start, persist dismissal, navigate, focus, activate, assert, capture, hash, reopen, stop, verify |
| Outputs | terminal R5 screenshot-state evidence |
| Evidence | PNG pixels, JSON state, hashes, visible anchors, process output |
| After status evidence | exact status, unchanged HEAD, zero listeners, no scratch |
| Actual changed set | exact final manifest |
| Manifest delta | NONE or truthful blocked explanation |
| Deletion or rename disposition | N/A with reason: no repository deletion or rename authorized |
| Approval boundary | no source, predecessor, session, commit, hosted, public, provider, or production authority |
| Diff evidence | status, diff, cached diff, and HEAD before/after |
| Claim boundary | current-source localhost R5 visual evidence only |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | deterministic localhost screenshot-state evidence |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT - no provider receipt authorized |
| actionEvidence | ACTION_EVIDENCE_PRESENT only through target-bound local browser actions and saved pixels |
| invocationBoundary | local Next, browser, image-viewer, and hash processes |
| interceptionBoundary | no provider, hosted, production, or external-service interception |
| claimLanguage | R5 records only directly observed current-source states and exact saved image bytes |
| forbiddenExpansion | source repair, hosted freshness, live governance, deploy, public, provider, production |

## Foundation Storage Layout Block

NOT_APPLICABLE_WITH_REASON: R5 creates review evidence only; no foundation,
registry, runtime store, or generated aggregate is created.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: R5 is private localhost acceptance evidence. Hosted, deploy, and public
lanes remain outside this packet.

## Acceptance Receipt Assertion Matrix

| Query ID | Receipt artifact | JSON path | Required value | Observed value | Status |
|---|---|---|---|---|---|
| R5-HOME | `docs/reviews/evidence/CVF_WEB_UX_T4_R5_LOCALHOST_2026-07-20/captures.json` | `$[0].overlayCount` | `0` | `0` | PASS |
| R5-WORKSPACE | `docs/reviews/evidence/CVF_WEB_UX_T4_R5_LOCALHOST_2026-07-20/captures.json` | `$[1].overlayCount` | `0` | `0` | PASS |
| R5-KNOWLEDGE | `docs/reviews/evidence/CVF_WEB_UX_T4_R5_LOCALHOST_2026-07-20/captures.json` | `$[2].overlayCount` | `0` | `0` | PASS |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this work order | Status CLOSED_PASS_BOUNDED | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_WEB_UX_T4_COMPLETION_2026-07-20.md` | reviewer decision CLOSED_PASS_BOUNDED | PASS |
| Roadmap state | active UX roadmap | Status CLOSED_PASS_BOUNDED | PASS |
| Registry JSON | corpus registry aggregate | generated aggregate drift check PASS; no entry mutation required | PASS |
| Registry Markdown | corpus registry source/front door | changed-path coverage and registry checks PASS; no entry mutation required | PASS |
| External evidence digest | R5 evidence root | SHA256 `78b68c72d25edf2f69b59ea7160cd7991ca34eabf87b8c91a33cb7c2e9c77a54`; `9ea9972c8fc3adaaf97f1377df5d6a1864d390761e8fe06d3286fde56533e68a`; `3a7d9bf71d165c182542e37be168979ff417ef5a37f7d029f460ab07ef1bcfb5` | PASS |
| System loop interlock | no system-loop mutation | evidence-only work order | N/A with reason |
| Session continuity | active session surfaces | separate session-sync follows material commit | N/A with reason |

## Claim Boundary

This packet authorizes only fresh R5 current-source localhost screenshot-state
binding evidence. It does not authorize Web source mutation, hosted equivalence,
deployment, public export, provider/live calls, production action, or roadmap
closure.
