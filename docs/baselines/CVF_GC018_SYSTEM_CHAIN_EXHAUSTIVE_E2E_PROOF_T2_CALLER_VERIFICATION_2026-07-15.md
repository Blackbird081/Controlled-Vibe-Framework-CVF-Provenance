# CVF GC-018 System Chain Exhaustive Proof T2 Caller Verification

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: baseline

Date: 2026-07-15

GC-018 ID: `SCLP-X-T2-GC018`

dispatchBaseHead: `4105d2848`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Authorize one provider-free, repository-wide, read-only source-verification
tranche for the two decision-bearing T1 candidates: GC-009
`MandatoryGateway`/`createMandatoryGateway` and GC-010
`AgentExecutionRuntime`. T2 verifies caller existence only. It does not invoke
either runtime, promote proof status, or mutate an owner or GAP.

## Proposed Tranche / Decision

`SCLP-X-T2` may create exactly one JSON caller-verification record, one human
audit, and one no-commit worker return. It must enumerate and terminally
classify every repository match for the target symbols and module paths before
assigning either target one allowed `callerVerificationDisposition`.

Allowed target dispositions:

- `NON_TEST_PRODUCTION_CALLER_FOUND`
- `NO_NON_TEST_PRODUCTION_CALLER_FOUND`
- `AMBIGUOUS_INDIRECT_REFERENCE`

Allowed proposal-only architecture recommendations:

- `UPDATE_EXISTING_PROPOSED`
- `ADD_GAP_ENTRY_PROPOSED`
- `RETURN_TO_ORCHESTRATOR`

## Depth And Value Decision

The smallest decision-changing step selected by T1 is a full-repository caller
search, not runtime execution. Its cost is low and its result directly decides
whether `OWNER-GAP-01` should next route toward an existing-owner update or a
formal GAP proposal. A test-only constructor, type import, comment, generated
coverage page, historical document, or private external review is not a
production caller.

## Dependency Release Evidence

| Dependency | Accepted artifact | Material commit | Final disposition | Release result |
|---|---|---|---|---|
| T1 value-selection closure | `docs/reviews/CVF_SYSTEM_CHAIN_EXHAUSTIVE_PROOF_T1_VALUE_SELECTION_COMPLETION_2026-07-15.md` | `c53bef36c` | bounded reviewer PASS | PASS - T2 packet authoring released |
| accepted T1 decision record | `docs/reference/system_chain/CVF_SYSTEM_CHAIN_EXHAUSTIVE_PROOF_T1_VALUE_SELECTION.json` | `c53bef36c` | two T2 candidates; recommendation only | PASS - immutable T2 selection input |
| exhaustive roadmap | `docs/roadmaps/CVF_SYSTEM_CHAIN_EXHAUSTIVE_E2E_PROOF_ROADMAP_2026-07-15.md` | `c53bef36c` | `ACTIVE_T1_CLOSED_T2_PACKET_AUTHORING_NEXT` | PASS - T2 packet only |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| GC-009 is selected as a T2 candidate | `docs/reference/system_chain/CVF_SYSTEM_CHAIN_EXHAUSTIVE_PROOF_T1_VALUE_SELECTION.json` | `decisionLedger`; `T1-DEC-01` | `candidateDecision` | T1 value-selection schema | VALUE_SET | ACCEPT |
| GC-010 is selected as a T2 candidate | `docs/reference/system_chain/CVF_SYSTEM_CHAIN_EXHAUSTIVE_PROOF_T1_VALUE_SELECTION.json` | `decisionLedger`; `T1-DEC-02` | `candidateDecision` | T1 value-selection schema | VALUE_SET | ACCEPT |
| the catalog GC-009 edge is not an independent branch | `docs/reference/system_chain/CVF_SYSTEM_CHAIN_EXHAUSTIVE_PROOF_T1_VALUE_SELECTION.json` | `decisionLedger`; `T1-DEC-03` | `relatedClaimRelationship` | T1 value-selection schema | VALUE_SET | ACCEPT |
| owner/GAP route reopens on repository-wide caller evidence | `docs/reference/system_chain/CVF_SYSTEM_CHAIN_EXHAUSTIVE_PROOF_T1_VALUE_SELECTION.json` | `decisionLedger`; `T1-DEC-04` | `reopenCondition` | T1 value-selection schema | VALUE_SET | ACCEPT |
| `MandatoryGateway` exists | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.ts` | line 65 | `MandatoryGateway` | guard-contract runtime | EXISTS | ACCEPT |
| `createMandatoryGateway` exists | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.ts` | line 219 | `createMandatoryGateway` | guard-contract runtime | EXISTS | ACCEPT |
| `AgentExecutionRuntime` exists | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime.ts` | line 129 | `AgentExecutionRuntime` | guard-contract runtime | EXISTS | ACCEPT |

## Accepted Input Hash Manifest

| Input | SHA-256 | Role |
|---|---|---|
| `docs/reference/system_chain/CVF_SYSTEM_CHAIN_EXHAUSTIVE_PROOF_T1_VALUE_SELECTION.json` | `ab7797912c35ff6a29173b956678f1af2ce47b8e69b5b2f8940713e1259863ae` | immutable two-target decision authority |
| `docs/reviews/CVF_SYSTEM_CHAIN_EXHAUSTIVE_PROOF_T1_VALUE_SELECTION_COMPLETION_2026-07-15.md` | `c429881283632af0f2ecb2f3b90ebd8c24bca423c3f4df3d0e53244ec1417a39` | immutable release evidence |

## Current Runtime Freshness Verification

Dispatch-time repository search found only the defining MandatoryGateway
factory/self-construction, test constructors, type/comment references,
generated coverage pages, historical documents, and private external-review
records. No non-test production construction or factory call was found. This
is dispatch freshness evidence only; the worker must repeat the complete scan
and classify every match.

## Evidence / Verification

Dispatch evidence consists of the accepted T1 hashes, direct source-symbol
verification, repository collision-search freshness, the exact three-path
fulfillment manifest, and the pre-dispatch machine-gate result. This is packet
verification only; the worker and reviewer must independently recompute the
complete filesystem search before any caller disposition is accepted.

## Negative Search And Collision Discipline

| Search class | Root and exclusions | Dispatch result | Required worker disposition |
|---|---|---|---|
| full collision inventory | repository filesystem, excluding `.git`, `node_modules`, `.next`, build outputs, and `.cvf` receipts | source, tests, docs, private review, and generated coverage collisions exist | terminally classify every match |
| constructor/factory calls | same root, with test/spec and generated matches retained for classification | defining factory plus test-only constructors | distinguish self/test from production caller |
| import/re-export/module-path references | same root | provider type imports and historical/generated references | resolve direct, type-only, comment, generated, or ambiguous |

## Planned Worker Fulfillment Manifest

| Path | Action | Required content |
|---|---|---|
| `docs/reference/system_chain/CVF_SYSTEM_CHAIN_EXHAUSTIVE_PROOF_T2_CALLER_VERIFICATION.json` | CREATE | source hashes, filesystem search manifest, terminal match ledger, two target decisions, proposal-only next route |
| `docs/audits/CVF_SYSTEM_CHAIN_EXHAUSTIVE_PROOF_T2_CALLER_VERIFICATION_AUDIT_2026-07-15.md` | CREATE | human match reconciliation, caller decisions, collision analysis, bounded recommendation |
| `docs/reviews/CVF_SYSTEM_CHAIN_EXHAUSTIVE_PROOF_T2_CALLER_VERIFICATION_WORKER_RETURN_2026-07-15.md` | CREATE | no-commit return, gates, exact status/diff, claim boundary |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | three T2 evidence outputs and read-only repository sources | enumerate/classify/recommend only | terminal match ledger and hashes | repository-file read only | `IMPLEMENTED` |
| `EXTERNAL_AGENT_CLI_MCP` | no T2 adapter | no ingress, mutation, execution, receipt, or public authority | forbidden scope | separate future source-verified adapter packet | `DEFERRED_WITH_REASON` |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --surface-selector "system-chain exhaustive proof T2 caller verification" --risk-ceiling HIGH --max-results 20 --json`

Returned defectIds: `ADIF-0001`, `ADIF-0002`, `ADIF-0007`, `ADIF-0014`,
`ADIF-0015`, `ADIF-0020`, `ADIF-0021`, `ADIF-0028`, `ADIF-0029`, and
`ADIF-0033`.

Dispatch impact: apply the returned source-fidelity, dispatch-quality,
literal-format, scope, no-commit, and reviewer-recomputation controls to this
packet.

## Corpus Completeness And Report Integrity

- Corpus task class: `FULL_REPOSITORY_MATCH_CORPUS` planned for worker
  execution; dispatch authoring itself uses targeted authority reads.
- Corpus root: repository filesystem at worker `executionBaseHead`.
- Snapshot time: worker execution start; not captured by this dispatch packet.
- Enumeration command: `rg --files --hidden --no-ignore` with only the explicit
  exclusions in Negative Search And Collision Discipline.
- Manifest artifact or inline manifest: planned T2 JSON `searchUniverse` and
  `queryManifest` fields.
- Manifest hash: worker must record the deterministic path-list hash.
- Processing ledger artifact or inline ledger: planned T2 JSON `matchLedger`.
- Allowed terminal statuses: `READ`, `SKIPPED_WITH_REASON`,
  `DEFERRED`, and `BLOCKED_UNREADABLE`. Match rows additionally use the ten
  `matchClassification` values authorized by this baseline.
- Reconciliation: manifest=planned-T2-JSON-search-universe; ledger_terminal=required-for-every-unique-match; exclusions=explicit-five-operational-classes-only; unresolved=0-required-for-a-no-caller-decision.
- Unresolved files: 0 required at worker completion; dispatch result is N/A
  with reason: the worker search has not executed.
- Declared exclusions: `.git`, dependency installs including `node_modules`,
  `.next`, build output, and `.cvf` runtime receipts.
- Unreadable or unsupported files: none permitted for terminal completion.
- Aggregation check: raw query hits must equal deduplicated ledger membership
  with every contributing query retained.
- Drift check: reviewer repeats enumeration and every query from the worker
  execution base.
- Output traceability: every target decision cites terminal ledger rows.
- Adversarial verification: generated, historical, private, test-only, type,
  and comment collisions cannot establish a production caller.
- Corpus verdict: PARTIAL

Reason: dispatch specifies the complete method, but worker enumeration and
terminal reconciliation have not executed.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_corpus_to_knowledge_map_reconciliation.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `Dependency Release Evidence`; `Source Verification Block`; `Negative Search And Collision Discipline`; `Reviewer Closure Conversion`; `COMPLETE_VERIFIED`; `Public Export Disposition` |
| gateRunPurpose | confirm T2 source fidelity, search-corpus accounting, handoff shape, and zero-execution boundary after read-ahead |
| claimBoundary | dispatch structure only; no caller result or architecture mutation claim |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id SCLP-X-T2 --title "System Chain Exhaustive Proof T2 Repository-Wide Caller Verification" --date 2026-07-15 --base 4105d2848 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic no-commit source-verification dispatch |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | accepted hashes, two-target search corpus, terminal match taxonomy, exact outputs, and execution hold |
| checkerReadAheadConfirmation | applicable dispatch, corpus, handoff, return, and freshness checkers read |
| docOnlyNewFields | `callerVerificationDisposition`; `matchClassification`; `architectureRecommendation` |
| claimBoundary | dispatch-authoring provenance only |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance caller verification; no public-sync authority.

## Claim Boundary

This baseline authorizes repository-wide read-only source search and
classification for exactly two target controls. It does not authorize runtime,
test, CI, browser, CLI, provider, live proof, owner/GAP mutation, proof-status
promotion, T3-T4 release, or public/production claims.
