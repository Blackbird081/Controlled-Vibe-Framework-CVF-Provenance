# CVF Roadmap: ASSF Package Certification Decision

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-26

docType: roadmap

Batch ID: ASSF-CERT-DECISION

baseHead: aad3b819

## Purpose

Close the bounded certification-decision lane for
`cvf-dispatch-quality-reviewer` after real UAT evidence was recorded.

## Authorization / Decision

| Field | Disposition |
|---|---|
| Authorization source | active session next allowed move plus user approval to process T0-T3 |
| Decision scope | certification evidence decision only |
| Lifecycle source mutation | deferred to a future source-verified roadmap |
| Material base | `aad3b819` |

## Scope / Methodology

This roadmap executes T0 through T3 as a single Codex reviewer/closer tranche.
It reviews source-backed package metadata, UAT evidence, lifecycle contract
rules, generated-index drift, and resolver readout. It records a certification
evidence decision without mutating package registry source, generated index,
resolver source, runtime, Web projection, or external adapter surfaces.

## Findings / Position

The UAT evidence satisfies the package's current `acceptanceEvidence` for one
committed governed dispatch packet. The certification evidence is approved for
the next lifecycle-state update lane, but this roadmap does not itself set
`uatState: PASSED` or `certificationState: CERTIFIED` in source.

## Risk / Corrective Action

| Risk | Disposition |
|---|---|
| Certification decision could be mistaken for lifecycle source mutation | Prevented: source-state update is deferred to T3 next-control |
| UAT evidence could be over-generalized from one packet | Prevented: decision is bounded to one committed governed dispatch packet |
| External adapter support could be inferred | Prevented: external CLI/MCP disposition remains deferred |

## Non-Goals

| Non-goal | Reason |
|---|---|
| package registry source mutation | deferred to lifecycle source-state update lane |
| generated-index mutation | deferred until registry source changes |
| resolver mutation | not needed for evidence decision |
| Web projection or adapter implementation | downstream of source-state update |
| provider/live proof or public-sync | outside this private provenance decision |

## Design Control Gate

| Control | Required outcome | Status |
|---|---|---|
| lifecycle boundary | evidence decision is separate from source-state mutation | PASS |
| generated aggregate discipline | no generated index touched in this tranche | PASS |
| dual-agent boundary | external CLI/MCP remains deferred | PASS |
| public/provenance boundary | no public-sync authorization used | PASS |

## Tranche Plan

| Tranche | Objective | Artifact | Status |
|---|---|---|---|
| T0 | Certification decision protocol | `docs/reviews/CVF_ASSF_CERT_T0_CERTIFICATION_DECISION_PROTOCOL_2026-06-26.md` | CLOSED_PASS_BOUNDED |
| T1 | Evidence review | `docs/reviews/CVF_ASSF_CERT_T1_EVIDENCE_REVIEW_2026-06-26.md` | CLOSED_PASS_BOUNDED |
| T2 | Certification evidence decision | `docs/reviews/CVF_ASSF_CERT_T2_CERTIFICATION_DECISION_2026-06-26.md` | CLOSED_PASS_BOUNDED |
| T3 | Post-decision next-control | `docs/reviews/CVF_ASSF_CERT_T3_POST_DECISION_NEXT_CONTROL_2026-06-26.md` | CLOSED_PASS_BOUNDED |

## Work Plan

| Step | Work | Output |
|---|---|---|
| 1 | define decision protocol | T0 review |
| 2 | compare evidence | T1 review |
| 3 | record decision | T2 review |
| 4 | route next control | T3 review |
| 5 | close roadmap | completion review |

## Acceptance Criteria

| ID | Criterion | Status |
|---|---|---|
| AC1 | T0-T3 reviews exist | PASS |
| AC2 | certification evidence disposition is recorded | PASS |
| AC3 | lifecycle source mutation is deferred | PASS |
| AC4 | roadmap has closure package and receipt assertion matrix | PASS |
| AC5 | material changed set excludes runtime/source/session mutation paths | PASS |

## Verification / Evidence

| Evidence | Result |
|---|---|
| real UAT evidence | PASS |
| ASSF generated index drift | PASS |
| ASSF resolver readout | PASS |
| T2 decision | `CERTIFICATION_EVIDENCE_APPROVED_SOURCE_STATE_UPDATE_DEFERRED` |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| package acceptance evidence requires dispatch-quality PASS and fast gate 5/5 PASS | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | root object | `acceptanceEvidence` | ASSF registry entry | VALUE_SET | ACCEPT |
| package lifecycle source state is not already certified | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | root object | `certificationState` | ASSF registry entry | VALUE_SET | ACCEPT |
| lifecycle guard separates UAT from certification | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | Certification And UAT State Model | `certificationState` | ASSF lifecycle guard | LITERAL_INVARIANT | ACCEPT |
| real UAT evidence was recorded | `docs/reviews/CVF_ASSF_REAL_MANUAL_UAT_EXECUTION_EVIDENCE_2026-06-26.md` | UAT Execution Evidence | `UAT-02` | ASSF real UAT evidence review | LITERAL_INVARIANT | ACCEPT |
| real UAT completion recommends certification-decision roadmap | `docs/reviews/CVF_ASSF_REAL_MANUAL_UAT_EXECUTION_EVIDENCE_COMPLETION_2026-06-26.md` | Next roadmap recommendation | `OPEN_ASSF_PACKAGE_CERTIFICATION_DECISION_ROADMAP` | ASSF real UAT completion review | VALUE_SET | ACCEPT |

## Current Runtime Freshness Verification

| Runtime surface | Freshness action | Evidence | Disposition |
|---|---|---|---|
| ASSF generated index drift | ran current drift check before authoring | `python governance/compat/check_assf_skill_index_drift.py` | PASS |
| ASSF resolver readout | ran current resolver query before authoring | `python governance/compat/run_assf_skill_resolver.py --task-class dispatch-authoring --role dispatcher --phase DISPATCH_AUTHORING --surface governance/compat --risk-ceiling R0` | PASS |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | authorized certification-decision roadmap |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this roadmap |
| Disposition | no external material absorbed |
| Claim boundary | repository-local source and command evidence only |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | ASSF certification-decision review artifacts | internal agents may use this decision to prepare a future lifecycle-state update work order | T0-T3 reviews and completion review | no loader, activation, package instruction execution, or generated-index mutation | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future adapter readout | external agents cannot consume, certify, activate, mutate, or execute this package through this roadmap | package entry still records external disposition deferred | external adapter remains deferred to later source-verified work | `DEFERRED_WITH_REASON` |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance certification-decision evidence; no public-sync
authorization.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ASSF package certification-decision roadmap |
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
| ARAM-05 | T2 decision review | certification evidence disposition | APPROVED | APPROVED | PASS |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_PACKAGE_CERTIFICATION_DECISION_T0_T3_FOR_CODEX_2026-06-26.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ASSF_PACKAGE_CERTIFICATION_DECISION_T0_T3_COMPLETION_2026-06-26.md` | `Reviewer verdict: CLOSED_PASS_BOUNDED`; `Certification evidence disposition: CERTIFICATION_EVIDENCE_APPROVED_SOURCE_STATE_UPDATE_DEFERRED` | PASS |
| Roadmap state | this roadmap | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | N/A with reason: no registry JSON mutation is authorized in this roadmap | no corpus registry JSON in changed set | BLOCKED with reason: out of scope |
| Registry Markdown | N/A with reason: no registry Markdown mutation is authorized in this roadmap | no corpus registry Markdown mutation | BLOCKED with reason: out of scope |
| External evidence digest | N/A with reason: no external artifact is created | no external digest applies | N/A with reason |
| System loop interlock | this roadmap and completion review | no runtime loop, provider call, activation, package execution, adapter, or public-sync occurred | PASS |
| Session continuity | N/A with reason: session-sync is separate after material closure | active session paths excluded from material changed set | N/A with reason |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatcher/worker/reviewer/closer |
| Agent type | single-agent multi-role |
| Provider or surface | local workspace |
| Session or invocation | ASSF package certification decision T0-T3, 2026-06-26 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | startup reads, source reads, ASSF drift check, ASSF resolver, apply_patch, governance gates, git |
| Target paths | roadmap, GC-018 baseline, work order, T0 protocol review, T1 evidence review, T2 decision review, T3 next-control review, completion review |
| Allowed scope source | active session next allowed move plus user approval to process T0-T3 |
| Before status evidence | baseHead `aad3b819`; worktree clean before authoring |
| After status evidence | material artifacts pending commit |
| Diff evidence | `git diff --name-status`; `git diff --check`; autorun gates |
| Approval boundary | certification evidence decision only |
| Claim boundary | no lifecycle source mutation, generated-index mutation, resolver mutation, runtime, provider/live, public-sync, package activation, package instance, or adapter behavior |
| Invocation ID | `assf-package-certification-decision-t0-t3-2026-06-26` |
| Expected manifest | roadmap, baseline, work order, T0 review, T1 review, T2 review, T3 review, completion review |
| Actual changed set | roadmap, baseline, work order, T0 review, T1 review, T2 review, T3 review, completion review |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

This roadmap records a bounded certification evidence decision only. It does
not mutate lifecycle state, certify the registry source, activate a package,
project to Web, export an adapter, or execute package instructions.
