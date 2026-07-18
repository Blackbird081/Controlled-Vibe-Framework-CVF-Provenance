# CVF Agent Work Order - SOT3 Operator Evidence Projection

Memory class: governed-worker-dispatch

Status: CLOSED_PASS_WITH_REVIEWER_REPAIRS

Batch ID: CVF-WEB-INHERITANCE-T2

Dispatch base head: `edeec4e94`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: delegated implementation worker

Reviewer/closer: CVF independent reviewer/closer

Worker return path: `docs/reviews/CVF_WEB_INHERITANCE_T2_WORKER_RETURN_2026-07-18.md`

## Dispatch Prompt Envelope

Role: implement only CVF-WEB-INHERITANCE-T2 as a no-commit worker.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_WEB_INHERITANCE_T2_SOT3_OPERATOR_EVIDENCE_PROJECTION_2026-07-18.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: use the dispatcher-provided post-dispatch session HEAD and
verify it before editing.

Current-time notes: artifact and source verification date is 2026-07-18.

Do-not-misread notes: this is a read-only evidence projection, not a SOT3
action surface, evidence editor, provider proof, or sibling-app port.

Required first actions: read startup surfaces, `DESIGN.md`, guard orientation,
literal gotchas, this packet, the paired baseline, all seven allowed source
paths that already exist, and checker sources listed below.

Return contract: leave exact allowed changes unstaged and uncommitted and
return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Build a safe server read model and operator page over the existing durable
SOT3 activation evidence store, with explicit privacy projection, deterministic
states, focused tests, and no action or persistence change.

## Agent Roles

- Worker: implementation and worker-return evidence only.
- Reviewer/closer: independent recomputation, bounded repair, closure, commit.
- Session-sync steward: protected continuity update in a separate commit.

## Authority Chain

Operator standing continuation authority -> CVF Web inheritance roadmap ->
accepted T1 completion review at `b186df669` -> this source-verified T2 packet
-> no-commit worker -> independent reviewer/closer -> session-sync steward.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
3. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
4. `AGENT_HANDOFF_V47_2026-07-18.md`
5. `docs/reference/guard_orientation/README.md`
6. `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
7. `DESIGN.md`
8. paired T2 baseline and every source in Source Verification

## Pre-Flight Checks

- capture `git rev-parse --short HEAD` and require the instructed execution HEAD;
- require a clean start with no staged or unstaged paths;
- run pre-implementation autorun against the real execution base;
- verify all allowed paths and forbidden source owners before editing; and
- stop before edit on a source contradiction or forbidden-scope dependency.

## Worker Autonomy / No-Question Rule

Repair allowed-scope checker or test failures directly. Return to the
orchestrator only for a source contradiction, execution-head mismatch,
forbidden-scope need, missing existing test owner assumption, or inability to
meet the privacy boundary without changing an existing source owner.

## Intake Role Routing Decision

routeMode: SINGLE_AGENT_SINGLE_ROLE selected route

Intake summary: repository-local bounded frontend implementation.

Scope classification: one server read model, one read-only page, discoverability,
focused tests, and one worker return.

Risk sensitivity: HIGH because persisted evidence fields require explicit
privacy projection and fail-closed error handling.

Role separation: implementation worker cannot accept or commit its own work.

Escalation condition: raw record access, auth change, action surface, provider
call, or evidence mutation is required.

## Dependency Release Evidence

| Dependency | Artifact | Material commit | Disposition |
|---|---|---|---|
| T1 accepted | `docs/reviews/CVF_WEB_INHERITANCE_T1_COMPLETION_REVIEW_2026-07-18.md` | `b186df669` | ACCEPT |
| T2 roadmap row | `docs/roadmaps/CVF_WEB_CAPABILITY_INHERITANCE_AND_OPERATOR_PROJECTION_ROADMAP_2026-07-18.md` | `b186df669` | ACCEPT |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| record top-level fields exist | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/sot3-activation-evidence-store.ts` | lines 52-65 | `Sot3ActivationEvidenceRecord` | activation evidence schema | ACCEPT |
| store read validates document and record integrity | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/sot3-activation-evidence-store.ts` | lines 239-266 and 286-292 | `readDocument` | `Sot3ActivationEvidenceStore` | ACCEPT |
| store enumerates records read-only | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/sot3-activation-evidence-store.ts` | lines 366-368 | `list` | `Sot3ActivationEvidenceStore` | ACCEPT |
| execute owner already configures the store path | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-knowledge-context.ts` | line 330 | `CVF_SOT3_ACTIVATION_EVIDENCE_PATH` | execute knowledge-context integration | ACCEPT |
| package scripts provide verification | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | scripts section | `test`; `check`; `build` | npm scripts | ACCEPT |
| roadmap releases bounded operator evidence | VALUE_SET | `docs/roadmaps/CVF_WEB_CAPABILITY_INHERITANCE_AND_OPERATOR_PROJECTION_ROADMAP_2026-07-18.md` | Tranche Plan | `CVF-WEB-INHERITANCE-T2` | roadmap | ACCEPT |

## New Doc-Only Fields

N/A with reason: proposed TypeScript interfaces are implementation outputs;
no governed documentation schema field is introduced.

## Scope / Target / Owner Boundary

The existing store remains the durable authority. The new server read model is
the only projection owner. The new page consumes only that safe read model.
The existing governance page receives one link and label per language.

## Allowed Scope

1. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/sot3-activation-evidence-readout.ts`
2. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/sot3-activation-evidence-readout.test.ts`
3. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/governance/sot3-evidence/page.tsx`
4. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/governance/sot3-evidence/page.test.tsx`
5. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/governance/page.tsx`
6. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/governance/page.test.tsx`
7. `docs/reviews/CVF_WEB_INHERITANCE_T2_WORKER_RETURN_2026-07-18.md`

## Write Ownership

The worker owns only the seven allowed paths. The reviewer owns those paths
for closure conversion plus the paired baseline, work order, roadmap, and
required completion review. The session steward separately owns continuity.

## Forbidden Scope

- do not modify the evidence store, execute route, adapter, package, API, auth,
  sidebar, persistence, or underlying record schema;
- do not expose `traces`, `integrityHash`, `actorId`, raw errors, store path,
  knowledge content, prompt text, provider payloads, or secret values;
- do not add POST/PUT/PATCH/DELETE, buttons that mutate, retry calls, evidence
  deletion, SOT3 execution, provider/live calls, or browser automation;
- do not implement T3-T5, public-sync, push, release, or production work; and
- do not stage, stash, commit, or edit session surfaces.

## Required Read Model Contract

Create a server-only report builder with an injectable store seam and an
injectable clock. It must:

- return `AVAILABLE`, `EMPTY`, or `UNAVAILABLE`;
- expose report generation time, bounded totals by mode/outcome, a clear
  read-only boundary, and no configured file path;
- project only `recordId`, `requestId`, `organization`, `team`, `mode`,
  `terminalOutcome`, `failureStage`, `createdAtUtc`, `diagnosticClass`,
  `schemaVersion`, and `traceCount`;
- sort records by `createdAtUtc` descending with `recordId` as deterministic
  tie-breaker and cap output at 50;
- preserve zero as a valid trace count and null team/failure stage;
- on a store error, return zero records and a secret-safe diagnostic class,
  never raw error text, record bytes, or path; and
- never call append or any write-capable surface.

## Execution Plan

1. Implement and test the safe server read model first.
2. Serialize representative reports and prove forbidden fields are absent.
3. Build and test populated, empty, and unavailable page states.
4. Add and test the governance overview link in both languages.
5. Run focused tests, typecheck, build, size, and worker-return fast gates.
6. Return exact unstaged changes without committing.

## Required UI Contract

Create `/governance/sot3-evidence` as a force-dynamic server page using the
CVF operational dashboard design language. It must visibly state read-only
and privacy boundaries, render mode/outcome summary, bounded record identifiers
and diagnostics, and provide dedicated empty and unavailable states. It must
not contain a mutation control. Add a discoverability link to the current
governance overview with concise English and Vietnamese labels.

## Text Encoding Exception

Bounded non-ASCII Vietnamese user-facing copy is required for the localized
discoverability label and its exact test assertion. A local exception note is
required in each affected source file; all other new text remains ASCII.

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| server read model | create safe deterministic projection |
| read-model test | prove available, empty, unavailable, sorting, limiting, and field exclusion |
| SOT3 evidence page | create read-only operator surface |
| page test | prove populated, empty, unavailable, boundary, and absence of mutation controls |
| governance overview | add one route label and link in both languages |
| governance overview test | prove link destination and both labels |
| worker return | record exact commands, boundary, changed set, and no-commit evidence |

## Required Artifact Manifest

| Required artifact set | Expected count | Closure evidence | Disposition |
|---|---:|---|---|
| Allowed Scope paths | 7 | exact worker-return manifest and reviewer status evidence | PASS |
| Extra, renamed, deleted, staged, or session paths | 0 | status, cached diff, and reviewer inspection | PASS |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order instruction | Evidence |
|---|---|---|
| read-only status/evidence surface | read model plus server page | focused tests |
| activation mode and outcome | explicit safe fields and summaries | read-model/page assertions |
| identifiers and bounded diagnostics | explicit allowlist and error projection | exclusion tests |
| no raw knowledge or secret leakage | forbidden field list and negative assertions | focused tests and diff review |
| focused tests and build | verification commands | worker return |

## Verification / Evidence

Focused tests must directly assert that `traces`, `integrityHash`, `actorId`,
raw errors, and configured paths never appear in serialized report output.
Page tests must cover populated, empty, and unavailable states and verify no
mutation button. Typecheck and production build must pass.

## Acceptance Criteria

- AC-01: safe readout uses only the explicit allowlist.
- AC-02: available, empty, unavailable, sorting, limit, and privacy exclusions pass.
- AC-03: page communicates state, identifiers, diagnostics, and boundary.
- AC-04: governance overview exposes the new route in both languages.
- AC-05: focused tests, `npm run check`, and `npm run build` pass.
- AC-06: file-size guard and worker-return fast gate pass.
- AC-07: exact seven-path, no-stage, unchanged-HEAD boundary is preserved.

## Evidence Requirements

Record focused test counts, typecheck/build results, file-size result,
worker-return fast result, `git diff --name-status`, cached diff, status, and
final HEAD. Do not report a command as PASS unless its final run exited zero.

## Review Gate

Independent reviewer must inspect serialized readout output, source diff,
privacy exclusions, page states, discoverability, focused tests, build, worker
boundary, and all governed gates before acceptance.

## Closure Checklist

- [x] execution HEAD matches dispatcher instruction;
- [x] exact safe readout allowlist and states implemented;
- [x] forbidden raw fields are absent from serialized output;
- [x] page and discoverability states are focused-test proven;
- [x] typecheck, build, and file-size pass;
- [x] exact seven-path changed set and no staging;
- [x] worker no-commit boundary honored; and
- [x] independent reviewer accepted the bounded result with repairs.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` before forbidden edits if the store lacks verified
list reads, privacy projection cannot be achieved through a new read model,
the execution HEAD mismatches, an existing path unexpectedly collides, or a
required test/build fix needs an eighth path.

## Operator Checkpoint

N/A with reason: operator standing authorization releases automatic bounded
roadmap continuation. Provider/live, public, push, production, or scope
expansion still requires a fresh explicit checkpoint.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | safe server read model and operator page | inspect only; no action or persistence | focused tests | existing store read seam | `IMPLEMENT_BOUNDED` |
| `EXTERNAL_AGENT_CLI_MCP` | no changed interface | no ingress, action, receipt, or mutation | no adapter output | parked | `N/A_WITH_REASON` |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | `SINGLE_AGENT_SINGLE_ROLE` |
| rolePattern | one implementation worker followed by independent reviewer/closer |
| phase | dispatch then no-commit execution then reviewer closure then session sync |
| baseHeadFor(phase) | dispatchBaseHead=`edeec4e94`; executionBaseHead=dispatcher-provided post-dispatch session HEAD; closureBaseHead=executionBaseHead |
| changedSetScope(phase) | dispatch=baseline/work order/roadmap; execution=exact seven allowed paths; closure=reviewer-owned artifacts; session=protected continuity only |
| traceScope(phase, actor) | each actor records only its own commands, changed set, and boundary |
| commitOwner(phase) | dispatcher; none for worker; reviewer/closer; session-sync steward |
| crossBatchIsolation | T3-T5 and every external mutation lane remain parked |
| nextMoveSurfaces | worker must not edit; session steward owns separately authorized protected updates |

## Reviewer Closure Conversion

completionReviewPath:
`docs/reviews/CVF_WEB_INHERITANCE_T2_COMPLETION_REVIEW_2026-07-18.md`

reviewerOwnedClosurePaths: all seven worker paths, paired baseline and work
order, roadmap, and completion review; continuity only in a separate commit.

closureOwner: CVF independent reviewer/closer.

workerCommitPermission: FORBIDDEN.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_WEB_INHERITANCE_T2_WORKER_RETURN_2026-07-18.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base $executionBaseHead --head HEAD
Set-Location EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web
npx vitest run src/lib/server/sot3-activation-evidence-readout.test.ts "src/app/(dashboard)/governance/sot3-evidence/page.test.tsx" "src/app/(dashboard)/governance/page.test.tsx"
npm run check
npm run build
Set-Location ../../..
python governance/compat/check_governed_file_size.py --enforce
python governance/compat/run_worker_return_fast_gate.py
git diff --name-status
git diff --cached --name-status
git status --short
git rev-parse --short HEAD
```

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`frontend`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class frontend --role dispatcher --lifecycle-phase pre-dispatch --surface-selector cvf-web --risk-ceiling HIGH --max-results 20 --json`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | Status; Dispatch Prompt Envelope; Scope / Target / Owner Boundary; Dependency Release Evidence; Source Verification Block; Roadmap-To-Work-Order Trace Matrix; Work-Order Fulfillment Manifest; Acceptance Criteria; Review Gate; Closure Checklist; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Public Export Disposition; Claim Boundary |
| gateRunPurpose | dispatch confirmation after direct source verification |
| claimBoundary | structural conformance does not replace implementation review |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-WEB-INHERITANCE-T2 --title "SOT3 Operator Evidence Projection" --date 2026-07-18 --base edeec4e94 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | filled exact source, page, test, privacy, evidence, and handoff contracts |
| checkerReadAheadConfirmation | checker paths listed above |
| docOnlyNewFields | none |
| claimBoundary | dispatch-authoring provenance only |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | local private provenance workspace |
| Session or invocation | CVF-WEB-INHERITANCE-T2 dispatch, 2026-07-18 |
| Working directory | repository root |
| Command or tool surface | source reads, repository search, artifact authoring, governance gates |
| Target paths | roadmap; paired T2 baseline; this work order |
| Allowed scope source | accepted T1 review and roadmap T2 release |
| Before status evidence | clean worktree at `edeec4e94` |
| After status evidence | exact three-path dispatch set pending commit |
| Diff evidence | material diff captured before commit |
| Approval boundary | bounded T2 read-only evidence projection dispatch only |
| Claim boundary | no worker execution, persistence, provider/live, public, push, or production mutation |
| Agent type | dispatcher |
| Invocation ID | `cvf-web-inheritance-t2-dispatch-2026-07-18` |
| Expected manifest | roadmap; baseline; work order |
| Actual changed set | exact three-path dispatch set |
| Manifest delta | MATCH expected after verification |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | read-only safe projection of existing durable evidence |
| claimDisposition | N/A with reason: no execution-control or enforcement behavior is implemented |
| receiptEvidence | N/A with reason: this surface reads existing records and creates no receipt |
| actionEvidence | N/A with reason: no command or mutation action is exposed |
| invocationBoundary | exact T2 worker packet |
| interceptionBoundary | no IDE, shell, provider, filesystem, or agent-action interception claim |
| claimLanguage | read, project, summarize, display, and report only |
| forbiddenExpansion | persistence mutation, raw knowledge, action, provider/live, public-sync, push, production |

## Current Runtime Freshness Verification

At dispatch base `edeec4e94`, the evidence store validates and lists durable
records, the execute integration supplies the configured local path, and no
current SOT3 operator readout/page exists. This packet adds only projection.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Baseline status | paired T2 GC-018 baseline | `Status: CLOSED_PASS_WITH_REVIEWER_REPAIRS` | PASS |
| Work order status | this file | `Status: CLOSED_PASS_WITH_REVIEWER_REPAIRS` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_WEB_INHERITANCE_T2_COMPLETION_REVIEW_2026-07-18.md` | `Status: REVIEWER_ACCEPTED_WITH_REPAIRS` | PASS |
| Worker return | T2 worker return | `Status: ACCEPTED_BY_REVIEWER_WITH_REPAIRS` | PASS |
| Roadmap state | CVF Web inheritance roadmap | `Status: CVF_WEB_INHERITANCE_T2_PASS_T3_PACKET_AUTHORING_NEXT` | PASS |
| Registry JSON | corpus registry generated aggregate | existing cvf-web `src/` scope coverage and aggregate drift check | PASS |
| Registry Markdown | corpus registry read model | existing cvf-web `src/` scope coverage | PASS |
| External evidence digest | N/A with reason: repository-local evidence only | none | N/A with reason |
| System loop interlock | N/A with reason: no loop owner changed | none | N/A with reason |
| Session continuity | protected session surfaces | separate session-sync commit | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| Runtime receipt evidence | N/A with reason: read-only projection creates no receipt | N/A_WITH_REASON |
| Query acceptance evidence | safe list read and three report states independently tested | PASS |
| Worker-return acceptance | independent diff, tests, build, and gates recomputed | PASS |
| Closure claim | bounded SOT3 evidence projection only | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance T2 dispatch; no public-sync action.

## Claim Boundary

This work order authorizes exactly seven no-commit paths for a safe read-only
operator projection. It does not authorize evidence mutation, raw trace or
knowledge exposure, SOT3 execution, provider/live proof, public export, push,
release, production readiness, or session mutation.
