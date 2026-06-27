# CVF GC-018 Baseline: ASSF Package Certification Decision T0-T3

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-26

docType: baseline

Batch ID: ASSF-CERT-DECISION

dispatchBaseHead: aad3b819

## Decision / Baseline / Proposed Tranche

| Field | Disposition |
|---|---|
| Decision | execute T0-T3 certification-decision lane for `cvf-dispatch-quality-reviewer` |
| Baseline | real UAT evidence closed at material commit `ec911be2` |
| Proposed tranche | `ASSF-CERT-DECISION` |
| Worker route | Codex single-agent multi-role execution |
| Closure posture | `CLOSED_PASS_BOUNDED` |

## Purpose

Provide GC-018 authority for a bounded certification-decision tranche after real
UAT evidence exists.

## Scope / Methodology

The tranche reviews the source package entry, lifecycle guard, real UAT
evidence, generated-index drift, and resolver readout. It records a decision
that certification evidence is approved for a future source-state update. It
does not mutate the package registry entry or generated index.

## Findings / Position

The target candidate has source-backed acceptance evidence and one passing real
UAT evidence record. The package source still records `uatState: NOT_STARTED`
and `certificationState: NOT_STARTED`, so source-state transition must remain a
separate next-control lane.

## Evidence / Verification

| Evidence | Result |
|---|---|
| package source entry | source verified |
| real UAT evidence | PASS |
| ASSF generated index drift | PASS |
| ASSF resolver readout | one metadata-only candidate |
| certification evidence decision | approved, source-state update deferred |

## Risk / Corrective Action

| Risk | Disposition |
|---|---|
| Evidence approval may be read as source-state certification | Prevented: all decision artifacts use source-state update deferred wording |
| Single UAT packet may be treated as broad runtime proof | Prevented: evidence is bounded to one committed governed packet |
| Checker or adapter work could reopen prematurely | Prevented: T3 routes those to later source-verified work |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| package acceptance evidence requires dispatch-quality PASS and fast gate 5/5 PASS | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | root object | `acceptanceEvidence` | ASSF registry entry | VALUE_SET | ACCEPT |
| package UAT state is source-visible | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | root object | `uatState` | ASSF registry entry | VALUE_SET | ACCEPT |
| package certification state is source-visible | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | root object | `certificationState` | ASSF registry entry | VALUE_SET | ACCEPT |
| lifecycle guard requires UAT before certification | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | Certification And UAT State Model | `certificationState` | ASSF lifecycle guard | LITERAL_INVARIANT | ACCEPT |
| real UAT evidence records dispatch-quality PASS | `docs/reviews/CVF_ASSF_REAL_MANUAL_UAT_EXECUTION_EVIDENCE_2026-06-26.md` | UAT Execution Evidence | `UAT-02` | ASSF real UAT evidence review | LITERAL_INVARIANT | ACCEPT |
| real UAT completion records certification-decision roadmap recommendation | `docs/reviews/CVF_ASSF_REAL_MANUAL_UAT_EXECUTION_EVIDENCE_COMPLETION_2026-06-26.md` | Next roadmap recommendation | `OPEN_ASSF_PACKAGE_CERTIFICATION_DECISION_ROADMAP` | ASSF real UAT completion review | VALUE_SET | ACCEPT |
| generated index drift checker exists | `governance/compat/check_assf_skill_index_drift.py` | module | `main` | ASSF drift checker | EXISTS | ACCEPT |
| ASSF resolver exists | `governance/compat/run_assf_skill_resolver.py` | module | `resolve_skill_packet` | ASSF resolver | EXISTS | ACCEPT |

## Current Runtime Freshness Verification

| Runtime surface | Freshness action | Evidence | Disposition |
|---|---|---|---|
| ASSF generated index drift | ran current drift check before authoring | `python governance/compat/check_assf_skill_index_drift.py` | PASS |
| ASSF resolver readout | ran current resolver query before authoring | `python governance/compat/run_assf_skill_resolver.py --task-class dispatch-authoring --role dispatcher --phase DISPATCH_AUTHORING --surface governance/compat --risk-ceiling R0` | PASS |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects:

- ADIF-0001: Exhaustive directory claim omits actual children
- ADIF-0002: Provider-local interaction accepted as authority
- ADIF-0007: Gate marker in boundary prose triggers wrong evidence class
- ADIF-0006: Source Verification symbol cell contains a value/type

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | authorized certification-decision roadmap |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this GC-018 baseline |
| Disposition | no external material absorbed |
| Claim boundary | repository-local source and command evidence only |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | ASSF-CERT-DECISION artifacts | internal agents may use this decision to prepare a future lifecycle-state update work order only | T0-T3 reviews and completion review | no loader, activation, package execution, or generated-index mutation | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future adapter readout | external agents cannot consume, certify, activate, mutate, or execute this package through this baseline | package entry external disposition remains deferred | external adapter remains deferred | `DEFERRED_WITH_REASON` |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance certification-decision evidence; no public-sync
authorization.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ASSF package certification-decision GC-018 |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE -- certification evidence decision only |
| receiptEvidence | CVF_RECEIPT_PRESENT - UAT evidence PASS, drift PASS, resolver PASS |
| actionEvidence | ACTION_EVIDENCE_PRESENT -- T0-T3 reviews and completion review |
| invocationBoundary | governed local documentation and read-only command evidence |
| interceptionBoundary | no provider, CLI, MCP, Web runtime, adapter, package instruction execution, package instance, lifecycle source mutation, or generated-index mutation |
| claimLanguage | approves certification evidence and defers source-state update |
| forbiddenExpansion | no package instance creation, lifecycle source mutation, registry-source mutation, generated-index mutation, resolver mutation, Web runtime change, CLI/MCP adapter, provider/live proof, public-sync, push, activation, readiness claim, package instruction execution, package integration, worker commit, or session-sync in material commit |

## Acceptance Receipt Assertion Matrix

| Query ID | Receipt artifact | JSON path | Required value | Observed value | Status |
|---|---|---|---|---|---|
| ARAM-01 | UAT evidence review | dispatch-quality violations | 0 | 0 | PASS |
| ARAM-02 | UAT evidence review | fast gate checks passed | 5/5 | 5/5 | PASS |
| ARAM-03 | drift command output | ASSF generated index drift | PASS | PASS | PASS |
| ARAM-04 | resolver output | totalCandidates | 1 | 1 | PASS |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_PACKAGE_CERTIFICATION_DECISION_T0_T3_FOR_CODEX_2026-06-26.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ASSF_PACKAGE_CERTIFICATION_DECISION_T0_T3_COMPLETION_2026-06-26.md` | final reviewer verdict and decision disposition | PASS |
| Roadmap state | `docs/roadmaps/CVF_ASSF_PACKAGE_CERTIFICATION_DECISION_ROADMAP_2026-06-26.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | N/A with reason: no registry JSON mutation is authorized in this tranche | no corpus registry JSON in changed set | BLOCKED with reason: out of scope |
| Registry Markdown | N/A with reason: no registry Markdown mutation is authorized in this tranche | no corpus registry Markdown mutation | BLOCKED with reason: out of scope |
| External evidence digest | N/A with reason: no external artifact is created | no external digest applies | N/A with reason |
| System loop interlock | this baseline and completion review | no runtime loop, provider call, activation, package execution, adapter, or public-sync occurred | PASS |
| Session continuity | N/A with reason: session-sync is separate after material closure | active session paths excluded from material changed set | N/A with reason |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatcher/worker/reviewer/closer |
| Agent type | single-agent multi-role |
| Provider or surface | local workspace |
| Session or invocation | ASSF package certification decision T0-T3 baseline, 2026-06-26 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | startup reads, source reads, ASSF drift check, ASSF resolver, apply_patch, governance gates, git |
| Target paths | roadmap, GC-018 baseline, work order, T0 review, T1 review, T2 review, T3 review, completion review |
| Allowed scope source | active session next allowed move plus user approval to process T0-T3 |
| Before status evidence | baseHead `aad3b819`; worktree clean before authoring |
| After status evidence | material artifacts pending commit |
| Diff evidence | `git diff --name-status`; `git diff --check`; autorun gates |
| Approval boundary | certification evidence decision only |
| Claim boundary | no lifecycle source mutation, generated-index mutation, resolver mutation, runtime, provider/live, public-sync, package activation, package instance, or adapter behavior |
| Invocation ID | `assf-package-certification-decision-baseline-2026-06-26` |
| Expected manifest | roadmap, baseline, work order, T0 review, T1 review, T2 review, T3 review, completion review |
| Actual changed set | roadmap, baseline, work order, T0 review, T1 review, T2 review, T3 review, completion review |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

This baseline authorizes a bounded certification evidence decision only. It
does not authorize lifecycle source mutation, generated-index mutation, resolver
mutation, runtime behavior, package activation, adapter work, provider/live
proof, public-sync, or package instruction execution.
