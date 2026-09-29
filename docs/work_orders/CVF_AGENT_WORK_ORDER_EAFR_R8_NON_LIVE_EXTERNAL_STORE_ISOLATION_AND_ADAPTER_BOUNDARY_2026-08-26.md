# CVF Agent Work Order - EAFR-R8 Non Live External Store Isolation And Adapter Boundary

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Work order ID: EAFR-R8

Date: 2026-08-26

dispatchBaseHead: `c1a8747cbc70c5d5a8ab9feffee2643509d8e5eb`

executionBaseHead: worker must capture actual HEAD and require this committed packet as ancestor

closureBaseHead: reviewer captures the committed dispatch head

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator through the committed EAFR roadmap

Reviewer/closer: current independent orchestrator/reviewer

Worker: external-store isolation worker role

## Dispatch Prompt Envelope

Batch ID: EAFR-R8-EXTERNAL-STORE-ISOLATION.

Role: no-commit external-store isolation worker.

Canonical packet: this committed work order and its paired baseline.

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

providerExecutionAuthority: FORBIDDEN

R8 isolates the non-live suite from external stores and closes one adapter
boundary. It makes no provider call, so no orchestrator provider grant is
requested, issued or consumed.

Current-time notes: R7 is accepted `CLOSED_BLOCKED` at material commit
`74cf99354`; the fail-closed egress guard is retained; the Upstash and adapter
residuals were verified at dispatch head `c1a8747cb`.

Do-not-misread notes: clearing suite failures is not the goal. Isolating the
suite from live infrastructure is the goal. Weakening the R7 egress default to
make failures disappear is a fail condition, not a solution. Re-accepting the
adapter residual without new evidence is not a valid outcome.

Required first actions: read startup surfaces, guard orientation, literal
gotchas, `DESIGN.md`, this packet, paired baseline, the R7 completion review,
every pinned input and the applicable checker sources for every output class.

Return contract: the exact manifest paths plus at most one permitted focused
test, no stage/commit, `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

Worker return path: `docs/reviews/CVF_EAFR_R8_NON_LIVE_EXTERNAL_STORE_ISOLATION_AND_ADAPTER_BOUNDARY_WORKER_RETURN_2026-08-26.md`

sourceAuthority: paired GC-018 baseline, committed EAFR roadmap, accepted R7 completion review, and source-verified cvf-web and gateway files named in this packet

## Purpose

Stop the non-live suite from reaching an ambient external store, prove isolation
with an injected fake, and close the adapter's unguarded fetch-injection
residual, without weakening the R7 fail-closed egress default.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id EAFR-R8 --title "Non Live External Store Isolation And Adapter Boundary" --date 2026-08-26 --base c1a8747cb --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | source-verified failure classification, injected-fake proof contract, adapter boundary disposition set and egress invariant preservation rule |
| checkerReadAheadConfirmation | applicable dispatch and worker-output checker sources read |
| docOnlyNewFields | External Store Isolation Contract; Adapter Boundary Contract; Egress Invariant Preservation Rule |
| claimBoundary | dispatch authoring only |

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| R7 blocked closure | `docs/reviews/CVF_EAFR_R7_FAIL_CLOSED_PROVIDER_EGRESS_AUTHORITY_REPAIR_COMPLETION_2026-08-26.md`; material commit `74cf99354` | ACCEPT |
| R7 corrective scope statement | same review, Risk / Corrective Action naming exactly two R8 controls | ACCEPT |
| R6 reconciliation | `docs/reviews/CVF_EAFR_R6_CLOSURE_RECONCILIATION_AND_RFR_RESUME_DECISION_COMPLETION_2026-08-26.md` | ACCEPT |
| EAFR roadmap authority | `docs/roadmaps/CVF_EAFR_REMEDIATION_ROADMAP_2026-08-25.md` | ACCEPT |

## Authority And Scope

Governing baseline:
`docs/baselines/CVF_GC018_EAFR_R8_NON_LIVE_EXTERNAL_STORE_ISOLATION_AND_ADAPTER_BOUNDARY_2026-08-26.md`.

The worker may edit or create exactly the paths in Write Ownership. No other
path is writable. The worker must not stage or commit.

## Authority Chain

Operator EAFR authority -> committed roadmap -> accepted R7 closure -> paired
baseline -> this work order -> no-commit worker -> independent reviewer/closer.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
| --- | --- | --- | --- | --- |
| non-live ambient external-store isolation | External Store Isolation Contract | rate limiter, storage adapter, setup and focused test | before/after suite totals and denial-reason search | PASS |
| injected fake Redis proof | Required Implementation, Control A | permitted focused test | focused Vitest run | PASS |
| adapter fetch-injection closure | Adapter Boundary Contract | OpenAI-compatible adapter | focused adapter tests and disposition | PASS |
| preserve fail-closed egress | Egress Invariant Preservation Rule | unchanged guard behavior | negative denial test | PASS |

## Required First Reads

Read `AGENTS.md`, `CVF_SESSION_MEMORY.md`, the bootstrap read model, active
handoff, `docs/reference/guard_orientation/README.md`, governed literal gotchas,
`DESIGN.md`, paired baseline, this work order, the R7 completion review, every
pinned source and worker-output checker sources named below. Resolve the full
session registry only for a targeted missing or contradictory fact.

## Agent Roles

Operator owns scope; dispatcher owns the packet; worker isolates, closes and
proves without commit; reviewer independently challenges, repairs, closes and
commits.

## Pre-Flight Checks

Confirm clean worktree, empty staging, actual HEAD, committed dispatch ancestry,
all pinned hashes, absent worker-return path and zero live-test selection.
Capture the before-state suite totals and the failing file list before any edit.
Hash drift or an existing return path blocks before edits.

## Write Ownership

Exactly these six paths:

1. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/setup.ts`
2. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/rate-limit.ts`
3. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/storage-adapter.ts`
4. `EXTENSIONS/CVF_MODEL_GATEWAY/src/openai-compatible-execute-adapter.ts`
5. `EXTENSIONS/CVF_MODEL_GATEWAY/tests/openai-compatible-execute-adapter.test.ts`
6. `docs/reviews/CVF_EAFR_R8_NON_LIVE_EXTERNAL_STORE_ISOLATION_AND_ADAPTER_BOUNDARY_WORKER_RETURN_2026-08-26.md`

One new focused test file under
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/` is additionally permitted
solely to prove injected-fake isolation. Its exact path must be named in the
return. No second new file may be created.

Forbidden: editing `provider-execution-guard.ts`, any package manifest, any
vitest or tsconfig configuration, any environment file, any checker, roadmap,
registry, session, baseline, work order, adapter outside paths 4-5, public clone or
deployment path.

## Pinned Input Hashes

| Path | SHA-256 |
| --- | --- |
| `docs/roadmaps/CVF_EAFR_REMEDIATION_ROADMAP_2026-08-25.md` | `0f2df429fe34457e0e0d6188584a9085a49bf49a18986c1ab2553ec3d64cb96a` |
| `docs/reviews/CVF_EAFR_R7_FAIL_CLOSED_PROVIDER_EGRESS_AUTHORITY_REPAIR_COMPLETION_2026-08-26.md` | `41b4180458ee1249778f88931ec3b0051d414f13bbf0941e1edbcff921a1d8e1` |
| `docs/reviews/CVF_EAFR_R6_CLOSURE_RECONCILIATION_AND_RFR_RESUME_DECISION_COMPLETION_2026-08-26.md` | `b3f3c721f44d670e6dee4c16c32170c0ecabf88d79aff71e0a8ce5de53450cf4` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/provider-execution-guard.ts` | `2e4f869bb6d912db9a480b0d178be62bce457991f90f485da13d13f72bc237f5` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/setup.ts` | `c44389e06b51f602a64ee719fda2d463021d68242a7626a0de05a93a1f5c994b` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/rate-limit.ts` | `3d0bd39f2f45e734bc9b87351ccce810a1d9854208789f1d775e072aae563ad5` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/storage-adapter.ts` | `d57ea274ac95235ef15fd3d577c8141ba27458576810acb654f505db83a119e6` |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/openai-compatible-execute-adapter.ts` | `22f264e8e3a8b6cb74d74fad8ae353a6d052a0a4fa2442a7581bcd69169d53c4` |
| `EXTENSIONS/CVF_MODEL_GATEWAY/tests/openai-compatible-execute-adapter.test.ts` | `5b26a8c2898a005dfbdf3fd763e3eda1ebadfc1e4cf5c8e2ab640ba5010eaaf6` |

The new worker-return path must be absent. Every hash is calculated at
`c1a8747cb`; mismatch returns `BLOCKED_WITH_REASON` before material edits.

## Verified Failure Classification

Verified at dispatch head. The worker must re-derive and report divergence:

| Class | Count | Evidence | R8 ownership |
| --- | --- | --- | --- |
| Ambient Upstash egress denials | 72 | identical denial reason naming an Upstash REST host | OWNED |
| PVV provider denials | 20 | previously named real-provider benchmark | NOT_OWNED |
| BuildAuthority residuals | 2 | previously named guard block | NOT_OWNED |

Total non-live failures at dispatch head: 88 across 16 files, out of 3553 tests.
R8 owns only the 72-failure class. Clearing the other 16 is out of scope, and
reporting them as cleared would be false.

## Verified Root Cause

- the Web local env file supplies `UPSTASH_REDIS_REST_URL` and
  `UPSTASH_REDIS_REST_TOKEN`;
- the shared test setup loads that file into `process.env`, so the credentials
  are present in ordinary local runs regardless of the invoking shell;
- `createRedisClientFromEnv` constructs a live Upstash client whenever both
  values are present, with no test-mode suppression;
- the R7 guard then denies the resulting request because the Upstash host is not
  a recognised destination;
- a `redisClient` seam already exists on `RateLimiterOptions`, so isolation can
  reuse an existing seam rather than add plumbing;
- `storage-adapter.ts` imports the same client and is a second surface in the
  same class.

## External Store Isolation Contract

The non-live suite must not reach any external store. Isolation must be proven
by an injected fake, never by unsetting a variable in one shell.

1. **Injected fake proof.** A default non-live run must exercise the rate-limit
   and storage paths against an injected in-process fake, with a focused test
   proving the fake is used and no external client is constructed.
2. **No ambient auto-construction.** Constructing a live external client from
   ambient environment values must not happen during a non-live run. A shell
   lacking the variable is not evidence, because the shared setup loads the
   local env file.
3. **Fail-closed preference.** Where a non-live run would otherwise construct a
   live client, use the fake or fail closed; never silently proceed.
4. **Deliberate live use preserved.** A live external store must remain usable
   under an explicit, deliberate opt-in, exactly as live provider tests are. A
   change that makes live external-store use impossible under any invocation is
   over-correction and must be returned blocked.

## Adapter Boundary Contract

The adapter's injected `fetchImpl` bypasses the guard because the guard wraps the
global fetch. Close this so an injected fetch cannot become unobserved egress.

Acceptable dispositions, in preference order:

- **CLOSED_BY_GUARDED_INJECTION**: the injected fetch is routed through, or
  validated by, the same destination classification the guard uses, so an
  unrecognised destination is denied regardless of injection.
- **CLOSED_BY_CONSTRAINT**: the adapter rejects an endpoint that does not
  classify as a permitted destination, independently of which fetch is injected.
- **BOUNDED_WITH_NAMED_RESIDUAL**: neither is achievable inside the manifest,
  with the exact blocking condition and the authority required stated.

`ACCEPTED_AS_IS` and silent carry-forward are forbidden. The residual was
accepted once in R7; R8 exists to close it, so re-accepting it without new
evidence is not a valid outcome.

If closing the boundary requires importing classification logic that currently
lives only in the cvf-web test guard, the worker must not copy that logic into a
second permit list. It must either import a shared source or return
`BOUNDED_WITH_NAMED_RESIDUAL` naming the missing shared surface.

### Provider registry accounting for this boundary

`EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` is a provider
registration and routing class and `PROVIDER_CAPABILITY_REGISTRY` supplies
provider, model and method. Neither declares a hostname, so neither can decide
whether an adapter endpoint is a permitted destination. This was established in
R6 and is the reason the R7 guard derives destinations from gateway endpoint
constants instead.

The worker must therefore not close this boundary by checking a `providerId`
against either registry: a covered provider identity can still carry an
uncovered endpoint, which is the exact false green R6 recorded. Destination
classification must remain keyed by endpoint, and the two registry surfaces are
deliberately not used for coverage decisions here.

## Egress Invariant Preservation Rule

The R7 fail-closed default must survive R8 unchanged:

- an unrecognised hostname must still be denied before network I/O;
- provider endpoints must still be derived from gateway constants;
- loopback and non-egress protocols must remain the only ungranted permits;
- an external-store allowance must not widen provider egress and must not create
  a second permit list a future endpoint could hide behind.

Any change that would restore silent external egress is a fail condition
regardless of how many suite failures it clears. `provider-execution-guard.ts`
is not writable in this tranche.

## Required Implementation

### Control A - non-live external store isolation

- Prevent ambient construction of a live external client during a non-live run,
  using the existing injection seam where one exists.
- Provide an in-process fake sufficient for the rate-limit and storage paths the
  suite exercises.
- Add one focused test proving the fake is used and that no external client is
  constructed under ambient credentials.
- Preserve deliberate live external-store use under an explicit opt-in.
- Do not edit the environment file and do not remove the credentials.

### Control B - adapter boundary closure

- Close the injected-fetch bypass per the Adapter Boundary Contract.
- Preserve the adapter's existing behavior for permitted destinations; this is a
  boundary addition, not a behavioral rewrite.
- Add or extend focused adapter tests proving an unrecognised destination is
  denied even when a permissive fetch is injected.
- Assign exactly one disposition from the contract.

## Adversarial Proof Matrix

| Vector | Boundary under test | Required result |
| --- | --- | --- |
| suite failures cleared by widening the egress permit list | egress invariant | forbidden; fail condition |
| Upstash host added to the guard's permitted destinations | manifest boundary | forbidden; guard is not writable |
| isolation claimed from an empty shell environment | isolation contract | forbidden; setup loads the env file |
| live external store made impossible under any invocation | over-correction rule | forbidden; blocked return |
| adapter residual re-accepted without new evidence | adapter contract | forbidden; not a valid disposition |
| classification logic copied into a second permit list | shared-source rule | forbidden; import or return bounded |
| the 16 out-of-scope failures reported as cleared | scope honesty | forbidden; R8 owns only the 72-failure class |
| provider or external-store call made during verification | zero-call rule | forbidden; blocked return with disclosure |

## Acceptance Criteria

- only the authorized paths plus at most one named new focused test changed;
- the Upstash destination appears in zero denial reasons after the change;
- a focused test proves injected-fake use with no external client construction;
- deliberate live external-store use remains possible under explicit opt-in;
- exactly one adapter boundary disposition, not `ACCEPTED_AS_IS`;
- R7 egress invariants unchanged, proven by a negative denial test;
- the 16 out-of-scope failures reported honestly as still failing;
- zero provider calls and zero external-store calls, explicitly stated;
- worker-return fast gate passes; staging empty; worker HEAD unchanged.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "EAFR-R8",
  "requestedProfile": "P3_ELEVATED",
  "classification": {
    "taskKind": "PURE_LOCAL_IMPLEMENTATION",
    "authorityImpact": "USES_EXISTING_OWNER",
    "externalEffect": "LOCAL_REVERSIBLE",
    "dataSensitivity": "PRIVATE_REPO",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "NAMED_FILES",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "KNOWN_PATTERN"
  },
  "pathFamilies": [
    "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/",
    "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/",
    "EXTENSIONS/CVF_MODEL_GATEWAY/src/openai-compatible-execute-adapter.ts",
    "EXTENSIONS/CVF_MODEL_GATEWAY/tests/openai-compatible-execute-adapter.test.ts",
    "docs/reviews/",
    "docs/baselines/CVF_GC018_EAFR_R8_NON_LIVE_EXTERNAL_STORE_ISOLATION_AND_ADAPTER_BOUNDARY_2026-08-26.md"
  ],
  "claims": ["the non-live suite is isolated from ambient external stores and the adapter injected-fetch bypass is closed"],
  "requiredProof": ["before/after suite totals", "zero Upstash denial reasons", "injected fake focused test", "adapter boundary disposition", "egress invariant negative test", "hashes", "worker-return fast gate", "independent review"],
  "operatorCheckpoints": [],
  "forbiddenEffects": ["guard edit", "package manifest or config edit", "environment file edit", "provider or external-store call", "widening egress permits", "worker stage or commit", "public/deploy/push"],
  "sourceEvidence": {"selectedFilesFullyRead": true, "corpusReceiptRef": null, "completenessClaimChanged": false}
}
```

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| selected role route | MULTI_AGENT_MULTI_ROLE |
| worker role | no-commit external-store isolation worker |
| reviewer role | independent reviewer/closer |
| external intake | none; all claims verified in CVF-owned sources |
| escalation condition | hash drift, a required guard or config edit, inability to close the adapter boundary inside the manifest, any external call, or a needed extra path |
| risk sensitivity | preserving fail-closed egress while removing live-store dependence |
| scope classification | bounded six-path local isolation plus one permitted focused test |

## Required Commands

Run from cvf-web:

1. `npm run test:run` before edits, capturing exact totals and failing files;
2. `npm run test:run` after edits;
3. focused runs of the new isolation test and any changed rate-limit or storage
   tests;
4. `npm run check`.

Run from the model gateway package:

5. focused adapter tests covering the boundary change;
6. the gateway package type check.

Run from repository root:

7. a denial-reason search proving the Upstash destination no longer appears;
8. bounded searches proving the guard, package manifests, configuration and
   environment files were not modified;
9. recompute pinned hashes for all inputs outside the worker manifest;
10. `python governance/compat/run_worker_return_fast_gate.py`;
11. `git diff --check`, `git diff --name-status`,
    `git status --short --untracked-files=all`, and
    `git diff --cached --name-only`.

Do not run `npm run build`, LPF `npm test`, `npm run test:live`, Playwright, any
provider, network, credential, release-gate, public-sync, deployment or
installation command. Do not run any command whose purpose is to contact the
external store.

## Execution Plan

1. Capture startup, clean status, empty staging, HEAD, ancestry, return-path
   absence, pinned hashes and before-state suite totals.
2. Implement Control A and prove isolation with the focused test.
3. Implement Control B and assign its disposition.
4. Re-measure the suite and confirm the Upstash class is cleared while the 16
   out-of-scope failures remain reported.
5. Prove the R7 egress invariants are unchanged, write the worker return, run
   every safe command, and return without staging or committing.

## Verification Commands

Run every Required Command, including the full:

`python governance/compat/run_worker_return_fast_gate.py`

Individual checker substitution is forbidden.

## Evidence Requirements

Report pre/post HEAD and status; exact changed paths including the named new
test; before/after suite totals and failing file lists; the denial-reason search
result; the injected-fake proof; the adapter disposition; the egress invariant
negative test; positive/negative search counts; non-manifest source hashes;
worker-return fast gate output; empty staging; an explicit zero-provider-call and
zero-external-store-call statement; and explicit zero external-effect evidence.
Failed, skipped, timed-out or ambiguous commands stay visible and cannot be
relabeled as passing.

## Fail Conditions

Return `BLOCKED_WITH_REASON` for hash drift, a required guard or configuration
edit, an inability to close the adapter boundary without copying classification
logic, any provider or external-store call, a needed extra path beyond the one
permitted test, loss of deliberate live external-store capability, or any change
that would restore silent external egress.

## Worker Autonomy / No-Question Rule

Implement and prove both controls without asking the operator. Do not expand
scope. If Control B cannot be closed inside the manifest, return
`BOUNDED_WITH_NAMED_RESIDUAL` for that control with the blocking condition
named, and keep Control A's result honest rather than inflating it.

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

recomputeReason: R8 changes test isolation and one adapter boundary, so suite totals, denial reasons, focused proofs, hashes and boundary searches must be fresh against the pending worker tree

priorVerificationArtifact: accepted R7 completion review and R6 reconciliation

priorVerificationAnchor: pinned SHA-256 values in this work order

freshRecomputeRequired: before/after suite totals, denial-reason search, focused isolation and adapter tests, typechecks, hashes and boundary searches

unicodePathHandling: use literal repository-relative paths and UTF-8-safe readers

extractedTextAuthority: CVF-governed sources and fresh local command output only

## Current Runtime Freshness Verification

Direct inspection at `c1a8747cb` confirms the retained fail-closed guard, 88
non-live failures of which 72 name a single ambient Upstash host, credentials
supplied by the Web local env file and loaded by the shared setup, ambient
client construction with an existing injection seam, a second external-store
surface, and an adapter that calls a caller-injected fetch the guard cannot
observe. No live behavior is claimed or required.

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

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_subagent_provider_execution_authority.py`; `governance/compat/check_equivalence_claim_evidence.py` |
| literalTokensReviewed | dispatch status; Source Verification Block; Current Runtime Freshness Verification; Evidence Reuse scalar fields; worker-return headings; trace and delta labels; providerExecutionAuthority declaration; equivalence disposition tokens |
| gateRunPurpose | confirm as evidence that the completed source-verified packet matches checker shape |
| claimBoundary | checker conformance does not prove the isolation is complete or the boundary closed |

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

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| exact R8 baseline, work-order and return paths | all absent before dispatch authoring | PASS |
| token search | `EAFR-R8` existed only in the R7 completion review corrective lane and continuity next-move text | PASS |
| external-store surface survey | two cvf-web surfaces import the Upstash client; both are in the manifest | PASS |
| collision decision | reuse the existing injection seam; create at most one new focused test and no new helper module | PASS |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| INTERNAL_AGENT | cvf-web test isolation and gateway adapter boundary | local test behavior and one adapter guard; no runtime product change | before/after suite totals and focused proofs | local source only | HARDEN_BOUNDED |
| EXTERNAL_AGENT_CLI_MCP | none | no CLI/MCP read, authority or adapter behavior is created or changed | unchanged adapter contract surfaces | separate source-verified work order required | DEFERRED_WITH_REASON |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | no-commit worker plus independent reviewer |
| phase | implementation pending worker return |
| baseHeadFor(phase) | dispatchBaseHead=c1a8747cb; executionBaseHead=worker captures; closureBaseHead=reviewer captures |
| changedSetScope(phase) | six-path manifest plus at most one named new focused test |
| traceScope(phase, actor) | external-store isolation, adapter boundary closure and deterministic proof |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | clean worktree required; RFR, BuildAuthority, provider/live, build and all external effects parked |
| nextMoveSurfaces | worker return then independent reviewer decision |

## Worker Output Checker Read-Ahead Mandate

Before writing each changed file or the worker return, read every checker source
applicable to its docType, path family and conditional content. Derive actual
headings and literal tokens before authoring; checklist prose is not a
substitute for the real sections.

## Work-Order Fulfillment Manifest

| Artifact group | Required worker action |
| --- | --- |
| rate limiter and storage adapter | remove ambient live-client construction in non-live runs using the existing seam |
| shared test setup | ensure the non-live default injects the fake rather than ambient credentials |
| permitted focused test | prove injected-fake use and absence of external client construction |
| OpenAI-compatible adapter | close the injected-fetch bypass and assign one disposition |
| worker return | record complete uncommitted evidence, both controls and honest out-of-scope reporting |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_EAFR_R8_NON_LIVE_EXTERNAL_STORE_ISOLATION_AND_ADAPTER_BOUNDARY_WORKER_RETURN_2026-08-26.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The return must carry the full review-family/no-commit shape, cite this work
order, report the actual dirty paths including the named new test, carry one
disposition per control, and preserve every residual without relabeling.

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_EAFR_R8_NON_LIVE_EXTERNAL_STORE_ISOLATION_AND_ADAPTER_BOUNDARY_COMPLETION_2026-08-26.md` |
| reviewerOwnedClosurePaths | worker manifest, return, optional completion review, EAFR roadmap and continuity |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

Reviewer must independently rerun the suite, verify the Upstash class is cleared
without any egress permit widening, confirm the injected-fake proof, challenge
the adapter disposition, and verify that deliberate live external-store use
still works.

## Review Gate

Only the independent reviewer/closer may accept, repair authorized defects, run
closure gates and commit. Acceptance requires direct source inspection and fresh
recomputation, not worker self-report.

## Closure Checklist

- authorized paths plus at most one named new test, and empty staging;
- Upstash destination absent from all denial reasons;
- injected-fake proof present and focused;
- one adapter disposition, not `ACCEPTED_AS_IS`;
- R7 egress invariants unchanged with a negative denial test;
- 16 out-of-scope failures reported as still failing;
- zero provider and zero external-store calls.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only with all acceptance evidence, including a
disposition for both controls. Otherwise return `BLOCKED_WITH_REASON`, naming
the first unresolved condition and preserving partial or failed evidence.

## Foundation Storage Layout Block

| Field | Disposition |
| --- | --- |
| Foundation Storage Layout Block | N/A with reason: R8 edits existing source in place and adds at most one focused test; it creates no foundation family file or storage topology |
| Protected storage paths | memory foundation filenames, folder front door, generated aggregates and indexes remain unchanged |
| Follow-up condition | any new stable foundation file, split, relocation or generated-state edit needs separate authorization |

## Operator Checkpoint

operator.checkpoint.waiver: none. Provider/live/network, build, credential
access, RFR resumption, BuildAuthority repair, public sync, deployment and push
all require fresh explicit authority.

## Commit Prompt Readiness

- worker commit: forbidden;
- reviewer material commit: only after independent acceptance;
- session sync: separate commit;
- push/public sync: unauthorized.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher/orchestrator |
| Provider or surface | private local repository |
| Session or invocation | EAFR-R8 dispatch authoring, 2026-08-26 |
| Working directory | repository root |
| Command or tool surface | source reads, searches, hashes, scaffold, ADIF resolver, safe non-live suite measurement, packet authoring and gates |
| Target paths | R8 baseline and work order |
| Allowed scope source | accepted R7 completion review corrective lane and EAFR roadmap |
| Before status evidence | clean worktree at HEAD `c1a8747cbc70c5d5a8ab9feffee2643509d8e5eb`; staging empty |
| After status evidence | two dispatch artifacts pending commit |
| Diff evidence | `git diff --name-status` over exact dispatch document set |
| Approval boundary | R8 dispatch only |
| Claim boundary | no worker implementation, live, provider, external-store, build or public effect |
| Agent type | dispatcher |
| Invocation ID | `eafr-r8-dispatch-2026-08-26` |
| Expected manifest | baseline and work order |
| Actual changed set | baseline and work order |
| Manifest delta | NONE |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | R8 dispatch authority only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT: pinned source hashes, failure classification and a fresh non-live suite measurement |
| actionEvidence | ACTION_EVIDENCE_PRESENT: committed baseline/work order after gates |
| invocationBoundary | local documentation authoring plus safe read-only measurement |
| interceptionBoundary | no universal runtime, CLI, MCP, provider or coding-control interception claim beyond the already-accepted R7 test-harness guard |
| forbiddenExpansion | paths and effects outside the exact manifest, including guard edits, configuration, environment files, provider or external-store calls, build and RFR |
| claimLanguage | packet authorizes bounded local isolation and one boundary closure only after commit |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | no new external input; every R8 claim derives from CVF-owned sources and fresh local measurement |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | EAFR roadmap, R7 completion review and current cvf-web and gateway sources |
| Disposition | N/A_WITH_REASON: no new external knowledge intake in this tranche |
| Claim boundary | accepted CVF reviews are authority; no external report is cited as authority |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

Reason: named-file source verification and failure classification, not an intake
refresh.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - R8 makes no repository-wide or
  all-surface completeness claim. The external-store survey is a bounded
  targeted search over cvf-web source.

## Epistemic Process Block

- Epistemic Process Applicability: HIGH_EVIDENCE
- Expected Result / Prediction: inspection would show the R7 denials
  concentrated on a small number of destinations, with the largest class being
  infrastructure rather than provider traffic.
- Evidence Comparison: that held precisely. Seventy-two of eighty-eight failures
  name a single Upstash host, and the mechanism is identical to the earlier
  provider incidents: credentials in a local env file, loaded by the shared
  setup, consumed by ambient client construction.
- Contradiction or Gap Disposition: the tempting resolution is to permit the
  Upstash host in the guard, which would clear seventy-two failures immediately
  and silently restore external egress. This packet forbids that explicitly,
  makes the guard non-writable, and requires isolation by injected fake instead.
- Claim Update: R8 is ready for bounded no-commit worker execution after this
  packet is committed. A `BOUNDED_WITH_NAMED_RESIDUAL` outcome on Control B is
  an acceptable honest result.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
| --- | --- | --- | --- | --- |
| ambient infrastructure credentials in a local env file caused live external-store traffic during ordinary non-live runs, the same mechanism as the earlier provider-call incidents | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | DESIGN_REVIEW_REQUIRED | isolate by injected fake in this tranche; a general rule that non-live suites never construct external clients from ambient values remains a standard candidate |
| a guard that wraps global fetch cannot observe an adapter that calls an injected fetch | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | close the boundary in this tranche; a shared destination-classification source usable by both the harness and adapters remains a candidate |

## Machine Closure Package

| Surface | R8 closure requirement |
| --- | --- |
| Work order | reviewer converts pending dispatch state only after acceptance |
| Completion/reviewer artifact | reviewer-owned decision with before/after totals, dispositions, diff and claim boundary |
| Roadmap | R8 accepted or blocked; RFR remains parked |
| Registry JSON/Markdown | N/A with reason: no corpus/generated registry classification changes |
| External evidence digest | N/A with reason: no external dataset is consumed |
| System loop interlock | R7 -> R8 -> RFR decision remains explicit |
| Session continuity | separate post-material sync required |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance test-isolation remediation; no public-sync authority.

## Claim Boundary

This work order authorizes only bounded local external-store isolation, one
adapter boundary closure and deterministic proof across the named manifest. It
authorizes no provider, live, network, credential, build, dependency,
environment-file, guard, configuration, checker, roadmap, registry, public-sync,
deployment or push action, no RFR resumption and no BuildAuthority repair.
Isolating a suite from an external store is not a security proof and makes no
claim about credential hygiene or past traffic.
