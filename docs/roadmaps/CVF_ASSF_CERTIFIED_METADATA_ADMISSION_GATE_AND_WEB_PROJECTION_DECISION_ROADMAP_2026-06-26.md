# CVF Roadmap: ASSF Certified Metadata Admission Gate And Web Projection Decision

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-26

docType: roadmap

Batch ID: ASSF-CERTIFIED-METADATA-ADMISSION

baseHead: a790bf58

## Purpose

Close T0-T4 for a bounded ASSF certified-metadata admission gate and Web
projection decision lane.

## Authorization / Decision

| Field | Disposition |
|---|---|
| Authorization source | operator approved continuation from next allowed move |
| Decision scope | checker/read-model gate plus decision artifacts |
| Material base | `a790bf58` |
| Closure posture | `CLOSED_PASS_BOUNDED` |

## Scope / Methodology

Codex source-verified ASSF lifecycle, generated-index, resolver, and Web
projection contracts; implemented a read-only certified metadata admission
checker; added focused tests; kept the checker as a direct material gate; and
recorded the Web projection decision without changing Web runtime source.

## Findings / Position

The new admission gate makes `certificationState: CERTIFIED` machine-checkable
against `uatState: PASSED`, review artifact existence, generated-index source
consistency, metadata-only resolver/loader boundaries, and adapter honesty
fields. The Web projection lane remains parked until a later source-verified
Web schema/mapping work order exists.

## Risk / Corrective Action

| Risk | Disposition |
|---|---|
| certified metadata could be cited without UAT pass | checker blocks certified entries without `uatState: PASSED` |
| generated index could drift from registry source | checker delegates to existing source/index drift validation |
| certified metadata could be mistaken for package activation | checker blocks `status: ACTIVE` as an admission outcome |
| adapter/Web claims could outrun evidence | checker enforces adapter evidence shape; T3 parks Web projection |

## Non-Goals

| Non-goal | Reason |
|---|---|
| package instance creation or activation | admission metadata only |
| resolver source mutation | resolver remains current metadata-only reader |
| Web runtime or schema mutation | T3 is decision-only |
| CLI/MCP adapter behavior | external adapter remains deferred |
| provider/live proof, public-sync, or push | outside this private provenance control lane |

## Design Control Gate

| Control | Required outcome | Status |
|---|---|---|
| certified metadata admission | checker validates certified entries before downstream citation | PASS |
| generated aggregate discipline | checker reads generated index and source entries without mutation | PASS |
| resolver boundary | resolver remains metadata-only and source is not modified | PASS |
| Web projection boundary | Web projection stays parked behind future source-verified work | PASS |

## Tranche Plan

| Tranche | Objective | Artifact | Status |
|---|---|---|---|
| T0 | source inventory and authority | `docs/reviews/CVF_ASSF_ADMISSION_T0_SOURCE_INVENTORY_AND_AUTHORITY_2026-06-26.md` | COMPLETE |
| T1 | checker implementation and tests | `docs/reviews/CVF_ASSF_ADMISSION_T1_CERTIFIED_METADATA_CHECKER_IMPLEMENTATION_2026-06-26.md` | COMPLETE |
| T2 | gate execution and read-model proof | `docs/reviews/CVF_ASSF_ADMISSION_T2_GATE_EXECUTION_AND_READ_MODEL_PROOF_2026-06-26.md` | COMPLETE |
| T3 | Web projection decision | `docs/reviews/CVF_ASSF_ADMISSION_T3_WEB_PROJECTION_DECISION_2026-06-26.md` | COMPLETE |
| T4 | closure and next control | `docs/reviews/CVF_ASSF_ADMISSION_T4_CLOSURE_NEXT_CONTROL_2026-06-26.md` | COMPLETE |

## Work Plan

| Step | Work | Output |
|---|---|---|
| 1 | inventory source authority | T0 review |
| 2 | implement checker and focused tests | T1 review |
| 3 | run admission, drift, and resolver proof | T2 review |
| 4 | decide Web projection boundary | T3 review |
| 5 | close next control | T4 and completion review |

## Roadmap-To-Work-Order Trace Matrix

| Requirement | Work-order instruction | Closure evidence | Disposition |
|---|---|---|---|
| T0 source inventory | verify lifecycle, registry, index, resolver, Web contracts | T0 review | PASS |
| T1 checker | implement read-only admission checker and tests | T1 review plus unit tests | PASS |
| T2 gate proof | run admission gate and resolver readout | T2 review | PASS |
| T3 Web decision | decide projection boundary without Web mutation | T3 review | PASS |
| T4 closure | close bounded lane and set next control | completion review | PASS |

## Acceptance Criteria

| ID | Criterion | Status |
|---|---|---|
| AC1 | A read-only ASSF certified metadata admission checker exists | PASS |
| AC2 | Focused unit tests cover pass and failure cases | PASS |
| AC3 | The checker passes against current ASSF registry/index state | PASS |
| AC4 | Direct admission gate is documented and passing | PASS |
| AC5 | Web projection remains decision-only, with no Web source mutation | PASS |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| current certified source state | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | lines 71-83 | `certificationState` | ASSF registry entry | VALUE_SET | ACCEPT |
| generated index carries lifecycle fields | `docs/reference/agent_system_skills/generated/skill-index.json` | lines 16-92 | `skills[0]` | ASSF generated index | VALUE_SET | ACCEPT |
| certification requires UAT pass | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | lines 89-91 | `certificationState` | lifecycle guard contract | LITERAL_INVARIANT | ACCEPT |
| adapter implemented claim requires evidence | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | lines 138-148 | `externalCliMcpDisposition` | adapter claim honesty rules | LITERAL_INVARIANT | ACCEPT |
| Web projection requires separate work order | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | lines 171-183 | `CERTIFIED_PACKAGE_PROJECTION` | Web bridge rule | LITERAL_INVARIANT | ACCEPT |
| generated index validation API exists | `governance/compat/generate_assf_skill_index.py` | lines 107-115 | `validate_index_matches_sources` | ASSF index generator | EXISTS | ACCEPT |
| resolver remains metadata-only | `governance/compat/run_assf_skill_resolver.py` | lines 202-267 | `resolve_skill_packet` | ASSF resolver | EXISTS | ACCEPT |

## Verification / Evidence

| Evidence | Result |
|---|---|
| `python -m unittest governance.compat.test_check_assf_certified_metadata_admission` | PASS - 6 tests |
| `python governance/compat/check_assf_certified_metadata_admission.py --require-certified` | PASS |
| `python governance/compat/check_assf_skill_index_drift.py` | PASS |
| resolver readout command | PASS - one metadata-only candidate |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance and ASSF metadata control; no public-sync
authorization.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ASSF certified metadata admission gate roadmap |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE -- read-only checker and decision artifacts |
| receiptEvidence | CVF_RECEIPT_PRESENT - unit tests, admission gate, drift gate, resolver readout |
| actionEvidence | ACTION_EVIDENCE_PRESENT -- checker, tests, governed artifacts |
| invocationBoundary | local governed file edits and read-only commands |
| interceptionBoundary | no provider, Web runtime, adapter, resolver source, or package activation claim |
| claimLanguage | certified metadata admission gate closed bounded |
| forbiddenExpansion | no package instance, activation, runtime behavior, resolver source mutation, Web projection implementation, CLI/MCP adapter, provider/live proof, public-sync, push, package execution, or session-sync |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_CERTIFIED_METADATA_ADMISSION_GATE_AND_WEB_PROJECTION_DECISION_T0_T4_FOR_CODEX_2026-06-26.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ASSF_CERTIFIED_METADATA_ADMISSION_GATE_AND_WEB_PROJECTION_DECISION_T0_T4_COMPLETION_2026-06-26.md` | completion review exists | PASS |
| Roadmap state | this roadmap | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | source read by checker; no mutation | PASS |
| Registry Markdown | N/A with reason: no markdown registry companion applies | JSON source only | BLOCKED with reason: no markdown registry companion exists for this JSON-only ASSF entry |
| External evidence digest | N/A with reason: no external artifact applies | repository-local evidence only | N/A with reason |
| System loop interlock | N/A with reason: no system loop surface changed | no system loop mutation | N/A with reason |
| Session continuity | N/A with reason: material commit excludes session-sync | session-sync follows separately if needed | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Query ID | Receipt artifact | JSON path | Required value | Observed value | Status |
|---|---|---|---|---|---|
| ARAM-ADM-R01 | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | `$.certificationState` | `CERTIFIED` | `CERTIFIED` | PASS |
| ARAM-ADM-R02 | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | `$.uatState` | `PASSED` | `PASSED` | PASS |
| ARAM-ADM-R03 | `governance/compat/check_assf_certified_metadata_admission.py` | CLI result | `PASS` | `PASS` | PASS |

## Claim Boundary

This roadmap closes admission-gate and decision work only. It does not certify
a new package, create an instance, mutate Web runtime, implement external
adapters, public-sync, push, or perform session-sync.
