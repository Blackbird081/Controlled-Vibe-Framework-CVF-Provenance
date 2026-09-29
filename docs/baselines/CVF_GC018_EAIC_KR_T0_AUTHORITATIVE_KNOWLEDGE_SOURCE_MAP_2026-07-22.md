# CVF GC-018 Baseline - EAIC-KR T0 Authoritative Knowledge Source Map

Memory class: governed-dispatch-baseline

Status: CLOSED_PASS_BOUNDED_WITH_REVIEWER_REPAIRS_AND_BOUNDARY_CORRECTION

Batch ID: CVF-EAIC-KR-T0

Dispatch base head: `969acaa32`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator

Reviewer/closer: Codex reviewer/closer

Worker route: manual copy/paste only

## Purpose

Freeze a documentation-only T0 that inventories existing CVF authority for
external-agent invocation control, classifies unresolved knowledge domains,
and produces a source-acquisition map without invoking or researching through
an external service.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind source-intake --batch-id CVF-EAIC-KR-T0 --title "External Agent Invocation Control Knowledge Readiness T0" --date 2026-07-22 --base 969acaa32 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "operator authorization 2026-07-22; invocation-control audit remains active" --stdout --include-worker-return-skeleton` |
| generatedProfile | source-intake plus no-commit documentation worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Replaced placeholders with the local-only source-map mission, exact output manifest, knowledge domains, stop rules, and reviewer boundary. |
| checkerReadAheadConfirmation | dispatch-quality, prompt-envelope, handoff, ADIF, structural, public-disposition, and worker-return gates |
| docOnlyNewFields | authorityClass; accessModeEvidenceClass; sourceAcquisitionPriority; blockingKnowledgeGap |
| claimBoundary | dispatch baseline only; no knowledge-completeness or runtime-control claim |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| operator lane selection | operator instruction on 2026-07-22 accepted priority 1 and requested its work order | explicit instruction exists in current session | ACCEPT |
| active critical-gap evidence | `docs/audits/CVF_AGENT_CLI_MCP_INVOCATION_CONTROL_SYSTEM_CHAIN_REASSESSMENT_2026-07-20.md`, Findings / Position and Decision / Recommendation | audit remains authority for the knowledge-first moratorium | ACCEPT |
| clean dispatch worktree | HEAD `969acaa32`; `git status --short` empty before authoring | one batch per clean worktree | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: ADIF-0001; ADIF-0002; ADIF-0006; ADIF-0007; ADIF-0014; ADIF-0015; ADIF-0016; ADIF-0017; ADIF-0020; ADIF-0021; ADIF-0024; ADIF-0028; ADIF-0029; ADIF-0031; ADIF-0033; ADIF-0039; ADIF-0043; ADIF-0044; ADIF-0045

## Target / Source

Target is a complete map of repository-local CVF authority and missing primary
knowledge for the nine domains in the parent roadmap. Sources are limited to
the current private provenance repository. Provider-local memory, chat history,
the Web, external repositories, and live services are not authority inputs.

## Decision / Baseline / Proposed Tranche

Release one manual copy/paste no-commit documentation worker to create the T0
knowledge gap and source-acquisition map. Every external or implementation
action remains held.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| global execution moratorium remains the audit decision | VALUE_SET | `docs/audits/CVF_AGENT_CLI_MCP_INVOCATION_CONTROL_SYSTEM_CHAIN_REASSESSMENT_2026-07-20.md` | Decision / Recommendation | GLOBAL_ROADMAP_EXECUTION_MORATORIUM_ACTIVE | invocation-control audit | ACCEPT |
| existing controls do not govern an external-agent lifecycle end to end | RUNTIME_BEHAVIOR | `docs/audits/CVF_AGENT_CLI_MCP_INVOCATION_CONTROL_SYSTEM_CHAIN_REASSESSMENT_2026-07-20.md` | Source ownership map; Quality Findings | External agent CLI | invocation-control audit | ACCEPT |
| missing primary knowledge is carried forward | VALUE_SET | `docs/audits/CVF_AGENT_CLI_MCP_INVOCATION_CONTROL_SYSTEM_CHAIN_REASSESSMENT_2026-07-20.md` | Carried-forward knowledge need | Carried-forward knowledge need | invocation-control audit | ACCEPT |
| provider/model assignment roadmap is a parked component | VALUE_SET | `docs/roadmaps/CVF_OPERATOR_APPROVED_PROVIDER_MODEL_ASSIGNMENT_AND_INVOCATION_RECEIPT_ROADMAP_2026-07-20.md` | top-level Status | Status | provider/model roadmap | ACCEPT |
| worker handoff must remain provider-neutral | LITERAL_INVARIANT | `docs/reference/guard_orientation/README.md` | Role-Neutrality Rule | Role-Neutrality Rule | guard orientation index | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| prior EAIC-KR artifact path | `Test-Path` on the three planned 2026-07-22 paths returned false before authoring | ACCEPT |
| roadmap-name collision | `rg -n -i "external.agent.invocation.control.knowledge.readiness|EAIC-KR" docs CVF_SESSION` returned no pre-existing owner before authoring | ACCEPT |
| adjacent owner collision | invocation-control audit and provider/model roadmap found; they are predecessor evidence and subordinate scope, not duplicate T0 outputs | ACCEPT |

## Scope / Methodology

The worker enumerates only repository-local, non-archive owner surfaces named
by the audit or discovered through bounded token searches. For every knowledge
domain it records exact source path and section, authority class, evidence
class by access mode, unresolved questions, and a later acquisition priority.
The worker must challenge broad claims and must not convert absence of evidence
into an implementation proposal.

## Required Artifact Manifest

Exactly three worker outputs are allowed:

1. `docs/reference/external_agent_invocation_control/README.md`
2. `docs/reference/external_agent_invocation_control/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_GAP_AND_SOURCE_ACQUISITION_MAP.md`
3. `docs/reviews/CVF_EAIC_KR_T0_WORKER_RETURN_2026-07-22.md`

Both remain unstaged and uncommitted. HEAD remains unchanged.

## CLI/MCP And External-Service Prohibition

The worker must not start a separately dispatched agent session, external
agent CLI, MCP tool/server, provider API, API key, account subscription,
browser, network service, external search, or external-repository clone.
Provider-native internal reasoning, exploration, context management, and
internal subagents remain autonomous inside the parent worker's approved
scope. Local Git, PowerShell, Python governance checks, filesystem reads, and
repository searches are allowed.

## Acceptance Criteria

- All nine roadmap domains have a terminal authority disposition.
- Every OWNED or PARTIAL claim cites a current repo-local source and section.
- Every missing source has a bounded acquisition question, source class,
  priority, and operator checkpoint.
- API-key spend, subscription quota, token telemetry, estimates, and unknown
  usage remain distinct evidence classes.
- No runtime owner, MCP behavior, cancellation behavior, cost precision, or
  provider capability is inferred from an external proposal or chat history.
- Exactly three Allowed outputs remain unstaged; HEAD is unchanged.
- External-service invocation counters remain zero.

## Evidence / Verification

Evidence is the exact source ledger, nine-domain terminal-state matrix,
acquisition rows, bounded search commands, actual changed manifest, zero-call
statement, worker-return fast gate, and file-size guard. The reviewer
recomputes representative paths, classifications, and coverage.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | parent worker session and provider-native internal orchestration | internal reasoning and task decomposition remain autonomous inside Allowed scope | worker-autonomy and delegation-boundary standards after operator correction | internal helpers inherit the parent envelope | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | no released interface | separately dispatched and perimeter-crossing actions remain prohibited | invocation-control audit and zero external-action evidence | future source-verified adapter owner remains parked | `DEFERRED_WITH_REASON` |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | closed bounded status; ACCEPT; Source Verification Block columns; exact ADIF query; Target / Source; Scope / Methodology; Claim Boundary |
| gateRunPurpose | confirm baseline shape and source-backed release evidence before manual dispatch |
| claimBoundary | structural compliance does not establish external-agent runtime control or source completeness |

## Current Runtime Freshness Verification

Reviewer closure re-read every critical owner surface named by the T0 map at
closure base `1e689ed52`. Current source confirms request-level and advisory
controls but no effective end-to-end external-agent lifecycle owner. No
runtime, provider, or external service was invoked.

## Epistemic Process Block

### Expected Result / Prediction

CVF should contain substantial request-level and governance evidence, but lack
authoritative cross-access-mode knowledge for process supervision and hard
external-agent loop control.

### Evidence Comparison

The opening audit directly found contracts, receipts, advisory adapters, and
static command controls, while recording missing lifecycle, telemetry, budget,
termination, and reconciliation ownership.

### Contradiction Or Gap Disposition

Any apparent complete-control claim must be narrowed when it lacks current
source, an effective caller, access-mode evidence, or a fail-closed boundary.

### Claim Update

T0 produces a knowledge and acquisition map only. Readiness remains unproven
until later operator-approved primary-source intake is reviewed.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | NOT_APPLICABLE_WITH_REASON: T0 consumes only CVF-governed records; it does not ingest a new external source |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | parent roadmap, this baseline, and the T0 source-acquisition map |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | later primary-source intake requires a fresh operator-approved tranche |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private control-gap and knowledge-readiness evidence only.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Baseline status | this file | reviewer-repaired closed bounded status | PASS |
| Work order status | paired EAIC-KR-T0 work order | reviewer-repaired closed bounded status | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_EAIC_KR_T0_COMPLETION_2026-07-22.md` | accepted output plus operator boundary correction | PASS |
| Roadmap state | parent EAIC-KR roadmap | T0 pass bounded; T1 parked | PASS |
| Registry JSON | corpus registry remains outside this T0 closure scope | no registry mutation authorized | BLOCKED with reason |
| Registry Markdown | corpus registry remains outside this T0 closure scope | no registry mutation authorized | BLOCKED with reason |
| External evidence digest | N/A with reason: no new external source intake | repository-local evidence only | N/A with reason |
| System loop interlock | stable knowledge map and operator source-selection gate | no T1 auto-release | PASS |
| Session continuity | active handoff sync after material commit | reviewer/closer owned | PASS |

## Claim Boundary

This baseline authorizes one manual no-commit worker to map repository-local
knowledge and acquisition needs. It does not authorize external research,
agent CLI/MCP, provider/API/account use, runtime or checker changes, secrets,
live proof, public-sync, commit, push, deployment, production action, or a lift
of the invocation moratorium.
