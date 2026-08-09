# CVF Agent Work Order - LPCI1 Web UC-01 Provider Live Proof

Memory class: governed-worker-dispatch

Status: CLOSED_PASS_BOUNDED_LIVE_PROOF_ACCEPTED

Batch ID: LPCI1-WEB-UC01-LIVE

dispatchBaseHead: `102fcc890`

executionBaseHead: WORKER_MUST_CAPTURE_AT_START

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker

Reviewer/closer: primary reviewer/dispatcher

workerReturnPath: `docs/reviews/CVF_LPCI1_WEB_UC01_PROVIDER_LIVE_PROOF_WORKER_RETURN_2026-08-09.md`

## Dispatch Prompt Envelope

Role: provider-live-proof worker. The primary agent is independent reviewer/closer.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI1_WEB_UC01_PROVIDER_LIVE_PROOF_2026-08-09.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: capture the clean committed HEAD immediately before worker actions.

Current-time notes: the exact operator authority permits only the UC-01
provider live proof, with one request maximum and zero retries.

Do-not-misread notes: credential presence is not permission to change the
supported provider/model/endpoint or run the full route/release bundle.

Required first actions: read the paired baseline, this packet, live diagnostic
standard, guard orientation, and current source; capture clean HEAD/status;
run ADIF and pre-implementation before credential load or network action.

Return contract: `COMPLETE_PENDING_REVIEW` after one sanitized success receipt,
or `BLOCKED_WITH_REASON` with a classified zero-call/failure diagnostic. Include
exact manifest, call/retry ledger, gates, staged-empty evidence, and unchanged HEAD.

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | `Worker Autonomy / No-Question Rule`; `Intake Role Routing Decision`; `CVF_RECEIPT_PRESENT`; `ACTION_EVIDENCE_PRESENT`; `COMPLETE_PENDING_REVIEW`; `BLOCKED_WITH_REASON` |
| gateRunPurpose | confirmation and evidence after checker-shape review, not first discovery |
| claimBoundary | read-ahead is not a live result or closure claim |

## 0. Surface Fidelity Gate

Refresh every decision-driving source at executionBaseHead. Any drift in the
exact pair, endpoint, credential name, bridge owner, or output contract blocks
the live action until returned to the reviewer.

## 1. Authority Chain

1. Operator token `AUTHORIZE_LPCI1_WEB_UC01_PROVIDER_LIVE_PROOF_ONLY`.
2. Accepted B2 completion at material commit `5c86f6d77`.
3. Paired GC-018 baseline.
4. This work order.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind runtime-provider-live --batch-id LPCI1-WEB-UC01-LIVE --title "LPCI1 Web UC-01 Provider Live Proof" --date 2026-08-09 --base 102fcc890 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "B2 accepted at 5c86f6d77" --stdout --include-worker-return-skeleton` |
| generatedProfile | runtime-provider-live plus evidence-only no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact current-source verification, two-path evidence manifest, one-attempt/no-retry rule, secret boundary, and reviewer conversion |
| checkerReadAheadConfirmation | required dispatch checkers reviewed before gate execution |
| docOnlyNewFields | pass and blocked reviewer tokens isolated in this work order |
| claimBoundary | scaffold provenance only |

## Purpose

Test the existing UC-01 LPCI provider binding against its exact supported
OpenAI pair with at most one real request, then return sanitized evidence for
independent reviewer disposition.

## Target / Source

Primary target: `executeLpciProviderBinding` in
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/provider-binding.ts`.
The route integration and B2 test suite are prior evidence; this tranche does
not mutate or broadly rerun the full product.

## Required First Reads

- paired GC-018 baseline and accepted B2 completion review;
- `docs/reference/guard_orientation/README.md`;
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`;
- `docs/reference/archive/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`;
- current LPCI provider binding, query route, Model Gateway adapter, and their
  focused tests.

## Pre-Flight Checks

Confirm clean worktree and executionBaseHead, run the worker ADIF query, run
pre-implementation, confirm both output paths are collision-free, and verify
staging is empty before any credential load or network action.

## Agent Roles

| Role | Actor | Responsibility |
|---|---|---|
| dispatcher | primary reviewer | source verification, dispatch packet, authority boundary |
| worker | delegated worker | one-attempt proof and exact two-path no-commit return |
| reviewer/closer | primary reviewer | independent evidence review, closure decision, material commit |
| session-sync steward | primary reviewer | protected continuity update from accepted completion review and material commit |

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | exact operator provider/live-proof-only token |
| Route | `MULTI_AGENT_MULTI_ROLE` |
| risk sensitivity | real credential and provider request, one attempt maximum |
| selected role route | delegated no-commit worker then independent reviewer |
| Worker role | live invocation and sanitized evidence only |
| Reviewer role | evidence recomputation, accept/block decision, commit, continuity |
| Commit mode | `WORKER_MUST_NOT_COMMIT` |
| Checkpoint disposition | provider/live proof released; broader checkpoints parked |
| escalation condition | source drift, scope expansion, secret-safety doubt, forbidden action, or inability to classify failure |

## Worker Autonomy / No-Question Rule

Repair and rerun every local gate failure inside the two-path allowed scope
without asking the operator. Stop and return a governed blocker for source
drift, output collision, missing compatible credential, secret-safety doubt,
scope expansion, forbidden action, or any result after the single allowed
fetch entry. Never request permission to retry; retries are forbidden.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`LPCI web UC-01 provider live proof`, role=`worker`, lifecyclePhase=`pre-implementation`

Returned defects: NONE_RETURNED

Resolver command:
`python governance/compat/run_adif_defect_resolver.py --task-class "LPCI web UC-01 provider live proof" --role worker --lifecycle-phase pre-implementation --json`

The worker must rerun this query at execution and disclose any changed result
in the worker return before proceeding.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| B2 dependency accepted | EXISTS | `docs/reviews/CVF_LPCI1_WEB_UC01_CONTEXT_TO_LLM_PROVIDER_BINDING_BUILD_COMPLETION_2026-08-09.md` | top status and closure decision | `LPCI1_WEB_UC01_PROVIDER_BINDING_BUILD_ACCEPT` | B2 reviewer | ACCEPT |
| exact model syntax | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/.env.example` | LPCI provider binding block | `LPCI_LLM_MODEL` | cvf-web config documentation | ACCEPT |
| required key name | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/provider-binding.ts` | credential reference | `LPCI_LLM_API_KEY` | LPCI binding | ACCEPT |
| exact provider/model enforcement | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/provider-binding.ts` | `resolveLpciProviderBindingConfig` | `OPENAI_PROVIDER_ID`; `OPENAI_MODEL_ID` | LPCI binding | ACCEPT |
| canonical endpoint enforcement | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/provider-binding.ts` | `resolveEndpoint` | `OPENAI_ENDPOINT` | LPCI binding | ACCEPT |
| real provider boundary | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_MODEL_GATEWAY/src/openai-compatible-execute-adapter.ts` | adapter `execute` | `fetchImpl` | Model Gateway adapter | ACCEPT |
| exact-pair receipt validation | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/provider-binding.ts` | `isValidExactPairResult` | `receipt.providerId`; `receipt.selectedModelId` | LPCI binding | ACCEPT |
| live diagnostics | EXISTS | `docs/reference/archive/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md` | Required Diagnostic Fields and Rerun Rule | `stage`; `class`; `retryable`; `userAction`; `safeMessage` | CVF live diagnostic standard | ACCEPT |

## New Doc-Only Fields

| Field | Purpose | Runtime claim |
|---|---|---|
| `LPCI1_WEB_UC01_PROVIDER_LIVE_PROOF_PASS` | reviewer token after independent acceptance | NONE_AT_DISPATCH |
| `LPCI1_WEB_UC01_PROVIDER_LIVE_PROOF_BLOCKED` | reviewer token for classified blocked evidence | NONE_AT_DISPATCH |

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | YES |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | current source verification and one fresh provider attempt maximum |
| requiredExecutionBase | clean post-dispatch HEAD captured by worker |
| staleEvidenceRule | no prior receipt may be presented as this invocation |

## Negative Search And Collision Discipline

Confirm both output paths do not already exist before creation. If either has
a conflicting owner, stop without network action and return the collision to
the reviewer. Do not create a second runtime binding or live harness.

## Evidence Reuse And Encoding Plan

Use ASCII in both outputs. Reuse the existing binding and local toolchain.
Persist only bounded metadata and a sanitized diagnostic or success receipt.
Do not persist the generated answer, prompt body, system prompt, provider raw
body, request headers, secret values, or secret-derived hashes.

## Runtime Expansion Control Block

| Field | Value |
|---|---|
| expansionClass | evidence-only invocation |
| providerOwner | existing LPCI binding composed over Model Gateway |
| callBudget | one attempted provider request maximum |
| retryBudget | zero |
| sourceMutation | forbidden |
| persistentRuntimeState | N/A with reason: sanitized review evidence only |

## Live Credential Control Block

| Field | Value |
|---|---|
| credential contract | `LPCI_LLM_API_KEY` only |
| load mode | process-local, secret-safe loader for the ignored cvf-web local environment file |
| allowed presence evidence | variable name plus `PRESENT_REDACTED` or `ABSENT` only |
| missing result | zero calls; diagnostic `auth` / `missing_api_key` / non-retryable / `check_api_key` |
| forbidden aliases | no mapping from `OPENAI_API_KEY`, DashScope, Alibaba, or DeepSeek variables |
| forbidden evidence | raw key, prefix/suffix, length, hash, authorization header, raw request/response body |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order control | Closure evidence |
|---|---|---|
| fresh separate provider/live authority | exact operator token in paired baseline | reviewer verifies authorization boundary |
| accepted complete DESIGN including UC-04/config | B2 completion dependency and current source verification | reviewer closure comparison |
| separate fresh provider/live chain | one-attempt evidence-only execution | evidence JSON and worker return |
| no broader roadmap release | forbidden-scope and claim-boundary controls | closure decision remains bounded |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| `docs/reviews/evidence/lpci1-web-uc01-provider-live-proof-2026-08-09.json` | create one sanitized success receipt or classified no-call/failure diagnostic |
| `docs/reviews/CVF_LPCI1_WEB_UC01_PROVIDER_LIVE_PROOF_WORKER_RETURN_2026-08-09.md` | create full no-commit worker return with exact command, call, gate, diff, and status evidence |

No other changed or untracked path is allowed.

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| durable governance root | `docs/reviews/` and `docs/reviews/evidence/` |
| evidence placement | one sanitized JSON under the established evidence directory |
| worker-return placement | one governed Markdown review under the established reviews directory |
| index or registry mutation | N/A with reason: no new durable foundation or lookup surface is created |
| duplicate owner check | required before either output is created |
| generated aggregate | N/A with reason: neither output is generated aggregate state |

## Execution Plan

1. Capture executionBaseHead and clean worktree evidence.
2. Run the worker ADIF query and mandatory pre-implementation gate.
3. Confirm the two output basenames are collision-free.
4. Use a secret-safe process-local loader to determine whether
   `LPCI_LLM_API_KEY` is nonblank without outputting value metadata.
5. If absent, make zero calls and write the required `missing_api_key`
   diagnostic. If present, set `LPCI_LLM_MODEL=openai/gpt-4o`, use the
   canonical endpoint, wrap the injected fetch solely to count at most one
   call and capture safe status/latency, then invoke
   `executeLpciProviderBinding` once.
6. Write the sanitized evidence JSON before considering any rerun. Reruns are
   forbidden in this work order.
7. Write the worker return, run the required gates, and leave staging empty.

## Required Live Behavior

Use a bounded public, non-sensitive prompt that requests a short constant-like
answer and contains no repository, user, credential, or proprietary content.
Do not invoke the full query route or release bundle. The proof target is the
existing provider binding only. Count fetch entry as a provider-call attempt
even when the network/provider later fails.

Success requires `ANSWER_EMITTED`, exactly one fetch entry, nonempty response,
and no exception. Persist only response length and SHA-256 digest, never the
response text. A `NO_PROVIDER_CONFIGURED` or `PROVIDER_ERROR` result is not a
pass; classify it using observed safe fetch metadata. If the binding suppresses
the lower-level cause, use `unknown_error` and
`do_not_retry_without_new_evidence` rather than guessing.

## Mandatory Live Run Diagnostic Block

Every no-call, failed, timed-out, partial, or empty result must include:
`stage`, `class`, `retryable`, `userAction`, `provider`, `model`, `httpStatus`
when available, `latencyMs` when available, `receiptId`/`traceId` when
available, and `safeMessage`. Record the diagnostic before any next action.
No live rerun is authorized.

## Sanitized Evidence JSON Contract

Required top-level fields: `schemaVersion`, `batchId`, `timestampUtc`,
`executionBaseHead`, `authorizationToken`, `providerId`, `modelId`,
`endpointClass`, `credentialPresence`, `callCountAttempted`, `retryCount`,
`result`, `latencyMs`, `httpStatus`, `responseLength`, `responseSha256`,
`diagnostic`, `secretSafety`, and `claimBoundary`.

Use `null` where a field is unavailable. `authorizationToken` may contain the
operator token because it is authority, not a credential. `secretSafety` must
state that no secret value, value metadata, authorization header, prompt,
generated answer, or raw body is persisted.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_LPCI1_WEB_UC01_PROVIDER_LIVE_PROOF_WORKER_RETURN_2026-08-09.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required sections: Purpose; Target / Source; Scope / Methodology; Findings /
Position; Risk / Corrective Action; Checker Source Read-Ahead Block; Agent
Operation Trace Block; Delta Execution Claim Boundary Control Block; External
Knowledge Intake Routing; Corpus Completeness And Report Integrity; Rescan
Intelligence Hardening; Finding-To-Governance Learning Disposition; Epistemic
Process Block; Machine Closure Package; Public Export Disposition; Claim
Boundary; git status --short; Changed Files; Command Evidence; No-Commit
Statement.

## Agent Handoff Contract Control Block

Contract source: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | delegated worker, independent reviewer/closer, session-sync steward |
| phase | EXECUTION |
| baseHeadFor(phase) | dispatchBaseHead=`102fcc890`; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | exactly two fulfillment paths |
| traceScope(phase, actor) | worker invocation receipt; reviewer recomputation; closer commit; steward continuity |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer owns material commit |
| crossBatchIsolation | worker starts from a clean worktree at post-dispatch HEAD; B2 closed at `102fcc890`; later roadmap and public lanes parked |
| nextMoveSurfaces | reviewer/session steward only from accepted completion review and material commit |
| Before status evidence | clean worktree at `102fcc890`; `git status --short` produced no output before dispatch authoring |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_LPCI1_WEB_UC01_PROVIDER_LIVE_PROOF_COMPLETION_2026-08-09.md` |
| reviewerOwnedClosurePaths | completion review, baseline/work-order disposition, roadmap disposition if warranted, and protected continuity surfaces |
| closureOwner | primary reviewer/dispatcher |
| workerCommitPermission | FORBIDDEN |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | delegated worker |
| Provider or surface | local filesystem and one OpenAI provider attempt maximum |
| Session or invocation | LPCI1-WEB-UC01-LIVE, 2026-08-09 |
| Working directory | CVF private provenance root and cvf-web package |
| Command or tool surface | PowerShell, Node/tsx, Python governance gates |
| Target paths | two fulfillment paths |
| Allowed scope source | this work order and paired GC-018 |
| Before status evidence | clean worktree at dispatch base `102fcc890`; worker must capture clean post-dispatch status |
| After status evidence | worker must paste `git status --short` |
| Diff evidence | `git diff --name-status` and untracked manifest |
| Approval boundary | exact one-attempt provider/live token only |
| Claim boundary | UC-01 provider binding proof only |
| Agent type | delegated worker |
| Invocation ID | `lpci1-web-uc01-provider-live-2026-08-09` |
| Expected manifest | exactly two output paths |
| Actual changed set | worker to fill |
| Manifest delta | worker to fill |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | one local UC-01 provider-binding attempt |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT required through sanitized JSON plus worker return |
| actionEvidence | ACTION_EVIDENCE_PRESENT required through call counter, result/diagnostic, gates, and no-commit evidence |
| invocationBoundary | manual local invocation only |
| interceptionBoundary | no universal wrapper or arbitrary command interception claim |
| claimLanguage | one local UC-01 provider-binding attempt at one timestamp only |
| forbiddenExpansion | full route/release proof, deployment, production, public, other provider/model, or later roadmap lane |

## External Knowledge Intake Routing

Canonical chain map:
`docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md`.

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | current local runtime source plus bounded provider receipt |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` and `governance/compat/check_delta_execution_claim_boundary.py` |
| Owner surface | paired GC-018, this work order, sanitized evidence JSON |
| Disposition | `BLOCKED_UNTIL_CVF_PROOF` until reviewer accepts the fresh receipt |
| Claim boundary | no external corpus absorption, provider generalization, or public claim |

## Corpus Completeness And Report Integrity

- Corpus task class: bounded provider-live source verification and evidence.
- Corpus root: repo-local files named in Required First Reads and Source
  Verification Block.
- Snapshot time: 2026-08-09 dispatch authoring.
- Enumeration command: filesystem-backed direct reads plus targeted `rg`.
- Manifest artifact or inline manifest: Required First Reads, Source
  Verification Block, and two-path fulfillment manifest in this work order.
- Manifest hash: N/A with reason: bounded direct-read dispatch, no generated
  corpus manifest.
- Processing ledger artifact or inline ledger: Source Verification Block rows.
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED |
  BLOCKED_UNREADABLE.
- Reconciliation: manifest=required source rows and two outputs; ledger_terminal=READ for cited source rows; exclusions=full-repo corpus scan and public surfaces; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: full-repo corpus intake, generated registry mutation,
  public-sync corpus, browser, deployment, and unrelated provider lanes.
- Unreadable or unsupported files: 0.
- Aggregation check: N/A with reason: no aggregate is generated by dispatch.
- Drift check: N/A with reason: no generated aggregate is edited.
- Output traceability: evidence JSON and worker return map directly to the
  single-call ledger and live diagnostic contract.
- Adversarial verification: exact pair, zero-call missing-key branch,
  one-attempt ceiling, no-retry rule, and secret scan are reviewer-checkable.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: with a nonblank compatible credential, the
accepted binding should return `ANSWER_EMITTED` after one fetch entry. Without
that credential it should make zero calls and return a classified blocked
receipt.

Evidence Comparison Requirement: compare credential presence, call count,
result, safe status/latency, response length/digest, and current B2 tests.

Contradiction Handling Requirement: any missing credential, provider/network
failure, empty response, source drift, or secret-safety doubt stops without a
retry and is recorded truthfully.

Claim Update Requirement: reviewer alone may record the pass or blocked token.

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/check_governed_file_size.py --enforce
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git diff --name-status
git status --short
git diff --cached --name-only
git rev-parse --short HEAD
```

The worker may use a secret-safe process-local Node loader and temporary inline
invocation. Command evidence must redact the loader implementation if printing
it would expose secret-handling details. It must never contain the credential.

Reviewer dispatch repair, 2026-08-09: the original verification command used
the pre-dispatch base `102fcc890`, which incorrectly combined dispatch and
protected session-sync commits into a `split` pre-implementation range. The
correct base is the clean committed `executionBaseHead` captured immediately
before worker action. This repair changes no call budget, credential boundary,
worker manifest, runtime source, or provider authority.

## Acceptance Criteria

- [x] B2 dependency and clean dispatch base identified.
- [x] exact operator authority token recorded.
- [x] exact two-path worker manifest declared.
- [x] one attempted call maximum and zero retries required.
- [x] missing compatible credential is a zero-call classified outcome.
- [x] source/config/package/session/public mutations forbidden.
- [x] worker commit forbidden and reviewer closure conversion declared.

## Review Gate

Reviewer independently verifies authorization, current source, exact manifest,
call/retry counts, diagnostic semantics, evidence redaction, relevant local
tests if needed, gates, and empty staging. Worker cannot accept its own live
claim.

## Write Ownership

Worker owns only the exact evidence JSON and worker-return paths. Reviewer owns
completion review, baseline/work-order/roadmap disposition, commits, and all
session/front-door/handoff surfaces.

## Evidence Requirements

Record executionBaseHead, authority token, credential presence without value
metadata, call and retry counts, safe provider/model/endpoint class,
status/latency when available, result or full diagnostic, response length and
digest only on success, exact changed manifest, gate results, unchanged HEAD,
and empty staging.

## Operator Checkpoint

The exact provider/live-proof-only checkpoint is satisfied. Deployment,
production readiness, public sync, full route/release proof, persistence,
vector/RAG, other providers/models, and later roadmap lanes remain parked.

## Closure Diff Gate

Compare roadmap, B2 completion, baseline, work order, evidence JSON, worker
return, current source, and command outputs. Any extra path/call, missing
field, raw value/body, guessed diagnostic, stale result, public/prod claim, or
unclear retry fails closure.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` before network action on failed pre-implementation,
source drift, output collision, missing credential, or secret-safety doubt.
After the single allowed fetch entry, return classified success/failure
evidence and do not retry for any reason.

## Closure Checklist

- [x] B2 dependency and exact operator authority recorded.
- [x] Source Verification Block uses current runtime owners.
- [x] Exact two-path worker scope declared.
- [x] One-attempt and zero-retry rules declared.
- [x] Secret-safe missing-key and failure diagnostics declared.
- [x] Worker commit and protected-surface mutation forbidden.
- [x] Reviewer closure conversion and public disposition declared.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this work order | `Status: CLOSED_PASS_BOUNDED_LIVE_PROOF_ACCEPTED` | PASS |
| Worker return | named worker-return path | `COMPLETE_PENDING_REVIEW`; reviewer accepted | PASS |
| Evidence JSON | named evidence path | one call; zero retries; success; HTTP 200 | PASS |
| Completion review | reviewer-owned path | `LPCI1_WEB_UC01_PROVIDER_LIVE_PROOF_PASS` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_LPCI1_WEB_UC01_PROVIDER_LIVE_PROOF_COMPLETION_2026-08-09.md` | closed bounded reviewer disposition | PASS |
| Roadmap state | LPCI1 roadmap | bounded live proof accepted; broader lanes parked | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | generated aggregate drift check PASS; no coverage owner changed | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | existing lookup guidance reviewed; no lookup/index/recommendation change | PASS |
| External evidence digest | sanitized JSON receipt | sha256 `C399D534AC902435C54F2772AF8EE4CF8760F6D1477F9569419DC1D79DBB1652` | PASS |
| System loop interlock | D1 -> B2 -> one live proof -> stop | no broader lane released | PASS |
| Session continuity | protected reviewer/session-steward update | follows material closure | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| exact authority token | `AUTHORIZE_LPCI1_WEB_UC01_PROVIDER_LIVE_PROOF_ONLY` | PASS |
| exact provider/model | `openai` / `gpt-4o` | PASS |
| call count maximum one | 1 | PASS |
| retry count zero | 0 | PASS |
| nonempty success | HTTP 200; response length 31 | PASS |
| secret-safe persistence | presence, length, digest, status, latency only | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: operator authorized provider/live proof only, not public sync.

## Claim Boundary

This work order authorizes one no-commit worker to run at most one real request
through the current UC-01 LPCI provider binding and file sanitized evidence.
It does not authorize source changes, a full route or release proof,
deployment, production, public sync, another provider/model, retry, or any
later roadmap tranche.
