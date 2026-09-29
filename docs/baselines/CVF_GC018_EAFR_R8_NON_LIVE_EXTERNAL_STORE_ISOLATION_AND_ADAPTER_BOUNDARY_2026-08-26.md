# CVF GC-018 Baseline - EAFR-R8 Non-Live External Store Isolation And Adapter Boundary

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: EAFR-R8-EXTERNAL-STORE-ISOLATION

Dispatch base head: `c1a8747cbc70c5d5a8ab9feffee2643509d8e5eb`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator through the committed EAFR roadmap

Reviewer owner: current independent orchestrator/reviewer

Worker target: external-store isolation worker role

providerExecutionAuthority: FORBIDDEN

## Purpose

Stop the non-live suite from reaching an ambient external store, and close the
adapter's unguarded fetch-injection residual, so that a default test run proves
behavior against injected fakes rather than against live infrastructure.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id EAFR-R8 --title "Non Live External Store Isolation And Adapter Boundary" --date 2026-08-26 --base c1a8747cb --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | source-verified failure classification, injected-fake proof contract, adapter boundary contract and egress-invariant preservation rule |
| checkerReadAheadConfirmation | dispatch, authority, trace, delta, epistemic and worker-return checker sources reviewed |
| docOnlyNewFields | External Store Isolation Contract; Adapter Boundary Contract; Egress Invariant Preservation Rule |
| claimBoundary | dispatch authoring only; no live, provider, network, credential, build or public claim |

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| EAFR-R7 blocked closure | `docs/reviews/CVF_EAFR_R7_FAIL_CLOSED_PROVIDER_EGRESS_AUTHORITY_REPAIR_COMPLETION_2026-08-26.md`; material commit `74cf99354` | RELEASED |
| R7 corrective scope statement | same review, Risk / Corrective Action naming exactly two R8 controls | ACCEPT |
| EAFR-R6 reconciliation | `docs/reviews/CVF_EAFR_R6_CLOSURE_RECONCILIATION_AND_RFR_RESUME_DECISION_COMPLETION_2026-08-26.md` | ACCEPT |
| EAFR roadmap authority | `docs/roadmaps/CVF_EAFR_REMEDIATION_ROADMAP_2026-08-25.md` | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`external store isolation`, role=`worker`, lifecyclePhase=`implementation`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "external store isolation" --role worker --lifecycle-phase implementation` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | none |
| Dispatch impact | ordinary CVF controls apply |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_subagent_provider_execution_authority.py`; `governance/compat/check_equivalence_claim_evidence.py` |
| literalTokensReviewed | Source Verification Block; Current Runtime Freshness Verification; exact manifest; no-commit status; trace labels; Public Export Disposition; providerExecutionAuthority declaration; equivalence disposition tokens |
| gateRunPurpose | confirm as evidence that the source-verified dispatch already matches required shape |
| claimBoundary | structural conformance does not prove the isolation is complete |

## Current Runtime Freshness Verification

Verified directly at HEAD `c1a8747cbc70c5d5a8ab9feffee2643509d8e5eb` on
2026-08-26, after R7 material closure:

- the R7 fail-closed guard is retained. It classifies by destination, derives
  provider endpoints from gateway constants, permits only loopback and
  non-egress protocols without a grant, and denies every unrecognised hostname
  before network I/O;
- the non-live suite reports 3553 tests with 88 failures across 16 files;
- 72 of those 88 failures carry the identical denial reason,
  `unrecognised egress destination balanced-shrew-118656.upstash.io`. That is
  an ambient Upstash Redis REST host, not a provider endpoint;
- the Web local env file supplies `UPSTASH_REDIS_REST_URL` and
  `UPSTASH_REDIS_REST_TOKEN`, and the shared test setup loads that file into the
  process environment, so the credentials are present in ordinary local runs;
- `createRedisClientFromEnv` in `src/lib/rate-limit.ts` constructs a live
  Upstash client whenever both variables are present, with no test-mode
  suppression;
- a `redisClient` injection seam already exists on `RateLimiterOptions`, so
  isolation can be achieved by using an existing seam rather than by adding new
  plumbing;
- `src/lib/storage-adapter.ts` also imports the Upstash client and is a second
  external-store surface in the same class;
- the OpenAI-compatible adapter calls a caller-injected `fetchImpl` directly.
  Because the R7 guard wraps `globalThis.fetch`, an injected fetch is never
  observed by the guard. This is the accepted R7 adapter residual, and it is
  unchanged at this head;
- the remaining 16 failures are the previously named PVV provider denials and
  BuildAuthority residuals, which R8 does not own.

No live, provider, network, credential or build command is authorized by this
baseline. R8 changes local test isolation and one adapter boundary; it claims no
provider, deployment, release or production posture.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| R8 is scoped to exactly two controls | ROADMAP_AUTHORITY | `docs/reviews/CVF_EAFR_R7_FAIL_CLOSED_PROVIDER_EGRESS_AUTHORITY_REPAIR_COMPLETION_2026-08-26.md` | Risk / Corrective Action | EAFR-R8 | R7 completion review | ACCEPT |
| the adapter fetch-injection residual is accepted and open | OWNER_AUTHORITY | `docs/reviews/CVF_EAFR_R7_FAIL_CLOSED_PROVIDER_EGRESS_AUTHORITY_REPAIR_COMPLETION_2026-08-26.md` | R6 row disposition table | BOUNDED_WITH_ACCEPTED_RESIDUAL | R7 completion review | ACCEPT |
| the guard denies unrecognised destinations before network I/O | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/provider-execution-guard.ts` | destination classifier default branch | classifyDestination | cvf-web provider execution guard | ACCEPT |
| the shared setup loads local env values into the process | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/setup.ts` | module-scope setup calls | loadLocalEnvFiles | cvf-web test setup | ACCEPT |
| a live Redis client is constructed from ambient environment values | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/rate-limit.ts` | client construction helper | createRedisClientFromEnv | cvf-web rate limiter | ACCEPT |
| an injection seam already exists for the Redis client | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/rate-limit.ts` | rate limiter options type | RateLimiterOptions | cvf-web rate limiter | ACCEPT |
| a second external-store surface imports the same client | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/storage-adapter.ts` | Upstash import and Redis adapters | RedisEventListAdapter | cvf-web storage adapter | ACCEPT |
| the adapter calls a caller-injected fetch the guard cannot observe | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_MODEL_GATEWAY/src/openai-compatible-execute-adapter.ts` | adapter execution body | fetchImpl | OpenAI-compatible execute adapter | ACCEPT |

## External Store Isolation Contract

The non-live suite must not reach any external store. Isolation must be proven
by an injected fake, never by unsetting a variable in one shell.

1. **Injected fake proof.** A default non-live run must exercise the rate-limit
   and storage paths against an injected in-process fake, with a focused test
   proving the fake is used and no external client is constructed.
2. **No ambient auto-construction.** Constructing a live external client from
   ambient environment values must not happen during a non-live run. A shell
   that merely lacks the variable is not evidence, because the shared setup
   loads the local env file.
3. **Fail-closed preference.** Where a non-live run would otherwise construct a
   live client, the correct behavior is to use the fake or to fail closed, never
   to silently proceed.
4. **Deliberate live use preserved.** A live external store must remain usable
   under an explicit, deliberate opt-in, exactly as live provider tests are.

## Adapter Boundary Contract

The adapter's injected `fetchImpl` bypasses the guard because the guard wraps
the global fetch. R8 must close this so that an injected fetch cannot become an
unobserved egress path.

Acceptable dispositions, in preference order:

- **CLOSED_BY_GUARDED_INJECTION**: the adapter's injected fetch is routed
  through, or validated by, the same destination classification the guard uses,
  so an unrecognised destination is denied regardless of injection.
- **CLOSED_BY_CONSTRAINT**: the adapter rejects an endpoint that does not
  classify as a permitted destination, independently of which fetch is injected.
- **BOUNDED_WITH_NAMED_RESIDUAL**: neither is achievable inside the manifest,
  with the exact blocking condition and the authority required stated.

`ACCEPTED_AS_IS` and silent carry-forward are forbidden dispositions. The
residual was already accepted once in R7; R8 exists to close it, so re-accepting
it without new evidence is not a valid outcome.

## Egress Invariant Preservation Rule

The R7 fail-closed default must survive R8 unchanged. Specifically:

- an unrecognised hostname must still be denied before network I/O;
- provider endpoints must still be derived from gateway constants;
- loopback and non-egress protocols must remain the only ungranted permits;
- adding an external-store allowance must not widen provider egress, and must
  not introduce a second permit list that a future endpoint could hide behind.

Any change that would restore silent external egress is a fail condition, not a
trade-off, regardless of how many suite failures it would clear.

## Exact Worker Manifest

1. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/setup.ts`
2. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/rate-limit.ts`
3. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/storage-adapter.ts`
4. `EXTENSIONS/CVF_MODEL_GATEWAY/src/openai-compatible-execute-adapter.ts`
5. `EXTENSIONS/CVF_MODEL_GATEWAY/tests/openai-compatible-execute-adapter.test.ts`
6. `docs/reviews/CVF_EAFR_R8_NON_LIVE_EXTERNAL_STORE_ISOLATION_AND_ADAPTER_BOUNDARY_WORKER_RETURN_2026-08-26.md`

One new focused test file under
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/` is additionally permitted
solely to prove injected-fake isolation, and must be named in the return.

## Baseline Decision / Proposed Tranche

Dispatch one bounded, no-commit tranche over the six manifest paths plus one
permitted focused test. Any need to edit the guard, a package manifest, an
environment file, a checker, a roadmap or a registry, to run a provider or build
command, or to widen provider egress returns blocked to the orchestrator.

## Evidence / Verification

The worker must return: before and after non-live suite totals with the failing
file list; proof that the Upstash destination no longer appears in any denial;
a focused test demonstrating injected-fake use with no external client
construction; one adapter boundary disposition from the contract; proof that the
R7 egress invariants are unchanged, including a negative test that an
unrecognised hostname is still denied; exact changed paths; pinned input hashes;
the worker-return fast gate; unchanged HEAD; empty staging; and an explicit
zero-provider-call and zero-external-store-call statement.

## Risk / Rollback

Primary risk is clearing suite failures by weakening the egress default rather
than by isolating the store. Secondary risk is re-accepting the adapter residual
without new evidence. Rollback is the bounded pending worker diff.

## Claim Boundary

This baseline authorizes only bounded local test isolation, one adapter boundary
closure and deterministic proof. It authorizes no provider, live, network,
credential, build, dependency, environment-file, checker, roadmap, registry,
public-sync, deployment or push action, no RFR resumption, and no BuildAuthority
repair. Isolating a test suite from an external store is not a security proof and
makes no claim about credential hygiene or past traffic.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance test-isolation remediation; public-sync is separately
governed and not authorized.
