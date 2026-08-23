# CVF GC-018 Baseline - MCP-KAR-T7-T8 Defensive Legacy Protocol Guards Implementation

Memory class: governed-dispatch-baseline

Status: REVIEWER_ACCEPTED_DISPATCH_READY

Batch ID: MCP-KAR-T7-T8

Dispatch base head: 26ab2c1cd945dd5ecca84795a8979cb82332d123

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: parent reviewer/closer

Worker target: implementation worker

## Purpose

Implement the reviewer-accepted T7 and T8 candidates as two pure defensive
legacy invariants in the existing MCP protocol profile: `MCP-PR-012` keeps
deprecated roots as hints rather than authority, and `MCP-PR-013` validates
deprecated sampling capability and tool-result sequencing. The tranche opens
no filesystem, model invocation, sampling runtime, or parallel approval lane.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MCP-KAR-T7-T8 --title "Defensive Legacy Protocol Guards Implementation" --date 2026-08-24 --base 26ab2c1cd945dd5ecca84795a8979cb82332d123 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "MCP-KAR-T6-T8 reviewer-accepted decision 93763c127; T7 and T8 proceed" --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker and MCP/CLI boundary stubs |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact five-path worker manifest, MCP-PR-012/MCP-PR-013 semantics, approval composition, deterministic tests, and held boundaries |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| docOnlyNewFields | `MCP-PR-012`; `MCP-PR-013`; `rootsHintEvidence`; `samplingSequenceEvidence`; `existingApprovalDisposition` |
| claimBoundary | dispatch authority only; implementation has not occurred |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| operator selection | autonomous valuable absorption instruction, 2026-08-24 | bounded local implementation may proceed under CVF governance | RELEASED |
| T7/T8 owner-value decision | `docs/reviews/CVF_MCP_KAR_T6_T8_RESIDUAL_PROTOCOL_OWNER_VALUE_DECISION_WORKER_RETURN_2026-08-24.md`; accepted material `93763c127` | requires `PROCEED_ROOTS_HINT_AUTHORITY_GUARD`, `PROCEED_SAMPLING_SEQUENCE_GUARD`, and exact four-path implementation manifest | RELEASED |
| current profile sequence | `MCP-PR-001` through `MCP-PR-011` exist at dispatch base | add only 012 and 013 in the existing owner | PASS |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`MCP defensive legacy protocol guards implementation dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "MCP defensive legacy protocol guards implementation dispatch" --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | N/A with reason: resolver returned none |
| Dispatch impact | canonical guards remain binding |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | dispatch status, Source Verification columns, fulfillment manifest, worker-return profile, operation trace, Delta boundary, MCP adapter boundary, and public disposition |
| gateRunPurpose | confirm completed dispatch before worker handoff |
| claimBoundary | paired documentation packet only |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| T7 and T8 are approved with exact owner and manifest | GOVERNED_REVIEW | `docs/reviews/CVF_MCP_KAR_T6_T8_RESIDUAL_PROTOCOL_OWNER_VALUE_DECISION_WORKER_RETURN_2026-08-24.md` | Decision / Disposition; Reviewer Decision | `PROCEED_ROOTS_HINT_AUTHORITY_GUARD`; `PROCEED_SAMPLING_SEQUENCE_GUARD` | accepted T6-T8 decision at `93763c127` | ACCEPT |
| normative owner currently ends at MCP-PR-011 | GOVERNED_REFERENCE | `docs/reference/mcp_gateway/CVF_MCP_NORMATIVE_INVARIANT_PROFILE.md` | Normative Mapping | `MCP-PR-001` through `MCP-PR-011` | MCP gateway reference | ACCEPT |
| source seam is the pure aggregate evaluator | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mcp.protocol.invariant.profile.ts` | `MCPProtocolInvariantProfileInput`; `MCPProtocolInvariantProfile.evaluate` | current rule union and check methods | execution-plane foundation | ACCEPT |
| focused composite test owner exists | TEST_SOURCE_FACT | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mcp.protocol.invariant.profile.test.ts` | `validInput`; profile suite | current accepted composite and negative oracles | execution-plane test owner | ACCEPT |
| barrel export exists | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/index.ts` | MCP protocol profile export | profile constructor and exported types | execution-plane foundation barrel | ACCEPT |
| roots are deprecated hints, not confinement | PINNED_UPSTREAM_FACT | `.private_reference/source_mirrors/modelcontextprotocol__modelcontextprotocol/docs/specification/2026-07-28/client/roots.mdx` | overview and security considerations | roots inform servers but do not enforce boundaries | pinned MCP roots specification | ACCEPT |
| sampling tools require capability and exact result sequence | PINNED_UPSTREAM_FACT | `.private_reference/source_mirrors/modelcontextprotocol__modelcontextprotocol/docs/specification/2026-07-28/client/sampling.mdx` | capabilities, tool loop, security | declared `sampling.tools`; matching adjacent results-only message | pinned MCP sampling specification | ACCEPT |
| approval authority already exists | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mcp.business.adapter.contract.ts` | invocation request and approval derivation | `MCPBusinessToolInvocationRequest`; `MCPBusinessAdapterContract.deriveApprovalDecision` | MCP business adapter contract | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| proposed dispatch paths | both absent at dispatch start | PASS |
| rule collision | accepted T6-T8 decision found no current roots or sampling sequence rule | PASS_WITH_GAP_OBSERVED |
| owner collision | both rules enrich the existing profile; no parallel evaluator permitted | PASS |
| approval collision | business adapter remains the sole approval owner; profile may consume an existing disposition only | PASS |
| negative-search command/root/query | `git grep -n "MCP-PR-012\|MCP-PR-013\|ROOTS_HINT_AUTHORITY_VIOLATION\|SAMPLING_SEQUENCE_VIOLATION" -- docs/reference/mcp_gateway EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests` | REQUIRED_BEFORE_EDIT |

## Decision / Baseline

The worker may add exactly two pure rules to the existing profile.

`MCP-PR-012` accepts absent roots and bounded legacy roots evidence only when
the evidence explicitly preserves caller consent/path-validation responsibility
and does not claim roots are authorization, containment, or filesystem
authority. It must fail closed for malformed/non-file roots and authority or
confinement claims. It must not discover, enumerate, resolve, open, or validate
real paths.

`MCP-PR-013` accepts absent sampling and bounded tool-less legacy sampling. If
tool use occurs, the nested `sampling.tools` capability must be declared and
each unique tool-use ID must have exactly one matching result in the immediately
following results-only user message, with no unknown, duplicate, missing,
mismatched, mixed-content, or intervening message. Any approval field is a
precomputed existing business approval disposition only. The rule must not
issue, validate, persist, or replay-protect approval and must not invoke a
model, tool, provider, transport, or sampling runtime.

Local decision codes are `ROOTS_HINT_AUTHORITY_VIOLATION` and
`SAMPLING_SEQUENCE_VIOLATION` unless fresh collision evidence requires equally
bounded source-verified local names.

## Scope / Owner Boundary

Allowed implementation paths are exactly the normative reference, profile
source, focused test, and barrel export. The only other worker write is the one
worker return named by the work order. All other paths are forbidden.

## Planned Artifact Manifest

| Artifact | Planned action |
| --- | --- |
| `docs/reference/mcp_gateway/CVF_MCP_NORMATIVE_INVARIANT_PROFILE.md` | add MCP-PR-012 and MCP-PR-013 mappings/boundaries |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mcp.protocol.invariant.profile.ts` | add pure closed types and checks in the existing evaluator |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mcp.protocol.invariant.profile.test.ts` | add deterministic positive, negative, malformed, and composite tests |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/index.ts` | preserve or minimally extend existing type exports only if needed |
| `docs/reviews/CVF_MCP_KAR_T7_T8_DEFENSIVE_LEGACY_PROTOCOL_GUARDS_IMPLEMENTATION_WORKER_RETURN_2026-08-24.md` | create one uncommitted worker evidence packet |

## Acceptance Criteria

- exact five-path worker manifest and no deletion/rename drift;
- `MCP-PR-012` is pure and never grants roots discovery/filesystem authority;
- `MCP-PR-013` validates declared capability and exact adjacent results-only
  correlation without model/tool/runtime invocation;
- absent roots/sampling and bounded tool-less sampling remain accepted;
- malformed, authority-claim, capability, correlation, and sequence negatives
  fail closed with deterministic codes;
- only a precomputed existing business approval disposition is consumed;
- all prior profile rules and composite tests remain passing;
- focused tests, TypeScript, worker-return fast gate, and `git diff --check` pass;
- worker stages and commits nothing.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | normative profile and pure invariant evaluator | structural evidence only; no filesystem/model/approval action | focused local tests | N/A with reason: direct local contract | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | possible legacy caller | no transport, filesystem, sampling execution, approval, receipt, or mutation authority | separate future adapter work required | deferred adapter/runtime | `DEFERRED_WITH_REASON` |

## MCP/CLI Adapter Boundary

| Field | Value |
| --- | --- |
| Adapter scope | none; pure defensive legacy invariant composition |
| No-runtime-overclaim | No MCP runtime, CLI, bridge, package, transport, filesystem, sampling loop, model invocation, or interoperability claim is authorized. |

## Risk / Corrective Action

Prevent roots metadata from becoming path authority and prevent a sampling
sequence validator from becoming an execution or approval owner. Keep both
rules structural, typed, local, deterministic, and side-effect-free.

## Evidence / Verification

Worker evidence must include exact source symbols, collision results, input
vocabulary, rule ordering, named tests/counts, focused test and TypeScript
results, prior-rule regression, zero external effects, exact changed set,
worker-return gate, and no-commit status.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | CVF-native implementation of accepted T7/T8 protocol facts in the exact existing owner |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_overlap_discipline.py` |
| Owner surface | exact four-path invariant implementation manifest |
| Disposition | bounded native adaptation; no new intake or direct import |
| Claim boundary | pinned protocol facts grant no runtime, filesystem, model, or approval authority |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| roots hints-not-authority | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mcp.protocol.invariant.profile.ts` | `ENRICH_EXISTING` | roots-specific authority rule absent | add MCP-PR-012 in existing owner |
| sampling sequence | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mcp.protocol.invariant.profile.ts` | `ENRICH_EXISTING` | capability/result correlation absent | add MCP-PR-013 in existing owner |
| approval derivation | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mcp.business.adapter.contract.ts` | `CONFIRMED_EXISTING` | separate owner already exists | consume disposition only; do not edit |

## Mandatory Blind-Spot Control Block

NOT_APPLICABLE_WITH_REASON: exact accepted T6-T8 decision reuse; no new corpus
or source family is opened.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - targeted implementation makes no completeness, inventory, or all-files-read claim.

## External Repository Absorption Entry Control

COMPARISON_ONLY_NO_ABSORPTION: no new enumeration, manifest, ledger, source
import, package, or runtime work.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance implementation dispatch; no public-sync authority.

## Claim Boundary

This baseline authorizes only the exact pure local implementation manifest and
one worker return. It does not authorize roots discovery or filesystem access,
sampling/model/tool execution, approval issuance/validation/replay claims,
runtime/package/transport, provider/live calls, public sync, deployment, or
production behavior.
