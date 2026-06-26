# CVF GC-018 Baseline: ASSF Certified Metadata Admission Gate And Web Projection Decision T0-T4

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-26

docType: baseline

Batch ID: ASSF-CERTIFIED-METADATA-ADMISSION

dispatchBaseHead: a790bf58

## Decision / Baseline / Proposed Tranche

| Field | Disposition |
|---|---|
| Decision | implement a read-only ASSF certified metadata admission gate and close Web projection decision |
| Baseline | certified source metadata already exists for `cvf-dispatch-quality-reviewer` |
| Proposed tranche | ASSF-CERTIFIED-METADATA-ADMISSION T0-T4 |
| Worker route | Codex single-agent multi-role execution |
| Closure posture | `CLOSED_PASS_BOUNDED` |

## Purpose

Authorize bounded implementation of the ASSF certified metadata admission
checker, tests, and decision artifacts.

## Scope / Methodology

The tranche reads existing ASSF registry/index and certification contracts,
adds a read-only checker under `governance/compat`, verifies it with unit tests,
keeps it as a direct material gate, and records that Web projection remains
parked behind a future source-verified work order.

## Findings / Position

The existing ASSF source and generated index contain certified metadata. Before
that state informs Web or other surfaces, a machine gate should validate its
admission boundaries. This baseline authorizes that control only.

## Risk / Corrective Action

| Risk | Disposition |
|---|---|
| protected governance checker edits require authorization | Core Guard block is included in the completion review |
| checker could imply Web projection | T3 decision states Web projection is not implemented |
| admission gate could mutate generated index | checker is read-only and delegates drift comparison only |
| resolver mutation could slip in | resolver source is forbidden scope |

## Evidence / Verification

| Evidence | Result |
|---|---|
| source inventory | T0 review |
| focused unit tests | PASS |
| direct admission gate | PASS |
| drift gate | PASS |
| resolver readout | metadata-only one candidate |

## Current Runtime Freshness Verification

| Surface | Command | Result |
|---|---|---|
| admission checker | `python governance/compat/check_assf_certified_metadata_admission.py --require-certified` | PASS |
| generated index drift | `python governance/compat/check_assf_skill_index_drift.py` | PASS |
| resolver readout | `python governance/compat/run_assf_skill_resolver.py --task-class dispatch-authoring --role reviewer --phase PRE_DISPATCH --surface governance/compat --risk-ceiling R0` | PASS |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`assf-certified-metadata-admission-gate`, role=`reviewer-closer`, lifecyclePhase=`material-closure`

Returned defects: NONE_RETURNED

- none

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| source certified state exists | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | lines 71-83 | `certificationState` | ASSF registry entry | VALUE_SET | ACCEPT |
| generated index exposes source certified state | `docs/reference/agent_system_skills/generated/skill-index.json` | lines 16-92 | `skills[0]` | ASSF generated index | VALUE_SET | ACCEPT |
| UAT pass is certification precondition | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | lines 89-91 | `uatState` | lifecycle guard contract | LITERAL_INVARIANT | ACCEPT |
| adapter claim honesty rules exist | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | lines 138-148 | `adapterEvidence` | lifecycle guard contract | LITERAL_INVARIANT | ACCEPT |
| Web projection requires later work order | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | lines 171-183 | `CERTIFIED_PACKAGE_PROJECTION` | lifecycle guard contract | LITERAL_INVARIANT | ACCEPT |
| generated index validation API exists | `governance/compat/generate_assf_skill_index.py` | lines 107-115 | `validate_index_matches_sources` | ASSF index generator | EXISTS | ACCEPT |

## Write Ownership

| Path | Owner | Disposition |
|---|---|---|
| `governance/compat/check_assf_certified_metadata_admission.py` | Codex | create read-only checker |
| `governance/compat/test_check_assf_certified_metadata_admission.py` | Codex | create focused tests |
| `docs/roadmaps/CVF_ASSF_CERTIFIED_METADATA_ADMISSION_GATE_AND_WEB_PROJECTION_DECISION_ROADMAP_2026-06-26.md` | Codex | create and close |
| `docs/baselines/CVF_GC018_ASSF_CERTIFIED_METADATA_ADMISSION_GATE_AND_WEB_PROJECTION_DECISION_T0_T4_2026-06-26.md` | Codex | create and close |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_CERTIFIED_METADATA_ADMISSION_GATE_AND_WEB_PROJECTION_DECISION_T0_T4_FOR_CODEX_2026-06-26.md` | Codex | create and close |
| `docs/reviews/CVF_ASSF_ADMISSION_T0_SOURCE_INVENTORY_AND_AUTHORITY_2026-06-26.md` | Codex | create |
| `docs/reviews/CVF_ASSF_ADMISSION_T1_CERTIFIED_METADATA_CHECKER_IMPLEMENTATION_2026-06-26.md` | Codex | create |
| `docs/reviews/CVF_ASSF_ADMISSION_T2_GATE_EXECUTION_AND_READ_MODEL_PROOF_2026-06-26.md` | Codex | create |
| `docs/reviews/CVF_ASSF_ADMISSION_T3_WEB_PROJECTION_DECISION_2026-06-26.md` | Codex | create |
| `docs/reviews/CVF_ASSF_ADMISSION_T4_CLOSURE_NEXT_CONTROL_2026-06-26.md` | Codex | create |
| `docs/reviews/CVF_ASSF_CERTIFIED_METADATA_ADMISSION_GATE_AND_WEB_PROJECTION_DECISION_T0_T4_COMPLETION_2026-06-26.md` | Codex | create |

## Forbidden Scope

No package instance creation, certification decision, generated-index mutation,
resolver source mutation, Web runtime change, CLI/MCP adapter, provider/live
proof, public-sync, push, or session-sync is authorized in the material commit.

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

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance control; no public-sync authorization.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ASSF certified metadata admission GC-018 baseline |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE -- checker and decision artifacts only |
| receiptEvidence | CVF_RECEIPT_PRESENT - tests and gate PASS |
| actionEvidence | ACTION_EVIDENCE_PRESENT -- checker, tests, artifacts |
| invocationBoundary | governed local material update |
| interceptionBoundary | no provider, Web, adapter, runtime, resolver mutation, or external mutation claim |
| claimLanguage | admission gate closed bounded |
| forbiddenExpansion | no package instance, activation, runtime behavior, resolver source mutation, Web projection implementation, CLI/MCP adapter, provider/live proof, public-sync, push, package execution, or session-sync |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_CERTIFIED_METADATA_ADMISSION_GATE_AND_WEB_PROJECTION_DECISION_T0_T4_FOR_CODEX_2026-06-26.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ASSF_CERTIFIED_METADATA_ADMISSION_GATE_AND_WEB_PROJECTION_DECISION_T0_T4_COMPLETION_2026-06-26.md` | completion review exists | PASS |
| Roadmap state | `docs/roadmaps/CVF_ASSF_CERTIFIED_METADATA_ADMISSION_GATE_AND_WEB_PROJECTION_DECISION_ROADMAP_2026-06-26.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | read-only source consumed by checker | PASS |
| Registry Markdown | N/A with reason: no markdown registry companion applies | JSON source only | BLOCKED with reason: no markdown registry companion exists for this JSON-only ASSF entry |
| External evidence digest | N/A with reason: no external artifact applies | repository-local evidence only | N/A with reason |
| System loop interlock | N/A with reason: no system loop surface changed | no system loop mutation | N/A with reason |
| Session continuity | N/A with reason: material commit excludes session-sync | session-sync follows separately if needed | N/A with reason |

## Claim Boundary

This baseline authorizes only the admission checker, focused tests, and decision
artifacts.
