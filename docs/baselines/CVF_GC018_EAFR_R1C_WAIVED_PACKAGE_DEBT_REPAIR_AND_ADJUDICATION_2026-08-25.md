# CVF GC-018 Baseline - EAFR-R1C Waived Package Debt Repair And Adjudication

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: EAFR-R1C-WAIVED-PACKAGE-DEBT

Dispatch base head: `f8cf62c743c6c5ad08a790400ba26a2c05679997`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator through the committed EAFR roadmap and the explicit
bounded R1 waiver

Reviewer owner: current independent orchestrator/reviewer

Worker target: package-debt repair worker role

## Purpose

Repair or freshly adjudicate the three criteria that the explicit bounded
operator waiver closed EAFR-R1 without proving: cvf-web typecheck, the cvf-web
full non-live suite, and the cvf-web production build. Each criterion must end
in a source-backed repair or a fresh, evidence-bearing adjudication, never a
relabel of the waived failure as PASS.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id EAFR-R1C --title "Waived Package Debt Repair And Adjudication" --date 2026-08-25 --base f8cf62c74 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | source-verified defect root causes, exact repair manifest, three-criterion disposition contract, safe-command discipline and adjudication rules |
| checkerReadAheadConfirmation | dispatch, authority, trace, delta, epistemic and worker-return checker sources reviewed |
| docOnlyNewFields | Waived Criterion Disposition Contract; Verified Defect Root Causes; Safe Command Discipline |
| claimBoundary | dispatch authoring only; no live, provider, public, deployment, credential or environment claim |

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| EAFR-R1 explicit bounded waiver | `docs/reviews/CVF_EAFR_R1_EXPLICIT_BOUNDED_OPERATOR_WAIVER_CLOSURE_2026-08-25.md`; three criteria recorded `WAIVED_WITH_NAMED_DEBT` with R1C named as follow-up owner | RELEASED |
| EAFR-R5 accepted | `docs/reviews/CVF_EAFR_R5_RETRIEVAL_EVIDENCE_SEMANTICS_AND_ADMISSION_BOUNDARY_COMPLETION_2026-08-25.md`; material commit `04a5cf40e3a396404b1aff0816534e4d8a6a1567` | RELEASED |
| EAFR roadmap authority | `docs/roadmaps/CVF_EAFR_REMEDIATION_ROADMAP_2026-08-25.md`, R1C row `READY_FOR_FRESH_DISPATCH_AUTHORING`, mandatory before R6 | ACCEPT |
| EAFR-R1A non-live runner fix | `docs/reviews/CVF_EAFR_R1A_NON_LIVE_TEST_RUNNER_EXTENSION_COVERAGE_COMPLETION_2026-08-25.md`; accepted at `ef142bfb2` | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`package debt repair`, role=`worker`, lifecyclePhase=`implementation`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "package debt repair" --role worker --lifecycle-phase implementation` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | none |
| Dispatch impact | ordinary CVF controls apply |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_equivalence_claim_evidence.py`; `governance/compat/check_worker_experience_retrospective.py` |
| literalTokensReviewed | Source Verification Block; Current Runtime Freshness Verification; exact manifest; no-commit status; trace labels; Public Export Disposition; equivalence disposition tokens; retrospective field block shape |
| gateRunPurpose | confirm as evidence that the source-verified dispatch already matches required shape |
| claimBoundary | structural conformance does not prove that any waived criterion is repairable |

## Current Runtime Freshness Verification

Verified directly at HEAD `f8cf62c743c6c5ad08a790400ba26a2c05679997` on
2026-08-25, after R5 material closure:

- cvf-web `npm run check` produces exactly 4 TypeScript errors, all in
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/provider-binding.test.ts`
  at lines 46, 150, 165 and 203. Zero errors exist in any production source
  file.
- cvf-web `npm run test:run` produces 29 failed, 3499 passed, 2 skipped across
  313 files, with 11 failing files. The runner already excludes both
  `.live.test.ts` and `.live.test.tsx` per the accepted R1A fix.
- 17 of the 29 failures are unexpected HTTP 401 assertions, concentrated in
  route tests whose authorization now flows through
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.ts`.
- LPF `npm test` is not a safe command: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/vitest.config.ts`
  declares no exclusion for `tests/**/*.alibaba.test.ts`, so three ambient-key
  provider tests are auto-selected when credentials exist. The explicit
  exclusion form reproduces 85 files and 1943/1943 passing with zero provider
  calls.
- The cvf-web production build was not run during this dispatch authoring.
  Prior R1 evidence records it as compiling through webpack and TypeScript and
  then failing Auth.js environment validation during page-data collection.

No live, provider, network, credential or build command is required or
authorized by this baseline. R1C proves local package health only and claims no
deployment, exposure, release or production readiness.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| R1C is authorized and mandatory before R6 | ROADMAP_AUTHORITY | `docs/roadmaps/CVF_EAFR_REMEDIATION_ROADMAP_2026-08-25.md` | Proposed Tranches, EAFR-R1C and EAFR-R6 rows | EAFR-R1C | EAFR roadmap | ACCEPT |
| exactly three criteria are waived debt, not PASS | OWNER_AUTHORITY | `docs/reviews/CVF_EAFR_R1_EXPLICIT_BOUNDED_OPERATOR_WAIVER_CLOSURE_2026-08-25.md` | Machine Closure Package, Typecheck/Full non-live suite/Build rows | WAIVED_WITH_NAMED_DEBT | R1 explicit waiver closure | ACCEPT |
| typecheck failures are confined to one test file | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/provider-binding.test.ts` | lines 46, 150, 165, 203 | bridgeResult; inline execute mocks | cvf-web LPCI provider binding test | ACCEPT |
| the missing field is required by the gateway interface | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | ProviderExecutionBridgeResult interface, lines 57-63 | ProviderExecutionBridgeResult; materialContextManifestDisposition | model gateway execution bridge | ACCEPT |
| route authorization flows through the governance proof helper | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.ts` | lines 136-241 | authorizeRouteGovernanceProof; verifySessionCookie | Web route governance proof helper | ACCEPT |
| failing route tests default the session to null | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.test.ts` | beforeEach, lines 127-128 | verifySessionCookieMock | cvf-web LPCI query route test | ACCEPT |
| the non-live runner already excludes both live extensions | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | scripts block, non-live runner entry | scripts non-live test runner entry | cvf-web package manifest | ACCEPT |
| LPF package test selection has no provider-test exclusion | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/vitest.config.ts` | test.include block | include | LPF vitest configuration | ACCEPT |
| the unsafe-command incident is recorded and grants no live authority | OWNER_RECONCILIATION | `docs/reviews/CVF_EAFR_R5_RETRIEVAL_EVIDENCE_SEMANTICS_AND_ADMISSION_BOUNDARY_COMPLETION_2026-08-25.md` | R5-RF6 section | providerCallCount | R5 completion review | ACCEPT |

## Verified Defect Root Causes

| Criterion | Verified root cause | Repairability at dispatch time |
| --- | --- | --- |
| typecheck | Four mock objects construct `ProviderExecutionBridgeResult` without the required `materialContextManifestDisposition` field that the gateway interface declares non-optional. The defect is entirely test-side; no production source is mistyped. | LOCALLY_REPAIRABLE |
| full non-live suite | Route authorization moved to `authorizeRouteGovernanceProof`, while affected route tests still arrange only the older session-mock shape and default the session to null, so routes correctly fail closed with 401 and assertions expecting 200/400/403 fail. Remaining failures include count and threshold assertions that require per-file diagnosis. | LIKELY_REPAIRABLE_PENDING_PER_FILE_DIAGNOSIS |
| build | Failure arises from Auth.js environment validation during page-data collection, which depends on environment and credential state that remains parked and unauthorized. | NOT_REPAIRABLE_WITHOUT_PARKED_AUTHORITY |

These are dispatch-time source findings, not a guarantee. The worker must
re-derive each root cause from current source and report any divergence.

## Waived Criterion Disposition Contract

Each of the three criteria must terminate in exactly one disposition, with
evidence:

- `REPAIRED_AND_GREEN`: the criterion now passes, proven by a fresh command
  transcript and an exact before/after count.
- `PARTIALLY_REPAIRED_WITH_NAMED_RESIDUAL`: measurable improvement with every
  remaining failure named, counted and root-caused.
- `FRESHLY_ADJUDICATED_BLOCKED`: the criterion cannot be repaired inside the
  authorized manifest and parked authority, with the exact blocking condition,
  the authority that would be required, and why that authority is not open.

`WAIVED`, `ACCEPTED_AS_IS`, and any relabeling of a failing command as PASS are
forbidden dispositions. A criterion that improves but is not green must not be
reported as green.

## Safe Command Discipline

R5 recorded six unintended provider calls caused by a required command that was
unsafe under ambient credentials. This baseline therefore fixes the following
rules for R1C:

- LPF `npm test` is FORBIDDEN in this tranche. The LPF package suite must be
  invoked only with the explicit provider-test exclusion.
- cvf-web `npm run test:run` is permitted because its script already excludes
  both live test extensions.
- `npm run test:live`, `npm run test:e2e`, any Playwright command, any command
  matching a provider or live test pattern, and any credential-bearing
  invocation are FORBIDDEN.
- `npm run build` is FORBIDDEN as a required command. Build adjudication is
  documentary, based on committed R1 evidence and current source inspection.
- If the worker finds that a permitted command still selects a provider test,
  it must stop, return `BLOCKED_WITH_REASON`, and disclose any call made.

## Exact Worker Manifest

The worker may edit or create exactly these paths:

1. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/provider-binding.test.ts`
2. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.test.ts`
3. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.test.ts`
4. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.governance-trace.test.ts`
5. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.knowledge.test.ts`
6. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/governance/override/route.governance.test.ts`
7. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/knowledge/ingest/route.test.ts`
8. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/knowledge/ingest/w116-cp5-delta.test.ts`
9. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/intake/route.governance.test.ts`
10. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.test.ts`
11. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/qbs/front-door-clarification/route.test.ts`
12. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/guard-runtime-adapter.test.ts`
13. `docs/reviews/CVF_EAFR_R1C_WAIVED_PACKAGE_DEBT_REPAIR_AND_ADJUDICATION_WORKER_RETURN_2026-08-25.md`

Paths 1 through 12 are exactly the twelve files that currently fail typecheck
or the non-live suite. Path 13 is the worker return.

## Production Source Protection Rule

R1C is a test-side repair tranche. If a failing test proves a real production
defect, the worker must not fix production source under this manifest. It must
record the finding, mark that criterion
`PARTIALLY_REPAIRED_WITH_NAMED_RESIDUAL` or `FRESHLY_ADJUDICATED_BLOCKED`, and
return for a separate source-verified authorization. Changing a test assertion
to match incorrect production behavior is forbidden and is treated as a
weakened-admission defect.

## Baseline Decision / Proposed Tranche

Dispatch one exact thirteen-path, no-commit local tranche. Any need for a
production source edit, a checker, package manifest, configuration, environment
or credential change, a build or live command, or a path outside this manifest
returns blocked to the orchestrator.

## Evidence / Verification

The worker must return: fresh before/after typecheck error counts; fresh
before/after non-live suite counts with the failing-file list; a per-criterion
disposition from the contract above; per-file root causes for every repaired
and every residual failure; exact changed paths; pinned input hashes; the
worker-return fast gate; unchanged HEAD; empty staging; and an explicit
zero-provider-call statement. The reviewer independently recomputes all
material proof.

## Risk / Rollback

Primary risk is a test edit that hides a real production defect by weakening an
assertion, or a report that presents partial improvement as green. Secondary
risk is an unsafe command selecting provider tests. Rollback is the exact
thirteen-path pending worker diff.

## Claim Boundary

This baseline authorizes only bounded local test-side repair, deterministic
re-measurement, and fresh adjudication of the three waived criteria. It
authorizes no production source edit, no configuration, package manifest,
checker or environment change, no build, live, provider, network or credential
action, no public sync, no deployment, no push, no R6 and no RFR work. It does
not relax any R2 through R6 acceptance criterion and creates no waiver
precedent.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance package-debt remediation; public-sync is separately
governed and not authorized.
