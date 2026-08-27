# CVF External Absorption Conditional Reopen Index

Memory class: FULL_RECORD

Status: ACTIVE_REFERENCE

docType: reference_index

Date: 2026-08-27

## Purpose

Provide the central governed index for external-absorption value that is real
but not ready for immediate CVF implementation, package activation, checker
wiring, runtime mutation, provider execution, public export, or production
claim.

This index exists to prevent a recurring blind spot: a candidate can be
correctly excluded from the current closeout because it is not yet authorized,
but still retain future CVF value. Such a candidate must not disappear into
closeout prose.

## Scope / Applies To

This index applies to external-repository, copied-folder, archived-pack,
external-agent-return, and retained-legacy-source absorption closeouts that
record one of these dispositions:

- `PACKAGE_CANDIDATE`
- `RUNTIME_CANDIDATE`
- `CHECKER_CANDIDATE`
- `DEFERRED`
- `DEFER_WITH_REOPEN_CONDITION`
- `DEFERRED_WITH_REOPEN_CONDITION`
- `VALUE_PARKED`

It does not reopen any lane by itself. It records where value is parked and
what evidence would be needed before a future GC-018, work order, source
verification pass, package promotion review, checker tranche, or runtime value
probe may be proposed.

## Core Distinction

`CONDITIONAL_REOPEN` is not the same thing as low-value rejection.

Rows belong in this index when all of these are true:

- the current tranche was right not to activate the value immediately;
- the value is still plausibly useful to CVF after a concrete condition is met;
- the reopen condition is observable, source-verifiable, or evidence-backed;
- the candidate has an owner surface or pending owner surface;
- the row does not claim implementation authority.

Rows do not belong in this index when direct import was rejected and there is no
remaining CVF-native value, when the source is merely a duplicate of an already
owned CVF surface, or when the only reopen condition is vague operator interest.

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | Seeded from governed CVF review and roadmap artifacts listed in the inline manifest below |
| Enumeration command | `rg -n "PACKAGE_CANDIDATE|RUNTIME_CANDIDATE|CHECKER_CANDIDATE|DEFER_WITH_REOPEN_CONDITION|DEFERRED_WITH_REOPEN_CONDITION|VALUE_PARKED" docs/reviews docs/roadmaps docs/reference` |
| Manifest artifact or inline manifest | inline seed-source manifest table in this file |
| Processing ledger artifact or inline ledger | inline candidate index table in this file |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | inline candidate index table in this file; source rows cite CVF-owned governed artifacts |
| Unresolved items | 0 for the seed set; future rows must record unresolved source gaps explicitly |
| Completion claim boundary | conditional reopen registry only; no runtime, package activation, checker wiring, provider, public, or production expansion |

## Corpus Completeness And Report Integrity

- Corpus task class: conditional reopen seed-source registry for recent external-absorption closeouts.
- Corpus root: governed artifacts under `docs/reviews`, `docs/roadmaps`, and `docs/reference` that already recorded candidate or reopen-condition dispositions.
- Snapshot time: 2026-06-29 local session.
- Enumeration command: `rg -n "PACKAGE_CANDIDATE|RUNTIME_CANDIDATE|CHECKER_CANDIDATE|DEFER_WITH_REOPEN_CONDITION|DEFERRED_WITH_REOPEN_CONDITION|VALUE_PARKED" docs/reviews docs/roadmaps docs/reference`
- Manifest artifact or inline manifest: inline seed-source manifest table in this file.
- Manifest hash: not generated; bounded index seed is path-listed and command-backed in the working session.
- Processing ledger artifact or inline ledger: inline candidate index table in this file.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE
- Reconciliation: manifest=16 source artifacts; ledger_terminal=40 indexed candidate rows plus 1 terminal source-family closure; exclusions=0; unresolved=0
- Unresolved files: 0
- Declared exclusions: none
- Unreadable or unsupported files: none
- Aggregation check: 40 indexed candidate rows and 1 terminal source-family closure are sourced from 16 governed artifacts listed below.
- Drift check: future external absorption closeouts must update this file or state `NO_CONDITIONAL_REOPEN_INDEX_ENTRY_WITH_REASON`.
- Output traceability: each indexed row names the source artifact and owner surface.
- Adversarial verification: direct-import rejection alone is not accepted as no-value closure when CVF-native package, runtime, or checker value remains.
- Corpus verdict: COMPLETE_VERIFIED

## Seed Source Manifest

| Source artifact | Seed role | Processing status |
|---|---|---|
| `docs/reference/CVF_CGE_R1_CODE_INTELLIGENCE_OWNER_SURFACE_MATRIX_2026-06-29.md` | CodeGraph package, runtime, and checker candidate ledgers | READ |
| `docs/reviews/CVF_CGE_R1_CODEGRAPH_FULL_REABSORPTION_REVIEW_2026-06-29.md` | CodeGraph full reabsorption closeout and claim boundary | READ |
| `docs/reviews/CVF_EVEROS_T5_REMAINING_VALUE_AUDIT_AND_LANE_CLOSEOUT_2026-06-28.md` | EverOS remaining runtime-shaped value with reopen conditions | READ |
| `docs/reviews/CVF_TKG_T5_TRUTH_FOUNDATION_REMAINING_VALUE_AUDIT_AND_LANE_CLOSEOUT_2026-06-28.md` | Truth-kernel remaining governance value with reopen conditions | READ |
| `docs/reviews/CVF_PINT_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md` | Provider-intelligence checker candidates parked behind evidence thresholds | READ |
| `docs/reviews/CVF_MSEA_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md` | MinerU checker candidates parked behind evidence thresholds | READ |
| `docs/roadmaps/CVF_AGSK_PACKAGE_CANDIDATE_TRIAGE_ROADMAP_2026-06-29.md` | Agent-skills package, runtime, and checker candidate triage | READ |
| `docs/reviews/CVF_CGE_R2_CODEGRAPH_RESCAN_VALUE_AUDIT_AND_CORRECTION_2026-06-29.md` | CodeGraph second-pass value audit and package-candidate correction | READ |
| `docs/reference/agent_system_skills/registry/entries/cvf-code-intelligence-context-review.json` | CodeGraph metadata-only ASSF package candidate created after CGE-R2 rescan | READ |
| `docs/reference/CVF_MSEA_R85_GOP_Y_CVF_SOURCE_RECONCILIATION_MATRIX_2026-07-10.md` | Terminal 27-file `Gop y CVF` residual-value reconciliation | READ |
| `docs/reference/external_agent_review/CVF_EAIC_KR_R1C_CVF_23_07_FINAL_OWNER_SURFACE_ABSORPTION_DECISION.md` | CVF 23.07 final owner-surface absorption reconciliation; source of the four R1C package/runtime/checker candidate rows below | READ |
| `docs/audits/CVF_PPMCP_R1_PINNED_UPSTREAM_AND_LEGACY_DELTA_REINTAKE_2026-07-25.md` | Pinned 107-file Pancake POS MCP upstream-plus-legacy re-intake; source of five conditionally parked CVF-native pattern rows | READ |
| `docs/roadmaps/CVF_CADP_FULL_KNOWLEDGE_AND_IMPLEMENTATION_ABSORPTION_ROADMAP_2026-08-13.md` | CADP-R1 full finding resolution through T5-R6; source of the six CADP integration rows below | READ |
| `docs/reviews/CVF_CADP_AI_T5_R6_READ_ONLY_AUTHORIZATION_AND_CONSUMER_VALUE_SEAM_COMPLETION_2026-08-15.md` | CADP-AI T5-R6 independently accepted `CLOSED_STOP_LOW_VALUE`; source of the external-readout runtime-seam row and the six-condition objective reopen contract | READ |
| `docs/reference/mcp_gateway/CVF_MCP_KAR_FINAL_EXHAUSTION_RECONCILIATION.md` | MCP-KAR T9 final bounded route reconciliation; source of the T2 schema/conformance and T6 discovery-admission objective reopen rows | READ |
| `docs/audits/CVF_MPA_AI_T0_LOCAL_MEMORY_POISONING_ABSORPTION_AUDIT_2026-08-27.md` | MPA-AI-T0 50-file mixed-origin intake; source of the deferred utility-under-attack evaluation precursor | READ |

## Candidate Index

| Candidate ID | Source lane | Candidate class | Value retained | Current status | Reopen condition | Owner surface | Blocked until reopen |
|---|---|---|---|---|---|---|---|
| `CGE-R2-code-intelligence-runtime-value-probe` | CodeGraph CGE-R1 | `RUNTIME_CANDIDATE` | Graph-assisted impact radius, dependency, route, and test-surface reasoning may reduce manual code-intelligence cost. | `READY_FOR_VALUE_PROBE_NOT_FULL_RUNTIME` | Open a bounded CGE-R2 value probe and prove value over static direct-read analysis, including staleness, receipt, fallback, and no-daemon boundaries. | `docs/reference/CVF_CGE_R1_CODE_INTELLIGENCE_OWNER_SURFACE_MATRIX_2026-06-29.md` | CodeGraph install, MCP server, watcher, daemon, SQLite index, package activation, and production claims |
| `CGE-code-intelligence-package-candidate` | CodeGraph CGE-R1/CGE-R2 | `PACKAGE_CANDIDATE` | `cvf.code_intelligence` package shape is now preserved as metadata-only ASSF candidate `cvf-code-intelligence-context-review`. | `METADATA_CANDIDATE_CREATED_NOT_ACTIVATED` | Reopen for promotion only after CGE-R2 proves useful value, a package promotion review authorizes `PROPOSED` or higher state, and source verification confirms no `freezeAllowed` authority leak. | `docs/reference/agent_system_skills/registry/entries/cvf-code-intelligence-context-review.json`; `docs/reference/CVF_CGE_R1_CODE_INTELLIGENCE_OWNER_SURFACE_MATRIX_2026-06-29.md` | ASSF package root, `SKILL.md`, ACTIVE package state, resolver activation, runtime graph query, automatic freeze authority |
| `CGE-code-intelligence-checker-candidates` | CodeGraph CGE-R1 | `CHECKER_CANDIDATE` | Boundary, graph-staleness, graph-scope, and graph-to-work-order trace guards may harden future graph-assisted work. | `PARKED_UNTIL_CONDITION` | Reopen after CGE-R2 exposes a repeated graph-intelligence defect or after an authorized graph runtime tranche creates checker-owned behavior. | `docs/reference/CVF_CGE_R1_CODE_INTELLIGENCE_OWNER_SURFACE_MATRIX_2026-06-29.md` | Python checker implementation, hook-chain wiring, CI mutation |
| `EVEROS-rebuild-receipt-schema-checker` | EverOS T5 | `CHECKER_CANDIDATE` | Rebuild-operation receipts could validate future generated derived-index rebuilds. | `PARKED_UNTIL_CONDITION` | Reopen only after a source-verified generated derived-index or rebuild implementation emits rebuild operations needing receipt validation. | `docs/reviews/CVF_EVEROS_T5_REMAINING_VALUE_AUDIT_AND_LANE_CLOSEOUT_2026-06-28.md` | Receipt schema, checker implementation, runtime rebuild workflow |
| `EVEROS-timestamp-helper-timezone-checker` | EverOS T5 | `CHECKER_CANDIDATE` | Timestamp and timezone discipline may be useful once persisted memory or index timestamps exist. | `PARKED_UNTIL_CONDITION` | Reopen only after a source-verified memory or index runtime writes persisted timestamps, or a receipt implementation creates timestamp fields. | `docs/reviews/CVF_EVEROS_T5_REMAINING_VALUE_AUDIT_AND_LANE_CLOSEOUT_2026-06-28.md` | Runtime timestamp helper, timezone checker, receipt mutation |
| `EVEROS-derived-row-retention-invalidation` | EverOS T5 | `RUNTIME_CANDIDATE` | Privacy, retention, and redaction invalidation could protect future derived memory rows. | `PARKED_UNTIL_CONDITION` | Reopen only when a source-verified derived index or memory candidate lifecycle implementation exists. | `docs/reviews/CVF_EVEROS_T5_REMAINING_VALUE_AUDIT_AND_LANE_CLOSEOUT_2026-06-28.md` | Derived-index runtime, memory lifecycle mutation, retention enforcement |
| `TKG-provenance-label-enforcement` | Truth Kernel T5 | `CHECKER_CANDIDATE` | Repo-wide provenance labels may become useful after a TKG-owned artifact family adopts them. | `PARKED_UNTIL_CONDITION` | Reopen after at least one TKG-owned artifact family adopts labels and source-verifies label applicability. | `docs/reviews/CVF_TKG_T5_TRUTH_FOUNDATION_REMAINING_VALUE_AUDIT_AND_LANE_CLOSEOUT_2026-06-28.md` | Repo-wide label checker, broad artifact-family mutation |
| `TKG-evidence-record-schema-checker` | Truth Kernel T5 | `CHECKER_CANDIDATE` | TKG evidence fields may serve a future concrete evidence packet. | `PARKED_UNTIL_CONDITION` | Reopen only when a concrete evidence packet needs TKG evidence fields. | `docs/reviews/CVF_TKG_T5_TRUTH_FOUNDATION_REMAINING_VALUE_AUDIT_AND_LANE_CLOSEOUT_2026-06-28.md` | Evidence schema, checker wiring, evidence-packet migration |
| `TKG-obligation-registry-runtime` | Truth Kernel T5 | `RUNTIME_CANDIDATE` | Obligation registry ideas may matter if CVF later authorizes policy or runtime obligation storage. | `PARKED_UNTIL_CONDITION` | Reopen only with explicit operator requirement and fresh GC-018. | `docs/reviews/CVF_TKG_T5_TRUTH_FOUNDATION_REMAINING_VALUE_AUDIT_AND_LANE_CLOSEOUT_2026-06-28.md` | Runtime obligation store, registry source layout, policy execution |
| `PINT-provider-intelligence-route-authority-checker` | Provider Intelligence T3 | `CHECKER_CANDIDATE` | A provider-intelligence route-authority checker may catch overclaims not covered by existing gates. | `PARKED_UNTIL_CONDITION` | Reopen after two or more real overclaim misses are not caught by existing claim, closure, or export gates. | `docs/reviews/CVF_PINT_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md` | New route-authority checker and hook-chain wiring |
| `PINT-dev-mcp-production-route-checker` | Provider Intelligence T3 | `CHECKER_CANDIDATE` | Dev-MCP versus production-route separation may need a checker if repeated overclaims occur. | `PARKED_UNTIL_CONDITION` | Reopen after repeated dev-MCP overclaims or an authorized MCP Model Gateway tranche. | `docs/reviews/CVF_PINT_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md` | MCP production-route checker, gateway behavior claim |
| `PINT-receipt-owner-checker` | Provider Intelligence T3 | `CHECKER_CANDIDATE` | Receipt-owner validation may matter if PINT gains a companion receipt schema. | `PARKED_UNTIL_CONDITION` | Reopen only after PINT receipt companion schema is authorized. | `docs/reviews/CVF_PINT_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md` | Receipt schema, receipt-owner checker |
| `MSEA-document-truth-overclaim-checker` | MinerU MSEA T3 | `CHECKER_CANDIDATE` | Document-truth overclaim detection may harden structured extraction claims. | `PARKED_UNTIL_CONDITION` | Reopen after two or more real overclaim misses are not caught by existing claim, closure, or export gates. | `docs/reviews/CVF_MSEA_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md` | Document-truth checker, hook-chain wiring |
| `MSEA-runtime-readiness-overclaim-checker` | MinerU MSEA T3 | `CHECKER_CANDIDATE` | Runtime readiness overclaim detection may matter if agents claim MinerU is installed or active without proof. | `PARKED_UNTIL_CONDITION` | Reopen after repeated claims that MinerU is installed, active, or production-ready without proof. | `docs/reviews/CVF_MSEA_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md` | Runtime-readiness checker, install/readiness proof surface |
| `MSEA-rag-handoff-checker` | MinerU MSEA T3 | `CHECKER_CANDIDATE` | RAG handoff guard may matter when extraction output feeds ingestion or context claims. | `PARKED_UNTIL_CONDITION` | Reopen after repeated RAG/context bypass claims or an authorized RAG ingestion tranche. | `docs/reviews/CVF_MSEA_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md` | RAG handoff checker, ingestion runtime |
| `AGSK-activation-resolver-runtime` | Agent Skills AGSK | `RUNTIME_CANDIDATE` | Risk-aware package resolver states could become useful executable selection behavior. | `PARKED_UNTIL_CONDITION` | Reopen after at least one package reaches APPROVED state through a later package promotion review. | `docs/roadmaps/CVF_AGSK_PACKAGE_CANDIDATE_TRIAGE_ROADMAP_2026-06-29.md` | Resolver runtime, ACTIVE package selection behavior |
| `AGSK-package-anatomy-checker` | Agent Skills AGSK | `CHECKER_CANDIDATE` | Package anatomy checker may become useful after concrete package fixtures expose a repeated defect or high-risk gap. | `PARKED_UNTIL_CONDITION` | Reopen only after AGSK-T4 and AGSK-T5 close and a concrete repeated defect or high-risk gap is demonstrated by a package instance. | `docs/roadmaps/CVF_AGSK_PACKAGE_CANDIDATE_TRIAGE_ROADMAP_2026-06-29.md` | Checker implementation, hook-chain mutation |
| `R1C-cvf2307-schema-fixture-package-candidates` | EAIC-KR-R1C CVF 23.07 (Conversation G3; Interaction Projection G9) | `PACKAGE_CANDIDATE` | Reusable evidence/decision-record schema shapes and canonical event/adapter/fixture template shapes (41 rows total) with potential CVF package or product value. | `PARKED_UNTIL_CONDITION` | Reopen only after a fresh field-by-field comparison against the current Guard Contract receipt-envelope schema and the agent-workspace design standard demonstrates a concrete reuse gap, and a package promotion review authorizes activation. | `docs/reference/external_agent_review/CVF_EAIC_KR_R1C_CVF_23_07_FINAL_OWNER_SURFACE_ABSORPTION_DECISION.md`; `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/receipt-envelope.contract.ts`; `docs/reference/agent_workspace/README.md` | Package activation, ASSF package root, schema adoption, fixture instantiation |
| `R1C-cvf2307-trajectory-control-runtime-candidate` | EAIC-KR-R1C CVF 23.07 (Conversation G5) | `RUNTIME_CANDIDATE` | Intent-accumulator and escalation-evaluator session-lifecycle concepts (3 rows) with no admission owner, process binding, or runtime proof. | `PARKED_UNTIL_CONDITION` | Reopen only after a future EAIC architecture tranche source-verifies an admission owner and process binding, consistent with EAIC-KR-T4's finding that GAP-05 runtime-enforcement proof remains open. | `docs/reference/external_agent_review/CVF_EAIC_KR_R1C_CVF_23_07_FINAL_OWNER_SURFACE_ABSORPTION_DECISION.md`; `docs/reference/external_agent_invocation_control/CVF_EAIC_KR_T3_OWNER_ARCHITECTURE_AND_THREAT_MODEL_DECISION_PACKET.md` | Runtime wiring, live proof, T5 authorization, moratorium lift |
| `R1C-cvf2307-deny-rule-test-spec-checker-candidates` | EAIC-KR-R1C CVF 23.07 (Conversation G4; Interaction Projection G11) | `CHECKER_CANDIDATE` | Concrete deny-by-default capability-composition rules and adapter/accessibility test-specification invariants (14 rows total). | `PARKED_UNTIL_CONDITION` | Reopen only after a future EAIC or adapter guard tranche demonstrates a repeated defect that these specific invariants would have caught, and a source-verified guard work order is authorized. | `docs/reference/external_agent_review/CVF_EAIC_KR_R1C_CVF_23_07_FINAL_OWNER_SURFACE_ABSORPTION_DECISION.md` | Checker implementation, hook-chain wiring |
| `R1C-cvf2307-accessibility-validation-product-candidate` | EAIC-KR-R1C CVF 23.07 (Interaction Projection G10A) | `PACKAGE_CANDIDATE` | Testable accessibility, evidence-classification, projection-parity, and validation requirements (12 rows). | `PARKED_UNTIL_CONDITION` | Reopen only when a named authorized cvf-web or agent-workspace audit records at least one failed accessibility criterion or unmapped requirement from G10A, identifies its exact source path and current owner, and assigns a remediation owner. | `docs/reference/external_agent_review/CVF_EAIC_KR_R1C_CVF_23_07_FINAL_OWNER_SURFACE_ABSORPTION_DECISION.md`; `docs/reference/agent_workspace/README.md` | UI accessibility implementation, validation automation |
| `R1C-cvf2307-adapter-renderer-product-candidate` | EAIC-KR-R1C CVF 23.07 (Interaction Projection G10B) | `PACKAGE_CANDIDATE` | Provider-neutral adapter normalization, provenance, renderer, and unsupported-version requirements (23 rows). | `PARKED_UNTIL_CONDITION` | Reopen only when an authorized product tranche names one target surface and source verification records at least one required field or event mapping absent from the current agent-workspace or Guard Contract owner. | `docs/reference/external_agent_review/CVF_EAIC_KR_R1C_CVF_23_07_FINAL_OWNER_SURFACE_ABSORPTION_DECISION.md`; `docs/reference/agent_workspace/README.md`; `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/receipt-envelope.contract.ts` | Adapter, renderer, provider mapping, package activation |
| `R1C-cvf2307-integration-seam-product-candidate` | EAIC-KR-R1C CVF 23.07 (Interaction Projection G10C) | `PACKAGE_CANDIDATE` | Owner-preserving CLI, MCP, Guard Contract, Execution Plane, workspace, phase, evidence, and model-gateway integration seams (11 rows). | `PARKED_UNTIL_CONDITION` | Reopen only when a separately authorized implementation tranche selects one named seam and its Source Verification Block identifies an exact current interface symbol or version delta that the G10C material can resolve. | `docs/reference/external_agent_review/CVF_EAIC_KR_R1C_CVF_23_07_FINAL_OWNER_SURFACE_ABSORPTION_DECISION.md`; `docs/reference/agent_workspace/README.md` | Interface mutation, runtime wiring, provider or process action |
| `R1C-cvf2307-roadmap-sequencing-product-candidate` | EAIC-KR-R1C CVF 23.07 (Interaction Projection G12) | `PACKAGE_CANDIDATE` | Source-pack dependency, exit-criteria, and five-phase sequencing material (4 rows). | `PARKED_UNTIL_CONDITION` | Reopen only after explicit operator authorization for an agent-workspace or interaction-projection product roadmap and a fresh GC-018 maps each proposed phase to current CVF owners, dependencies, and exit evidence. | `docs/reference/external_agent_review/CVF_EAIC_KR_R1C_CVF_23_07_FINAL_OWNER_SURFACE_ABSORPTION_DECISION.md`; `docs/reference/agent_workspace/README.md` | Roadmap adoption, implementation release |
| `R1C-cvf2307-worked-example-fixture-candidate` | EAIC-KR-R1C CVF 23.07 (Interaction Projection G14B) | `PACKAGE_CANDIDATE` | Seven worked approval, handoff, freeze/reopen, diff, blocked-call, and provider-neutral session examples with reusable documentation or validation-fixture value. | `PARKED_UNTIL_CONDITION` | Reopen only when an authorized documentation or validation tranche records an exact missing fixture scenario, compares that gap against the seven G14B examples, and a current Agent Handoff, Guard Contract, or agent-workspace owner accepts the mapped fields. | `docs/reference/external_agent_review/CVF_EAIC_KR_R1C_CVF_23_07_FINAL_OWNER_SURFACE_ABSORPTION_DECISION.md`; `docs/reference/agent_workspace/README.md`; `docs/reference/agent_handoff/README.md` | Fixture adoption, schema adoption, package activation |
| `PPMCP-R1-transport-risk-gating-runtime-candidate` | PPMCP-R1 retained legacy transport policy | `RUNTIME_CANDIDATE` | Risk-aware transport gating could add defense in depth beyond each tool contract's current transport allowlist. | `PARKED_UNTIL_CONDITION` | Reopen only after a fresh runtime work order source-verifies a concrete need for risk-aware transport restriction beyond the current `allowedTransports` allowlist check. | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mcp.business.adapter.contract.ts` | Runtime mutation, MCP transport activation, provider execution |
| `PPMCP-R1-action-schema-validation-runtime-candidate` | PPMCP-R1 upstream per-tool discriminated action schemas | `RUNTIME_CANDIDATE` | Runtime parsing of action-specific input variants may close the current opaque-schema validation gap without adopting the source repository's provider-specific implementation. | `PARKED_UNTIL_CONDITION` | Reopen only after an operator-authorized CVF MCP contract tranche source-verifies a concrete invalid-input or schema-drift problem and selects a provider-neutral validation contract; this row does not require Zod. | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mcp.business.adapter.contract.ts` | Dependency installation, runtime validator wiring, MCP transport activation |
| `PPMCP-R1-compact-response-projection-runtime-candidate` | PPMCP-R1 upstream response projection and replay evidence | `RUNTIME_CANDIDATE` | Selective response shaping may reduce MCP result context cost; the source measured 26.8%-63.1% reduction across five tool/action pairs. | `PARKED_UNTIL_CONDITION` | Reopen only after an operator-authorized CVF MCP response-shaping layer exists and a fresh work order source-verifies a concrete context-budget or quota problem this pattern would solve. | Pending future CVF MCP response-shaping owner | Dependency installation, runtime response mutation, production cost claim |
| `PPMCP-R1-display-id-resolver-runtime-candidate` | PPMCP-R1 upstream safe entity targeting | `RUNTIME_CANDIDATE` | Two-stage display-ID resolution with structured ambiguity and state errors may reduce destructive mutation against the wrong entity. | `PARKED_UNTIL_CONDITION` | Reopen only after a fresh runtime work order source-verifies a concrete CVF-native destructive-action-targeting need this pattern would address. | Pending future CVF safe-entity-targeting owner | Domain-specific code import, destructive runtime mutation |
| `PPMCP-R1-replay-regression-checker-candidate` | PPMCP-R1 upstream replay and negative-mutation fixtures | `CHECKER_CANDIDATE` | Replay regression and negative mutation fixtures may harden a future MCP-adjacent adapter test surface. | `PARKED_UNTIL_CONDITION` | Reopen only after a repeated real defect in CVF MCP-adjacent adapter testing demonstrates a gap these patterns would have caught. | Pending future CVF MCP-adjacent test owner | Checker implementation, hook-chain wiring, CI mutation |
| `CADP-AI-contract-kernel` | CADP-R1 F01-F04, F08, F11, F12 | `PACKAGE_CANDIDATE` | CVF-native admission, assignment, distribution, evidence and deterministic-receipt contract logic. | `T1_ACCEPTED_BOUNDED_IMPLEMENTED_BOUNDED_INTERNAL` | Round-6 independent review accepted the hermetic contract against R01-R28; F11 source authentication remains outside T1. T5-R1/R2/R2A extended it with an accepted bounded authority foundation and pure transport-neutral external-readout adapter. | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-admission-distribution-profile.contract.ts`; `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/cadp-external-readout-adapter.contract.ts` | runtime consumer wiring, authenticated evidence ownership, catalog readiness overclaim |
| `CADP-AI-work-order-observation-reconciliation` | CADP-R1 F05/F08/F09/F11 | `RUNTIME_CANDIDATE` | Exact owner-bound evidence plus granted-versus-observed work-order reconciliation across version, action, transport, resource, credentials, expiry, invocation and retry limits. | `T2A_ACCEPTED_BOUNDED_IMPLEMENTED_BOUNDED_INTERNAL` | T2A-R1 is independently accepted at material commit `944bfe852131f2ac0aa403254c33157820ba3ee5`; grant v1 remains fail-closed and additive v2 binds authority to committed private-provenance Git blobs with durable local replay state. | Guard Contract repository owner plus committed grant and SQLite replay state | provider/live action, cross-runtime determinism, trusted-evidence readiness |
| `CADP-AI-downstream-consumer-adapters` | CADP-R1 F02/F06/F08 | `RUNTIME_CANDIDATE` | Internal execution-plane/model-gateway consumption and bounded SaaS constraint metadata without authority widening. | `T3A_T3B_ACCEPTED_BOUNDED_IMPLEMENTED_BOUNDED_INTERNAL` | T3A independently accepts only the hermetic non-executing Execution Plane eligibility consumer; T3B independently accepts only provider-neutral constraint metadata with no secret resolution, provider call, or execution authority. | Guard Contract plus `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/cadp.capability.consumer.contract.ts` and `EXTENSIONS/CVF_MODEL_GATEWAY/src/cadp.constraint.projection.contract.ts` | provider calls, credentials, CLI/MCP, SaaS execution, trusted-evidence readiness, cross-runtime determinism |
| `CADP-AI-negative-fixture-and-drift-checker` | CADP-R1 F09 | `CHECKER_CANDIDATE` | Cross-owner negative fixtures and schema/contract drift detection machine-enforce the accepted bounded CADP invariants. | `T4_ACCEPTED_BOUNDED_STANDALONE_UNWIRED_IMPLEMENTED_BOUNDED_INTERNAL` | T4 independently accepted the strict fixture, read-only checker, focused negative suite, and package-boundary probes at material commit `7dfee6e4d`; it remains standalone and unwired. | `governance/compat/check_cadp_authority_boundary_drift.py`; `governance/compat/fixtures/cadp_authority_boundary_contract.v1.json`; focused checker tests | hook/autorun/CI wiring, full TypeScript compiler equivalence, provider/live behavior, public/deploy/production |
| `CADP-AI-authentication-composition` | CADP-AI T5-R3/R4/R5 | `RUNTIME_CANDIDATE` | Fail-closed authentication-composition wrapper and literal-`false` CADP authorization projection over the existing route-governance-proof owner. | `T5_R4_R5_ACCEPTED_BOUNDED_IMPLEMENTED_FAIL_CLOSED_UNREACHABLE` | T5-R4 selects the `CADP_FAIL_CLOSED_ON_INVALID_TOKEN` contract at `af2f425d8`; T5-R5 implements and tests it at `6284e5bd1`. Real and hermetic, but has zero current non-test caller. | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/cadp-authentication-policy.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/cadp-authorization.ts` | CADP route registration, transport activation, CLI/MCP invocation, credential delegation |
| `CADP-AI-external-readout-runtime-seam` | CADP-AI T5-R6 | `RUNTIME_CANDIDATE` | A read-only CADP external-readout runtime seam (route, transport, CADP authorization owner, and durable receipt/operator destination) that would connect the accepted contract/authentication foundations above to an external or internal consumer. | `T5_R6_CLOSED_STOP_LOW_VALUE_PARKED_DEMAND_GATED` | Independently accepted `STOP_LOW_VALUE` at material commit `83491ade1`: zero current non-test consumer, no authoritative runtime metadata owner, no durable receipt/operator destination, and a value/cost margin (`base -22`, `sensitized -26`) far below the required `+12` threshold. Reopen requires all six conjunctive conditions in the Objective Reopen Contract below. | `docs/reviews/CVF_CADP_AI_T5_R6_READ_ONLY_AUTHORIZATION_AND_CONSUMER_VALUE_SEAM_COMPLETION_2026-08-15.md` | CADP route registration, MCP/CLI transport activation, CADP authorization-owner wiring, durable receipt/operator destination, provider/live/network, credentials, public sync, deployment, production |
| `MCP-KAR-T2-schema-conformance-repair` | MCP-KAR T0/T2 | `CHECKER_CANDIDATE` | Four external schema-repair candidates and five dependent positive fixtures retain bounded conformance value, but have no named non-test consumer or accepted schema owner. | `STOPPED_NO_NAMED_CONSUMER` | Reopen only when all five T2 gates pass together: an exact non-test consumer names the schema identity; a current owner accepts responsibility; an exact field-level gap remains after T1/T4/T5/T7/T8; a smallest manifest is operator-selected; and deterministic fail-closed negative proof is specified. | `docs/reviews/CVF_MCP_KAR_T2_SCHEMA_CONSUMER_OWNER_VALUE_DECISION_WORKER_RETURN_2026-08-23.md`; `docs/reference/mcp_gateway/CVF_MCP_KAR_FINAL_EXHAUSTION_RECONCILIATION.md` | schema adoption or repair, checker wiring, runtime/package/provider behavior |
| `MCP-KAR-T6-bound-discovery-admission` | MCP-KAR T0/T6 | `RUNTIME_CANDIDATE` | A bound discovery-admission snapshot with digest, freshness, and drift quarantine may retain value only after a durable owner and consumer exist. | `STOPPED_NO_BOUND_ADMISSION_SNAPSHOT_OWNER` | Reopen only when a current non-test source names and consumes a repository-owned bound admission snapshot/digest/freshness identity at an exact path and symbol, an explicit owner accepts durable-state responsibility, and an operator-selected work order pins deterministic drift/quarantine proof. | `docs/reviews/CVF_MCP_KAR_T6_T8_RESIDUAL_PROTOCOL_OWNER_VALUE_DECISION_WORKER_RETURN_2026-08-24.md`; `docs/reference/mcp_gateway/CVF_MCP_KAR_FINAL_EXHAUSTION_RECONCILIATION.md` | durable state, discovery admission runtime, transport, filesystem, provider/live behavior |
| `RSPB-capability-preflight-bootstrap-runtime-and-checker-candidates` | RSPB-AI-T0 through T4 reverse-skill/Capability Preflight & Bootstrap mixed-origin intake | `IMPLEMENTED_BOUNDED_AND_CONDITIONAL_RUNTIME` | The read-only Environment Snapshot is implemented in the existing doctor/pre-dispatch seam. Guard Contract now owns both the Controlled Acquisition Contract Kernel and a Route/Readiness Evidence Kernel covering two-stage escalation, material-authority ambiguity, rationale/fallback visibility, and fail-closed readiness precedence. | `PROCEED_SELECTIVELY_RUNTIME_STAGED_T4_ROUTE_READINESS_ACCEPTED` | Knowledge and three selected runtime-value clusters are materialized. Route/READY outputs and acquisition authorization remain non-executing evidence; no candidate router, installer, or transport was imported. Reopen executor work only for named demand with approved authority and evidence destination. | `docs/reviews/CVF_RSPB_AI_T4_CAPABILITY_ROUTE_AND_READINESS_EVIDENCE_KERNEL_COMPLETION_2026-08-16.md` | no direct import; no acquisition execution; no MCP/CLI activation; no provider/live/network, credential access, public sync, deployment, or production |
| `MPA-AI-utility-under-attack-evaluation-precursor` | MPA-AI-T0 local mixed-origin memory-poisoning intake | `RUNTIME_CANDIDATE` | Utility-preserving adversarial evaluation covering benign correct untrusted evidence, retrieval-versus-reader separation, conflict, staleness, duplicate lineage, cross-scope isolation, and action-time revalidation. | `DEFERRED_HIGH_POTENTIAL_FORWARD_SIGNAL` | Reopen Gate UAA-G1 only after the EACQ-FV roadmap receives external adversarial review and operator acceptance; G1 must source-verify owners, ground truth, formulas, budgets, and provider-free stop rules. UAA-G2 and UAA-G3 require separate gate evidence and authority. | `docs/roadmaps/CVF_EXTERNAL_AGENT_CODING_QUALITY_AND_FORWARD_VALUE_ABSORPTION_ROADMAP_2026-08-27.md`; future named evaluation owner | No direct import, runtime mutation, threshold claim, model/provider run, public sync, deployment, production, or security-effectiveness claim |

## CADP External Runtime Objective Reopen Contract

This contract governs only the `CADP-AI-external-readout-runtime-seam` row
above. It does not govern the other four CADP rows, which remain accepted
bounded internal foundations (`IMPLEMENTED_BOUNDED_INTERNAL` or
`IMPLEMENTED_FAIL_CLOSED_UNREACHABLE`).

Reopen CADP external runtime expansion (route registration, MCP/CLI transport
activation, a CADP authorization owner, or a durable receipt/operator
destination) only when one fresh, operator-approved governed work order proves
all six of the following conjunctively:

1. a named current non-test consumer;
2. a concrete blocked workflow and operator-visible outcome;
3. an authoritative metadata/authorization owner, not caller-supplied truth;
4. a bounded receipt or operator destination;
5. base and sensitized value-cost margins each at least `+12`;
6. a fresh operator-approved work order scoped to the smallest required
   surface.

Absent all six conditions, this row remains `PARKED_DEMAND_GATED`. This is a
deliberate stop with an explicit, evidence-gated reopen path, not a
`pending implementation` or `runtime work remains automatically required`
disposition. See `docs/roadmaps/CVF_CADP_FULL_KNOWLEDGE_AND_IMPLEMENTATION_ABSORPTION_ROADMAP_2026-08-13.md`
`Objective Reopen Contract` for the paired roadmap-side statement of the same
six conditions.

## Terminal Source-Family Closures

| Source family | Source evidence | Terminal status | Value retained | Reopen disposition |
| --- | --- | --- | --- | --- |
| `Gop y CVF` EI-01 through EI-13 | `docs/reference/CVF_MSEA_R85_GOP_Y_CVF_SOURCE_RECONCILIATION_MATRIX_2026-07-10.md` | `RECONCILED_NO_REOPEN` | EI-01 through EI-04 closed in R65A; EI-06 through EI-10 are owned by R85 CVF-native references; EI-11 through EI-13 retain reject/no-new-value decisions | NO_CONDITIONAL_REOPEN_INDEX_ENTRY_WITH_REASON: useful docs/schema value is absorbed; runtime/checker expansion lacks a current source-backed value case and requires a fresh independent problem if ever proposed |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| Recent closeout lessons | Conditional reopen index itself hardens the distinction between low-value rejection and valuable-but-not-now candidates. | `DOCTRINE_ADAPTED` | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CONDITIONAL_REOPEN_INDEX.md` | Keep as active reference and require future closeouts to update it. | No runtime or package behavior |
| CodeGraph package shape | Code-intelligence package candidate enriches CVF package surfaces as a metadata-only ASSF candidate. | `PACKAGE_CANDIDATE` | `docs/reference/agent_system_skills/registry/entries/cvf-code-intelligence-context-review.json` | Promotion requires CGE value proof and ASSF package promotion review | No package activation from this index |
| CodeGraph services and adapters | Graph-assisted context, impact, dependency, staleness, query-planner, direct-read fallback, and fixture-blueprint concepts may have practical CVF utility. | `RUNTIME_CANDIDATE` | Pending CGE-R2 value-probe roadmap | Open bounded value probe before any install, index, MCP, watcher, daemon, or CI work | No runtime activation from this index |
| CodeGraph guards plus PINT, MSEA, TKG, EverOS checker ideas | Several checker candidates may become useful after repeated misses or source-owned behavior exists. | `CHECKER_CANDIDATE` | Pending future `governance/compat` checker work orders | Reopen only when row-specific evidence thresholds are met | No checker wiring from this index |
| Direct external implementations | Direct package, adapter, runtime, MCP, daemon, and public-interface import remains rejected without fresh CVF authorization. | `REJECT_DIRECT_IMPORT` | CVF-native rewrite lanes only | Use this index to preserve value without copying foreign implementation authority. | Direct import remains blocked |
| Already-owned duplicate material | Rows with no remaining package, runtime, checker, or doctrine delta stay outside this index. | `NO_PACKAGE_OR_RUNTIME_VALUE` | Existing CVF owner surfaces | State no-index reason in the closeout. | No runtime or package behavior |
| MPA utility-under-attack cluster | Benign-untrusted utility and retrieval/reader separation retain forward evaluation value even though the related Memory/Truth risk is already owned. | `RUNTIME_CANDIDATE` | EACQ-FV roadmap and future named evaluation owner | Apply UAA-G1, then G2, and open G3 only with separate authority. | G1/G2 provider-free; no runtime activation from this index |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| Existing indexed candidates | existing governed owner paths in the Candidate Index | CONFIRMED_EXISTING | PPMCP-R1 does not alter the evidence thresholds or authority of the prior 25 rows | retain the prior rows and add only the five PPMCP-R1 rows above |
| MPA utility-under-attack cluster | `docs/audits/CVF_MPA_AI_T0_LOCAL_MEMORY_POISONING_ABSORPTION_AUDIT_2026-08-27.md`; current Memory/Truth/EAFR owners | NEW_FINDING | underlying poisoning risk overlaps, but the composed utility-preserving evaluation precursor and forward-value lesson are not owned by those risk surfaces | add the conditional row and route through EACQ-FV review-first gates |
| `Gop y CVF` EI-01 through EI-05 | `docs/reference/CVF_MSEA_R64_EXTERNAL_CRITIQUE_INTAKE_CLASSIFICATION_MATRIX_2026-07-07.md` and R65A closure | CONFIRMED_EXISTING | prior public-drift treatment remains authoritative | record terminal source-family closure |
| `Gop y CVF` EI-06 through EI-10 | `docs/reference/agent_build_loop/`; `docs/reference/public_trust/`; `docs/guides/CVF_5_MINUTE_TRUST_DEMO.md` | ENRICH_EXISTING | R85 adds bounded CVF-native owner surfaces without runtime/checker admission | close source-family row with no conditional reopen |
| `Gop y CVF` EI-11 through EI-13 | `docs/reference/CVF_MSEA_R85_GOP_Y_CVF_SOURCE_RECONCILIATION_MATRIX_2026-07-10.md` | NO_NEW_VALUE | reject and structural-only decisions remain terminal | no candidate-index row |

## Future Update Rule

Every future external absorption closeout that records `PACKAGE_CANDIDATE`,
`RUNTIME_CANDIDATE`, `CHECKER_CANDIDATE`, `DEFERRED`,
`DEFER_WITH_REOPEN_CONDITION`, `DEFERRED_WITH_REOPEN_CONDITION`, or
`VALUE_PARKED` must do exactly one of these before closure:

- add or update the matching row in this index;
- cite the existing row in this index and state why it remains current;
- state `NO_CONDITIONAL_REOPEN_INDEX_ENTRY_WITH_REASON` because the value was
  fully adapted, rejected with no remaining CVF-native value, or is already
  owned by another governed index.

Do not treat "not authorized in this tranche" as a value decision. Direct
import may be rejected while CVF-native runtime, package, checker, or doctrine
value remains conditionally reopenable.

## Selection Rule Before Next Repo

Before proposing the next external repository absorption target, the reviewer
must scan this index for rows whose reopen condition is now met. If one or more
rows are newly eligible, the reviewer must decide whether a bounded value
probe or GC-018 should outrank a new external repo.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator correction -> external absorption closeout blind-spot repair -> central conditional reopen index -> future GC-018 or work order only after condition evidence |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py` |
| Owner surface | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CONDITIONAL_REOPEN_INDEX.md` |
| Disposition | ADAPT operator correction into central index for conditionally parked external-absorption value |
| Claim boundary | reference index only; no implementation, runtime, package activation, checker wiring, provider, public, or production claim |

## Epistemic Process Block

Epistemic Process Applicability: EPISTEMIC_PROCESS_NA_WITH_REASON: reference
index and governance routing artifact; it records already-governed candidate
conditions and does not assert a new empirical runtime, provider, public, or
production behavior claim.

Expected Result / Prediction: N/A - conditional reopen registry definition.

Evidence Comparison: N/A with reason: row eligibility must be proven by a
future GC-018, value probe, work order, or source-verification pass before any
candidate is implemented.

Contradiction Or Gap Disposition: N/A with reason: if a row's condition becomes
stale, a future reviewer must update or close the row in this index.

Claim Update: establishes an active reference index for conditionally
reopenable external-absorption value.

## Claim Boundary

This index records parked candidate value and reopen conditions only. It does
not authorize implementation, package activation, checker wiring, runtime
mutation, provider calls, MCP activation, public sync, or production readiness.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex reviewer/closer role |
| Provider or surface | local workspace |
| Session or invocation | EACQ-FV roadmap design and MPA conditional-reopen repair, 2026-08-27 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | `rg`; `Get-Content`; `apply_patch`; governance gates |
| Target paths | EACQ-FV roadmap and this conditional reopen index |
| Allowed scope source | operator approval to design external-agent quality and deferred-value upgrades, with external critique before implementation |
| Before status evidence | clean worktree at MPA-AI-T0 closure `19c223ce06d579cfe16fb7feb4ff8996363797ab` |
| After status evidence | MPA utility evaluation precursor is indexed with three gated reopen stages; implementation remains closed pending critique and operator acceptance |
| Diff evidence | `git diff --name-status` before material commit |
| Approval boundary | roadmap and conditional-reopen preservation only; no implementation |
| Claim boundary | no runtime, package activation, checker wiring, provider, public, deployment, production, or effectiveness claim |
| Agent type | dispatcher/source reviewer |
| Invocation ID | `eacq-fv-roadmap-design-2026-08-27` |
| Expected manifest | EACQ-FV roadmap and this conditional reopen index |
| Actual changed set | EACQ-FV roadmap and this conditional reopen index |
| Manifest delta | MATCH |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
