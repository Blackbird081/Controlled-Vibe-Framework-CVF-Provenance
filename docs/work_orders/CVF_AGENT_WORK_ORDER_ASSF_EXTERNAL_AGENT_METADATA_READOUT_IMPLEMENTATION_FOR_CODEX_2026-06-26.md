# CVF Agent Work Order: ASSF External-Agent Metadata Readout Implementation

Memory class: FULL_RECORD
Status: DISPATCH_READY
Date: 2026-06-26
docType: work_order
Batch ID: ASSF-EAMR-T1
dispatchBaseHead: c2d2ee17
executionBaseHead: c2d2ee17
closureBaseHead: c2d2ee17
Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: Codex single-agent multi-role worker/reviewer/closer for a bounded
read-only ASSF external-agent metadata readout implementation tranche.

executionBaseHead: `c2d2ee17`

Required first actions: read the paired GC-018 baseline, read all Required
First Reads, run the pre-flight checks, and stop before any forbidden adapter,
provider, package, public-sync, registry, generated-index, resolver, lifecycle,
or session mutation.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_EXTERNAL_AGENT_METADATA_READOUT_IMPLEMENTATION_FOR_CODEX_2026-06-26.md`

Paired GC-018 baseline:
`docs/baselines/CVF_GC018_ASSF_EXTERNAL_AGENT_METADATA_READOUT_IMPLEMENTATION_2026-06-26.md`

Commit mode: `WORKER_MUST_NOT_COMMIT` for worker execution. Codex may later
review, repair allowed-scope defects, close, and commit as reviewer/closer only
once worker-return and gates pass.

Current-time notes: active handoff is `AGENT_HANDOFF_V23_2026-06-26.md`;
current HEAD before dispatch authoring is `c2d2ee17`; this packet authorizes
implementation work-order dispatch only, not implementation before this packet
is committed.

Do-not-misread notes: implementation means a local read-only metadata readout
helper plus focused tests inside Write Ownership only. It is not CLI/MCP
adapter behavior, provider proof, package activation, package execution,
certification, registry/index/resolver mutation, public-sync, push, or
session-sync.

Return contract: produce a worker return and completion review. Return
`BLOCKED_WITH_REASON` if implementation requires forbidden mutation or cannot
preserve the claim boundary.

## Purpose

Implement a local read-only ASSF metadata readout helper for external-agent
planning surfaces. The helper must expose only allowlisted metadata from the
existing generated ASSF skill index and must make the no-adapter boundary
visible in both human and JSON output.

## Scope / Target / Owner Boundary

Target: governance compatibility helper, focused tests, worker return, and
completion review for a read-only external-agent metadata readout.

Owner boundary: the worker may edit only the Write Ownership paths in this work
order. The worker must not mutate ASSF registry source, ASSF generated-index
source, resolver source, package roots, lifecycle state, certification state,
adapter surfaces, provider/live proof surfaces, public-sync surfaces, or
session surfaces in the material execution commit.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator next move | continue by opening read-only external-agent metadata readout implementation GC-018/work order | ACCEPT |
| Active front door | `CVF_SESSION_MEMORY.md` | ACCEPT |
| Bootstrap read model | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | ACCEPT |
| Active state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V23_2026-06-26.md` | ACCEPT |
| Paired GC-018 baseline | `docs/baselines/CVF_GC018_ASSF_EXTERNAL_AGENT_METADATA_READOUT_IMPLEMENTATION_2026-06-26.md` | ACCEPT |
| Boundary contract | `docs/reference/agent_system_skills/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_CONTRACT.md` | ACCEPT |
| ASSF package contract | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | ACCEPT |
| Existing ASSF resolver | `governance/compat/run_assf_skill_resolver.py` | ACCEPT |

## Agent Roles

| Role | Owner |
|---|---|
| Operator | approves next-move lane and later scope expansion |
| Dispatcher | Codex |
| Worker | Codex, no commit during worker execution |
| Reviewer | Codex once worker return exists |
| Closer | Codex once reviewer acceptance is recorded |
| Session-sync steward | Codex in a separate commit if next move changes |

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | active next allowed move from ASSF external-agent boundary closure |
| Scope classification | bounded read-only metadata readout implementation work order |
| Intake role | Codex dispatches; Codex worker executes without commit |
| Reviewer role | Codex reviewer/closer validates worker return, gates, changed paths, and boundaries |
| Routing decision | `WORKER_MUST_NOT_COMMIT`; single-agent multi-role with reviewer closure conversion |
| Public route | `DEFERRED_PRIVATE_ONLY`; no public-sync |
| canonical route mode | `SINGLE_AGENT_MULTI_ROLE` |
| selected role route | Codex dispatch author to Codex no-commit worker to Codex reviewer/closer |
| escalation condition | stop and return `BLOCKED_WITH_REASON` if implementation requires ASSF registry/index/resolver mutation, package lifecycle mutation, certification decision, adapter behavior, provider/live proof, public-sync, push, package activation, or package execution |

## Required First Reads

| Source | Action | Reason |
|---|---|---|
| `CVF_SESSION_MEMORY.md` | READ | active front door |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | READ | compact startup facts |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | READ | active state registry |
| `AGENT_HANDOFF_V23_2026-06-26.md` | READ | active handoff |
| `docs/reference/guard_orientation/README.md` | READ | role and guard orientation |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ | literal-format checklist |
| `docs/baselines/CVF_GC018_ASSF_EXTERNAL_AGENT_METADATA_READOUT_IMPLEMENTATION_2026-06-26.md` | READ | paired authorization baseline |
| `docs/reference/agent_system_skills/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_CONTRACT.md` | SOURCE_VERIFIED | canonical readout boundary |
| `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | SOURCE_VERIFIED | ASSF external adapter fields |
| `docs/reference/agent_system_skills/generated/skill-index.json` | SOURCE_VERIFIED | metadata source |
| `governance/compat/run_assf_skill_resolver.py` | SOURCE_VERIFIED | read-only resolver pattern |
| `governance/compat/generate_assf_skill_index.py` | SOURCE_VERIFIED | generated-index drift helper |
| `governance/compat/check_assf_certified_metadata_admission.py` | SOURCE_VERIFIED | adapter-evidence admission boundary |

## Pre-Flight Checks

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/check_assf_skill_index_drift.py
python governance/compat/check_assf_certified_metadata_admission.py --require-certified
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base c2d2ee17 --head HEAD
```

## Worker Return Packet Shape Contract

The worker-return artifact must be scaffold-first and must retain or complete
the sections listed below so reviewer-fast and pre-closure gates can diagnose
issues before material commit:

- `Status`
- `dispatchWorkOrder`
- `Purpose`
- `Source Inventory`
- `Scope / Methodology`
- `Findings / Position`
- `Risk / Corrective Action`
- `Decision / Recommendation`
- `Claim Boundary`
- `Source Verification Block`
- `Agent Operation Trace Block`
- `Delta Execution Claim Boundary Control Block`
- `Public Export Disposition`
- `External Knowledge Intake Routing`
- `Rescan Intelligence Hardening`
- `Corpus Completeness And Report Integrity`
- `Finding-To-Governance Learning Disposition`
- `Epistemic Process Block`
- `Worker Return Scaffold Effectiveness Measurement`
- `Machine Closure Package`
- `Acceptance Receipt Assertion Matrix`
- actual `executionBaseHead`
- actual `git status --short`
- `Actual changed set` listing real paths
- command evidence
- no commit statement

If a conditional section is not applicable, include the section with
`N/A with reason` or `NOT_APPLICABLE_WITH_REASON` and a short reason instead
of omitting it. The worker return must include
`receiptEvidence: CVF_RECEIPT_PRESENT - ...` when execution produced local
command or diff evidence.

## Worker Autonomy / No-Question Rule

Within Allowed scope, the worker must repair machine-check, source-inventory,
packet-shape, focused-command, worker-return fast-gate, and allowed test
failures and rerun the required checks without asking the operator. Ask the
operator only if remediation would exceed Allowed scope, change the claim
boundary, require ASSF registry/generated-index/resolver mutation, package
instance creation, lifecycle mutation, certification decision, CLI/MCP adapter
behavior, provider/live proof, public-sync, push, destructive action, or a
separate roadmap batch.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| Boundary contract defines the readout field allowlist | `docs/reference/agent_system_skills/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_CONTRACT.md` | lines 26-36 | `Readout Field Allowlist` | ASSF external-agent boundary contract | VALUE_SET | ACCEPT |
| Boundary contract keeps adapter admission separate from readout | `docs/reference/agent_system_skills/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_CONTRACT.md` | lines 47-61 | `Adapter Admission Boundary` | ASSF external-agent boundary contract | LITERAL_INVARIANT | ACCEPT |
| Package contract defines external adapter fields | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | lines 133-141 | `externalCliMcpDisposition` | ASSF package contract | EXISTS | ACCEPT |
| Generated ASSF index is metadata-only | `docs/reference/agent_system_skills/generated/skill-index.json` | line 2 | `claimBoundary` | ASSF generated skill index | LITERAL_INVARIANT | ACCEPT |
| Generated ASSF index carries adapter posture fields | `docs/reference/agent_system_skills/generated/skill-index.json` | lines 9-25 and 98-114 | `externalCliMcpDisposition` | ASSF generated skill index | VALUE_SET | ACCEPT |
| Existing ASSF resolver has read-only metadata packet shape | `governance/compat/run_assf_skill_resolver.py` | lines 78-103 | `SkillPacket` | ASSF resolver | EXISTS | ACCEPT |
| Existing ASSF resolver loads generated entries without mutation | `governance/compat/run_assf_skill_resolver.py` | lines 150-165 | `load_entries` | ASSF resolver | RUNTIME_BEHAVIOR | ACCEPT |
| Existing ASSF resolver has a CLI entrypoint pattern | `governance/compat/run_assf_skill_resolver.py` | line 265 | `main` | ASSF resolver CLI | EXISTS | ACCEPT |
| Generated-index helper can validate source drift | `governance/compat/generate_assf_skill_index.py` | lines 107-137 | `validate_index_matches_sources` | ASSF generated-index helper | RUNTIME_BEHAVIOR | ACCEPT |
| Certified metadata admission checker blocks implemented adapter claims without evidence | `governance/compat/check_assf_certified_metadata_admission.py` | lines 145-164 | `adapterEvidence` | certified metadata admission checker | RUNTIME_BEHAVIOR | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

API invocation used: `resolve_defect_packet(task_class="Work-order authoring / dispatch", role="dispatcher", lifecycle_phase="pre-dispatch")`

Returned defects:

- ADIF-0001: Exhaustive directory claim omits actual children
- ADIF-0002: Provider-local interaction accepted as authority
- ADIF-0007: Gate marker in boundary prose triggers wrong evidence class
- ADIF-0006: Source Verification symbol cell contains a value/type

Task-specific resolver query: taskClass=`ASSF external agent metadata readout implementation`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Task-specific returned defects:

- N/A with reason: resolver returned no task-specific entries.

Remediation applied: use bounded manifests, CVF-governed/runtime sources only,
source symbols without value/type assignments, and explicit control blocks for
boundary language.

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | Codex dispatches, executes no-commit worker implementation, reviews, and closes if evidence supports closure |
| phase | DISPATCH_AUTHORING; IMPLEMENTATION; REVIEWER_CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=c2d2ee17`; `executionBaseHead=c2d2ee17`; closure base recorded in completion review |
| changedSetScope(phase) | dispatch packet first; later implementation/review paths only; session-sync separate |
| traceScope(phase, actor) | worker return and completion review record Agent Operation Trace Block |
| commitOwner(phase) | Codex reviewer/closer owns material commit once worker return passes gates |
| crossBatchIsolation | no ASSF registry/index/resolver, package, adapter, provider, public-sync, or session-sync mutation in worker material commit |
| Before status evidence | dispatchBaseHead `c2d2ee17`; `git status --short` (empty) before dispatch authoring |
| nextMoveSurfaces | updated only in a separate session-sync commit paired to the accepted material commit |
| Closer designation | Codex reviewer/closer |

## Single-Agent Multi-Role Control Block

| Field | Control |
|---|---|
| Role separation ledger | dispatch packet, worker return, completion review, material commit, and session-sync are separate steps |
| Evidence basis | source verification, focused helper tests, read-only proof, pre-closure gates, commit steward preflight |
| Self-review boundary | Codex may review its own worker return only against this work order and machine gates |
| Gate sequence | pre-dispatch for packet, pre-implementation for worker start, reviewer-fast/pre-closure for closure, session-sync gates only in the dedicated session-sync phase |
| Escalation conditions | any required ASSF registry/index/resolver mutation, package lifecycle mutation, adapter behavior, provider/live proof, public-sync, or push |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| workerReturnPath | `docs/reviews/CVF_ASSF_EXTERNAL_AGENT_METADATA_READOUT_IMPLEMENTATION_WORKER_RETURN_2026-06-26.md` |
| completionReviewPath | `docs/reviews/CVF_ASSF_EXTERNAL_AGENT_METADATA_READOUT_IMPLEMENTATION_COMPLETION_2026-06-26.md` |
| reviewerOwnedClosurePaths | worker return, completion review, and allowed implementation paths listed in Write Ownership |
| workerReturnStatus | `COMPLETE_PENDING_REVIEW` expected |
| closer | Codex |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | local governance/compat readout helper | internal agents may read allowlisted metadata only; no package activation or mutation | boundary contract and generated index | no adapter behavior is implemented | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future adapter may consume the readout after separate authorization | no external mutation, certification, activation, package execution, provider call, commit, push, or public claim | dual-agent standard and boundary contract | adapter remains deferred; this tranche is metadata readout only | `DEFERRED_WITH_REASON` |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator next-move direction to continue the ASSF external-agent metadata readout lane |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this work order |
| Disposition | no external material absorbed |
| Claim boundary | repository-local source and command evidence only |

## Roadmap-To-Work-Order Trace Matrix

| Requirement | Work-order instruction | Expected closure evidence | Disposition |
|---|---|---|---|
| Use boundary contract as authority | Required First Reads and Source Verification Block | worker return Source Verification Block | PASS |
| Implement read-only metadata readout | Required Outputs and Execution Plan | helper and tests | PASS |
| Keep adapter behavior deferred | Dual Agent Surface Matrix and Claim Boundary | completion review | PASS |
| Avoid registry/index/resolver mutation | Forbidden Scope and Write Ownership | `git diff --name-status` evidence | PASS |

## Execution Plan

1. Confirm startup sources, paired GC-018 baseline, boundary contract, and ASSF
   generated metadata source.
2. Add `run_assf_external_agent_metadata_readout.py` as a read-only helper that
   loads the existing generated index and emits only allowlisted metadata plus
   explicit no-adapter claim-boundary fields.
3. Add focused tests proving allowlist shape, JSON/human output, no writes, no
   package instruction body access, and no mutation of ASSF registry/index or
   resolver files.
4. Run focused tests and required governance gates.
5. Author worker return and completion review without committing as worker.
6. Reviewer/closer validates changed set and commits material closure only if
   gates pass.

## Required Outputs

| Output | Required path | Disposition |
|---|---|---|
| Readout helper | `governance/compat/run_assf_external_agent_metadata_readout.py` | CREATE |
| Focused tests | `governance/compat/test_run_assf_external_agent_metadata_readout.py` | CREATE |
| Worker return | `docs/reviews/CVF_ASSF_EXTERNAL_AGENT_METADATA_READOUT_IMPLEMENTATION_WORKER_RETURN_2026-06-26.md` | CREATE |
| Completion review | `docs/reviews/CVF_ASSF_EXTERNAL_AGENT_METADATA_READOUT_IMPLEMENTATION_COMPLETION_2026-06-26.md` | CREATE |

## Write Ownership

Allowed paths:

- `governance/compat/run_assf_external_agent_metadata_readout.py`
- `governance/compat/test_run_assf_external_agent_metadata_readout.py`
- `docs/reviews/CVF_ASSF_EXTERNAL_AGENT_METADATA_READOUT_IMPLEMENTATION_WORKER_RETURN_2026-06-26.md`
- `docs/reviews/CVF_ASSF_EXTERNAL_AGENT_METADATA_READOUT_IMPLEMENTATION_COMPLETION_2026-06-26.md`

Forbidden paths:

- `docs/reference/agent_system_skills/registry/entries/**`
- `docs/reference/agent_system_skills/generated/skill-index.json`
- `governance/compat/generate_assf_skill_index.py`
- `governance/compat/run_assf_skill_resolver.py`
- package roots or package instances;
- `CVF_SESSION/**`, `CVF_SESSION_MEMORY.md`, and `AGENT_HANDOFF_*.md` during material execution;
- public-sync repository or push surfaces.

## Forbidden Path Manifest

| Path | Disposition |
|---|---|
| `CVF_SESSION_MEMORY.md` | FORBIDDEN for material execution; read-only startup source only |
| `CVF_SESSION/**` | FORBIDDEN for material execution; session-sync separate |
| `AGENT_HANDOFF_*.md` | FORBIDDEN for material execution; session-sync separate |
| `docs/reference/agent_system_skills/registry/entries/**` | FORBIDDEN |
| `docs/reference/agent_system_skills/generated/skill-index.json` | FORBIDDEN |
| `governance/compat/generate_assf_skill_index.py` | FORBIDDEN; source-verified read only |
| `governance/compat/run_assf_skill_resolver.py` | FORBIDDEN; source-verified read only |

## Work-Order Fulfillment Manifest

| Required artifact | Required status | Forbidden substitute |
|---|---|---|
| `governance/compat/run_assf_external_agent_metadata_readout.py` | present and tested | changing `run_assf_skill_resolver.py` |
| `governance/compat/test_run_assf_external_agent_metadata_readout.py` | focused tests pass | broad unrelated test rewrites |
| worker return | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` | handwritten chat-only status |
| completion review | reviewer-owned closure artifact | session-sync commit |

## Evidence Requirements

| Evidence item | Required form | Owner |
|---|---|---|
| Read-only helper proof | focused unittest assertions and code review | worker then reviewer |
| Allowlist proof | test comparing emitted keys to boundary allowlist | worker then reviewer |
| No instruction body access | test guarding package body paths or `SKILL.md` opens | worker then reviewer |
| No mutation proof | `git diff --name-status`, write-guard test, and forbidden-path review | reviewer |
| Gate proof | command outputs listed in Verification Commands | worker then reviewer |

## Review Gate

Reviewer must reject closure unless:

- all changed paths are inside Write Ownership;
- Source Verification rows remain current;
- helper output preserves the no-adapter claim boundary;
- focused tests pass;
- worker return fast gate, pre-closure autorun, commit steward preflight, and
  `git diff --check` pass.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only after all Required Outputs exist, focused
tests pass, and the worker-return fast gate is compliant. Return
`BLOCKED_WITH_REASON` if the readout requires any forbidden mutation or cannot
preserve the allowlist and no-adapter boundary.

## Operator Checkpoint

Operator checkpoint is required before any expansion into CLI/MCP adapter
availability, provider/live proof, public-sync, package activation, package
execution, package instance creation, certification decision, lifecycle
mutation, ASSF registry/generated-index source mutation, or resolver mutation.

## Closure Checklist

| Item | Required disposition |
|---|---|
| Write Ownership respected | PASS or BLOCKED with reason |
| Readout allowlist preserved | PASS or BLOCKED with reason |
| No adapter behavior claim | PASS or BLOCKED with reason |
| Focused tests pass | PASS or BLOCKED with reason |
| Worker return fast gate pass | PASS or BLOCKED with reason |
| Pre-closure gates pass | PASS or BLOCKED with reason |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Durable governance foundation file change | CREATE two bounded `governance/compat/` helper/test files |
| Source layout | helper and focused test live beside existing ASSF resolver and tests |
| Index/layout mutation | N/A with reason: no registry, generated index, resolver, hook, or catalog mutation is authorized |
| Split/refactor posture | N/A with reason: this tranche creates a narrow helper rather than splitting an existing file |
| Storage claim boundary | local governance compatibility helper only; not package storage, adapter storage, queue, runtime state, or public surface |

## Verification Commands

Required before worker return:

```powershell
python -m unittest governance.compat.test_run_assf_external_agent_metadata_readout
python governance/compat/check_assf_skill_index_drift.py
python governance/compat/check_assf_certified_metadata_admission.py --require-certified
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git status --short
```

Required before material closure commit:

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base c2d2ee17 --head HEAD
python governance/compat/run_agent_commit_steward_preflight.py --mode closure --base c2d2ee17 --head HEAD --enforce
git diff --check
```

## Acceptance Criteria

| Criterion | Required evidence |
|---|---|
| AC1 | Helper emits only allowlisted readout fields plus claim-boundary metadata |
| AC2 | Helper is read-only and does not open package instruction bodies |
| AC3 | Helper does not mutate ASSF registry source, generated index, resolver, lifecycle state, or package roots |
| AC4 | CLI/json output states no adapter behavior is implemented |
| AC5 | Focused tests and governance gates pass |

## Fail Conditions

Return `BLOCKED_WITH_REASON` if:

- implementation requires editing ASSF registry source, generated index source,
  resolver source, package roots, lifecycle state, or certification state;
- readout cannot be bounded to the allowlist;
- helper would imply CLI/MCP adapter availability;
- focused tests require provider/live proof;
- governance gates fail outside the allowed packet scope.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance work order; no public-sync authorization.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ASSF external-agent metadata readout implementation work-order dispatch |
| claimDisposition | N/A with reason: dispatch authorization only; no implementation claim |
| receiptEvidence | N/A with reason: no runtime receipt is created by this work order |
| actionEvidence | ACTION_EVIDENCE_PRESENT: source verification, write ownership, and verification commands |
| invocationBoundary | governed local dispatch packet authoring only |
| interceptionBoundary | no provider, adapter, package execution, external MCP, or interception claim |
| claimLanguage | implementation instructions only |
| forbiddenExpansion | package instance, certification decision, lifecycle mutation, ASSF registry-source mutation, ASSF generated-index source mutation, resolver mutation, CLI/MCP adapter behavior, provider/live proof, public-sync, push, activation, and package instruction execution remain out of scope |

## Current Runtime Freshness Verification

| Runtime claim | Verification command or source | Observed value | Disposition |
|---|---|---|---|
| ASSF metadata source exists | `docs/reference/agent_system_skills/generated/skill-index.json` | metadata-only claim boundary and skill entries present | PASS |
| Existing resolver is read-only | `governance/compat/run_assf_skill_resolver.py` | load/resolve packet functions read generated index and return dict payload | PASS |
| Adapter is not implemented by this dispatch | boundary contract and generated adapter posture fields | adapter disposition remains deferred | PASS |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: bounded creation of a new read-only ASSF
metadata readout helper and focused tests under `governance/compat/`.

Protected paths:

- create `governance/compat/run_assf_external_agent_metadata_readout.py`;
- create `governance/compat/test_run_assf_external_agent_metadata_readout.py`.

Reason: bounded read-only governance helper implementation and focused tests
for this ASSF metadata readout tranche. No existing checker, resolver,
generator, hook, registry, generated index, or runtime adapter may be mutated.

Operator authorization: operator instructed Codex to continue according to the
current roadmap after adding the small finding to the checklist; active next
allowed move authorizes a fresh GC-018/source-verified work order for this
read-only metadata readout implementation.

Rollback boundary: delete the newly created helper/test and reviewer artifacts;
do not revert prior ASSF package, Web projection, boundary contract, or session
continuity commits.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatcher |
| Provider or surface | local repository tools |
| Session or invocation | ASSF-EAMR-T1 dispatch authoring, 2026-06-26 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, apply_patch, Python gates |
| Target paths | paired GC-018 baseline and this work order |
| Allowed scope source | active next allowed move after session-sync commit `c2d2ee17` |
| Before status evidence | baseHead `c2d2ee17`; `git status --short` (empty) before dispatch authoring |
| After status evidence | pre-dispatch gates and commit steward preflight before dispatch commit |
| Diff evidence | `git diff --name-status` against baseHead `c2d2ee17` |
| Approval boundary | dispatch packet only |
| Claim boundary | no implementation, adapter behavior, provider/live proof, public-sync, ASSF registry/generated-index source mutation, resolver mutation, package activation, or package execution |
| Agent type | dispatcher |
| Invocation ID | ASSF-EAMR-T1-dispatch-2026-06-26 |
| Expected manifest | `docs/baselines/CVF_GC018_ASSF_EXTERNAL_AGENT_METADATA_READOUT_IMPLEMENTATION_2026-06-26.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_EXTERNAL_AGENT_METADATA_READOUT_IMPLEMENTATION_FOR_CODEX_2026-06-26.md` |
| Actual changed set | `docs/baselines/CVF_GC018_ASSF_EXTERNAL_AGENT_METADATA_READOUT_IMPLEMENTATION_2026-06-26.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_EXTERNAL_AGENT_METADATA_READOUT_IMPLEMENTATION_FOR_CODEX_2026-06-26.md` |
| Manifest delta | MATCH |

## Claim Boundary

This work order dispatches only the bounded local metadata readout
implementation. It does not authorize adapter behavior, provider/live proof,
public-sync, push, package activation, package execution, package integration,
certification decision, lifecycle mutation, ASSF registry-source mutation,
ASSF generated-index source mutation, or resolver mutation.
