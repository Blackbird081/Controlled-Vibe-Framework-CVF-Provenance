# CVF GC-018 Baseline - GLP T1 Workspace Governance Learning Carrier Design

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: baseline

Date: 2026-08-05

Batch ID: GLP-T1

dispatchBaseHead: `bdc6540ca`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: independent reviewer/closer

Worker target: documentation and source-verification design worker

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id GLP-T1 --title "Workspace Governance Learning Carrier Design" --date 2026-08-05 --base bdc6540ca --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic worker dispatch plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with GLP-T1 carrier candidates, public-safety boundary, design questions, and exact two-output scope |
| checkerReadAheadConfirmation | dispatch-quality, structural, source-intake, ADIF, handoff, trace, scaffold, worker-return, and public-disposition checkers |
| docOnlyNewFields | carrierOwnerPath; carrierForm; publicSafeContentBoundary; profileExposure; propagationConsumer; implementationProofPlan |
| claimBoundary | design dispatch baseline only; no design execution or implementation |

## Purpose

Authorize one local, documentation-only design comparison that selects the
smallest safe owner and carrier for the governance-latency learning confirmed
by GLP-T0. The result must prefer an existing distributed owner when it can
carry the rule without semantic overload; otherwise it may specify one compact
public-safe carrier.

## Target / Source

- accepted GLP-T0 audit and reviewer return at material commit `60884f5c0`;
- `workspace_overlay_catalog.json` and `workspace_overlay_profiles/`;
- `docs/reference/guard_orientation/README.md`;
- `governance/toolkit/05_OPERATION/CVF_DOWNSTREAM_AGENTS_TEMPLATE.md`;
- `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md`;
- `docs/reference/governance_control_index/CVF_GOVERNANCE_CONTROL_INDEX.md`;
- `docs/reference/review_cost_control/README.md` and its paired standard;
- `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0026.md`;
- `docs/reference/work_order_authoring/CVF_WORKER_RETURN_QUALITY_GATE_STANDARD.md`;
- R72C/R84 evidence named by the GLP roadmap and T0 audit.

## Decision / Proposed Tranche

Release `GLP-T1` design evidence only. The worker creates one design audit and
one worker return, makes no carrier or catalog edit, and recommends exactly one:

- `CARRIER_DESIGN_ACCEPTED`
- `STOP_NO_SAFE_CARRIER`

The independent reviewer owns the accepted exit decision.

## Allowed Scope

- read current provenance sources and Git history locally;
- compare the three distributed existing-owner candidates with one compact
  public-safe carrier candidate;
- define exact operational semantics to include and private evidence to omit;
- identify one canonical owner path or stop;
- specify catalog/profile/template disposition without editing those surfaces;
- define T2 focused tests, leakage negatives, rollback, and drift ownership;
- create exactly the two worker-owned documentation artifacts.

## Forbidden Scope

- creating the proposed carrier or modifying any existing carrier;
- catalog, profile, template, bootstrap, runtime, checker, test, or hook edits;
- generated workspace, sibling workspace, downstream project, or public-sync edits;
- provider/network use, live proof, push, deployment, or secret access;
- copying private incident history, session telemetry, raw reviewer traces, or
  the full ADIF/review-cost/R72C/R84 owners into a distributed carrier;
- GLP-T2 implementation or later-tranche dispatch.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| GLP-T0 accepted `PROCEED_DOC_ONLY` | VALUE_SET | `docs/reviews/CVF_GLP_T0_WORKSPACE_GOVERNANCE_LEARNING_PROPAGATION_AUDIT_WORKER_RETURN_2026-08-05.md` | `## Independent Reviewer Closure Addendum` | `PROCEED_DOC_ONLY` | GLP-T0 reviewer disposition | ACCEPT |
| guard orientation is a distributed catalog owner | VALUE_SET | canonical contract: workspace overlay catalog schema | artifact `guard-orientation-index` | `guard-orientation-index` | workspace overlay catalog | ACCEPT |
| downstream AGENTS template is a distributed catalog owner | VALUE_SET | canonical contract: workspace overlay catalog schema | artifact `downstream-agents-template` | `downstream-agents-template` | workspace overlay catalog | ACCEPT |
| governance control matrix is a distributed catalog owner | VALUE_SET | canonical contract: workspace overlay catalog schema | artifact `governance-control-matrix` | `governance-control-matrix` | workspace overlay catalog | ACCEPT |
| guard orientation already routes reviewer cost and escalation | EXISTS | `docs/reference/guard_orientation/README.md` | Reviewer-return review row | `Reviewer-return review` | guard-orientation task map | ACCEPT |
| control index owns minimum-effective-governance lifecycle semantics but is not catalog-carried | EXISTS | `docs/reference/governance_control_index/CVF_GOVERNANCE_CONTROL_INDEX.md` | Purpose; Control Family Index | `GCI-010`; `GCI-017` | governance control index | ACCEPT |
| review-cost family is a private provenance owner | EXISTS | `docs/reference/review_cost_control/README.md` | Purpose; Public Export Disposition | `review_cost_control` | review-cost front door | ACCEPT |
| same-scope authority owner exists | EXISTS | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0026.md` | Remediation | `AVOIDABLE_OPERATOR_WAIT` | ADIF-0026 | ACCEPT |
| Fast Doc has a compact dispatch-authenticated contract | EXISTS | `docs/reference/work_order_authoring/CVF_WORKER_RETURN_QUALITY_GATE_STANDARD.md` | Dispatch-Authorized Fast Doc Variant | `WORKER_RETURN_FAST_DOC_V1` | worker-return quality standard | ACCEPT |

## Current Source Freshness Verification

At HEAD `bdc6540ca`, direct catalog queries returned one exact entry each for
guard orientation, downstream AGENTS template, and governance control matrix;
they returned zero for the governance control index, worker-return quality
standard, and review-cost front door. GLP-T1 must repeat these results and must
not treat this baseline as execution evidence.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`design specification`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

Command: `python governance/compat/run_adif_defect_resolver.py --task-class "design specification" --role dispatcher --lifecycle-phase pre-dispatch --json`

## Design Questions

The worker must answer every question before recommending a carrier:

1. Can guard orientation carry a self-contained minimum-effective-governance
   rule without depending on non-copied private paths?
2. Would the governance control matrix make the rule discoverable at the
   action point, or only classify ownership after the fact?
3. Would modifying the downstream template overgrow a high-blast-radius shared
   control surface?
4. Does a new compact carrier reduce recurring drift cost enough to justify a
   new catalog artifact?
5. Which exact semantics are public-safe: same-scope authority continuity,
   real escalation boundaries, one consolidated review pass, diminishing-
   return stop, and dispatch-authenticated Fast Doc eligibility?
6. Which evidence must remain private: incident chronology, operator/session
   detail, quota/timing telemetry, raw reviewer traces, and private paths?
7. Which profile tags and project consumers should receive the carrier?
8. What deterministic T2 proof demonstrates inclusion, private leakage
   exclusion, idempotent refresh, and rollback?

## Acceptance Criteria

| ID | Required result |
|---|---|
| AC1 | four carrier candidates are compared against one decision rubric |
| AC2 | one canonical owner path is selected or the tranche stops |
| AC3 | included semantics and excluded private evidence are exact |
| AC4 | catalog/profile/template disposition is source-backed and non-mutating |
| AC5 | maintenance owner, drift trigger, and versioning rule are specified |
| AC6 | T2 changed-set, tests, negative leakage proof, and rollback are bounded |
| AC7 | exactly one T1 exit recommendation is returned |
| AC8 | Git evidence proves only the two worker-owned paths changed |

## Evidence / Verification

Evidence must include current catalog membership, resolved profile exposure,
source sections for every proposed semantic, a candidate decision matrix,
supporting and contradicting evidence, final Git status, and governance-cost
telemetry. A recommendation without an excluded-content boundary is rejected.

## Stop Conditions

Stop with `BLOCKED_WITH_REASON` if no candidate can be public-safe and
self-contained, a canonical owner cannot be assigned, required evidence needs a
forbidden edit or external action, or the worktree is not isolated.

## Governance Cost Budget

One design audit, one worker return, one focused local gate pass, and one
independent review. Prefer modifying one existing distributed owner over adding
a new owner only when semantic fit and discoverability are at least equivalent.
Do not trade one propagation gap for duplicated governance ownership.

## Reviewer Independence

The worker must not approve or commit its own design. The reviewer independently
recomputes candidate catalog membership and challenges the selected owner's
semantic fit before accepting `CARRIER_DESIGN_ACCEPTED`.

## Dual Agent Surface Matrix

| Surface class | Interface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | local provenance reads | may create two no-commit design artifacts only | source paths, matrices, and Git evidence | local filesystem | ALLOWED |
| `EXTERNAL_AGENT_CLI_MCP` | role-neutral handoff | no external command or provider adapter is required | N/A with reason | no adapter | CONTRACT_ONLY |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | dispatch status, Source Verification columns, ADIF query line, Fast Doc terms, handoff route, trace labels, decision tokens, and public-export labels |
| gateRunPurpose | confirm packet shape after source-backed design requirements were written |
| claimBoundary | GLP-T1 documentation design dispatch only |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: guard orientation may be the lowest-cost existing
owner because it is already distributed and already routes review-cost work,
but a compact carrier may be safer if self-contained semantics would overload
the orientation index.

Evidence Comparison Requirement: compare all four candidates without treating
the prediction as a selection.

Contradiction Or Gap Disposition: preserve any evidence that favors the
downstream template, control matrix, compact carrier, or stopping.

Claim Update Requirement: select, narrow, or invalidate the candidate set.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | local private provenance repository |
| Session or invocation | GLP-T1 dispatch authoring, 2026-08-05 |
| Working directory | repository root |
| Command or tool surface | local source reads, exact catalog queries, ADIF resolver, apply_patch, governance gates |
| Target paths | paired GLP-T1 baseline and work order |
| Allowed scope source | GLP roadmap and accepted T0 decision at `60884f5c0` |
| Before status evidence | HEAD `bdc6540ca`; clean worktree |
| After status evidence | GLP-T1 dispatch packet pending commit |
| Diff evidence | `git diff --name-status` before commit |
| Approval boundary | documentation-only design dispatch |
| Claim boundary | no design execution, carrier/catalog/template implementation, or external effect |
| Agent type | dispatcher |
| Invocation ID | `glp-t1-dispatch-authoring-2026-08-05` |
| Expected manifest | paired GLP-T1 baseline and work order |
| Actual changed set | paired GLP-T1 baseline and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

This baseline releases only a local no-commit carrier-design analysis. It does
not authorize carrier creation, catalog/profile/template/bootstrap mutation,
generated workspace or downstream mutation, public-sync, provider/network use,
push, deployment, or production claims.
