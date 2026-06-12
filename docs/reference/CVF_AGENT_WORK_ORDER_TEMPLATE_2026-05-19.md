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
- inherit GC-020, GC-023, GC-024, GC-046, GC-047, GC-048, public/provenance, and live-proof
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
- ready or dispatched work orders must include a Worker Autonomy / No-Question
  Rule so routine allowed-scope remediation is not escalated to the operator.
- allowed-scope machine-gate failures must be repaired and rerun by the assigned
  agent; they must not be escalated to the operator as preference questions.
- self-reported gate evidence must be current before handoff; non-blocked
  artifacts must not record failed required gates and leave rerun/disposition
  to the reviewer or operator.
- delegated runtime/source work must include a Work-Order Fulfillment Manifest
  with required artifacts, forbidden paths, and required proof literals.
- bounded corpus tasks must include GC-047 manifest, terminal processing
  ledger, reconciliation evidence, exclusions/unreadable accounting, and an
  honest machine-checked completeness verdict.
- corpus-derived knowledge maps must include GC-048 source-authority,
  semantic-region, mapped/deferred/unmapped, drift, rebuildability, and
  retrieval-boundary evidence with an honest machine-checked verdict.
- GC-048 machine check:
  `governance/compat/check_corpus_to_knowledge_map_reconciliation.py`.
- governed tranches must follow the commit choreography standard:
  `docs/reference/CVF_TRANCHE_COMMIT_CHOREOGRAPHY_STANDARD_2026-06-03.md`.
- agent-authored text must follow the text encoding and symbol discipline
  standard:
  `docs/reference/CVF_TEXT_ENCODING_AND_SYMBOL_DISCIPLINE_STANDARD_2026-06-07.md`.
- roadmap-derived work must carry forward the roadmap design-control gate:
  scope boundary, non-goals, lane split, dependency/source-verification plan,
  claim boundary, acceptance criteria, verification evidence, and dispatch
  readiness. If the roadmap lacks these controls, the next work order must be
  source-verification, design-audit, or spec work, not implementation.

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

Guard/runtime claim-language discipline:

- do not use `functionally enforced`, `directly enforced`, `already enforced`,
  `runtime enforcement behavior`, or equivalent enforcement-language for a
  guard/policy unless the cited source contains named guard wiring or an
  explicit test assertion that names the guard/policy ID;
- if source behavior exists but is not named as the guard/policy, call it
  `source-visible behavior connection`, `behavior corresponding to guard
  intent`, or `implementation candidate`;
- metadata such as `cvfOwnerExists`, owner paths, registry entries, or policy
  IDs proves owner/registry presence only, not enforcement;
- completion packets must keep this distinction in Purpose, Findings,
  Decision, Claim Boundary, and Finding-To-Governance Learning Disposition.

Text encoding and symbol discipline:

- default to ASCII for agent-authored prose, comments, tests, and governed
  markdown;
- non-ASCII is allowed only under the exceptions in
  `docs/reference/CVF_TEXT_ENCODING_AND_SYMBOL_DISCIPLINE_STANDARD_2026-06-07.md`;
- if changed files retain agent-authored Unicode, the completion packet must
  record the exception and reason.

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
- Parent roadmaps that remain open for later child lanes must not use
  `CLOSED` in the top-level `Status` merely because one child lane passed.
  Use child-lane wording such as `EX_T1_PASS_BOUNDED` in the parent roadmap,
  and reserve `CLOSED_PASS_BOUNDED` for the child work order, completion
  review, or fully closed roadmap.

## 1. Mission

<One paragraph describing the exact mission. Include what success means.>

## 2. Authority Chain

- Operator instruction: <path or date/time note>
- Active session state: <path>
- Decision pack / review authority: <path>
- Roadmap: <path>
- Roadmap design-control gate: <section/path OR N/A with reason>
- Spec / contract / machine-readable semantics: <path OR N/A with reason>
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

- Allowed-scope failures are mandatory remediation. Complete the remediation
  and execute the failed gate again.
- Missing `N/A with reason`, stale closure residue, source-verification
  corrections, allowed continuity sync, and routine guard failures are not
  operator-preference questions.
- Escalation is reserved for remediation that would exceed Allowed scope,
  change the claim boundary, release a `HOLD_*` prerequisite, change risk
  level, open public-sync, run live/provider proof, consume secrets/quota,
  touch forbidden paths, or perform destructive/irreversible actions.
- Any attempted handoff that turns an allowed-scope gate failure into an
  operator preference is a governance/control-plane learning signal.

Staging and checker-source rule:

- Before running `run_local_governance_hook_chain.py`, simulating pre-commit,
  or committing, stage the intended file set with `git add <paths>` so
  staged-index checkers read the current artifact.
- Before staging, working-tree-aware component gates may be used for pending
  worker artifacts; record that status as pending, not clean closure.
- If a checker appears to reject a file that is correct on disk, first verify
  whether the corrected file was staged. Some helpers read the working tree,
  while hook-chain checks may read the staged index.
- Hook-chain failures are cascade layers. Fix the first failing gate, rerun
  that gate directly, then rerun the full applicable autorun or hook chain
  before recording PASS.

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
- Same-token collisions with different meaning:
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

If the work order claims a runtime/source capability is absent, not
implemented, hardcoded, per-role only, stale, missing, or intentionally not
used in the current lane, include a Current Runtime Freshness Verification
section before dispatch. This includes non-use statements such as "no
provider/API key use", "no provider calls", "no runtime/source edits", or "no
registry update" when current runtime/source owners exist. That section must
show the repo searches or source files that were checked and must cite current
owner paths for any partial implementation surface found.

### Negative Search And Collision Discipline

If the work order claims a token, field, enum, schema key, failure token, or
config key is `NOT FOUND`, or uses `BLOCKED_SOURCE_NOT_FOUND`, include a
Negative Search And Collision Discipline section before dispatch. The section
must record exact search roots, exact search command or structured query,
coverage across source, tests, docs, JSON, and external evidence when
applicable, same-token collision results, and the absent-versus-collision
disposition.

If the same token appears elsewhere with a different meaning, do not mark it
`NOT FOUND`. Record the collision or non-authoritative occurrence, cite it,
and explain why it is or is not binding for this work.

If a roadmap-derived work order claims complete ACCEPT_AS_OWNER_MAP coverage
from a source audit, include an ACCEPT_AS_OWNER_MAP coverage disposition that
names each accepted concept from the cited audit and marks it as in-scope,
already completed, deferred, rejected, or out-of-scope with reason.

### Intake Role Routing Decision

Ready or dispatched work orders must include `## Intake Role Routing Decision`
before worker execution. The orchestrator owns this block and must include the
fields required by
`docs/reference/CVF_INTAKE_ROLE_ROUTING_DECISION_STANDARD_2026-06-11.md`;
unresolved routing keeps the work order in `HOLD_*` or `DRAFT`.

### Single-Agent Multi-Role Control Block

If one agent owns implementation plus review/closure roles, include the block required by `docs/reference/CVF_SINGLE_AGENT_MULTI_ROLE_CONTROL_STANDARD_2026-06-11.md`.

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
- Ready/dispatch Authority Chain, Dependency Gate, and Source Verification
  rows must use final checker-accepted dispositions such as `ACCEPT`, `REJECT`,
  or `BLOCKED_SOURCE_NOT_FOUND`. Do not use `REQUIRED` as a disposition in a
  ready/dispatch packet; `REQUIRED` is allowed only in draft/HOLD dependency
  prose or in artifact/proof manifest columns where it is a boolean
  requirement.
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
- If a claimed token appears elsewhere with a different meaning, do not mark
  it `NOT FOUND`; record the collision, cite the occurrence, and explain why
  it is or is not binding for this work.
- Source Verification Table columns are canonical per `docs/reference/CVF_SOURCE_VERIFICATION_TABLE_SHAPE_STANDARD_2026-06-11.md`;
  do not dispatch abbreviated source tables or doc-only fields as verified source facts.
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
`docs/reference/archive/CVF_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_STANDARD_2026-05-26.md`.
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

## 6C. Worker Autonomy / No-Question Rule

The worker proceeds without operator confirmation for non-destructive actions
inside this work order's Allowed scope.

Proceed autonomously with:

- reading files named by this work order;
- running `git status`, `git diff`, `git rev-parse`, manifest/hash checks, and
  listed governance gates;
- documentation format remediation inside Allowed scope;
- required evidence block completion inside Allowed scope;
- repeated guard or autorun execution after allowed-scope remediation.

Escalation is reserved for actions that would exceed Allowed scope, edit legacy
source, edit runtime/source code outside ownership, run live/provider proof, use
secrets/quota, public-sync, push/publish, change risk or claim boundary, release
a `HOLD_*` prerequisite, touch forbidden paths, or perform destructive or
irreversible action.

If a machine gate fails inside Allowed scope, complete the remediation and
execute the gate again. Routine gate remediation is not an operator-preference
checkpoint.

Orchestrator wording hygiene:

- keep any `Operator Checkpoint` section factual and separate from
  gate-remediation instructions;
- do not place operator-preference terms near allowed-scope remediation text;
- prefer `Escalation is reserved for...` over `Ask the operator if...`.

## 6C.1 System Loop Interlock Routing

Include this section when the work order scans, classifies, absorbs, or maps a
corpus, or when it records findings, "not found" claims, negative search
evidence, search/filter readiness, or downstream roadmap candidates.

Required content:

- upstream loop and output artifact;
- downstream loop and input artifact;
- machine-readable registry, finding packet, or intake path;
- routing rule for deferred or blocked findings;
- claim boundary that blocks autonomous mutation.

Minimum scan-routing rule:

- findings must be recorded in the corpus scan registry and a finding packet;
- deferred or blocked findings must include `defectClass`, `learningLane`,
  `nextAction`, and `f2gRef`, `roadmapRef`, or `workOrderRef`;
- a scan report with findings only in prose is not final.

## 6D. Pending Artifact Evidence Finality

If the worker leaves a changed, staged, or untracked governed artifact for
review, the artifact must not claim `git status --short` is clean. It must
record the actual pending status or state that clean-status evidence is
post-commit and command-backed.

Pending artifacts must not cite `--base HEAD~1 --head HEAD` or another
committed-only range as proof for the pending artifact itself. Use
working-tree-aware validation for pending artifacts, or commit first and rerun
the real changed range.

Finality and reviewer-conversion details are extracted to keep this template
reviewable:

`docs/reference/CVF_AGENT_WORK_ORDER_FINALITY_AND_REVIEW_CONVERSION_ADDENDUM_2026-06-12.md`

Work orders that use worker handoff, pending artifacts, prerequisite release, or
reviewer-owned closure must apply these extracted sections:

- Commit Mode And Base-Anchor Lifecycle
- Dependency Release And Next-Work-Order Refresh
- Two-Stage Handoff Finality
- Worker Pending-Return Gate
- Reviewer Closure Conversion Block

## 6E. Self-Reported Gate Evidence Consistency

If the artifact records governance gate results, those results must match the
current handoff state.

Rules:

- if a required gate fails inside Allowed scope, repair and rerun before
  handoff;
- if the failure cannot be repaired inside Allowed scope, set status to
  `BLOCKED` or `HOLD_*` and name the return action;
- do not leave a non-blocked artifact saying a required gate failed while asking
  the reviewer/operator to rerun, decide, or pick it up;
- do not record autorun `PASS` when a required section for that phase is still
  missing, such as `## Finding-To-Governance Learning Disposition` on a
  finding-bearing review;
- if recording `git status --short` for a pending artifact, include the pending
  status line for the artifact itself;
- after rerunning a gate, update the recorded Governance Gates Run result before
  returning the artifact.
- do not treat `FAIL_EXPECTED_PENDING_FINALITY` as a closed-equivalent PASS;
  it is valid only for `WORKER_MUST_NOT_COMMIT` pending review handoff;

## 6E.1 Machine Closure Package

Any work order that scans, classifies, imports, maps, routes, closes, or
hands off governed work must define the machine-readable outputs that turn the
worker result into the next loop's input.

Machine check:

```powershell
python governance/compat/check_machine_closure_package.py --base <baseHead> --head HEAD --enforce
```

Required closure package table:

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/<work-order>.md` | closed-equivalent status, no stale `DISPATCH_READY`, no unchecked required checklist residue, closure anchor policy recorded | `<PASS/BLOCKED/N/A with reason>` |
| Completion or reviewer artifact | `docs/reviews/<completion>.md` or `N/A with reason` | final disposition, changed-file evidence, claim boundary, gate evidence, reviewer-owned closure when `WORKER_MUST_NOT_COMMIT` | `<PASS/BLOCKED/N/A with reason>` |
| Roadmap state | `docs/roadmaps/<roadmap>.md` or `N/A with reason` | tranche row final status, next tranche dependency release state, no stale `READY_WITH_CONDITIONS` residue | `<PASS/BLOCKED/N/A with reason>` |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` or `N/A with reason` | entry id, normalized paths, hashes, verdicts, gap ids, next action | `<PASS/BLOCKED/N/A with reason>` |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` or `N/A with reason` | human quick lookup, negative-search note, next recommendation | `<PASS/BLOCKED/N/A with reason>` |
| External evidence digest | repo-local completion section or digest artifact | external path, schema/version, record count, hash, generated time, privacy boundary | `<PASS/BLOCKED/N/A with reason>` |
| System loop interlock | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_*.json` or `N/A with reason` | upstream output, downstream input, learning/finding route, mutation boundary | `<PASS/BLOCKED/N/A with reason>` |
| Session continuity | `CVF_SESSION_MEMORY.md`, `CVF_SESSION/ACTIVE_SESSION_STATE.json`, active handoff | mode, next allowed move, handoff HEAD or accepted parent marker | `<PASS/BLOCKED/N/A with reason>` |

Rules:

- External workspace paths are evidence inputs, not source-authority rows. Do
  not put `D:\...`, local upload paths, or other non-repo paths in Source
  Verification as if they were canonical source files. Record them in the
  External Evidence Digest with a hash, schema/version, record count, and
  privacy boundary, then cite the repo-local digest or completion section in
  Source Verification if a later work order needs it.
- Corpus work that changes scan, classification, readiness, or gap state must
  update both GC-051 registry surfaces when applicable: the JSON is the
  machine input and the Markdown file is the operator/reviewer lookup. A
  report-only closure is not enough when the registry is the downstream input.
- Machine Closure Package row names and final status tokens must follow
  `docs/reference/CVF_WORK_ORDER_AUTHORING_HARDENING_ADDENDUM_2026-06-11.md`.
- Closed-equivalent artifacts must not retain stale `DISPATCH_READY`,
  `READY_WITH_CONDITIONS`, `NOT_EXECUTED_YET`, `PRE_CLOSURE_NOT_RUN`, or
  placeholder dependency language unless the artifact is explicitly still a
  pending-review worker handoff.
- If findings are recorded, use checker-accepted Finding-To-Governance defect
  classes only. `EVIDENCE_GAP` is not a defect class; use `RULE_GAP`,
  `MACHINE_GATE_GAP`, `ORCHESTRATOR_PACKET_GAP`, or
  `PHASE_GATE_PLACEMENT_GAP` as appropriate. `N/A_WITH_REASON` is a
  disposition, not a defect class.
- The closure package must be updated after final gate reruns, not copied from
  pre-implementation or pending-worker evidence.
- If any roadmap path is cited in Authority Chain, Source Verification,
  Trace Matrix, or closure evidence, the Roadmap state row must name that
  roadmap and its final state. Do not mark Roadmap state `N/A with reason` or
  "no roadmap" when a roadmap path appears anywhere in the artifact.
- Receipt-based PASS claims must include an Acceptance Receipt Assertion
  Matrix. The matrix must compare each required receipt value against the
  observed value from the generated receipt artifact. A query cannot pass if a
  required value and observed value differ, even when the broader answer class
  is correct.
- External evidence from a sibling workspace, local data folder, provider
  receipt, browser artifact, or generated file must include an External
  Artifact Hash Manifest with sha256 for every external artifact used as
  closure evidence. Counts and schemas are not enough by themselves.
- External evidence digest hash rules are defined in
  `docs/reference/CVF_WORK_ORDER_AUTHORING_HARDENING_ADDENDUM_2026-06-11.md`.
- When material closure and session-sync closure use different commits, record
  both ranges. The material range must cover implementation evidence; the
  session-sync range must cover state, memory, and handoff updates. Do not use
  a combined range that includes files outside the work order Allowed scope
  unless the Allowed scope explicitly authorizes those continuity files.

Acceptance Receipt Assertion Matrix template:

| Query ID | Receipt artifact | JSON path | Required value | Observed value | Status |
|---|---|---|---|---|---|
| <AQ-id> | <path or digest section> | <receipt JSON path> | <required> | <observed> | <PASS/BLOCKED> |

External Artifact Hash Manifest template:

| Artifact | Evidence role | sha256 | Generated or verified at | Status |
|---|---|---|---|---|
| <path or redacted path> | <script/receipt/data/etc.> | `sha256:<hex>` | <timestamp/command> | <PASS/BLOCKED> |

## 6F. Commit Choreography

Governed work orders must follow:

`docs/reference/CVF_TRANCHE_COMMIT_CHOREOGRAPHY_STANDARD_2026-06-03.md`

Machine-token quick reference:

| Surface | Required exact tokens / values |
|---|---|
| Core guard-maintenance authorization | `Authorized guard-maintenance scope`, `Protected paths`, `Operator authorization`, `Rollback boundary` |
| Scope firewall authorization | `Allowed paths`, `Forbidden paths`, `Operator authorization`, `Rollback boundary` |
| Commit prompt rule | `Diff scope: PASS`, `Tests: PASS`, `Gates: PASS`, `Untracked unrelated: NONE`, `Forbidden touched paths: NONE` |
| Finding-To-Governance defect classes | `WORKER_EXECUTION_ERROR`, `ORCHESTRATOR_PACKET_GAP`, `RULE_GAP`, `MACHINE_GATE_GAP`, `PHASE_GATE_PLACEMENT_GAP`, `OPERATOR_SCOPE_CLARITY_GAP`, `RUNTIME_SIGNAL_GAP` |
| Finding-To-Governance lanes | `GOVERNANCE_CONTROL_PLANE`, `RUNTIME_BEHAVIOR_LEARNING`, `PROVIDER_OUTPUT_LEARNING`, `COST_ECONOMICS_LEARNING`, `DOCUMENTATION_ONLY_LEARNING` |
| Finding-To-Governance dispositions | `RULE_EXISTS`, `RULE_ADDED`, `MACHINE_CHECK_ADDED`, `MACHINE_CHECK_CANDIDATE`, `PHASE_GATE_PLACEMENT_GAP`, `DESIGN_REVIEW_REQUIRED`, `RUNTIME_LEARNING_CANDIDATE`, `N/A_WITH_REASON`, `TEMPLATE_UPDATED`, `STANDARD_UPDATED`, `STANDARD_ADDED` |
| Source Verification dispositions | `ACCEPT`, `REJECT`, `BLOCKED_SOURCE_NOT_FOUND` |

Notes:

- `N/A_WITH_REASON` is a disposition, not a defect class.
- New governed markdown should use plain checker-matched headings such as
  `## Purpose`; avoid numbered variants like `## 1. Purpose` unless the
  artifact type is already known to allow them.

Required rules:

- check archive hygiene before material tranche edits;
- keep archive cleanup, artifact implementation, closure transition, session
  state sync, and handoff sync in separate commits unless the work order
  explicitly owns the combined scope;
- stage large-scope authorization in the same commit as the large-scope diff;
- capture `executionBaseHead` immediately before worker edits;
- capture `closureBaseHead` immediately before reviewer closure commit;
- expect a dedicated handoff-sync-only commit after material/session commits;
- never use a stale dispatch base as closure proof after intervening commits.
- record component-gate PASS separately from committed-range `pre-closure`
  PASS so a reviewer can see exactly which transition remains.
- for mode/next-move changes, update `CVF_SESSION/ACTIVE_SESSION_STATE.json`,
  `CVF_SESSION_MEMORY.md`, and active handoff context together, then expect a
  dedicated handoff-sync commit for the final HEAD.

### 6F.1 Session / Handoff Commit Protocol

Use this protocol when a closure touches session continuity or active handoff
state:

1. Put `Core Guard Self-Protection Authorization` in the changed governed
   authorization artifact under one of the checker-recognized prefixes:
   `docs/baselines/`, `docs/roadmaps/`, `docs/reviews/`, or
   `docs/work_orders/`.
2. For a protected session/front-door sync commit, the changed root active
   handoff matching `AGENT_HANDOFF*.md` may carry the same authorization block
   if it lists every protected path in the changed range. Archived handoffs do
   not count.
3. Preferred two-commit closure:
   - material/session commit: close the artifact, update session state/front
     door if needed, and include the same-range authorization doc;
   - handoff-only sync commit: update only the active handoff with the material
     commit SHA so `check_active_session_state.py` can accept the parent SHA as
     `parent-present-for-sync-commit`.
4. If the front door or state registry must record the material commit SHA
   itself, use a protected session-sync commit whose changed active handoff or
   docs-prefixed artifact carries same-range authorization.
5. Run committed-range `pre-closure` only after the material/session commit and
   required handoff sync are complete.

## 6F. Near-Threshold Owner Maintainability Plan

If Allowed scope adds or modifies source inside a registered owner domain whose
active entrypoint is within the GC-023 near-hard margin, include this section
before dispatch.

Required content:

- active owner entrypoint path;
- current line count and hard threshold;
- split, extract, rotate, or archive action;
- new helper/barrel/archive path;
- `Minimum shrink target: 50 lines`;
- command-backed post-change line count;
- explicit statement that the owner entrypoint is in Allowed scope and Write
  Ownership.

Do not classify the near-threshold owner entrypoint as forbidden-touch while
adding adjacent source. That is a maintainability bypass, not a split.

## 6G. Work-Order Fulfillment Manifest

For runtime/source implementation work, include these machine-readable tables
before dispatch.

## Required Artifact Manifest

| Path | Required at handoff | Purpose |
|---|---|---|
| <source/test/review path> | Yes | <why this file must exist> |

## Forbidden Path Manifest

| Path | Reason |
|---|---|
| <forbidden path or glob> | <why this path is out of scope> |

## Forbidden Filesystem State At Dispatch

Record the filesystem state of every forbidden path at the moment this work
order is dispatched. The orchestrator must verify each path before dispatch.
A path that exists on disk at dispatch must be explained or cleaned up; the
worker must not be sent into an environment where forbidden files already exist.

This block is verified by `check_forbidden_filesystem_state.py` at the
`pre-implementation` autorun gate phase.

| Forbidden path | Expected state | Actual state at dispatch | Action if PRESENT |
|---|---|---|---|
| <forbidden path> | ABSENT | ABSENT ✓ | N/A |

Rules:

- `ABSENT` — path does not exist on disk (file or directory). Dispatch is safe.
- `PRESENT` — path already exists. Dispatch is blocked until the orchestrator
  either removes the files, opens a governance packet for them, or records an
  explicit operator exemption with reason.
- `PRESENT_EXEMPTED` — path exists; orchestrator has explicitly authorized
  worker to ignore it; worker must not edit, stage, or claim the path.

## Pre-Existing Dirty Path Exemptions

Use only when the repository is already dirty before dispatch and the worker
must ignore, not edit, the path.

| Path | Status at dispatch | Exemption boundary |
|---|---|---|
| <pre-existing dirty path> | <M/A/?? from git status> | <do not edit/stage/claim> |

## Required Proof Manifest

| Proof | Path | Required literal | Required at handoff |
|---|---|---|---|
| <sentinel/invariant/test proof> | <test or source path> | <literal token> | Yes |

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

## 8A. Design Control Carry-Forward

Roadmap-derived work orders must preserve the roadmap design-control gate.

| Design control | Roadmap source | Work-order handling | Verdict |
|---|---|---|---|
| Scope boundary | <section/path> | <how this work order preserves it> | <PASS/BLOCKED/N/A> |
| Non-goals | <section/path> | <how forbidden claims/actions are blocked> | <PASS/BLOCKED/N/A> |
| Lane split | <section/path> | <which lane this work order executes> | <PASS/BLOCKED/N/A> |
| Dependency/source-verification plan | <section/path> | <source checks required before build> | <PASS/BLOCKED/N/A> |
| Claim boundary | <section/path> | <claim boundary inherited here> | <PASS/BLOCKED/N/A> |
| Acceptance criteria | <section/path> | <observable acceptance rows below> | <PASS/BLOCKED/N/A> |
| Verification/evidence | <section/path> | <commands/artifacts required> | <PASS/BLOCKED/N/A> |
| Dispatch-readiness decision | <section/path> | <why this work order may dispatch> | <PASS/BLOCKED/N/A> |

If any required design control is `BLOCKED`, this work order must remain
`DRAFT`, `HOLD_*`, or return to Orchestrator. Do not ask a worker to resolve
roadmap ambiguity during implementation unless this work order is explicitly a
source-verification, design-audit, or spec task.

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

Base-anchor evidence:

- `dispatchBaseHead`:
- `executionBaseHead`:
- `closureBaseHead`: `<post-review commit stage or N/A - pending review>`
- Commit mode: `<WORKER_MAY_COMMIT | WORKER_MUST_NOT_COMMIT>`
- Pending-artifact component gates:
- Worker Pending-Return Gate table:
- Committed-range `pre-closure`: `<PASS after commit | N/A - pending review>`

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

For `WORKER_MUST_NOT_COMMIT` mode, worker handoff is not closure. The reviewer
or committer must approve disposition, commit the reviewed owned diff, and run
the committed-range `pre-closure` gate before changing status to a
closed-equivalent value.

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
- [ ] Commit mode recorded as `WORKER_MAY_COMMIT` or `WORKER_MUST_NOT_COMMIT`
- [ ] `dispatchBaseHead`, `executionBaseHead`, and closure-stage base evidence
  recorded without treating a stale dispatch anchor as current worker proof
- [ ] For `WORKER_MUST_NOT_COMMIT`, pending handoff used a non-closed status,
  recorded actual `git status --short`, and left committed-range
  `pre-closure` to reviewer / committer
- [ ] For `WORKER_MUST_NOT_COMMIT`, Worker Pending-Return Gate results are
  recorded, required component-gate failures inside Allowed scope are repaired,
  and remaining failures are explicitly `BLOCKED`, `N/A with reason`, or
  `FAIL_EXPECTED_PENDING_FINALITY`
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
- `docs/reference/CVF_AGENT_WORK_ORDER_FINALITY_AND_REVIEW_CONVERSION_ADDENDUM_2026-06-12.md`
- `docs/reference/CVF_GC018_CONTINUATION_CANDIDATE_TEMPLATE.md`
- `governance/toolkit/05_OPERATION/CVF_AGENT_REVIEW_ANTI_COLLUSION_GUARD.md`
- `governance/toolkit/05_OPERATION/CVF_DOCUMENT_STORAGE_GUARD.md`
