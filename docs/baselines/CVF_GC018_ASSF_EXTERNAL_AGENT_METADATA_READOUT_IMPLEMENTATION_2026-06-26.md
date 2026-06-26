# CVF GC-018 Baseline: ASSF External-Agent Metadata Readout Implementation

Memory class: FULL_RECORD
Status: DISPATCH_READY
Date: 2026-06-26
docType: baseline
Batch ID: ASSF-EAMR-T1
dispatchBaseHead: c2d2ee17

## Decision / Baseline / Proposed Tranche

| Field | Disposition |
|---|---|
| Decision | dispatch a source-verified implementation work order for a read-only external-agent metadata readout |
| Baseline | ASSF external-agent readout / CLI-MCP adapter boundary closed bounded at `99fabd26` |
| Proposed tranche | `ASSF-EAMR-T1` |
| Worker route | Codex single-agent multi-role, material packet first |
| Closure posture | `DISPATCH_READY` |

## Purpose

Authorize a bounded implementation work order that adds a local, read-only
metadata readout for external-agent-facing ASSF package metadata. The readout
must expose only the field families allowed by the boundary contract and must
not claim CLI/MCP adapter availability.

## Scope / Methodology

In scope:

- create a read-only helper under `governance/compat/` that reads the existing
  generated ASSF skill index and emits an allowlisted metadata packet;
- add focused tests proving allowlist shape, claim-boundary language,
  no-instruction-body access, and no filesystem writes;
- produce worker-return and completion-review artifacts.

Out of scope:

- ASSF registry-source mutation;
- ASSF generated-index source mutation;
- resolver mutation;
- package instance creation;
- certification decision or lifecycle mutation;
- CLI/MCP adapter behavior implementation;
- provider/live proof;
- public-sync or push;
- package activation, package instruction execution, or package integration.

## Dependency Release Evidence

| Dependency | Status | Evidence |
|---|---|---|
| Active next move authorizes this packet | SATISFIED | `CVF_SESSION_MEMORY.md` names a fresh GC-018/source-verified work order for read-only external-agent metadata readout implementation |
| Boundary contract exists | SATISFIED | `docs/reference/agent_system_skills/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_CONTRACT.md` |
| ASSF generated metadata source exists | SATISFIED | `docs/reference/agent_system_skills/generated/skill-index.json` |
| Metadata-only resolver pattern exists | SATISFIED | `governance/compat/run_assf_skill_resolver.py` |
| Adapter remains deferred | SATISFIED | generated index `externalCliMcpDisposition` values remain `DEFERRED_WITH_REASON` |

## Evidence / Verification

| Evidence | Result |
|---|---|
| `git rev-parse --short HEAD` | `c2d2ee17` before dispatch authoring |
| `git status --short` | clean worktree before dispatch authoring |
| ADIF resolver API call for work-order authoring/dispatcher/pre-dispatch | returned ADIF-0001, ADIF-0002, ADIF-0007, ADIF-0006 |
| ADIF resolver API call for ASSF external agent metadata readout implementation/dispatcher/pre-dispatch | returned no task-specific entries |

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

## New Implementation Surfaces

These paths are authorized for the worker to create. They are not cited above
as existing source facts.

| Path | Purpose | Boundary |
|---|---|---|
| `governance/compat/run_assf_external_agent_metadata_readout.py` | read-only metadata readout helper | no write, no provider, no adapter availability claim |
| `governance/compat/test_run_assf_external_agent_metadata_readout.py` | focused regression tests | no live/provider proof |

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

Remediation applied: bounded manifests, CVF-governed source facts only,
source-symbol cells without values/types, and explicit claim-boundary rows.

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
| Owner surface | this GC-018 baseline |
| Disposition | no external artifact absorbed |
| Claim boundary | repository-local source and command evidence only |

## Roadmap-To-Work-Order Trace Matrix

| Requirement | Work-order coverage | Planned closure evidence | Disposition |
|---|---|---|---|
| Use boundary contract as authority | Required First Reads and Source Verification Block | worker return | PASS |
| Implement read-only metadata readout | Required Outputs and Execution Plan | helper, tests, completion review | PASS |
| Keep adapter behavior deferred | Dual Agent Surface Matrix and Claim Boundary | completion review | PASS |
| Avoid registry/index/resolver mutation | Forbidden Scope and Write Ownership | git diff evidence | PASS |

## Planned Artifact Manifest

| Artifact | Purpose | Status |
|---|---|---|
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_EXTERNAL_AGENT_METADATA_READOUT_IMPLEMENTATION_FOR_CODEX_2026-06-26.md` | paired implementation work order | PRESENT |
| `governance/compat/run_assf_external_agent_metadata_readout.py` | future helper | PLANNED |
| `governance/compat/test_run_assf_external_agent_metadata_readout.py` | future focused tests | PLANNED |
| `docs/reviews/CVF_ASSF_EXTERNAL_AGENT_METADATA_READOUT_IMPLEMENTATION_WORKER_RETURN_2026-06-26.md` | future worker return | PLANNED |
| `docs/reviews/CVF_ASSF_EXTERNAL_AGENT_METADATA_READOUT_IMPLEMENTATION_COMPLETION_2026-06-26.md` | future reviewer/closure review | PLANNED |

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

Reason: private provenance dispatch packet; no public-sync authorization.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ASSF external-agent metadata readout implementation dispatch baseline |
| claimDisposition | N/A with reason: dispatch authorization only; no implementation claim |
| receiptEvidence | N/A with reason: no runtime receipt is created by this baseline |
| actionEvidence | ACTION_EVIDENCE_PRESENT: source verification and dependency release evidence |
| invocationBoundary | governed local dispatch packet authoring only |
| interceptionBoundary | no provider, adapter, package execution, external MCP, or interception claim |
| claimLanguage | implementation work order authoring only |
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

## Claim Boundary

This baseline authorizes only dispatch of the paired implementation work order.
It does not implement adapter behavior, certify packages, create package
instances, mutate ASSF registry or generated-index sources, mutate resolver
source, run providers, public-sync, push, activate packages, or execute package
instruction bodies.
