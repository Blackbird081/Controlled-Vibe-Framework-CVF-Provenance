# CVF GC-018 - Delta-T7 Receipt-To-Execution Evidence Auditor

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-19

Owner: Codex

Base head: `f3219048`

## Purpose

Authorize a pure, deterministic auditor that correlates existing Delta
preflight, receipt-consumption, governed-execution, optional approval-marker,
and expected/observed changed-set evidence. It must fail closed on broken
identity, binding, chronology, finalization, profile, or changed-set links.

No new MCP tool registration, command execution, filesystem interception,
provider/live call, public-sync, queue/daemon, or universal governed-coding
claim is authorized.

## Decision / Baseline / Proposed Tranche

| Field | Disposition |
| --- | --- |
| Decision | dispatch pure receipt-to-execution evidence auditor |
| Baseline | GGL-T1 closure session sync `f3219048` |
| Proposed tranche | Delta-T7 |
| Route | `SINGLE_AGENT_MULTI_ROLE` |
| Runtime mutation | forbidden |

## Scope / Target / Owner Boundary

Allowed scope:

- add one pure TypeScript audit module and focused tests;
- consume existing in-memory evidence types without reading runtime files;
- verify receipt and request identity, ALLOW decision, consumption and binding
  identity, execution finalization, chronology, profile, expected/observed
  changed-set equality, and optional approval-marker identity;
- produce stable finding codes and a bounded claim summary;
- add completion review and evidence JSON.

Forbidden scope:

- no launcher, store, preflight, consumer, profile, marker-writer, MCP index,
  provider, Web, CLI registration, queue, daemon, public-sync, or live change;
- no assertion that the auditor forces invocation or observes external actions.

Risk ceiling: R1 pure evidence audit.

## Source Verification Block

| Claimed item | Verification type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Preflight audit carries request identity, context, final decision, and execution timestamp. | EXISTS | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/guards/types.ts` | `GuardAuditEntry`; `GuardPipelineResult` | `GuardAuditEntry`; `GuardPipelineResult` | guard types | ACCEPT |
| Receipt consumption marker carries receipt, consumption, action class, binding hash, and bounded false claims. | EXISTS | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/persistence/json-receipt-consumption.store.ts` | `ReceiptConsumptionMarker` | `ReceiptConsumptionMarker` | receipt consumption store | ACCEPT |
| Governed execution receipt carries receipt/consumption/profile/binding identity, status, chronology, execution flags, and false interception claim. | EXISTS | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/persistence/json-governed-execution.store.ts` | `GovernedExecutionReceipt` | `GovernedExecutionReceipt` | governed execution store | ACCEPT |
| Static profile registry declares the bounded expected mutation target. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts` | `getGovernedCommandProfile` | `getGovernedCommandProfile`; `GovernedCommandProfile` | governed command launcher | ACCEPT |
| Approval marker writer persists contract, profile, approval, binding, consumption, target, and completion evidence. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/mutating-profile-approval.ts` | `writeApprovalMarkerFile` | `APPROVAL_MARKER_CONTRACT`; `writeApprovalMarkerFile` | mutating profile approval | ACCEPT |
| Delta capability roadmap names Delta-T7 and its required evidence classes. | LITERAL_INVARIANT | `docs/roadmaps/CVF_DELTA_EXECUTION_CONTROL_CAPABILITY_ROADMAP_2026-06-19.md` | Delta-T7 row near line 163 | `Delta-T7 Receipt-To-Execution Evidence Auditor` | Delta-T5 roadmap | ACCEPT |

## New Doc-Only Fields

| New item | Required value or shape | Purpose |
| --- | --- | --- |
| `Receipt-To-Execution Audit Control Block` | governed Markdown table | declare chain and claim boundary |
| `expectedChangedSetSource` | static profile target policy | prevent caller-invented expected mutations |
| `observedChangedSetAuthority` | caller-supplied evidence, not filesystem observation | preserve audit boundary |

## Receipt-To-Execution Audit Control Block

| Field | Disposition |
| --- | --- |
| chain | preflight audit -> consumption marker -> governed execution -> optional approval marker -> changed-set evidence |
| identity | receiptId, requestId, consumptionId, profileId, and bindingHash must match owning contracts |
| chronology | preflight, consumption, admission, start, completion, and marker timestamps must be ordered when present |
| finalization | only durable COMPLETED or FAILED execution evidence may pass chain completeness |
| expectedChangedSetSource | static governed profile mutation target; empty for non-mutating profiles |
| observedChangedSetAuthority | explicit caller-provided audit evidence only; no filesystem observation claim |
| claimBoundary | audit consistency only; no mandatory invocation or external interception proof |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
| --- | --- |
| claimScope | pure evidence consistency auditor |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT through existing typed receipt chain |
| actionEvidence | ACTION_EVIDENCE_PRESENT only when finalized execution evidence is internally consistent |
| invocationBoundary | cooperating caller supplies evidence objects |
| interceptionBoundary | no IDE, shell, git, filesystem, or provider interception |
| claimLanguage | evidence chain consistency, not universal governed coding |
| forbiddenExpansion | runtime execution, new profiles/tools, provider/live, public-sync, queue/daemon, and direct interception remain parked |

## Delta Mutating Profile Boundary Control Block

| Field | Disposition |
| --- | --- |
| profileScope | existing static profile metadata is read only |
| fixedTargetPolicy | existing approval-marker target only |
| approvalEvidenceSource | optional supplied marker under existing contract |
| callerPathInput | CALLER_PATH_INPUT_FORBIDDEN as target authority; observed changed set is evidence only |
| commandAuthority | no command authority added |
| receiptChain | existing receipt/consumption/execution identity audit |
| claimBoundary | no mutation or execution capability added |
| forbiddenExpansion | arbitrary targets, EDIT/COMMIT, provider/live, public-sync, and interception remain parked |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | runtime/provider/mcp/readiness claim |
| Chain map route | current runtime contracts -> source verification -> bounded pure auditor |
| Matching local-view guard | `governance/compat/check_delta_execution_claim_boundary.py` |
| Owner surface | Delta-T7 GC-018 and work order |
| Disposition | `DO_NOW` for pure audit; runtime expansion remains blocked |
| Claim boundary | no runtime/provider/public/direct-interception/readiness claim |

## Acceptance Criteria

| ID | Criterion |
| --- | --- |
| AC1 | Valid non-mutating finalized chain passes with empty changed set. |
| AC2 | Valid approval-marker chain passes only with its fixed target and matching marker. |
| AC3 | Identity, binding, decision, chronology, finalization, profile, marker, or changed-set mismatch fails with stable code. |
| AC4 | Unknown profile and ADMITTED-only evidence fail closed. |
| AC5 | Output explicitly keeps external interception and mandatory invocation unproved. |
| AC6 | Focused tests, package tests, and build pass. |

## Evidence / Verification

Required: focused Vitest, package `test:run`, package build, worker-return gate,
committed-range pre-closure, exact diff/status, completion review, and evidence
JSON. Provider/live and public evidence are not applicable because forbidden.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance Delta evidence-control tranche.

## Claim Boundary

Delta-T7 may prove only deterministic consistency auditing of supplied Delta
evidence objects. It does not prove that an external action occurred, that all
actions pass through CVF, or that IDE/shell/git/filesystem activity is
intercepted.
