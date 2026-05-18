# CVF Agent Work Order - Lane B/C/H

Memory class: POINTER_RECORD

Status: DRAFT - derived from root `promt.md` and normalized to CVF Agent Work
Order structure.

## Purpose

Provide one governed Agent Work Order that turns Claude's root `promt.md`
execution prompt into a reviewable, bounded CVF artifact. The file is an
example instance of the new work-order form and a usable dispatch packet for
Lane B/C/H once the required lane gates are satisfied.

This work order is not a review artifact. It is stored under `docs/work_orders/`
because its function is tactical dispatch from final roadmap to implementing
agent.

## Source

Source prompt: root `promt.md`.

Source disposition: useful and materially correct tactical material, but too
prompt-shaped for canonical CVF delegation. It is promoted here into an Agent
Work Order with explicit authority chain, scope boundary, review gate, closure
requirements, and stop conditions.

## Work Order Position

Position: adopt the Agent Work Order pattern for final-roadmap implementation
dispatch.

- `promt.md` contains the right operational detail for agent execution.
- Handoff and active session state remain too general for precise worker
  delegation.
- The root prompt needed taxonomy placement, structural headings, and claim
  boundaries before it could become durable CVF canon.

## Risk Control

Risk: if tactical prompts remain unstandardized, future agents can follow the
right roadmap while still drifting on write scope, reviewer gate, public catalog
boundary, or closure evidence.

Corrective action: use this work order as the first normalized example and use
`docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` for future worker
dispatch packets.

## Decision

Decision: promote the pattern as a reusable CVF Agent Work Order artifact.

Recommendation: keep scratch prompts temporary. Once a prompt is meant to guide
another agent's implementation, convert it into a governed work order under the
`docs/work_orders/` taxonomy folder.

Disposition: Lane B/C/H work should use this normalized work order rather than
root `promt.md` as the agent-facing execution packet. Future final roadmaps
that delegate implementation to another agent or a later session must produce
a work order before implementation begins.

## Owner / Source

Owner: CVF orchestration and delegation surface.

Source:

- root `promt.md`;
- `docs/reference/CVF_AGENT_EXECUTION_WORKFLOW_SOP_2026-05-19.md`;
- `docs/work_orders/CVF_AGENT_WORK_ORDER_AGENT_ROLE_ASSIGNMENT_2026-05-19.md`;
- operator instruction in this session;
- active Lane B/C/H roadmap and decision pack.

## Scope / Target / Owner Boundary

Target: Lane B, then Lane C, then Lane H.

Owner boundary:

- Codex or assigned implementer owns only the active lane at a given time;
- Claude or assigned reviewer owns blocking/no-blocking review;
- operator owns waiver, lane-order changes, and public/provenance ambiguity.

## Protocol / Contract / Requirements

Protocol:

- complete the agent role assignment prerequisite work order before Lane B
  GC-018, unless the operator explicitly waives that prerequisite;
- no implementation before lane-specific GC-018;
- no next lane before prior lane closure;
- no reviewer-silence approval;
- no public catalog edit from the private provenance repo;
- GC-020 handoff sync remains mandatory.

Contract:

- implementer follows the lane write ownership and forbidden scope;
- reviewer checks evidence against acceptance criteria;
- orchestrator pauses on any return-to-orchestrator condition.

## Enforcement / Verification

Verification is through:

- pre-flight commands;
- lane-specific tests;
- Evidence Trace Blocks in closure packets;
- public catalog Test-Path checks when public catalog changes;
- active session state and handoff compatibility gates.

## Boundaries / Non-Goals

Non-goals:

- no Lane D/E/F/G work;
- no global lift of `system_reconvergence_stop`;
- no new governance semantics outside the selected lanes;
- no live-proven claim without live proof;
- no replacement of roadmap, GC-018, or handoff authority.

## Claim Boundary

Claim boundary:

- Lane B may claim schema-defined workflow packs only.
- Lane C may claim CLI execution gateway only after tests and applicable live
  proof.
- Lane H may claim only the proven audit-event memory flow, not full memory
  governance.

Final boundary:

- each lane closes only after acceptance criteria, evidence, review disposition,
  public catalog disposition, and GC-020 status are recorded.

## 1. Mission

Execute the approved three-lane roadmap in strict sequence:

1. Lane B - Workflow Packaging
2. Lane C - Execution Gateway
3. Lane H - Memory Runtime Wiring

Each lane must be separately authorized, implemented, tested, reviewed, and
closed before the next lane begins. This work order translates the roadmap into
agent-facing execution instructions; it does not widen the roadmap.

## 2. Authority Chain

- Operator instruction: 2026-05-19 operator request to implement Lane B, Lane C,
  and Lane H in order.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- Decision pack:
  `docs/reviews/CVF_MULTI_AGENT_DECISION_PACK_REVIEW_CVF_NEXT_PHASE_2026-05-18.md`
- Roadmap:
  `docs/roadmaps/CVF_NEXT_PHASE_ROADMAP_LANE_B_C_H_2026-05-19.md`
- Work order source example: root `promt.md`
- Active handoff: `AGENT_HANDOFF_V9_2026-05-18.md`

Authority boundary:

- GC-018 must be filed before implementation for each lane.
- This work order does not authorize Lane D, E, F, G, broad legacy absorption,
  global stop-lift, or new public claims outside the selected lanes.
- If this work order conflicts with the roadmap, active state, or handoff, stop
  and reconcile before implementation.

## 3. Agent Roles

- Orchestrator / dispatcher: operator and current coordinating agent.
- Implementer: Codex or assigned implementing agent.
- Reviewer: Claude, under the multi-agent review posture.
- Operator approval required for: reviewer waiver, scope expansion, public repo
  ambiguity, or any lane order change.

## 4. Global Execution Rules

Allowed scope:

- File a lane-specific GC-018 before implementation.
- Implement only the current lane.
- Run required tests and evidence commands.
- File a completion packet for each lane.
- Update the public catalog only from the public-sync clone when required.
- Update GC-020 handoff after commits.

Forbidden scope:

- Do not batch two lanes in one implementation step.
- Do not parallelize lanes.
- Do not use `--no-verify`.
- Do not edit the public catalog from the private provenance workspace.
- Do not print or commit raw API keys.
- Do not claim live-proven behavior without required live proof.

Risk ceiling:

- Lane B: R0.
- Lane C: R1.
- Lane H: R1.

## 5. Required First Reads

Before any GC-018 or implementation:

- `docs/reference/CVF_AGENT_EXECUTION_WORKFLOW_SOP_2026-05-19.md` - standard
  roadmap-to-agent operating workflow.
- `docs/work_orders/CVF_AGENT_WORK_ORDER_AGENT_ROLE_ASSIGNMENT_2026-05-19.md`
  - pre-lane role assignment and delegation prerequisite.
- `docs/reference/CVF_AGENT_ROLE_ASSIGNMENT_MATRIX_2026-05-19.md` - role
  ownership matrix for operator, orchestrator, planner, implementer, reviewer,
  auditor, and specialist workers.
- `docs/reference/CVF_AGENT_DELEGATION_AND_SUBAGENT_BOUNDARY_STANDARD_2026-05-19.md`
  - bounded delegation and subagent boundary standard.
- `CVF_SESSION_MEMORY.md` - session front door and active routing.
- `CVF_SESSION/ACTIVE_SESSION_STATE.json` - current mode and selected lanes.
- `AGENT_HANDOFF_V9_2026-05-18.md` - active handoff and GC-020 posture.
- `docs/roadmaps/CVF_NEXT_PHASE_ROADMAP_LANE_B_C_H_2026-05-19.md` -
  governing roadmap.
- `docs/reference/CVF_GC018_CONTINUATION_CANDIDATE_TEMPLATE.md` - GC-018
  required structure and closure checklist.
- `governance/compat/CVF_GOVERNED_FILE_SIZE_EXCEPTION_REGISTRY.json` -
  GC-023 file-size exception registry.

## 6. Global Pre-Flight Checks

Run before filing the first lane GC-018:

```powershell
python governance/compat/check_active_session_state.py --enforce
python governance/compat/check_markdown_structural_completeness.py
python governance/compat/check_docs_governance_compat.py
git status --short
```

Expected result:

- active session state is compliant;
- Markdown/doc governance gates pass;
- any unrelated working-tree changes are identified and not overwritten.

## 7. Commit And Handoff Discipline

Each lane should use separate commits for:

- GC-018 baseline;
- implementation;
- tests or evidence updates, if separated by repo practice;
- completion packet;
- GC-020 handoff sync.

After each commit, update the active handoff according to GC-020 and commit that
handoff update separately.

## 8. Lane B - Workflow Packaging

### Scope

Create governed workflow capability pack files for exactly three existing
templates. Lane B is docs/schema only and must not change runtime behavior.

### Required Pre-Flight

```powershell
Test-Path "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates.ts"
rg -n "app_builder|business|content|category|id:" "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates.ts"
```

### GC-018 Requirements

Before implementation, file:

```text
docs/baselines/CVF_GC018_LANE_B_WORKFLOW_PACKAGING_2026-05-19.md
```

The GC-018 must record:

- exact selected template IDs;
- planned governed-pack paths;
- R0 risk statement;
- explicit no-runtime-change boundary;
- acceptance criteria;
- Tranche Closure Checklist.

Use planned paths in GC-018. Verify actual path existence in completion evidence
after implementation.

### Write Ownership

Owned path:

```text
EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/<template-id>/
```

Forbidden paths:

```text
EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts
```

Write mode: create-only, plus public catalog update in public-sync after lane
closure.

### Build

For each selected template, create:

```text
workflow.spec.md
execution.policy.json
receipt.schema.json
```

`workflow.spec.md` must describe:

- template ID;
- role binding;
- governed-by statement;
- intake;
- workflow steps;
- output;
- evidence.

`execution.policy.json` must include:

- `templateId`;
- `requiredRole`;
- `minimumPermission`;
- `dlpEnabled`;
- `quotaEnabled`;
- `providerLane`;
- `receiptRequired`;
- `guardPolicyRef`.

`receipt.schema.json` must use JSON Schema draft 2020-12 and include:

- `templateId`;
- `role`;
- `stepTraces`;
- `providerLane`;
- `dlpResult`;
- `quotaResult`;
- `issuedAt`.

### Acceptance Criteria

- [x] Exactly 3 templates have all 3 pack files.
- [x] No runtime code is added or modified during Lane B.
- [x] New pack paths exist and are cited in completion evidence.
- [x] Public catalog row says workflow capability packs are defined or
      schema-packaged, not live-proven.
- [ ] GC-020 handoff is updated after commit.

## 9. Lane C - Execution Gateway

### Scope

Add a minimal `cvf execute` CLI surface that calls the existing governed
`/api/execute` route. The CLI is a caller, not a replacement runtime.

### Required Pre-Flight

```powershell
Test-Path "EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI"
rg -n "commander|Commander|program\\.command|yargs|cac" "EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src"
rg -n "export async function|POST|NextRequest|session|DASHSCOPE|request\\.json" "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts"
```

### GC-018 Requirements

Before implementation, file:

```text
docs/baselines/CVF_GC018_LANE_C_EXECUTION_GATEWAY_2026-05-19.md
```

The GC-018 must answer all six inventory questions with file:line citations:

1. Invocation model.
2. Auth/session model.
3. Env/key loading.
4. Input schema.
5. Receipt output.
6. Error and timeout behavior.

### Write Ownership

Preferred owned path:

```text
EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/
```

Alternative path if justified in GC-018:

```text
EXTENSIONS/CVF_CLI_EXECUTE/
```

Forbidden scope:

- no governance logic changes in `execute/route.ts`;
- no new auth system;
- no `cvf trace`, `cvf run`, or `cvf debug`;
- no live provider call in CI without provider key gate.

### Build

Minimum command:

```text
cvf execute --template <id> --role <role> [--input <json>] [--endpoint <url>] [--verbose]
```

Expected behavior:

- POST to `<endpoint>/api/execute`;
- pass the documented auth mechanism;
- print governance receipt JSON to stdout;
- print verbose step traces to stderr only when `--verbose` is set;
- return non-zero exit codes on failure.

### Tests

- Unit: mock HTTP receipt returns valid JSON on stdout.
- Unit: missing `--template` exits 1 and prints usage.
- Integration: skipped by default unless a running CVF server and provider key
  gate are available.

### Acceptance Criteria

- [x] `cvf execute --help` shows usage.
- [x] Missing required flags fail with exit 1.
- [x] Mock HTTP unit test passes.
- [ ] Live acceptance proof is recorded only when a running CVF server and key
      gate are available.
- [x] No secrets are printed.
- [x] Public catalog updates CLI row with bounded wording.
- [ ] GC-020 handoff is updated after commit.

## 10. Lane H - Memory Runtime Wiring

### Scope

Wire exactly one memory-related flow: governance audit event persistence
receipt. This must remain post-response or otherwise prove no provider prompt
reinjection occurs.

### Required Pre-Flight

```powershell
Test-Path "EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/index.ts"
Test-Path "EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts"
rg -n "MemoryTierOwner|MemoryReinjectionPolicy" "EXTENSIONS/CVF_GUARD_CONTRACT/src"
rg -n "audit|receipt|governance" "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts"
```

### GC-018 Requirements

Before implementation, file:

```text
docs/baselines/CVF_GC018_LANE_H_MEMORY_RUNTIME_WIRING_2026-05-19.md
```

The GC-018 must answer all seven inventory questions with file:line citations:

1. Audit event location.
2. Storage owner.
3. Persistence boundary.
4. Retention policy.
5. Contamination boundary.
6. Receipt shape.
7. Live proof requirement.

If the audit event cannot be proven post-response or non-reinjected, stop and
return to orchestrator.

### Write Ownership

Candidate owned paths, subject to GC-018 inventory:

```text
EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/
EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/
EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts
```

Write mode: modify-listed only.

Forbidden scope:

- no provider prompt reinjection;
- no multi-flow memory;
- no breaking contract signature changes;
- no full memory governance claim;
- no deletion or replacement of existing audit mechanisms.

### Build

Define `AuditMemoryReceipt` with:

- `eventType: "governance_audit"`;
- `sessionId`;
- `templateId`;
- `role`;
- `tier: "audit"`;
- `retentionPolicy`;
- `reinjectionAllowed: false`;
- `persistedAt`;
- optional `storageRef`.

Wire receipt emission only after existing governance receipt construction and
without adding the audit receipt to provider prompts.

### Tests

- Unit: audit event classifies to audit tier.
- Unit: reinjection policy denies audit tier.
- Unit: audit receipt helper emits valid receipt.
- Integration: execute flow exposes or records the audit memory receipt.

### Acceptance Criteria

- [x] Audit event maps to session-tier audit memory receipt capture.
- [x] Reinjection remains false.
- [x] Execute flow emits or records `AuditMemoryReceipt`.
- [x] Audit memory data is not present in provider prompt.
- [x] Required tests pass.
- [x] Public catalog wording is bounded to the proven audit-event flow.
- [ ] GC-020 handoff is updated after commit.

## 11. Review Gate

For each lane:

- File GC-018.
- Get explicit Claude no-blocking review, or explicit operator waiver for that
  lane.
- Implement only after the review gate is satisfied.
- Pause on structural blocking objection.

Reviewer silence is not approval.

## 12. Completion Requirements

Each lane closure packet must include:

- Evidence Trace Block for significant claims;
- acceptance criteria checklist;
- changed files;
- test commands and results;
- public catalog update or explicit N/A;
- public-sync `git remote -v` result if public catalog changed;
- GC-020 handoff record.

After all three lanes complete, file:

```text
docs/reviews/CVF_LANE_BCH_FULL_CLOSURE_2026-05-19.md
```

## 13. Return-To-Orchestrator Conditions

Stop and return to orchestrator if:

- active session state no longer lists `operator_lane_selection_active`;
- GC-018 inventory cannot find required file:line evidence;
- required pre-flight path is absent;
- implementation would touch forbidden paths;
- public/provenance repo boundary is unclear;
- live proof is required but no live key/server gate is available;
- reviewer raises a structural blocking objection.

## Related Artifacts

- `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`
- `docs/reference/CVF_AGENT_EXECUTION_WORKFLOW_SOP_2026-05-19.md`
- `promt.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V9_2026-05-18.md`
- `docs/reviews/CVF_MULTI_AGENT_DECISION_PACK_REVIEW_CVF_NEXT_PHASE_2026-05-18.md`
- `docs/roadmaps/CVF_NEXT_PHASE_ROADMAP_LANE_B_C_H_2026-05-19.md`
- `docs/reference/CVF_GC018_CONTINUATION_CANDIDATE_TEMPLATE.md`
