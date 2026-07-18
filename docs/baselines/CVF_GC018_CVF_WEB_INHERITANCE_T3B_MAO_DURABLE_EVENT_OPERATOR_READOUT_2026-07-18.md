# CVF GC-018 Baseline - CVF Web Inheritance T3B MAO Durable Event Operator Readout

Memory class: governed-dispatch-baseline

Status: CLOSED_PASS_WITH_REVIEWER_REPAIR

Batch ID: CVF-WEB-INHERITANCE-T3B

Dispatch base head: `f16432325`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: CVF dispatcher

Reviewer owner: independent CVF reviewer/closer

Worker target: one implementation worker

## Purpose

Add a bounded read-only cvf-web projection over the existing durable MAO run
store. Expose only run discovery, generated task state, timeout counts, and
event recency released by accepted T3P2 evidence.

## Scope / Target / Owner Boundary

The worker may add the execution-plane package dependency, explicit local
store-path configuration, one server read model and tests, one operator page
and tests, governance discoverability, registry truth correction, and its
worker return. The file-backed store and `buildReadModel` remain the semantic
owners; cvf-web owns only a safe bounded projection.

## Dependency Release Evidence

| Dependency | Accepted artifact | Material commit | Final disposition | Release effect |
|---|---|---|---|---|
| T3A source-seam decision | `docs/reviews/CVF_WEB_INHERITANCE_T3A_COMPLETION_REVIEW_2026-07-18.md` | `c0d88ff34` | REVIEWER_ACCEPTED_WITH_REPAIRS | prerequisite split required |
| T3P1 run discovery | `docs/reviews/CVF_WEB_INHERITANCE_T3P1_COMPLETION_REVIEW_2026-07-18.md` | `c282312b9` | REVIEWER_ACCEPTED_WITH_REPAIR | `listRunIds` released |
| T3P2 availability decision | `docs/reviews/CVF_WEB_INHERITANCE_T3P2_COMPLETION_REVIEW_2026-07-18.md` | `32813a983` | REVIEWER_ACCEPTED_WITH_REPAIR | durable-event-only route released |

## Baseline Decision

Implement `BOUNDED_DURABLE_EVENT_ONLY_WEB_ROUTE` now. Evidence records,
evidence-derived milestones, evidence freshness, heartbeat, live-process
status, worker launch, timeout mutation, and provider calls are excluded.

## Design Control Gate

`DESIGN.md` was read before packet authoring and controls the UI. Reuse current
cvf-web patterns and dependencies. Provide accessible `AVAILABLE`, `EMPTY`,
and `UNAVAILABLE` states, responsive containment, keyboard-safe links, and no
mutation control.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| execution package identity | VALUE_SET | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/package.json` | name field | `name` | package manifest | ACCEPT |
| package-root MAO exports | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/index.ts` | final export | `./mao` | package root | ACCEPT |
| durable store constructor | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts` | `MaoFileRunStore` | `MaoFileRunStore` | class | ACCEPT |
| run discovery | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts` | `listRunIds` | `listRunIds` | `MaoFileRunStore` | ACCEPT |
| replay | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts` | `resumeRun` | `resumeRun` | `MaoFileRunStore` | ACCEPT |
| generated task state | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/read.model.contract.ts` | `buildReadModel` | `buildReadModel` | function | ACCEPT |
| event timestamp | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/event.ledger.contract.ts` | `MaoEventLedgerEntry` | `occurredAt` | interface | ACCEPT |
| timeout event token | VALUE_SET | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/event.ledger.contract.ts` | `MaoEventType` | `TIMEOUT_DETECTED` | union | ACCEPT |
| safe Web readout precedent | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/sot3-activation-evidence-readout.ts` | `getSot3ActivationEvidenceReadout` | `getSot3ActivationEvidenceReadout` | function | ACCEPT |
| registry current state | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/runtime-modules.ts` | execution-plane entry | `webExposureState` | module registry entry | ACCEPT |

## New Implementation Symbols

| Proposed symbol | Owner path | Required role |
|---|---|---|
| `CVF_MAO_DURABLE_RUN_PATH` | cvf-web environment contract | explicit operator-supplied store root; missing value fails visibly unavailable |
| `MaoDurableRunReadoutReport` | new server readout module | safe bounded projection type |
| `getMaoDurableRunReadout` | new server readout module | read-only orchestration over `listRunIds`, `resumeRun`, and `buildReadModel` |
| `/governance/mao-runs` | new page | operator readout only |

## Allowed Scope

Exactly the twelve paths named in the paired work order may change. The worker
must not add any other source, test, documentation, registry, session, or
generated artifact.

## Forbidden Scope

- no change to execution-plane source or tests;
- no evidence ledger, evidence milestone, evidence recency, or heartbeat data;
- no worker launch, timeout recording, cancellation, retry, queue, or provider call;
- no raw graph authority, idempotency key, event detail, filesystem path, or raw error projection;
- no API route, auth, RBAC, new UI library, browser/live proof, public-sync, push, or production action;
- no commit, staging, session-state, handoff, or corpus-registry mutation by the worker.

## Acceptance Criteria

- AC-01: missing configuration returns `UNAVAILABLE`, never an implicit path.
- AC-02: empty store returns `EMPTY`; valid runs return `AVAILABLE`.
- AC-03: any discovery or replay failure fails the whole report closed with a
  safe diagnostic class and no partial records or raw detail.
- AC-04: the allowlist contains only run ID, counts, latest event time, and
  generated task-state fields released by T3P2.
- AC-05: output is deterministic, bounded to 50 runs and 100 tasks per run,
  and ordered by latest event time then run ID.
- AC-06: timeout counts derive only from replayed `TIMEOUT_DETECTED` events.
- AC-07: page states and boundary copy are visible and no mutation control exists.
- AC-08: dependency, lockfile, registry entry, and governance link match source truth.
- AC-09: focused tests, full cvf-web typecheck/build, file-size enforcement,
  worker-return fast gate, and exact no-commit boundary pass.

## Evidence / Verification

Evidence must include the exact changed set, unchanged execution HEAD, empty
cached diff, focused server/page/registry tests, cvf-web TypeScript and
production build, governed file-size enforcement, pre-implementation autorun,
and the complete worker-return fast gate. Browser and live proof are not part
of this tranche and must not be claimed.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`frontend`, role=`worker`, lifecyclePhase=`pre-implementation`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class frontend --role worker --lifecycle-phase pre-implementation --surface-selector cvf-web --risk-ceiling HIGH --max-results 20 --json`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | Status; Dependency Release Evidence; Source Verification Block; Allowed Scope; Forbidden Scope; Design Control Gate; Acceptance Criteria; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirmation after direct source and checker read-ahead |
| claimBoundary | structural conformance does not prove Web behavior |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-WEB-INHERITANCE-T3B --title "MAO Durable Event Operator Readout" --date 2026-07-18 --base f16432325 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | filled dependency release, source facts, exact implementation boundary, UI contract, and twelve-path manifest |
| checkerReadAheadConfirmation | checker paths listed above |
| docOnlyNewFields | N/A with reason: proposed symbols are implementation-owned, not doc-only contracts |
| claimBoundary | dispatch-authoring provenance only |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance implementation dispatch; no public-sync action.

## Claim Boundary

This baseline authorizes only the paired bounded T3B implementation packet.
It does not prove the implementation, authorize excluded evidence/liveness
dimensions, or authorize live, public, push, release, or production action.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Baseline status | this file | `Status: CLOSED_PASS_WITH_REVIEWER_REPAIR` | PASS |
| Work order status | paired T3B work order | `Status: CLOSED_PASS_WITH_REVIEWER_REPAIR` | PASS |
| Completion or reviewer artifact | T3B completion review | `Status: REVIEWER_ACCEPTED_WITH_REPAIR` | PASS |
| Worker return | T3B worker return | `Status: ACCEPTED_BY_REVIEWER_WITH_REPAIR` | PASS |
| Roadmap state | CVF Web inheritance roadmap | `Status: CVF_WEB_INHERITANCE_T3B_PASS_T4_PACKET_AUTHORING_NEXT` | PASS |
| Registry JSON | corpus registry generated aggregate | existing cvf-web scope coverage; drift check passes | PASS |
| Registry Markdown | corpus registry read model | existing cvf-web scope coverage | PASS |
| External evidence digest | N/A with reason: repository-local implementation | none | N/A with reason |
| System loop interlock | N/A with reason: no loop owner changed | none | N/A with reason |
| Session continuity | protected session surfaces | separate session-sync commit follows | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| Runtime receipt evidence | N/A with reason: read-only local file projection creates no action receipt | N/A_WITH_REASON |
| Query acceptance evidence | 21 focused tests, typecheck, and build pass | PASS |
| Worker-return acceptance | exact twelve paths, unchanged HEAD, no staging | PASS |
| Closure claim | bounded MAO durable-event Web readout accepted after localization repair | PASS |
