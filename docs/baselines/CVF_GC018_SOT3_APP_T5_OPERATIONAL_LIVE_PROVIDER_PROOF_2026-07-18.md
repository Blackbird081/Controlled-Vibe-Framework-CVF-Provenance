# CVF GC-018 Baseline - SOT3-APP-T5 Operational Live Provider Proof

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: SOT3-APP-T5

Dispatch base head: `1bd039a07`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: Operator

Reviewer owner: independent reviewer/designated closer

Worker target: delegated implementation worker

## Authorization / Decision

The operator authorized T5 to use root CVF live API keys for a bounded sibling
application live test after noting that the app does not yet have a valid
provider/live adapter. This baseline releases exactly one worker execution that
may implement a minimal governed live adapter behind the sibling app's existing
`GovernedExecutionAdapter` abstraction, load root CVF keys into process
environment only, and attempt one DashScope-compatible provider call.

## Purpose

Turn the accepted T4 local Controlled Quotation proof into one bounded
operational live-provider proof for the sibling SOT Application. The claim is
limited to a single governed output path using real provider evidence, not
production readiness, public readiness, or universal SOT3 behavior.

## Baseline Decision

Proceed with a no-commit worker. The worker may add a minimal live execution
adapter, deterministic fake-fetch tests, a one-call runner, a sanitized
evidence JSON, and a worker return. The worker must not copy or persist root
`.env.local` into the sibling app; keys may be passed only through the process
environment used for the live command.

## Scope / Target / Owner Boundary

Target root: `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application`.

The sibling app owns the application service chain and its
`GovernedExecutionAdapter` boundary. CVF root owns operator key storage and the
reference Model Gateway live harness pattern. This baseline does not authorize
CVF Core source changes, session-state mutation, public-sync, browser/UI work,
production action, or more than one provider-call attempt.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
|---|---|---|
| T4 accepted closure | material commit `1f815d7f5`; `docs/reviews/CVF_SOT3_APP_T4_COMPLETION_REVIEW_2026-07-17.md` | ACCEPT |
| session sync after T4 closure | current dispatch base `1bd039a07` | ACCEPT |
| operator live/key authorization | operator message on 2026-07-18: root CVF keys may be passed through for test execution | ACCEPT_BOUNDED_ONE_CALL |
| live diagnostic standard | `AGENTS.md` Mandatory Live Governance Proof and Mandatory Live Run Diagnostics sections | ACCEPT |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldTool | `governance/compat/build_dispatch_packet_scaffold.py` |
| packetKind | `runtime-provider-live` |
| scaffoldBase | `1bd039a07` |
| scaffoldDisposition | completed against current source evidence and operator authorization |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind runtime-provider-live --batch-id SOT3-APP-T5 --title "Operational Live Provider Proof" --date 2026-07-18 --base 1bd039a07 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "SOT3-APP-T4 accepted closure 1f815d7f5" --stdout --include-worker-return-skeleton` |
| generatedProfile | runtime-provider-live plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | source verification, exact sibling scope, root-key transfer control, one-call live boundary, and worker manifest |
| checkerReadAheadConfirmation | applicable checker and guard surfaces were read before final packet text |
| docOnlyNewFields | `SOT3_APP_T5_LIVE_PROOF_PASS`; `SOT3_APP_T5_LIVE_PROOF_BLOCKED` |
| claimBoundary | scaffold provenance does not prove execution, provider behavior, or live result |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`SOT downstream application live provider proof`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "SOT downstream application live provider proof" --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | no additional ADIF controls beyond standard live, handoff, and worker-return gates |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| T5 roadmap lane | EXISTS | `docs/roadmaps/CVF_SOT3_DOWNSTREAM_APPLICATION_ROADMAP_2026-07-15.md` | Work Plan row for SOT3-APP-T5 | `SOT3-APP-T5` | SOT3-APP roadmap | ACCEPT |
| T4 release for T5 authoring | EXISTS | `docs/reviews/CVF_SOT3_APP_T4_COMPLETION_REVIEW_2026-07-17.md` | completion review status and final commands | `CLOSED_PASS_BOUNDED_WITH_REVIEWER_REPAIR` | T4 completion review | ACCEPT |
| mandatory live proof rule | EXISTS | `AGENTS.md` | Mandatory Live Governance Proof | `python scripts/run_cvf_release_gate_bundle.py --json` | CVF root agent instructions | ACCEPT |
| root key continuity rule | EXISTS | `AGENTS.md` | Operator-key continuity note | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/.env.local` | CVF root agent instructions | ACCEPT |
| root key aliases present locally | RUNTIME_BEHAVIOR | `CANONICAL_CONTRACT: redacted local existence check; root cvf-web .env.local` | `ALIBABA_API_KEY`, `DASHSCOPE_API_KEY`, and `DEEPSEEK_API_KEY` present without value output | API key alias presence | local operator environment | ACCEPT |
| sibling provider calls disabled by default | VALUE_SET | `CANONICAL_CONTRACT: external sibling direct-read evidence; .env.example` | `CVF_PROVIDER_CALLS_ENABLED=false` | `CVF_PROVIDER_CALLS_ENABLED` | SOT Application config | ACCEPT |
| direct provider bypass forbidden | EXISTS | `CANONICAL_CONTRACT: external sibling direct-read evidence; AGENTS.md` | Do not call providers directly | provider call boundary | SOT Application local instructions | ACCEPT |
| local-first live provider boundary | EXISTS | `CANONICAL_CONTRACT: external sibling direct-read evidence - LOCAL_FIRST_OPERATIONS_DOC` | live provider use is explicit, approved, budget-bounded, and separately evidenced | live provider use | SOT Application operations docs | ACCEPT |
| current governed execution abstraction | EXISTS | `CANONICAL_CONTRACT: external sibling direct-read evidence; packages/cvf-bindings/src/governed-execution.adapter.ts` | `GovernedExecutionPort` and `GovernedExecutionAdapter.execute` | `GovernedExecutionAdapter` | SOT Application CVF bindings | ACCEPT |
| current output service calls execution adapter | RUNTIME_BEHAVIOR | `CANONICAL_CONTRACT: external sibling direct-read evidence; packages/application/src/services/governed-output.service.ts` | `this.execution.execute(...)` after usable ALLOW context | `GovernedOutputService.create` | SOT Application application service | ACCEPT |
| Model Gateway live harness pattern | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/p4b-b-live-proof-harness.ts` | `runLiveProof` resolves secret only when liveAuthorized and calls OpenAI-compatible endpoint through fetch | `runLiveProof` | Model Gateway live proof harness | ACCEPT |
| DashScope-compatible endpoint owner | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/alibaba-free-quota-model-ledger.ts` | `ALIBABA_DASHSCOPE_INTL_ENDPOINT`; endpoint resolver aliases | `resolveAlibabaDashScopeEndpoint` | Model Gateway Alibaba ledger | ACCEPT |
| currently usable model candidate | VALUE_SET | `EXTENSIONS/CVF_MODEL_GATEWAY/src/alibaba-free-quota-model-ledger.ts` | `qwen3.7-plus` entry expires 2026-08-31 | `qwen3.7-plus` | Model Gateway Alibaba ledger | ACCEPT |

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | YES |
| runtimeMutationAuthorized | YES_BOUNDED |
| freshnessVerificationMode | current sibling source verification plus one new provider-call attempt |
| verifiedBase | `1bd039a07` |
| staleEvidenceRule | T4 local proof receipts and prior root live receipts are context only; they cannot satisfy T5 |

## Runtime Expansion Control Block

| Field | Value |
|---|---|
| expansionClass | minimal sibling live execution adapter plus one runner and one evidence file |
| existingOwnerReuse | SOT Application `GovernedExecutionAdapter`; Model Gateway protocol pattern |
| sideEffectCeiling | one attempted provider call and one sanitized evidence JSON |
| retryCeiling | zero retries |
| forbiddenOwners | CVF Core source, provider registry, queue, UI, browser, public-sync, session state, production |

## Live Key Transfer Control Block

| Field | Value |
|---|---|
| sourceKeyLocation | root CVF `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/.env.local` |
| transferMode | process environment only |
| allowedAliases | `DASHSCOPE_API_KEY`; `ALIBABA_API_KEY`; `CVF_ALIBABA_API_KEY`; `CVF_BENCHMARK_ALIBABA_KEY`; `DEEPSEEK_API_KEY` |
| persistenceRule | do not copy, commit, echo, print, or write raw keys or authorization headers |
| evidenceRule | record alias presence and provider/model metadata only; secret value evidence is forbidden |

## Allowed Scope

Exactly the five worker-owned fulfillment paths named in the paired work order.
The worker may read root CVF source, root `.env.local` key names/presence, and
sibling app source as evidence. The worker may not commit.

## Forbidden Scope

All other paths; staging; commit; push; public-sync; browser/UI; server daemon;
production data; second provider call; retry; raw key or raw provider payload
persistence; CVF Core runtime source mutation; session-state mutation.

## Evidence / Verification

Required evidence: focused fake-fetch tests, sibling typecheck/build/test
commands as relevant, exactly one live attempt, zero retries, sanitized
provider/model/latency/usage metadata when returned, raw-response hash,
redacted diagnostic on failure, secret scan, worker-return fast gate, and exact
diff/status/no-commit proof.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | paired T5 work order | `Status: DISPATCH_READY` | READY |
| Completion or reviewer artifact | reviewer to create after worker return | worker return must be independently reviewed before closure | PENDING_REVIEW |
| Roadmap state | SOT3-APP roadmap | T5 dispatch packet recorded | READY |
| Registry JSON | N/A with reason: T5 worker does not own CVF generated corpus registry mutation | no registry mutation in worker scope | N/A with reason |
| External evidence digest | T5 evidence JSON | required after worker execution | PENDING_WORKER |
| System loop interlock | T4 -> T5 | T5 worker released; later lanes remain parked | PASS |
| Session continuity | active session | session sync follows material dispatch commit | PENDING_STEWARD |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value at dispatch | Status |
|---|---|---|---|
| call count | exactly one attempted provider call by worker | not yet executed | PENDING_WORKER |
| retry count | zero | not yet executed | PENDING_WORKER |
| key handling | process env only, no key persistence | authorized by packet | READY |
| live result | secret-safe PASS or diagnostic | not yet executed | PENDING_WORKER |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | Status: DISPATCH_READY; WORKER_MUST_NOT_COMMIT; Source Verification Block; ADIF Defect Registry Disclosure; Current Runtime Freshness Verification; Runtime Expansion Control Block; Live Key Transfer Control Block; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirm source-backed live authorization before worker execution |
| claimBoundary | checker read-ahead is not live-result evidence |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private sibling application proof; no public-sync authorization exists.

## Claim Boundary

This baseline authorizes one bounded sibling-application live proof attempt and
the minimum source/test/evidence files needed to make that proof governed and
reviewable. It does not claim the call has run, does not certify production or
public readiness, does not promote SOT Application into CVF Core, and does not
authorize any later tranche.
