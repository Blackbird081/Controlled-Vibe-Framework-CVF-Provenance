# CVF GC-018 Authorization Baseline - AHB-T2 Agent Handoff Contract Ratification

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: gc018

Date: 2026-06-16

Batch ID: AHB-T2

rawMemoryReleased: false

## Purpose

Authorize AHB-T2 as a bounded contract-ratification tranche for the CVF Agent
Handoff Boundary Systemization roadmap.

AHB-T2 consumes the closed AHB-T1 audit, Codex rebuttal, AHB-T1A cleanup, and
AOT-T3 dispatch-manifest scope check as source inputs. It must produce a
ratification packet that turns the AHB-T1 proposed Agent Handoff Contract into
a governed contract decision, without implementing a checker or building the
future agent-interaction workspace.

## Authorization Decision

Operator instruction on 2026-06-16: proceed after AOT-T3; use AOT-T3 as a
clean input for the Agent Handoff Contract and create a Claude work order.

Decision: dispatch AHB-T2 to Claude under `WORKER_MUST_NOT_COMMIT`. Claude
authors the ratification packet and worker return; Codex reviews actual files,
records critique/closure, and commits accepted material.

## Baseline Decision

Dispatch AHB-T2 as a documentation-only contract-ratification tranche.

This baseline authorizes exactly two Claude-authored worker outputs:

- `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`
- `docs/reviews/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_WORKER_RETURN_2026-06-16.md`

Codex-owned closure artifacts, roadmap status updates, and session continuity
updates are reviewer/closer work after the worker return is reviewed.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| AHB roadmap defines AHB-T2 as contract ratification after T1 | `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md` | Tranche Plan | `AHB-T2` | AHB roadmap | ACCEPT |
| AHB-T1 audit proposes the Agent Handoff Contract fields | `docs/audits/CVF_AHB_T1_HANDOFF_BOUNDARY_AUDIT_2026-06-16.md` | Proposed Agent Handoff Contract Model | contract fields | AHB-T1 audit | ACCEPT |
| Codex rebuttal requires AHB-T2 to decide cross-batch isolation and C3 semantics | `docs/reviews/CVF_AHB_T1_HANDOFF_BOUNDARY_AUDIT_CODEX_REBUTTAL_2026-06-16.md` | Condition Delta | `crossBatchIsolation`; C3 per-actor semantics | Codex rebuttal | ACCEPT |
| AOT-T3 is closed and provides the dispatch-manifest scope rule | `docs/reviews/CVF_AOT_T3_DISPATCH_MANIFEST_SCOPE_CHECK_COMPLETION_2026-06-16.md` | Findings / Position | `DISPATCH_SCOPE_VIOLATION` | AOT-T3 completion | ACCEPT |
| Dispatch envelope is a governed handoff input | `docs/reference/CVF_AGENT_DISPATCH_PROMPT_ENVELOPE_STANDARD_2026-06-15.md` | Required Fields | `Dispatch Prompt Envelope` | dispatch prompt envelope standard | ACCEPT |
| Commit steward protocol is a governed handoff input | `docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md` | protocol body | commit steward protocol | commit steward standard | ACCEPT |
| AOT trace standard is a governed handoff input | `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md` | Required Agent Operation Trace Block | Agent Operation Trace Block | AOT trace standard | ACCEPT |
| MA1 is predecessor multi-agent handoff vocabulary | `docs/reference/archive/CVF_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_STANDARD_2026-05-26.md` | standard body | MA1 transfer packet | archived MA1 standard | ACCEPT |

## Authorized Scope

Authorized:

- read and reconcile the AHB-T1 audit, Codex rebuttal, AHB-T1 completion,
  AHB-T1A cleanup closure, and AOT-T3 completion;
- author one AHB-T2 ratification packet under `docs/reference/`;
- decide the canonical Agent Handoff Contract field set, vocabulary, and surface
  mapping for MA1, dispatch envelope, commit steward, AOT trace, and session-sync
  next-move surfaces;
- explicitly decide `crossBatchIsolation` as a contract rule or bounded
  unresolved design point;
- explicitly decide C3 three-or-more-agent trace scope, commit owner, and closer
  identity semantics;
- absorb AOT-T3 as an already-closed derived AOT rule in the contract;
- author one worker return under `docs/reviews/`.

Forbidden:

- checker implementation or gate wiring;
- runtime/source/test mutation;
- interlock registry edits;
- provider/API/OCR/live proof;
- public-sync or public catalog changes;
- building or scaffolding the dedicated agent-interaction workspace;
- changing generated active session state;
- claiming production readiness, public readiness, or live governance behavior.

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | Ratification packet names the canonical Agent Handoff Contract fields and marks each as RATIFIED, RATIFIED_WITH_BOUNDARY, or DEFERRED_WITH_REASON. |
| AC2 | Surface mapping reconciles MA1, dispatch envelope, commit steward, AOT trace, and session-sync next-move surfaces with no orphaned source surface. |
| AC3 | AOT-T3 is absorbed as a closed input: dispatch trace manifests describe dispatch changed set only; future execution deliverables stay outside dispatch manifests. |
| AC4 | `crossBatchIsolation` decision is explicit and bounded, including whether the rule is one-batch-per-worktree, queue discipline, workspace isolation, or deferred mechanism. |
| AC5 | C3 three-or-more-agent trace-scope, commit-owner, and closer-identity semantics are explicitly resolved or deferred with blocking reason. |
| AC6 | Ratification packet states what AHB-T3 may implement later and what remains out of scope. |
| AC7 | No checker/runtime/registry/provider/public-sync/workspace mutation is claimed. |

## Commit Mode

WORKER_MUST_NOT_COMMIT for Claude. Codex owns review, closure, accepted material
commit, and session sync.

## Negative Search And Collision Discipline

Before authoring, Claude must run:

```powershell
rg -n "Agent Handoff Contract|handoff contract|crossBatchIsolation|AHB-T2" docs
```

Search roots: `docs/`.

Dispatch-time collision evidence:

| Query term | Observed source class | Dispatch disposition |
|---|---|---|
| `Agent Handoff Contract` | AHB-T1 proposal and AHB roadmap predecessor text | PREDECESSOR_INPUT |
| `handoff contract` | archived/predecessor standards and AHB family artifacts | PREDECESSOR_INPUT |
| `crossBatchIsolation` | AHB-T1 audit and Codex rebuttal gap/decision text | PREDECESSOR_INPUT |
| `AHB-T2` | AHB roadmap and this dispatch packet | CURRENT_DISPATCH |

If Claude finds a same-purpose already-ratified contract artifact, stop and
return corrected path evidence to Codex.

## Current Runtime Freshness Verification

Runtime freshness is N/A with reason: this is a governed markdown contract
ratification tranche. Runtime/source/test files, provider registry files such as
`provider-registry.ts`, `PROVIDER_CAPABILITY_REGISTRY`, interlock registries,
live proof, and public-sync are out of scope and must remain untouched.

## Evidence / Verification

Pre-dispatch checks for this dispatch batch:

- `python governance/compat/check_dispatch_prompt_envelope.py --base 88111c19 --head HEAD --enforce`
- `python governance/compat/check_work_order_dispatch_quality.py --base 88111c19 --head HEAD --enforce`
- `python governance/compat/check_agent_operation_trace.py --base 88111c19 --head HEAD --enforce`
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 88111c19 --head HEAD`

Worker return checks for Codex after Claude returns:

- `python governance/compat/run_worker_return_fast_gate.py`
- `python governance/compat/check_agent_operation_trace.py --base <executionBaseHead> --head HEAD --enforce`
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base <executionBaseHead> --head HEAD`

## Knowledge Absorption Blind-Spot Control Block

- Absorption target: AHB-T1 audit model, Codex rebuttal, AHB-T1A cleanup, and
  AOT-T3 closed dispatch-manifest scope check.
- Prior absorption evidence resolved: AHB-T1 inventory/model and AOT-T3 checker
  completion are governed artifacts, not provider memory.
- Blind spot risk: AHB-T2 could ratify only the two-agent case and leave C3 or
  session-sync semantics under-specified.
- Mitigation: AC2 and AC5 require no orphaned surfaces and explicit C3 handling.
- Runtime/source authority boundary: documentation contract only; no runtime,
  checker, registry, provider, or workspace claim.

## Rescan Intelligence Hardening

- Original source artifact: AHB-T1 audit and Codex rebuttal.
- Predecessor intake artifact: AHB roadmap, AHB-T1 completion, AHB-T1A cleanup,
  and AOT-T3 completion.
- Delta ledger status: COMPLETE_WITH_DECLARED_LIMITS.
- Routing matrix status: DO_NOW for AHB-T2 contract ratification; AHB-T3 machine
  check and agent-interaction workspace remain separate future tranches.
- Semantic sampling status: bounded adversarial samples below.
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Delta category | Dispatch disposition |
|---|---|
| `UNCHANGED_FROM_INTAKE` | AHB-T1 proposed fields remain the source model. |
| `CHANGED_DISPOSITION` | AOT-T3 moved from parked candidate to closed input. |
| `NEW_FINDING` | None in dispatch; Claude must record any new finding in the worker return. |
| `REMOVED_OR_REJECTED` | Checker/workspace/runtime work remains out of scope. |

### Follow-Up Routing Matrix

| Lane | Applies to | Rationale |
|---|---|---|
| DO_NOW | AHB-T2 ratification packet | operator authorized after AOT-T3 closure |
| RESOLVED_BY_DESIGN | AOT-T3 dispatch-manifest scope | closed input to contract |
| STRATEGIC_OPERATOR_DECISION | unresolved ratification field | only if Claude cannot safely ratify or bound a required field |
| SEPARATE_RUNTIME_TRANCHE | AHB-T3 unified machine check | requires ratified contract first |
| SEPARATE_RUNTIME_TRANCHE | agent-interaction workspace | requires contract and cross-batch decision |
| OUT_OF_SCOPE | runtime/provider/public-sync/registry/live proof | explicitly forbidden |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| AHB-T2-S1 | AHB-T1 contract proposal | one contract can cover all role configurations | ratification candidate | Could T2 ratify only the two-agent path? | PASS_BOUNDARY - AC5 requires C3 semantics. |
| AHB-T2-S2 | AOT-T3 completion | dispatch manifests exclude future execution deliverables | closed input | Could T2 reopen B12 as undecided? | PASS_BOUNDARY - AC3 absorbs AOT-T3 as closed. |

## Finding-To-Governance Learning Disposition

| Field | Disposition |
|---|---|
| Defect class | `RULE_GAP` |
| Learning lane | `GOVERNANCE_CONTROL_PLANE` |
| Escalation state | `STANDARD_CANDIDATE`; `CONTRACT_RATIFICATION_DISPATCHED` |
| Next control action | Claude authors AHB-T2 ratification packet; Codex reviews before closure |
| Worker blame | `N/A_WITH_REASON`: AHB-T2 addresses shared handoff-boundary semantics, not individual worker fault |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance dispatch. No public-sync batch is
authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatcher |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-16 AHB-T2 dispatch authoring |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, apply_patch, governance gates |
| Target paths | `docs/baselines/CVF_GC018_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_FOR_CLAUDE_2026-06-16.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md` |
| Allowed scope source | operator instruction 2026-06-16 to proceed with AHB-T2 after AOT-T3 |
| Before status evidence | HEAD `88111c19`; clean worktree |
| After status evidence | AHB-T2 dispatch batch pending commit |
| Diff evidence | `git diff --name-status 88111c19..HEAD` |
| Approval boundary | dispatch packet only |
| Claim boundary | no checker/runtime/provider/public/registry/workspace mutation |
| Agent type | Codex dispatcher |
| Invocation ID | `ahb-t2-agent-handoff-contract-ratification-dispatch-codex-2026-06-16` |
| Expected manifest | `docs/baselines/CVF_GC018_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_FOR_CLAUDE_2026-06-16.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md` |
| Actual changed set | `docs/baselines/CVF_GC018_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_FOR_CLAUDE_2026-06-16.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

This baseline authorizes AHB-T2 contract ratification packet authoring only. It
does not implement AHB-T3, wire gates, build the workspace, edit runtime/source
or registry files, run providers, public-sync, or claim production/public
readiness.
