# CVF ASSF Package Instance Certification Pilot Roadmap

Memory class: FULL_RECORD

Status: ROADMAP_READY

Date: 2026-06-25

docType: roadmap

Batch ID: ASSF-PIC

## Purpose

Define a bounded pilot for converting the ASSF package foundation from
contract-only architecture into one source-backed package-instance
certification path. The pilot exists to prove the manual workflow before CVF
adds broad machine enforcement: candidate selection, package instance
evidence, UAT evidence, certification review, generated-index disposition,
resolver readout, Web projection boundary, and checker-readiness decision.

This roadmap follows ASSF-T1 through ASSF-T7. It does not reopen the ASSF
foundation sequence. It selects the next forward lane: one narrow package
instance and certification pilot, then a decision on which controls are stable
enough to machine-check.

## Authorization / Decision

The operator accepted Codex's recommendation to continue after ASSF-T7 with an
ASSF Package Instance And Certification Pilot roadmap. The reason is simple:
ASSF now has the package contract, generated index, resolver, composition
contract, Web projection boundary, and certification lifecycle guard, but it
has not yet demonstrated one full governed package certification path.

This roadmap authorizes roadmap planning only. Each tranche still requires
fresh GC-018, Source Verification, ADIF disclosure where applicable, Dual
Agent Surface Matrix, dependency-release evidence, and an approved work order
before implementation.

## Scope

In scope:

- select one ASSF package candidate for pilot certification;
- source-verify package identity, authority, selectors, evidence, and
  lifecycle fields;
- create or update only the package-instance artifacts explicitly released by
  later work orders;
- collect manual UAT and reviewer certification evidence;
- decide whether generated index and resolver surfaces should be updated or
  kept candidate-only;
- decide whether the Web projection bridge can remain documentation-only or
  needs a schema/mapping work order;
- decide which ASSF-T7 machine-check candidates are ready for implementation
  after the pilot.

Out of scope:

- bulk package migration;
- broad legacy absorption;
- automatic package promotion;
- package activation;
- package instruction execution;
- package loader implementation;
- generated-index mutation without a dedicated tranche;
- resolver mutation without a dedicated tranche;
- CVF Web runtime mutation without a dedicated tranche;
- external CLI/MCP adapter implementation;
- provider call, live proof, public-sync, push, or public catalog claim.

## Non-Goals

- certify every existing skill-related artifact;
- migrate the legacy skill corpus;
- make generated metadata equivalent to package activation;
- expose a CLI/MCP adapter;
- convert CVF Web examples into certified projections by presentation alone;
- implement all T7 machine-check candidates before one manual pilot proves the
  rules are stable.

## Design Control Gate

ASSF-PIC must preserve the T5 no-automatic-promotion invariant and the T7
certification lifecycle boundary. A package candidate may advance only through
explicit review evidence. A generated index or resolver readout remains
metadata-only until a later tranche changes its source entries and reruns the
generator/checker path. A Web projection remains display-only until a later
Web-specific work order source-verifies the schema bridge.

The first tranche must be PIC-T0 candidate selection and source inventory. No
tranche after PIC-T0 may choose a different package silently. If the selected
candidate is found unsuitable, the package must be rejected or returned to
candidate status with evidence, then a new PIC-T0 work order must select a
replacement.

## Dependency Release Evidence

| Dependency | Released by | Evidence | Disposition |
|---|---|---|---|
| Package contract foundation | ASSF-T1 closure | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | SATISFIED |
| Generated index and resolver foundation | ASSF-T2 closure | `docs/reference/agent_system_skills/generated/README.md`; `governance/compat/run_assf_skill_resolver.py` | SATISFIED |
| Composition and no-promotion foundation | ASSF-T5 closure | `docs/reference/agent_system_skills/CVF_ASSF_COMPOSITION_CONTROL_CONTRACT.md` | SATISFIED |
| Web projection boundary | ASSF-T6 closure | `docs/reference/agent_system_skills/CVF_ASSF_WEB_PROJECTION_CONTRACT.md` | SATISFIED |
| Certification lifecycle guard | ASSF-T7 closure | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | SATISFIED |
| Operator selection | current roadmap request | operator agreed to the package-instance certification pilot roadmap | SATISFIED |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| ASSF-T1 defines package identity and lifecycle fields | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Compact Machine Source Schema | `skillId` | ASSF-T1 package schema | EXISTS | ACCEPT |
| ASSF-T1 defines certification and UAT fields | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Compact Machine Source Schema | `certificationState` | ASSF-T1 package schema | EXISTS | ACCEPT |
| ASSF-T1 defines external-agent disposition fields | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Internal-Agent And External-Agent CLI/MCP Disposition Fields | `externalCliMcpDisposition` | ASSF-T1 package schema | EXISTS | ACCEPT |
| ASSF-T1 lifecycle vocabulary includes candidate and terminal states | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Risk And Lifecycle Fields | `CANDIDATE` | ASSF-T1 package schema | VALUE_SET | ACCEPT |
| T2 generated index is a read-only aggregate | `docs/reference/agent_system_skills/generated/README.md` | Purpose | `skill-index.json` | ASSF-T2 generated README | LITERAL_INVARIANT | ACCEPT |
| T2 generated index claim boundary is metadata-only | `docs/reference/agent_system_skills/generated/skill-index.json` | `claimBoundary` | `claimBoundary` | ASSF-T2 generated index | LITERAL_INVARIANT | ACCEPT |
| T2 resolver excludes retired and rejected packages by default | `governance/compat/run_assf_skill_resolver.py` | `_EXCLUDED_STATUSES` | `_EXCLUDED_STATUSES` | ASSF-T2 resolver | VALUE_SET | ACCEPT |
| T2 resolver exposes read-only skill packet resolution | `governance/compat/run_assf_skill_resolver.py` | `resolve_skill_packet` | `resolve_skill_packet` | ASSF-T2 resolver | EXISTS | ACCEPT |
| T5 forbids automatic package promotion | `docs/reference/agent_system_skills/CVF_ASSF_COMPOSITION_CONTROL_CONTRACT.md` | No-Automatic-Promotion Invariant | `No-Automatic-Promotion Invariant` | ASSF-T5 composition contract | LITERAL_INVARIANT | ACCEPT |
| T5 package graph boundary excludes candidate and terminal nodes | `docs/reference/agent_system_skills/CVF_ASSF_COMPOSITION_CONTROL_CONTRACT.md` | Package Graph Boundary | `Package Graph Boundary` | ASSF-T5 composition contract | LITERAL_INVARIANT | ACCEPT |
| T6 Web projection contract defines candidate and certified projection tokens | `docs/reference/agent_system_skills/CVF_ASSF_WEB_PROJECTION_CONTRACT.md` | Classification Vocabulary | `CERTIFIED_PACKAGE_PROJECTION` | ASSF-T6 Web projection contract | VALUE_SET | ACCEPT |
| T6 requires package certification before Web projection | `docs/reference/agent_system_skills/CVF_ASSF_WEB_PROJECTION_CONTRACT.md` | Design Principle 3 | `Projection Requires Prior Certification` | ASSF-T6 Web projection contract | LITERAL_INVARIANT | ACCEPT |
| T7 defines certification and UAT state model | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | Certification And UAT State Model | `uatState` | ASSF-T7 certification lifecycle guard | VALUE_SET | ACCEPT |
| T7 defines generated-index and resolver drift classes | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | Drift Detection Classes | `GENERATED_INDEX_DRIFT` | ASSF-T7 certification lifecycle guard | VALUE_SET | ACCEPT |
| T7 defines adapter claim honesty rules | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | Adapter Claim Honesty Rules | `adapterEvidence` | ASSF-T7 certification lifecycle guard | LITERAL_INVARIANT | ACCEPT |
| Dual Agent standard requires internal and external consumer accounting | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | Mandatory Dual Agent Surface Matrix | `EXTERNAL_AGENT_CLI_MCP` | Dual Agent Surface Accounting Standard | VALUE_SET | ACCEPT |

## Current Runtime Freshness Verification

| Runtime surface | Freshness action | Evidence | Disposition |
|---|---|---|---|
| ASSF generated index | checked current generated README and generated index claim boundary | `docs/reference/agent_system_skills/generated/README.md`; `docs/reference/agent_system_skills/generated/skill-index.json` | roadmap records metadata-only boundary |
| ASSF resolver | checked current resolver source for excluded statuses and packet function | `governance/compat/run_assf_skill_resolver.py` | roadmap records read-only resolver boundary |
| ASSF Web projection | checked current T6 Web projection contract boundary | `docs/reference/agent_system_skills/CVF_ASSF_WEB_PROJECTION_CONTRACT.md` | roadmap records projection-only boundary |
| External CLI/MCP adapter | checked T1/T7 external disposition and adapter honesty contracts | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`; `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | roadmap defers adapter implementation |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | future ASSF-PIC work orders and package-instance artifacts under the agent-system-skills reference surface | internal agents may select one pilot candidate, gather evidence, and perform reviewer certification only inside later work-order scope; roadmap reading alone grants no activation, loader, generated-index, resolver, Web, commit, or public authority | ASSF-T1 package contract, ASSF-T2 generated index/resolver, ASSF-T5 composition contract, ASSF-T6 Web projection contract, ASSF-T7 certification lifecycle guard, this roadmap | no internal runtime adapter or loader is implemented by this roadmap; any generated-index, resolver, or Web change requires its own tranche | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future external package readout, adapter contract, or CLI/MCP certification claim | external agents cannot certify, mutate, activate, execute, or consume package instructions through this roadmap; any external readout must preserve authentication, approval, receipt, raw-data, mutation, and public boundary requirements | Dual Agent Surface Accounting Standard and T7 Adapter Claim Honesty Rules | adapter implementation is deferred; a later source-verified adapter work order is required before `IMPLEMENTED` external disposition is allowed | `DEFERRED_WITH_REASON` |

## Work Plan

The pilot proceeds in a strict single-candidate sequence. PIC-T0 chooses the
candidate and every later tranche either continues that same candidate, holds
with reason, or returns to PIC-T0 for a replacement selection.

## Tranche Sequence

### ASSF-PIC-T0 - Pilot Candidate Selection And Source Inventory

Select exactly one pilot candidate from existing ASSF registry entries or an
explicitly source-backed candidate file. Produce a candidate-selection review,
source inventory, authority boundary, and rejection fallback. Do not change the
generated index, resolver, Web runtime, package lifecycle state, or external
adapter.

Status: `CLOSED_PASS_BOUNDED`.

Closure note: PIC-T0 selected exactly one pilot candidate,
`cvf-dispatch-quality-reviewer`, in
`docs/audits/CVF_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_AUDIT_2026-06-25.md`.
The selection is bounded to candidate identity and source inventory only.
PIC-T1 is not released until the Active Session State Bootstrap Read Model And
Aggregate Size Refactor is handled.

Required outputs:

- GC-018 baseline for PIC-T0;
- source-verified work order;
- candidate-selection audit;
- completion review;
- explicit decision: `PILOT_CANDIDATE_SELECTED` or `PILOT_CANDIDATE_REJECTED`.

### ASSF-PIC-T1 - Package Instance Evidence And Skeleton Hardening

Create or harden the selected package's source-backed package-instance
artifacts only if PIC-T0 selected a candidate. The work must preserve the T1
package schema and T7 lifecycle guard. If an existing registry entry is used,
the generated source layout must be respected and drift checks must pass.

Status: `CLOSED_PASS_BOUNDED`.

Closure note: PIC-T1 mapped the selected candidate's package evidence skeleton
in
`docs/audits/CVF_ASSF_PIC_T1_PACKAGE_INSTANCE_EVIDENCE_SKELETON_HARDENING_AUDIT_2026-06-26.md`
and accepted the worker-return scaffold-effectiveness measurement in
`docs/reviews/CVF_ASSF_PIC_T1_PACKAGE_INSTANCE_EVIDENCE_SKELETON_HARDENING_WORKER_RETURN_2026-06-26.md`.
The result is bounded: `cvf-dispatch-quality-reviewer` has no current schema
field-family gap, but UAT/certification evidence remains absent and no package
instance or certification decision was made. The same return shows the recent
report-friction reduction is only partially effective; therefore PIC-T2 is
parked until work-order dispatch scaffold optimization is handled or the
operator explicitly reopens PIC-T2.

Required outputs:

- package-instance source artifact changes only if authorized by work order;
- updated package evidence manifest;
- no certification claim unless T2 completes later;
- generated-index drift disposition.

### ASSF-PIC-T2 - Manual UAT And Certification Review

Run the first manual UAT/certification review for the selected package. The
review may accept, reject, or hold certification. It must not treat a generated
metadata packet or Web display as certification evidence.

Status: `CLOSED_PASS_BOUNDED`.

Closure note: PIC-T2 accepted the Claude worker return and UAT/certification
review in
`docs/reviews/CVF_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_2026-06-26.md`
and
`docs/reviews/CVF_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_WORKER_RETURN_2026-06-26.md`.
The lifecycle recommendation is `CERTIFICATION_HELD_WITH_REASON`: local
dispatch-quality evidence is sufficient to hold rather than reject, but
`uatState` and `certificationState` remain `NOT_STARTED`, no registry mutation
is authorized, and no final certification decision is made. The worker also
confirmed WODS-T1 improved scaffold/rescan friction but found three remaining
dispatch-authoring defects for a follow-up WODS hardening lane.

Required outputs:

- UAT evidence review;
- certification decision review;
- lifecycle disposition: `CERTIFIED`, `CERTIFICATION_REJECTED`, or
  `CERTIFICATION_HELD_WITH_REASON`;
- explicit external adapter disposition.

### ASSF-PIC-T3 - Generated Index And Resolver Integration Decision

If PIC-T2 certifies the package, decide whether generated index source entries
and resolver tests should be updated. This tranche may be doc-only or
implementation-bearing depending on the work order. Any source mutation must
edit generated source entries first and run the generator/checker path.

Status: `CLOSED_PASS_BOUNDED`.

Closure note: PIC-T2 did not certify the package. ASSF-PIC-T3 therefore closed
as a decision-only review under the certification hold with disposition
`INTEGRATION_DEFERRED_CERTIFICATION_HELD` in
`docs/reviews/CVF_ASSF_PIC_T3_GENERATED_INDEX_RESOLVER_INTEGRATION_DECISION_COMPLETION_2026-06-26.md`.
The worker and reviewer confirmed generated-index drift check PASS and resolver
readout metadata-only behavior. This closure does not authorize generated-index
source mutation, generated aggregate mutation, resolver mutation, registry
mutation, package integration, package activation, or certification state
advancement. The operator-reported T3 worker experience also fired the parked
WODS reopen condition, so PIC-T4 remains held while WODS follow-up is the next
material lane.

Required outputs:

- generated-index disposition;
- resolver behavior disposition;
- drift check evidence;
- no package activation claim.

### ASSF-PIC-T4 - Web Projection Bridge Decision

Decide whether the certified package should remain absent from CVF Web, remain
candidate-only, or receive a Web projection bridge work order. This tranche
does not mutate Web runtime unless a later work order explicitly releases that
scope and source-verifies the schema bridge.

Status: `CLOSED_PASS_BOUNDED`.

Closure evidence:

- baseline:
  `docs/baselines/CVF_GC018_ASSF_PIC_T4_WEB_PROJECTION_BRIDGE_DECISION_2026-06-26.md`;
- work order:
  `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_PIC_T4_WEB_PROJECTION_BRIDGE_DECISION_FOR_CODEX_2026-06-26.md`;
- decision review:
  `docs/reviews/CVF_ASSF_PIC_T4_WEB_PROJECTION_BRIDGE_DECISION_2026-06-26.md`;
- completion review:
  `docs/reviews/CVF_ASSF_PIC_T4_WEB_PROJECTION_BRIDGE_DECISION_COMPLETION_2026-06-26.md`;
- disposition: `WEB_PROJECTION_DEFERRED_CERTIFICATION_HELD`.

Required outputs:

- Web projection decision;
- schema bridge disposition;
- no self-certification claim from Web display;
- external-agent adapter disposition.

### ASSF-PIC-T5 - Checker Readiness And Next-Control Decision

Review the pilot defects and decide which T7 machine-check candidates are ready
for implementation: certification lifecycle, generated-index/resolver drift,
Web projection drift, or adapter-claim honesty. This tranche may dispatch a
new checker roadmap or keep machine checks deferred with reason.

Status: `READY_FOR_GC018_AFTER_T4_CLOSURE`.

Required outputs:

- checker-readiness matrix;
- ADIF entries for any repeated non-obvious defects found during the pilot;
- next roadmap/work-order recommendation;
- session continuity update.

## Acceptance Criteria

The roadmap can be considered ready for PIC-T0 dispatch only when:

- this file exists as the governing roadmap for ASSF-PIC;
- Source Verification cites current CVF-governed source surfaces, not
  provider-local memory;
- Dual Agent Surface Matrix includes both internal and external rows;
- PIC-T0 is the only next work-order candidate;
- all later tranches remain dependency-held;
- no runtime, provider, live, Web, resolver, generated-index, adapter,
  package-activation, public-sync, or push claim is made.

## Verification / Evidence

Required verification for this roadmap and its child tranches:

- pre-dispatch autorun gate on the changed roadmap/work-order range;
- commit steward preflight before material commit;
- source verification for every named runtime field, schema key, function,
  generated aggregate, adapter boundary, and existing path;
- generated-index drift check before any generated index claim changes;
- resolver test evidence before any resolver behavior claim changes;
- reviewer completion packet before any certification state advances;
- separate session-sync commit after material closure when next-move surfaces
  change.

## Fail Conditions

Return to orchestrator if any ASSF-PIC work order:

- selects more than one pilot package in the same tranche;
- changes the generated index without editing generated sources first;
- treats resolver output as package activation or certification proof;
- treats Web display as canonical package truth;
- certifies a package while `uatState` evidence is absent or failed;
- claims external CLI/MCP support without adapter contract and evidence;
- omits the external-agent row or adapter boundary in the Dual Agent Surface
  Matrix;
- tries to bulk-migrate legacy skill material inside this pilot;
- mixes material package work and session-sync edits in the same commit.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | roadmap selection to governed work-order/source-verification/autorun lane |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this roadmap |
| Disposition | local roadmap planning only; no external material is absorbed as source authority |
| Claim boundary | operator direction selects the next ASSF lane; package facts must still be source-verified before dispatch |

## Finding-To-Governance Learning Disposition

- Defect class: `ORCHESTRATOR_PACKET_GAP`
- Learning lane: `GOVERNANCE_CONTROL_PLANE`
- Disposition: `CAPTURED_FOR_FOLLOW_UP` - ASSF-PIC-T3 closed bounded, but the
  operator-reported worker experience hit the parked WODS reopen condition:
  3 gate runs and recurring scaffold/template/format defects.
- Next control action: create a source-verified WODS follow-up GC-018/work
  order before ASSF-PIC-T4 dispatch.
- Runtime/provider/cost learning lane: `N/A_WITH_REASON` - this roadmap does
  not run provider calls or cost-bearing tests.

## Epistemic Process Block

### Expected Result / Prediction

A narrow package-instance certification pilot should expose whether ASSF-T1
through ASSF-T7 are usable as a real workflow before CVF promotes more
machine checks or Web/external-agent surfaces.

### Evidence Comparison

ASSF-T1 through ASSF-T7 already provide the contract surfaces needed for a
pilot, but the current closure evidence shows no package has been certified,
activated, projected as certified, or exposed through a CLI/MCP adapter by the
ASSF foundation sequence.

### Contradiction Or Gap Disposition

The gap is execution maturity, not missing architecture vocabulary. This
roadmap therefore chooses a single pilot package path instead of another broad
contract tranche.

### Claim Update

ASSF-PIC is ready for PIC-T0 dispatch planning only. It does not certify,
activate, project, execute, export, or adapt any package.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this roadmap references private provenance architecture and package
governance surfaces. Public-safe export requires separate redaction and
public-sync authorization.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ASSF Package Instance Certification Pilot roadmap creation |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE -- roadmap planning only |
| receiptEvidence | N/A with reason: no runtime execution, provider call, or adapter receipt exists |
| actionEvidence | ACTION_EVIDENCE_PRESENT -- Source Verification Block, Dual Agent Surface Matrix, and tranche dependency plan |
| invocationBoundary | governed local roadmap authoring only |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, CLI, MCP, Web runtime, or adapter interception claim beyond local artifact authoring |
| claimLanguage | creates the forward roadmap for one controlled ASSF package-instance certification pilot |
| forbiddenExpansion | no package instance, certification decision, generated-index mutation, resolver mutation, Web runtime change, CLI/MCP adapter, provider call, live proof, public-sync, push, or session-sync edit in the roadmap material commit |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex roadmap author |
| Agent type | planner/closer |
| Role | roadmap author |
| Provider or surface | local workspace |
| Session or invocation | ASSF-PIC roadmap creation, 2026-06-25 |
| Invocation ID | `assf-pic-roadmap-codex-2026-06-25` |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | source reads, `rg`, apply_patch, autorun gate, commit steward |
| Target paths | this roadmap |
| Allowed scope source | human authorization after ASSF-T7 closure and active handoff next-move selection |
| Before status evidence | HEAD `4fae3a3b`; worktree clean before roadmap creation |
| After status evidence | this roadmap pending material commit |
| Diff evidence | `git diff -- docs/roadmaps/CVF_ASSF_PACKAGE_INSTANCE_CERTIFICATION_PILOT_ROADMAP_2026-06-25.md` |
| Approval boundary | roadmap planning only |
| Claim boundary | no runtime, provider/live, public-sync, external adapter, generated index, resolver, Web runtime, or package activation claim |
| Expected manifest | this roadmap only |
| Actual manifest | this roadmap only |

## Claim Boundary

This roadmap authorizes only the forward plan for a controlled ASSF package
instance certification pilot. It does not create or certify a package, mutate
the generated index, modify the resolver, change CVF Web runtime source,
implement a CLI/MCP adapter, activate or execute any skill, run provider/live
proof, export public artifacts, push to any remote, or update session
continuity in the material commit.
