# CVF GC-018 GC010 SCR-R2-T1D Pending Agent Execution Non-Production Consumer And Package Export Boundary Decision

Memory class: governed-baseline

docType: baseline

Status: DISPATCHED_DECISION_ONLY

Batch ID: GC010-SCR-R2-T1D

Date: 2026-08-31

dispatchBaseHead: `6c2ef5cc6`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Authorize one documentation-only decision that identifies the smallest real
non-production consumer of the accepted durable single-node pending-execution
core and the exact package-export/composition boundary required by that
consumer. This tranche implements nothing and treats a bare export with no
caller as insufficient system-chain progress.

## Authority Chain

- Operator instructed continuation of the same GC010 system chain with full
  orchestrator/reviewer authority.
- Accepted T1C material commit: `82c64a6f5`.
- T1C completion:
  `docs/reviews/CVF_GC010_SCR_R2_T1C_PENDING_AGENT_EXECUTION_DURABLE_SINGLE_NODE_NON_PRODUCTION_IMPLEMENTATION_COMPLETION_2026-08-31.md`.
- Accepted T1C source owners:
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution.ts`,
  `pending-agent-execution-sqlite-store.ts`, and
  `pending-agent-execution-composition.ts`.
- Paired work order:
  `docs/work_orders/CVF_AGENT_WORK_ORDER_GC010_SCR_R2_T1D_PENDING_AGENT_EXECUTION_NON_PRODUCTION_CONSUMER_PACKAGE_EXPORT_BOUNDARY_DECISION_2026-08-31.md`.

Historical GC010-SCR-R1 T1-T5 production work remains parked and is not
authority for this non-production decision.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| Durable single-node core | T1C completion and material `82c64a6f5` | decision may inspect accepted interfaces and composition only | ACCEPT |
| Package owner | `cvf-web/package.json` is private and has scripts but no exports map | worker must identify the actual import/export convention | ACCEPT_FOR_ANALYSIS |
| Current caller | fresh dispatcher search found composition construction only in its focused test | worker must re-verify; no caller may be invented | UNRESOLVED |
| Production consumer | historical production route remains parked | no route/provider/audit wiring in T1D | ACCEPT_PARKED |

## Scope / Target / Owner Boundary

Worker creates exactly one assessment and one worker return. The assessment
must compare five candidate families, identify an exact consumer owner and
export/composition seam or retain the core orphaned, freeze the smallest later
manifest, and select one terminal token.

Runtime, source, test, route, package, dependency, lockfile, configuration,
checker, workflow, continuity, provider/live, public-sync, deployment,
distributed, audit, and production mutation are forbidden.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| T1C owns bounded construction | runtime | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution-composition.ts` | exported builder | `buildPendingAgentExecutionRuntime` | pending-execution composition | ACCEPT |
| T1C requires explicit absolute DB path | runtime | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution-sqlite-store.ts` | constructor validation | `PendingAgentExecutionSqliteStore` | pending-execution store | ACCEPT |
| Construction is currently test-only | source/test | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution-sqlite-store.test.ts` | focused composition tests | builder import and calls | cvf-web test owner | ACCEPT_AT_DISPATCH_BASE |
| Package is private and exposes no package export map | dependency | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | root fields/scripts | `private`; no `exports` | cvf-web package | ACCEPT |
| Existing representative domain barrel is domain-local, not a root package API | structure | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflow-composition/index.ts` | current exports | workflow-composition barrel | cvf-web source | ACCEPT |
| Historical pilot constructs another runtime and needs provider credentials | script | `scripts/run-brigade-residual-absorption-runtime-pilot.ts` | imports/construction | `AgentExecutionRuntime` | manually runnable script | ACCEPT_NON_MATCH |

## Candidate Families Required

Compare exactly these families:

1. Package-native export only, with no new caller.
2. A new cvf-web non-production library consumer/harness.
3. An existing manually runnable script or pilot.
4. An existing execution-plane or MAO owner.
5. No safe current consumer; retain the accepted core orphaned and parked.

Every family must receive exactly one classification:
`EXISTING_SOURCE_COMPATIBLE`, `EXISTING_SOURCE_INCOMPATIBLE`,
`PROPOSED_NEW_OWNER_COMPATIBLE`, `NO_CURRENT_OWNER`, or
`PROPOSED_EXPORT_ONLY_NOT_A_CONSUMER`.

## Required Decision Contract

The assessment must answer all twelve questions in order:

1. Does any non-test caller currently construct or consume the T1C runtime?
2. What exact repo-relative file and symbol would own the smallest genuine
   non-production consumer?
3. Is the consumer existing source or proposed new source, and which candidate
   classification proves that distinction?
4. What exact import/export convention does cvf-web use for this boundary;
   does it need a new domain barrel, a direct internal import, or no export?
5. Who supplies and validates the explicit absolute SQLite database path,
   without environment, home-directory, or repository-root defaulting?
6. Who owns `create`, claim, begin, complete/fail, recovery, and close lifecycle
   calls, and how are actor/request identities supplied?
7. Can the consumer remain hermetic and zero-provider, zero-network,
   zero-route, zero-audit, and zero-production-effect?
8. What focused test proves real construction and one bounded lifecycle while
   preserving durable restart behavior and cleanup?
9. What dependency, package, server-only, bundling, and import-cycle effects
   would the proposed boundary introduce?
10. Why are the four non-selected candidate families incompatible or not
    genuine consumers?
11. What exact smallest later T1E file manifest is justified, or which source
    fact requires the core to remain orphaned?
12. What separate evidence is required before route, provider admission,
    durable audit, production consumer, cross-node/distributed, public-sync,
    deployment, or production work can open?

The decision must not count a barrel/export declaration, a test, a doc, or an
unregistered credential-dependent script as a production caller. T1D may
select only a non-production boundary.

## Allowed Terminal Tokens

Select exactly one:

- `NON_PRODUCTION_CONSUMER_EXPORT_BOUNDARY_READY_FOR_T1E_CONSIDERATION`
- `PARTIAL_READY_REQUIRES_INTERFACE_OR_OWNER_CHANGE`
- `NO_SAFE_NON_PRODUCTION_CONSUMER_RETAIN_ORPHANED`
- `BLOCKED_SOURCE_CONTRADICTION`

## Acceptance Criteria

- Exactly five candidate families are compared and classified.
- Current non-test caller and export searches are freshly reproduced.
- A selected consumer is an executable local owner, not merely an export or
  documentation proposal.
- DB-path, lifecycle, server-only, dependency and cleanup ownership is exact.
- Smallest future manifest contains exact repo-relative paths and symbols.
- Exactly one terminal token is selected; no automatic successor opens.
- Worker returns exactly two uncommitted files with zero provider/external calls.

## Decision / Baseline / Proposed Tranche

T1D is a documentation-only consumer/export boundary gate after accepted T1C.
A ready result may name a future T1E implementation manifest, but neither this
baseline nor the worker return authorizes implementation.

## Evidence / Verification

Required evidence: fresh execution base/status; exhaustive symbol, import,
barrel, package-script and workflow searches; five-family matrix; twelve
ordered answers; exactly one selected terminal; exact two-file changed set;
full worker-return gate; zero external/provider calls; no commit.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id GC010-SCR-R2-T1D --title "Pending Agent Execution Non-Production Consumer And Package Export Boundary Decision" --date 2026-08-31 --base 6c2ef5cc6 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "accepted T1C durable single-node non-production core material 82c64a6f5; decision-only consumer and package-export boundary" --dispatch-kind INITIAL --dispatch-surface EXTERNAL_AGENT_CLI_MCP --review-round-count 0 --cumulative-external-invocation-count 0 --external-invocation-ceiling 2 --include-worker-return-skeleton --stdout` |
| generatedProfile | generic worker dispatch plus no-commit decision profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact candidates, twelve questions, two-path scope, terminal tokens and claim boundaries |
| checkerReadAheadConfirmation | dispatch, lifecycle, read-ahead, review-cost, worker-return, trace, delta, public, handoff and external-intake checkers read |
| docOnlyNewFields | consumerCompatibilityClass; exportBoundaryDisposition; futureT1eManifest |
| claimBoundary | authoring provenance only; no consumer or export exists from this packet |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | normal decision-only controls remain binding |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_external_knowledge_intake_routing.py` |
| literalTokensReviewed | dispatch fields, exact scope, trace/delta labels, external-intake literals, public disposition and worker-return profile |
| gateRunPurpose | conformance evidence before dispatch, not runtime proof |
| claimBoundary | artifact conformance only; worker/reviewer own semantic correctness |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private decision-only system-chain dispatch; no public export is authorized.

## Claim Boundary

This baseline authorizes exactly one documentation-only consumer/export
decision. It does not create or export source, construct a runtime, create a
database, call a lifecycle operation, wire a route, admit/invoke a provider,
emit audit, synchronize public artifacts, deploy, prove distributed safety,
open a production consumer, or claim production readiness.
