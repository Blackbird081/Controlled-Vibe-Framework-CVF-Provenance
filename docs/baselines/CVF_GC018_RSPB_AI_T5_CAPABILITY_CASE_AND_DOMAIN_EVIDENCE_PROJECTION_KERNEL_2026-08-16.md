# CVF GC-018 Baseline - RSPB-AI-T5 Capability Case And Domain Evidence Projection Kernel

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: RSPB-AI-T5

Dispatch base head: `a36710734e9949d363c0ed3e8dec93cb46d29611`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator

Reviewer owner: independent reviewer, then reviewer/closer

Worker target: delegated worker role

Mixed-origin derived synthesis: REQUIRED

## Purpose

Authorize one bounded local-first implementation tranche that converts the
accepted snapshot, route/readiness, and controlled-acquisition contract outputs
into a deterministic projection-only case/evidence read model. The tranche
improves agent and user inspectability without creating a new authority owner,
writing case files, or activating an adapter or executor.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id RSPB-AI-T5 --title "Capability Case And Domain Evidence Projection Kernel" --date 2026-08-16 --base a36710734 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced all placeholders; added exact local source hashes, owner mapping, four-path worker manifest, value/cost boundary, and hermetic acceptance criteria |
| checkerReadAheadConfirmation | dispatch, source-verification, mixed-origin, overlap, value-conversion, dual-agent, trace, delta-boundary, and worker-return checker sources read |
| docOnlyNewFields | projection authority notice, projection source bindings, staleness state, evidence verification state, deterministic projection digest |
| claimBoundary | Dispatch-authoring provenance only; no runtime, provider, live, public, Web, CLI/MCP, filesystem-write, or executor claim. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_mixed_origin_derived_synthesis_absorption.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_knowledge_intake_routing.py` |
| literalTokensReviewed | Purpose; Source Verification Block; Mixed-Origin Derived Synthesis Provenance; Absorption Decision Vector; System-Chain Value Review; Dual Agent Surface Matrix; Public Export Disposition; Claim Boundary; ACCEPT; DEFERRED_WITH_REASON; CONTRACT_ONLY |
| gateRunPurpose | confirmation and dispatch evidence after source inspection |
| claimBoundary | Structural read-ahead does not prove implementation correctness or runtime availability. |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`external-absorption-implementation`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class external-absorption-implementation --role dispatcher --lifecycle-phase pre-dispatch --surface-selector EXTENSIONS/CVF_GUARD_CONTRACT --risk-ceiling MEDIUM --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | no additional defect-specific constraint; repository-wide local-first and independent-review rules remain binding |

## Authorization / Source

- Operator instruction: `next`, 2026-08-16, continuing selective absorption.
- Active continuity: `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`.
- Corrective decision: `docs/assessments/CVF_RSPB_AI_T0_MIXED_ORIGIN_CORRECTIVE_REASSESSMENT_2026-08-16.md`.
- T3 owner: `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/controlled-acquisition.contract.ts`.
- T4-R1 owner: `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-route-readiness.contract.ts`.
- Accepted local corpus ledger: `docs/audits/CVF_RSPB_AI_T0_CAPABILITY_PREFLIGHT_BOOTSTRAP_PROPOSAL_FILE_LEDGER_2026-08-15.json`.
- Local candidate files are design evidence only and do not become CVF authority.

## Decision / Baseline

Decision: `PROCEED_BOUNDED_HIGH_VALUE`.

The case/evidence projection is the lowest-cost missing seam after T3 and T4:
it exposes canonical decisions as deterministic, traceable, secret-safe data
for later internal or external consumers. It does not justify filesystem
materialization, CLI/MCP, Web, or acquisition execution.

## Scope / Owner Boundary

Owner: `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/`.

Risk ceiling: `R1`. Pure TypeScript transformation and validation only. The
kernel may consume contract-shaped values but must not invoke an executor,
provider, network, credential, subprocess, filesystem, clock, or random source.

## Allowed Paths

- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-case-evidence-projection.contract.ts` (NEW)
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-case-evidence-projection.contract.test.ts` (NEW)
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/index.ts`
- `docs/reviews/CVF_RSPB_AI_T5_CAPABILITY_CASE_AND_DOMAIN_EVIDENCE_PROJECTION_KERNEL_WORKER_RETURN_2026-08-16.md` (NEW)

## Forbidden Actions

- No direct copy or execution of local candidate source.
- No file writing, case-directory creation, adapter, router, executor, CLI,
  MCP, HTTP, provider, credential, network, subprocess, or live invocation.
- No edit to T1-T4 contract behavior, runtime providers, registries, hooks,
  session state, handoff, catalog, public-sync clone, deployment, or production.
- Worker must not stage or commit.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| route decision owner exists | EXISTS | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-route-readiness.contract.ts` | interface definition | `CapabilityRouteDecision` | Guard Contract | ACCEPT |
| readiness decision owner exists | EXISTS | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-route-readiness.contract.ts` | interface definition | `CapabilityReadinessDecision` | Guard Contract | ACCEPT |
| acquisition plan and receipt owners exist | EXISTS | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/controlled-acquisition.contract.ts` | interface definitions | `ControlledAcquisitionPlan`; `ControlledAcquisitionReceipt` | Guard Contract | ACCEPT |
| barrel export owner exists | EXISTS | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/index.ts` | capability exports | `evaluateCapabilityReadiness`; `reconcileControlledAcquisitionReceipt` | Guard Contract barrel | ACCEPT |
| local case projection is non-authoritative input | RUNTIME_BEHAVIOR | `.private_reference/legacy/CVF 13.08/CVF_CAPABILITY_PREFLIGHT_BOOTSTRAP/EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/capability_preflight/case.projection.ts` | `AUTHORITY_NOTICE`; `projectCapabilityCase` | `projectCapabilityCase` | mixed-origin candidate | REJECT |
| local domain projection is non-authoritative input | RUNTIME_BEHAVIOR | `.private_reference/legacy/CVF 13.08/CVF_CAPABILITY_PREFLIGHT_BOOTSTRAP/EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/capability_preflight/domain.evidence.projection.ts` | `projectDomainEvidence` | `projectDomainEvidence` | mixed-origin candidate | REJECT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| planned contract path | `rg -n "capability-case-evidence-projection|CapabilityCaseEvidenceProjection" EXTENSIONS/CVF_GUARD_CONTRACT/src`; zero current owner matches before authoring | NEW_PATH_CONFIRMED |
| projection language collisions | current repo contains general evidence and learning references but no same-symbol owner | NO_OWNER_COLLISION |
| owner decision | enrich Guard Contract beside T3/T4; do not create Execution Plane duplicate | ENRICH_EXISTING |

## Mixed-Origin Derived Synthesis Provenance

artifactClass: PROVENANCE_BACKED_DERIVED_SYNTHESIS_CANDIDATE

authorityStatus: NON_AUTHORITATIVE_UNTIL_REVIEWED

| Input or concept | Origin class | Evidence basis | Claim type | Validation method | Current CVF owner | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| case projection set and authority notice | OPERATOR_AGENT_CO_DESIGNED | local contract/schema/source/tests | derived design | content inspection plus CVF-native tests | Guard Contract | ADAPT |
| Evidence -> Finding -> Path projection | MIXED_ORIGIN | local domain contract/schema/source/tests | derived design | adversarial reference-binding tests | Guard Contract | ADAPT |
| source binding and no-authority rule | CVF_PUBLIC_DERIVED | local profile plus current CVF authority hierarchy | governance invariant | current owner reconciliation | Guard Contract | ENRICH_EXISTING |
| filesystem export and adapters | OPERATOR_AGENT_CO_DESIGNED | local candidate | runtime proposal | value/risk split | no owner opened | DEFER |

## Absorption Decision Vector

| Decision axis | Decision | Evidence | Cost boundary |
| --- | --- | --- | --- |
| Knowledge absorption | PROCEED_BOUNDED | nine-file selected local cluster | one capability cluster |
| Direct import | REJECT_DIRECT_IMPORT | candidate implementation is weaker and non-authoritative | CVF-native rewrite only |
| Runtime activation | NOT_AUTHORIZED | pure returned-data kernel only | no I/O or adapter |
| Authority promotion | GUARD_CONTRACT_ONLY | existing T3/T4 owner composition | no new authority surface |

## System-Chain Value Review

| Chain component | Evidence path | Existing CVF owner/gap | Value disposition | Readiness disposition | Next action |
| --- | --- | --- | --- | --- | --- |
| snapshot/route/readiness inputs | current T2/T4 contracts | accepted owners, no combined read model | HIGH_VALUE | READY_TO_CONSUME | bind as sources |
| acquisition decision/receipt inputs | current T3 contract | accepted owner, separately governed executor | HIGH_VALUE | CONTRACT_ONLY | project without executing |
| case/evidence read model | selected local cluster | missing bounded owner seam | HIGH_VALUE | IMPLEMENT_NOW | add pure kernel |
| filesystem/CLI/MCP/Web consumers | local adapter/projection candidates | demand and authorization absent | DEFER | PARKED | separate tranche only |

## Absorption Efficiency And Provenance Reuse

manifestLedgerReuse: REUSE_IF_FRESH

semanticReviewUnit: CAPABILITY_CLUSTER

defaultValuePosture: PRESERVE_UNTIL_CONTRADICTED

additionalValueProbe: SKIP_UNLESS_NAMED_GAP

latencyBudget: SINGLE_PASS_BOUNDED

intakePriority: LOCAL_SYNTHESIZED_PACK_FIRST

localSemanticInspection: FILE_AND_USE_CASE_CONTENT_REQUIRED

mappingAction: DIRECT_WORK_ORDER_FOR_HIGH_FIT_CLUSTERS

deliverySequence: WORK_ORDER_THEN_WORKER_THEN_INDEPENDENT_REVIEWER

namePatternInference: FORBIDDEN_AS_VALUE_DISPOSITION

upstreamConsultation: TARGETED_FOR_PROVENANCE_OR_GAP

| Control | Disposition |
| --- | --- |
| manifestLedgerReuse | REUSE_IF_FRESH |
| semanticReviewUnit | CAPABILITY_CLUSTER |
| defaultValuePosture | PRESERVE_UNTIL_CONTRADICTED |
| additionalValueProbe | SKIP_UNLESS_NAMED_GAP |
| latencyBudget | SINGLE_PASS_BOUNDED |
| intakePriority | LOCAL_SYNTHESIZED_PACK_FIRST |
| localSemanticInspection | FILE_AND_USE_CASE_CONTENT_REQUIRED |
| mappingAction | DIRECT_WORK_ORDER_FOR_HIGH_FIT_CLUSTERS |
| deliverySequence | WORK_ORDER_THEN_WORKER_THEN_INDEPENDENT_REVIEWER |
| namePatternInference | FORBIDDEN_AS_VALUE_DISPOSITION |
| upstreamConsultation | TARGETED_FOR_PROVENANCE_OR_GAP |

## External Absorption Core

| Field | Value |
| --- | --- |
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | accepted local Capability Preflight Bootstrap folder |
| Enumeration command | predecessor `rg --files --hidden --no-ignore`; current named nine-file selection |
| Manifest artifact or inline manifest | `docs/audits/CVF_RSPB_AI_T0_CAPABILITY_PREFLIGHT_BOOTSTRAP_PROPOSAL_MANIFEST_2026-08-15.json` |
| Processing ledger artifact or inline ledger | `docs/audits/CVF_RSPB_AI_T0_CAPABILITY_PREFLIGHT_BOOTSTRAP_PROPOSAL_FILE_LEDGER_2026-08-15.json` |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/` plus System-Chain Value Review above |
| Unresolved items | 0 processing rows; implementation remains pending worker/reviewer |
| Completion claim boundary | selected-cluster dispatch only; no full-corpus refresh or runtime activation |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
| --- | --- | --- | --- | --- | --- |
| projection contracts and schemas | projection-only authority and trace model | PACKAGE_CANDIDATE | Guard Contract | implement pure contract | no I/O/runtime activation |
| candidate source and tests | use cases and adversarial cases | RUNTIME_CANDIDATE | Guard Contract tests | rewrite, do not copy | hermetic function only |
| secret-redaction policy | safe evidence shaping | CHECKER_CANDIDATE | projection validation | add focused negative cases | no hook wiring |
| candidate direct file export | useful intent, unsafe owner fit | REJECT_DIRECT_IMPORT | none | defer | filesystem/runtime forbidden |
| local review scaffolds outside cluster | no selected implementation value in T5 | NO_PACKAGE_OR_RUNTIME_VALUE | predecessor ledger | retain prior disposition | out of tranche |
| projection authority doctrine | no new doctrine owner required | DOCTRINE_ADAPTED | existing Guard Contract boundary | encode as invariant | contract only |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| route/readiness data | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-route-readiness.contract.ts` | CONFIRMED_EXISTING | accepted input | consume without changing |
| acquisition evidence | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/controlled-acquisition.contract.ts` | CONFIRMED_EXISTING | accepted optional input | consume without executing |
| combined case/evidence projection | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/` | NEW_FINDING | missing traceable read model | add one owner file |
| local projector/file writer | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/`; `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/` | REJECT_DIRECT_IMPORT | weaker and I/O-shaped | do not copy or activate |

## Mandatory Blind-Spot Control Block

The local folder is provenance-backed derived synthesis. Selection followed
detailed file/use-case inspection and owner comparison; absence from current
paths was not treated as low value. Knowledge, import, runtime, and authority
decisions remain separate.

## External Repository Absorption Entry Control

| Field | Value |
| --- | --- |
| Source type | selected mixed-origin copied folder with upstream provenance context |
| Upstream or source-mirror disposition | predecessor evidence reused; no fetch or execution |
| Enumeration or manifest plan | accepted 205-file ledger; named nine-file cluster |
| Per-file terminal-ledger plan | nine hashes remain traceable to the accepted ledger |
| Owner or overlap route | existing Guard Contract package |
| Value-disposition route | pure projection DO_NOW; adapters/executor deferred |
| Claim boundary | no direct import, full rescan, or activation claim |

## Rescan Intelligence Hardening

Original source artifact: accepted mixed-origin local Capability Preflight Bootstrap folder.

Predecessor intake artifact: RSPB-AI-T0 205-file manifest and ledger.

Delta ledger status: reused; nine selected hashes recomputed.

Routing matrix status: projection cluster routed to Guard Contract.

Semantic sampling status: selected contracts, schemas, source, tests, and redaction policy inspected.

- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Category | Disposition |
| --- | --- |
| UNCHANGED_FROM_INTAKE | 196 files retain prior disposition |
| CHANGED_DISPOSITION | nine-file cluster selected for CVF-native adaptation |
| NEW_FINDING | combined projection seam is absent from current owner |
| REMOVED_OR_REJECTED | direct candidate import and I/O remain rejected |

### Follow-Up Routing Matrix

| Lane | Routing |
| --- | --- |
| DO_NOW | pure projection contract and tests |
| SEPARATE_RUNTIME_TRANCHE | any file export or adapter |
| STRATEGIC_OPERATOR_DECISION | any authority/runtime expansion |
| OUT_OF_SCOPE | provider/live/public/deploy/production |
| RESOLVED_BY_DESIGN | projection-only authority boundary |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- |
| RSPB-T5-S1 | case projection contract | projection does not create authority | ADAPT | manual/projected state cannot authorize action | REQUIRE_FAIL_CLOSED |
| RSPB-T5-S2 | domain evidence contract | findings require evidence | ADAPT | unresolved references and false demonstrated steps | REQUIRE_FAIL_CLOSED |
| RSPB-T5-S3 | secret policy | raw secrets cannot enter projection | ADAPT | nested secret-like value | REQUIRE_SECRET_SAFE |

## Corpus Completeness And Report Integrity

- Corpus task class: selected capability-cluster absorption.
- Corpus root: nine selected files in the accepted local folder.
- Snapshot time: 2026-08-16 dispatcher selection.
- Enumeration command: `rg --files --hidden --no-ignore` from the accepted predecessor, plus named nine-file selection.
- Manifest artifact or inline manifest: accepted 205-file manifest and Selected Cluster Evidence in the work order.
- Manifest hash: nine per-file SHA-256 values in the paired work order.
- Processing ledger artifact or inline ledger: accepted 205-row ledger plus value conversion matrix above.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.
- Reconciliation: manifest=9; ledger_terminal=9; exclusions=196; unresolved=0; predecessor_total=205.
- Unresolved files: 0.
- Declared exclusions: 196 files outside this capability cluster.
- Unreadable or unsupported files: none in the selected cluster.
- Aggregation check: 9 + 196 = 205.
- Drift check: selected hashes recomputed; no excluded-file freshness claim.
- Output traceability: cluster maps to four worker-owned paths.
- Adversarial verification: authority, evidence binding, freshness, secrets, and determinism required.
- Corpus verdict: PARTIAL

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | Guard Contract barrel export | returned projection data is non-authoritative and read-only | focused tests required | internal contract import only | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | no adapter opened | no ingress, authentication, approval, receipt transport, raw-data export, or mutation authority | forbidden scope | deferred separate adapter owner | DEFERRED_WITH_REASON |

## Evidence / Verification

Required proof: TypeScript no-emit; focused Vitest tests; Guard Contract package
tests; reviewer-fast gate; exact manifest diff; independent reviewer probes;
pre-commit only by reviewer/closer.

## Risk / Corrective Action

Fail closed on malformed/unbounded input, unknown evidence references, stale
source bindings, secret-like values, inferred steps misrepresented as
demonstrated, nondeterministic ordering, or any authority-mutation implication.
If safe behavior requires I/O or changes outside the four allowed paths, stop.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | accepted ledger -> inspected projection cluster -> current T3/T4 owners -> Guard Contract adaptation |
| Matching local-view guard | `governance/compat/check_mixed_origin_derived_synthesis_absorption.py` |
| Owner surface | Guard Contract projection kernel |
| Disposition | PROCEED_BOUNDED_HIGH_VALUE |
| Claim boundary | no autonomous mutation, adapter activation, or external authority |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance implementation dispatch; public sync is forbidden.

## Claim Boundary

This baseline authorizes one hermetic projection contract and tests. It does
not certify runtime integration, filesystem export, adapter availability,
trusted evidence, cross-runtime determinism, provider/live behavior, public
readiness, deployment, or production.
