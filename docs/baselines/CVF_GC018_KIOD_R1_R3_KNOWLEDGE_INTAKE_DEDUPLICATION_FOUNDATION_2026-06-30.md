# CVF GC-018 Baseline: KIOD-R1-R3 Knowledge Intake Deduplication Foundation

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-30

docType: baseline

Batch ID: KIOD-R1-R3

dispatchBaseHead: f3200159

## Decision / Baseline / Proposed Tranche

| Field | Disposition |
|---|---|
| Decision | create the R1 owner-surface taxonomy, R2 pre-scan packet standard, and R3 routing matrix before the next source repo/folder pilot |
| Baseline | KIOD-T0 roadmap is ready for R1; KIOD-T1 overlap checker is already closed and wired |
| Proposed tranche | source-verified reference foundation for deduplicated future knowledge intake |
| Execution route | Codex single-agent multi-role governed documentation batch |
| Closure posture | CLOSED_PASS_BOUNDED after R1-R3 references, roadmap update, focused guards, and autorun gates |

## Purpose

KIOD-R1-R3 turns the KIOD-T0 roadmap into a reusable front-loaded discipline:
future agents must classify source value against known CVF owner surfaces,
complete a pre-scan packet, and route overlap or novelty before proposing a new
lane.

## Scope / Methodology

Allowed scope:

- create the R1 owner-surface taxonomy reference;
- create the R2 pre-scan packet standard;
- create the R3 overlap routing matrix standard;
- update the KIOD-T0 roadmap to record R1-R3 as bounded pass and make R4 the
  next decision point;
- file this baseline, the paired work order, and a completion review;
- run focused guards and autorun gates for documentation/reference changes.

Forbidden scope:

- absorbing any selected upstream source;
- changing runtime source, generated Web data, package registries, skill roots,
  provider routes, MCP/CLI adapters, or public-sync files;
- implementing a new checker beyond the already-closed KIOD-T1 overlap guard;
- claiming live governance behavior, production readiness, semantic completeness,
  automatic invocation, or dashboard/console functionality.

## Findings / Position

R1-R3 should be a reference foundation, not another source intake closeout. The
valuable control is to make the overlap decision visible before a future agent
reads a large repo and accidentally duplicates an existing CVF surface or marks
valuable deltas as no-new-value too early.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`knowledge-intake-deduplication`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

Disclosure command:

```text
python governance/compat/run_adif_defect_resolver.py --task-class knowledge-intake-deduplication --role dispatcher --lifecycle-phase dispatch --json
```

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| KIOD-T0 authorizes R1 owner-surface taxonomy | `docs/roadmaps/CVF_KIOD_T0_KNOWLEDGE_INTAKE_OVERLAP_DEDUPLICATION_ROADMAP_2026-06-30.md` | Work Plan | `KIOD-R1` | KIOD-T0 roadmap | LITERAL_INVARIANT | ACCEPT |
| KIOD-T0 authorizes R2 pre-scan packet definition | `docs/roadmaps/CVF_KIOD_T0_KNOWLEDGE_INTAKE_OVERLAP_DEDUPLICATION_ROADMAP_2026-06-30.md` | Work Plan | `KIOD-R2` | KIOD-T0 roadmap | LITERAL_INVARIANT | ACCEPT |
| KIOD-T0 authorizes R3 overlap routing matrix | `docs/roadmaps/CVF_KIOD_T0_KNOWLEDGE_INTAKE_OVERLAP_DEDUPLICATION_ROADMAP_2026-06-30.md` | Work Plan | `KIOD-R3` | KIOD-T0 roadmap | LITERAL_INVARIANT | ACCEPT |
| Future intake artifacts must use the KIOD-T1 overlap dispositions | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | Overlap And Novelty Classification Rule | `CONFIRMED_EXISTING`; `ENRICH_EXISTING`; `NEW_FINDING`; `REJECT_DIRECT_IMPORT`; `NO_NEW_VALUE`; `OWNER_SURFACE_NOT_FOUND` | external-agent-review standard | LITERAL_INVARIANT | ACCEPT |
| The overlap discipline checker requires the R1-R3 table columns and allowed dispositions | `governance/compat/check_external_absorption_overlap_discipline.py` | constants | `REQUIRED_COLUMNS`; `ALLOWED_DISPOSITIONS` | overlap discipline checker | RUNTIME_BEHAVIOR | ACCEPT |
| External knowledge intake routing requires a field/value routing block | `governance/compat/check_external_knowledge_intake_routing.py` | constants | `REQUIRED_FIELDS`; `ALLOWED_INPUT_TYPES` | external knowledge intake routing checker | RUNTIME_BEHAVIOR | ACCEPT |
| Package-skill mentions must remain within package productionization SOP boundaries | `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md` | claim boundary rows | `Claim boundary` | package skill productionization SOP | LITERAL_INVARIANT | ACCEPT |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | KIOD-T0 roadmap, external knowledge intake routing checker, KIOD-T1 overlap checker, package productionization SOP |
| Runtime behavior claimed | N/A_WITH_REASON: this batch creates reference documentation only |
| Live/provider proof claimed | N/A_WITH_REASON: no provider/API/model behavior or live governance behavior is claimed |
| Public-sync claimed | N/A_WITH_REASON: no public-sync is authorized |
| Freshness disposition | PASS - current sources support R1-R3 documentation foundation |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| KIOD-R1 owner-surface taxonomy | Execution Plan | `docs/reference/external_agent_review/CVF_KIOD_R1_OWNER_SURFACE_TAXONOMY.md` | markdown and intake routing guards | PASS |
| KIOD-R2 pre-scan packet | Execution Plan | `docs/reference/external_agent_review/CVF_KIOD_R2_PRE_SCAN_PACKET_STANDARD.md` | markdown and intake routing guards | PASS |
| KIOD-R3 routing matrix | Execution Plan | `docs/reference/external_agent_review/CVF_KIOD_R3_OVERLAP_ROUTING_MATRIX_STANDARD.md` | markdown and intake routing guards | PASS |
| Keep runtime/package/public boundaries parked | Claim Boundary | forbidden scope and control blocks | autorun pre-closure | PASS |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator decision -> KIOD-T0 roadmap -> KIOD-R1 taxonomy -> KIOD-R2 pre-scan packet -> KIOD-R3 routing matrix -> KIOD-R4 negative-search decision |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_overlap_discipline.py` |
| Owner surface | `docs/roadmaps/CVF_KIOD_T0_KNOWLEDGE_INTAKE_OVERLAP_DEDUPLICATION_ROADMAP_2026-06-30.md` |
| Disposition | ADAPT operator-approved deduplication discipline into three reusable reference surfaces |
| Claim boundary | documentation foundation only; no selected source intake, runtime, package, provider, public, dashboard, adapter, or production-readiness claim |

## Package Skill Productionization Control Block

SOP source: `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md`

Current phase: NOT_APPLICABLE_WITH_REASON - this batch mentions package-skill
owner surfaces only as intake-routing targets and does not mutate package
roots, generated indexes, runtime eligibility, truth packets, or usage receipts.

Target lifecycle state: NOT_APPLICABLE_WITH_REASON - no package skill lifecycle
state is changed.

Prior phase evidence: SCPL and package productionization closures remain the
current package-skill evidence surfaces; KIOD-R1-R3 only prevents duplicate
future intake lanes.

Next forbidden skip: future package candidate intake must still follow the ASSF
package productionization SOP and cannot use this taxonomy as activation proof.

Runtime/provider proof: N/A with reason: no runtime, package, provider, model,
or live governance behavior is claimed.

Claim boundary: package-skill references are owner-surface labels only; no
package conversion, lifecycle mutation, activation, adapter behavior, or
production-readiness claim is made.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | KIOD-R1-R3 documentation foundation |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | ACTION_EVIDENCE_PRESENT - three reference files, baseline, work order, completion review, and roadmap update |
| invocationBoundary | local governed Markdown authoring only |
| interceptionBoundary | no IDE, shell hook, git hook, provider, MCP, Web, public-sync, or runtime interception claim |
| claimLanguage | defines classification and routing references for future intake |
| forbiddenExpansion | no selected source intake, checker implementation, runtime change, package activation, provider/live proof, public-sync, dashboard, adapter, or production-readiness claim |

## Verification / Evidence

| Evidence item | Required result |
|---|---|
| Pre-implementation autorun | PASS on `f3200159..HEAD` before edits |
| ADIF disclosure query | PASS with `NONE_RETURNED` |
| Focused intake routing guard | PASS for changed R1-R3 artifacts |
| Focused overlap discipline guard | PASS for changed R1-R3 artifacts where applicable |
| Pre-closure autorun | PASS on material range before commit |
| Commit steward preflight | PASS before material commit |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_KIOD_R1_R3_KNOWLEDGE_INTAKE_DEDUPLICATION_FOUNDATION_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_KIOD_R1_R3_KNOWLEDGE_INTAKE_DEDUPLICATION_FOUNDATION_COMPLETION_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_KIOD_T0_KNOWLEDGE_INTAKE_OVERLAP_DEDUPLICATION_ROADMAP_2026-06-30.md` | R1-R3 `PASS_BOUNDED`; R4 next | PASS |
| Registry JSON | N/A with reason: no generated registry JSON changed | N/A with reason | PASS |
| Registry Markdown | R1-R3 reference files | `Status: ACTIVE_REFERENCE` | PASS |
| External evidence digest | N/A with reason: no selected source evidence digest created | N/A with reason | N/A with reason |
| System loop interlock | R1-R3 routing references | future intake must route through R1-R3 before pilot | PASS |
| Session continuity | session-sync may follow material closure | N/A with reason | PASS |
| Focused tests | focused guards and autorun gates | PASS |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |
| Live proof | this file | N/A with reason: no live governance behavior claim | PASS |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| R1 taxonomy | present | `docs/reference/external_agent_review/CVF_KIOD_R1_OWNER_SURFACE_TAXONOMY.md` | PASS |
| R2 pre-scan packet standard | present | `docs/reference/external_agent_review/CVF_KIOD_R2_PRE_SCAN_PACKET_STANDARD.md` | PASS |
| R3 routing matrix | present | `docs/reference/external_agent_review/CVF_KIOD_R3_OVERLAP_ROUTING_MATRIX_STANDARD.md` | PASS |
| Provider/live claim | none | NOT_RUN_WITH_REASON | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance foundation. Public-safe publication would
require separate public-sync authorization.

## Claim Boundary

KIOD-R1-R3 creates documentation and routing references only. It does not absorb
or certify a selected source, does not make outside material canonical, does not
change runtime or package state, does not run providers, does not publish public
artifacts, and does not prove semantic completeness for future intake.
