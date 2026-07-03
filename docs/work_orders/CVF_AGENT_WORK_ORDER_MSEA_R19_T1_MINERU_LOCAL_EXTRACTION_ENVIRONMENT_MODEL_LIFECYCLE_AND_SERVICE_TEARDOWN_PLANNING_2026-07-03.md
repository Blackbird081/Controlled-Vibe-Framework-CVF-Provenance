# CVF Agent Work Order - MSEA-R19-T1 MinerU Local Extraction Environment Model Lifecycle And Service Teardown Planning

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: MSEA_R19_T1

Dispatch base head: add7eda4

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker

Reviewer/closer: reviewer/closer

Worker return path: `docs/reviews/CVF_MSEA_R19_T1_MINERU_LOCAL_EXTRACTION_ENVIRONMENT_MODEL_LIFECYCLE_AND_SERVICE_TEARDOWN_PLANNING_WORKER_RETURN_2026-07-03.md`

## Dispatch Prompt Envelope

Role: delegated worker for MSEA_R19_T1.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R19_T1_MINERU_LOCAL_EXTRACTION_ENVIRONMENT_MODEL_LIFECYCLE_AND_SERVICE_TEARDOWN_PLANNING_2026-07-03.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: worker must capture `git rev-parse --short HEAD` before edits.

Current-time notes: artifact date is 2026-07-03; use current repository state and pinned MinerU source mirror, not stale chat memory.

Do-not-misread notes: this packet opens planning and read-only local inventory only; it does not authorize running MinerU, importing MinerU, installing packages, downloading models, starting a local service, running Docker, reading document body content, creating extraction outputs, public-sync, schema/writer/adapter/checker implementation, document-truth, extraction-accuracy, legal advice, current-law, production, or workflow-chain claims.

Required first actions: read startup files, guard orientation, literal gotchas, this work order, the paired GC-018 baseline, source references, and checker source listed in the Checker Source Read-Ahead Block before writing worker outputs.

Return contract: create the worker return and companion readiness matrix, run required gates, leave changes uncommitted, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Create a source-verified environment/model lifecycle and local-service teardown
readiness matrix for a future private MinerU local runtime smoke pilot on
Candidate Group A. The worker must classify whether the next governed move can
open a runtime-smoke work order, or must hold for model-cache planning,
operator environment choice, service teardown proof, or output-quarantine
design.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind source-intake --batch-id MSEA_R19_T1 --title "MinerU Local Extraction Environment Model Lifecycle And Service Teardown Planning" --date 2026-07-03 --base add7eda4 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | source-intake plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Completed scaffold fields, set DISPATCH_READY, added R18 dependency release, source-verified MinerU environment/model/service facts, evidence-reuse plan, output-shape mandate, route tokens, and runtime hold boundaries. |
| checkerReadAheadConfirmation | Read `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_source_intake_decision_packet_preflight.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`. |
| docOnlyNewFields | selectedRouteToken; environmentInventoryMode; modelLifecyclePlan; temporaryServiceTeardownPlan; runtimeSmokePilotReadiness; outputQuarantineDisposition |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |

## Worker Autonomy / No-Question Rule

Worker must repair allowed-scope checker failures directly by reading the
failing checker source and matching the literal required shape. Worker should
return to orchestrator only for a source contradiction, missing source mirror,
missing Candidate Group A authority, forbidden-scope need, or missing local
permission that makes completion impossible.

## Dependency Release Evidence

| Dependency | Evidence artifact | Commit | Release disposition |
| --- | --- | --- | --- |
| MSEA-R18-T1 accepted route selection | `docs/reviews/CVF_MSEA_R18_T1_MINERU_CANDIDATE_GROUP_A_LOCAL_EXTRACTION_PILOT_PLAN_AND_RECEIPT_READINESS_SELECTION_WORKER_RETURN_2026-07-03.md`; `docs/reference/CVF_MSEA_R18_T1_MINERU_CANDIDATE_GROUP_A_LOCAL_EXTRACTION_PILOT_PLAN_AND_RECEIPT_READINESS_MATRIX_2026-07-03.md` | `d40e21c8` | SATISFIED - route token `HOLD_RUNTIME_PENDING_ENVIRONMENT_OR_MODEL_PLAN` releases this planning-only work order |
| Session next-move freshness | `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `AGENT_HANDOFF_V34_2026-07-03.md` | `add7eda4` | SATISFIED - next allowed move permits fresh GC-018/source-verified work order or roadmap for environment/model/local-service planning |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: ADIF-0001; ADIF-0002; ADIF-0014; ADIF-0015; ADIF-0020; ADIF-0021; ADIF-0007; ADIF-0016; ADIF-0017; ADIF-0006

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch` |
| Returned defect count | 10 |
| Returned defects | ADIF-0001; ADIF-0002; ADIF-0014; ADIF-0015; ADIF-0020; ADIF-0021; ADIF-0007; ADIF-0016; ADIF-0017; ADIF-0006 |
| Disclosed defectIds | ADIF-0001; ADIF-0002; ADIF-0014; ADIF-0015; ADIF-0020; ADIF-0021; ADIF-0007; ADIF-0016; ADIF-0017; ADIF-0006 |
| Dispatch impact | Worker output checker read-ahead is mandatory; provider-local authority is excluded; runtime candidates are classified without execution; source verification symbol cells use real symbols or sections only. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_source_intake_decision_packet_preflight.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py` |
| literalTokensReviewed | Dispatch Prompt Envelope fields; Scaffold Provenance Block fields; Source Verification Block columns; Evidence Reuse And Encoding Plan fields; ADIF resolver query exactness; Dependency Release Evidence; Agent Handoff Contract Control Block fields; Reviewer Closure Conversion fields; Worker Return Packet Shape Contract fields; Source-Intake Decision Packet Fields; Public Export Disposition token `DEFERRED_PRIVATE_ONLY`; Target / Source; Scope / Applies To; Rescan Intelligence Hardening; ledger terminal marker; `CHECKER_CANDIDATE`; `REMOVED_OR_REJECTED`; `RESOLVED_BY_DESIGN`; Delta block field labels; Agent Operation Trace labels. |
| gateRunPurpose | Confirmation evidence after checker source read-ahead, not first discovery; gates confirm this work order's dispatch shape and source-fidelity evidence. |
| claimBoundary | Read-ahead covers this work order and paired baseline only; worker output artifacts must perform their own checker-source read-ahead before writing. |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

recomputeReason: R19-T1 must re-read current CVF-governed sources, pinned MinerU source mirror docs, and read-only local environment indicators before selecting the next route; Candidate Group A document metadata may be referenced from R17/R18 without reading document body content.

unicodePathHandling: Use LiteralPath and UTF-8-safe command output for local paths; do not normalize or rewrite filenames.

extractedTextAuthority: N/A with reason

| Field | Value |
| --- | --- |
| verificationMode | RECOMPUTE_REQUIRED |
| priorVerificationArtifact | `docs/reference/CVF_MSEA_R18_T1_MINERU_CANDIDATE_GROUP_A_LOCAL_EXTRACTION_PILOT_PLAN_AND_RECEIPT_READINESS_MATRIX_2026-07-03.md` |
| priorVerificationAnchor | `## Runtime Prerequisite Disposition` |
| recomputeReason | R19-T1 must re-read current CVF-governed sources, pinned MinerU source mirror docs, and read-only local environment indicators before selecting the next route |
| freshRecomputeRequired | true for source facts and read-only environment inventory only; no document body read and no MinerU extraction |
| unicodePathHandling | Use `-LiteralPath` and UTF-8-safe command output for local paths; do not normalize or rewrite filenames |
| extractedTextAuthority | N/A with reason: R19-T1 must not read document body text or treat extracted text as authority |

## Operator Authorization And Privacy Boundary

Candidate Group A source documents are authorized for local private CVF testing
only. Original documents must not be public-synced or redistributed. This
tranche may plan a future runtime smoke pilot but must not create extraction
outputs, copy source documents into the repository, read source document body
content, or include sensitive personal/legal details in committed artifacts.

## Source Verification Block

| Claimed item | Claim type | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R18 accepted route holds runtime pending environment or model plan | VALUE_SET | VALUE_SET | `docs/reviews/CVF_MSEA_R18_T1_MINERU_CANDIDATE_GROUP_A_LOCAL_EXTRACTION_PILOT_PLAN_AND_RECEIPT_READINESS_SELECTION_WORKER_RETURN_2026-07-03.md` | `## Reviewer Decision / Closure Disposition` | `HOLD_RUNTIME_PENDING_ENVIRONMENT_OR_MODEL_PLAN` | MSEA-R18-T1 worker return | ACCEPT |
| R18 matrix marks Environment Plan, Model Lifecycle, and Temporary Service as unresolved | VALUE_SET | VALUE_SET | `docs/reference/CVF_MSEA_R18_T1_MINERU_CANDIDATE_GROUP_A_LOCAL_EXTRACTION_PILOT_PLAN_AND_RECEIPT_READINESS_MATRIX_2026-07-03.md` | `## Runtime Prerequisite Disposition` | Runtime Prerequisite Disposition | MSEA-R18-T1 readiness matrix | ACCEPT |
| R18 command envelope is future-only and not executed | VALUE_SET | VALUE_SET | `docs/reference/CVF_MSEA_R18_T1_MINERU_CANDIDATE_GROUP_A_LOCAL_EXTRACTION_PILOT_PLAN_AND_RECEIPT_READINESS_MATRIX_2026-07-03.md` | `## Pilot Command Envelope` | Pilot Command Envelope | MSEA-R18-T1 readiness matrix | ACCEPT |
| R17 accepted Candidate Group A only for local private CVF testing | VALUE_SET | VALUE_SET | `docs/reference/CVF_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_LEDGER_2026-07-03.md` | `## Claim Boundary` | Candidate Group A | MSEA-R17-T1 intake ledger | ACCEPT |
| R12 local parser runtime pilot requires fresh GC-018 authorization | VALUE_SET | VALUE_SET | `docs/reference/CVF_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_2026-07-03.md` | runtime pilot gating table | Local parser runtime pilot | MSEA-R12-T1 policy reference | ACCEPT |
| MinerU pinned mirror is the upstream authority for this lane | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/INDEX.md` | row `opendatalab__MinerU` | `opendatalab__MinerU` | source mirror index | ACCEPT |
| MinerU CLI entry point is available as a project script | EXISTS | EXISTS | `.private_reference/source_mirrors/opendatalab__MinerU/pyproject.toml` | project scripts section | `mineru` | project scripts | ACCEPT |
| MinerU model download command is available as a project script but remains forbidden here | EXISTS | EXISTS | `.private_reference/source_mirrors/opendatalab__MinerU/pyproject.toml` | project scripts section | `mineru-models-download` | project scripts | ACCEPT |
| MinerU README says the pipeline backend runs on CPU or GPU | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/README.md` | line 74 | `pipeline` | upstream README | ACCEPT |
| MinerU README states `mineru` can automatically start a local temporary service when no API URL is provided | RUNTIME_BEHAVIOR | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/README.md` | line 146 | `mineru` | upstream README | ACCEPT |
| MinerU README states pure CPU execution is supported and GPU/MPS acceleration also exists | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/README.md` | line 184 | pure CPU environment | upstream README | ACCEPT |
| MinerU README cautions that non-mainline environments are not guaranteed | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/README.md` | line 216 | non-mainline environments | upstream README | ACCEPT |
| MinerU README shows pipeline command envelope for CPU use | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/README.md` | lines 334-336 | `mineru -p <input_path> -o <output_path> -b pipeline` | upstream README | ACCEPT |
| MinerU model-source docs define `MINERU_MODEL_SOURCE` accepted values | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/model_source.md` | line 12 | `MINERU_MODEL_SOURCE` | model source documentation | ACCEPT |
| MinerU model-source docs say unset variable allows automatic source selection | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/model_source.md` | line 12 | `MINERU_MODEL_SOURCE` | model source documentation | ACCEPT |
| MinerU model-source docs say the config write-back records the actual source after first auto probe | RUNTIME_BEHAVIOR | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/model_source.md` | line 26 | `model-source` | model source documentation | ACCEPT |
| MinerU model-source docs say model download writes model path and source to `mineru.json` | RUNTIME_BEHAVIOR | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/model_source.md` | line 44 | `mineru.json` | model source documentation | ACCEPT |
| MinerU model-source docs say local models can be enabled through environment variables | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/model_source.md` | lines 53-55 | `MINERU_MODEL_SOURCE` | model source documentation | ACCEPT |
| MinerU Docker docs restrict Docker deployment to Linux and Windows with WSL2 | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/quick_start/docker_deployment.md` | line 6 | Docker deployment | Docker deployment documentation | ACCEPT |
| MinerU Docker docs warn GPU memory pre-allocation can block multiple vLLM services | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/quick_start/docker_deployment.md` | line 54 | vLLM service | Docker deployment documentation | ACCEPT |

## New Doc-Only Fields

| Field | Meaning | Disposition |
| --- | --- | --- |
| selectedRouteToken | Worker-selected next-route token for reviewer/closer consideration | DOC_ONLY_NEW |
| environmentInventoryMode | Read-only local inventory mode, not installation or runtime execution | DOC_ONLY_NEW |
| modelLifecyclePlan | Documentation-only model source/cache/download/local-mode plan for a later tranche | DOC_ONLY_NEW |
| temporaryServiceTeardownPlan | Documentation-only local service detection and teardown checklist for a later tranche | DOC_ONLY_NEW |
| runtimeSmokePilotReadiness | Worker classification of whether a future runtime pilot can be authored | DOC_ONLY_NEW |
| outputQuarantineDisposition | Worker classification of private output root and no-public/no-commit handling | DOC_ONLY_NEW |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Existing MSEA-R19 artifacts | negative search for `MSEA_R19_T1`, `MSEA-R19-T1`, `LOCAL_EXTRACTION_ENVIRONMENT_MODEL_LIFECYCLE_AND_SERVICE_TEARDOWN`, and `Local Extraction Environment Model Lifecycle And Service Teardown` across governed docs and active session surfaces returned no matches before authoring | NO_PRIOR_ARTIFACT_COLLISION |
| Dispatch packet path check | No existing baseline or work order with these exact R19 names existed before this add operation | ABSENT_BEFORE_AUTHORING |
| Collision decision | MSEA-R19-T1 is a new child tranche after accepted MSEA-R18-T1 planning route selection | SAFE_TO_CREATE |

## Authority Chain

- Operator instruction: continue after accepted MSEA-R18-T1.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Active handoff: `AGENT_HANDOFF_V34_2026-07-03.md`.
- Paired GC-018 baseline: `docs/baselines/CVF_GC018_MSEA_R19_T1_MINERU_LOCAL_EXTRACTION_ENVIRONMENT_MODEL_LIFECYCLE_AND_SERVICE_TEARDOWN_PLANNING_2026-07-03.md`.
- Accepted R18 route selection: `docs/reviews/CVF_MSEA_R18_T1_MINERU_CANDIDATE_GROUP_A_LOCAL_EXTRACTION_PILOT_PLAN_AND_RECEIPT_READINESS_SELECTION_WORKER_RETURN_2026-07-03.md`.
- R18 readiness matrix: `docs/reference/CVF_MSEA_R18_T1_MINERU_CANDIDATE_GROUP_A_LOCAL_EXTRACTION_PILOT_PLAN_AND_RECEIPT_READINESS_MATRIX_2026-07-03.md`.
- Candidate Group A private intake: `docs/reference/CVF_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_LEDGER_2026-07-03.md`.
- Sample and receipt policy: `docs/reference/CVF_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_2026-07-03.md`.
- MinerU source authority: `.private_reference/source_mirrors/opendatalab__MinerU/`.

Authority boundary: if any source contradicts this packet, stop and return
`BLOCKED_WITH_REASON`. The worker may not upgrade planning language into
runtime authority.

## Required First Reads

| Source | Required action |
| --- | --- |
| active session front door named by root agent instructions | READ |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | READ |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | READ |
| `AGENT_HANDOFF_V34_2026-07-03.md` | READ |
| `docs/reference/guard_orientation/README.md` | READ |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ |
| paired GC-018 baseline | READ |
| this work order | READ |
| source files listed in Source Verification Block | READ |
| checker source listed in Checker Source Read-Ahead Block | READ |

## Agent Roles

| Role | Owner | Responsibility |
| --- | --- | --- |
| Operator | operator | owns future runtime/full-content/public decisions and any installation/model-download authorization |
| Dispatcher | dispatcher role | authors this GC-018/work order and runs pre-dispatch gates |
| Worker | delegated worker role | creates only the named worker return and companion readiness matrix, without commit |
| Reviewer/closer | reviewer/closer | reviews returned artifacts, repairs allowed-scope shape defects if needed, commits material if accepted |
| Session-sync steward | reviewer/closer once material is accepted | updates active session state once accepted material exists |

## Pre-Flight Checks

Required before worker execution:

```powershell
git rev-parse --short HEAD
git status --short
Test-Path 'docs\reviews\CVF_MSEA_R19_T1_MINERU_LOCAL_EXTRACTION_ENVIRONMENT_MODEL_LIFECYCLE_AND_SERVICE_TEARDOWN_PLANNING_WORKER_RETURN_2026-07-03.md'
Test-Path 'docs\reference\CVF_MSEA_R19_T1_MINERU_LOCAL_EXTRACTION_ENVIRONMENT_MODEL_LIFECYCLE_AND_SERVICE_TEARDOWN_READINESS_MATRIX_2026-07-03.md'
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
```

Expected result: clean worktree at execution start, planned worker outputs
absent before writing, and pre-implementation gate passing after worker output
authoring and allowed-scope repairs.

## Write Ownership

| Path family | Worker permission |
| --- | --- |
| `docs/reviews/CVF_MSEA_R19_T1_MINERU_LOCAL_EXTRACTION_ENVIRONMENT_MODEL_LIFECYCLE_AND_SERVICE_TEARDOWN_PLANNING_WORKER_RETURN_2026-07-03.md` | CREATE_ONLY_UNCOMMITTED |
| `docs/reference/CVF_MSEA_R19_T1_MINERU_LOCAL_EXTRACTION_ENVIRONMENT_MODEL_LIFECYCLE_AND_SERVICE_TEARDOWN_READINESS_MATRIX_2026-07-03.md` | CREATE_ONLY_UNCOMMITTED |
| session-state, front-door, and active-handoff surfaces | FORBIDDEN |
| `.private_reference/source_mirrors/**` | READ_ONLY |
| runtime, package, source, public-sync, Web, MCP, model-router, checker, adapter paths | FORBIDDEN |

## Execution Plan

1. Capture `executionBaseHead` and current worktree status.
2. Complete Required First Reads and checker-source read-ahead.
3. Recompute source facts from R18/R17/R12 and the pinned MinerU mirror.
4. Run only allowed read-only local inventory commands.
5. Author the worker return and companion readiness matrix.
6. Run worker-return fast gate and pre-implementation autorun.
7. Leave changes uncommitted and return the status token.

## Evidence Requirements

| Evidence | Required form |
| --- | --- |
| Base and worktree status | `executionBaseHead`, `git status --short`, and actual changed file list |
| Source verification | Source Inventory plus Source Verification Block in worker outputs |
| Local inventory | Command/result table, with no secrets or document content printed |
| Runtime non-execution | Explicit statement that no MinerU import, command, install, model download, service startup, Docker run, or extraction output occurred |
| Route decision | exactly one `selectedRouteToken` in both worker return and companion matrix |
| Gates | worker-return fast gate and pre-implementation autorun output |

## Allowed Read-Only Local Inventory

The worker may run only metadata/read-only commands needed to classify the
current host for a later runtime pilot. Allowed examples:

- `git rev-parse --short HEAD`
- `git status --short`
- `python --version`
- `where python`
- `Get-Command docker -ErrorAction SilentlyContinue`
- `Get-Command wsl -ErrorAction SilentlyContinue`
- `Get-ChildItem Env:MINERU_MODEL_SOURCE -ErrorAction SilentlyContinue`
- `Test-Path` for proposed private output roots or existing local document paths

Forbidden even for inventory:

- importing MinerU modules;
- invoking `mineru`, `mineru-api`, `mineru-router`, `mineru-gradio`, or `mineru-models-download`;
- running `pip`, `uv`, `conda`, Docker containers, WSL commands, API calls, model downloads, parser/OCR/VLM/hybrid execution, or any command that creates extraction outputs or starts local services;
- printing secret values or document body content.

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| intakeRole | dispatcher-authored private runtime-precondition planning work order |
| scope classification | bounded private planning and read-only local inventory; changed paths limited to the two worker outputs |
| workerRole | no-commit source verifier, environment/model/service readiness matrix author, and route selector |
| reviewerRole | reviewer/closer validates worker return and companion readiness matrix |
| operatorRole | owns any later runtime, installation, model-download, fuller-content, public-sync, provider, or production decision |
| route mode | MULTI_AGENT_SINGLE_ROLE |
| routeDecision | proceed with environment/model/service planning; hold all runtime execution |
| escalationCondition | source contradiction, need to run MinerU, need to install/download/start services, need to read document body content, need to quote fuller content, or need to edit forbidden paths |
| claimBoundary | role routing only; no automatic execution, provider routing, public export, or production claim |

## Route Decision Menu

Worker must select exactly one `selectedRouteToken`:

| Token | Meaning |
| --- | --- |
| OPEN_MSEA_R20_LOCAL_RUNTIME_SMOKE_PILOT_WORK_ORDER | A future local runtime smoke pilot work order can be authored, still requiring fresh runtime authorization before execution |
| OPEN_MODEL_CACHE_AND_LOCAL_SOURCE_PREP_WORK_ORDER_FIRST | Model source/cache/local-mode preparation must be planned before any runtime smoke pilot |
| HOLD_PENDING_OPERATOR_ENVIRONMENT_CHOICE | Operator must choose CPU/GPU/WSL2/Docker/local-model path before runtime can proceed |
| HOLD_RUNTIME_PENDING_SERVICE_TEARDOWN_PROOF | Temporary service detection and teardown remains insufficiently planned |
| HOLD_ALL_RUNTIME_LANES | No source-backed runtime-adjacent lane is ready |

## Required Worker Analysis

1. Re-read R18 worker return and matrix; summarize why runtime remained held.
2. Re-read R17 privacy boundary and R12 receipt/runtime gating policy.
3. Re-read pinned MinerU source mirror docs for model source, pipeline backend,
   CPU/GPU/MPS support, Docker/WSL2 boundary, local temporary service behavior,
   model-download config write-back, and local-model mode.
4. Perform read-only local inventory only from the allowed command list.
5. Produce a companion readiness matrix with:
   - environment posture;
   - model source/cache lifecycle posture;
   - local temporary service detection and teardown posture;
   - output quarantine posture;
   - privacy/redaction posture;
   - forbidden runtime action checklist;
   - selected route token and rationale.
6. Do not include document body content, raw secrets, or source file copies.

## Runtime Candidate Parking Checks

| Candidate | Required disposition for this tranche | Reason |
| --- | --- | --- |
| MinerU install or package activation | REMOVED_OR_REJECTED | package lifecycle mutation is outside this planning tranche |
| model download | REMOVED_OR_REJECTED | model lifecycle may be planned, but download is forbidden |
| `mineru` local parser run | REMOVED_OR_REJECTED | execution requires a later GC-018/work order |
| local temporary service startup | RUNTIME_CANDIDATE | source-visible behavior must be planned for detection and teardown before any later run |
| `mineru-api`, `mineru-router`, `mineru-gradio` | REMOVED_OR_REJECTED | API/router/Gradio lanes remain out of scope |
| Docker deployment | REMOVED_OR_REJECTED | Docker/WSL2 may be classified, but container execution is forbidden |
| output quarantine root | CHECKER_CANDIDATE | future receipts must prove outputs stay private and outside public-sync paths |
| service teardown checklist | CHECKER_CANDIDATE | future runtime smoke pilot should have machine-checkable stop/cleanup evidence |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher authors packet; delegated worker executes under no-commit; reviewer/closer accepts or rejects |
| phase | dispatch |
| baseHeadFor(phase) | dispatchBaseHead=add7eda4; executionBaseHead=worker captures at start; closureBaseHead=reviewer/closer sets before material commit |
| changedSetScope(phase) | dispatch may add only this work order and paired GC-018 baseline; worker may add only the named worker return and companion readiness matrix |
| traceScope(phase, actor) | dispatcher trace in this work order; worker trace in worker return and companion reference; reviewer trace in commit/steward evidence |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer/closer owns any material commit after review |
| crossBatchIsolation | clean worktree required before worker execution; worker must not touch session, handoff, runtime, public, source-mirror, package, or checker paths |
| nextMoveSurfaces | reviewer/closer updates active session state only once accepted material exists; worker must not edit session state |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_MSEA_R19_T1_MINERU_LOCAL_EXTRACTION_ENVIRONMENT_MODEL_LIFECYCLE_AND_SERVICE_TEARDOWN_PLANNING_COMPLETION_2026-07-03.md` (optional; prefer reviewer repair inside the worker return unless a separate completion artifact is necessary) |
| reviewerOwnedClosurePaths | worker return and companion reference named in Work-Order Fulfillment Manifest; session-sync surfaces only after material acceptance |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Output Checker Read-Ahead Mandate

Before writing each worker-owned output artifact, read checker source for that
file's docType, path family, and conditional content class.

| Output artifact | Required read-ahead result |
| --- | --- |
| worker return under the reviews directory | derive exact review headings, worker-return quality terms, trace labels, delta boundary labels, corpus/value/rescan tokens, and no-commit evidence shape before writing |
| companion reference under the reference directory | derive exact reference headings such as Scope / Applies To, Target / Source, source verification, corpus/value/rescan, trace, and claim-boundary labels before writing |

Literal-shape reminders: do not list required headings as backticked heading
strings before the real section; write source-not-found disposition spelling in
prose instead of the exact blocked enum in literalTokensReviewed; avoid stale
dependency wording unless a dependency-release row cites the accepted artifact
path and commit.

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| `docs/reviews/CVF_MSEA_R19_T1_MINERU_LOCAL_EXTRACTION_ENVIRONMENT_MODEL_LIFECYCLE_AND_SERVICE_TEARDOWN_PLANNING_WORKER_RETURN_2026-07-03.md` | create uncommitted worker return with `Status: COMPLETE_PENDING_REVIEW` or `Status: BLOCKED_WITH_REASON` |
| `docs/reference/CVF_MSEA_R19_T1_MINERU_LOCAL_EXTRACTION_ENVIRONMENT_MODEL_LIFECYCLE_AND_SERVICE_TEARDOWN_READINESS_MATRIX_2026-07-03.md` | create uncommitted companion readiness matrix with selected route token and claim boundary |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R19_T1_MINERU_LOCAL_EXTRACTION_ENVIRONMENT_MODEL_LIFECYCLE_AND_SERVICE_TEARDOWN_PLANNING_WORKER_RETURN_2026-07-03.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Shape-list rule: when listing required worker-output sections, write section
names without the heading prefix. Reserve actual heading syntax for real
sections so structural checkers do not treat this checklist as the artifact
section body.

## Review Gate

Reviewer/closer must run reviewer-return steward preflight before accepting the
worker return. Reviewer may repair only allowed-scope shape defects inside the
two worker-owned outputs. Any runtime, install, model download, local service,
document body, public-sync, schema/writer/checker/adapter, package, Web, MCP,
model-router, or action-authority need returns to orchestrator.

## Closure Checklist

| Item | Required disposition |
| --- | --- |
| Worker mode honored | PASS or BLOCKED with reason |
| Output manifest matches work order | PASS or BLOCKED with reason |
| Source verification recomputed | PASS or BLOCKED with reason |
| Read-only inventory stayed bounded | PASS or BLOCKED with reason |
| Route token is one of the menu tokens | PASS or BLOCKED with reason |
| Claim boundary excludes runtime execution | PASS or BLOCKED with reason |
| Reviewer-return steward preflight | PASS or BLOCKED with reason |
| Session-sync update after material acceptance | reviewer/closer-owned only |

## Operator Checkpoint

Operator checkpoint is required before any later tranche authorizes MinerU
installation, model download, local service startup, parser/OCR/VLM/hybrid/API/
router/Gradio/Docker execution, source document body read, derived-output
inclusion beyond metadata, public-sync, production claim, or workflow-chain
completion claim.

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/run_worker_return_fast_gate.py
git status --short
```

## Source-Intake Decision Packet Fields

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | source-mirror absorption follow-on planning |
| Negative search performed | Yes - see Negative Search And Collision Discipline |
| Disposition | ADAPT |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| R18 environment/model/service hold | `docs/reference/CVF_MSEA_R18_T1_MINERU_CANDIDATE_GROUP_A_LOCAL_EXTRACTION_PILOT_PLAN_AND_RECEIPT_READINESS_MATRIX_2026-07-03.md` | ENRICH_EXISTING | converts unresolved prerequisites into a worker-owned readiness matrix | execute planning only |
| MinerU model-source and local-service facts | `.private_reference/source_mirrors/opendatalab__MinerU/`; R18 matrix | ENRICH_EXISTING | adds model-source/cache/config write-back and service teardown planning surface | source-verify and classify |
| MinerU runtime execution | R12/R18 held-lane surfaces | REJECT_DIRECT_IMPORT | runtime remains unauthorized in this tranche | forbid execution |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher |
| Provider or surface | local workspace |
| Session or invocation | MSEA_R19_T1 MinerU Local Extraction Environment Model Lifecycle And Service Teardown Planning dispatch, 2026-07-03 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, `rg`, `Get-Content`, `python governance/compat/build_dispatch_packet_scaffold.py`, `apply_patch` |
| Target paths | `docs/baselines/CVF_GC018_MSEA_R19_T1_MINERU_LOCAL_EXTRACTION_ENVIRONMENT_MODEL_LIFECYCLE_AND_SERVICE_TEARDOWN_PLANNING_2026-07-03.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R19_T1_MINERU_LOCAL_EXTRACTION_ENVIRONMENT_MODEL_LIFECYCLE_AND_SERVICE_TEARDOWN_PLANNING_2026-07-03.md` |
| Allowed scope source | active next allowed move after session-sync commit `add7eda4` and accepted MSEA-R18-T1 route token |
| Before status evidence | `git rev-parse --short HEAD` returned `add7eda4`; clean worktree confirmed because `git status --short` was empty |
| After status evidence | two new dispatch artifacts pending gate confirmation |
| Diff evidence | `git diff --name-status` |
| Approval boundary | operator said continue following accepted MSEA-R18-T1 material commit; active next allowed move authorizes fresh GC-018/source-verified work order or roadmap for environment/model/local-service planning |
| Claim boundary | dispatch authoring and planning-only worker assignment |
| Agent type | dispatcher |
| Invocation ID | `msea-r19-t1-dispatch-2026-07-03` |
| Expected manifest | the two dispatch artifacts named in Target paths |
| Actual changed set | pending pre-dispatch gate confirmation |
| Manifest delta | pending pre-dispatch gate confirmation |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | MSEA-R19-T1 dispatch authoring for MinerU environment/model/service teardown planning |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, or mandatory-wrapper behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT |
| actionEvidence | CLAIM_REJECTED_NO_ACTION |
| invocationBoundary | delegated worker may perform source verification and read-only local inventory only |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized |
| claimLanguage | planning, readiness matrix, and route selection only |
| forbiddenExpansion | Do not expand into runtime/provider/live/public/package/Web/MCP/model-router behavior without a fresh source-verified authorization |

## Acceptance Criteria

| Criterion | Required evidence |
| --- | --- |
| Worker obeys no-commit mode | worker return includes `WORKER_MUST_NOT_COMMIT honored`, changed files, and actual `git status --short` |
| Worker creates only authorized outputs | worker return and companion matrix paths match Work-Order Fulfillment Manifest |
| Source facts are re-read | worker output Source Inventory lists R18/R17/R12 and MinerU source mirror docs used |
| Read-only local inventory stays bounded | worker output names commands used and confirms no install, import, model download, service start, Docker run, parser/OCR run, or extraction output |
| Route decision is explicit | companion matrix includes exactly one `selectedRouteToken` from Route Decision Menu |
| Privacy boundary is preserved | no document body content, raw secrets, original document copy/import, public-sync, or sensitive legal details in committed artifacts |
| Gates pass | worker-return fast gate and pre-implementation autorun pass before handoff or report the blocker |

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` if:

- Candidate Group A authority is missing or contradicted;
- pinned MinerU source mirror is missing or drifted beyond citation repair;
- a useful answer requires MinerU execution, install, model download, service
  startup, Docker/WSL execution, API/router/Gradio use, or document body read;
- required output artifacts cannot pass worker-return fast gate after
  allowed-scope repairs;
- local inventory would require printing secrets or sensitive document content.

## Claim Boundary

This work order authorizes only source-verified planning and read-only local
inventory for a future private MinerU runtime smoke pilot. It does not
authorize MinerU install, model download, parser/OCR/VLM/hybrid/API/router/
Gradio/Docker execution, local temporary service startup, provider/live proof,
S3/RAG, source document copy/import, fuller content quotation, schema/writer/
adapter/checker implementation, package activation, public-sync, benchmark,
document-truth, extraction-accuracy, legal advice quality, current-law
correctness, production readiness, action authority, or workflow-chain
completion claim.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: Candidate Group A source documents and this internal runtime-precondition
planning lane are authorized only for local private CVF testing. No public-sync
export is authorized.
