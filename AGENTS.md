# CVF Agent Instructions

## Session Memory Front Door

The active session front door for new or resumed agents is:

`CVF_SESSION_MEMORY.md`

Resolve the machine-readable state registry before treating any root handoff as
current:

`CVF_SESSION/ACTIVE_SESSION_STATE.json`

The current active handoff in that registry is:

`AGENT_HANDOFF_V22_2026-06-22.md`

Historical handoffs are archived under:

`CVF_SESSION/handoffs/archive/`

This includes `CVF_SESSION/handoffs/archive/AGENT_HANDOFF.md`, V2-V20, and
side-channel handoff files. Do not append new status to archived handoffs;
update the active handoff named by `CVF_SESSION/ACTIVE_SESSION_STATE.json` or
open a later versioned handoff when the active handoff approaches the limit.
After opening a successor handoff, startup front doors and routing docs must
reference only the active handoff by bare filename. Superseded handoffs may
appear only as archive-qualified paths under `CVF_SESSION/handoffs/archive/`.

## Mandatory Startup Acknowledgment - 2026-05-26

Before material governed work in any new or resumed session, the agent must read
`CVF_SESSION_MEMORY.md`, resolve `CVF_SESSION/ACTIVE_SESSION_STATE.json`, and
identify the active handoff named by that registry.

The agent must then state to the operator or record in the active handoff/session
state one concise acknowledgment naming:

- current mode;
- active handoff;
- next allowed move;
- any parked operator checkpoint.

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

This rule is agent-enforced. Future agents must obey it without waiting for a
human reminder.

Canonical stop-rule packet:

`docs/reviews/CVF_F1_DIMINISHING_RETURNS_STOP_RULE_2026-05-15.md`

F-1 output-quality parity work must not continue as open-ended prompt,
template, model, or token-budget tuning. The current evidence already proves a
useful product boundary: CVF preserves governance evidence and safety on the
EVT-4 corpus, but still carries measurable output-quality tax for some
non-coder deliverables.

Binding instructions:

- Do not continue broad prompt/template/model/token-budget tuning for F-1.
- Do not increase the trusted non-coder DeepSeek `deepseek-v4-pro` token cap
  above the retained stable `3072` setting.
- Do not reintroduce runtime two-pass expansion for F-1.
- Do not rerun full EVT-4 merely hoping reviewer variance closes the gap.
- Do not repeat broad family-contract reshaping; R2 is rejected evidence.
- Retain the lean governed system prompt, DeepSeek `3072` cap, and bounded
  CFG-A direct-empty retry unless a later explicit roadmap supersedes them.

The one bounded continuation was completed on 2026-05-15. Closure packet:

`docs/reviews/CVF_F1_OUTPUT_QUALITY_PARITY_CLOSURE_NOT_MET_2026-05-15.md`

Final F-1 status is `closed: not met, evidence-backed`. Do not claim
output-quality parity and do not continue F-1 micro-tuning.

Carry this bounded claim forward:

`docs/reviews/CVF_EVT4_BOUNDED_VALUE_CLAIM_2026-05-15.md`

The next product roadmap is:

`docs/roadmaps/CVF_NONCODER_OUTPUT_QUALITY_HARDENING_ROADMAP_2026-05-15.md`

Future output-quality work must proceed through that roadmap as product-level
non-coder deliverable hardening, not as F-1 parity tuning. EVT-4 may be used as
a regression benchmark only after meaningful product changes.

Any later attempt to reopen broad F-1 tuning requires fresh explicit human
authorization and a new review/roadmap packet explaining why the stop rule no
longer applies.

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

Canonical standard:

`docs/reference/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md`

Agent-neutral commit steward standard:

`docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md`

For latency control, agents must use the narrowest steward lane that matches
the changed set. Use `session-sync` for generated/front-door session updates,
and use `handoff-sync` only for a dedicated root active-handoff-only continuity
commit after the material/session commit is already aligned.

Agent-error learning philosophy:

`docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md`

Any agent-led CVF workflow that drafts, dispatches, implements, reviews, closes,
commits, pushes, or public-syncs governed work must use the autorun workflow
gates. The intent is to protect non-coder operators from having to manually
inspect whether a worker agent followed the process.

Repeated agent errors are governance training samples, not merely worker blame.
If a defect pattern repeats, promote it from finding to written rule; if the
rule remains interpretable, promote it to machine check; if the machine check
only catches the issue at closure, move it into the earliest applicable autorun
phase gate. CVF trust belongs to the governance control chain, not to any one
agent model.

Required phase gates:

- before ready/dispatch:
  `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base <baseHead> --head HEAD`
- before material implementation:
  `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <baseHead> --head HEAD`
- before any `CLOSED`, `CLOSED_PASS`, `CLOSED_PASS_BOUNDED`, or equivalent
  claim:
  `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base <baseHead> --head HEAD`
- before push:
  `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-push --base <baseHead> --head HEAD`

Reviewer fast preflight:

- when a no-commit worker returns uncommitted or staged governed artifacts for
  Codex/orchestrator review, run the focused reviewer gate before attempting a
  full commit:
  `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast`
- for lower total operator wait time, workers/reviewers may run the one-command
  fast bundle first:
  `python governance/compat/run_worker_return_fast_gate.py`
  and add `--pytest-target <path>` for focused tests named by the work order.
- This gate is not closure evidence and does not replace pre-closure or
  pre-push autorun gates. It is an early defect filter for reviewer-return
  packets: closure residue, source/registry coverage, public export
  disposition, machine closure rows, finding-learning disposition, and active
  session continuity.
- `reviewer-fast`, `pre-commit`, and `pre-push` local hook modes run in
  parallel by default for latency control. Use `--serial` only for debugging
  order-dependent output.

If a phase gate fails, the agent must stop at that phase and mark the artifact
`DRAFT`, `HOLD_*`, `BLOCKED`, or return it to Orchestrator. A worker may not
"fix while implementing" a failed dispatch packet unless that remediation is
the explicitly assigned task. A reviewer may not accept handwritten PASS
claims when the autorun gate fails. Operator silence is not a waiver.

Allowed-scope gate remediation is mandatory, not optional. Once a work order is
dispatched, any machine-gate failure inside its Allowed scope must be repaired
and rerun by the assigned agent instead of escalated as "do you want me to fix
this?" to the operator. Ask the operator only when the repair would exceed
Allowed scope, change the claim boundary, release a `HOLD_*` prerequisite,
alter risk level, open public-sync, run live/provider proof, consume
secrets/quota, touch forbidden paths, or perform destructive/irreversible
actions. Treat an agent asking whether to fix an allowed-scope guard failure as
a governance/control-plane learning signal.

Pre-closure must not accept untracked, modified, or unresolved worktree changes
as a clean closure claim. Closure must be backed by committed diff evidence,
`git status --short`, receipts, command output, or explicit `N/A with reason`.

Before a governed commit or worker-return handoff, run the agent-neutral commit
steward preflight for the matching mode:

```bash
python governance/compat/run_agent_commit_steward_preflight.py --mode <dispatch|implementation|reviewer-return|closure|push|session-sync> --base <baseHead> --head HEAD --enforce
```

The steward preflight does not replace autorun phase gates or git hooks. It
reduces total elapsed time by running the correct phase gate early, printing the
material/session split plan, and blocking high-risk commit shapes such as
Agent Operation Trace exact-manifest artifacts mixed with active handoff/session
sync. This rule is provider-neutral and applies when a single agent performs
multiple roles.

Latest-closure continuity is mandatory. If the state registry contains a
higher closed `lhwN...CLOSED_PASS_BOUNDED` record, then `nextAllowedMove`,
`CVF_SESSION_MEMORY.md` `Next Allowed Move`, and the active handoff must
reference that same latest `LHWN`; stale lower-wave text blocks closure.

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

The latest closed continuation roadmap is `docs/roadmaps/CVF_W132_T1_PROVIDER_RUNTIME_STABILITY_AND_BROWSER_SESSION_HARDENING_ROADMAP_2026-04-30.md`.

The previous closed continuation roadmap is `docs/roadmaps/CVF_W131_T1_NONCODER_POST_W130_REAL_TRAFFIC_STABILITY_AND_CLAIM_HARDENING_ROADMAP_2026-04-30.md`.

The active next runtime-stability tranche is W133, authorized conceptually by the W132 continuation decision but still requiring a fresh GC-018 and roadmap file before implementation. W133 scope: SSE/connection lifecycle fix, inter-journey delay/backoff, `user_persona` routing coverage, and stability re-run.

Treat the W113/W116/W117/W118/W119/W122/W123/W124/W125/W126/W127/W128/W129/W130/W131/W132 boundary language as binding:

- Workspace bootstrap is now agent-enforcement-ready when generated artifacts, workspace-root `WORKSPACE_RULES.md`, and the workspace doctor pass. Canonical workspace topology is `docs/reference/CVF_WORKSPACE_RULES.md`: a non-git parent workspace, hidden `.Controlled-Vibe-Framework-CVF` governance clone, and sibling downstream application folders.
- W113 proved this in one real downstream sample project with live API-backed governance evidence.
- W116 proved the downstream knowledge pipeline: `.md` files in `knowledge/` → ingested chunks → positive retrieval delta confirmed by unit evidence tests (16/16 pass).
- W117 proved the writable knowledge store: `KNOWLEDGE_COLLECTIONS` constant replaced by `InProcessKnowledgeStore`; admin CRUD API and UI delivered; Wave 2 live regression 4/4 pass; D1.4b deferred note retired.
- W118 proved unified persistent knowledge store: `_runtimeCollections` Map eliminated; `InProcessKnowledgeStore` unified with ephemeral path (`registerEphemeral()`); `FileBackedKnowledgeStore` delivers JSON-file persistence for admin-CRUD collections; `KnowledgeStoreAuditEntry` append-only audit trail delivered; `GET /api/admin/knowledge/audit` route delivered; Wave 2 live regression 4/4 pass; CP2 evidence hardening added real file I/O regression coverage (11 CP4 tests + 3 audit route tests in targeted W118 coverage).
- W119 proved the bounded non-coder adoption journey: secret-free first-run readiness; project knowledge ingest into governed `/api/execute`; route-returned `governanceEvidenceReceipt`; ProcessingScreen/ResultViewer evidence visibility and copy/export; live W119 runner 3/3 locked journeys pass on Alibaba lane with raw keys not printed.
- W122 proved the noncoder intent-first front door: `intent-router.ts` as single routing source of truth; `IntentEntry` component extracted and rendered behind `NEXT_PUBLIC_CVF_INTENT_FIRST_FRONT_DOOR` feature flag (default `false`); weak-confidence fallback = no routed target (all target fields null, CTA disabled); wizard-family (9-entry) trusted routing subset enforced; evidence parity between routed and direct handoff paths proven (10/10); live E2E 6 passed / 2 skipped on Alibaba `qwen-turbo`; release gate 7/7 PASS. Feature flag default is `false` — rollout-safe. Known limit: VN `ứng dụng` `\b` boundary requires ASCII keywords for strong routing.
- W123 proved noncoder iteration memory and follow-up continuity: `execution-continuity.ts` helper module with `buildContinuationExecution`, `buildRootExecution`, thread selectors, `buildEvidenceSnapshot`, and `buildContinuityParityObject`; `Execution` type extended with `threadId`, `rootExecutionId`, `parentExecutionId`, `projectLabel`, `knowledgeCollectionId`, `evidenceReceiptSnapshot`, `starterSource`; Zustand store extended with `getThreadExecutions` + `setProjectLabel`; `handleFollowUp` in `home/page.tsx` creates durable continuation chain; `HistoryList` shows thread-label + follow-up badge + continue-work CTA behind `NEXT_PUBLIC_CVF_NONCODER_ITERATION_MEMORY` flag (default `false`); vitest 77/77 targeted; Playwright 6 passed / 1 skipped on Alibaba lane.
- W124 proved noncoder clarification loop and safe routing recovery: `intent-router-clarification.ts` with `startClarification`, `submitClarificationAnswer`, `buildEnrichedInput`, `buildNextQuestion` (max depth=2), `buildClarificationState`, `advanceClarificationState`; eligible cases = `weak_confidence` VN/EN only; browse-only cases = `unsupported_language`, `empty_input`; `IntentEntry` extended with clarification question + option buttons behind `NEXT_PUBLIC_CVF_NONCODER_CLARIFICATION_LOOP` flag (default `false`); 5 analytics event types added; vitest 23/23 clarification + 45/45 targeted; Playwright 2 passed / 2 skipped. Feature flag default `false` — rollout-safe. No parallel detector introduced; enrichment delegates to W122 `intent-router.ts`.
- W125 proved noncoder deliverable packs and handoff productization: `deliverable-pack.ts` typed contract (`DeliverablePack`, `PackType`, `PackGovernanceEvidence`); `inferPackType()` with template-match → category-fallback → `documentation_handoff` default; `generateDeliverablePack(execution, receipt?)` builds all pack fields; `serializePackToMarkdown()` 7-section export; `ResultViewer` upgraded with Result/Pack tab toggle and pack preview panel (6 sections); export menu extended with distinct "Download Deliverable Pack (.md)" option; 28/28 unit tests + 36/36 ResultViewer tests + E2E spec 4 journeys; release gate PASS.
- W126 proved trusted form-template routing expansion: `form-routing.ts` adds the bounded trusted-form subset (`email_template`, `documentation`, `competitor_review`, `risk_assessment`, `user_persona`, `feature_prioritization`, `pricing_strategy`, `strategy_analysis`); `routeIntent()` now enforces wizard -> trusted form -> weak-fallback precedence; form routes return `routeType: 'form'` with `starterKey: null`; Home handoff guard became route-type aware; vitest 28/28 pass. Routing claim remains bounded to the audited trusted subset, not the full template corpus.
- W127 proved noncoder adoption metrics and friction baseline: `noncoder-metrics.ts` computes 6 browser-local metrics (`time_to_first_value`, `route_recovery_rate`, `weak_fallback_rate`, `followup_continuation_rate`, `evidence_export_rate`, `deliverable_pack_export_rate`); `generateMetricReport()` + `summarizeFriction()` provide threshold-based readout; analytics instrumentation now includes `intent_routed`, `followup_started`, `evidence_exported`, and `deliverable_pack_exported`; Day-0 baseline artifact is published with N/A values until real traffic accumulates. Release gate PASS.
- W128 proved noncoder rollout readout and optimization loop: `noncoder-rollout-readout.ts` adds typed lane readouts and bounded `RolloutRecommendation` output across 6 lanes (`entry_routing`, `clarification_recovery`, `trusted_form`, `followup_continuity`, `evidence_export`, `deliverable_pack`); recommendations are feature-flag aware via `readNoncoderFlags()` and deterministic threshold logic; `AnalyticsDashboard` now exposes a `Noncoder Health` readout with low-data caveat, summary strip, flag posture, lane cards, and prioritized next actions. Targeted verification: 56/56 pass; release gate PASS 7/7.
- W129 proved noncoder controlled rollout posture and full Stage A → B → C signal capture: GC-018 issued 2026-04-27 (depth audit 9/10); rollout playbook (flag order + enable/hold/rollback criteria) + Stage A operator-local flag posture (`NEXT_PUBLIC_CVF_INTENT_FIRST_FRONT_DOOR`) + two rollout analytics events (`rollout_flag_enabled`, `rollout_session_start`) + dedicated live signal capture spec (`w129-stage-a-signal-capture.live.spec.ts`) with governed execution `ALLOW`, `intent_routed=5`, `clarification_browse_fallback=0`, and lane readout `entry_routing=healthy`, `trusted_form=healthy`. §7 post-closure addendum: `w129-stage-a-volume-capture.live.spec.ts` — `execution_created=12`, `entry_routing=healthy`, `stageBDecision=STAGE_B_MAY_ENABLE`. §8 Stage B signal capture (2026-04-28): `NEXT_PUBLIC_CVF_NONCODER_CLARIFICATION_LOOP=true` enabled; `w129-stage-b-signal-capture.live.spec.ts` — 8 short-input (≤5 char) journeys, `clarification_question_asked=8`, `clarification_recovery=healthy`, `stageCDecision=STAGE_C_MAY_ENABLE`. §9 Stage C signal capture (2026-04-28): `NEXT_PUBLIC_CVF_NONCODER_ITERATION_MEMORY=true` enabled; `w129-stage-c-signal-capture.live.spec.ts` — 5 browser-driven UI journeys with 3 successful follow-up submissions, plus one final live governed proof call; `followup_started=3`, `followup_continuity=healthy`, `rolloutDecision=W129_ROLLOUT_COMPLETE`. Boundary: the Stage C packet alone may show `clarification_recovery=no_data` because it does not replay weak-confidence prompts; rollout completion relies on aggregate Stage A+B+C evidence, with Stage B already proving `clarification_recovery=healthy`. All 3 noncoder flags now enabled in operator environment. W129 rollout is FULLY COMPLETE. W130 requires fresh GC-018.
- W130 proved noncoder evidence and pack export activation: GC-018 issued 2026-04-28 (depth 9/10); export activation contract published in `docs/reviews/CVF_W130_EXPORT_ACTIVATION_CONTRACT_2026-04-28.md`; `ResultViewer.tsx` now surfaces a noncoder export nudge and defaults to Pack view for noncoder sessions; `ProcessingScreen.tsx` now waits for hydrated local settings before launching live execution, preventing false fallback to default Gemini settings during governed browser runs; `ResultViewer.tsx` now uses a clipboard fallback path so evidence-copy analytics still fire when browser clipboard permissions are limited. Live proof: `w130-evidence-pack-export.live.spec.ts` PASS on Alibaba lane with `evidence_exported=1`, `deliverable_pack_exported=1`, `execution_accepted=1`, `evidence_export=healthy`, and `deliverable_pack=healthy`. Boundary: the W130 evidence packet contains 1 successful governed journey that fired both export events, plus 2 `mock_fallback_no_receipt` journeys retained for transparency; W130 proves both export lanes can exit `no_data`, not uniform live stability for every trusted-form prompt. W131 requires fresh GC-018.
- W131 proved post-W130 claim hardening by finding the current instability boundary: GC-018 issued 2026-04-30 (depth 10/10); W131 evidence packets show Alibaba `qwen-turbo` and DeepSeek `deepseek-chat` both at 1/6 accepted with 2 `api_timeout`, 2 `mock_fallback_no_receipt`, and 1 `route_miss`; Alibaba's long matrix also collapsed browser context after the first 6 real journeys. The continuation decision is data-backed: W132 = provider/runtime stability and browser session hardening. W131 does not prove stable multi-form noncoder operation.
- W132 proved browser-session isolation and diagnostics while classifying the remaining provider/runtime blocker: CP1-CP7 delivered, browser cascade failure eliminated, diagnostic subcodes and navigation hardening confirmed. Persistent blocker is `sequential_journey_failure_server_side_connection`: J1 succeeds, J2+ times out at about 93s across Alibaba and DeepSeek/model variants, indicating server-side SSE/streaming connection lifecycle. Secondary blocker: `user_persona` routing gap. W133 requires fresh GC-018 before implementation.
- CVF ADD doctrine absorption is officially integrated through docs and bounded runtime activation. Canon docs live in `docs/reference/CVF_GOVERNED_CAPABILITY_INTAKE_DOCTRINE_2026-05-07.md`, `docs/reference/CVF_BOUNDARY_FIRST_GOVERNANCE_DOCTRINE_2026-05-07.md`, `docs/reference/CVF_GOVERNED_CONTEXT_PROFILE_METADATA_DOCTRINE_2026-05-07.md`, `docs/reference/CVF_AGENT_CONTINUITY_AND_DELEGATION_DOCTRINE_2026-05-07.md`, and `docs/reference/CVF_SCOPED_KNOWLEDGE_PROVIDER_BOUNDARY_DOCTRINE_2026-05-07.md`. Runtime RT0-RT7 is delivered in `docs/roadmaps/CVF_ADD_RUNTIME_ACTIVATION_ROADMAP_2026-05-07.md`: metadata is runtime-readable, registry-persisted, and visible in External Asset Governance UI, without executing external tools or widening provider behavior.
- Web is governance-inherited on the active governed AI path, not the full CVF runtime.
- Future work must improve enforcement without overstating either claim.
