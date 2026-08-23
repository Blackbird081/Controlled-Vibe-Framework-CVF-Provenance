# CVF GC-018 Baseline - MCP-KAR-T5 Approval-Reference Request-Binding Contract Implementation

Memory class: governed-dispatch-baseline

Status: REVIEWER_ACCEPTED_DISPATCH_READY

Batch ID: MCP-KAR-T5I

Dispatch base head: 6801f9333ec03c035aa9651c3a1a77b2b7926489

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: parent reviewer/closer

Worker target: implementation worker subagent

## Purpose

Implement the T5-approved pure caller-supplied approval-reference binding
contract in the existing MCP business adapter. Fail closed before an
approval-required branch treats supplied evidence as valid, while preserving
the existing read-only and approval-not-required behavior and all durable-state
boundaries.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MCP-KAR-T5I --title "Approval-Reference Request-Binding Contract Implementation" --date 2026-08-24 --base 6801f9333ec03c035aa9651c3a1a77b2b7926489 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "MCP-KAR-T5 reviewer-accepted decision c7388c127; operator autonomous valuable absorption instruction" --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker and MCP/CLI boundary stubs |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | accepted T5 authority, exact three-path implementation manifest, binding/time/consumed behavior, deterministic verification, and durable-state exclusions |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| docOnlyNewFields | caller-supplied approval evidence fields and deterministic local validation result fields selected by the worker inside the accepted semantic boundary |
| claimBoundary | dispatch authority only; no implementation, approval-state mutation, or runtime action has occurred |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| operator selection | autonomous valuable-absorption instruction, 2026-08-24 | operator may select valuable bounded local tranches under CVF rules | RELEASED |
| T5 owner/value decision | reviewer-accepted closure `c7388c127`; decision return names `PROCEED_APPROVAL_BINDING_CONTRACT` and exact three-path later manifest | all five decision gates PASS and durable replay limitation explicit | RELEASED |
| current clean implementation base | clean HEAD `6801f9333ec03c035aa9651c3a1a77b2b7926489` | implementation dispatch must start from accepted decision continuity | RELEASED |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`MCP approval-reference request-binding contract implementation dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "MCP approval-reference request-binding contract implementation dispatch" --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | N/A with reason: resolver returned none |
| Dispatch impact | canonical guards and the accepted T5 durable-state boundary remain binding |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | dispatch status; Source Verification columns; fulfillment manifest; worker-return profile; operation-trace labels; Delta boundary enums; MCP adapter boundary; Public Export Disposition |
| gateRunPurpose | confirm the authored dispatch is structurally complete after source/checker read-ahead; gates are not first-discovery tools |
| claimBoundary | paired documentation dispatch only |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| T5 authorizes bounded contract implementation | GOVERNED_REVIEW | `docs/reviews/CVF_MCP_KAR_T5_APPROVAL_REFERENCE_REQUEST_BINDING_OWNER_VALUE_DECISION_WORKER_RETURN_2026-08-24.md` | Findings / Position; Mandatory Decision Gates; Decision / Disposition | `PROCEED_APPROVAL_BINDING_CONTRACT`; exact later manifest | reviewer-accepted T5 decision `c7388c127` | ACCEPT |
| request and approval decision share one owner | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mcp.business.adapter.contract.ts` | request interface and approval evaluation | `MCPBusinessToolInvocationRequest`; `MCPBusinessAdapterContract.deriveApprovalDecision` | execution-plane foundation | ACCEPT |
| current gap is truthiness-only approval | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mcp.business.adapter.contract.ts` | approval-required risk branches | `request.approvalReference` checks | MCP business adapter | ACCEPT |
| focused regression owner exists | TEST_SOURCE_FACT | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mcp.business.adapter.contract.test.ts` | read-only, approval-required, destructive, and transport cases | `makeRequest`; business-adapter suite | Vitest test owner | ACCEPT |
| public type export owner exists | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/index.ts` | MCP business-adapter export block | business-adapter type exports | execution-plane barrel | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| proposed dispatch paths | both absent before authoring | PASS |
| exact owner collision | T5 selected the existing business adapter; a parallel approval owner is forbidden | PASS |
| durable owner collision | Guard Contract approval evidence and CADP grant consumption own different authority objects; no MCP approval-state repository owner is selected | PASS |
| worker fresh search | worker must search current source/tests for approval-evidence, request-binding, issuance, consumption, persistence, replay, and secret-like identifier controls before editing | REQUIRED_BEFORE_EDIT |

## Decision / Baseline

The worker may enrich only the existing MCP business-adapter request and
approval decision seam with a closed caller-supplied evidence shape. An
approval-required branch accepts supplied evidence only when:

- the evidence reference and bound request ID match the current invocation
  exactly;
- the supplied decision is exactly `APPROVE`;
- issued and expiry timestamps are valid, ordered, and contain the explicit
  injected `now` instant;
- `consumed` is exactly `false`; and
- all required fields are present, no unknown fields exist, and metadata
  identifiers are bounded non-secret-like identifiers.

Bare references, mismatches, non-approved decisions, expired/future/malformed
time values, consumed evidence, missing or unknown fields, and secret-like
identifiers fail closed. The evaluator receives metadata only and must not
issue, persist, look up, consume, mutate, log, or return raw credentials or
secret material.

## Scope / Owner Boundary

Allowed implementation paths are exactly the current MCP business-adapter
source, focused test, and barrel export named in the work-order manifest. The
only other worker write is one uncommitted worker return. External fixtures,
durable stores, Guard Contract/CADP sources, package manifests, runtime bridges,
transports, sessions, providers, live systems, public sync, deployment, and
production are forbidden.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | MCP business-adapter request and pure approval decision | validates caller-supplied metadata only; cannot prove durable consumption | source plus focused local tests | N/A with reason: direct local contract composition | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | possible future invocation caller | no ingress, issuance, persistence, atomic consume, transport, or execution authority | separate runtime/durable-state work order required | deferred adapter/runtime | `DEFERRED_WITH_REASON` |

## MCP/CLI Adapter Boundary

| Field | Value |
| --- | --- |
| Adapter scope | no new adapter; pure validation inside an existing local business-adapter contract |
| No-runtime-overclaim | This dispatch does not authorize an MCP client/server, CLI, bridge, transport, approval issuer/store, network path, or external invocation. |

## Risk / Corrective Action

The primary risk is describing caller-supplied `consumed=false` evidence as
replay protection. Correct by exposing explicit local validation only, keeping
durable replay/issuance/persistence/atomic consumption claims false or absent,
and testing deterministic repeated input without calling it consume-once
behavior. A durable MCP approval-state owner requires a separate dispatch.

## Evidence / Verification

- focused tests must cover one valid bound approval and every required
  fail-closed class: bare, mismatched, non-approved, expired, future,
  malformed, consumed, missing, unknown, and secret-like;
- focused tests must prove unchanged read-only and approval-not-required paths;
- repeated identical evidence and fixed injected `now` must yield an identical
  decision/hash without state mutation;
- run the package's actual focused test command, full package tests, and
  TypeScript no-emit check;
- prove the exact changed set and zero issuance/persistence/consumption seam;
- run pre-implementation and worker-return fast governance gates;
- provider/network/live call count must remain zero.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | reuse accepted T5 decision and rewrite the retained negative scenario as CVF-native local tests; no new intake |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_overlap_discipline.py` |
| Owner surface | exact three-path MCP business-adapter manifest |
| Disposition | bounded native implementation; no direct fixture or source import |
| Claim boundary | current CVF source owns the contract; copied evidence grants no runtime or durable-state authority |

## Mandatory Blind-Spot Control Block

NOT_APPLICABLE_WITH_REASON: this implementation dispatch reuses the accepted T5
targeted decision and exact manifest; it opens no source family, scan, or new
corpus claim.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - targeted implementation from an
  accepted source/owner decision; no inventory or all-files-read claim.

## External Repository Absorption Entry Control

COMPARISON_ONLY_NO_ABSORPTION: no new enumeration, manifest, ledger, source
import, package, durable-state, or runtime work occurs.

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | dispatch authority for pure local caller-supplied approval evidence validation |
| claimDisposition | CLAIM_REJECTED: the baseline does not prove implementation, durable replay prevention, or runtime execution |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: governance checks are not MCP, approval-state, or runtime receipts |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: dispatcher performed reads and documentation authoring only |
| invocationBoundary | repository-local provider-free tools |
| interceptionBoundary | no wrapper, proxy, MCP client/server, CLI, transport, approval repository, or runtime gate |
| claimLanguage | bounded local implementation authority only |
| forbiddenExpansion | issuance/persistence/atomic consumption/durable replay, runtime/package/transport/fixture/session/provider/live/public/deploy/production |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance implementation dispatch; no public-sync authority.

## Claim Boundary

This baseline authorizes only a deterministic repository-local validation
contract inside the exact manifest. It does not claim or authorize approval
issuance, lookup, persistence, atomic consumption, durable replay prevention,
runtime enforcement, MCP interoperability, provider/live behavior, public
export, deployment, or production readiness.
