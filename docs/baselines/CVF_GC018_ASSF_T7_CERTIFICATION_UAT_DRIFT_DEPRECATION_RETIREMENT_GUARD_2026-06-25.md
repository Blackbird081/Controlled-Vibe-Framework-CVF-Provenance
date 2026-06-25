# CVF GC-018 Baseline: ASSF-T7 Certification UAT Drift Deprecation Retirement Guard

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-25

docType: baseline

Batch ID: ASSF-T7

## Proposed Tranche

Tranche: ASSF-T7

Baseline decision: documentation-only guard foundation tranche to define the
certification, UAT, drift, deprecation, successor, retirement, duplicate-ID,
and adapter-claim control model for CVF agent system-skill packages. This
tranche must not implement a runtime checker, resolver mutation, generated
index mutation, package activation path, Web projection change, CLI/MCP
adapter, provider call, live proof, public-sync, or session-sync edit.

Verdicts:

- Dispatcher verdict: DISPATCH_APPROVED
- Worker verdict: COMPLETE_PENDING_REVIEW_ACCEPTED
- Reviewer verdict: CLOSED_PASS_BOUNDED

## Purpose

ASSF-T7 converts the lifecycle risks discovered across ASSF-T1 through
ASSF-T6 into a compact guard contract that later agents and checkers can
reuse. Success means a reviewer can decide when a skill package is still a
candidate, when it has enough UAT and certification evidence to advance, when
it must be held for drift, and when Web or external-agent surfaces are making
claims that outrun canonical package evidence.

## Evidence / Verification

Closure evidence includes source verification, dependency release evidence,
ADIF disclosure, Dual Agent Surface Matrix, worker artifact paths, the matching
ASSF-T7 work order, the worker-return packet, reviewer gate evidence, and the
completion review. Worker-created contract and worker return artifacts were
reviewed by Codex and accepted as bounded documentation-only closure.

## Roadmap-to-Work-Order Trace Matrix

| Roadmap requirement | Dispatch artifact | Worker obligation | Evidence required |
|---|---|---|---|
| ASSF-T7 must check package/index consistency | this baseline; matching ASSF-T7 work order | define consistency rules for package contract fields, generated index metadata, and resolver behavior | source-verified contract rows and worker return evidence |
| ASSF-T7 must address dangling sources and invalid selectors | this baseline; matching ASSF-T7 work order | define drift classes for missing source artifacts, invalid selector values, and stale package metadata | guard contract section plus source verification |
| ASSF-T7 must block dishonest enforcement or adapter claims | this baseline; matching ASSF-T7 work order | define adapter-claim honesty rules for `externalCliMcpDisposition`, `adapterContract`, `adapterEvidence`, and `externalMutationBoundary` | Dual Agent Surface Matrix and claim-boundary table |
| ASSF-T7 must address duplicate IDs, stale successors, missing UAT, and lifecycle violations | this baseline; matching ASSF-T7 work order | define lifecycle violation taxonomy and hold/reject dispositions | lifecycle guard table and reviewer decision requirements |
| ASSF-T7 must integrate machine gates only after stable repeated use | this baseline; matching ASSF-T7 work order | mark machine checks as candidates only unless existing source already implements them | no checker implementation in worker changed set |
| T7 must cite T1, T2, T5, and T6 foundations | this baseline; matching ASSF-T7 work order | cite package contract, generated index/resolver, composition contract, Web projection contract, and T6 migration audit | Source Verification Block |

## Scope / Applies To

Applies to:

- future package certification and UAT review;
- future generated index and resolver drift checks;
- future deprecation, successor, retirement, duplicate-ID, and stale-claim
  detection;
- future Web projection promotion from `PACKAGE_CANDIDATE` to
  `CERTIFIED_PACKAGE_PROJECTION`;
- future internal-agent and external-agent CLI/MCP skill package consumers.

Does not apply to:

- implementing a Python checker or local hook;
- changing `docs/reference/agent_system_skills/generated/skill-index.json`;
- changing `governance/compat/run_assf_skill_resolver.py`;
- creating package instances, `SKILL.md`, or `skill.source.json`;
- changing CVF Web runtime source or Web projection data;
- implementing an external CLI/MCP adapter;
- using provider secrets, live proof, public-sync, push, or session state.

## Dependency Release Evidence

| Dependency | Status | Evidence |
|---|---|---|
| ASSF-T1 Canonical Package Contract | CLOSED_PASS_BOUNDED | `docs/reviews/CVF_ASSF_T1_CANONICAL_PACKAGE_CONTRACT_COMPLETION_2026-06-23.md`; material commit `2752d04e` |
| ASSF-T2 Generated Index And Progressive Resolver | CLOSED_PASS_BOUNDED | `docs/reviews/CVF_ASSF_T2_GENERATED_INDEX_AND_PROGRESSIVE_RESOLVER_COMPLETION_2026-06-23.md`; material commit `3746bd48` |
| ASSF-T5 Composition, Dependency, Conflict, And Capability Controls | CLOSED_PASS_BOUNDED | `docs/reviews/CVF_ASSF_T5_COMPOSITION_DEPENDENCY_CONFLICT_CAPABILITY_CONTROLS_COMPLETION_2026-06-25.md`; material commit `afeb2673`; reviewer repair commit `d0a24e90` |
| ASSF-T6 CVF Web Projection And Existing Example Migration | CLOSED_PASS_BOUNDED | `docs/reviews/CVF_ASSF_T6_CVF_WEB_PROJECTION_EXISTING_EXAMPLE_MIGRATION_COMPLETION_2026-06-25.md`; material commit `489ff38a`; Codex final-review addendum commit `b31b4aca` |
| ADIF authoring hardening | CLOSED_PASS_BOUNDED | material commit `8afbe0aa`; active session sync at `eb269c4c` |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | ASSF package lifecycle guard contract under `docs/reference/agent_system_skills/` | T7 may define certification, UAT, drift, deprecation, successor, retirement, duplicate-ID, and adapter-claim rules; it must not activate packages or mutate resolver/index behavior | ASSF roadmap T7 section, T1 package contract, T2 generated index and resolver, T5 composition contract, T6 Web projection contract and migration audit | no internal checker, loader, resolver, hook, or generated-index change is authorized in this tranche | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future external-agent package readout or adapter certification claim | T7 must define honesty rules for external disposition and adapter evidence; external agents cannot certify, mutate, activate, or execute packages through this tranche | Dual Agent Surface Accounting Standard; T1 external disposition fields; T6 projection boundary | any implemented CLI/MCP adapter requires a later source-verified adapter contract, tests, and public/private boundary review | `DEFERRED_WITH_REASON` |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| ASSF roadmap authorizes T7 Certification UAT Drift Deprecation Retirement Guard | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | ASSF-T7 section | `ASSF-T7` | ASSF roadmap | EXISTS | ACCEPT |
| Roadmap requires T7 to check package/index consistency and lifecycle violations | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | ASSF-T7 section | `missing UAT` | ASSF roadmap | LITERAL_INVARIANT | ACCEPT |
| Roadmap requires future T7 packet to cite T1, T2, T5, and T6 foundations | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | Machine Closure Package notes | `ASSF-T7 packet` | ASSF roadmap | LITERAL_INVARIANT | ACCEPT |
| T1 package contract defines lifecycle fields | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Compact Machine Source Schema | `certificationState` | ASSF-T1 package schema | EXISTS | ACCEPT |
| T1 package contract defines UAT field | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Compact Machine Source Schema | `uatState` | ASSF-T1 package schema | EXISTS | ACCEPT |
| T1 package contract defines deprecation and retirement fields | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Compact Machine Source Schema | `retirement` | ASSF-T1 package schema | EXISTS | ACCEPT |
| T1 package contract defines lifecycle status vocabulary | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Lifecycle State Vocabulary | `ACTIVE` | ASSF-T1 package schema | VALUE_SET | ACCEPT |
| T1 package contract defines external CLI/MCP disposition fields | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Internal-Agent And External-Agent CLI/MCP Disposition Fields | `externalCliMcpDisposition` | ASSF-T1 package schema | EXISTS | ACCEPT |
| T2 generated index is metadata-only and not activation evidence | `docs/reference/agent_system_skills/generated/skill-index.json` | claimBoundary | `claimBoundary` | ASSF-T2 generated index | LITERAL_INVARIANT | ACCEPT |
| Current generated index records unstarted certification states | `docs/reference/agent_system_skills/generated/skill-index.json` | skill entries | `certificationState` | ASSF-T2 generated index | VALUE_SET | ACCEPT |
| T2 resolver excludes retired and rejected skills by default | `governance/compat/run_assf_skill_resolver.py` | `_EXCLUDED_STATUSES` | `_EXCLUDED_STATUSES` | ASSF-T2 resolver | VALUE_SET | ACCEPT |
| T2 resolver exposes read-only skill packet resolution | `governance/compat/run_assf_skill_resolver.py` | `resolve_skill_packet` | `resolve_skill_packet` | ASSF-T2 resolver | EXISTS | ACCEPT |
| T5 composition contract forbids automatic package promotion | `docs/reference/agent_system_skills/CVF_ASSF_COMPOSITION_CONTROL_CONTRACT.md` | No-Automatic-Promotion Invariant | `No-Automatic-Promotion Invariant` | ASSF-T5 composition contract | LITERAL_INVARIANT | ACCEPT |
| T5 composition contract restricts package graph lifecycle states | `docs/reference/agent_system_skills/CVF_ASSF_COMPOSITION_CONTROL_CONTRACT.md` | Package Graph Boundary | `Package Graph Boundary` | ASSF-T5 composition contract | LITERAL_INVARIANT | ACCEPT |
| T6 Web projection contract defines certified projection token | `docs/reference/agent_system_skills/CVF_ASSF_WEB_PROJECTION_CONTRACT.md` | Projection Classification Vocabulary | `CERTIFIED_PACKAGE_PROJECTION` | ASSF-T6 Web projection contract | VALUE_SET | ACCEPT |
| T6 migration audit found no certified Web projections | `docs/audits/CVF_ASSF_T6_EXISTING_WEB_SKILL_EXAMPLE_MIGRATION_AUDIT_2026-06-25.md` | Classification Summary | `CERTIFIED_PACKAGE_PROJECTION` | ASSF-T6 migration audit | VALUE_SET | ACCEPT |
| T6 migration audit escalated Web certification schema gap to T7 | `docs/audits/CVF_ASSF_T6_EXISTING_WEB_SKILL_EXAMPLE_MIGRATION_AUDIT_2026-06-25.md` | Next Action | `certificationState` | ASSF-T6 migration audit | LITERAL_INVARIANT | ACCEPT |
| Dual Agent standard requires external-agent disposition and adapter boundary | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | Mandatory Dual Agent Surface Matrix | `EXTERNAL_AGENT_CLI_MCP` | Dual Agent Surface Accounting Standard | VALUE_SET | ACCEPT |
| Governed artifact literal-format gotchas checklist exists | `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | Purpose | `CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | Governed Artifact Literal Format Gotchas | EXISTS | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects:

- ADIF-0001: Exhaustive directory claim omits actual children
- ADIF-0002: Provider-local interaction accepted as authority
- ADIF-0006: Source Verification symbol cell contains a value/type
- ADIF-0007: Gate keyword in exclusion prose triggers wrong evidence class

Remediation applied:

- ADIF-0001: This baseline does not claim exhaustive package or Web coverage;
  the worker must cite exact search roots and observed files only.
- ADIF-0002: ACCEPT rows cite CVF-governed docs or repository source files.
- ADIF-0006: Verified path or symbol cells contain only field, function,
  section, or token names.
- ADIF-0007: Evidence rows use concrete source facts instead of exclusion
  keyword prose.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external-agent packet request |
| Chain map route | operator request to governed work-order/source-verification/autorun lane |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this GC-018 baseline and the matching ASSF-T7 work order |
| Disposition | local contract dispatch only; no external material is absorbed |
| Claim boundary | no external-agent packet, adapter behavior, public claim, or provider proof is accepted as source authority |

## Required Worker Deliverables

| Path | Required at worker return | Purpose |
|---|---|---|
| `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | Yes | T7 certification, UAT, drift, deprecation, successor, retirement, duplicate-ID, and adapter-claim guard contract |
| `docs/reviews/CVF_ASSF_T7_CERTIFICATION_UAT_DRIFT_DEPRECATION_RETIREMENT_GUARD_WORKER_RETURN_2026-06-25.md` | Yes | Worker return with evidence, changed files, gate receipts, and remaining review boundary |

## Reviewer-Owned Closure Deliverables

| Path | Owner | Purpose |
|---|---|---|
| `docs/reviews/CVF_ASSF_T7_CERTIFICATION_UAT_DRIFT_DEPRECATION_RETIREMENT_GUARD_COMPLETION_2026-06-25.md` | Codex reviewer/closer | Completion review after worker return |
| this baseline | Codex reviewer/closer | Final status conversion after review |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_T7_CERTIFICATION_UAT_DRIFT_DEPRECATION_RETIREMENT_GUARD_FOR_CLAUDE_2026-06-25.md` | Codex reviewer/closer | Final status conversion after review |
| `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | Codex reviewer/closer | T7 closure rows only after review passes |
| active session front door and active handoff | Codex session-sync steward | Session continuity after material commit |

## Dispatch Readiness Package

| Readiness item | Required artifact/path | Evidence | Status |
|---|---|---|---|
| Roadmap source | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | ASSF-T7 section exists | PASS |
| GC-018 status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_T7_CERTIFICATION_UAT_DRIFT_DEPRECATION_RETIREMENT_GUARD_FOR_CLAUDE_2026-06-25.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Worker output paths | this file | Required Worker Deliverables table | PASS |
| External adapter boundary | this file | Dual Agent Surface Matrix | PASS |
| Runtime implementation | N/A with reason | runtime implementation is forbidden in this tranche | N/A with reason |

## Planned Output Filesystem State At Dispatch

| Path | Dispatch-time state | Required worker action |
|---|---|---|
| `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | ABSENT at dispatch | create |
| `docs/reviews/CVF_ASSF_T7_CERTIFICATION_UAT_DRIFT_DEPRECATION_RETIREMENT_GUARD_WORKER_RETURN_2026-06-25.md` | ABSENT at dispatch | create |
| `docs/reviews/CVF_ASSF_T7_CERTIFICATION_UAT_DRIFT_DEPRECATION_RETIREMENT_GUARD_COMPLETION_2026-06-25.md` | ABSENT at dispatch | do not create; Codex reviewer owns |

## Acceptance Criteria

| Criterion | Required disposition |
|---|---|
| T7 contract defines certification, UAT, drift, deprecation, successor, retirement, duplicate-ID, and adapter-claim guard classes | REQUIRED |
| T7 contract includes a Dual Agent Surface Matrix with internal-agent and external-agent CLI/MCP rows | REQUIRED |
| T7 contract states that machine-check integration is candidate-only unless implemented by a later governed tranche | REQUIRED |
| T7 contract preserves T2 metadata-only resolver/index boundary | REQUIRED |
| T7 contract preserves T5 no-automatic-promotion and package graph restrictions | REQUIRED |
| T7 contract preserves T6 rule that no Web example becomes `CERTIFIED_PACKAGE_PROJECTION` without package certification evidence | REQUIRED |
| Worker return includes command-backed evidence and exact changed files | REQUIRED |
| Worker does not edit active session state, active handoff, session front door, generated active-session aggregate, public-sync clone, runtime source, generated index, resolver, or adapter source | REQUIRED |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ASSF-T7 certification lifecycle guard contract dispatch |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE -- dispatch baseline only |
| receiptEvidence | N/A with reason: no runtime execution, provider call, or adapter receipt exists at dispatch |
| actionEvidence | ACTION_EVIDENCE_PRESENT -- Source Verification Block, dependency release evidence, ADIF disclosure, and artifact manifest |
| invocationBoundary | governed local documentation dispatch only |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, CLI, MCP, Web runtime, or adapter interception claim |
| claimLanguage | authorizes bounded documentation worker execution for Claude |
| forbiddenExpansion | no checker implementation, generated-index mutation, resolver mutation, package activation, Web runtime change, CLI/MCP adapter, provider call, live proof, public-sync, push, or session-sync edit by worker |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this dispatch references private provenance architecture and repository
source surfaces. Public-safe export requires a separate redaction and
public-sync authorization.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Roadmap state | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | `Status: ASSF_T7_CLOSED_PASS_BOUNDED` | PASS |
| GC-018 status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_T7_CERTIFICATION_UAT_DRIFT_DEPRECATION_RETIREMENT_GUARD_FOR_CLAUDE_2026-06-25.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Worker material artifacts | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md`; `docs/reviews/CVF_ASSF_T7_CERTIFICATION_UAT_DRIFT_DEPRECATION_RETIREMENT_GUARD_WORKER_RETURN_2026-06-25.md` | created by Claude worker and accepted by Codex review | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ASSF_T7_CERTIFICATION_UAT_DRIFT_DEPRECATION_RETIREMENT_GUARD_COMPLETION_2026-06-25.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | BLOCKED with reason | T7 closure is not authorized to update GC-051 corpus registry or generated ASSF index surfaces | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason | T7 closure is not authorized to update GC-051 corpus registry Markdown surfaces | BLOCKED with reason |
| External evidence digest | N/A with reason | no external evidence imported; external-agent boundary is contract-only | N/A with reason |
| System loop interlock | this baseline | T7 closes after T1/T2/T5/T6 prerequisites and releases no package activation | PASS |
| Session continuity | N/A with reason | Codex session-sync occurs after dispatch commit and after review if accepted; worker must not edit session surfaces | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Roadmap status | `ASSF_T7_CLOSED_PASS_BOUNDED` | `ASSF_T7_CLOSED_PASS_BOUNDED` | PASS |
| Worker commit mode | `WORKER_MUST_NOT_COMMIT` | worker left two uncommitted deliverables for Codex review | PASS |
| T7 contract | created | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | PASS |
| Worker return | `COMPLETE_PENDING_REVIEW` | accepted by Codex completion review | PASS |
| Runtime/provider/live claim | none | none | PASS |
| External CLI/MCP adapter | deferred | `DEFERRED_WITH_REASON` | PASS |

## Claim Boundary

This baseline records bounded ASSF-T7 closure only. It does not certify any
package, does not change any generated index, does not classify any Web example
as certified, does not create a checker, and does not authorize public-sync or
external adapter behavior.
