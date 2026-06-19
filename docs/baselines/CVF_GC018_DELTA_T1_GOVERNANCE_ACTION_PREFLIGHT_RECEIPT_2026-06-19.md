# CVF GC-018 - Delta-T1 Governance Action Preflight Receipt

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-06-19

Owner: Codex Orchestrator

Worker target: Claude

Commit mode: WORKER_MUST_NOT_COMMIT

Base head: `087f7678`

## Purpose

Authorize one bounded Delta Execution Control tranche after the MCP to Model
Gateway Composition Proof closed at material commit `befad4a9`.

Delta-T1 adds a durable, secret-safe governance preflight receipt for planned
`EDIT`, `RUN`, and `COMMIT` actions. It does not claim that MCP can force an
agent to call the tool or intercept operating-system, IDE, shell, or filesystem
actions outside the MCP call path.

## Decision / Baseline / Proposed Tranche

| Field | Disposition |
| --- | --- |
| Decision | Dispatch one bounded local deterministic Delta-T1 implementation |
| Proposed tranche | Delta-T1 Governance Action Preflight Receipt |
| Base head | `087f7678` |
| Worker | Claude |
| Reviewer / closer | Codex |
| Commit route | `WORKER_MUST_NOT_COMMIT` |
| Upstream evidence | `MCP-GW-001`; external knowledge absorption chain map; Composition Proof closure |
| Later tranche | wrapper/CLI/proxy receipt enforcement remains separately authorized work |

## Scope / Target / Owner Boundary

Allowed scope:

- add one modular MCP tool named `cvf_preflight_governance_action`;
- evaluate a source-verified `GuardRequestContext` with the existing
  `GuardRuntimeEngine`;
- persist a secret-safe `GuardAuditEntry` through the existing
  `PersistenceAdapter` / `JsonFileAdapter` boundary;
- return a correlation receipt only after durable persistence succeeds;
- fail closed when input is invalid, credential-bearing content is detected,
  guard evaluation blocks or escalates, or persistence fails;
- add focused deterministic tests and update MCP system-prompt guidance;
- produce a worker-return packet without committing.

Forbidden scope:

- no live provider call, API key use, or quota consumption;
- no Model Gateway source mutation or provider execution change;
- no public-sync;
- no runtime queue, scheduler, daemon, or workspace state mutation;
- no wrapper, CLI proxy, shell interception, IDE interception, git hook, or
  filesystem interception;
- no change to the existing Gamma `cvf_check_governance_action` contract;
- no claim that Claude, Codex, an IDE, or every coding action is governed;
- no production, release, hosted, public, or external-facing readiness claim.

Risk ceiling: R2 local deterministic runtime implementation. Network, secret,
public, destructive, and irreversible actions remain forbidden.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| Gamma already exposes an advisory action classifier under `cvf_check_governance_action`. | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts` | lines 512-526 | `cvf_check_governance_action` | MCP server registration | ACCEPT |
| Gamma action classification currently accepts only action text and returns rule/artifact guidance. | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/startup/startup-state.ts` | lines 39-46, 193-243 | `GovernanceCheckReadout`; `checkGovernanceAction` | startup-state Gamma helper | ACCEPT |
| The existing full pipeline evaluates a `GuardRequestContext`. | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/guards/engine.ts` | lines 55-113 | `evaluate` | `GuardRuntimeEngine` | ACCEPT |
| Guard context already defines phase, risk, role, action, agent, files, mutation, scope, trace, and metadata fields. | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/guards/types.ts` | lines 27-40 | `GuardRequestContext` | guard types | ACCEPT |
| Guard pipeline decisions are `ALLOW`, `BLOCK`, or `ESCALATE`. | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/guards/types.ts` | lines 12, 51-60 | `GuardDecision`; `GuardPipelineResult` | guard types | ACCEPT |
| Durable audit input already has a source-defined `GuardAuditEntry` shape. | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/guards/types.ts` | lines 62-67 | `GuardAuditEntry` | guard types | ACCEPT |
| Persistence exposes save and request-filtered read methods for guard audit entries. | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/persistence/persistence.interface.ts` | lines 17-29 | `saveAuditEntry`; `getAuditEntries` | `PersistenceAdapter` | ACCEPT |
| JSON persistence writes audit entries to `audit-log.json`. | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/persistence/json-file.adapter.ts` | lines 31-44, 62-67 | `JsonFileAdapter`; `saveAuditEntry` | JSON persistence adapter | ACCEPT |
| Existing MCP tool-call audit is in-process only and records argument keys rather than durable guard receipts. | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/mcp-tool-audit.ts` | lines 4-6, 26-49 | `auditEntries`; `recordMcpToolCall` | Gamma MCP tool audit | ACCEPT |
| MCP system prompt currently instructs agents to use `cvf_evaluate_full` before file modification. | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/prompt/system-prompt.ts` | lines 52-60, 263-281 | `MCP_TOOL_DESCRIPTIONS`; `buildMcpToolsSection` | MCP system prompt | ACCEPT |
| Legacy coverage requires pre-action governance, durable audit/receipt, and no governed-coding claim without a CVF receipt. | `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` | row `MCP-GW-001` | `MCP-GW-001` | legacy absorption coverage index | ACCEPT |
| Composition Proof closed deterministic MCP-to-Model-Gateway composition and left durable audit/wrapper/proxy enforcement for Delta. | `docs/reviews/CVF_MCP_MODEL_GATEWAY_COMPOSITION_PROOF_COMPLETION_2026-06-19.md` | `## Claim Boundary` | `CLOSED_PASS_BOUNDED` | Composition Proof completion | ACCEPT |
| Runtime and MCP implementation requires fresh GC-018 and a source-verified work order. | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | `## Mandatory Chain`; `## Input Type Router` | `Runtime/provider/MCP/readiness claim` | external knowledge absorption chain map | ACCEPT |

## New Delta-T1 Fields

These are explicitly new fields authorized by this GC-018. They are not
presented as existing runtime facts.

| New item | Required value or shape | Purpose |
| --- | --- | --- |
| MCP tool id | `cvf_preflight_governance_action` | distinguish Delta preflight from Gamma advisory classification |
| contract version | `cvf.delta.governanceActionPreflight.v1` | stable local receipt version |
| action type | `EDIT`, `RUN`, or `COMMIT` | bind the receipt to the planned action class |
| audit directory config | `CVF_MCP_DELTA_AUDIT_DIR` with a user-local default outside the repo | configure durable local JSON storage without repository mutation |
| receipt correlation | `receiptId` equal to persisted audit `requestId` | allow retrieval and evidence correlation |
| persistence marker | `auditPersisted` | distinguish durable success from fail-closed diagnostic response |
| claim marker | `governedActionClaimAllowed` | true only for `ALLOW` plus successful durable persistence |
| receipt claim boundary | preflight decision only; action execution is not proved | prevent universal enforcement claims |

## Current Runtime Freshness Verification

| Runtime surface | Fresh source checked | Result |
| --- | --- | --- |
| Gamma advisory classifier | `startup/startup-state.ts`; `index.ts` | exists and remains unchanged by Delta-T1 |
| Guard pipeline | `guards/engine.ts`; `guards/types.ts`; `guards/index.ts` | deterministic six-guard pipeline exists |
| Durable audit port | `persistence/persistence.interface.ts` | source-defined save/read contract exists |
| JSON audit adapter | `persistence/json-file.adapter.ts` | durable local JSON implementation exists |
| Prompt workflow guidance | `prompt/system-prompt.ts` | current edit guidance uses `cvf_evaluate_full` and needs bounded Delta-T1 update |
| MCP entrypoint size | `src/index.ts` | 881 lines at dispatch; below 1000-line hard threshold, with new behavior required in a separate module |

## Delta-T1 Control Block

| Field | Disposition |
| --- | --- |
| Existing Gamma tool | preserve `cvf_check_governance_action` unchanged as advisory classification |
| New Delta tool | `cvf_preflight_governance_action` |
| Guard authority | existing `GuardRuntimeEngine.evaluate` |
| Durable audit authority | existing `PersistenceAdapter.saveAuditEntry` and `JsonFileAdapter` |
| Allowed action classes | `EDIT`, `RUN`, `COMMIT` |
| Receipt issuance | only after audit persistence succeeds |
| Block/escalate behavior | return decision and persisted receipt; `governedActionClaimAllowed=false` |
| Persistence failure | fail closed; no valid governed-action receipt |
| Credential boundary | raw secret-bearing action text must not be returned or persisted |
| Workflow guidance | require Delta preflight before edit/run/commit when MCP tool is available |
| Enforcement boundary | MCP and prompt guidance cannot force external agents or intercept non-MCP actions |
| Provider boundary | no Model Gateway or live-provider execution |
| Public boundary | private provenance only |

## Rescan Intelligence Hardening

- Original source artifact: `MCP-GW-001` legacy coverage row, external
  knowledge absorption chain map, and external-agent assessment routed through
  the governed legacy recheck.
- Predecessor intake artifact:
  `docs/reviews/CVF_MCP_GATEWAY_EXECUTION_CONTROL_LEGACY_RECHECK_COMPLETION_2026-06-19.md`;
  `docs/reviews/CVF_MCP_MODEL_GATEWAY_COMPOSITION_PROOF_COMPLETION_2026-06-19.md`.
- Delta ledger status: `CHANGED_DISPOSITION` because durable preflight moves
  from parked post-composition work to a bounded implementation dispatch.
- Routing matrix status: `DO_NOW` for preflight/durable receipt;
  `SEPARATE_RUNTIME_TRANCHE` for wrapper/CLI/proxy receipt enforcement;
  `STRATEGIC_OPERATOR_DECISION` for interception breadth; `OUT_OF_SCOPE` for
  provider/live and public-sync.
- Semantic sampling status: `PARTIAL_TARGETED`, covering Gamma collision,
  persistence ordering, claim boundary, and secret-safe JSON readback.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE
- Machine guard: `governance/compat/check_rescan_intelligence_hardening.py`

### Original-Intake Delta Ledger

| Item | Delta category | Original disposition | Updated disposition | Rationale |
| --- | --- | --- | --- | --- |
| Pre-action governance requirement | `UNCHANGED_FROM_INTAKE` | Delta must add preflight before governed action claims | preserved | Delta-T1 implements the first bounded component |
| Durable audit/receipt | `CHANGED_DISPOSITION` | parked until Composition Proof | dispatched for local deterministic implementation | prerequisite is closed at `befad4a9` |
| Gamma tool name collision | `NEW_FINDING` | external assessment phrased the checker as absent | preserve existing Gamma and add distinct Delta tool | current source proves Gamma already owns the name |
| Universal interception claim | `REMOVED_OR_REJECTED` | possible future execution-control goal | rejected from Delta-T1 | MCP cannot force invocation outside its call path |
| Guard and persistence owner reuse | `UNCHANGED_FROM_INTAKE` | CVF owners remain authoritative | reuse existing engine and adapter | avoids parallel semantics |

### Follow-Up Routing Matrix

| Lane | Applies to | Rationale |
| --- | --- | --- |
| DO_NOW | Delta preflight tool, durable receipt, prompt guidance, tests | bounded prerequisite for later enforcement |
| RESOLVED_BY_DESIGN | reuse guard engine and persistence adapter | avoids parallel control semantics |
| SEPARATE_RUNTIME_TRANCHE | wrapper/CLI/proxy receipt consumption and no-receipt blocking | requires wider execution ownership and explicit authorization |
| STRATEGIC_OPERATOR_DECISION | IDE/shell/filesystem interception breadth | changes control reach and operator workflow |
| OUT_OF_SCOPE | provider/live, public-sync, readiness claims | not needed for deterministic Delta-T1 |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | required verdict |
| --- | --- | --- | --- | --- | --- |
| DELTA-T1-01 | Gamma tool registration | Gamma classifier already exists | `NEW_FINDING` | Could Delta silently replace its contract? | No; add distinct tool and regression coverage |
| DELTA-T1-02 | persistence interface | durable receipt proves preflight | `CHANGED_DISPOSITION` | Could receipt be issued before disk persistence? | No; fail closed until save resolves |
| DELTA-T1-03 | claim boundary | prompt says preflight is required | `REMOVED_OR_REJECTED` | Does that prove external runtime interception? | No; claim remains MCP-call-path guidance only |
| DELTA-T1-04 | secret-safety requirement | audit is secret-safe | `UNCHANGED_FROM_INTAKE` | Could action text leak a raw key? | No; deterministic test must prove raw value absent from response and persisted JSON |

## Acceptance Criteria

| ID | Criterion | Dispatch state |
| --- | --- | --- |
| AC1 | New modular tool is registered as `cvf_preflight_governance_action`; Gamma tool remains source-compatible. | REQUIRED |
| AC2 | `EDIT`, `RUN`, and `COMMIT` inputs are evaluated through the existing guard engine. | REQUIRED |
| AC3 | `ALLOW` returns a receipt only after durable audit persistence succeeds. | REQUIRED |
| AC4 | `BLOCK` and `ESCALATE` remain non-proceed decisions and are durably recorded. | REQUIRED |
| AC5 | Persistence failure fails closed with no valid governed-action claim. | REQUIRED |
| AC6 | Raw credential-bearing text is absent from tool output and persisted audit JSON. | REQUIRED |
| AC7 | MCP prompt guidance requires this preflight before edit/run/commit without claiming external interception. | REQUIRED |
| AC8 | Focused tests, full MCP tests, MCP build, and governance return gates pass. | REQUIRED |
| AC9 | Claude returns uncommitted changes and a worker-return packet; Codex owns closure. | REQUIRED |

## Evidence / Verification

Required worker evidence:

- focused Vitest for Delta-T1;
- focused prompt test;
- `npm run test:run` and `npm run build` in the MCP package;
- temp-directory readback proving durable persisted receipt and secret safety;
- `git diff --check`;
- worker-return fast gate;
- `git status --short` and `git diff --name-status`;
- HEAD unchanged from worker start.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance Delta runtime tranche. No public-sync authorization.

## Claim Boundary

This GC-018 authorizes one deterministic local MCP preflight and durable receipt
component. Even after tests pass, the valid claim is limited to actions that
actually invoke the tool. It does not prove that an external agent called it,
that an edit/run/commit was intercepted, that the receipt was consumed by a
wrapper, or that all coding actions are governed.
