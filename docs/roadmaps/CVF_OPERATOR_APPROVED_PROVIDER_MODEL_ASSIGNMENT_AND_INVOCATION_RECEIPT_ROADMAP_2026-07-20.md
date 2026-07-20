# CVF Operator-Approved Provider/Model Assignment And Invocation Receipt Roadmap

Memory class: governed-roadmap

Status: PARKED_BY_GLOBAL_CLI_MCP_INVOCATION_CONTROL_REASSESSMENT

Date: 2026-07-20

Roadmap ID: CVF-OPM-AIR

## Purpose

Add a provider-neutral control-plane contract that lets an operator approve a
bounded provider/model envelope, lets an orchestrator assign one approved
provider/model to a task, and requires secret-safe evidence of which
provider/model actually executed. The roadmap closes the operational gap seen
when a worker exhausts time or quota and another approved provider, model, API
key, or account subscription may be needed.

This roadmap does not create a new model gateway. It extends the existing CVF
Model Gateway foundations with operator approval, task assignment, and
assigned-versus-actual reconciliation semantics.

## Operator Decision Carried Forward

The operator requires all future agent sessions to declare the model used and
wants a later orchestrator to assign provider/model per task inside an
operator-approved envelope. CVF must not hardcode a provider. The operator may
supply API-key access or an account subscription. Raw keys, tokens, cookies,
or subscription secrets must never enter governed artifacts or receipts.

The 2026-07-20 T2 repair used a task-specific operator assignment of
`claude-sonnet-5` at effort `high`. That invocation is evidence for the gap,
not a default, recommendation, provider preference, or runtime foundation.

## Authorization / Decision

The operator authorized this provider-neutral roadmap after Continuous
Projection T2 closure and, on 2026-07-20, explicitly started T0 with this
sequence: reviewer/orchestrator opens the roadmap; Claude authors the work-order
packet; reviewer repairs and accepts it; Claude executes as no-commit worker;
reviewer repairs, closes, and reports tranche findings and learning candidates
to the operator. The packet is reviewer-accepted and committed. The first
worker attempt reached a subscription-session limit without producing output,
so only a fresh T0 R1 worker invocation under the bounded profile below is now
released. T1-T5, credential use, provider calls, fallback, public action, and
deployment remain parked.

## Global Invocation-Control Reassessment Override - 2026-07-20

The operator revoked the T0 R1 rerun authorization and parked every roadmap
after the first delegated-agent experiment exhausted the five-hour Claude
session quota. The interim bounded profile below remains incident evidence; it
is not executable authority.

This roadmap is superseded for execution by
`docs/audits/CVF_AGENT_CLI_MCP_INVOCATION_CONTROL_SYSTEM_CHAIN_REASSESSMENT_2026-07-20.md`.
No subscription reset, available model, account subscription, API key, old
dispatch packet, or roadmap-local next step may restart T0 or any later tranche.
Only a fresh explicit operator decision after the read-only reassessment can
lift the global moratorium.

## Operator Usage Baseline Snapshot

The operator supplied a Claude plan-usage screenshot immediately before T0:

| UI measure | Observed value | Evidence boundary |
|---|---:|---|
| current session | 21 percent used; reset shown in 4 hours 13 minutes | operator-provided UI snapshot; not an API quota receipt |
| weekly all-models | 41 percent used; reset shown Tuesday 10:00 PM | operator-provided UI snapshot; plan limits were shown as temporarily boosted |
| usage credits | off | no paid overage authorization |
| usage-credit spend | USD 0.00; reset shown August 1 | UI snapshot only |

T0 must preserve this as `OPERATOR_UI_SNAPSHOT` evidence and pair it with
deduplicated Claude CLI JSONL usage by unique `message.id`. UI percentages,
token counters, billed API cost, and subscription quota are distinct
measurement classes and must never be silently converted into one another.

## T0 Invocation-Cost Incident And Immediate Control

The first T0 worker invocation ended before creating any artifact because the
Claude subscription reported a session limit. The operator supplied a second
UI snapshot showing current-session usage at 100 percent and weekly all-models
usage at 45 percent. This is `OPERATOR_UI_SNAPSHOT` evidence only; the change
from the earlier 21/41 snapshot must not be converted into tokens, dollars, or
per-invocation attribution.

The exact failed worker session basename is
`62571339-7d3f-4865-9141-7e59dd67776b.jsonl`. Secret-safe deduplication by
unique `message.id` produced 11 responses, 20 input tokens, 196127 cache-create
tokens, 1154709 cache-read tokens, 5622 output tokens, and 87.5 seconds elapsed.
The final diagnostic was `SUBSCRIPTION_SESSION_LIMIT`; no cost field was
present. No output file, staged change, commit, retry, or fallback resulted.

The preceding packet-author session produced 147 unique responses, 47856327
cache-read tokens, 131666 output tokens, 73 Bash calls, 57 Read calls, and 21
Edit calls. A single CLI command therefore cannot be treated as one provider
response or as a bounded-cost unit.

Before any T0 R1 worker redispatch, the caller must enforce this interim
bounded-invocation profile:

- start a new session; do not resume either enlarged T0 session;
- retain the operator-assigned model and effort, but use Claude `--safe-mode`;
- expose only `Read`, `Write`, `Edit`, and `Bash`; disable MCP, plugins,
  TaskCreate, TaskUpdate, ToolSearch, browser, and subagent surfaces;
- allow one focused gate pass and one allowed-scope repair pass only;
- stop at 10 elapsed minutes, 24 unique model responses, 3000000 cumulative
  cache-read tokens, or 40000 cumulative output tokens, whichever occurs first;
- terminate the caller and its child process tree when a limit is crossed;
- classify the result `INVOCATION_BUDGET_EXCEEDED` or
  `SUBSCRIPTION_SESSION_LIMIT` before any later attempt; and
- never retry, resume, change model/provider, or use fallback without a fresh
  operator-approved assignment.

This interim profile prevents another uncontrolled call. T1 must ratify the
provider-neutral budget fields, while a later source-verified implementation
tranche owns a reusable launcher and tests. The profile is not a claim that
Claude subscription quota can be converted to API dollars or that
`--max-budget-usd` governs account-subscription usage.

## Authority And Existing Foundation

| Existing owner | Reused capability | Roadmap boundary |
|---|---|---|
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | provider records, models, status, capabilities, and selection options | reuse as the provider registry owner; do not create or hardcode a replacement |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | `PROVIDER_CAPABILITY_REGISTRY` capability records | reuse as the provider capability owner; do not create a parallel capability registry |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/dynamic-model-registry-contract.ts` | provider/model identity, capability, tier, cost, latency, rate-limit, and health metadata | reuse for candidate discovery; do not duplicate a registry |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-receipt.ts` | requested/selected model, provider, decision, fallback, credential fingerprint, validation state, and redacted metadata | extend or compose; do not create an unrelated receipt silo |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/credential-boundary.ts` | environment-backed credential references and secret-safe metadata | broaden only through a source-verified adapter contract if account subscriptions are supported |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/fallback-policy.ts` | bounded attempts and retryable status handling | subordinate fallback to operator approval; never infer cross-provider permission |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | selected provider/model execution, quota/health/credential checks, actual response model, and receipt production | integrate after contract ratification; no duplicate execution bridge |
| `docs/reference/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md` | failure classification before retry | reuse for timeout, quota, authentication, availability, and mismatch diagnostics |

## Problem Statement

Current foundations can select and execute a provider/model, but they do not
yet prove all of the following as one operator-controlled chain:

1. the operator approved the provider/model and credential-source envelope;
2. the orchestrator assigned an exact approved provider/model to one task;
3. the invocation resolved to that exact provider/model or an explicitly
   permitted fallback;
4. the credential source was referenced without exposing a secret;
5. time, quota, authentication, availability, and model mismatch were
   classified before retry or reassignment; and
6. the reviewer can reconcile approval, assignment, invocation, and result
   without relying on chat history or provider-local memory.

## Scope / Target / Owner Boundary

In scope:

- provider-neutral approval, assignment, invocation, and reconciliation schemas;
- secret-safe references for API-key and account-subscription access;
- exact provider/model identity and alias-resolution evidence;
- capability, cost/quota, latency, expiry, and fallback bounds;
- deterministic reviewer checks and negative fixtures;
- integration planning over existing Model Gateway owners;
- operator and orchestrator responsibilities.

Out of scope:

- storing, printing, copying, or committing raw credentials;
- hardcoding or preferring Claude, Codex, OpenAI, Anthropic, Alibaba,
  DeepSeek, or any other provider;
- creating a second model registry, execution bridge, credential store, or
  fallback engine;
- provider onboarding, commercial negotiation, billing automation, or account
  creation;
- live calls before a separately authorized live-proof tranche;
- automatic fallback outside the approved envelope;
- changing agent prompts, quality policy, or model rankings in this roadmap;
- public-sync, deployment, or production release.

## Non-Goals

- no default-provider or preferred-provider policy;
- no provider quality ranking or benchmark in this roadmap;
- no replacement for `provider-registry.ts`,
  `PROVIDER_CAPABILITY_REGISTRY`, the dynamic model registry, gateway receipt,
  credential boundary, fallback policy, or provider execution bridge;
- no secret manager, account-subscription login automation, or credential
  persistence;
- no live proof, production orchestration, or public release.

## Design Principles

1. Operator authority is explicit, bounded, expiring, and revocable.
2. Assignment is task-specific and cannot widen the approval envelope.
3. Actual runtime identity is evidence, not inferred from a CLI argument.
4. Provider aliases must resolve to canonical identities before execution.
5. Unknown identity, unapproved fallback, or missing reconciliation fails closed.
6. Credentials are referenced by type and secret-safe locator only.
7. Existing gateway, registry, receipt, quota, health, and diagnostic owners are
   composed rather than replaced.
8. Every retry has a classified reason and consumes an approved attempt budget.

## Design Control Gate

Before any implementation tranche, the source map must show whether each
proposed field extends an existing owner, composes existing evidence, or is a
new doc-only contract. A design review blocks dispatch if it finds duplicate
registry/receipt/bridge ownership, provider-specific assumptions, raw-secret
storage, unverifiable actual-model identity, or fallback authority wider than
the operator approval envelope.

## Proposed Contract Groups

All fields below are proposed doc-only fields until a source-verified GC-018
and work order ratify them.

### A. Operator Approval Envelope

| Field | Meaning |
|---|---|
| `approvalId` | stable approval identity |
| `operatorId` | secret-safe operator identity or local operator marker |
| `approvedProviders` | canonical provider identities or bounded families |
| `approvedModels` | canonical model identities, families, or constrained selectors |
| `requiredCapabilities` | task capabilities that candidates must satisfy |
| `credentialSourceType` | provider-neutral class such as environment key, account subscription, managed identity, or external secret reference |
| `credentialReference` | secret-safe locator; never the secret value |
| `costQuotaCeiling` | approved cost, token, request, or subscription quota boundary |
| `latencyCeilingMs` | optional operator-approved latency boundary |
| `fallbackPolicy` | forbidden, same-model retry, same-provider alternate, or explicit approved cross-provider set |
| `validFrom` / `expiresAt` | approval time window |
| `reapprovalTriggers` | model/provider change, capability change, credential change, expiry, cost change, or policy change |
| `approvalHash` | deterministic identity over non-secret approval content |

### B. Task Assignment Receipt

| Field | Meaning |
|---|---|
| `assignmentId` | stable assignment identity |
| `taskId` | governed task or work-order identity |
| `approvalId` | approval envelope consumed |
| `assignedProviderId` | exact canonical provider identity |
| `assignedModelId` | exact canonical model identity |
| `assignedEffort` | optional provider-neutral effort/reasoning class mapped by adapter |
| `requiredCapabilities` | task-required capability set |
| `selectionReason` | source-backed reason inside the approved envelope |
| `inputHash` | deterministic hash of non-secret task input or dispatch identity |
| `fallbackPermission` | exact bounded fallback set or forbidden marker |
| `assignedBy` | orchestrator or reviewer identity |
| `assignedAt` | assignment timestamp |

### C. Invocation Receipt

| Field | Meaning |
|---|---|
| `invocationId` | stable invocation identity |
| `assignmentId` / `approvalId` | chain to task authority |
| `adapterId` / `adapterVersion` | provider adapter identity |
| `requestedProviderId` / `requestedModelId` | assignment passed to the execution surface |
| `actualProviderId` / `actualModelId` | canonical identity reported or independently extracted from the invocation |
| `actualEffort` | resolved provider-neutral effort class when observable |
| `credentialSourceType` / `credentialReference` | secret-safe access provenance |
| `fallbackUsed` / `fallbackFrom` | exact fallback evidence |
| `usageMeasurement` | measured tokens/cost class or unavailable-with-reason |
| `latencyMeasurement` | measured duration class or unavailable-with-reason |
| `diagnosticClass` | success or classified timeout/quota/authentication/availability/mismatch result |
| `reconciliationResult` | exact match, approved fallback match, or blocking mismatch |
| `receiptHash` | deterministic identity over secret-safe receipt content |

### D. Reviewer Reconciliation Decision

The reviewer must join `approvalId`, `assignmentId`, and `invocationId`, then
verify:

- approval was current and covered the canonical assigned identities;
- task requirements did not exceed approved capabilities or budget;
- actual identities exactly matched the assignment or an explicitly approved
  fallback;
- credential references were secret-safe and did not contain credential data;
- retry/fallback counts remained inside the approved policy;
- failures were classified before another live attempt; and
- any mismatch blocks acceptance and returns to the operator or orchestrator.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| provider registry owner exists | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | `ProviderRecord` interface | `ProviderRecord` | provider registry | ACCEPT |
| provider capability registry exists | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | exported registry declaration | `PROVIDER_CAPABILITY_REGISTRY` | provider capability registry | ACCEPT |
| provider/model records exist | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/dynamic-model-registry-contract.ts` | `DynamicModelRecord` interface | `providerId`; `modelId` | dynamic model registry contract | ACCEPT |
| capability-aware candidate query exists | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/dynamic-model-registry-contract.ts` | `FindOptimalQuery` interface | `requiredMethod`; `allowedProviderIds`; `blockedProviderIds` | dynamic model registry contract | ACCEPT |
| requested and selected model receipt fields exist | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-receipt.ts` | `GatewayReceiptInput` | `requestedModelId`; `selectedModelId` | gateway receipt schema | ACCEPT |
| fallback receipt evidence exists | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-receipt.ts` | `GatewayReceiptInput` and `GatewayReceipt` | `fallbackFromProviderId`; `fallbackFromModelId`; `fallback` | gateway receipt schema | ACCEPT |
| secret-safe credential metadata exists | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/credential-boundary.ts` | `CredentialReference`; `CredentialMetadata` | `keyId`; `envNames`; `fingerprint`; `redactedValue` | credential boundary | ACCEPT |
| current credential source is environment-only | VALUE_SET | `EXTENSIONS/CVF_MODEL_GATEWAY/src/credential-boundary.ts` | `CredentialMetadata.source` | `source` | credential metadata schema | ACCEPT |
| fallback attempt budget exists | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/fallback-policy.ts` | `FallbackPolicyConfig`; `FallbackDecision` | `maxAttempts`; `remainingAttempts` | fallback policy | ACCEPT |
| execution response reports provider/model | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | success response assembly | `response.model.providerId`; `response.model.modelId` | provider execution bridge | ACCEPT |
| quota and credential failures exist | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | `execute` failure branches | `quota_exceeded`; `credential_shielded` | provider execution bridge | ACCEPT |

## New Doc-Only Fields

Every field in Proposed Contract Groups A-D is `DOC_ONLY_NEW` unless the
Source Verification Block explicitly maps it to an existing runtime symbol.
Names may change only through a future source-fidelity pass; this roadmap does
not claim they already exist in runtime.

## Work Plan

### T0 - Source Map And Contract Gap Baseline

Produce a fresh GC-018 that maps every proposed field to an existing owner,
an extension seam, or a doc-only proposal. Reconcile Model Gateway, control
plane, execution plane, agent handoff, live diagnostics, and receipt-envelope
owners. Explicitly reject duplicate registry, bridge, credential, and receipt
owners.

### T1 - Approval And Assignment Contract

Ratify provider-neutral operator approval and task assignment schemas with
deterministic hashes, expiry/revocation, capability and budget bounds, and
secret-safe credential references. Prove API-key and account-subscription
classes without storing credentials.

### T2 - Invocation Receipt And Identity Reconciliation

Extend or compose the existing gateway receipt so requested, assigned,
selected, and actual provider/model identities can be reconciled. Add exact
alias resolution, adapter identity, effort mapping, usage/latency measurement
classes, and blocking mismatch diagnostics.

### T3 - Orchestrator Assignment Seam

Add a bounded orchestrator seam that selects only within the current approval
envelope and emits the task assignment receipt before invocation. No provider
ranking or automatic policy widening is authorized.

### T4 - Negative Conformance And Disposable Proof

Prove missing approval, expired approval, alias ambiguity, capability mismatch,
budget overflow, credential-reference leakage, provider/model mismatch,
unapproved fallback, retry overflow, quota exhaustion, timeout,
authentication failure, and provider/model unavailability using disposable
fixtures and injected adapters only.

### T5 - Operator-Authorized Live Pilot

Only after T0-T4 closure and fresh operator authorization, run one bounded live
pilot using an operator-supplied API key or account subscription. Record
secret-safe approval, assignment, invocation, diagnostic, cost/quota, latency,
and assigned-versus-actual evidence. A live call is not authorized by this
roadmap alone.

## Tranche Release Rules

- Each tranche requires fresh GC-018, source-verified work order, independent
  review, exact changed manifest, and phase-matched autorun gates.
- T1 cannot dispatch until T0 closes and names extension seams.
- T2 cannot dispatch until T1 ratifies approval and assignment identities.
- T3 cannot dispatch until T2 proves exact identity reconciliation.
- T4 cannot dispatch until T1-T3 close with deterministic fixture seams.
- T5 requires explicit fresh operator authorization, available secret-safe
  credential access, live diagnostic compliance, and a release-quality proof
  plan. Operator silence is not authorization.

## Acceptance Criteria

- [x] Roadmap is provider-neutral and does not hardcode a provider preference.
- [x] Existing Model Gateway registry, receipt, credential, fallback, and
  execution owners are reused rather than duplicated.
- [x] API-key and account-subscription access are represented only by
  secret-safe source type and reference.
- [x] Operator approval, task assignment, invocation, and reviewer
  reconciliation are separate linked records.
- [x] Assigned-versus-actual provider/model mismatch fails closed.
- [x] Fallback is bounded by explicit operator approval.
- [x] Timeout, quota, authentication, availability, and mismatch diagnostics
  are required before retry.
- [x] Live proof and implementation remain parked behind later tranche gates.

## Failure Conditions

- a provider, model, or credential mechanism becomes a hardcoded default;
- a raw key, token, cookie, subscription secret, or secret-bearing path enters
  an artifact or receipt;
- orchestration assigns outside an active approval envelope;
- actual provider/model identity is absent, ambiguous, inferred only from the
  command, or mismatched without a blocking result;
- fallback occurs outside the approved set or attempt budget;
- a retry consumes live quota before the prior failure is classified;
- a new registry, bridge, or receipt silo duplicates an existing owner; or
- a tranche claims closure without independent negative proof.

## Verification Strategy

- schema and deterministic-hash fixtures;
- exact canonical identity and alias-resolution fixtures;
- secret-pattern and credential-reference boundary scans;
- approval expiry/revocation and assignment-envelope tests;
- assignment-versus-actual reconciliation tests;
- fallback, retry-budget, quota, timeout, authentication, and availability
  negative tests;
- existing Model Gateway compatibility suites;
- one separately authorized live proof only after all fixture gates pass.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_multi_provider_execution_log.py` |
| literalTokensReviewed | Status; Purpose; Scope / Target / Owner Boundary; Source Verification Block; New Doc-Only Fields; Acceptance Criteria; Public Export Disposition; Next Allowed Move; Claim Boundary |
| gateRunPurpose | confirm provider-neutral roadmap structure and source-backed reuse boundaries as evidence before operator review |
| claimBoundary | checker compliance proves document shape only; it does not prove runtime assignment or provider execution |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | runtime/provider/mcp/readiness claim |
| Chain map route | NOT_APPLICABLE_WITH_REASON: the roadmap is derived from operator requirements and repository-local Model Gateway source, not an imported provider claim |
| Matching local-view guard | N/A with reason: current runtime symbols are verified directly from repository source |
| Owner surface | this roadmap and future source-verified T0 packet |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | the task-specific Claude invocation is bounded evidence of an operational need, not external authority for the proposed contract |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | reviewer and roadmap author |
| Provider or surface | local private provenance workspace |
| Session or invocation | CVF-OPM-AIR roadmap authoring, 2026-07-20 |
| Working directory | repository root |
| Command or tool surface | direct source reads, repository search, apply_patch, governed gates, git evidence |
| Target paths | this roadmap only |
| Allowed scope source | operator instruction and Continuous Projection T2 completion review Next Allowed Move |
| Before status evidence | clean worktree at session-sync HEAD `a183d6a37` |
| After status evidence | one proposed roadmap; no runtime or provider call |
| Diff evidence | exact one-path staged and committed manifest |
| Approval boundary | roadmap authoring only |
| Claim boundary | no GC-018, work order, implementation, credential use, provider call, public mutation, push, or deployment |
| Agent type | reviewer and roadmap author |
| Invocation ID | `cvf-opm-air-roadmap-authoring-2026-07-20` |
| Expected manifest | this roadmap only |
| Actual changed set | this roadmap only |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Current Runtime Freshness Verification

The roadmap directly re-read the current dynamic model registry, gateway
receipt, credential boundary, fallback policy, and provider execution bridge.
It confirms reusable foundation and the missing approval/assignment/actual
identity chain only. No runtime was changed or invoked. Disposition:
DOCUMENTATION_ONLY_WITH_REASON.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is a private proposed control-plane roadmap. It contains no
public-safe implementation or release evidence and authorizes no public-sync
mutation.

## Next Allowed Move

After the Claude subscription session resets, start one fresh T0 R1 no-commit
worker session under the Interim Bounded Invocation Profile. Do not resume the
packet-author or failed-worker context. The caller must stop the complete
process tree at the first budget threshold and must not retry or fallback.
Codex remains reviewer/closer. T1-T5, credentials, provider calls, live proof,
public-sync, push, deployment, and production action remain parked.

## Claim Boundary

This roadmap authorizes only the bounded T0 R1 documentation/source-inspection
worker for a provider-neutral approval, assignment, invocation, and
reconciliation program over existing CVF Model Gateway foundations. It does
not establish a default provider/model, certify account-subscription
integration, implement orchestration or the reusable cost governor, authorize
fallback, store credentials, call a provider, prove production behavior,
mutate public-sync, push, or deploy.
