# CVF Task-Proportional Governance Second Upgrade External Critique Plan

Memory class: governed-planning-review

Status: PROPOSED_PENDING_EXTERNAL_CRITIQUE

docType: planning_review

Date: 2026-08-17

baseHead: `8f95a645f87f5fa94bcf9d36b0314c37c2d28c8f`

## Purpose

Define a critique-ready plan for the second upgrade of Task-Proportional
Governance Routing (TPGR). The intended outcome is governance whose cost
follows the actual task, claim, uncertainty, and effect boundary while CVF
remains the canonical authority and new knowledge continues to receive
rigorous semantic review.

This is a planning artifact only. It does not amend the active TPGR standard,
authorize selective gate execution, open RSPB-AI-T15, or dispatch an
implementation worker.

## Scope / Target / Owner Boundary

In scope:

- redesign the routing model after TPGR-T0 shadow operation;
- distinguish source provenance from the work currently being performed;
- reuse accepted corpus and cluster evidence without weakening freshness or
  semantic inspection;
- map routed bundles to concrete checkers and their dependencies;
- define fail-closed escalation and full-bundle triggers;
- define shadow, replay, adversarial, canary, activation, and rollback stages;
- prepare explicit questions for an independent external critique.

Out of scope:

- modifying a standard, schema, registry, checker, hook, or autorun catalog;
- selecting or absorbing another RSPB capability cluster;
- implementing T15 or any other feature tranche;
- provider/live calls, credentials, network access, public sync, deployment,
  production, destructive operations, or runtime activation.

Proposed long-term owner remains
`docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md`.
No second canonical TPGR owner should be created by implementation.

## Startup And Operator Checkpoint

Current mode:
`task_proportional_governance_second_upgrade_plan_pending_claude_critique`.

Operator checkpoint: obtain independent critique of this plan, reconcile the
critique in a separate review artifact, and obtain operator approval before
authoring any implementation baseline or work order.

Implementation before that checkpoint is forbidden.

## Source Verification

| Source | Verified proposition | Disposition |
| --- | --- | --- |
| `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md` | TPGR-T0 classifies manifests but deliberately retains the full legacy gate bundle; selective execution awaits later equivalence evidence. | ACCEPT |
| `governance/compat/CVF_TASK_GOVERNANCE_ROUTE_REGISTRY.json` | The active registry owns eight classification dimensions, five profiles, ten abstract bundles, path minimums, and the full-gate fallback. | ACCEPT |
| `governance/compat/route_task_governance.py` | The current router selects explanatory bundles but returns `selectiveExecutionAuthorized: false` and does not resolve bundles into concrete commands. | ACCEPT |
| `docs/reference/external_agent_review/CVF_MIXED_ORIGIN_DERIVED_SYNTHESIS_ABSORPTION_STANDARD.md` | A co-designed local pack is a provenance-backed candidate; fresh manifest/ledger evidence is reusable and semantic review defaults to bounded capability clusters. | ACCEPT |
| `docs/reviews/CVF_MIXED_ORIGIN_ABSORPTION_LATENCY_AND_VALUE_PRESERVATION_LEARNING_2026-08-16.md` | Repeated semantic adjudication and extra value-probe tranches are known cost defects when no decision-changing gap exists. | ACCEPT |
| `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md` | Prior complete or partial scan state must be inherited; any repeated scan begins only from a justified delta. | ACCEPT |
| `docs/reference/review_cost_control/CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md` | Review should use one bounded dependency audit, focused proof, one phase gate, and a bounded commit plan. | ACCEPT |
| `docs/audits/CVF_RSPB_AI_T0_CAPABILITY_PREFLIGHT_BOOTSTRAP_PROPOSAL_MANIFEST_2026-08-15.json` | Existing immutable manifest evidence covers the 205-file local corpus. | ACCEPT |
| `docs/audits/CVF_RSPB_AI_T0_CAPABILITY_PREFLIGHT_BOOTSTRAP_PROPOSAL_FILE_LEDGER_2026-08-15.json` | Existing file-level processing evidence may be reused by later selected clusters subject to freshness and contradiction triggers. | ACCEPT |

No provider-specific memory, external-agent conversation, or unpublished
review response is treated as CVF authority.

## Problem Statement

TPGR-T0 fixed classification visibility but not execution cost. Three distinct
concerns are still collapsed:

1. **Provenance** - where a concept came from and what evidence supports it.
2. **Current task** - intake, semantic selection, CVF-native conversion,
   runtime activation, release, or another operation.
3. **Verification effect** - which concrete guards can detect a defect in the
   changed paths and claims during the current lifecycle phase.

Consequently, a small CVF-native conversion selected from an already accepted
205-file local ledger can still look like a new external-repository intake.
The packet repeats absorption ceremony and the repository executes every
legacy guard even when most guards cannot observe the change. More guards are
not automatically stronger governance; relevant guards, valid inherited
evidence, and fail-closed escalation are stronger governance per unit cost.

## Design Principles

1. CVF remains the source of truth. Derived material becomes canonical only
   through an existing CVF owner or an explicitly approved new owner.
2. Provenance is evidence metadata, not a permanent task-risk label.
3. New or changed knowledge is read semantically; already accepted evidence is
   inherited until a named invalidation trigger fires.
4. File count never overrides novelty, authority impact, uncertainty, external
   effect, reversibility, or claim criticality.
5. Every skipped checker needs a deterministic reason and dependency proof.
6. Unknown classification, dependency-map drift, receipt mismatch, or scope
   expansion escalates; it never silently reduces verification.
7. Safety, authority, live, public, secret, destructive, and irreversible
   boundaries remain fail-closed.
8. Selective execution activates progressively only after bounded equivalence
   and seeded-defect evidence, with the full bundle always available as
   fallback.
9. Governance artifacts are created only when they carry durable decision or
   evidence value; ceremony is not evidence.

## Proposed Model A - Separate Provenance From Task Stage

Add an orthogonal `sourceContext` block rather than encoding provenance only
through `taskKind: EXTERNAL_ABSORPTION`:

| Field | Proposed values | Purpose |
| --- | --- | --- |
| `originClass` | `CVF_NATIVE`, `NEW_EXTERNAL_SOURCE`, `REUSED_ACCEPTED_CORPUS`, `PROVENANCE_BACKED_DERIVED_SYNTHESIS`, `MIXED_ORIGIN`, `UNRESOLVED` | Records where the relevant knowledge comes from. |
| `intakeStage` | `NONE`, `I0_NEW_CORPUS_INTAKE`, `I1_CLUSTER_SELECTION`, `I2_CVF_NATIVE_CONVERSION`, `I3_AUTHORITY_OR_RUNTIME_PROMOTION` | Records the current absorption lifecycle stage. |
| `evidenceState` | `NEW`, `INHERITED_FRESH`, `DELTA_REFRESHED`, `INVALIDATED`, `MISSING` | Records whether earlier proof is reusable. |
| `ownerFit` | `EXISTING_OWNER_EXACT`, `EXISTING_OWNER_COMPOSITION`, `OWNER_GAP`, `OWNER_CONFLICT`, `UNKNOWN` | Makes owner overlap explicit. |
| `decisionUncertainty` | `LOW`, `MEDIUM`, `HIGH`, `BLOCKED` | Routes semantic uncertainty separately from provenance. |

Routing consequence:

- I0 performs manifest, completeness, provenance, and terminal-ledger work.
- I1 fully reads the selected cluster and decides value/owner fit without
  re-adjudicating unrelated files.
- I2 is classified by the CVF-native change being made. A pure contract under
  an existing owner is not perpetually treated as fresh external intake merely
  because its design lineage includes a local synthesis corpus.
- I3 separately evaluates authority promotion, state, runtime, provider/live,
  public, or destructive effects.

Provenance references remain attached through all stages. Separation does not
erase lineage or permit direct copy/paste into arbitrary CVF paths.

## Proposed Model B - Typed Evidence Inheritance

Introduce a closed-shape `evidenceInheritance` block whose references are
validated before routing:

| Evidence type | Minimum binding |
| --- | --- |
| corpus inventory | manifest path, hash algorithm, manifest hash, file count |
| file-level processing | terminal-ledger path, hash, reconciliation totals |
| selected cluster | exact file paths and current hashes; full semantic read receipt |
| provenance | applicable origin graph and unresolved-origin count |
| owner mapping | current CVF owner paths and owner-fit disposition |
| decision | prior value/readiness disposition and claim boundary |
| checker map | checker-inventory version and dependency-graph digest |

Inheritance is allowed only when all referenced artifacts exist, hashes match,
the selected source hashes match, the current owner has not materially changed,
and the new task makes no broader completeness or absence claim.

### Mandatory invalidation triggers

Any trigger below changes `evidenceState` to `DELTA_REFRESHED`, `INVALIDATED`,
or `MISSING` and selects the required stronger route:

- corpus root, manifest hash, ledger hash, or selected-file hash changed;
- selected scope expanded beyond the accepted ledger;
- provenance is unresolved or contradicts the prior origin graph;
- current CVF owner moved, changed semantics, or conflicts with the prior map;
- a new completeness, absence, equivalence, safety, or runtime-effect claim is
  introduced;
- prior evidence is unreadable, structurally invalid, or outside its freshness
  policy;
- reviewer identifies a named decision-changing uncertainty;
- actual changed paths or external effects exceed the routed manifest.

No trigger means reuse the accepted 205-file evidence and inspect only the
selected capability cluster plus its current CVF owner/dependencies.

## Proposed Model C - Claim-And-Impact Routing

Retain the useful TPGR-T0 dimensions and add the decision dimensions that are
currently implicit:

- `ownerFit`;
- `decisionUncertainty`;
- `changeImpact`: `LOCAL_LEAF`, `OWNER_COMPOSITION`, `CROSS_OWNER`,
  `CONTROL_PLANE`, `RUNTIME_OR_EXTERNAL`;
- `claimClasses`: explicit set such as documentation, contract behavior,
  schema compatibility, authority, completeness, runtime, live, public, or
  destructive;
- `lifecyclePhase`: `PLAN`, `DISPATCH`, `WORKER_RETURN`, `REVIEW`, `CLOSURE`,
  `CONTINUITY`, `PUBLIC_RELEASE`.

Profile is the maximum of all applicable minimums. Neither a small diff nor an
inherited corpus receipt can downgrade authority, safety, runtime, secret,
public, destructive, or irreversible risk.

## Proposed Model D - Concrete Guard Dependency Graph

Replace abstract bundle counting with a versioned inventory of concrete
commands. Each checker record should declare:

- checker ID and command;
- applicable path families and artifact types;
- claim/content triggers;
- lifecycle phases;
- prerequisite and downstream checker IDs;
- protected owners whose changes force selection;
- cache inputs: checker source hash, dependency hashes, changed-path digest,
  manifest digest, and relevant evidence-receipt digests;
- skip reason vocabulary;
- full-bundle escalation conditions.

The router computes a dependency closure, not a flat list. If checker B depends
on the output or invariant of checker A, selecting B also selects A. A changed
checker, registry, generator, hook, or routing owner invalidates cached results
and forces the governance-maintenance route.

### Always-on minimum core

The proposed minimum core is intentionally small:

1. route-manifest/schema validation;
2. actual-diff versus authorized-path reconciliation;
3. protected-path and external-effect escalation check;
4. checker-inventory/dependency-graph freshness;
5. no-secret/no-destructive-boundary check when those detectors can inspect
   the changed material safely;
6. phase receipt integrity.

The external critique must challenge whether each item belongs in the
always-on core and identify any missing invariant whose omission could allow a
high-impact false negative.

## Proposed Model E - Phase-Specific Verification

| Phase | Default proof | Added when triggered |
| --- | --- | --- |
| plan | source/owner verification and critique questions | corpus accounting only for new or changed corpus claims |
| dispatch | manifest validity, exact path authorization, source-read contract | delegation/handoff and risk-specific checkpoints |
| worker return | diff/manifest reconciliation, focused tests, applicable artifact/checker set | code, state/security, runtime/live, corpus, or public bundles selected by impact |
| review | independent semantic dependency audit and adversarial tests | stronger owner, authority, security, or uncertainty probes |
| closure | closure evidence, accepted findings, exact commit range | roadmap/registry/system-chain updates only when the task changes them |
| continuity | generated-state integrity and active-handoff alignment | no implementation or absorption bundle by default |
| public release | full public/repository/release chain | provider/live proof when the release claim requires it |

A lifecycle phase must not inherit a prior phase's PASS when its inputs changed.
It may reuse a PASS when every declared cache input is identical and the
checker explicitly supports receipt reuse.

## Proposed Model F - Full-Bundle Escalation Triggers

The complete legacy bundle remains mandatory when any of these conditions is
true:

- route manifest invalid, incomplete, contradictory, or self-downgraded;
- checker inventory or dependency graph is stale or cannot resolve closure;
- actual paths, claims, or effects exceed the authorized manifest;
- governance machinery, canonical authority, hooks, generators, or the router
  itself changes;
- `decisionUncertainty` is `HIGH` or `BLOCKED` for an authority, safety,
  runtime, live, public, destructive, or irreversible claim;
- new corpus completeness/absence or cross-owner equivalence is claimed;
- secret value, regulated data, provider/live, public write, destructive, or
  irreversible effects are present;
- selective and full results diverge during shadow/canary operation;
- reviewer invokes a documented escalation because focused proof exposed a
  decision-changing contradiction.

P3/P4 does not always mean every unrelated checker forever. It means the
relevant high-risk dependency closure plus any explicit full-bundle trigger.
During initial activation, P3/P4 should retain full legacy execution until
separate evidence supports a narrower policy.

## Absorption Route For The Existing 205-File Local Corpus

The accepted local corpus is classified as
`PROVENANCE_BACKED_DERIVED_SYNTHESIS`, not as an arbitrary external repository
and not as CVF authority. Its existing manifest and terminal ledger remain the
corpus evidence baseline.

For a later selected cluster:

1. recompute hashes only for selected files and validate ledger references;
2. fully read the substantive selected files and relevant use cases;
3. inspect current CVF owner and direct dependencies;
4. classify the current conversion task by its actual change/effect boundary;
5. implement through the existing CVF owner using CVF conventions;
6. run focused code/contract tests and the routed dependency closure;
7. perform independent semantic review;
8. refresh the full corpus only if an invalidation trigger fires.

This route forbids bulk copy/paste. Source structures are inputs to analysis;
accepted value is adapted into coherent CVF owners, terminology, invariants,
tests, and claim boundaries.

## Cost Controls And Telemetry

Every shadow or active route receipt should record:

- selected, skipped, reused, and escalated checker counts;
- command wall time and repeated-command count;
- cache hit/miss with digest basis;
- full-bundle comparison result when dual-run applies;
- defects detected uniquely by selective, focused, reviewer, or full proof;
- packet/artifact count by lifecycle phase;
- repeated-read counts: corpus files, selected files, owner files;
- escalation reason and whether it changed the decision.

Cost reduction is accepted only when safety and authority detection remain
boundedly equivalent for the evaluated tranche classes. A faster route with an
unexplained missed material defect fails activation.

## Proposed Delivery Sequence

### TPGR-U2-P0 - External critique and operator decision

- Transfer this artifact to an independent external reviewer.
- Require a written challenge against the questions below.
- Reconcile accepted, modified, and rejected recommendations in CVF.
- Obtain explicit operator approval for an implementation roadmap.

Exit: reviewed design decision only; no machine change.

### TPGR-U2-P1 - Taxonomy and receipt contract in shadow

- Amend the existing TPGR owner rather than creating a parallel standard.
- Define source context, intake stages, evidence inheritance, uncertainty,
  owner fit, change impact, phase, and invalidation vocabulary.
- Extend schema/registry/router with closed-shape receipts.
- Continue full legacy execution.

Exit: deterministic classification and evidence invalidation tests pass.

### TPGR-U2-P2 - Concrete checker inventory and dependency graph

- Inventory current guard commands by phase, path, artifact, claim, and
  dependency.
- Detect unmapped commands and graph drift fail-closed.
- Emit an executable selective plan but do not execute selectively.

Exit: every legacy command is mapped, explicitly global, or blocked with an
owner; no silent orphan checker.

### TPGR-U2-P3 - Historical replay and seeded-defect evaluation

- Replay representative low-, medium-, elevated-, and critical-risk tranches.
- Include the seven-file profile/policy example, pure local contract clusters,
  governance-checker changes, continuity-only changes, provider/live work, and
  public-release work.
- Seed known defects involving source drift, unauthorized paths, owner
  conflict, schema mismatch, fail-open behavior, secret exposure, and closure
  mismatch.
- Compare proposed selection with the full legacy result.

Exit: no unexplained material false negative; all differences classified.

### TPGR-U2-P4 - Dual-run canary

- Execute selective plan and full legacy bundle in the same governed ranges.
- Treat selective results as advisory only.
- Collect cost, divergence, and defect attribution telemetry.
- Automatically fall back on any invalidation or divergence trigger.

Exit: operator-approved evidence threshold achieved for named task classes.

### TPGR-U2-P5 - Progressive selective activation

- Activate first for P0/P1 read-only, docs, and pure local existing-owner work.
- Expand to eligible P2 bounded clusters only after independent acceptance.
- Keep P3/P4 full-gate by default until separately proven.
- Retain operator override and deterministic full-bundle fallback.

Exit: selective execution is authorized only for an explicit allowlist of
task classes, phases, and checker-inventory versions.

### TPGR-U2-P6 - Absorption and project-governance adoption

- Apply the same routing semantics to future CVF knowledge intake and
  CVF-governed project delivery.
- Project code remains governed by its task effects and claims; merely using
  CVF does not require every CVF repository guard.
- New external knowledge still enters through intake/provenance controls;
  previously accepted evidence follows inheritance and invalidation rules.

Exit: documented examples and independent review show consistent routing
without authority dilution or structural copy/paste.

## Evaluation Matrix

| Scenario | Expected route | Must not happen |
| --- | --- | --- |
| seven short profile/policy templates already in accepted cluster | I2 CVF-native bounded conversion; selected hashes/read + owner tests + relevant artifact/code/review checks | repeated full 205-file scan or fresh external-repository intake ceremony |
| pure local contract under unchanged owner | P1/P2 according to delegation; focused code dependency closure | runtime/live/public/corpus bundles without a trigger |
| new external repository | I0 intake with manifest, provenance, completeness, ledger, semantic dispositions | reuse claim without a valid receipt |
| changed canonical standard or checker | P3 governance-maintenance route and full fallback during initial activation | self-selective verification of the router/checker being changed |
| continuity-only sync | continuity and integrity checks | rerun unrelated implementation or corpus proof |
| provider/live proof | P4 with real-call and diagnostic controls | cache or mock substituted for required current live evidence |
| public release or destructive action | P4 complete release/destructive chain and operator checkpoint | selective downgrade from small file count |
| owner conflict or high uncertainty | escalation and named decision checkpoint | value silently discarded or authority silently promoted |

## Questions Required From The External Critique

The external reviewer should answer each item with `ACCEPT`, `MODIFY`, or
`REJECT`, a rationale, and a concrete alternative where applicable:

1. Does separating `originClass` and `intakeStage` from `taskKind` preserve
   provenance while preventing permanent over-classification?
2. Are the evidence bindings and invalidation triggers sufficient to prevent
   stale ledger or owner-map reuse?
3. Which proposed always-on core checks are unnecessary, and which missing
   invariant could cause a material false negative?
4. Can the concrete checker dependency graph be maintained without becoming a
   second high-cost governance system? Propose the smallest reliable schema.
5. Are the full-bundle triggers too broad or too narrow for authority, safety,
   live, public, destructive, and irreversible work?
6. What bounded equivalence threshold should be required before P0/P1 and P2
   selective activation? Avoid unsupported claims of universal equivalence.
7. How should semantic reviewer judgment interact with deterministic routing
   without allowing either silent downgrade or automatic over-escalation?
8. Does the proposed route for the accepted 205-file corpus still inspect
   enough content to absorb new knowledge correctly and adapt it coherently
   into CVF owners?
9. Which historical or seeded adversarial cases are missing from P3?
10. What rollback signal should immediately return all tasks to the full
    legacy bundle?
11. Identify any place where this plan creates new ceremony whose cost exceeds
    its control value.
12. Give a final disposition: `PROCEED_TO_REVISED_PLAN`,
    `REVISE_BEFORE_IMPLEMENTATION_PLANNING`, or `REJECT_AND_REDESIGN`.

## Critique Return Contract

The external critique should contain:

- exact plan identity and hash supplied by the operator;
- per-question disposition;
- strongest three failure modes;
- proposed schema or routing changes;
- activation/equivalence objections;
- absorption-specific objections;
- final disposition;
- explicit statement that the critique is advisory input and not CVF
  authority or implementation authorization.

The operator may paste the critique back into the reviewer/orchestrator
session. The next CVF action is reconciliation of that critique, not immediate
implementation.

## Acceptance Criteria For This Planning Stage

- one critique-ready plan exists under a CVF-governed assessment path;
- current TPGR-T0 remains unchanged and selective execution remains false;
- the 205-file manifest/ledger is referenced as reusable evidence, not re-enumerated;
- CVF authority and CVF-native adaptation boundaries are explicit;
- full fallback and high-risk escalation remain explicit;
- external critique questions cover safety, cost, evidence freshness,
  dependency mapping, activation, and rollback;
- no T15, baseline, work order, checker, hook, runtime, provider, public, or
  deployment action is opened.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_docs_governance_compat.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_mixed_origin_derived_synthesis_absorption.py`; `governance/compat/check_absorption_blindspot_control_presence.py`; `governance/compat/check_rescan_intelligence_hardening.py` |
| literalTokensReviewed | metadata, purpose/scope/source/risk/decision/claim-boundary headings; operation trace fields; public disposition; compact N/A disposition |
| gateRunPurpose | confirm planning-artifact structure and boundary only; no implementation or selective-execution proof |
| claimBoundary | plan shape and critique readiness only |

## External Repository Absorption Entry Control

Source type: COMPARISON_ONLY_NO_ABSORPTION.

Upstream/source-mirror disposition: no new external repository, mirror, or
copied folder enters scope. The plan references already governed RSPB evidence
only.

Enumeration/manifest plan: reuse the accepted 205-file manifest as a cited
planning example; do not enumerate or repeat its scan.

Per-file terminal-ledger plan: reuse the accepted terminal ledger; no row is
changed by this plan.

Owner/overlap route: proposed TPGR changes enrich the existing TPGR owner only.

Value-disposition route: planning recommendation pending independent critique
and operator decision.

Claim boundary: comparison and process design only.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | existing governed evidence; no new intake |
| Route | COMPARISON_ONLY_NO_ABSORPTION |
| Local guard | current mixed-origin and absorption blind-spot controls remain unchanged |
| Disposition | PLAN_FOR_CRITIQUE_ONLY |
| Claim boundary | no source promotion, import, or runtime activation |

## Mixed-Origin Derived Synthesis Provenance

Mixed-origin derived synthesis applicability: NOT_APPLICABLE_WITH_REASON -
this artifact does not evaluate or absorb a new local pack. It cites the
already governed RSPB local synthesis solely as a routing test case.

manifestLedgerReuse: REUSE_IF_FRESH

semanticReviewUnit: CAPABILITY_CLUSTER

defaultValuePosture: PRESERVE_UNTIL_CONTRADICTED

additionalValueProbe: SKIP_UNLESS_NAMED_GAP

latencyBudget: SINGLE_PASS_BOUNDED

## Absorption Decision Vector

| Decision axis | Decision | Evidence | Cost boundary |
| --- | --- | --- | --- |
| Knowledge intake | NO_NEW_INTAKE_IN_THIS_PLAN | existing governed standards only | no corpus work |
| Direct import | REJECT_DIRECT_IMPORT | CVF authority boundary | no copied implementation |
| Runtime activation | NOT_AUTHORIZED | operator checkpoint | no runtime work |
| Authority promotion | NOT_AUTHORIZED | critique pending | no rule change |

## System-Chain Value Review

| Chain component | Evidence path | Existing CVF owner/gap | Value disposition | Readiness disposition | Next action |
| --- | --- | --- | --- | --- | --- |
| TPGR classification | `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md` | existing owner; task/provenance coupling gap | ENRICH_EXISTING_CANDIDATE | PLAN_ONLY | external critique |
| routing implementation | `governance/compat/route_task_governance.py` | abstract bundle selection only | ENRICH_EXISTING_CANDIDATE | NOT_AUTHORIZED | wait for approved roadmap |
| guard execution | current autorun/hook catalogs | concrete dependency map absent | NEW_GOVERNANCE_CANDIDATE_WITHIN_EXISTING_OWNER | NOT_AUTHORIZED | critique maintenance cost |
| RSPB evidence reuse | accepted manifest and ledger | rules exist but full gates remain | PRESERVE | EVIDENCE_REUSE_ONLY | use as replay case |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON
- N/A with reason: this planning artifact performs no corpus scan, intake
  refresh, completeness update, or absence claim; it only proposes future
  evidence-invalidation rules against already governed receipts.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - this planning artifact makes no
  new complete-corpus claim and does not modify the accepted 205-file manifest
  or ledger.

## Risk / Corrective Action

Primary risk: selective routing could miss a material defect because checker
applicability or dependencies were mapped incorrectly.

Corrective action: retain full execution through taxonomy and mapping stages;
require historical replay, seeded defects, dual-run canaries, divergence
fallback, progressive allowlisting, and independent review before activation.

Secondary risk: evidence reuse could become a pretext for shallow semantic
review.

Corrective action: reuse corpus accounting, not selected-file understanding.
Every selected cluster still requires current hashes, substantive full reads,
use-case inspection, owner mapping, focused proof, and independent review.

## Evidence / Verification

| Check | Result |
| --- | --- |
| exact changed-path reconciliation | PASS: this planning assessment only before its material commit |
| markdown structural completeness | PASS |
| docs governance compatibility | PASS |
| absorption and compact non-scan applicability guards | PASS without creating a synthetic corpus packet |
| reviewer-fast gate | PASS 65/65 after ASCII normalization |
| pre-commit governance chain | required at material commit |
| provider/live calls | zero |

## Decision / Disposition

`SEEK_EXTERNAL_CRITIQUE_BEFORE_IMPLEMENTATION_PLANNING`

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE_PLANNING.

Expected Result / Prediction: separating provenance, task stage, evidence
freshness, and concrete checker applicability should remove repeated corpus
ceremony and unrelated gates while preserving fail-closed escalation.

Evidence Comparison: TPGR-T0 exposes deterministic classification but retains
the full legacy bundle; the mixed-origin learning already proves that accepted
ledger evidence must not be re-adjudicated without a named gap. This plan
combines those current facts but has not yet established selective-execution
equivalence.

Contradiction Or Gap Disposition: the unresolved gap is whether a maintainable
checker dependency graph and bounded activation threshold can avoid material
false negatives. Independent critique and later replay evidence are required.

Claim Update: no active governance claim changes. The proposal is ready for
critique only.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | reviewer/orchestrator planning role |
| Provider or surface | local private provenance repository |
| Session or invocation | TPGR second-upgrade plan, 2026-08-17 |
| Working directory | repository root |
| Command or tool surface | governed source reads, repository search, planning authoring, structural checks, Git |
| Target paths | this planning assessment plus later continuity-only state update |
| Allowed scope source | operator instruction to finish T14, then draft a plan for external critique before implementation |
| Before status evidence | clean T14 closure HEAD `8f95a645f87f5fa94bcf9d36b0314c37c2d28c8f` |
| After status evidence | plan structurally compliant; reviewer-fast PASS 65/65; material commit pending |
| Diff evidence | exact changed-path output before commit |
| Approval boundary | plan and critique handoff only |
| Claim boundary | no TPGR implementation, selective execution, T15, runtime/provider/live, public, deploy, or production |
| Agent type | reviewer/orchestrator |
| Invocation ID | `tpgr-second-upgrade-plan-20260817` |
| Expected manifest | this one planning assessment |
| Actual changed set | required to equal the expected manifest before material commit |
| Manifest delta | required to be zero |
| Deletion or rename disposition | N/A with reason: no deletion or rename authorized |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private planning and critique preparation; public sync is not
authorized.

## Claim Boundary

This artifact proposes a governance redesign and evaluation sequence. It does
not change CVF authority, certify equivalence, authorize selective execution,
make the 205-file local pack canonical, permit direct import, waive semantic
inspection, open T15, or authorize runtime, provider/live, credentials,
network, public, destructive, deployment, or production actions.
