# CVF GC-018 Authorization Baseline - AHB-T1 Handoff Boundary Audit

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: gc018

Date: 2026-06-16

Batch ID: AHB-T1

rawMemoryReleased: false

## Purpose

Authorize a bounded, read-only audit that maps every existing CVF agent-handoff
surface against every first-class role configuration and phase, identifies where
the handoff seam is currently left to per-batch interpretation, and proposes one
canonical Agent Handoff Contract model for Codex critique.

This tranche does not implement checkers, wire gates, mutate runtime/source/test
files, edit the interlock registry, run providers, public-sync, or build the
future agent-interaction workspace. It produces an audit matrix and a proposed
model only.

## Authorization Decision

Operator instruction on 2026-06-16: single-agent/multi-role and
multi-agent/multi-role are both first-class CVF operating modes; CVF must
guarantee the handoff seam is sound across all of them; a single shared handoff
pattern is mandatory rather than per-finding patching; a dedicated
agent-interaction workspace is planned. Operator direction: Claude authors and
proposes the roadmap and audit; Codex participates by critique/rebuttal before
ratification.

Rationale: recent dispatch batches (PLCS-T2, PLCS-T3, B11/B12 promotion) hit
defects at the seam between authoring and executing actors (B12 dispatch-scope
manifest, stale trace blocks, base-head ambiguity, cross-batch worktree
pollution). These are seam errors caused by independent per-batch interpretation
of a shared boundary. An audit-first model proposal is the safe first step before
any unified machine check.

Additional operator-reported authoring-time seam findings B13, B14, and B15 are
in scope as audit inputs. They must be treated as findings to verify against
current artifacts, not as provider-memory authority.

State-vs-redirect note: at the time of this baseline,
`CVF_SESSION/ACTIVE_SESSION_STATE.json` still records the next move as AOT-T3
(prepared from PLCS-T3 closure). The AHB redirect is an in-session operator
instruction that pauses AOT-T3 pending AHB review; it is NOT yet reflected in the
state file. The authorization source for AHB-T1 is therefore the operator
instruction, not the state file. Codex must reconcile
`CVF_SESSION/ACTIVE_SESSION_STATE.json` `nextAllowedMove` to AHB at AHB-T1
closure (and re-record AOT-T3 as queued), so the state file stops disagreeing
with the active next move.

## Baseline Decision

Decision: dispatch AHB-T1 to Claude as author/proposer under
`WORKER_MUST_NOT_COMMIT`; Codex reviews/critiques and owns commit and closure.

This tranche must create:

- the AHB-T1 handoff-boundary audit and proposed contract model (Markdown, under
  `docs/audits/` and/or `docs/reference/`);
- a worker return packet under `docs/reviews/`.

Codex reviews the audit, records critique using the multi-agent rebuttal
template, and decides whether to close AHB-T1, request repair, or escalate to the
operator. No checker, runtime, registry, provider, or public-sync mutation is
authorized.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Dispatch prompt envelope is a governed handoff surface | `docs/reference/CVF_AGENT_DISPATCH_PROMPT_ENVELOPE_STANDARD_2026-06-15.md` | envelope fields | `Dispatch Prompt Envelope` | dispatch prompt envelope standard | ACCEPT |
| Commit steward protocol governs commit ownership at handoff | `docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md` | protocol body | commit steward protocol | commit steward standard | ACCEPT |
| Manifest/trace scope is governed by the AOT trace standard | `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md` | `### Expected Manifest And Manifest Delta (AOT-T2-C01)` | `Expected manifest` | AOT trace standard | ACCEPT |
| B12 dispatch manifest scope discipline is documented | `docs/reference/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_STANDARD_2026-06-16.md` | `## Dispatch Manifest Scope Discipline` | `Dispatch Manifest Scope Discipline` | finding propagation standard | ACCEPT |
| MA1 multi-agent work transfer packet is predecessor authority | `docs/reference/archive/CVF_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_STANDARD_2026-05-26.md` | standard body | MA1 transfer packet | archived MA1 standard | ACCEPT |
| Multi-agent rebuttal template exists for Codex critique | `docs/reference/CVF_MULTI_AGENT_REBUTTAL_TEMPLATE.md` | template body | rebuttal template | multi-agent rebuttal template | ACCEPT |
| Active session state currently names AOT-T3 as the recorded next move | `CVF_SESSION/state/entries/nextAllowedMove.json` | value | nextAllowedMove | active session state | ACCEPT (read-only fact; AHB is NOT yet the recorded state move) |
| AHB-T1 authorization is an in-session operator redirect, not yet reflected in state | canonical: operator instruction 2026-06-16 (this session) | operator turn redirecting next-move to AHB and pausing AOT-T3 pending AHB review | operator instruction | operator authorization | ACCEPT (operator-redirect source; state file to be reconciled when Codex closes AHB-T1) |

## Authorized Scope

Authorized:

- read the named handoff-surface authority files and the AHB roadmap;
- read, as read-only SESSION_SYNC-phase handoff surfaces, `AGENTS.md`,
  `CVF_SESSION_MEMORY.md`, `CVF_SESSION/ACTIVE_SESSION_STATE.json` and its
  session-state entries, the active handoff document, and the next-move
  freshness checker standard, so the SESSION_SYNC phase row and AC1 (every
  current handoff surface) can be completed without mutating any of them;
- produce one AHB-T1 audit artifact containing the handoff-surface inventory, the
  role-configuration x phase x invariant matrix, the gap ledger, and the proposed
  Agent Handoff Contract model;
- map every existing surface (MA1, dispatch envelope, commit steward, AOT trace)
  into the proposed model with no orphaned surface;
- record where the future agent-interaction workspace would attach to the
  contract, as analysis input only;
- catalog B13, B14, and B15 in the audit gap ledger or recent seam findings
  section, clearly marking them as operator-reported authoring-time findings
  pending artifact-level verification;
- produce a worker return packet that states changed paths, blocked decisions,
  and HEAD unchanged.

Forbidden:

- implement or modify any checker;
- wire any check into the autorun gate chain or local hook chain;
- ratify the contract (ratification is AHB-T2, gated on Codex critique and
  operator decision);
- build or scaffold the agent-interaction workspace;
- edit `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json`;
- scan new `.private_reference/legacy/` roots;
- rewrite historical closed artifacts;
- edit runtime/source/test files;
- mutate generated active session state;
- run provider/API/OCR/live proof;
- public-sync;
- claim production/public readiness.

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | Audit inventories every current handoff surface with its owning artifact; no surface is invented. |
| AC2 | The matrix covers single-agent/multi-role, two-agent author/execute, N-plus-agent, and worker-must-not-commit configurations across dispatch/execution/closure/session-sync phases with the six invariants (actor identity, base-head anchor, changed-set attribution, trace-scope, commit ownership, cross-batch isolation). |
| AC3 | The gap ledger flags each per-batch-interpretation cell, citing a concrete recent example where available. |
| AC4 | The proposed contract maps MA1, dispatch envelope, commit steward, and AOT trace into the model with no orphaned surface. |
| AC5 | AHB-T1 claims no enforcement; it proposes a model and bounds AHB-T2 ratification scope. |
| AC6 | Worker return preserves WORKER_MUST_NOT_COMMIT and states HEAD unchanged. |
| AC7 | No runtime/checker/registry/provider/public-sync mutation is claimed. |

## Commit Mode

WORKER_MUST_NOT_COMMIT for the Claude author. Codex reviews actual files,
records critique, performs any allowed reviewer repairs, commits accepted
material, and runs the closure gate. This mirrors the PLCS-T1 author/reviewer
split and is itself an instance of the seam this roadmap studies.

## Negative Search And Collision Discipline

Search command used before authoring:

```powershell
rg -n "Agent Handoff Boundary|handoff contract|handoff seam|AHB-T" docs
```

Search roots: `docs/`.

Same-purpose collision result: this batch establishes the AHB family. MA1,
dispatch envelope, commit steward, and AOT trace are predecessor authority and
are reconciled, not superseded. No existing AHB audit artifact exists.

Collision disposition: AHB owns the unified handoff-boundary model. Predecessor
surfaces remain source authority until AHB-T2 explicitly reconciles them.

## Current Runtime Freshness Verification

This baseline makes no runtime/source/test/provider/live behavior claim. Runtime
freshness is `N/A with reason`: AHB-T1 is a read-only governed-markdown audit and
model proposal. No claim is made about provider registry surfaces; runtime,
checker, registry, provider, OCR, and public-sync mutation are forbidden.

## Evidence / Verification

Required authoring checks before dispatch/commit:

- `python governance/compat/check_dispatch_prompt_envelope.py --base 105e22cf --head HEAD --enforce`
- `python governance/compat/check_work_order_dispatch_quality.py --base 105e22cf --head HEAD --enforce`
- `python governance/compat/check_markdown_structural_completeness.py --base 105e22cf --head HEAD --enforce`
- `python governance/compat/check_agent_operation_trace.py --base 105e22cf --head HEAD --enforce`
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 105e22cf --head HEAD`

Required post-commit closure checks (Codex):

- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 105e22cf --head HEAD`
- `python governance/compat/run_agent_commit_steward_preflight.py --mode closure --base 105e22cf --head HEAD --enforce`

## Knowledge Absorption Blind-Spot Control Block

- Absorption target: existing governed handoff surfaces and the B11/B12 seam
  findings from the PLCS dispatch sessions.
- Prior absorption evidence resolved: dispatch envelope, commit steward, AOT
  trace, finding-propagation standard current; MA1 archived as predecessor.
- Blind spot risk: the audit could miss a role configuration (for example a
  three-agent chain) or a phase (session sync), leaving a seam unmodeled.
- Mitigation: AC2 fixes the required role configurations, phases, and invariants;
  Codex critique explicitly checks for missing cells.
- Runtime/source authority boundary: this is a documentation audit; no runtime,
  checker, or workspace claim is introduced.

## Rescan Intelligence Hardening

- Original source artifact: NOT_APPLICABLE_WITH_REASON - this baseline does not
  reopen a corpus rescan or new intake replay.
- Predecessor intake artifact: dispatch envelope, commit steward, AOT trace,
  finding-propagation, and archived MA1 standards.
- Delta ledger status: NOT_APPLICABLE_WITH_REASON - AHB-T1 audits already-governed
  surfaces; no new delta ledger.
- Routing matrix status: DO_NOW for the AHB-T1 audit and model proposal; contract
  ratification, machine check, and workspace build belong SEPARATE_RUNTIME_TRANCHE
  or STRATEGIC_OPERATOR_DECISION.
- Semantic sampling status: bounded adversarial boundary sample below.
- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

### Original-Intake Delta Ledger

Delta category vocabulary retained for decision boundary:
`UNCHANGED_FROM_INTAKE`, `CHANGED_DISPOSITION`, `NEW_FINDING`, and
`REMOVED_OR_REJECTED`. AHB-T1 audits existing surfaces; it must not claim a fresh
rescan delta.

### Follow-Up Routing Matrix

Routing lane vocabulary retained for decision boundary: `DO_NOW`,
`SEPARATE_RUNTIME_TRANCHE`, `STRATEGIC_OPERATOR_DECISION`, `OUT_OF_SCOPE`, and
`RESOLVED_BY_DESIGN`. AHB-T1 itself is the DO_NOW audit; contract ratification is
a STRATEGIC_OPERATOR_DECISION after Codex critique; the unified machine check and
workspace are SEPARATE_RUNTIME_TRANCHE.

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| AHB-T1-S1 | Authorized Scope | Audit proposes a contract model without ratifying it | DO_NOW bounded audit | Could a proposed model be treated as enforced governance? | PASS_BOUNDARY - AC5 forbids enforcement claims; ratification is AHB-T2 gated on critique and operator decision. |
| AHB-T1-S2 | Acceptance Criteria | Matrix covers all four role configurations | DO_NOW bounded audit | Could the audit silently cover only the two-agent case it was triggered by? | PASS_BOUNDARY - AC2 mandates all four configurations and four phases; Codex critique checks for missing cells. |

## Core Guard Self-Protection Block

This GC-018 baseline authorizes AHB-T1 handoff-boundary audit and model proposal
only. It does not self-modify GC-018, GC-021, GC-022, GC-023, GC-047, GC-048,
GC-049, GC-050, GC-051, GC-052, or any other governance control document. Any
change to governance controls, any checker implementation, or any workspace build
requires a separate GC-018 and operator authorization.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch baseline. No public-sync batch is authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Claude Code (GC-018 authoring) |
| Provider or surface | Claude Code local workspace |
| Session or invocation | 2026-06-16 AHB-T1 GC-018 authoring |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | Read, Write, Grep, Glob, PowerShell |
| Target paths | `docs/baselines/CVF_GC018_AHB_T1_HANDOFF_BOUNDARY_AUDIT_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_T1_HANDOFF_BOUNDARY_AUDIT_FOR_CLAUDE_2026-06-16.md` |
| Allowed scope source | operator instruction 2026-06-16: build one shared handoff pattern; Claude proposes, Codex critiques |
| Before status evidence | HEAD `105e22cf`; clean worktree |
| After status evidence | pending material commit |
| Diff evidence | `git diff --name-status` before commit |
| Approval boundary | audit dispatch authoring only; no checker/runtime/registry/provider/public mutation |
| Claim boundary | no runtime/provider/live/public/registry/checker/workspace mutation |
| Agent type | Claude Code (GC-018 dispatch authoring); Claude (audit author); Codex (critic/closer) |
| Invocation ID | `ahb-t1-gc018-dispatch-authoring-2026-06-16` |
| Expected manifest | `docs/baselines/CVF_GC018_AHB_T1_HANDOFF_BOUNDARY_AUDIT_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_T1_HANDOFF_BOUNDARY_AUDIT_FOR_CLAUDE_2026-06-16.md` |
| Actual changed set | pending |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

This baseline authorizes AHB-T1 handoff-boundary audit and model proposal only.
It does not ratify a contract, implement checkers, build the agent-interaction
workspace, edit the interlock registry, run live proof, public-sync, or make
production/public readiness claims. Contract ratification is AHB-T2, gated on
Codex critique and operator decision.
