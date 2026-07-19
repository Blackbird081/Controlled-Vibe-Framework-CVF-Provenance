# CVF Agent Work Order - CVF Web UX T4 R1 Browser Evidence Repair

Memory class: governed-worker-dispatch

Status: REVIEWED_BLOCK_ACCEPTED_R2_REQUIRED

Batch ID: CVF-WEB-UX-T4-R1

Dispatch base head: `a8df6b90d`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: delegated browser-evidence worker

Reviewer/closer: independent reviewer/closer

Worker return path: `docs/reviews/CVF_WEB_UX_T4_R1_WORKER_RETURN_2026-07-19.md`

## Dispatch Prompt Envelope

Role: replace incomplete T4 acceptance proof with a fresh, machine-bound
current-source localhost browser evidence set.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_WEB_UX_T4_R1_BROWSER_EVIDENCE_REPAIR_2026-07-19.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: require the operator-provided final packet/session-sync HEAD before any action.

Current-time notes: the first T4 return is reviewed blocked, not product-failed.
Its evidence remains immutable. R1 writes only a new matrix, return, and
evidence root.

Do-not-misread notes: start current Web and use a real rendered browser. Never
copy or overwrite the first T4 images. A filename, expected-label phrase, or
summary focus claim is not evidence.

Required first actions: confirm clean worktree and supplied HEAD; read startup
surfaces, guard orientation, literal gotchas, `DESIGN.md`, original T4 packet,
blocked review, this order, and checker sources; run pre-implementation before
starting Web.

Return contract: produce twelve fresh captures plus JSON trace, prove unique
interaction states, stop all processes, leave only exact Allowed Scope, and
return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Close the narrow evidence defects that prevented T4 acceptance: duplicated
tablet interaction evidence, descriptive rather than literal anchors, absent
row-to-image binding, and unsupported keyboard/focus summaries.

## Authority Chain

Operator continuation instruction -> active UX roadmap -> first T4 work order
-> reviewed blocked return -> this R1 evidence-only work order.

## Agent Roles

- Worker: browser evidence repair only; no source mutation or commit.
- Reviewer/closer: recomputes images, traces, hashes, and roadmap disposition.
- Session-sync steward: updates protected continuity only after acceptance.

## Write Ownership

Worker owns exactly the new R1 matrix, R1 evidence directory, and R1 worker
return. Prior evidence, source, tests, roadmap, session state, deployment, and
public surfaces are forbidden.

## Dependency Release Evidence

| Dependency | Artifact | Material commit | Final disposition |
|---|---|---|---|
| first T4 blocked review | `docs/reviews/CVF_WEB_UX_T4_BLOCKED_RETURN_REVIEW_2026-07-19.md` | N/A with reason: reviewer block and R1 packet are committed in one material dispatch batch | `REVIEWED_BLOCK_ACCEPTED_R1_REQUIRED` |
| T4 execution-mode reconciliation | active handoff/session surfaces | `a8df6b90d` | session mode compatible before R1 packet authoring |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-WEB-UX-T4-R1 --title "CVF Web UX T4 R1 Browser Evidence Repair" --date 2026-07-19 --base a8df6b90d --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus read-only browser-evidence repair profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | added exact blocked findings, new evidence root, per-row hash/anchor/focus schema, and no-overwrite boundary |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_dispatch_scaffold_provenance.py` |
| docOnlyNewFields | R1 capture trace fields below |
| claimBoundary | packet provenance only; no browser acceptance claim |

## Worker Autonomy / No-Question Rule

Repair only R1 audit artifacts and capture process. Do not repair Web source or
protected continuity. Return blocked before unauthorized edits if the current
source cannot generate truthful evidence.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`web-ui-browser-audit`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "web-ui-browser-audit" --role dispatcher --lifecycle-phase pre-dispatch` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | explicit hash uniqueness, literal anchors, screenshot binding, and focus trace added from blocked review |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | dispatch status; dependency rows; Source Verification; New Doc-Only Fields; handoff route; worker-return shape |
| gateRunPurpose | confirm R1 dispatch shape after blocked-evidence review |
| claimBoundary | machine compliance confirms packet shape only |

## Roadmap-to-Work-Order Trace Matrix

| Roadmap requirement | R1 repair | Evidence required | Fail condition |
|---|---|---|---|
| viewport/theme/accent matrix | recapture all twelve named states fresh | twelve PNGs and twelve trace records | any copied, missing, or stale image |
| route identity | capture browser URL after navigation | exact localhost URL per record | URL inferred from filename |
| visible identity | query a rendered locator and store its normalized text | non-empty literal `visibleAnchorText` | expected-description phrase only |
| interaction identity | store action plus before/after state | trace for sidebar, advanced details, preferences, focus | interaction asserted without state delta |
| screenshot binding | store repository-relative image path and SHA-256 | path exists and hash recomputes | missing or mismatched binding |
| keyboard usability | retain key sequence and active-element descriptors | focus trace for required controls | summary phrase without trace |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| first T4 matrix is blocked on duplicate interaction proof | LITERAL_INVARIANT | `docs/reviews/CVF_WEB_UX_T4_BROWSER_ACCEPTANCE_MATRIX_2026-07-19.md` | Findings and tablet sidebar row | `BLOCKED_DUPLICATE_EVIDENCE` | first T4 matrix | ACCEPT |
| reviewer requires R1 | LITERAL_INVARIANT | `docs/reviews/CVF_WEB_UX_T4_BLOCKED_RETURN_REVIEW_2026-07-19.md` | Decision / Disposition | `REVIEWED_BLOCK_ACCEPTED_R1_REQUIRED` | T4 reviewer | ACCEPT |
| original evidence root is preserved | EXISTS | `docs/reviews/evidence/CVF_WEB_UX_T4_LOCALHOST_2026-07-19/captures.json` | capture records | `desktop-dark-home` | first T4 evidence | ACCEPT |
| original T4 work order defines twelve states | LITERAL_INVARIANT | `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_WEB_UX_T4_BROWSER_ACCEPTANCE_AND_ROADMAP_CLOSURE_2026-07-19.md` | Browser Acceptance Matrix | `desktop-dark-home`; `mobile-accent-transfer` | T4 dispatch | ACCEPT |
| browser presentation contract remains canonical | LITERAL_INVARIANT | canonical contract: `DESIGN.md` | sections 4, 7, 8, 9, 14.6 | responsive priority; visible focus; progressive disclosure | CVF design contract | ACCEPT |

## New Doc-Only Fields

| Field | Purpose | Claim boundary |
|---|---|---|
| `screenshotPath` | bind record to durable PNG | R1 repository-local evidence only |
| `sha256` | prove exact image identity | no semantic correctness by hash alone |
| `visibleAnchorSelector` | disclose rendered locator | selector is evidence method, not authority |
| `visibleAnchorText` | store literal normalized rendered text | current-source localhost only |
| `interactionTrace` | store action and visible/state result | no source behavior beyond observed state |
| `focusTrace` | store keys and active-element before/after descriptors | sampled keyboard path only |

## Required First Reads

Read `DESIGN.md`, original T4 work order, blocked review, original matrix,
this order, worker-return/checker sources, and browser instructions available
to the worker before starting the server.

## Pre-Flight Checks

- require clean worktree and exact supplied `executionBaseHead`;
- run pre-implementation before starting Web;
- never edit protected continuity to repair a gate; return blocked instead;
- verify the new R1 evidence directory is absent;
- verify original T4 evidence hashes before work and do not overwrite them;
- load no provider key and invoke no live/provider proof.

## Execution Plan

1. Start current-source Next Web on localhost:3000 and wait for Ready.
2. Use browser subagent when available; otherwise use Playwright and disclose the fallback.
3. Capture all twelve states into the new R1 evidence root.
4. For every state, record exact URL, literal visible anchor selector/text, width metrics, screenshot path/hash, diagnostics, and verdict.
5. For interaction states, record before/action/after evidence and confirm distinct hashes.
6. Record keyboard keys plus active-element descriptors for required controls.
7. Write the R1 matrix and worker return in full checker shape.
8. Run provider-free focused tests, file-size, worker-fast, exact manifest, and teardown checks.
9. Stop all processes started by R1 and return without staging or committing.

## Required Browser States

Recapture the same twelve IDs from the original T4 work order. All twelve PNG
hashes must be unique unless a record explicitly proves why two distinct
required states can render the same pixels; the tablet Home/sidebar pair may
not share a hash because sidebar-open is a required visible delta.

Required interaction trace rows:

- desktop Workspace ordinary -> advanced details open -> closed;
- tablet Home -> sidebar open -> closed;
- mobile Home -> sidebar open -> closed;
- Home preferences open, theme/accent selection visible, then closed;
- keyboard focus through preferences, sidebar, primary Home action, Workspace
  details, and one journey action using Tab/Shift+Tab/Enter/Escape.

## Allowed Scope

- `docs/reviews/CVF_WEB_UX_T4_R1_BROWSER_ACCEPTANCE_MATRIX_2026-07-19.md`
- `docs/reviews/CVF_WEB_UX_T4_R1_WORKER_RETURN_2026-07-19.md`
- `docs/reviews/evidence/CVF_WEB_UX_T4_R1_LOCALHOST_2026-07-19/`

## Forbidden Scope

Every other path, especially original T4 outputs/evidence, Web source/tests,
dependencies, scripts, temp capture script, lockfiles, session state, handoff,
roadmap, hosted/deploy/public/provider/live/production/projection surfaces.

## Evidence Requirements

- twelve fresh PNGs plus `captures.json` and `console.json` in R1 evidence;
- one terminal record per state with exact URL, literal anchor selector/text,
  dimensions, document/body widths, screenshot path/hash, diagnostics, verdict;
- explicit interaction and focus traces with before/after state;
- hash uniqueness report and original-evidence non-mutation hash check;
- server start/Ready/stop and no-listener evidence;
- exact git manifest, nothing staged, unchanged worker HEAD;
- provider-free focused checks, file-size, and worker-fast PASS.

## Verification Commands

1. repository root: pre-implementation autorun using the actual execution base;
2. cvf-web package: provider-free focused tests for Home, Workspace, sidebar, header, and journey;
3. repository root: `python governance/compat/check_governed_file_size.py --enforce`;
4. repository root: `python governance/compat/run_worker_return_fast_gate.py`;
5. final git HEAD/status/diff/cached-diff, SHA-256, and port listener checks.

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | reviewed blocked T4 evidence plus current source |
| Scope classification | browser evidence repair only |
| Intake role | worker creates fresh bound evidence |
| Reviewer role | independent reviewer recomputes and decides T4/roadmap closure |
| Routing decision | `WORKER_MUST_NOT_COMMIT` |
| Public route | `DEFERRED_PRIVATE_ONLY` |
| canonical route mode | `SINGLE_AGENT_SINGLE_ROLE` |
| selected role route | R1 worker return to reviewer closure conversion |
| escalation condition | protected-path need, source defect, unavailable real browser, or non-terminal required state |
| risk sensitivity | MEDIUM: final roadmap acceptance proof |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | NOT_APPLICABLE_WITH_REASON: no outside artifact is promoted |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | R1 evidence and independent completion review |
| Disposition | NOT_APPLICABLE_WITH_REASON: current source and local browser control |
| Claim boundary | no external authority or hosted equivalence proof |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | delegated browser-evidence worker to independent reviewer/closer |
| phase | implementation |
| baseHeadFor(phase) | dispatchBaseHead=a8df6b90d; executionBaseHead=OPERATOR_PROVIDED_FINAL_SESSION_SYNC_HEAD; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | exact new R1 Allowed Scope |
| traceScope(phase, actor) | process, browser, images, hashes, anchors, interactions, focus, diagnostics, commands, return |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | original evidence immutable; source and all mutation lanes parked |
| nextMoveSurfaces | reviewer decides T4/roadmap closure; session steward updates continuity |

## Dual Agent Surface Matrix

| Surface | Interface | Authority / risk boundary | Required evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | repository/browser worker | exact new R1 outputs; no source or commit | fresh bound browser evidence | current filesystem and browser tooling | REPAIR_EVIDENCE_ONLY |
| EXTERNAL_AGENT_CLI_MCP | external browser worker | same packet and no-commit boundary | same trace and image schema | operator-provided browser/CLI adapter only | CONTRACT_ONLY |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_WEB_UX_T4_COMPLETION_2026-07-19.md` |
| reviewerOwnedClosurePaths | T4 completion review; active UX roadmap; material commit |
| conversionRule | R1 `COMPLETE_PENDING_REVIEW` is not closure; reviewer recomputes hashes, images, representative browser states when available, traces, diagnostics, and scope |
| failureRoute | truthful R1 block remains open; source repair needs a separate packet |

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The return must contain every full-gate heading and scalar token, exact base,
browser trace summary, image/hash/anchor evidence, diagnostics, teardown,
conditional-control N/A blocks in checker shape, retrospective, actual changed
set, no-commit evidence, and Machine Closure Package.

## Agent Operation Trace Block

| Field | Required worker evidence |
|---|---|
| Actor | delegated browser-evidence worker |
| Provider or surface | current-source localhost rendered browser |
| Agent type | audit repair worker |
| Session or invocation | T4-R1 worker session |
| Invocation ID | worker records identifier or N/A with reason |
| Working directory | repository root and cvf-web package |
| Command or tool surface | git, Next dev, browser automation, hashing, provider-free tests, gates |
| Intent | repair final browser acceptance evidence |
| Inputs | R1 order, blocked review, DESIGN.md, current source |
| Target paths | exact R1 Allowed Scope |
| Allowed scope source | this work order |
| Expected manifest | R1 matrix, R1 return, R1 evidence directory |
| Before status evidence | clean worktree and supplied HEAD |
| Actions | start, interact, capture, hash, classify, verify, stop |
| Outputs | fresh trace-bound evidence and return |
| Evidence | JSON, PNGs, literal anchors, interactions, focus, metrics, diagnostics, commands |
| After status evidence | exact status, cached state, HEAD, original evidence hashes, port listeners |
| Actual changed set | exact final manifest |
| Manifest delta | NONE or explained allowed subset |
| Deletion or rename disposition | N/A with reason: no deletion, rename, or overwrite authorized |
| Approval boundary | no source, original evidence, session, commit, hosted, deploy, public, provider, or production authority |
| Diff evidence | `git diff --name-status`; cached diff; HEAD before/after |
| Claim boundary | current-source localhost R1 browser evidence only |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | deterministic current-source localhost browser evidence repair |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT - no provider or governed execution receipt authorized |
| actionEvidence | ACTION_EVIDENCE_PRESENT through trace-bound browser interactions and images |
| invocationBoundary | local Next and provider-free browser/test process only |
| interceptionBoundary | no provider, hosted, production, or external-service interception |
| claimLanguage | R1 records exact states observed on current-source localhost |
| forbiddenExpansion | source repair, hosted freshness, live governance, deploy, public, provider, production |

## Foundation Storage Layout Block

NOT_APPLICABLE_WITH_REASON: R1 writes a new evidence folder in the existing
reviews tree and creates no durable foundation, registry, or aggregate.

## Acceptance Criteria

- [ ] Exactly twelve fresh required PNGs exist in the R1 evidence root.
- [ ] Every record binds exact URL, literal visible text, path, and recomputed hash.
- [ ] Tablet Home and sidebar-open captures are visibly and hash-distinct.
- [ ] Interaction traces prove advanced details, sidebar, and preferences deltas.
- [ ] Focus traces record keys and active-element before/after descriptors.
- [ ] Width and diagnostic fields are terminal for every state.
- [ ] Original T4 evidence hashes are unchanged.
- [ ] Server/browser teardown and no-listener checks pass.
- [ ] Exactly R1 Allowed Scope changed; nothing staged; HEAD unchanged.
- [ ] Provider-free focused checks, file-size, and worker-fast pass.

## Review Gate

Reviewer must inspect all original-resolution R1 images, recompute hashes,
compare trace records to files, check literal anchors and interactions, inspect
diagnostics, verify original evidence unchanged, and reproduce representative
states if a browser backend is available. Any mismatch blocks closure.

## Closure Checklist

- [ ] Every R1 acceptance item is independently recomputed.
- [ ] Closure Diff Gate reconciles roadmap, both T4 packets, images, traces, and claims.
- [ ] T4 and roadmap close only after accepted R1 evidence.
- [ ] Material commit contains no protected session-sync path.
- [ ] Hosted/deploy/public/provider/production/projection lanes remain parked.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only after every required R1 row and trace is
terminal. Return `BLOCKED_WITH_REASON` before unauthorized edits when browser,
source, protected-path, or evidence-state conditions prevent truthful proof.

## Operator Checkpoint

No mid-worker preference checkpoint is required. Roadmap closure remains
reviewer-owned. All hosted/deploy/public/provider/production/projection lanes
remain separately parked.

## Current Runtime Freshness Verification

| Claim | Current evidence | Freshness disposition |
|---|---|---|
| first T4 evidence blocked | reviewed matrix and block review in this material batch | VERIFIED_CURRENT |
| session mode compatible | session repair `a8df6b90d` | VERIFIED_CURRENT |
| source repair not required by evidence defect | block review decision | VERIFIED_CURRENT |
| original evidence preservation required | distinct original and R1 evidence roots | VERIFIED_CURRENT |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this work order | `DISPATCH_READY` | PASS |
| Completion or reviewer artifact | future T4 completion review | N/A with reason: R1 not started | N/A with reason |
| Roadmap state | active UX roadmap | T4-R1 dispatch-ready | PASS |
| Registry JSON | corpus registry aggregate | current drift check | PASS |
| Registry Markdown | paired registry surface | no mutation unless coverage gate reports a gap | PASS |
| External evidence digest | future R1 evidence | N/A with reason: repository-local evidence produced during R1 | N/A with reason |
| System loop interlock | no system-loop mutation | N/A with reason: evidence repair only | N/A with reason |
| Session continuity | compatible at `a8df6b90d` | PASS | PASS |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Dispatch receipt | source-verified R1 packet | this packet plus reviewed block | PASS |
| Browser receipt | fresh R1 trace and images | N/A with reason: R1 not started | N/A with reason |
| Provider receipt | none | N/A with reason: provider/live forbidden | N/A with reason |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: T4 remains private and open pending R1 evidence acceptance.

## Claim Boundary

This packet authorizes fresh R1 browser evidence only. It does not authorize
source changes, prior-evidence mutation, roadmap closure, hosted deployment,
public sync, provider/live calls, production, or projection execution.
