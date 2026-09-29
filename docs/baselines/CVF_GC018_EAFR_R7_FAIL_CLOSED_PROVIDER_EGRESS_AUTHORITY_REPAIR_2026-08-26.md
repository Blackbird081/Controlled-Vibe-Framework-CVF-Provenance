# CVF GC-018 Baseline - EAFR-R7 Fail-Closed Provider Egress Authority Repair

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: EAFR-R7-PROVIDER-EGRESS-REPAIR

Dispatch base head: `edf8f18d293b50e65df04eebd37c091d9c13d975`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator through the committed EAFR roadmap

Reviewer owner: current independent orchestrator/reviewer

Worker target: provider-egress repair worker role

## Purpose

Convert the process-local provider-execution guard from a hardcoded
hostname-allowlist that fails open on unknown hosts into a fail-closed egress
control whose recognised set derives from an authoritative surface, and resolve
or explicitly bound each of the four P1 provider-authority bypass classes that
R6 left unresolved.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id EAFR-R7 --title "Fail Closed Provider Egress Authority Repair" --date 2026-08-26 --base edf8f18d2 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | source-verified fail-open defect statement, four-class P1 disposition contract, egress default-deny repair contract, adapter boundary validation contract, out-of-process harness disposition contract and historical-traffic quantification contract |
| checkerReadAheadConfirmation | dispatch, authority, trace, delta, epistemic and worker-return checker sources reviewed |
| docOnlyNewFields | Fail-Closed Egress Repair Contract; Endpoint Authority Derivation Contract; Adapter Boundary Validation Contract; Out-Of-Process Harness Disposition Contract; Historical Traffic Quantification Contract |
| claimBoundary | dispatch authoring only; no live, provider, public, deployment, credential or environment claim |

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| EAFR-R6 blocked closure | `docs/reviews/CVF_EAFR_R6_CLOSURE_RECONCILIATION_AND_RFR_RESUME_DECISION_COMPLETION_2026-08-26.md`; material commit `2bc2b2d0d` | RELEASED |
| EAFR-R6 worker return with the four P1 rows | `docs/reviews/CVF_EAFR_R6_CLOSURE_RECONCILIATION_AND_RFR_RESUME_DECISION_WORKER_RETURN_2026-08-26.md`; material commit `2bc2b2d0d` | RELEASED |
| EAFR-R1E provider execution authority | `docs/reviews/CVF_EAFR_R1E_ORCHESTRATOR_PROVIDER_EXECUTION_AUTHORITY_COMPLETION_2026-08-25.md`; material commit `8007e269f` | RELEASED |
| EAFR-R1D non-live runner provider exclusion | `docs/reviews/CVF_EAFR_R1D_NON_LIVE_RUNNER_PROVIDER_EXCLUSION_COMPLETION_2026-08-25.md`; material commit `87d3ddd40` | RELEASED |
| R7 roadmap authority | `docs/roadmaps/CVF_EAFR_REMEDIATION_ROADMAP_2026-08-25.md`, EAFR-R7 row and the R7-clears-every-P1 acceptance rule | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`provider egress fail-closed repair`, role=`worker`, lifecyclePhase=`implementation`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "provider egress fail-closed repair" --role worker --lifecycle-phase implementation` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | none |
| Dispatch impact | ordinary CVF controls apply |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_subagent_provider_execution_authority.py`; `governance/compat/check_equivalence_claim_evidence.py` |
| literalTokensReviewed | Source Verification Block; Current Runtime Freshness Verification; exact manifest; no-commit status; trace labels; Public Export Disposition; equivalence disposition tokens |
| gateRunPurpose | confirm as evidence that the source-verified dispatch already matches required shape |
| claimBoundary | structural conformance does not prove any bypass class is closed or that RFR may resume |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Path existence for EAFR-R7 artifacts | `ls docs/baselines/*EAFR_R7* docs/work_orders/*EAFR_R7* docs/reviews/*EAFR_R7*` returned no such file for all three roots | NO_COLLISION |
| Token search for EAFR-R7 (2026-08-26) | search roots: governed artifact roots plus session state; exact search command: `rg -n "EAFR-R7\|EAFR_R7" docs CVF_SESSION`; query used the R7 batch token in both hyphen and underscore forms; result: 8 hits, all forward references from the roadmap R7 row, the R6 return and completion successor proposal, and session next-move fields; zero existing R7 packet artifacts | NO_COLLISION |
| Collision decision | R7 is pre-reserved by the committed roadmap row and by the R6 successor recommendation; no prior R7 baseline, work order or return exists to supersede | AUTHOR_NEW_PACKET |

## Current Runtime Freshness Verification

Verified directly at HEAD `edf8f18d293b50e65df04eebd37c091d9c13d975` on
2026-08-26, after R6 blocked closure:

- the guard in `provider-execution-guard.ts` maps exactly six hostname string
  keys to provider identifiers. Its control flow resolves the request hostname,
  looks it up in that map, and when the lookup yields no provider it returns
  `fetchImpl(input, init)` directly. Unknown hostnames therefore bypass the
  authority evaluation entirely. The guard is an allowlist-to-deny control that
  fails open, not a default-deny egress control;
- the denial branch is reached only for the six recognised hostnames, so the
  strength of `evaluateProviderExecutionAuthority` is irrelevant to any egress
  whose hostname is absent from the map;
- `setup.ts` assigns the guard to `globalThis.fetch` at module scope, so the
  control is process-local to the Vitest worker process and binds no egress
  performed by a separate process;
- `ALIBABA_DASHSCOPE_MAINLAND_ENDPOINT` in the gateway ledger resolves to the
  mainland DashScope compatible-mode chat completions URL, whose hostname is
  absent from the guard map while the intl hostname is present. One Alibaba
  endpoint is covered and another is not, which is exactly the false green that
  a providerId-keyed comparison would report as covered;
- `resolveAlibabaDashScopeEndpoint` returns the first non-empty trimmed value of
  `DASHSCOPE_COMPAT_ENDPOINT`, `ALIBABA_DASHSCOPE_ENDPOINT` and
  `CVF_ALIBABA_DASHSCOPE_ENDPOINT` before falling back to the intl constant, so
  the resolved hostname is operator-controlled and unbounded;
- `OpenAiCompatibleAdapterOptions` and
  `CredentialBoundOpenAiCompatibleAdapterOptions` each declare `endpoint` as an
  unconstrained string alongside `providerId`, and
  `createOpenAiCompatibleExecuteAdapter` passes that string straight to
  `fetchImpl` after checking only that the identity of the input matches the
  configured `providerId` and `modelId`. Identity is validated; destination is
  not;
- the adapter receives `fetchImpl` by injection, so an adapter constructed
  outside the guarded process, or handed an unguarded fetch, performs egress
  that no in-process control observes;
- the existing provider registry surfaces do not close this gap and must not be
  mistaken for the authoritative endpoint surface R7 needs.
  `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` declares
  `ProviderRecord` with `id`, `displayName`, `status`, `riskClass`, `models`,
  `credentialKeyIds`, `tags` and `metadata`, and `ProviderRegistry` keys its map
  by provider id. Neither that file nor `PROVIDER_CAPABILITY_REGISTRY` carries a
  hostname, endpoint or base URL field, so no registry-derived lookup can decide
  endpoint coverage today. This is why the guard's set is hardcoded, and why a
  providerId-to-guard comparison reports a false green for Alibaba;
- `vitest.config.ts` supplies `CVF_LIVE_TEST_SELECTION` as a collection-only
  value and excludes live patterns from default runs, which controls selection
  and not egress; the selection barrier and the egress barrier are independent
  and only the latter is in R7 scope;
- at this head no endpoint override is set in the Web local env file, the Web
  source references neither the mainland constant nor the resolver, and no
  out-of-process harness is wired into a package script. The P0 escalation
  condition is therefore still unmet, and all four rows remain P1.

No live, provider, network, credential or build command is authorized by this
baseline. R7 repairs local egress-control source and tests; it makes no runtime
or provider claim.

providerExecutionAuthority: FORBIDDEN

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| R7 must repair provider-execution authority coverage across endpoint constants, configurable/caller endpoints and harness boundaries | ROADMAP_AUTHORITY | `docs/roadmaps/CVF_EAFR_REMEDIATION_ROADMAP_2026-08-25.md` | Proposed Tranches, EAFR-R7 row; Acceptance Criteria R7-clears-every-P1 rule | EAFR-R7 | EAFR roadmap | ACCEPT |
| four P1 provider-authority bypass classes remain unresolved and block RFR | OWNER_AUTHORITY | `docs/reviews/CVF_EAFR_R6_CLOSURE_RECONCILIATION_AND_RFR_RESUME_DECISION_COMPLETION_2026-08-26.md` | Findings R6-RF3; Reviewer Decision | REVIEWER_ACCEPTED_CLOSED_BLOCKED | R6 completion review | ACCEPT |
| the successor repair tranche scope was recommended but granted no authority | OWNER_RECONCILIATION | `docs/reviews/CVF_EAFR_R6_CLOSURE_RECONCILIATION_AND_RFR_RESUME_DECISION_WORKER_RETURN_2026-08-26.md` | Risk / Corrective Action, proposed successor repair tranche | EAFR-R7 | R6 worker return | ACCEPT |
| the guard returns the unwrapped fetch when the hostname is unrecognised | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/provider-execution-guard.ts` | returned guard closure, provider resolution and early-return branch | createProviderExecutionFetchGuard | cvf-web provider execution guard | ACCEPT |
| the recognised set is a hardcoded six-entry hostname literal | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/provider-execution-guard.ts` | module-scope provider host map literal | PROVIDER_HOSTS | cvf-web provider execution guard | ACCEPT |
| the guard binds only the current process global fetch | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/setup.ts` | module-scope global fetch assignment | createProviderExecutionFetchGuard | cvf-web test setup | ACCEPT |
| a mainland DashScope endpoint constant exists outside the guard map | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_MODEL_GATEWAY/src/alibaba-free-quota-model-ledger.ts` | exported mainland endpoint constant | ALIBABA_DASHSCOPE_MAINLAND_ENDPOINT | Alibaba free quota model ledger | ACCEPT |
| three environment variables can redirect the resolved DashScope endpoint | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_MODEL_GATEWAY/src/alibaba-free-quota-model-ledger.ts` | endpoint resolver fallback chain | resolveAlibabaDashScopeEndpoint | Alibaba free quota model ledger | ACCEPT |
| both adapter option shapes accept an unconstrained caller-supplied endpoint | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_MODEL_GATEWAY/src/openai-compatible-execute-adapter.ts` | adapter option interfaces and adapter execute body | OpenAiCompatibleAdapterOptions; CredentialBoundOpenAiCompatibleAdapterOptions; createOpenAiCompatibleExecuteAdapter | OpenAI-compatible execute adapter | ACCEPT |
| the live selection barrier authorizes collection only and is not an egress control | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/vitest.config.ts` | live selection exclusion and collection-only env comment | CVF_LIVE_TEST_SELECTION | cvf-web vitest configuration | ACCEPT |
| the provider registry owns identities and carries no hostname or endpoint field | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | provider record interface and registry map keying | ProviderRecord; ProviderRegistry; PROVIDER_CAPABILITY_REGISTRY | gateway provider registry | ACCEPT |

## Fail-Closed Egress Repair Contract

The defect is directional. The current control asks whether a hostname is one it
knows to be a provider, and permits everything else. A fail-closed control must
instead ask whether the egress is authorized, and deny everything else.

R7 must invert that default for provider egress. An unrecognised hostname must
not be treated as evidence that the request is not provider traffic. The worker
must state, in source and in the return, exactly which destinations remain
permitted without an authority grant and why each is safe to permit, rather
than permitting a destination merely because it was never enumerated.

The repair must preserve the non-provider egress that current non-live tests
legitimately perform. A repair that denies loopback or test-fixture traffic and
breaks the suite is not acceptable, and neither is a repair that restores the
fail-open default under a different name.

## Endpoint Authority Derivation Contract

The recognised provider-endpoint set must stop being a literal maintained inside
the guard. R7 must derive it from an authoritative surface such that adding a
provider endpoint constant to the gateway cannot silently escape coverage.

The worker must demonstrate the derivation with a negative test: an endpoint
that exists on the authoritative surface but was never named in the guard must
be covered without editing the guard. Coverage may never be inferred from
provider identity, from a sibling endpoint of the same provider, or from a
surface being currently unused.

The mainland DashScope endpoint must receive an explicit recorded disposition:
either it is brought into coverage, or the artifact records why it must remain
out of scope. Silence is not a disposition.

## Adapter Boundary Validation Contract

Identity validation is not destination validation. R7 must constrain or validate
the caller-supplied and environment-override endpoint values at the adapter
boundary so an arbitrary hostname cannot be paired with a covered `providerId`.

The worker must decide and record whether the constraint is enforced by
validating the endpoint against the authoritative surface, by narrowing the
option type, or by requiring the injected fetch to be a guarded implementation.
Whichever is chosen, the return must show the rejected case failing closed, not
merely the accepted case passing.

Because `fetchImpl` is injected, the worker must also record what happens when
an adapter is constructed with an unguarded fetch, and whether that path is
closed, constrained, or explicitly accepted as an out-of-scope caller
responsibility with a stated reason.

## Out-Of-Process Harness Disposition Contract

The guard cannot bind a process it does not run in. R7 must decide, and record
with evidence, whether the out-of-process harness scripts must carry an
equivalent egress control or must be formally classified as operator-only
surfaces outside the in-process guard's remit.

Either disposition is acceptable if it is explicit and evidenced. Classifying a
harness as operator-only requires naming the harness paths, showing they are not
package-script wired, and stating the control that governs their invocation. An
unstated assumption that harnesses are safe because nobody currently runs them
is not a disposition and leaves the row unresolved.

## Historical Traffic Quantification Contract

R6 recorded 12 individually disclosed provider calls plus a separate
unquantified historical DashScope class from pre-guard non-live runs. R7 must
either quantify that class from committed evidence, or record it as permanently
unquantifiable with a stated reason and the boundary that follows from it.

The worker must not fold an unquantified class into a numeric total, and must
not make a provider call to establish any figure. This item is a ledger
completeness obligation, not a P1 bypass row, and its disposition must not be
used to argue that any P1 row is cleared.

## Exact Worker Manifest

1. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/provider-execution-guard.ts`
2. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/provider-execution-guard.test.ts`
3. `docs/reviews/CVF_EAFR_R7_FAIL_CLOSED_PROVIDER_EGRESS_AUTHORITY_REPAIR_WORKER_RETURN_2026-08-26.md`

Additional source paths required by the chosen adapter-boundary mechanism are
permitted only when the worker return names each one with the source-verified
reason it was unavoidable. Any need to edit a roadmap, registry, session file or
existing governance checker returns blocked to the orchestrator instead.

## Baseline Decision / Proposed Tranche

Dispatch one no-commit repair tranche scoped to provider-egress authority. The
worker repairs the egress control and its focused tests, decides each of the
four P1 dispositions with evidence, and returns without committing. Any need to
resume RFR, call a provider, run a build, widen scope to unrelated failures, or
repair the BuildAuthority residuals returns blocked to the orchestrator.

The two known BuildAuthority residual failures and the R1 build criterion are
explicitly out of R7 scope and must remain untouched.

## Evidence / Verification

The worker must return: the repaired guard and its focused tests passing with
recomputed counts; a negative test proving derivation coverage without guard
edits; per-class disposition for each of the four P1 rows with source evidence;
the historical-traffic disposition; a fresh full non-live suite count with the
PVV denial count explained against the R6 figure of 22 failures; TypeScript
diagnostics; pinned input hashes; the worker-return fast gate; unchanged HEAD;
empty staging; and an explicit zero-provider-call statement.

A repair that reduces the PVV denial count must be explained: fewer denials may
mean the benchmark now fails closed earlier, or may mean egress was re-opened.
The worker must show which.

## Risk / Rollback

Primary risk is a repair that satisfies the four rows structurally while
restoring fail-open behavior through a broader default-permit path. Secondary
risk is scope drift into the BuildAuthority residuals or into RFR resumption.
Tertiary risk is a derivation that couples the test-scope guard to gateway
internals in a way that breaks the non-live suite. Rollback is the pending
uncommitted worker manifest.

## Claim Boundary

This baseline authorizes only bounded local egress-control source and test
repair, evidence-backed disposition of four recorded P1 rows, and one written
worker return. It authorizes no provider, live, network, credential or build
action, no public sync, deployment or push, no RFR resumption, no roadmap,
registry or session edit, and no repair of the BuildAuthority residuals. A
fail-closed local test-scope egress control is not a network, OS, proxy or
production security control, and closing these rows is not a security,
deployment or production-readiness proof.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance egress-control repair; public-sync is separately
governed and not authorized.
