# CVF GC-018 Baseline - EACQ-FV MV-2 External Agent Task Capsule Context

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: EACQ-FV-MV2

Date: 2026-08-27

Dispatch base head: `22644e47e118bd88bf0d004cb74819fd2956c061`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator

Worker: delegated no-commit implementation worker

Orchestrator/reviewer/closer: designated internal reviewer

providerExecutionAuthority: FORBIDDEN

## Purpose

Open only EACQ-FV-MV2: enrich the existing external-agent task capsule with
four bounded context groups and an explicit offline, staleness-aware creation
path. This extends the current schema/generator owner; it creates no parallel
protocol and makes no quality-effectiveness claim.

## Operator Authorization And Role Split

On 2026-08-27 the operator instructed the orchestrator/reviewer to continue
after MV-1 closure. The orchestrator applied the serious, source-backed,
non-duplicate, value-exceeds-cost gate and selected MV-2 only. MV-3 and UAA
remain parked. The worker must leave all implementation changes unstaged and
uncommitted; the reviewer owns review, bounded repair, commits, closure, and
continuity sync.

## Baseline Decision / Proposed Tranche

| Field | Decision |
| --- | --- |
| Candidate | EACQ-FV-MV2 task-capsule context enrichment |
| Quality-first action | REMEDIATE_FIRST |
| Why now | The current capsule omits protected paths, owner map, invariants, and verification context, while its production `prepare-task` route refreshes public state before capsule creation. |
| Active-path impact | Bounded extension of the existing schema, generator, wrapper, documentation, and focused tests. |
| Operator authorization | YES, explicit continuation on 2026-08-27 |
| Next batch | EACQ-FV-MV2 only |
| Successor authority | Independent review and fresh operator value gate; no MV-3 or UAA authority follows. |

## Depth Audit

| Question | Answer |
| --- | --- |
| Is the gap source-backed? | YES; direct schema and generator reads show the four groups are absent and `prepare-task` calls `refresh_snapshot` first. |
| Is it serious enough? | YES; the missing fields map to duplicate-owner, protected-path, invariant, and negative-test repair classes seen in recent review. |
| Is it non-duplicate? | YES; the existing capsule is the binding owner and will be enriched in place. |
| Is there a current owner? | YES; the task capsule schema, generator, wrapper, README, and focused tests. |
| Can the owner be extended? | YES; no new protocol or package is required. |
| Is it locally testable? | YES; schema and CLI tests require no provider or network. |
| Are cost, latency, and quota bounded? | YES; five implementation paths, one return, local tests, zero provider quota. |
| Does value exceed cost? | YES; one reusable context contract affects future delegated coding tasks and enables a later evidence-based quality comparison. |

Depth decision: CONTINUE_WITH_BOUNDED_MV2. MV-3 remains parked because MV-1
already preserves forward-value candidates and no capsule-enhanced comparison
evidence exists yet.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| capsule owner exists and is strict | current source fact | `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_TASK_CAPSULE.schema.json` | root required/properties and `additionalProperties: false` | `cvf.externalAgentTaskCapsule.v1` | JSON Schema root | ACCEPT |
| four planned context groups are absent | current source fact | `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_TASK_CAPSULE.schema.json` | root required/properties | `protectedPaths`, `ownerMap`, `invariants`, `verification` | JSON Schema root | ACCEPT |
| generator owns capsule construction | current source fact | `scripts/external_agent_packet.py` | `create_capsule` | `create_capsule(args, public_sha)` | packet CLI module | ACCEPT |
| current prepare route is live-refresh coupled | current source fact | `scripts/external_agent_packet.py` | `main`, command dispatch | `prepare-task`, `refresh_snapshot`, `create_capsule` | packet CLI module | ACCEPT |
| wrapper exposes only refresh, prepare, and validate | current source fact | `scripts/Update-CVF-External-Agent-Packet.ps1` | parameter `Mode` and dispatch branches | `RefreshSnapshot`, `PrepareTask`, `ValidateReturn` | PowerShell wrapper | ACCEPT |
| focused strict-schema test owner exists | current test fact | `scripts/test_external_agent_packet.py` | `test_generated_task_capsule_matches_strict_schema` | `create_capsule` test | pytest module | ACCEPT |
| MV-2 is the selected bounded roadmap lane | governed design fact | `docs/roadmaps/CVF_EXTERNAL_AGENT_CODING_QUALITY_AND_FORWARD_VALUE_ABSORPTION_ROADMAP_2026-08-27.md` | External-Agent Coding Context Contract; Work Plan | `EACQ-FV-MV2` | roadmap | ACCEPT |

## Acceptance Criteria

1. The existing v1 capsule gains exactly four context groups: protected paths,
   owner map, invariants, and verification.
2. Every group carries a named consumer and freshness rule and rejects missing,
   empty, malformed, or unexpected content under the strict schema.
3. The current live-verified prepare route remains backward compatible.
4. A separate explicit offline path creates a capsule from an operator-pinned
   public commit without network access and labels that source as pinned but
   not live-verified; it must not reuse a stale refresh receipt as current truth.
5. CLI and PowerShell wrapper inputs are deterministic and fail closed.
6. Focused positive and negative tests cover both live and offline production
   semantics after the final edit.

## Verification Evidence

Review evidence must include the exact six-path manifest, empty staging,
focused test output, strict-schema positive and negative cases, an independent
offline no-network probe, non-overwrite evidence for invalid input, exact live
versus pinned source-posture values, and applicable governance-gate results.

## Scope Firewall

Worker implementation is limited to the five existing owner/test paths and
one new worker-return path named by the work order. No roadmap, standard,
session, hook, catalog, public packet instance, external packet folder,
provider, network, public-sync, deployment, push, staging, or worker commit is
authorized.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order-authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

The resolver used risk ceiling `MEDIUM`; the result was not truncated.

## Checker Source Read-Ahead Block

| Field | Evidence |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py` |
| literalTokensReviewed | `DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; `providerExecutionAuthority: FORBIDDEN`; Source Verification Block columns; Dispatch Prompt Envelope fields; Agent Operation Trace labels |
| gateRunPurpose | Confirm dispatch, source-verification, read-ahead, trace, and no-commit shapes before authoring. |
| claimBoundary | Read-ahead is preparation evidence; it does not prove implementation correctness or gate success. |

## Scaffold Provenance Block

| Field | Evidence |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id EACQ_FV_MV2_EXTERNAL_AGENT_TASK_CAPSULE_CONTEXT --title "EACQ-FV MV-2 External Agent Task Capsule Context" --date 2026-08-27 --base 22644e47e118bd88bf0d004cb74819fd2956c061 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Filled value gate, exact current owners, four-group contract, offline source posture, tests, boundaries, and return contract. |
| checkerReadAheadConfirmation | Applicable dispatch checker sources were read before authoring. |
| docOnlyNewFields | N/A with reason: the baseline introduces no runtime field; proposed schema fields are worker implementation targets. |
| claimBoundary | Dispatch authoring provenance only. |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | reviewed R0 proposal -> minimum viable roadmap -> MV-1 closure -> MV-2 value gate and dispatch |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | existing external-agent task capsule schema/generator/wrapper |
| Disposition | ENRICH_EXISTING through a bounded no-commit implementation tranche |
| Claim boundary | no direct import, provider use, public mutation, or measured quality claim |

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - bounded current-owner implementation; no corpus scan or completeness claim.

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON
- N/A with reason: source verification is bounded to named current owners; no corpus reassessment occurs.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | internal orchestrator/dispatcher/reviewer |
| Provider or surface | local private-provenance workspace |
| Session or invocation | EACQ-FV-MV2 value gate and dispatch authoring, 2026-08-27 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | governed reads, `rg`, Git, scaffold helper, ADIF resolver, `apply_patch` |
| Target paths | this baseline and paired work order |
| Allowed scope source | operator instruction to continue, 2026-08-27 |
| Before status evidence | clean `22644e47e118bd88bf0d004cb74819fd2956c061` |
| After status evidence | two-path dispatch packet authored; implementation not started |
| Diff evidence | baseline and paired work-order diff before commit |
| Approval boundary | open MV-2 dispatch only; MV-3 and UAA remain parked |
| Claim boundary | no implementation, provider, public, deployment, push, or production claim |
| Agent type | orchestrator/dispatcher/reviewer |
| Invocation ID | `eacq-fv-mv2-dispatch-2026-08-27` |
| Expected manifest | `docs/baselines/CVF_GC018_EACQ_FV_MV2_EXTERNAL_AGENT_TASK_CAPSULE_CONTEXT_2026-08-27.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_EACQ_FV_MV2_EXTERNAL_AGENT_TASK_CAPSULE_CONTEXT_2026-08-27.md` |
| Actual changed set | `docs/baselines/CVF_GC018_EACQ_FV_MV2_EXTERNAL_AGENT_TASK_CAPSULE_CONTEXT_2026-08-27.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_EACQ_FV_MV2_EXTERNAL_AGENT_TASK_CAPSULE_CONTEXT_2026-08-27.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | NONE |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

The dispatch packet is private provenance evidence. Public export is not
authorized.

## Claim Boundary

This baseline opens only bounded no-commit MV-2 implementation. It does not
prove quality improvement, authorize MV-3/UAA, call a provider, refresh or
write the external packet folder, publish, deploy, push, or close MV-2.
