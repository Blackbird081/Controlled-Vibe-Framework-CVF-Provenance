# CVF TPGR Second Upgrade Critique Reconciliation And Revised Plan

Memory class: governed-planning-review

Status: REVISED_PLAN_PENDING_OPERATOR_APPROVAL

docType: planning_review

Date: 2026-08-17

planningBaseHead: `e063df90b0ee592c6475b3f5e826e5a7d99deecf`

## Purpose

Reconcile the independent external critique of the second Task-Proportional
Governance Routing upgrade and produce one revised plan for operator decision.
This artifact deliberately combines reconciliation and revision so the review
does not create another planning-document chain with no additional control
value.

## Target / Source

| Input | Identity | Authority disposition |
| --- | --- | --- |
| original critique plan | `docs/assessments/CVF_TASK_PROPORTIONAL_GOVERNANCE_SECOND_UPGRADE_EXTERNAL_CRITIQUE_PLAN_2026-08-17.md`; commit `b6bee448ce4ccc69b5969315d00255ca9100f1be`; SHA-256 `6cc0cde0dd98b6dbc79aa9bd01357e24fcc4657860c67e5aa1ca7ec1c7882653` | CVF-governed planning source |
| external critique return | `docs/reviews/CVF_TPGR_SECOND_UPGRADE_EXTERNAL_CRITIQUE_2026-08-17.md`; original return SHA-256 `4f3a02c2ca95028e2109f5c37f4311b755bd33dd81b2ea812917e6ff5dff588a` | advisory input; facts require CVF re-verification |
| active TPGR owner | `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md` | canonical current T0 authority |
| active route registry | `governance/compat/CVF_TASK_GOVERNANCE_ROUTE_REGISTRY.json` | canonical current route vocabulary |
| active router | `governance/compat/route_task_governance.py` | canonical current deterministic T0 behavior |
| autorun catalog | `governance/compat/agent_autorun_command_catalog.py` | current phase-command catalog |
| mixed-origin standard | `docs/reference/external_agent_review/CVF_MIXED_ORIGIN_DERIVED_SYNTHESIS_ABSORPTION_STANDARD.md` | canonical local-synthesis evidence reuse and owner-promotion boundary |

## Scope / Methodology

The reviewer read the complete critique, recomputed its SHA-256, checked the
plan Git identity and blob equality, inspected current TPGR machine sources,
recomputed checker/catalog counts, and challenged every recommended change
against CVF authority, cost, and fail-closed behavior.

This is plan-only reconciliation. No standard, schema, registry, router,
checker, hook, phase catalog, runtime, or feature implementation is changed.

## Findings / Position

Final reconciliation disposition:
`ACCEPT_REVISE_BEFORE_IMPLEMENTATION_PLANNING`.

The critique correctly found three decision-changing issues:

1. the first plan understated the cost of checker applicability metadata;
2. reviewer-assigned `decisionUncertainty` could act as a self-downgrade
   channel;
3. inherited evidence was not explicitly invalidated by changes in the
   checker closure that produced it.

The revised design accepts those findings but corrects two overclaims in the
critique:

- 114 checker files are absent from the autorun catalog, but absence from that
  catalog does not prove they are repository orphans. They are called
  `catalog-unwired` until a broader usage audit proves otherwise.
- A content hash binds a receipt to bytes. It does not prove semantic reading.
  Semantic evidence needs a concise content/use-case/value/owner record plus
  independent review.

## Independent Source Verification

| Claim from critique | CVF verification | Result |
| --- | --- | --- |
| 193 `governance/compat/check_*.py` files | filesystem count using `Get-ChildItem -LiteralPath governance/compat -File -Filter check_*.py` | VERIFIED: 193 |
| 79 unique checker filenames referenced by the autorun catalog | regex extraction of `check_[A-Za-z0-9_]+.py` from `governance/compat/agent_autorun_command_catalog.py`, unique and existence checked | VERIFIED: 79 |
| 114 remaining files are orphans | arithmetic `193 - 79 = 114` is correct, but repository searches show catalog-unwired checkers referenced by other files | MODIFIED: 114 `catalog-unwired`, orphan status not established |
| `GateCommand` contains only name and command | direct read of dataclass in `governance/compat/agent_autorun_command_catalog.py` | VERIFIED |
| selected-file full-read evidence is currently a boolean | direct read of `SOURCE_EVIDENCE_KEYS` and validation in `governance/compat/route_task_governance.py` | VERIFIED |
| current selective execution is disabled | direct read of TPGR standard/router receipt fields | VERIFIED |
| external critique verified the plan blob | plan blob `344a32faa4fe2be0fd78c7d95050b4f5b9959a86` matches at plan commit and current continuity HEAD | VERIFIED |

The external note stated a 642-line plan while PowerShell line enumeration
returns 641. Blob identity and SHA-256 match, so this representation difference
does not affect artifact verification.

## Reconciliation Matrix

| Critique item | CVF disposition | Revised decision |
| --- | --- | --- |
| Q1 source/task separation | ACCEPT_WITH_MODIFICATION | reduce routable origin values to four; require a valid I1 receipt before I2 |
| Q2 evidence invalidation | ACCEPT_WITH_MODIFICATION | add checker-closure digest and commit-reachability freshness; no wall-clock-only expiry |
| Q3 always-on core | ACCEPT | uninspectable secret/destructive material escalates; actual diff determines protected impact |
| Q4 checker graph | ACCEPT_FINDING_MODIFY_SOLUTION | use coarse groups and minimal metadata over current phase-catalog commands; do not auto-run all 114 catalog-unwired files |
| Q5 fallback triggers | ACCEPT | add escalation/divergence-rate loss of eligibility; triggers use actual diff |
| Q6 activation evidence | ACCEPT | pre-register quantitative per-class floors before replay |
| Q7 uncertainty | ACCEPT | replace confidence scale with escalation-only request; no downward effect |
| Q8 selected-cluster evidence | ACCEPT_FINDING_MODIFY_CLAIM | hashes bind bytes but do not prove reading; add semantic evidence and allow bounded reuse across unchanged stages |
| Q9 router-targeting defects | ACCEPT | add six route-system attacks plus rename and multi-owner cases |
| Q10 rollback | ACCEPT_WITH_TERMINOLOGY_FIX | two tiers; use activated governed ranges, not undefined production runs |
| Q11 ceremony cuts | ACCEPT_WITH_MODIFICATION | three decision metrics; defer project adoption; keep audit references outside routing |
| Q12 final disposition | ACCEPT | revise once, then require operator decision and bounded feasibility evidence |

## Risk / Corrective Action

### Risk 1 - selective mapping becomes a second governance system

Corrective action: route only the current canonical phase-command universe.
Use coarse groups, forward-safe defaults, and one source of command truth.
Catalog-unwired files are not automatically executed or declared irrelevant;
they are outside the initial equivalence baseline pending separate
classification.

### Risk 2 - self-downgrade through reviewer judgment

Corrective action: deterministic dimensions establish the minimum profile.
Human input may request escalation with a reason; it can never reduce the
deterministic floor, omit an actual-diff trigger, or disable independent
review.

### Risk 3 - stale evidence after owner or checker hardening

Corrective action: each reusable receipt binds selected source hashes, current
owner hashes, `issuedAtCommit`, claim classes, and a digest of the checker
closure that produced it. A relevant change refreshes only the implicated
closure unless corpus-level drift is proven.

## Revised Design 1 - Minimal Source Context

Routable fields:

| Field | Values | Routing rule |
| --- | --- | --- |
| `originClass` | `CVF_NATIVE`, `EXTERNAL_UNACCEPTED`, `ACCEPTED_DERIVED`, `UNRESOLVED` | unresolved and unaccepted external inputs cannot enter I2 |
| `intakeStage` | `NONE`, `I0_NEW_CORPUS_INTAKE`, `I1_CLUSTER_SELECTION`, `I2_CVF_NATIVE_CONVERSION`, `I3_AUTHORITY_OR_RUNTIME_PROMOTION` | I2 requires a valid I1 cluster semantic receipt |
| `evidenceState` | `NEW`, `INHERITED_FRESH`, `DELTA_REFRESHED`, `INVALIDATED`, `MISSING` | invalidated/missing fail closed; refreshed evidence is delta-scoped |
| `ownerFit` | `EXISTING_OWNER_EXACT`, `EXISTING_OWNER_COMPOSITION`, `OWNER_GAP`, `OWNER_CONFLICT`, `UNKNOWN` | conflict/unknown escalates; owner gap requires an authority decision |

Detailed lineage remains in `auditRefs`; it is not discarded, but values that
route identically do not receive separate routing enums.

`decisionUncertainty` is removed. Its replacement is optional:

```json
{"escalationRequest": {"reason": "non-empty reviewer rationale"}}
```

Presence may only raise the route. Absence leaves the deterministic route
unchanged.

## Revised Design 2 - Typed Evidence With Semantic Binding

The routing structure contains four receipt types:

| Receipt | Required binding |
| --- | --- |
| `corpusReceipt` | manifest path/hash, terminal-ledger path/hash, file count, reconciliation totals |
| `clusterSemanticReceipt` | selected paths/hashes, semantic summary per file or inseparable group, use cases, value disposition, target owner, claim boundary, reviewer identity |
| `ownerMapReceipt` | owner paths/hashes, owner-fit result, direct dependency paths |
| `checkerClosureReceipt` | selected command IDs, checker source hashes, group-order digest, issued-at commit |

`auditRefs` retains provenance graphs, prior decisions, rationale, and external
source citations. Those references remain reviewable but do not change the
route unless a deterministic contradiction trigger reads them.

Hash binding is necessary but not sufficient for semantic proof. A receipt
with hashes and no semantic summary/use-case/value/owner mapping is rejected.

Semantic understanding may be reused from I1 to I2, or across a repeated
unchanged claim, only when source hashes, owner hashes, direct dependencies,
claim classes, and checker closure remain unchanged. A new material claim,
owner conflict, or decision-changing contradiction requires targeted semantic
refresh. This prevents both shallow attestation and repeated reading with no
new decision value.

## Revised Design 3 - Deterministic Impact And Claim Floor

Keep the active eight TPGR-T0 dimensions. Add:

- `changeImpact`: `LOCAL_LEAF`, `OWNER_COMPOSITION`, `CROSS_OWNER`,
  `CONTROL_PLANE`, `RUNTIME_OR_EXTERNAL`;
- `claimClasses`: documentation, contract, schema, authority, completeness,
  absence, equivalence, state, security, runtime, live, public, destructive;
- `lifecyclePhase`: plan, dispatch, worker return, review, closure,
  continuity, public release.

The router computes actual path and effect signals from the diff. The manifest
is cross-check evidence, never the sole detector. The final profile is the
maximum of every deterministic minimum plus any escalation request.

No user-, worker-, dispatcher-, or reviewer-supplied field may lower that
floor.

## Revised Design 4 - Bounded Command Applicability Model

### Command universe

The initial equivalence baseline is the union of commands currently returned
by the canonical autorun phase catalog, including non-checker commands. It is
not all Python files whose names begin with `check_`.

The 193/79/114 measurement is maintained as discovery evidence:

- 193 checker-shaped files exist;
- 79 unique checker filenames are referenced by the catalog;
- 114 are catalog-unwired, not proven orphaned;
- catalog-unwired classification is separate work and cannot block the first
  feasibility decision.

### Minimal route metadata

Keep `GateCommand.name` and `GateCommand.command` as execution truth. Add a
minimal route metadata shape:

| Field | Purpose |
| --- | --- |
| `routeId` | stable machine identity |
| `appliesTo` | path/artifact/claim predicates |
| `phases` | applicable lifecycle phases |
| `group` | coarse dependency group |
| `receiptReuse` | explicit opt-in boolean |

The implementation decision may extend `GateCommand` with defaults or use a
generated companion projection derived from the same catalog. A handwritten
parallel command list is forbidden.

Groups:

1. `CORE`
2. `STRUCTURE`
3. `GOVERNANCE_COMPAT`
4. `ABSORPTION`
5. `CODE`
6. `STATE_SECURITY`
7. `RUNTIME_LIVE`
8. `PUBLIC_RELEASE`

Dependencies are a partial order over groups. Rare producer/consumer command
pairs may declare one unidirectional prerequisite on the consumer. There is no
bidirectional prerequisite/downstream duplication.

Any active catalog command lacking valid metadata remains always selected in
shadow output and blocks selective activation for every class that could omit
it. It does not silently disappear. A catalog-unwired file does not enter the
active command universe merely because of its filename.

## Revised Design 5 - Always-On Core

Every route runs:

1. manifest/schema and closed-shape validation;
2. actual diff versus authorized paths/claims/effects;
3. diff-derived authority/protected-path escalation;
4. command metadata and group-order freshness;
5. secret/destructive inspection across changed paths;
6. phase receipt integrity.

`UNINSPECTABLE` is an escalation result, never a clean result. During shadow
and early activation, any always-on core failure runs the complete current
phase catalog and blocks the selective decision.

## Revised Design 6 - Invalidation And Full Fallback

Evidence or selective eligibility is invalidated by:

- selected source, owner, dependency, manifest, or ledger hash drift;
- selected scope or claim-class expansion;
- unresolved provenance or owner contradiction;
- checker source or group-order change inside the receipt's closure;
- new completeness, absence, equivalence, safety, state, runtime, live,
  public, destructive, or irreversible claim;
- actual paths/effects exceeding the manifest;
- invalid route metadata or unresolved dependency closure;
- unexplained selective/full divergence;
- class escalation/divergence rate above the pre-registered limit;
- a reviewer-recorded decision-changing contradiction.

Authority/router/schema/registry/hook/generator changes and every P3/P4 class
retain full current-phase execution during initial activation.

## Revised Design 7 - Pre-Registered Proof Floors

Before replay results are visible, record these minimums in the governed TPGR
owner for each class proposed for activation:

- at least 12 distinct historical ranges;
- at least 4 defect-bearing ranges;
- at least 2 rename-heavy or multi-owner ranges in the combined set;
- 100 percent recall for all seeded defects;
- zero tolerance for misses involving authority, unauthorized paths, secrets,
  destructive or irreversible effects, receipt integrity, router
  self-modification, or fail-closed behavior;
- zero unexplained full-detects/selective-misses divergence;
- classification by a reviewer other than the route metadata author;
- median command-count reduction of at least 40 percent and median wall-time
  reduction of at least 30 percent for eligible classes;
- route computation p95 at or below one second on the local reference
  environment.

If sufficient historical ranges do not exist, the class remains full-bundle;
clean cases are not fabricated to reach the floor.

Required router-targeting seeded cases:

1. mis-mapped applicability predicate;
2. checker-closure version drift beneath a receipt;
3. manifest omission of an actual protected path;
4. attempted uncertainty/profile deflation;
5. I2 conversion without a valid I1 semantic receipt;
6. active-catalog command with missing route metadata.

## Revised Design 8 - Canary, Activation, And Rollback

### Canary

Selective output is advisory while the complete phase catalog still decides.
Each eligible class needs at least 12 canary ranges with zero unexplained
full-detects/selective-misses divergence after replay floors pass.

### First activation allowlist

- P0 read-only;
- P1 docs-only under an unchanged owner;
- P1 pure-local implementation under an unchanged owner with no authority,
  state/security, runtime/live, public, destructive, or irreversible claim.

P2, P3, and P4 remain full-bundle. P2 receives a separate operator decision
only after the initial allowlist completes its canary evidence.

### Rollback

Tier 1 global fallback:

- material false negative in an activated governed range;
- any missed fail-closed category;
- route/metadata/receipt integrity corruption;
- router self-modification outside the governance-maintenance route;
- ambiguity about rollback tier.

Tier 2 class-scoped fallback:

- divergence confined to one class;
- escalation-rate threshold breach;
- relevant checker-closure or group-order version change.

Rollback must be configuration-only, rehearsed during canary, and measurable.
Reactivation repeats replay and canary against the new inventory version.

## Revised 205-File Absorption Route

The accepted 205-file local pack remains
`ACCEPTED_DERIVED` and non-authoritative until promoted through CVF owners.

For a seven-file profile/policy cluster:

1. reuse the accepted corpus manifest and ledger;
2. recompute only the seven selected hashes;
3. create one cluster semantic receipt covering the substantive content, use
   cases, value dispositions, and target CVF owner mapping;
4. inspect the current owner and direct dependencies;
5. route the actual CVF-native conversion impact;
6. implement only through coherent CVF owners and terminology;
7. run focused proof and the applicable command closure;
8. obtain independent semantic review.

Do not repeat the full 205-file scan, re-adjudicate unrelated ledger rows, or
restart external-repository intake. Do not infer semantic reading from hashes.
Do not copy source structure directly into an arbitrary CVF path.

## Revised Delivery Sequence

| Stage | Work | Exit condition |
| --- | --- | --- |
| R0 | reconcile external critique and issue this revised plan | committed plan-only evidence |
| R1 | operator accepts, modifies, or rejects the revised plan | explicit operator decision; no implicit approval |
| R2 | read-only feasibility/cost assessment over the current phase-catalog universe | mapping cost model proves bounded value; no machine change |
| R3 | pre-register per-class replay, recall, divergence, cost, and rollback floors | thresholds fixed before results |
| R4 | shadow taxonomy and receipt contract | deterministic tests; full execution unchanged |
| R5 | shadow command metadata and group closure | every active catalog command mapped or always-selected |
| R6 | historical and seeded-defect replay | all pre-registered floors pass |
| R7 | dual-run canary and rollback rehearsal | selective advisory only; rollback proven |
| R8 | P0/P1 allowlisted activation | exact class and inventory-version authority only |
| R9 | separate P2 decision | only after bounded clean activated-range evidence |

Project-governance adoption, P3/P4 narrowing, and classification of all
catalog-unwired checker files are deferred. They are not part of this approval
request.

## Cost Model Required At R2

Compare the seven-file cluster and one medium local tranche:

- one-time metadata authoring minutes;
- recurring maintenance minutes per catalog change;
- route computation time;
- selected versus full command count;
- selected versus full wall time;
- divergence and escalation rate.

If projected maintenance plus escalation cost does not remain below measured
execution savings, stop after R2 and retain TPGR-T0 full execution.

## Decision Requested From Operator

Requested decision is limited to this revised plan:

- `APPROVE_R2_READ_ONLY_FEASIBILITY_ASSESSMENT`;
- `MODIFY_REVISED_PLAN`; or
- `REJECT_TPGR_SECOND_UPGRADE`.

Approval of R2 does not authorize R3-R9, standard/checker changes, selective
execution, T15, runtime/provider/live, public, deployment, or production.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_rescan_intelligence_hardening.py`; `governance/compat/check_corpus_completeness_report_integrity.py` |
| literalTokensReviewed | planning-review common headings; trace labels; ASCII discipline; compact non-scan and non-corpus dispositions; public disposition |
| gateRunPurpose | confirmatory evidence after source verification and reconciliation authoring; verify structure and boundaries only |
| claimBoundary | no machine design, equivalence, or activation is proven by document checks |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | advisory input -> CVF source verification -> accept/modify/reject reconciliation |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_agent_absorption_table.py` |
| Owner surface | this reconciliation/revised plan; active TPGR owner remains unchanged |
| Disposition | SELECTIVELY_ADAPTED_INTO_REVISED_PLAN |
| Claim boundary | critique itself remains non-authoritative |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON
- N/A with reason: this reconciliation performs no corpus scan, intake
  refresh, completeness update, or absence claim. It reuses existing governed
  evidence and proposes future invalidation rules.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - this planning review makes no
  new complete-corpus claim and changes no corpus manifest or ledger.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
| --- | --- | --- | --- | --- |
| checker applicability design under-costed | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | require R2 feasibility/cost gate |
| uncertainty field allowed self-downgrade | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | escalation-only human input |
| checker hardening did not invalidate receipts | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | checker-closure receipt digest |
| catalog absence called orphan status | ORCHESTRATOR_PACKET_GAP | DOCUMENTATION_ONLY_LEARNING | N/A_WITH_REASON | documentation correction only: use catalog-unwired until broader audit |
| content hash called proof of reading | ORCHESTRATOR_PACKET_GAP | DOCUMENTATION_ONLY_LEARNING | N/A_WITH_REASON | claim narrowing only: pair byte binding with semantic receipt/review |

runtimeProviderCostLearningLane: N/A_WITH_REASON - local plan reconciliation;
zero provider/live calls and zero quota usage.

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE_PLANNING.

Expected Result / Prediction: a smaller command universe, group-based
dependencies, escalation-only judgment, and checker-bound receipts should
preserve the critique's safety gains without creating another governance
system larger than the cost it removes.

Evidence Comparison: the critique's 193/79/114 arithmetic and two-field
`GateCommand` claim were reproduced. Broader repository references contradicted
the stronger orphan label. Current source also confirms the full-read field is
a boolean, while hashing alone cannot demonstrate semantic understanding.

Contradiction Or Gap Disposition: accept the measured catalog gap; narrow its
meaning; require R2 cost evidence before any implementation planning.

Claim Update: the original plan is revised, not activated. TPGR-T0 remains the
only active machine authority and still runs the full legacy bundle.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | CVF reviewer/orchestrator |
| Provider or surface | local private provenance repository |
| Session or invocation | TPGR external critique reconciliation, 2026-08-17 |
| Working directory | repository root |
| Command or tool surface | full artifact reads, SHA-256, Git identity, PowerShell counts, repository search, governed authoring, structural gates |
| Target paths | external critique normalization plus this reconciliation/revised plan; later continuity is separate |
| Allowed scope source | operator returned the critique for CVF review and decision |
| Before status evidence | continuity HEAD `e063df90b`; external critique sole untracked path |
| After status evidence | critique reconciled; revised plan pending operator approval; no implementation opened |
| Diff evidence | exact changed-path list and final gate output before commit |
| Approval boundary | advisory evidence admission and plan revision only |
| Claim boundary | no rule/checker/catalog change, selective execution, T15, runtime/provider/live, public, deploy, or production |
| Agent type | reviewer/orchestrator |
| Invocation ID | `tpgr-second-upgrade-critique-reconciliation-20260817` |
| Expected manifest | external critique plus this reconciliation/revised plan |
| Actual changed set | exact same two review paths |
| Manifest delta | zero |
| Deletion or rename disposition | N/A with reason: no deletion or rename authorized |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private critique reconciliation and revised planning; public sync is
not authorized.

## Decision / Disposition

`REVISED_PLAN_PENDING_OPERATOR_APPROVAL`

## Claim Boundary

This artifact accepts, modifies, or rejects advisory recommendations and
defines a revised plan. It does not amend active TPGR authority, prove checker
equivalence, authorize R2 or later stages, enable selective execution, open
T15, promote the 205-file corpus to authority, permit direct import, or
authorize runtime/provider/live, network, public, destructive, deployment, or
production action.
