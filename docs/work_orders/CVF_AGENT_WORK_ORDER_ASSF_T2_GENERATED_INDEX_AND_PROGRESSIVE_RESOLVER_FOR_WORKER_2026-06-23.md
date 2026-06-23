# CVF Agent Work Order ASSF-T2 Generated Index And Progressive Resolver For Worker

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-23

docType: work_order

Batch ID: ASSF-T2

Commit mode: WORKER_MUST_NOT_COMMIT

## Dispatch Prompt Envelope

Role: ASSF-T2 no-commit worker; generated index, generator, drift checker, and read-only resolver builder.

Canonical packet: this work order plus `docs/baselines/CVF_GC018_ASSF_T2_GENERATED_INDEX_AND_PROGRESSIVE_RESOLVER_2026-06-23.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

dispatchBaseHead: `4d8ecc06`.

executionBaseHead: worker must capture with `git rev-parse --short HEAD` before edits.

Current-time notes: current dispatch date is 2026-06-23; worker must record actual local start time in the return packet.

Do-not-misread notes: T2 consumes the frozen ASSF-T1 contract; do not re-derive schema. The resolver is read-only and returns metadata only; it must never open or execute a package instruction body. The generated index is produced only by the deterministic generator; never hand-edit it. No CLI/MCP adapter, no skill activation, no migration.

Required first actions: read front door/state/handoff/guard orientation, read this packet, the GC-018 baseline, the ASSF-T1 contract, the generated aggregate standard, and the two named code precedents; capture `git status --short`; run pre-implementation gate.

Return contract: return `COMPLETE_PENDING_REVIEW`, `COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`, or `BLOCKED_WITH_REASON` without committing.

You are the ASSF-T2 worker. Build only the registry sources, deterministic
generator, drift checker, read-only resolver, generated index, required folder
README front doors, paired tests, and the worker-return packet described here.
You must not commit. Return `COMPLETE_PENDING_REVIEW` only with the required
artifacts present and reviewer-fast evidence captured, or return
`BLOCKED_WITH_REASON` if a gate fails outside allowed scope.

## Core Guard Self-Protection Authorization

| Field | Disposition |
|---|---|
| Authorized guard-maintenance scope | ASSF-T2 creates NEW governed automation files under `governance/compat/` (generator, drift checker, resolver, and paired tests); it does not modify, delete, or weaken any existing protected guard, hook chain, or autorun gate |
| Protected paths | `governance/compat/run_local_governance_hook_chain.py`, `governance/compat/run_agent_autorun_workflow_gate.py`, and all existing `governance/compat/check_*.py` and `generate_*.py` files remain unmodified by this tranche |
| Operator authorization | operator selected ASSF-T2 with full executable scope and directed careful authoring that avoids the prior tranche finding classes |
| Rollback boundary | worker creates only new ASSF-T2 files (sources, generator, drift checker, resolver, generated index, READMEs, tests, worker return); revert is deletion of those new files |

## Purpose

Provide a no-commit worker packet for ASSF-T2 so the first executable ASSF data
plane (compact registry sources, deterministic generator, drift checker, and
read-only progressive resolver) is built against the frozen ASSF-T1 package
contract and returned for Codex review before ASSF-T3 maps learning evidence
into skill candidates.

## Objective

Build at least one contract-conforming compact registry source, a deterministic
generator that builds the generated skill index from sources, a drift checker
that fails when the index diverges from sources, and a read-only progressive
resolver that returns bounded package metadata from task/role/phase/surface/
risk selectors before loading any package instruction body, with paired tests,
and return them for Codex review.

## Authority Chain

| Authority | Path | Disposition |
|---|---|---|
| Active session front door | `CVF_SESSION_MEMORY.md` | ASSF-T2 is the operator-selected next move |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | current lane points to ASSF-T2 |
| Active handoff | `AGENT_HANDOFF_V22_2026-06-22.md` | active handoff for governed execution context |
| Roadmap | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | ASSF-T2 tranche definition; T2 must consume the T1 contract |
| GC-018 baseline | `docs/baselines/CVF_GC018_ASSF_T2_GENERATED_INDEX_AND_PROGRESSIVE_RESOLVER_2026-06-23.md` | continuation baseline for this work order |
| ASSF-T1 package contract | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | mandatory schema and topology input |
| Generated aggregate standard | `docs/reference/CVF_JSON_GENERATED_AGGREGATE_DISCIPLINE_STANDARD_2026-06-12.md` | source/generator/drift/tests discipline |
| Resolver precedent | `governance/compat/run_adif_defect_resolver.py` | read-only deterministic resolver pattern to mirror |
| Generator/drift precedent | `governance/compat/generate_corpus_scan_registry.py` | deterministic generator and drift-checker pattern |
| Dual-agent standard | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | internal and external CLI/MCP accounting |

## Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | Claude (this turn) | Create source-verified dispatch packet; dispatcher does not execute |
| Worker | assigned worker agent | Build the data plane and worker-return packet; do not commit |
| Reviewer/closer | Codex | Validate determinism, read-only behavior, contract conformance, tests, close T2, update session surfaces, and commit if accepted |

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V22_2026-06-22.md`
- `docs/reference/guard_orientation/README.md`
- this work order
- `docs/baselines/CVF_GC018_ASSF_T2_GENERATED_INDEX_AND_PROGRESSIVE_RESOLVER_2026-06-23.md`
- `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`
- `docs/reference/CVF_JSON_GENERATED_AGGREGATE_DISCIPLINE_STANDARD_2026-06-12.md`
- `governance/compat/run_adif_defect_resolver.py`
- `governance/compat/generate_corpus_scan_registry.py`

## Pre-Flight Checks

- `git rev-parse --short HEAD`
- `git status --short`
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 4d8ecc06 --head HEAD`

## Write Ownership

The worker owns only the artifacts named in Allowed Scope. Codex owns the
dispatch commit, closure review, roadmap closure update, session sync, and any
final material commit.

## Execution Plan

Execute the Required Execution Steps in order. Do not begin ASSF-T3 work. Do
not implement a CLI/MCP adapter, activate any skill, execute any package
instruction body, or migrate any existing CVF Web example.

## Evidence Requirements

Evidence must include a contract-conformance table mapping each registry source
field to a contract field family, a determinism proof (regenerate the index and
show byte-stable output), a drift-detection proof (hand-edit the index in a temp
copy and show the checker fails), a resolver read-only proof, selector tests,
the changed-set manifest, gate receipts, and explicit no-commit status.

## Review Gate

Codex reviewer must rerun reviewer-fast and relevant autorun gates and verify
determinism, read-only resolver behavior, drift detection, and contract
conformance before accepting worker output. Worker self-approval is not closure.

## Closure Checklist

- [x] Work order status is dispatch-ready.
- [x] Commit mode is `WORKER_MUST_NOT_COMMIT`.
- [x] Allowed output paths are named.
- [x] Dual Agent Surface Matrix is present.
- [x] External knowledge intake routing is present.
- [x] Worker return packet shape is present.
- [x] Public Export Disposition is private-only.
- [x] Required new-folder README front doors are named in the artifact manifest.
- [x] Core Guard Self-Protection Authorization is present for new governance/compat files.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` only for Stop Conditions. Return
`COMPLETE_PENDING_REVIEW` only after the required artifacts and gate evidence
exist.

## Operator Checkpoint

N/A with reason: the operator selected ASSF-T2 with full executable scope. No
extra checkpoint is required before bounded worker execution; stop conditions
define the return path.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| ASSF-T2 must create registry sources, a generator, a drift check, and a resolver returning bounded metadata before loading instructions | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | ASSF-T2 - Generated Index And Progressive Resolver | resolver that returns bounded package metadata | ASSF roadmap | LITERAL_INVARIANT | ACCEPT |
| ASSF-T2 must consume the ASSF-T1 contract before creating index or resolver surfaces | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | Next control action | ASSF-T2 must consume the ASSF-T1 package contract | ASSF roadmap | LITERAL_INVARIANT | ACCEPT |
| The contract defines the compact machine source schema field families | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Compact Machine Source Schema | Identity; Selectors; Risk and authority; Lifecycle | ASSF-T1 contract | VALUE_SET | ACCEPT |
| The contract defines the package lifecycle states the resolver must respect | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Risk And Lifecycle Fields | CANDIDATE; PROPOSED; APPROVED; ACTIVE; DEPRECATED; RETIRED; REJECTED | ASSF-T1 contract | VALUE_SET | ACCEPT |
| The contract names the storage topology with a registry entries path and generated index path | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Storage Topology | generated | ASSF-T1 contract | LITERAL_INVARIANT | ACCEPT |
| The generated aggregate pattern requires compact sources, a deterministic generator, a drift checker, and focused tests | `docs/reference/CVF_JSON_GENERATED_AGGREGATE_DISCIPLINE_STANDARD_2026-06-12.md` | Rule | deterministic generator | generated aggregate standard | LITERAL_INVARIANT | ACCEPT |
| Creating a generated aggregate requires recording a generated-source-layout closure token | `docs/reference/CVF_JSON_GENERATED_AGGREGATE_DISCIPLINE_STANDARD_2026-06-12.md` | Closure Requirement | GENERATED_SOURCE_LAYOUT_ADDED | generated aggregate standard | VALUE_SET | ACCEPT |
| A read-only deterministic resolver pattern exists to mirror | `governance/compat/run_adif_defect_resolver.py` | resolve_defect_packet | resolve_defect_packet | ADIF resolver | RUNTIME_BEHAVIOR | ACCEPT |
| A deterministic generator pattern exists to mirror | `governance/compat/generate_corpus_scan_registry.py` | generator entry point | generate_corpus_scan_registry | corpus registry generator | EXISTS | ACCEPT |
| Dual Agent Surface Matrix must account for internal and external CLI/MCP consumers | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | Core Rule; Mandatory Dual Agent Surface Matrix | INTERNAL_AGENT; EXTERNAL_AGENT_CLI_MCP | dual-agent surface standard | LITERAL_INVARIANT | ACCEPT |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_SINGLE_ROLE` |
| rolePattern | Claude dispatcher creates work order; worker builds the data plane and returns review artifacts; Codex reviewer/closer decides closure and commit |
| phase | DISPATCH_AUTHORING -> WORKER_EXECUTION -> REVIEWER_CLOSURE -> SESSION_SYNC if next move changes |
| baseHeadFor(phase) | dispatchBaseHead=`4d8ecc06`; executionBaseHead=worker must capture with `git rev-parse --short HEAD`; closureBaseHead=reviewer captures from worker return |
| changedSetScope(phase) | worker may create only the paths named in Allowed Scope |
| traceScope(phase, actor) | worker records commands, conformance/determinism/drift/read-only proofs, changed-set evidence, and gate receipts in the return packet |
| commitOwner(phase) | `WORKER_MUST_NOT_COMMIT`; Codex reviewer/closer owns any material and session-sync commit |
| crossBatchIsolation | no ASSF-T3/T4/T5/T6/T7 implementation; no unrelated cleanup |
| nextMoveSurfaces | worker must not edit active session state, session front door, active handoff, or generated active-session aggregate |
| closer designation | Codex reviewer/closer |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| completionReviewPath | reviewer creates a completion review under the reviews directory after accepting this return |
| workerReturnPath | `docs/reviews/CVF_ASSF_T2_GENERATED_INDEX_AND_PROGRESSIVE_RESOLVER_WORKER_RETURN_2026-06-23.md` |
| reviewerOwnedClosurePaths | ASSF roadmap update, T2 completion review, active session state/front door/handoff sync, material commit, and session-sync commit if accepted |
| workerReturnDisposition | `COMPLETE_PENDING_REVIEW`, `COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`, or `BLOCKED_WITH_REASON` |
| reviewerCommitRule | Reviewer may commit only after validating determinism, read-only behavior, drift detection, contract conformance, and tests |

## Worker Autonomy / No-Question Rule

The worker must repair any machine-gate failure inside Allowed Scope and rerun
the relevant gate without pausing for approval. The worker must stop and return
`BLOCKED_WITH_REASON` only when repair would exceed Allowed Scope, alter commit
mode, touch forbidden paths, require live/provider/public-sync/secrets, release
a new prerequisite, require session/front-door/handoff ownership, or require a
change to the frozen ASSF-T1 contract (a contract gap must be reported, not
silently worked around).

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake class | legacy source family |
| Route mode | `MULTI_AGENT_SINGLE_ROLE` |
| Selected route | Claude dispatcher -> worker data-plane builder -> Codex reviewer/closer |
| Primary worker role | generated index, generator, drift checker, and read-only resolver builder |
| Reviewer role | Codex reviewer/closer validates determinism, read-only behavior, and closure |
| External intake route | consume the accepted ASSF-T1 contract, which already reconciled the ASSF-T0.1 ledger |
| Scope classification | bounded no-commit worker-return building the executable ASSF data plane |
| Risk sensitivity | high because the generator, drift checker, and resolver become the executable data plane every later ASSF tranche depends on, affecting selection behavior, external CLI/MCP disposition, public-sync boundary, and production-readiness language |
| Escalation condition | stop with `BLOCKED_WITH_REASON` if remediation exceeds allowed scope, touches forbidden paths, needs new human authorization, requires session/front-door/handoff ownership, or requires a contract change |
| Dispatch status | ACCEPT |
| Reason | T2 is selected, source-verified, and bounded to a no-commit executable-data-plane worker-return |

## Legacy Absorption Coverage Index Disposition

| Field | Disposition |
|---|---|
| Coverage index status | NOT_APPLICABLE_WITH_REASON |
| Canonical coverage index | `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` is the canonical legacy coverage index; T2 does not run a new legacy scan and so does not update it |
| Reason | ASSF-T0.1 already enumerated and classified the legacy corpus and ASSF-T1 reconciled it into the package contract; T2 builds against the contract rather than re-running the scan or updating the canonical coverage index |
| Required worker evidence | a contract-conformance table mapping each registry source field to a contract field family |
| Future guard candidate | wire the ASSF index drift checker into an autorun phase before ASSF-T3 dispatch |

## Required Artifact Manifest

| Required output | Path | Required at handoff | Exists |
|---|---|---|---|
| Registry source README front door | `docs/reference/agent_system_skills/registry/README.md` | yes | yes |
| At least one compact registry source | `docs/reference/agent_system_skills/registry/entries/cvf-worker-return-author.json` | yes | yes |
| Generated index README front door | `docs/reference/agent_system_skills/generated/README.md` | yes | yes |
| Generated skill index | `docs/reference/agent_system_skills/generated/skill-index.json` | yes | yes |
| Deterministic generator | `governance/compat/generate_assf_skill_index.py` | yes | yes |
| Drift checker | `governance/compat/check_assf_skill_index_drift.py` | yes | yes |
| Read-only resolver | `governance/compat/run_assf_skill_resolver.py` | yes | yes |
| Generator test | `governance/compat/test_generate_assf_skill_index.py` | yes | yes |
| Drift checker test | `governance/compat/test_check_assf_skill_index_drift.py` | yes | yes |
| Resolver test | `governance/compat/test_run_assf_skill_resolver.py` | yes | yes |
| T2 worker return | `docs/reviews/CVF_ASSF_T2_GENERATED_INDEX_AND_PROGRESSIVE_RESOLVER_WORKER_RETURN_2026-06-23.md` | yes | yes |

## Work-Order Fulfillment Manifest

| Required output | Path or evidence | Owner | Status |
|---|---|---|---|
| Registry source README front door | `docs/reference/agent_system_skills/registry/README.md` | worker | WORKER_RETURNED |
| At least one compact registry source | `docs/reference/agent_system_skills/registry/entries/<skill-id>.json` | worker | WORKER_RETURNED |
| Generated index README front door | `docs/reference/agent_system_skills/generated/README.md` | worker | WORKER_RETURNED |
| Generated skill index | `docs/reference/agent_system_skills/generated/skill-index.json` | worker | WORKER_RETURNED |
| Deterministic generator | `governance/compat/generate_assf_skill_index.py` | worker | WORKER_RETURNED |
| Drift checker | `governance/compat/check_assf_skill_index_drift.py` | worker | WORKER_RETURNED |
| Read-only resolver | `governance/compat/run_assf_skill_resolver.py` | worker | WORKER_RETURNED |
| Generator test | `governance/compat/test_generate_assf_skill_index.py` | worker | WORKER_RETURNED |
| Drift checker test | `governance/compat/test_check_assf_skill_index_drift.py` | worker | WORKER_RETURNED |
| Resolver test | `governance/compat/test_run_assf_skill_resolver.py` | worker | WORKER_RETURNED |
| T2 worker return | `docs/reviews/CVF_ASSF_T2_GENERATED_INDEX_AND_PROGRESSIVE_RESOLVER_WORKER_RETURN_2026-06-23.md` | worker | WORKER_RETURNED |
| T2 completion review | a reviewer-created completion review under the reviews directory | reviewer | CLOSED_PASS_BOUNDED |
| Material commit | git commit after reviewer acceptance | reviewer | CLOSURE_READY |

## Allowed Scope

The worker may create or edit only:

- `docs/reference/agent_system_skills/registry/README.md`
- `docs/reference/agent_system_skills/registry/entries/<skill-id>.json` (at least one)
- `docs/reference/agent_system_skills/generated/README.md`
- `docs/reference/agent_system_skills/generated/skill-index.json`
- `governance/compat/generate_assf_skill_index.py`
- `governance/compat/check_assf_skill_index_drift.py`
- `governance/compat/run_assf_skill_resolver.py`
- `governance/compat/test_generate_assf_skill_index.py`
- `governance/compat/test_check_assf_skill_index_drift.py`
- `governance/compat/test_run_assf_skill_resolver.py`
- `docs/reviews/CVF_ASSF_T2_GENERATED_INDEX_AND_PROGRESSIVE_RESOLVER_WORKER_RETURN_2026-06-23.md`

The worker may read these for evidence:

- `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`
- `docs/reference/agent_system_skills/README.md`
- `docs/reference/CVF_JSON_GENERATED_AGGREGATE_DISCIPLINE_STANDARD_2026-06-12.md`
- `governance/compat/run_adif_defect_resolver.py`
- `governance/compat/generate_corpus_scan_registry.py`
- `governance/compat/check_corpus_scan_registry.py`
- `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V22_2026-06-22.md`

The worker must create a `README.md` front door in each new
`docs/reference/agent_system_skills/` subfolder it adds (`registry/` and
`generated/`), each with a Purpose and a Claim Boundary, because the foundation
storage layout guard requires a README front door in every reference-family
folder. This is named explicitly here so it is built up front, not added as a
review repair.

## Forbidden Scope

The worker must not:

- commit, push, public-sync, or edit Git remotes;
- modify, delete, or weaken any existing `governance/compat/*.py` guard, hook
  chain, autorun gate, or any file outside Allowed Scope;
- hand-edit the generated `skill-index.json`; it must be produced only by the
  generator and must pass the drift checker;
- build a resolver that opens, reads, loads, or executes any package
  instruction body (`SKILL.md`) or reference file; the resolver returns
  metadata only;
- create a `packages/<skill-id>/SKILL.md` or any package instruction body;
- implement a CLI/MCP adapter, runtime activation, loader-executor, or any
  runtime/provider/live behavior;
- activate, promote, or set any skill to `ACTIVE` beyond what a source file
  declares as static metadata;
- migrate or reclassify any existing CVF Web example or `governance/skill-library` entry;
- edit `.private_reference/legacy/` or re-run the full legacy scan;
- edit active session state/front door/handoff or generated session aggregate;
- change GC-051 corpus registries, roadmap status, baselines, work orders, or unrelated files;
- change the frozen ASSF-T1 contract (report a contract gap instead);
- promote legacy/provider-local content into canonical authority.

## Required Execution Steps

1. Capture startup state:
   - `git rev-parse --short HEAD`
   - `git status --short`
2. Read the required first reads, including the ASSF-T1 contract, the generated
   aggregate standard, and the two code precedents.
3. Run the pre-implementation gate using the dispatch base unless the reviewer
   has provided a newer dispatch commit:
   - `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 4d8ecc06 --head HEAD`
4. Author at least one compact registry source under
   `registry/entries/` conforming to the contract field families, plus the
   `registry/README.md` front door. Use a `CANDIDATE` or `PROPOSED` lifecycle
   state; do not declare a skill `ACTIVE`.
5. Build the deterministic generator
   (`generate_assf_skill_index.py`) that reads the registry sources and writes
   `generated/skill-index.json` byte-stably (sorted keys, stable ordering,
   trailing newline, source-only fields stripped), plus the `generated/README.md`
   front door.
6. Build the drift checker (`check_assf_skill_index_drift.py`) that regenerates
   in memory and fails when the committed index diverges from its sources.
7. Build the read-only resolver (`run_assf_skill_resolver.py`) that returns
   bounded package metadata from task/role/phase/surface/risk selectors, mirrors
   the ADIF resolver read-only pattern, excludes `RETIRED`/`REJECTED` by default,
   and never opens a package instruction body.
8. Write paired tests for the generator (determinism, source-only stripping),
   the drift checker (drift detection), and the resolver (selector matching,
   read-only proof by patching `builtins.open` to raise on write/instruction
   read during resolution).
9. Author the worker-return packet.
10. Run:
    - `python -m pytest governance/compat/test_generate_assf_skill_index.py governance/compat/test_check_assf_skill_index_drift.py governance/compat/test_run_assf_skill_resolver.py`
    - `python governance/compat/run_worker_return_fast_gate.py`
    - `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast`
11. Return `COMPLETE_PENDING_REVIEW`, `COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`,
    or `BLOCKED_WITH_REASON` without committing.

## Required Deliverables

### Registry Source And Generated Index

The compact registry source(s) must conform to the contract Compact Machine
Source Schema field families. The generated index must be produced only by the
generator. Each new reference-family subfolder must carry a `README.md` front
door with a Purpose and a Claim Boundary.

### Code Files

The generator, drift checker, and resolver must each be standalone,
deterministic, and read-only with respect to existing repository state (the
generator writes only the index; the drift checker and resolver write nothing).
Keep each file under the 600-line Python automation soft threshold.

## Worker Return Packet Shape Contract

Path:

`docs/reviews/CVF_ASSF_T2_GENERATED_INDEX_AND_PROGRESSIVE_RESOLVER_WORKER_RETURN_2026-06-23.md`

Required sections:

- Purpose
- Target / Source
- Scope / Methodology
- Findings / Position
- Risk / Corrective Action
- Worker Status
- Required Artifact Manifest
- Roadmap-To-Work-Order Trace Matrix
- Core Guard Self-Protection Authorization
- Dual Agent Surface Matrix
- Corpus Completeness And Report Integrity
- External Knowledge Intake Routing
- Rescan Intelligence Hardening
- Finding-To-Governance Learning Disposition
- Epistemic Process Block
- Delta Execution Claim Boundary Control Block
- Public Export Disposition
- Machine Closure Package
- Acceptance Receipt Assertion Matrix
- Agent Operation Trace Block
- Claim Boundary

The worker return must also record `executionBaseHead`, `git status --short`,
a `dispatchWorkOrder:` line citing this work order, a top-level `Status:` line,
the `GENERATED_SOURCE_LAYOUT_ADDED` closure token, and use `N/A with reason` or
`NOT_APPLICABLE_WITH_REASON` for conditional blocks that do not apply. Because
this changeset touches `governance/compat/*.py`, the worker return must carry a
`## Core Guard Self-Protection Authorization` block listing the protected paths
and the four required tokens (`Authorized guard-maintenance scope`,
`Protected paths`, `Operator authorization`, `Rollback boundary`); do not write
the literal token `todo` anywhere in the Rescan Intelligence Hardening section.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | the ASSF resolver, generator, drift checker, and generated index this tranche builds | T2 implements read-only selection and deterministic generation only; loading metadata never widens authority and never executes a package instruction body | resolver/generator/drift tests and the generated index | no adapter implemented | `IMPLEMENTED` |
| `EXTERNAL_AGENT_CLI_MCP` | future CLI/MCP skill discovery or load adapter | T2 records the external-agent disposition in registry sources and resolver output; it does not implement, expose, or authorize any adapter | contract external-agent disposition field | separate ASSF adapter work required | `DEFERRED_WITH_REASON` |

## External Knowledge Intake Routing

| Field | Worker requirement |
|---|---|
| Chain map | cite `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Legacy source family |
| Chain map route | legacy source family -> ASSF-T0.1 candidate ledger -> ASSF-T1 contract -> ASSF-T2 registry sources and resolver -> reviewer decision |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | ASSF-T2 generated index and resolver and future ASSF-T3/T4 work |
| Disposition | candidate intake only; resolver selection never activates a skill |
| Route | consume the accepted ASSF-T1 contract |
| Boundary | metadata only; no instruction loading or activation |
| External-agent disposition | required in matrix and in registry source fields |
| Claim boundary | legacy and external skills remain candidate inputs, not CVF authority |

## Rescan Intelligence Hardening

- Original source artifact: `docs/reviews/CVF_ASSF_T1_CANONICAL_PACKAGE_CONTRACT_COMPLETION_2026-06-23.md`
- Predecessor intake artifact: `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`
- Delta ledger status: worker must refresh in the worker-return packet.
- Routing matrix status: worker must refresh in the worker-return packet.
- Semantic sampling status: worker must include at least three samples in the worker-return packet.
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Delta category | Worker instruction |
|---|---|
| `UNCHANGED_FROM_INTAKE` | preserve the ASSF-T1 contract field families and lifecycle states as schema authority |
| `CHANGED_DISPOSITION` | record the contract moving from a definition into executable registry sources, generator, drift checker, and resolver |
| `NEW_FINDING` | record any field a registry source needs that the contract does not define, as a contract gap |
| `REMOVED_OR_REJECTED` | record hand-edited-aggregate and instruction-loading resolver behavior as rejected |

### Follow-Up Routing Matrix

| Routing lane | Worker instruction |
|---|---|
| `DO_NOW` | build registry sources, generator, drift checker, resolver, generated index, READMEs, tests, and the worker-return packet |
| `SEPARATE_RUNTIME_TRANCHE` | route CLI/MCP adapter and runtime activation to ASSF-T5/T7 |
| `STRATEGIC_OPERATOR_DECISION` | flag whether the drift checker should be wired into an autorun phase before ASSF-T3 |
| `OUT_OF_SCOPE` | mark migration of existing CVF Web examples, public-sync, and runtime/provider/live out of scope |
| `RESOLVED_BY_DESIGN` | mark items handled by the read-only-resolver and drift-checked-generator design |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| ASSF-T2-WO-S1 | roadmap ASSF-T2 tranche | resolver returns metadata before loading instructions | read-only resolver required | could the resolver open a SKILL.md body? | reject |
| ASSF-T2-WO-S2 | generated aggregate standard Rule | aggregate built only by deterministic generator | drift checker required | could the index be hand-edited? | reject |
| ASSF-T2-WO-S3 | dual-agent standard | external CLI/MCP disposition required | matrix and source field required | could an internal-only resolver pass? | reject |

The worker must record whether this defect class should become a future
machine-check candidate. At minimum, evaluate:

- whether the ASSF index drift checker should be wired into an autorun phase
  before ASSF-T3;
- whether closure packets should fail if a generated aggregate lacks a
  matching drift checker;
- whether the resolver read-only property should have a standing regression test.

## Finding-To-Governance Learning Disposition

| Field | Required worker value |
|---|---|
| Defect class | choose one or more: `RULE_GAP`, `MACHINE_GATE_GAP`, `PHASE_GATE_PLACEMENT_GAP`, `OPERATOR_SCOPE_CLARITY_GAP` |
| Learning lane | `GOVERNANCE_CONTROL_PLANE` |
| Disposition | `DESIGN_REVIEW_REQUIRED`, `MACHINE_CHECK_CANDIDATE`, or `REFERENCE_ONLY` |
| Runtime/provider/cost lane | `N/A_WITH_REASON` unless a runtime/provider/cost finding arises |
| Next control action | state whether ASSF-T3/T7 should absorb each control (e.g. wiring the drift checker into autorun) |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: the registry sources carry provenance reconciled from a private legacy
absorption ledger. Public-safe skill index output requires later redaction and
public-sync authority.

## Acceptance Criteria

- Required artifacts exist in allowed paths only, including a README front door
  in each new reference-family subfolder.
- At least one compact registry source conforms to the contract field families,
  proven by a contract-conformance table.
- The generated index is produced only by the deterministic generator and the
  drift checker fails on a hand-edited index, both proven by tests.
- The resolver is read-only, deterministic, returns metadata without loading
  any package instruction body, and respects the contract lifecycle states,
  proven by tests.
- The Dual Agent Surface Matrix accounts for internal and external CLI/MCP
  consumers.
- No CLI/MCP adapter, skill activation, package instruction execution, or
  migration is created.
- The worker return carries the Core Guard Self-Protection Authorization block,
  the `GENERATED_SOURCE_LAYOUT_ADDED` token, and a top-level `Status:` line.
- No commit is made by the worker.
- Reviewer-fast gates and the new tests are run or failure is classified.

## Stop Conditions

Return `BLOCKED_WITH_REASON` if:

- the pre-implementation gate fails outside allowed scope;
- the ASSF-T1 contract or the named precedents are unavailable;
- the worker cannot create the required artifacts;
- a registry source needs a field the contract does not define (report the
  contract gap rather than changing the contract);
- a repair would require session sync, roadmap/baseline/work-order edits,
  public-sync, live/provider proof, CLI/MCP adapter or runtime activation,
  modification of an existing protected guard, or a commit.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Roadmap state | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | `Status: ASSF_T2_CLOSED_PASS_BOUNDED_PENDING_T3_SELECTION` | PASS |
| GC-018 status | `docs/baselines/CVF_GC018_ASSF_T2_GENERATED_INDEX_AND_PROGRESSIVE_RESOLVER_2026-06-23.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion review | `docs/reviews/CVF_ASSF_T2_GENERATED_INDEX_AND_PROGRESSIVE_RESOLVER_COMPLETION_2026-06-23.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Worker return | `docs/reviews/CVF_ASSF_T2_GENERATED_INDEX_AND_PROGRESSIVE_RESOLVER_WORKER_RETURN_2026-06-23.md` | `Status: COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`, accepted after reviewer repair | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ASSF_T2_GENERATED_INDEX_AND_PROGRESSIVE_RESOLVER_COMPLETION_2026-06-23.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Generated source layout | registry sources plus generator plus drift checker | `GENERATED_SOURCE_LAYOUT_ADDED` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | BLOCKED with reason: ASSF-T2 is not authorized to update GC-051 corpus registry surfaces; the new generated skill index is a separate, T1-contract-scoped aggregate | BLOCKED with reason |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | BLOCKED with reason: ASSF-T2 is not authorized to update GC-051 corpus registry surfaces; the new generated skill index is a separate, T1-contract-scoped aggregate | BLOCKED with reason |
| External evidence digest | N/A with reason | no external evidence imported in this tranche | N/A with reason |
| System loop interlock | this work order | T1 contract was required before T2 and is now consumed; T2 is required before T3; no automatic package activation | PASS |
| Session continuity | active session sync after material commit | separate session-sync lane after material commit | PASS |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |
| Runtime/provider/live | N/A with reason | no runtime/provider/live claim | N/A with reason |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Durable files created by worker | registry sources, generator, drift checker, resolver, generated index, two new subfolder READMEs, three test files, and the worker-return packet |
| Canonical package root | PARTIAL_CREATED: T2 creates `registry/` and `generated/` subfolders with sources and the generated index; it does not create `packages/<skill-id>/` or any `SKILL.md` instruction body |
| Generated index or aggregate | `generated/skill-index.json` produced only by the deterministic generator, drift-checked |
| Storage migration | N/A with reason: out of scope; ASSF-T6 scope |
| New reference-family folders | `registry/` and `generated/` each require a `README.md` front door, named in the Work-Order Fulfillment Manifest |
| Layout risk | bounded executable data plane; reviewer owns closure commit |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Work order status | `DISPATCH_READY` | `DISPATCH_READY` | PASS |
| Worker commit mode | `WORKER_MUST_NOT_COMMIT` | `WORKER_MUST_NOT_COMMIT` | PASS |
| Allowed output paths | registry/generator/drift/resolver/index/READMEs/tests/worker-return only | as listed | PASS |
| T1 contract consumption required | yes | yes | PASS |
| Generated index hand-edit | forbidden; drift-checked | forbidden by work order | PASS |
| Resolver instruction loading | forbidden; read-only | forbidden by work order | PASS |
| New-folder README front doors | required | named in manifest | PASS |
| Generator/drift/resolver implementation | required with tests | required by work order | PASS |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | Worker-return ASSF generated index, generator, drift checker, and read-only resolver only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE - no-commit executable-data-plane worker-return dispatch |
| receiptEvidence | CVF_RECEIPT_PRESENT - worker must provide command, test, and gate receipts in the return packet |
| actionEvidence | ACTION_EVIDENCE_PRESENT - worker must provide conformance, determinism, drift, and read-only proofs plus changed-set evidence |
| invocationBoundary | governed local automation authoring and read-only resolver execution |
| interceptionBoundary | no provider/runtime/API/browser interception claim |
| claimLanguage | build a generated index, generator, drift checker, and read-only resolver |
| forbiddenExpansion | no CLI/MCP adapter, skill activation, package instruction execution, migration, runtime/provider/live, public-sync, or hand-edited aggregate |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Claude dispatcher |
| Provider or surface | local workspace |
| Session or invocation | ASSF-T2 dispatch, 2026-06-23 |
| Working directory | repository root |
| Command or tool surface | source reads, file authoring, governance gates, git commit by reviewer only |
| Target paths | this work order; T2 GC-018 baseline |
| Allowed scope source | operator instruction to author the ASSF-T2 work order with full executable scope |
| Before status evidence | clean worktree at HEAD `4d8ecc06` |
| After status evidence | ASSF-T2 dispatch ready |
| Diff evidence | real-range name-status and gate output before reviewer commit |
| Approval boundary | dispatch authoring only |
| Claim boundary | worker-return lane; no data-plane build |
| Agent type | dispatcher |
| Invocation ID | `cvf-assf-t2-generated-index-and-progressive-resolver-work-order-2026-06-23` |
| Expected manifest | this work order; T2 GC-018 baseline |
| Actual changed set | this work order; T2 GC-018 baseline |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Claim Boundary

This work order authorizes only a no-commit worker-return lane that builds the
ASSF generated index, deterministic generator, drift checker, read-only
resolver, at least one compact registry source, required folder READMEs, and
paired tests. It does not authorize ASSF-T3, a CLI/MCP adapter, skill
activation, package instruction execution, migration of any existing CVF Web
example, runtime/provider/live proof, public-sync, modification of any existing
protected guard, a change to the frozen ASSF-T1 contract, session sync, or
worker commit.
