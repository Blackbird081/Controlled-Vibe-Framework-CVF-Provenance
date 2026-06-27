# CVF Roadmap: ASSF Package Lifecycle Source-State Update

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-26

docType: roadmap

Batch ID: ASSF-LIFECYCLE-SOURCE-STATE

baseHead: 9c48f83b

## Purpose

Close the lifecycle source-state update lane for
`cvf-dispatch-quality-reviewer` after certification evidence was approved at
material commit `208ae418`.

## Authorization / Decision

| Field | Disposition |
|---|---|
| Authorization source | active session next allowed move plus operator approval to process T0-T4 |
| Decision scope | registry source lifecycle metadata and generated index only |
| Material base | `9c48f83b` |
| Closure posture | `CLOSED_PASS_BOUNDED` |

## Scope / Methodology

This roadmap executes T0 through T4 as a single Codex reviewer/closer tranche.
It source-verifies lifecycle authority, updates the compact registry source,
regenerates the ASSF generated index, verifies resolver projection, and records
the next-control boundary.

## Findings / Position

The package source now records `uatState: PASSED` and
`certificationState: CERTIFIED`, and the generated index matches the updated
source. The resolver remains metadata-only and does not activate, execute, or
project Web/runtime behavior.

## Risk / Corrective Action

| Risk | Disposition |
|---|---|
| Lifecycle update could be mistaken for activation | Prevented: `status`, `candidateState`, and adapter fields remain non-active/deferred |
| Generated index could be hand-edited | Prevented: updated only through `generate_assf_skill_index.py --generate` |
| Resolver projection could imply instruction-body loading | Prevented: resolver output remains identity/selector metadata only |
| Web or adapter work could start prematurely | Prevented: T4 parks those behind future source-verified work |

## Non-Goals

| Non-goal | Reason |
|---|---|
| package instance creation or activation | metadata update only |
| resolver source mutation | existing resolver remains sufficient |
| Web projection | separate future source-verified lane |
| CLI/MCP adapter behavior | external adapter remains deferred |
| provider/live proof or public-sync | outside private provenance metadata update |

## Design Control Gate

| Control | Required outcome | Status |
|---|---|---|
| lifecycle state discipline | source update uses T7 lifecycle values | PASS |
| generated aggregate discipline | generated index comes from generator | PASS |
| resolver boundary | resolver remains metadata-only | PASS |
| dual-agent boundary | external CLI/MCP remains deferred | PASS |

## Tranche Plan

| Tranche | Objective | Artifact | Status |
|---|---|---|---|
| T0 | Source authority and mutation protocol | `docs/reviews/CVF_ASSF_LIFECYCLE_T0_SOURCE_AUTHORITY_MUTATION_PROTOCOL_2026-06-26.md` | CLOSED_PASS_BOUNDED |
| T1 | Registry source lifecycle update | `docs/reviews/CVF_ASSF_LIFECYCLE_T1_REGISTRY_SOURCE_UPDATE_2026-06-26.md` | CLOSED_PASS_BOUNDED |
| T2 | Generated index regeneration and drift proof | `docs/reviews/CVF_ASSF_LIFECYCLE_T2_GENERATED_INDEX_REGENERATION_DRIFT_PROOF_2026-06-26.md` | CLOSED_PASS_BOUNDED |
| T3 | Resolver projection verification | `docs/reviews/CVF_ASSF_LIFECYCLE_T3_RESOLVER_PROJECTION_VERIFICATION_2026-06-26.md` | CLOSED_PASS_BOUNDED |
| T4 | Closure and next-control decision | `docs/reviews/CVF_ASSF_LIFECYCLE_T4_CLOSURE_NEXT_CONTROL_DECISION_2026-06-26.md` | CLOSED_PASS_BOUNDED |

## Work Plan

| Step | Work | Output |
|---|---|---|
| 1 | verify current source authority | T0 protocol |
| 2 | update registry source | T1 evidence review |
| 3 | regenerate generated index and check drift | T2 evidence review |
| 4 | verify resolver readout | T3 evidence review |
| 5 | close next-control | T4 and completion review |

## Acceptance Criteria

| ID | Criterion | Status |
|---|---|---|
| AC1 | Registry source records `uatState: PASSED` and `certificationState: CERTIFIED` | PASS |
| AC2 | Generated index matches registry source after generator run | PASS |
| AC3 | Resolver returns the target candidate as metadata-only readout | PASS |
| AC4 | No package instance, activation, Web, adapter, provider/live, or public-sync path changed | PASS |
| AC5 | Roadmap carries machine closure package and acceptance matrix at closure | PASS |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| target source entry contains lifecycle fields | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | root object | `uatState` | ASSF registry entry | VALUE_SET | ACCEPT |
| target source entry contains certification field | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | root object | `certificationState` | ASSF registry entry | VALUE_SET | ACCEPT |
| T7 lifecycle guard defines `PASSED` and `CERTIFIED` values | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | Certification And UAT State Model | `PASSED` | ASSF lifecycle guard | VALUE_SET | ACCEPT |
| certification evidence was approved for later source-state update | `docs/reviews/CVF_ASSF_PACKAGE_CERTIFICATION_DECISION_T0_T3_COMPLETION_2026-06-26.md` | top disposition | `CERTIFICATION_EVIDENCE_APPROVED_SOURCE_STATE_UPDATE_DEFERRED` | ASSF certification decision completion | VALUE_SET | ACCEPT |
| generator writes only the generated index aggregate | `governance/compat/generate_assf_skill_index.py` | module | `generate_index` | ASSF index generator | EXISTS | ACCEPT |
| drift checker validates generated index against source entries | `governance/compat/check_assf_skill_index_drift.py` | module | `main` | ASSF drift checker | EXISTS | ACCEPT |
| resolver returns read-only metadata packet | `governance/compat/run_assf_skill_resolver.py` | module | `resolve_skill_packet` | ASSF resolver | EXISTS | ACCEPT |

## Current Runtime Freshness Verification

| Surface | Command | Result |
|---|---|---|
| pre-update drift | `python governance/compat/check_assf_skill_index_drift.py` | PASS |
| post-update drift | `python governance/compat/check_assf_skill_index_drift.py` | PASS |
| resolver projection | `python governance/compat/run_assf_skill_resolver.py --task-class dispatch-authoring --role reviewer --phase PRE_DISPATCH --surface governance/compat --risk-ceiling R0` | PASS |

## Verification / Evidence

| Evidence | Result |
|---|---|
| registry source readback | `uatState=PASSED`; `certificationState=CERTIFIED` |
| generated index readback | target entry has `certificationState=CERTIFIED` |
| ASSF drift checker | PASS |
| resolver readout | one metadata-only target result |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | direct operator authorization to continue T0-T4 |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this roadmap |
| Disposition | no external material absorbed |
| Claim boundary | repository-local source and command evidence only |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | ASSF generated index and resolver metadata | internal agents may observe certified metadata but may not activate or execute the package | source entry, generated index, drift proof, resolver proof | no loader, package instance, or instruction execution | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future adapter readout | external agents cannot mutate, activate, certify, or execute this package through this roadmap | external fields remain `DEFERRED_WITH_REASON` | separate adapter work order required | `DEFERRED_WITH_REASON` |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance registry source and generated index update; no
public-sync authorization.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ASSF lifecycle source-state update roadmap |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE -- source-state and generated-index metadata only |
| receiptEvidence | CVF_RECEIPT_PRESENT - drift PASS and resolver PASS |
| actionEvidence | ACTION_EVIDENCE_PRESENT -- registry source diff and generated index diff |
| invocationBoundary | governed local file edits and read-only local verification commands |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, CLI, MCP, or Web interception claim |
| claimLanguage | lifecycle metadata update only |
| forbiddenExpansion | no package instance, activation, runtime behavior, resolver source mutation, Web projection, CLI/MCP adapter, provider/live proof, public-sync, push, package execution, or package integration |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_PACKAGE_LIFECYCLE_SOURCE_STATE_UPDATE_T0_T4_FOR_CODEX_2026-06-26.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ASSF_PACKAGE_LIFECYCLE_SOURCE_STATE_UPDATE_T0_T4_COMPLETION_2026-06-26.md` | closure review records lifecycle source-state update | PASS |
| Roadmap state | this roadmap | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | `uatState: PASSED`; `certificationState: CERTIFIED` | PASS |
| Registry Markdown | N/A with reason: ASSF registry source for this candidate is JSON, not markdown | no markdown registry companion applies | BLOCKED with reason: no markdown registry companion exists for this JSON-only ASSF entry |
| External evidence digest | N/A with reason: no external artifact created or consumed | repository-local evidence only | N/A with reason |
| System loop interlock | N/A with reason: no system loop surface changed | no system loop mutation | N/A with reason |
| Session continuity | N/A with reason: material commit excludes session-sync | session-sync follows in separate commit | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Query ID | Receipt artifact | JSON path | Required value | Observed value | Status |
|---|---|---|---|---|---|
| ARAM-LSU-01 | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | `$.uatState` | `PASSED` | `PASSED` | PASS |
| ARAM-LSU-02 | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | `$.certificationState` | `CERTIFIED` | `CERTIFIED` | PASS |
| ARAM-LSU-03 | `docs/reference/agent_system_skills/generated/skill-index.json` | `$.skills[0].certificationState` | `CERTIFIED` | `CERTIFIED` | PASS |

## Claim Boundary

This roadmap records a private provenance metadata update only. It does not
activate a package, create a package instance, execute package instructions,
wire Web/runtime behavior, implement an adapter, run provider/live proof,
public-sync, push, or authorize external mutation.
