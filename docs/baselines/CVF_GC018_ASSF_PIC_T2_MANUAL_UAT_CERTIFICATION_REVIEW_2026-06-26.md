# CVF GC-018 Baseline: ASSF-PIC-T2 Manual UAT And Certification Review

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-06-26

docType: baseline

Batch ID: ASSF-PIC-T2

dispatchBaseHead: 61ad760c

## Dispatch Prompt Envelope

Role: Worker. Reviewer/closer is Codex after worker return.

Canonical packet:
`docs/baselines/CVF_GC018_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_2026-06-26.md`

Paired work order:
`docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_FOR_CLAUDE_2026-06-26.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Current-time notes: ASSF-PIC-T0 selected `cvf-dispatch-quality-reviewer`;
ASSF-PIC-T1 mapped its evidence skeleton; work-order dispatch scaffold
optimization is closed bounded at `d08e8ab6` with GC-020 classifier hotfix
`59197332`. This baseline releases only a manual UAT/certification evidence
review worker task.

Do-not-misread notes: this baseline does not create a package instance, does
not mutate `uatState` or `certificationState`, and does not certify the package
by itself. Worker output is uncommitted evidence for Codex review.

## Proposed Tranche

Tranche: ASSF-PIC-T2

Baseline decision: authorize a bounded no-commit worker review for the
single selected candidate `cvf-dispatch-quality-reviewer`. The worker may run
read-only local UAT evidence commands against the current dispatch packet and
may recommend one certification lifecycle disposition for reviewer decision.
The worker must not advance lifecycle state, edit package registry source,
edit generated index output, edit resolver source, edit CVF Web runtime, create
a package instance, implement a CLI/MCP adapter, run provider/live proof,
public-sync, push, or commit.

Verdicts:

- Dispatcher verdict: DISPATCH_APPROVED
- Worker verdict: PENDING_WORKER_RETURN
- Reviewer verdict: PENDING_REVIEW

## Purpose

Release ASSF-PIC-T2 as a manual UAT and certification evidence review for
`cvf-dispatch-quality-reviewer`. Success means the worker produces one
source-backed UAT/certification review and one scaffold-first worker return,
with command-backed evidence and an honest recommended lifecycle disposition:
`CERTIFICATION_HELD_WITH_REASON`, `CERTIFICATION_REJECTED`, or
`CERTIFIED_RECOMMENDATION_FOR_REVIEWER_ONLY`.

The default expected outcome is a hold recommendation unless evidence proves
otherwise, because the package registry currently records `uatState` and
`certificationState` as `NOT_STARTED` and this tranche does not authorize
registry mutation.

## Evidence / Verification

Dispatch evidence is limited to current CVF-governed source surfaces:

- ASSF-PIC roadmap;
- PIC-T0 selected-candidate audit and completion;
- PIC-T1 evidence skeleton audit and completion;
- selected registry entry;
- ASSF package contract;
- ASSF certification lifecycle guard;
- worker-return scaffold and fast gate helpers;
- current dispatch-quality gates for the selected candidate's declared
  acceptance evidence.

Worker-created review and worker-return files do not exist at dispatch time
and must not be claimed as complete until the worker returns uncommitted
artifacts and Codex accepts them.

## Scope / Applies To

Applies to:

- manual UAT evidence review for the selected candidate;
- certification recommendation review for the selected candidate;
- scaffold-first worker-return authoring;
- read-only local gate execution for candidate acceptance evidence;
- reviewer closure after no-commit worker return.

Does not apply to:

- package instance creation;
- `SKILL.md` or `skill.source.json` creation;
- `packages/` directory creation;
- registry source mutation;
- generated-index mutation;
- resolver mutation;
- CVF Web runtime mutation;
- CLI/MCP adapter implementation;
- provider call, live proof, public-sync, push, package activation, or package
  instruction execution.

## Dependency Release Evidence

| Dependency | Status | Evidence |
|---|---|---|
| ASSF-PIC roadmap exists and defines PIC-T2 manual UAT/certification review | SATISFIED | `docs/roadmaps/CVF_ASSF_PACKAGE_INSTANCE_CERTIFICATION_PILOT_ROADMAP_2026-06-25.md` lines 205-223 |
| PIC-T0 selected exactly one candidate | SATISFIED | `docs/audits/CVF_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_AUDIT_2026-06-25.md` lines 13-15 |
| PIC-T1 mapped the selected candidate evidence skeleton | SATISFIED | `docs/audits/CVF_ASSF_PIC_T1_PACKAGE_INSTANCE_EVIDENCE_SKELETON_HARDENING_AUDIT_2026-06-26.md` lines 130-137 |
| Dispatch scaffold optimization prerequisite handled | SATISFIED | `docs/reviews/CVF_WODS_T1_WORK_ORDER_DISPATCH_SCAFFOLD_OPTIMIZATION_COMPLETION_2026-06-26.md` status plus active session next allowed move |
| Candidate current lifecycle state is not started | SATISFIED | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` lines 67-68 |
| Current dispatch worktree isolation | SATISFIED | `git status --short` returned no paths before authoring |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| ASSF-PIC-T2 is manual UAT and certification review | `docs/roadmaps/CVF_ASSF_PACKAGE_INSTANCE_CERTIFICATION_PILOT_ROADMAP_2026-06-25.md` | lines 205-223 | `ASSF-PIC-T2` | ASSF-PIC roadmap | LITERAL_INVARIANT | ACCEPT |
| PIC-T2 must not treat generated metadata or Web display as certification evidence | `docs/roadmaps/CVF_ASSF_PACKAGE_INSTANCE_CERTIFICATION_PILOT_ROADMAP_2026-06-25.md` | lines 207-208 | `generated metadata` | ASSF-PIC roadmap | LITERAL_INVARIANT | ACCEPT |
| PIC-T0 selected `cvf-dispatch-quality-reviewer` | `docs/audits/CVF_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_AUDIT_2026-06-25.md` | lines 13-15 | `Selected candidate` | ASSF-PIC-T0 audit | VALUE_SET | ACCEPT |
| PIC-T1 mapped the selected candidate evidence skeleton | `docs/audits/CVF_ASSF_PIC_T1_PACKAGE_INSTANCE_EVIDENCE_SKELETON_HARDENING_AUDIT_2026-06-26.md` | lines 130-137 | `EVIDENCE_SKELETON_MAPPED` | ASSF-PIC-T1 audit | VALUE_SET | ACCEPT |
| Candidate registry entry exists | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | lines 1-8 | `skillId` | ASSF-T2 registry source entry | EXISTS | ACCEPT |
| Candidate acceptance evidence names dispatch-quality gates | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | line 58 | `acceptanceEvidence` | ASSF-T2 registry source entry | VALUE_SET | ACCEPT |
| Candidate UAT and certification states are not started | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | lines 67-68 | `uatState` | ASSF-T2 registry source entry | VALUE_SET | ACCEPT |
| Candidate external adapter disposition is deferred | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | lines 79-82 | `externalCliMcpDisposition` | ASSF-T2 registry source entry | VALUE_SET | ACCEPT |
| Package contract defines lifecycle and external disposition fields | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | lines 72-75 | `certificationState` | ASSF-T1 package schema | EXISTS | ACCEPT |
| T7 lifecycle guard blocks `CERTIFIED` without `uatState: PASSED` | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | lines 89-91 | `MISSING_UAT` | ASSF-T7 certification lifecycle guard | LITERAL_INVARIANT | ACCEPT |
| T7 lifecycle guard defines hold/reject/certified state vocabulary | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | lines 79-87 | `certificationState` | ASSF-T7 certification lifecycle guard | VALUE_SET | ACCEPT |
| T7 adapter claim honesty rules require real adapter evidence before implementation claim | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | lines 132-149 | `adapterEvidence` | ASSF-T7 certification lifecycle guard | LITERAL_INVARIANT | ACCEPT |
| Worker-return scaffold can create one new scaffold file | `governance/compat/run_worker_return_scaffold.py` | lines 209-232 | `write_scaffold` | worker-return scaffold helper | RUNTIME_BEHAVIOR | ACCEPT |
| Worker-return fast gate is the diagnostic gate for returned packets | `governance/compat/run_worker_return_fast_gate.py` | lines 78-80 | `main` | worker-return fast gate | EXISTS | ACCEPT |
| Dispatch packet author fast gate is a current acceptance-evidence command | `governance/compat/run_dispatch_packet_author_fast_gate.py` | lines 119-134 | `main` | dispatch packet author fast gate | EXISTS | ACCEPT |

## Current Runtime Freshness Verification

| Runtime surface | Freshness action | Evidence | Disposition |
|---|---|---|---|
| Selected registry entry | read current source entry | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | current lifecycle states remain `NOT_STARTED` |
| Generated index drift | ran current drift check before dispatch authoring | `python governance/compat/check_assf_skill_index_drift.py` | PASS |
| Candidate source artifacts | verified current paths exist | `Test-Path` for T2 baseline, dispatch-quality checker, and fast gate returned `True` | source artifacts present |
| External CLI/MCP adapter | read current candidate and T7 adapter fields | registry entry lines 79-82; T7 lines 132-149 | adapter remains deferred; no implementation claim |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects:

- ADIF-0001: Exhaustive directory claim omits actual children
- ADIF-0002: Provider-local interaction accepted as authority
- ADIF-0007: Gate keyword in exclusion prose triggers wrong evidence class
- ADIF-0006: Source Verification symbol cell contains a value/type

Remediation applied:

- ADIF-0001: This baseline names bounded paths and does not claim exhaustive
  directory coverage.
- ADIF-0002: ACCEPT rows cite CVF-governed repository files only.
- ADIF-0007: Keyword-heavy exclusions are boundaries, not evidence rows.
- ADIF-0006: Verified path or symbol cells contain only fields, functions,
  sections, paths, or tokens.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator request routed to governed work-order/source-verification/autorun lane |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this ASSF-PIC-T2 baseline and paired work order |
| Disposition | local manual UAT/certification evidence review only; no external material absorbed |
| Claim boundary | source facts must cite CVF-governed files and command evidence |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

recomputeReason: worker must re-read current CVF-governed sources and rerun
the listed local UAT evidence commands before making a recommendation.

unicodePathHandling: literal path or UTF-8 reader required.

extractedTextAuthority: N/A with reason

priorVerificationUse: PIC-T0 and PIC-T1 artifacts are dependency-release
evidence only; T2 UAT evidence must be rerun by the worker.

encodingBoundary: agent-authored artifacts default to ASCII; existing
repository paths are cited literally.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | ASSF-PIC-T2 UAT/certification review and worker return for `cvf-dispatch-quality-reviewer` | internal agents may run read-only local gate evidence and recommend a lifecycle disposition for Codex review; no registry mutation, package instance, generated-index update, resolver behavior, Web projection, commit authority, activation, package execution, or final certification is granted to the worker | this baseline, paired work order, PIC-T0 audit/completion, PIC-T1 audit/completion, ASSF package contract, T7 lifecycle guard | no internal loader, resolver, generator, Web bridge, or package root is implemented | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future external package readout or adapter certification claim | external agents cannot mutate, certify, activate, execute, or consume packages through this tranche | Dual Agent Surface Accounting Standard and T7 adapter honesty contract | adapter implementation is deferred to a separate source-verified work order | `DEFERRED_WITH_REASON` |

## Planned Artifact Manifest

| Path | Owner | Purpose |
|---|---|---|
| `docs/reviews/CVF_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_2026-06-26.md` | worker | manual UAT/certification evidence review |
| `docs/reviews/CVF_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_WORKER_RETURN_2026-06-26.md` | worker | scaffold-first no-commit worker return |
| `docs/reviews/CVF_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_COMPLETION_2026-06-26.md` | Codex reviewer/closer | reviewer-owned completion review after accepted worker return |

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | Worker return is created through `governance/compat/run_worker_return_scaffold.py --write` before long prose. |
| AC2 | Worker reruns `check_work_order_dispatch_quality.py` against `dispatchBaseHead=61ad760c..HEAD` and records result. |
| AC3 | Worker reruns `run_dispatch_packet_author_fast_gate.py` against `dispatchBaseHead=61ad760c..HEAD` and records result. |
| AC4 | Worker runs `check_assf_skill_index_drift.py` and records result. |
| AC5 | UAT/certification review records one recommended lifecycle disposition without mutating registry lifecycle fields. |
| AC6 | Worker return and review record exact changed paths and command-backed evidence. |
| AC7 | No package instance, generated-index mutation, resolver mutation, Web runtime change, CLI/MCP adapter, provider/live proof, public-sync, push, package activation, session-sync, or worker commit occurs. |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| Worker return | `docs/reviews/CVF_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_WORKER_RETURN_2026-06-26.md` |
| UAT/certification review | `docs/reviews/CVF_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_2026-06-26.md` |
| Completion review | `docs/reviews/CVF_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_COMPLETION_2026-06-26.md` |
| Closure decision | reviewer determines after worker return |
| Roadmap disposition | update only after accepted material review |
| Session-sync disposition | required after material closure commit if next allowed move changes |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance dispatch; no public-sync authorization.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ASSF-PIC-T2 manual UAT/certification review dispatch baseline |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE -- dispatch authorization only |
| receiptEvidence | N/A with reason: no runtime/provider/adapter receipt or worker return exists at dispatch |
| actionEvidence | ACTION_EVIDENCE_PRESENT -- Source Verification Block, dependency release evidence, ADIF disclosure, and planned artifact manifest |
| invocationBoundary | governed local documentation and read-only local gate evidence only |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, CLI, MCP, Web runtime, or adapter interception claim |
| claimLanguage | authorizes bounded no-commit UAT/certification evidence review by worker |
| forbiddenExpansion | no package instance, lifecycle mutation, generated-index mutation, resolver mutation, Web runtime change, CLI/MCP adapter, provider/live proof, public-sync, push, activation, package instruction execution, session-sync, or worker commit |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch author role |
| Provider or surface | Codex local workspace |
| Session or invocation | ASSF-PIC-T2 dispatch authoring, 2026-06-26 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | startup reads, source reads, rg, ADIF resolver import, apply_patch |
| Target paths | this baseline; paired work order |
| Allowed scope source | operator request to issue ASSF-PIC-T2 work order |
| Before status evidence | dispatchBaseHead `61ad760c`; clean worktree evidence: `git status --short` returned no paths before authoring |
| After status evidence | dispatch artifacts pending gate and commit |
| Diff evidence | `git diff --name-status` before material dispatch commit |
| Approval boundary | dispatch packet only; worker execution follows after material dispatch |
| Claim boundary | repo-local dispatch evidence only; no runtime/provider/live/public claim |
| Agent type | dispatcher |
| Invocation ID | `assf-pic-t2-manual-uat-certification-review-dispatch-2026-06-26` |
| Expected manifest | `docs/baselines/CVF_GC018_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_2026-06-26.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_FOR_CLAUDE_2026-06-26.md` |
| Actual changed set | `docs/baselines/CVF_GC018_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_2026-06-26.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_FOR_CLAUDE_2026-06-26.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

This baseline authorizes dispatch of ASSF-PIC-T2 manual UAT and certification
evidence review only. It does not create or certify a package, mutate
`uatState` or `certificationState`, mutate the generated index or resolver,
change CVF Web runtime, implement an adapter, run live proof, public-sync,
push, update session continuity, or allow worker commits.
