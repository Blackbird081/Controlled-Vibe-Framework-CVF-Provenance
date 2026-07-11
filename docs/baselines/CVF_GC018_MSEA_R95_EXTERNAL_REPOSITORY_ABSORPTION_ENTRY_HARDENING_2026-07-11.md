# CVF GC-018 MSEA-R95 External Repository Absorption Entry Hardening

Memory class: FULL_RECORD

Status: DISPATCH_READY

Batch ID: MSEA-R95

Date: 2026-07-11

Dispatch base head: `1334ea465`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Make R85-style evidence discipline the default entry route when an agent begins
external repository or copied-folder absorption. Extend the existing ADIF-0014
presence checker rather than creating a second absorption mechanism.

## Scope / Target / Owner Boundary

Authorize one bounded rule/checker/test/reference hardening. The worker may add
one exact `External Repository Absorption Entry Control` block contract, expand
the existing trigger to source mirrors and explicit external-repository intake,
and document the route in existing front doors.

## Decision / Baseline / Proposed Tranche

Current controls are strong after an absorption artifact exists, but ADIF-0014
only triggers on two legacy prefixes. R95 closes the pre-artifact recognition
gap while preserving all existing corpus, source-mirror, overlap, value and
review semantics.

## Evidence / Verification

Verification requires focused unit tests for legacy paths, source mirrors,
external repository/copied-folder intent, unrelated prose, archival exclusion,
required entry block fields, and existing two-block compatibility.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R95 --title "External Repository Absorption Entry Hardening" --date 2026-07-11 --base 1334ea465 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker dispatch plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Added existing-checker extension, exact entry block, protected-path authorization, focused trigger tests, and no-new-mechanism boundary. |
| checkerReadAheadConfirmation | dispatch, core-guard, blind-spot, structural, handoff, worker-return, trace and Delta checkers read |
| docOnlyNewFields | `External Repository Absorption Entry Control` fields are new documentation control fields; they do not change runtime schemas. |
| claimBoundary | Dispatch authority only. |

## Dependency Release Evidence

| Dependency | Artifact | Commit | Final disposition | Status |
|---|---|---|---|---|
| R85 terminal absorption model | R85 completion review | `6872dbc94` | REVIEWER_ACCEPTED_BOUNDED | PASS |
| R94 system-chain closure | R94 completion review | `cf3187659` | REVIEWER_ACCEPTED_BOUNDED | PASS |
| operator authorization | current instruction | 2026-07-11 | harden automatic R85 entry before MAO | PASS |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| ADIF-0014 path trigger is limited to two source-prefix constants | VALUE_SET | `governance/compat/check_absorption_blindspot_control_presence.py` | `ABSORPTION_SOURCE_PREFIXES` | legacy and deprecated external-clone prefixes | blind-spot presence checker | ACCEPT |
| ADIF-0014 currently requires two blocks | RUNTIME_BEHAVIOR | `governance/compat/check_absorption_blindspot_control_presence.py` | `_check_artifact` | Mandatory Blind-Spot and Corpus Completeness headings | checker | ACCEPT |
| focused unit-test owner exists | EXISTS | `governance/compat/test_check_absorption_blindspot_control_presence.py` | test classes | content trigger and integration tests | unittest suite | ACCEPT |
| source-mirror route is canonical | VALUE_SET | `docs/reference/external_agent_review/README.md` | Authoring Flow | `.private_reference/source_mirrors/INDEX.md` | external absorption front door | ACCEPT |
| R85 per-file terminal model exists | VALUE_SET | `docs/reference/CVF_MSEA_R85_GOP_Y_CVF_SOURCE_RECONCILIATION_MATRIX_2026-07-10.md` | Corpus and Per-File Ledger | manifest plus terminal disposition | R85 reconciliation owner | ACCEPT |

## Current Runtime Freshness Verification

At `1334ea465`, source-mirror paths and generic external-repository intake can
avoid the ADIF-0014 trigger. Existing downstream absorption guards do not by
themselves force a pre-dispatch entry declaration when the artifact omits their
claim language.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`implementation`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class implementation --role dispatcher --lifecycle-phase dispatch --json`

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_absorption_blindspot_control_presence.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | protected path authorization; entry control heading; source mirror; manifest; per-file ledger; overlap; value disposition; claim boundary |
| gateRunPurpose | Confirmation after source verification. |
| claimBoundary | Packet and checker-shape evidence only. |

## Core Guard Self-Protection Authorization - MSEA-R95

Authorized paths:

- `AGENTS.md`
- `governance/compat/check_absorption_blindspot_control_presence.py`

Operator authorization: harden automatic R85-style external repository entry
before continuing the parked Multi-Agent Orchestration roadmap.

Rollback boundary: revert only R95 rule/checker/test/front-door changes; retain
R85, R94 and unrelated governance behavior.

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intakeSummary | Extend existing entry recognition for external repository absorption. |
| scopeClassification | bounded governance hardening |
| riskSensitivity | R2; protected rule/checker paths |
| selectedRouteMode | MULTI_AGENT_MULTI_ROLE |
| roleSeparationBasis | worker implements without commit; independent reviewer validates and closes |
| escalationCondition | new checker, runtime/provider behavior, public-sync, or semantic weakening |

## Dual Agent Surface Matrix

| Agent surface | Role | Interface | Authority and risk boundary | Required evidence | Adapter boundary and disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | worker and reviewer | rule, existing checker/test, front doors, gates | exact R95 paths only | focused tests, fixtures, full gates | native route; ALLOWED |
| EXTERNAL_AGENT_CLI_MCP | external worker surface | governed work order | must receive same entry rule; no hidden authority | worker return and internal review | no runtime adapter; DOCUMENTED_ONLY |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance hardening; public-sync requires separate
review after accepted material closure.

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

## Claim Boundary

R95 authorizes entry recognition and machine enforcement only. It does not
perform an absorption, clone a repository, change provider/runtime behavior,
create a second checker, reopen R85 findings, or start MAO implementation.
