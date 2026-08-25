# CVF GC-018 Baseline - EAFR-R1D Non-Live Runner Provider Exclusion

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: EAFR-R1D-NON-LIVE-RUNNER-EXCLUSION

Dispatch base head: `ca1f14add009cae1b8c57b9dbdf8d28eb53d03d3`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator through the committed EAFR roadmap and the accepted
R1C completion review

Reviewer owner: current independent orchestrator/reviewer

Worker target: test-runner boundary worker role

## Purpose

Make the cvf-web non-live test runner structurally incapable of selecting
ambient-key real-provider integration tests, so a command labelled safe cannot
perform provider calls, and reconcile the disclosed five-call incident.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id EAFR-R1D --title "Non-Live Runner Provider Exclusion" --date 2026-08-25 --base ca1f14add --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | source-verified selection-path trace, exact manifest, defense-in-depth exclusion requirement, incident reconciliation contract and safe-command discipline |
| checkerReadAheadConfirmation | dispatch, authority, trace, delta, epistemic and worker-return checker sources reviewed |
| docOnlyNewFields | Verified Provider Selection Path; Exclusion Sufficiency Contract; Incident Reconciliation Requirement |
| claimBoundary | dispatch authoring only; no live, provider, public, deployment, credential or environment claim |

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| EAFR-R1C bounded closure | `docs/reviews/CVF_EAFR_R1C_WAIVED_PACKAGE_DEBT_REPAIR_AND_ADJUDICATION_COMPLETION_2026-08-25.md`; material commit `3c51ac5e6` | RELEASED |
| R1C-RF5 incident finding | same completion review, `R1C-RF5` section; five OpenAI calls disclosed and routed to R1D | ACCEPT |
| EAFR roadmap authority | `docs/roadmaps/CVF_EAFR_REMEDIATION_ROADMAP_2026-08-25.md`, R1C accepted and R1D named as next dispatch | ACCEPT |
| EAFR-R1A predecessor runner fix | `docs/reviews/CVF_EAFR_R1A_NON_LIVE_TEST_RUNNER_EXTENSION_COVERAGE_COMPLETION_2026-08-25.md`; accepted at `ef142bfb2` | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`test runner provider exclusion`, role=`worker`, lifecyclePhase=`implementation`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "test runner provider exclusion" --role worker --lifecycle-phase implementation` |
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
| claimBoundary | structural conformance does not prove the exclusion is sufficient |

## Current Runtime Freshness Verification

Verified directly at HEAD `ca1f14add009cae1b8c57b9dbdf8d28eb53d03d3` on
2026-08-25, after R1C material closure:

- the non-live runner script excludes only `src/**/*.live.test.ts` and
  `src/**/*.live.test.tsx`;
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/providers.integration.test.ts`
  carries no `.live.` segment, so those exclusions do not match it, and the
  vitest `include` glob `src/**/*.{test,spec}.{ts,tsx}` collects it;
- that file selects its OpenAI case through `openaiKey ? it : it.skip` and calls
  the real `executeAI` with no mocked transport, so an available key produces a
  genuine outbound request;
- the key does not need to be present in the invoking shell: the shared setup
  file calls `loadLocalEnvFiles()`, which reads `.env.local` and assigns
  `OPENAI_API_KEY` into `process.env` when the variable is unset or empty;
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/vitest.config.ts` declares no
  `test.exclude` entry, so no config-level guard compensates for the script-level
  gap;
- a targeted survey of non-live test files found exactly one file in this
  exposure class. `src/lib/ai/providers.test.ts` also calls `executeAI`, but it
  stubs `fetch` at module scope and is therefore contained;
- running the non-live suite with the integration file additionally excluded
  produced 312 files and 3527 tests with 2 failures and zero skips, matching the
  corrected reviewer figures, with zero provider calls.

No live, provider, network, credential or build command is authorized by this
baseline. R1D changes test selection only and claims no provider, deployment,
release or production readiness.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| R1D is the authorized next tranche | ROADMAP_AUTHORITY | `docs/reviews/CVF_EAFR_R1C_WAIVED_PACKAGE_DEBT_REPAIR_AND_ADJUDICATION_COMPLETION_2026-08-25.md` | Risk / Corrective Action, corrective lane 1; Reviewer Decision | EAFR-R1D | R1C completion review | ACCEPT |
| five provider calls occurred through a purportedly safe runner | OWNER_AUTHORITY | `docs/reviews/CVF_EAFR_R1C_WAIVED_PACKAGE_DEBT_REPAIR_AND_ADJUDICATION_COMPLETION_2026-08-25.md` | R1C-RF5 section | incident disclosure | R1C completion review | ACCEPT |
| the non-live runner excludes only live-suffix files | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | scripts block, non-live runner entry | scripts non-live test runner entry | cvf-web package manifest | ACCEPT |
| the integration file is collected by the include glob | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/vitest.config.ts` | test block include entry with no exclude entry | include | cvf-web vitest configuration | ACCEPT |
| the OpenAI case activates on an available key and calls the real provider | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/providers.integration.test.ts` | ambient key constants and OpenAI case | testOpenAI; executeAI | cvf-web provider integration test | ACCEPT |
| the shared setup injects local env values into the process environment | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/setup.ts` | module-scope setup call | loadLocalEnvFiles | cvf-web test setup | ACCEPT |
| local env loading assigns keys when unset or empty | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/load-local-env.ts` | default env file list and assignment branch | loadLocalEnvFiles; DEFAULT_ENV_FILES | cvf-web local env loader | ACCEPT |
| the sibling provider unit test is contained by a module-scope transport stub | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/providers.test.ts` | module-scope global stub | fetchMock | cvf-web provider unit test | ACCEPT |
| the predecessor runner fix covered only file-extension coverage | OWNER_RECONCILIATION | `docs/reviews/CVF_EAFR_R1A_NON_LIVE_TEST_RUNNER_EXTENSION_COVERAGE_COMPLETION_2026-08-25.md` | accepted scope | non-live runner extension coverage | R1A completion review | ACCEPT |

## Verified Provider Selection Path

```text
non-live runner script
  -> vitest include glob collects every *.test.ts under src
  -> live-suffix exclusions do not match providers.integration.test.ts
  -> shared setup runs loadLocalEnvFiles()
  -> .env.local supplies OPENAI_API_KEY into process.env
  -> ambient-key ternary activates the OpenAI case instead of skipping
  -> real executeAI call with unmocked transport
  -> outbound provider request
```

Every step in this chain was read from source at the dispatch head. Breaking any
single step prevents the call; the Exclusion Sufficiency Contract requires
breaking more than one.

## Exclusion Sufficiency Contract

A naming convention alone is not a provider boundary. R1D must satisfy defense
in depth, so that no single future rename, new file, or script edit silently
restores provider selection:

1. **Selection barrier.** The non-live runner must not collect real-provider
   integration tests, enforced where selection happens rather than only in one
   script string.
2. **Activation barrier.** A real-provider case must not activate merely because
   an ambient key exists; it must require an explicit, deliberate opt-in signal
   that the non-live path never sets.
3. **Evidence.** The worker must show the file is not collected by the non-live
   runner and that the safe suite totals match the corrected R1C figures.

Satisfying only the selection barrier is insufficient and must be reported as a
partial result, not as a completed exclusion.

## Incident Reconciliation Requirement

The worker must reconcile the disclosed five-call incident in the return:
restate the count and its four attributed sources from the R1C completion
review, confirm from source whether the same path could still fire after the
change, and state explicitly that R1D grants no repeat-live authority and
performs zero provider calls of its own. The worker must not attempt to verify
the fix by making a provider call, and must not treat the absence of a key in
one shell as proof of safety, because the setup file supplies the key
independently of the shell.

## Exact Worker Manifest

The worker may edit or create exactly these paths:

1. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json`
2. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/vitest.config.ts`
3. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/providers.integration.test.ts`
4. `docs/reviews/CVF_EAFR_R1D_NON_LIVE_RUNNER_PROVIDER_EXCLUSION_WORKER_RETURN_2026-08-25.md`

Paths 1 and 2 are the selection surfaces. Path 3 is the activation surface.
Path 4 is the worker return. A file rename inside path 3's directory is
permitted only if the resulting path is recorded as a rename in the return and
no other file is created.

## Package Manifest Edit Exception

R1C forbade package manifest edits because its scope was test-side repair. R1D
is explicitly authorized to edit the cvf-web package manifest and vitest
configuration, because the defect lives in test selection itself. This
authorization is bounded to the non-live runner and provider-exclusion
semantics. It does not authorize dependency changes, version bumps, lockfile
edits, new scripts unrelated to provider exclusion, or any change to the live
runner's ability to run real provider tests when deliberately invoked.

## Baseline Decision / Proposed Tranche

Dispatch one exact four-path, no-commit local tranche. Any need for a production
source edit outside the named test surfaces, a dependency or lockfile change, a
credential, build, live or provider command, or a path outside this manifest
returns blocked to the orchestrator.

## Evidence / Verification

The worker must return: proof that the non-live runner no longer collects the
integration file; proof that the activation gate now requires explicit opt-in;
fresh safe-suite totals compared against the corrected R1C figures of 312 files,
3527 tests, 2 failures and zero skips; confirmation that the two failures remain
the known BuildAuthority residuals and no new failure appeared; the preserved
ability to run real provider tests deliberately; exact changed paths; pinned
input hashes; the worker-return fast gate; unchanged HEAD; empty staging; and an
explicit zero-provider-call statement.

## Risk / Rollback

Primary risk is a change that appears to exclude provider tests while leaving a
second selection path open, or one that disables deliberate live testing
altogether. Secondary risk is verifying the fix by making a provider call.
Rollback is the exact four-path pending worker diff.

## Claim Boundary

This baseline authorizes only bounded local test-selection and activation
hardening plus incident reconciliation. It authorizes no provider, live,
network, credential, build, dependency, lockfile, deployment, public-sync or
push action, no production runtime change, no BuildAuthority work, no R6 and no
RFR work. Excluding a provider test from a runner is not a security proof and
makes no claim about credential hygiene, past call content, or provider account
state.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance test-runner remediation; public-sync is separately
governed and not authorized.
