# CVF Agent Work Order - RSPB-AI-T1 Capability Preflight Owner Reconciliation And Read-Only Snapshot Value Probe

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

docType: work_order

Date: 2026-08-16

Batch ID: RSPB-AI-T1

Dispatch base head: 29b2f32c6

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: bounded source-analysis worker

Reviewer/closer: independent reviewer/closer

Worker return path: `docs/reviews/CVF_RSPB_AI_T1_PREFLIGHT_OWNER_RECONCILIATION_AND_SNAPSHOT_VALUE_PROBE_WORKER_RETURN_2026-08-16.md`

Mixed-origin derived synthesis: REQUIRED

## Dispatch Prompt Envelope

Role: execute RSPB-AI-T1 as a documentation-only no-commit worker.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_RSPB_AI_T1_CAPABILITY_PREFLIGHT_OWNER_RECONCILIATION_AND_READ_ONLY_SNAPSHOT_VALUE_PROBE_2026-08-16.md`

Paired baseline: `docs/baselines/CVF_GC018_RSPB_AI_T1_CAPABILITY_PREFLIGHT_OWNER_RECONCILIATION_AND_READ_ONLY_SNAPSHOT_VALUE_PROBE_2026-08-16.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: resolve current HEAD at worker start; expected dispatch parent is recorded after dispatcher commit.

Do-not-misread notes: local source is a provenance-backed candidate, not CVF
authority. Read-only observation means bounded availability/version/path-status
facts only; it does not permit executing candidate scripts, reading secrets,
dumping environment variables, probing networks, installing, repairing, or
changing configuration.

Required first actions: read startup surfaces, guard orientation, literal
gotchas, paired baseline, MODS-T0 standard/corrective assessment, this packet,
selected local sources, current owner sources, and applicable checker sources.

Current-time notes: governed date is 2026-08-16; resolve actual HEAD and source
hashes at worker start, and disclose drift from the dispatch anchor.

Return contract: create exactly the three allowed outputs, set the worker
return to `COMPLETE_PENDING_REVIEW`, run required gates, and make no commit.

## Purpose

Determine whether the selected Capability Preflight profile/snapshot value can
be adapted into current CVF owners at a cost lower than the workflow value it
adds. Produce an owner reconciliation contract and a value-probe assessment;
do not implement the runtime candidate.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind source-intake --batch-id RSPB-AI-T1 --title "Capability Preflight Owner Reconciliation And Read-Only Environment Snapshot Value Probe" --date 2026-08-16 --base 29b2f32c6 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | source-intake plus WORKER_MUST_NOT_COMMIT profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact sources, output manifest, observation limits, decision enum, worker-return contract, and dual-agent boundary supplied |
| checkerReadAheadConfirmation | work-order, worker-return, absorption, mixed-origin, blind-spot, operation-trace, dual-agent, and public-disposition guards read |
| docOnlyNewFields | ownerFit, consumerEvidence, observationClass, valueCostDecision, implementationReopenCondition |
| claimBoundary | packet provenance only |

## Worker Autonomy / No-Question Rule

Repair in-manifest documentation/checker-shape defects and rerun gates without
asking the operator. Stop only for source contradiction, missing required
source, unsafe observation, or any need to touch a path/action outside scope.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`external-knowledge-absorption`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "external-knowledge-absorption" --role dispatcher --lifecycle-phase pre-dispatch --surface-selector "capability environment snapshot preflight owner reconciliation" --risk-ceiling MEDIUM --max-results 20 --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | `ADIF-0019`; `ADIF-0053` by direct relevance |
| Dispatch impact | preserve mixed-origin value, prohibit maturity-as-value, and require an explicit stop decision |

## Authority Chain

Operator continuation instruction -> active next-allowed move -> MODS-T0 standard and
corrective assessment -> paired GC-018 baseline -> this work order.

## Agent Roles

The worker inspects and authors the pending outputs. A different reviewer or
closer owns semantic acceptance, repair authorization beyond the manifest,
material commit, closure gate, and continuity update.

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| intakeType | selected mixed-origin source-family owner/value probe |
| intake summary | operator continued the MODS-T0 staged next action |
| scope classification | documentation-only three-output no-commit tranche |
| risk sensitivity | bounded observation; mutation/secrets/network/runtime parked |
| selected role route | `SINGLE_AGENT_MULTI_ROLE` with independent reviewer conversion |
| selectedRole | bounded source-analysis worker |
| rejectedRole | runtime implementer, installer, acquisition executor, deployer |
| routingReason | owner/value evidence must precede implementation authority |
| escalation condition | any need for source/runtime mutation, secret, network, provider, or extra path |
| authorityBoundary | worker has no commit or downstream-tranche authority |

## Allowed / Forbidden Scope

Allowed: read-only file/source inspection; bounded non-secret local command
availability/version observation; three exact output files; focused structural
gates. Forbidden: candidate-code execution; full environment-variable output;
secret/credential access; filesystem/network discovery beyond named commands;
dependency install/update/repair; source import; runtime/test/source edits;
hook wiring; provider/live; public sync; push; deployment; production.

## Required First Reads

- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION_MEMORY.md`
- `AGENT_HANDOFF_V59_2026-08-11.md`
- `docs/reference/guard_orientation/README.md`
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
- paired baseline and this work order
- `docs/reference/external_agent_review/CVF_MIXED_ORIGIN_DERIVED_SYNTHESIS_ABSORPTION_STANDARD.md`
- `docs/assessments/CVF_RSPB_AI_T0_MIXED_ORIGIN_CORRECTIVE_REASSESSMENT_2026-08-16.md`
- selected local paths in Source Verification and Source Inventory Scope
- current owner paths in Source Verification
- applicable checker sources listed below

## Pre-Flight Checks

1. Record `git rev-parse HEAD` and `git status --short --untracked-files=all`.
2. Stop if pre-existing changes overlap any allowed output.
3. Confirm all selected local source files and current owner sources exist.
4. Confirm no allowed output already exists with unrelated content.
5. Run pre-implementation autorun using the committed dispatch base.

## Write Ownership

The worker may create or edit exactly:

1. `docs/reference/capability_preflight_bootstrap/CVF_CAPABILITY_PREFLIGHT_OWNER_RECONCILIATION_CONTRACT_2026-08-16.md`
2. `docs/assessments/CVF_RSPB_AI_T1_CAPABILITY_ENVIRONMENT_SNAPSHOT_VALUE_PROBE_2026-08-16.md`
3. `docs/reviews/CVF_RSPB_AI_T1_PREFLIGHT_OWNER_RECONCILIATION_AND_SNAPSHOT_VALUE_PROBE_WORKER_RETURN_2026-08-16.md`

Every other path is read-only. Dispatcher-owned baseline/work order are not
worker-writable.

## Source Inventory Scope

The worker must fully read and terminally classify at least these selected
local sources; add directly dependent type/fixture files only when disclosed:

| Selected source | Required action |
| --- | --- |
| local profile `docs/reference/capability_preflight_bootstrap/README.md` | FULL_READ |
| local snapshot schema `schemas/capability-environment-snapshot.schema.json` | FULL_READ |
| local freshness policy `policies/CVF_CAPABILITY_SNAPSHOT_FRESHNESS_POLICY.md` | FULL_READ |
| local `environment.snapshot.ts` | FULL_READ |
| local `environment.scanner.ts` | FULL_READ |
| local read-only CLI example `examples/read-only-cli/ENVIRONMENT_SNAPSHOT.json` | FULL_READ |
| local read-only CLI example `examples/read-only-cli/READINESS_DECISION.json` | FULL_READ |
| directly referenced local types/scanners/fixtures | FULL_READ when added to inventory |

All local paths are rooted at `.private_reference/legacy/CVF 13.08/CVF_CAPABILITY_PREFLIGHT_BOOTSTRAP/`.

## Execution Plan

1. Build a selected-source inventory with size/hash, origin class, claim type,
   terminal disposition, and dependent-file reconciliation. Stop on unreadable
   or origin-unresolved evidence.
2. Map every candidate profile/snapshot invariant and field to a current CVF
   owner, an explicit owner gap, or rejection. Do not create a parallel owner.
3. Define the minimal CVF-native snapshot contract: observations only,
   freshness/TTL, redaction, fail-closed unknown state, workspace scope,
   evidence/authority separation, and invalidation triggers.
4. Evaluate named CADP T6/T6-R2 blocked workflows counterfactually: state what
   earlier decision the minimal snapshot could have changed and what it could
   not have prevented.
5. Optionally collect bounded read-only workspace observations for `git`,
   `python`, `node`, `npm`, and `npx` using command discovery and `--version`.
   Record only command name, AVAILABLE/MISSING/UNKNOWN, normalized executable
   path or redacted path class, and version. Do not enumerate PATH, environment
   variables, credentials, registries, caches, network, or unrelated tools.
6. Compare lane-specific implementation/test/maintenance cost with named
   consumer value. Select exactly one final value/cost decision.
7. Scaffold and complete the worker return, run all required gates, record the
   actual pending changed set, and stop without staging or committing.

## Mixed-Origin Derived Synthesis Provenance

artifactClass: PROVENANCE_BACKED_DERIVED_SYNTHESIS_CANDIDATE

authorityStatus: NON_AUTHORITATIVE_UNTIL_REVIEWED

| Input or concept | Origin class | Evidence basis | Claim type | Validation method | Current CVF owner | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| environment inventory pattern | UPSTREAM_REPOSITORY_BACKED | prior pinned RSPB evidence | upstream pattern | prior ledger; no rescan | external absorption core | CONTEXT_ONLY |
| CVF authority separation | CVF_PUBLIC_DERIVED | local design input checked against current CVF | design constraint | current owner sources | Guard Contract / Work Order | REVIEW |
| earlier environment blocker detection | OPERATOR_REQUIREMENT | operator continuation and CADP evidence | outcome | counterfactual workflow analysis | dispatcher / Execution Plane | ACCEPT_AS_REQUIREMENT |
| snapshot schema/profile | OPERATOR_AGENT_CO_DESIGNED | selected local source family | derived design | field/invariant owner reconciliation | owner review required | ADAPT_CANDIDATE |
| minimal read-only probe | MIXED_ORIGIN | design plus current workflow evidence | candidate behavior | bounded observation and value/cost analysis | prospective Execution Plane seam | PROBE_ONLY |

## Absorption Decision Vector

| Decision axis | Decision | Evidence | Cost boundary |
| --- | --- | --- | --- |
| Knowledge absorption | PROCEED_BOUNDED | selected profile/schema/invariants | three output artifacts |
| Direct import | REJECT_DIRECT_IMPORT | non-authoritative local code and owner mismatch | no copied implementation |
| Runtime activation | NOT_AUTHORIZED_VALUE_PROBE_ONLY | no accepted owner contract yet | observation evidence only |
| Authority promotion | REVIEW_REQUIRED | reviewer decides per field/owner | no automatic promotion |

## System-Chain Value Review

| Chain component | Evidence path | Existing CVF owner/gap | Value disposition | Readiness disposition | Next action |
| --- | --- | --- | --- | --- | --- |
| profile/invariants | selected local README | current cross-owner gap | ADAPT_CANDIDATE | reconcile | owner matrix |
| snapshot contract | schema/policy/types | owner unresolved | HIGH_VALUE_CANDIDATE | design only | minimal contract |
| observation | scanner/examples | prospective Execution Plane | RUNTIME_CANDIDATE | probe only | value/cost decision |
| consumer | CADP T6/T6-R2 evidence | dispatch/live workflow | VALUE_EVIDENCE | bounded historical evidence | counterfactual |
| acquisition | bootstrap sources | mutation owners | DEFER | parked | no action |

## External Repository Absorption Entry Control

| Field | Value |
| --- | --- |
| Source type | previously reconciled upstream plus selected mixed-origin local synthesis |
| Upstream or source-mirror disposition | comparison only; reuse pinned prior evidence |
| Enumeration or manifest plan | selected-source inventory and dependent-file closure; no full-corpus claim |
| Per-file terminal-ledger plan | terminal disposition for every selected/dependent file |
| Owner or overlap route | current Guard Contract, Execution Plane, Work Order, ASSF, review/freeze surfaces |
| Value-disposition route | separate knowledge/import/runtime/promotion decisions plus system-chain review |
| Claim boundary | selected family and read-only value probe only |

## Mandatory Blind-Spot Control Block

Treat local inputs as provenance-backed derived synthesis, not low-value
proposal residue. Maturity, absence from current owner paths, upstream reject
counts, and full-runtime cost are forbidden as standalone value rationales.

## External Absorption Core

| Field | Value |
| --- | --- |
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | selected family under `.private_reference/legacy/CVF 13.08/CVF_CAPABILITY_PREFLIGHT_BOOTSTRAP/` plus prior RSPB evidence |
| Enumeration command | filesystem-backed direct reads of selected inventory and disclosed dependencies |
| Manifest artifact or inline manifest | inline table: Source Inventory Scope in this work order; worker return refreshes it |
| Processing ledger artifact or inline ledger | inline table: Required action column in Source Inventory Scope |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | `docs/reference/capability_preflight_bootstrap/CVF_CAPABILITY_PREFLIGHT_OWNER_RECONCILIATION_CONTRACT_2026-08-16.md` planned output |
| Unresolved items | zero required for final proceed/stop; otherwise defer |
| Completion claim boundary | selected family only; no full-corpus or runtime claim |

## Corpus Completeness And Report Integrity

- Corpus task class: selected-family reconciliation.
- Corpus root: selected files and disclosed direct dependencies.
- Snapshot time: worker execution time.
- Enumeration command: filesystem-backed direct reads from Source Inventory Scope.
- Manifest artifact or inline manifest: worker-return Source Inventory.
- Manifest hash: per-file SHA-256.
- Processing ledger artifact or inline ledger: worker-return terminal ledger.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.
- Reconciliation: manifest=7; ledger_terminal=7; exclusions=198; unresolved=0 at dispatch planning; worker recomputes if direct dependencies are added.
- Unresolved files: 0 at dispatch planning; worker defers if recomputed unresolved is non-zero.
- Declared exclusions: unselected members of the prior local corpus.
- Unreadable or unsupported files: worker records exact count and defers if non-zero.
- Aggregation check: selected and dependency-added totals are separate.
- Drift check: current hashes recorded; no unselected-source freshness claim.
- Output traceability: retained fields route to owner-contract rows.
- Adversarial verification: reviewer checks dependencies and value false negatives.
- Corpus verdict: PARTIAL

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External repo or copied folder |
| Chain map route | source -> provenance -> owner/overlap -> split decisions -> review |
| Matching local-view guard | `governance/compat/check_mixed_origin_derived_synthesis_absorption.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_overlap_discipline.py` |
| Owner surface | three worker outputs |
| Disposition | PROCEED_BOUNDED_SELECTED_FAMILY |
| Claim boundary | no direct import, full-corpus claim, or runtime activation |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
| --- | --- | --- | --- | --- | --- |
| profile invariants | owner-separation doctrine | DOCTRINE_ADAPTED | owner contract | reconcile | no runtime |
| snapshot fields | reusable contract shape | PACKAGE_CANDIDATE | owner decision | reviewer disposition | no activation |
| observation semantics | prerequisite evidence | RUNTIME_CANDIDATE | prospective Execution Plane seam | value probe | no implementation |
| freshness/redaction cases | negative-proof shapes | CHECKER_CANDIDATE | future owner tests | retain conditionally | no wiring |
| local implementation | design evidence | REJECT_DIRECT_IMPORT | none | CVF-native rewrite only if later authorized | no import |
| acquisition family | parked context | NO_PACKAGE_OR_RUNTIME_VALUE | reopen index | no current action | no current runtime/package value |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| authority semantics | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-owner-binding.contract.ts` | CONFIRMED_EXISTING | snapshot must not grant authority | map |
| environment snapshot | OWNER_SURFACE_NOT_FOUND | OWNER_SURFACE_NOT_FOUND | canonical owner gap | evaluate Execution Plane fit |
| acquisition | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | ENRICH_EXISTING | higher-risk chain remains separately governed | keep parked |

## Rescan Intelligence Hardening

- Original source artifact: prior RSPB upstream/local intake plus selected local source family.
- Predecessor intake artifact: `docs/audits/CVF_RSPB_AI_T0_DUAL_CORPUS_INTAKE_AUDIT_2026-08-15.md`.
- Delta ledger status: bounded selected-family delta declared below.
- Routing matrix status: all mandatory lanes declared below.
- Semantic sampling status: high-risk claims sampled below.
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Delta category | Current treatment |
| --- | --- |
| UNCHANGED_FROM_INTAKE | upstream safety rejection and prior corpus accounting remain unchanged |
| CHANGED_DISPOSITION | local snapshot family changes from maturity-only defer to selected value probe |
| NEW_FINDING | current CVF has a prospective environment-observation owner gap and named blocker evidence |
| REMOVED_OR_REJECTED | direct local-code import and mutating acquisition remain rejected/out of scope |

### Follow-Up Routing Matrix

| Routing lane | RSPB-AI-T1 handling |
| --- | --- |
| DO_NOW | selected-source inventory, owner reconciliation, and value analysis |
| SEPARATE_RUNTIME_TRANCHE | minimal CVF-native snapshot implementation only if reviewer/operator later approve |
| STRATEGIC_OPERATOR_DECISION | acquisition/mutation, provider/live, public export, and deployment |
| OUT_OF_SCOPE | full local pack implementation, UI/MCP/CLI projection, and source-corpus execution |
| RESOLVED_BY_DESIGN | snapshot evidence remains separate from authority and direct import remains prohibited |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- |
| RSPB-T1-S1 | local profile Core invariants | snapshot is evidence, not authority | ADAPT_CANDIDATE | could this duplicate Guard Contract authority? | review owner separation |
| RSPB-T1-S2 | local snapshot schema dependencies | availability/blocking fields add value | RUNTIME_CANDIDATE | are these fields already owned or too costly? | require field-level owner/cost evidence |
| RSPB-T1-S3 | CADP T6 blocker evidence | earlier preflight could change workflow decisions | VALUE_EVIDENCE | is the counterfactual specific and bounded? | reviewer must verify |

## Foundation Storage Layout Block

| Content class | Governing location | RSPB-AI-T1 handling |
| --- | --- | --- |
| cross-owner profile contract | `docs/reference/capability_preflight_bootstrap/` | create one candidate contract |
| empirical/value assessment | `docs/assessments/` | create one bounded probe assessment |
| pending worker evidence | `docs/reviews/` | create worker return |
| runtime/source/tests | existing owner packages | no edit |
| corpus sources | private legacy reference | read-only |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: this tranche evaluates a selected family from the
already registered RSPB intake and neither introduces a new legacy family nor
claims coverage-index completeness.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| next tranche is owner reconciliation then read-only value probe | GOVERNED_DECISION | `docs/assessments/CVF_RSPB_AI_T0_MIXED_ORIGIN_CORRECTIVE_REASSESSMENT_2026-08-16.md` | Baseline Decision / Proposed Tranche | Capability Environment Snapshot | MODS-T0 correction | ACCEPT |
| snapshot evidence is distinct from authority | VALUE_SET | `.private_reference/legacy/CVF 13.08/CVF_CAPABILITY_PREFLIGHT_BOOTSTRAP/docs/reference/capability_preflight_bootstrap/README.md` | Core invariants | environment snapshot | derived profile | ACCEPT |
| local snapshot shape is explicit and reviewable | VALUE_SET | `.private_reference/legacy/CVF 13.08/CVF_CAPABILITY_PREFLIGHT_BOOTSTRAP/docs/reference/capability_preflight_bootstrap/schemas/capability-environment-snapshot.schema.json` | required/properties | dependency observations and verification | derived schema | ACCEPT |
| current Execution Plane has a real capability consumer | SOURCE_VISIBLE_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/cadp.capability.consumer.contract.ts` | module purpose and exported consumer | verified capability consumer | Execution Plane | ACCEPT |
| authority binding has a current Guard Contract owner | SOURCE_VISIBLE_BEHAVIOR | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-owner-binding.contract.ts` | exported validation/binding | owner binding | Guard Contract | ACCEPT |
| environment blockers affected an existing workflow | EVIDENCE_RECORD | `docs/reviews/CVF_CADP_AI_T6_LIVE_COMPATIBILITY_PROOF_WORKER_RETURN_2026-08-15.md` | Findings / Position | npm/npx prerequisites | CADP live proof | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_mixed_origin_derived_synthesis_absorption.py`; `governance/compat/check_absorption_blindspot_control_presence.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | exact worker-return contract fields, review headings, source inventory actions, provenance/decision/system-chain tokens, entry-control fields, public disposition |
| gateRunPurpose | post-authoring confirmation and worker output verification |
| claimBoundary | structure is machine-checkable; semantic owner/value judgment remains reviewer-owned |

## Dual Agent Surface Matrix

| Surface | Role | Interface | Authority / risk boundary | Required evidence | Adapter boundary |
| --- | --- | --- | --- | --- | --- |
| INTERNAL_AGENT | worker/reviewer workflow | governed files and local shell | read-only source analysis; no commit by worker | source inventory, diff, gates | repository-native only |
| EXTERNAL_AGENT_CLI_MCP | external worker projection | copied work-order text or file | same scope; no CLI/MCP runtime support claim | returned worker packet and actual changed set | DOCUMENTATION_ONLY_WITH_REASON: no adapter is authorized |
| operator | checkpoint owner | explicit decision | implementation/mutation/public authority remains operator-owned | later authorization | no automatic transition |

## Single-Agent Multi-Role Control Block

The route token describes the governed phase chain, not self-acceptance. The
worker stops at `COMPLETE_PENDING_REVIEW`; an independent reviewer/closer owns
semantic acceptance and commits. Escalation triggers are source contradiction,
manifest expansion, unsafe observation, or any forbidden action. Gate sequence:
pre-implementation -> worker-return fast gate -> independent review ->
reviewer-return gate -> material commit -> material-only pre-closure ->
separate continuity sync. No worker statement is closure evidence.

Role separation ledger: dispatcher commits authority; worker authors pending
outputs without commit; reviewer/closer independently inspects and commits.

Self-review boundary: worker checks are diagnostic evidence only and cannot
accept the worker's own conclusions.

## Agent Handoff Contract Control Block

Contract source: archive evidence citation `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

Current active handoff: `AGENT_HANDOFF_V59_2026-08-11.md`

| Field | Value |
| --- | --- |
| route | SINGLE_AGENT_MULTI_ROLE |
| rolePattern | WORKER_MUST_NOT_COMMIT |
| phase | source analysis and pending worker return |
| baseHeadFor(phase) | current committed dispatch HEAD at worker start |
| changedSetScope(phase) | exactly three write-owned outputs |
| traceScope(phase, actor) | source reads, bounded observations, output diff, gate evidence |
| commitOwner(phase) | reviewer/closer only |
| crossBatchIsolation | clean worktree required at dispatch/worker start; stop on overlapping changes |
| nextMoveSurfaces | reviewer decision; continuity only after accepted material commit |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_RSPB_AI_T1_CAPABILITY_PREFLIGHT_OWNER_RECONCILIATION_AND_READ_ONLY_SNAPSHOT_VALUE_PROBE_COMPLETION_2026-08-16.md` |
| reviewerOwnedClosurePaths | accepted three worker outputs; completion review; continuity separately |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

Worker result `COMPLETE_PENDING_REVIEW` is not closure. Reviewer must verify
selected-source completeness, field-level owner fit, observation safety,
consumer counterfactuals, value/cost arithmetic, exact changed manifest, and
all gates. Reviewer may choose proceed, stop, defer, or require bounded repair;
only reviewer/closer may commit.

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The return must include Purpose, Target / Source, Scope / Methodology,
Findings / Position, Risk / Corrective Action, Decision / Disposition, Claim
Boundary, Checker Source Read-Ahead Block, Agent Operation Trace Block,
External Knowledge Intake Routing, Epistemic Process Block, Public Export
Disposition, Source Inventory, actual git status, and all required N/A blocks.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
| --- | --- |
| claimScope | selected-source owner reconciliation and bounded read-only observation evidence |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | N/A with reason: this tranche creates no runtime receipt |
| actionEvidence | ACTION_EVIDENCE_PRESENT: source inventory, command summaries, and file diff |
| invocationBoundary | governed reads and three documentation outputs only |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | value probe and contract proposal, not runtime implementation |
| forbiddenExpansion | candidate execution, acquisition, mutation, runtime, secrets, network/provider, public/deploy/production |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: a reduced snapshot contract has positive value
for environment-prerequisite failures, while the full local system and
mutating acquisition remain too costly for immediate implementation.

Evidence Comparison Requirement: compare selected sources, current owners,
bounded observations, and CADP counterfactuals against that prediction.

Contradiction Handling Requirement: contradictory evidence requires a
Contradiction Or Gap Disposition and narrowed claim boundary.

Claim Update Requirement: record confirmed, revised, narrowed, or invalidated.

## Evidence Requirements

- selected-source inventory with hashes and zero unresolved;
- owner/field/invariant reconciliation matrix;
- named consumer and blocked-workflow counterfactual;
- bounded observation ledger or `NOT_RUN_WITH_REASON`;
- cost table separating knowledge, contract, implementation, testing, and maintenance;
- one exact final decision token;
- actual pending changed set and no-commit proof.

dispatchBaseHead: 29b2f32c6

executionBaseHead: resolve current committed dispatch HEAD at worker start

closureBaseHead: N/A - pending independent review

## Acceptance Criteria

- [ ] Three and only three worker-owned outputs exist.
- [ ] Selected and directly dependent source files reconcile with zero unresolved.
- [ ] Every retained field/invariant has a current owner or explicit owner gap.
- [ ] No value claim relies on unmerged/unreviewed maturity or file counts.
- [ ] No candidate script, dependency install, secret read, network call, or environment mutation occurred.
- [ ] Final decision is exactly `PROCEED_TO_IMPLEMENTATION_WORK_ORDER`, `STOP_COST_EXCEEDS_VALUE`, or `DEFER_EVIDENCE_INSUFFICIENT`.
- [ ] Worker return is `COMPLETE_PENDING_REVIEW` and uncommitted.

Fail conditions:

- [ ] any required source is unreadable or origin remains unresolved;
- [ ] value requires a new parallel authority owner;
- [ ] meaningful evidence requires mutation, secrets, network/provider access, or candidate execution;
- [ ] changed paths exceed the exact manifest.

## Verification Commands

```powershell
python governance/compat/run_worker_return_scaffold.py --write docs/reviews/CVF_RSPB_AI_T1_PREFLIGHT_OWNER_RECONCILIATION_AND_SNAPSHOT_VALUE_PROBE_WORKER_RETURN_2026-08-16.md --title "CVF RSPB-AI-T1 Preflight Owner Reconciliation And Snapshot Value Probe Worker Return"
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/check_mixed_origin_derived_synthesis_absorption.py --base 29b2f32c6 --head HEAD --enforce --json
python governance/compat/check_absorption_blindspot_control_presence.py --base 29b2f32c6 --head HEAD --enforce
git diff --check
git status --short --untracked-files=all
```

The worker must not run a committed-range closure command or commit. The
reviewer later runs reviewer-return and pre-closure gates using material-only
and continuity ranges separately.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | bounded source-analysis worker |
| Provider or surface | provider-neutral local repository workspace |
| Session or invocation | RSPB-AI-T1 worker session |
| Working directory | repository root |
| Command or tool surface | governed reads, bounded command discovery/version observation, apply_patch, worker-return gates |
| Target paths | exact three-path worker manifest |
| Allowed scope source | operator continuation, active next move, paired baseline, this work order |
| Before status evidence | clean worktree at dispatcher base `29b2f32c6`; worker records current HEAD and full short status before editing |
| After status evidence | worker records three pending outputs and any disclosed pre-existing change |
| Diff evidence | `git diff --name-status`; untracked output listing |
| Approval boundary | documentation-only value probe; no implementation authority |
| Claim boundary | repo-local and bounded workspace observation only |
| Deletion or rename disposition | N/A with reason: no deletion or rename authorized |
| Agent type | no-commit source-analysis worker |
| Invocation ID | rspb-ai-t1-worker-2026-08-16 |
| Expected manifest | exact three worker-owned output paths |
| Actual changed set | required in worker return |
| Manifest delta | required in worker return; must be zero or explicitly blocked |

## Review Gate

Dispatch requires pre-dispatch PASS. Worker execution requires
pre-implementation PASS. Closure requires an independent semantic review,
reviewer-return PASS, material commit by reviewer/closer, material-only
pre-closure PASS, then a separately verified continuity commit if state changes.

## Operator Checkpoint

No checkpoint is needed for documentation-only execution. A fresh explicit
operator checkpoint is mandatory before implementation, candidate execution,
acquisition/mutation, provider/live, public sync, deployment, or production.

## Closure Checklist

- [ ] worker output manifest contains exactly three paths;
- [ ] selected-source ledger reconciles with zero unresolved or defers;
- [ ] owner and counterfactual evidence support one exact decision token;
- [ ] worker-return fast gate and focused absorption guards pass;
- [ ] worker records real pending status and makes no commit;
- [ ] reviewer independently checks semantics and changed set;
- [ ] reviewer/closer owns completion review, material commit, and material-only pre-closure;
- [ ] continuity, if needed, is a separate commit and range;
- [ ] no forbidden runtime/public action occurred.

## Return-To-Orchestrator Conditions

Return `BLOCKED` without continuing if a fail condition occurs, evidence needs
out-of-scope authority, or the required final decision cannot be supported.
Do not convert missing evidence into `STOP_COST_EXCEEDS_VALUE`.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private mixed-origin source/owner/value analysis; no public artifact or
public-sync authority exists.

## Claim Boundary

This work order authorizes no source import, candidate execution, acquisition,
environment mutation, runtime activation, transport/route, MCP/CLI adapter,
provider/live proof, secret access, public sync, push, deployment, production,
or automatic downstream tranche.
