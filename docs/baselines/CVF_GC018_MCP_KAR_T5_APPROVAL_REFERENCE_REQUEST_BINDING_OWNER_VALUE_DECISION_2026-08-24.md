# CVF GC-018 Baseline - MCP-KAR-T5 Approval-Reference Request-Binding Owner Value Decision

Memory class: SUMMARY_RECORD

rawMemoryReleased=false

Status: REVIEWER_ACCEPTED_DISPATCH_READY

Batch ID: MCP-KAR-T5

Dispatch base head: `9f4d20a72`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator

Dispatcher/reviewer/closer: parent agent in explicitly separated phases

Worker target: one delegated local-only evidence decision worker

## Purpose

Authorize one decision-first tranche to determine whether CVF should later
strengthen its existing business-adapter approval reference so it is bound to
the invocation request and explicit approval state. This baseline authorizes
evidence and owner/value analysis only. A caller-supplied contract may validate
binding metadata, but it cannot claim durable replay prevention without a
repository-owned durable approval-state owner.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MCP-KAR-T5 --title "Approval-Reference Request-Binding Owner Value Decision" --date 2026-08-24 --base 9f4d20a72 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "MCP-KAR-T2 closed STOP_NO_NAMED_CONSUMER at 5de1ecc98; operator instructed continue on 2026-08-24" --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker and MCP/CLI boundary stubs |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact T4 dependency, registered approval-reuse negative case, current business-adapter owner, durable-state boundary, terminal outcomes, and local-only boundary |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_packet_authority_and_encoding.py` |
| docOnlyNewFields | `approvalBindingOwnerGate`; `durableReplayClaimGate`; `terminalDisposition` |
| claimBoundary | dispatch evidence only; no executable approval-binding contract or MCP behavior |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| MCP-KAR-T2 bounded stop closure | `docs/reviews/CVF_MCP_KAR_T2_SCHEMA_CONSUMER_OWNER_VALUE_DECISION_WORKER_RETURN_2026-08-23.md`; material `5de1ecc98` | T5 must not reopen schema repair or widen T4 and may inspect only a separate adapted invariant cluster | PASS |
| MCP-KAR-T4 closure | material `43aea7a18`; continuity `9f4d20a72` | releases the next decision-first local tranche only | PASS |
| operator selection | operator autonomous audit/absorption instruction, 2026-08-24 | permits bounded valuable local tranches, not external-effect expansion | PASS |
| pinned T0-T4 evidence | `docs/audits/CVF_MCP_KAR_T0_ABSORPTION_AUDIT_2026-08-23.md`; T1 material `c179e656a` | reuse ledgers and prove non-duplication against T1/current owners | PASS |
| TPGR-R8 hold | `AGENT_HANDOFF_V59_2026-08-11.md` Current Authority and Next Allowed Move | no R8/R9/T15 or runtime/external expansion | PASS |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`MCP approval reference request binding owner value decision dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "MCP approval reference request binding owner value decision dispatch" --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | N/A with reason: resolver returned none |
| Dispatch impact | canonical guards remain binding |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; worker-return checker sources named by the paired work order |
| literalTokensReviewed | dispatch status, ADIF query, Source Verification columns, worker-return contract, operation trace, Delta boundary, external-intake routing, and Public Export Disposition |
| gateRunPurpose | confirm completed source-backed dispatch shape |
| claimBoundary | paired T5 baseline/work order and expected worker return only |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| external redesign flags reused approval references as a negative case | SECONDARY_COMPARISON_EVIDENCE | `.private_reference/legacy/CVF 13.08/CVF_MCP_KNOWLEDGE_ABSORPTION_REDESIGN/docs/reference/mcp_knowledge_absorption_redesign/fixtures/negative_cases/reused_approval_reference.json` | root object | reused approval reference | comparison/test hypothesis only | ACCEPT |
| current invocation request carries a nullable approval reference | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mcp.business.adapter.contract.ts` | `MCPBusinessToolInvocationRequest` | `approvalReference` | execution-plane business adapter | ACCEPT |
| current approval decision accepts any truthy reference for approval-required tools | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mcp.business.adapter.contract.ts` | decision helper | `deriveApprovalDecision` | `MCPBusinessAdapterContract` | ACCEPT |
| durable decision and replay state are not owned by this pure contract | GOVERNED_REFERENCE | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mcp.business.adapter.contract.ts` | owner/collision boundary | `deriveApprovalDecision` has no consumed/expiry/request-bound repository | execution-plane business adapter | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| proposed artifact paths | baseline, work-order, and worker-return paths returned `False` before authoring | PASS |
| current approval-binding contract search | exact owner accepts a truthy string but has no request-id, decision, expiry, or consumed-state binding | PASS_WITH_GAP_OBSERVED |
| adjacent-owner overlap | CADP durable evidence and generic approval controls do not duplicate this exact business-invocation seam | PASS_NON_DUPLICATE_CANDIDATE |
| collision decision | new decision-only T5; no T1-T4 mutation | PASS |

## Decision / Baseline

The worker returns `PROCEED_APPROVAL_BINDING_CONTRACT` only if all five gates pass:

1. the registered negative case and current local gap are source-verified;
2. the exact current request and decision owner is named by path and symbol;
3. the proposed binding contract is non-duplicate with existing approval and
   durable-evidence owners;
4. a later pure implementation can validate caller-supplied binding state
   without claiming it persists or prevents replay durably; and
5. the smallest later manifest, tests, and objective durable-owner limitation
   are exact.

If any gate fails, return `STOP_DUPLICATE_OR_NO_DURABLE_OWNER`. Neither outcome may
implement the rule in this tranche.

## Scope / Owner Boundary

Allowed work is targeted direct reading of the registered external negative
fixture, T0-T4 evidence, the current business-adapter request/decision owner,
and adjacent approval/durable-evidence owners, followed by one worker return.
All existing source, test,
checker, registry, roadmap, schema, session, and runtime paths are read-only.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | business-adapter request and decision contract | decision evidence only; caller-supplied binding metadata cannot establish durable state | registered negative case plus current source | N/A with reason: no implementation | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | possible future caller | no ingress, authentication, persistence, mutation, consumption, or replay-prevention authority | owner/value decision must precede any adapter | deferred durable/runtime work order | `DEFERRED_WITH_REASON` |

## MCP/CLI Adapter Boundary

| Field | Value |
| --- | --- |
| Adapter scope | owner/value decision for a possible approval-reference binding guard |
| No-runtime-overclaim | This packet does not claim an adapter executes, intercepts, wraps, connects to, or certifies any MCP runtime command or transport. |

## Risk / Corrective Action

The risk is accepting an approval reference that is unrelated, expired,
denied, or already consumed, or overstating a pure validation contract as
durable replay prevention. The control is decision-first owner composition,
an explicit durable-state claim boundary, and no implementation authority.

## Evidence / Verification

The worker must record exact source sections, current-source search commands,
owner paths and symbols, overlap with current approval/durable owners, all five
gate outcomes, terminal decision, current HEAD/status, exact changed set, and
the worker-return fast-gate result. The reviewer must recompute the decisive
searches and inspect the named owner before acceptance.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | reuse T0 row classifications and compare only the registered reused-reference negative case with current business-adapter and durable-evidence owners |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_overlap_discipline.py` |
| Owner surface | MCP gateway, Work Order/approval, Guard Contract, and execution-plane candidates |
| Disposition | decision-only reuse; no new intake or direct import |
| Claim boundary | pinned upstream supplies protocol facts; external synthesis remains secondary evidence |

## External Absorption Core

| Field | Value |
| --- | --- |
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | T0-pinned official MCP source mirror plus registered copied external redesign folder |
| Enumeration command | reused T0 filesystem-backed `rg --files --hidden --no-ignore -g '!.git/**'` and recursive file reconciliation |
| Manifest artifact or inline manifest | `docs/audits/CVF_MCP_KAR_T0_UPSTREAM_MANIFEST_2026-08-23.json`; `docs/audits/CVF_MCP_KAR_T0_EXTERNAL_REDESIGN_MANIFEST_2026-08-23.json` |
| Processing ledger artifact or inline ledger | `docs/audits/CVF_MCP_KAR_T0_UPSTREAM_FILE_LEDGER_2026-08-23.json`; `docs/audits/CVF_MCP_KAR_T0_EXTERNAL_REDESIGN_FILE_LEDGER_2026-08-23.json` |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | `docs/audits/CVF_MCP_KAR_T0_ABSORPTION_AUDIT_2026-08-23.md` Current CVF Owner Map plus this decision's current-source composition check |
| Unresolved items | zero unclassified/unreadable; T5 targets one registered negative case and named current owner surfaces |
| Completion claim boundary | reuse of accepted T0 corpus evidence only; no new completeness or implementation claim |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
| --- | --- | --- | --- | --- | --- |
| reused-approval-reference negative case | request/reference replay-binding hypothesis | `DOCTRINE_ADAPTED` | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mcp.business.adapter.contract.ts` | decide bounded owner/value seam | no runtime/package action |
| caller-supplied approval-state cases | deterministic contract-validation scenarios | `CHECKER_CANDIDATE` | paired business-adapter test owner | later tests must be CVF-native, not imported | no direct import or execution |
| package projection | no package value is established | `PACKAGE_CANDIDATE` | `docs/reference/mcp_gateway/` | hold with reason: decision does not justify a package | package activation forbidden |
| runtime projection | durable issuance, lookup, expiry, and consume-once enforcement are outside T5 | `RUNTIME_CANDIDATE` | future repository-owned approval-state surface | park pending named owner and separate authority | runtime/persistence wiring forbidden |
| external security test plan prose | test-design hypothesis only | `NO_PACKAGE_OR_RUNTIME_VALUE` | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | comparison-only; reject direct import | no runtime/package value |
| external implementation prescription | upstream-specific implementation detail is not CVF authority | `REJECT_DIRECT_IMPORT` | `docs/reference/mcp_gateway/CVF_MCP_NORMATIVE_INVARIANT_PROFILE.md` | retain only the verified normative rule and fixture evidence | direct import forbidden |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| approval-reference request binding | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mcp.business.adapter.contract.ts` | `ENRICH_EXISTING` | exact invocation seam validates only string presence today | decide bounded owner and contract-only delta |
| external negative fixture | `docs/audits/CVF_MCP_KAR_T0_EXTERNAL_REDESIGN_FILE_LEDGER_2026-08-23.json`; `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mcp.business.adapter.contract.test.ts` | `ENRICH_EXISTING` | no current request-bound/expiry/decision/consumed validation | secondary decision evidence only |
| external implementation/test-plan prose | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | `REJECT_DIRECT_IMPORT` | governance/testing discipline is already owned | do not import or execute |

## Mandatory Blind-Spot Control Block

NOT_APPLICABLE_WITH_REASON: T5 reuses complete reconciled T0 ledgers and one
already classified negative-case row; it opens no new source family or scan.

## Corpus Completeness And Report Integrity

- Corpus task class: targeted decision reusing the accepted MCP-KAR-T0 dual-corpus manifest and ledgers.
- Corpus root: T0-pinned MCP source mirror and registered copied external redesign folder.
- Snapshot time: 2026-08-23T00:00:00+07:00, reused from accepted T0.
- Enumeration command: filesystem-backed direct file reads plus `rg --files --hidden --no-ignore -g '!.git/**'` reconciliation recorded by T0.
- Manifest artifact or inline manifest: the two committed T0 manifest JSON artifacts.
- Manifest hash: combined T0 receipt `fb3b313dd136095352598f575cc54f46d7fc8a6440fd0cdc2fdc493902780c35`.
- Processing ledger artifact or inline ledger: the two committed T0 semantic ledger JSON artifacts.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE; semantic rows also retain ADAPTED, REJECTED, and NO_NEW_VALUE.
- Reconciliation: manifest=993; ledger_terminal=993; exclusions=0; unresolved=0.
- Unresolved files: zero unclassified or unreadable files; deferred rows retain explicit terminal rationale.
- Declared exclusions: none.
- Unreadable or unsupported files: none.
- Aggregation check: 885 upstream plus 108 external equals 993.
- Drift check: REUSED_ACCEPTED_T0; T5 performs exact file-existence/source reads only.
- Output traceability: exact T0 manifest/ledger paths, hashes, evidence selectors, and owner surfaces remain the source of record.
- Adversarial verification: T5 reuses the registered reused-approval-reference negative case but does not execute or import it.
- Corpus verdict: COMPLETE_VERIFIED - reused accepted T0 corpus proof; no new scan claim.

## External Repository Absorption Entry Control

COMPARISON_ONLY_NO_ABSORPTION: no new enumeration, ledger, source import,
schema adoption, runtime, or external action occurs.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance decision dispatch; no public-sync authority.

## Claim Boundary

This baseline authorizes one documentation-only owner/value decision. It does
not authorize contract/test implementation, durable approval persistence or replay-prevention claims, schema changes,
MCP runtime/package/transport, provider/live, public sync, deployment,
production, TPGR-R8/R9, P0/P1, canary/selective execution, or T15.

