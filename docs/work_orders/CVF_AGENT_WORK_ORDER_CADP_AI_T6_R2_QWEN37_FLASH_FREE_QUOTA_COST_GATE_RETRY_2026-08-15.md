# CVF Agent Work Order - CADP-AI-T6-R2 Qwen3.7 Flash Free Quota Cost Gate Retry

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

docType: work-order

Date: 2026-08-15

Batch ID: CADP-AI-T6-R2

## Dispatch Prompt Envelope

Role: live-proof worker; independent reviewer/closer follows.
Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_CADP_AI_T6_R2_QWEN37_FLASH_FREE_QUOTA_COST_GATE_RETRY_2026-08-15.md`.
Commit mode: `WORKER_MUST_NOT_COMMIT`.
executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`.
Current-time notes: same exact model as R1, `qwen3.7-flash`, snapshot
`qwen3.7-flash-2026-07-15`; governed ledger capture date 2026-08-15;
expiration 2026-10-22; operator permits bounded API-key use by reference.
Do-not-misread notes: predecessor R1 is historical
`REVIEWER_ACCEPTED_BLOCKED_R1_REOPEN_R2_SAME_MODEL` with zero calls, blocked
only because the public Alibaba pricing page omits `qwen3.7-flash`. R2 does
not authorize `qwen-turbo`, any other model substitution, source/config
mutation, deployment, public sync, CLI/MCP use, or a worker commit.
Required first actions: capture clean HEAD/status; read all named
authorities and checker sources; verify node/npm/npx in the same PowerShell
process; run dry-run and local negative gate; establish the Free-Quota Cost
Gate evidence (not a pricing-page bound); only then run the live command.
Return contract: create exactly seven R2 paths, keep secrets redacted, staging
empty and HEAD unchanged, then return `COMPLETE_PENDING_INDEPENDENT_REVIEW`
or `BLOCKED_WITH_REASON`.

dispatchBaseHead: `8ce45e190b16f9dc262ef672016fa758d9d04daa`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

closureBaseHead: `NOT_EXECUTED_YET`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Execute one bounded live compatibility retry for CADP-AI-T6 using the exact
Alibaba/DashScope model `qwen3.7-flash`, unchanged from R1. Resolve R1's
official-pricing-page coverage gap through an operator-directed free-quota
cost gate instead of a pricing-arithmetic gate, then run the canonical
release gate once and produce secret-safe evidence without committing.

completionReviewPath: `docs/reviews/CVF_CADP_AI_T6_R2_QWEN37_FLASH_FREE_QUOTA_COST_GATE_RETRY_COMPLETION_2026-08-15.md`

roadmapPath: `docs/roadmaps/CVF_CADP_FULL_KNOWLEDGE_AND_IMPLEMENTATION_ABSORPTION_ROADMAP_2026-08-13.md`

reviewerOwnedClosurePaths: optional completion review, CADP T6 roadmap
projection, and separate session continuity; worker owns none.

## Authority Chain And Required First Reads

1. `AGENTS.md`
2. `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
3. `CVF_SESSION_MEMORY.md`
4. active handoff named by the bootstrap read model
5. `docs/reference/guard_orientation/README.md`
6. `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
7. `docs/reference/archive/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`
8. `docs/baselines/CVF_GC018_CADP_AI_T6_R2_QWEN37_FLASH_FREE_QUOTA_COST_GATE_RETRY_2026-08-15.md`
9. this work order
10. predecessor worker return at `docs/reviews/CVF_CADP_AI_T6_R1_QWEN37_FLASH_LIVE_COMPATIBILITY_RETRY_WORKER_RETURN_2026-08-15.md` (including its Reviewer Acceptance Note)
11. `scripts/run_cvf_release_gate_bundle.py`
12. `scripts/run_cvf_sot3_a5_release_proof.py`
13. `scripts/run_cvf_sot3_a4_failure_recovery_proof.py`
14. `scripts/_local_env.py`
15. exact SOT3 Alibaba live test route named below
16. governed Alibaba free-quota ledger JSON and Markdown
17. official Alibaba free-quota documentation at
    `https://www.alibabacloud.com/help/en/model-studio/new-free-quota`

Operator authorization permits at most 3 cumulative calls across R1 and R2
combined (R1 consumed 0) and US$1 total, with keys used only by reference.
The paired R2 baseline, roadmap T6 row, root live-proof rule, and current
session surfaces govern this execution. Provider-specific memory is not
canonical evidence.

## Required First Reads

The numbered list in the preceding Authority Chain section is mandatory and
must be completed before any preflight or provider action.

## Agent Roles

| Role | Responsibility |
|---|---|
| Operator | authorizes bounded key use, calls, cost ceiling, and the free-quota gate substitution |
| Dispatcher | authors and validates the R2 packet; makes zero API calls |
| Worker | executes preflight and proof, writes seven paths, commits nothing |
| Reviewer/closer | independently verifies and owns material closure commits |

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intake summary | retry bounded T6 live proof under a free-quota cost gate after R1's pricing-page coverage gap |
| scope classification | LIVE_PROOF_NO_COMMIT |
| primary task class | runtime-provider-live compatibility proof |
| risk sensitivity | high: secrets, quota, cost and live claim |
| selected role route | SINGLE_AGENT_SINGLE_ROLE |
| orchestration requirement | no-commit worker then independent reviewer |
| role separation basis | worker cannot accept its own live evidence |
| escalation condition | preflight, authority, ceiling, free-quota-gate uncertainty, or scope violation |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification | State |
|---|---|---|---|---|
| T6 credentials | Secret Handling | alias presence status | secret-safe preflight | MAPPED |
| T6 call/cost bounds | Cost And Call Ceiling | call ledger and free-quota-gate evidence | worker return | MAPPED |
| T6 synthetic sandbox | Synthetic Input | safe payload boundary | worker return | MAPPED |
| T6 live proof | Required Live-Proof Execution | result and manifest JSON | reviewer verification | MAPPED |
| T6 diagnostic | Diagnostic And Retry Protocol | SOT3/E2E diagnostics | fast gate | MAPPED |

## Worker Autonomy / No-Question Rule

Proceed without routine confirmation for non-destructive actions inside the
allowed scope. Stop only for source contradiction, unrelated dirty state,
failed mandatory preflight, missing credential alias, free-quota-gate
uncertainty, cost/call ceiling risk, or a need to touch forbidden scope. Do
not ask permission merely to run the authorized exact command after all
preflight conditions pass.

## Pre-Flight Checks

At start:

```powershell
git rev-parse HEAD
git status --short
where.exe node
where.exe npm
where.exe npx
node --version
npm --version
npx --version
python scripts/run_cvf_release_gate_bundle.py --dry-run --e2e --json
python scripts/run_cvf_sot3_a4_failure_recovery_proof.py --local-only --json --receipt docs/reviews/evidence/cadp-ai-t6-r2-local-negative-receipt-2026-08-15.json
```

Requirements:

- HEAD must be the clean dispatcher-return HEAD and staging must be empty;
- the dedicated `--receipt` argument must keep the historical
  `sot3-act-a4-failure-recovery-negative-receipt-2026-07-13.json` unchanged;
- node, npm, and npx must all resolve in this same PowerShell process; npm and
  npx must resolve through the active NVM4W nodejs path, not through an
  assumed `nvm use` side effect;
- record only environment path/version facts, never secret values;
- verify at least one accepted key alias as `PRESENT_REDACTED` using the
  repository bootstrap behavior, without a probe API call;
- run the focused route negative gate locally without live-run permission;
- complete the Free-Quota Cost Gate (below) before any call;
- verify all seven output paths are absent;
- any failure means `BLOCKED_WITH_REASON`, zero provider calls.

## Allowed Scope And Write Ownership

The worker may create exactly:

1. `docs/reviews/CVF_CADP_AI_T6_R2_QWEN37_FLASH_FREE_QUOTA_COST_GATE_RETRY_WORKER_RETURN_2026-08-15.md`
2. `docs/reviews/evidence/cadp-ai-t6-r2-free-quota-preflight-2026-08-15.json`
3. `docs/reviews/evidence/cadp-ai-t6-r2-local-negative-receipt-2026-08-15.json`
4. `docs/reviews/evidence/cadp-ai-t6-r2-release-gate-result-2026-08-15.json`
5. `docs/reviews/evidence/cadp-ai-t6-r2-release-gate-manifest-2026-08-15.json`
6. `docs/reviews/evidence/cadp-ai-t6-r2-sot3-diagnostic-2026-08-15.json`
7. `docs/reviews/evidence/cadp-ai-t6-r2-e2e-diagnostic-2026-08-15.json`

Every other path is forbidden. Do not modify or delete existing files; the
dedicated R2 local-negative receipt prevents reuse of the historical receipt
path. Do not stage or commit; do
not edit `.env.local`; do not change source, tests, configuration, model
ledgers, registry, roadmap, session, handoff, aggregate, scripts, hooks, or
CI. Do not rotate credentials, mutate quota, invoke an external CLI/MCP
agent, deploy, push, or public-sync.

## Write Ownership

Worker ownership is limited to the seven paths above. The independent reviewer
owns any completion review, roadmap projection, material commit, and later
session/handoff synchronization.

## Provider And Model Selection Rule

- Exact provider route: Alibaba/DashScope-compatible.
- Exact model sent by the canonical route: `qwen3.7-flash` (unchanged from
  R1).
- Governed snapshot reference: `qwen3.7-flash-2026-07-15`.
- Never use or fall back to removed model `qwen-turbo`, and do not substitute
  any other model; this packet authorizes only `qwen3.7-flash`.
- Accepted secret aliases: `DASHSCOPE_API_KEY`, `ALIBABA_API_KEY`,
  `CVF_ALIBABA_API_KEY`, `CVF_BENCHMARK_ALIBABA_KEY`.
- Canonical route:
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.sot3-activation.alibaba.live.test.ts`.

## Free-Quota Cost Gate (Replaces R1's Official-Pricing Gate)

Before any provider call, in place of R1's pricing-arithmetic requirement,
the worker must establish and record all of the following in the dedicated
preflight receipt
`docs/reviews/evidence/cadp-ai-t6-r2-free-quota-preflight-2026-08-15.json`:

1. **currentGovernedConsoleEvidence**: cross-check
   `docs/reference/model_gateway/CVF_ALIBABA_FREE_QUOTA_MODEL_LEDGER.json`'s
   `qwen3.7-flash` row against the execution date; confirm execution date is
   on or before `expirationDate` `2026-10-22`; record the ledger
   `captureDate` `2026-08-15` and note explicitly whether this is a
   same-session live console pull or a reused governed-ledger snapshot. If
   only the ledger snapshot is available in this environment, that is
   acceptable evidence provided it is disclosed as such, not silently
   presented as a fresh console read.
2. **freeQuotaOnlyToggleState**: cite official documentation
   `https://www.alibabacloud.com/help/en/model-studio/new-free-quota`
   (record exact URL and access date) for the toggle's behavior: when
   enabled, exceeding the free quota halts the call with error
   `AllocationQuota.FreeTierOnly` and applies zero charge. Record whether the
   worker confirms the account state from the R2 baseline's governed
   operator screenshot when execution remains on capture date 2026-08-15,
   or from a fresher console observation. Record the evidence source and
   whether it is a same-session pull. A later-date execution without fresher
   evidence must record `UNCONFIRMED` and stop with `BLOCKED_WITH_REASON`.
3. **remainingQuotaAboveCeiling**: record the ledger's
   `freeQuotaRemaining` value for `qwen3.7-flash` and confirm it exceeds a
   conservative worst-case total-token estimate for one bounded request
   (`max_tokens` 4096 output, plus a reasonable fixed input bound well under
   the remaining quota).
4. **officialDocumentationCitation**: the exact URL, access date, and the
   toggle-name/halt-error/zero-charge-guarantee language from point 2,
   recorded with an exact source locator. Disposition: ADAPTED_WITH_REASON.

If any of points 1 through 4 cannot be established, stop with
`BLOCKED_WITH_REASON` and zero calls. Do not proceed on an assumption that
the toggle is enabled or that quota is sufficient without recorded evidence.

## Cost And Call Ceiling

- Maximum cumulative real provider calls across R1 and R2: 3. R1 made 0, so
  up to 3 remain available to R2; expected and accepted count for R2 is
  exactly 1.
- Total charge ceiling: US$1, unchanged.
- No probe call and no blind retry. A second call requires a recorded,
  result-changing remediation and must remain inside both ceilings.
- The Free-Quota Cost Gate above replaces R1's official-pricing-plus-
  arithmetic requirement as the pre-call financial-exposure control; it does
  not relax the ceiling.

## Synthetic Input, Data Retention, And Secret Handling

Use only repository-defined synthetic, non-sensitive test content. Load keys
by reference from
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/.env.local` through
`scripts/_local_env.py`. Report only alias names and `PRESENT_REDACTED`,
`EMPTY`, or `NOT_FOUND`. Never print or persist key values, bearer tokens,
signed headers, unredacted request bodies, or raw provider response bodies.
No deliberate provider-side storage upload is authorized, and this packet
makes no claim about provider retention.

## Required Live-Proof Execution

After every preflight condition and the Free-Quota Cost Gate pass, run
exactly:

```powershell
python scripts/run_cvf_release_gate_bundle.py --e2e --json --output docs/reviews/evidence/cadp-ai-t6-r2-release-gate-result-2026-08-15.json --manifest-output docs/reviews/evidence/cadp-ai-t6-r2-release-gate-manifest-2026-08-15.json --sot3-diagnostic-output docs/reviews/evidence/cadp-ai-t6-r2-sot3-diagnostic-2026-08-15.json --e2e-diagnostic-output docs/reviews/evidence/cadp-ai-t6-r2-e2e-diagnostic-2026-08-15.json
```

`--e2e` selects the UI-only mock Playwright supplement while the mandatory
SOT3 path remains real; it does not authorize `--e2e-live`. The SOT3 A5/A4
path is the governance acceptance surface and must observe exactly one real
Alibaba recovery call. Mock output alone is never acceptance evidence.

## Diagnostic And Retry Protocol

Before execution, record a secret-safe precheck containing executable
resolution, versions, key-alias statuses, dry-run selection, local focused
test result, the four Free-Quota Cost Gate points, expected call count, and
current call counter. On any failure, partial result, timeout, or ambiguity,
stop and record `stage`, `class`, `retryable`, `userAction`, `safeMessage`,
and `httpStatus` when available. A retry is allowed only after an explicit
result-changing remediation is recorded and the cumulative count/cost remains
inside the ceilings. Never blind-retry.

## Evidence Output Paths

The exact seven paths in Allowed Scope are the complete worker manifest. The
quota preflight receipt, local-negative receipt, and four release-bundle JSONs must be secret-safe and
schema-compatible with the release bundle, manifest builder, and diagnostic
writers. Write the preflight receipt first, then let the primary command
produce its four JSONs, then write the worker return last, after evidence
stabilizes.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| primary command and flags | LITERAL_INVARIANT | `scripts/run_cvf_release_gate_bundle.py` | argparse | `--e2e`; output/manifest/diagnostic flags | release bundle | ACCEPT |
| no mock bypass | LITERAL_INVARIANT | `scripts/run_cvf_release_gate_bundle.py` | SOT3 check | mock has no effect on SOT3 | release bundle | ACCEPT |
| environment bootstrap | LITERAL_INVARIANT | `scripts/_local_env.py` | `bootstrap_repo_env` | default env files | local env loader | ACCEPT |
| exact one-call admission | VALUE_SET | `scripts/run_cvf_sot3_a5_release_proof.py` | admission constants | `REQUIRED_RECOVERY_PROVIDER_CALL_COUNT` | SOT3 A5 | ACCEPT |
| live route and aliases | VALUE_SET | `scripts/run_cvf_sot3_a4_failure_recovery_proof.py` | live constants | `LIVE_TEST_RELATIVE_PATH`; `ALIBABA_KEY_ALIASES` | SOT3 A4 | ACCEPT |
| exact live model | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.sot3-activation.alibaba.live.test.ts` | Alibaba request | `qwen3.7-flash` | live route | ACCEPT |
| current model/quota | VALUE_SET | `docs/reference/model_gateway/CVF_ALIBABA_FREE_QUOTA_MODEL_LEDGER.json` | `qwen3.7-flash` model row | `freeQuotaRemaining`; `expirationDate`; `statusAtCapture` | quota ledger | ACCEPT |
| R1 blocker and reviewer acceptance | VALUE_SET | `docs/reviews/CVF_CADP_AI_T6_R1_QWEN37_FLASH_LIVE_COMPATIBILITY_RETRY_WORKER_RETURN_2026-08-15.md` | top `Status:` and Reviewer Acceptance Note | `REVIEWER_ACCEPTED_BLOCKED_R1_REOPEN_R2_SAME_MODEL` | R1 worker return | ACCEPT |
| real-call requirement | LITERAL_INVARIANT | `AGENTS.md` | Mandatory Live Governance Proof | real provider API call | root carrier | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | `Dispatch Prompt Envelope`; `Source Verification Block`; `Checker Source Read-Ahead Block`; `Agent Handoff Contract Control Block`; `Dual Agent Surface Matrix`; `Reviewer Closure Conversion`; `Work-Order Fulfillment Manifest`; `Worker Return Packet Shape Contract`; `WORKER_MUST_NOT_COMMIT`; `Public Export Disposition` |
| gateRunPurpose | confirmation and evidence after checker-source read-ahead, not first discovery |
| claimBoundary | structural PASS cannot substitute for a real provider receipt or for confirmed free-quota-toggle state |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind runtime-provider-live --batch-id CADP-AI-T6-R2 --title "CADP AI T6 R2 Qwen3.7 Flash Free Quota Cost Gate Retry" --date 2026-08-15 --base c607779d31771dbdd9e789baf69ba297e01de2f5 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | runtime-provider-live plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| scaffoldedSections | envelope, source verification, handoff, reviewer conversion, return contract, trace, delta and public disposition |
| manualEditsAfterScaffold | bound R1 reviewer-accepted predecessor, free-quota cost gate replacing pricing gate, dedicated R2 evidence paths, seven-path manifest, official free-quota documentation citation requirement |
| checkerReadAheadConfirmation | all listed checker sources read before authoring |
| docOnlyNewFields | Free-Quota Cost Gate fields (`currentGovernedConsoleEvidence`, `freeQuotaOnlyToggleState`, `remainingQuotaAboveCeiling`, `officialDocumentationCitation`) are new doc-only preflight-receipt field names introduced by this dispatch; no runtime schema change |
| claimBoundary | dispatch authoring only; no API call |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| exact baseline/work-order paths | absent before authoring | ABSENT_BEFORE_AUTHORING |
| `CADP-AI-T6-R2` bounded search | no prior owner | NO_COLLISION |
| historical R1 | R1 packet and reviewer-accepted-blocked return reused as immutable evidence | REUSE_AS_SOURCE_NOT_DUPLICATE_OWNER |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`, surfaceSelector=`cadp`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class dispatch --role dispatcher --lifecycle-phase pre-dispatch --surface-selector cadp --risk-ceiling HIGH --max-results 10 --json` |
| Returned defect count | 0 |
| Returned defects | none |
| Disclosed defectIds | none |
| Dispatch impact | no added constraint; executable, free-quota-gate, and no-live-claim gates remain mandatory |

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | NO: worker has not run R2 |
| liveProofAuthorized | YES only after all preflight gates including the Free-Quota Cost Gate pass |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | source verified at dispatch HEAD; worker performs fresh proof and a fresh free-quota-gate check |
| reason | R1 made zero provider calls and its blocker was a pricing-page coverage gap, not a compatibility failure |
| requiredFutureAction | execute exact command and return secret-safe evidence uncommitted |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | release bundle and SOT3 scripts | bounded R2 proof only | future seven-path receipt | none | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | none | no invocation, credentials, mutation, or public authority | separate T5 decision | fresh packet | `DEFERRED_WITH_REASON` |

## Agent Handoff Contract Control Block

Contract locator archive `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` retained for machine compatibility.

| Field | Requirement |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | one no-commit worker followed by independent reviewer/closer |
| phase | worker execution pending |
| baseHeadFor(phase) | dispatchBaseHead=`8ce45e190b16f9dc262ef672016fa758d9d04daa`; executionBaseHead=`WORKER_MUST_CAPTURE_AT_START`; closureBaseHead=`REVIEWER_TO_SET` |
| executionBaseHead | capture exact dispatcher-return HEAD before edits; clean worktree Before status evidence is mandatory |
| dirtyPathPolicy | zero unrelated dirty paths beyond the known mandated-command receipt refresh |
| changedSetScope(phase) | exact seven R2 paths |
| traceScope(phase, actor) | reads, preflight, free-quota-gate evidence, commands, calls, diagnostics, diff, status and gates |
| operationReceiptWriteOrder | preflight receipt first; evidence JSON next; worker return last |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer owns commits |
| crossBatchIsolation | no R1 or unrelated path changes |
| nextMoveSurfaces | independent review/closure then separate session sync |
| commitBoundary | worker staging empty and HEAD unchanged |

## Reviewer Closure Conversion

| Field | Requirement |
|---|---|
| completionReviewPath | `docs/reviews/CVF_CADP_AI_T6_R2_QWEN37_FLASH_FREE_QUOTA_COST_GATE_RETRY_COMPLETION_2026-08-15.md` (optional) |
| reviewerOwnedClosurePaths | optional completion review; CADP T6 roadmap projection; separate session continuity |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |
| publicRule | no export claim without public-sync remote, commit, and artifact evidence |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| worker return | record execution/final HEAD, preflight, exact model, free-quota-gate evidence, calls, cost, diagnostics, gates and no-commit state |
| preflight receipt | dedicated R2 JSON recording the four Free-Quota Cost Gate points before the primary command |
| local-negative receipt | dedicated R2 `--receipt` output proving the local matrix without touching historical evidence |
| result JSON | primary command `--output` |
| manifest JSON | primary command `--manifest-output` with hashes and safe rerun metadata |
| SOT3 diagnostic JSON | primary command `--sot3-diagnostic-output` |
| E2E diagnostic JSON | primary command `--e2e-diagnostic-output` |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_CADP_AI_T6_R2_QWEN37_FLASH_FREE_QUOTA_COST_GATE_RETRY_WORKER_RETURN_2026-08-15.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Before writing outputs, read checker source for each docType/path family. The
return must include Work-Order Fulfillment Manifest reconciliation, Source
Verification, Checker Source Read-Ahead, Agent Operation Trace, Delta
Execution Claim Boundary, Public Export Disposition, exact changed set,
staging status, and no-commit evidence.

## Acceptance Criteria And Return Conditions

Return `COMPLETE_PENDING_INDEPENDENT_REVIEW` only when:

- node/npm/npx preflight passed in the execution shell;
- exact model `qwen3.7-flash` made exactly one real non-mock SOT3 call;
- the Free-Quota Cost Gate's four points are all established and recorded,
  including a confirmed (not assumed) Free Quota Only toggle state;
- all evidence JSONs (preflight receipt plus four release-bundle JSONs) and
  the worker return exist at exact paths and are secret-safe;
- worker-return fast gate and required verification pass;
- exactly seven paths changed, staging is empty, HEAD unchanged, and no commit
  was made.

Return `BLOCKED_WITH_REASON` for any unmet preflight, missing credential,
free-quota-gate uncertainty (including an unconfirmed toggle state),
local/live failure, ceiling risk, ambiguity, or forbidden-scope need. State
cumulative provider calls (across R1 and R2) and quota consumed; zero is
expected for every pre-call blocker.

## Execution Plan

| Step | Action | Evidence |
|---|---|---|
| 1 | capture clean execution base; complete required reads | `git rev-parse HEAD`; `git status --short` |
| 2 | verify executables, local selection, key-alias presence | `where.exe`/`--version` outputs; alias presence table |
| 3 | run dry-run and SOT3 A4 local-only negative gate | dry-run JSON; `--local-only` receipt |
| 4 | establish and record Free-Quota Cost Gate evidence | `cadp-ai-t6-r2-free-quota-preflight-2026-08-15.json` |
| 5 | run the exact primary command once | four release-bundle evidence JSONs |
| 6 | write the worker return last | worker return with fast-gate PASS |
| 7 | run fast gates, reconcile the seven-path manifest, leave HEAD unchanged | gate output; `git status --short`; `git diff --cached` |

## Evidence Requirements

Record exact commands and outcomes, executable paths/versions, alias presence
statuses, the four Free-Quota Cost Gate points with their evidence sources,
exact model, real call count, cost bound, diagnostics, evidence hashes,
changed set, staging state, and execution/final HEAD. Never include a raw
secret or provider body.

## Review Gate

The independent reviewer must challenge executable resolution, exact model,
free-quota-gate evidence and official documentation citation, call
cardinality, mock exclusion, secret safety, evidence schema, seven-path
isolation, and no-commit state. Machine gate success is necessary but not
semantic acceptance.

## Closure Checklist

- [ ] node/npm/npx preflight PASS in execution shell
- [ ] exact `qwen3.7-flash`, one real SOT3 call
- [ ] Free-Quota Cost Gate evidence complete, toggle state confirmed
- [ ] exact seven secret-safe paths
- [ ] worker-return fast gate PASS
- [ ] staging empty, HEAD unchanged, no worker commit

## Return-To-Orchestrator Conditions

Return only one disposition: `COMPLETE_PENDING_INDEPENDENT_REVIEW` after full
acceptance evidence, or `BLOCKED_WITH_REASON` with a secret-safe blocker,
cumulative call count, and quota/cost impact.

## Operator Checkpoint

No model substitution, source remediation, credential rotation, retry beyond
the recorded protocol, deployment, public sync, production action, T5 work,
or external CLI/MCP use opens from this packet. Such a move requires fresh
operator authority and governed dispatch.

## Verification Commands

```powershell
git rev-parse HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git diff --name-only
git diff --cached --name-only
git rev-parse HEAD
```

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | local repository tools plus two official Alibaba documentation fetches |
| Session or invocation | CADP-AI-T6-R2 dispatch, 2026-08-15 |
| Working directory | repository root |
| Command or tool surface | PowerShell, repository Python guards, web documentation fetch |
| Target paths | paired R2 baseline and work order |
| Allowed scope source | operator authorization proposing the free-quota gate substitution, 2026-08-15 |
| Before status evidence | clean worktree at HEAD `8ce45e190b16f9dc262ef672016fa758d9d04daa`; R1 reviewer-accepted-blocked is committed and anchored |
| After status evidence | exact paired dispatch paths before validation |
| Diff evidence | `git diff --name-status` |
| Approval boundary | dispatch authoring only; zero API calls |
| Claim boundary | packet and local-gate evidence only |
| Agent type | single dispatcher role |
| Invocation ID | `cadp-ai-t6-r2-dispatch-2026-08-15` |
| Expected manifest | paired R2 baseline and work order |
| Actual changed set | paired R2 baseline and work order |
| Manifest delta | MATCH |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | repo-local CADP-AI-T6-R2 dispatch |
| claimDisposition | CLAIM_REJECTED: no runtime enforcement or provider compatibility claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: dispatch has no live receipt |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: dispatch made zero API calls |
| invocationBoundary | local reads, guards, two documentation fetches, and document authoring only |
| interceptionBoundary | no wrapper, proxy, hook, mandatory runtime gate, or process interception |
| claimLanguage | bounded live retry authorization pending worker execution and review |
| forbiddenExpansion | no production, universal-provider, trusted-evidence, deployment, public-export, T5, CLI/MCP, or cross-runtime claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: the proof uses private credentials and private provenance workflow;
there is no public-sync authorization or evidence.

## Claim Boundary

This work order authorizes exactly one bounded R2 live proof using
`qwen3.7-flash` after mandatory preflight including the Free-Quota Cost Gate.
It makes no live claim itself and does not authorize source/config mutation,
deployment, production action, public sync, external CLI/MCP use, staging,
or worker commit.
