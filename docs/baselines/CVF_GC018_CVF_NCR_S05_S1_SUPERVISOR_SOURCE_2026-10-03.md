# GC-018 - NCR S05 S1 Independent Supervisor Source

Memory class: POINTER_RECORD
docType: baseline
Status: ACCEPTED_BASELINE
Date: 2026-10-03
Batch ID: CVF-NCR-S05-S1-SUPERVISOR-SOURCE
providerExecutionAuthority: FORBIDDEN

## Purpose

Author a standalone, parameterized supervisor source contract/component and six inert fixture sources. Accept source identity, explicit data/state contracts, fail-closed backend seams and complete static review evidence only. No C1 dependency/cache completion, upstream integration or runtime containment claim.

## Authority Chain

| Authority | Evidence | Disposition |
|---|---|---|
| Operator current request | `docs/reviews/evidence/cvf-ncr-s05-s1-supervisor-source-inputs-2026-10-03.json` exact instruction | ACCEPT packet authoring/review and manual worker relay after gate, no provider invocation |
| Project source contract | `docs/reference/CVF_NCR_S05_SUPERVISOR_SOURCE_CONTRACT_2026-10-03.md` | ACCEPT new versioned independent data/state contract |
| GC-018 | `docs/baselines/CVF_GC018_CVF_NCR_S05_S1_SUPERVISOR_SOURCE_2026-10-03.md` | ACCEPT exact source-write limits only after bound release |
| Old C1 disposition | `docs/reviews/CVF_CVF_NCR_S05_CONTROL_FIXTURE_DESIGN_LOCAL_REVIEW_2026-10-03.md` | ACCEPT historical STOP retained; not a dependency to reset |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| New independent component contract | GOVERNED_PROJECT_CONTRACT | `docs/reference/CVF_NCR_S05_SUPERVISOR_SOURCE_CONTRACT_2026-10-03.md` | Protocol / Contract / Requirements | validate_envelope; SupervisorPlan; BoundaryAdmission | local-supervisor-source@0.1.0 | ACCEPT |
| Old STOP retained | GOVERNED_DECISION | `docs/reviews/CVF_CVF_NCR_S05_CONTROL_FIXTURE_DESIGN_LOCAL_REVIEW_2026-10-03.md` | Operator-Delegated Architecture Disposition - Option D | STOP_AT_DESIGN | Local review | ACCEPT |
| Stable problem and readiness | GOVERNED_STANDARD | `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md` | Enforcement Invariants 1/7/8/9 | stable key; no same-problem successor | SCEC | ACCEPT |
| Fixture planning constraints | GOVERNED_RETAINED_EVIDENCE | `docs/reference/CVF_NCR_S05_CONTROL_FIXTURE_DESIGN_2026-10-03.md` | Finite fixtures | FX-D1..FX-L1 | planned fixtures, not OS proof | ACCEPT |
| Verified Windows native ABI/backend | SOURCE_GAP | `docs/reference/CVF_NCR_S05_SUPERVISOR_SOURCE_CONTRACT_2026-10-03.md` | WindowsJobBackend unavailable | NotAdmitted | no API evidence acquired | REJECT |

## Scope / Target / Owner Boundary

Worker may create only the new sibling source root `D:\UNG DUNG AI\TOOL AI 2026\CVF-NCR-S05-S1-SOURCE-20261003`, subdirectories src/fixtures/evidence, its fourteen allowlisted files, and two new CVF return/evidence files. Source text authoring plus read-only syntax/hash inspection only. Do not run/import/compile source or fixtures, launch processes, call native APIs, fetch/install/build, import upstream, create runtime roots or VHD/quota/ACL/firewall, infer/audio/render/provider/public/deploy, stage/commit or delegate. Ordinary new source-file writes are the only admitted effects after release; costs UNKNOWN.

## Architecture And Authority Boundary

Old problem `cvf-ncr-c1-metadata-footprint` remains STOP at ordinal2 with its original blocker and counters; nothing in this packet is its ordinal3 or a resolution. Previous option D applied to the C1-scoped candidate lacking an independent contract. The operator now explicitly instructs Local to create a work order. This packet supplies the previously missing separate technical contract, rather than merely renaming the candidate.

| Dimension | Stopped C1 design | This source component admission |
|---|---|---|
| Objective | establish C1 dependency/cache/rights/preparation readiness | implement versioned, caller-parameterized source data/state interfaces |
| Authority | documentary design, no source writes | exact new sibling root/files, after bound release and pre-dispatch PASS |
| Deliverable | component metadata/design disposition | inert Python source, six fixture sources, exact hashes and static requirement mapping |
| Acceptance | unresolved C1 preparation/control contract | source structure and mandatory refusal at unimplemented native/disk/network seams |
| Integration | VieNeu/HyperFrames/model/browser/component identity | none: no upstream names, preset constants or C1 defaults in source logic |
| Blocker effect | old blocker retained | source can be accepted while old blocker stays wholly unresolved |

Independence test: removing all VieNeu/HyperFrames/dependency metadata leaves every source acceptance criterion meaningful. Implementing this source contract does not change C1 admission. The old stopped key/counters are preserved as historical constraints, not reset into this source lifecycle. New initial identity `local-supervisor-source-contract` denotes this concrete independent contract only; no C1 successor is released. If implementation introduces C1-specific behavior or claims to reduce its blocker, reject as scope/identity violation rather than silently reroute.


## Independent Review Probe Admission Contract

independentProbeRequired: YES
independentProbeRiskClass: HIGH
independentProbeDispositionAtDispatch: PLAN_ADMITTED_PENDING_REVIEWER_EXECUTION
probeExecutorRole: LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER
implementationOracleSeparation: REQUIRED_DIFFERENT_FIXTURE_AND_ASSERTION_PATH
positiveControl: Local independently reads actual source/AST and identity ledger with a separately authored oracle; valid pure-data plans and explicit unavailable backend remain source-only.
negativeMutationClasses: missing preconditions; traversal/case collisions; non-finite limits; committed-versus-working-set conflation; import-time effects; fake capability booleans enabling OS actions; missing FX-L1; source hash called runtime proof; old STOP silently resolved.
expectedInformationGain: verify actual source effect boundary and contract correspondence, not OS behavior.
rerunCostReason: one narrow post-return static probe; no worker suite/native/source/fixture/provider execution.
reviewerDecisionOwner: LOCAL

Worker records PENDING_REVIEWER_EXECUTION; Local owns probe result. No live/runtime control proof is claimed.

## Semantic Convergence Outcome

```json
{"schemaVersion": "cvf.semanticConvergenceControl.v1", "problemKey": "local-supervisor-source-contract", "chainMode": "INITIAL", "chainOrdinal": 0, "predecessor": null, "blockerDelta": {"prior": [], "resolved": [], "retained": [], "new": ["SOURCE_CONTRACT_NOT_IMPLEMENTED", "SOURCE_STATIC_REVIEW_PENDING"], "reopened": [], "current": ["SOURCE_CONTRACT_NOT_IMPLEMENTED", "SOURCE_STATIC_REVIEW_PENDING"]}, "resolutionEvidence": {}, "counters": {"partialReadyClosures": 0, "reviewerScopeExpansions": 0, "sameClaimCorrections": 0, "nonDecreasingBlockerTransitions": 0}, "claims": [{"claimId": "SOURCE_PLAN_ONLY", "claimClass": "DOCUMENTATION_ONLY", "proofClass": "PROPOSAL_ONLY_NO_RUNTIME_READINESS", "evidenceRef": "docs/reference/CVF_NCR_S05_SUPERVISOR_SOURCE_CONTRACT_2026-10-03.md"}], "requiredDisposition": "CONTINUE_BOUNDED", "successorScope": "INITIAL_BOUNDED"}
```

New source lifecycle is justified by Architecture And Authority Boundary and the numbered independent protocol. The stopped C1 state remains a distinct historical constraint; no metadata successor or reset.

## Acceptance Criteria

- [ ] fourteen exact source files and two governed outputs; raw identity joins; no extra cache/bytecode files.
- [ ] versioned data/state interface and unavailable native/disk/network paths implemented; no import-time or enabled OS effect.
- [ ] six inert fixture contracts including FX-L1; planned cases/unknown controls retained.
- [ ] old C1 STOP/key/counters unchanged; no integration or claimed blocker reduction.
- [ ] full return gate PASS; pending distinct Local static source review; worker no commit.

## Evidence Requirements

Source rows include full external path, relative path, bytes/raw SHA-256, actor and created/not-created status; manifest recipe and separate root safety record. Static requirements map must distinguish source syntax, source-plan structure and unexecuted OS cases. Every asserted field has a source symbol/locator; unresolved native evidence => NO_GO. File/time limits cooperative, all costs UNKNOWN.

## Prospective File-Size Admission

| Path | Current lines | Maximum physical lines |
|---|---|---|
| `docs/reviews/evidence/cvf-ncr-s05-s1-supervisor-source-worker-2026-10-03.json` | absent | 950 |
| `docs/reviews/CVF_CVF_NCR_S05_S1_SUPERVISOR_SOURCE_WORKER_RETURN_2026-10-03.md` | absent | 620 |

External fourteen files: <=1MiB total, Python<=1200 lines each and Markdown/JSON<=600 each; one cooperative120-minute turn. Exact-root custody pending Local review, no automatic expiry/deletion.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: Local binds this paired source admission and actual material commit to currentAuthority/nextAllowedMove; worker has no continuity or commit permission.

Protected paths:
- `AGENT_HANDOFF_V63_2026-09-18.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`

Operator authorization: explicit instruction to orchestrator/reviewer to create the work order; Local reviews source-writing boundary, commits pair then continuity and runs actual bound pre-dispatch. No automatic worker invocation.

Rollback boundary: revert this packet continuity only; preserve historical design/D decision and C1 STOP; no source root or runtime cleanup grant.

## Retained Evidence Read Envelope

Only receipt input paths and this source contract; no mirror/snapshot refresh or direct source intake. General platform claims remain unverified and OS backend unavailable. Exact future source-target filesystem safety reads only; no host software/OS/user-document sweep.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local dispatcher/reviewer |
| Provider or surface | private shared CVF workspace |
| Session or invocation | CVF-NCR-S05-S1-SUPERVISOR-SOURCE |
| Working directory | repository root |
| Command or tool surface | local governed reads, scaffold, packet authoring and structural gates |
| Target paths | `docs/reference/CVF_NCR_S05_SUPERVISOR_SOURCE_CONTRACT_2026-10-03.md`; `docs/baselines/CVF_GC018_CVF_NCR_S05_S1_SUPERVISOR_SOURCE_2026-10-03.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_S05_S1_SUPERVISOR_SOURCE_2026-10-03.md`; `docs/reviews/evidence/cvf-ncr-s05-s1-supervisor-source-inputs-2026-10-03.json` |
| Allowed scope source | operator explicitly instructed orchestrator/reviewer to create work order |
| Before status evidence | prior clean worktree at captured HEAD 64dbfafd53bad6a2ad076bce16cd4851d68b5e27; exact four packet paths/two outputs absent |
| After status evidence | four dispatcher paths; no worker/source root creation |
| Diff evidence | git diff --check; git status --short --untracked-files=all |
| Approval boundary | manual worker relay after actual bound gate; no dispatcher worker/provider invocation |
| Claim boundary | source contract/admission only, no native proof |
| Agent type | INTERNAL_AGENT dispatcher |
| Invocation ID | cvf-ncr-s05-s1-source-dispatch-20261003 |
| Expected manifest | `docs/reference/CVF_NCR_S05_SUPERVISOR_SOURCE_CONTRACT_2026-10-03.md`; `docs/baselines/CVF_GC018_CVF_NCR_S05_S1_SUPERVISOR_SOURCE_2026-10-03.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_S05_S1_SUPERVISOR_SOURCE_2026-10-03.md`; `docs/reviews/evidence/cvf-ncr-s05-s1-supervisor-source-inputs-2026-10-03.json` |
| Actual changed set | `docs/reference/CVF_NCR_S05_SUPERVISOR_SOURCE_CONTRACT_2026-10-03.md`; `docs/baselines/CVF_GC018_CVF_NCR_S05_S1_SUPERVISOR_SOURCE_2026-10-03.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_S05_S1_SUPERVISOR_SOURCE_2026-10-03.md`; `docs/reviews/evidence/cvf-ncr-s05-s1-supervisor-source-inputs-2026-10-03.json` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_acceptance_ledger.py`; `governance/compat/check_dispatch_release_readiness.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_independent_review_probe_admission.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_absorption_blindspot_control_presence.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | first-section envelope; acceptance ledger; gate-role graph; SCEC predecessor/retained counters/escalation; trace/delta fields; standalone independent-probe declaration |
| gateRunPurpose | Confirm bounded paired design dispatch before release, not first discovery |
| claimBoundary | Declaration/static evidence only; not runtime enforcement |

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - exact named-file source task, not upstream absorption, full scan or all-files-read claim; fourteen-file write ledger is mandatory identity evidence.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Input source | accepted Local source-only closure `docs/reviews/CVF_CVF_NCR_HYPERFRAMES_REUSE_CAPABILITY_AUDIT_COMPLETION_2026-10-03.md` and governed evidence `docs/reviews/evidence/cvf-ncr-hyperframes-vieneu-local-review-2026-10-03.json` |
| Chain map route | D110 qualified metadata -> operator requested integrated design -> Local disposition |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | accepted private video design / work-order / Local artifact-verification owners |
| Disposition | SOURCE_COMPARISON_RUNTIME_PENDING |
| Claim boundary | bounded public text/metadata reads, no binary acquisition/absorption/runtime or external-agent dispatch |

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Mandatory Blind-Spot Control Block

Named blind spots: absent/unreviewed helper, literal ingress versus read bytes, editable SDK seam, npm partial graph/hooks, rights/consent, stage-specific human gates, enforcement and quality unknown. Neither proposal nor budget proves runtime.

## Claim Boundary

Worker may create only the new sibling source root `D:\UNG DUNG AI\TOOL AI 2026\CVF-NCR-S05-S1-SOURCE-20261003`, subdirectories src/fixtures/evidence, its fourteen allowlisted files, and two new CVF return/evidence files. Source text authoring plus read-only syntax/hash inspection only. Do not run/import/compile source or fixtures, launch processes, call native APIs, fetch/install/build, import upstream, create runtime roots or VHD/quota/ACL/firewall, infer/audio/render/provider/public/deploy, stage/commit or delegate. Ordinary new source-file writes are the only admitted effects after release; costs UNKNOWN.

SOURCE_PLAN_ONLY, all OS cases NOT_EXECUTED_PLANNED. Old C1 STOP/preset/lane remain unchanged. No installed helper or runtime-ready/containment/rights/cost proof.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Decision / Baseline / Proposed Tranche

Exact source authoring admitted only after committed/hash-bound pair, Local continuity and pre-dispatch PASS. No source execution or runtime admission. No automatic worker call.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work_order_authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Command: `python governance/compat/run_adif_defect_resolver.py --task-class work_order_authoring --role dispatcher --lifecycle-phase pre-dispatch --json`; 0 items, truncated=false.

Returned defects: NONE_RETURNED

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | independent supervisor source contract |
| claimDisposition | CLAIM_REJECTED: no runtime behavior proven |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: source will be authored only under bound release; no OS action or source execution |
| invocationBoundary | source writing and static local evidence only |
| interceptionBoundary | no implemented enforcement |
| claimLanguage | proposals, UNKNOWN or NO_GO, cases planned |
| forbiddenExpansion | payload/install/build/upstream import/control mutation/voice/render/provider/public/deploy |

## Negative Search And Collision Discipline

Dispatcher checked exact four material paths and two governed returns absent at clean 64dbfafd53bad6a2ad076bce16cd4851d68b5e27. Worker must check sibling target/parent/reparse safety after release immediately before first write; absence was not certified by this packet. No overwrites/deletion/reset/stash or broad inventory.
