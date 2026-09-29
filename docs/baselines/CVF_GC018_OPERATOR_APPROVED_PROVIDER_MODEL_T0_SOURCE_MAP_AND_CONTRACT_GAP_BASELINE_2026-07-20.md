# CVF GC-018 Baseline - Operator-Approved Provider Model T0 Source Map And Contract Gap Baseline

Memory class: governed-dispatch-baseline

Status: REVIEWER_ACCEPTED_DISPATCH_READY_WITH_REPAIRS

Batch ID: OPM-AIR-T0

Dispatch base head: 683543e49

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: Operator

Reviewer owner: reviewer role (operator-assigned current reviewer: Codex)

Worker target: worker role (operator-assigned current worker: Claude)

## Purpose

This baseline is the CVF-OPM-AIR T0 Source Map And Contract Gap Baseline. It
maps every proposed Group A-D field in the operator-approved provider/model
roadmap to an EXISTS, VALUE_SET, LITERAL_INVARIANT, RUNTIME_BEHAVIOR, or
DOC_ONLY_NEW disposition against current Model Gateway, routing, quota,
credential, fallback, receipt, and live-diagnostic owners, blocks duplicate
owner creation, records the operator usage baseline snapshot with its
measurement-class boundary, defines the deduplicated CLI usage measurement
contract, and authorizes exactly three future no-commit worker outputs. T0 is
documentation and direct source-inspection only; it performs no runtime,
checker source, test, provider CLI, credential, public-sync, push, or
deployment mutation. Repository governance gates remain required evidence.

## Scope / Target / Owner Boundary

In scope:

- direct verification of every existing Model Gateway, routing, quota,
  credential, fallback, receipt, and unified-gateway-interface source file
  named by the roadmap plus adjacent owners discovered during verification;
- a field-by-field Contract Gap Reconciliation Matrix for roadmap Groups
  A (Operator Approval Envelope), B (Task Assignment Receipt), C (Invocation
  Receipt), and D (Reviewer Reconciliation Decision);
- the operator usage baseline snapshot, its measurement-class boundary, and
  the deduplicated Claude CLI JSONL measurement contract;
- a bounded future manual comparison contract definition, not its execution;
- authorization of exactly three future `docs/reviews/` no-commit worker
  outputs.

Out of scope:

- any runtime, checker, test, or automation change to
  `EXTENSIONS/CVF_MODEL_GATEWAY/`;
- any credential use, provider call, or live invocation;
- any new registry, execution bridge, credential store, or fallback engine;
- public-sync, push, or deployment;
- the manual comparison itself (contract definition only);
- T1-T5 implementation of the roadmap contract groups.

Owner boundary: this baseline and its paired work order are owned by the
CVF-OPM-AIR roadmap dispatch lane. Implementation of Groups A-D remains
parked behind fresh GC-018 and source-verified work orders for T1-T4 per the
roadmap Tranche Release Rules.

## Reviewer Finding Carry-Forward

| Finding | Reviewer repair | Worker carry-forward |
|---|---|---|
| full pre-dispatch found three missing work-order control blocks after the packet-author CLI was stopped | added Checker Source Read-Ahead, External Knowledge Intake Routing, and Foundation Storage Layout blocks | do not remove or weaken these blocks |
| work order promoted provider-local JSONL shape through a same-packet baseline `ACCEPT` row | replaced with a repository-source claim and marked JSONL as `NOT_CVF_SOURCE` operational evidence only | use JSONL only for secret-safe measurement evidence, never Source Authority |
| worker preflight expected the two packet files to remain untracked and reused stale base `683543e49` | require a clean committed dispatch/session-sync execution base supplied by the reviewer | stop if HEAD differs or the worktree is dirty |
| completion review was optional even though the operator assigned Codex reviewer/closer ownership | fixed an exact completion-review path and four-path closure conversion | return three worker outputs only; reviewer owns closure conversion |
| caller wrapper timed out at 124.6 seconds while Claude child continued and accumulated large usage | record `CALLER_TIMEOUT_CHILD_CONTINUED_REVIEWER_STOPPED` for packet-author session `3788ceeb-8aac-415b-a2c9-6e7dc1b01edf` | measure this exact session without retrying or reading prompt/response content |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id OPM-AIR-T0 --title "Operator-Approved Provider Model T0 Source Map And Contract Gap Baseline" --date 2026-07-20 --base 683543e49 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced scaffold placeholder file names with the operator-directed exact baseline/work-order/worker-return paths; resolved every scaffold placeholder field with source-verified content; added the Contract Gap Reconciliation Matrix, usage-measurement classification, and role-sequence sections that the generic scaffold does not generate |
| checkerReadAheadConfirmation | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_forbidden_filesystem_state.py`; `governance/compat/check_work_order_dispatch_quality_artifacts.py` |
| docOnlyNewFields | every field listed `DOC_ONLY_NEW` in the Contract Gap Reconciliation Matrix below; none are claimed as existing runtime |
| claimBoundary | dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects (16 total, `--max-results 50`, `--json`):

| defectId | One-line avoidance note for this dispatch |
| --- | --- |
| ADIF-0001 | Contract Gap Reconciliation Matrix cites only files this agent directly read in this session; no exhaustive-directory claim is made without listing actual children |
| ADIF-0002 | No provider-specific memory file (NOT_CVF_SOURCE: local agent guidance files, session summaries) is cited as CVF source authority; every claim traces to a CVF-governed file or direct source read |
| ADIF-0014 | Corpus Completeness, Rescan Intelligence, and Mandatory Blind-Spot Control blocks are all included below with explicit `NOT_APPLICABLE_WITH_REASON`, not silence |
| ADIF-0015 | This packet is authored under `dispatch-authoring`, not `pre-implementation`; the Agent Handoff Contract Control Block records `dispatch` as the phase and does not claim executor-shaped self-correction |
| ADIF-0020 | Checker Source Read-Ahead Block below lists the applicable checker source files actually read before this artifact was drafted |
| ADIF-0021 | No applicability-marker string for another guard family (rescan, Delta block, absorption) is used loosely; each conditional section uses the guard's own safe vocabulary |
| ADIF-0028 | The Contract Gap Reconciliation Matrix is per-field, not an aggregated claim wider than the per-field source evidence recorded in the Source Verification Block |
| ADIF-0029 | No durable-evidence projection or admission-record claim is made by this documentation-only baseline |
| ADIF-0033 | No protected path (`governance/compat/*.py`, `CVF_SESSION/**`, `AGENT_HANDOFF*.md`) is listed in scope; no Core Guard Self-Protection Authorization block is required or included |
| ADIF-0007 | Gate-marker vocabulary ("pre-dispatch", "pre-implementation") is used only in its literal phase-gate sense, not as unrelated boundary prose |
| ADIF-0016 | This entry lists a reusable resolver-disclosure pattern already promoted to the ADIF registry itself, not trapped in a one-off checklist |
| ADIF-0017 | Commit-shape planning is deferred to the reviewer/closer per the Reviewer Closure Conversion block; this dispatcher does not probe commit shape |
| ADIF-0024 | The paired worker return will use the `WORKER_RETURN_FULL_GATE_V1` scaffold and rerun the worker-return fast gate before `COMPLETE_PENDING_REVIEW`, per the work order |
| ADIF-0031 | No `REJECT` row is present in the Source Verification Block below; all cited claims resolved `ACCEPT` after direct source reads |
| ADIF-0039 | The paired work order's Verification Commands include the worker-return fast gate and `run_agent_automation_assist.py` terms |
| ADIF-0006 | Every Source Verification `Verified path or symbol` cell below contains a bare symbol or field name, never a value assignment or type annotation |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_artifacts.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_forbidden_filesystem_state.py`; `governance/compat/check_docs_governance_compat.py`; `governance/compat/check_absorption_blindspot_control_presence.py`; `governance/compat/check_rescan_intelligence_hardening.py` |
| literalTokensReviewed | `## Purpose`; `## Scope / Target / Owner Boundary`; `## Claim Boundary`; `## Source`; `## Baseline Decision`; `## Verification`; `Memory class`; `Status`; `## ADIF Defect Registry Disclosure`; `Resolver query: taskClass=` line shape; `ROUTE_TOKENS` (`SINGLE_AGENT_SINGLE_ROLE`, `SINGLE_AGENT_MULTI_ROLE`, `MULTI_AGENT_SINGLE_ROLE`, `MULTI_AGENT_MULTI_ROLE`); the eight Delta block fields (`claimScope`, `claimDisposition`, `receiptEvidence`, `actionEvidence`, `invocationBoundary`, `interceptionBoundary`, `claimLanguage`, `forbiddenExpansion`); `EXPORTED` / `DEFERRED_PRIVATE_ONLY` / `BLOCKED_MISSING_PUBLIC_ARTIFACTS`; the seven `## External Knowledge Intake Routing` row labels |
| gateRunPurpose | confirmation evidence after direct checker-source reading in this session, not first discovery; the dispatch-author fast gate and pre-dispatch autorun gate are run after drafting to verify, not to locate required shape |
| claimBoundary | this block records which checker sources were read and which literal tokens were matched against them; it does not itself prove gate PASS, which is recorded separately in the Verification Commands section |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Provider registry owner exists with allow/block-list selection | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | `ProviderRecord` and `ProviderSelectionOptions` interfaces | `ProviderRecord`; `ProviderSelectionOptions` | provider registry | ACCEPT |
| Provider selection supports allowed/blocked provider id lists | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | `ProviderSelectionOptions` interface | `allowedProviderIds`; `blockedProviderIds` | provider registry | ACCEPT |
| Provider capability registry exists with per-model supported methods | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | exported registry declaration | `PROVIDER_CAPABILITY_REGISTRY` | provider capability registry | ACCEPT |
| Capability owner refs already name retry, cost, and risk as existing owner surfaces | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | `PROVIDER_CAPABILITY_OWNER_REFS` array | `PROVIDER_CAPABILITY_OWNER_REFS` | provider capability registry | ACCEPT |
| Dynamic model record carries tier, cost, latency class, rate limit, health | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/dynamic-model-registry-contract.ts` | `DynamicModelRecord` interface | `DynamicModelRecord` | dynamic model registry contract | ACCEPT |
| Capability-aware candidate query exists with method and allow/block bounds | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/dynamic-model-registry-contract.ts` | `FindOptimalQuery` interface | `requiredMethod`; `allowedProviderIds`; `blockedProviderIds` | dynamic model registry contract | ACCEPT |
| Routing request carries required capabilities and latency budget | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | `RoutingRequest` interface | `requiredCapabilities`; `latencyBudgetMs`; `preferredProviderId`; `requestedModelId` | routing policy engine | ACCEPT |
| Routing decision carries selected provider/model and quota decision | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | `RoutingDecision` type | `RoutingDecision` | routing policy engine | ACCEPT |
| Quota ledger owns numeric per-day request/token ceilings | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/quota-ledger.ts` | `QuotaLimit` interface | `QuotaLimit` | quota ledger | ACCEPT |
| Requested and selected model receipt fields exist | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-receipt.ts` | `GatewayReceiptInput` interface | `requestedModelId`; `selectedModelId` | gateway receipt schema | ACCEPT |
| Selection reason field exists on the receipt input and output | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-receipt.ts` | `GatewayReceiptInput` and `GatewayReceipt` | `reason` | gateway receipt schema | ACCEPT |
| Fallback receipt evidence exists on the receipt input and output | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-receipt.ts` | `GatewayReceiptInput` and `GatewayReceipt` | `fallbackFromProviderId`; `fallbackFromModelId`; `fallback` | gateway receipt schema | ACCEPT |
| Receipt validation state is a three-value not_run/passed/failed field | LITERAL_INVARIANT | `EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-receipt.ts` | `GatewayReceiptInput.validationState` | `validationState` | gateway receipt schema | ACCEPT |
| Receipt metadata redacts key/secret/token/credential-named fields | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-receipt.ts` | `sanitizeReceiptMetadata` function | `sanitizeReceiptMetadata` | gateway receipt schema | ACCEPT |
| Secret-safe credential reference and metadata exist | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/credential-boundary.ts` | `CredentialReference` and `CredentialMetadata` interfaces | `keyId`; `envNames`; `fingerprint`; `redactedValue` | credential boundary | ACCEPT |
| Current credential source is fixed to the literal string env | VALUE_SET | `EXTENSIONS/CVF_MODEL_GATEWAY/src/credential-boundary.ts` | `CredentialMetadata.source` | `source` | credential metadata schema | ACCEPT |
| Fallback attempt budget and retryable status codes exist | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/fallback-policy.ts` | `FallbackPolicyConfig` and `FallbackDecision` interfaces | `maxAttempts`; `retryableStatusCodes`; `remainingAttempts` | fallback policy | ACCEPT |
| Execution response reports actual provider/model identity and usage tokens | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/unified-gateway-interface-contract.ts` | `GatewayExecuteResponse` interface | `model`; `usage` | unified gateway interface contract | ACCEPT |
| Error class enum exists for quota, credential, availability, and admission failures | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/unified-gateway-interface-contract.ts` | `GatewayErrorClass` type | `GatewayErrorClass` | unified gateway interface contract | ACCEPT |
| Execution bridge assembles actual provider/model identity onto the response | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | success response assembly in `execute` | `response.model.providerId`; `response.model.modelId` | provider execution bridge | ACCEPT |
| Quota-exceeded and credential-shielded failures are classified before adapter execution | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | quota and credential guard branches in `execute` | `quota_exceeded`; `credential_shielded` | provider execution bridge | ACCEPT |
| Live-run diagnostic standard defines stage/class/retryable/userAction vocabulary | EXISTS | `docs/reference/archive/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md` | `Required Diagnostic Fields` and `Stable Classes` sections | `stage`; `class`; `retryable`; `userAction` | live run diagnostic standard | ACCEPT |
| Operator-approved provider/model roadmap names the T0 mission and Groups A-D fields | EXISTS | `docs/roadmaps/CVF_OPERATOR_APPROVED_PROVIDER_MODEL_ASSIGNMENT_AND_INVOCATION_RECEIPT_ROADMAP_2026-07-20.md` | `Proposed Contract Groups` sections A-D | `approvalId` through `receiptHash` field list | CVF-OPM-AIR roadmap | ACCEPT |
| Roadmap records the operator usage baseline snapshot | EXISTS | `docs/roadmaps/CVF_OPERATOR_APPROVED_PROVIDER_MODEL_ASSIGNMENT_AND_INVOCATION_RECEIPT_ROADMAP_2026-07-20.md` | `Operator Usage Baseline Snapshot` section | current session; weekly all-models; usage credits; usage-credit spend rows | CVF-OPM-AIR roadmap | ACCEPT |
| Active handoff authorizes the current packet-authoring mode and five-stage sequence | EXISTS | `AGENT_HANDOFF_V49_2026-07-20.md` | `CVF-OPM-AIR T0 Packet Authoring Authorization` section | Operator sequence bullet list | active handoff | ACCEPT |
| Work-order template requires an Operator Checkpoint heading for work_order docType | LITERAL_INVARIANT | `governance/compat/check_markdown_structural_completeness.py` | `SECTION_GROUPS["work_order"]` operator checkpoint row | `Operator Checkpoint` | markdown structural completeness gate | ACCEPT |
| ADIF disclosure gate re-derives expected defect ids from the resolver query line | RUNTIME_BEHAVIOR | `governance/compat/check_adif_defect_registry_disclosure.py` | `_expected_defect_ids` function | `_expected_defect_ids` | ADIF disclosure gate | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Path existence for the GC-018 baseline file | `test -f docs/baselines/CVF_GC018_OPERATOR_APPROVED_PROVIDER_MODEL_T0_SOURCE_MAP_AND_CONTRACT_GAP_BASELINE_2026-07-20.md` returned `NOT_EXISTS` | no collision; file may be created |
| Path existence for the paired work order | `test -f docs/work_orders/CVF_AGENT_WORK_ORDER_OPERATOR_APPROVED_PROVIDER_MODEL_T0_SOURCE_MAP_AND_CONTRACT_GAP_BASELINE_2026-07-20.md` returned `NOT_EXISTS` | no collision; file may be created |
| Path existence for the three planned worker outputs | `test -f` on each of the three `docs/reviews/CVF_OPERATOR_APPROVED_PROVIDER_MODEL_T0_*_2026-07-20.md` paths returned `NOT_EXISTS` for all three | no collision; paths are free for the worker |
| Token search for the batch identity string | search root: `docs`, `CVF_SESSION`, `AGENT_HANDOFF_V49_2026-07-20.md`; exact command: `rg -n --fixed-strings "OPM-AIR-T0" docs CVF_SESSION AGENT_HANDOFF_V49_2026-07-20.md`; result: zero matches | no prior use of the compact batch id; safe to introduce |
| Token search for the roadmap identity string | search root: `docs`, `CVF_SESSION_MEMORY.md`, `AGENT_HANDOFF_V49_2026-07-20.md`; exact command: `rg -n --fixed-strings "CVF-OPM-AIR" docs CVF_SESSION_MEMORY.md AGENT_HANDOFF_V49_2026-07-20.md`; result: five matches, all prior authorization records (roadmap file, active handoff, session memory) | expected authorization trail, not a naming collision |

## Current Runtime Freshness Verification

| Field | Value |
| --- | --- |
| runtimeClaimPresent | YES (Contract Gap Reconciliation Matrix below states which fields are absent from current runtime) |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | DIRECT_SOURCE_READ_THIS_SESSION |
| reason | every EXISTS/VALUE_SET/RUNTIME_BEHAVIOR/LITERAL_INVARIANT row in the Source Verification Block above was confirmed by directly opening the cited file in this session; every DOC_ONLY_NEW row in the Contract Gap Reconciliation Matrix below reflects the absence of a matching field in the same directly read files |
| requiredFutureAction | T1 must re-verify freshness against current HEAD immediately before ratifying the approval/assignment schema, since source may drift between T0 and T1 dispatch |

## Contract Gap Reconciliation Matrix

Disposition legend: `EXISTING_OWNER` (a current field or type directly satisfies
the proposed field), `EXTENSION_SEAM` (a current field or type is the closest
composition point but does not yet carry the full proposed semantics),
`DOC_ONLY_NEW` (no current field, type, or owner surface was found by direct
source read in this session).

### Group A - Operator Approval Envelope

| Field | Disposition | Owner / extension seam | Note |
| --- | --- | --- | --- |
| `approvalId` | DOC_ONLY_NEW | none found | no approval-envelope identity owner exists in the read source set |
| `operatorId` | DOC_ONLY_NEW | none found | no operator-identity field exists in the read source set |
| `approvedProviders` | EXTENSION_SEAM | `provider-registry.ts` `ProviderSelectionOptions.allowedProviderIds`/`blockedProviderIds` | current allow/block lists are per-call options, not a stored, expiring, operator-scoped envelope |
| `approvedModels` | EXTENSION_SEAM | `dynamic-model-registry-contract.ts` `FindOptimalQuery.allowedProviderIds`/`blockedProviderIds` | current bounds are provider-scoped in the read query shape; no per-model allow-list field was found |
| `requiredCapabilities` | EXTENSION_SEAM | `routing-policy.ts` `RoutingRequest.requiredCapabilities`; `dynamic-model-registry-contract.ts` `FindOptimalQuery.requiredMethod` | capability shape exists; envelope-level requirement binding is new |
| `credentialSourceType` | EXTENSION_SEAM | `credential-boundary.ts` `CredentialMetadata.source` | currently `VALUE_SET` to the literal string `env` only; an account-subscription class would be a new literal value on the same field |
| `credentialReference` | EXISTING_OWNER | `credential-boundary.ts` `CredentialReference` | `providerId`, `keyId`, `envNames` already match the proposed secret-safe locator shape |
| `costQuotaCeiling` | EXISTING_OWNER | `quota-ledger.ts` `QuotaLimit` | `requestsPerDay`, `estimatedTokensPerDay`, `actualTokensPerDay` already match the proposed cost/quota ceiling shape |
| `latencyCeilingMs` | EXTENSION_SEAM | `routing-policy.ts` `RoutingRequest.latencyBudgetMs` | existing field is per-call, not a stored operator-approved ceiling |
| `fallbackPolicy` | EXISTING_OWNER | `fallback-policy.ts` `FallbackPolicyConfig`/`FallbackDecision` | attempt budget and retryable-status bounds already exist |
| `validFrom` | DOC_ONLY_NEW | none found | no approval time-window field exists in the read source set |
| `expiresAt` | DOC_ONLY_NEW | none found | no approval time-window field exists in the read source set |
| `reapprovalTriggers` | DOC_ONLY_NEW | none found | no reapproval-trigger field exists in the read source set |
| `approvalHash` | DOC_ONLY_NEW | none found | no deterministic approval-content hash field exists in the read source set |

### Group B - Task Assignment Receipt

| Field | Disposition | Owner / extension seam | Note |
| --- | --- | --- | --- |
| `assignmentId` | DOC_ONLY_NEW | none found | no task-assignment identity owner exists |
| `taskId` | DOC_ONLY_NEW | none found | no governed-task identity field exists on the gateway receipt schema |
| `approvalId` (chain reference) | DOC_ONLY_NEW | none found | depends on the new Group A `approvalId`, itself `DOC_ONLY_NEW` |
| `assignedProviderId` | EXTENSION_SEAM | `gateway-receipt.ts` `GatewayReceiptInput.providerId`; `routing-policy.ts` `RoutingRequest.preferredProviderId` | field name differs (`providerId`/`preferredProviderId` versus `assignedProviderId`); semantics are close |
| `assignedModelId` | EXTENSION_SEAM | `gateway-receipt.ts` `GatewayReceiptInput.requestedModelId`; `routing-policy.ts` `RoutingRequest.requestedModelId` | same as above; naming differs, no separate assignment-versus-request distinction exists yet |
| `assignedEffort` | DOC_ONLY_NEW | none found | no effort/reasoning-class field exists in any read schema |
| `requiredCapabilities` | EXTENSION_SEAM | same as Group A `requiredCapabilities` | reused capability shape |
| `selectionReason` | EXISTING_OWNER | `gateway-receipt.ts` `GatewayReceiptInput.reason`/`GatewayReceipt.reason` | direct match |
| `inputHash` | DOC_ONLY_NEW | none found | no deterministic task-input hash field exists |
| `fallbackPermission` | EXTENSION_SEAM | `fallback-policy.ts` `FallbackPolicyConfig.retryableStatusCodes` | bounds automatic same-provider retry; an explicit approved cross-provider fallback set is new |
| `assignedBy` | DOC_ONLY_NEW | none found | no assigner-identity field exists |
| `assignedAt` | EXTENSION_SEAM | `gateway-receipt.ts` `GatewayReceipt.createdAt` | existing ISO-timestamp convention on the receipt, not yet on an assignment record |

### Group C - Invocation Receipt

| Field | Disposition | Owner / extension seam | Note |
| --- | --- | --- | --- |
| `invocationId` | EXTENSION_SEAM | `gateway-receipt.ts` `GatewayReceipt.receiptId` generation pattern | existing `gw_<timestamp>_<nonce>` id pattern is the closest generator |
| `assignmentId` (chain reference) | DOC_ONLY_NEW | none found | depends on the new Group B `assignmentId` |
| `approvalId` (chain reference) | DOC_ONLY_NEW | none found | depends on the new Group A `approvalId` |
| `adapterId` | DOC_ONLY_NEW | `provider-execution-bridge.ts` `ProviderExecutionAdapter.providerId` | adapter has a provider id but no separate adapter identity field |
| `adapterVersion` | DOC_ONLY_NEW | none found | no adapter-version field exists |
| `requestedProviderId` | EXTENSION_SEAM | `routing-policy.ts` `RoutingRequest.preferredProviderId` | field name differs |
| `requestedModelId` | EXISTING_OWNER | `gateway-receipt.ts` `GatewayReceiptInput.requestedModelId`; `routing-policy.ts` `RoutingRequest.requestedModelId` | direct match |
| `actualProviderId` | EXISTING_OWNER | `unified-gateway-interface-contract.ts` `GatewayExecuteResponse.model.providerId` | direct match, populated by `provider-execution-bridge.ts` `execute` |
| `actualModelId` | EXISTING_OWNER | `unified-gateway-interface-contract.ts` `GatewayExecuteResponse.model.modelId` | direct match, populated by `provider-execution-bridge.ts` `execute` |
| `actualEffort` | DOC_ONLY_NEW | none found | no effort/reasoning-class field exists |
| `credentialSourceType` | EXTENSION_SEAM | same as Group A `credentialSourceType` | reused |
| `credentialReference` | EXISTING_OWNER | `gateway-receipt.ts` `GatewayReceipt.credentialKeyId`/`credentialFingerprint` | secret-safe fields already exist, distinct from the raw `CredentialReference` used at request time |
| `fallbackUsed` | EXISTING_OWNER | `gateway-receipt.ts` `GatewayReceipt.fallback` | presence of the `fallback` object already signals fallback use |
| `fallbackFrom` | EXISTING_OWNER | `gateway-receipt.ts` `GatewayReceiptInput.fallbackFromProviderId`/`fallbackFromModelId` | direct match |
| `usageMeasurement` | EXTENSION_SEAM | `unified-gateway-interface-contract.ts` `GatewayExecuteResponse.usage` | `inputTokens`/`outputTokens` exist; no cost field and no CLI-JSONL dedup class exists |
| `latencyMeasurement` | DOC_ONLY_NEW | none found | no latency-measurement field was found on the receipt or response schemas read |
| `diagnosticClass` | EXTENSION_SEAM | `unified-gateway-interface-contract.ts` `GatewayErrorClass`; `docs/reference/archive/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md` stable classes | the gateway error enum and the live-diagnostic class vocabulary both exist but are not yet composed into one invocation-receipt field |
| `reconciliationResult` | DOC_ONLY_NEW | none found | no exact-match/approved-fallback/blocking-mismatch tri-state field exists |
| `receiptHash` | DOC_ONLY_NEW | none found | no deterministic secret-safe receipt-content hash field exists |

### Group D - Reviewer Reconciliation Decision

Group D is a reviewer procedure, not a schema field group. The closest
existing owner is `gateway-receipt.ts` `GatewayReceipt.validationState`
(`not_run` / `passed` / `failed`), which is `EXISTING_OWNER` for the
tri-state pass/fail concept but `DOC_ONLY_NEW` for the specific
approval-assignment-invocation join, capability/budget check, and
mismatch-blocks-acceptance procedure the roadmap describes.

## Baseline Decision

No duplicate provider registry, provider capability registry, dynamic model
registry, gateway receipt, credential boundary, fallback policy, routing
policy engine, quota ledger, or provider execution bridge owner is proposed or
created by this baseline. Every `EXISTING_OWNER` and `EXTENSION_SEAM` row in
the Contract Gap Reconciliation Matrix composes an already-verified file under
`EXTENSIONS/CVF_MODEL_GATEWAY/src/`. Every `DOC_ONLY_NEW` row is a proposed
field with no current runtime symbol; it must not be presented as existing
runtime in any later T1-T4 packet.

T1 (Approval And Assignment Contract) may proceed to schema ratification only
for the Group A and Group B fields listed above, using the `EXISTING_OWNER`
and `EXTENSION_SEAM` rows as composition points and the `DOC_ONLY_NEW` rows as
new schema to design. T2 (Invocation Receipt And Identity Reconciliation) has
a stronger existing-owner base than A/B: `actualProviderId`, `actualModelId`,
and `requestedModelId` are already `EXISTING_OWNER`. T2 must still add
`latencyMeasurement`, `reconciliationResult`, `receiptHash`, `assignmentId`,
and `approvalId` as new fields.

## Operator Usage Baseline Snapshot And Measurement Classification

| UI measure | Observed value | Evidence boundary |
| --- | ---: | --- |
| current session | 21 percent used; reset shown in 4 hours 13 minutes | operator-provided UI snapshot; not an API quota receipt |
| weekly all-models | 41 percent used; reset shown Tuesday 10:00 PM | operator-provided UI snapshot; plan limits were shown as temporarily boosted |
| usage credits | off | no paid overage authorization |
| usage-credit spend | USD 0.00; reset shown August 1 | UI snapshot only |

This snapshot is classified `OPERATOR_UI_SNAPSHOT`, not
`API_BILLED_USAGE_EXACT` and not `CLI_USAGE_EXACT_ACCOUNT_QUOTA_UNKNOWN`. It
must never be silently converted into a token count, a dollar cost, or a
subscription-quota fraction. It may only be paired alongside, not merged
into, a deduplicated Claude CLI JSONL measurement (below).

## Deduplicated Claude CLI JSONL Measurement Requirement

Claude JSONL is provider-local operational evidence and `NOT_CVF_SOURCE`. It
must not appear in Source Authority or Source Verification `ACCEPT` rows.
T0 measures exact session basenames
`fe820583-4b33-480e-b9d3-14451324dc23.jsonl` (T2 repair) and
`3788ceeb-8aac-415b-a2c9-6e7dc1b01edf.jsonl` (T0 packet author). The latter
must carry diagnostic
`CALLER_TIMEOUT_CHILD_CONTINUED_REVIEWER_STOPPED`: the caller timed out at
124.6 seconds, the child continued, no duplicate retry was launched, and the
reviewer later stopped the exact Claude/MCP process pair under the cost guard.

T0 R1 also measures
`62571339-7d3f-4865-9141-7e59dd67776b.jsonl`, the first T0 worker attempt that
ended with `SUBSCRIPTION_SESSION_LIMIT` before producing an artifact. The
worker must preserve this session as a separate failed-attempt row rather than
adding it to either earlier session or treating the three sessions as one
invocation.

A future usage-measurement worker output must deduplicate by unique
`message.id` before reporting any total. For each unique `message.id`, record:

- `input_tokens`;
- `cache_creation_input_tokens`;
- `cache_read_input_tokens`;
- `output_tokens`;
- a unique-API-response count (distinct `message.id` count, not raw JSONL line
  count, since one API response can appear in multiple JSONL lines);
- elapsed measurement (wall-clock span between first and last timestamp in the
  bounded session window);
- model identity as recorded in the JSONL entry;
- safe absence/presence of any cost field in the JSONL entry, without
  inferring a dollar amount when the field is absent.

## Interim Bounded Invocation Profile

The first worker attempt proved that a caller command is not a provider-call
cardinality boundary. Any R1 invocation is permitted only when the caller
enforces all of these caps:

| Control | Required value |
|---|---|
| session posture | new session; no resume of packet-author or failed-worker context |
| customization posture | Claude `--safe-mode`; no MCP, plugin, browser, subagent, TaskCreate, TaskUpdate, or ToolSearch surface |
| built-in tool allowlist | `Read`, `Write`, `Edit`, `Bash` |
| wall-clock ceiling | 10 minutes |
| unique-response ceiling | 24 deduplicated `message.id` values |
| cumulative cache-read ceiling | 3000000 tokens |
| cumulative output ceiling | 40000 tokens |
| gate/repair ceiling | one focused gate pass and one allowed-scope repair pass |
| threshold action | terminate the complete invocation process tree; emit `INVOCATION_BUDGET_EXCEEDED`; do not retry |
| provider/model posture | exact operator assignment retained; fallback forbidden without fresh approval |

These are temporary caller controls, not a runtime implementation or a
provider-specific default. T1 owns provider-neutral schema ratification and a
later implementation tranche owns a reusable monitored launcher.

## Measurement Classes

| Class | Meaning |
| --- | --- |
| `CLI_USAGE_EXACT_ACCOUNT_QUOTA_UNKNOWN` | exact deduplicated token counts read directly from local CLI JSONL; the account-level subscription quota consumed by those tokens is not derivable from the JSONL alone |
| `API_BILLED_USAGE_EXACT` | exact billed usage from a provider billing/usage API response |
| `SUBSCRIPTION_LIMIT_EVENT_ONLY` | an operator-visible UI percent-used or reset-time event, with no token or dollar figure attached |
| `ESTIMATED_FROM_TEXT` | a value derived by estimation from prose, screenshots, or unverified operator recollection, not from a JSONL or API record |
| `NOT_AVAILABLE_WITH_REASON` | the measurement could not be obtained, with the blocking reason stated |

A future worker output must never convert a `SUBSCRIPTION_LIMIT_EVENT_ONLY`
percentage, a `CLI_USAGE_EXACT_ACCOUNT_QUOTA_UNKNOWN` token count, an
`API_BILLED_USAGE_EXACT` cost, or a subscription quota fraction into one
another without a source-backed conversion rule that is itself evidenced by a
provider-published rate table or an operator-confirmed account statement.

## Manual Comparison Contract (Future Use Only, Not Performed In T0)

A future manual copy/paste comparison contract must record, per compared run:

- operator active time (wall-clock time the operator spent directing the run);
- elapsed time (wall-clock span from dispatch to accepted closure);
- turns (number of operator/agent exchange turns);
- repair rounds (number of reviewer-requested correction cycles);
- accepted outcome (`ACCEPTED`, `ACCEPTED_WITH_REPAIRS`, `REJECTED`, or
  `BLOCKED_WITH_REASON`);
- token evidence class (one of the five Measurement Classes above, or
  `NOT_AVAILABLE_WITH_REASON`).

T0 defines this contract only. T0 does not populate it, does not run the
comparison, and does not compare providers, models, or agents against each
other.

## Role Sequence

1. Codex authors and owns the CVF-OPM-AIR roadmap.
2. Claude, acting as dispatch author, authors this GC-018 baseline and the
   paired work order, then returns `COMPLETE_PENDING_REVIEW` without commit.
3. Codex, acting as reviewer, independently reviews and repairs the packet,
   then commits the accepted dispatch.
4. Claude, acting as worker under `WORKER_MUST_NOT_COMMIT`, executes the
   accepted work order and returns the three required outputs uncommitted.
5. Codex, acting as reviewer/closer, reviews, repairs if necessary, closes,
   and reports tranche findings and learning candidates to the operator.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | runtime/provider/mcp/readiness claim |
| Chain map route | NOT_APPLICABLE_WITH_REASON: this baseline is derived from direct repository source reads and the operator-approved roadmap, not an imported external-provider claim |
| Matching local-view guard | N/A with reason: current runtime symbols were verified directly from repository source in this session |
| Owner surface | this baseline and the paired work order |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | the operator usage snapshot and the task-specific prior Claude invocation are bounded evidence of an operational need, not external authority for the proposed contract fields |

## Corpus Completeness And Report Integrity

- Corpus task class: OTHER
- Corpus root: N/A with reason: this baseline verifies a bounded named list of source files cited by the roadmap Authority table, not a folder, archive, or corpus tree
- Corpus verdict: NOT_APPLICABLE_WITH_REASON - this baseline verifies a bounded named list of source files, not a folder or archive tree

## Rescan Intelligence Hardening

- Original source artifact: N/A with reason: this baseline is not derived from a prior scan, intake, or replayed finding set
- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

## Mandatory Blind-Spot Control Block

- Standard read: `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md`
- Applicability: NOT_APPLICABLE_WITH_REASON. This baseline does not absorb,
  reopen, scope, or implement knowledge from a legacy source folder,
  archived absorption packets, external capability sources, Review-CVF pain
  points, memory, graph, workflow, CLI/MCP/tool, provider, benchmark,
  context, or non-coder outcome surfaces. It composes current
  `EXTENSIONS/CVF_MODEL_GATEWAY/` source that this agent read directly in
  this session, plus the operator-approved roadmap.
- Blind-spot verdict: NOT_APPLICABLE_WITH_REASON

## External Repository Absorption Entry Control

NOT_APPLICABLE_WITH_REASON: this baseline cites no dot-private-reference
legacy folder, external-clone folder, or source-mirror folder path, and uses
no explicit external-repository or copied-folder intake language. Its only
sources are current `EXTENSIONS/CVF_MODEL_GATEWAY/src/` files read directly
in this session and the operator-approved CVF-OPM-AIR roadmap.

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: the roadmap's Group A-D fields would split
roughly evenly between fields that already exist on current Model Gateway
owners and fields that are genuinely new control-plane concepts (approval
envelope identity, task assignment identity, and reconciliation result),
because the roadmap explicitly composes existing owners for provider
selection, credentials, and fallback while proposing a new approval/assignment
layer on top of them.

Evidence Comparison: direct reads of ten `EXTENSIONS/CVF_MODEL_GATEWAY/src/`
files plus the archived live-run diagnostic standard confirmed the prediction.
Of 45 named Group A-D fields, 13 resolved `EXISTING_OWNER`, 14 resolved
`EXTENSION_SEAM`, and 18 resolved `DOC_ONLY_NEW`. The strongest existing-owner
concentration is in Group C (`actualProviderId`, `actualModelId`,
`requestedModelId`, `credentialReference`, `fallbackUsed`, `fallbackFrom`),
matching the prediction that invocation-time identity and fallback evidence
already exist on the gateway receipt and unified gateway interface contract.

Contradiction Or Gap Disposition: one partial contradiction was found.
`costQuotaCeiling` and `fallbackPolicy` resolved `EXISTING_OWNER` rather than
the predicted even split toward `EXTENSION_SEAM`, because `quota-ledger.ts`
and `fallback-policy.ts` already carry a closer structural match than
expected before this session's direct reads. This narrows, rather than
invalidates, the original prediction.

Claim Update: prediction CONFIRMED_BOUNDED. The roadmap composes more
existing Model Gateway structure than a first read of the roadmap text alone
would suggest, and the new-field count (18 of 45) is real and must not be
minimized in T1-T4 dispatch.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | roadmap-author role transitions to reviewer role, then to reviewer/closer role; dispatch-author role transitions to worker role under `WORKER_MUST_NOT_COMMIT` only after the reviewer role accepts the dispatch |
| phase | dispatch |
| baseHeadFor(phase) | dispatchBaseHead=683543e49; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | this baseline and the paired work order only; no other path is touched by this dispatch-authoring phase |
| traceScope(phase, actor) | this dispatch-authoring session's Agent Operation Trace Block below covers only the two authored files |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer/closer owns the material commit after acceptance |
| crossBatchIsolation | this batch does not touch Continuous Projection, MAO, SOT3, or any other active lane; only the CVF-OPM-AIR roadmap and this T0 packet |
| nextMoveSurfaces | `CVF_SESSION_MEMORY.md`, `CVF_SESSION/ACTIVE_SESSION_STATE.json`, and `AGENT_HANDOFF_V49_2026-07-20.md` remain unchanged by this dispatch-authoring turn; the reviewer/closer updates them after accepted commit |

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 683543e49 --head HEAD
python governance/compat/run_dispatch_packet_author_fast_gate.py --base 683543e49 --head HEAD
python governance/compat/check_adif_defect_registry_disclosure.py --base 683543e49 --head HEAD --enforce
python governance/compat/check_governed_file_size.py --enforce
```

Results are recorded in the paired work order's Verification Commands
section and in the `COMPLETE_PENDING_REVIEW` return for this dispatch-authoring
turn, since both this baseline and the work order are validated together as
one uncommitted changed set.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is a private dispatch baseline for an unreleased provider-neutral
control-plane roadmap. It contains no public-safe implementation or release
evidence and authorizes no public-sync mutation.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatch author (operator-assigned current actor: Claude) |
| Provider or surface | local private provenance workspace |
| Session or invocation | CVF-OPM-AIR T0 packet authoring, 2026-07-20 |
| Working directory | repository root |
| Command or tool surface | direct source reads, repository search, governed file writes, governance gates |
| Target paths | this baseline; the paired work order |
| Allowed scope source | `AGENT_HANDOFF_V49_2026-07-20.md` `CVF-OPM-AIR T0 Packet Authoring Authorization` section; operator dispatch instruction naming the two exact output paths |
| Before status evidence | clean worktree at `683543e49`, confirmed by `git status --short` before any file was created |
| After status evidence | two new untracked governed files; no other path changed |
| Diff evidence | `git status --short` showing exactly two untracked paths under `docs/baselines/` and `docs/work_orders/` |
| Approval boundary | dispatch-authoring only; no implementation, credential use, provider call, or commit |
| Claim boundary | repo-local trace only; no runtime, provider, live, public-sync, push, or production claim |
| Agent type | dispatch author |
| Invocation ID | `cvf-opm-air-t0-packet-authoring-2026-07-20` |
| Expected manifest | this baseline; the paired work order |
| Actual changed set | this baseline; the paired work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename in this batch |

## Claim Boundary

This baseline authorizes only T0 documentation and direct source-inspection
work for the CVF-OPM-AIR roadmap: the Contract Gap Reconciliation Matrix, the
usage-measurement classification and CLI JSONL contract, the manual-comparison
contract definition, and authorization of exactly three future
`docs/reviews/` no-commit worker outputs named in the paired work order. It
does not implement any Group A-D field, use a credential, call a provider,
run live proof, mutate public-sync, push, deploy, or claim production
readiness. It is a dispatch packet draft pending Codex reviewer acceptance and
does not itself claim implementation authorization or closure.
