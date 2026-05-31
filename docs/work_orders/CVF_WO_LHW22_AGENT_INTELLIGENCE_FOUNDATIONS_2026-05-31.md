# CVF Agent Work Order - LHW22 Agent Intelligence Foundations

Memory class: FULL_RECORD

Status: READY_FOR_DISPATCH

docType: work_order

Date: 2026-05-31

## Purpose

Dispatch LHW22 as a documentation-only advisory connector wave for the three
highest-value agent-intelligence concepts selected from the LHW20 full scan:
UCO capability constraints, agent self-report, and capability registry.

Success means the implementer produces three source-verified connector specs
and three completion reviews without modifying runtime code, public-sync, route
files, provider behavior, live governance behavior, or receipt schemas.

## Scope / Target / Owner Boundary

Target wave: LHW22 documentation-only advisory connectors.

Allowed scope:

- Create `docs/reference/CVF_LHW22_T1_UCO_CAPABILITY_CONSTRAINT_ADVISORY_CONNECTOR_SPEC_2026-05-31.md`.
- Create `docs/reference/CVF_LHW22_T2_AGENT_SELF_REPORT_PROTOCOL_ADVISORY_CONNECTOR_SPEC_2026-05-31.md`.
- Create `docs/reference/CVF_LHW22_T3_CAPABILITY_REGISTRY_ADVISORY_CONNECTOR_SPEC_2026-05-31.md`.
- Create `docs/reviews/CVF_LHW22_T1_UCO_CAPABILITY_CONSTRAINT_ADVISORY_CONNECTOR_COMPLETION_2026-05-31.md`.
- Create `docs/reviews/CVF_LHW22_T2_AGENT_SELF_REPORT_PROTOCOL_ADVISORY_CONNECTOR_COMPLETION_2026-05-31.md`.
- Create `docs/reviews/CVF_LHW22_T3_CAPABILITY_REGISTRY_ADVISORY_CONNECTOR_COMPLETION_2026-05-31.md`.
- Update this work order, the LHW22 GC-018 baseline, the parent roadmap, and
  session continuity only when closure evidence exists.

Forbidden scope:

- Do not edit any `EXTENSIONS/` source or test file.
- Do not edit any `route.ts` file or runtime API response schema.
- Do not modify `GovernanceEvidenceReceipt`, provider routing, model gateway,
  memory gateway, learning-plane source, or R0-R3 risk taxonomy.
- Do not run live provider calls or claim live governance proof.
- Do not edit or push the public-sync clone.
- Do not execute LHW23 or LHW24 work from this order.

## Authority Chain

| Authority | Path / basis | Disposition |
|---|---|---|
| Operator instruction | In-session request on 2026-05-31 to raise guards, catch findings, and repair the packet | ACCEPT |
| Parent roadmap | `docs/roadmaps/CVF_LHW22_LHW23_LHW24_AGENT_INTELLIGENCE_ROADMAP_2026-05-31.md` | ACCEPT |
| Fresh GC-018 baseline | `docs/baselines/CVF_GC018_LHW22_AGENT_INTELLIGENCE_FOUNDATIONS_2026-05-31.md` | ACCEPT |
| Full-scan audit | `docs/audits/CVF_IMPORTANT_FULL_FILE_SCAN_BLINDSPOT_RECORD_2026-05-31.md` | ACCEPT |
| Work-order template | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | ACCEPT |

## Agent Roles

| Role | Responsibility | Boundary |
|---|---|---|
| Implementer | Author the three specs and completion reviews | Docs only |
| Reviewer | Run closure diff and verify source fidelity | No runtime claim expansion |
| Orchestrator | Stop or return the order if a source fact cannot be verified | No silent dispatch waiver |

## Required First Reads

- `docs/roadmaps/CVF_LHW22_LHW23_LHW24_AGENT_INTELLIGENCE_ROADMAP_2026-05-31.md`
- `docs/baselines/CVF_GC018_LHW22_AGENT_INTELLIGENCE_FOUNDATIONS_2026-05-31.md`
- `docs/audits/CVF_IMPORTANT_FULL_FILE_SCAN_BLINDSPOT_RECORD_2026-05-31.md`
- `.private_reference/legacy/CVF_Important/ADDING_TRUST & ISOLATION LAYER/CVF_TRUST_AND_ISOLATION_LAYER.md`
- `.private_reference/legacy/CVF_Important/ADDING_TRUST & ISOLATION LAYER/CVF_CAPABILITY_INTEGRATION_SPEC.md`
- `.private_reference/legacy/CVF_Important/ADDING_TRUST & ISOLATION LAYER/CVF_AGENT_RUNTIME_PROTOCOL.md`
- `.private_reference/legacy/CVF_Important/ADDING_AGENT DEFINITION/CVF_CAPABILITY_REGISTRY_MODEL.md`
- `docs/reference/CVF_LHW20_T1_SECURITY_HARDENING_CHECKLIST_FULL_ADVISORY_CONNECTOR_SPEC_2026-05-31.md`
- `governance/compat/check_work_order_dispatch_quality.py`

## Pre-Flight Checks

Capture a non-empty base before implementation:

```bash
git rev-parse --short HEAD
```

Run the required phase gates with the captured base and current head:

```bash
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base <baseHead> --head HEAD
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <baseHead> --head HEAD
```

If either phase fails, stop and return the order to Orchestrator with the
machine output. Do not continue by saying the implementer will fix it later.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| EXISTS UCO source concept | `.private_reference/legacy/CVF_Important/ADDING_TRUST & ISOLATION LAYER/CVF_TRUST_AND_ISOLATION_LAYER.md` | UCO trust/isolation source file | `UCO` | Future advisory map to `CVF_GUARD_CONTRACT` | ACCEPT |
| EXISTS UCO capability integration source | `.private_reference/legacy/CVF_Important/ADDING_TRUST & ISOLATION LAYER/CVF_CAPABILITY_INTEGRATION_SPEC.md` | Capability integration source file | `UCO` | Future advisory map to capability boundary docs | ACCEPT |
| EXISTS agent runtime self-report source | `.private_reference/legacy/CVF_Important/ADDING_TRUST & ISOLATION LAYER/CVF_AGENT_RUNTIME_PROTOCOL.md` | Agent runtime protocol source file | `confidence` | Future additive advisory map to `/api/execute` response surface | ACCEPT |
| EXISTS capability registry source | `.private_reference/legacy/CVF_Important/ADDING_AGENT DEFINITION/CVF_CAPABILITY_REGISTRY_MODEL.md` | Capability registry model source file | `Task->Capability->Agent` | Future advisory map to agent identity/capability ownership | ACCEPT |
| EXISTS full-scan acceptance record | `docs/audits/CVF_IMPORTANT_FULL_FILE_SCAN_BLINDSPOT_RECORD_2026-05-31.md` | Gate 3 accepted owner-map concepts | `ACCEPT_AS_OWNER_MAP` | LHW22 advisory intake owner map | ACCEPT |
| EXISTS prior UCO-related advisory boundary | `docs/reference/CVF_LHW20_T1_SECURITY_HARDENING_CHECKLIST_FULL_ADVISORY_CONNECTOR_SPEC_2026-05-31.md` | LHW20 T1 spec | `runtimeExecutionAuthorized` | Prior connector boundary | ACCEPT |

## Current Runtime Freshness Verification

This work order is allowed to cite current runtime surfaces only as owner
targets or gap boundaries. It does not authorize runtime edits.

| Runtime fact | Current source checked | Freshness disposition |
|---|---|---|
| Agent response schema changes are out of scope | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | Do not edit; LHW22 only documents future additive self-report concept |
| Guard-contract owner surface exists | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/contracts.phase2b-runtime-coherence.test.ts` | Owner-map reference only; no contract mutation |
| Capability registry runtime implementation is not being changed here | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | Current provider capability registry exists; LHW22 capability-to-agent advisory remains doc-only |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order instruction | Closure evidence required |
|---|---|---|
| LHW22 T1 UCO capability constraint advisory | Create T1 spec and completion review | Spec path, review path, source table, advisory boundary |
| LHW22 T2 agent self-report protocol advisory | Create T2 spec and completion review | Spec path, review path, source table, additive future-field boundary |
| LHW22 T3 capability registry advisory | Create T3 spec and completion review | Spec path, review path, source table, no runtime registry claim |
| Fresh GC-018 before dispatch | Use LHW22 GC-018 baseline as authority | Baseline remains `Status: AUTHORIZED` until closure update |
| Documentation-only execution | Forbid code, route, public-sync, and live proof work | `git diff --name-status`, gate output, explicit N/A reasons |

## Write Ownership

The implementer may create or update only the LHW22 spec/review files named in
Allowed scope, this work order, the LHW22 GC-018 baseline, the parent roadmap,
and session continuity files at closure. Any other changed path is a return
condition unless Orchestrator explicitly opens a separate governed batch.

## Execution Plan

1. Re-read the source files in the Source Verification Block.
2. Author T1, T2, and T3 specs with explicit source, gap, owner map, advisory
   boundary, memory class, and public export disposition.
3. Author one completion review per spec with closure diff, evidence, and
   Finding-To-Governance Learning Disposition if findings are recorded.
4. Run dispatch, implementation, closure, and markdown/public-export guards.
5. Update session continuity only after the wave has machine-backed closure
   evidence.

## Evidence Requirements

- `git diff --name-status <baseHead> HEAD`
- `python governance/compat/check_work_order_dispatch_quality.py --enforce --base <baseHead> --head HEAD`
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base <baseHead> --head HEAD`
- `python governance/compat/check_public_export_disposition.py --enforce --base <baseHead> --head HEAD`
- `python governance/compat/check_governed_file_size.py --enforce`
- Explicit `N/A with reason` for live proof, public-sync, and runtime tests.

## Acceptance Criteria

| Criterion | Required disposition |
|---|---|
| T1/T2/T3 specs exist at named paths | PASS with path evidence |
| T1/T2/T3 completion reviews exist at named paths | PASS with path evidence |
| Every source fact cites an existing source file or canonical contract | PASS |
| Every spec states `runtimeExecutionAuthorized=false` | PASS |
| Public Export Disposition is present and private-only | PASS |
| No runtime, route, public-sync, or live provider change occurred | PASS with diff evidence |
| Autorun and compatibility guards pass on a non-empty range | PASS |

## Review Gate

The reviewer must compare the parent roadmap, this work order, all final specs,
all completion reviews, and the actual git diff. A handwritten PASS is not
accepted if any machine guard fails.

## Closure Checklist

| Item | Resolution |
|---|---|
| Source Verification Block remains complete | PENDING |
| Roadmap-To-Work-Order Trace Matrix remains complete | PENDING |
| Closure Diff Gate completed | PENDING |
| Public Export Disposition present in changed governed artifacts | PENDING |
| Session continuity updated after closure only | PENDING |
| No untracked or unrelated worktree residue remains | PENDING |

## Return-To-Orchestrator Conditions

Return this order without implementation if a cited source path is missing, a
runtime field name cannot be verified, a guard fails and the assigned task is
not guard repair, a code/public/live change is required to satisfy a claim, or
the implementer finds LHW23/LHW24 work mixed into this LHW22 closure.

## Operator Checkpoint

SATISFIED_FOR_DISPATCH_PREP by operator instruction on 2026-05-31 to repair the
guards and clean the LHW22-LHW24 findings. Implementation still requires the
pre-dispatch and pre-implementation gates to pass.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Private provenance dispatch only. No public-sync artifact or public catalog
claim is authorized by this work order.

## Claim Boundary

This work order authorizes documentation-only advisory connector work for LHW22.
It does not prove runtime governance behavior, provider quality, public
readiness, model-routing intelligence, learning-loop execution, or production
readiness.
