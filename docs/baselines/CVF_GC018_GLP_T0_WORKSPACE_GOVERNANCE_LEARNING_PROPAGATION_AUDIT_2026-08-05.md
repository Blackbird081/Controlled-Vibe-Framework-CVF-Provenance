# CVF GC-018 Baseline - GLP T0 Workspace Governance Learning Propagation Audit

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: baseline

Date: 2026-08-05

Batch ID: GLP-T0

dispatchBaseHead: `ace02fda7`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator

Reviewer owner: independent reviewer/closer

Worker target: documentation and source-verification worker

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id GLP-T0 --title "Workspace Governance Learning Propagation Audit" --date 2026-08-05 --base ace02fda7 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic worker dispatch plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with GLP source chain, two-output scope, exact decisions, and no-external-effect boundary |
| checkerReadAheadConfirmation | dispatch-quality, structural, ADIF, handoff, trace, scaffold, and public-disposition checkers |
| docOnlyNewFields | authorityClass; carrierStatus; alternativeCost; T0Decision |
| claimBoundary | dispatch baseline only; no worker execution or implementation |

## Purpose

Authorize one local, documentation-only audit of the provenance-to-workspace
learning propagation chain. The audit must reproduce or invalidate the gap
recorded by GLP-R0 and return exactly one bounded T0 decision.

## Target / Source

- `docs/roadmaps/CVF_WORKSPACE_GOVERNANCE_LEARNING_PROPAGATION_ROADMAP_2026-08-05.md` at material commit `3b8781b3b`;
- `Initialize-CVF-Operator-Workspace.ps1`;
- `scripts/sync_cvf_workspace_rule_pack.ps1`;
- `workspace_overlay_catalog.json` and `workspace_overlay_profiles/`;
- `docs/reference/CVF_WORKSPACE_RULES.md`;
- `governance/toolkit/05_OPERATION/CVF_DOWNSTREAM_AGENTS_TEMPLATE.md`;
- `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0026.md`;
- `docs/reference/review_cost_control/CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md`;
- R72C Fast Lane evidence and R84 compact worker-return closure.

## Decision / Proposed Tranche

Release `GLP-T0` only. The worker creates an audit and worker return, makes no
implementation change, and returns one of:

- `PROCEED_BOOTSTRAP_ALIGNMENT`
- `PROCEED_DOC_ONLY`
- `STOP_ALREADY_PROPAGATED`

## Allowed Scope

- read current provenance files and Git history;
- resolve profile inheritance and exact catalog membership;
- compare canonical learning owners with workspace and project carriers;
- inventory pointer-without-owner and owner-without-consumer gaps;
- compare catalog addition, compact carrier, project-template-only, and no-change alternatives;
- create exactly the two worker-owned documentation artifacts.

## Forbidden Scope

- bootstrap, catalog, profile, template, runtime, checker, test, or hook edits;
- sibling workspace, hidden public core, application-project, or downstream edits;
- public-sync, provider/network use, push, deployment, or live proof;
- copying private continuity or the full provenance governance corpus;
- reopening governance-latency WS2 or GC010-AER.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| initializer owns create/update/profile sequencing | RUNTIME_BEHAVIOR | canonical contract: root workspace initializer | `Initialize-CVF-Operator-Workspace.ps1` lines 443-520 | `Install-NewWorkspace`; `Refresh-ExistingWorkspace`; `Apply-SelectedProfile` | workspace initializer functions | ACCEPT |
| rule-pack projection is catalog/tag selected | RUNTIME_BEHAVIOR | `scripts/sync_cvf_workspace_rule_pack.ps1` | lines 157-245 | `Resolve-ProfileTags`; `selectionTags` | rule-pack synchronizer | ACCEPT |
| generated manifest records exact projection | RUNTIME_BEHAVIOR | `scripts/sync_cvf_workspace_rule_pack.ps1` | lines 287-318 | `RULE_PACK_MANIFEST.json` | rule-pack manifest writer | ACCEPT |
| operator-local profile inheritance exists | VALUE_SET | canonical contract: workspace overlay profile schema | `workspace_overlay_profiles/operator-local.json` field `extends` | `operator-local` | workspace overlay profile schema | ACCEPT |
| guard orientation is catalog selected | VALUE_SET | canonical contract: workspace overlay catalog schema | `workspace_overlay_catalog.json` artifact `guard-orientation-index` | `guard-orientation-index` | workspace overlay catalog | ACCEPT |
| same-scope authority learning owner exists | EXISTS | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0026.md` | Remediation | `AVOIDABLE_OPERATOR_WAIT` | ADIF-0026 | ACCEPT |

## Current Runtime Freshness Verification

The dispatcher re-read current initializer, synchronizer, profiles, catalog,
workspace rules, and downstream agent template at HEAD `ace02fda7`. T0 must
repeat the searches and must not rely on this baseline as execution evidence.

## Negative Search And Collision Discipline

| Search | Root | Result | Disposition |
|---|---|---|---|
| exact catalog paths for ADIF-0026, review-cost standard, and R72C matrix | `workspace_overlay_catalog.json` | zero exact entries for all three paths | ACCEPT_AS_AUDIT_INPUT |
| same-scope, avoidable-wait, review-cost, diminishing-return, and Fast Doc vocabulary | `governance/toolkit/05_OPERATION/CVF_DOWNSTREAM_AGENTS_TEMPLATE.md` | no matching carrier vocabulary | ACCEPT_AS_AUDIT_INPUT |
| GLP-T0 output path collision | `docs/audits` and `docs/reviews` | no existing target paths | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`source audit`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

Command: `python governance/compat/run_adif_defect_resolver.py --task-class "source audit" --role dispatcher --lifecycle-phase pre-dispatch --json`

## Acceptance Criteria

| ID | Required result |
|---|---|
| AC1 | chain map separates provenance, public core, workspace root, rule pack, and project authority |
| AC2 | every relevant profile has an exact resolved-tag and selected-artifact inventory |
| AC3 | ADIF-0026, review-cost, R72C/R84, guard orientation, and project-template coverage are classified separately |
| AC4 | disagreements and missing carriers remain visible |
| AC5 | four cheap alternatives are compared before any implementation proposal |
| AC6 | exactly one T0 decision is returned |
| AC7 | governance cost and `AVOIDABLE_OPERATOR_WAIT` count are reported |
| AC8 | Git evidence proves only the two worker-owned paths changed |

## Evidence / Verification

Evidence must include exact commands, result summaries, current source paths,
resolved profile tags, catalog membership counts, and final Git status. Prior
roadmap observations are predictions to reproduce, not reusable proof.

## Stop Conditions

Stop with `BLOCKED_WITH_REASON` if source relationships cannot be reproduced,
the worktree is not isolated, a required result needs a forbidden edit, or a
safe public/private carrier distinction cannot be made from current source.

## Governance Cost Budget

One audit, one worker return, focused local checks, and one independent review.
No repeated operator confirmation is required for allowed-scope repair. The
worker records first-pass/final gate counts, repair rounds, elapsed time when
available, and avoidable wait events.

## Reviewer Independence

The worker must not approve or commit its own result. The independent reviewer
recomputes profile/catalog membership and preserves disagreement before closure.

## Dual Agent Surface Matrix

| Surface class | Interface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | local provenance reads | may create two no-commit T0 artifacts only | source paths and Git evidence | local filesystem | ALLOWED |
| `EXTERNAL_AGENT_CLI_MCP` | role-neutral handoff | no external command/provider adapter is needed | N/A with reason | no adapter | CONTRACT_ONLY |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | dispatch status, Source Verification columns, ADIF query line, acceptance, stop, dual-agent, trace, and public-export labels |
| gateRunPurpose | confirm dispatch shape after source verification |
| claimBoundary | GLP-T0 documentation audit dispatch only |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: a bounded carrier gap will remain after exact
profile resolution, but the cheapest safe remedy may be smaller than copying
the three provenance owners.

Evidence Comparison Requirement: compare exact current source with this
prediction and record supporting and contradicting evidence.

Contradiction Or Gap Disposition: return `STOP_ALREADY_PROPAGATED` if an
equivalent source-backed carrier already reaches the generated project.

Claim Update Requirement: confirm, narrow, or invalidate each gap claim.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | local private provenance repository |
| Session or invocation | GLP-T0 dispatch authoring, 2026-08-05 |
| Working directory | repository root |
| Command or tool surface | local reads, exact searches, JSON queries, apply_patch, governance gates |
| Target paths | paired GLP-T0 baseline and work order |
| Allowed scope source | GLP-R0 roadmap at `3b8781b3b` and operator continuation |
| Before status evidence | HEAD `ace02fda7`; clean worktree |
| After status evidence | GLP-T0 dispatch packet pending commit |
| Diff evidence | `git diff --name-status` before commit |
| Approval boundary | documentation-only T0 dispatch |
| Claim boundary | no implementation or external effects |
| Agent type | dispatcher |
| Invocation ID | `glp-t0-dispatch-authoring-2026-08-05` |
| Expected manifest | paired GLP-T0 baseline and work order |
| Actual changed set | paired GLP-T0 baseline and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

This baseline releases only a local, no-commit, documentation/source audit.
It grants no implementation, generated-workspace, downstream, public, live,
provider, network, push, deployment, or production authority.
