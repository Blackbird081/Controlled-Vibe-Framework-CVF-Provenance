# CVF Agent Instructions

## Session Memory Front Door

The active session front door for new or resumed agents is:

`CVF_SESSION_MEMORY.md`

Read continuity surfaces progressively, not the full state/history aggregate
by default: (1) read the bootstrap read model first for compact current
facts (current mode, active handoff, next allowed move):

`CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`

(2) read the compact front door above and the current active handoff named
by the state registry; (3) read only the current-authority paths those two
surfaces name for the current task; (4) resolve the full machine-readable
state registry only as a targeted lookup, when a current fact is missing,
contradictory, or the task explicitly requires historical evidence:

`CVF_SESSION/ACTIVE_SESSION_STATE.json`

Canonical standard for these budgets and their exact-hash migration debt:
`docs/reference/CVF_ACTIVE_CONTINUITY_READ_BUDGET_STANDARD_2026-08-10.md`.
Machine guard: `governance/compat/check_active_session_state.py`. Some
current Core surfaces still exceed the canonical budgets in that standard as
exact-hash tracked migration debt in
`governance/compat/CVF_ACTIVE_CONTINUITY_READ_BUDGET_MIGRATION.json`; that
debt cannot grow and does not license reading full history by default.

The current active handoff in that registry is:

`AGENT_HANDOFF_V57_2026-08-10.md`

Historical handoffs are archived under:

`CVF_SESSION/handoffs/archive/`

This includes `CVF_SESSION/handoffs/archive/AGENT_HANDOFF.md`, V2-V30, and
side-channel handoff files. Do not append new status to archived handoffs;
update the active handoff named by `CVF_SESSION/ACTIVE_SESSION_STATE.json` or
open a later versioned handoff when the active handoff approaches the limit.
After opening a successor handoff, startup front doors and routing docs must
reference only the active handoff by bare filename. Superseded handoffs may
appear only as archive-qualified paths under `CVF_SESSION/handoffs/archive/`.

## Mandatory Startup Acknowledgment - 2026-05-26

Before material governed work in any new or resumed session, the agent must
read `CVF_SESSION_MEMORY.md` and its bootstrap read model, identify the
active handoff those surfaces name, and resolve the full state registry only
as a targeted lookup when a current fact above is missing or contradictory.

The agent must then state to the operator or record in the active handoff/session
state one concise acknowledgment naming:

- current mode;
- active handoff;
- next allowed move;
- any parked operator checkpoint.

When the operator asks to create or refresh a local CVF Workspace from a fresh
provenance clone, use `Initialize-CVF-Operator-Workspace.ps1` as the autorun
entrypoint and preserve interactive profile selection unless the operator has
already selected an exact path and profile.

Suggested format:

`Startup acknowledged: current mode=<mode>; active handoff=<handoff>; next allowed move=<summary>; parked checkpoint=<none|summary>.`

This is a soft-accountability requirement, not proof of runtime auto-load,
universal tool support, MCP availability, or hidden cross-agent memory transfer.
Trivial direct answers may keep the confirmation internal, but any roadmap,
implementation, review, live run, commit, handoff, or public-sync work must
satisfy this acknowledgment first.

## Guard Orientation Index - 2026-06-20

Before authoring any governed CVF artifact, read
`docs/reference/guard_orientation/README.md` to identify which guard surfaces
apply to the current task class and role, what blocks or outputs are required,
and what common failure patterns to avoid.

This applies to all roles: dispatcher, worker, reviewer, closer, and
session-sync steward. The index is an orientation layer only; canonical
standards, work orders, and machine checkers still control.

## Mandatory Provider-Specific Agent Memory Boundary - 2026-06-13

Provider-specific files and memory stores are execution aids for the agent or
provider that owns them. They are not CVF source of truth and must not be cited
as canonical CVF authority in Source Authority tables, Source Verification
ACCEPT rows, corpus manifests, closure proof, or roadmap/work-order evidence.

Examples include `CLAUDE.md`, Codex memory files, Claude memory files, IDE
side-channel summaries, provider-local memories, and other agent-private
continuity mechanisms.

Canonical CVF continuity and authority must come from CVF-governed surfaces:

- `AGENTS.md`;
- `CVF_SESSION_MEMORY.md`;
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`;
- the active handoff named by the state registry;
- canonical standards under `docs/reference/`;
- governed roadmaps, baselines, work orders, reviews, registries, checkers, and
  runtime source.

Provider-specific files may be read as local operating guidance for that agent
only. Any source fact learned from them must be re-verified against a
CVF-governed surface before it is used as evidence or dispatched to another
agent. If no CVF-governed source exists, mark the claim
`BLOCKED_SOURCE_NOT_FOUND`, `DOCUMENTATION_ONLY_WITH_REASON`, or
`NOT_CVF_SOURCE` instead of promoting the provider-specific file to authority.

## Mandatory F-1 Diminishing Returns Stop Rule - 2026-05-15

Final F-1 status: `closed: not met, evidence-backed`. This rule is agent-enforced; do not claim output-quality parity, do not continue broad F-1 prompt/template/model/token-budget tuning, do not increase the DeepSeek `3072` token cap, do not reintroduce runtime two-pass expansion, and do not rerun full EVT-4 hoping reviewer variance closes the gap. Reopening broad F-1 work requires fresh explicit human authorization and a new review/roadmap packet.

Canonical owners: stop-rule packet `docs/reviews/CVF_F1_DIMINISHING_RETURNS_STOP_RULE_2026-05-15.md`; closure packet `docs/reviews/CVF_F1_OUTPUT_QUALITY_PARITY_CLOSURE_NOT_MET_2026-05-15.md`; bounded value claim `docs/reviews/CVF_EVT4_BOUNDED_VALUE_CLAIM_2026-05-15.md`; successor roadmap `docs/roadmaps/CVF_NONCODER_OUTPUT_QUALITY_HARDENING_ROADMAP_2026-05-15.md`. Future output-quality work proceeds through that roadmap as product-level non-coder hardening, not F-1 parity tuning.

## Mandatory Public Export Disposition Guard - 2026-05-30

Canonical standard:

`docs/reference/CVF_PUBLIC_EXPORT_DISPOSITION_STANDARD_2026-05-30.md`

Machine guard:

`governance/compat/check_public_export_disposition.py`

Any changed closed roadmap, final wave completion packet, public-sync batch, or
public catalog claim must include a `Public Export Disposition` section with
exactly one of:

- `EXPORTED`
- `DEFERRED_PRIVATE_ONLY`
- `BLOCKED_MISSING_PUBLIC_ARTIFACTS`

`EXPORTED` requires public-sync remote, commit, and artifact path evidence.
Private provenance closure is not public catalog export. If public-sync lacks
matching artifacts/source, the artifact must say `DEFERRED_PRIVATE_ONLY` or
`BLOCKED_MISSING_PUBLIC_ARTIFACTS` and name the next action before any public
README/catalog claim is made.

## Critical Repository Boundary - 2026-05-09

Rotated under the Governed File Size Guard (GC-023) to:

`docs/reference/CVF_AGENTS_CRITICAL_REPOSITORY_BOUNDARY_2026-06-23.md`

Read that file before any push, public-sync work, or repository-boundary
decision. Summary: this workspace is the private provenance repository;
public-facing changes must go through the sibling public-sync clone; run
`git remote -v` before any push intended for the public repository.

## UI / Web Design Contract

For any UI, frontend, web app, redesign, dashboard, landing page, or visual
handoff work, read the root `DESIGN.md` before implementation. Treat
`DESIGN.md` as the canonical CVF visual contract.

Use external design repos, Claude Design prototypes, screenshots, and copied
HTML only as reference material. Absorb patterns into CVF language; do not
copy a third-party brand identity or override CVF's design contract.

## Mandatory Live Governance Proof

Any test, roadmap closure, release gate, demo proof, or public claim that asserts CVF governance behavior must use a real provider API call.

This includes claims about risk classification, approval flow, phase gates, DLP filtering, bypass detection, output validation, provider routing, audit trail updates, or CVF controlling AI/agent behavior for non-coders.

Mock mode is allowed only for pure UI structure checks such as navigation, routing, static badges, layout, and RBAC pages that do not assert AI governance behavior.

Required command for release-quality proof:

```bash
python scripts/run_cvf_release_gate_bundle.py --json
```

This command must include live governance E2E and must fail if no DashScope-compatible live key is available. `DASHSCOPE_API_KEY` is accepted directly; `ALIBABA_API_KEY`, `CVF_ALIBABA_API_KEY`, and `CVF_BENCHMARK_ALIBABA_KEY` are accepted aliases. `--e2e` is a targeted UI-only mock check and is not a substitute for governance proof.

Never commit or print raw API key values. Use operator-supplied environment variables such as `DASHSCOPE_API_KEY`, `ALIBABA_API_KEY`, and `DEEPSEEK_API_KEY`.

Operator-key continuity note: in this provenance workspace, operator-supplied
live keys may already exist in
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/.env.local`. Future agents must
check/load that file before claiming no live key is available. Do not print raw
values, do not copy that file into the public-sync repository, and only pass the
values through process environment for live proof commands.

## Mandatory Live Run Diagnostics - 2026-05-24

Canonical standard:

`docs/reference/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`

Any AI/agent that runs a live provider/API-key/service-token/CLI/MCP/browser
proof must classify failures before rerunning. A failed, partial, timed-out,
empty-output, or rerun-triggering live run must record a secret-safe diagnostic
with stage, class, retryability, user action, provider/model when known, HTTP
status/latency when available, receipt/trace when available, and a safe
human-readable message.

Do not consume more live quota by repeating the same unclear test until the
previous failure has a diagnostic or an explicit reason why diagnostic capture
was impossible.

Benchmark evidence that emits multiple events per live call must report both
the call-level result and the event-model denominator so readers do not confuse
event ratios with execution pass rate.

## Mandatory ADIF Defect Registry Disclosure - 2026-06-23

CVF accumulates recurring agent-defect patterns (gate-trap quirks,
dispatch-quality requirements, role-boundary rules) as governed entries
under `docs/reference/agent_defect_intelligence/entries/`, queryable
through the read-only resolver `governance/compat/run_adif_defect_resolver.py`.
A pattern recorded only in one provider's session memory is invisible to
every other agent and every future session; it is the registry, not any
single agent's memory, that all agents share.

Any GC-018 baseline or work order an agent files must include an
`## ADIF Defect Registry Disclosure` section: query the resolver for this
dispatch's own task class, role, and lifecycle phase, then list every
returned defectId. `governance/compat/check_adif_defect_registry_disclosure.py`
(wired into the pre-dispatch and pre-implementation autorun phases) blocks
dispatch if this section is missing, the query line is missing, or any
defectId the resolver actually returns is omitted from the disclosed list.

If a reviewer or worker observes a new repeated or non-obvious defect
pattern while executing a tranche, add a new entry to the ADIF registry
(following `docs/reference/agent_defect_intelligence/CVF_ADIF_ENTRY_TEMPLATE.md`)
before closing that tranche, rather than recording the lesson only in
provider-specific memory (`CVF_ADIF-0008` names this exact anti-pattern).

## Mandatory Value-Parked Lane Reopen Discipline - 2026-06-25

Canonical standard:

`docs/reference/CVF_VALUE_PARKED_LANE_REOPEN_DISCIPLINE_STANDARD_2026-06-25.md`

A lane declined for low expected value (not blocked by a missing
authority/credential/dependency) needs a concrete, checkable reopen
condition recorded in `nextAllowedMove`, not a vague restatement. No agent
may re-propose such a lane without first checking that condition.

## Mandatory Work Order Source Verification - 2026-05-27

Canonical work-order template:

`docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`

Any future CVF work order that names, maps, modifies, consumes, or instructs an
agent to use a runtime field, interface, function, type, schema key, receipt
field, diagnostic class, role value, route state, template ID, pack ID, policy
enum, config key, CLI/MCP tool name, or existing source path must include a
Source Verification Block before implementation.

Required Source Verification Table columns:

- `Claimed item`
- `Source file`
- `Verified line/section`
- `Verified path or symbol`
- `Owning interface/function/schema`
- `Disposition`

Allowed dispositions are `ACCEPT`, `REJECT`, or `BLOCKED_SOURCE_NOT_FOUND`.
`ACCEPT` requires direct verification from the cited source file or canonical
contract. `REJECT` must name the corrected field/symbol when known.
`BLOCKED_SOURCE_NOT_FOUND` stops the work order and returns it to Orchestrator.

Work-order authors must run a pre-dispatch source-fidelity pass before assigning
implementation:

- cite source file plus line, symbol, or canonical section for every source fact;
- prefer current runtime source or canonical contract over completion reviews,
  handoffs, or memory summaries when a runtime/source file exists;
- search the repo for each named token/field/class/enum/tool/section label; if
  the term appears only in the draft work order, dispatch is blocked unless it
  is explicitly listed as a new doc-only field in a separate "New Doc-Only
  Fields" table;
- do not put newly proposed connector/documentation fields in the Source
  Verification Table as if they already exist in runtime/source;
- source-verify any MA1 section reference against
  `docs/reference/CVF_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_STANDARD_2026-05-26.md`
  using the canonical section names: `## 0. Surface Fidelity Gate`, `## 1.
  Authority Chain`, `## 2. Transfer Objective`, `## 3. Source Packet`, `## 4.
  Role Assignment`, `## 5. Execution Instructions`, `## 6. Role Output Schema`,
  `## 7. Dissent And Review Ledger`, `## 8. Integration Decision`, `## 9.
  Completion Evidence`, and `## 10. Claim Boundary`.

No future agent may close a work order with guessed fields, inferred names,
placeholder source paths, stale memory-only vocabulary, or "confirm later"
language for a runtime/source contract. If a work order author is unsure, the
work order must assign a source-verification task to the orchestrator/reviewer
before dispatching implementation.

Forbidden closeout vocabulary for applicable source facts includes
`UNVERIFIED`, `TBD`, `TODO`, `confirm later`, `confirm field name`,
`verify during implementation`, `inferred`, `stale-memory`, `placeholder`,
`assume`, and `to be confirmed`. These terms may appear only inside an explicit
defect note that blocks dispatch. They must not appear in acceptance criteria,
evidence requirements, completion reviews, or closure checklists as if they were
allowed dispositions.

## Governed Artifact Literal-Format Gotchas - 2026-06-25

Before drafting a GC-018, work order, worker-return, or completion review,
read:

`docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`

It is a pre-write checklist of literal-format failure modes already hit by
`governance/compat/check_*.py` gates (self-recomputed line numbers,
word-wrapped multi-word terms, trailing punctuation after verdict tokens,
bare directory-path substrings, heading-collision false matches, ADIF
disclosure query exactness, and more). Reading it before writing avoids
discovering these one gate-run at a time. Any new literal-format trap found
while authoring an artifact should be added there in the same batch.

## Mandatory Work Order Closure Quality Gate - 2026-05-28

Canonical standard:

`docs/reference/CVF_WORK_ORDER_CLOSURE_QUALITY_GATE_STANDARD_2026-05-28.md`

Any future CVF work order, roadmap task, completion review, public-sync batch,
or delegated agent execution must satisfy the closure-quality gate before it is
marked `CLOSED`, `CLOSED_PASS`, `CLOSED_PASS_BOUNDED`, or equivalent.

Binding requirements:

- include a Roadmap-to-Work-Order Trace Matrix for work derived from a roadmap;
- run a Closure Diff Gate comparing roadmap requirements, work-order
  instructions, final artifacts, and completion claims;
- back file-change and no-runtime/no-public/no-live-proof claims with
  `git diff --name-status`, `git status --short`, committed diff output,
  receipts, command output, or explicit `N/A with reason`;
- include explicit fail conditions for missing fields, ambiguous thresholds,
  stale source facts, public/provenance boundary errors, and forbidden runtime
  claims;
- resolve every closure checklist item as checked, `N/A with reason`, or
  `BLOCKED` with return-to-orchestrator action;
- closed-equivalent artifacts must not retain `| OPEN |` rows, unchecked
  `- [ ]` checklist items, stale roadmap `WORK_ORDER_READY`/`HOLD until`
  residue, or Fast Lane `ACTIVE` status paired with pass/approve disposition;
- update active session front door, machine-readable state, and active handoff
  when current mode, next allowed move, public-sync status, roadmap status, or
  handoff status changes.

Open checkbox residue, stale continuity state, memory-based file-change claims,
and roadmap requirements lost between dispatch and final artifact are closure
defects. Operator silence is not a waiver.

## Mandatory Roadmap Closure Freshness Guard - 2026-06-18

Stable front door:

`docs/reference/roadmap_closure_freshness/README.md`

Canonical standard:

`docs/reference/roadmap_closure_freshness/CVF_ROADMAP_CLOSURE_FRESHNESS_STANDARD.md`

Machine guard:

`governance/compat/check_roadmap_closure_freshness.py`

Any agent that changes a roadmap top-of-file `Status:` line, edits a roadmap
`## Machine Closure Package`, closes or reopens a roadmap tranche, or updates a
roadmap self-reference must keep same-file roadmap closure state
self-consistent.

If a changed active roadmap's `Machine Closure Package` `Roadmap state` row
refers to the same roadmap file, the row's cited `Status:` value must match the
actual top-of-file `Status:` value exactly. Do not retype closure status from
provider memory, chat history, or a previous packet; copy it from the roadmap's
current top `Status:` line after the closure/status decision is made.

This guard is mandatory in reviewer-fast, pre-commit, pre-push, and autorun
workflow gates. It is intentionally range-aware and forward-only: archived or
unchanged historical roadmaps are not reopened solely for this rule.

## Mandatory Work Order Dependency Release Evidence - 2026-06-03

Canonical standard:

`docs/reference/CVF_WORK_ORDER_DEPENDENCY_RELEASE_EVIDENCE_STANDARD_2026-06-03.md`

Any future work order, roadmap task, dispatch packet, or tranche sequence that
is blocked by a prior tranche, closure review, registry update, artifact, live
proof, or operator checkpoint must not move from `HOLD_*`, `DRAFT`,
`PROPOSED`, or prerequisite-bound status into `READY`, `DISPATCH_READY`,
`DISPATCHED`, or equivalent execution status until dependency-release evidence
is refreshed.

Before dispatch, replace placeholder dependency rows such as
`Disposition: REQUIRED`, `after closure`, `after Tn closure`, or
`pending prior tranche` with artifact path, closure commit, final disposition,
and refreshed base anchors. Rerun dispatch-quality and pre-dispatch autorun
gates on the release range. A worker agent must not be asked to infer which
prior artifact satisfied a HOLD dependency from chat history or stale prose.

`governance/compat/check_work_order_dispatch_quality.py` enforces this for
ready/dispatch-equivalent work orders. If the dependency cannot be source-backed,
keep the packet in `HOLD_*`, `DRAFT`, or `BLOCKED` and return it to the
orchestrator.

Hard enforcement:

- `governance/compat/check_work_order_dispatch_quality.py` is mandatory in the
  local hook chain and CI documentation workflow.
- Agent autorun gates must use a real changed range. Capture `baseHead` with
  `git rev-parse --short HEAD` before implementation and run closure/push gates
  as `--base <baseHead> --head HEAD`; `--base HEAD --head HEAD` is not valid
  closure evidence for changed governed artifacts.
- Any work order, connector roadmap, or Fast Lane audit that is marked
  `DISPATCHED`, `FAST_LANE_READY`, `READY`, `CLOSED`, `CLOSED_PASS`, or an
  equivalent execution/closure status must satisfy the machine gate before the
  agent may proceed.
- A future connector wave may not be marked ready/dispatch unless the matching
  fresh GC-018 baseline exists.
- A Source Verification `ACCEPT` row must cite an existing source file or a
  canonical-contract marker, and value rows must include the source-declared
  values they claim.
- Source Verification `Verified path or symbol` cells must contain only the
  field/path/symbol being verified, not a value assignment or type annotation.
  Use `rawMemoryReleased`, not `rawMemoryReleased: false`; use `canReinject`,
  not `canReinject: boolean`.
- Source Verification must distinguish `EXISTS`, `VALUE_SET`,
  `LITERAL_INVARIANT`, `RUNTIME_BEHAVIOR`, and `DOC_ONLY_NEW`. A false
  invariant such as `canReinject=false` may be source-claimed only when the
  cited source line literally declares/assigns false or the cited runtime path
  proves that connector-specific invariant. A `boolean` field alone is not a
  false-invariant proof.
- Roadmap-derived work orders must include the Roadmap-to-Work-Order Trace
  Matrix before ready/dispatch.
- Conditional prerequisites such as `CLOSED_PASS` must keep the artifact in a
  `HOLD_*`, `DRAFT`, or `PROPOSED` status until the prerequisite evidence
  exists and has been checked.
- `HOLD_*`, `DRAFT`, or `PROPOSED` status labels must not contain the token
  `CLOSED`; use `PASS` or `SATISFIED` prerequisite wording such as
  `HOLD_UNTIL_T1_PASS`.
- Single-work-order closure ranges must stay inside that work order's Allowed
  scope. Archive cleanup, baseline movement, governance maintenance, or
  unrelated refactors require explicit ownership or a separate governed batch.
- A closed multi-tranche LHW connector roadmap must be validated with a full
  wave range that includes T1, T2, and T3 artifacts; a final-tranche-only range
  is not closure evidence for the whole wave.
- Connector spec line-count and "actual line count" claims must match the
  current file and be command-backed or machine-verifiable.

## Mandatory Governed File Maintainability Planning - 2026-05-28

Canonical guard:

`governance/toolkit/05_OPERATION/CVF_GOVERNED_FILE_SIZE_GUARD.md`

Any agent that touches a governed source, test, frontend, active markdown,
front-door, or handoff file near its hard line-count threshold must rotate,
archive, split, or meaningfully reduce that file in the same batch.

Binding requirements:

- do not compress prose merely to fit under the hard threshold;
- front doors such as `CVF_SESSION_MEMORY.md` must remain compact pointer
  records, with long history moved to versioned archives;
- active handoffs must open a successor handoff when they approach threshold
  instead of accumulating indefinite continuity text;
- feature work touching near-threshold source/test/frontend files must extract
  a same-domain module/component/test file or shrink the touched file
  materially;
- `governance/compat/check_governed_file_size.py --enforce` must pass before
  claiming the work is ready, closed, or safe for tester review.

The guard now hard-fails touched near-hard-threshold governed files without
same-domain rotation/split evidence or meaningful shrink. Maintainability
planning is part of the work, not cleanup left for testers.

## Mandatory Text Encoding And Symbol Discipline - 2026-06-07

Canonical standard:

`docs/reference/CVF_TEXT_ENCODING_AND_SYMBOL_DISCIPLINE_STANDARD_2026-06-07.md`

Agent-authored source comments, tests, governed markdown, work orders,
completion packets, handoffs, registries, and public-sync summaries must
default to ASCII. Non-ASCII is allowed only for explicit exceptions such as
existing file convention, user-facing language requirements, protocol/data
contracts, existing Unicode filenames, or evidence quotes.

Do not introduce smart punctuation, decorative bullets, Unicode arrows,
non-breaking spaces, zero-width characters, or invisible control characters
unless the changed artifact records the exception and reason. Do not perform
broad Unicode normalization outside the assigned scope.

## Mandatory JSON Generated Aggregate Discipline - 2026-06-12

Canonical standard:

`docs/reference/CVF_JSON_GENERATED_AGGREGATE_DISCIPLINE_STANDARD_2026-06-12.md`

Large governed JSON aggregates that are repeatedly edited by agents should not
remain hand-edited monoliths. Once a generated source layout exists, agents must
edit the compact source files and run the matching generator instead of editing
only the aggregate.

Current generated JSON aggregates:

- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`
  - source: `docs/corpus-intelligence/registry/`
  - generator: `governance/compat/generate_corpus_scan_registry.py`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
  - source: `CVF_SESSION/state/`
  - generator: `governance/compat/generate_active_session_state.py`
- `CVF_SESSION/agent_workspace/ACTIVE_AGENT_WORKSPACE_STATE.json`
  - source: `CVF_SESSION/agent_workspace/state/`
  - generator: `governance/compat/generate_agent_workspace_state.py`

Changed generated aggregates must pass their drift check before dispatch,
closure, or commit. A future large governed JSON aggregate must record whether
it added, reused, or explicitly did not need a generated source layout.

## Mandatory Agent Autorun Workflow Control - 2026-05-28

Canonical standard (read this for the full rule set, phase-gate commands,
remediation policy, and commit steward usage):

`docs/reference/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md`

Agent-neutral commit steward standard:

`docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md`

Agent-error learning philosophy:

`docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md`

Any agent-led CVF workflow that drafts, dispatches, implements, reviews,
closes, commits, pushes, or public-syncs governed work must run the matching
`run_agent_autorun_workflow_gate.py` phase (`pre-dispatch`,
`pre-implementation`, `pre-closure`, `pre-push`) before that step, and use
`run_agent_commit_steward_preflight.py` before any governed commit or
worker-return handoff. A failed gate blocks the claim - mark the artifact
`DRAFT`/`HOLD_*`/`BLOCKED` instead of writing a handwritten PASS.
Allowed-scope gate failures must be repaired and rerun by the assigned
agent, not escalated to the operator as a preference question. Pre-closure
must not accept untracked/unresolved worktree changes as clean closure.
Latest-closure continuity is mandatory: `nextAllowedMove`,
`CVF_SESSION_MEMORY.md`, and the active handoff must all reference the same
latest closed `LHWN` wave.

## Mandatory Agent Handoff Boundary Contract Guard - 2026-06-17

Stable front door:

`docs/reference/agent_handoff/README.md`

Canonical machine-check standard:

`docs/reference/agent_handoff/CVF_AGENT_HANDOFF_BOUNDARY_MACHINE_CHECK_STANDARD.md`

Machine guard:

`governance/compat/check_agent_handoff_boundary.py`

The ratified Agent Handoff Contract is the Central Core for all governed
handoff semantics:

`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

Any changed governed work order that uses agent handoff semantics, including
`dispatchBaseHead`, `executionBaseHead`, `closureBaseHead`,
`WORKER_MAY_COMMIT`, `WORKER_MUST_NOT_COMMIT`, multi-agent role routing,
reviewer closure conversion, AOT trace scope, commit ownership, session-sync,
or next-move surface updates, must include an
`Agent Handoff Contract Control Block`.

The block must select exactly one canonical route token, name the `rolePattern`,
state the phase/base-head/changed-set/trace/commit-owner dispositions, record
cross-batch isolation, and state how next-move surfaces are handled.

`WORKER_MUST_NOT_COMMIT` work orders must also include
`Reviewer Closure Conversion` with `completionReviewPath` and
`reviewerOwnedClosurePaths`. Three-or-more-agent chains must designate one
closer before dispatch.

This guard is mandatory in the autorun workflow and local hook chain. It does
not replace the AOT trace guard, commit steward, or next-move freshness guard;
it binds their local views back to the ratified handoff Central Core.

## Mandatory Agent Interaction Workspace Design Boundary - 2026-06-17

Stable front door:

`docs/reference/agent_workspace/README.md`

Canonical design standard:

`docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`

Canonical state topology contract:

`docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md`

Canonical state lane taxonomy:

`docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_LANE_TAXONOMY.md`

Canonical state item template:

`docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_ITEM_TEMPLATE.json`

Machine guard:

`governance/compat/check_agent_workspace_design.py`

Any future task that proposes, analyzes, designs, builds, or modifies a
dedicated Claude/Codex/other-agent interaction workspace must read the stable
agent workspace front door before implementation.

The AHB-Tn.1 design foundation is not workspace build authorization. A future
workspace build, runtime state file, UI, queue, provider proof, public-sync, or
registry edit requires fresh GC-018, a separate work order, Agent Handoff
Contract Control Block evidence, and an Agent Workspace Design Control Block.

The workspace design guard is mandatory in the autorun workflow and local hook
chain. Changed workspace work orders must explicitly account for workspace
purpose, contract source, front door, storage class, handoff fields, state
ownership, guard owner, and build boundary before dispatch or closure.

Future workspace state, generated workspace state, workspace queues, inboxes,
review lanes, dashboards, or runtime work must also cite the state topology
contract and map proposed records to its required state fields before
implementation.

Stable workspace foundation rules live under `docs/reference/agent_workspace/`.
Dated GC-018 packets, work orders, reviews, and evidence remain in their normal
execution folders. Do not use provider-local memory, chat history, or an
unindexed folder as the source of truth for workspace design.

## Mandatory Agent Workspace State Generated Aggregate Guard - 2026-06-17

Generated workspace state aggregate:

`CVF_SESSION/agent_workspace/ACTIVE_AGENT_WORKSPACE_STATE.json`

Generated source layout:

`CVF_SESSION/agent_workspace/state/`

Generator:

`governance/compat/generate_agent_workspace_state.py`

Machine guard:

`governance/compat/check_agent_workspace_state.py`

Any future task that changes the agent workspace generated state must edit the
source fragments under `CVF_SESSION/agent_workspace/state/` and run the
generator. Direct aggregate-only edits are drift defects.

The generated workspace state is a compact governed state view, not a chat log,
provider-local memory store, runtime queue, UI, public surface, or production
claim. Items must map to the required fields in
`docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md`,
the lane vocabulary in
`docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_LANE_TAXONOMY.md`,
and the source shape in
`docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_ITEM_TEMPLATE.json`.

The agent workspace state guard is mandatory in the autorun workflow and local
hook chain. It checks drift, required state fields, source/front-door pointers,
and hook binding. A future workspace build, runtime queue, provider proof,
public-sync, registry edit, or generated-state expansion still requires fresh
GC-018 and a separate work order.

## Mandatory Agent Workspace Skeleton Guard - 2026-06-17

Bounded local workspace skeleton:

`CVF_SESSION/agent_workspace/workspace/README.md`

Lane index:

`CVF_SESSION/agent_workspace/workspace/lanes/README.md`

Machine guard:

`governance/compat/check_agent_workspace_skeleton.py`

The workspace skeleton is a repo-local governance coordination surface. It is
not a runtime queue, scheduler, UI, provider route, public-sync surface,
registry entry, production claim, or public readiness claim.

Any future task that modifies the local workspace skeleton, lane folders, lane
index, or workspace front doors must keep the skeleton bound to the stable
agent workspace reference front door, lane taxonomy, generated workspace state,
and machine guard. Agents must not create active work by dropping ad hoc files
into lane folders; active workspace state remains governed by source fragments
under `CVF_SESSION/agent_workspace/state/` plus the generator and checker.

The agent workspace skeleton guard is mandatory in the autorun workflow and
local hook chain. Future runtime/build expansion beyond this skeleton requires
fresh GC-018 and a source-verified work order.

## Mandatory Agent Workspace Runtime Boundary Guard - 2026-06-17

Stable front door:

`docs/reference/agent_workspace/README.md`

Canonical runtime expansion readiness contract:

`docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_RUNTIME_EXPANSION_READINESS_CONTRACT.md`

Bounded runtime queue skeleton:

`CVF_SESSION/agent_workspace/runtime_queue/README.md`

Operator-facing read model plan:

`docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPERATOR_VIEW_PLAN.md`

Machine guard:

`governance/compat/check_agent_workspace_runtime_boundary.py`

The runtime queue skeleton is `QUEUE_SKELETON_ONLY`. It is not an executable
queue, scheduler, worker daemon, provider route, UI, public-sync surface,
registry edit, production claim, or public readiness claim.

Any future task that proposes or modifies workspace runtime queues, queue
records, operator views, dashboards, provider proof, public-sync, registries,
or runtime execution must read the runtime expansion readiness contract and
include a Runtime Expansion Control Block. Queue skeleton and read-model work
must preserve the no-runtime/no-provider/no-public/no-registry boundary unless
a fresh GC-018 explicitly authorizes the wider mode.

The agent workspace runtime boundary guard is mandatory in the autorun workflow
and local hook chain. It binds the runtime-readiness contract, queue skeleton,
operator view plan, AGENTS.md, and hook placement so agents cannot silently
promote workspace folders into runtime behavior.

## Mandatory IDE Extension Multi-Provider Execution Log Guard - 2026-05-29

Canonical standard:

`docs/reference/CVF_IDE_EXTENSION_MULTI_PROVIDER_EXECUTION_LOG_STANDARD_2026-05-29.md`

Machine guard:

`governance/compat/check_multi_provider_execution_log.py`

Any agent-led batch that uses more than one provider, VS Code extension tab,
Antigravity session, browser agent, direct provider script, CLI, MCP client, or
other external execution surface must produce or update a bounded session log
when it closes governed work, compares provider effectiveness, or makes
quality/cost claims.

The log must identify provider/model, role, invocation surface, evidence basis,
commit range, changed files, known findings, direct-provider-proof boundary,
and cost/quality attribution. It must include an `Execution Attribution Block`
that separates roadmap/order author, worker/executor, reviewer/closer,
provider/model, execution surface, evidence basis, and attribution boundary.
Operator-reported hidden IDE or Antigravity history must be labeled as
operator-reported; CVF may trust only artifacts, diffs, receipts, tests, and
explicit operator reports.

Governance hook PASS, `CLOSED_PASS`, or `CLOSED_PASS_BOUNDED` is not by itself
proof of code design quality, provider output quality, governed-route behavior,
public readiness, production readiness, or cost optimization.

Scripts that call provider APIs directly may be claimed only as provider-method
capability proof unless they also pass through the governed CVF route or the
mandatory live governance proof release gate.

Autorun and local hook chains must run this guard. A missing provider/model,
execution surface, evidence basis, commit range, Execution Attribution Block,
quality finding disposition, cost boundary, or direct-provider-proof boundary
blocks governed closure.

## Mandatory Finding-To-Governance Learning Trigger Guard - 2026-05-29

Canonical standard:

`docs/reference/CVF_FINDING_TO_GOVERNANCE_LEARNING_TRIGGER_STANDARD.md`

Machine guard:

`governance/compat/check_finding_to_governance_learning.py`

Any changed CVF log, review, assessment, or audit that records findings, known
issues, quality findings, defects, or post-run problems must include a
`Finding-To-Governance Learning Disposition` section. The disposition must
classify the defect, learning lane, escalation state, and next control action.

Allowed learning lanes include governance/control-plane learning,
runtime-behavior learning, provider-output learning, cost/economics learning,
and documentation-only learning. A finding may close as `N/A with reason`, but
it must not close as worker blame without saying whether CVF rule, guard, phase
placement, runtime signal capture, or operator scope clarity also failed.

Any repeated, future-agent, reusable, systemic, rule/template, guard,
phase-gate, orchestration, or machine-check finding must be promoted into a
reusable CVF control when feasible: `RULE_ADDED`, `TEMPLATE_UPDATED`,
`STANDARD_ADDED`, `STANDARD_UPDATED`, `MACHINE_CHECK_ADDED`, or
`MACHINE_CHECK_CANDIDATE`. This is the default CVF learning rule: fix once,
reuse many times. Documentation-only closure is valid only with explicit
`N/A_WITH_REASON` explaining why promotion is unsafe, impossible, or out of
scope.

Autorun and local hook chains must run this guard. A finding-bearing artifact
without learning disposition blocks governed closure.

## Mandatory Learning Signal Intake Bridge - 2026-05-29

Canonical standard:

`docs/reference/CVF_LEARNING_SIGNAL_INTAKE_BRIDGE_STANDARD_2026-05-29.md`

Owner implementation:

`EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/learning-signal-intake-bridge.ts`

Runtime/provider/cost learning candidates, phase-gate placement gaps, design
review candidates, and machine-check candidates must be normalized into a
`LearningSignalIntakeRecord` before a follow-up roadmap claims Learning Plane
routing. The bridge emits `LearningFeedbackInput` for the existing feedback
ledger and keeps `autonomousMutationAuthorized=false`.

This is a bounded intake bridge only. It does not authorize autonomous rule
mutation, runtime behavior mutation, provider prompt changes, memory
reinjection, model tuning, public readiness, or production readiness.

## Mandatory External Repository Absorption Entry Rule - 2026-07-11

Machine guard (extends ADIF-0014, no second checker created):

`governance/compat/check_absorption_blindspot_control_presence.py`

Before authoring, editing, or dispatching a governed work order, GC-018
baseline, or completion review that references a `.private_reference/legacy/`,
`.private_reference/external_repos/`, or `.private_reference/source_mirrors/`
absorption source path, or that uses bounded explicit intake language such as
"external repository absorption", "copied folder absorption", or the
canonical "external repo or copied folder" phrase, the agent must declare
R85-style entry evidence in a `## External Repository Absorption Entry
Control` block before absorption planning proceeds. R85's terminal-ledger
discipline is the model:
`docs/reference/CVF_MSEA_R85_GOP_Y_CVF_SOURCE_RECONCILIATION_MATRIX_2026-07-10.md`.

The block must name: source type, upstream/source-mirror disposition,
enumeration/manifest plan, per-file terminal-ledger plan, owner/overlap
route, value-disposition route, and claim boundary. Check
`.private_reference/source_mirrors/INDEX.md` for an existing pinned mirror
before treating a derived external-agent pack as source authority.

The block may be replaced by an allowed `NOT_APPLICABLE_WITH_REASON` /
`SKIPPED_WITH_REASON` disposition, matching the existing two ADIF-0014
blocks, or by the narrow `COMPARISON_ONLY_NO_ABSORPTION` disposition when the
artifact cites an external source purely for side-by-side wording comparison
and makes no absorption, adaptation, or import claim. Generic bare words such
as `repo` are forbidden triggers; only exact source paths or the bounded
multi-word intake phrases above may activate this rule.

This rule does not create a second absorption mechanism, checker, or
registry. It extends the same ADIF-0014 presence checker that already
requires the Mandatory Blind-Spot Control Block and Corpus Completeness And
Report Integrity headings, so pre-dispatch entry recognition happens before
an absorption artifact exists, not only after.

## Mandatory Knowledge Absorption Blind-Spot Prevention - 2026-06-01

Canonical standard:

`docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md`

Any AI/agent that absorbs, reopens, scopes, or implements knowledge from
`.private_reference/legacy/`, archived absorption packets, external capability
sources, Review-CVF pain points, memory, graph, workflow, CLI/MCP/tool,
provider, benchmark, context, or non-coder outcome surfaces must complete the
Knowledge Absorption Blind-Spot Control Block before implementation.

Every future `GC-018` packet touching memory, graph, or intelligence work must
include that Control Block. A missing block makes the packet incomplete and
implementation must not be dispatched.

Do not scope from active summaries alone. Resolve prior absorption evidence,
read detailed source files when present, normalize accepted value into existing
CVF owner surfaces, record accept/defer/reject dispositions, run adversarial
role review, and close with a blind-spot delta. If the block is `PARTIAL` or
`BLOCKED`, the implementation must stop or explicitly record why the remaining
blind spot is low-risk and out of scope.

For LHW connector waves, scope rejection must not be misread as source
rejection. A family that is excluded only because the current wave is
documentation-only must be labeled:

`rejected from this LHW wave (doc-only scope) - requires live route; eligible for separate live-proof roadmap post-LHW.`

Do not blame a worker agent for not running live proof when the work order
scoped a doc-only LHW wave. `abtop` and `gridex` may have API/key paths and may
be eligible for later live testing; they are still the wrong scope for a
doc-only connector wave. Finish LHW absorption of remaining
`PARTIALLY_ABSORBED` LH1 families first. Only after the Orchestrator confirms no
additional connector value remains may CVF open a separate live-proof roadmap
for `abtop`, `gridex`, or other route-execution families.

## Mandatory Corpus Completeness And Report Integrity - 2026-06-01

Canonical standard:

`docs/reference/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_STANDARD_2026-06-01.md`

Machine guard:

`governance/compat/check_corpus_completeness_report_integrity.py`

Any AI/agent that reads an existing folder, subfolder tree, archive, file list,
or project source set to produce an inventory, report, comparison, extraction,
audit, migration, roadmap, work order, or knowledge-absorption decision must
prove the bounded source corpus before claiming completeness.

The output must include a `Corpus Completeness And Report Integrity` block with
filesystem-backed enumeration, a file-level processing ledger, reconciliation,
explicit unresolved files, exclusions, unreadable/unsupported formats,
aggregation check, drift check, output traceability, adversarial verification,
and one allowed verdict:

- `COMPLETE_VERIFIED`
- `COMPLETE_WITH_DECLARED_EXCLUSIONS`
- `PARTIAL`
- `BLOCKED`
- `STALE_SNAPSHOT`

Self-reported counts, folder-level summaries, prior reports, and model claims
are not corpus evidence. `COMPLETE_VERIFIED` requires zero unresolved files.
Machine checks prove evidence discipline, not semantic understanding of every
file; high-impact reports still require adversarial sampling or independent
recomputation.

## Mandatory Corpus-To-Knowledge-Map Reconciliation - 2026-06-01

Canonical standards:

- `docs/reference/CVF_KNOWLEDGE_SYSTEM_METHOD_STANDARD_2026-06-01.md`
- `docs/reference/CVF_CORPUS_TO_KNOWLEDGE_MAP_RECONCILIATION_STANDARD_2026-06-01.md`

Machine guard:

`governance/compat/check_corpus_to_knowledge_map_reconciliation.py`

Any AI/agent that creates, refreshes, or relies on a corpus-derived knowledge
map, semantic-region ledger, architecture reconciliation, Memory synthesis,
graphification plan, or retrieval-readiness claim must include a `Knowledge
System Reconciliation` block.

The block must distinguish source authority from rebuildable derived views,
use filesystem-backed or structured-complete enumeration, account for all
authority assets through mapped/deferred/unmapped totals, expose cross-region
links, check drift and rebuildability, bound retrieval claims, and record
adversarial verification.

Bare `rg --files` is not completeness evidence. Ripgrep inventory must use
`rg --files --hidden --no-ignore`. `RECONCILED_VERIFIED` requires zero deferred
and zero unmapped assets plus `Drift check: PASS`.

Graph, semantic-region, Palace, summary, cache, snapshot, and retrieval views
are derived views. They may improve navigation but must remain rebuildable from
governed source authority. Machine checks prove reconciliation discipline, not
deep semantic correctness or runtime integration.

## Mandatory Corpus Intelligence Classification - 2026-06-01

Canonical standard:

`docs/reference/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_STANDARD_2026-06-01.md`

Machine guard:

`governance/compat/check_corpus_intelligence_classification.py`

Any AI/agent that classifies corpus-derived intelligence for chatbot,
retrieval, legal/policy, internal-decision, or answer surfaces must include a
`Corpus Intelligence Classification` block before claiming response readiness.

The block must include a classification ledger with `sourcePath`,
`processingStatus`, `knowledgeRegion`, `ownerSurface`, `disposition`, and
`evidencePointer`, plus response-boundary classes:

- `DIRECT_CITED_ANSWER`
- `SUMMARY_WITH_SOURCE`
- `PROCEDURAL_GUIDANCE`
- `ESCALATE_OR_ABSTAIN`

Accepted dispositions require evidence pointers. `READ_SHALLOW` cannot support
direct cited answers. Legal/policy corpus classification must include domain
fields such as jurisdiction, authority level, effective date, source authority,
and answer boundary.

GC-050 is a structural guard. It proves classification discipline, not semantic
correctness, legal advice quality, runtime integration, or chatbot answer
truth. Semantic correctness remains review and adversarial sampling work.

## Mandatory Corpus Search And Filter Readiness - 2026-06-02

Canonical standard:

`docs/reference/CVF_CORPUS_SEARCH_FILTER_READINESS_STANDARD_2026-06-02.md`

Any AI/agent that scans a corpus for retrieval, chatbot use, knowledge
absorption, migration, project intelligence, owner-surface routing, or "not
found" claims must preserve search/filter evidence before claiming readiness.

The required discipline is broader than legal/policy chatbot work and applies
to legacy folders, user project folders, public docs, internal company corpora,
source-code documentation, SOPs, policies, and knowledge bases.

Required evidence includes corpus discovery index, facet schema, processing
ledger, negative search evidence, derived-view trace, query receipt model, and
adversarial sampling plan. Search/filter readiness proves traceability and
reviewability; it does not prove semantic correctness, answer truth, legal
correctness, or runtime behavior.

## Mandatory Corpus Scan Registry Consultation - 2026-06-02

Canonical standard:

`docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md`

Generated registry front door:

`docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`

Registry authoring sources:

`docs/corpus-intelligence/registry/`

Guard (GC-051):

`governance/toolkit/05_OPERATION/CVF_GC051_CORPUS_SCAN_REGISTRY_GUARD.md`

Any AI/agent that intends to scan, classify, or absorb knowledge from any
corpus — legacy folders, project source trees, policy documents, company
documentation, or external sources — must first read
`docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`.

If the target corpus path is already registered:

- `SCANNED` / `DEEP_CLASSIFIED` → inherit prior state; do NOT re-scan without
  explicit operator authorization.
- `PARTIALLY_SCANNED` → continue from where the prior scan left off.
- `SCANNED_WITH_FINDINGS` → read all `findings[]` entries for that corpus
  before starting related implementation work.
- `NOT_STARTED` / absent → proceed with new scan; add a registry entry first.

After completing a scan, the agent MUST update the per-entry source under
`docs/corpus-intelligence/registry/entries/`, run
`python governance/compat/generate_corpus_scan_registry.py --generate`, and
commit the source entry plus generated aggregate in the same governed batch as
the scan evidence. Do not hand-edit the generated aggregate for ordinary entry
updates.

Manifest hash standard: SHA-256 of sorted filesystem paths joined with `\n`
(newline-separated, with trailing newline). Record `hashAlgorithm: sha256`
and `hashInput: sorted-paths-newline-joined-with-trailing-newline` in the
registry entry.

Finding discovery: before implementing a feature in a domain that has been
scanned, search `findings[]` in the registry. Cite any matching prior finding
in the work order — do not rediscover it as a new gap.

Checker: `governance/compat/check_corpus_scan_registry.py` — wired into
autorun gate and pre-commit hook chain.

## Mandatory System Loop Interlock - 2026-06-02

Canonical standard:

`docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_STANDARD_2026-06-02.md`

Canonical registry:

`docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json`

Machine guard:

`governance/compat/check_system_loop_interlock.py`

CVF planes and loops must not close as system-connected merely because their
artifacts exist. A governed loop output must become a declared downstream loop
input through the interlock registry.

Any future work that claims one loop feeds another loop, one plane consumes
another plane's output, or a scan/finding/runtime/public-sync signal has been
routed into another CVF surface must ensure the registry contains a connection
with upstream loop, output artifact, signal contract, downstream loop, input
artifact, routing rule, evidence refs, automation level, and claim boundary.

The first active interlock is `scan-loop-to-learning-loop`: GC-051 scan findings
feed Finding-To-Governance / Learning Signal Intake through F2G-compatible
`defectClass`, `learningLane`, and real action evidence. This proves
traceability, not semantic correctness, autonomous roadmap creation, runtime
mutation, or production readiness.

Autorun and local hook chains must run the interlock checker. A missing or
broken active interlock blocks system-connected closure claims.

## Latest Closed Continuation Roadmap

Latest closed: `docs/roadmaps/CVF_W132_T1_PROVIDER_RUNTIME_STABILITY_AND_BROWSER_SESSION_HARDENING_ROADMAP_2026-04-30.md`. Previous closed: `docs/roadmaps/CVF_W131_T1_NONCODER_POST_W130_REAL_TRAFFIC_STABILITY_AND_CLAIM_HARDENING_ROADMAP_2026-04-30.md`. W133 (SSE/connection lifecycle fix, inter-journey delay/backoff, `user_persona` routing coverage, stability re-run) requires fresh GC-018 and roadmap authority before implementation; it is not yet started.

Full per-wave evidence for the closed W113-W132 continuation chain lives in each wave's own roadmap file under `docs/roadmaps/`; do not restate it here and do not expand this claim beyond those versioned roadmap/review owners.

Web is governance-inherited on the active governed AI path, not the full CVF runtime. Future work must improve enforcement without overstating either claim.
