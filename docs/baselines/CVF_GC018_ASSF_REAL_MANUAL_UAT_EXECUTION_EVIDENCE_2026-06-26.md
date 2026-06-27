# CVF GC-018 Baseline: ASSF Real Manual UAT Execution Evidence

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-26

docType: baseline

Batch ID: ASSF-UAT-EXEC

dispatchBaseHead: 6c39af2d

## Decision / Baseline / Proposed Tranche

| Field | Disposition |
|---|---|
| Decision | execute the prepared manual UAT script for `cvf-dispatch-quality-reviewer` against a committed governed packet |
| Baseline | ASSF-UAT T0-T4 closed bounded at material commit `a3805d26` |
| Proposed tranche | `ASSF-UAT-EXEC` |
| Worker route | Codex single-agent multi-role execution |
| Closure posture | `CLOSED_PASS_BOUNDED` |

## Purpose

Record real manual UAT execution evidence for `cvf-dispatch-quality-reviewer`
without certifying or mutating the package.

## Scope / Methodology

Codex executed the T2 manual UAT script from
`docs/reviews/CVF_ASSF_UAT_T2_MANUAL_OPERATOR_UAT_SCRIPT_2026-06-26.md` against
the committed ASSF-UAT packet range `110b64bf..a3805d26`.

## Evidence / Verification

| Evidence | Result |
|---|---|
| UAT target range | `110b64bf..a3805d26` |
| UAT target baseline | `docs/baselines/CVF_GC018_ASSF_UAT_EVIDENCE_COLLECTION_T0_T4_2026-06-26.md` |
| UAT target work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_UAT_EVIDENCE_COLLECTION_T0_T4_FOR_CODEX_2026-06-26.md` |
| Dispatch-quality command | PASS; 9 files checked; 0 violations; 0 marker violations |
| Dispatch packet author fast gate | PASS; 5/5 checks passed |
| ASSF generated index drift | PASS |
| ASSF resolver readout | PASS; one `cvf-dispatch-quality-reviewer` metadata-only candidate |

## Findings / Position

The package acceptance evidence is satisfied for this UAT target: the
dispatch-quality checker passed and the dispatch packet author fast gate passed
5/5. This is execution evidence for the package's stated validation purpose.
It is not certification and does not change source lifecycle fields.

## Risk / Corrective Action

| Risk | Disposition |
|---|---|
| UAT PASS could be mistaken for certification | Prevented: certification decision is not authorized in this tranche |
| UAT PASS could mutate registry state | Prevented: registry source and generated index remain unchanged |
| Fast gate could be cited without direct command evidence | Prevented: the command and 5/5 PASS result are recorded in this baseline and completion review |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| candidate identity is source-backed | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | root object | `skillId` | ASSF registry entry | VALUE_SET | ACCEPT |
| candidate acceptance evidence names dispatch-quality and fast gate checks | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | root object | `acceptanceEvidence` | ASSF registry entry | VALUE_SET | ACCEPT |
| T2 UAT script names dispatch-quality command | `docs/reviews/CVF_ASSF_UAT_T2_MANUAL_OPERATOR_UAT_SCRIPT_2026-06-26.md` | Manual UAT Script | `UAT-02` | ASSF-UAT script | LITERAL_INVARIANT | ACCEPT |
| T2 UAT script names fast gate command | `docs/reviews/CVF_ASSF_UAT_T2_MANUAL_OPERATOR_UAT_SCRIPT_2026-06-26.md` | Manual UAT Script | `UAT-03` | ASSF-UAT script | LITERAL_INVARIANT | ACCEPT |
| dispatch-quality checker exists | `governance/compat/check_work_order_dispatch_quality.py` | module | `main` | governance compatibility checker | EXISTS | ACCEPT |
| dispatch packet author fast gate exists | `governance/compat/run_dispatch_packet_author_fast_gate.py` | module | `GATE_COMMANDS` | governance compatibility helper | EXISTS | ACCEPT |

## Current Runtime Freshness Verification

| Runtime surface | Freshness action | Evidence | Disposition |
|---|---|---|---|
| Dispatch-quality UAT | ran current checker on committed target range | `python governance/compat/check_work_order_dispatch_quality.py --base 110b64bf --head a3805d26 --enforce` | PASS |
| Dispatch packet author fast gate | ran current 5-check helper on committed target range | `python governance/compat/run_dispatch_packet_author_fast_gate.py --base 110b64bf --head a3805d26 --enforce` | PASS |
| ASSF generated index drift | ran current drift check | `python governance/compat/check_assf_skill_index_drift.py` | PASS |
| ASSF resolver readout | ran current resolver query | `python governance/compat/run_assf_skill_resolver.py --task-class dispatch-authoring --role dispatcher --phase DISPATCH_AUTHORING --surface governance/compat --risk-ceiling R0` | PASS |

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
| Chain map route | operator direction to execute next allowed UAT evidence tranche |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this GC-018 baseline |
| Disposition | no external material absorbed |
| Claim boundary | repository-local command evidence only |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | ASSF-UAT-EXEC evidence artifacts | internal agents may use this UAT evidence to prepare a future certification-decision roadmap or work order only | UAT command evidence and completion review | no loader, activation, lifecycle mutation, or checker implementation | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future external package readout or adapter | external agents cannot certify, mutate, activate, execute, or consume package instructions through this tranche | registry external disposition remains deferred | external adapter remains deferred to later source-verified work | `DEFERRED_WITH_REASON` |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance UAT evidence; no public-sync authorization.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ASSF real manual UAT execution evidence |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE -- UAT commands executed; no certification |
| receiptEvidence | CVF_RECEIPT_PRESENT - dispatch-quality PASS, fast gate 5/5 PASS, drift PASS, resolver readout PASS |
| actionEvidence | ACTION_EVIDENCE_PRESENT -- command execution evidence and review artifacts |
| invocationBoundary | governed local command execution against committed documentation packet |
| interceptionBoundary | no provider, CLI, MCP, Web runtime, adapter, package instruction execution, lifecycle mutation, or certification action |
| claimLanguage | records UAT execution evidence and releases a future certification-decision lane |
| forbiddenExpansion | no package instance creation, certification decision, lifecycle mutation, registry mutation, generated-index mutation, resolver mutation, Web runtime change, CLI/MCP adapter, provider/live proof, public-sync, push, activation, readiness claim, package instruction execution, or session-sync in material commit |

## Acceptance Receipt Assertion Matrix

| Query ID | Receipt artifact | JSON path | Required value | Observed value | Status |
|---|---|---|---|---|---|
| ARAM-01 | command output | dispatch-quality violations | 0 | 0 | PASS |
| ARAM-02 | command output | dispatch-quality marker violations | 0 | 0 | PASS |
| ARAM-03 | command output | fast gate checks passed | 5/5 | 5/5 | PASS |
| ARAM-04 | command output | ASSF generated index drift | PASS | PASS | PASS |
| ARAM-05 | resolver output | totalCandidates | 1 | 1 | PASS |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_REAL_MANUAL_UAT_EXECUTION_EVIDENCE_FOR_CODEX_2026-06-26.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ASSF_REAL_MANUAL_UAT_EXECUTION_EVIDENCE_COMPLETION_2026-06-26.md` | `Reviewer verdict: CLOSED_PASS_BOUNDED`; `UAT evidence disposition: UAT_EXECUTION_PASS_EVIDENCE_RECORDED` | PASS |
| Roadmap state | N/A with reason: this is a next-allowed-move evidence tranche, not a new roadmap | no roadmap mutated | N/A with reason |
| Registry JSON | N/A with reason: no registry JSON mutation is authorized | no corpus registry JSON in changed set | BLOCKED with reason: out of scope |
| Registry Markdown | N/A with reason: no registry Markdown mutation is authorized | no corpus registry Markdown mutation | BLOCKED with reason: out of scope |
| External evidence digest | N/A with reason: no external artifact is created | no external digest applies | N/A with reason |
| System loop interlock | this baseline and completion review | no runtime loop, provider call, package activation, public-sync, or worker commit occurred | PASS |
| Session continuity | N/A with reason: session-sync is separate after material closure | active session paths excluded from material changed set | N/A with reason |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatcher/worker/reviewer/closer |
| Agent type | single-agent multi-role |
| Provider or surface | local workspace |
| Session or invocation | ASSF real manual UAT execution evidence, 2026-06-26 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | startup reads, source reads, UAT commands, apply_patch, governance gates, git |
| Target paths | `docs/baselines/CVF_GC018_ASSF_REAL_MANUAL_UAT_EXECUTION_EVIDENCE_2026-06-26.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_REAL_MANUAL_UAT_EXECUTION_EVIDENCE_FOR_CODEX_2026-06-26.md`; `docs/reviews/CVF_ASSF_REAL_MANUAL_UAT_EXECUTION_EVIDENCE_2026-06-26.md`; `docs/reviews/CVF_ASSF_REAL_MANUAL_UAT_EXECUTION_EVIDENCE_COMPLETION_2026-06-26.md` |
| Allowed scope source | next allowed move after ASSF-UAT T0-T4 session sync |
| Before status evidence | baseHead `6c39af2d`; worktree clean before material authoring |
| After status evidence | material artifacts pending commit |
| Diff evidence | `git diff --name-status`; `git diff --check`; autorun gates |
| Approval boundary | real manual UAT evidence recording only |
| Claim boundary | no certification, lifecycle mutation, runtime, provider/live, public-sync, package activation, or adapter behavior |
| Invocation ID | `assf-real-manual-uat-execution-evidence-2026-06-26` |
| Expected manifest | baseline, work order, UAT execution review, completion review |
| Actual changed set | baseline, work order, UAT execution review, completion review |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename in this material batch |

## Claim Boundary

This baseline records UAT execution evidence only. It does not certify, activate,
project, execute package instructions, export, adapt, machine-enforce, or mutate
any package or runtime surface.
