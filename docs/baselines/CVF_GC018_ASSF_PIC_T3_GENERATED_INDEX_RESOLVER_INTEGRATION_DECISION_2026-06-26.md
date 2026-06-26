# CVF GC-018 Baseline: ASSF-PIC-T3 Generated Index And Resolver Integration Decision

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-06-26

docType: baseline

Batch ID: ASSF-PIC-T3

dispatchBaseHead: 1d17f8bf

## Dispatch Prompt Envelope

Role: Worker. Reviewer/closer is Codex after worker return.

Canonical packet:
`docs/baselines/CVF_GC018_ASSF_PIC_T3_GENERATED_INDEX_RESOLVER_INTEGRATION_DECISION_2026-06-26.md`

Paired work order:
`docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_PIC_T3_GENERATED_INDEX_RESOLVER_INTEGRATION_DECISION_FOR_CLAUDE_2026-06-26.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Current-time notes: ASSF-PIC-T2 closed bounded with lifecycle disposition
`CERTIFICATION_HELD_WITH_REASON`. The operator accepted value-parking the
residual WODS lane with a concrete reopen condition, then explicitly selected
ASSF-PIC-T3 work-order dispatch. This baseline releases a decision-only T3
review under the certification hold.

Do-not-misread notes: this baseline does not authorize generated-index source
mutation, generated aggregate mutation, resolver mutation, registry mutation,
package instance creation, certification decision, lifecycle state mutation,
Web runtime change, CLI/MCP adapter behavior, provider/live proof, public-sync,
push, activation, readiness, or package instruction execution.

## Proposed Tranche

Tranche: ASSF-PIC-T3

Baseline decision: authorize a bounded no-commit worker decision review for the
selected candidate `cvf-dispatch-quality-reviewer`. The worker must verify the
current generated-index drift state, the current resolver readout boundary, and
the T2 certification-hold dependency. The expected decision is
`INTEGRATION_DEFERRED_CERTIFICATION_HELD` unless the worker finds a source-backed
blocker that requires `BLOCKED_WITH_REASON`.

Verdicts:

- Dispatcher verdict: DISPATCH_APPROVED_DECISION_ONLY
- Worker verdict: PENDING_WORKER_RETURN
- Reviewer verdict: PENDING_REVIEW

## Purpose

Release ASSF-PIC-T3 as a generated-index and resolver integration decision
only. Success means the worker creates one source-backed decision review and
one scaffold-first worker return that confirm whether integration is deferred
under the current certification hold. The worker must not edit registry source,
the generated index, the resolver, tests, Web files, package roots, or session
surfaces.

## Evidence / Verification

Dispatch evidence is limited to current CVF-governed source surfaces:

- ASSF-PIC roadmap;
- PIC-T2 completion review and certification-hold disposition;
- selected candidate registry entry;
- generated index README and generated aggregate claim boundary;
- ASSF resolver source and resolver readout command;
- ASSF certification lifecycle guard;
- current generated-index drift check.

Worker-created decision and worker-return files do not exist at dispatch time
and must not be claimed as complete until the worker returns uncommitted
artifacts and Codex accepts them.

## Scope / Applies To

Applies to:

- decision review for generated-index disposition;
- decision review for resolver behavior disposition;
- read-only generated-index drift check;
- read-only resolver query for the selected candidate selectors;
- scaffold-first worker-return authoring;
- reviewer closure after no-commit worker return.

Does not apply to:

- registry source mutation;
- generated-index source or aggregate mutation;
- resolver source mutation or resolver test creation;
- package instance creation;
- `SKILL.md` or `skill.source.json` creation;
- CVF Web runtime mutation;
- CLI/MCP adapter implementation;
- provider call, live proof, public-sync, push, package activation, package
  readiness, or package instruction execution.

## Dependency Release Evidence

| Dependency | Status | Evidence |
|---|---|---|
| ASSF-PIC roadmap exists and defines T3 as generated-index and resolver integration decision | SATISFIED | `docs/roadmaps/CVF_ASSF_PACKAGE_INSTANCE_CERTIFICATION_PILOT_ROADMAP_2026-06-25.md` section `ASSF-PIC-T3 - Generated Index And Resolver Integration Decision` |
| PIC-T2 lifecycle disposition is certification hold | SATISFIED | `docs/reviews/CVF_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_COMPLETION_2026-06-26.md` records `Lifecycle disposition: CERTIFICATION_HELD_WITH_REASON` |
| Operator selected T3 despite the hold | SATISFIED | 2026-06-26 operator instruction: residual WODS defects are parked with reopen condition; issue ASSF-PIC-T3 work order |
| Selected candidate remains current | SATISFIED | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` has `skillId`, `status`, `uatState`, and `certificationState` fields |
| Generated index source layout exists | SATISFIED | `docs/reference/agent_system_skills/generated/README.md` names source entries, generated aggregate, generator, and drift check |
| Resolver exists and is read-only | SATISFIED | `governance/compat/run_assf_skill_resolver.py` module docstring and `resolve_skill_packet` |
| Current dispatch worktree isolation | SATISFIED | `git status --short` returned no paths before authoring |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| ASSF-PIC-T3 is generated-index and resolver integration decision | `docs/roadmaps/CVF_ASSF_PACKAGE_INSTANCE_CERTIFICATION_PILOT_ROADMAP_2026-06-25.md` | `ASSF-PIC-T3 - Generated Index And Resolver Integration Decision` | `ASSF-PIC-T3` | ASSF-PIC roadmap | LITERAL_INVARIANT | ACCEPT |
| PIC-T3 requires drift check evidence and no package activation claim | `docs/roadmaps/CVF_ASSF_PACKAGE_INSTANCE_CERTIFICATION_PILOT_ROADMAP_2026-06-25.md` | T3 Required outputs | `drift check evidence` | ASSF-PIC roadmap | LITERAL_INVARIANT | ACCEPT |
| PIC-T2 closed with certification held | `docs/reviews/CVF_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_COMPLETION_2026-06-26.md` | top lifecycle disposition and Findings / Position | `CERTIFICATION_HELD_WITH_REASON` | ASSF-PIC-T2 completion review | VALUE_SET | ACCEPT |
| Candidate registry entry exists | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | root object | `skillId` | ASSF-T2 registry source entry | EXISTS | ACCEPT |
| Candidate currently remains candidate-stage metadata | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | root object | `status` | ASSF-T2 registry source entry | VALUE_SET | ACCEPT |
| Candidate UAT and certification states are not started | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | root object | `uatState` | ASSF-T2 registry source entry | VALUE_SET | ACCEPT |
| Generated index is a read-only aggregate and must not be hand-edited | `docs/reference/agent_system_skills/generated/README.md` | Purpose | `skill-index.json` | ASSF-T2 generated README | LITERAL_INVARIANT | ACCEPT |
| Generated index drift check exists | `docs/reference/agent_system_skills/generated/README.md` | Purpose | `check_assf_skill_index_drift.py` | ASSF-T2 generated README | EXISTS | ACCEPT |
| Resolver excludes retired and rejected packages by default | `governance/compat/run_assf_skill_resolver.py` | `_EXCLUDED_STATUSES` | `_EXCLUDED_STATUSES` | ASSF-T2 resolver | VALUE_SET | ACCEPT |
| Resolver returns metadata-only bounded packets | `governance/compat/run_assf_skill_resolver.py` | `SkillPacket.to_dict` | `claimBoundary` | ASSF-T2 resolver | LITERAL_INVARIANT | ACCEPT |
| Resolver exposes read-only skill packet resolution | `governance/compat/run_assf_skill_resolver.py` | `resolve_skill_packet` | `resolve_skill_packet` | ASSF-T2 resolver | EXISTS | ACCEPT |
| T7 blocks certification without passed UAT | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | Certification And UAT State Model | `MISSING_UAT` | ASSF-T7 certification lifecycle guard | LITERAL_INVARIANT | ACCEPT |
| T7 defines generated-index and resolver drift classes | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | Drift Detection Classes | `GENERATED_INDEX_DRIFT` | ASSF-T7 certification lifecycle guard | VALUE_SET | ACCEPT |
| T7 keeps machine-check candidates future-only until authorized | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | Machine-Check Candidate Matrix | `check_assf_generated_index_drift.py extension` | ASSF-T7 certification lifecycle guard | LITERAL_INVARIANT | ACCEPT |

## Current Runtime Freshness Verification

| Runtime surface | Freshness action | Evidence | Disposition |
|---|---|---|---|
| Selected registry entry | read current source entry | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | current lifecycle fields remain not started |
| Generated index drift | ran current drift check before dispatch authoring | `python governance/compat/check_assf_skill_index_drift.py` | PASS |
| Resolver readout | ran current resolver query for candidate selectors before dispatch authoring | `python governance/compat/run_assf_skill_resolver.py --task-class dispatch-authoring --role dispatcher --phase DISPATCH_AUTHORING --surface governance/compat --risk-ceiling R0` | returns one metadata item for `cvf-dispatch-quality-reviewer` and a claim boundary denying activation or adapter authority |
| Candidate source paths | verified current paths exist | `Test-Path` for generated index, resolver, and selected registry entry returned `True` | source artifacts present |
| Model gateway provider registry | checked current provider registry surface only because provider-boundary terms appear in forbidden-scope prose | `Test-Path EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` returned `True`; `rg -n "PROVIDER_CAPABILITY_REGISTRY" EXTENSIONS/CVF_MODEL_GATEWAY/src -g "*.ts"` found `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` line 70 | N/A with reason: this baseline makes no provider registry absence claim and authorizes no provider/runtime change |
| External CLI/MCP adapter | read current candidate and T7 adapter fields | registry entry external fields; T7 Adapter Claim Honesty Rules | adapter remains deferred; no implementation claim |

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
| Owner surface | this ASSF-PIC-T3 baseline and paired work order |
| Disposition | local integration-decision review only; no external material absorbed |
| Claim boundary | source facts must cite CVF-governed files and command evidence |

## Value-Parked Lane Reopen Discipline

| Parked lane | Reopen condition | Current disposition |
|---|---|---|
| residual WODS defects after WODS-T2 | reopen only if the next delegated worker-return still needs more than 2 fast-gate repair rounds for scaffold/template/keyword-guard format defects, or if the same recursive keyword false-trigger appears again despite gotcha 22 | parked; not part of ASSF-PIC-T3 execution |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | ASSF-PIC-T3 decision review and worker return for `cvf-dispatch-quality-reviewer` | internal agents may read generated-index drift and resolver readout evidence for reviewer decision only; no registry mutation, generated-index update, resolver behavior change, Web projection, commit authority, activation, package execution, or certification is granted to the worker | this baseline, paired work order, PIC-T2 completion, selected registry entry, generated README, resolver source, T7 lifecycle guard | no internal loader, resolver mutation, generator mutation, Web bridge, or package root is implemented | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future external package readout or adapter certification claim | external agents cannot mutate, certify, activate, execute, or consume packages through this tranche | Dual Agent Surface Accounting Standard and T7 adapter honesty contract | adapter implementation is deferred to a separate source-verified work order | `DEFERRED_WITH_REASON` |

## Planned Artifact Manifest

| Path | Owner | Purpose |
|---|---|---|
| `docs/reviews/CVF_ASSF_PIC_T3_GENERATED_INDEX_RESOLVER_INTEGRATION_DECISION_2026-06-26.md` | worker | generated-index and resolver integration decision review |
| `docs/reviews/CVF_ASSF_PIC_T3_GENERATED_INDEX_RESOLVER_INTEGRATION_DECISION_WORKER_RETURN_2026-06-26.md` | worker | scaffold-first no-commit worker return |
| `docs/reviews/CVF_ASSF_PIC_T3_GENERATED_INDEX_RESOLVER_INTEGRATION_DECISION_COMPLETION_2026-06-26.md` | Codex reviewer/closer | reviewer-owned completion review after accepted worker return |

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | Worker return is created through `governance/compat/run_worker_return_scaffold.py --write` before long prose. |
| AC2 | Decision review records `python governance/compat/check_assf_skill_index_drift.py`. |
| AC3 | Decision review records the resolver query for selected candidate selectors. |
| AC4 | Decision review records one integration disposition without registry, generated-index, or resolver mutation. |
| AC5 | Worker return and decision review record exact changed paths and command-backed evidence. |
| AC6 | No package instance, lifecycle mutation, generated-index mutation, resolver mutation, Web runtime change, CLI/MCP adapter, provider/live proof, public-sync, push, activation, session-sync, or worker commit occurs. |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| Worker return | `docs/reviews/CVF_ASSF_PIC_T3_GENERATED_INDEX_RESOLVER_INTEGRATION_DECISION_WORKER_RETURN_2026-06-26.md` |
| Integration decision review | `docs/reviews/CVF_ASSF_PIC_T3_GENERATED_INDEX_RESOLVER_INTEGRATION_DECISION_2026-06-26.md` |
| Completion review | `docs/reviews/CVF_ASSF_PIC_T3_GENERATED_INDEX_RESOLVER_INTEGRATION_DECISION_COMPLETION_2026-06-26.md` |
| Closure decision | reviewer determines after worker return |
| Roadmap disposition | update only after accepted material review |
| Session-sync disposition | required after material closure commit if next allowed move changes |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance dispatch; no public-sync authorization.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ASSF-PIC-T3 generated-index and resolver integration decision dispatch baseline |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE -- dispatch authorization only |
| receiptEvidence | N/A with reason: no runtime/provider/adapter receipt or worker return exists at dispatch |
| actionEvidence | ACTION_EVIDENCE_PRESENT -- Source Verification Block, dependency release evidence, ADIF disclosure, and planned artifact manifest |
| invocationBoundary | governed local documentation and read-only local gate evidence only |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, CLI, MCP, Web runtime, or adapter interception claim |
| claimLanguage | authorizes bounded no-commit generated-index and resolver integration decision review by worker |
| forbiddenExpansion | no package instance, lifecycle mutation, registry-source mutation, generated-index mutation, resolver mutation, Web runtime change, CLI/MCP adapter, provider/live proof, public-sync, push, activation, package instruction execution, session-sync, or worker commit |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch author role |
| Provider or surface | Codex local workspace |
| Session or invocation | ASSF-PIC-T3 dispatch authoring, 2026-06-26 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | startup reads, source reads, rg, ADIF resolver import, generated-index drift check, resolver query, apply_patch |
| Target paths | this baseline; paired work order; ASSF-PIC roadmap |
| Allowed scope source | operator request to value-park residual WODS defects and issue ASSF-PIC-T3 work order |
| Before status evidence | dispatchBaseHead `1d17f8bf`; clean worktree evidence: `git status --short` returned no paths before authoring |
| After status evidence | dispatch artifacts pending gate and commit |
| Diff evidence | `git diff --name-status` before material dispatch commit |
| Approval boundary | dispatch packet only; worker execution follows after material dispatch |
| Claim boundary | repo-local dispatch evidence only; no runtime/provider/live/public claim |
| Agent type | dispatcher |
| Invocation ID | `assf-pic-t3-generated-index-resolver-integration-decision-dispatch-2026-06-26` |
| Expected manifest | `docs/baselines/CVF_GC018_ASSF_PIC_T3_GENERATED_INDEX_RESOLVER_INTEGRATION_DECISION_2026-06-26.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_PIC_T3_GENERATED_INDEX_RESOLVER_INTEGRATION_DECISION_FOR_CLAUDE_2026-06-26.md`; `docs/roadmaps/CVF_ASSF_PACKAGE_INSTANCE_CERTIFICATION_PILOT_ROADMAP_2026-06-25.md` |
| Actual changed set | `docs/baselines/CVF_GC018_ASSF_PIC_T3_GENERATED_INDEX_RESOLVER_INTEGRATION_DECISION_2026-06-26.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_PIC_T3_GENERATED_INDEX_RESOLVER_INTEGRATION_DECISION_FOR_CLAUDE_2026-06-26.md`; `docs/roadmaps/CVF_ASSF_PACKAGE_INSTANCE_CERTIFICATION_PILOT_ROADMAP_2026-06-25.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

This baseline authorizes dispatch of an ASSF-PIC-T3 generated-index and resolver
integration decision review only. It does not create or certify a package,
mutate `uatState` or `certificationState`, mutate registry sources, mutate the
generated index or resolver, change CVF Web runtime, implement an adapter, run
live proof, public-sync, push, update session continuity, or allow worker
commits.
