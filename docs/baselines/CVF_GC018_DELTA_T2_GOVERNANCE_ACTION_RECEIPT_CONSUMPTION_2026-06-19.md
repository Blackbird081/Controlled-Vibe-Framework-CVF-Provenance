# CVF GC-018 - Delta-T2 Governance Action Receipt Consumption

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-19

Owner: Codex

Execution route: SINGLE_AGENT_MULTI_ROLE

Base head: `8c4c95ca`

## Purpose

Authorize one bounded Delta-T2 Local Workspace Runtime tranche after Delta-T1
closed at accepted material commit `156b0610` and closure commit `a196e42f`.

Delta-T2 adds deterministic validation and atomic one-time consumption of an
existing Delta-T1 governance-action preflight receipt. It does not execute the
planned action, launch a shell command, force an agent to use MCP, or intercept
IDE, git, shell, or filesystem activity.

## Decision / Baseline / Proposed Tranche

| Field | Disposition |
| --- | --- |
| Decision | Dispatch one bounded local deterministic Delta-T2 implementation |
| Proposed tranche | Delta-T2 Governance Action Receipt Consumption |
| Base head | `8c4c95ca` |
| Worker / reviewer / closer | Codex across phase-separated roles |
| Route | `SINGLE_AGENT_MULTI_ROLE` |
| Upstream evidence | Delta-T1 closure; `MCP-GW-001`; external knowledge absorption chain map |
| Later tranche | wrapper/CLI/proxy action execution remains separately authorized work |

## Scope / Target / Owner Boundary

Allowed scope:

- add one modular MCP tool named `cvf_consume_governance_action_receipt`;
- read the existing Delta-T1 audit entry through the source-defined
  `getAuditEntries` boundary;
- verify receipt identity, Delta-T1 contract, action class, exact safe action
  binding, normalized target-file binding, ALLOW decision, and bounded age;
- atomically claim a one-time consumption marker in the configured Delta audit
  directory using create-exclusive filesystem semantics;
- store only secret-safe receipt identifiers, timestamps, contract ids, and a
  SHA-256 binding hash in the consumption marker;
- fail closed for missing, ambiguous, stale, mismatched, blocked, escalated,
  replayed, invalid, secret-bearing, or persistence-failed requests;
- add focused deterministic tests, registration, and bounded prompt guidance.

Forbidden scope:

- no shell, process, command, edit, commit, provider, or Model Gateway action;
- no wrapper, launcher, CLI proxy, IDE extension, git hook, filesystem watcher,
  queue, scheduler, daemon, or workspace-state mutation;
- no live provider call, credential use, quota consumption, or public-sync;
- no change to the Delta-T1 receipt contract or Gamma classifier contract;
- no claim of mandatory MCP invocation, action execution, external
  interception, universal governed coding, or readiness.

Risk ceiling: R2 local deterministic runtime implementation. Any actual action
execution or interception requires a later fresh GC-018 and source-verified
work order.

## Source Verification Block

| Claimed item | Verification type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Delta-T1 receipt ids equal persisted audit request ids. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/governance-action-preflight.ts` | lines 234-274 | `receiptId`; `requestId` | `preflightGovernanceAction` | ACCEPT |
| Delta-T1 audit metadata records action class and contract id. | VALUE_SET | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/governance-action-preflight.ts` | lines 211-226 | `metadata` | `GuardRequestContext` construction | ACCEPT |
| Delta-T1 audit timestamp comes from guard-pipeline execution time. | VALUE_SET | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/governance-action-preflight.ts` | lines 229-235 | `timestamp` | `GuardAuditEntry` construction | ACCEPT |
| Delta-T1 action context binds the action class and action description. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/governance-action-preflight.ts` | lines 211-226 | `action` | `GuardRequestContext` construction | ACCEPT |
| Audit entries can be read by request id. | EXISTS | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/persistence/persistence.interface.ts` | lines 24-29 | `getAuditEntries` | `PersistenceAdapter` | ACCEPT |
| JSON persistence filters audit entries by request id. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/persistence/json-file.adapter.ts` | lines 69-83 | `getAuditEntries` | `JsonFileAdapter` | ACCEPT |
| Delta audit storage has one configured directory with a user-local default. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts` | lines 440-456 | `resolveDeltaAuditDir` | MCP server registration | ACCEPT |
| Current prompt requires preflight before EDIT, RUN, or COMMIT but denies execution/interception inference. | LITERAL_INVARIANT | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/prompt/system-prompt.ts` | lines 275-283 | `buildMcpToolsSection` | MCP system prompt | ACCEPT |
| Delta-T1 closure leaves receipt consumption and launcher enforcement for later authorization. | LITERAL_INVARIANT | `docs/reviews/CVF_DELTA_T1_GOVERNANCE_ACTION_PREFLIGHT_RECEIPT_COMPLETION_2026-06-19.md` | `## Risk / Corrective Action`; `## Claim Boundary` | `CLOSED_PASS_BOUNDED` | Delta-T1 completion | ACCEPT |
| Runtime/MCP implementation requires fresh GC-018 and a source-verified work order. | LITERAL_INVARIANT | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | `## Mandatory Chain`; `## Input Type Router` | `Runtime/provider/MCP/readiness claim` | external knowledge absorption chain map | ACCEPT |

## New Delta-T2 Fields

These are new authorized fields, not existing runtime facts.

| New item | Required value or shape | Purpose |
| --- | --- | --- |
| MCP tool id | `cvf_consume_governance_action_receipt` | distinguish receipt consumption from preflight issuance |
| contract version | `cvf.delta.governanceActionReceiptConsumption.v1` | stable local consumption contract |
| receipt TTL config | `CVF_MCP_DELTA_RECEIPT_TTL_SECONDS` with bounded default | prevent stale receipt consumption |
| consumption id | generated local correlation id | correlate one successful consumption |
| binding hash | SHA-256 of canonical receipt/action/target binding | avoid storing raw action or target details in marker |
| one-time marker | create-exclusive file under the Delta audit directory | reject replay without a new shared persistence contract |
| execution proof marker | `actionExecutionProved=false` | prevent receipt consumption from becoming an execution claim |
| interception proof marker | `externalInterceptionProved=false` | preserve the external-runtime boundary |

## Current Runtime Freshness Verification

| Runtime surface | Fresh source checked | Result |
| --- | --- | --- |
| Delta-T1 preflight contract | `src/tools/governance-action-preflight.ts` | persisted request-correlated ALLOW receipt exists |
| Audit read port | `src/persistence/persistence.interface.ts` | request-filtered read exists |
| JSON audit adapter | `src/persistence/json-file.adapter.ts` | local audit readback exists |
| Consumption tool | repository negative search | no `cvf_consume_governance_action_receipt` exists before Delta-T2 |
| Consumption marker | repository negative search | no receipt-consumption marker store exists before Delta-T2 |
| MCP entrypoint | `src/index.ts` | 906 lines at dispatch; new behavior must stay in modular files |

## Delta-T2 Control Block

| Field | Disposition |
| --- | --- |
| Receipt authority | persisted Delta-T1 `GuardAuditEntry` only |
| Valid decision | `ALLOW` only |
| Action binding | exact safe action plus normalized target-file set and action class |
| Freshness | fixed server-side TTL; caller cannot extend it |
| Replay protection | atomic create-exclusive one-time marker |
| Marker data | ids, timestamps, contracts, action class, binding hash only |
| Successful claim | `receiptValid=true`, `receiptConsumed=true`, `executionAdmissionEligible=true` |
| Execution claim | always `actionExecutionProved=false` |
| Interception claim | always `externalInterceptionProved=false` |
| Failure posture | fail closed without an admission-eligible claim |
| Provider boundary | no provider or Model Gateway execution |
| Public boundary | private provenance only |

## Rescan Intelligence Hardening

- Original source artifact: `MCP-GW-001`, Delta-T1 completion, and the external
  knowledge absorption chain map.
- Predecessor intake artifact:
  `docs/reviews/CVF_DELTA_T1_GOVERNANCE_ACTION_PREFLIGHT_RECEIPT_COMPLETION_2026-06-19.md`.
- Delta ledger status: `CHANGED_DISPOSITION` because receipt consumption moves
  from parked post-T1 work to a bounded operator-authorized tranche.
- Routing matrix status: `DO_NOW` for deterministic validation and atomic
  one-time claim; `SEPARATE_RUNTIME_TRANCHE` for action launcher/wrapper/proxy;
  `STRATEGIC_OPERATOR_DECISION` for external interception breadth;
  `OUT_OF_SCOPE` for provider/live, public-sync, and readiness.
- Semantic sampling status: `PARTIAL_TARGETED`, covering action binding, stale
  receipt, replay race, secret-safe marker, and no-execution claim.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE
- Machine guard: `governance/compat/check_rescan_intelligence_hardening.py`

### Original-Intake Delta Ledger

| Item | Delta category | Original disposition | Updated disposition | Rationale |
| --- | --- | --- | --- | --- |
| Durable preflight receipt | `UNCHANGED_FROM_INTAKE` | implemented in Delta-T1 | preserved as sole receipt authority | avoids parallel receipt semantics |
| Receipt consumption | `CHANGED_DISPOSITION` | parked after Delta-T1 | authorized for deterministic T2 | operator selected foundation hardening |
| Replay rejection | `NEW_FINDING` | not implemented in T1 | atomic one-time marker required | consumption without replay protection is not safe admission evidence |
| Action execution | `REMOVED_OR_REJECTED` | possible later enforcement goal | rejected from T2 | T2 proves consumption only |
| Universal interception | `REMOVED_OR_REJECTED` | strategic future option | rejected from T2 | MCP cannot force invocation outside its call path |

### Follow-Up Routing Matrix

| Lane | Applies to | Rationale |
| --- | --- | --- |
| DO_NOW | receipt validation, TTL, binding, atomic marker, tests, prompt | bounded T2 foundation |
| RESOLVED_BY_DESIGN | reuse persisted T1 audit and existing audit-read port | avoids a second receipt authority |
| SEPARATE_RUNTIME_TRANCHE | wrapper/CLI/proxy consumes eligibility and executes action | changes execution ownership and risk |
| STRATEGIC_OPERATOR_DECISION | shell/IDE/git/filesystem interception breadth | changes operator workflow and control reach |
| OUT_OF_SCOPE | provider/live, public-sync, queues, readiness claims | unnecessary for deterministic T2 |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | required verdict |
| --- | --- | --- | --- | --- | --- |
| DELTA-T2-01 | T1 audit context | receipt binds an action | `UNCHANGED_FROM_INTAKE` | Can a receipt admit a different action or targets? | No; exact canonical binding required |
| DELTA-T2-02 | timestamp | receipt is fresh | `CHANGED_DISPOSITION` | Can caller extend TTL? | No; server-owned bounded TTL |
| DELTA-T2-03 | one-time marker | receipt is consumed once | `NEW_FINDING` | Can concurrent callers both succeed? | No; create-exclusive claim permits at most one |
| DELTA-T2-04 | claim boundary | consumption supports later enforcement | `REMOVED_OR_REJECTED` | Does consumption prove action execution? | No; proof markers remain false |
| DELTA-T2-05 | marker contents | consumption evidence is secret-safe | `NEW_FINDING` | Can raw action or target paths leak? | No; marker stores only ids and binding hash |

## Acceptance Criteria

| ID | Criterion | Final state |
| --- | --- | --- |
| AC1 | Distinct Delta-T2 tool is registered without changing Delta-T1 or Gamma contracts. | PASS |
| AC2 | Only one unambiguous persisted Delta-T1 ALLOW receipt can validate. | PASS |
| AC3 | Action class, safe action, target binding, contract, and TTL must match. | PASS |
| AC4 | Successful consumption creates a secret-safe atomic marker before returning eligibility. | PASS |
| AC5 | Replay, stale, mismatch, BLOCK, ESCALATE, missing, ambiguous, and storage failure paths fail closed. | PASS |
| AC6 | Marker and response omit raw action, target paths, and credential-bearing values. | PASS |
| AC7 | Prompt requires consumption after preflight but preserves no-execution/no-interception language. | PASS |
| AC8 | Focused tests, full MCP tests, MCP build, and governance gates pass. | PASS |
| AC9 | No action execution, provider/live, public-sync, queue, workspace-state, or broad interception work occurs. | PASS |

## Evidence / Verification

Required evidence:

- focused Vitest for receipt validation, binding, TTL, replay, concurrent claim,
  persistence failure, and secret-safe marker readback;
- focused system-prompt regression coverage;
- full MCP test suite and TypeScript build;
- `git diff --check`, exact changed-set evidence, reviewer-fast, autorun phase
  gates, and commit-steward preflights;
- no provider/live receipt because provider behavior and action execution are
  outside this tranche.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance Delta runtime tranche. No public-sync authorization.

## Claim Boundary

Delta-T2 may prove only that an invoked local MCP consumer validated and
atomically claimed one matching fresh Delta-T1 receipt. It does not prove that
the planned action executed, that the consumer was mandatory, that a wrapper
enforced the result, or that external coding activity was intercepted.
