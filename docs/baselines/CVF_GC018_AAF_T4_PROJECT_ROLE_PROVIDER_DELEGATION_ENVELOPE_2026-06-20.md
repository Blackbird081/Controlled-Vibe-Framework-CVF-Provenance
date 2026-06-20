# CVF GC-018 - AAF-T4 Project Role And Provider Delegation Envelope

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-06-20

docType: baseline

dispatchBaseHead: f209d973

Batch ID: AAF-T4

## Purpose

Authorize AAF-T4 as a bounded governance-reference follow-up to AAF-T3. AAF-T3
closed the role-neutral Guard Orientation Index. AAF-T4 adds the missing
project-level delegation envelope behind CVF's public multi-agent/provider
routing guidance: how an operator approves role delegation and provider-lane
selection for a specific project before agents begin work.

AAF-T4 is documentation/reference only. It does not implement automated
provider selection, provider routing, runtime worker routing, CLI/MCP behavior,
provider calls, live proof, public-sync, queue/daemon behavior, watcher
behavior, or universal governed-coding control.

## Operator Authorization

The operator directed the sequence to process AAF-T3 first and then move to
AAF-T4. The operator also clarified that CVF should build toward the existing
public multi-agent provider routing guide without needing to rewrite that guide
now. Model/provider version details in public guidance remain updateable later;
the private CVF gap is the governed role/provider delegation substrate.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-20 AAF-T4 selection after AAF-T3 closure | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V20_2026-06-19.md` | ACCEPT |
| AAF-T3 completion | `docs/reviews/CVF_AAF_T3_GUARD_ORIENTATION_INDEX_COMPLETION_2026-06-20.md` | ACCEPT |
| Guard Orientation Index | `docs/reference/guard_orientation/README.md` | ACCEPT |
| Agent role assignment matrix | `docs/reference/CVF_AGENT_ROLE_ASSIGNMENT_MATRIX_2026-05-19.md` | ACCEPT |
| Delegation/subagent boundary standard | `docs/reference/CVF_AGENT_DELEGATION_AND_SUBAGENT_BOUNDARY_STANDARD_2026-05-19.md` | ACCEPT |
| C-02 provider-routing boundary plan | `docs/reference/CVF_MODEL_GATEWAY_C02_PROVIDER_ROUTING_BOUNDARY_REWRITE_PLAN_2026-06-14.md` | ACCEPT |
| C-02 provider-routing closure | `docs/reviews/CVF_MODEL_GATEWAY_C02_PROVIDER_ROUTING_BOUNDARY_REWRITE_COMPLETION_2026-06-14.md` | ACCEPT |
| Public guide context | `docs/guides/CVF_MULTI_AGENT_PROVIDER_ROUTING.md` in public-sync, cited by active next move | CONTEXT_ONLY_NOT_CVF_SOURCE |

## Scope / Owner Boundary

Allowed scope:

- create a stable private reference front door under
  `docs/reference/project_role_provider_delegation/`;
- update `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` to
  route project role/provider delegation setup to the new front door;
- update `docs/reference/guard_orientation/README.md` only enough to point
  project delegation tasks to the AAF-T4 envelope;
- create one AAF-T4 worker-return artifact.

Forbidden scope:

- no runtime/source/test implementation;
- no edits under `EXTENSIONS/**`, `.github/**`, public-sync, dependency
  manifests, generated session state, active handoff, or session memory;
- no provider/model addition, concrete provider binding, automated provider
  selection, provider/API call, live proof, secrets/quota use, package install,
  queue/daemon, watcher, background service, or CVF Web action execution;
- no wrapper/proxy enforcement, direct IDE/shell/git/filesystem interception,
  arbitrary command execution, EDIT/COMMIT execution, production/public/release
  readiness, full-hook equivalence, universal speed, or universal
  governed-coding-control claim.

Risk ceiling: R1 governance documentation and reference.

## Required Deliverables

The worker must return uncommitted `COMPLETE_PENDING_REVIEW` with exactly these
owned artifacts changed or created:

- `docs/reference/project_role_provider_delegation/README.md`
- `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`
- `docs/reference/guard_orientation/README.md`
- `docs/reviews/CVF_AAF_T4_PROJECT_ROLE_PROVIDER_DELEGATION_ENVELOPE_WORKER_RETURN_2026-06-20.md`

No other files are authorized for the worker.

## Decision / Baseline / Proposed Tranche

Baseline decision: AAF-T4 is ready for role-neutral worker dispatch as a bounded
project role/provider delegation envelope tranche.

Proposed tranche: `AAF-T4 Project Role And Provider Delegation Envelope`.

Tranche owner split: the dispatch author creates this GC-018 and the paired work
order; the worker creates the reference envelope and updates allowed routing
surfaces without committing; the reviewer/closer reviews, repairs only within
allowed scope if needed, commits accepted material, and session-syncs only after
material closure.

Baseline evidence:

- Current HEAD is `f209d973`.
- AAF-T3 closed at material commit `45fd5468` and closure continuity commit
  `f209d973`.
- Active next move names AAF-T4 as the next governed documentation/reference
  foundation and lists the required substrate fields.
- Existing role/delegation standards define role assignment and bounded
  delegation, but no compact project envelope exists for operator-approved
  role/provider-lane setup.
- Existing Model Gateway C-02 artifacts keep provider-routing implementation
  planning-only; AAF-T4 must not turn that planning into provider runtime.

## Source / Predecessor Evidence

| Source | Evidence | Disposition |
|---|---|---|
| Active next move | `CVF_SESSION/ACTIVE_SESSION_STATE.json` line 2706 names AAF-T4 and required substrate fields | ACCEPT |
| AAF-T3 completion | lines 126-127, 150, 158-159 name AAF-T4 follow-up and no runtime/provider expansion | ACCEPT |
| Guard Orientation Index | lines 37-54 require role-neutrality; lines 73 and 81 define startup and live-proof boundaries | ACCEPT |
| Role assignment matrix | role assignment flow, specialist worker mapping, and runtime-enforcement boundary | ACCEPT |
| Delegation boundary standard | lines 117, 139, 176, 197, and 308 define delegation decision, mandatory packet, tool, memory, and review boundaries | ACCEPT |
| C-02 provider-routing plan | lines 39, 518, 530, and 578 keep provider routing planning-only and require fresh GC-018 for implementation | ACCEPT |
| C-02 closure | lines 61, 83, and 146 preserve planning-only claim boundary | ACCEPT |

## Evidence / Verification

Dispatch author verification before this packet:

- `git rev-parse --short HEAD` returned `f209d973`.
- `git status --short` was clean except the recurring Windows global
  git-ignore permission warning.
- `Test-Path docs/guides/CVF_MULTI_AGENT_PROVIDER_ROUTING.md` returned
  `False` in the provenance workspace, so the public guide path is context
  only and not a CVF-governed source authority.
- Source verification used direct file reads and `rg -n` lookups against
  current repository files.

Required pre-dispatch verification before commit:

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base f209d973 --head HEAD
python governance/compat/check_work_order_dispatch_quality.py --base f209d973 --head HEAD --enforce
python governance/compat/run_agent_commit_steward_preflight.py --mode dispatch --base f209d973 --head HEAD --enforce
```

## Required Envelope Shape

The new `docs/reference/project_role_provider_delegation/README.md` must be
short enough to read during project setup and concrete enough to prevent
ambiguous delegation.

Minimum required sections:

- `## Purpose`
- `## When To Use`
- `## Operator Approval Envelope`
- `## Role And Delegation Map`
- `## Provider Lane Selection Boundary`
- `## Cost And Quota Ceiling`
- `## Evidence Log`
- `## Reapproval Triggers`
- `## Non-Goals`
- `## Claim Boundary`
- `## Related Surfaces`

The envelope must state that provider/model names, versions, prices, and
availability are project-configuration inputs that may change. AAF-T4 defines
the approval/evidence shape, not a permanent provider recommendation.

## Claim Boundary

AAF-T4 may claim only a documentation/reference substrate for
operator-approved project role delegation and provider-lane selection. It must
not claim automated provider selection, runtime provider routing, provider
quality/cost optimization, live provider behavior, hosted freshness, public
readiness, production readiness, release readiness, direct interception,
wrapper/proxy enforcement, queue/daemon execution, or universal governed-coding
control.

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | governed work-order/source-verification/autorun lane |
| Matching local-view guard | `governance/compat/check_work_order_dispatch_quality.py`; guard orientation index |
| Owner surface | `docs/reference/project_role_provider_delegation/README.md` |
| Disposition | ADAPT as CVF-owned private delegation reference |
| Claim boundary | public guide context is not CVF source authority; CVF-owned standards and state control |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | AAF-T4 project delegation documentation dispatch only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | cooperating local operator/roles read the envelope manually |
| interceptionBoundary | no direct IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | delegation envelope and reference substrate only |
| forbiddenExpansion | automated provider selection, runtime routing, provider/live proof, wrapper/proxy enforcement, direct interception, arbitrary commands, EDIT/COMMIT execution, public-sync, queue/daemon, watcher, readiness, full-hook equivalence, and universal control remain parked |

## Rescan Intelligence Hardening

- Original source artifact: operator AAF-T4 selection after AAF-T3 and AAF-T3
  completion follow-up candidate.
- Predecessor intake artifact:
  `docs/reviews/CVF_AAF_T3_GUARD_ORIENTATION_INDEX_COMPLETION_2026-06-20.md`.
- Delta ledger status: `CHANGED_DISPOSITION` because project role/provider
  delegation moves from follow-up candidate into dispatch-ready reference work.
- Routing matrix status:
  - `DO_NOW`: create private project role/provider delegation envelope.
  - `RESOLVED_BY_DESIGN`: keep provider examples configurable and non-canonical.
  - `SEPARATE_RUNTIME_TRANCHE`: automated provider selection, runtime routing,
    provider calls, queue/daemon, direct interception.
  - `OUT_OF_SCOPE`: public-sync, production readiness, universal control.
- Semantic sampling status: `PARTIAL_TARGETED`, limited to AAF-T3 follow-up,
  delegation standards, and provider-routing planning boundary.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Delta category | Disposition |
|---|---|
| UNCHANGED_FROM_INTAKE | Public guide remains context; CVF source authority remains private governed surfaces. |
| CHANGED_DISPOSITION | AAF-T4 delegation envelope becomes dispatch-ready documentation/reference work. |
| NEW_FINDING | Project provider-lane approval needs explicit cost/quota and reapproval fields before external-agent use. |
| REMOVED_OR_REJECTED | Automated provider selection, runtime routing, provider/live, public-sync, direct-interception scope remains rejected. |

### Follow-Up Routing Matrix

| Lane | Disposition |
|---|---|
| DO_NOW | Create project delegation envelope and route it from reference surfaces. |
| RESOLVED_BY_DESIGN | Keep provider/model examples as project configuration, not CVF source authority. |
| SEPARATE_RUNTIME_TRANCHE | Automated provider selection, runtime routing, CLI/MCP integration, watcher/daemon, provider/live, direct interception. |
| STRATEGIC_OPERATOR_DECISION | Broad CGE-T3 absorption and ACE-R1 remain parked. |
| DEFER | Public-sync summary or public-facing provider-routing guide refresh. |
| OUT_OF_SCOPE | Production readiness, public release readiness, universal governed-coding-control claim. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| AAF-T4-RS1 | Active next move | AAF-T4 creates private substrate | DO_NOW | Could this be mistaken for runtime routing? | PASS_DOC_ONLY_REQUIRED |
| AAF-T4-RS2 | Delegation standard | delegation is bounded execution, not authority transfer | DO_NOW | Could a role delegate authority to a provider/worker? | PASS_AUTHORITY_BOUNDARY_REQUIRED |
| AAF-T4-RS3 | C-02 plan | provider routing remains planning-only | OUT_OF_SCOPE runtime | Could the envelope implement provider selection? | PASS_RUNTIME_REJECTED |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: AAF-T4 is private provenance governance-reference work. Public export
requires separate public-sync authorization and remote verification.

## Corpus Completeness And Report Integrity

- Corpus task class: N/A with reason - this is a GC-018 dispatch baseline, not
  a corpus inventory, folder-tree scan, or extraction report.
- Corpus root: N/A with reason - no corpus root was authorized or enumerated.
- Snapshot time: 2026-06-20 dispatch authoring.
- Enumeration command: filesystem-backed direct file reads and `rg -n` source
  lookups over named AAF-T4 authority files.
- Manifest artifact or inline manifest: Authority Chain, Source / Predecessor
  Evidence, and Source Verification Block in the paired work order.
- Manifest hash: N/A with reason - no generated corpus manifest artifact was
  produced.
- Processing ledger artifact or inline ledger: inline in Evidence /
  Verification.
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED | BLOCKED_UNREADABLE
- Reconciliation: manifest=inline; ledger_terminal=inline; exclusions=no-corpus-inventory-scope; unresolved=0
- Unresolved files: 0
- Declared exclusions: full corpus inventory, runtime/source implementation,
  provider/live proof, public-sync.
- Unreadable or unsupported files: none.
- Aggregation check: N/A with reason - no corpus aggregate was produced.
- Drift check: N/A with reason - no corpus aggregate was produced.
- Output traceability: baseline source evidence cites current repo authority
  files and the AAF-T4 work order carries detailed line anchors.
- Adversarial verification: claim rejects any runtime provider routing,
  automated selection, cost optimization, or readiness assertion.
- Corpus verdict: PARTIAL

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
|---|---|---|---|---|
| Public multi-agent/provider routing language needs a private governed delegation substrate before project use | RULE_GAP | GOVERNANCE_CONTROL_PLANE | STANDARD_ADDED | AAF-T4 dispatches a project delegation envelope reference. |
| Runtime/provider/cost behavior is mentioned but not changed | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | AAF-T4 records configuration boundaries only; no provider/live/cost behavior changes. |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: Current CVF sources will show role assignment and
delegation standards plus provider-routing planning boundaries, but no compact
project-level envelope that combines operator approval, role delegation,
provider-lane selection boundary, cost/quota ceiling, evidence log, and
reapproval triggers.

Evidence Comparison Requirement: worker return must compare the created
envelope against AAF-T3 follow-up rows, role/delegation standards, and C-02
planning-only boundaries.

Contradiction Handling Requirement: if current source already contains an
equivalent active envelope, worker must stop and return `BLOCKED_WITH_REASON`
instead of duplicating it.

Claim Update Requirement: worker return records whether AAF-T4 confirms,
narrows, or rejects the dispatch prediction.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch author role |
| Provider or surface | local workspace |
| Session or invocation | AAF-T4 dispatch authoring, 2026-06-20 |
| Working directory | repository root |
| Command or tool surface | file reads, `rg -n`, `apply_patch`, governance gates |
| Target paths | AAF-T4 GC-018 baseline and paired work order |
| Allowed scope source | operator AAF-T4 selection and active next-move state |
| Before status evidence | HEAD `f209d973`; clean worktree except recurring Windows global git-ignore warning |
| After status evidence | AAF-T4 dispatch packet ready for pre-dispatch gates |
| Diff evidence | exact dispatch diff and dispatch-quality gate |
| Approval boundary | dispatch authoring only; no implementation by dispatch author in this packet |
| Claim boundary | no runtime mutation, provider/live, public-sync, direct interception, automated provider selection, or universal enforcement claim |
| Agent type | single-role dispatch author |
| Invocation ID | `aaf-t4-dispatch-authoring-2026-06-20` |
| Expected manifest | `docs/baselines/CVF_GC018_AAF_T4_PROJECT_ROLE_PROVIDER_DELEGATION_ENVELOPE_2026-06-20.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AAF_T4_PROJECT_ROLE_PROVIDER_DELEGATION_ENVELOPE_FOR_WORKER_2026-06-20.md` |
| Actual changed set | `docs/baselines/CVF_GC018_AAF_T4_PROJECT_ROLE_PROVIDER_DELEGATION_ENVELOPE_2026-06-20.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AAF_T4_PROJECT_ROLE_PROVIDER_DELEGATION_ENVELOPE_FOR_WORKER_2026-06-20.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename authorized |
