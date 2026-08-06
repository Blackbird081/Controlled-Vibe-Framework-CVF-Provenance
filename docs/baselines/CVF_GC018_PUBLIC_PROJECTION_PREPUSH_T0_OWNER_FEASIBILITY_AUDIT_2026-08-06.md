# CVF GC-018 Baseline - Public Projection Pre-Push T0 Owner Feasibility Audit

Memory class: FULL_RECORD

Status: APPROVED_FOR_T0_AUDIT

docType: baseline

Date: 2026-08-06

Batch ID: CVF-PUBLIC-PROJECTION-PREPUSH-T0

dispatchBaseHead: `68fbd0442`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: independent reviewer/closer

Worker target: documentation and source-verification audit worker

## Purpose

Authorize one bounded, local, read-only feasibility audit of the public
projection pre-push proof mismatch recorded during GLP-PUBLIC-R1. The audit
must decide whether an additional projection-aware gate profile has enough
incremental value to justify its governance and maintenance cost.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-PUBLIC-PROJECTION-PREPUSH-T0 --title "Public Projection Pre-Push Owner Feasibility Audit" --date 2026-08-06 --base 68fbd0442 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with exact evidence owners, four-option decision rubric, cost ceiling, two-output manifest, and no-build boundary |
| checkerReadAheadConfirmation | dispatch-quality, checker-read-ahead, structural, trace, handoff, lifecycle, ADIF, and prompt-envelope checker sources inspected |
| docOnlyNewFields | optionId; incrementalCoverage; projectionOwnership; recurringCost; T0Decision |
| claimBoundary | dispatch baseline only; no checker, hook, public projection, provider, network, or runtime mutation |

## Source / Predecessor Evidence

- `docs/reviews/CVF_GLP_PUBLIC_R1_GOVERNANCE_LATENCY_CARRIER_REFRESH_COMPLETION_2026-08-06.md`
  records the profile mismatch and explicitly leaves it for a separately
  authorized candidate.
- `governance/compat/run_local_governance_hook_chain.py` resolves named hook
  chains from the local catalog.
- `governance/compat/local_governance_hook_catalog.py` maps `pre-push` to
  `PRE_PUSH_CHECKS`.
- `governance/compat/local_governance_hook_catalog_pre_push.py` includes
  private continuity and pre-public readiness checks.
- `scripts/cvf-public-sync.ps1` defines the allowlisted public projection.
- The sibling public-sync clone is read-only evidence and is not provenance
  authority.

## Decision / Proposed Tranche

Release T0 evidence work only. The worker must return exactly one decision:

- `PROCEED_PUBLIC_PROFILE_DESIGN`
- `USE_EXISTING_FOCUSED_PROOF`
- `DEFER_LOW_VALUE`
- `BLOCKED_NO_OWNER`

No decision in this list authorizes implementation.

## Allowed Scope

- read current provenance source, tests, standards, reviews, and Git metadata;
- inspect the sibling public-sync clone without modifying it;
- inventory generic pre-push checks and classify their public ownership;
- compare four cheap alternatives using normalized coverage and recurring cost;
- create exactly one audit and one worker-return artifact;
- run local documentation and worker-return gates without provider use.

## Forbidden Scope

- editing `governance/compat/`, hook catalogs, scripts, tests, or Git hooks;
- editing, staging, committing, or pushing the sibling public-sync clone;
- weakening, removing, skipping, or reclassifying provenance checks;
- changing session state, active handoff, roadmap, registry, or public catalog;
- provider/network calls, live proof, secrets, deployment, or downstream edits;
- design implementation, specification implementation, or build work.

Risk ceiling: R1 documentation and local read-only evidence.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| named hook chain entrypoint | EXISTS | `governance/compat/run_local_governance_hook_chain.py` | lines 117-121 and 218-250 | `HOOK_CHAINS` | hook-chain runner | ACCEPT |
| generic pre-push chain mapping | VALUE_SET | `governance/compat/local_governance_hook_catalog.py` | lines 16-22 | `pre-push` | `HOOK_CHAINS` | ACCEPT |
| generic pre-push catalog | EXISTS | `governance/compat/local_governance_hook_catalog_pre_push.py` | line 6 | `PRE_PUSH_CHECKS` | pre-push catalog | ACCEPT |
| active-session check in generic pre-push | VALUE_SET | `governance/compat/local_governance_hook_catalog_pre_push.py` | lines 259-263 | `PRE_PUSH_CHECKS` | pre-push catalog | ACCEPT |
| exposure and P3 checks in generic pre-push | VALUE_SET | `governance/compat/local_governance_hook_catalog_pre_push.py` | lines 408-415 | `PRE_PUSH_CHECKS` | pre-push catalog | ACCEPT |
| public projection selection owner | EXISTS | `scripts/cvf-public-sync.ps1` | lines 37, 103, 118, 215, and 225 | `ALLOWED_TREES`; `MAPPED_FILES`; `WORKSPACE_KIT_FILES`; `Test-Denied`; `Get-AllowedFiles` | public-sync projection script | ACCEPT |
| recorded profile mismatch | VALUE_SET | `docs/reviews/CVF_GLP_PUBLIC_R1_GOVERNANCE_LATENCY_CARRIER_REFRESH_COMPLETION_2026-08-06.md` | Finding-To-Governance row at line 131 | `PUBLIC_PROJECTION_GATE_PROFILE_MISMATCH` | GLP-PUBLIC-R1 completion review | ACCEPT |

## Current Source Freshness Verification

At provenance HEAD `68fbd0442`, direct source search found one generic
`pre-push` mapping and the three cited private-dependent checks. At public HEAD
`9b039ea6b`, the hook runner and pre-push catalog exist, while
`CVF_SESSION_MEMORY.md` and `CVF_SESSION/ACTIVE_SESSION_STATE.json` do not.
These are inventory facts only; the worker must recompute them.

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| planned output paths | `Test-Path` before authoring returns false for both worker outputs | ACCEPT |
| existing finding token | exact search found the token only in the accepted GLP-PUBLIC-R1 completion context | ACCEPT |
| public-specific profile claim | no absence claim is accepted from memory; worker must search current source and report collisions or partial owners | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020,
ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044, ADIF-0045,
ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024, ADIF-0031, ADIF-0039,
ADIF-0043, ADIF-0049, ADIF-0006.

Resolver command:
`python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 30 --json`

Returned defect count: 20. Dispatch impact: exact inventories, current source,
explicit role separation, no protected-path authorization, and no invented
command signature are required.

## Audit Questions

1. Which generic pre-push checks are public-owned, private-owned, mixed, or
   inapplicable to a public projection?
2. What incremental defect coverage is missing after the focused golden
   bootstrap harness, public-surface checks that actually exist, Git diff
   checks, leakage scan, and authoritative provenance pre-push gate?
3. Can an existing command or subset provide that coverage without a new
   profile owner?
4. Would a public-specific profile duplicate check ownership or weaken the
   private provenance gate by implication?
5. Which source path would own a later profile, if justified, and what focused
   tests and rollback would be required?
6. What authoring, review, runtime, and drift cost would the new control add?

## Cheap-Alternative Inventory

The audit must compare all four options before recommending work:

| Option | Required comparison |
| --- | --- |
| A | retain authoritative provenance pre-push plus existing focused public proof |
| B | document an exact existing public-safe subset without new code |
| C | design a thin public projection wrapper/profile with no private-check weakening |
| D | defer the mismatch because incremental risk reduction is immaterial |

## Acceptance Criteria

| ID | Required result |
| --- | --- |
| AC1 | exact generic pre-push inventory with public/private/mixed ownership |
| AC2 | exact public projection present/absent inventory, without treating absence as a defect by itself |
| AC3 | existing focused proof and its coverage limits are identified |
| AC4 | all four cheap alternatives are compared on coverage, maintenance, execution latency, and drift |
| AC5 | any proposed owner path and test boundary are source-backed |
| AC6 | provenance gate coverage is explicitly preserved |
| AC7 | exactly one allowed T0 decision is returned with supporting and contradicting evidence |
| AC8 | Git evidence proves only the two worker-owned artifacts changed |

## Evidence / Verification

Evidence must use current command/result/path rows, exact check counts, exact
path-presence results, and a normalized option matrix. Timing claims require
measured local runs; otherwise mark timing as not measured with reason. Do not
infer security or regression coverage from file presence alone.

## Governance Cost Budget

One audit, one worker return, one focused worker-return gate, and one
independent review. The worker must prefer an existing proof path when its
incremental coverage is materially equivalent. A new profile is justified only
if it closes a named risk with a stable owner and bounded recurring cost.

## Reviewer Independence

The worker must not approve or commit its own recommendation. The reviewer
recomputes the check ownership sample, challenges the incremental-value claim,
and preserves disagreements. Gate PASS is not semantic acceptance.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | local provenance and read-only public projection inspection | two uncommitted documentation outputs only | source, Git, and local gate evidence | local command/file boundary | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | no external agent adapter in T0 | no authentication, mutation, receipt, or provider authority | N/A with reason: T0 is local evidence work | no CLI/MCP adapter is designed or invoked | N/A_WITH_REASON |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_dispatch_prompt_envelope.py` |
| literalTokensReviewed | dispatch envelope fields, source table columns, ADIF query line, handoff fields, reviewer conversion, work-order structural groups, trace labels, and public disposition |
| gateRunPurpose | confirm the packet shape after source evidence and cost constraints were defined |
| claimBoundary | structural confirmation only; no semantic or implementation approval |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: existing focused public proof plus authoritative
provenance pre-push may provide most useful coverage at lower recurring cost
than a new public-specific profile.

Evidence Comparison Requirement: compare the prediction with the exact current
catalog, projection contents, focused tests, and known failure evidence.

Contradiction Or Gap Disposition: preserve evidence that a thin profile closes
a material uncovered risk, or that no stable owner exists.

Claim Update Requirement: confirm, narrow, revise, or invalidate the prediction
and return exactly one T0 decision.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Public/simple CVF vocabulary |
| Chain map route | public projection hypothesis -> provenance source verification -> bounded T0 audit -> independent review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | paired provenance baseline, work order, audit, and reviewer artifacts |
| Disposition | ADAPT path-presence evidence into a feasibility question; do not promote the public clone as authority |
| Claim boundary | provenance remains authoritative; no external absorption, public mutation, provider, runtime, or production claim |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher role |
| Provider or surface | local private provenance repository and read-only sibling public projection |
| Session or invocation | CVF-PUBLIC-PROJECTION-PREPUSH-T0 packet authoring, 2026-08-06 |
| Working directory | provenance repository root; public sibling inspected read-only |
| Command or tool surface | local source reads, Git inspection, ADIF resolver, scaffold stdout, apply_patch, governance gates |
| Target paths | paired T0 baseline and work order |
| Allowed scope source | operator continuation and accepted GLP-PUBLIC-R1 finding |
| Before status evidence | provenance HEAD `68fbd0442`, clean; public HEAD equals origin/main `9b039ea6b`, clean |
| After status evidence | paired dispatch packet pending commit |
| Diff evidence | `git diff --name-status` before commit |
| Approval boundary | T0 documentation/source audit dispatch only |
| Claim boundary | no checker, hook, public, provider, network, runtime, or session mutation |
| Agent type | dispatcher |
| Invocation ID | `cvf-public-projection-prepush-t0-dispatch-2026-08-06` |
| Expected manifest | paired T0 baseline and work order |
| Actual changed set | paired T0 baseline and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Stop Conditions

Stop for a source contradiction, non-isolated worktree, required protected-path
edit, public mutation, provider/network need, ambiguous repository authority, or
any request to implement before independent T0 review.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is a private provenance feasibility baseline; no public artifact
or public-sync action is authorized.

## Claim Boundary

This baseline authorizes only two uncommitted T0 documentation outputs. It does
not authorize a new gate profile, checker/hook change, public edit, live proof,
provider/network call, downstream mutation, commit, push, or T1+ work.
