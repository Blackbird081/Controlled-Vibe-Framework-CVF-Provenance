# CVF Agent Work Order: ASSF-PIC-T1 Package Instance Evidence Skeleton Hardening

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-06-26

docType: work_order

Batch ID: ASSF-PIC-T1

dispatchBaseHead: 8afaf0e7

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: Worker. Reviewer/closer is Codex after worker return.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_PIC_T1_PACKAGE_INSTANCE_EVIDENCE_SKELETON_HARDENING_FOR_CLAUDE_2026-06-26.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`

executionBaseHead: record with `git rev-parse --short HEAD` at worker start.

Current-time notes: ASSF-PIC-T0 is closed bounded and selected exactly one
candidate, `cvf-dispatch-quality-reviewer`. The state-bootstrap blocker has
been handled before dispatch base `8afaf0e7`. This ASSF-PIC-T1 task is a
documentation evidence-skeleton hardening pass plus a worker-return scaffold
effectiveness trial.

Do-not-misread notes: this is not package instance creation and not
certification. Do not create package roots, `SKILL.md`, `skill.source.json`,
registry entries, generated index changes, resolver changes, Web runtime
changes, CLI/MCP adapter behavior, provider/live proof, public-sync, push,
package activation, or lifecycle state advancement.

Required first actions: read this work order, read the paired GC-018 baseline,
read `CVF_SESSION_MEMORY.md`, read
`CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`, resolve
`CVF_SESSION/ACTIVE_SESSION_STATE.json`, read `AGENT_HANDOFF_V22_2026-06-22.md`,
read `docs/reference/guard_orientation/README.md`, read
`docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`,
then record actual `executionBaseHead` and `git status --short`.

Return contract: return `COMPLETE_PENDING_REVIEW` with uncommitted artifacts
only, actual `executionBaseHead`, actual `git status --short`, changed paths,
source inventory, focused command evidence, worker-return scaffold measurement,
and no commit. If blocked, return `BLOCKED_WITH_REASON` and name the exact
source, scope, or gate that blocks completion.

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | operator request to issue a Claude work order to test the worker-return/report-friction changes |
| Scope classification | bounded ASSF-PIC-T1 documentation evidence skeleton hardening and worker-return scaffold effectiveness trial |
| Intake role | worker authors audit and scaffold-first worker return |
| Reviewer role | Codex reviewer/closer validates artifacts, gates, boundaries, and commits accepted material |
| Routing decision | `WORKER_MUST_NOT_COMMIT`; worker returns uncommitted artifacts |
| Public route | `DEFERRED_PRIVATE_ONLY`; no public-sync |
| canonical route mode | `MULTI_AGENT_SINGLE_ROLE` |
| selected role route | worker return to reviewer/closer closure conversion |
| escalation condition | stop and return `BLOCKED_WITH_REASON` if completion would require package instance creation, certification, lifecycle state advancement, generated-index mutation, resolver mutation, Web runtime, CLI/MCP adapter, provider/live proof, public-sync, push, package activation, destructive action, or a broader ASSF roadmap change |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_SINGLE_ROLE` |
| rolePattern | dispatcher creates packet; worker executes ASSF-PIC-T1 documentation-only tranche and returns no-commit evidence; reviewer/closer reviews, commits accepted material, and session-syncs if accepted |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=8afaf0e7`; `executionBaseHead` recorded by worker; `closureBaseHead` set by reviewer before closure commit |
| changedSetScope(phase) | execution changes only Write Ownership paths; closer owns status conversion, reviewer artifact, accepted material commit, and later session-sync |
| traceScope(phase, actor) | worker-return trace covers pending ASSF-PIC-T1 artifacts only; reviewer trace covers review/closure; session-sync trace covers continuity only |
| commitOwner(phase) | worker commits nothing (`WORKER_MUST_NOT_COMMIT`); reviewer/closer owns any material, closure, or session-sync commit |
| crossBatchIsolation | do not mix this tranche with package instance creation, certification, generated-index/resolver/Web/runtime/adapter/provider/public-sync work, or another dispatch batch |
| Before status evidence | dispatchBaseHead `8afaf0e7`; clean worktree evidence: `git status --short` returned no paths before dispatch authoring |
| nextMoveSurfaces | reviewer/closer updates next-move surfaces only after accepted material review if mode or next allowed move changes |
| Closer designation | Codex reviewer/closer role is the designated closer |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| completionReviewPath | `docs/reviews/CVF_ASSF_PIC_T1_PACKAGE_INSTANCE_EVIDENCE_SKELETON_HARDENING_COMPLETION_2026-06-26.md` |
| reviewerOwnedClosurePaths | this work order; paired GC-018 baseline; worker-return artifact; ASSF-PIC roadmap status rows if accepted; reviewer completion review; optional session-sync surfaces if accepted |
| workerReturnStatus | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
| closer | Codex reviewer/closer role |

## Purpose

Create a selected-candidate evidence skeleton hardening audit for
`cvf-dispatch-quality-reviewer`, then create a scaffold-first worker return
that measures whether the new worker-return helper reduces report-format
violations. The audit must identify evidence requirements and gaps for a later
manual package-instance/certification path, without creating the package
instance or making a certification decision.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-26 request to issue Claude work order and test the recent report-friction changes | ACCEPT |
| Active session front door | `CVF_SESSION_MEMORY.md` | ACCEPT |
| Active session bootstrap read model | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | ACCEPT |
| Active session state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V22_2026-06-22.md` | ACCEPT |
| Paired GC-018 baseline | `docs/baselines/CVF_GC018_ASSF_PIC_T1_PACKAGE_INSTANCE_EVIDENCE_SKELETON_HARDENING_2026-06-26.md` | ACCEPT |
| ASSF-PIC roadmap | `docs/roadmaps/CVF_ASSF_PACKAGE_INSTANCE_CERTIFICATION_PILOT_ROADMAP_2026-06-25.md` | ACCEPT |
| PIC-T0 completion review | `docs/reviews/CVF_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_COMPLETION_2026-06-25.md` | ACCEPT |
| PIC-T0 audit | `docs/audits/CVF_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_AUDIT_2026-06-25.md` | ACCEPT |
| ASSF package contract | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | ACCEPT |
| ASSF certification lifecycle guard | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | ACCEPT |
| Worker-return scaffold helper | `governance/compat/run_worker_return_scaffold.py` | ACCEPT |

## Agent Roles

| Role | Owner |
|---|---|
| Operator | project authority and scope approval |
| Dispatcher | Codex dispatch author role |
| Worker | Claude documentation/audit and no-commit return role |
| Reviewer | Codex reviewer role after worker return |
| Closer | Codex closer role after acceptance |
| Session-sync steward | Codex session-sync role after material commit if next move changes |

## Required First Reads

| Source | Reason |
|---|---|
| `docs/baselines/CVF_GC018_ASSF_PIC_T1_PACKAGE_INSTANCE_EVIDENCE_SKELETON_HARDENING_2026-06-26.md` | authorization, scope, and claim boundary |
| `CVF_SESSION_MEMORY.md` | active front door and current next allowed move |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | compact startup read model |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | current generated aggregate and active handoff pointer |
| `AGENT_HANDOFF_V22_2026-06-22.md` | active handoff and current session continuity |
| `docs/reference/guard_orientation/README.md` | task-first guard orientation |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | pre-write checklist for gate-parsed artifacts |
| `docs/roadmaps/CVF_ASSF_PACKAGE_INSTANCE_CERTIFICATION_PILOT_ROADMAP_2026-06-25.md` | ASSF-PIC sequence and T1 boundary |
| `docs/reviews/CVF_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_COMPLETION_2026-06-25.md` | T0 closure and selected candidate |
| `docs/audits/CVF_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_AUDIT_2026-06-25.md` | selected-candidate source inventory |
| `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | selected candidate source entry |
| `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | package evidence and lifecycle fields |
| `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | certification/UAT/drift/adaptor claim boundaries |
| `governance/compat/run_worker_return_scaffold.py` | required worker-return scaffold generator |
| `governance/compat/run_worker_return_fast_gate.py` | required early worker-return gate |

## Pre-Flight Checks

The worker must run these before editing. For commands that use
`<executionBaseHead>`, replace it with the exact value returned by
`git rev-parse --short HEAD` at worker start.

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/run_agent_commit_steward_preflight.py --mode worker-return --base <executionBaseHead> --head HEAD --enforce
Test-Path docs/audits/CVF_ASSF_PIC_T1_PACKAGE_INSTANCE_EVIDENCE_SKELETON_HARDENING_AUDIT_2026-06-26.md
Test-Path docs/reviews/CVF_ASSF_PIC_T1_PACKAGE_INSTANCE_EVIDENCE_SKELETON_HARDENING_WORKER_RETURN_2026-06-26.md
```

If a command fails before edits because of a pre-existing out-of-scope
violation, record it in the worker return and continue only when the violation
does not affect the allowed changed paths. Do not repair out-of-scope material.

## Worker Return Packet Shape Contract

The worker-return artifact must be scaffold-first. The scaffold helper supplies
the starting shape, and the completed worker return must retain or complete the
sections listed below so reviewer-fast can diagnose issues before closure:

- `Status`
- `dispatchWorkOrder`
- `Purpose`
- `Source Inventory`
- `Scope / Methodology`
- `Findings / Position`
- `Risk / Corrective Action`
- `Claim Boundary`
- `Agent Operation Trace Block`
- `Delta Execution Claim Boundary Control Block`
- `Public Export Disposition`
- `External Knowledge Intake Routing`
- `Rescan Intelligence Hardening`
- `Corpus Completeness And Report Integrity`
- `Finding-To-Governance Learning Disposition`
- `Epistemic Process Block`
- `Worker Return Scaffold Effectiveness Measurement`
- `Machine Closure Package`
- actual `executionBaseHead`
- actual `git status --short`
- changed-path list
- command evidence
- no commit statement

If any section is not applicable, include the section with `N/A with reason`
or `NOT_APPLICABLE_WITH_REASON` and a short reason instead of omitting it.

### Worker Return Scaffold-First Requirement

Before writing long report content, the worker must create the worker return
from the scaffold helper:

```powershell
python governance/compat/run_worker_return_scaffold.py --write docs/reviews/CVF_ASSF_PIC_T1_PACKAGE_INSTANCE_EVIDENCE_SKELETON_HARDENING_WORKER_RETURN_2026-06-26.md --title "CVF ASSF-PIC-T1 Package Instance Evidence Skeleton Hardening Worker Return"
```

Then fill the scaffold completely. Do not leave `TODO` strings in the returned
artifact. The worker return must include:

- `dispatchWorkOrder: ` followed by this work order path in backticks;
- `## Source Inventory` with real paths and actions;
- `receiptEvidence: CVF_RECEIPT_PRESENT - ...`;
- `Corpus verdict: NOT_APPLICABLE_WITH_REASON - ...`;
- `Defect class:` with a valid value used by the finding-to-governance guard;
- `Actual changed set` listing real changed paths, not shorthand prose;
- worker-return scaffold measurement fields named in the next section.

## Worker-Return Effectiveness Measurement

The worker return must include a section named:

`## Worker Return Scaffold Effectiveness Measurement`

Required rows:

| Field | Required content |
|---|---|
| scaffoldCommand | exact `run_worker_return_scaffold.py --write` command run |
| scaffoldCreated | `YES` or `NO_WITH_REASON` |
| firstFastGateCommand | exact `run_worker_return_fast_gate.py` command first run after filling the scaffold |
| firstFastGateResult | `PASS` or `FAIL_WITH_REPAIRS_LISTED` |
| manualFormatRepairsAfterFirstFastGate | list exact repairs made after first fast gate; use `NONE` only if first fast gate passed |
| finalFastGateResult | `PASS` or `BLOCKED_WITH_REASON` |
| remainingReportFriction | short bounded assessment of whether scaffold reduced report-format loops |

This measurement is not a certification decision. It is process evidence for
the recent worker-return friction reduction.

## Worker Autonomy / No-Question Rule

Within Allowed scope, the worker must repair machine-check, source-inventory,
packet-shape, focused-command, and worker-return fast-gate failures and rerun
the required checks without asking the operator. Ask the operator only if
remediation would exceed Allowed scope, change the claim boundary, require
package instance creation, certification, lifecycle state advancement,
generated-index mutation, resolver mutation, Web runtime, adapter work,
provider/live proof, public-sync, push, destructive action, or another roadmap
batch.

## Write Ownership

| Path | Owner | Disposition |
|---|---|---|
| `docs/audits/CVF_ASSF_PIC_T1_PACKAGE_INSTANCE_EVIDENCE_SKELETON_HARDENING_AUDIT_2026-06-26.md` | Claude worker | create selected-candidate evidence skeleton hardening audit |
| `docs/reviews/CVF_ASSF_PIC_T1_PACKAGE_INSTANCE_EVIDENCE_SKELETON_HARDENING_WORKER_RETURN_2026-06-26.md` | Claude worker | create scaffold-first no-commit worker return |
| `docs/reviews/CVF_ASSF_PIC_T1_PACKAGE_INSTANCE_EVIDENCE_SKELETON_HARDENING_COMPLETION_2026-06-26.md` | Codex reviewer/closer | create only after accepted worker return |
| this work order | Codex reviewer/closer | status conversion only after accepted worker return |
| paired GC-018 baseline | Codex reviewer/closer | status conversion only after accepted worker return |
| ASSF-PIC roadmap | Codex reviewer/closer | status conversion only after accepted worker return, if accepted |
| session-sync surfaces | Codex session-sync steward | update only after material commit if next move changes |

Claude worker may create or modify only these execution paths:

- `docs/audits/CVF_ASSF_PIC_T1_PACKAGE_INSTANCE_EVIDENCE_SKELETON_HARDENING_AUDIT_2026-06-26.md`
- `docs/reviews/CVF_ASSF_PIC_T1_PACKAGE_INSTANCE_EVIDENCE_SKELETON_HARDENING_WORKER_RETURN_2026-06-26.md`

Codex reviewer/closer later owns:

- `docs/reviews/CVF_ASSF_PIC_T1_PACKAGE_INSTANCE_EVIDENCE_SKELETON_HARDENING_COMPLETION_2026-06-26.md`
- this work order status conversion;
- paired GC-018 baseline status conversion;
- roadmap status conversion if accepted;
- session-sync surfaces after material commit if next move changes.

## Forbidden Changed Paths And Actions

The worker must not change:

- `docs/reference/agent_system_skills/registry/entries/*.json`
- `docs/reference/agent_system_skills/generated/skill-index.json`
- `governance/compat/run_assf_skill_resolver.py`
- `governance/compat/generate_assf_skill_index.py`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/**`
- `CVF_SESSION/**`
- `AGENT_HANDOFF_V22_2026-06-22.md`
- `CVF_SESSION_MEMORY.md`
- public-sync clone files or remotes.

The worker must not commit, push, run live/provider proof, create package
roots, create `SKILL.md`, create `skill.source.json`, activate a package,
advance `uatState`, advance `certificationState`, or claim certification.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Durable governance files created by worker | one audit file and one worker-return file only |
| New generated aggregate | N/A with reason: no generated aggregate or generated-index mutation is authorized |
| New source layout | N/A with reason: no source-layout split, registry source family, resolver source, Web source, or adapter source is authorized |
| Index or registry mutation | N/A with reason: ASSF generated index and registry entries remain out of scope |
| Storage owner | documentation evidence under the planned audit/review paths |
| Closure disposition required | reviewer verifies changed paths exactly match Write Ownership before any material commit |

## Required Audit Shape

Create:

`docs/audits/CVF_ASSF_PIC_T1_PACKAGE_INSTANCE_EVIDENCE_SKELETON_HARDENING_AUDIT_2026-06-26.md`

Required sections:

- `Status: COMPLETE_PENDING_REVIEW`
- `Selected Candidate`
- `Source Inventory`
- `Evidence Skeleton Requirements`
- `Evidence Gap Matrix`
- `Lifecycle And Certification Boundary`
- `Dual Agent Surface Matrix`
- `Source Verification Block`
- `Claim Boundary`
- `Worker Return Scaffold Effectiveness Link`

The audit must map the selected candidate's existing fields and source
artifacts to the package contract's evidence requirements. It may recommend
what a future package instance should contain, but it must label those rows as
future-required evidence, not as created package material.

## Execution Plan

1. Complete all Required First Reads and Pre-Flight Checks.
2. Create the worker-return scaffold with `run_worker_return_scaffold.py
   --write` before drafting the long return.
3. Create the ASSF-PIC-T1 evidence skeleton hardening audit under Write
   Ownership.
4. Fill the worker return from the scaffold and record scaffold effectiveness
   measurement rows.
5. Run required commands, repair allowed-scope worker-return format defects,
   and rerun `run_worker_return_fast_gate.py`.
6. Return `COMPLETE_PENDING_REVIEW` with no commit when all allowed-scope
   checks pass, or `BLOCKED_WITH_REASON` with exact blocker evidence.

## Evidence Requirements

The worker-return artifact must record:

- actual `executionBaseHead`;
- actual `git status --short`;
- exact changed paths;
- source inventory for every file read or changed;
- scaffold command and scaffold-created result;
- first and final `run_worker_return_fast_gate.py` results;
- manual format repairs after first fast gate, or `NONE`;
- `git diff --check`;
- `git diff --name-status`;
- explicit no-commit statement;
- explicit statement that no package instance, certification, generated index,
  resolver, Web runtime, CLI/MCP adapter, provider/live proof, public-sync,
  push, activation, session-sync, or lifecycle state change occurred.

## Required Commands Before Return

Run and record results:

```powershell
git status --short
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git diff --name-status
```

If `run_worker_return_fast_gate.py` fails because the worker-return artifact is
still malformed, repair the artifact and rerun it. If it fails because of an
out-of-scope pre-existing violation, record the exact failing command and
return `BLOCKED_WITH_REASON`.

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

- ADIF-0001: This work order cites bounded files and exact planned artifacts
  only; the worker must list real changed paths.
- ADIF-0002: ACCEPT rows cite CVF-governed repository files only.
- ADIF-0007: Scope exclusions are boundaries, not evidence claims.
- ADIF-0006: Verified path or symbol cells contain only paths, fields,
  functions, sections, or tokens.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | local governance/process-improvement dispatch; no external source fact is promoted to authority |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this ASSF-PIC-T1 work order and paired GC-018 baseline |
| Disposition | worker-return scaffold effectiveness is measured as local process evidence only |
| Claim boundary | operator/Claude report motivates the trial; implementation facts must still be source-verified against CVF-governed files |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap or checkpoint requirement | Work-order coverage | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| PIC-T0 selects exactly one candidate before later tranches | Authority Chain and Source Verification | selected candidate `cvf-dispatch-quality-reviewer` | T0 audit/completion review | SATISFIED |
| PIC-T1 hardens package evidence skeleton | Required Audit Shape | T1 audit path | reviewer diff and worker return | READY |
| No certification claim before later evidence | Lifecycle And Certification Boundary | audit and worker return claim boundary | reviewer closure | READY |
| Report-friction changes should be tested with a worker | Worker Return Scaffold Effectiveness Measurement | worker return measurement section | `run_worker_return_fast_gate.py` result | READY |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | ASSF-PIC-T1 audit and worker-return artifacts for `cvf-dispatch-quality-reviewer` | internal agents may inspect and harden evidence skeleton requirements only; no lifecycle advance, generated-index update, resolver behavior, Web projection, commit authority, activation, package execution, or certification is granted | this work order, paired baseline, PIC-T0 audit/completion, ASSF package contract, T7 lifecycle guard | no internal loader, resolver, generator, Web bridge, or package root is implemented | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future external package readout or adapter claim | external agents cannot mutate, certify, activate, execute, or consume packages through this tranche | Dual Agent Surface Accounting Standard and T7 adapter honesty contract | adapter implementation is deferred to a separate source-verified work order | `DEFERRED_WITH_REASON` |

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | Worker return is created through `governance/compat/run_worker_return_scaffold.py --write` before manual filling. |
| AC2 | Worker return records scaffold command, first fast-gate result, remaining manual format repairs, and final fast-gate result. |
| AC3 | Audit maps selected-candidate evidence requirements without creating a package instance or changing lifecycle state. |
| AC4 | Audit and worker return include exact changed paths and command-backed evidence. |
| AC5 | No generated index, resolver, Web runtime, CLI/MCP adapter, provider/live proof, public-sync, push, package activation, or certification claim appears in worker changes. |
| AC6 | Claude returns uncommitted artifacts only under `WORKER_MUST_NOT_COMMIT`. |

## Review Gate

Codex reviewer/closer must verify the worker return against Write Ownership,
review the audit for source-backed evidence skeleton mapping, run reviewer-fast
or committed-range gates as appropriate, confirm the scaffold effectiveness
measurement is present, and only then convert accepted material into a
completion review and material commit.

## Closure Checklist

- [ ] Worker returned `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.
- [ ] Changed paths stay inside Write Ownership.
- [ ] Worker return was created through `run_worker_return_scaffold.py --write`.
- [ ] Worker return includes scaffold effectiveness measurement rows.
- [ ] Audit maps selected-candidate evidence skeleton requirements without
  creating a package instance.
- [ ] Required commands are recorded with PASS or blocking reason.
- [ ] Worker did not commit, push, public-sync, run provider/live proof, mutate
  generated index/resolver/Web/adapter/session state, activate a package, or
  claim certification.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` when the audit and worker return are present,
the worker-return fast gate passes, required evidence is recorded, and changed
files remain inside Write Ownership.

Return `BLOCKED_WITH_REASON` when a required source is missing, a required gate
cannot pass inside Allowed scope, the selected candidate proves unsuitable for
evidence-skeleton hardening, or the repair would require forbidden package,
runtime, provider, public, session-sync, or lifecycle scope.

## Operator Checkpoint

No operator checkpoint is required for routine allowed-scope remediation inside
this work order. Operator checkpoint is required only if execution would require
package instance creation, certification, lifecycle state advancement,
generated-index mutation, resolver mutation, Web runtime, CLI/MCP adapter
behavior, provider/live proof, public-sync, push, package activation,
secrets/quota, destructive action, or a change to the claim boundary.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ASSF-PIC-T1 package evidence skeleton hardening work order |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE -- dispatch work order only |
| receiptEvidence | N/A with reason: no runtime execution, provider call, adapter receipt, or worker return exists at dispatch |
| actionEvidence | ACTION_EVIDENCE_PRESENT -- Source Verification Block, dependency release evidence, ADIF disclosure, and planned manifest |
| invocationBoundary | governed local documentation evidence only |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, CLI, MCP, Web runtime, or adapter interception claim |
| claimLanguage | authorizes bounded no-commit documentation/audit execution by Claude worker |
| forbiddenExpansion | no package instance, certification decision, lifecycle advancement, generated-index mutation, resolver mutation, Web runtime change, CLI/MCP adapter, provider/live proof, public-sync, push, activation, package instruction execution, or session-sync |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch author role |
| Provider or surface | Codex local workspace |
| Session or invocation | ASSF-PIC-T1 dispatch authoring, 2026-06-26 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | file reads, rg, ADIF resolver import, apply_patch |
| Target paths | this work order; paired GC-018 baseline |
| Allowed scope source | operator request to issue a Claude work order to test worker-return/report-friction changes |
| Before status evidence | dispatchBaseHead `8afaf0e7`; clean worktree evidence: `git status --short` returned no paths before dispatch authoring |
| After status evidence | dispatch artifacts pending gate and commit |
| Diff evidence | `git diff --name-status` before material dispatch commit |
| Approval boundary | dispatch packet only; worker execution follows after material dispatch and session-sync |
| Claim boundary | repo-local dispatch evidence only; no runtime/provider/live/public claim |
| Agent type | dispatcher |
| Invocation ID | `assf-pic-t1-package-evidence-skeleton-dispatch-2026-06-26` |
| Expected manifest | `docs/baselines/CVF_GC018_ASSF_PIC_T1_PACKAGE_INSTANCE_EVIDENCE_SKELETON_HARDENING_2026-06-26.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_PIC_T1_PACKAGE_INSTANCE_EVIDENCE_SKELETON_HARDENING_FOR_CLAUDE_2026-06-26.md` |
| Actual changed set | `docs/baselines/CVF_GC018_ASSF_PIC_T1_PACKAGE_INSTANCE_EVIDENCE_SKELETON_HARDENING_2026-06-26.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_PIC_T1_PACKAGE_INSTANCE_EVIDENCE_SKELETON_HARDENING_FOR_CLAUDE_2026-06-26.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Handoff Prompt For Claude

You are Claude in the CVF repo:
`D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF`

Read this work order first:
`docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_PIC_T1_PACKAGE_INSTANCE_EVIDENCE_SKELETON_HARDENING_FOR_CLAUDE_2026-06-26.md`

Then execute exactly the bounded ASSF-PIC-T1 worker task. You are
`WORKER_MUST_NOT_COMMIT`.

Required output paths:

- `docs/audits/CVF_ASSF_PIC_T1_PACKAGE_INSTANCE_EVIDENCE_SKELETON_HARDENING_AUDIT_2026-06-26.md`
- `docs/reviews/CVF_ASSF_PIC_T1_PACKAGE_INSTANCE_EVIDENCE_SKELETON_HARDENING_WORKER_RETURN_2026-06-26.md`

Before writing the worker return, run:

```powershell
python governance/compat/run_worker_return_scaffold.py --write docs/reviews/CVF_ASSF_PIC_T1_PACKAGE_INSTANCE_EVIDENCE_SKELETON_HARDENING_WORKER_RETURN_2026-06-26.md --title "CVF ASSF-PIC-T1 Package Instance Evidence Skeleton Hardening Worker Return"
```

No commits. No package instance creation. No certification decision. No
generated-index mutation. No resolver mutation. No Web runtime change. No
CLI/MCP adapter. No provider/live proof. No public-sync/push.

Return `COMPLETE_PENDING_REVIEW` only after the worker-return fast gate passes,
or `BLOCKED_WITH_REASON` with the exact blocking command/scope reason.

## Claim Boundary

This work order authorizes Claude to produce ASSF-PIC-T1 documentation evidence
skeleton hardening and scaffold-first worker-return measurement only. It does
not authorize package creation, certification, lifecycle advancement,
generated-index mutation, resolver mutation, Web runtime changes, adapter
implementation, live/provider calls, public-sync, push, session-sync, or
commits.
