# CVF PRG-T0 Product Spec External Package Absorption Roadmap

Memory class: FULL_RECORD

Status: ROADMAP_READY_FOR_OPERATOR_APPROVAL

docType: roadmap

Date: 2026-06-28

Owner: Codex

rawMemoryReleased: false

External knowledge intake routing: REQUIRED

## Authorization / Decision

User instruction redirected the next move to absorb value from the external
repository `https://github.com/hieubui2409/product-spec` and the
operator-provided folder `CVF_Product_Requirement_Governance/`.

Decision:

`ACCEPT_PACKAGE_AS_T1_SEED_WITH_HARDENING_REQUIRED`.

Selected implementation lane:

none in T0.

Recommended next decision:

`AUTHOR_PRG_T1_GC018_FOR_PACKAGE_PROMOTION_AND_VALIDATOR_FOUNDATION`.

## Purpose

Audit the operator-provided Product Requirement Governance package in substance,
not as a filename inventory, and decide whether it should become a CVF-owned
absorption lane.

The package is fit for CVF as a seed because it captures the strongest
architecture primitives observed in `product-spec`: product requirement graph,
frontmatter control, deterministic validation versus LLM judgment, decision
receipts, no-silent-reversal, read-only critique, impact analysis, traceability,
and product-spec-to-work-order handoff.

The package is not ready to become a canonical reference surface yet. It must be
hardened through CVF provenance, license boundary, status-token alignment,
fixtures, validator design, receipt schemas, and placement decisions before it
is promoted out of the root untracked folder.

## Scope / Target / Owner Boundary

In scope:

- audit every phase of `CVF_Product_Requirement_Governance/`;
- compare the package against the pinned external repository commit
  `b33fc6ff01546e1d1b25363edd9bea7e32218c59`;
- classify package content as absorb, adapt, defer, reject, or block;
- define the correct CVF owner surfaces and next tranche;
- preserve the license and external-source boundary.

Out of scope:

- copying AGPL code from `product-spec` into CVF;
- promoting the root package folder directly into canonical reference authority;
- implementing validators, runtime, UI, provider proof, public-sync, package
  activation, or certification;
- moving public-facing artifacts from the provenance workspace;
- claiming product-management replacement, production readiness, live provider
  behavior, or universal requirement governance.

## Non-Goals

This roadmap does not:

- certify `CVF_Product_Requirement_Governance/` as a governed CVF reference
  surface;
- migrate the package into `docs/reference/` or another owner path;
- create, edit, or run product requirement validators;
- define final PRG storage, registry, receipt, or generated aggregate layout;
- authorize copied source code from the external AGPL repository;
- authorize UI, provider/live, package-release, or public-sync work.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external-agent returned output |
| Chain map route | External-agent returned package plus external repo evidence -> classify items -> map value to CVF owner surfaces -> open GC-018/work order before implementation |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_agent_absorption_table.py` for later review/audit absorption packets |
| Owner surface | This roadmap for T0 decision; future `docs/reference/product_requirement_governance/` or equivalent owner after PRG-T1 promotion |
| Disposition | ADAPT as CVF Product Requirement Governance seed; reject direct code/runtime/Claude-specific absorption |
| Claim boundary | External package and repo are advisory inputs only; CVF authority starts only after governed promotion, source verification, and gates |

## Source Authority And External Evidence Boundary

| Source | Role | Verification status |
|---|---|---|
| `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | canonical routing for external/corpus/repo input | SOURCE_VERIFIED |
| `docs/reference/guard_orientation/README.md` | task-class guard map for external knowledge absorption | SOURCE_VERIFIED |
| `CVF_Product_Requirement_Governance/` | operator-provided external-agent package under audit | EXTERNAL_INPUT_NOT_AUTHORITY |
| `https://github.com/hieubui2409/product-spec` at commit `b33fc6ff01546e1d1b25363edd9bea7e32218c59` | external repo evidence for package premise | EXTERNAL_INPUT_NOT_AUTHORITY |
| Codex provider memory or chat summary | local operating context only | NOT_CVF_SOURCE |

No external package file, GitHub repository file, provider memory file, or chat
claim is CVF source authority by itself.

## External Repo Evidence Crosswalk

| External fact checked | External evidence | Package mapping | Disposition |
|---|---|---|---|
| `product-spec` is a structured Product Owner spec hierarchy | `README.md` line 18 | Phase 01 product artifact model and metadata protocol | ABSORB_AS_CVF_PATTERN |
| Frontmatter is structural source of truth | `document-model-and-hierarchy.md` lines 122-128 | Phase 01 metadata and ID protocols | ABSORB_AS_CVF_PATTERN |
| Validation separates deterministic structure from LLM meaning | `validation-rules-spec.md` lines 5-71 and 115-170 | Phase 02 deterministic check versus LLM judgment, validation gate, findings receipt | ABSORB_AS_CVF_PATTERN |
| Approved artifacts cannot be silently reversed | `README.md` line 104; `document-model-and-hierarchy.md` line 118; `validation-rules-spec.md` line 183 | Phase 02 no-silent-reversal guard | ABSORB_AS_CVF_GUARD_PATTERN |
| Critique is report-only and not a CI gate | `README.md` lines 119-120 and 162-163; `product-spec-critique/SKILL.md` lines 20, 38-40, and 180 | Phase 04 read-only reviewer lane and critique review | ADAPT_TO_CVF_REVIEW_LANE |
| Apply-critique uses read fence and decision register | `workflow-apply-critique.md` lines 4-19 and 39-70 | Phase 03 decision receipt and Phase 04 finding resolution | ADAPT_TO_CVF_DECISION_RECEIPTS |
| Packaging safety and deterministic release exist in repo but are tool-specific | `README.md` lines 20, 38, 171, 410, and 439; `safety-rules.md` lines 1-95 | Not central to PRG; possible future packaging lesson only | DEFER_NOT_PRG_T0 |
| Repository is AGPL-3.0 and forbids proprietary closed-source code reuse without separate license | `README.md` lines 311-315 and 447-449; `LICENSE` | Clean-room pattern absorption only | REJECT_DIRECT_CODE_COPY |

## Package Content Audit Matrix

| Package item | Substance readout | Fit for CVF | Disposition | Required hardening |
|---|---|---|---|---|
| `capabilities/README.md` | Positions PRG as strengthening SPEC, WORK ORDER, review, evidence, and guard layers without replacing CVF workflow | High | ACCEPT_AS_SEED | Add CVF provenance, final placement, and external boundary |
| `manifest.json` | Records 24 markdown files and phase counts | Medium | ADAPT | Convert to governed manifest after final placement |
| `TREEVIEW.md` | Root tree view, but undercounts detail relative to actual phase tree | Low | DEFER | Replace with generated or checked tree in T1 |
| Phase 01 README | Defines artifact foundation, lifecycle, and CVF workflow relationship | High | ACCEPT_AS_SEED | Align lifecycle tokens with existing CVF states where needed |
| `PRODUCT_ARTIFACT_MODEL.md` | Defines Vision, Business Requirement, Product Requirement, Epic, Story, Acceptance Criterion plus governance objects | High | ACCEPT_AS_MODEL_INPUT | Reconcile with CVF SPEC and Work Order templates |
| `SPEC_METADATA_PROTOCOL.md` | Defines required metadata, control fields, evidence refs, decisions, risk, approval, freeze, claim boundary | High | ACCEPT_AS_METADATA_PATTERN | Source-verify field vocabulary and distinguish doc-only new fields |
| `TRACEABLE_ARTIFACT_ID_PROTOCOL.md` | Defines stable IDs, prefixes, lineage, registry concept, and collision handling | High | ACCEPT_AS_ID_PATTERN | Avoid collision with existing CVF artifact IDs and registries |
| Phase 02 README | Defines validation governance, severity levels, movement gates | High | ACCEPT_AS_GATE_PATTERN | Map to current CVF gate phases and statuses |
| `DETERMINISTIC_CHECK_VS_LLM_JUDGMENT.md` | Clear rule: computed checks must be computed; LLM judges ambiguity/meaning only | Very high | ABSORB_AS_DOCTRINE | Convert into validator architecture and reviewer contract |
| `SPEC_VALIDATION_GATE.md` | Defines inputs, outputs, metadata/id/relationship/acceptance/evidence/decision/claim-boundary checks | High | ACCEPT_AS_T1_VALIDATOR_SCOPE | Produce fixtures and machine-check candidate |
| `VALIDATION_FINDINGS_RECEIPT.md` | Defines validation receipt and finding schema with result calculation | High | ACCEPT_AS_RECEIPT_PATTERN | Align receipt IDs, storage, and generated aggregate discipline |
| `NO_SILENT_REVERSAL_GUARD.md` | Defines controlled meaning reversal, trigger, required options, decision receipt need | Very high | ABSORB_AS_GUARD_PATTERN | Integrate with existing CVF closure/work-order no-silent-reversal rules |
| Phase 03 README | Makes decisions/evidence first-class governance objects | High | ACCEPT_AS_EVIDENCE_PATTERN | Connect to existing CVF evidence and review directories |
| `DECISION_RECEIPT_PROTOCOL.md` | Defines decision schema, authority tiers, use cases, invalid receipts | High | ACCEPT_AS_DECISION_PATTERN | Align with existing decision/approval authority tokens |
| `CHANGE_TRACE_PROTOCOL.md` | Separates what changed from why; classifies semantic and non-semantic changes | High | ACCEPT_AS_TRACE_PATTERN | Decide diff evidence and storage format |
| `IMPACT_ANALYSIS_PROTOCOL.md` | Traverses artifact graph, decisions, evidence, work orders, freezes; classifies impact levels | High | ACCEPT_AS_IMPACT_PATTERN | Implement only after artifact registry exists |
| `DECISION_ARCHIVE_PROTOCOL.md` | Preserves decisions by supersession, not deletion | Medium-high | ACCEPT_AS_ARCHIVE_PATTERN | Reconcile with CVF archive conventions and retention guards |
| Phase 04 README | Separates validation, critique, review, mutation authority | High | ACCEPT_AS_REVIEW_PATTERN | Map to CVF reviewer/closer roles |
| `SPEC_CRITIQUE_REVIEW.md` | Defines critique capabilities/limits, lenses, output, severity, and flow | High | ADAPT | Keep critique advisory; reject harsh/personal tone as governance mechanism |
| `READ_ONLY_REVIEWER_LANE.md` | Defines reviewer lane allowed/forbidden actions and output types | Very high | ABSORB_AS_LANE_RULE | Align with Agent Handoff Contract and worker/reviewer role split |
| `REVIEW_FINDING_PROTOCOL.md` | Defines structured review finding, lifecycle, resolution requirements | High | ACCEPT_AS_FINDING_PATTERN | Map to existing review finding and ADIF conventions |
| `REVIEW_REPORT_TEMPLATE.md` | Defines report structure, gate context, lens review, findings, boundary | Medium-high | ADAPT | Convert to CVF exact headings/checker-friendly format |
| Phase 05 README | Defines handoff integration, conditions, and no direct PRD-to-build bypass | Very high | ABSORB_AS_HANDOFF_RULE | Map to Work Order template and source verification |
| `PRODUCT_REQUIREMENT_TO_SPEC.md` | Defines product requirement to SPEC input mapping, unknown handling, normalization | Very high | ACCEPT_AS_SPEC_INPUT_PATTERN | Source-verify any new SPEC fields before dispatch |
| `PRODUCT_TRACEABILITY_MATRIX.md` | Defines matrix across product artifact, decision, evidence, SPEC, Work Order, Review, Freeze | Very high | ACCEPT_AS_TRACE_MATRIX_PATTERN | Implement after registry and receipt paths are decided |
| `PRODUCT_SPEC_HANDOFF_TO_WORK_ORDER.md` | Defines handoff schema, status, checks, work-order mapping, forbidden handoff cases | Very high | ACCEPT_AS_HANDOFF_PATTERN | Must be converted into CVF Work Order Source Verification and Agent Handoff blocks |
| `CVF_PRODUCT_REQUIREMENT_PACKAGE.md` | Summarizes package positioning, non-absorption, workflow, and implementation roadmap | High | ACCEPT_AS_T1_BLUEPRINT | Promote only after T1 hardening and placement decision |

## Absorption Classification

| Class | Items | Decision |
|---|---|---|
| Absorb now as doctrine | frontmatter governance contract, deterministic check versus LLM judgment, no-silent-reversal, read-only reviewer lane, product-spec-to-work-order cannot bypass SPEC | ACCEPT |
| Adapt into CVF | metadata schema, ID grammar, receipt schemas, critique report template, trace matrix, handoff schema | ADAPT |
| Defer until implementation | validator, artifact registry, generated traceability matrix, receipt storage, review lane automation | DEFER_TO_PRG_T1_OR_LATER |
| Reject direct absorption | AGPL code, Claude skill format, hooks, subagent orchestration, harsh/personal critique tone, package/release runtime | REJECT_DIRECT |
| Block unless separately authorized | runtime provider proof, public-sync, package certification, UI, external adapter, closed-source commercial reuse of copied code | BLOCK |

## Fit Assessment

The package is strong where CVF needs a non-coder-first product requirement
control layer:

- It keeps product requirement artifacts structured before Work Order drafting.
- It prevents LLMs from inferring structure from polished prose.
- It preserves decisions and evidence as first-class artifacts.
- It keeps critique read-only and separates opinion from deterministic gates.
- It creates a clear bridge from product requirement to SPEC, then Work Order.

The package has gaps that must be fixed before canonical promotion:

- It introduces new field names and status values that are not yet
  source-verified against CVF runtime or templates.
- It suggests storage paths that do not yet exist in this repo.
- It has no fixtures, validators, generated registry, receipts, or gate output.
- It does not yet include a CVF External Knowledge Intake Routing block in the
  package itself.
- It must not become a parallel workflow or package system under repo root.
- It must preserve AGPL clean-room boundaries.

## Selected Routing Outcome

Selected routing outcome:

`ACCEPT_PACKAGE_AS_T1_SEED_WITH_HARDENING_REQUIRED`.

Allowed next move:

`AUTHOR_PRG_T1_GC018_FOR_PACKAGE_PROMOTION_AND_VALIDATOR_FOUNDATION`.

PRG-T1 should:

1. decide final governed placement for the package;
2. add an absorption map and provenance block;
3. normalize status/field vocabulary against current CVF surfaces;
4. create fixtures for valid, invalid, approved-change, frozen-supersession,
   and work-order handoff cases;
5. implement or specify the first deterministic validator only after source
   verification;
6. keep code copying from `product-spec` forbidden.

Forbidden next moves from this T0 roadmap:

- moving the package into canonical reference authority without T1 hardening;
- committing AGPL source code copied from the external repo;
- treating the package as runtime implementation;
- using critique as validation or approval;
- generating Work Orders directly from PRD without SPEC;
- public-sync, provider/live, package certification, UI, adapter, or runtime
  claims.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | T0 response | Future owner |
|---|---|---|
| Audit package content in substance | Completed in Package Content Audit Matrix | PRG-T0 |
| Verify package premise against external repo | Completed in External Repo Evidence Crosswalk | PRG-T0 |
| Preserve external-source boundary | Captured in Source Authority And External Evidence Boundary | PRG-T0 and PRG-T1 |
| Use the package if fit for CVF | Accepted as T1 seed with hardening required | PRG-T1 dispatcher |
| Avoid root-folder promotion without governance | Root package remains unpromoted in T0 | PRG-T1 dispatcher |
| Avoid direct AGPL code absorption | Rejected in Absorption Classification | All future PRG work |

## Design Control Gate

Accepted design:

- T0 records a classified absorption decision only.
- External repo and package material stay advisory until a governed PRG-T1
  artifact promotes selected primitives.
- The operator-provided root package remains external input, not canonical CVF
  source authority.
- Product requirement governance must strengthen the existing SPEC and Work
  Order route instead of bypassing it.

Rejected design:

- Directly adopting the external repo's Claude skill format, hooks,
  orchestrator files, or AGPL implementation code.
- Treating critique as validation, approval, or freeze authority.
- Creating a parallel product-to-build path outside SPEC and Work Order gates.

## Work Plan

No implementation work is assigned by this roadmap.

Recommended next steps:

1. Commit this T0 roadmap after gates pass.
2. Open PRG-T1 GC-018 and work order for package promotion, fixtures, and
   validator foundation.
3. After PRG-T1 closes, move or regenerate the package into the selected CVF
   owner surface with provenance and guard-compatible headings.

## Acceptance Criteria

| ID | Criterion | Required result |
|---|---|---|
| AC1 | All five package phases are read and classified by substance | PASS |
| AC2 | External repository evidence is pinned to commit `b33fc6ff01546e1d1b25363edd9bea7e32218c59` | PASS |
| AC3 | Direct AGPL code absorption is rejected | PASS |
| AC4 | Claude-specific skill/hook/orchestrator material is rejected or deferred outside PRG | PASS |
| AC5 | PRG package is accepted only as a hardening seed, not canonical authority | PASS |
| AC6 | Next move is a GC-018/work-order route before implementation | PASS |
| AC7 | Public/runtime/provider/certification claims remain out of scope | PASS |

## Verification / Evidence

| Evidence item | Command or artifact | Required result |
|---|---|---|
| External knowledge routing guard | `python governance/compat/check_external_knowledge_intake_routing.py --base 45088112 --head HEAD --enforce` | PASS before commit |
| Markdown structural completeness | `python governance/compat/check_markdown_structural_completeness.py --base 45088112 --head HEAD --enforce` | PASS before commit |
| Work-order dispatch quality range check | `python governance/compat/check_work_order_dispatch_quality.py --base 45088112 --head HEAD --enforce` | PASS or N/A with reason: roadmap-only, no dispatch |
| Diff hygiene | `git diff --check` | PASS before commit |

## Fail Conditions

PRG-T0 must fail or block if:

- any package phase is accepted without reading its protocol content;
- the external repo is treated as CVF authority;
- AGPL code is copied into CVF;
- the root package folder is promoted directly without GC-018/work-order
  hardening;
- product requirement handoff is allowed to bypass SPEC;
- critique is treated as validation, approval, or freeze;
- validators, runtime, UI, public-sync, or provider/live claims are made from
  this roadmap;
- a future work order omits source verification for newly proposed fields.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is a private provenance absorption roadmap. No public-sync artifact
or public export is authorized.

## Claim Boundary

This roadmap records an external package absorption decision only. It does not
make `CVF_Product_Requirement_Governance/` canonical, does not implement a
validator, does not certify product requirements, does not authorize runtime or
provider behavior, does not import AGPL code, does not authorize public-sync,
and does not replace existing CVF workflow, work-order, source-verification,
handoff, review, closure, or autorun gates.
