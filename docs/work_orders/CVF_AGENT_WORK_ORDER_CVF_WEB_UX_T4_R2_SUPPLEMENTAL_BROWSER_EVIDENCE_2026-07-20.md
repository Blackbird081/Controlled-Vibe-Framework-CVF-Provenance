# CVF Agent Work Order - CVF Web UX T4 R2 Supplemental Browser Evidence

Memory class: governed-worker-dispatch

Status: REVIEWED_BLOCK_ACCEPTED_R3_REQUIRED

Batch ID: CVF-WEB-UX-T4-R2

Dispatch base head: `576bc1a18`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: delegated browser-evidence worker

Reviewer/closer: independent reviewer/closer

Worker return path: `docs/reviews/CVF_WEB_UX_T4_R2_WORKER_RETURN_2026-07-20.md`

## Dispatch Prompt Envelope

Role: capture only the missing source-valid supplemental browser proof.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_WEB_UX_T4_R2_SUPPLEMENTAL_BROWSER_EVIDENCE_2026-07-20.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: require the operator-provided final packet/session-sync HEAD.

Current-time notes: R1 route/render evidence is retained and immutable. At
820px the sidebar is persistent; do not claim an open/closed drawer there.

Do-not-misread notes: R2 is supplemental. Do not recapture the full twelve-row
matrix and do not mutate Web source or R1 evidence.

Required first actions: confirm clean worktree and exact HEAD, read source
breakpoints, run pre-implementation, then start current Web on localhost:3000.

Return contract: create four fresh screenshots plus complete JSON/console/focus
evidence, run worker-fast, stop all processes, and return a terminal result.

## Purpose

Close only the evidence gaps left by R1: source-valid narrow sidebar behavior,
820px persistent-sidebar truth, visible non-default preference selection,
required keyboard paths, diagnostics, and full worker-return gate shape.

## Authority Chain

Operator continuation -> active UX roadmap -> first T4 block -> R1 block ->
R1 independent review -> this R2 supplemental evidence packet.

## Agent Roles

- Worker: supplemental browser evidence only; no commit.
- Reviewer/closer: combines accepted T4/R1/R2 evidence and decides closure.
- Session-sync steward: updates continuity only after reviewer decision.

## Write Ownership

Worker owns exactly the R2 matrix, R2 return, and fresh R2 evidence directory.
All earlier evidence and all source/session/public surfaces are forbidden.

## Dependency Release Evidence

| Dependency | Artifact | Material commit | Final disposition |
|---|---|---|---|
| R1 independent review | `docs/reviews/CVF_WEB_UX_T4_R1_BLOCKED_RETURN_REVIEW_2026-07-20.md` | N/A with reason: review and R2 dispatch share one material batch | `REVIEWED_BLOCK_ACCEPTED_R2_REQUIRED` |
| R1 evidence | `docs/reviews/evidence/CVF_WEB_UX_T4_R1_LOCALHOST_2026-07-19/captures.json` | `f2f8c95e1` dispatch lineage plus uncommitted worker output | reusable partial evidence; immutable during R2 |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-WEB-UX-T4-R2 --title "CVF Web UX T4 R2 Supplemental Browser Evidence" --date 2026-07-20 --base 576bc1a18 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus supplemental browser-evidence profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | added source-valid breakpoints, four-state ceiling, focus/console proof, and immutable predecessor boundary |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py` |
| docOnlyNewFields | R2 supplemental trace fields below |
| claimBoundary | scaffold provenance only; no browser acceptance claim |

## Worker Autonomy / No-Question Rule

Execute the four-state evidence supplement without asking preference questions.
Return blocked before any forbidden edit if current source cannot prove a state.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`web-ui-browser-audit`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "web-ui-browser-audit" --role dispatcher --lifecycle-phase pre-dispatch` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | direct breakpoint source verification replaces the invalid R1 tablet-drawer assumption |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | dispatch status; source verification symbols; worker-return full fields; handoff route; closure conversion |
| gateRunPurpose | confirm R2 source fidelity and dispatch shape before execution |
| claimBoundary | gate PASS authorizes evidence work only |

## Roadmap-to-Work-Order Trace Matrix

| Roadmap requirement | R2 control | Evidence required | Fail condition |
|---|---|---|---|
| responsive navigation | distinguish 820px persistent and 767px drawer behavior | three bound screenshots and state traces | treating 820px as drawer state |
| non-default accent | visibly select violet while preferences are open | selected-control state plus resulting CSS/local state | color inferred from screenshot only |
| keyboard usability | traverse named controls using keyboard | keys and before/after active-element descriptors | generic Tab summary |
| diagnostics | retain console events | `console.json` with terminal classification | missing file or hidden errors |
| browser acceptance | combine with accepted predecessor evidence | supplemental matrix links predecessor | full-matrix recapture or unsupported closure claim |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| mobile header and drawer controls are below `md` | LITERAL_INVARIANT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/CompactHeader.tsx` | definition line 66; responsive header line 132 | `CompactHeader` | `CompactHeader` | ACCEPT |
| sidebar is persistent at `md` and above | LITERAL_INVARIANT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/Sidebar.tsx` | definition line 48; responsive class line 100 | `Sidebar` | `Sidebar` | ACCEPT |
| sidebar close control is hidden at `md` | LITERAL_INVARIANT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/Sidebar.tsx` | definition line 48; close-control line 116 | `Sidebar` | `Sidebar` | ACCEPT |
| drawer opener has accessible label | LITERAL_INVARIANT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/SidebarToggle.tsx` | line 11 | `aria-label` | `SidebarToggle` | ACCEPT |
| default accent is indigo | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/CompactHeader.tsx` | lines 27-31 | `DEFAULT_TWEAKS` | `TweaksState` | ACCEPT |
| preferences expose accent options | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/CompactHeader.tsx` | lines 172-230 | `isPreferencesOpen` | `CompactHeader` | ACCEPT |

## New Doc-Only Fields

| Field | Purpose | Claim boundary |
|---|---|---|
| `responsiveMode` | distinguish persistent sidebar from drawer | R2 evidence vocabulary only |
| `computedAccentRgb` | retain applied non-default accent token | observed localhost DOM only |
| `keyboardScenario` | bind keys to target and result | sampled browser path only |
| `predecessorEvidenceRef` | reuse accepted R1 rows without copying | no alteration or blanket acceptance of R1 |

## Evidence Reuse And Encoding Plan

verificationMode: REUSE_PRIOR_VERIFICATION

priorVerificationArtifact: `docs/reviews/CVF_WEB_UX_T4_R1_BLOCKED_RETURN_REVIEW_2026-07-20.md`

priorVerificationAnchor: reviewer-accepted bounded R1 route/hash evidence

freshRecomputeRequired: four R2 screenshots, all R2 hashes, console and focus traces

unicodePathHandling: use literal repository paths and UTF-8-safe readers for Vietnamese visible text

extractedTextAuthority: rendered browser text is evidence only; current source remains authority

## Required First Reads

Read `DESIGN.md`, this packet, R1 blocked review, R1 matrix, responsive source,
and worker-return checker sources before starting Web.

## Pre-Flight Checks

- require clean worktree and exact supplied execution base;
- verify R2 output paths do not exist;
- hash R1 evidence before work and preserve it;
- run pre-implementation before starting Web;
- do not load provider keys or invoke live proof.

## Execution Plan

1. Start current-source Web on localhost:3000 and wait for Ready.
2. Use browser subagent when available; disclose Playwright fallback otherwise.
3. Capture `tablet-820-persistent-sidebar` at 820x1180.
4. Capture `narrow-tablet-767-sidebar-closed` and `narrow-tablet-767-sidebar-open` at 767x1024.
5. Capture `desktop-dark-preferences-violet-open` at 1440x900 with violet selected and applied.
6. Record keyboard scenarios for preferences, drawer open/close, primary Home action, Workspace details open/close, and one journey action using Tab, Shift+Tab, Enter, and Escape where applicable.
7. Write `captures.json`, `console.json`, `focus-trace.json`, and predecessor hash check.
8. Run focused provider-free tests, file-size, worker-fast, exact manifest, and teardown checks.
9. Stop all started processes and return without staging or committing.

## Required Browser States

Exactly four fresh screenshots:

- `tablet-820-persistent-sidebar.png`;
- `narrow-tablet-767-sidebar-closed.png`;
- `narrow-tablet-767-sidebar-open.png`;
- `desktop-dark-preferences-violet-open.png`.

The 767px closed/open pair must be visibly and hash-distinct. The 820px state
must be classified persistent, not open/closed. Preferences must visibly show
violet selected while default source value remains indigo.

## Allowed Scope

- `docs/reviews/CVF_WEB_UX_T4_R2_SUPPLEMENTAL_BROWSER_ACCEPTANCE_MATRIX_2026-07-20.md`
- `docs/reviews/CVF_WEB_UX_T4_R2_WORKER_RETURN_2026-07-20.md`
- `docs/reviews/evidence/CVF_WEB_UX_T4_R2_LOCALHOST_2026-07-20/`

## Forbidden Scope

Every other path, including Web source/tests, R1/T4 evidence, roadmap, session,
handoff, dependencies, scripts, lockfiles, hosted/deploy/public/provider/live,
production, and continuous-projection surfaces.

## Evidence Requirements

- exactly four fresh PNGs and four bound records;
- `captures.json`, `console.json`, `focus-trace.json`, and predecessor hash check;
- exact URL, literal anchor, selector, viewport, responsive mode, image path,
  SHA-256, widths, diagnostics, and verdict per screenshot;
- named keyboard scenario records with before/after active-element descriptors;
- server Ready/stop and no-listener evidence;
- exact git manifest, unchanged HEAD, nothing staged;
- focused provider-free checks, file-size, and worker-fast PASS.

## Verification Commands

1. pre-implementation autorun with the actual execution base;
2. provider-free focused tests for header, sidebar, Home, Workspace, and journey;
3. `python governance/compat/check_governed_file_size.py --enforce`;
4. `python governance/compat/run_worker_return_fast_gate.py`;
5. final git HEAD/status/diff/cached-diff, hashes, and listener checks.

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | reviewed R1 evidence and current source |
| Scope classification | supplemental browser evidence only |
| Intake role | worker captures missing proof |
| Reviewer role | independent reviewer combines T4/R1/R2 evidence |
| Routing decision | WORKER_MUST_NOT_COMMIT |
| Public route | DEFERRED_PRIVATE_ONLY |
| canonical route mode | SINGLE_AGENT_SINGLE_ROLE |
| selected role route | R2 worker return to reviewer closure conversion |
| escalation condition | source defect, unavailable rendered browser, protected-path need, or non-terminal required state |
| risk sensitivity | MEDIUM: final roadmap acceptance proof |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | NOT_APPLICABLE_WITH_REASON: no outside artifact promoted |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | R2 evidence and independent completion review |
| Disposition | NOT_APPLICABLE_WITH_REASON: current source and local browser only |
| Claim boundary | no external authority or hosted equivalence claim |

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

## Agent Handoff Contract Control Block

| Field | Value |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | delegated browser-evidence worker to independent reviewer/closer |
| phase | implementation |
| baseHeadFor(phase) | dispatchBaseHead=576bc1a18; executionBaseHead=OPERATOR_PROVIDED_FINAL_SESSION_SYNC_HEAD; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | exact new R2 Allowed Scope |
| traceScope(phase, actor) | process, browser, four images, hashes, focus, console, tests, gates, return |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | predecessor evidence immutable; source and mutation lanes parked |
| nextMoveSurfaces | reviewer decides T4/roadmap closure; session steward updates continuity |

## Dual Agent Surface Matrix

| Surface | Interface | Authority / risk boundary | Required evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | repository/browser worker | exact R2 outputs; no source or commit | supplemental rendered evidence | current filesystem/browser tooling | REPAIR_EVIDENCE_ONLY |
| EXTERNAL_AGENT_CLI_MCP | external browser worker | same packet and no-commit boundary | same four-state trace schema | operator-provided browser/CLI adapter only | CONTRACT_ONLY |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_WEB_UX_T4_COMPLETION_2026-07-20.md` |
| reviewerOwnedClosurePaths | final T4 completion review; active UX roadmap; material commit |
| conversionRule | reviewer combines accepted predecessor rows with R2, recomputes all R2 evidence, and closes only when every roadmap criterion is terminal |
| failureRoute | truthful R2 block; any source repair requires a separate packet |

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The return must contain every full-gate field, actual command evidence, exact
manifest, diagnostics, teardown, retrospective, and Machine Closure Package.

## Agent Operation Trace Block

| Field | Required worker evidence |
|---|---|
| Actor | delegated R2 browser-evidence worker |
| Provider or surface | current-source localhost browser |
| Agent type | evidence worker |
| Session or invocation | R2 worker session |
| Invocation ID | worker identifier or N/A with reason |
| Working directory | repository root and cvf-web package |
| Command or tool surface | git, Next, browser automation, hashing, tests, gates |
| Intent | close the remaining browser-evidence gaps |
| Inputs | R2 order, R1 review, DESIGN.md, responsive source |
| Target paths | exact R2 Allowed Scope |
| Allowed scope source | this work order |
| Expected manifest | matrix, return, evidence directory |
| Before status evidence | clean worktree and supplied HEAD |
| Actions | start, interact, capture, trace, verify, stop |
| Outputs | four-state supplemental evidence and return |
| Evidence | JSON, PNGs, anchors, focus, console, metrics, commands |
| After status evidence | exact status, unchanged HEAD, no listeners |
| Actual changed set | exact final manifest |
| Manifest delta | NONE or explained allowed subset |
| Deletion or rename disposition | N/A with reason: no deletion or rename authorized |
| Approval boundary | no source, predecessor evidence, session, commit, hosted, deploy, public, provider, or production authority |
| Diff evidence | git status, diff, cached diff, and HEAD before/after |
| Claim boundary | current-source localhost R2 evidence only |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | deterministic supplemental localhost browser evidence |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT - no provider receipt authorized |
| actionEvidence | ACTION_EVIDENCE_PRESENT through four browser states and named keyboard traces |
| invocationBoundary | local Next and provider-free browser/test process only |
| interceptionBoundary | no provider, hosted, production, or external-service interception |
| claimLanguage | R2 records only the observed supplemental states |
| forbiddenExpansion | source repair, hosted freshness, live governance, deploy, public, provider, production |

## Foundation Storage Layout Block

NOT_APPLICABLE_WITH_REASON: R2 uses a new review-evidence folder and creates no
foundation, registry, durable store, or generated aggregate.

## Acceptance Criteria

- [ ] Exactly four required fresh PNGs and bound records exist.
- [ ] 820px is proven as persistent-sidebar behavior.
- [ ] 767px closed/open drawer states are visibly and hash-distinct.
- [ ] Preferences visibly show violet selected and applied versus default indigo.
- [ ] All five named keyboard scenarios have keys and before/after descriptors.
- [ ] Console diagnostics are retained and terminally classified.
- [ ] R1/T4 evidence hashes remain unchanged.
- [ ] Server teardown and no-listener checks pass.
- [ ] Only exact R2 Allowed Scope changes; nothing staged; HEAD unchanged.
- [ ] Focused checks, file-size, and worker-fast pass.

## Review Gate

Reviewer inspects all four original-resolution images, recomputes hashes,
verifies source-valid responsive semantics, checks focus/console evidence,
confirms predecessor immutability, and reruns reviewer/pre-closure gates.

## Closure Checklist

- [ ] Four supplemental states terminal.
- [ ] Every evidence field recomputed.
- [ ] Focus and console proof terminal.
- [ ] Exact scope and teardown proven.
- [ ] Reviewer decision recorded.
- [ ] Roadmap closure state reconciled only if accepted.

## Return-To-Orchestrator Conditions

Return blocked for any unavailable rendered state, source contradiction, missing
trace, failing gate, listener residue, or forbidden-path need.

## Operator Checkpoint

No checkpoint is needed for evidence-only execution. Any source, hosted,
deployment, public, provider, or production action requires new authorization.

## Current Runtime Freshness Verification

| Surface | Verification | Required disposition |
|---|---|---|
| current Web source | exact worker HEAD and localhost start | PASS or BLOCKED |
| responsive semantics | source lines plus rendered states | PASS or BLOCKED |
| predecessor evidence | hash check | PASS or BLOCKED |
| hosted runtime | not invoked | N/A with reason |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | dispatch-ready before worker | PASS |
| Completion or reviewer artifact | reviewer-owned completion review | pending R2 review | N/A with reason |
| Roadmap state | active UX roadmap | T4-R2 dispatch-ready | PASS |
| Registry JSON | corpus aggregate | drift check only; no mutation authorized | N/A with reason |
| Registry Markdown | paired registry | no mutation authorized | N/A with reason |
| External evidence digest | R2 evidence hashes | worker to create | N/A with reason |
| System loop interlock | no loop mutation | evidence-only packet | N/A with reason |
| Session continuity | final session-sync HEAD | operator supplies | PASS |

## Acceptance Receipt Assertion Matrix

| Query ID | Receipt artifact | JSON path | Required value | Observed value | Status |
|---|---|---|---|---|---|
| R2-AR-01 | R2 `captures.json` | four capture records | four terminal records | pending worker | N/A with reason |
| R2-AR-02 | R2 `focus-trace.json` | keyboard scenarios | five terminal scenarios | pending worker | N/A with reason |
| R2-AR-03 | R2 `console.json` | diagnostic entries | terminal classification | pending worker | N/A with reason |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: R2 is private localhost acceptance evidence; public/deploy lanes remain
outside this packet.

## Claim Boundary

This packet authorizes four-state supplemental current-source localhost
evidence only. It does not authorize source mutation, hosted equivalence,
deployment, public export, provider/live calls, production action, or closure.
