# CVF GC-018 Baseline: ASSF-PIC-T1 Package Instance Evidence Skeleton Hardening

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-26

docType: baseline

Batch ID: ASSF-PIC-T1

dispatchBaseHead: 8afaf0e7

## Proposed Tranche

Tranche: ASSF-PIC-T1

Baseline decision: authorize a bounded worker-executed evidence skeleton
hardening pass for the single ASSF-PIC-T0 selected candidate
`cvf-dispatch-quality-reviewer`. This tranche creates documentation evidence
for the package-instance evidence shape only. It does not create a package
instance, certify a package, advance lifecycle state, mutate the generated
index, mutate resolver behavior, change Web runtime, implement a CLI/MCP
adapter, run provider/live proof, public-sync, push, or activate a package.

Verdicts:

- Dispatcher verdict: DISPATCH_APPROVED
- Worker verdict: COMPLETE_PENDING_REVIEW
- Reviewer verdict: CLOSED_PASS_BOUNDED

## Purpose

The prior worker-return path exposed avoidable report-format friction. This
baseline releases a narrow ASSF-PIC-T1 worker task that must use the new
worker-return scaffold helper before writing the return packet. The worker
will produce:

- one package-evidence skeleton hardening audit for the selected candidate;
- one scaffold-first worker return that records how many format issues remain;
- no package instance or certification decision.

Success means Claude can complete the worker return with fewer manual
format-repair loops while preserving hard controls for authority, source
verification, changed paths, receipt evidence, and claim boundaries.

## Evidence / Verification

Dispatch evidence is limited to the ASSF-PIC roadmap, PIC-T0 closure evidence,
the selected registry entry, ASSF package/certification contracts, ADIF
disclosure, and the worker-return scaffold helper. Worker-created audit and
worker-return files do not exist at dispatch time and must not be claimed as
complete until Claude returns uncommitted artifacts and Codex reviews them.

## Scope / Applies To

Applies to:

- selected-candidate evidence skeleton audit under the planned audit path;
- scaffold-first worker-return authoring under the planned review path;
- command-backed measurement of worker-return scaffold and fast-gate behavior;
- reviewer closure after no-commit worker return.

Does not apply to:

- ASSF package instance creation;
- ASSF certification or UAT decision;
- ASSF generated-index mutation;
- ASSF resolver mutation;
- CVF Web runtime mutation;
- CLI/MCP adapter implementation;
- provider call, live proof, public-sync, push, package activation, or package
  instruction execution.

## Dependency Release Evidence

| Dependency | Status | Evidence |
|---|---|---|
| ASSF-PIC roadmap exists and defines PIC-T1 package evidence skeleton hardening | SATISFIED | `docs/roadmaps/CVF_ASSF_PACKAGE_INSTANCE_CERTIFICATION_PILOT_ROADMAP_2026-06-25.md` lines 177-190 |
| ASSF-PIC-T0 selected exactly one candidate | SATISFIED | `docs/reviews/CVF_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_COMPLETION_2026-06-25.md` lines 46-48 |
| Candidate identity is source-backed | SATISFIED | `docs/audits/CVF_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_AUDIT_2026-06-25.md` lines 83 and 102-107 |
| State-bootstrap blocker has been closed before this dispatch base | SATISFIED | `AGENT_HANDOFF_V22_2026-06-22.md` current active handoff references HEAD `8afaf0e7`; startup acknowledgment recorded current next move as ASSF-PIC-T1 GC-018/work order creation |
| Current dispatch worktree isolation | SATISFIED | `git status --short` returned no paths before authoring |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | ASSF-PIC-T1 audit and worker-return artifacts for `cvf-dispatch-quality-reviewer` | internal agents may inspect and harden evidence skeleton requirements only; no lifecycle advance, generated-index update, resolver behavior, Web projection, commit authority, activation, package execution, or certification is granted | this baseline, paired work order, PIC-T0 audit/completion, ASSF package contract, T7 lifecycle guard | no internal loader, resolver, generator, Web bridge, or package root is implemented | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future external package readout or adapter claim | external agents cannot mutate, certify, activate, execute, or consume packages through this tranche | Dual Agent Surface Accounting Standard and T7 adapter honesty contract | adapter implementation is deferred to a separate source-verified work order | `DEFERRED_WITH_REASON` |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| ASSF-PIC-T1 is package instance evidence and skeleton hardening | `docs/roadmaps/CVF_ASSF_PACKAGE_INSTANCE_CERTIFICATION_PILOT_ROADMAP_2026-06-25.md` | lines 177-190 | `ASSF-PIC-T1` | ASSF-PIC roadmap | LITERAL_INVARIANT | ACCEPT |
| PIC-T0 selected `cvf-dispatch-quality-reviewer` | `docs/reviews/CVF_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_COMPLETION_2026-06-25.md` | lines 46-48 | `cvf-dispatch-quality-reviewer` | ASSF-PIC-T0 completion review | VALUE_SET | ACCEPT |
| Candidate source entry exists | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | lines 3-5 | `skillId` | ASSF-T2 registry source entry | EXISTS | ACCEPT |
| Candidate has source artifacts and selectors | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | lines 10, 32-43 | `sourceArtifacts` | ASSF-T2 registry source entry | VALUE_SET | ACCEPT |
| Candidate acceptance evidence and no side effects are declared | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | lines 58 and 61 | `acceptanceEvidence` | ASSF-T2 registry source entry | VALUE_SET | ACCEPT |
| Candidate UAT and certification states are not started | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | lines 67-68 | `uatState` | ASSF-T2 registry source entry | VALUE_SET | ACCEPT |
| Package contract defines lifecycle and evidence fields | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | lines 56-75 and 128 | `certificationState` | ASSF-T1 package schema | EXISTS | ACCEPT |
| Package contract defines internal and external disposition fields | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | lines 133-141 | `externalCliMcpDisposition` | ASSF-T1 package schema | VALUE_SET | ACCEPT |
| T7 lifecycle guard blocks certification without UAT evidence | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | lines 69-98 | `MISSING_UAT` | ASSF-T7 certification lifecycle guard | LITERAL_INVARIANT | ACCEPT |
| T7 lifecycle guard defines generated-index and resolver drift classes | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | lines 118-121 | `GENERATED_INDEX_DRIFT` | ASSF-T7 certification lifecycle guard | VALUE_SET | ACCEPT |
| Worker-return scaffold helper writes one new worker-return scaffold | `governance/compat/run_worker_return_scaffold.py` | lines 152-188 | `write_scaffold` | worker-return scaffold helper | RUNTIME_BEHAVIOR | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects:

- ADIF-0001: Exhaustive directory claim omits actual children
- ADIF-0002: Provider-local interaction accepted as authority
- ADIF-0007: Gate keyword in exclusion prose triggers wrong evidence class
- ADIF-0006: Source Verification symbol cell contains a value/type

Remediation applied:

- ADIF-0001: This baseline cites bounded files and exact planned artifacts
  only; no exhaustive directory coverage claim is made.
- ADIF-0002: ACCEPT rows cite CVF-governed repository files only.
- ADIF-0007: Scope exclusions are kept as boundaries, not evidence claims.
- ADIF-0006: Verified path or symbol cells contain only paths, fields,
  functions, sections, or tokens.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator feedback about Claude worker-return friction routed to local scaffold-effectiveness measurement |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this ASSF-PIC-T1 baseline and paired work order |
| Disposition | local process-evidence dispatch only; no provider-local report is accepted as source authority |
| Claim boundary | operator/Claude feedback motivates the trial; all source facts still cite CVF-governed files |

## Planned Artifact Manifest

| Path | Owner | Purpose |
|---|---|---|
| `docs/audits/CVF_ASSF_PIC_T1_PACKAGE_INSTANCE_EVIDENCE_SKELETON_HARDENING_AUDIT_2026-06-26.md` | Claude worker | selected-candidate evidence skeleton hardening audit |
| `docs/reviews/CVF_ASSF_PIC_T1_PACKAGE_INSTANCE_EVIDENCE_SKELETON_HARDENING_WORKER_RETURN_2026-06-26.md` | Claude worker | scaffold-first no-commit worker return |
| `docs/reviews/CVF_ASSF_PIC_T1_PACKAGE_INSTANCE_EVIDENCE_SKELETON_HARDENING_COMPLETION_2026-06-26.md` | Codex reviewer/closer | reviewer-owned completion review after accepted worker return |

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | Worker return is created through `governance/compat/run_worker_return_scaffold.py --write` before manual filling. |
| AC2 | Worker return records scaffold command, first fast-gate result, remaining manual format repairs, and final fast-gate result. |
| AC3 | Audit maps selected-candidate evidence requirements without creating a package instance or changing lifecycle state. |
| AC4 | Audit and worker return include exact changed paths and command-backed evidence. |
| AC5 | No generated index, resolver, Web runtime, CLI/MCP adapter, provider/live proof, public-sync, push, package activation, or certification claim appears in worker changes. |
| AC6 | Claude returns uncommitted artifacts only under `WORKER_MUST_NOT_COMMIT`. |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| Worker return | `docs/reviews/CVF_ASSF_PIC_T1_PACKAGE_INSTANCE_EVIDENCE_SKELETON_HARDENING_WORKER_RETURN_2026-06-26.md` |
| Completion review | `docs/reviews/CVF_ASSF_PIC_T1_PACKAGE_INSTANCE_EVIDENCE_SKELETON_HARDENING_COMPLETION_2026-06-26.md` |
| Closure decision | `CLOSED_PASS_BOUNDED` |
| Roadmap disposition | ASSF-PIC-T1 closed bounded; ASSF-PIC-T2 parked pending work-order dispatch scaffold optimization |
| Session-sync disposition | required after material closure commit, in a separate commit |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Baseline status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_PIC_T1_PACKAGE_INSTANCE_EVIDENCE_SKELETON_HARDENING_FOR_CLAUDE_2026-06-26.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Worker return | `docs/reviews/CVF_ASSF_PIC_T1_PACKAGE_INSTANCE_EVIDENCE_SKELETON_HARDENING_WORKER_RETURN_2026-06-26.md` | `Status: COMPLETE_PENDING_REVIEW` | PASS |
| Evidence audit | `docs/audits/CVF_ASSF_PIC_T1_PACKAGE_INSTANCE_EVIDENCE_SKELETON_HARDENING_AUDIT_2026-06-26.md` | `EVIDENCE_SKELETON_MAPPED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ASSF_PIC_T1_PACKAGE_INSTANCE_EVIDENCE_SKELETON_HARDENING_COMPLETION_2026-06-26.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_ASSF_PACKAGE_INSTANCE_CERTIFICATION_PILOT_ROADMAP_2026-06-25.md` | PIC-T1 `CLOSED_PASS_BOUNDED`; PIC-T2 parked for work-order dispatch scaffold optimization | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | not authorized for PIC-T1 closure; no GC-051 corpus registry mutation in scope | BLOCKED with reason |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | not authorized for PIC-T1 closure; no GC-051 corpus registry mutation in scope | BLOCKED with reason |
| External evidence digest | N/A with reason | no external evidence imported | N/A with reason |
| System loop interlock | this baseline | T1 closed bounded; T2 parked; next lane is optimization | PASS |
| Session continuity | N/A with reason | separate session-sync commit required after material closure | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| Runtime receipt evidence absent for T1 | `receiptEvidence` is `N/A with reason` | PASS |
| Evidence skeleton mapped | `EVIDENCE_SKELETON_MAPPED` | PASS |
| Selected candidate unchanged | `cvf-dispatch-quality-reviewer` | PASS |
| UAT/certification not advanced | `uatState` and `certificationState` remain `NOT_STARTED` | PASS |
| PIC-T2 not released | roadmap T2 parked for optimization lane | PASS |

## Claim Boundary

This baseline authorizes dispatch of ASSF-PIC-T1 documentation evidence
skeleton hardening only. It does not create or certify a package, advance
`uatState` or `certificationState`, mutate the generated index or resolver,
change Web runtime, implement an adapter, run live proof, public-sync, push,
or update session continuity.
