# CVF Agent Work Order - EAFR-R7 Fail-Closed Provider Egress Authority Repair

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Work order ID: EAFR-R7

Date: 2026-08-26

dispatchBaseHead: `edf8f18d293b50e65df04eebd37c091d9c13d975`

executionBaseHead: worker must capture actual HEAD and require this committed packet as ancestor

closureBaseHead: reviewer captures the committed dispatch head

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator through the committed EAFR roadmap

Reviewer/closer: current independent orchestrator/reviewer

Worker: provider-egress repair worker role

## Dispatch Prompt Envelope

Batch ID: EAFR-R7-PROVIDER-EGRESS-REPAIR.

Role: no-commit provider-egress repair worker.

Canonical packet: this committed work order and its paired baseline.

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: R6 is reviewer-accepted `CLOSED_BLOCKED` at material commit
`2bc2b2d0d` with four unresolved P1 provider-authority bypass classes. The
guard's fail-open control flow, the mainland endpoint constant, the three
environment overrides and both unconstrained adapter endpoint fields were
verified in source at dispatch head `edf8f18d2`.

Do-not-misread notes: R7 repairs the egress control and its focused tests only.
It is not authority to resume RFR, to make any provider or network call, to run
a build or release gate, to repair the two BuildAuthority residuals or the R1
build criterion, to edit a roadmap, registry, checker or session file, or to
claim any runtime, security, deployment or production property. Closing these
four rows is a local test-scope control repair and nothing more.

Required first actions: read startup surfaces, guard orientation, literal
gotchas, this packet, paired baseline, the R6 completion review and worker
return, every pinned input and the applicable checker sources for the
worker-return class before writing any artifact.

Return contract: the exact manifest, no stage or commit, `COMPLETE_PENDING_REVIEW`
or `BLOCKED_WITH_REASON`.

providerExecutionAuthority: FORBIDDEN

R7 repairs a local egress control and makes no provider call of any kind, so no
orchestrator provider grant is requested, issued or consumed. The worker must
not construct, borrow or synthesize a grant to observe permitted behavior; the
permitted path is proven with an injected fake fetch, never with real egress.

Worker return path: `docs/reviews/CVF_EAFR_R7_FAIL_CLOSED_PROVIDER_EGRESS_AUTHORITY_REPAIR_WORKER_RETURN_2026-08-26.md`

sourceAuthority: paired GC-018 baseline, committed EAFR roadmap, the accepted R6 completion review and worker return, and the source-verified cvf-web and gateway files named in this packet

## Purpose

Repair the provider-execution egress control so that unrecognised destinations
fail closed rather than fail open, derive the recognised endpoint set from an
authoritative surface rather than a hardcoded literal, constrain the adapter
destination boundary, and give each of the four recorded P1 bypass classes an
evidence-backed disposition.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id EAFR-R7 --title "Fail Closed Provider Egress Authority Repair" --date 2026-08-26 --base edf8f18d2 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | source-verified fail-open control-flow finding, endpoint authority derivation contract, adapter boundary validation contract, out-of-process harness disposition contract, four-token P1 row disposition contract, adversarial proof matrix and the provider-registry non-authority finding |
| checkerReadAheadConfirmation | dispatch, envelope, authority, trace, delta, epistemic, handoff, lifecycle and worker-return checker sources reviewed |
| docOnlyNewFields | Fail-Closed Egress Repair Contract; Endpoint Authority Derivation Contract; Adapter Boundary Validation Contract; Out-Of-Process Harness Disposition Contract; P1 Row Disposition Contract; Historical Traffic Quantification Contract; Adversarial Proof Matrix |
| claimBoundary | dispatch authoring only; no implementation, live, provider, public, deployment, credential or environment claim |

## Authority And Scope

Governing baseline:
`docs/baselines/CVF_GC018_EAFR_R7_FAIL_CLOSED_PROVIDER_EGRESS_AUTHORITY_REPAIR_2026-08-26.md`.

The worker may write exactly the paths in Write Ownership. No other path is
writable. The worker must not stage or commit.

## Authority Chain

Operator EAFR authority -> committed roadmap -> R6 blocked closure -> paired
baseline -> this work order -> no-commit worker -> independent reviewer/closer.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
| --- | --- | --- | --- | --- |
| repair coverage across endpoint constants | Endpoint Authority Derivation Contract | derived recognised set plus negative derivation test | focused guard suite and source inspection | PASS |
| repair coverage across configurable and caller endpoints | Adapter Boundary Validation Contract | rejected-destination evidence at the adapter boundary | focused guard suite and adapter source inspection | PASS |
| repair coverage across out-of-process harness boundaries | Out-Of-Process Harness Disposition Contract | explicit evidenced harness disposition | harness path survey and package-script check | PASS |
| clear every R6 P1 row before RFR can be reconsidered | P1 Row Disposition Contract | four-row disposition table | reviewer closure conversion | PASS |

## Required First Reads

Read `AGENTS.md`, `CVF_SESSION_MEMORY.md`, the bootstrap read model, active
handoff, `docs/reference/guard_orientation/README.md`, governed literal gotchas,
paired baseline, this work order, the R6 completion review and worker return,
every pinned source and the worker-output checker sources named below. Resolve
the full session registry only for a targeted missing or contradictory fact.

`DESIGN.md` is not required: R7 changes no Web, UI or dashboard surface.

## Agent Roles

Operator owns scope; dispatcher owns the packet; worker repairs the egress
control, decides each P1 disposition and returns without commit; reviewer
independently re-derives the fail-closed behavior, challenges every disposition,
repairs allowed-scope defects, closes and commits.

## Pre-Flight Checks

Confirm clean worktree, empty staging, actual HEAD, committed dispatch ancestry,
all pinned hashes, absent worker-return path and zero live-test selection. Hash
drift or an existing return path blocks before authoring.

## Write Ownership

Exactly these paths:

1. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/provider-execution-guard.ts`
2. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/provider-execution-guard.test.ts`
3. `docs/reviews/CVF_EAFR_R7_FAIL_CLOSED_PROVIDER_EGRESS_AUTHORITY_REPAIR_WORKER_RETURN_2026-08-26.md`

A source path outside this list may be written only when the chosen
adapter-boundary mechanism cannot be implemented without it. In that case the
worker must name the path, quote the source fact that made it unavoidable, and
record it as a disclosed manifest delta in the return. Discovering that the
mechanism requires touching the gateway package is a legitimate outcome; hiding
it inside an undisclosed changed set is not.

No roadmap, registry, baseline, work order, session, package manifest, existing
governance checker, environment, adapter credential, public clone or deployment
edit is authorized under any circumstance.

## Pinned Input Hashes

| Path | SHA-256 |
| --- | --- |
| `docs/roadmaps/CVF_EAFR_REMEDIATION_ROADMAP_2026-08-25.md` | `6495e00d77aa2e204435575245f4f6be32999345896b61ed003d9f8990bf7ea7` |
| `docs/reviews/CVF_EAFR_R6_CLOSURE_RECONCILIATION_AND_RFR_RESUME_DECISION_COMPLETION_2026-08-26.md` | `b3f3c721f44d670e6dee4c16c32170c0ecabf88d79aff71e0a8ce5de53450cf4` |
| `docs/reviews/CVF_EAFR_R6_CLOSURE_RECONCILIATION_AND_RFR_RESUME_DECISION_WORKER_RETURN_2026-08-26.md` | `e598d6a36a10ed862d7b9808a7e7c7ccc04f31f6a4cab17ee5a739b1421fa66f` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/provider-execution-guard.ts` | `b9895607b2a2bb2caef186673be646ec0b2b9ae8695da3bbdc5447b5821e4a31` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/setup.ts` | `c44389e06b51f602a64ee719fda2d463021d68242a7626a0de05a93a1f5c994b` |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/alibaba-free-quota-model-ledger.ts` | `1e1a3cf72662d9235e09ddde8b7cbb6238d1100baedc1f1b23662b016d010a51` |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/openai-compatible-execute-adapter.ts` | `22f264e8e3a8b6cb74d74fad8ae353a6d052a0a4fa2442a7581bcd69169d53c4` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/vitest.config.ts` | `9a4a65976b5b7a5d038f9cb412a90d417f804108cf1dd33bae4421989a863420` |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | `2cd55057e28dd1f8e99973f45e6e5d2b3fed0aa3e05e832e32d92e062bf35e56` |

The new worker-return path must be absent. Every hash is calculated at
`edf8f18d2`; mismatch returns `BLOCKED_WITH_REASON` before authoring.

The two guard paths in Write Ownership are pinned as inputs and expected to
change. Their post-repair content is evidence, not drift.

## Fail-Closed Egress Repair Contract

The defect is directional, and the worker must repair the direction, not add
entries to the map. The current control resolves a hostname, looks it up, and
returns the unwrapped fetch when the lookup misses. Every destination the guard
has never heard of is therefore permitted.

R7 must invert that default for provider egress. The repaired control must
deny by default and permit only what it can justify. The worker must state, in
source comments and in the return, the exact set of destinations that remain
permitted without an authority grant, and the reason each is safe.

Two constraints bound the repair:

- the current non-live suite performs legitimate non-provider egress. A repair
  that denies loopback, relative, data, blob or in-test fixture traffic and
  breaks the suite is not acceptable;
- a repair that reintroduces a broad default-permit branch under a new name is
  a failed repair even if every P1 row is nominally addressed. The reviewer will
  read the control flow for a permit path reachable by an arbitrary hostname.

If the worker concludes that a strict default-deny cannot preserve the suite,
it must return `BLOCKED_WITH_REASON` with the specific conflicting traffic
named, rather than shipping a weakened control described as fail-closed.

## Endpoint Authority Derivation Contract

The recognised provider-endpoint set must stop being a literal maintained inside
the guard file. R7 must derive it from an authoritative surface so that adding a
provider endpoint constant to the gateway cannot silently escape coverage.

The worker must demonstrate the derivation with a negative test: an endpoint
that exists on the authoritative surface but is named nowhere in the guard must
be covered without editing the guard. A test that merely asserts the six current
hostnames are still covered does not satisfy this contract.

Coverage may never be inferred from provider identity, from a sibling endpoint
of the same provider, or from a surface being currently unused. The Alibaba row
is the worked example: `dashscope-intl.aliyuncs.com` being covered is not
evidence about `dashscope.aliyuncs.com`.

The mainland DashScope endpoint must receive an explicit recorded disposition:
either brought into coverage, or recorded with the reason it must remain out of
scope. Silence is not a disposition.

The existing provider registry is not that authoritative surface as it stands,
and the worker must not assume otherwise.
`EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` keys `ProviderRecord`
and `ProviderRegistry` by provider id and carries `models`, `riskClass`,
`credentialKeyIds`, `tags` and `metadata`; neither it nor
`PROVIDER_CAPABILITY_REGISTRY` declares a hostname, endpoint or base URL field.
A derivation built on provider identity alone would reproduce the exact false
green R6 recorded for Alibaba. The worker must therefore derive from a surface
that actually owns endpoints, and must record which surface it chose and why
that surface is authoritative for destinations rather than identities.

If the authoritative surface lives in a package the guard cannot import without
a dependency change, the worker must record that as a blocking source fact and
propose the smallest sufficient mechanism, rather than silently adding a
dependency or copying the constants back into a literal.

## Adapter Boundary Validation Contract

Identity validation is not destination validation.
`createOpenAiCompatibleExecuteAdapter` checks that the input's `providerId` and
`modelId` match its configuration, then sends the request to whatever `endpoint`
string it was constructed with. R7 must constrain or validate the
caller-supplied and environment-override endpoint values so an arbitrary
hostname cannot be paired with a covered `providerId`.

The worker must choose one mechanism and record why: validating the endpoint
against the authoritative surface, narrowing the option type so an arbitrary
string is not constructible, or requiring the injected fetch to be a guarded
implementation. The return must show the rejected case failing closed, not
merely the accepted case passing.

Because `fetchImpl` is injected, the worker must also record what happens when
an adapter is constructed with an unguarded fetch, and whether that path is
closed, constrained, or explicitly accepted as an out-of-scope caller
responsibility with a stated reason and a named owner for the residual risk.

The three environment overrides in `resolveAlibabaDashScopeEndpoint` are part of
this row. A disposition that constrains the caller-supplied field while leaving
the resolver able to return an arbitrary hostname resolves half a row and must
be reported as such.

## Out-Of-Process Harness Disposition Contract

The guard binds `globalThis.fetch` in the process that loaded the test setup. It
cannot bind a process it does not run in. R7 must decide, and record with
evidence, whether the out-of-process harness scripts must carry an equivalent
egress control or must be formally classified as operator-only surfaces outside
the in-process guard's remit.

Either disposition is acceptable if it is explicit and evidenced. Classifying a
harness as operator-only requires naming each harness path, showing it is not
package-script wired, and stating the control that governs its invocation. An
unstated assumption that harnesses are safe because nobody currently runs them
is not a disposition and leaves the row unresolved.

The worker must enumerate the harness paths it considered and how it found
them, so the reviewer can test the enumeration for completeness rather than
trusting it.

## P1 Row Disposition Contract

R7 must return one disposition per R6 P1 row, using exactly these tokens:

- `RESOLVED_FAIL_CLOSED`: the bypass no longer exists, with a test that fails
  closed on the specific bypass path;
- `BOUNDED_WITH_ACCEPTED_RESIDUAL`: the bypass is constrained but a named
  residual remains, with the residual, its owner and its blast radius stated;
- `CLASSIFIED_OUT_OF_REMIT`: the surface is formally outside the in-process
  control, with the naming, wiring evidence and governing control recorded;
- `UNRESOLVED`: the row stands.

The four rows are: mainland DashScope endpoint constant; endpoint environment
overrides; caller-supplied adapter endpoints; out-of-process harnesses.

A row may not be marked resolved because it is currently unused, because no
override is currently set, or because the surface is deliberately invoked. R6
already rejected each of those arguments and the reviewer will reject them
again. Any `UNRESOLVED` row keeps RFR parked and must be reported plainly; a
partial repair honestly reported is an acceptable return.

## Historical Traffic Quantification Contract

R6 recorded 12 individually disclosed provider calls plus a separate
unquantified historical DashScope class from pre-guard non-live runs. R7 must
either quantify that class from committed evidence, or record it as permanently
unquantifiable with a stated reason and the boundary that follows.

The worker must not fold an unquantified class into a numeric total and must not
make a provider call to establish any figure. This is a ledger completeness
obligation, not a P1 bypass row, and its disposition must not be used to argue
that any P1 row is cleared.

## Adversarial Proof Matrix

The worker must attempt each of the following against the repaired control and
report the observed result, not the intended one:

| Attack | Required observed result |
| --- | --- |
| request to a hostname named nowhere in the guard or the authoritative surface | denied before network I/O |
| request to the mainland DashScope hostname | matches the recorded mainland disposition |
| request to a hostname supplied through each of the three environment overrides | matches the recorded override disposition |
| adapter constructed with a covered `providerId` and an arbitrary endpoint | matches the recorded adapter disposition |
| adapter constructed with an unguarded injected fetch | matches the recorded injection disposition |
| request to loopback or a test fixture destination | permitted, suite unaffected |

A row whose observed result differs from the recorded disposition is a defect
the worker must report, not reconcile.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "EAFR-R7",
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
    "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/",
    "docs/reviews/",
    "docs/work_orders/",
    "docs/baselines/CVF_GC018_EAFR_R7_FAIL_CLOSED_PROVIDER_EGRESS_AUTHORITY_REPAIR_2026-08-26.md"
  ],
  "claims": ["provider egress fails closed on unrecognised destinations and every R6 P1 row has an evidence-backed disposition"],
  "requiredProof": ["fail-closed control flow", "negative derivation test", "adversarial proof matrix", "four P1 dispositions", "focused and full non-live suite counts", "typecheck", "hashes", "worker-return fast gate", "independent review"],
  "operatorCheckpoints": [],
  "forbiddenEffects": ["provider or live call", "build or release gate", "BuildAuthority repair", "roadmap or registry edit", "RFR resumption", "worker stage or commit", "public/deploy/push"],
  "sourceEvidence": {"selectedFilesFullyRead": true, "corpusReceiptRef": null, "completenessClaimChanged": false}
}
```

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| selected role route | MULTI_AGENT_MULTI_ROLE |
| worker role | no-commit provider-egress repair worker |
| reviewer role | independent reviewer/closer |
| external intake | none; all claims verified in CVF-owned sources |
| escalation condition | hash drift, a default-deny that cannot preserve the suite, a required dependency change, a required provider call, or a P1 row that cannot be dispositioned without out-of-manifest edits |
| risk sensitivity | fail-open regression disguised as a repair; severity integrity of the four rows |
| scope classification | bounded egress-control repair with a fixed manifest |

## Required Commands

Run from cvf-web:

1. `npx vitest run src/test/provider-execution-guard.test.ts`, capturing exact
   totals before and after the repair;
2. `npm run check`;
3. `npm run test:run`, capturing exact totals and every failing file;
4. non-live and live collection listings, list-only, to confirm the R1D and R1E
   selection boundaries still hold.

Run from repository root:

5. `python governance/compat/check_subagent_provider_execution_authority.py --enforce`;
6. bounded searches enumerating provider endpoint constants and out-of-process
   harness paths;
7. recompute pinned hashes for every pinned input;
8. `python governance/compat/run_worker_return_fast_gate.py`;
9. `git diff --check`, `git diff --name-status`,
   `git status --short --untracked-files=all`, and
   `git diff --cached --name-only`.

Do not run `npm run build`, LPF `npm test`, Playwright, any live or
execution-mode provider command, release gate, network, environment/key,
public-sync, deployment or installation commands. The live script is list-only
at current HEAD and must stay that way; do not reconstruct an executing variant.

## Execution Plan

1. Capture startup, clean status, empty staging, HEAD, ancestry, return-path
   absence and pinned hashes; record the pre-repair focused and full suite
   totals.
2. Read the guard, setup, gateway ledger, adapter and vitest config in full
   before changing any line.
3. Invert the egress default and derive the recognised set from the
   authoritative surface.
4. Add the negative derivation test and the adversarial proof matrix cases.
5. Decide the adapter-boundary mechanism and the harness disposition, recording
   any out-of-manifest path the mechanism required.
6. Assign one disposition token to each of the four P1 rows.
7. Decide the historical-traffic disposition from committed evidence only.
8. Write the worker return, run every safe command, and return without staging
   or committing.

## Verification Commands

Run every Required Command, including the full:

`python governance/compat/run_worker_return_fast_gate.py`

Individual checker substitution is forbidden.

## Evidence Requirements

Report pre/post HEAD and status; the actual changed set against the exact
manifest with any delta disclosed; the repaired control flow quoted with its
permitted-destination set; the negative derivation test and its result; the
adversarial proof matrix with observed results; one disposition token per P1
row with cited evidence; the historical-traffic disposition; pre- and
post-repair focused guard counts; the full non-live suite count with the PVV
denial count explained against the R6 figure of 22 failures; TypeScript
diagnostics; pinned input hashes; worker-return fast gate output; empty staging;
and an explicit zero-provider-call statement.

A change in the PVV denial count must be explained directionally. Fewer denials
may mean the benchmark now fails closed earlier at a different boundary, or may
mean egress was re-opened. The worker must show which, with evidence.

## Fail Conditions

Return `BLOCKED_WITH_REASON` on: pinned hash drift; an existing worker-return
path; a default-deny that cannot preserve legitimate non-provider suite traffic;
a derivation that requires an unauthorized dependency or package-manifest
change; any condition that would require a provider call, a build, a checker
edit, or a roadmap, registry or session edit; or a P1 row that cannot be
dispositioned within the manifest.

Shipping a weakened control described as fail-closed, or marking a row resolved
on the argument that the surface is currently unused, is a failed return rather
than a blocked one.

## Worker Autonomy / No-Question Rule

The worker executes this packet without asking the orchestrator for
clarification. Where the packet leaves a mechanism choice open, the worker
chooses, records the choice and its reason, and proceeds. Where the packet
forbids an action, the worker returns blocked rather than requesting an
exception.

## Evidence Reuse And Encoding Plan

evidenceReuseSource: R6 completion review and worker return, both committed at `2bc2b2d0d`

evidenceReuseDisposition: REUSE_AS_RECORDED_INPUT_ONLY

verificationMode: RECOMPUTE_REQUIRED

recomputeReason: R6 measured its suite figures at an earlier head, and the R7 repair itself changes the guard that produces the PVV denial count, so every focused, full-suite, typecheck and denial figure must be re-measured at the execution head rather than carried forward.

recomputationRequirement: every numeric claim repeated from R6 must be recomputed at execution head

encodingPlan: UTF-8 without BOM; ASCII-only in governed artifact prose; existing source file encoding preserved

## Current Runtime Freshness Verification

| Field | Value |
| --- | --- |
| runtimeClaimPresent | NO |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | NOT_APPLICABLE_WITH_REASON |
| reason | R7 repairs a process-local test-harness egress control and its focused tests. It makes no provider, network, live or runtime behavior claim, and executes no provider call, so no live-run diagnostic is required or permitted. |
| requiredFutureAction | any claim that provider egress is controlled outside the Vitest process, or any RFR resumption, requires a fresh source-verified authorization and, where a runtime claim is made, a real live-run diagnostic |

Live-proof boundary reminder: mock mode is UI-structure-only; any claim about
governance behavior, provider routing, or model call requires a real API call
and a live-run diagnostic per
`docs/reference/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| R7 must repair provider-execution authority coverage across endpoint constants, configurable/caller endpoints and harness boundaries | ROADMAP_AUTHORITY | `docs/roadmaps/CVF_EAFR_REMEDIATION_ROADMAP_2026-08-25.md` | Proposed Tranches, EAFR-R7 row; Acceptance Criteria R7-clears-every-P1 rule | EAFR-R7 | EAFR roadmap | ACCEPT |
| four P1 provider-authority bypass classes remain unresolved and block RFR | OWNER_AUTHORITY | `docs/reviews/CVF_EAFR_R6_CLOSURE_RECONCILIATION_AND_RFR_RESUME_DECISION_COMPLETION_2026-08-26.md` | Findings R6-RF3; Reviewer Decision | REVIEWER_ACCEPTED_CLOSED_BLOCKED | R6 completion review | ACCEPT |
| the four rows are named exactly and the successor tranche carries no authority | OWNER_RECONCILIATION | `docs/reviews/CVF_EAFR_R6_CLOSURE_RECONCILIATION_AND_RFR_RESUME_DECISION_WORKER_RETURN_2026-08-26.md` | endpoint surface coverage matrix; Risk / Corrective Action successor proposal | EAFR-R7 | R6 worker return | ACCEPT |
| the guard returns the unwrapped fetch when the hostname is unrecognised | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/provider-execution-guard.ts` | returned guard closure, provider resolution and early-return branch | createProviderExecutionFetchGuard | cvf-web provider execution guard | ACCEPT |
| the recognised set is a hardcoded six-entry hostname literal | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/provider-execution-guard.ts` | module-scope provider host map literal | PROVIDER_HOSTS | cvf-web provider execution guard | ACCEPT |
| the guard binds only the current process global fetch | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/setup.ts` | module-scope global fetch assignment | createProviderExecutionFetchGuard | cvf-web test setup | ACCEPT |
| a mainland DashScope endpoint constant exists outside the guard map | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_MODEL_GATEWAY/src/alibaba-free-quota-model-ledger.ts` | exported mainland endpoint constant | ALIBABA_DASHSCOPE_MAINLAND_ENDPOINT | Alibaba free quota model ledger | ACCEPT |
| three environment variables can redirect the resolved DashScope endpoint | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_MODEL_GATEWAY/src/alibaba-free-quota-model-ledger.ts` | endpoint resolver fallback chain | resolveAlibabaDashScopeEndpoint | Alibaba free quota model ledger | ACCEPT |
| both adapter option shapes accept an unconstrained caller-supplied endpoint and the adapter validates identity only | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_MODEL_GATEWAY/src/openai-compatible-execute-adapter.ts` | adapter option interfaces and adapter execute body | OpenAiCompatibleAdapterOptions; CredentialBoundOpenAiCompatibleAdapterOptions; createOpenAiCompatibleExecuteAdapter | OpenAI-compatible execute adapter | ACCEPT |
| the live selection barrier authorizes collection only and is not an egress control | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/vitest.config.ts` | live selection exclusion and collection-only env comment | CVF_LIVE_TEST_SELECTION | cvf-web vitest configuration | ACCEPT |
| the provider registry owns identities and carries no hostname or endpoint field | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | provider record interface and registry map keying | ProviderRecord; ProviderRegistry; PROVIDER_CAPABILITY_REGISTRY | gateway provider registry | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_subagent_provider_execution_authority.py`; `governance/compat/check_equivalence_claim_evidence.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py` |
| literalTokensReviewed | Source Verification Block; Current Runtime Freshness Verification; exact manifest and write-ownership shape; no-commit status; Agent Operation Trace label set; Delta field-row labels and receipt/action tokens; Public Export Disposition; equivalence disposition tokens; source-not-found disposition spelling |
| gateRunPurpose | confirm as evidence that the source-verified dispatch already matches required shape, not to discover required tokens by gate failure |
| claimBoundary | structural conformance proves packet shape only; it does not prove any bypass class is closed or that RFR may resume |

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

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| exact R7 baseline, work-order and return paths | all absent before dispatch authoring | PASS |
| token search | search roots `docs` and `CVF_SESSION`; command `rg -n "EAFR-R7\|EAFR_R7" docs CVF_SESSION`; the R7 token existed only in the roadmap R7 row, the R6 return and completion successor proposal, and session next-move text | PASS |
| endpoint constant survey | mainland and intl DashScope constants, the three-variable resolver and both adapter option shapes located in the gateway package and pinned as inputs | PASS |
| collision decision | repair in the two guard paths plus one new worker return; create no roadmap, registry or checker change | PASS |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| INTERNAL_AGENT | cvf-web test-harness provider egress control | process-local test-scope control only; no runtime, product or network behavior change | fail-closed control flow, negative derivation test and adversarial proof matrix | local sources only | REPAIR_BOUNDED |
| EXTERNAL_AGENT_CLI_MCP | none | no CLI/MCP read, authority or adapter behavior is created or changed | unchanged adapter boundaries | separate source-verified work order required | DEFERRED_WITH_REASON |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | no-commit worker plus independent reviewer |
| phase | egress repair pending worker return |
| baseHeadFor(phase) | dispatchBaseHead=edf8f18d2; executionBaseHead=worker captures; closureBaseHead=reviewer captures |
| changedSetScope(phase) | exact three-path worker manifest plus any disclosed mechanism-required path |
| traceScope(phase, actor) | egress control repair, endpoint derivation, adapter boundary decision, harness disposition and four P1 dispositions |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | clean worktree required; RFR, build, BuildAuthority repair, ungranted provider and all external effects parked |
| nextMoveSurfaces | worker return then independent reviewer decision |

## Worker Output Checker Read-Ahead Mandate

Before writing the worker return, read every checker source applicable to its
docType, path family and conditional content class. Derive actual headings,
table labels, marker lines and enum tokens from checker source before authoring;
this packet's checklist prose is not a substitute for the real sections.

| Output artifact | Required read-ahead result |
| --- | --- |
| worker return under `docs/reviews/` | derive exact review headings, worker-return quality terms, trace labels, delta boundary labels, every conditional-section token its checkers require, and no-commit evidence shape before writing |

Literal-shape reminders: do not list required headings as backticked heading
strings before the real section; write the source-not-found disposition spelling
rather than the exact blocked enum in `literalTokensReviewed`; avoid
`after ... closure` wording unless a dependency-release row cites the accepted
artifact path and commit.

## Work-Order Fulfillment Manifest

| Artifact group | Required worker action |
| --- | --- |
| egress control source | invert the default to deny and derive the recognised set from an authoritative surface |
| focused guard tests | add the negative derivation test and every adversarial proof matrix case |
| four P1 rows | assign exactly one disposition token each, with cited evidence |
| historical traffic class | quantify from committed evidence or record as permanently unquantifiable with a reason |
| worker return | report observed results, disclosed manifest deltas and recomputed counts without relabeling |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_EAFR_R7_FAIL_CLOSED_PROVIDER_EGRESS_AUTHORITY_REPAIR_WORKER_RETURN_2026-08-26.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Shape-list rule: when listing required worker-output sections, write section
names without the heading prefix. Reserve actual heading syntax for real
sections so structural checkers do not treat a checklist as the artifact section
body.

The return must carry the full review-family no-commit shape, cite this work
order, report the actual dirty paths, and preserve every residual, unresolved
row and unquantified class without relabeling.

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_EAFR_R7_FAIL_CLOSED_PROVIDER_EGRESS_AUTHORITY_REPAIR_COMPLETION_2026-08-26.md` |
| reviewerOwnedClosurePaths | worker return, optional completion review, EAFR roadmap and continuity |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

The reviewer must independently read the repaired control flow for any permit
path reachable by an arbitrary hostname, rerun the focused and full non-live
suites and recompute the cited counts, re-execute the adversarial proof matrix
rather than trusting the reported results, challenge every P1 disposition token
against its evidence, and confirm that no out-of-manifest path was changed
without disclosure.

## Review Gate

Only the independent reviewer/closer may accept, repair authorized defects, run
closure gates and commit. Acceptance requires direct source inspection and fresh
recomputation, not worker self-report.

## Closure Checklist

- changed set matches the exact manifest, or every delta is disclosed;
- the repaired control denies an arbitrary unrecognised hostname;
- the negative derivation test covers an endpoint the guard never names;
- every adversarial proof matrix row reports an observed result;
- each of the four P1 rows carries exactly one disposition token with evidence;
- the historical-traffic class is quantified or explicitly bounded;
- focused and full non-live counts are recomputed and divergences explained;
- zero provider calls, zero build, zero roadmap, registry or session change.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only with all acceptance evidence, including a
disposition for every P1 row. Otherwise return `BLOCKED_WITH_REASON`, naming the
first unresolved condition and preserving partial or failed evidence.

A return in which some rows are `RESOLVED_FAIL_CLOSED` and others `UNRESOLVED`
is a legitimate `COMPLETE_PENDING_REVIEW` provided every row is dispositioned
honestly. RFR simply stays parked.

## Foundation Storage Layout Block

| Field | Disposition |
| --- | --- |
| Foundation Storage Layout Block | N/A with reason: R7 repairs two existing source paths and creates one review artifact, with no foundation family file or storage topology change |
| Protected storage paths | memory foundation filenames, folder front door, generated aggregates and indexes remain unchanged |
| Follow-up condition | any new stable foundation file, split, relocation or generated-state edit needs separate authorization |

## Operator Checkpoint

operator.checkpoint.waiver: none. RFR resumption, build, ungranted live or
provider action, credential access, public sync, deployment and push all require
fresh explicit authority. Clearing every P1 row confers none of them; the
operator decides whether RFR resumes.

## Commit Prompt Readiness

- worker commit: forbidden;
- reviewer material commit: only after independent acceptance;
- session sync: separate commit;
- push/public sync: unauthorized.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher/orchestrator |
| Provider or surface | private local repository; zero provider calls |
| Session or invocation | EAFR-R7 dispatch authoring, 2026-08-26 |
| Working directory | repository root and cvf-web package |
| Command or tool surface | source inspection, bounded searches, SHA-256 hashing, ADIF resolver and dispatch scaffold helper |
| Target paths | R7 baseline and this work order |
| Allowed scope source | committed EAFR roadmap R7 row and the accepted R6 blocked closure |
| Before status evidence | HEAD `edf8f18d2`; clean worktree; empty staging; no R7 artifact present |
| After status evidence | two new dispatch paths pending commit; staging empty |
| Diff evidence | `git diff --name-status` |
| Approval boundary | R7 dispatch authoring only |
| Claim boundary | no implementation, provider/live, build, RFR resume or external effect |
| Agent type | dispatcher/orchestrator |
| Invocation ID | `eafr-r7-dispatch-2026-08-26` |
| Expected manifest | R7 baseline and this work order |
| Actual changed set | R7 baseline and this work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | R7 dispatch authority only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT: pinned source hashes and direct source verification of the fail-open branch, the mainland constant, the three-variable resolver and both adapter option shapes |
| actionEvidence | ACTION_EVIDENCE_PRESENT: committed baseline and work order after gates |
| invocationBoundary | local documentation authoring plus safe read-only source inspection |
| interceptionBoundary | no universal runtime, OS, network, proxy, CLI, MCP or provider interception claim; the repaired control binds one process's global fetch and nothing else |
| forbiddenExpansion | paths and effects outside the exact manifest, including provider or live calls, build or release gates, BuildAuthority repair, roadmap or registry edits, RFR resumption, public sync, deployment and push |
| claimLanguage | packet authorizes bounded local egress-control repair and one worker return only after commit |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | no new external input; every R7 claim derives from CVF-owned sources and direct source inspection |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | EAFR roadmap and the accepted R6 closure artifacts |
| Disposition | N/A_WITH_REASON: no new external knowledge intake in this tranche |
| Claim boundary | accepted CVF reviews are authority; no external report is cited as authority |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

Reason: bounded repair of two named source paths, and never an intake refresh or repository rescan of any kind.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - R7 repairs a bounded, named set
  of source paths and makes no repository-wide or all-surface completeness
  claim. The endpoint and harness enumerations are scoped surveys whose method
  the worker must state so the reviewer can test them, not completeness claims.

## Epistemic Process Block

- Epistemic Process Applicability: HIGH_EVIDENCE
- Expected Result / Prediction: the four P1 rows would prove to be four
  independent defects requiring four separate mechanisms.
- Evidence Comparison: reading the source showed otherwise. The mainland
  constant and the environment overrides are the same defect seen twice, because
  both are destinations absent from a hardcoded literal. The controlling fault
  is one line of control flow: an unrecognised hostname returns the unwrapped
  fetch. Fixing the direction addresses the first three rows; only the
  out-of-process harness row is genuinely separate, because no in-process
  control can reach it.
- Contradiction or Gap Disposition: rather than dispatch four parallel repairs,
  this packet requires one directional repair plus an authoritative derivation,
  and keeps the four rows as separate disposition obligations so a single
  mechanism cannot be claimed to clear rows it does not actually reach.
- Claim Update: R7 is ready for no-commit worker execution after this packet is
  committed. A partial disposition is an acceptable outcome; RFR stays parked
  until every row is cleared.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
| --- | --- | --- | --- | --- |
| an egress control was written as an allowlist-to-deny that fails open on unknown destinations | MACHINE_GATE_GAP | RUNTIME_BEHAVIOR_LEARNING | DESIGN_REVIEW_REQUIRED | this packet requires the default inverted and the recognised set derived from an authoritative surface |
| a hardcoded recognised set drifted from the authoritative endpoint constants it was meant to mirror | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | this packet forbids literal maintenance and requires a negative derivation test |

## Machine Closure Package

| Surface | R7 closure requirement |
| --- | --- |
| Work order | reviewer converts pending dispatch state only after acceptance |
| Completion/reviewer artifact | reviewer-owned decision with control-flow verification, adversarial matrix re-execution, four dispositions and claim boundary |
| Roadmap | R7 accepted or blocked; RFR resumption remains an operator decision |
| Registry JSON/Markdown | N/A with reason: no corpus/generated registry classification changes |
| External evidence digest | N/A with reason: no external dataset is consumed |
| System loop interlock | R1E -> R6 blocked -> R7 repair -> operator RFR decision remains explicit |
| Session continuity | separate post-material sync required |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance egress-control repair; no public-sync authority.

## Claim Boundary

This work order authorizes only bounded local egress-control source and test
repair within the exact manifest, evidence-backed disposition of four recorded
P1 rows, and one written worker return. It authorizes no provider, live,
network, credential or build action, no public sync, deployment, push or
production claim, no RFR resumption, no roadmap, registry, checker or session
edit, and no repair of the BuildAuthority residuals or the R1 build criterion.

A fail-closed process-local test-harness egress control is not a network, OS,
proxy or production security control. Clearing every P1 row is not a security,
deployment or production-readiness proof, and does not itself resume RFR.
