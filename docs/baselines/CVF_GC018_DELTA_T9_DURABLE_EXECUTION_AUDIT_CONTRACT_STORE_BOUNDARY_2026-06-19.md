# CVF GC-018 - Delta-T9 Durable Execution Audit Contract And Store Boundary

Memory class: FULL_RECORD

Status: DISPATCHED

Date: 2026-06-19

Owner: Codex dispatcher, Claude worker, Codex reviewer

Base head: `1c1247d6`

## Purpose

Authorize a bounded Delta-T9 implementation tranche that adds a durable,
secret-safe execution-audit contract and local JSONL store boundary for existing
Delta receipt-to-execution evidence.

This tranche may make supplied Delta evidence durable. It must not make MCP
tools mandatory, add wrapper/proxy enforcement, intercept IDE/shell/git/
filesystem actions, execute EDIT or COMMIT actions, add provider/live behavior,
publish public artifacts, or claim universal governed-coding control.

## Decision / Baseline / Proposed Tranche

| Field | Disposition |
| --- | --- |
| Decision | dispatch durable execution audit contract and local store boundary |
| Baseline | GGL-T2 final handoff bridge `1c1247d6` |
| Proposed tranche | Delta-T9 |
| Route | `MULTI_AGENT_MULTI_ROLE` |
| Worker commit mode | `WORKER_MUST_NOT_COMMIT` |
| Runtime mutation | bounded new audit module and tests only |
| Risk ceiling | R1 local deterministic audit persistence |

## Scope / Target / Owner Boundary

Allowed scope:

- add one TypeScript durable execution audit contract/store module under the
  existing MCP audit owner surface;
- add one focused Vitest file for the new module;
- create a Claude worker-return review packet and evidence JSON;
- keep all persistence local, caller-directed, append-only or fail-closed;
- record retention/privacy/secret-safe boundaries in the contract output.

Forbidden scope:

- no MCP tool registration or `src/index.ts` changes;
- no launcher/profile expansion and no existing launcher behavior change;
- no Model Gateway, CVF Web, queue, daemon, provider/live, public-sync, lockfile,
  generated session state, active handoff, or front-door changes by Claude;
- no direct IDE, shell, git, or filesystem interception claim;
- no universal governed-coding, external readiness, deployment readiness, release
  readiness, or mandatory invocation claim.

## Source Verification Block

| Claimed item | Verification type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Preflight evidence schema exists. | EXISTS | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/guards/types.ts` | lines 51 and 62 | `GuardPipelineResult`; `GuardAuditEntry` | guard types | ACCEPT |
| Receipt consumption marker schema exists and is already persisted by a JSON store. | EXISTS | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/persistence/json-receipt-consumption.store.ts` | lines 24, 55, 73, 86 | `ReceiptConsumptionMarker`; `JsonReceiptConsumptionStore`; `claimReceipt` | receipt consumption store | ACCEPT |
| Governed execution receipt schema exists and is already persisted/finalized by a JSON store. | EXISTS | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/persistence/json-governed-execution.store.ts` | lines 13, 59, 73, 106, 133 | `GovernedExecutionReceipt`; `JsonGovernedExecutionStore`; `beginExecution`; `finalizeExecution`; `readExecution` | governed execution store | ACCEPT |
| Receipt-to-execution evidence auditor exists and exposes bounded evidence/action verdicts. | EXISTS | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/receipt-to-execution-evidence-auditor.ts` | lines 55, 64, 67-68, 93, 200-201 | `ReceiptToExecutionEvidenceInput`; `ReceiptToExecutionEvidenceAudit`; `auditReceiptToExecutionEvidence`; `evidenceChainValid`; `actionExecutionProved` | Delta-T7 auditor | ACCEPT |
| Static launcher profiles and approval-marker profile exist, but arbitrary command/profile expansion is not authorized. | EXISTS | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts` | lines 34-35, 40, 48, 52-69 | `GovernedCommandProfile`; `getGovernedCommandProfile`; `approval-marker-write` | governed command launcher | ACCEPT |
| Approval marker contract and fixed target writer exist. | EXISTS | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/mutating-profile-approval.ts` | lines 11, 14, 166, 191 | `APPROVAL_MARKER_TARGET_RELATIVE_PATH`; `APPROVAL_MARKER_CONTRACT`; `writeApprovalMarkerFile` | mutating profile approval | ACCEPT |
| Delta capability roadmap parks durable audit until fresh GC-018, source-verified work order, storage schema, privacy boundary, retention/disposal rule, and drift check. | LITERAL_INVARIANT | `docs/roadmaps/CVF_DELTA_EXECUTION_CONTROL_CAPABILITY_ROADMAP_2026-06-19.md` | lines 149 and 165 | `Durable execution audit`; `Delta-T9 Durable Audit Store` | Delta-T5 roadmap | ACCEPT |

## New Planned Runtime Surface

| Planned item | Required shape | Purpose |
| --- | --- | --- |
| `durable-execution-audit-store.ts` | pure builder plus local JSONL store boundary | make existing Delta evidence durable without runtime interception |
| `DurableExecutionAuditRecord` | typed record with contract version, identity chain, verdicts, retention, secret-safe boundary, and claim boundary | stable audit record |
| `JsonDurableExecutionAuditStore` or equivalent | caller-supplied directory/file, append/read methods, fail-closed path handling | local durable audit storage boundary |
| `DURABLE_EXECUTION_AUDIT_CONTRACT` or equivalent | literal contract version string | drift-checkable contract identity |

These are new planned symbols, not existing source facts. Claude may adjust exact
symbol names only if the worker-return packet records the final names and keeps
the same contract semantics.

## Durable Execution Audit Store Control Block

| Field | Disposition |
| --- | --- |
| chain | preflight audit -> receipt consumption -> governed execution -> optional approval marker -> Delta-T7 audit verdict -> durable audit record |
| identity | receiptId, requestId, consumptionId, profileId, bindingHash, and contractVersion must be preserved |
| persistence | local JSONL or equivalent append-only file boundary under caller-supplied path |
| path policy | caller may choose audit directory/file; store must reject traversal or unsafe non-local paths if path normalization is implemented |
| privacy boundary | no raw secrets, environment values, provider keys, or full command output in durable records |
| retention | record includes retention class and disposal advisory; no deletion daemon in this tranche |
| durability claim | durable local record only, not external action observation |
| claim boundary | no mandatory invocation, no direct interception, no provider/live proof |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
| --- | --- |
| claimScope | durable audit contract and local store boundary |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | `CVF_RECEIPT_PRESENT` when supplied chain includes valid receipt; `CLAIM_REJECTED_NO_RECEIPT` otherwise |
| actionEvidence | `ACTION_EVIDENCE_PRESENT` only when Delta-T7 `actionExecutionProved` is true; `CLAIM_REJECTED_NO_ACTION` otherwise |
| invocationBoundary | cooperating caller or wrapper supplies evidence and calls the store |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception |
| claimLanguage | durable local audit evidence for supplied chain |
| forbiddenExpansion | wrapper/proxy enforcement, direct interception, EDIT/COMMIT, provider/live, public-sync, queue/daemon, and universal control parked |

## Delta Mutating Profile Boundary Control Block

| Field | Disposition |
| --- | --- |
| profileScope | read existing static profile evidence only when supplied by caller |
| fixedTargetPolicy | existing approval-marker target only, if approval-marker evidence is present |
| approvalEvidenceSource | optional supplied marker under existing Delta-T4A contract |
| callerPathInput | CALLER_PATH_INPUT_FORBIDDEN as target authority; store records observed changed set only as supplied evidence |
| commandAuthority | no command authority, launcher profile, or target path authority added |
| receiptChain | existing receipt/consumption/execution/audit identity chain only |
| claimBoundary | durable audit record does not add mutation or execution capability |
| forbiddenExpansion | arbitrary targets, EDIT/COMMIT, provider/live, public-sync, and interception remain parked |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | runtime/provider/mcp/readiness claim |
| Chain map route | external runtime-control finding -> Delta roadmap -> durable audit bounded tranche |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| Owner surface | Delta-T9 GC-018 and work order |
| Disposition | `DO_NOW` durable audit store boundary only |
| Claim boundary | no runtime/provider/public/direct-interception/readiness/universal-control claim |

## Acceptance Criteria

| ID | Criterion |
| --- | --- |
| AC1 | Valid Delta-T7 evidence audit can be converted into a durable audit record with stable contract version and identity chain. |
| AC2 | Store appends and reads durable records deterministically in a temp local path. |
| AC3 | Record builder redacts or rejects secret-like fields and records privacy/retention boundaries. |
| AC4 | Invalid or incomplete evidence cannot be persisted as a passing governed-action claim. |
| AC5 | Output explicitly preserves `mandatoryInvocationProved=false` and `directInterceptionProved=false` or equivalent bounded fields. |
| AC6 | Focused tests, MCP package tests, build, worker-return fast gate, and reviewer-fast gate pass before handoff. |

## Evidence / Verification

Required from Claude:

- focused Vitest for the new durable audit store test;
- MCP package `npm run test:run`;
- MCP package `npm run build`;
- worker-return fast gate;
- `git diff --name-status`;
- worker-return review packet;
- evidence JSON;
- explicit no-commit handoff status.

Provider/live and public proof are not applicable because they are forbidden.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance Delta execution-control foundation tranche. Public
sync is not authorized for this worker packet.

## Claim Boundary

Delta-T9 may prove only a bounded local durable audit contract/store for
supplied Delta receipt-to-execution evidence. It does not prove that all actions
pass through CVF, that external actions are observed, that direct IDE/shell/git/
filesystem activity is intercepted, or that CVF has universal governed-coding
control.
