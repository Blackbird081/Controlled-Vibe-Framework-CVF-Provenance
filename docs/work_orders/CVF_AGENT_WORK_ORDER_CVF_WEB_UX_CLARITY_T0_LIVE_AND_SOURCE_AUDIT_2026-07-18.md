# CVF Agent Work Order - CVF Web UX Clarity T0 Live And Source Audit

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: CVF-WEB-UX-T0

Dispatch base head: `7051eb87d`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: delegated audit worker

Reviewer/closer: independent reviewer/closer

Worker return path: `docs/reviews/CVF_WEB_UX_CLARITY_T0_WORKER_RETURN_2026-07-18.md`

## Dispatch Prompt Envelope

Role: independent UX, information-architecture, and plain-language audit worker.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_WEB_UX_CLARITY_T0_LIVE_AND_SOURCE_AUDIT_2026-07-18.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: capture `git rev-parse --short HEAD` before any write and
require it to equal the committed dispatch/session-sync HEAD named in the
operator prompt.

Current-time notes: audit public site state visible on 2026-07-18; record the
actual observation timestamp and do not claim hosted freshness beyond it.

Do-not-misread notes: this is an audit, not a redesign implementation. Do not
submit forms, trigger AI/provider actions, mutate production, edit source,
change data, commit, push, or deploy.

Required first actions: read `AGENTS.md`, session front doors, active handoff,
Guard Orientation, literal gotchas, `DESIGN.md`, paired GC-018 baseline, this
packet, and checker source applicable to both worker-owned outputs.

Return contract: create exactly the two authorized review outputs, run the
required gates, leave them uncommitted, and return `COMPLETE_PENDING_REVIEW` or
`BLOCKED_WITH_REASON`.

## Purpose

Audit why the current public CVF Web is difficult for a non-technical operator
to understand. Produce an evidence-backed route inventory and redesign backlog
that separates user jobs from internal governance machinery and establishes a
coherent Vietnamese-first information architecture.

## Authority Chain

Operator instruction -> `AGENTS.md` -> active session front doors -> paired
GC-018 baseline -> this work order -> `DESIGN.md` and source-verified Web files.
Provider-local memory and chat summaries are not claim authority.

## Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Operator | human operator | authorizes audit scope and later checkpoints |
| Dispatcher | dispatch steward | source-verifies and dispatches packet |
| Worker | delegated audit worker | performs live/source audit and creates two uncommitted outputs |
| Reviewer/closer | independent review lane | recomputes evidence, repairs bounded output defects, and owns commit |

## Required First Reads

1. `AGENTS.md` and active session front doors.
2. Guard Orientation and governed literal-format gotchas.
3. Paired GC-018 baseline and this work order.
4. `DESIGN.md`.
5. Every source in Source Verification.
6. Output-specific checker sources before writing either review file.

## Pre-Flight Checks

- Confirm HEAD equals the committed dispatch/session-sync HEAD named in the
  operator prompt and capture it as executionBaseHead.
- Confirm the worktree is clean before worker execution.
- Confirm both allowed output paths do not exist.
- Run the pre-implementation autorun gate before the first write.
- Confirm live browsing remains read-only and requires no credential entry.

## Write Ownership

Worker owns exactly the two new review outputs in the fulfillment manifest and
must not stage or commit them. Reviewer/closer owns any bounded repair and the
material commit. Session-sync remains separately owned.

## Target / Source

- Live site: `https://cvfcoding.vn`.
- Required routes: `/home`, `/workspace`, `/help`, `/governance/knowledge`,
  `/knowledge/intake`, `/artifacts`, and `/work-transfer`.
- Shared surfaces: sidebar and top header.
- Canonical visual/language authority: `DESIGN.md`.
- Source ownership: only the files and symbols listed in Source Verification.

## Scope / Methodology

1. Inspect each required route read-only at desktop width. Inspect mobile or
   tablet only if the browser supports it without changing production state.
2. Capture secret-safe screenshots or precise visible-text observations.
3. Identify the presumed user, primary job, primary action, vocabulary burden,
   stale/missing state, hierarchy defects, and navigation overlap per route.
4. Trace each material finding to current source; do not infer an endpoint,
   field, or runtime behavior from appearance alone.
5. Produce a proposed navigation tree with at most five primary user-facing
   groups. Internal/operator diagnostics must be separated from ordinary
   product workflows.
6. Produce a Vietnamese-first terminology table: current label, problem,
   recommended label, English equivalent, and keep/hide/admin-only decision.
7. Classify every finding as `P0_BROKEN_TRUTH`, `P1_TASK_BLOCKING`,
   `P2_HIGH_COGNITIVE_LOAD`, or `P3_POLISH`.
8. Map remediation into later tranches without editing implementation.

## Execution Plan

| Step | Action | Output |
|---|---|---|
| 1 | Capture base/status and inspect required sources/checkers. | pre-flight evidence |
| 2 | Audit live routes and global chrome read-only. | route observations |
| 3 | Reconcile observations with source and DESIGN. | terminal audit matrix |
| 4 | Design bounded IA, terminology, and priority recommendations. | audit companion |
| 5 | Run gates and capture exact changed set/no-commit state. | worker return |

## Findings / Position

The worker must test, not merely repeat, these initial hypotheses:

- the sidebar exposes too many peer-level concepts and mixes languages;
- `/workspace` exposes internal continuity/dispatch vocabulary and stale source
  fallbacks to ordinary users;
- help content explains implementation names rather than user outcomes;
- governance, knowledge intake, review export, and work transfer are presented
  as separate concepts without one understandable end-to-end workflow;
- large cards, repeated explanatory prose, and weak primary-action hierarchy
  increase scanning cost;
- version, Tweaks, admin, and language controls dominate the global chrome.

Each hypothesis must resolve as CONFIRMED, PARTIAL, REJECTED, or
BLOCKED_EVIDENCE with route and source evidence.

## Risk / Corrective Action

| Risk | Required control |
|---|---|
| Audit becomes subjective visual opinion | Tie every material finding to a user job, visible evidence, DESIGN rule, and source owner. |
| Internal governance truth is removed blindly | Recommend hide, translate, progressive-disclose, or admin-only before deletion. |
| Vietnamese copy becomes literal translation | Prefer short natural Vietnamese and preserve an English equivalent table. |
| Worker changes production while exploring | Read-only navigation only; no form submission or provider action. |
| Audit turns into implementation | Stop at prioritized backlog and tranche map. |

## Evidence Requirements

- Observation timestamp and route URL for every live row.
- Secret-safe screenshot reference or exact visible-text note.
- Current source path and owner symbol for every P0/P1 finding.
- DESIGN section for every reusable visual/language judgment.
- Explicit browser limitation and fallback evidence if a route cannot be read.
- Command-backed HEAD, staged state, and exact two-file changed set.

## Review Gate

Reviewer must independently sample every P0/P1 row, recompute the `/workspace`
stale-state diagnosis from source, verify the proposed IA does not hide required
review/admin controls without a route, and reject implementation claims.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id CVF-WEB-UX-T0 --title "CVF Web UX Clarity And Information Architecture Live Audit" --date 2026-07-18 --base 7051eb87d --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | web-ui-dashboard plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Added live/source audit methodology, route matrix, hypotheses, language taxonomy, exact two-file scope, and no-interaction safety boundary. |
| checkerReadAheadConfirmation | Applicable dispatch, ADIF, trace, handoff, lifecycle, structural, and authority checkers inspected before authoring. |
| docOnlyNewFields | Severity and redesign-disposition values are audit-only fields. |
| claimBoundary | Dispatch authoring evidence only; no redesign or hosted-quality claim. |

## Worker Autonomy / No-Question Rule

Repair allowed-output checker failures by reading checker source. Return to the
orchestrator only for live-site inaccessibility, source contradiction,
forbidden-scope need, or missing authority that prevents a truthful audit.

## Intake Role Routing Decision

Intake summary: operator request for a live/source audit of confusing Web UI.

Scope classification: bounded documentation-only audit with exactly two worker
output paths.

Risk sensitivity: public hosted observation, but no provider, secret,
production mutation, or public-sync write.

Selected role route: multi-agent multi-role execution model.

Role separation basis: delegated worker gathers evidence; independent reviewer
recomputes and owns closure.

Escalation condition: stop and return blocked at inaccessible live evidence,
source contradiction, forbidden-scope need, or operator checkpoint.

| Field | Value |
|---|---|
| intakeClass | OPERATOR_DIRECTED_INTERNAL_WEB_AUDIT |
| workerRoute | delegated audit worker |
| reviewerRoute | independent reviewer/closer |
| providerMemoryAuthority | NOT_CVF_SOURCE |
| decision | MULTI_AGENT_MULTI_ROLE audit chain |

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator observation to source-verified independent audit, then reviewer-owned acceptance or rejection |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; pre-dispatch and reviewer gates |
| Owner surface | CVF-WEB-UX-T0 audit packet and its two worker outputs |
| Disposition | ADAPT as bounded evidence input; independently verify every source or live-route claim |
| Claim boundary | screenshots and operator critique are audit inputs, not canonical CVF authority or implementation authorization |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: ADIF-0001, ADIF-0002, ADIF-0007, ADIF-0014, ADIF-0015,
ADIF-0020, ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033.

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 10 |
| Returned defects | ADIF-0001, ADIF-0002, ADIF-0007, ADIF-0014, ADIF-0015, ADIF-0020, ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033 |
| Disclosed defectIds | ADIF-0001, ADIF-0002, ADIF-0007, ADIF-0014, ADIF-0015, ADIF-0020, ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033 |
| Dispatch impact | DESIGN-first audit, source-backed findings, no mutation, and exact no-commit return scope. |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_packet_authority_and_encoding.py` |
| literalTokensReviewed | Dispatch Prompt Envelope, Source Verification Block, Agent Handoff Contract Control Block, Reviewer Closure Conversion, Worker Return Packet Shape Contract, Agent Operation Trace Block, Delta Execution Claim Boundary Control Block, Public Export Disposition |
| gateRunPurpose | Confirm source fidelity and packet shape before dispatch. |
| claimBoundary | Worker must independently read output-specific checkers before authoring review files. |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Vietnamese natural-language rule | LITERAL_INVARIANT | canonical-contract:DESIGN.md | Section 8 | Vietnamese UI language rules | CVF design contract | ACCEPT |
| Shared navigation labels and language footer | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/Sidebar.tsx` | symbol definition line 48; navigation lines 153-176 | `Sidebar` | dashboard navigation | ACCEPT |
| Workspace V19/WWU-T2 fallback values | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/cvf-workspace-read-model.ts` | symbol definition line 261; values lines 267-278 | `getCvfWorkspaceReadModel` | workspace server read model | ACCEPT |
| Help feature terminology | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/data/help-content.ts` | symbol definition line 41 | `HELP_CONTENT` | help data model | ACCEPT |
| Artifact review-export surface | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | symbol definition line 208 | `ArtifactExportPanel` | artifact export panel | ACCEPT |
| Header Tweaks/language controls | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/CompactHeader.tsx` | symbol definition line 65 | `CompactHeader` | shared compact header | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| Planned path existence | All four paths returned false before authoring. | NEW_PATHS_CONFIRMED |
| Batch token search | Exact batch/title search returned no prior artifact. | NO_COLLISION |
| Collision decision | New audit-only batch; prior inheritance roadmap remains historical evidence, not this audit output. | ACCEPT |

## Evidence Reuse And Encoding Plan

verificationMode: FRESH_RECOMPUTE

priorVerificationArtifact: N/A with reason: operator screenshots are reference
input but no prior route-by-route UX audit covers the current public surface.

priorVerificationAnchor: N/A with reason: fresh live observation required.

freshRecomputeRequired: YES

unicodePathHandling: use literal repository paths and UTF-8-safe readers; do
not normalize or rename source paths.

extractedTextAuthority: visible browser text is observation evidence; current
source and DESIGN are authority for implementation and design claims.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | delegated audit worker; independent reviewer/closer |
| phase | worker execution, reviewer return, material close, session sync |
| baseHeadFor(phase) | dispatchBaseHead=7051eb87d; executionBaseHead=committed dispatch/session-sync HEAD from operator prompt; closureBaseHead=reviewer capture |
| changedSetScope(phase) | worker may create exactly two review outputs; reviewer owns repair/closure only within those paths |
| traceScope(phase, actor) | worker records live/source audit and no-commit evidence; reviewer recomputes route/source findings |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer/closer owns material commit |
| crossBatchIsolation | Clean worktree at dispatch base `7051eb87d`; no edits to current source, public-sync, roadmap, session, generated aggregates, or unrelated reviews. |
| nextMoveSurfaces | Reviewer/session-sync steward updates next-move surfaces only if this audit is accepted and a redesign roadmap is released. |
| Before status evidence | Worktree was clean at dispatch base `7051eb87d` before the two dispatch artifacts were authored. |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_WEB_UX_CLARITY_T0_COMPLETION_2026-07-18.md` |
| reviewerOwnedClosurePaths | the two worker output paths plus the conventional completion path only if independent closure cannot be recorded safely in the worker return |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Output Checker Read-Ahead Mandate

Before writing either output, derive exact required headings, tables, trace
labels, corpus/value/rescan dispositions, and no-commit evidence from the
current worker-return, structural, packet-authority, finding-to-learning, and
operation-trace checker sources.

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| `docs/reviews/CVF_WEB_UX_CLARITY_T0_LIVE_AND_SOURCE_AUDIT_2026-07-18.md` | Create route matrix, hypothesis verdicts, IA proposal, terminology map, source-owner map, priority backlog, tranche recommendation, and claim boundary. |
| `docs/reviews/CVF_WEB_UX_CLARITY_T0_WORKER_RETURN_2026-07-18.md` | Create full no-commit worker return with executionBaseHead, commands, changed set, gates, browser limitations, and worker experience retrospective. |

No other path may change.

## Allowed Scope

- The two new review paths in the fulfillment manifest.
- Read-only browser navigation on the named public routes.
- Read-only repository source and checker inspection.

## Forbidden Scope

- Any source, test, configuration, dependency, public-sync, session, roadmap,
  registry, generated aggregate, or existing review edit.
- Form submission, authentication changes, provider/live calls, API-key use,
  production mutation, commit, push, deployment, or destructive command.

## Acceptance Criteria

- Every required route has a terminal audit row.
- Every initial hypothesis has a terminal verdict.
- At least one proposed navigation tree and terminology map are present.
- P0/P1 findings cite visible evidence plus current source owner.
- `/workspace` stale/missing state is separated into data-truth, deployment
  packaging, and presentation findings rather than treated as styling only.
- Recommendations distinguish ordinary user, reviewer, and admin/operator
  surfaces.
- No implementation is performed and no unverified production claim is made.
- Exactly two new review files exist; nothing is staged; HEAD is unchanged.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_WEB_UX_CLARITY_T0_WORKER_RETURN_2026-07-18.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The generated return must contain Purpose, Scope / Methodology, Findings /
Position, Risk / Corrective Action, Claim Boundary, Agent Operation Trace
Block, Delta Execution Claim Boundary Control Block, Public Export
Disposition, executionBaseHead, and git status --short evidence.

Conditional sections External Knowledge Intake Routing, Rescan Intelligence
Hardening, Corpus Completeness And Report Integrity, Finding-To-Governance
Learning Disposition, Epistemic Process Block, and Machine Closure Package must
be completed when applicable or marked N/A with reason.

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/check_governed_file_size.py --enforce
git diff --name-status
git diff --cached --name-status
git status --short
git rev-parse --short HEAD
```

## Web/UI Claim Boundary

| Field | Value |
|---|---|
| DESIGN.md read | REQUIRED before live/source audit. |
| UI claim boundary | Findings and redesign backlog only; no production-readiness, hosted-correctness, or implementation-completion claim. |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch steward |
| Provider or surface | private provenance workspace |
| Session or invocation | CVF-WEB-UX-T0 dispatch, 2026-07-18 |
| Working directory | repository root |
| Command or tool surface | source reads, operator screenshots, browser availability check, scaffold preview, resolver, apply_patch, dispatch gates |
| Target paths | paired GC-018 baseline and this work order |
| Allowed scope source | operator instructed that a delegated worker audit the live Web UI when direct browser access was unavailable |
| Before status evidence | HEAD `7051eb87d`; worktree clean before authoring this dispatch packet |
| After status evidence | one source-verified no-commit audit work order exists |
| Diff evidence | `git diff --name-status` before dispatch commit |
| Approval boundary | audit dispatch only; no implementation, provider, production, public-sync, or deploy authority |
| Claim boundary | packet readiness only; no worker execution or audit acceptance claim |
| Agent type | dispatcher |
| Invocation ID | `cvf-web-ux-t0-dispatch-2026-07-18` |
| Expected manifest | paired baseline and work order |
| Actual changed set | paired baseline and work order |
| Manifest delta | MATCH |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | Read-only browser observation and source audit. |
| claimDisposition | CLAIM_REJECTED: no execution-control or runtime-enforcement behavior is claimed. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: browser observations and documentation evidence are not runtime receipts. |
| actionEvidence | ACTION_EVIDENCE_PRESENT: exactly two documentation outputs; no runtime action. |
| invocationBoundary | No provider or product workflow invocation is authorized. |
| interceptionBoundary | No direct interception, wrapper, runtime gate, or coding control is authorized. |
| claimLanguage | Audit evidence may say observed, source-verified, stale, missing, confusing, or recommended; it may not say implemented or production-ready. |
| forbiddenExpansion | No source edit, runtime/provider/live action, public-sync, commit, push, or deploy. |

## Claim Boundary

This work order authorizes a read-only live/source UX audit and exactly two
private review outputs. It does not authorize redesign implementation, route or
data repair, provider use, production interaction, public export, commit, push,
deployment, or session-state mutation.

## Closure Checklist

- [x] Dispatch source facts verified.
- [x] Worker scope limited to two outputs.
- [x] Reviewer conversion and commit owner declared.
- [x] Runtime/provider/public mutation forbidden.
- [ ] Worker route matrix terminal; return-to-orchestrator action: worker must complete before review.
- [ ] Reviewer recomputation complete; return-to-orchestrator action: reviewer owns closure decision.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only when the two outputs exist, required gates
pass, nothing is staged, and HEAD is unchanged. Return `BLOCKED_WITH_REASON`
for inaccessible live evidence, source contradiction, or forbidden-scope need.

## Operator Checkpoint

The audit itself is authorized. Any redesign roadmap, source edit, route
reorganization, data repair, public push, or deployment remains parked for a
new operator checkpoint after reviewer acceptance.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private audit dispatch. Public implementation/export requires reviewer
acceptance and a separate source-verified redesign roadmap or work order.
