# CVF Agent Work Order - CVF Web UX T4 R3 Interaction Trace Repair

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: CVF-WEB-UX-T4-R3

Dispatch base head: `64ee90665`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: delegated browser-evidence worker

Reviewer/closer: independent reviewer/closer

Worker return path: `docs/reviews/CVF_WEB_UX_T4_R3_WORKER_RETURN_2026-07-20.md`

## Dispatch Prompt Envelope

Role: repair only the missing semantic interaction evidence from T4-R2.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_WEB_UX_T4_R3_INTERACTION_TRACE_REPAIR_2026-07-20.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: require the operator-provided final packet/session-sync HEAD.

Current-time notes: R1/R2 responsive evidence is retained and immutable. Start
the current cvf-web source on localhost:3000 before browser capture.

Do-not-misread notes: a scenario name or filename is not evidence. Every row
must identify the observed accessible target and a before/after state delta.

Required first actions: confirm clean worktree and exact HEAD; read `DESIGN.md`,
this packet, the R2 review, target source, and worker-return checker source; run
pre-implementation; then start Web and wait for Ready.

Return contract: create exact fresh R3 outputs, run worker-fast, stop the Web
process, prove no listener remains, and return `COMPLETE_PENDING_REVIEW` or
`BLOCKED_WITH_REASON` without staging or committing.

## Purpose

Close the remaining T4 evidence gap with deterministic preferences and keyboard
interaction proof, terminal diagnostics, predecessor integrity, and retained
server/test/gate evidence. Do not recapture accepted responsive states.

## Authority Chain

Operator continuation -> active UX roadmap -> T4 -> R1 -> R2 blocked review ->
this R3 evidence-only packet.

## Agent Roles

- Worker: localhost interaction evidence only; no commit.
- Reviewer/closer: recomputes R3, combines accepted prior evidence, and decides T4 closure.
- Session-sync steward: updates continuity after reviewer decision.

## Write Ownership

Worker owns exactly the R3 matrix, R3 return, and fresh R3 evidence directory.
All Web source, prior evidence, roadmap, session, public, and runtime mutation
surfaces are forbidden.

## Dependency Release Evidence

| Dependency | Artifact | Material commit | Final disposition |
|---|---|---|---|
| R2 independent review | `docs/reviews/CVF_WEB_UX_T4_R2_BLOCKED_RETURN_REVIEW_2026-07-20.md` | N/A with reason: review and R3 dispatch share one material batch | `REVIEWED_BLOCK_ACCEPTED_R3_REQUIRED` |
| R2 responsive evidence | `docs/reviews/evidence/CVF_WEB_UX_T4_R2_LOCALHOST_2026-07-20/` | reviewer material batch pending | immutable bounded predecessor evidence |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-WEB-UX-T4-R3 --title "CVF Web UX T4 R3 Interaction Trace Repair" --date 2026-07-20 --base 64ee90665 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit Web/UI profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | added source-bound target selectors, state-delta schema, diagnostics, integrity manifest, and immutable predecessor boundary |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py` |
| docOnlyNewFields | `targetAccessibleName`; `beforeState`; `afterState`; `resultAnchor`; `computedAccentRgb`; `diagnosticDisposition` |
| claimBoundary | dispatch provenance only; no browser acceptance claim |

## Worker Autonomy / No-Question Rule

Repair allowed-scope gate failures directly. Return blocked only for a source
contradiction, unavailable rendered browser, forbidden-scope need, or missing
authority that makes completion impossible.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`web-ui-browser-audit`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "web-ui-browser-audit" --role dispatcher --lifecycle-phase pre-dispatch` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | R3 adds a local fail-closed interaction evidence contract |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | dispatch status; source verification; worker return; handoff; closure conversion |
| gateRunPurpose | confirmation and evidence only after source-fidelity authoring; not first discovery |
| claimBoundary | checker PASS authorizes evidence work only |

## Roadmap-to-Work-Order Trace Matrix

| Roadmap requirement | R3 control | Evidence required | Fail condition |
|---|---|---|---|
| non-default accent | open preferences, keyboard-select violet, retain applied token | visible panel/control plus `139 92 246` | missing visible anchor or inferred color |
| keyboard navigation | exact target identity and state delta | five target-bound scenarios | generic Tab/class trace |
| primary actions | activate real Home and journey actions | result anchors from current source | Enter without outcome evidence |
| diagnostics | classify each unique event class | terminal diagnostics ledger | raw console dump only |
| browser acceptance | reuse immutable responsive evidence | predecessor hash manifest | recapture or predecessor mutation |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| preferences opener has accessible Vietnamese name | LITERAL_INVARIANT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/CompactHeader.tsx` | lines 112-118 | `aria-label` | `CompactHeader` | ACCEPT |
| open panel exposes a close control | LITERAL_INVARIANT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/CompactHeader.tsx` | lines 172-188 | `aria-label` | `CompactHeader` | ACCEPT |
| violet control and RGB token exist | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/CompactHeader.tsx` | lines 33-39 and 220-229 | `ACCENT_OPTIONS` | `CompactHeader` | ACCEPT |
| drawer opener/closer expose accessible names | LITERAL_INVARIANT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/SidebarToggle.tsx`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/Sidebar.tsx` | opener line 11; closer line 117 | `aria-label` | `SidebarToggle`; `Sidebar` | ACCEPT |
| Home exposes `Tao PRD` outcome action | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/OutcomeQuickActions.tsx` | lines 79-109 | `onSelectTemplate` | `OutcomeQuickActions` | ACCEPT |
| Home action changes browse state to form | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app` | child route file `(dashboard)/home/page.tsx`, lines 265-290 and 582-589 | `handleOutcomeQuickAction` | `HomePage` | ACCEPT |
| Workspace advanced disclosure is a details/summary control | LITERAL_INVARIANT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app` | child route file `(dashboard)/workspace/page.tsx`, lines 167-176 | `advanced-detail` | `WorkspacePage` | ACCEPT |
| knowledge journey has a compile action | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app` | child route file `(dashboard)/governance/knowledge/page.tsx`, lines 232-258 | `handleCompile` | `KnowledgeGovernancePage` | ACCEPT |

## New Doc-Only Fields

| Field | Purpose | Claim boundary |
|---|---|---|
| `targetAccessibleName` | bind trace to the intended control | R3 browser evidence only |
| `beforeState` | retain state before activation | observed localhost DOM only |
| `afterState` | retain state after activation | observed localhost DOM only |
| `resultAnchor` | prove the action outcome visibly | sampled route only |
| `diagnosticDisposition` | classify a unique console event class | R3 session only |

## Evidence Reuse And Encoding Plan

verificationMode: REUSE_PRIOR_VERIFICATION

priorVerificationArtifact: `docs/reviews/CVF_WEB_UX_T4_R2_BLOCKED_RETURN_REVIEW_2026-07-20.md`

priorVerificationAnchor: accepted R1/R2 responsive evidence

freshRecomputeRequired: preferences capture, five keyboard traces, diagnostics,
predecessor hashes, tests, Ready/stop/listener proof

unicodePathHandling: use UTF-8-safe readers for rendered Vietnamese text

extractedTextAuthority: browser text is observed evidence; source remains authority

## Required First Reads

Read `DESIGN.md`, this packet, the R2 blocked review, target components/pages,
and worker-return checker sources before starting Web.

## Pre-Flight Checks

- require clean worktree and exact supplied execution base;
- verify R3 output paths do not exist;
- hash all R1 and R2 evidence before work;
- run pre-implementation before starting Web;
- do not load provider keys or invoke live proof.

## Execution Plan

1. Start current cvf-web on localhost:3000 and retain Ready output.
2. Use browser subagent when available; disclose Playwright fallback otherwise.
3. At 1440x900, use keyboard to open `Cai dat`, select `violet`, and retain one
   screenshot with the panel and selected swatch visibly open.
4. Record `--cvf-accent-rgb` as exactly `139 92 246`, selected control identity,
   and local persisted accent state.
5. At 767x1024, keyboard-open the drawer, focus `Close sidebar`, close it, and
   record transform/visibility state before and after.
6. On Home, keyboard-activate `Tao PRD` and prove the resulting form with its
   visible heading or field anchor.
7. On `/workspace`, keyboard-toggle the exact advanced `summary` open then
   closed and retain the `details.open` deltas.
8. On `/governance/knowledge`, enter a harmless local content fixture,
   keyboard-activate `Bien soan`, and retain the visible result or a terminal
   local diagnostic. Do not make provider/live calls.
9. Write exact capture/interaction/diagnostic/integrity/command evidence.
10. Run focused provider-free tests, file-size, worker-fast, exact manifest,
    teardown, and no-listener checks; return without staging or committing.

Text Encoding Exception: the unaccented Vietnamese target spellings in this
packet are source-locator hints. Evidence must retain the exact rendered UTF-8
accessible names observed by the browser.

## Required Browser Evidence

Create one fresh screenshot:

- `desktop-dark-preferences-violet-open.png`.

Create these machine-readable files:

- `interaction-trace.json` with exactly five named scenarios;
- `diagnostics.json` with terminal per-class dispositions;
- `predecessor-integrity.json` with R1/R2 hashes before and after;
- `commands.json` with server Ready/stop, tests, gates, git, and listener results;
- `captures.json` binding the preferences image, visible anchors, RGB, metrics,
  hash, and verdict.

Additional screenshots are allowed only when needed to prove a required result
anchor, and every such image must be listed in `captures.json`.

## Interaction Trace Schema

Each of the five scenarios must record route, viewport, ordered keys,
`targetAccessibleName`, target tag/role, stable selector, focused-before,
`beforeState`, activation key, focused-after, `afterState`, literal
`resultAnchor`, console delta, and terminal verdict. Required scenarios are:

- preferences open/select violet/close;
- 767px drawer open/focus close/close;
- Home `Tao PRD` action to form;
- Workspace advanced details open/close;
- Knowledge `Bien soan` action to result or terminal local diagnostic.

Any missing target, `NOT_FOUND`, generic class-only descriptor, unchanged state,
or absent result anchor is an immediate `BLOCKED_WITH_REASON`, never PASS.

## Allowed Scope

- `docs/reviews/CVF_WEB_UX_T4_R3_INTERACTION_ACCEPTANCE_MATRIX_2026-07-20.md`
- `docs/reviews/CVF_WEB_UX_T4_R3_WORKER_RETURN_2026-07-20.md`
- `docs/reviews/evidence/CVF_WEB_UX_T4_R3_LOCALHOST_2026-07-20/`

## Forbidden Scope

Every other path, including Web source/tests, R1/R2/T4 evidence, roadmap,
session, handoff, dependencies, scripts, lockfiles, hosted/deploy/public,
provider/live, production, and continuous-projection surfaces.

## Evidence Requirements

- exact preferences image and bound capture record;
- five semantic interaction records matching the schema;
- terminal classification for every unique console error/warning class;
- R1/R2 integrity hashes before and after;
- server Ready/stop and no-listener evidence;
- exact git manifest, unchanged HEAD, and nothing staged;
- focused provider-free checks, file-size, and worker-fast PASS.

## Verification Commands

1. pre-implementation autorun with actual execution base;
2. focused provider-free tests for header, sidebar, Home, Workspace, and knowledge;
3. `python governance/compat/check_governed_file_size.py --enforce`;
4. `python governance/compat/run_worker_return_fast_gate.py`;
5. final HEAD/status/diff/cached-diff, hashes, and port-listener checks.

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | reviewed R2 evidence and current source |
| Scope classification | semantic browser evidence repair only |
| Intake role | worker captures deterministic target/state proof |
| Reviewer role | independent reviewer recomputes and decides closure |
| Routing decision | WORKER_MUST_NOT_COMMIT |
| Public route | DEFERRED_PRIVATE_ONLY |
| canonical route mode | SINGLE_AGENT_SINGLE_ROLE |
| selected role route | R3 worker return to reviewer closure conversion |
| escalation condition | source contradiction, unavailable browser, or forbidden-path need |
| risk sensitivity | MEDIUM: final roadmap acceptance proof |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | NOT_APPLICABLE_WITH_REASON: no outside artifact promoted |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | R3 evidence and independent review |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | no external authority or hosted equivalence claim |

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

## Agent Handoff Contract Control Block

| Field | Value |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | delegated browser-evidence worker to independent reviewer/closer |
| phase | implementation |
| baseHeadFor(phase) | dispatchBaseHead=64ee90665; executionBaseHead=OPERATOR_PROVIDED_FINAL_SESSION_SYNC_HEAD; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | exact new R3 Allowed Scope |
| traceScope(phase, actor) | process, browser, targets, state deltas, image, hashes, diagnostics, tests, gates, return |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | predecessor evidence immutable; source and mutation lanes parked |
| nextMoveSurfaces | reviewer decides T4/roadmap closure and session steward updates continuity |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_WEB_UX_T4_COMPLETION_2026-07-20.md` |
| reviewerOwnedClosurePaths | final T4 completion review; active UX roadmap; material commit |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |
| conversionRule | reviewer recomputes R3 and combines only accepted predecessor evidence |
| failureRoute | truthful block; source repair needs a separate packet |

## Worker Output Checker Read-Ahead Mandate

Before writing the matrix or return, read checker source for the path and
document type. Derive exact headings, trace fields, claim boundary, no-commit
evidence, and machine closure shape before content authoring.

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| R3 interaction matrix | create with five terminal scenario rows |
| R3 worker return | create full-gate packet with actual command evidence |
| R3 evidence directory | create exact fresh JSON/image manifest |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_WEB_UX_T4_R3_WORKER_RETURN_2026-07-20.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Web/UI Claim Boundary

| Field | Value |
|---|---|
| DESIGN.md read | required before browser execution |
| UI claim boundary | current-source localhost interaction evidence only; no hosted or production-readiness claim |

## Agent Operation Trace Block

| Field | Required worker evidence |
|---|---|
| Actor | delegated R3 browser-evidence worker |
| Provider or surface | current-source localhost browser |
| Agent type | evidence worker |
| Session or invocation | R3 worker session |
| Invocation ID | actual identifier or N/A with reason |
| Working directory | repository root and cvf-web package |
| Command or tool surface | git, Next, browser automation, hashes, tests, gates |
| Intent | close semantic interaction evidence gaps |
| Inputs | R3 order, R2 review, DESIGN.md, target source |
| Target paths | exact R3 Allowed Scope |
| Allowed scope source | this work order |
| Expected manifest | matrix, return, evidence directory |
| Before status evidence | clean worktree and supplied HEAD |
| Actions | start, focus, activate, assert, capture, verify, stop |
| Outputs | R3 semantic interaction evidence |
| Evidence | JSON, PNG, visible anchors, states, diagnostics, commands |
| After status evidence | exact status, unchanged HEAD, no listeners |
| Actual changed set | exact final manifest |
| Manifest delta | NONE or explained allowed subset |
| Deletion or rename disposition | N/A with reason: none authorized |
| Approval boundary | no source, predecessor, session, commit, hosted, public, provider, or production authority |
| Diff evidence | git status, diff, cached diff, and HEAD before/after |
| Claim boundary | current-source localhost R3 evidence only |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | deterministic localhost interaction evidence |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT - no provider receipt authorized |
| actionEvidence | ACTION_EVIDENCE_PRESENT through target-bound browser interactions only |
| invocationBoundary | local Next and provider-free browser/test process |
| interceptionBoundary | no provider, hosted, production, or external-service interception |
| claimLanguage | R3 records only directly observed current-source states |
| forbiddenExpansion | source repair, hosted freshness, live governance, deploy, public, provider, production |

## Foundation Storage Layout Block

NOT_APPLICABLE_WITH_REASON: R3 creates only a fresh review-evidence directory;
it creates no foundation, registry, durable runtime store, or generated aggregate.

## Acceptance Criteria

- [ ] Preferences screenshot visibly shows the open panel and selected violet control.
- [ ] Computed accent token equals `139 92 246` and persisted state is retained.
- [ ] Five target-bound keyboard scenarios have real before/after state deltas.
- [ ] Every result anchor is literal, visible, and not `NOT_FOUND`.
- [ ] Console errors and warnings are terminally classified.
- [ ] R1/R2 evidence hashes remain unchanged.
- [ ] Server Ready, stop, and no-listener evidence are retained.
- [ ] Only exact R3 Allowed Scope changes; nothing staged; HEAD unchanged.
- [ ] Focused checks, file-size, and worker-fast pass.

## Review Gate

Reviewer inspects the preferences image at original resolution, recomputes all
hashes and state records, verifies all five target identities/results against
source, checks diagnostics/integrity/commands, and reruns reviewer/pre-closure
gates before any T4 or roadmap closure.

## Closure Checklist

- [ ] Preferences and accent proof terminal.
- [ ] Five keyboard paths terminal.
- [ ] Diagnostics and predecessor integrity terminal.
- [ ] Exact scope and teardown proven.
- [ ] Reviewer decision recorded.
- [ ] Roadmap closure state reconciled only if accepted.

## Return-To-Orchestrator Conditions

Return blocked for unavailable browser state, missing accessible target,
unchanged interaction state, missing result anchor, failing gate, listener
residue, predecessor drift, or forbidden-path need.

## Operator Checkpoint

No checkpoint is needed for evidence-only execution. Source, hosted, deploy,
public, provider, or production action requires new authorization.

## Current Runtime Freshness Verification

| Surface | Verification | Required disposition |
|---|---|---|
| current Web source | exact worker HEAD and localhost start | PASS or BLOCKED |
| target semantics | source lines plus rendered states | PASS or BLOCKED |
| predecessor evidence | before/after hash manifest | PASS or BLOCKED |
| hosted runtime | not invoked | N/A with reason |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | dispatch-ready | PASS |
| Completion or reviewer artifact | reviewer-owned completion review | pending R3 review | N/A with reason |
| Roadmap state | active UX roadmap | T4-R3 dispatch-ready | PASS |
| Registry JSON | corpus aggregate | no mutation authorized | N/A with reason |
| Registry Markdown | paired registry | no mutation authorized | N/A with reason |
| External evidence digest | R3 hashes and predecessor integrity | worker to create | N/A with reason |
| System loop interlock | no loop mutation | evidence-only packet | N/A with reason |
| Session continuity | final session-sync HEAD | operator supplies | PASS |

## Acceptance Receipt Assertion Matrix

| Query ID | Receipt artifact | JSON path | Required value | Observed value | Status |
|---|---|---|---|---|---|
| R3-AR-01 | R3 `captures.json` | preferences capture | visible open panel and violet token | pending worker | N/A with reason |
| R3-AR-02 | R3 `interaction-trace.json` | five scenarios | target identity and state delta | pending worker | N/A with reason |
| R3-AR-03 | R3 `diagnostics.json` | unique classes | terminal dispositions | pending worker | N/A with reason |
| R3-AR-04 | R3 `predecessor-integrity.json` | R1/R2 hashes | unchanged before/after | pending worker | N/A with reason |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: R3 is private localhost acceptance evidence. Hosted, deploy, and public
lanes remain outside this packet.

## Claim Boundary

This packet authorizes only fresh R3 current-source localhost interaction
evidence. It does not authorize Web source mutation, hosted equivalence,
deployment, public export, provider/live calls, production action, or closure.
