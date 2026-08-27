# CVF EACQ-FV MV2 External Agent Task Capsule Context Worker Return

Status: COMPLETE_PENDING_REVIEW

Self-declared worker-return artifact: yes

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_EACQ_FV_MV2_EXTERNAL_AGENT_TASK_CAPSULE_CONTEXT_2026-08-27.md`

dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_EACQ_FV_MV2_EXTERNAL_AGENT_TASK_CAPSULE_CONTEXT_2026-08-27.md`

executionBaseHead: `586115eae89864c456cebdc30f439caee071b109`

Memory class: FULL_RECORD

docType: review

Date: 2026-08-27

## Purpose

Extend the existing external-agent task capsule with four task-proportional
context groups (`protectedPaths`, `ownerMap`, `invariants`, `verification`)
and a deterministic offline, staleness-aware creation path, per EACQ-FV-MV2,
while preserving the current live `prepare-task` route and strict fail-closed
schema. This return delivers exactly the five modified owner paths and this
worker return, and records exact-command verification results.

## Scope / Methodology

Worker role: delegated no-commit implementation worker. Commit mode:
`WORKER_MUST_NOT_COMMIT`. Write ownership was exactly five existing paths
(schema, README, generator, generator tests, PowerShell wrapper) plus this
new worker return; every other path, including
`D:\UNG DUNG AI\EXTERNAL_AGENT_READ`, was out of scope and untouched.

Methodology: read every Required First Read source in full, recompute all
five pinned input hashes, confirm dispatch-base ancestry and a clean/empty
starting worktree, run the mandated negative-search collision queries,
design the smallest strict four-group JSON shape as an additive `allOf`/
`if`-`then` extension to the existing v1 capsule schema, implement the
generator's context-file loader, offline creation route, and live-route
`--context-file` option, extend the PowerShell wrapper with an explicit
`PrepareTaskOffline` mode, document consumers/freshness/live-offline
boundary in the owner README, build the full Test Matrix, then run every
pinned verification command and record exact output.

## Target / Source

Target: the existing `cvf.externalAgentTaskCapsule.v1` schema, its Python
generator (`scripts/external_agent_packet.py`), its focused test module,
its PowerShell wrapper, and its owner README, per the EACQ-FV-MV2 work
order and paired GC-018 baseline.

## Source Inventory

| Source | Action |
| --- | --- |
| `AGENTS.md` | READ |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | READ |
| `CVF_SESSION_MEMORY.md` | READ |
| `AGENT_HANDOFF_V59_2026-08-11.md` | READ |
| `docs/reference/guard_orientation/README.md` | PARTIAL_READ |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | FULL_READ |
| `docs/roadmaps/CVF_EXTERNAL_AGENT_CODING_QUALITY_AND_FORWARD_VALUE_ABSORPTION_ROADMAP_2026-08-27.md` | SOURCE_VERIFIED |
| `docs/baselines/CVF_GC018_EACQ_FV_MV2_EXTERNAL_AGENT_TASK_CAPSULE_CONTEXT_2026-08-27.md` | FULL_READ |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_EACQ_FV_MV2_EXTERNAL_AGENT_TASK_CAPSULE_CONTEXT_2026-08-27.md` | FULL_READ |
| `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_TASK_CAPSULE.schema.json` | FULL_READ |
| `scripts/external_agent_packet.py` | FULL_READ |
| `scripts/test_external_agent_packet.py` | FULL_READ |
| `scripts/Update-CVF-External-Agent-Packet.ps1` | FULL_READ |
| `docs/reference/external_agent_review/README.md` | FULL_READ |

## Findings / Position

### Finding 1 - schema, generator, and tests implemented as an additive extension; existing behavior unchanged

The four groups were added as optional root properties on the existing
`cvf.externalAgentTaskCapsule.v1` schema (no new `$id`, no v2). An
`allOf`/`if`-`then` clause requires all four groups only when
`task.workingMode` is `BUILD_NEW_REPOSITORY` or `EXTEND_SUPPLIED_REPOSITORY`;
`REVIEW_ONLY`, `DESIGN_ONLY`, and `SOURCE_PACK_PREPARATION` remain
proportionally exempt because those modes do not mutate a target repository.
This exemption is schema-visible (the `if`/`then` clause itself), not a
silent generator-side skip, per the work order's compatibility contract.
`additionalProperties: false` is preserved at every existing boundary and
added at every new one (`protectedPaths`, `ownerMap`, each `owners[]` item,
`invariants`, `verification`, and the shared `$defs/freshnessRule`).

The pre-existing `test_generated_task_capsule_matches_strict_schema` test
(using `working_mode="SOURCE_PACK_PREPARATION"`, which is exempt) continues
to pass unmodified against the extended schema, confirming the extension is
backward compatible.

### Finding 2 - offline route makes zero network/Git-remote calls, verified by patching the module's only subprocess entrypoint

`create_capsule_offline` never calls `refresh_snapshot`, never touches Git,
and never reads a prior refresh receipt. `test_offline_path_makes_zero_
network_or_git_remote_calls` monkeypatches `subprocess.run` (the sole
Git/network entrypoint in `scripts/external_agent_packet.py`) to raise if
invoked at all, then runs the full offline creation path; the test passes,
proving no call reaches that entrypoint rather than merely asserting no
error was raised.

### Finding 3 - invalid offline input cannot overwrite an existing capsule

`create_capsule` validates the fully assembled capsule against the strict
schema (`_validate_capsule`) before calling `_write_json`. Because
`_write_json` is the only write, a `PacketError` raised during validation
happens before any file I/O for that call.
`test_invalid_offline_input_does_not_overwrite_existing_capsule` seeds a
pre-existing capsule file with a distinctive marker, attempts an offline
creation with a deliberately invalid context group (empty `paths` array),
asserts `PacketError` is raised, then asserts the original file bytes are
byte-for-byte unchanged.

### Finding 4 - pinned `--phase pre-closure` autorun command surfaces expected pre-return noise, not a worker-scope defect

Running the pinned command
`python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 22644e47e118bd88bf0d004cb74819fd2956c061 --head HEAD`
fails at the "committed range shape preflight" step because the dispatch
base..HEAD range mixes the orchestrator's material dispatch commit
(`437d59a48`) with a session-sync commit (`586115eae`), per literal-format
gotcha 12
(`docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
item 12). Running the recommended material-only sub-range
(`22644e47e..437d59a48`) as a supplementary check shows the substantive
gates passing; the only genuine failures there are: (a) "closure worktree
finality", which correctly rejects a *pre-closure* claim while this
no-commit worker's five files remain uncommitted by design; (b) "agent
operation trace integrity", which compares my worktree changes against the
*dispatcher's* dispatch-time Agent Operation Trace manifest (baseline + work
order only, "implementation absent" per that block's own text) rather than
this worker return's own trace manifest below; and (c) "work-order dispatch
quality", which flags that the work order document itself lacks a literal
`## Required Artifact Manifest` heading (it uses `## Work-Order Fulfillment
Manifest` and `## Expected Output Manifest` instead) - a pre-existing shape
gap in a read-only dispatch artifact, outside this worker's write ownership.
None of these three are defects in the five paths this worker modified.
Reported for reviewer awareness, consistent with the same class of finding
recorded in the accepted MV-1 worker return.

## Risk / Corrective Action

Risk: the `if`/`then` conditional-required clause depends on `task.
workingMode` being present and correctly set by the caller before schema
validation; a caller that mis-sets `workingMode` could bypass the intended
context-group requirement for a repository-mutating task while still
passing strict validation. Corrective action available to the reviewer, not
taken by this worker (would require touching the work order's own mode
enum or a new cross-field CVF-native invariant beyond this bounded schema
delta): treat `workingMode` selection itself as an invariant the dispatching
work order/GC-018 must state and the reviewer must source-verify per task,
the same way `working_mode` is already source-verified elsewhere in this
protocol. No schema change is proposed here because the four-group
requirement is correctly conditioned on the documented working-mode
semantics already governed by the existing `task.workingMode` enum.

## Implementation Location

- `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_TASK_CAPSULE.schema.json`
  - `$defs.consumerList`, `$defs.freshnessRule`, `$defs.safeRelPath` - shared
    strict building blocks.
  - `properties.protectedPaths`, `properties.ownerMap`, `properties.
    invariants`, `properties.verification` - the four new root groups.
  - top-level `allOf`/`if`-`then` clause - conditional requirement for
    `BUILD_NEW_REPOSITORY` / `EXTEND_SUPPLIED_REPOSITORY`.
  - `properties.cvfPublicSource.properties.sourcePosture` - new required
    enum distinguishing live-verified from operator-pinned source.
- `scripts/external_agent_packet.py`
  - `SOURCE_POSTURE_LIVE`, `SOURCE_POSTURE_OFFLINE` - the two exact literal
    values.
  - `CONTEXT_REQUIRED_MODES`, `CONTEXT_GROUP_NAMES`, `CONSUMER_ROLES` -
    named constants, no new candidate vocabulary beyond the work order's
    four groups.
  - `_load_capsule_schema`, `_validate_capsule` - pre-write strict
    validation shared by both routes.
  - `load_context_groups(context_file)` - loads and structurally checks a
    local context JSON file; rejects unknown top-level groups before
    per-field schema validation.
  - `create_capsule(args, public_sha, *, source_posture=..., context_groups=None)`
    - extended signature, backward compatible via keyword-only defaults;
    enforces the four-group requirement for context-required working modes
    before validating and writing.
  - `create_capsule_offline(args)` - the new offline entrypoint; validates
    `--cvf-public-commit` as a 40-char SHA, loads the context file, and
    calls `create_capsule` with `SOURCE_POSTURE_OFFLINE`.
  - `_build_parser` - adds `--context-file` to `prepare-task` and the new
    `create-capsule-offline` subparser.
  - `main` - dispatches `create-capsule-offline` to `create_capsule_offline`
    and passes `--context-file` through the live `prepare-task` route.
- `scripts/Update-CVF-External-Agent-Packet.ps1` - adds `PrepareTaskOffline`
  to `-Mode`, plus `-ContextFile` and `-CvfPublicCommit` parameters; the
  live `PrepareTask` mode forwards `-ContextFile` when supplied.
- `docs/reference/external_agent_review/README.md` - documents the four
  groups, their consumers/freshness contract, and the live-versus-offline
  source-posture distinction.

## Focused Case Names

| Test Matrix requirement | Test |
| --- | --- |
| strict valid capsule, all four groups | `test_strict_valid_capsule_with_all_four_groups` |
| each missing group fails | `test_each_missing_group_fails_for_context_required_mode[protectedPaths\|ownerMap\|invariants\|verification]` (4 parametrized cases) |
| empty/unknown/malformed group content fails | `test_empty_unknown_or_malformed_group_content_fails` (6 parametrized cases) |
| duplicate protected path fails | `test_duplicate_protected_path_fails` |
| unsafe protected path fails | `test_unsafe_protected_path_fails` |
| owner path/symbol/competing-owner preserved exactly | `test_owner_path_symbol_and_competing_owners_preserved_exactly` |
| invariants/forbidden transitions preserved exactly | `test_invariants_and_forbidden_transitions_preserved_exactly` |
| verification items preserved exactly | `test_verification_items_preserved_exactly` |
| live path records live-verified posture | `test_live_preparation_path_records_live_verified_source_posture` |
| offline path records pinned-not-live-verified posture | `test_offline_path_records_pinned_not_live_verified_posture` |
| offline path succeeds with Git/network helpers patched to fail | `test_offline_path_makes_zero_network_or_git_remote_calls` |
| invalid offline input does not overwrite existing capsule | `test_invalid_offline_input_does_not_overwrite_existing_capsule` |
| existing return-validation tests remain passing | `test_existing_return_validation_tests_remain_passing` (plus the 5 pre-existing unmodified tests, all still passing) |
| PowerShell route/argument construction source-inspected, no network execution | `test_prepare_task_cli_exposes_context_file_option`, `test_create_capsule_offline_cli_subcommand_registered` (Python-CLI side; the PowerShell wrapper's new branches were source-read and its file was parse-checked with `[System.Management.Automation.Language.Parser]::ParseFile`, not executed, since it would require a real Python subprocess call - see Command Evidence) |
| additional negative coverage beyond the matrix | `test_offline_context_file_missing_fails_with_packet_error`, `test_offline_context_file_invalid_json_fails`, `test_offline_context_file_unknown_group_fails`, `test_offline_invalid_public_commit_fails`, `test_load_context_groups_round_trips_valid_file`, `test_review_only_mode_does_not_require_context_groups` |

35 focused tests total (6 pre-existing unmodified plus 29 new), 35 passed.

## Command Evidence

```text
$ git merge-base --is-ancestor 22644e47e118bd88bf0d004cb74819fd2956c061 HEAD
exit code: 0 (ancestry confirmed)

$ python governance/compat/run_adif_defect_resolver.py --task-class "task capsule implementation" --role worker --lifecycle-phase pre-implementation --surface-selector scripts --risk-ceiling MEDIUM --json
{"items": [], "truncated": false, "totalCandidates": 0, ...}
exit code: 0 (matches dispatch-time NONE_RETURNED; no overlay)

$ python -m pytest scripts/test_external_agent_packet.py -q
35 passed in 0.43s
exit code: 0

$ python governance/compat/run_worker_return_fast_gate.py --pytest-target scripts/test_external_agent_packet.py
pytest target: 35 passed
[CVF hook] All reviewer-fast governance checks passed. / PASS: reviewer-fast governance gate (3.34s)
git diff --check: PASS (CRLF-on-touch informational warnings only, no whitespace violation)
COMPLIANT: worker-return fast gate passed in 4.84s.
exit code: 0

$ python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 22644e47e118bd88bf0d004cb74819fd2956c061 --head HEAD
FAIL at committed range shape preflight: range mixes material dispatch commit `437d59a48` with session-sync commit `586115eae` (literal-format gotcha 12); not a worker-scope defect. See Finding 4.
exit code: 1 (pinned range; see supplementary sub-range below)

$ python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 22644e47e118bd88bf0d004cb74819fd2956c061 --head 437d59a48
[supplementary only, per gotcha 12's recommended split] substantive gates PASS; 3 remaining FAILs are: closure worktree finality (correctly rejects pre-closure claim on an intentionally uncommitted no-commit return), agent operation trace integrity (compares against the dispatcher's dispatch-time trace manifest, not this worker return's own manifest below), work-order dispatch quality (work order lacks literal `## Required Artifact Manifest` heading - read-only file outside this worker's scope). None are defects in the five modified paths.
exit code: 1 (supplementary; see Finding 4)

$ git diff --check
(CRLF-will-be-replaced informational warnings only on 4 modified files; no reported whitespace violation)
exit code: 0

$ git diff --name-status
M	docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_TASK_CAPSULE.schema.json
M	docs/reference/external_agent_review/README.md
M	scripts/Update-CVF-External-Agent-Packet.ps1
M	scripts/external_agent_packet.py
M	scripts/test_external_agent_packet.py

$ git diff --name-only
docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_TASK_CAPSULE.schema.json
docs/reference/external_agent_review/README.md
scripts/Update-CVF-External-Agent-Packet.ps1
scripts/external_agent_packet.py
scripts/test_external_agent_packet.py

$ git diff --cached --name-only
(no output - staging area empty)

$ git status --short
 M docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_TASK_CAPSULE.schema.json
 M docs/reference/external_agent_review/README.md
 M scripts/Update-CVF-External-Agent-Packet.ps1
 M scripts/external_agent_packet.py
 M scripts/test_external_agent_packet.py
?? docs/reviews/CVF_EACQ_FV_MV2_EXTERNAL_AGENT_TASK_CAPSULE_CONTEXT_WORKER_RETURN_2026-08-27.md

$ [System.Management.Automation.Language.Parser]::ParseFile('scripts/Update-CVF-External-Agent-Packet.ps1', ...)
SYNTAX_OK (no parse errors; PowerShell wrapper not executed against any network/provider surface)
```

## Checker Source Read-Ahead Block

| Field | Evidence |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `check_dispatch_prompt_envelope.py`; `check_governed_artifact_checker_read_ahead.py`; `check_agent_operation_trace.py`; `check_worker_return_quality_gate.py`; `check_worker_experience_retrospective.py`; `check_finding_to_governance_learning.py`; `check_markdown_structural_completeness.py` |
| literalTokensReviewed | `Self-declared worker-return artifact: yes`; `Responds to work order:`; `WORKER_MUST_NOT_COMMIT honored`; the worker-experience-retrospective structured block token; `CLAIM_REJECTED_NO_RECEIPT`; `CLAIM_REJECTED_NO_ACTION`; `VERIFIED_LIVE_PUBLIC_MAIN_AT_CREATION`; `OPERATOR_PINNED_NOT_LIVE_VERIFIED`; required worker-return heading set |
| gateRunPurpose | Confirm dispatch and worker-return contract shapes were already known before implementation; the gate runs recorded above are evidence-recording confirmation of the final artifacts, run after the required reads and pinned-hash checks completed. |
| claimBoundary | Source read-ahead is preparation evidence only and does not establish implementation correctness or closure. |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | delegated no-commit implementation worker |
| Provider or surface | local private-provenance workspace |
| Session or invocation | EACQ-FV-MV2 worker execution, 2026-08-27 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | Read, Write, Edit, Bash (`git`, `python`, `pytest`), PowerShell (`Parser::ParseFile`), governance gates |
| Target paths | the five Write Ownership modify paths plus this new worker return |
| Allowed scope source | `docs/work_orders/CVF_AGENT_WORK_ORDER_EACQ_FV_MV2_EXTERNAL_AGENT_TASK_CAPSULE_CONTEXT_2026-08-27.md` |
| Before status evidence | clean worktree and empty staging at execution head `586115eae89864c456cebdc30f439caee071b109`; all five pinned input hashes matched exactly; worker return path absent |
| After status evidence | five modified tracked paths plus one new untracked worker-return path; no staged changes; no other path touched |
| Diff evidence | `git diff --name-status` and `git status --short`, recorded above under Command Evidence |
| Approval boundary | six-path no-commit implementation only; no closure, hook wiring, provider, public, or production claim |
| Claim boundary | no runtime/provider/live/public/production claim; local deterministic schema/generator/test/docs implementation pending independent review |
| Agent type | delegated no-commit implementation worker |
| Invocation ID | `eacq-fv-mv2-worker-2026-08-27` |
| Expected manifest | `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_TASK_CAPSULE.schema.json`; `docs/reference/external_agent_review/README.md`; `scripts/external_agent_packet.py`; `scripts/test_external_agent_packet.py`; `scripts/Update-CVF-External-Agent-Packet.ps1`; this worker return |
| Actual changed set | `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_TASK_CAPSULE.schema.json`; `docs/reference/external_agent_review/README.md`; `scripts/external_agent_packet.py`; `scripts/test_external_agent_packet.py`; `scripts/Update-CVF-External-Agent-Packet.ps1`; this worker return |
| Manifest delta | MATCH |
| Deletion or rename disposition | NONE |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | local schema/generator/test/wrapper/docs implementation only |
| claimDisposition | CLAIM_REJECTED: no universal agent-control or runtime-enforcement claim |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no provider/runtime receipt is created or consumed by this return |
| actionEvidence | ACTION_EVIDENCE_PRESENT: local unit/subprocess-patched test execution and command evidence, recorded above |
| invocationBoundary | this return does not assert mandatory invocation or wrapper coverage; helper/wrapper invocation remains explicit and manual |
| interceptionBoundary | no interception, proxy, hook, daemon, or universal dispatch control is authorized or claimed |
| claimLanguage | validated local capsule production pending independent review; not self-closed |
| forbiddenExpansion | no provider/live/public/package/Web/MCP/deployment/production claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

No public artifact, remote, commit, external packet-folder write, or path is
authorized or claimed by this worker return.
`D:\UNG DUNG AI\EXTERNAL_AGENT_READ` was not written to at any point.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | reviewed R0 proposal -> minimum viable roadmap -> MV-1 closure -> MV-2 value gate/dispatch -> this worker return |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | existing external-agent task capsule schema/generator/wrapper |
| Disposition | ADAPT only as an additive extension of the existing owner |
| Claim boundary | no new external knowledge, doctrine, provider, or effectiveness claim |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON
- N/A with reason: bounded implementation of an already-accepted work order
  against a fixed owner set; no source reassessment is performed by this
  worker.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - bounded named-owner
  implementation; no corpus inventory or completeness claim is made by this
  return.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next action |
| --- | --- | --- | --- | --- |
| Pinned `--phase pre-closure` autorun command's committed range mixes a material dispatch commit with a session-sync commit at dispatch time, reproducing the same range-shape class as MV-1's pinned-command finding | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | RUNTIME_LEARNING_CANDIDATE, N/A_WITH_REASON for any live/provider/cost claim - this is a committed-range shape mismatch, not a runtime/provider/cost defect | Next action: reviewer/dispatcher considers whether the dispatch scaffold should split the material-authoring commit from the session-sync commit before naming a single `dispatchBaseHead..HEAD` pinned command in future work orders; outside this worker's write ownership to resolve. |
| Dispatch-time Agent Operation Trace block in a work order cannot be diffed against worker-produced files without appearing as unauthorized additions, since the dispatcher's own trace manifest intentionally excludes not-yet-created worker output | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | Next action: reviewer decides whether `agent operation trace integrity` should compare a worker-execution sub-range against the worker return's own trace block instead of the dispatcher's dispatch-authoring trace block; this worker makes no checker change. |

## Worker Experience Retrospective

WORKER_EXPERIENCE_RETRO:

frictionLevel: LOW

frictionType: GATE_SURPRISE

observedStep: running the pinned `--phase pre-closure` command against the full `dispatchBaseHead..HEAD` range, which failed at committed-range-shape preflight for the same reason already documented in literal-format gotcha 12 and already observed once in the accepted MV-1 worker return

preventiveControlCandidate: WORK_ORDER_TEMPLATE

## Epistemic Process Block

Expected Result / Prediction: extending the existing strict v1 schema
additively, with a schema-visible conditional-required clause keyed to
`task.workingMode`, would let the four context groups become mandatory for
code-mutating tasks without breaking the existing live `prepare-task` route
or its current test coverage.

Evidence Comparison: all 6 pre-existing tests pass unmodified against the
extended schema and generator. The new 29 tests confirm every Test Matrix
clause: strict positive/negative shape, exact preservation of owner/
invariant/verification content, live-versus-offline source-posture honesty,
zero network/Git-remote calls on the offline route (proven by patching the
module's sole `subprocess.run` entrypoint to fail if called), and
non-overwrite of an existing capsule on invalid offline input.

Contradiction Or Gap Disposition: no contradiction. The pinned pre-closure
autorun command's range-shape failure and the trace-manifest comparison
mismatch are both explainable by this being mid-tranche worker execution,
not implementation defects; both are reported for reviewer disposition
rather than silently worked around.

Claim Update: the capsule schema/generator/wrapper/docs now support four
task-proportional context groups and an explicit offline creation route;
this return makes no claim that external-agent coding quality has measurably
improved, no claim that capsule use is now mandatory anywhere outside the
schema's own conditional clause, and no claim of MV-3/UAA readiness.

## Claim Boundary

This return delivers exactly six paths under `WORKER_MUST_NOT_COMMIT`: the
capsule schema, its owner README, its Python generator, its focused test
module, its PowerShell wrapper, and this worker return. It implements no new
protocol, no external packet-folder write, no mandatory network refresh, no
roadmap/session/standard/hook/catalog mutation, no MV-3, no UAA, no
provider/network/live call, no public sync, and no push. It makes no
closure claim, no measured external-agent-quality-improvement claim, and no
claim that capsule use is now universally mandatory. Commit, repair-or-
accept, and continuity update remain reviewer-owned per the work order's
Reviewer Closure Conversion and Review Gate sections.

## git status --short

```text
 M docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_TASK_CAPSULE.schema.json
 M docs/reference/external_agent_review/README.md
 M scripts/Update-CVF-External-Agent-Packet.ps1
 M scripts/external_agent_packet.py
 M scripts/test_external_agent_packet.py
?? docs/reviews/CVF_EACQ_FV_MV2_EXTERNAL_AGENT_TASK_CAPSULE_CONTEXT_WORKER_RETURN_2026-08-27.md
```

## Changed Files

- `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_TASK_CAPSULE.schema.json` (modified)
- `docs/reference/external_agent_review/README.md` (modified)
- `scripts/Update-CVF-External-Agent-Packet.ps1` (modified)
- `scripts/external_agent_packet.py` (modified)
- `scripts/test_external_agent_packet.py` (modified)
- `docs/reviews/CVF_EACQ_FV_MV2_EXTERNAL_AGENT_TASK_CAPSULE_CONTEXT_WORKER_RETURN_2026-08-27.md` (new, this file)

No other path was modified, staged, or committed.

## No-Commit Statement

WORKER_MUST_NOT_COMMIT honored: this worker did not run `git add`, `git
commit`, `git push`, or any staging command at any point in this tranche.
All five modified paths remain unstaged in the working tree and this
worker-return path remains untracked. `git status --short` above is the
exact observed state after the final verification run. Commit, repair,
closure, and continuity-state update are reserved for the designated
reviewer/closer per the work order's Commit Mode And Base-Anchor Lifecycle
and Reviewer Closure Conversion sections.

## Independent Reviewer Addendum

Reviewer date: 2026-08-28

Reviewer verdict: ACCEPT_AFTER_BOUNDED_REPAIR

The worker respected the exact six-path manifest, empty-staging rule, and
no-commit boundary. Independent semantic review found two blocking defects
inside the authorized schema/helper/test scope:

1. `safeRelPath` accepted Windows absolute paths, URLs, dot-prefixed paths,
   duplicate separators, and trailing whitespace. This allowed a value to be
   schema-valid while not being a normalized repo-relative path. The reviewer
   tightened the existing schema definition and added adversarial rejection
   plus valid-path regressions.
2. `jsonschema` was imported at module scope, which made legacy
   `refresh-snapshot` and `validate-return` startup depend on a package those
   routes do not use. The reviewer moved the dependency to capsule-only lazy
   loading and added a subprocess regression that shadows `jsonschema` as
   unavailable while `validate-return` still reaches its normal
   `RETURN_FOR_REPAIR` result.

Final independent evidence:

- focused suite: 47/47 PASS;
- unsafe-path probe: Windows absolute, URL, dot, duplicate-separator,
  whitespace, and backslash forms rejected; normalized repo-relative path
  accepted;
- legacy dependency-isolation probe: PASS;
- PowerShell parser: `SYNTAX_OK`;
- worker-return fast gate including reviewer-fast: PASS;
- `git diff --check`: PASS;
- exact manifest: five modified owner/test paths plus this worker return;
- staging: empty; provider/network/live calls by reviewer: zero.

The reviewer's first dependency-isolation probe used `python -S`, which also
disabled the environment's timezone-data package and therefore tested a wider
condition than intended. It was replaced by a targeted `PYTHONPATH` shadow of
`jsonschema`; no product claim relies on the discarded probe.

This addendum supersedes the worker's 35-test count with the final 47-test
evidence. The worker's disclosed range-shape and dispatch-trace findings remain
recorded as orchestration candidates and do not widen this material tranche.
