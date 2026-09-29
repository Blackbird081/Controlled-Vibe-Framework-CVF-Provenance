# CVF Agent Work Order - MSEA-R72D Governance Cost Metric And Monthly Readout

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: MSEA_R72D_GOVERNANCE_COST_METRIC_AND_MONTHLY_READOUT

Dispatch base head: 194e98ae4

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker

Reviewer/closer: reviewer/closer role

Worker return path: `docs/reviews/CVF_MSEA_R72D_GOVERNANCE_COST_METRIC_AND_MONTHLY_READOUT_WORKER_RETURN_2026-07-08.md`

## Dispatch Prompt Envelope

Role: delegated worker for MSEA_R72D_GOVERNANCE_COST_METRIC_AND_MONTHLY_READOUT.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R72D_GOVERNANCE_COST_METRIC_AND_MONTHLY_READOUT_2026-07-08.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: artifact date is 2026-07-08. The R72B checker
lifecycle inventory, the R72C case matrix, and the R72C1 checker repair
are accepted inputs. Public GitHub Actions status is drift-prone; if the
worker cites a current public CI status value, it must refresh it
read-only at execution time rather than trusting a cached R72A figure.

Do-not-misread notes: this work order authorizes a metric specification
and monthly readout design only. It does not authorize metrics automation
implementation, any new checker, any checker or hook edit, any Fast Lane
standard edit, public-sync mutation, merge, push, provider/live proof,
product extraction, onboarding changes, or release claims.

Required first actions: read required startup files, guard orientation,
literal gotchas, this packet, the paired GC-018 baseline, the R72 roadmap,
the Governance Control Index README and index, the R72B inventory, the
R72C case matrix, the R72C1 repair record, the critical repository
boundary, the commit steward standard, and all checker source listed in
the Checker Source Read-Ahead Block before writing any artifact.

Return contract: create the worker-owned metric-specification artifact and
worker return, run required gates, leave changes uncommitted, and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Execute a bounded no-commit R72D tranche. The worker must define a stable,
reproducible governance cost metric specification covering product-source
touches, governance-artifact touches, checker additions and deletions,
public CI status, and a ceremony ratio, using the Governance Control Index
metric boundary and the R72B/R72C evidence as input, then propose a
monthly readout design and a candidate script-or-checker implementation
decision. The worker must not implement any metric-computation automation.

## Scope / Target / Owner Boundary

Allowed worker-owned outputs in this provenance workspace:

- `docs/reference/CVF_MSEA_R72D_GOVERNANCE_COST_METRIC_AND_MONTHLY_READOUT_SPECIFICATION_2026-07-08.md`
- `docs/reviews/CVF_MSEA_R72D_GOVERNANCE_COST_METRIC_AND_MONTHLY_READOUT_WORKER_RETURN_2026-07-08.md`

Allowed no-commit investigation scope:

- read the Governance Control Index Baseline Measurement and Metric
  Boundary sections to confirm the direct checker-script counting rule;
- read the R72B inventory's wiring-scan methodology and its own disclosed
  self-correction rounds as evidence for why each metric definition in
  this tranche must name an exact, reproducible command;
- read the R72C case matrix's ceremony-cost proxy methodology and its own
  disclosed evidence limit;
- run read-only commands such as `git log`, `git diff --stat`,
  `Get-ChildItem`, and `rg` to test whether each proposed metric can
  actually be computed from the current repository state without an
  unstable assumption;
- optionally refresh public-main GitHub Actions status read-only via `gh
  run list` only if the worker chooses to cite a current public CI status
  value; this is not required if the worker instead cites the existing
  R72A-classified figure with its date and commit;
- produce one combined metric-specification-plus-readout-design artifact;
- mark any metric that cannot be computed reproducibly as
  `METRIC_NOT_REPRODUCIBLE_WITH_REASON` inside the artifact instead of
  asserting an unstable definition;
- recommend a candidate script-or-checker implementation only as a future
  R72D-follow-up input, not as implemented state.

Forbidden scope:

- no worker commit;
- no metrics-automation implementation, no new script, no new checker, no
  scheduled job, no generated-aggregate wiring;
- no checker severity change, deletion, disablement, retirement,
  consolidation, rename, source edit, test edit, or hook edit;
- no Fast Lane guard or audit-template edit;
- no public-sync file creation, edit, staging, commit, push, PR action, or
  public release claim;
- no runtime/source/test edit outside the two worker-owned documentation
  outputs;
- no provider/live proof, secrets, paid quota, or live governance proof
  beyond an optional read-only `gh run list` for current public CI status;
- no product extraction, operator onboarding implementation, or
  use-case/legal workflow change;
- no private/generated MinerU output read;
- no session/front-door/handoff edit by the worker.

## Worker Autonomy / No-Question Rule

Worker must repair allowed-scope formatting, specification-shape, and
worker-return packet defects directly by reading the failing checker
source and matching the literal required shape. Worker must not treat
allowed-scope machine-gate failures as preference questions. If a proposed
metric cannot be computed reproducibly from git or GitHub without an
unstable assumption, if the readout design would require editing a checker
or standard, or if a gate fails outside allowed repair scope, return
`BLOCKED_WITH_REASON` with exact source-backed evidence.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA_R72D_GOVERNANCE_COST_METRIC_AND_MONTHLY_READOUT --title "MSEA-R72D Governance Cost Metric And Monthly Readout" --date 2026-07-08 --base 194e98ae4 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Filled R72D route, metric-boundary scope, R72B/R72C/R72C1-input boundary, worker outputs, no-automation constraints, source-verification rows, and specification acceptance criteria. |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_rescan_intelligence_hardening.py` |
| docOnlyNewFields | R72D governance cost metric specification artifact; monthly readout design; per-metric reproducibility evidence; candidate script/checker decision; ceremony-ratio definition |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_rescan_intelligence_hardening.py` |
| literalTokensReviewed | section name: Dispatch Prompt Envelope; section name: Source Verification Block; section name: ADIF Defect Registry Disclosure; section name: Checker Source Read-Ahead Block; section name: Agent Handoff Contract Control Block; section name: Reviewer Closure Conversion; section name: Worker Return Packet Shape Contract; enum: DISPATCH_READY; enum: WORKER_MUST_NOT_COMMIT; enum: DEFERRED_PRIVATE_ONLY; field: completionReviewPath; field: reviewerOwnedClosurePaths; source-not-found disposition spelling |
| gateRunPurpose | Confirmation evidence before dispatch; not first discovery. |
| claimBoundary | Read-ahead covers R72D dispatch artifacts only; worker-created output must perform its own checker read-ahead before writing. |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order-authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class work-order-authoring --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | No ADIF defectId is required for this exact resolver query. |

## 5. Required First Reads

| File | Required action |
| --- | --- |
| `CVF_SESSION_MEMORY.md` | READ |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | READ |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | READ |
| `AGENT_HANDOFF_V39_2026-07-08.md` | READ |
| `docs/reference/guard_orientation/README.md` | READ |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ |
| `docs/baselines/CVF_GC018_MSEA_R72D_GOVERNANCE_COST_METRIC_AND_MONTHLY_READOUT_2026-07-08.md` | READ |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R72D_GOVERNANCE_COST_METRIC_AND_MONTHLY_READOUT_2026-07-08.md` | READ |
| `docs/roadmaps/CVF_MSEA_R72_EA_ASSESSMENT_INTAKE_AND_GOVERNANCE_LOAD_REBALANCING_ROADMAP_2026-07-07.md` | READ |
| `docs/reference/governance_control_index/README.md` | READ |
| `docs/reference/governance_control_index/CVF_GOVERNANCE_CONTROL_INDEX.md` | READ |
| `docs/reference/CVF_MSEA_R72B_GOVERNANCE_CONTROL_CHECKER_LIFECYCLE_INVENTORY_2026-07-08.md` | READ |
| `docs/reference/CVF_MSEA_R72C_FAST_LANE_CALIBRATION_AND_RISK_CLASS_ROUTER_CASE_MATRIX_2026-07-08.md` | READ |
| `docs/reviews/CVF_MSEA_R72C1_RESCAN_GUARD_SELF_REFERENCE_FALSE_POSITIVE_REPAIR_2026-07-08.md` | READ |
| `docs/reference/CVF_AGENTS_CRITICAL_REPOSITORY_BOUNDARY_2026-06-23.md` | READ |
| `docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md` | READ |

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator instruction | operator instructed the current session to author the R72D work order from the accepted post-R72C1 state | ACCEPT |
| Current session next move | `CVF_SESSION/ACTIVE_SESSION_STATE.json` key `nextAllowedMove` names R72D GC-018/work-order authoring only | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V39_2026-07-08.md` section `Next Allowed Move` authorizes R72D specification dispatch only | ACCEPT |
| R72 roadmap | work plan row `R72D` requires Governance Cost Metric And Monthly Readout | ACCEPT |
| R72 roadmap acceptance criterion | `AC11` requires the direct checker-script baseline correction to distinguish checkers from checker tests | ACCEPT |
| Governance Control Index | Baseline Measurement and Metric Boundary sections define the reproducible checker-count spine | ACCEPT |
| R72B inventory | wiring-scan methodology and self-correction rounds are R72D input only, not re-litigated | ACCEPT_AS_INPUT |
| R72C case matrix | ceremony-cost proxy methodology is R72D input only, not re-litigated | ACCEPT_AS_INPUT |
| R72C1 repair | the false-positive repair of the rescan guard confirms the current checker behavior this specification may reference | ACCEPT_AS_INPUT |
| Public/provenance boundary | critical repository boundary standard forbids public-facing action from provenance workspace beyond optional read-only CI status refresh | ACCEPT |
| Commit steward standard | upstream commit debt is zero; normal one-material plus optional session-sync commit shape applies later | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Source roadmap location | Work-order implementation | Disposition |
| --- | --- | --- | --- |
| R72D must define stable metrics for product-source touches, governance-artifact touches, checker additions/deletions, public CI status, and ceremony ratio | `docs/roadmaps/CVF_MSEA_R72_EA_ASSESSMENT_INTAKE_AND_GOVERNANCE_LOAD_REBALANCING_ROADMAP_2026-07-07.md` section `Work Plan` row `R72D` | worker must define each named metric with an exact reproducible command or mark it a source gap | ACCEPT |
| R72D must HOLD if a metric cannot be computed reproducibly from git/GitHub without unstable assumptions | same row `R72D` fail condition | worker must return `BLOCKED_WITH_REASON` or mark the specific metric `METRIC_NOT_REPRODUCIBLE_WITH_REASON` rather than asserting an unstable definition | ACCEPT |
| AC11 requires the direct checker-script baseline correction so future metrics do not confuse checker tests with checkers | `Acceptance Criteria` row `AC11` | worker must carry forward the GCI metric boundary (direct `check_*.py` only, excluding `test_check_*.py` and support modules) into every checker-count metric in the specification | ACCEPT |
| GCI-R72 routing states R72D monthly readout uses GCI metric boundaries so checker counts are reproducible | GCI `R72 Routing` row `R72D` | specification must cite the GCI metric boundary for every checker-count-based metric | ACCEPT |
| Actual metrics automation or checker addition is a later tranche | active next move; roadmap design boundary | R72D proposes only; no script, checker, or hook is created or edited | ACCEPT |

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| intake summary | R72B inventoried the checker surface; R72C proposed a routing-design input; R72C1 repaired a discovered false positive in the rescan guard. R72D now defines the governance cost metric spine before any monthly readout automation exists. |
| scope classification | DOCUMENTATION_AND_EVIDENCE_ONLY_NO_COMMIT |
| risk sensitivity | metric-reproducibility, governance-load measurement, and checker-count-boundary sensitive |
| selected role route | MULTI_AGENT_MULTI_ROLE |
| canonical route mode | MULTI_AGENT_MULTI_ROLE |
| role separation basis | dispatcher authors packet, worker creates metric specification and worker return no-commit, reviewer/closer accepts or returns with exact source-backed defects |
| escalation condition | a proposed metric cannot be computed reproducibly, the readout design would require editing a checker or standard, or a required gate fails outside allowed repair |
| Intake type | R72 roadmap follow-up |
| Source role | dispatcher using R72 roadmap, GCI, active handoff, and R72B/R72C/R72C1 accepted evidence |
| Target role | no-commit worker for R72D source-backed metric-specification authoring |
| Routing disposition | DISPATCH_TO_NO_COMMIT_WORKER |
| Reason | R72D must produce a stable, reproducible metric spine before any later tranche implements monthly readout automation. |
| Claim boundary | This routing decision does not implement metrics automation, add a checker, mutate public-sync, or release a product claim. |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator EA critique -> R72 roadmap -> R72A/R72B/R72C accepted evidence -> R72D metric-specification dispatch |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this R72D work order and paired GC-018 baseline |
| Disposition | ADAPT the R72B/R72C evidence as bounded R72D decision input only; do not import it as ratified metric authority |
| Claim boundary | R72B/R72C evidence informs the metric-definition question, but each metric's reproducibility claim must be source-backed from a real, runnable command. |

## Agent Roles

| Role | Owner | Responsibility |
| --- | --- | --- |
| Operator | human operator | authorizes scope and later metrics-automation or checker-addition decisions if any |
| Dispatcher | dispatcher role | authors R72D baseline/work order and runs pre-dispatch gates |
| Worker | delegated worker role | tests metric reproducibility and creates the R72D specification plus worker return without committing |
| Reviewer/closer | reviewer/closer role | reviews the specification, repairs only allowed-scope defects, and owns any accepted material commit |

## Foundation Storage Layout Block

| Field | Disposition |
| --- | --- |
| Foundation path class | one new dated reference artifact under `docs/reference/` plus one worker return under `docs/reviews/` |
| Storage decision | create `docs/reference/CVF_MSEA_R72D_GOVERNANCE_COST_METRIC_AND_MONTHLY_READOUT_SPECIFICATION_2026-07-08.md` as the R72D metric-specification-plus-readout-design artifact; do not create a stable alias in this tranche |
| Reference index requirement | no index row required unless the reviewer later classifies the specification as a durable active reference; if that happens, add only one source-backed row in reviewer-owned scope |
| Existing aggregate impact | no generated JSON aggregate impact |
| Generated state impact | none; worker must not edit `CVF_SESSION/**` |
| Durable governance boundary | R72D records a metric specification and readout-design proposal only; metrics automation, checker addition, and Fast Lane widening require later tranches |

## Write Ownership

| Path or lane | Worker permission | Notes |
| --- | --- | --- |
| `docs/reference/CVF_MSEA_R72D_GOVERNANCE_COST_METRIC_AND_MONTHLY_READOUT_SPECIFICATION_2026-07-08.md` | CREATE_UNCOMMITTED | required metric-specification-plus-readout-design artifact |
| `docs/reviews/CVF_MSEA_R72D_GOVERNANCE_COST_METRIC_AND_MONTHLY_READOUT_WORKER_RETURN_2026-07-08.md` | CREATE_UNCOMMITTED | required worker return |
| `governance/compat/check_*.py` | READ_ONLY | source-read to confirm checker-count boundary only; no edits |
| `governance/toolkit/05_OPERATION/CVF_FAST_LANE_GOVERNANCE_GUARD.md` | FORBIDDEN_TO_WORKER | out of scope for R72D |
| `docs/reference/governance_control_index/**` | READ_ONLY | metric spine only; no edits |
| `docs/reference/CVF_MSEA_R72B_GOVERNANCE_CONTROL_CHECKER_LIFECYCLE_INVENTORY_2026-07-08.md` | READ_ONLY | accepted input only; no edits |
| `docs/reference/CVF_MSEA_R72C_FAST_LANE_CALIBRATION_AND_RISK_CLASS_ROUTER_CASE_MATRIX_2026-07-08.md` | READ_ONLY | accepted input only; no edits |
| `CVF_SESSION_MEMORY.md`, `CVF_SESSION/`, `AGENT_HANDOFF_V39_2026-07-08.md` | FORBIDDEN_TO_WORKER | reviewer/session-sync steward only after acceptance |
| public-sync files | FORBIDDEN_TO_MUTATE | no create, edit, stage, commit, or push |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | dispatcher -> no-commit worker -> reviewer/closer |
| phase | dispatch |
| baseHeadFor(phase) | dispatchBaseHead=194e98ae4; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | dispatch author changes only the R72D GC-018 baseline and R72D work order; worker may create only the R72D specification and worker return uncommitted |
| traceScope(phase, actor) | R72D work order Agent Operation Trace Block for dispatch; worker return Agent Operation Trace Block for execution |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer/closer owns any accepted material commit |
| crossBatchIsolation | upstream ahead count is zero at dispatch; worker must preserve one-batch-per-worktree discipline and leave HEAD unchanged |
| nextMoveSurfaces | reviewer/session-sync steward updates front door, active state, and handoff only after accepted R72D return |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_MSEA_R72D_GOVERNANCE_COST_METRIC_AND_MONTHLY_READOUT_COMPLETION_2026-07-08.md` (optional; prefer repairing evidence in the worker return unless a separate completion packet is required) |
| reviewerOwnedClosurePaths | `docs/reference/CVF_MSEA_R72D_GOVERNANCE_COST_METRIC_AND_MONTHLY_READOUT_SPECIFICATION_2026-07-08.md`; `docs/reviews/CVF_MSEA_R72D_GOVERNANCE_COST_METRIC_AND_MONTHLY_READOUT_WORKER_RETURN_2026-07-08.md`; session state/front door/handoff only after reviewer acceptance |
| closureOwner | reviewer/closer role |
| workerCommitPermission | FORBIDDEN |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: none in R72D worker execution. GCI,
checker-count, and CI-status surfaces are read-only specification inputs.

Protected paths:

| Path | Purpose |
| --- | --- |
| N/A with reason | R72D does not authorize edits to `governance/compat`, hook catalogs, Fast Lane guard/template, `AGENTS.md`, or session-state paths. |
| `CVF_SESSION_MEMORY.md` | protected session front door; worker must not edit |
| `AGENT_HANDOFF_V39_2026-07-08.md` | protected active handoff; worker must not edit |

Operator authorization: operator instructed the current session to author
the R72D work order from the accepted post-R72C1 state. This does not
authorize implementation beyond worker-owned evidence artifacts, metrics
automation, checker edits, public push, public-sync mutation, or GitHub
merge.

Rollback boundary: revert only this R72D dispatch pair if rejected; do not
revert prior R72C1 repair, R72C acceptance, R72B acceptance, R72A
acceptance, R72 GCI front door, R72 roadmap, or the assessment input unless
separately requested.

## 6. Pre-Flight Checks

1. Capture provenance `executionBaseHead` with `git rev-parse --short HEAD`.
2. Run provenance `git status --short --branch`.
3. Run provenance `git remote -v` and confirm it is the provenance repository.
4. Confirm upstream commit debt with `git log --oneline "HEAD@{upstream}..HEAD"`.
5. Read the GCI Baseline Measurement and Metric Boundary sections, the R72B inventory, the R72C case matrix, and the R72C1 repair record before drafting.
6. Test each proposed metric definition against a real, runnable command before including it as reproducible.
7. Confirm no merge, push, commit, public-sync mutation, checker edit, Fast Lane standard edit, or metrics-automation implementation is performed.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Current session next move authorizes fresh R72D packet authoring only | VALUE_SET | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | key `nextAllowedMove` | nextAllowedMove | active session state | ACCEPT |
| R72D must not implement metrics automation or edit checkers/hooks/Fast Lane standards | VALUE_SET | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | key `nextAllowedMove` | R72D forbidden actions | active session state | ACCEPT |
| R72D must HOLD if a metric cannot be computed reproducibly without unstable assumptions | VALUE_SET | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | key `nextAllowedMove` | R72D hold condition | active session state | ACCEPT |
| R72D deliverable is Governance Cost Metric And Monthly Readout | EXISTS | `docs/roadmaps/CVF_MSEA_R72_EA_ASSESSMENT_INTAKE_AND_GOVERNANCE_LOAD_REBALANCING_ROADMAP_2026-07-07.md` | section `Work Plan` row `R72D` | R72D | R72 roadmap | ACCEPT |
| AC11 requires the direct checker-script baseline correction distinguishing checkers from checker tests | EXISTS | `docs/roadmaps/CVF_MSEA_R72_EA_ASSESSMENT_INTAKE_AND_GOVERNANCE_LOAD_REBALANCING_ROADMAP_2026-07-07.md` | section `Acceptance Criteria` row `AC11` | AC11 | R72 roadmap | ACCEPT |
| GCI metric boundary keeps direct checker-script counts separate from checker tests and support modules | EXISTS | `docs/reference/governance_control_index/CVF_GOVERNANCE_CONTROL_INDEX.md` | section `Baseline Measurement`; metric-boundary paragraph | direct checker scripts | Governance Control Index | ACCEPT |
| GCI R72 routing states R72D monthly readout uses GCI metric boundaries so checker counts are reproducible | EXISTS | `docs/reference/governance_control_index/CVF_GOVERNANCE_CONTROL_INDEX.md` | section `R72 Routing` row `R72D` | monthly readout | Governance Control Index | ACCEPT |
| R72B inventory's own wiring-scan methodology disclosed two self-correction rounds | EXISTS | `docs/reference/CVF_MSEA_R72B_GOVERNANCE_CONTROL_CHECKER_LIFECYCLE_INVENTORY_2026-07-08.md` | section `Finding-To-Governance Learning Disposition` | wiring-scan bugs | R72B inventory | ACCEPT |
| R72C case matrix used worker-return line count as a disclosed ceremony-cost proxy with an explicit evidence limit | EXISTS | `docs/reference/CVF_MSEA_R72C_FAST_LANE_CALIBRATION_AND_RISK_CLASS_ROUTER_CASE_MATRIX_2026-07-08.md` | section `Methodology And Evidence-Limit Disclosure` | ceremony-cost proxy | R72C case matrix | ACCEPT |
| R72C1 repaired a self-reference false positive in the rescan guard at commit `3cad26401` | EXISTS | `docs/reviews/CVF_MSEA_R72C1_RESCAN_GUARD_SELF_REFERENCE_FALSE_POSITIVE_REPAIR_2026-07-08.md` | file present | rescan guard repair | R72C1 repair record | ACCEPT |
| Public-facing changes must use the sibling public-sync clone and remote verification | EXISTS | `docs/reference/CVF_AGENTS_CRITICAL_REPOSITORY_BOUNDARY_2026-06-23.md` | section `Critical Repository Boundary - 2026-05-09` | public-sync clone | critical repository boundary standard | ACCEPT |
| Work order template requires dispatch envelope and source-verification surfaces used here | EXISTS | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | sections `Dispatch Prompt Envelope Placement Rule` and `Source Verification Block` | Dispatch Prompt Envelope | work order template | ACCEPT |
| No-commit work orders must include Reviewer Closure Conversion | EXISTS | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | no-commit and review gate guidance | Reviewer Closure Conversion | work order template | ACCEPT |
| ADIF resolver returned no defects for this dispatch-authoring query | RUNTIME_BEHAVIOR | canonical-contract marker: `governance/compat/run_adif_defect_resolver.py` | command output recorded in this packet | NONE_RETURNED | ADIF resolver invocation | ACCEPT |

## Dispatch Evidence Snapshot

| Evidence item | Command or source | Observed result | Disposition |
| --- | --- | --- | --- |
| Dispatch base head | `git rev-parse --short HEAD` | `194e98ae4` | COMMAND_VERIFIED |
| Provenance remote | `git remote -v` | `origin` points to the provenance repository | COMMAND_VERIFIED |
| Provenance branch status | `git status --short --branch` | branch `codex/p1-p5-small-debt-remediation` even with upstream | COMMAND_VERIFIED |
| Upstream commit debt | `git log --oneline "HEAD@{upstream}..HEAD"` counted with `Measure-Object -Line` | `0` unpushed commits | COMMAND_VERIFIED |
| Direct checker count | `ls governance/compat/check_*.py` counted | `186` | COMMAND_VERIFIED |
| R72B/R72C/R72C1 accepted artifacts present | `Test-Path` on each accepted input path | all present | COMMAND_VERIFIED |

## Required Metric Specification Schema

The specification artifact must include these fields per metric or a
source-backed reason why a metric cannot be defined:

| Field | Required meaning |
| --- | --- |
| metricName | one of: product-source touches, governance-artifact touches, checker additions, checker deletions, public CI status, ceremony ratio, or a worker-proposed additional metric with justification |
| metricDefinition | the exact quantity being counted, in plain language |
| computationCommand | the exact, runnable git/GitHub/filesystem command that computes the metric |
| reproducibilityEvidence | direct output from running the command against the current repository state, or `METRIC_NOT_REPRODUCIBLE_WITH_REASON` |
| boundaryNote | how the metric respects the GCI metric boundary (for example, excluding `test_check_*.py` from checker counts) |
| readoutCadence | proposed reporting cadence, for example monthly, and what triggers a reading |
| candidateImplementation | a candidate script or checker name for future automation, marked explicitly as not yet implemented |

## Required Specification Principles

| Principle | Worker instruction |
| --- | --- |
| Reproducibility over convenience | A metric is included only if its computation command was actually run against the current repository and produced a real, cited result; a plausible-sounding but unverified command is not sufficient. |
| Preserve the GCI metric boundary | Every checker-count-based metric must explicitly exclude `test_check_*.py` and non-`check_*.py` support modules, per AC11 and the GCI Metric Boundary paragraph. |
| Ceremony ratio must be defined, not asserted | The ceremony-ratio metric must state its numerator and denominator explicitly (for example, gate-shape repair rounds over total worker-return line count, or a similar source-backed formula) rather than a vague qualitative claim. |
| Propose, do not implement | R72D may propose a monthly readout design and a candidate script or checker, but must not create or edit any script, checker, or hook. |
| Do not guess | A metric that cannot be computed reproducibly must become a source-gap row or `BLOCKED_WITH_REASON`, not a confident but unstable definition. |

## Execution Plan

| Step | Action | Evidence |
| --- | --- | --- |
| 1 | Capture `executionBaseHead`, git status, and upstream commit debt | command output in worker return |
| 2 | Read required startup, R72, GCI, R72B, R72C, and R72C1 sources | Source Inventory and Checker Source Read-Ahead Block |
| 3 | Draft each metric definition and test its computation command against the current repository | reproducibility-evidence cells with real command output |
| 4 | Define the ceremony-ratio formula and the monthly readout design | specification section with numerator/denominator and cadence |
| 5 | Produce the specification artifact and worker return | changed-file evidence and no-commit statement |
| 6 | Run required gates or return exact blocker | command evidence table |

## Evidence Requirements

| Requirement | Required evidence |
| --- | --- |
| Metric reproducibility | each metric's computation command actually run with cited real output, or `METRIC_NOT_REPRODUCIBLE_WITH_REASON` |
| GCI metric boundary preserved | each checker-count metric explicitly excludes checker tests and support modules |
| Ceremony ratio defined | explicit numerator/denominator formula with source-backed evidence for at least one worked example |
| Non-implementing proposal | the readout design and candidate script/checker are a proposal; no script, checker, or hook is created or edited |
| Unknowns | exact `METRIC_NOT_REPRODUCIBLE_WITH_REASON` or `HOLD_SOURCE_GAP` cell language instead of guessed metric values |
| No forbidden action | git status, git diff, and no-commit statement proving no checker/standard/source/test/public-sync/session path edit by worker |

## Verification Commands

```powershell
git rev-parse --short HEAD
git status --short --branch
git log --oneline "HEAD@{upstream}..HEAD"
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 194e98ae4 --head HEAD
git diff --name-status
```

## Acceptance Criteria

| Criterion | Required result |
| --- | --- |
| No mutation beyond worker-owned outputs | HEAD unchanged and only allowed worker-owned outputs are uncommitted |
| Metric specification present and source-backed | worker return and artifact include real computation-command output for each metric or an explicit source gap |
| GCI metric boundary preserved | every checker-count metric excludes checker tests and support modules |
| Ceremony ratio defined with a formula | numerator and denominator are explicit and source-backed |
| Readout design is a proposal only | no script, checker, or hook is created or edited |
| Unknowns marked honestly | source gaps use the exact source-gap token, not guessed values |
| No public/runtime overclaim | no public release, production, provider/live, runtime behavior, metrics-automation, or checker-addition claim is made |

## Review Gate

Reviewer/closer must not accept R72D unless the worker return preserves
no-commit execution; includes a source-backed metric specification with
real computation-command output for each metric; preserves the GCI metric
boundary for every checker-count metric; defines the ceremony ratio with
an explicit formula; keeps the readout design a proposal with no script,
checker, or hook edit; records commit-stack debt and does not add a new
commit without a plan; and passes the worker-return fast gate and
pre-implementation autorun gate or returns a source-backed block reason.

## Closure Checklist

| Item | Required disposition |
| --- | --- |
| Worker-owned artifacts present | PASS or BLOCKED with exact reason |
| Metric specification source-backed with real command output | PASS or BLOCKED with exact reason |
| GCI metric boundary preserved per metric | PASS or BLOCKED with exact reason |
| Ceremony ratio defined with explicit formula | PASS or BLOCKED with exact reason |
| No checker/standard/source/test/public-sync/session edit by worker | PASS or BLOCKED with exact reason |
| Readout design and candidate implementation are proposal only | PASS or BLOCKED with exact reason |
| Worker-return fast gate | PASS or BLOCKED with exact reason |
| Pre-implementation autorun gate | PASS or BLOCKED with exact reason |
| Commit-stack debt decision recorded | PASS, HOLD, or REJECT |
| Session-sync decision | reviewer/session-sync steward only if next move changes |

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` when the metric specification and readout
design are created at the allowed paths, every metric is either
reproducible with cited real command output or explicitly marked a source
gap, the GCI metric boundary is preserved for every checker-count metric,
the ceremony ratio has an explicit formula, required gates pass, and HEAD
remains unchanged by the worker.

Return `BLOCKED_WITH_REASON` when a required metric cannot be computed
reproducibly without an unstable assumption, the readout design would
require editing a checker or standard, a required gate fails outside
allowed repair scope, or any action would require merge, push,
implementation, Fast Lane standard edit, public-sync mutation, or
provider/live proof.

## Operator Checkpoint

No operator checkpoint is required for ordinary R72D metric-specification
completion. Return to operator before continuing if the worker concludes
that R72D cannot be completed without editing a checker or standard,
implementing metrics automation, mutating public-sync, making a public
claim, or running provider/live proof beyond the optional read-only CI
status refresh.

## Worker Output Checker Read-Ahead Mandate

Before writing each worker-owned output artifact, read checker source for
that file's docType, path family, and conditional content class.

| Output artifact | Required read-ahead result |
| --- | --- |
| worker return under reviews directory | derive exact review headings, worker-return quality terms, trace labels, delta boundary labels, corpus and value and guard-family-applicability tokens, and no-commit evidence shape before writing |
| companion reference under reference directory | derive exact reference headings such as Scope or Applies To, Target or Source, source verification, corpus and value and guard-family-applicability labels, trace, and claim-boundary labels before writing |

Literal-shape reminders: list required worker-output section names without
heading syntax in checklist prose; write source-not-found disposition
spelling in read-ahead prose; keep every required multi-word term on one
physical line so a literal substring matcher can find it; avoid an em-dash
character, a bare truncated path token, and a remote URL adjacent to the
word absorption in worker prose; wrap any literal governed-section name in
backticks rather than plain prose when citing it outside that section's own
required place, and independently run
`python governance/compat/check_rescan_intelligence_hardening.py --base
<executionBaseHead> --head HEAD --enforce` against the drafted return
before relying on the bundled fast gate alone.

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| `docs/reference/CVF_MSEA_R72D_GOVERNANCE_COST_METRIC_AND_MONTHLY_READOUT_SPECIFICATION_2026-07-08.md` | create uncommitted source-backed metric specification plus monthly readout design with the required schema, GCI metric boundary preservation, ceremony-ratio formula, candidate implementation decision, and non-implementation claim boundary |
| `docs/reviews/CVF_MSEA_R72D_GOVERNANCE_COST_METRIC_AND_MONTHLY_READOUT_WORKER_RETURN_2026-07-08.md` | create uncommitted worker return with command evidence, gates, changed files, no-commit statement, and exact hold reason if incomplete |

## Required Artifact Manifest

| Path | Required at handoff | Owner | Notes |
| --- | --- | --- | --- |
| `docs/reference/CVF_MSEA_R72D_GOVERNANCE_COST_METRIC_AND_MONTHLY_READOUT_SPECIFICATION_2026-07-08.md` | false | worker | required worker output; not present at dispatch |
| `docs/reviews/CVF_MSEA_R72D_GOVERNANCE_COST_METRIC_AND_MONTHLY_READOUT_WORKER_RETURN_2026-07-08.md` | false | worker | required worker output; not present at dispatch |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R72D_GOVERNANCE_COST_METRIC_AND_MONTHLY_READOUT_WORKER_RETURN_2026-07-08.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

executionBaseHead: the worker return must record its own executionBaseHead captured at worker start.

Required section names for the worker return, each written on its own line so a literal substring matcher finds it:

- Purpose
- Target / Source
- Scope / Methodology
- Findings / Position
- Risk / Corrective Action
- Checker Source Read-Ahead Block
- Agent Operation Trace Block
- Delta Execution Claim Boundary Control Block
- Public Export Disposition
- External Knowledge Intake Routing
- `Rescan Intelligence Hardening`
- Corpus Completeness And Report Integrity
- Finding-To-Governance Learning Disposition
- Epistemic Process Block
- Machine Closure Package
- Claim Boundary
- git status --short
- Changed Files
- Worker Experience Retrospective
- Command Evidence
- No-Commit Statement

Conditional dispositions must use `N/A with reason` where a section does not
apply. If the worker identifies a repeated checker false-positive or
micromanagement defect pattern not already represented by ADIF, the worker
must record a Finding-To-Governance Learning disposition and return the
proposed ADIF need for reviewer decision rather than silently adding broad
new rules.

## Return-To-Orchestrator Conditions Reminder

Return the exact result token `COMPLETE_PENDING_REVIEW` or
`BLOCKED_WITH_REASON` and leave all changes uncommitted.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Claude dispatcher |
| Provider or surface | Claude Code CLI, local workspace |
| Session or invocation | R72D dispatch authoring at base `194e98ae4` |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | Bash (git, ls, grep, python governance helpers), Read, Write |
| Target paths | R72D GC-018 baseline and R72D work order |
| Allowed scope source | operator instruction, active session next move, active handoff, R72 roadmap, Governance Control Index, R72B/R72C/R72C1 accepted evidence |
| Before status evidence | clean worktree for tracked files at base `194e98ae4`; upstream ahead count `0`; no R72D artifact present before authoring |
| After status evidence | R72D dispatch artifacts authored; pre-dispatch gates to run before worker dispatch |
| Diff evidence | `git status --short --untracked-files=all` and pre-dispatch gate output |
| Approval boundary | dispatch authoring only; no implementation, merge, push, public-sync mutation, provider/live proof, runtime/source/test/checker edit, Fast Lane standard edit, or metrics automation |
| Claim boundary | repo-local dispatch trace only; no OS/user attribution, runtime behavior, public-release posture, or provider behavior claim |
| Agent type | Claude |
| Invocation ID | r72d-governance-cost-metric-and-monthly-readout-dispatch-2026-07-08 |
| Expected manifest | `docs/baselines/CVF_GC018_MSEA_R72D_GOVERNANCE_COST_METRIC_AND_MONTHLY_READOUT_2026-07-08.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R72D_GOVERNANCE_COST_METRIC_AND_MONTHLY_READOUT_2026-07-08.md` |
| Actual changed set | `docs/baselines/CVF_GC018_MSEA_R72D_GOVERNANCE_COST_METRIC_AND_MONTHLY_READOUT_2026-07-08.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R72D_GOVERNANCE_COST_METRIC_AND_MONTHLY_READOUT_2026-07-08.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
| --- | --- |
| claimScope | R72D dispatch and no-commit specification assignment |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, or mandatory-wrapper behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT |
| actionEvidence | CLAIM_REJECTED_NO_ACTION |
| invocationBoundary | local governed document authoring and future read-only evidence commands only |
| interceptionBoundary | No direct interception, wrapper or proxy enforcement, runtime gate, or agent coding control is authorized |
| claimLanguage | work-order dispatches source-backed governance cost metric specification and readout-design authoring only |
| forbiddenExpansion | Do not expand into runtime, provider, live, public, package, Web, MCP, or model-router behavior, public-sync mutation, source or test or checker edits, Fast Lane standard edits, hook edits, or metrics automation without fresh source-verified authorization. |

## Public/Provenance Boundary

| Field | Value |
| --- | --- |
| Provenance repo | this workspace is the private provenance repository |
| Public-sync boundary | R72D does not read or mutate public-sync; an optional public CI status refresh uses read-only `gh run list` only |
| Export disposition | see Public Export Disposition below |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is a private provenance work order and does not change
public-sync, push public branches, or publish public artifacts. Any later
public-facing summary requires a separate public-sync governed packet.

## Claim Boundary

This work order authorizes only R72D no-commit governance cost metric
specification and monthly readout design authoring. It does not implement
or authorize metrics automation, checker severity change, checker
deletion, checker disablement, checker retirement, checker consolidation,
hook-chain edit, Fast Lane standard edit, runtime/source/test/checker edit,
public-sync mutation, merge, push, provider/live proof, product
extraction, onboarding changes, or release claims.
