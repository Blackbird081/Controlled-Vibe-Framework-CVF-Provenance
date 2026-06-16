# CVF GC-018 Authorization Baseline - PLCS-T3 Companion Routing Checker And Template Decision

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: gc018

Date: 2026-06-16

Batch ID: PLCS-T3

rawMemoryReleased: false

## Purpose

Authorize a bounded, documentation-only PLCS-T3 decision task to determine
whether a machine check should require absorption-derived governed artifacts
to carry an explicit workflow-chain routing disposition, and whether the
PLCS companion block locked by PLCS-T2 should be promoted into a reusable
template that future C01-C04 registry-edit work orders must follow.

This tranche does not implement runtime checkers against the live gate chain,
edit the interlock registry, mutate runtime/source/test files, run providers,
or public-sync. It produces one decision-and-template packet (Codex-owned)
that records the checker disposition, the companion-block template shape, and
the enforcement-placement recommendation before any C01-C04 registry-edit work
order is dispatched.

## Authorization Decision

Operator instruction on 2026-06-16: after PLCS-T2 closure, PLCS-T3
checker/template hardening is the next bounded move. Decide whether a checker
should enforce that absorption-derived governed artifacts carry a
workflow-chain routing disposition, and lock the companion-block template so
the four future C01-C04 registry-edit work orders cannot each invent their own
companion shape.

Rationale: PLCS-T2 locked what a PLCS companion block must contain
(`plcs_routing_row`, `plcs_routing_disposition`, `cclv_disposition`,
`parallel_lane_risk`, `plcs_cross_reference`, `registry_edit_boundary`,
`c05_boundary`). It did not lock how a machine check would enforce the block
or whether a reusable template should carry it. Without a PLCS-T3 decision,
each of the four C01-C04 registry-edit work orders will independently decide
its companion-block format and its checker posture, re-creating the
parallel-lane drift that PLCS was designed to prevent, this time at the
checker/template layer rather than the routing layer.

## Baseline Decision

Decision: dispatch PLCS-T3 to Codex under `WORKER_MAY_COMMIT` mode.

This tranche must create:

- `docs/reference/CVF_PLCS_T3_COMPANION_ROUTING_CHECKER_TEMPLATE_DECISION_2026-06-16.md`.

Codex owns authoring, gate verification, commit, and session sync.

No provider/model/live proof is authorized. This baseline does not authorize
runtime checker wiring into the autorun gate chain or the local hook chain;
it authorizes only a checker disposition decision plus the companion-block
template definition. Actual checker implementation, if approved, requires a
separate GC-018 and source-verified work order.

Operator update during dispatch review: Claude-reported B11/B12 lessons were
provider-memory learning candidates and must be promoted into governed CVF
authoring guidance before PLCS-T3 proceeds. This dispatch batch therefore also
authorizes bounded documentation updates to the finding propagation standard
and work-order authoring addendum. It does not authorize checker code changes.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| PLCS-T2 locked the companion block minimum fields | `docs/reference/CVF_PLCS_T2_REGISTRY_COMPANION_DECISION_2026-06-16.md` | `## Companion Entry Shape Definition` | `plcs_routing_row` | PLCS-T2 decision packet | ACCEPT |
| PLCS-T2 ruled C01-C04 companion REQUIRED and deferred C05 | `docs/reference/CVF_PLCS_T2_REGISTRY_COMPANION_DECISION_2026-06-16.md` | `## Per-Candidate Decision Table` | `REQUIRED` | PLCS-T2 decision packet | ACCEPT |
| C05 companion ruling deferred pending FPC-T3-C01 | `docs/reference/CVF_PLCS_T2_REGISTRY_COMPANION_DECISION_2026-06-16.md` | `## C05 Companion Ruling Deferral` | `DEFERRED_PENDING_FPC_T3_C01` | PLCS-T2 decision packet | ACCEPT |
| PLCS-T1 matrix records per-row checker/template dispositions | `docs/reference/CVF_PLCS_T1_ABSORPTION_TO_WORKFLOW_CHAIN_ROUTING_MATRIX_2026-06-16.md` | checker/template disposition rows | `candidate` | PLCS-T1 routing matrix | ACCEPT |
| CCLV standard defines required central facts and local references | `docs/reference/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_STANDARD_2026-06-16.md` | `## Required Central Facts` | `centralFactsReference` | CCLV standard | ACCEPT |
| FPRC-T2 promoted finding-to-governance learning enforcement | `docs/reference/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_STANDARD_2026-06-16.md` | finding propagation rules | `GOVERNANCE_CONTROL_PLANE` | finding propagation standard | ACCEPT |
| Work-order authoring addendum carries reusable dispatch authoring guidance | `docs/reference/CVF_WORK_ORDER_AUTHORING_HARDENING_ADDENDUM_2026-06-11.md` | `## Dispatch Packet Authoring Learning Promotion` | `Dispatch Packet Authoring Learning Promotion` | work-order authoring addendum | ACCEPT |
| PLCS-T3 is the authorized next bounded move after PLCS-T2 closure | `CVF_SESSION/state/entries/nextAllowedMove.json` | value | nextAllowedMove | active session state | ACCEPT |

## Authorized Scope

Authorized:

- read source authority files named in this baseline and the work order;
- produce one PLCS-T3 decision-and-template packet (Markdown, under
  `docs/reference/`);
- decide whether a machine check should require absorption-derived governed
  artifacts to carry a workflow-chain routing disposition, with a verdict of
  CHECKER_APPROVED, CHECKER_DEFERRED, or CHECKER_REJECTED and reason;
- define the reusable companion-block template that C01-C04 registry-edit work
  orders must embed, derived from the PLCS-T2 locked field set;
- record the recommended enforcement placement (earliest applicable autorun
  phase gate, hook chain, or template-only) without wiring it in this batch;
- record CCLV applicability for the template and the decision packet;
- record parallel-lane risk if no template or checker is adopted.
- promote the Claude-reported B11/B12 reusable dispatch-authoring lessons into
  governed documentation surfaces only:
  `docs/reference/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_STANDARD_2026-06-16.md`
  and
  `docs/reference/CVF_WORK_ORDER_AUTHORING_HARDENING_ADDENDUM_2026-06-11.md`.

Forbidden:

- implement a runtime checker file or modify any existing checker;
- wire any check into `run_agent_autorun_workflow_gate.py` or
  `run_local_governance_hook_chain.py`;
- edit `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json`;
- edit the interlock registry Markdown companion;
- scan new `.private_reference/legacy/` roots;
- rewrite historical closed artifacts;
- edit runtime/source/test files;
- mutate generated active session state;
- run provider/API/OCR/live proof;
- public-sync;
- claim production/public readiness;
- authorize downstream use-case adapter work;
- decide the C05 companion ruling (remains deferred until FPC-T3-C01).
- implement B11/B12 as checker logic in this batch.

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | Decision packet records a checker disposition verdict (CHECKER_APPROVED / CHECKER_DEFERRED / CHECKER_REJECTED) with reason, citing PLCS-T1 and PLCS-T2 evidence. |
| AC2 | Decision packet defines the reusable companion-block template derived from the PLCS-T2 locked field set, suitable for embedding in C01-C04 registry-edit work orders. |
| AC3 | Decision packet records the recommended enforcement placement (autorun phase, hook chain, or template-only) without wiring any check in this batch. |
| AC4 | CCLV disposition is recorded for both the template and the decision packet. |
| AC5 | Parallel-lane risk for the no-template / no-checker case is assessed (low / medium / high). |
| AC6 | Packet is documentation-only; no checker implementation, registry, runtime, provider, or public-sync mutation is claimed. |
| AC7 | C05 companion ruling remains deferred; PLCS-T3 does not decide it. |
| AC8 | Codex owns authoring and commit; no WORKER_MUST_NOT_COMMIT mode. |
| AC9 | B11/B12 reusable dispatch-authoring lessons are promoted into governed documentation surfaces or explicitly carried as machine-check candidates; no provider-memory-only learning remains. |

## Commit Mode

WORKER_MAY_COMMIT. Codex authors the decision-and-template packet directly and
commits. No separate worker return is required. Codex runs pre-closure gate
after committing the decision packet and roadmap update.

## Negative Search And Collision Discipline

Search command used before authoring:

```powershell
rg -n "PLCS-T3|companion.routing.checker|companion.block.template|workflow.chain.routing.disposition.checker" docs
```

Search roots: `docs/`.

Same-purpose collision result: search found only the PLCS-T3 `CANDIDATE_AFTER_T1`
row in the PLCS roadmap and PLCS-T2 cross-references that name a future checker.
No existing PLCS-T3 decision-and-template packet exists. This batch establishes
PLCS-T3 as the first companion-routing checker-and-template decision artifact.

Collision disposition: PLCS-T3 owns the companion-routing checker disposition
and template decision only. PLCS-T1 matrix and PLCS-T2 decision packet remain
source authority and are not superseded.

## Current Runtime Freshness Verification

This baseline makes no runtime/source/test/provider/live behavior claim.
Runtime freshness is `N/A with reason`: PLCS-T3 is a governed markdown
decision-and-template packet only. Runtime/source/test, checker
implementation, registry, provider, OCR, and public-sync mutation are
explicitly forbidden.

## Evidence / Verification

Required authoring checks before dispatch/commit:

- `python governance/compat/check_dispatch_prompt_envelope.py --base 7ca00450 --head HEAD --enforce`
- `python governance/compat/check_work_order_dispatch_quality.py --base 7ca00450 --head HEAD --enforce`
- `python governance/compat/check_markdown_structural_completeness.py --base 7ca00450 --head HEAD --enforce`
- `python governance/compat/check_agent_operation_trace.py --base 7ca00450 --head HEAD --enforce`
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 7ca00450 --head HEAD`

Required post-commit closure checks (Codex):

- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 7ca00450 --head HEAD`
- `python governance/compat/run_agent_commit_steward_preflight.py --mode closure --base 7ca00450 --head HEAD --enforce`

## Knowledge Absorption Blind-Spot Control Block

- Absorption target: PLCS-T1 matrix checker/template disposition rows and
  PLCS-T2 companion shape definition.
- Prior absorption evidence resolved: PLCS-T1 routing matrix CLOSED; PLCS-T2
  decision packet CLOSED; FPRC-T2 finding propagation standard current.
- Blind spot risk: the companion-block template and checker posture could be
  decided ad-hoc by each C01-C04 registry-edit work order, creating four
  inconsistent enforcement postures at the checker/template layer.
- Mitigation: PLCS-T3 decision packet locks one canonical template and one
  checker disposition before any C01-C04 work order is dispatched.
- Runtime/source authority boundary: no legacy symbol may become a current
  runtime/source fact without future source verification; checker
  implementation requires a separate GC-018.

## Rescan Intelligence Hardening

- Original source artifact: NOT_APPLICABLE_WITH_REASON - this baseline does
  not reopen a corpus rescan or new intake replay.
- Predecessor intake artifact: PLCS-T1 routing matrix and PLCS-T2 decision
  packet (both closed).
- Delta ledger status: NOT_APPLICABLE_WITH_REASON - PLCS-T3 derives from
  already-governed inputs; no new delta ledger.
- Routing matrix status: DO_NOW for the PLCS-T3 decision-and-template packet;
  checker implementation, registry edits, runtime, provider, and public-sync
  are OUT_OF_SCOPE.
- Semantic sampling status: bounded adversarial boundary sample below.
- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

### Original-Intake Delta Ledger

Delta category vocabulary retained for decision boundary:
`UNCHANGED_FROM_INTAKE`, `CHANGED_DISPOSITION`, `NEW_FINDING`, and
`REMOVED_OR_REJECTED`. PLCS-T3 may note changed enforcement posture relative
to PLCS-T1/PLCS-T2 dispositions, but must not claim a fresh rescan delta.

### Follow-Up Routing Matrix

Routing lane vocabulary retained for decision boundary: `DO_NOW`,
`SEPARATE_RUNTIME_TRANCHE`, `STRATEGIC_OPERATOR_DECISION`, `OUT_OF_SCOPE`,
and `RESOLVED_BY_DESIGN`. PLCS-T3 itself is the DO_NOW checker-and-template
decision; actual checker implementation belongs to a separate runtime tranche.

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| PLCS-T3-S1 | Authorized Scope | Checker disposition and template can be decided before checker implementation | DO_NOW bounded decision only | Could this be misread as authorization to wire a checker into the gate chain? | PASS_BOUNDARY - checker implementation and gate wiring are explicitly forbidden; decision packet only records disposition and template. |
| PLCS-T3-S2 | Acceptance Criteria | C05 companion ruling remains deferred | STRATEGIC_OPERATOR_DECISION | Could PLCS-T3 decide C05 since it touches checker posture? | PASS_BOUNDARY - C05 remains DEFERRED_PENDING_FPC_T3_C01; PLCS-T3 does not reopen it. |

## Core Guard Self-Protection Block

This GC-018 baseline authorizes PLCS-T3 decision-and-template packet authoring
plus the bounded B11/B12 authoring-guidance promotion described above. It does
not self-modify GC-018, GC-021, GC-022, GC-023, GC-047, GC-048, GC-049,
GC-050, GC-051, GC-052, or any runtime checker. Any checker implementation
requires a separate GC-018 and operator authorization.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch baseline. No public-sync batch is
authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Claude Code (GC-018 authoring) |
| Provider or surface | Claude Code local workspace |
| Session or invocation | 2026-06-16 PLCS-T3 GC-018 authoring |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | Read, Write, Grep, PowerShell |
| Target paths | `docs/baselines/CVF_GC018_PLCS_T3_COMPANION_ROUTING_CHECKER_TEMPLATE_DECISION_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_PLCS_T3_COMPANION_ROUTING_CHECKER_TEMPLATE_DECISION_FOR_CODEX_2026-06-16.md` |
| Allowed scope source | operator instruction on 2026-06-16; PLCS roadmap PLCS-T3 CANDIDATE_AFTER_T1 |
| Before status evidence | HEAD `7ca00450`; clean worktree |
| After status evidence | pending material commit |
| Diff evidence | `git diff --name-status` before commit |
| Approval boundary | decision-and-template packet dispatch only; no checker/registry/runtime/provider/public mutation |
| Claim boundary | no runtime/provider/live/public/registry/checker-implementation mutation |
| Agent type | Claude Code (GC-018 dispatch authoring); Codex (decision packet owner) |
| Invocation ID | `plcs-t3-gc018-dispatch-authoring-2026-06-16` |
| Expected manifest | `docs/baselines/CVF_GC018_PLCS_T3_COMPANION_ROUTING_CHECKER_TEMPLATE_DECISION_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_PLCS_T3_COMPANION_ROUTING_CHECKER_TEMPLATE_DECISION_FOR_CODEX_2026-06-16.md`; `docs/roadmaps/CVF_PLANE_LAYER_WORKFLOW_CHAIN_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/reference/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_STANDARD_2026-06-16.md`; `docs/reference/CVF_WORK_ORDER_AUTHORING_HARDENING_ADDENDUM_2026-06-11.md` |
| Actual changed set | `docs/baselines/CVF_GC018_PLCS_T3_COMPANION_ROUTING_CHECKER_TEMPLATE_DECISION_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_PLCS_T3_COMPANION_ROUTING_CHECKER_TEMPLATE_DECISION_FOR_CODEX_2026-06-16.md`; `docs/roadmaps/CVF_PLANE_LAYER_WORKFLOW_CHAIN_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/reference/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_STANDARD_2026-06-16.md`; `docs/reference/CVF_WORK_ORDER_AUTHORING_HARDENING_ADDENDUM_2026-06-11.md` |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

This baseline authorizes PLCS-T3 decision-and-template packet authoring and
bounded B11/B12 documentation-only lesson promotion. It does not edit the
interlock registry, implement checkers, wire gate chains, implement runtime,
run live proof, public-sync, or make production/public readiness claims. The
C05 companion ruling remains deferred until FPC-T3-C01 exists.
