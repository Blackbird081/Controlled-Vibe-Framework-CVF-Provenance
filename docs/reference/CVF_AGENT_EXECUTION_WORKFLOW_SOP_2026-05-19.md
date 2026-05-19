# CVF Agent Execution Workflow SOP

Memory class: POINTER_RECORD

Status: canonical operating workflow for roadmap-to-agent execution.

## Purpose

This SOP defines the standard operating workflow for CVF when a strategic
decision, final roadmap, or operator lane selection must become implementation
work.

It closes the missing layer between high-level governance artifacts and actual
agent execution. In company terms, this is the operating procedure that turns
strategy into accountable work orders, evidence, review, and closure.

## Scope

This SOP applies when any of the following happens:

- a final roadmap assigns implementation to an agent or later session;
- an operator selects one or more lanes for execution;
- an orchestrator or CEO-style agent delegates work to implementers;
- a reviewer asks another agent to perform scoped remediation;
- a task touches runtime, public claims, catalog rows, governance proofs,
  handoff state, or cross-agent coordination.

This SOP does not replace GC-018, GC-020, handoff, active session state,
roadmaps, decision packs, or reviewer records. It defines how those artifacts
flow together.

## Owner Surface / Source Lineage

Owner surface: CVF orchestration and delegation layer.

Canonical sources:

- `docs/CVF_ARCHITECTURE_DECISIONS.md` - architecture decisions and ADR-047.
- `docs/reviews/CVF_17_05_GOVERNANCE_KERNEL_OWNER_MAP_2026-05-17.md` -
  records the orchestrator/worker-lane gap.
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/delegation.contract.ts` -
  typed delegation ownership contract.
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/agent.handoff.contract.ts` -
  typed handoff bridge.
- `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` - tactical
  work order form.

## Protocol / Contract / Requirements

The mandatory operating chain is:

```text
Operator / CEO intent
  -> Intake or review packet
  -> Decision pack when multiple agents or disputed scope are involved
  -> Final roadmap
  -> Agent Work Order
  -> Lane-specific GC-018 when implementation scope opens
  -> Implementation
  -> Evidence and tests
  -> Reviewer disposition
  -> Completion packet
  -> Catalog update when applicable
  -> GC-020 handoff sync
```

Requirement 1: final roadmap is not enough for delegated execution. If another
agent or later session must implement the work, an Agent Work Order is required
before implementation begins.

Requirement 2: work orders cannot authorize scope. They must cite the
authorizing session state, roadmap, decision pack, operator instruction, and
GC-018 requirement.

Requirement 3: implementers execute only the active work order. If a discovery
suggests a better path, the implementer returns to the orchestrator instead of
silently widening scope.

Requirement 4: reviewers review against the work order, not against memory or
informal intent.

Requirement 5: closure is not complete until evidence, review disposition,
catalog status when applicable, and handoff sync are recorded.

## Inputs And Outputs

Input artifacts:

- operator instruction or active session decision;
- decision pack or review packet;
- final roadmap;
- active session state;
- active handoff;
- relevant prior-art inventory;
- GC-018 baseline template when implementation opens.

Output artifacts:

- Agent Work Order under `docs/work_orders/`;
- lane-specific GC-018 baseline when required;
- implementation changes;
- test or live-proof evidence;
- completion packet;
- public catalog update or explicit N/A;
- GC-020 handoff sync.

## Role Workflow

### Operator / CEO Intent

The operator sets business intent, lane selection, waivers, and final authority
when agents disagree or when public/provenance ambiguity appears.

The operator does not need to write implementation detail. That detail belongs
in the Agent Work Order.

### Orchestrator

The orchestrator converts final roadmap intent into work orders.

Responsibilities:

- choose the next active lane or task;
- ensure authority chain is cited;
- define write ownership and forbidden scope;
- define stop conditions;
- ensure pre-flight checks are present;
- assign implementer and reviewer;
- prevent parallel work unless explicitly authorized.

### Planner

The planner may decompose work into steps, but the decomposition must land in
the work order or GC-018. Planner notes are advisory until captured in a
governed artifact.

### Implementer

The implementer executes the current work order only.

Responsibilities:

- read required first-read artifacts;
- run pre-flight commands;
- file GC-018 before implementation when required;
- touch only owned files/modules;
- run evidence commands and tests;
- stop on return-to-orchestrator conditions.

### Reviewer

The reviewer checks whether the implementer satisfied the work order and
whether evidence supports the claim.

Reviewer silence is not approval unless an operator waiver is explicitly
recorded.

### Auditor / Governance Gates

Automated and manual governance gates validate naming, taxonomy, structural
completeness, session state, public/provenance boundary, and proof discipline.

## Standard Workflow

### Step 0 - Intake

Trigger:

- operator request;
- review finding;
- roadmap continuation;
- multi-agent disagreement;
- system gap.

Output:

- issue statement or review packet;
- explicit decision whether a decision pack is needed.

### Step 1 - Decision Pack

Use when:

- multiple agents disagree;
- scope could widen;
- claims need counter-evidence;
- operator must choose among lanes.

Output:

- accepted decision pack;
- selected lane or hold decision.

### Step 2 - Final Roadmap

The roadmap defines strategic scope, order, non-goals, and acceptance at lane
level.

Output:

- final roadmap path;
- lane order;
- claim boundary.

### Step 3 - Agent Work Order

The work order translates the roadmap into executable instructions.

Minimum content:

- mission;
- authority chain;
- agent roles;
- allowed and forbidden scope;
- required first reads;
- pre-flight commands;
- write ownership;
- execution plan;
- evidence requirements;
- acceptance criteria;
- review gate;
- closure checklist;
- return-to-orchestrator conditions.

Output:

- `docs/work_orders/CVF_AGENT_WORK_ORDER_<SCOPE>_<DATE>.md`.

### Step 4 - GC-018 Authorization

Use before implementation when the lane opens new implementation scope,
runtime behavior, public claim posture, or meaningful proof work.

Output:

- `docs/baselines/CVF_GC018_<SCOPE>_<DATE>.md`.

### Step 5 - Implementation

Implementation follows only the current work order and GC-018.

Output:

- scoped file changes;
- no unrelated cleanup unless required by the work order.

### Step 6 - Evidence

Evidence must be proportional to the claim:

- docs/schema work: path existence and structural checks;
- unit/integration work: focused tests;
- governance behavior: live proof when repository rules require it;
- public claim: public-sync catalog evidence and source path verification.

### Step 7 - Review

Reviewer checks:

- scope adherence;
- forbidden-path compliance;
- test/proof adequacy;
- claim wording;
- catalog/handoff completeness.

Output:

- no-blocking disposition, required correction, or operator arbitration.

### Step 8 - Closure

Closure records:

- acceptance criteria;
- changed files;
- evidence commands/results;
- reviewer disposition;
- catalog update or N/A;
- GC-020 handoff sync.

## Enforcement / Verification

Mandatory local gates for workflow artifacts:

```powershell
python governance/compat/check_docs_governance_compat.py
python governance/compat/check_markdown_structural_completeness.py
python governance/compat/check_active_session_state.py --enforce
```

Additional gates depend on the work order:

- GC-023 line-count/file-size checks before modifying large files;
- unit or integration tests for implementation lanes;
- `python scripts/run_cvf_release_gate_bundle.py --json` for release-quality
  governance behavior claims;
- public-sync `git remote -v` before public catalog edits.

## GitHub Push Workflow Chain

GitHub push is a governed delivery chain, not a raw `git push` action.

Required sequence:

```text
Confirm repository boundary
  -> Review worktree scope
  -> Run/update archive hygiene when docs churn occurred
  -> Run pre-commit hook chain or equivalent targeted guards
  -> Commit with scoped message
  -> Sync active handoff HEAD block when GC-020 requires it
  -> Run full pre-push hook chain
  -> Verify remote target before push
  -> Push only from the correct repository
  -> Record post-push status or handoff update when needed
```

Push chain requirements:

- provenance workspace pushes must stay private/provenance only;
- public-facing docs, catalog, README, release, contributor, or setup changes
  must be prepared from the public-sync clone after `git remote -v`;
- `.githooks/pre-commit` and `.githooks/pre-push` are the canonical local hook
  entrypoints and both route through
  `governance/compat/run_local_governance_hook_chain.py`;
- docs archive cleanup must use `scripts/cvf_active_archive.py`; never delete
  historical docs by hand;
- archive-link rewrites are mechanical hygiene updates and must not force
  retro-validation of legacy archived records;
- canonical retained docs referenced by active guards must be protected through
  permanent path allowlists, not restored ad hoc after every archive run;
- after a commit, the active handoff must contain the current HEAD SHA before
  pre-push may pass;
- any failing hook is treated as a broken workflow link until classified as
  true violation, historical false-positive, or guard-scope bug.

Minimum push evidence for a governed batch:

```powershell
git remote -v
git status --short
python governance/compat/run_local_governance_hook_chain.py --hook pre-push
```

## Boundaries / Non-Goals

This SOP does not:

- authorize implementation without GC-018 when GC-018 is required;
- replace active session state;
- replace handoff;
- replace decision packs;
- make reviewer silence an approval signal;
- allow public catalog edits from the private provenance repository;
- create new runtime role semantics by itself.

This SOP standardizes operating workflow. Runtime enforcement of every role
remains subject to future scoped implementation work.

## Failure Modes And Required Action

| Failure mode | Required action |
|---|---|
| Final roadmap exists but no work order | Stop before implementation and create work order. |
| Work order lacks authority chain | Stop and add authority chain. |
| Implementer needs to touch forbidden path | Return to orchestrator. |
| Reviewer is silent | Wait or get explicit operator waiver. |
| Public/provenance boundary unclear | Stop and run `git remote -v` in the relevant workspace. |
| Evidence cannot support claim | Downgrade claim or add required proof. |
| GC-018 inventory cannot cite source lines | Pause lane; file correction or design-only note. |

## Related Artifacts

- `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_LANE_BCH_2026-05-19.md`
- `docs/CVF_ARCHITECTURE_DECISIONS.md#adr-047-agent-work-orders-become-the-mandatory-tactical-dispatch-layer`
- `docs/reference/CVF_GC018_CONTINUATION_CANDIDATE_TEMPLATE.md`
- `docs/reference/CVF_SESSION_GOVERNANCE_BOOTSTRAP.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V9_2026-05-18.md`

## Claim Boundary

This SOP creates a governed operating workflow standard. It does not prove that
every runtime actor is technically enforced in the live product. Claims about
runtime actor enforcement, live execution identity, or full memory governance
still require separate scoped implementation and evidence.
