# CVF GC-018 Baseline: ASSF Package Lifecycle Source-State Update T0-T4

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-26

docType: baseline

Batch ID: ASSF-LIFECYCLE-SOURCE-STATE

dispatchBaseHead: 9c48f83b

## Decision / Baseline / Proposed Tranche

| Field | Disposition |
|---|---|
| Decision | execute lifecycle source-state update for `cvf-dispatch-quality-reviewer` |
| Baseline | certification evidence approved at material commit `208ae418` |
| Proposed tranche | ASSF-LIFECYCLE-SOURCE-STATE T0-T4 |
| Worker route | Codex single-agent multi-role execution |
| Closure posture | `CLOSED_PASS_BOUNDED` |

## Purpose

Authorize the bounded registry-source update, generated-index regeneration, and
metadata resolver verification for the selected candidate.

## Scope / Methodology

Codex updates the compact registry source, runs the ASSF generated-index
generator, checks drift, verifies resolver output, and closes with a
next-control decision. The batch does not edit resolver source or any runtime,
Web, CLI/MCP, provider/live, public-sync, activation, or package-instance
surface.

## Findings / Position

The source update is justified by the accepted certification evidence. T7's
newer lifecycle guard uses `uatState: PASSED`, while the older promotion bridge
mentions `COMPLETE`; this tranche follows T7 for the current update and records
the discrepancy as advisory only.

## Risk / Corrective Action

| Risk | Disposition |
|---|---|
| Older `COMPLETE` wording could conflict with T7 `PASSED` | Use T7 as current lifecycle guard authority for this tranche |
| Index drift could remain after source edit | Run generator and drift checker |
| Metadata certification could be read as activation | Preserve non-active status and external adapter deferral |

## Evidence / Verification

| Evidence | Result |
|---|---|
| registry source readback | `uatState=PASSED`; `certificationState=CERTIFIED` |
| generated index drift | PASS |
| resolver readout | one metadata-only target result |
| changed set | selected registry source, generated index, roadmap, baseline, work order, reviews |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`assf-lifecycle-source-state-update`, role=`reviewer-closer`, lifecyclePhase=`material-closure`

Returned defects: NONE_RETURNED

- none

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| target source entry contains `uatState` | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | line 67 before update | `uatState` | ASSF registry entry | VALUE_SET | ACCEPT |
| target source entry contains `certificationState` | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | line 68 before update | `certificationState` | ASSF registry entry | VALUE_SET | ACCEPT |
| T7 lifecycle guard defines `PASSED` | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | line 86 | `PASSED` | ASSF lifecycle guard | VALUE_SET | ACCEPT |
| T7 lifecycle guard defines `CERTIFIED` | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | line 81 | `CERTIFIED` | ASSF lifecycle guard | VALUE_SET | ACCEPT |
| certification decision approved evidence for source-state update | `docs/reviews/CVF_ASSF_PACKAGE_CERTIFICATION_DECISION_T0_T3_COMPLETION_2026-06-26.md` | line 17 | `CERTIFICATION_EVIDENCE_APPROVED_SOURCE_STATE_UPDATE_DEFERRED` | ASSF certification decision completion | VALUE_SET | ACCEPT |
| generator writes generated index | `governance/compat/generate_assf_skill_index.py` | line 94 | `generate_index` | ASSF index generator | EXISTS | ACCEPT |
| drift checker validates generated index | `governance/compat/check_assf_skill_index_drift.py` | module | `main` | ASSF drift checker | EXISTS | ACCEPT |
| resolver remains read-only metadata resolver | `governance/compat/run_assf_skill_resolver.py` | line 200 | `resolve_skill_packet` | ASSF resolver | EXISTS | ACCEPT |

## Write Ownership

| Path | Owner | Disposition |
|---|---|---|
| `docs/roadmaps/CVF_ASSF_PACKAGE_LIFECYCLE_SOURCE_STATE_UPDATE_ROADMAP_2026-06-26.md` | Codex | create and close |
| `docs/baselines/CVF_GC018_ASSF_PACKAGE_LIFECYCLE_SOURCE_STATE_UPDATE_T0_T4_2026-06-26.md` | Codex | create and close |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_PACKAGE_LIFECYCLE_SOURCE_STATE_UPDATE_T0_T4_FOR_CODEX_2026-06-26.md` | Codex | create and close |
| `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | Codex | update lifecycle state and review evidence |
| `docs/reference/agent_system_skills/generated/skill-index.json` | generator | regenerate from source |
| `docs/reviews/CVF_ASSF_LIFECYCLE_T0_SOURCE_AUTHORITY_MUTATION_PROTOCOL_2026-06-26.md` | Codex | create T0 review |
| `docs/reviews/CVF_ASSF_LIFECYCLE_T1_REGISTRY_SOURCE_UPDATE_2026-06-26.md` | Codex | create T1 review |
| `docs/reviews/CVF_ASSF_LIFECYCLE_T2_GENERATED_INDEX_REGENERATION_DRIFT_PROOF_2026-06-26.md` | Codex | create T2 review |
| `docs/reviews/CVF_ASSF_LIFECYCLE_T3_RESOLVER_PROJECTION_VERIFICATION_2026-06-26.md` | Codex | create T3 review |
| `docs/reviews/CVF_ASSF_LIFECYCLE_T4_CLOSURE_NEXT_CONTROL_DECISION_2026-06-26.md` | Codex | create T4 review |
| `docs/reviews/CVF_ASSF_PACKAGE_LIFECYCLE_SOURCE_STATE_UPDATE_T0_T4_COMPLETION_2026-06-26.md` | Codex | create completion review |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | direct operator authorization |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this GC-018 baseline |
| Disposition | no external material absorbed |
| Claim boundary | repository-local source and command evidence only |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | registry source and generated index metadata | internal agents may observe certification metadata only | source diff, generated diff, drift check | no package loader or execution | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future adapter readout | external agents have no mutation or execution authority | external disposition remains deferred | separate adapter work order required | `DEFERRED_WITH_REASON` |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance registry and generated metadata update; no
public-sync authorization.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ASSF lifecycle source-state GC-018 baseline |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE -- registry source and generated index only |
| receiptEvidence | CVF_RECEIPT_PRESENT - drift and resolver proof |
| actionEvidence | ACTION_EVIDENCE_PRESENT -- source diff and generated index diff |
| invocationBoundary | governed local metadata update |
| interceptionBoundary | no provider, Web, adapter, runtime, or external mutation claim |
| claimLanguage | lifecycle metadata update only |
| forbiddenExpansion | no package instance, activation, runtime behavior, resolver source mutation, Web projection, CLI/MCP adapter, provider/live proof, public-sync, push, package execution, or package integration |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_PACKAGE_LIFECYCLE_SOURCE_STATE_UPDATE_T0_T4_FOR_CODEX_2026-06-26.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ASSF_PACKAGE_LIFECYCLE_SOURCE_STATE_UPDATE_T0_T4_COMPLETION_2026-06-26.md` | completion review exists | PASS |
| Roadmap state | `docs/roadmaps/CVF_ASSF_PACKAGE_LIFECYCLE_SOURCE_STATE_UPDATE_ROADMAP_2026-06-26.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | lifecycle update in selected source | PASS |
| Registry Markdown | N/A with reason: no markdown registry companion applies | JSON source only | BLOCKED with reason: no markdown registry companion exists for this JSON-only ASSF entry |
| External evidence digest | N/A with reason: no external artifact applies | repository-local evidence only | N/A with reason |
| System loop interlock | N/A with reason: no system loop surface changed | no system loop mutation | N/A with reason |
| Session continuity | N/A with reason: material commit excludes session-sync | session-sync follows in separate commit | N/A with reason |

## Claim Boundary

This baseline authorizes only the selected registry source update, generated
index regeneration, and read-only resolver verification.
