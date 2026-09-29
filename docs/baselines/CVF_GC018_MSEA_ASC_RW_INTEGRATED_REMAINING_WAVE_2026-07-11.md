# CVF GC-018 MSEA-ASC-RW Integrated Remaining Wave

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: MSEA-ASC-RW

Dispatch base head: `107bece0e`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Authorize one continuous worker execution for ASC-T1 through ASC-T5, with
phase-local evidence/checkpoints but one final worker return and one final
independent reviewer/closer review. Intermediate reviewer closure is not
required unless a stop condition is met.

## Scope / Target / Owner Boundary

The wave may populate catalog source entries/aggregate, trace interfaces and
edges, build the indexed gap ledger, complete the human as-built front door,
and implement the scoped sibling freshness/admission mechanism selected by T0.
It may not change doctrine, R91-owned map/freshness semantics, runtime/product,
provider, public-sync, session state, or L4 readiness.

## Decision / Baseline / Proposed Tranche

ASC-T0 is accepted at `9f8815fb7`. T1-T5 are consolidated to reduce ceremony.
Truth-before-presentation order remains binding inside the wave:
`T1 -> T2 -> T3 -> T4 -> T5`.

## Evidence / Verification

Each phase must emit a terminal checkpoint ledger in the final worker return.
The worker continues past a locally blocked phase only when later work remains
truthful and non-dependent; otherwise it returns `BLOCKED_WITH_REASON`.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-ASC-RW --title "Integrated Remaining Wave" --date 2026-07-11 --base 107bece0e --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | all normative content authored/repaired manually against source-verified checker requirements after scaffold review |
| checkerReadAheadConfirmation | applicable `governance/compat/check_*.py` sources read before authoring; see Checker Source Read-Ahead Block |
| docOnlyNewFields | reserved T5 generator/checker paths recorded in work order New Doc/Implementation Fields And Paths table, not as baseline ACCEPT rows |
| claimBoundary | scaffold/text-generation provenance only; no runtime or automatic-invocation claim |

## Dependency Release Evidence

| Dependency | Artifact | Commit | Disposition |
|---|---|---|---|
| ASC-T0 contract | `docs/reviews/CVF_MSEA_ASC_T0_SOURCE_SCHEMA_AND_RECONCILIATION_CONTRACT_WORKER_RETURN_2026-07-11.md` | `9f8815fb7` | SATISFIED |
| operator batching authority | current instruction | 2026-07-11 | SATISFIED |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| wave requirements | VALUE_SET | `docs/roadmaps/CVF_AS_BUILT_ARCHITECTURE_AND_SYSTEM_CATALOG_ROADMAP_2026-07-11.md` | ASC-T1 through ASC-T5 | ASC-T1; ASC-T2; ASC-T3; ASC-T4; ASC-T5 | roadmap | ACCEPT |
| catalog schema | EXISTS | `docs/reference/system_architecture_catalog/CVF_AS_BUILT_SYSTEM_CATALOG_SCHEMA.json` | root schema | cvf.as_built_system_catalog.schema.v0 | ASC-T0 contract | ACCEPT |
| topology choice | VALUE_SET | `docs/reference/system_architecture_catalog/CVF_AS_BUILT_SYSTEM_CATALOG_TOPOLOGY_DECISIONS.md` | Decisions 1-3 | scoped sibling freshness family | ASC-T0 decision | ACCEPT |
| R91 ownership boundary | VALUE_SET | `governance/compat/check_system_chain_map_freshness.py` | module constants | MAP_PATH; EXPECTED_LANE_COUNT; CANONICAL_LANE_IDS | R91 checker | ACCEPT |
| local pre-commit catalog | EXISTS | `governance/compat/local_governance_hook_catalog_pre_commit.py` | `build_pre_commit_commands` command list | system chain map freshness command entry | local pre-commit hook catalog | ACCEPT |
| local reviewer-fast catalog | EXISTS | `governance/compat/local_governance_hook_catalog_reviewer_fast.py` | `build_reviewer_fast_commands` command list | system chain map freshness command entry | reviewer-fast hook catalog | ACCEPT |
| local pre-push catalog | EXISTS | `governance/compat/local_governance_hook_catalog_pre_push.py` | pre-push command list | system chain map freshness command entry | local pre-push hook catalog | ACCEPT |
| autorun catalog | EXISTS | `governance/compat/agent_autorun_command_catalog.py` | pre-dispatch/pre-implementation command catalog | system chain map freshness command entry | agent autorun command catalog | ACCEPT |
| documentation CI owner | EXISTS | `.github/workflows/documentation-testing.yml` | system-chain-map-freshness job | Enforce system chain map freshness guard | documentation workflow | ACCEPT |

## New Doc/Implementation Fields And Paths

The following two paths are new authorized T5 output paths, not existing
source. They are excluded from Source Verification `ACCEPT` rows because the
files do not exist yet, and are instead recorded here as `NEW_AUTHORIZED_OUTPUT`.

| Path | Disposition | Authorizing contract |
|---|---|---|
| `governance/compat/generate_as_built_system_catalog.py` | NEW_AUTHORIZED_OUTPUT | ASC-T0 topology decision; this baseline's Core Guard Self-Protection Authorization |
| `governance/compat/check_as_built_system_catalog_drift.py` | NEW_AUTHORIZED_OUTPUT | ASC-T0 topology decision; this baseline's Core Guard Self-Protection Authorization |
| `.github/workflows/as-built-system-catalog-freshness.yml` | NEW_AUTHORIZED_OUTPUT | ASC-T0 Decision 2 distinct weekly wiring without modifying the R91-owned weekly workflow |

## Current Runtime Freshness Verification

N/A with reason: architecture catalog/governance metadata wave; no runtime claim.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`documentation`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_source.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_foundation_storage_layout.py`; `governance/compat/check_system_chain_map_freshness.py` |
| literalTokensReviewed | DISPATCH_READY; WORKER_MUST_NOT_COMMIT; integrated phase ledger; protected paths; NEW_AUTHORIZED_OUTPUT; Scaffold Provenance Block fields |
| gateRunPurpose | confirmation and evidence after source-backed authoring; not first discovery |
| claimBoundary | integrated-wave authorization only |

## Intake Role Routing Decision

| Field | Value |
|---|---|
| Intake summary | Execute ASC-T1 through ASC-T5 once, then return for one final review. |
| Scope classification | BOUNDED_INTEGRATED_GOVERNED_WAVE |
| Risk sensitivity | R2 because T5 may add protected governance automation |
| Selected role route | routeMode=`SINGLE_AGENT_SINGLE_ROLE`; one worker executes all phases, then independent reviewer/closer converts. |
| Role separation basis | worker must not commit; reviewer/closer performs final semantic review and closure |
| Escalation condition | authority conflict, schema-breaking evidence, R91 semantic change, or forbidden expansion |

## Dual Agent Surface Matrix

| Agent surface | Role | Interface | Authority and risk boundary | Required evidence | Adapter boundary and disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | reviewer/closer | source, gates, closure | final classification/commit authority | independent recomputation | ALLOWED |
| EXTERNAL_AGENT_CLI_MCP | integrated worker | local repository tools | no commit; exact allowed families | phase ledger and final return | ALLOWED_BOUNDED_NO_COMMIT |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance architecture-catalog wave.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: T5 protected automation creation only,
scoped to the two reserved paths and their focused tests.

Protected paths potentially authorized in T5 only:

- `governance/compat/generate_as_built_system_catalog.py`
- `governance/compat/check_as_built_system_catalog_drift.py`
- focused test files for those two paths;
- `governance/compat/local_governance_hook_catalog_pre_commit.py`;
- `governance/compat/local_governance_hook_catalog_reviewer_fast.py`;
- `governance/compat/local_governance_hook_catalog_pre_push.py`;
- `governance/compat/agent_autorun_command_catalog.py`;
- `.github/workflows/documentation-testing.yml`;
- `.github/workflows/as-built-system-catalog-freshness.yml` (new T5 output).

Operator authorization: integrated ASC remaining wave. Rollback boundary:
revert only ASC-RW material paths; never alter R91 semantics.

## Claim Boundary

This baseline authorizes one no-commit integrated wave, not automatic closure
or permission to improvise outside T1-T5.
