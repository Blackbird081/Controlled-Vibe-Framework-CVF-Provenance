# CVF Agent Work Order Template

Memory class: POINTER_RECORD

Status: reusable template for scoped agent execution orders.

## Purpose

A CVF Agent Work Order is the tactical execution packet that an orchestrator,
reviewer, or operator gives to an implementing agent.

It sits below roadmap and governance authorization, and above raw task prompts.
It exists to prevent scope drift by making the worker's mission, authority
chain, write ownership, forbidden actions, evidence requirements, and return
conditions explicit.

Work orders are mandatory after a final roadmap when an orchestrator, reviewer,
operator, or lead agent delegates implementation to another agent or a later
session.

Work orders are governed by the operating workflow in
`docs/reference/CVF_AGENT_EXECUTION_WORKFLOW_SOP_2026-05-19.md`.

## Owner / Source

Owner: CVF orchestration and delegation surface.

Source inputs may include:

- an operator instruction;
- a multi-agent decision pack;
- a roadmap;
- an active handoff;
- a root scratch prompt that needs conversion into a governed artifact.

## Scope / Target / Owner Boundary

Target: one bounded agent execution assignment or one explicitly ordered group
of assignments.

Owner boundary:

- the work order names who dispatches, who implements, who reviews, and when
  the operator must intervene;
- the work order must define owned paths, forbidden paths, and write mode;
- work outside those boundaries requires a new work order or an operator
  correction.

Architecture relationship:

- operator sets business and authority intent;
- orchestrator or CEO role translates final roadmap into one or more work
  orders;
- implementer executes only the current work order;
- reviewer evaluates evidence and blocking defects;
- auditor and governance gates verify structure, taxonomy, and proof.

## Protocol / Contract / Requirements

Protocol:

- cite the authority chain before instructions;
- file required GC-018 baselines before implementation;
- inherit GC-020, GC-023, GC-024, GC-046, GC-047, public/provenance, and live-proof
  rules from the repository;
- make reviewer gate and waiver rules explicit.

Contract:

- the implementer follows the allowed scope and forbidden scope;
- the reviewer evaluates evidence against acceptance criteria;
- the orchestrator receives a closure packet or a stop condition.

## Enforcement / Verification

Verification requirements:

- pre-flight commands must be listed;
- autorun phase gates must be listed and passed before dispatch,
  implementation, closure, and push when applicable;
- existing paths, symbols, role values, template IDs, and policy fields must be
  source-verified before the work order is marked ready;
- work-order authors must verify source facts before dispatch, not delegate
  ambiguous source discovery to the implementer;
- roadmap-derived work orders must include a Roadmap-to-Work-Order Trace Matrix;
- acceptance criteria must be observable;
- fail conditions must be explicit when missing fields, stale source facts,
  ambiguous thresholds, public/provenance boundary errors, or forbidden runtime
  claims would invalidate the task;
- evidence must use command/result/path form where possible;
- completion must record changed files, closure diff status, checklist
  finalization, and required governance updates.
- closure diff evidence must prove the changed files stayed inside Allowed
  scope; archive cleanup, governance maintenance, or unrelated refactors require
  explicit ownership or a separate work order.
- connector wave roadmap closure must use a full-wave changed range, not only
  the final tranche range.
- allowed-scope machine-gate failures must be repaired and rerun by the assigned
  agent; they must not be escalated to the operator as preference questions.
- bounded corpus tasks must include GC-047 manifest, terminal processing
  ledger, reconciliation evidence, exclusions/unreadable accounting, and an
  honest machine-checked completeness verdict.

The work order is invalid for execution if it does not name stop conditions.

## Boundaries / Non-Goals

Non-goals:

- not a replacement for roadmap, GC-018, handoff, or active session state;
- not a way to broaden scope;
- not a public claim artifact;
- not a substitute for live governance proof.

## Claim Boundary

Claim boundary:

- `defined` means the artifact exists as docs/schema;
- `tested` means tests or local verification support the claim;
- `live-proven` requires the repository's live governance proof standard.

Final boundary:

- a work order is closed only when the completion packet or final report records
  evidence, changed files, reviewer disposition, and handoff sync status.

## Relationship To Other Artifacts

The work order does not authorize work by itself.

It must cite an authority chain:

- active session state or operator instruction;
- decision pack, roadmap, or approved review packet;
- lane-specific GC-018 or an explicit instruction that GC-018 must be filed
  before implementation;
- current active handoff and GC-020 requirements.

Use this artifact when a roadmap is too broad for direct implementation and an
agent needs precise marching orders.

Do not use it to bypass:

- GC-018 authorization;
- GC-020 handoff sync;
- GC-023 file-size discipline;
- public/provenance repository boundary;
- live governance proof requirements;
- reviewer gates or operator waivers.

## Required File Naming

Use:

```text
docs/work_orders/CVF_AGENT_WORK_ORDER_<SCOPE>_<YYYY-MM-DD>.md
```

Examples:

```text
docs/work_orders/CVF_AGENT_WORK_ORDER_LANE_B_WORKFLOW_PACKAGING_2026-05-19.md
docs/work_orders/CVF_AGENT_WORK_ORDER_LANE_BCH_2026-05-19.md
```

Root-level scratch prompts are allowed only as temporary intake material. Once a
prompt becomes execution authority for another agent, convert it into a work
order under `docs/work_orders/`.

## Required Structure

Copy and complete the block below.

```text
# CVF Agent Work Order - <Scope>

Memory class: POINTER_RECORD

Status: <DRAFT | READY_FOR_REVIEW | APPROVED_FOR_EXECUTION | CLOSED>

Status token rule:

- `HOLD_*`, `DRAFT`, or `PROPOSED` statuses must not include the token
  `CLOSED`; use `PASS` or `SATISFIED` for prerequisite wording, for example
  `HOLD_UNTIL_T1_PASS`.

## 1. Mission

<One paragraph describing the exact mission. Include what success means.>

## 2. Authority Chain

- Operator instruction: <path or date/time note>
- Active session state: <path>
- Decision pack / review authority: <path>
- Roadmap: <path>
- GC-018 requirement: <already filed path OR must be filed before implementation>
- Active handoff: <path>

Authority boundary:

- This work order does not authorize work outside the cited authority chain.
- If any authority artifact conflicts with this work order, stop and reconcile
  before implementation.

## 3. Agent Roles

- Orchestrator / dispatcher: <agent or operator>
- Implementer: <agent>
- Reviewer: <agent>
- Operator approval required for: <conditions>

## 4. Scope

Allowed scope:

- <allowed action 1>
- <allowed action 2>

Forbidden scope:

- <forbidden action 1>
- <forbidden action 2>

Risk ceiling:

- <R0 | R1 | R2 | R3>

## 5. Required First Reads

Before filing GC-018 or editing files, read:

- <path 1> - why it matters
- <path 2> - why it matters

## 6. Pre-Flight Checks

Commands to run before implementation:

```powershell
git rev-parse --short HEAD
<command 1>
<command 2>
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base <baseHead> --head HEAD
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <baseHead> --head HEAD
python governance/compat/check_work_order_dispatch_quality.py --base <baseHead> --head HEAD --enforce
```

Expected results:

- <expected result 1>
- <expected result 2>

If a pre-flight check fails, stop and record the failed command and result.
The worker must not continue past a failed autorun phase gate.

Mandatory Gate-Failure Remediation Protocol:

- If the failure is inside Allowed scope, repair it and rerun the failed gate.
- Do not ask the operator whether to fix missing `N/A with reason`, stale
  closure residue, source-verification corrections, allowed continuity sync, or
  other routine guard failures.
- Ask the operator only if remediation would exceed Allowed scope, change the
  claim boundary, release a `HOLD_*` prerequisite, change risk level, open
  public-sync, run live/provider proof, consume secrets/quota, touch forbidden
  paths, or perform destructive/irreversible actions.
- Treat any attempted "do you want me to fix this gate failure?" handoff as a
  governance/control-plane learning signal.

## 6A. Source-Fidelity Pass

Before marking this work order ready for execution, verify the source facts the
work order depends on:

Every ready/dispatch work order that names runtime/source facts must include a
Source Verification Block with the required table columns.

```powershell
Test-Path "<existing path named in first reads>"
rg -n "<claimed function/type/templateId/role/policy field>" <source path>
rg -n --fixed-strings "<claimed token>" .
```

Required source-fidelity notes:

- Existing paths verified:
- Planned new paths clearly marked as NEW:
- Canonical role/type values verified from:
- Canonical template or pack IDs verified from:
- Runtime/source facts verified from current source or canonical contract:
- Completion review facts used only when no runtime/source contract exists:
- Draft-only tokens that appear nowhere else in repo:
- Any missing or ambiguous source fact:

If a source fact cannot be verified, either correct the work order or return to
the orchestrator. Do not ask the implementer to discover that the work order
invented a path, symbol, role value, or baseline source.

Source priority:

1. current runtime/source file or schema;
2. canonical reference/contract document;
3. completion review with explicit source trace;
4. handoff/session memory summary only as a pointer, not as source authority.

If a current runtime/source file exists, a completion review alone is not enough
to verify a field, enum, diagnostic class, route state, tool name, or schema key.

If the work order claims a runtime/source capability is absent, not implemented,
hardcoded, per-role only, stale, or missing, include a
Current Runtime Freshness Verification section before dispatch. That section must show the repo searches
or source files that were checked and must cite current owner paths for any
partial implementation surface found.

If a roadmap-derived work order claims complete ACCEPT_AS_OWNER_MAP coverage
from a source audit, include an ACCEPT_AS_OWNER_MAP coverage disposition that
names each accepted concept from the cited audit and marks it as in-scope,
already completed, deferred, rejected, or out-of-scope with reason.

If the work order names, maps, modifies, consumes, or instructs an agent to use
any runtime field, interface, function, type, schema key, receipt field,
diagnostic class, role value, route state, template ID, pack ID, policy enum,
config key, CLI/MCP tool name, or existing source path, include this table
before implementation:

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| <field/type/path/etc.> | <source path> | <line number or canonical section> | <verified field/symbol> | <owner> | <ACCEPT/REJECT/BLOCKED_SOURCE_NOT_FOUND> |

Rules:

- `ACCEPT` requires direct verification from the cited source file or canonical
  contract.
- `REJECT` must name the corrected field/symbol when known.
- `BLOCKED_SOURCE_NOT_FOUND` stops dispatch and returns to Orchestrator.
- A source fact with no file plus line/section is not verified.
- Source Verification row type must be clear in the claimed item or owning
  schema: `EXISTS`, `VALUE_SET`, `LITERAL_INVARIANT`, `RUNTIME_BEHAVIOR`, or
  `DOC_ONLY_NEW`.
- `Verified path or symbol` must contain only the field, path, or symbol being
  verified. Do not put value assignments or type annotations in that cell; use
  `rawMemoryReleased`, not `rawMemoryReleased: false`, and `canReinject`, not
  `canReinject: boolean`.
- For code sources, an `ACCEPT` row must cite a symbol that exists in the cited
  file. Dotted symbols must exist under the cited owner/interface/class; if the
  owner does not contain that field or method, correct the symbol or use
  `REJECT` / `BLOCKED_SOURCE_NOT_FOUND`.
- `LITERAL_INVARIANT` requires the cited source to declare or assign the value
  literally, for example `field: false` or `field = false`.
- If the source type is `boolean`, the worker must not claim "`field=false`
  preserved from source" unless a cited runtime branch or literal source line
  proves that invariant for the specific connector path.
- If the connector requires a safer value than the source globally guarantees,
  mark it as `DOC_ONLY_NEW` or "connector-normalized requirement", not as a
  source-proven invariant.
- If a claimed token appears only in this draft work order, mark it
  `BLOCKED_SOURCE_NOT_FOUND` unless it is explicitly listed as a new doc-only
  field in the table below.
- Newly proposed documentation/connector fields must not be placed in the
  Source Verification Table as if they already exist.
- Do not dispatch implementation with guessed fields, inferred names,
  placeholder paths, stale memory-only vocabulary, or "confirm later" language.
- Forbidden closeout vocabulary for source facts includes `UNVERIFIED`, `TBD`,
  `TODO`, `confirm later`, `confirm field name`, and
  `verify during implementation`. These terms may appear only as a blocking
  defect note, not as an allowed disposition, acceptance criterion, evidence
  requirement, or closure checklist item.

When the work order introduces new documentation-only connector fields, include
this separate table:

| New doc-only field | Purpose | Not sourced from runtime? | Runtime claim blocked? | Validation expectation |
|---|---|---|---|---|
| <field name> | <why it exists> | Yes | Yes | <doc/schema/checklist validation only> |

MA1 section references are locked to the canonical standard at
`docs/reference/CVF_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_STANDARD_2026-05-26.md`.
Do not invent or rename MA1 sections. Use only:

- `## 0. Surface Fidelity Gate`
- `## 1. Authority Chain`
- `## 2. Transfer Objective`
- `## 3. Source Packet`
- `## 4. Role Assignment`
- `## 5. Execution Instructions`
- `## 6. Role Output Schema`
- `## 7. Dissent And Review Ledger`
- `## 8. Integration Decision`
- `## 9. Completion Evidence`
- `## 10. Claim Boundary`

Any alternate MA1 section label, including `Input Package`, `Purpose`, or
`Return Protocol`, is a blocking defect unless the canonical MA1 standard has
been updated first in a separate governed change.

## 6B. Roadmap-To-Work-Order Trace Matrix

If this work order is derived from a roadmap, map every roadmap requirement to
the executable instruction and closure evidence:

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| <requirement> | <section> | <path/field> | <command/check> | <PASS/BLOCKED/N/A with reason> |

Rules:

- every roadmap acceptance item must have a row or explicit `N/A with reason`;
- every required roadmap field must appear in the output artifact or in the
  New Doc-Only Fields table;
- `PASS` is allowed only after the final artifact exists and has been checked;
- missing rows block dispatch or closure.

## 7. Write Ownership

Owned files or modules:

- <path or module>

Forbidden paths:

- <path or module>

Write mode:

- <append-only | create-only | modify-listed>

Any file outside ownership requires an updated work order or operator approval.
If the closure diff shows files outside Allowed scope or ownership, the worker
must stop, split the cleanup into a separate governed batch, or return to the
Orchestrator.

## 8. Execution Plan

Steps must be sequential unless explicitly marked parallel-safe.

1. <step>
2. <step>
3. <step>

Each step must state:

- input artifact;
- output artifact;
- validation command or evidence;
- stop condition.

## 9. Evidence Requirements

Required evidence:

- <command/result/path>
- <test result>
- <catalog path verification, if applicable>

Evidence Trace Block requirements:

- Claim:
- Command:
- Result:
- Key path:
- Verdict:

## 10. Acceptance Criteria

- [ ] <criterion 1>
- [ ] <criterion 2>
- [ ] <criterion 3>

Criteria must be observable through files, commands, tests, or review records.

Fail conditions:

- [ ] <blocking missing field, source mismatch, boundary error, or ambiguous
  threshold condition>
- [ ] <forbidden runtime/public/live-proof claim condition>

Closure is blocked if any fail condition is present.

## 11. Review Gate

Implementation may proceed only after:

- <GC-018 filed and reviewed | operator waiver recorded | other condition>
- `pre-dispatch` autorun gate passed before dispatch
- `pre-implementation` autorun gate passed before material edits

Closure may proceed only after:

- <reviewer no-blocking objection | operator waiver | gate result>
- `pre-closure` autorun gate passed and result recorded

Mandatory remediation rule:

- A gate failure inside this work order's Allowed scope is authorization to
  repair and rerun, not a reason to ask the operator for preference.
- Operator approval is required only for scope expansion, claim-boundary
  changes, `HOLD_*` release, live/provider proof, public-sync, secrets/quota,
  forbidden paths, destructive actions, or higher risk.

Reviewer silence is not approval unless the operator explicitly records a
waiver for this work order.

## 12. Closure Checklist

- [ ] All acceptance criteria satisfied or explicitly marked N/A with reason
- [ ] Required tests or evidence commands run
- [ ] Autorun `pre-closure` gate passed:
  `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base <baseHead> --head HEAD`
- [ ] Closure gate used a non-empty committed diff range; no `--base HEAD --head HEAD`
- [ ] Changed-file set from `git diff --name-status` is inside this work
  order's Allowed scope, or every extra path has explicit operator/work-order
  authorization
- [ ] If this closes a multi-tranche connector wave roadmap, the pre-closure
  range includes all tranche artifacts, not only the final tranche
- [ ] Any line-count threshold or "actual line count" claim is current and
  command-backed
- [ ] Roadmap-to-work-order trace matrix final statuses are PASS or N/A with reason
- [ ] Closure Diff Gate completed: roadmap, work order, final artifact, and
  completion claims were compared
- [ ] Claim Integrity Scan completed with `git diff --name-status`,
  `git status --short`, committed diff output, receipt, command output, or N/A
  evidence for file-change and boundary claims
- [ ] Fail conditions checked and absent, or work returned BLOCKED
- [ ] No open checkbox residue remains in roadmap, work order, completion
  packet, or public-sync checklist
- [ ] No closed work order contains unresolved `HOLD`, `PENDING`, or
  `READY_FOR_DISPATCH` checklist rows or stale dispatch-blocking prose
- [ ] Public catalog updated or explicitly N/A with reason
- [ ] Public/provenance repository boundary checked if public files changed
- [ ] GC-020 handoff updated with current HEAD after commit
- [ ] Post-commit active-session gate passed:
  `python governance/compat/check_active_session_state.py --enforce`
- [ ] Active session front door and state registry updated if mode, next
  allowed move, public-sync status, roadmap status, or handoff status changed
- [ ] Completion packet filed if the roadmap requires one
- [ ] Changed files listed for reviewer
- [ ] No closed-equivalent claim remains if any autorun phase gate failed
- [ ] Any allowed-scope autorun/guard failure was repaired and rerun, not left
  as an operator preference checkpoint

## 13. Return-To-Orchestrator Conditions

Return to orchestrator without continuing if:

- pre-flight fails;
- any autorun phase gate fails outside Allowed scope or cannot be repaired
  inside this work order;
- source-fidelity pass finds a missing path, invented symbol, or unverified
  role/template mapping;
- scope conflict is discovered;
- required citation cannot be found;
- implementation would exceed risk ceiling;
- reviewer raises a structural blocking objection;
- public/provenance boundary is unclear.
```

## Authoring Rules

- Use precise paths, not prose-only references.
- Prefer file:line citations for inventory answers.
- Use planned paths in GC-018 when files do not exist yet; verify existence in
  completion evidence after implementation.
- Keep public claims bounded to evidence level:
  - `defined` for schema/docs only;
  - `tested` for unit or integration evidence;
  - `live-proven` only after required live governance proof.
- Do not include raw API keys, secrets, or private credentials.
- Do not make the work order broader than the authorizing roadmap.

## Minimum Quality Bar

A work order is not ready for execution unless it answers:

- What exactly should be done?
- Why is it authorized?
- Who is implementer and who reviews?
- Which files may be touched?
- Which files or actions are forbidden?
- Which command proves pre-flight readiness?
- Which evidence proves completion?
- What stops the agent from continuing?

## Related Artifacts

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/delegation.contract.ts`
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/agent.handoff.contract.ts`
- `docs/reference/CVF_AGENT_EXECUTION_WORKFLOW_SOP_2026-05-19.md`
- `docs/reference/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md`
- `docs/reference/CVF_GC018_CONTINUATION_CANDIDATE_TEMPLATE.md`
- `governance/toolkit/05_OPERATION/CVF_AGENT_REVIEW_ANTI_COLLUSION_GUARD.md`
- `governance/toolkit/05_OPERATION/CVF_DOCUMENT_STORAGE_GUARD.md`
