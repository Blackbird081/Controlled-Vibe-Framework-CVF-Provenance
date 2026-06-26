# CVF Review: ASSF Web Projection Schema Mapping Decision

Memory class: FULL_RECORD
Status: COMPLETE_PENDING_REVIEW
Date: 2026-06-26
docType: review
batchId: ASSF-WEBPROJ-T0
executionBaseHead: `3d983897`
dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_WEB_PROJECTION_SCHEMA_MAPPING_DECISION_FOR_CODEX_2026-06-26.md`
route: SINGLE_AGENT_MULTI_ROLE
decisionDisposition: `OPEN_WEB_PROJECTION_IMPLEMENTATION_WORK_ORDER`

## Purpose

Decide the source-verified Web projection schema and mapping posture for ASSF
certified package metadata before any Web runtime, Web data, adapter, package
instance, registry, generated-index, resolver, or public-sync mutation.

## Target / Source

Target decision surface:

- `docs/reviews/CVF_ASSF_WEB_PROJECTION_SCHEMA_MAPPING_DECISION_2026-06-26.md`
- `docs/reviews/CVF_ASSF_WEB_PROJECTION_SCHEMA_MAPPING_DECISION_COMPLETION_2026-06-26.md`

Dispatch authority:

- `docs/baselines/CVF_GC018_ASSF_WEB_PROJECTION_SCHEMA_MAPPING_DECISION_2026-06-26.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_WEB_PROJECTION_SCHEMA_MAPPING_DECISION_FOR_CODEX_2026-06-26.md`

## Scope / Methodology

This review used source inspection only. It verified the ASSF Web projection
contract, certification lifecycle contract, generated ASSF skill index, one
certified registry entry, and the current CVF Web type/mapping/read surfaces.
No implementation files were changed.

## Source Inventory

| File | Action |
|---|---|
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_WEB_PROJECTION_SCHEMA_MAPPING_DECISION_FOR_CODEX_2026-06-26.md` | READ |
| `docs/baselines/CVF_GC018_ASSF_WEB_PROJECTION_SCHEMA_MAPPING_DECISION_2026-06-26.md` | READ |
| `docs/reference/guard_orientation/README.md` | READ |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ |
| `docs/reference/agent_system_skills/CVF_ASSF_WEB_PROJECTION_CONTRACT.md` | SOURCE_VERIFIED |
| `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | SOURCE_VERIFIED |
| `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | SOURCE_VERIFIED |
| `docs/reference/agent_system_skills/generated/skill-index.json` | SOURCE_VERIFIED |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/types/skill.ts` | SOURCE_VERIFIED |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/frontdoor-skills.ts` | SOURCE_VERIFIED |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/skill-template-map.ts` | SOURCE_VERIFIED |

## Findings / Position

1. ASSF already has a certified metadata source suitable for a future Web
   projection decision. The registry entry `cvf-dispatch-quality-reviewer`
   declares `uatState` as `PASSED` and `certificationState` as `CERTIFIED`;
   the generated ASSF index carries the same values and a metadata-only claim
   boundary.
2. The current Web `Skill` type is a presentation/read model with corpus and
   front-door fields. It does not currently carry ASSF certification fields.
   The future Web projection must add explicit optional ASSF projection fields
   instead of overloading `corpusClass`.
3. The existing Web front-door reader maps Web skills into search records. It
   should remain a read/search adapter unless a future implementation work
   order separately source-verifies a `SkillRecord` schema expansion.
4. The existing `skill-template-map` surface is UI linkage only. It must not
   own, derive, or imply certification.
5. External CLI/MCP adapter work remains deferred. A Web projection can display
   source-backed metadata, but it must not authorize external-agent use.

## Schema And Mapping Decision Matrix

| Decision item | Decision | Source basis | Implementation posture |
|---|---|---|---|
| Projection class vocabulary | Use `CERTIFIED_PACKAGE_PROJECTION`, `PACKAGE_CANDIDATE`, `LEGACY_REFERENCE_ONLY`, `DUPLICATE_OR_SUPERSEDED`, and `REJECTED_WITH_REASON` as the Web presentation classification vocabulary. | Web projection contract classification table. | Future Web implementation may add `assfProjectionClass?: string` or a stricter union type after source-verified implementation dispatch. |
| Certification state | Carry ASSF `certificationState` as a separate projected field; do not alias it to Web `corpusClass`. | Lifecycle contract keeps `corpusClass` and `certificationState` separate until bridge implementation. | Future Web implementation may add `certificationState?: string` to `Skill`. |
| UAT state | Carry ASSF `uatState` as a separate projected field when available. | Lifecycle contract requires `uatState: PASSED` before `certificationState: CERTIFIED`. | Future Web implementation may add `uatState?: string` to `Skill`. |
| Review evidence | Carry `reviewArtifacts` as projected evidence links or strings, not as runtime authority. | ASSF registry and generated index include review metadata; generated index is metadata-only. | Future Web implementation may add `reviewArtifacts?: string[]` or a typed evidence structure. |
| Canonical root | Carry `canonicalRoot` for traceability from Web display back to ASSF registry source. | Generated ASSF index exposes `canonicalRoot`. | Future Web implementation may add `canonicalRoot?: string` to `Skill`. |
| Adapter fields | Carry `externalCliMcpDisposition` and `adapterContract` only as deferred/claim-boundary display metadata. | Generated ASSF index marks adapter fields as deferred and metadata-only. | Future Web implementation may display these fields but must not build an adapter. |
| Web public data | Treat the Web public skills-index artifact as the current data artifact that would need an implementation path. | Web fetchers read `/data/skills-index.json`; current Web source search found corpus fields only. | Future work order must source-verify whether this artifact is generated or hand-maintained before mutation. |
| Front-door search record | Do not change `SkillRecord` as part of this decision. | `frontdoor-skills.ts` currently maps search-oriented fields only. | Future implementation should keep this unchanged unless UI search requires projected certification filtering. |
| Template map | Keep `templateToSkillMap` as UI linkage only. | Web projection contract says mapping does not certify; source header names input/knowledge linkage. | No certification logic belongs in this map. |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| Web projection vocabulary exists | `docs/reference/agent_system_skills/CVF_ASSF_WEB_PROJECTION_CONTRACT.md` | lines 80-91 | `CERTIFIED_PACKAGE_PROJECTION` | ASSF Web projection contract | VALUE_SET | ACCEPT |
| Web mapping must not certify | `docs/reference/agent_system_skills/CVF_ASSF_WEB_PROJECTION_CONTRACT.md` | lines 93-103 | `skill-template-map.ts` | ASSF Web projection contract | LITERAL_INVARIANT | ACCEPT |
| Web display must not self-certify | `docs/reference/agent_system_skills/CVF_ASSF_WEB_PROJECTION_CONTRACT.md` | lines 105-110 | No-Self-Certification Invariant | ASSF Web projection contract | LITERAL_INVARIANT | ACCEPT |
| Generated ASSF index is metadata-only | `docs/reference/agent_system_skills/generated/skill-index.json` | lines 1-3 | `claimBoundary` | ASSF generated skill index | LITERAL_INVARIANT | ACCEPT |
| Certified package metadata exists | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | lines 69-72 | `certificationState` | ASSF registry entry | VALUE_SET | ACCEPT |
| Generated index carries certified state | `docs/reference/agent_system_skills/generated/skill-index.json` | lines 14-16 and 92-94 | `certificationState` | ASSF generated skill index | VALUE_SET | ACCEPT |
| Adapter fields remain deferred | `docs/reference/agent_system_skills/generated/skill-index.json` | lines 8-25 | `externalCliMcpDisposition` | ASSF generated skill index | VALUE_SET | ACCEPT |
| Certification requires UAT pass first | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | lines 84-91 | `uatState` | ASSF certification lifecycle contract | LITERAL_INVARIANT | ACCEPT |
| Web bridge is separate implementation work | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | lines 176-184 | `certificationState` | ASSF certification lifecycle contract | LITERAL_INVARIANT | ACCEPT |
| Web `Skill` has current corpus/front-door fields | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/types/skill.ts` | lines 7-34 | `Skill` | CVF Web Skill type | EXISTS | ACCEPT |
| Web `SkillIndexMeta` has current corpus counters | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/types/skill.ts` | lines 42-50 | `SkillIndexMeta` | CVF Web Skill type | EXISTS | ACCEPT |
| Web front door reads the public skill index | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/frontdoor-skills.ts` | lines 28-36 | `fetchFrontDoorSkillRecords` | CVF Web front-door reader | EXISTS | ACCEPT |
| Web front-door reader maps search fields | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/frontdoor-skills.ts` | lines 14-25 | `toSkillRecord` | CVF Web front-door reader | EXISTS | ACCEPT |
| Web template map is UI linkage | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/skill-template-map.ts` | lines 1-13 and 26-41 | `templateToSkillMap` | CVF Web template map | LITERAL_INVARIANT | ACCEPT |
| Web source search found current corpus fields | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/types/skill.ts` | lines 27-30 and 42-50 | `corpusClass` | CVF Web Skill type | EXISTS | ACCEPT |

## Negative Search And Collision Discipline

Command-backed negative search was limited to the current Web type and Web
public skill-index artifact:

`rg -n "certificationState|uatState|reviewArtifacts" <current Web type> <current Web public skill-index artifact>`

Result token: `NO_MATCHES_IN_WEB_TYPE_OR_PUBLIC_INDEX`.

This is not a repo-wide absence claim. It only supports the decision that the
future bridge must add or derive ASSF projection fields on the Web side.

## Risk / Corrective Action

| Risk | Disposition | Corrective action |
|---|---|---|
| Web `corpusClass` could be mistaken for ASSF certification | ACCEPTED_RISK_BOUNDED | Future implementation must add separate ASSF projection fields and keep `corpusClass` as corpus governance metadata. |
| Public Web data mutation path is not yet source-verified | ACCEPTED_RISK_BOUNDED | Future implementation work order must identify whether the Web public skills-index artifact is generated or hand-maintained before editing it. |
| Adapter metadata could be mistaken for adapter availability | ACCEPTED_RISK_BOUNDED | Future Web copy and schema must carry claim-boundary language; adapter implementation remains a separate work order. |
| Template mapping could be promoted beyond UI linkage | REJECTED | Keep `skill-template-map` out of certification ownership. |

## Decision / Recommendation

Recommendation: `OPEN_WEB_PROJECTION_IMPLEMENTATION_WORK_ORDER`.

Recommended next work order shape:

- Implement optional ASSF projection fields in the Web `Skill` read model.
- Source-verify the Web public data production path before mutating the public
  skill index artifact.
- Map certified ASSF package metadata from canonical ASSF registry/generated
  metadata into read-only Web presentation fields.
- Keep `corpusClass` and `certificationState` separate.
- Keep `skill-template-map` as UI linkage only.
- Keep CLI/MCP adapter work deferred to a later adapter-contract decision.

## External Knowledge Intake Routing

Standard citation:
`docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md`

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Public/simple CVF vocabulary |
| Chain map route | local governed source-verification lane to decision review. |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/run_agent_autorun_workflow_gate.py` |
| Owner surface | CVF provenance workspace. |
| Disposition | N/A with reason: no external knowledge was absorbed. |
| Claim boundary | No web browsing, connector evidence, provider proof, or external runtime state is used as authority. |

## Dual Agent Surface Matrix

| Surface | Consumer | Disposition | Boundary |
|---|---|---|---|
| ASSF registry/generated metadata | Codex reviewer/worker | READ_ONLY | Decision evidence only. |
| CVF Web type/data/mapping files | Codex reviewer/worker | READ_ONLY | Source verification only; no Web mutation. |
| External-agent CLI/MCP adapter | Future external agent | DEFERRED_WITH_REASON | Adapter is not implemented or authorized by this decision. |
| Public-sync repository | Public readers | N/A with reason | No public-sync or push authorized. |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | Decision-only review artifacts. |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE: decision review only. |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed. |
| actionEvidence | ACTION_EVIDENCE_PRESENT: source inspection commands and review artifact creation only. |
| invocationBoundary | No runtime, provider, adapter, package, or Web invocation. |
| interceptionBoundary | N/A with reason: no interception or proxy surface was used. |
| claimLanguage | Decision recommends future work order only; no implementation claim. |
| forbiddenExpansion | No package instance, certification decision, Web runtime mutation, adapter mutation, generated-index mutation, resolver mutation, public-sync, or push. |

## Epistemic Process Block

### Expected Result / Prediction

ASSF certified metadata should be source-ready for read-only Web projection, but
the current Web type and public data should require a separate implementation
bridge before carrying ASSF certification fields.

### Evidence Comparison

Evidence matched the prediction: ASSF registry/generated metadata contains a
certified package record, while the current Web type and public data carry corpus
metadata rather than ASSF certification metadata.

### Contradiction Or Gap Disposition

No blocking contradiction was found. The remaining gap is implementation-path
selection for the Web public data artifact, which is assigned to the recommended
next work order.

### Claim Update

The decision is updated from "schema/mapping unknown" to
`OPEN_WEB_PROJECTION_IMPLEMENTATION_WORK_ORDER`.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: This is a private provenance decision review. No public-sync batch or
public catalog export was authorized.

## Agent Operation Trace Block

| Field | Value |
|---|---|
| actor | Codex |
| rolePattern | SINGLE_AGENT_MULTI_ROLE |
| dispatchWorkOrder | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_WEB_PROJECTION_SCHEMA_MAPPING_DECISION_FOR_CODEX_2026-06-26.md` |
| executionBaseHead | `3d983897` |
| materialMutation | Review artifacts only |
| forbiddenScopeObserved | Yes |

## Claim Boundary

This review does not certify a new package, create a package instance, mutate
the Web runtime, mutate Web public data, mutate ASSF registry/generated sources,
implement an adapter, authorize external-agent use, run live provider proof,
push to public-sync, or close a public export.
