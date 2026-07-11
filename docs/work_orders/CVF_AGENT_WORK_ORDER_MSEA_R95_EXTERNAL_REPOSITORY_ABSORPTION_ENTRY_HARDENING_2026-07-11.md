# CVF Agent Work Order MSEA-R95 External Repository Absorption Entry Hardening

Memory class: FULL_RECORD

Status: DISPATCH_READY

Batch ID: MSEA-R95

Date: 2026-07-11

dispatchBaseHead: `1334ea465`

executionBaseHead: WORKER_MUST_CAPTURE_AT_START

closureBaseHead: REVIEWER_MUST_CAPTURE_AT_CLOSURE

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: delegated worker for MSEA-R95.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R95_EXTERNAL_REPOSITORY_ABSORPTION_ENTRY_HARDENING_2026-07-11.md`

Paired baseline: `docs/baselines/CVF_GC018_MSEA_R95_EXTERNAL_REPOSITORY_ABSORPTION_ENTRY_HARDENING_2026-07-11.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

Current-time notes: authored 2026-07-11 at base `1334ea465`.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Do-not-misread notes: extend ADIF-0014; do not create another checker or perform
any repository absorption.

Required first actions: capture HEAD/status, complete Required First Reads, run
pre-implementation, then edit only worker-owned paths.

Return contract: COMPLETE_PENDING_REVIEW or BLOCKED_WITH_REASON; no commit.

## Purpose

Require agents to declare and satisfy R85-style entry evidence whenever a new
external repository, copied folder, or source mirror is introduced for
absorption planning.

## Authority Chain

- Operator authorization follows verified R94 material commit `cf3187659`.
- Active session state and handoff.
- R85 reconciliation model and R94 next move.
- External absorption core/front door and source-mirror index.
- Paired R95 GC-018.

## Agent Roles

Dispatcher authors packet; worker implements/tests without commit; independent
reviewer validates protected changes and commits; steward syncs only when the reviewer records an accepted material commit.

## Scope / Target / Owner Boundary

Worker-owned paths:

- `AGENTS.md`
- `docs/reference/guard_orientation/README.md`
- `docs/reference/external_agent_review/README.md`
- `governance/compat/check_absorption_blindspot_control_presence.py`
- `governance/compat/test_check_absorption_blindspot_control_presence.py`
- `docs/reviews/CVF_MSEA_R95_EXTERNAL_REPOSITORY_ABSORPTION_ENTRY_HARDENING_WORKER_RETURN_2026-07-11.md`

Required behavior:

- preserve all current legacy/external-repos triggers and two-block checks;
- trigger additionally on `.private_reference/source_mirrors/` and bounded,
  explicit external-repository/copied-folder intake language;
- require `## External Repository Absorption Entry Control` with source type,
  upstream/source-mirror disposition, enumeration/manifest plan, per-file
  terminal ledger plan, owner/overlap route, value disposition route, and claim
  boundary;
- allow an exact non-absorption disposition for comparison-only references;
- document the rule in root instructions and existing front doors;
- retain range awareness, UTF-8 subprocess handling and archive exclusion.

Forbidden scope:

- no new checker file, hook/catalog wiring, runtime, provider, Web, UI, package,
  registry taxonomy, public-sync, absorption execution, clone, commit or push;
- no weakening of corpus, overlap, value-conversion, source-mirror or reviewer
  semantic-audit requirements;
- no MAO work.

Risk ceiling: R2 protected governance hardening.

## Write Ownership

Worker owns exactly six paths. Reviewer owns completion conversion and any
required GC-051 reconciliation. Steward alone owns session paths.

## Dependency Release Evidence

| Dependency | Artifact | Commit | Status |
|---|---|---|---|
| R85 closed | R85 completion | `6872dbc94` | PASS |
| R94 closed | R94 completion | `cf3187659` | PASS |
| operator checkpoint | current instruction | 2026-07-11 | PASS |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R95 --title "External Repository Absorption Entry Hardening" --date 2026-07-11 --base 1334ea465 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker dispatch plus protected no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Added exact trigger/block contract, six-path scope, protected authorization, tests and no-new-checker boundary. |
| checkerReadAheadConfirmation | core guard, ADIF-0014, dispatch, structural, handoff, worker-return, trace, Delta sources read |
| docOnlyNewFields | entry-control fields are documentation fields enforced by the existing checker. |
| claimBoundary | Dispatch authoring only. |

## Required First Reads

1. startup front doors, active handoff, guard orientation and literal gotchas;
2. paired R95 baseline and this work order;
3. R85 source reconciliation matrix and completion;
4. external absorption front door/core/chain map and source-mirror index;
5. ADIF-0014 checker and full focused test file;
6. core guard self-protection and applicable artifact checkers.

## Legacy Absorption Coverage Index Disposition

| Field | Disposition |
|---|---|
| Coverage index requirement | NOT_APPLICABLE_WITH_REASON |
| Reason | R95 hardens the entry control for future source intake; it does not scan or absorb a legacy corpus. |
| Coverage evidence used instead | R85 terminal reconciliation model and the current ADIF-0014 checker/test source. |

## Pre-Flight Checks

Capture executionBaseHead and clean status; run ADIF query and pre-implementation
before editing. Any unrelated path or source contradiction blocks execution.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| current trigger prefixes | VALUE_SET | `governance/compat/check_absorption_blindspot_control_presence.py` | `ABSORPTION_SOURCE_PREFIXES` | two legacy prefixes | ADIF-0014 checker | ACCEPT |
| content-based trigger | RUNTIME_BEHAVIOR | `governance/compat/check_absorption_blindspot_control_presence.py` | `_artifact_references_absorption_source` | governed artifact content scan | ADIF-0014 checker | ACCEPT |
| current required blocks | VALUE_SET | `governance/compat/check_absorption_blindspot_control_presence.py` | `BLIND_SPOT_HEADING`; `CORPUS_HEADING` | two headings | ADIF-0014 checker | ACCEPT |
| existing test seam | EXISTS | `governance/compat/test_check_absorption_blindspot_control_presence.py` | test classes | trigger/check/integration seams | unittest | ACCEPT |
| source-mirror front door | VALUE_SET | `docs/reference/external_agent_review/README.md` | Authoring Flow | source mirror before full absorption | external absorption owner | ACCEPT |
| root agent rule owner | EXISTS | `AGENTS.md` | provider-memory and work-order sections | mandatory agent instruction surface | root rule | ACCEPT |

## Current Runtime Freshness Verification

The dispatcher freshly confirmed the gap at `1334ea465`. Worker must repeat the
reads and preserve existing passing fixtures before modifying triggers.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`implementation`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class implementation --role dispatcher --lifecycle-phase dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | Existing checker extension and exact tests remain mandatory. |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_absorption_blindspot_control_presence.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | protected paths; entry-control heading and fields; full worker-return profile |
| gateRunPurpose | Confirmation after direct source reading. |
| claimBoundary | Packet and checker-shape only. |

## Core Guard Self-Protection Authorization - MSEA-R95

Protected paths authorized:

- `AGENTS.md`
- `governance/compat/check_absorption_blindspot_control_presence.py`

Operator authorization: implement R85-style automatic absorption entry
hardening before Multi-Agent Orchestration work.

Rollback boundary: R95 changes only; preserve existing ADIF-0014 behavior.

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intakeSummary | Harden agent and machine recognition at external-repo absorption entry. |
| scopeClassification | protected governance implementation |
| riskSensitivity | R2 |
| selectedRouteMode | MULTI_AGENT_MULTI_ROLE |
| roleSeparationBasis | worker implements; independent reviewer validates protected diff |
| escalationCondition | new checker/hook, runtime/provider/public, or compatibility break |

## Dual Agent Surface Matrix

| Agent surface | Role | Interface | Authority and risk boundary | Required evidence | Adapter boundary and disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | worker/reviewer | root rule, checker/test, front doors | exact six-path scope | fixtures, tests, full gates | native route; ALLOWED |
| EXTERNAL_AGENT_CLI_MCP | delegated worker | governed packet | same entry contract, no hidden memory | worker return plus internal review | documented route; ALLOWED_BOUNDED |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | dispatcher authors; worker implements; reviewer/closer validates; steward syncs |
| phase | DISPATCH_AUTHORING, EXECUTION, CLOSURE, SESSION_SYNC |
| baseHeadFor(phase) | dispatchBaseHead=`1334ea465`; executionBaseHead=worker capture; closureBaseHead=reviewer capture |
| changedSetScope(phase) | packet; six worker paths; reviewer closure/registry; separate session paths |
| traceScope(phase, actor) | actor records commands, paths, status and boundaries |
| commitOwner(phase) | dispatcher commits packet; worker must not commit; reviewer commits closure; steward syncs |
| crossBatchIsolation | unrelated changes prohibited |
| nextMoveSurfaces | update only when reviewer acceptance and material commit evidence exist |

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_MSEA_R95_EXTERNAL_REPOSITORY_ABSORPTION_ENTRY_HARDENING_COMPLETION_2026-07-11.md`

reviewerOwnedClosurePaths: paired packet; six worker paths; completion review;
GC-051 entry/aggregate only if required.

closureOwner: independent reviewer/closer.

workerCommitPermission: FORBIDDEN.

## Roadmap-to-Work-Order Trace Matrix

| Requirement | Work-order owner | Evidence | Status |
|---|---|---|---|
| automatic agent entry recognition | AGENTS and front doors | exact mandatory rule | PASS |
| source mirror and intent triggers | existing checker | focused fixtures | PASS |
| R85 evidence shape | entry-control block | required field validation | PASS |
| no duplicate mechanism | checker scope | no new checker/catalog | PASS |
| compatibility | focused and full gates | legacy fixtures remain green | PASS |

## Work-Order Fulfillment Manifest

| Artifact | Required action |
|---|---|
| `AGENTS.md` | add mandatory external-repository absorption entry rule |
| `docs/reference/guard_orientation/README.md` | route task class through entry control |
| `docs/reference/external_agent_review/README.md` | document exact entry block and order |
| `governance/compat/check_absorption_blindspot_control_presence.py` | extend trigger and validate entry control |
| `governance/compat/test_check_absorption_blindspot_control_presence.py` | add positive/negative/compatibility tests |
| worker return | full no-commit evidence packet |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R95_EXTERNAL_REPOSITORY_ABSORPTION_ENTRY_HARDENING_WORKER_RETURN_2026-07-11.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Execution Plan

1. Capture HEAD/status; run pre-implementation and existing focused tests.
2. Define exact entry heading/fields with bounded comparison-only disposition.
3. Extend trigger and validation in the existing checker.
4. Add unit/integration fixtures including false positives and archives.
5. Update AGENTS and two existing front doors.
6. Run focused tests, direct checker fixtures, worker-return gate, diff hygiene.
7. Stop without commit.

## Verification Commands

```powershell
git rev-parse --short HEAD
git status --short
python -m unittest governance.compat.test_check_absorption_blindspot_control_presence
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base $executionBaseHead --head HEAD
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git status --short
```

No live proof is required; this is local governance entry hardening.

## Acceptance Criteria

- Existing triggers and fixtures remain passing.
- Source-mirror and explicit external-repo/copied-folder intake trigger.
- Comparison-only references have a narrow explicit non-absorption route.
- Entry block validates all R85 evidence-plan fields.
- AGENTS and front doors agree with checker vocabulary.
- No new checker/hook/runtime/provider/public behavior.
- Full worker return and gates pass; worker does not commit.

## Evidence Requirements

Return exact trigger vocabulary, entry fields, before/after fixture table,
focused-test counts, changed paths, gate results and no-commit evidence.

## Worker Autonomy / No-Question Rule

Proceed autonomously for allowed edits/tests and gate repairs. Return blocked
for new checker/hook needs, runtime/provider/public scope, unrelated changes,
or unavoidable false positives outside the bounded vocabulary.

## Negative And Fail-Condition Scan

Fail for broad words such as bare `repo` triggering unrelated docs, comparison
references forced into full absorption, archives checked as active artifacts,
missing entry fields, compatibility regression, provider-memory authority,
new mechanism creation, or forbidden scope.

## Review Gate

Reviewer independently tests every trigger/non-trigger fixture, inspects root
rule consistency, confirms no catalog duplication, runs reviewer-fast/full
pre-commit, and rejects any claim that this performs absorption automatically.

## Closure Checklist

- [ ] Entry rule and checker vocabulary agree.
- [ ] Legacy triggers preserved.
- [ ] Source mirror and explicit intake triggers pass.
- [ ] Comparison-only and unrelated prose do not false-trigger.
- [ ] Entry block fields enforced.
- [ ] Focused/full gates pass.
- [ ] Worker return is complete and uncommitted.

## Return-To-Orchestrator Conditions

Return COMPLETE_PENDING_REVIEW only with every acceptance item satisfied;
otherwise BLOCKED_WITH_REASON with exact source/test evidence.

## Operator Checkpoint

No checkpoint is needed inside authorized scope. New checker, hook, runtime,
provider, public-sync or MAO work requires fresh authorization.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | local private provenance repository |
| Session or invocation | MSEA-R95 dispatch authoring, 2026-07-11 |
| Working directory | repository root |
| Command or tool surface | source reads, rg, apply_patch, gates, git |
| Target paths | paired R95 baseline and work order |
| Allowed scope source | operator instruction plus R94 next move |
| Before status evidence | clean worktree at `1334ea465` |
| After status evidence | paired dispatch artifacts only |
| Diff evidence | name-status and pre-dispatch gate |
| Approval boundary | dispatch only |
| Claim boundary | no worker implementation in dispatch commit |
| Agent type | dispatcher |
| Invocation ID | msea-r95-dispatch-authoring-2026-07-11 |
| Expected manifest | paired baseline and work order |
| Actual changed set | paired baseline and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | external repository absorption entry hardening packet |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | N/A with reason: dispatch creates no runtime receipt |
| actionEvidence | ACTION_EVIDENCE_PRESENT: source verification, exact scope, tests and gates |
| invocationBoundary | local governance authoring only |
| interceptionBoundary | no provider, IDE, MCP, Web, wrapper, proxy, or runtime interception claim |
| claimLanguage | entry recognition and required planning evidence only |
| forbiddenExpansion | no absorption execution, clone, runtime, provider, public, new checker, or MAO work |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance hardening; no public-sync scope.

+## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | bounded CVF-governed R85 evidence and ADIF-0014 source/test set |
| Enumeration command | filesystem-backed direct reads plus targeted `rg -n` symbol verification |
| Manifest artifact or inline manifest | Source Verification Block |
| Processing ledger artifact or inline ledger | Source Verification Block |
| Ledger terminal statuses | ACCEPT, REJECT, BLOCKED |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | existing checker, AGENTS, Guard Orientation, and external-review front door |
| Unresolved items | 0 at dispatch |
| Completion claim boundary | entry hardening only; no repository is absorbed |

## Corpus Completeness And Report Integrity

- Corpus task class: GOVERNED_SOURCE_SET_HARDENING.
- Corpus root: named CVF-governed sources in the Source Verification Block.
- Snapshot time: 2026-07-11 local dispatch authoring.
- Enumeration command: filesystem-backed direct reads and targeted `rg -n`.
- Manifest artifact or inline manifest: Source Verification Block.
- Manifest hash: not generated; bounded named source set.
- Processing ledger artifact or inline ledger: Source Verification Block.
- Allowed terminal statuses: READ, SOURCE_VERIFIED, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.
- Reconciliation: manifest=5; ledger_terminal=5; exclusions=0; unresolved=0.
- Unresolved count: 0.
- Unresolved files: 0.
- Declared exclusions: none.
- Unreadable or unsupported files: none.
- Aggregation check: named sources reconcile to planned owners.
- Drift check: worker repeats verification at executionBaseHead.
- Output traceability: each edit maps to an owner and focused test.
- Adversarial verification: false-positive, archive, comparison-only and duplicate-checker risks covered.
- Corpus verdict: COMPLETE_VERIFIED

## Mandatory Blind-Spot Control Block

| Control | Disposition |
|---|---|
| source enumeration | bounded governed source set enumerated |
| per-file terminal status | Source Verification ACCEPT rows |
| owner routing | existing checker and front doors only |
| semantic review | independent reviewer required |
| blind-spot verdict | CLEAR_FOR_DISPATCH |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| R85 model | manifest, terminal ledger and owner disposition at entry | CHECKER_CANDIDATE | existing ADIF-0014 checker | enrich existing checker/test | no runtime/package behavior |
| absorption front door | source mirror and overlap/value route | DOCTRINE_ADAPTED | existing front doors | add exact entry order | documentation only |
| current trigger | reusable content trigger with incomplete vocabulary | CHECKER_CANDIDATE | existing checker | extend without new checker | local governance only |
| package candidates | none in R95 | PACKAGE_CANDIDATE | conditional reopen index | no package action | package activation forbidden |
| runtime candidates | none in R95 | RUNTIME_CANDIDATE | conditional reopen index | no runtime action | runtime mutation forbidden |
| direct external imports | rejected by existing doctrine | REJECT_DIRECT_IMPORT | CVF-owned surfaces only | retain rejection | no direct import |
| remaining source value | no package or runtime value in this hardening source set | NO_PACKAGE_OR_RUNTIME_VALUE | existing governance owners | close without expansion | no package/runtime behavior |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| entry guidance | external-review front door and AGENTS | ENRICH_EXISTING | pre-dispatch recognition is incomplete | enrich existing owners |
| machine trigger | ADIF-0014 checker | ENRICH_EXISTING | source mirror and explicit intake intent absent | extend existing checker |
| corpus/overlap/value rules | absorption core and existing guards | CONFIRMED_EXISTING | no new semantic rule needed | preserve and route |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external knowledge intake routing guard implementation |
| Chain map route | governed R85 lesson -> absorption core -> existing ADIF-0014 checker -> future governed intake |
| Matching local-view guard | `governance/compat/check_absorption_blindspot_control_presence.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_overlap_discipline.py` |
| Owner surface | existing ADIF-0014 checker and external-review front door |
| Disposition | ADAPT existing owners; no direct import or new checker |
| Claim boundary | entry hardening only; no external corpus is absorbed by R95 |

## Negative Search And Collision Discipline

The dispatcher searched current trigger constants, entry-control headings and
checker/test symbols directly. No source-not-found disposition remains. Generic
bare words such as `repo` are forbidden triggers; only exact source surfaces or
bounded multi-word intake patterns may activate the checker.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | existing root rule, existing reference front doors, and existing checker/test pair |
| Storage decision | edit existing owners only; create no new folder, registry, checker or aggregate |
| Existing aggregate impact | none |
| Generated state impact | none during worker execution |
| Durable governance boundary | entry control is machine-checked planning evidence, not an absorption runtime or source store |

## Claim Boundary

R95 requires R85-style planning evidence at external-repository absorption
entry. It does not itself absorb, copy, clone, execute, publish, or authorize
downstream implementation.
