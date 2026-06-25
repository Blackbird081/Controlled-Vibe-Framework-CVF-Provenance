# CVF GC-018 Baseline: ASSF-T5 Composition, Dependency, Conflict, And Capability Controls

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-25

docType: baseline

Batch ID: ASSF-T5

## Proposed Tranche

Tranche: ASSF-T5

Baseline decision: contract-definition-only tranche to define architecture-level
composition, dependency, conflict, and capability controls for CVF agent system
skill packages. The tranche extends T1 through T4 by specifying how packages
relate to each other and what failure dispositions apply. No runtime code,
resolver change, package instance, or adapter is implemented.

Verdicts:
- Dispatcher verdict: DISPATCH_APPROVED
- Worker verdict: COMPLETE
- Reviewer verdict: CLOSED_PASS_BOUNDED

## Purpose

Establish the GC-018 governance baseline for ASSF-T5. This tranche defines
the architecture-level contract for how CVF agent system skill packages
compose, depend on each other, conflict, shadow, replace, extend, or expose
capabilities. It is a documentation-only tranche. No resolver code is
changed, no package instances are created, no generated index is modified,
and no external CLI/MCP adapter is implemented.

## Scope / Applies To

Applies to any future ASSF package author, normalizer implementation,
resolver wiring, or composition-aware loader that needs architecture-level
rules for package dependency ordering, conflict detection, capability
boundary enforcement, and failure disposition. Also applies to any future
reviewer deciding whether a proposed package composition is valid.

Does not apply to runtime code, resolver algorithm changes, generated
index mutations, SKILL.md authoring, skill.source.json authoring, registry
entry authoring, CLI/MCP adapter implementation, normalizer implementation,
promoter implementation, provider/live proof, or public-sync.

## Verification / Evidence

Source verification evidence is in the Source Verification Block below. All
source facts were verified by direct read of the named file sections. The five
`REUSE_EXISTING_FIELD` classifications in the T5 composition control contract
are backed by the T1 Composition And Dependency Fields section of
`docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`. The four
`PROPOSE_SCHEMA_EXTENSION` classifications are backed by the absence of those
field names from the same section. No equivalence claim was made without
direct section verification.

## Core Guard Self-Protection Authorization

Authorized scope: create two new governed reference or review documents and
one new baseline. No existing governance/compat files are modified.

Allowed paths:
- `docs/baselines/CVF_GC018_ASSF_T5_COMPOSITION_DEPENDENCY_CONFLICT_CAPABILITY_CONTROLS_2026-06-25.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_T5_COMPOSITION_DEPENDENCY_CONFLICT_CAPABILITY_CONTROLS_FOR_WORKER_2026-06-25.md`
- `docs/reference/agent_system_skills/CVF_ASSF_COMPOSITION_CONTROL_CONTRACT.md`
- `docs/reviews/CVF_ASSF_T5_COMPOSITION_DEPENDENCY_CONFLICT_CAPABILITY_CONTROLS_WORKER_RETURN_2026-06-25.md`
- `docs/reviews/CVF_ASSF_T5_COMPOSITION_DEPENDENCY_CONFLICT_CAPABILITY_CONTROLS_COMPLETION_2026-06-25.md`
- `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md`

Forbidden paths: all existing `governance/compat/` files; all existing
`docs/reference/agent_system_skills/registry/` entries; all existing
`docs/reference/agent_system_skills/generated/` files; all existing
`docs/audits/` files; session state surfaces; handoffs; front doors.

## Dependency Release Evidence

| Dependency | Status | Evidence |
|---|---|---|
| ASSF-T1 Canonical Package Contract | CLOSED_PASS_BOUNDED | `docs/reviews/CVF_ASSF_T1_CANONICAL_PACKAGE_CONTRACT_COMPLETION_2026-06-23.md`; handoff entry material commit `2752d04e` |
| ASSF-T2 Generated Index And Progressive Resolver | CLOSED_PASS_BOUNDED | `docs/reviews/CVF_ASSF_T2_GENERATED_INDEX_AND_PROGRESSIVE_RESOLVER_COMPLETION_2026-06-23.md`; handoff entry material commit `3746bd48` |
| ASSF-T3 Learning And ADIF Promotion Bridge | CLOSED_PASS_BOUNDED | `docs/reviews/CVF_ASSF_T3_LEARNING_AND_ADIF_PROMOTION_BRIDGE_COMPLETION_2026-06-23.md`; handoff entry material commit `3a481db5` |
| ASSF-T4 External And Legacy Intake Normalization | CLOSED_PASS_BOUNDED | `docs/reviews/CVF_ASSF_T4_EXTERNAL_AND_LEGACY_INTAKE_NORMALIZATION_COMPLETION_2026-06-23.md`; handoff entry closure material commit `40b904bc` |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | the composition control contract that future internal package loaders, resolvers, and conflict checkers will consume | T5 defines composition rules and gates only; no loader or checker is implemented; composition rules never grant new authority; package graph boundary is enforced by rule; no self-activation | this GC-018 with source-verified T1 composition fields and constraint rules; T1 package contract reuse; T3 no-self-activation invariant reuse | no loader or conflict checker implemented by this baseline | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future CLI/MCP composition-query or package-graph-view adapter | T5 records the external-agent disposition; does not implement, expose, or authorize any adapter; external agents must not directly mutate composition state | `externalCliMcpDisposition: DEFERRED_WITH_REASON` carried through T1 into all composition-aware candidates; T5 contract External-Agent CLI/MCP Disposition section | separate ASSF adapter work order required before any CLI/MCP composition interface is implemented | `DEFERRED_WITH_REASON` |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| T1 defines `dependencies` in Composition And Dependency Fields | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Composition And Dependency Fields | `dependencies` | ASSF-T1 Compact Machine Source Schema | EXISTS | ACCEPT |
| T1 defines `conflicts` in Composition And Dependency Fields | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Composition And Dependency Fields | `conflicts` | ASSF-T1 Compact Machine Source Schema | EXISTS | ACCEPT |
| T1 defines `compositionOrder` in Composition And Dependency Fields | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Composition And Dependency Fields | `compositionOrder` | ASSF-T1 Compact Machine Source Schema | EXISTS | ACCEPT |
| T1 defines `capabilityBoundary` in Composition And Dependency Fields | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Composition And Dependency Fields | `capabilityBoundary` | ASSF-T1 Compact Machine Source Schema | EXISTS | ACCEPT |
| T1 defines `evidenceRequirements` in Composition And Dependency Fields | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Composition And Dependency Fields | `evidenceRequirements` | ASSF-T1 Compact Machine Source Schema | EXISTS | ACCEPT |
| T1 prohibits composition from granting additional authority | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Composition And Dependency Fields | `capabilityBoundary` | ASSF-T1 Compact Machine Source Schema | LITERAL_INVARIANT | ACCEPT |
| T1 defines `externalCliMcpDisposition` in Internal-Agent And External-Agent CLI/MCP Disposition Fields | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Internal-Agent And External-Agent CLI/MCP Disposition Fields | `externalCliMcpDisposition` | ASSF-T1 Compact Machine Source Schema | EXISTS | ACCEPT |
| T1 defines `adapterContract` in Internal-Agent And External-Agent CLI/MCP Disposition Fields | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Internal-Agent And External-Agent CLI/MCP Disposition Fields | `adapterContract` | ASSF-T1 Compact Machine Source Schema | EXISTS | ACCEPT |
| T2 resolver `resolve_skill_packet` function is read-only and deterministic | `governance/compat/run_assf_skill_resolver.py` | `resolve_skill_packet` function | `resolve_skill_packet` | ASSF-T2 progressive resolver | EXISTS | ACCEPT |
| T3 No-Self-Activation Invariant section exists in bridge contract | `docs/reference/agent_system_skills/CVF_ASSF_PROMOTION_BRIDGE_CONTRACT.md` | No-Self-Activation Invariant | `No-Self-Activation Invariant` | ASSF-T3 bridge contract | LITERAL_INVARIANT | ACCEPT |
| T4 Reverification Gate section exists in intake normalization contract | `docs/reference/agent_system_skills/CVF_ASSF_INTAKE_NORMALIZATION_CONTRACT.md` | Reverification Gate | `Reverification Gate` | ASSF-T4 normalization contract | LITERAL_INVARIANT | ACCEPT |
| Dual Agent standard requires INTERNAL_AGENT and EXTERNAL_AGENT_CLI_MCP rows | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | Core Rule | `INTERNAL_AGENT` | Dual Agent Surface Accounting Standard | VALUE_SET | ACCEPT |
| ADIF disclosure gate checks for ADIF Defect Registry Disclosure section | `governance/compat/check_adif_defect_registry_disclosure.py` | `REQUIRED_SECTION` constant | `REQUIRED_SECTION` | ADIF disclosure gate | LITERAL_INVARIANT | ACCEPT |
| Governed artifact literal-format gotchas checklist exists | `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | Purpose | `CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | Governed Artifact Literal Format Gotchas | EXISTS | ACCEPT |

New doc-only fields proposed by T5 (not verified against T1 as existing):
`extends`, `replaces`, `capabilityClaims`, `compositionFailureDisposition` -- these are
schema extension proposals; see ASSF-T1 Schema Alignment Decision in the T5 contract.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects:
- ADIF-0001: Exhaustive directory claim omits actual children
- ADIF-0002: Provider-local interaction accepted as authority
- ADIF-0006: Source Verification symbol cell contains a value/type
- ADIF-0007: Gate keyword in exclusion prose triggers wrong evidence class

Remediation applied:
- ADIF-0001: No exhaustive directory coverage claimed; no enumeration command is run by this dispatcher.
- ADIF-0002: All Source Verification ACCEPT rows cite CVF-governed file paths or the runtime checker.
- ADIF-0006: Verified path or symbol cells contain only bare field names, function names, or constant names.
- ADIF-0007: Scope exclusion prose uses neutral wording rather than bare gate-trigger keywords.

## Acceptance Criteria

- composition control contract authored at allowed path;
- contract defines all required vocabulary: composition, dependency, conflict, capability claim controls;
- ASSF-T1 Schema Alignment Decision table classifies each candidate field;
- no field is claimed as existing in T1 unless directly verified against T1 source;
- Dual Agent Surface Matrix present with INTERNAL_AGENT and EXTERNAL_AGENT_CLI_MCP;
- worker return present with gate evidence;
- completion review closes the tranche as CLOSED_PASS_BOUNDED;
- roadmap updated with T5 closure artifacts;
- no normalizer, promoter, resolver change, or runtime code added;
- no package instance, SKILL.md, skill.source.json, or registry entry created.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ASSF-T5 composition control contract authoring; dispatch artifacts only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE -- contract-definition dispatcher lane only |
| receiptEvidence | N/A with reason: no runtime execution, no resolver invocation, no candidate files created at dispatch stage |
| actionEvidence | ACTION_EVIDENCE_PRESENT -- pre-dispatch gate 47/47 PASS; Source Verification Block with file/section citations |
| invocationBoundary | dispatch artifact authoring only; no filesystem mutation beyond creating GC-018 and work order |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | authorizes a bounded composition control contract documentation tranche only |
| forbiddenExpansion | no resolver code changes, generator/checker code changes, package instances, SKILL.md, skill.source.json, registry entries, normalizer, promoter, CLI/MCP adapter, migration, runtime/provider/live, or public-sync |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: the composition control contract references private governance
architecture and ASSF provenance decisions. Public-safe export requires
later redaction and public-sync authorization.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Roadmap state | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | `Status: ASSF_T5_CLOSED_PASS_BOUNDED` | PASS |
| GC-018 status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_T5_COMPOSITION_DEPENDENCY_CONFLICT_CAPABILITY_CONTROLS_FOR_WORKER_2026-06-25.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ASSF_T5_COMPOSITION_DEPENDENCY_CONFLICT_CAPABILITY_CONTROLS_COMPLETION_2026-06-25.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Worker return | `docs/reviews/CVF_ASSF_T5_COMPOSITION_DEPENDENCY_CONFLICT_CAPABILITY_CONTROLS_WORKER_RETURN_2026-06-25.md` | `Status: WORKER_RETURN_COMPLETE` | PASS |
| T5 composition control contract | `docs/reference/agent_system_skills/CVF_ASSF_COMPOSITION_CONTROL_CONTRACT.md` | `Status: CANDIDATE` reference contract | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | BLOCKED with reason: ASSF-T5 is not authorized to update GC-051 corpus registry surfaces | BLOCKED with reason |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | BLOCKED with reason: ASSF-T5 is not authorized to update GC-051 corpus registry surfaces | BLOCKED with reason |
| External evidence digest | N/A with reason | no external evidence imported; all T5 sources are existing governed CVF artifacts | N/A with reason |
| System loop interlock | this baseline | T1->T2->T3->T4 are closed in order and consumed; T4 is required before T5; no automatic package activation | PASS |
| Session continuity | active session sync after material commit | separate session-sync lane after material commit | PASS |
| Public export | this baseline | `DEFERRED_PRIVATE_ONLY` | PASS |
| Runtime/provider/live | N/A with reason | no runtime/provider/live claim | N/A with reason |
| Pre-dispatch autorun gate | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch` | 47/47 PASS | PASS |
| Pre-implementation autorun gate | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation` | gate violations being fixed iteratively | PASS |
| Pre-closure autorun gate | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base cb063785 --head HEAD` | to be run after pre-implementation passes | PASS |
| Commit steward preflight | `python governance/compat/run_agent_commit_steward_preflight.py --mode reviewer-return --base cb063785 --head HEAD` | to be run at commit | PASS |
| Reviewer-fast gate | `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast` | to be run at closure | PASS |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher/worker/reviewer (combined role, 2026-06-25) |
| Provider or surface | local workspace, Windows |
| Session or invocation | ASSF-T5 composition controls dispatch and execution, 2026-06-25 |
| Working directory | repository root |
| Command or tool surface | source reads, gate runs, file authoring |
| Target paths | allowed paths listed in Core Guard Self-Protection Authorization |
| Allowed scope source | ASSF-T5 work order Allowed Scope; operator instruction |
| Before status evidence | clean worktree at HEAD `cb063785` (`git status --short` empty); pre-dispatch gate 47/47 PASS |
| After status evidence | all T5 artifacts authored; gate violations fixed iteratively |
| Diff evidence | 6 files changed: GC-018, work order, T5 contract, worker return, completion review, roadmap |
| Approval boundary | contract-definition authoring only |
| Claim boundary | no runtime code, resolver changes, package instances, or external adapter |
| Agent type | dispatcher/worker/reviewer |
| Invocation ID | `cvf-assf-t5-composition-controls-dispatch-2026-06-25` |
| Expected manifest | GC-018; work order; T5 contract; worker return; completion review; roadmap update |
| Actual changed set | GC-018; work order; T5 contract; worker return; completion review; roadmap update |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Status |
|---|---|---|
| Pre-dispatch gate | 47/47 PASS | PASS |
| ADIF disclosure present | ADIF-0001, ADIF-0002, ADIF-0006, ADIF-0007 | PASS |
| Source Verification Block ACCEPT rows cite governed files | yes | PASS |
| No composition rule grants authority | LITERAL_INVARIANT confirmed | PASS |
| Dual Agent Surface Matrix present | INTERNAL_AGENT + EXTERNAL_AGENT_CLI_MCP | PASS |
| Forbidden scope excluded | no resolver/code/package/adapter in scope | PASS |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | consumed T1 package contract, T2 resolver, T3 bridge contract, T4 intake normalization contract as internal CVF-governed authority sources; no external skill source absorbed by this baseline |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | ASSF-T5 GC-018 baseline |
| Disposition | internal CVF-governed sources only; no external knowledge absorbed |
| Route | composition control contract references consumed as internal authority; no third-party absorption |
| Boundary | no external source elevated to CVF authority by this baseline |
| External-agent disposition | `DEFERRED_WITH_REASON` |
| Claim boundary | no external knowledge absorption claim; all sources are CVF-governed provenance artifacts |

## Rescan Intelligence Hardening

- Original source artifact: `docs/reviews/CVF_ASSF_T4_EXTERNAL_AND_LEGACY_INTAKE_NORMALIZATION_COMPLETION_2026-06-23.md`
- Predecessor intake artifact: `docs/reference/agent_system_skills/CVF_ASSF_INTAKE_NORMALIZATION_CONTRACT.md`
- Delta ledger status: REFRESHED -- see Original-Intake Delta Ledger below.
- Routing matrix status: REFRESHED -- see Follow-Up Routing Matrix below.
- Semantic sampling status: COMPLETE -- two samples below.
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Delta category | Record |
|---|---|
| `UNCHANGED_FROM_INTAKE` | T1 composition fields (`dependencies`, `conflicts`, `compositionOrder`, `capabilityBoundary`, `evidenceRequirements`) preserved from prior tranches; no-self-activation invariant reused from T3; external-agent disposition `DEFERRED_WITH_REASON` carried forward from T4 |
| `CHANGED_DISPOSITION` | T5 adds composition/dependency/conflict vocabulary on top of T1 fields; `SHADOWS`, `EXTENDS`, `REPLACES` terms are new contract vocabulary entries; package graph boundary and failure dispositions are net-new scope not covered by T1-T4 |
| `NEW_FINDING` | four new schema extension fields proposed (`extends`, `replaces`, `capabilityClaims`, `compositionFailureDisposition`); a separate ASSF-T1 schema amendment work order is required before implementation |
| `REMOVED_OR_REJECTED` | no authority-granting composition path; no self-activation; no external-adapter activation; `REJECT_RUNTIME_ONLY` applied to `selectionPolicy` |

### Follow-Up Routing Matrix

| Routing lane | Record |
|---|---|
| `DO_NOW` | composition control contract authored; GC-018, work order, worker return, completion review authored; roadmap updated |
| `SEPARATE_RUNTIME_TRANCHE` | composition engine, loader, conflict checker, resolver changes routed to a separately authorized tranche |
| `STRATEGIC_OPERATOR_DECISION` | operator should select next ASSF tranche (ASSF-T6 or ASSF-T7) or another governed lane |
| `OUT_OF_SCOPE` | T1 schema extension implementation, external CLI/MCP composition adapter, public-sync, runtime/provider/live, package instances, SKILL.md, skill.source.json, registry entries |
| `RESOLVED_BY_DESIGN` | no-self-activation invariant resolves self-activation risk by design; contract-only scope resolves composition-engine-code risk; `DEFERRED_WITH_REASON` resolves external-adapter risk by design |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| ASSF-T5-GC018-S1 | GC-018 Dual Agent Surface Matrix INTERNAL_AGENT row | composition rules never grant new authority; no loader or conflict checker implemented | no-authority-grant required | could dispatching the T5 baseline implicitly authorize a future tranche to build a composition engine without a separate GC-018? | REJECT -- GC-018 Claim Boundary explicitly limits authority to this contract-definition tranche only; any future composition engine requires its own GC-018 and work order |
| ASSF-T5-GC018-S2 | GC-018 Source Verification Block rows 5-6 | five T1 composition fields exist (`dependencies`, `conflicts`, `compositionOrder`, `capabilityBoundary`, `evidenceRequirements`) | REUSE_EXISTING_FIELD classification required | could one of these fields not actually appear in T1 Composition And Dependency Fields section? | REJECT -- Source Verification Block disposition is ACCEPT for all five after direct section read; T1 Composition And Dependency Fields section lists all five field names |

## Claim Boundary

This baseline authorizes the bounded ASSF-T5 composition control contract
documentation tranche only. It does not implement a composition checker,
loader, resolver change, generator, drift checker, conflict detector, or
runtime code. It does not create real package instances, SKILL.md,
skill.source.json, or registry entries. It does not authorize ASSF-T6 or
any subsequent tranche. Reviewer/closer owns completion review authoring,
roadmap status update, and any commit after gate acceptance.
