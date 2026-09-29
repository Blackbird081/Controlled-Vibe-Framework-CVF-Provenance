# CVF GC-018 Baseline - CVF EAFR-R1A Non-Live Test Runner Extension Coverage

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: EAFR-R1A-NON-LIVE-TEST-RUNNER-EXTENSION-COVERAGE

Dispatch base head: bb49266fd

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator through standing EAFR roadmap authority

Reviewer owner: independent orchestrator/reviewer/closer

Worker target: delegated no-commit implementation worker

## Purpose

Repair the cvf-web package test-script boundary so every tracked `.live.test.ts`
and `.live.test.tsx` file is excluded from non-live run and coverage scripts and
included only by the explicit live runner. Add a deterministic static regression
without invoking any provider, network surface or live test.

## Scope / Target / Owner Boundary

Worker write ownership is exactly:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/package-test-script-boundary.test.ts`
- `docs/reviews/CVF_EAFR_R1A_NON_LIVE_TEST_RUNNER_EXTENSION_COVERAGE_WORKER_RETURN_2026-08-25.md`

No other file may be edited, staged or committed. In particular, the existing
live test, credentials, routes, provider adapters, Vitest configuration and R1
helper/test are read-only. `test:live`, provider SDKs and network calls are
forbidden.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id EAFR-R1A-NON-LIVE-TEST-RUNNER-EXTENSION-COVERAGE --title "CVF EAFR-R1A Non-Live Test Runner Extension Coverage" --date 2026-08-25 --base bb49266fd --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced all placeholders; added exact three-path manifest, source hashes, safe verification and incident boundaries |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py` |
| docOnlyNewFields | `trackedLiveTestExtensions`; `incidentEvidenceDisposition`; `repeatLiveAuthority` |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |


## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| EAFR-R1 accepted material blocked by live-test activation incident at bb49266fd | `docs/reviews/CVF_EAFR_R1_AIF_REINJECTION_PROVENANCE_FAIL_CLOSED_COMPLETION_2026-08-25.md`; commit `bb49266fd09bea5c2252520d838526d5d8f13086` | R1 implementation accepted and the non-live runner defect named as mandatory R1A | RELEASED_FOR_R1A_ONLY |

Author reminder: do not move this packet to DISPATCH_READY/DISPATCHED until every dependency row carries source-backed evidence.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`implementation`, role=`worker`, lifecyclePhase=`pre-execution`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class implementation --role worker --lifecycle-phase pre-execution --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | no additional ADIF constraint beyond the governing packet |

Author reminder: run the resolver command above for real before dispatch; list every defectId it actually returns.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py` |
| literalTokensReviewed | `DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; Source Verification columns; Dependency Release Evidence; Public Export Disposition |
| gateRunPurpose | confirm final baseline structure before pre-dispatch, not discover required content |
| claimBoundary | read-ahead proves artifact shape only; package-script facts come from current source and hashes |

Author reminder: read every applicable checker source before writing the first governed line, then fill this block as confirmation evidence.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| current non-live script excludes only TypeScript source files | PACKAGE_SOURCE | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | scripts block | `scripts` | npm package scripts | ACCEPT |
| one tracked live test uses the TSX extension | TEST_SOURCE | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.gc009-live-t5-mandatory-gateway.alibaba.live.test.tsx` | file path and `describe.skipIf` | `ALIBABA_API_KEY` | Vitest live acceptance file | ACCEPT |
| R1 reviewer requires R1A before R2 | REVIEW_SOURCE | `docs/reviews/CVF_EAFR_R1_AIF_REINJECTION_PROVENANCE_FAIL_CLOSED_COMPLETION_2026-08-25.md` | Findings R1-F8/R1-F9 and final position | `R1-F8` | EAFR reviewer decision | ACCEPT |

## Source Hash Manifest

| Path | SHA-256 at dispatch |
| --- | --- |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | `60358c01e39d962ce64a78bdad5eddd6a6690057f461d2c71a0355d1fa465ed1` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.gc009-live-t5-mandatory-gateway.alibaba.live.test.tsx` | `92d7034f06235296086565244ca5ae416abed6c5f64375fd642e1eefe1ead292` |
| `docs/reviews/CVF_EAFR_R1_AIF_REINJECTION_PROVENANCE_FAIL_CLOSED_COMPLETION_2026-08-25.md` | `98fd295ec8d5bb86b14968ad297d7940c8d0704ec4fa83e5cd8ae04847a8ab08` |

Author reminder: every claimed item needs a real source file and line/section; do not leave placeholder rows in the dispatched artifact.

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Path existence for "CVF EAFR-R1A Non-Live Test Runner Extension Coverage" artifacts | both target dispatch paths were absent before scaffold creation | PASS |
| Token search for "CVF EAFR-R1A Non-Live Test Runner Extension Coverage" (2026-08-25) | `rg -n "EAFR-R1A-NON-LIVE-TEST-RUNNER-EXTENSION-COVERAGE" docs CVF_SESSION`; results after authoring are limited to this paired packet | PASS |
| Collision decision | fresh R1A suffix and exact paths; no prior governed artifact collision | PROCEED |

Author reminder: run the searches for real before dispatch; do not leave placeholder rows.

## Baseline Decision

`PROCEED_WITH_BOUNDED_R1A_REPAIR`. The source defect is current, the accepted
R1 review makes it the mandatory next dependency, and the three-path repair is
local and reversible. R1 and later tranches remain unclosed until independent
R1A review.

## Proposed Tranche

One no-commit worker edits only the three owned paths, returns deterministic
evidence, and stops. The reviewer owns semantic acceptance, any R1/R1A
reconciliation, commits and continuity.

## Evidence / Verification

Dispatch evidence is the exact package/live-test/completion hash manifest,
34-file tracked live-test enumeration (33 TS and 1 TSX), zero-result ADIF
resolver receipt and pre-dispatch gate. Worker evidence must include focused
static tests, a non-executing Vitest file list, exact diff/status and the
worker-return fast gate.

## Claim Boundary

This baseline authorizes only a package-script boundary correction, one static
regression test and one worker return. It authorizes no live/provider/network
execution, API key access, route or provider behavior change, dependency
installation, build, deployment, public sync, push or worker commit.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance repair dispatch; no public-sync scope is opened.
