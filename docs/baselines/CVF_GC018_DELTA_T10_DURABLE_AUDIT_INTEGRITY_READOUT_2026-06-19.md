# CVF GC-018 - Delta-T10 Durable Audit Integrity Readout

Memory class: FULL_RECORD

Status: DISPATCHED

Date: 2026-06-19

Owner: Codex dispatcher, Claude worker, Codex reviewer

Base head: `5f774742`

## Purpose

Authorize a bounded Delta-T10 implementation tranche that adds a deterministic,
secret-safe integrity readout for supplied Delta-T9 durable execution audit
records.

This tranche may classify the integrity of durable audit records that are
already supplied to the readout. It must not create mandatory MCP invocation,
wrapper/proxy enforcement, direct IDE/shell/git/filesystem interception,
arbitrary command execution, EDIT or COMMIT execution, provider/live behavior,
public artifacts, queues, daemons, CVF Web action execution, release readiness,
or universal governed-coding control.

## Decision / Baseline / Proposed Tranche

| Field | Disposition |
| --- | --- |
| Decision | dispatch durable audit integrity readout for supplied records |
| Baseline | Delta-T9 closure continuity `5f774742` |
| Proposed tranche | Delta-T10 |
| Route | `MULTI_AGENT_MULTI_ROLE` |
| Worker commit mode | `WORKER_MUST_NOT_COMMIT` |
| Runtime mutation | bounded new audit readout module and tests only |
| Risk ceiling | R1 local deterministic audit classification |

## Scope / Target / Owner Boundary

Allowed scope:

- add one TypeScript durable audit integrity readout module under the existing
  MCP audit owner surface;
- add one focused Vitest file for the new module;
- create a Claude worker-return review packet and evidence JSON;
- classify supplied records and/or supplied JSONL text only;
- keep output deterministic, secret-safe, and explicit about bounded false claim
  fields.

Forbidden scope:

- no MCP tool registration or `src/index.ts` changes;
- no launcher/profile expansion and no existing launcher behavior change;
- no Model Gateway, CVF Web, queue, daemon, provider/live, public-sync, lockfile,
  generated session state, active handoff, or front-door changes by Claude;
- no direct IDE, shell, git, or filesystem interception claim;
- no arbitrary command, EDIT, COMMIT, public action, provider action, external
  readiness, deployment readiness, release readiness, or universal governed
  coding claim.

## Source Verification Block

| Claimed item | Verification type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Durable audit contract constant exists. | EXISTS | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-execution-audit-store.ts` | line 11 | `DURABLE_EXECUTION_AUDIT_CONTRACT` | Delta-T9 durable store | ACCEPT |
| Binding hash validation pattern exists. | EXISTS | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-execution-audit-store.ts` | line 14 | `BINDING_HASH_PATTERN` | Delta-T9 durable store | ACCEPT |
| Durable audit record interface exists. | EXISTS | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-execution-audit-store.ts` | line 28 | `DurableExecutionAuditRecord` | Delta-T9 durable store | ACCEPT |
| Durable records set mandatory invocation proof false. | LITERAL_INVARIANT | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-execution-audit-store.ts` | lines 43, 109, and 138 | `mandatoryInvocationProved` | `DurableExecutionAuditRecord`; `buildDurableAuditRecord`; `validateDurableRecordBoundary` | ACCEPT |
| Durable records set direct interception proof false. | LITERAL_INVARIANT | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-execution-audit-store.ts` | lines 44, 110, and 141 | `directInterceptionProved` | `DurableExecutionAuditRecord`; `buildDurableAuditRecord`; `validateDurableRecordBoundary` | ACCEPT |
| Durable store validates records before append/read. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-execution-audit-store.ts` | lines 121, 156-157, and 181-182 | `validateDurableRecordBoundary`; `appendRecord`; `readRecords` | `JsonDurableExecutionAuditStore` | ACCEPT |
| Receipt-to-execution audit exposes evidence, action, and approval-backed mutation proof fields. | EXISTS | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/receipt-to-execution-evidence-auditor.ts` | lines 64 and 67-69 | `ReceiptToExecutionEvidenceAudit`; `evidenceChainValid`; `actionExecutionProved`; `approvalBackedMutationProved` | Delta-T7 auditor | ACCEPT |
| Delta-T9 completion status is closed. | VALUE_SET | `docs/reviews/CVF_DELTA_T9_DURABLE_EXECUTION_AUDIT_CONTRACT_STORE_BOUNDARY_COMPLETION_2026-06-19.md` | line 5 | `Status` | Delta-T9 completion packet | ACCEPT |
| Delta-T9 completion records focused, full MCP, build, and worker-return gate evidence. | VALUE_SET | `docs/reviews/CVF_DELTA_T9_DURABLE_EXECUTION_AUDIT_CONTRACT_STORE_BOUNDARY_COMPLETION_2026-06-19.md` | line 121 | `AC6` | Delta-T9 completion packet | ACCEPT |
| Roadmap parks durable audit and all broader execution-control claims behind fresh source-verified work. | LITERAL_INVARIANT | `docs/roadmaps/CVF_DELTA_EXECUTION_CONTROL_CAPABILITY_ROADMAP_2026-06-19.md` | lines 149-151 and 158 | `Durable execution audit`; `Wrapper/proxy enforcement`; `Direct IDE/shell/git/filesystem interception`; `Next-Tranche Release Conditions` | Delta execution roadmap | ACCEPT |

## New Planned Runtime Surface

| Planned item | Required shape | Purpose |
| --- | --- | --- |
| `durable-execution-audit-readout.ts` | pure deterministic readout helpers over supplied records and/or supplied JSONL text | classify durable record integrity without observing external actions |
| `DURABLE_AUDIT_INTEGRITY_READOUT_CONTRACT` | literal contract version string | drift-checkable readout identity |
| `DurableAuditIntegrityReadout` | typed summary with total, valid, invalid, finding counts, and claim-boundary fields | reviewable readout output |
| `DurableAuditIntegrityFinding` | typed finding records with deterministic codes and record identity | classify corrupt, forged, incomplete, or secret-like records |
| `buildDurableAuditIntegrityReadout` | pure function over supplied records | deterministic integrity classification |
| `parseDurableAuditJsonlLines` or equivalent | parser for supplied JSONL text, if implemented | classify parse failures without file I/O |

These are new planned symbols, not existing source facts. Claude may adjust exact
symbol names only if the worker-return packet records the final names and keeps
the same contract semantics.

## Durable Audit Integrity Readout Control Block

| Field | Disposition |
| --- | --- |
| input boundary | supplied `DurableExecutionAuditRecord[]` and/or supplied JSONL text only |
| identity | receiptId, requestId, consumptionId, profileId, bindingHash, and contractVersion preserved in findings when safe |
| parsing | fail-closed parse findings for malformed supplied JSONL lines |
| classification | invalid contract, malformed identity, invalid binding hash, invalid proof consistency, forbidden true claim fields, and secret-like values |
| determinism | stable sorted findings and stable summary counts |
| privacy boundary | no raw secrets, environment values, provider keys, or full command output in readout output |
| retention | readout reports existing retention/disposal fields; no deletion daemon |
| claim boundary | readout classifies supplied records only; no mandatory invocation, direct interception, provider/live proof, or external observation |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
| --- | --- |
| claimScope | durable audit integrity readout for supplied records only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | `CVF_RECEIPT_PRESENT` only when supplied records include valid receipt identity; `CLAIM_REJECTED_NO_RECEIPT` for missing or invalid receipt identity |
| actionEvidence | `ACTION_EVIDENCE_PRESENT` only as a supplied durable record field; `CLAIM_REJECTED_NO_ACTION` for invalid or missing action evidence |
| invocationBoundary | cooperating caller supplies records or JSONL text to the readout |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception |
| claimLanguage | deterministic integrity readout of supplied durable audit records |
| forbiddenExpansion | wrapper/proxy enforcement, direct interception, EDIT/COMMIT, provider/live, public-sync, queue/daemon, CVF Web action execution, and universal control parked |

## Delta Mutating Profile Boundary Control Block

| Field | Disposition |
| --- | --- |
| profileScope | N/A with reason: no mutating profile or target mutation is added |
| fixedTargetPolicy | N/A with reason: no target authority is added |
| approvalEvidenceSource | existing supplied durable record field only when present |
| callerPathInput | CALLER_PATH_INPUT_FORBIDDEN as target authority; readout consumes supplied record text/objects only |
| commandAuthority | no command authority, launcher profile, or target path authority added |
| receiptChain | existing receipt/consumption/execution/audit identity chain only |
| claimBoundary | readout does not add mutation or execution capability |
| forbiddenExpansion | arbitrary targets, EDIT/COMMIT, provider/live, public-sync, and interception remain parked |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order owner | Evidence |
| --- | --- | --- |
| durable execution audit requires fresh source-verified work | Codex dispatch | this GC-018 and matching Delta-T10 work order |
| secret-safe retention/disposal readout | Claude worker | integrity readout fields, focused tests, worker return |
| local gate evidence | Claude worker | focused/full/build/worker-return fast gate results |
| wrapper/proxy and direct interception remain parked | Claude worker and Codex reviewer | claim boundary blocks and forbidden scope |
| no universal control claim | Claude worker and Codex reviewer | readout-only contract and closure evidence |

## Acceptance Criteria

| ID | Criterion |
| --- | --- |
| AC1 | Valid Delta-T9 durable records produce a deterministic integrity readout with stable contract version, valid counts, and no findings. |
| AC2 | Malformed JSONL or structurally invalid records produce findings and cannot be summarized as all valid. |
| AC3 | `mandatoryInvocationProved=true` or `directInterceptionProved=true` is classified as a violation, and bounded false fields remain explicit in valid summaries. |
| AC4 | Secret-like values in supplied record fields are classified or rejected without being echoed raw in readout output. |
| AC5 | Finding order and finding counts are deterministic across repeated calls. |
| AC6 | Focused tests, MCP package tests, build, worker-return fast gate, and reviewer-fast gate pass before handoff. |

## Evidence / Verification

Required from Claude:

- focused Vitest for the new durable audit integrity readout test;
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

Delta-T10 may prove only a bounded deterministic integrity readout for supplied
Delta-T9 durable execution audit records. It does not prove that all actions
pass through CVF, that external actions are observed, that direct IDE/shell/git/
filesystem activity is intercepted, or that CVF has universal governed-coding
control.
