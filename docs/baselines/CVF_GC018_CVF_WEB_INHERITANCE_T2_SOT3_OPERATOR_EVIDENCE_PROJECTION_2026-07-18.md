# CVF GC-018 Baseline - SOT3 Operator Evidence Projection

Memory class: governed-dispatch-baseline

Status: CLOSED_PASS_WITH_REVIEWER_REPAIRS

Batch ID: CVF-WEB-INHERITANCE-T2

Dispatch base head: `edeec4e94`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator

Reviewer owner: CVF independent reviewer/closer

Worker target: delegated implementation worker

## Purpose

Release one bounded cvf-web implementation tranche that projects existing
durable SOT3 activation evidence into a read-only operator page without
exposing raw knowledge, trace payloads, integrity hashes, secrets, or actions.

## Scope / Target / Owner Boundary

The worker may create a server read model, its focused test, one dashboard
page and page test, add one discoverability link on the existing governance
page with a focused test, and create the worker return. Existing evidence
persistence and execute-route behavior are source owners and must not change.

## Dependency Release Evidence

| Dependency | Artifact | Material commit | Disposition |
|---|---|---|---|
| T1 registry truth | `docs/reviews/CVF_WEB_INHERITANCE_T1_COMPLETION_REVIEW_2026-07-18.md` | `b186df669` | ACCEPT |
| roadmap T2 release | `docs/roadmaps/CVF_WEB_CAPABILITY_INHERITANCE_AND_OPERATOR_PROJECTION_ROADMAP_2026-07-18.md` | `b186df669` | ACCEPT |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| durable records expose bounded top-level fields | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/sot3-activation-evidence-store.ts` | lines 52-65 | `Sot3ActivationEvidenceRecord` | activation evidence schema | ACCEPT |
| store provides verified read enumeration | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/sot3-activation-evidence-store.ts` | lines 278-368 | `list` | `Sot3ActivationEvidenceStore` | ACCEPT |
| default store path is already environment-configurable | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-knowledge-context.ts` | line 330 | `CVF_SOT3_ACTIVATION_EVIDENCE_PATH` | execute knowledge-context integration | ACCEPT |
| current scripts support test, typecheck, and build | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | scripts section | `test`; `check`; `build` | npm scripts | ACCEPT |
| T2 requires bounded SOT3 operator evidence | VALUE_SET | `docs/roadmaps/CVF_WEB_CAPABILITY_INHERITANCE_AND_OPERATOR_PROJECTION_ROADMAP_2026-07-18.md` | Tranche Plan | `CVF-WEB-INHERITANCE-T2` | roadmap | ACCEPT |

## New Doc-Only Fields

N/A with reason: no new governed documentation schema field is introduced.
New TypeScript read-model fields are implementation outputs, not pre-existing
source facts.

## Allowed Scope

1. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/sot3-activation-evidence-readout.ts`
2. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/sot3-activation-evidence-readout.test.ts`
3. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/governance/sot3-evidence/page.tsx`
4. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/governance/sot3-evidence/page.test.tsx`
5. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/governance/page.tsx`
6. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/governance/page.test.tsx`
7. `docs/reviews/CVF_WEB_INHERITANCE_T2_WORKER_RETURN_2026-07-18.md`

## Forbidden Scope

- no evidence-store, execute-route, knowledge adapter, package, API, auth,
  sidebar, persistence, or raw record schema mutation;
- no raw `traces`, `integrityHash`, actor identifier, knowledge content,
  prompts, provider payloads, secret paths, or environment values in output;
- no write, delete, retry, refresh mutation, worker launch, provider call,
  live proof, browser automation, public-sync, push, or production action;
- no T3-T5 implementation or session-state mutation; and
- no worker commit, staging, or stash.

## Required Read Model Boundary

The new read model must consume `Sot3ActivationEvidenceStore.list()` through an
injectable store seam. It may expose only record ID, request ID, organization,
team, activation mode, terminal outcome, failure stage, creation time,
persisted diagnostic class, schema version, and trace count. It must return
explicit AVAILABLE, EMPTY, or UNAVAILABLE state, sort deterministically newest
first, apply a bounded record limit, and convert read failures into a
secret-safe diagnostic without returning raw error text or the configured path.

## Required Page Boundary

The server-rendered page must be read-only, use existing CVF design tokens and
components, identify its boundary visibly, render loading-independent server
results plus available, empty, and unavailable states, remain responsive and
keyboard-readable, and contain no command control. The governance overview
must link to `/governance/sot3-evidence` in both language label maps.

## Baseline Decision

Dispatch one new safe read model and read-only operator page, plus the minimum
existing governance-page link and focused tests. The current governance page
is an allowed implementation target, not evidence authority for record fields.

## Verification / Evidence

Worker evidence must include focused read-model/page/link tests, typecheck,
production build, file-size enforcement, worker-return fast gate, exact changed
set, empty cached diff, unchanged execution HEAD, and no-commit statement.

## Acceptance Criteria

- AC-01: safe readout fields are explicit and forbidden raw fields are absent.
- AC-02: available, empty, corrupt/unavailable, deterministic sort, and limit
  cases are focused-test proven.
- AC-03: page renders summary, identifiers, mode, outcome, bounded diagnostic,
  boundary, empty state, and unavailable state.
- AC-04: governance overview exposes the new route in English and Vietnamese.
- AC-05: focused tests, typecheck, build, and file-size guard pass.
- AC-06: exactly seven allowed paths change; nothing is staged; HEAD remains
  the worker's execution base.

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| three new artifact paths | `Test-Path` returned False before authoring | ACCEPT |
| batch token search | only roadmap, accepted T1 closure, and active next-move references existed | ACCEPT |
| source collision | no current SOT3 operator readout/page owner exists | ACCEPT |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | server read model and read-only page | inspect bounded persisted evidence only | focused tests | existing store read seam | `IMPLEMENT_BOUNDED` |
| `EXTERNAL_AGENT_CLI_MCP` | no changed interface | no ingress, action, receipt, or mutation | no adapter output | parked | `N/A_WITH_REASON` |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`frontend`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class frontend --role dispatcher --lifecycle-phase pre-dispatch --surface-selector cvf-web --risk-ceiling HIGH --max-results 20 --json`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | Status; Scope / Target / Owner Boundary; Dependency Release Evidence; Source Verification Block; Acceptance Criteria; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirmation after direct source verification |
| claimBoundary | structural conformance does not replace implementation review |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-WEB-INHERITANCE-T2 --title "SOT3 Operator Evidence Projection" --date 2026-07-18 --base edeec4e94 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | filled exact source, page, test, privacy, evidence, and handoff boundaries |
| checkerReadAheadConfirmation | checker paths listed above |
| docOnlyNewFields | none |
| claimBoundary | dispatch-authoring provenance only |

## Current Runtime Freshness Verification

At dispatch base `edeec4e94`, durable evidence records and verified list reads
exist, the execute path uses the configured local evidence path, and no current
operator readout or page owns this evidence. T1 is accepted at `b186df669`.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Baseline status | this file | `Status: CLOSED_PASS_WITH_REVIEWER_REPAIRS` | PASS |
| Work order status | paired T2 work order | `Status: CLOSED_PASS_WITH_REVIEWER_REPAIRS` | PASS |
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

Reason: private provenance implementation dispatch; no public-sync action.

## Claim Boundary

This baseline authorizes a bounded read-only Web projection only. It does not
authorize evidence mutation, raw knowledge access, actor surveillance, SOT3
execution, provider/live proof, public export, push, or production readiness.
