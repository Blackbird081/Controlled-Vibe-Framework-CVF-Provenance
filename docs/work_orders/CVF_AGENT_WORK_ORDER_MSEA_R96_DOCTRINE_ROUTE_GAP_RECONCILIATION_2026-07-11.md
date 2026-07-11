# CVF Agent Work Order MSEA-R96 Doctrine Route Gap Reconciliation

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: MSEA-R96

Dispatch base head: `82607778a`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: delegated documentation/source-audit worker.

Canonical packet: this file.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: worker captures current HEAD at start.

Current-time notes: artifact date is 2026-07-11; refresh source evidence at execution start.

Do-not-misread notes: this is a decision pass, not doctrine or folder implementation.

Required first actions: read startup front doors, guard orientation, literal gotchas, paired baseline, required reads, and checker sources before writing.

Return contract: create all four outputs, run required gates, leave changes uncommitted, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Reconcile only doctrine layers L1, L2, L4, and L6 against current CVF-governed
owners. Produce evidence strong enough for a later reviewer to decide whether
to adapt, intentionally retain archive-only status, record a partial owner, or
retain an unresolved owner disposition.

## Authority Chain

Operator authorization -> paired GC-018 -> this work order -> frozen doctrine
and current governed sources -> worker evidence -> independent reviewer.
Legacy material is historical evidence, not authority.

## Agent Roles

- Worker: source audit and documentation outputs; must not commit.
- Reviewer/closer: semantic challenge, repairs within scope, closure commit.
- Session-sync steward: separate continuity commit following the accepted R96 material commit and completion-review evidence.

## Scope / Target / Owner Boundary

Worker-owned paths:

- `docs/audits/CVF_MSEA_R96_DOCTRINE_ROUTE_GAP_RECONCILIATION_2026-07-11.md`
- `docs/audits/CVF_MSEA_R96_DOCTRINE_ROUTE_GAP_RECONCILIATION_EVIDENCE_2026-07-11.json`
- `docs/reference/system_chain/CVF_DOCTRINE_TO_CONTRACT_ROUTE_MAP.md`
- `docs/reviews/CVF_MSEA_R96_DOCTRINE_ROUTE_GAP_RECONCILIATION_WORKER_RETURN_2026-07-11.md`

The route map may change only if evidence changes a four-row disposition or
adds a bounded decision note. No other layer row or numbering map may change.

Forbidden: legacy copying, new architecture folders, frozen doctrine edits,
runtime/tests/checkers/hooks, Web/UI, public-sync, provider/live proof, package
activation, MAO work, session state, commit, push.

## Write Ownership

Exactly the four worker-owned paths above. Existing unrelated worktree changes
cause `BLOCKED_WORKTREE_CONTAMINATION`.

## Dependency Release Evidence

| Dependency | Evidence | Commit | Disposition |
|---|---|---|---|
| R94 route findings | `docs/reviews/CVF_MSEA_R94_REMAINING_WAVE_SYSTEM_CHAIN_COMPLETION_2026-07-11.md` | `cf3187659` | SATISFIED |
| R95 entry hardening | `docs/reviews/CVF_MSEA_R95_EXTERNAL_REPOSITORY_ABSORPTION_ENTRY_HARDENING_COMPLETION_2026-07-11.md` | `8c5755051` | SATISFIED |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind source-intake --batch-id MSEA-R96 --title "Doctrine Route Gap Reconciliation L1 L2 L4 L6" --date 2026-07-11 --base 03392c2b8 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | source-intake plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Added four-row decision contract, exact outputs, evidence schema, and forbidden mutation boundary. |
| checkerReadAheadConfirmation | dispatch, worker-return, corpus, source-intake, blind-spot, trace, handoff, closure, public guards |
| docOnlyNewFields | layerId, priorDisposition, candidateOwner, responsibilityMatch, negativeSearch, finalDisposition, nextOwnerAction |
| claimBoundary | scaffold provenance only |

## Required First Reads

1. `ECOSYSTEM/doctrine/CVF_LAYER_MODEL.md`
2. `docs/reference/system_chain/CVF_DOCTRINE_TO_CONTRACT_ROUTE_MAP.md`
3. `docs/reference/system_chain/README.md`
4. `docs/reference/system_chain/CVF_SYSTEM_CHAIN_MAP.json`
5. `docs/audits/CVF_MSEA_R90_SYSTEM_CHAIN_AUDIT_A_2026-07-10.md`
6. `docs/reviews/CVF_MSEA_R94_REMAINING_WAVE_SYSTEM_CHAIN_COMPLETION_2026-07-11.md`
7. `ARCHITECTURE.md`
8. `docs/reference/CVF_ARCHITECTURE_DIAGRAMS.md`
9. `docs/reference/CVF_MODULE_INVENTORY.md`
10. `.private_reference/legacy/CVF_Restructure/CVF_ECOSYSTEM/system/CVF_PROJECT_MANIFEST.md`
11. `.private_reference/legacy/CVF_Restructure/CVF_ECOSYSTEM/protocols/CVF_AGENT_BUILD_PROTOCOL.md`

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md`
is not used as corpus authority because R96 is limited to the two explicitly
named R94 evidence files. No broad legacy scan or absorption claim is authorized.

## Pre-Flight Checks

- Confirm HEAD equals the session-dispatch execution base and worktree is clean.
- Run pre-implementation before edits.
- Confirm all required sources are readable.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| L1 frozen responsibility | VALUE_SET | canonical contract: `ECOSYSTEM/doctrine/CVF_LAYER_MODEL.md` | L1 declares `/system` | L1 - System Definition | doctrine layer map | ACCEPT |
| L2 frozen responsibility | VALUE_SET | canonical contract: `ECOSYSTEM/doctrine/CVF_LAYER_MODEL.md` | L2 declares `/protocols` | L2 - Build Protocol | doctrine layer map | ACCEPT |
| L4 frozen responsibility | VALUE_SET | canonical contract: `ECOSYSTEM/doctrine/CVF_LAYER_MODEL.md` | L4 declares `/cvf-core` | L4 - Product Implementation | doctrine layer map | ACCEPT |
| L6 frozen responsibility | VALUE_SET | canonical contract: `ECOSYSTEM/doctrine/CVF_LAYER_MODEL.md` | L6 declares `/examples` and `/docs` | L6 - Ecosystem Layer | doctrine layer map | ACCEPT |
| current four-row status | VALUE_SET | `docs/reference/system_chain/CVF_DOCTRINE_TO_CONTRACT_ROUTE_MAP.md` | L0-L6 Doctrine Route Table | L1, L2, L4, L6 | doctrine route map | ACCEPT |
| L1 historical content | EXISTS | `.private_reference/legacy/CVF_Restructure/CVF_ECOSYSTEM/system/CVF_PROJECT_MANIFEST.md` | full file | `CVF_PROJECT_MANIFEST.md` | legacy evidence | ACCEPT |
| L2 historical content | EXISTS | `.private_reference/legacy/CVF_Restructure/CVF_ECOSYSTEM/protocols/CVF_AGENT_BUILD_PROTOCOL.md` | full file | `CVF_AGENT_BUILD_PROTOCOL.md` | legacy evidence | ACCEPT |
| L4 candidate maturity | VALUE_SET | `docs/reference/CVF_MODULE_INVENTORY.md` | relevant module row | `EXTENSIONS/CVF_v3.0_CORE_GIT_FOR_AI/` | module inventory | ACCEPT |

## Current Runtime Freshness Verification

N/A with reason: read-only doctrine/source reconciliation; runtime behavior is
outside scope and must not be inferred from file existence.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`documentation`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class documentation --role dispatcher --lifecycle-phase dispatch` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | none |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_source_intake_decision_packet_preflight.py`; `governance/compat/check_absorption_blindspot_control_presence.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | source table columns; canonical input type; executionBaseHead; exact changed set; corpus fields; trace labels |
| gateRunPurpose | confirmation after source reads |
| claimBoundary | dispatch shape only; reviewer owns semantic acceptance |

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intakeSummary | Reconcile four doctrine route gaps using bounded legacy evidence and active sources. |
| scopeClassification | DOCUMENTATION_AND_EVIDENCE_ONLY_NO_COMMIT |
| riskSensitivity | R1 |
| selectedRouteMode | MULTI_AGENT_MULTI_ROLE |
| roleSeparationBasis | worker audits; independent reviewer challenges all upgraded claims |
| escalationCondition | doctrine mutation, new folder, runtime change, or source contradiction |

## Dual Agent Surface Matrix

| Agent surface | Role | Interface | Authority and risk boundary | Required evidence | Adapter boundary and disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | worker/reviewer | local repo reads and governed artifacts | bounded four-row decision | manifest, citations, negative searches | authorized documentation lane |
| EXTERNAL_AGENT_CLI_MCP | optional external reviewer | bounded evidence export | advisory only | dissent and source citations | DEFERRED; no adapter |

## Agent Handoff Contract Control Block

| Field | Value |
|---|---|
Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | delegated worker -> independent reviewer/closer -> session-sync steward |
| phase | execution then review |
| baseHeadFor(phase) | dispatchBaseHead=82607778a; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | exact four worker-owned paths |
| traceScope(phase, actor) | worker commands and manifest; reviewer independent searches and diff |
| commitOwner(phase) | reviewer/closer; worker forbidden |
| crossBatchIsolation | Before status evidence: clean worktree at `82607778a`; no MAO, T3B, R73F, R84, public, runtime, or session mixing |
| nextMoveSurfaces | reviewer-owned separate session sync following accepted material commit evidence |

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_MSEA_R96_DOCTRINE_ROUTE_GAP_RECONCILIATION_COMPLETION_2026-07-11.md`

reviewerOwnedClosurePaths: paired packet, four worker paths, completion review,
and separate session-sync surfaces.

closureOwner: reviewer/closer

workerCommitPermission: FORBIDDEN

## Roadmap-to-Work-Order Trace Matrix

| Residual gap | Worker decision required | Evidence minimum |
|---|---|---|
| L1 | active equivalent, adaptation, archive-only, or unresolved | legacy responsibility vs active owner citations |
| L2 | active equivalent, adaptation, archive-only, or unresolved | build protocol responsibility vs current workflow standards |
| L4 | prove or reject each plausible current owner | source ownership and maturity evidence; no draft promotion |
| L6 | decide docs/examples partial ownership | example responsibility and audience comparison |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| audit Markdown | four-row human decision ledger and candidate comparisons |
| evidence JSON | deterministic sourceManifest, searches, citations, counts, hash |
| doctrine route map | update only evidence-backed changed rows or append no-change decision note |
| worker return | reconcile outputs, commands, gates, status, and no-commit evidence |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R96_DOCTRINE_ROUTE_GAP_RECONCILIATION_WORKER_RETURN_2026-07-11.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Execution Plan

1. Capture HEAD/status and run pre-implementation.
2. Enumerate the bounded corpus and compute normalized manifest SHA-256.
3. Extract responsibility statements for L1/L2/L4/L6 from doctrine.
4. Compare legacy L1/L2 intent to active governed owner candidates.
5. Search and disposition all plausible L4 and L6 owners.
6. Assign exactly one terminal disposition per layer.
7. Update route map only where evidence changes or clarifies a row.
8. Reconcile Markdown/JSON, run gates, return without commit.

Allowed final dispositions:

- `ACTIVE_EQUIVALENT_OWNER_PROVEN`
- `ADAPTATION_CANDIDATE`
- `INTENTIONAL_ARCHIVE_ONLY`
- `PARTIAL_OWNER_WITH_GAP`
- `SOURCE_OWNER_UNRESOLVED_WITH_SEARCH_EVIDENCE`

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/check_system_chain_map_freshness.py --enforce
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git status --short
```

## Acceptance Criteria

- Exactly four layer rows receive terminal dispositions.
- Every upgraded owner claim has responsibility and active-authority evidence.
- L1/L2 legacy content is not copied or promoted.
- L4 draft/future modules are not treated as owners without stronger authority.
- L6 docs and example surfaces are evaluated separately.
- Independent numbering schemes remain intentionally separate.
- Markdown/JSON counts, citations, and hash reconcile.
- Exact four-path changed set; HEAD unchanged.

## Evidence Requirements

Per layer: doctrine responsibility, prior status, candidate list, positive
evidence, negative search, contradiction, final disposition, confidence
boundary, and next owner action. Search absence alone cannot prove intent.

## Worker Autonomy / No-Question Rule

Repair allowed-scope gate defects directly. Return only for a source
contradiction, forbidden mutation requirement, contaminated worktree, or a
missing authority that prevents truthful terminal disposition.

## Negative And Fail-Condition Scan

Fail for legacy promotion, guessed owner, filename-only ownership, draft L4
promotion, false numbering equivalence, missing candidate terminal records,
non-deterministic JSON, route-map changes outside four rows, forbidden paths,
commit, or public/runtime claims.

## Review Gate

Reviewer independently samples all four rows, repeats negative searches,
challenges every owner upgrade, checks exact diff, and reruns required gates.

## Closure Checklist

- [ ] Four rows terminal.
- [ ] Manifest and ledger reconcile.
- [ ] Legacy authority boundary preserved.
- [ ] Route-map diff bounded.
- [ ] Freshness remains CURRENT.
- [ ] Worker HEAD unchanged.
- [ ] Reviewer closure pending.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` for source contradiction, need to edit frozen
doctrine/runtime, unreadable required source, or inability to keep exact scope.

## Future Authorization Boundary

Any later content adaptation, new active folder, doctrine revision, or owner
promotion implementation requires a fresh packet citing the accepted R96
completion artifact and material commit.

## Operator Checkpoint

No checkpoint is pending for this read-only execution. Any later structural
mutation remains outside R96 and requires separate authorization.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | local private provenance repository |
| Session or invocation | MSEA-R96 dispatch, 2026-07-11 |
| Working directory | repository root |
| Command or tool surface | direct reads, rg, scaffold preview, apply_patch, governance gates |
| Target paths | paired GC-018 and this work order |
| Allowed scope source | user authorization to continue L1/L2/L4/L6 |
| Before status evidence | clean worktree at HEAD `82607778a`; target paths absent |
| After status evidence | two dispatch paths pending |
| Diff evidence | `git diff --name-status` |
| Approval boundary | packet authoring and dispatch only |
| Claim boundary | no worker execution or doctrine mutation |
| Agent type | dispatcher |
| Invocation ID | msea-r96-dispatch-2026-07-11 |
| Expected manifest | paired GC-018 and work order |
| Actual changed set | paired GC-018 and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | four-layer source reconciliation dispatch |
| claimDisposition | CLAIM_REJECTED: no runtime enforcement or direct interception claim |
| receiptEvidence | N/A with reason: no runtime receipt applies |
| actionEvidence | ACTION_EVIDENCE_PRESENT: source reads and dispatch gates |
| invocationBoundary | documentation/source audit only |
| interceptionBoundary | no provider, IDE, MCP, Web, proxy, or runtime interception |
| claimLanguage | authority decision evidence, not implementation |
| forbiddenExpansion | no doctrine mutation, runtime, public, provider, package, MAO, or T3B |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private doctrine-route decision tranche.

## Corpus Completeness And Report Integrity

- Corpus task class: BOUNDED_DOCTRINE_ROUTE_RECONCILIATION.
- Corpus root: required reads and candidate roots enumerated by worker.
- Snapshot time: worker execution start.
- Enumeration command: `rg --files --hidden --no-ignore ECOSYSTEM docs governance EXTENSIONS .private_reference/legacy/CVF_Restructure/CVF_ECOSYSTEM`.
- Manifest artifact or inline manifest: inline Required First Reads list.
- Manifest hash: deterministic SHA-256 required.
- Processing ledger artifact or inline ledger: inline Roadmap-to-Work-Order Trace Matrix.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.
- Reconciliation: manifest=11; ledger_terminal=11; exclusions=0; unresolved=0.
- Unresolved count: 0.
- Unresolved files: 0.
- Declared exclusions: none.
- Unreadable or unsupported files: none.
- Aggregation check: Markdown/JSON equality.
- Drift check: compare R94 dispositions.
- Output traceability: file plus line/section per claim.
- Adversarial verification: false owner and false-equivalence cases.
- Corpus verdict: COMPLETE_VERIFIED

## Mandatory Blind-Spot Control Block

- Enumerate exact legacy evidence and active candidates.
- Record terminal candidate decisions and negative searches.
- Blind-spot verdict: pending worker audit.

## External Repository Absorption Entry Control

NOT_APPLICABLE_WITH_REASON: bounded legacy doctrine evidence review only; no
external repository or copied-folder absorption.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Legacy source family |
| Chain map route | legacy evidence -> active owner comparison -> terminal decision |
| Matching local-view guard | `governance/compat/check_source_intake_decision_packet.py` |
| Owner surface | R96 audit and doctrine route map |
| Disposition | ADAPT decision evidence only |
| Claim boundary | no legacy promotion or direct import |

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | two named legacy files plus active candidate roots |
| Enumeration command | filesystem-backed direct reads and targeted `rg -n` |
| Manifest artifact or inline manifest | inline Required First Reads list |
| Processing ledger artifact or inline ledger | inline Roadmap-to-Work-Order Trace Matrix |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | `docs/reference/system_chain/CVF_DOCTRINE_TO_CONTRACT_ROUTE_MAP.md` |
| Unresolved items | explicit row disposition allowed |
| Completion claim boundary | decision evidence only; no absorption |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| L1/L2 legacy evidence | historical responsibilities | DOCTRINE_ADAPTED | audit and route map | compare without copying | no runtime/package |
| L4/L6 candidates | active ownership evidence | NO_PACKAGE_OR_RUNTIME_VALUE | audit and route map | prove or retain gap | no activation |
| direct import | none | REJECT_DIRECT_IMPORT | N/A with reason | reject | forbidden |
| package opportunity | NO_PACKAGE_OR_RUNTIME_VALUE with reason: doctrine routing only | PACKAGE_CANDIDATE | conditional reopen only | no action | package forbidden |
| runtime opportunity | NO_PACKAGE_OR_RUNTIME_VALUE with reason: doctrine routing only | RUNTIME_CANDIDATE | conditional reopen only | no action | runtime forbidden |
| checker opportunity | NO_NEW_VALUE with reason: R91 freshness owner exists | CHECKER_CANDIDATE | existing freshness owner | no action | no new checker |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| L1/L2 responsibilities | `docs/reference/system_chain/CVF_DOCTRINE_TO_CONTRACT_ROUTE_MAP.md` | ENRICH_EXISTING | active ownership unconfirmed | reconcile |
| L4 responsibility | OWNER_SURFACE_NOT_FOUND | OWNER_SURFACE_NOT_FOUND | search required | decide |
| L6 responsibility | `docs/` and `governance/toolkit/06_EXAMPLES/` | ENRICH_EXISTING | partial owner | bound responsibility |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| target paths | absent before authoring | CLEAR |
| existing decision owner | R94 route map | REUSE_OWNER |
| source tokens | doctrine and active candidate searches required | WORKER_ACTION |

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| canonical outputs | `docs/audits/`, `docs/reference/system_chain/`, `docs/reviews/` |
| legacy inputs | read-only historical evidence |
| runtime/package storage | N/A with reason: forbidden |
| cleanup boundary | no move, copy, delete, or archive action |

## Claim Boundary

This order authorizes a no-commit, four-layer evidence and decision pass only.
It does not authorize filling architectural folders, copying legacy doctrine,
editing frozen doctrine, or claiming universal system-chain completeness.
