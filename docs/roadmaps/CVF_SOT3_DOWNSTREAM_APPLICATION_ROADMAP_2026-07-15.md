# CVF SOT3 Downstream Application Roadmap

Memory class: FULL_RECORD

Status: OPERATOR_AUTHORIZED_T0_QUEUED

docType: roadmap

Date: 2026-07-15

Roadmap ID: `SOT3-APP`

## Authorization / Decision

The operator authorized roadmap authoring after the intake and independent
rebuttal were classified at material commit `24d50f0d7`.

Decision: retain the application as a sibling downstream product candidate,
not CVF Core. Queue T0 packet authoring until FSCB-ADAPT-T0 has a material
closure commit so the two source families do not share one changed set.

## Purpose

Convert the 336-file SOT Application source into a source-verified, reproducible
downstream product that consumes current CVF public contracts and proves only
the exact local, runtime, or live boundary reached by each later tranche.

## Scope / Target / Owner Boundary

Source root: `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application`.

The accepted intake snapshot contains 336 files and 238,522 bytes. The source
has no local Git history or root lockfile and declares a hidden CVF workspace
clone through its `.cvf` manifest/bindings, `.env.example`, documentation, and
API configuration. Static declarations are verified; runtime use is not.

The application remains outside CVF Core. Each implementation tranche must
source-verify current Refinery, Kernel, Flow, phase, guard, evidence, and T8
owners before modifying the sibling source.

## Non-Goals

- no source mutation or application execution from roadmap authoring;
- no copy of application-local contracts into CVF Core;
- no acceptance of fixture, constant, echo-controller, or binding-presence
  checks as runtime governance proof;
- no inference that every non-`ALLOW` Flow decision has identical semantics;
- no reopening of SOT3-T8 or expansion of bounded activation proof;
- no public, production, scale, certification, shipment, or user-value claim.

## Dispatch Boundary

| Control | Decision |
|---|---|
| current active tranche | none |
| queued next packet | SOT3-APP-T0 source ledger and provenance disposition |
| scheduling release | FSCB-ADAPT-T0 material closure commit exists and worktree is clean |
| source mutation | forbidden until a later source-verified implementation work order passes pre-dispatch |
| hidden-clone coupling | T0 must sever, govern, or block every declared path |
| runtime/live | separately authorized only in tranches whose acceptance requires it |
| claim boundary | roadmap sequence only |

## Work Plan

| Tranche | Objective | Required output | Release condition |
|---|---|---|---|
| SOT3-APP-T0 | freeze application intake and provenance | 336-row terminal ledger, aggregate digest, declared hidden-clone path inventory and disposition | 336/336 terminal; zero unresolved declared clone paths; reviewer semantic audit PASS |
| SOT3-APP-T1 | ratify downstream contracts | owner map for business domain, current CVF public adapters, T8 packet binding, decision semantics, evidence, and freeze | every runtime/source symbol and decision value directly source-verified |
| SOT3-APP-T2 | harden application boundaries | identity, phase/guard decisions, all decision consumers, controller-service wiring, redaction, and freeze | negative paths and non-continuable decisions reach no output/provider lane |
| SOT3-APP-T3 | establish reproducible build and real tests | lockfile, owned package scripts, schema compatibility, request-admission tests, and behavior-path failure injection | build/typecheck/tests command-backed and non-tautological |
| SOT3-APP-T4 | prove Controlled Quotation locally | real local source-to-freeze-impact-recall slice with replayable receipts | complete identifier/evidence chain survives replay |
| SOT3-APP-T5 | optional operational/live proof | separately authorized real-provider and release evidence | exact bounded claim only; no production or universal SOT3 inference |

Each tranche after T0 requires accepted predecessor evidence, fresh GC-018, a
source-verified work order, and a clean dispatch base.

## Acceptance Criteria

- T0 reconciles all 336 files before any source mutation.
- Hidden-clone declarations receive path, owner, version/drift, and runtime-use
  dispositions.
- Application-local duplicates are rejected or rewritten against current CVF
  owners; interface presence is never proof of integration.
- T1 ratifies one explicit continuation matrix for `ALLOW`, `WARN`,
  `ESCALATE`, `BLOCK`, and `REVIEW_REQUIRED` across every consumer.
- T2 negative paths demonstrate that blocked or non-continuable requests create
  no output or provider action.
- T3 tests invoke production behavior rather than preassigned constants.
- T4 and T5 retain full identifier, receipt, evidence, and replay boundaries.
- No tranche broadens closed SOT3 claims.

## Verification Evidence

Evidence progresses by tranche: filesystem manifest and hashes in T0; direct
source verification in T1; focused negative behavior tests in T2; reproducible
build/typecheck/test commands in T3; local replay receipts in T4; and mandatory
real-provider governance proof only if T5 is separately dispatched. Mock or
fixture evidence cannot satisfy governance behavior claims.

## Stop Conditions

Stop and return to the orchestrator when:

- the 336-file snapshot drifts without a fresh manifest;
- hidden-clone ownership or version pinning cannot be established;
- a claimed current CVF symbol is missing or contradicts the work order;
- an implementation tranche would duplicate CVF Core authority;
- a failed live run lacks the mandatory secret-safe diagnostic;
- completion would require an unowned public, runtime, checker, package, or
  session-state expansion.

## Dependency And Sequence Control

Material commit `24d50f0d7` releases roadmap authoring. SOT3-APP-T0 packet
authoring is queued behind the concrete scheduling condition in Dispatch
Boundary; this is cross-batch isolation, not a semantic dependency on the
Four-Surface doctrine result.

No later tranche is released by this roadmap table alone.

## Reverse Architecture Projection Matrix

| Accepted value group | Catalog/GAP owner check | Disposition before closure | Target source | Claim class | Evidence |
|---|---|---|---|---|---|
| downstream SOT product owner | current as-built catalog | `DEFER_PENDING_ACCEPTANCE` | existing entity or proposed GAP after T1 | downstream product candidate | T0 ledger and T1 owner map |
| application runtime gaps | current runtime owners and GAP registry | `DEFER_PENDING_ACCEPTANCE` | existing owner update or proposed GAP | runtime candidate | later source and behavior proof |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | roadmap and future governed tranche artifacts | no source mutation without released work order | per-tranche evidence | repository and sibling-source operations only as authorized | `PROPOSED` |
| `EXTERNAL_AGENT_CLI_MCP` | no downstream adapter ratified | no external ingress or execution claim | explicit no-adapter boundary | fresh adapter roadmap required | `DEFERRED_WITH_REASON` |

## External Repository Absorption Entry Control

| Field | Value |
|---|---|
| Source type | downstream copied-folder application |
| Upstream or source-mirror disposition | `LOCAL_OPERATOR_AUTHORED_INPUT_WITHOUT_UPSTREAM`; no local Git provenance exists |
| Enumeration or manifest plan | future T0 direct recursive enumeration with relative path, bytes, and SHA-256 |
| Per-file terminal-ledger plan | one row for each of 336 files using READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, or BLOCKED_UNREADABLE |
| Owner or overlap route | T1 maps accepted groups to current SOT3, package, runtime, evidence, and product owners |
| Value-disposition route | ABSORB, ADAPT, DEFER, REJECT, BLOCK, or NO_NEW_VALUE plus reviewer semantic audit |
| Claim boundary | queued roadmap only; no source mutation or absorption completion |

## Mandatory Blind-Spot Control Block

| Field | Disposition |
|---|---|
| Trigger source | operator-named downstream copied folder |
| Control disposition | APPLICABLE |
| Corpus completeness section | PRESENT |
| Completeness trigger model | exact 336-file enumeration plus terminal per-file ledger |
| Blind-spot prevention action | preserve paths/digests and audit rejected/no-new-value groups |
| Residual gap | all 336 terminal decisions remain open |
| Blind-spot verdict | PARTIAL_PENDING_T0_LEDGER |

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | literal sibling source root in Scope / Target / Owner Boundary |
| Enumeration command | future filesystem-backed direct recursive `Get-ChildItem` enumeration |
| Manifest artifact or inline manifest | inline 336-file/238,522-byte snapshot; future T0 ledger |
| Processing ledger artifact or inline ledger | inline Work Plan and Corpus Completeness And Report Integrity sections; future T0 file-level ledger path is fixed by its work order |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | inline Overlap And Novelty Classification table plus `docs/reference/sot_three_layer/README.md` |
| Unresolved items | 336 file-level terminal decisions |
| Completion claim boundary | queued roadmap only; no absorption completion or runtime claim |

## Corpus Completeness And Report Integrity

- Corpus task class: downstream SOT application intake and productization.
- Corpus root: literal sibling source root in Scope / Target / Owner Boundary.
- Snapshot time: 2026-07-15 intake snapshot.
- Enumeration command: future filesystem-backed direct recursive `Get-ChildItem` enumeration.
- Manifest artifact or inline manifest: inline 336-file and 238,522-byte snapshot.
- Manifest hash: future T0 must compute per-file SHA-256 and aggregate digest.
- Processing ledger artifact or inline ledger: future T0 file-level ledger.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE
- Reconciliation: manifest=336; ledger_terminal=0; exclusions=0; unresolved=336.
- Unresolved files: 336.
- Declared exclusions: none.
- Unreadable or unsupported files: none observed during intake.
- Aggregation check: 336 files and 238,522 bytes in accepted intake snapshot.
- Drift check: T0 recomputes paths, counts, bytes, and hashes.
- Output traceability: source path, digest, status, disposition, owner, and reason.
- Adversarial verification: roadmap authorization is not source or product proof.
- Corpus verdict: PARTIAL

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| business/domain model | scoped authority, context, output, freeze, impact, and recall | `PACKAGE_CANDIDATE` | downstream application owner | T1 owner ratification | no package activation |
| CVF ports and workflows | fail-closed integration intent | `RUNTIME_CANDIDATE` | current CVF owners | T1 compatibility design | no runtime claim |
| governance-shaped source paths | decision and evidence boundary intent | `CHECKER_CANDIDATE` | existing behavior/guard owners | classify only if an owner gap remains | no checker wiring |
| duplicated local contracts and fixture proof | negative compatibility evidence | `REJECT_DIRECT_IMPORT` | T1/T3 repair ledger | rewrite or reject | no proof reuse |
| generated tree and repeated summaries | navigation only | `NO_PACKAGE_OR_RUNTIME_VALUE` | retained provenance input | confirm in T0 | no package/runtime value |
| scoped product workflow | potential doctrine and product value | `DOCTRINE_ADAPTED` | downstream application roadmap | retain bounded sequence | no CVF Core promotion |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| three-layer core contracts | `docs/reference/sot_three_layer/README.md` | `CONFIRMED_EXISTING` | application must consume, not own | source-verify in T1 |
| T8 packet binding | `EXTENSIONS/CVF_REFINERY/src/packet-hash/packet-hash.ts` | `REJECT_DIRECT_IMPORT` | local packet-ID-only path is insufficient | replace through compatibility design |
| scoped downstream product | `OWNER_SURFACE_NOT_FOUND` | `OWNER_SURFACE_NOT_FOUND` | potential new sibling product owner | decide after T0/T1 |
| copied controller/UI scaffold | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | `REJECT_DIRECT_IMPORT` | reference shell lacks current binding proof | harden only in sibling source |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External repo or copied folder |
| Chain map route | intake authorization -> queued SOT3-APP roadmap -> future T0 GC-018/work order -> file ledger -> contract ratification -> bounded implementation |
| Matching local-view guard | `governance/compat/check_absorption_blindspot_control_presence.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_corpus_completeness_report_integrity.py` |
| Owner surface | this roadmap until a T0 completion review selects the application owner route |
| Disposition | PACKAGE_CANDIDATE and RUNTIME_CANDIDATE; reject direct import |
| Claim boundary | queued roadmap only |

## Epistemic Process Block

Expected Result / Prediction: the source contains useful downstream product
semantics but requires provenance freeze, contract replacement, and real
behavior evidence before any product claim.

Evidence Comparison: intake found packet-ID-only Kernel binding, fixture-only
quotation proof, repeated `BLOCK`-only decision checks, incomplete freeze data,
reference controllers, missing lockfile, and declared hidden-clone paths.

Contradiction Or Gap Disposition: T0/T1 must record source contradictions as
blocked rows or proposed owner gaps rather than guessing current CVF contracts.

Claim Update: operator authorization opens roadmap sequencing only; T0 packet
authoring remains queued and source mutation remains unauthorized.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_absorption_blindspot_control_presence.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py` |
| literalTokensReviewed | Authorization / Decision; Purpose; Scope; Non-Goals; Dispatch Boundary; Work Plan; Acceptance Criteria; Verification Evidence; External Repository Absorption Entry Control; Mandatory Blind-Spot Control Block; External Absorption Core; External Absorption Value Conversion Matrix; Overlap And Novelty Classification; External Knowledge Intake Routing; PARTIAL; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirmation of queued roadmap and external-absorption shape |
| claimBoundary | structural confirmation only; no source, runtime, or product proof |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private sibling-source roadmap; no public-sync authorization or
public-safe artifact set exists.

## Claim Boundary

This roadmap records an operator-authorized sequence and a concrete T0 packet-
authoring queue condition. It does not dispatch T0, authorize source mutation,
complete the 336-file ledger, ratify application contracts, prove build/runtime/
live behavior, promote the application into CVF Core, or claim public or
production readiness.
