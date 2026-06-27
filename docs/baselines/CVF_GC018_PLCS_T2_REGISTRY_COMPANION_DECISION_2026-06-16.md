# CVF GC-018 Authorization Baseline - PLCS-T2 Registry-Companion Decision

Memory class: FULL_RECORD

Status: DISPATCH_SATISFIED_BY_PLCS_T2_REVIEW

docType: gc018

Date: 2026-06-16

Batch ID: PLCS-T2

rawMemoryReleased: false

## Purpose

Authorize a bounded, documentation-only PLCS-T2 decision task to determine
whether each FPC-T2 C01-C04 registry-edit work order should carry an
absorption-intake companion entry, and if so, what the minimum required shape
of that companion entry must be.

This tranche does not edit the interlock registry, implement checkers, mutate
runtime/source/test files, run providers, or public-sync. It produces one
decision packet (Codex-owned) that defines the companion entry shape and
per-candidate ruling before any C01-C04 registry-edit work order is
dispatched.

## Authorization Decision

Operator instruction on 2026-06-16: PLCS-T2 registry-companion decision is
the next bounded move after PLCS-T1 closure. Decide the companion entry shape
so that future C01-C04 registry-edit batches do not run as parallel isolated
documentation lanes.

Rationale: PLCS-T1 routed FPC-T2 C01/C02/C03/C04 as `ADD_INTERLOCK_ENTRY`
proposal-only (separate work orders required). Each of those future work
orders will touch the system-loop interlock registry JSON and Markdown. Without
a prior decision on whether the routing matrix row, CCLV central facts entry,
and PLCS roadmap posture should travel as a companion alongside each registry
edit, the four registry-edit batches will each independently decide (or
ignore) the absorption-intake link - creating exactly the parallel-lane drift
PLCS was designed to prevent.

## Baseline Decision

Decision: dispatch PLCS-T2 to Codex under `CODEX_OWNS_COMMIT` mode.

This tranche must create:

- `docs/reference/CVF_PLCS_T2_REGISTRY_COMPANION_DECISION_2026-06-16.md`.

Codex owns authoring, gate verification, commit, and session sync.

No provider/model/live proof is authorized. This baseline does not authorize
access to `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` or
`PROVIDER_CAPABILITY_REGISTRY`; those surfaces are out of scope for this
documentation-only decision packet.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| FPC-T2 C01-C04 are proposal-only ADD_INTERLOCK_ENTRY decisions | `docs/reviews/CVF_FPC_T2_SYSTEM_LOOP_INTERLOCK_EXPANSION_DECISION_COMPLETION_2026-06-13.md` | `## Decision Result` | C01; C02; C03; C04 | FPC-T2 completion review | ACCEPT |
| PLCS-T1 matrix Section C routes C01-C04 as registry-edit candidates | `docs/reference/CVF_PLCS_T1_ABSORPTION_TO_WORKFLOW_CHAIN_ROUTING_MATRIX_2026-06-16.md` | `## Section C: FPC-T2 Candidate Routing Summary` | C01; C02; C03; C04 `next action` | PLCS-T1 routing matrix | ACCEPT |
| CCLV standard defines Required Central Facts fields for shared batch facts | `docs/reference/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_STANDARD_2026-06-16.md` | `## Required Central Facts` | `centralFactsReference` | CCLV standard | ACCEPT |
| PLCS Standing Operating Rule requires Central Core + Local View for all future related foundation hardening | `docs/roadmaps/CVF_PLANE_LAYER_WORKFLOW_CHAIN_SYSTEMIZATION_ROADMAP_2026-06-16.md` | `## Standing Operating Rule` | `Central Core + Local View` | PLCS roadmap | ACCEPT |
| System-loop interlock registry standard defines required fields for an interlock entry | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_STANDARD_2026-06-02.md` | `## Required Fields` | `id`; `upstreamPlane`; `downstreamPlane`; `automationLevel`; `routingRule` | interlock standard | ACCEPT |
| PLCS-T1 closed at material commit b05286fe and session sync 38c17198 | `CVF_SESSION/state/entries/nextAllowedMove.json` | value | nextAllowedMove | active session state | ACCEPT |

## Authorized Scope

Authorized:

- read source authority files named in this baseline and the work order;
- produce one PLCS-T2 decision packet (Markdown, under `docs/reference/`);
- decide per-candidate (C01/C02/C03/C04) whether a companion entry is
  REQUIRED, OPTIONAL, or NOT_APPLICABLE, with reason;
- define the minimum companion entry shape fields if REQUIRED or OPTIONAL;
- record CCLV applicability (central facts/local view/N/A) for each candidate;
- record parallel-lane risk if companion entry is absent;
- record next-action for each candidate's registry-edit work order.

Forbidden:

- edit `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json`;
- edit the interlock registry Markdown companion;
- implement any FPC-T3 checker or template;
- scan new `.private_reference/legacy/` roots;
- rewrite historical closed artifacts;
- edit runtime/source/test files;
- mutate generated active session state;
- run provider/API/OCR/live proof;
- public-sync;
- claim production/public readiness;
- authorize downstream use-case adapter work;
- authorize C05 registry entry (blocked until FPC-T3-C01).

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | Decision packet covers all four candidates C01/C02/C03/C04 with a per-candidate companion ruling (REQUIRED / OPTIONAL / NOT_APPLICABLE). |
| AC2 | Where companion entry is REQUIRED or OPTIONAL, packet defines minimum shape fields (at minimum: which PLCS routing row, which CCLV disposition, and whether the registry-edit work order must carry a PLCS cross-reference). |
| AC3 | C05 remains blocked; its companion ruling is explicitly deferred until FPC-T3-C01 checker exists. |
| AC4 | CCLV disposition is recorded per candidate (central facts useful / local view only / N/A). |
| AC5 | Parallel-lane risk for each absent companion entry is assessed (low / medium / high). |
| AC6 | Packet is documentation-only; no registry, runtime, provider, or public-sync mutation is claimed. |
| AC7 | Codex owns authoring and commit; no WORKER_MUST_NOT_COMMIT mode. |

## Commit Mode

CODEX_OWNS_COMMIT. Codex authors the decision packet directly and commits.
No separate worker return is required. Codex runs pre-closure gate after
committing the decision packet and roadmap update.

## Negative Search And Collision Discipline

Search command used before authoring:

```powershell
rg -n "PLCS-T2|Registry.Companion|registry.companion|companion.entry|companion.shape" docs
```

Search roots: `docs/`.

Same-purpose collision result: search found only PLCS-T1 cross-references to
PLCS-T2 as a `CANDIDATE_AFTER_T1` row and one incidental "companion entries"
mention in an unrelated MEOR review. No existing PLCS-T2 decision packet
exists. This batch establishes PLCS-T2 as the first registry-companion
decision artifact.

Collision disposition: PLCS-T2 owns the registry-companion shape decision
only. FPC-T2 completion and PLCS-T1 matrix remain source authority and are
not superseded.

## Current Runtime Freshness Verification

This baseline makes no runtime/source/test/provider/live behavior claim.
Runtime freshness is `N/A with reason`: PLCS-T2 is a governed markdown
decision packet only. Runtime/source/test, registry, provider, OCR, and
public-sync mutation are explicitly forbidden.

## Evidence / Verification

Required authoring checks before dispatch/commit:

- `python governance/compat/check_dispatch_prompt_envelope.py --base 38c17198 --head HEAD --enforce`
- `python governance/compat/check_work_order_dispatch_quality.py --base 38c17198 --head HEAD --enforce`
- `python governance/compat/check_markdown_structural_completeness.py --base 38c17198 --head HEAD --enforce`
- `python governance/compat/check_agent_operation_trace.py --base 38c17198 --head HEAD --enforce`
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 38c17198 --head HEAD`

Required post-commit closure checks (Codex):

- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 38c17198 --head HEAD`
- `python governance/compat/run_agent_commit_steward_preflight.py --mode closure --base 38c17198 --head HEAD --enforce`

## Knowledge Absorption Blind-Spot Control Block

- Absorption target: PLCS-T1 matrix Section C (FPC-T2 candidate routing
  rows) and FPC-T2 completion review Decision Result.
- Prior absorption evidence resolved: PLCS-T1 routing matrix CLOSED; FPC-T2
  completion CLOSED; CCLV standard current.
- Blind spot risk: companion entry shape could be decided ad-hoc by each
  C01-C04 registry-edit work order, creating four inconsistent PLCS posture
  references.
- Mitigation: PLCS-T2 decision packet locks one canonical companion shape
  before any C01-C04 work order is dispatched.
- Runtime/source authority boundary: no legacy symbol may become a current
  runtime/source fact without future source verification.

## Rescan Intelligence Hardening

- Original source artifact: N/A with reason - this baseline does
  not reopen a corpus rescan or new intake replay.
- Predecessor intake artifact: PLCS-T1 routing matrix and FPC-T2 completion
  review (both closed).
- Delta ledger status: COMPLETE_WITH_DECLARED_LIMITS - PLCS-T2 derives from
  already-governed inputs; no new delta ledger.
- Routing matrix status: DO_NOW for the PLCS-T2 decision packet;
  registry edits, runtime, provider, and public-sync are OUT_OF_SCOPE.
- Semantic sampling status: bounded adversarial boundary sample below.
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

Delta category vocabulary retained for decision boundary:
`UNCHANGED_FROM_INTAKE`, `CHANGED_DISPOSITION`, `NEW_FINDING`, and
`REMOVED_OR_REJECTED`. PLCS-T2 may note changed companion requirements
relative to PLCS-T1 routing rows, but must not claim a fresh rescan delta.

### Follow-Up Routing Matrix

Routing lane vocabulary retained for decision boundary: `DO_NOW`,
`SEPARATE_RUNTIME_TRANCHE`, `STRATEGIC_OPERATOR_DECISION`, `OUT_OF_SCOPE`,
and `RESOLVED_BY_DESIGN`. PLCS-T2 itself is the DO_NOW companion-shape
decision; actual registry edits belong to separate C01-C04 work orders.

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| PLCS-T2-S1 | Authorized Scope | Companion entry shape can be decided before registry-edit work orders | DO_NOW bounded decision only | Could this be misread as authorization to edit the registry? | PASS_BOUNDARY - registry edit is explicitly forbidden; decision packet only defines shape rules. |
| PLCS-T2-S2 | Acceptance Criteria | C05 companion ruling deferred until FPC-T3-C01 | OUT_OF_SCOPE | Could C05 companion be decided now without the checker? | PASS_BOUNDARY - C05 registry entry remains MACHINE_CHECK_FIRST; companion decision inherits same block. |

## Core Guard Self-Protection Block

This GC-018 baseline authorizes PLCS-T2 decision packet authoring only. It
does not self-modify GC-018, GC-021, GC-022, GC-023, GC-047, GC-048, GC-049,
GC-050, GC-051, GC-052, or any other governance control document. Any change
to governance controls requires a separate GC-018 and operator authorization.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch baseline. No public-sync batch is
authorized.

## Closure Verification

PLCS-T2 is satisfied by:

`docs/reference/CVF_PLCS_T2_REGISTRY_COMPANION_DECISION_2026-06-16.md`

Final disposition: `CLOSED_PASS_BOUNDED`.

The decision packet is documentation-only and keeps registry edits, checker
implementation, runtime/source/test mutation, provider/live proof, public-sync,
C05 companion ruling, and downstream adapter authorization out of scope.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex orchestrator (GC-018 authoring) |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-16 PLCS-T2 GC-018 authoring |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | rg, Read, Write |
| Target paths | `docs/baselines/CVF_GC018_PLCS_T2_REGISTRY_COMPANION_DECISION_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_PLCS_T2_REGISTRY_COMPANION_DECISION_FOR_CODEX_2026-06-16.md` |
| Allowed scope source | operator instruction on 2026-06-16; PLCS roadmap PLCS-T2 CANDIDATE_AFTER_T1 |
| Before status evidence | HEAD `38c17198`; clean worktree |
| After status evidence | pending material commit |
| Diff evidence | `git diff --name-status` before commit |
| Approval boundary | decision packet dispatch only; no registry/runtime/provider/public mutation |
| Claim boundary | no runtime/provider/live/public/registry mutation |
| Agent type | Claude Code (GC-018 dispatch authoring); Codex (decision packet owner) |
| Invocation ID | `plcs-t2-gc018-dispatch-authoring-2026-06-16` |
| Expected manifest | `docs/baselines/CVF_GC018_PLCS_T2_REGISTRY_COMPANION_DECISION_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_PLCS_T2_REGISTRY_COMPANION_DECISION_FOR_CODEX_2026-06-16.md` |
| Actual changed set | pending |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

This baseline authorizes PLCS-T2 decision packet authoring only. It does not
absorb new knowledge, edit the interlock registry, implement checkers,
implement runtime, run live proof, public-sync, or make production/public
readiness claims. C05 companion ruling remains blocked until FPC-T3-C01
exists.
