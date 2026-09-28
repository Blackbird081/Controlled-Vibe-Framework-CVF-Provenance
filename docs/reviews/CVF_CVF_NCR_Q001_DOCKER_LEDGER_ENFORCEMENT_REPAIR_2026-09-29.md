# CVF NCR Q001 Docker Ledger And Enforcement Repair

Memory class: governed-review

docType: review

Status: BOUNDED_LOCAL_REPAIR_OBSERVED

Date: 2026-09-29

Decision owner: Local reviewer/closer under the operator's instruction to resolve the Q001 Docker findings. External Web remains advisory and was not invoked.

executionBaseHead: `c8ca57360`

## Purpose

Resolve the two contradictions recorded in `docs/reviews/CVF_CVF_NCR_Q001_DOCKER_RECEIPT_WIRING_EVIDENCE_2026-09-28.md`: the object-shaped tracked ledger seed conflicts with the running list-based ledger, and a nested `ALLOW` decision was labelled `LOG_ONLY` by enforcement. This packet updates the bounded Q001 evidence; it does not close the pilot or accept the HTML artifact.

## Target / Source

Source changes are confined to `EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/adapters/cvf_enforcement_adapter.py`, `api/server.py`, `ledger_layer/immutable_ledger.py`, their focused tests, and the NCR roadmap. Role: shared-workspace INTERNAL_AGENT Local implementer/reviewer. Phase: Q001 local Docker corrective run. Final technical decision owner: Local. No external repository or runtime was absorbed.

## Scope / Methodology

The enforcement adapter now reads the REST report's `decision_analysis.final_decision`, retains the flat legacy form, and maps a conflicting flat/nested pair to `UNKNOWN`/`LOG_ONLY` rather than promoting either side to `ALLOW`. The server binds one ledger instance to `CVF_GOVERNANCE_LEDGER_PATH` for both evaluate and `/api/v1/ledger`. `ImmutableLedger` rejects a non-list JSON ledger at initialization without modifying it. The tracked object-shaped seed remains untouched; no migration of its contents is claimed.

The prior tracked-source-only temporary Docker context was updated with these three source files. The engine image **included** the object-shaped seed. A separate named Docker volume mounted at `/var/lib/cvf` supplied `CVF_GOVERNANCE_LEDGER_PATH=/var/lib/cvf/ledger_chain.json`; the engine created a new list there. Web and engine shared the same internal Docker network, with no host port published. The web image and synthetic development mock-login/service-token HTTP probe were reused from the prior Q001 run. No user document or provider credential entered the probe.

## Findings / Position

| Finding | Observed evidence | Disposition |
|---|---|---|
| Ledger schema boundary | Image's tracked `ledger_chain.json` was confirmed `dict`; the runtime volume ledger was a list. Unit test confirms an incompatible existing file raises at initialization and remains unchanged. | SOURCE_REPAIRED_BOUNDED; seed migration remains outside this change |
| Decision/enforcement consistency | Real `/api/governance/evaluate` returned HTTP 200 with `cvf_enforcement.action=ALLOW` for the synthetic `ALLOW` decision. Nested ALLOW, DENY, REVIEW and flat/nested contradiction tests passed. | SOURCE_REPAIRED_BOUNDED; no artifact approval inferred |
| Receipt and persistence | Real export returned HTTP 200, `success=true`, service-token auth, receipt `ALLOW/R0`, verification 8/8 and `DRAFT_UNACCEPTED`. Receipt ID matched the first volume ledger event's request ID. Two-block chain validated before and after engine restart; `/api/v1/ledger` returned both blocks from the configured path. | LOCAL_HTTP_AND_SINGLE_RESTART_OBSERVED |

Engine image digest: `sha256:9763611fe69dbcf6e4f2f309f897d1139a0ac088a6d0a4b25c2c0fa0b7cb91cd`. Receipt ID: `artifact-proof-q001-docker-1790615520207-1790615521713`; matching ledger block hash: `ab2d1b0af178075a8ff6d87626de3a71a85813e8e09c91ef6f1538fd6524e003`. Two-block post-restart tip hash: `4b9de1aefb99d643e9b3b97bb760b40eb5c9459a98a0774fff53d70ef9a0559f`. The additional block came from the enforcement-shape probe. One export took 1,786 ms in development mode; it is not a latency bound.

Python Governance Engine suite passed 152/152. The unchanged web export route's focused suite passed 27/27. `git diff --check` passed. The local HTTP run used real web and engine services and did not intercept fetch. The tests alone are not proof of provider governance.

## Risk / Corrective Action

The volume verifies survival of one container restart, not backup, restore, RPO/RTO, multi-writer safety or hosted persistence. The tracked seed remains a distinct historical/object schema and must not be treated as a live block-chain ledger. A deployment profile must bind a writable isolated ledger path and specify lifecycle/retention before promotion. There was no real browser UI walkthrough, production auth, broad P08 secret scan, Netlify deployment, real-provider API call, cost budget, latency distribution or downstream HTML acceptance. Q001 and R0 exit remain open; P11 and external runtimes remain parked.

## Decision / Recommendation / Disposition

Accept the source correction and bounded local HTTP/volume-restart observation. Keep the HTML artifact `DRAFT_UNACCEPTED`. Continue Q001 with a real UI/profile and separately authorized effect and live-provider proof under its governing baseline; do not infer pilot closure or public export from this packet.

## Epistemic Process Block

### Expected Result / Prediction

The isolated runtime ledger would allow engine startup with the incompatible seed still in the image; a nested `ALLOW` report would produce enforcement `ALLOW`; a volume restart would retain its chain.

### Evidence Comparison

The seed was present as a dict, but the API used its configured volume path. The real evaluate and export HTTP responses showed matching ALLOW decision/action and draft receipt. Ledger validation passed before and after restart. The one-run latency and restart cannot establish deployment durability or cost.

### Contradiction Or Gap Disposition

The two D017 contradictions are corrected in source and bounded local proof. Seed migration, retention policy, backup/restore and higher-level Q001 effect gates remain separate open items.

### Claim Update

Q001 now has consistent decision/enforcement and an isolated ledger path demonstrated on a local Docker network. It has no artifact-acceptance, hosted, provider-live or production-readiness proof from this run.

## Finding-To-Governance Learning Disposition

| Defect class | Learning lane | Disposition | Next control action |
|---|---|---|---|
| RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | DESIGN_REVIEW_REQUIRED | Bind the writable ledger path and persistence lifecycle in the deployment profile; retain nested decision/enforcement mismatch cases in the engine test suite. |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | `Target / Source`, `Scope / Methodology`, `Findings / Position`, `Risk / Corrective Action`, `Decision / Recommendation / Disposition`, `Evidence Comparison`, `Contradiction Or Gap Disposition`, `Claim Update`, `Public Export Disposition` |
| gateRunPurpose | Confirm the corrective packet shape and local evidence after source read-ahead. |
| claimBoundary | Checker compliance does not promote a synthetic Docker test to provider-live or artifact-acceptance proof. |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local single agent in implementer and reviewer roles |
| Provider or surface | Private CVF workspace and local Docker Desktop |
| Session or invocation | Q001 ledger/enforcement correction, 2026-09-29 |
| Working directory | Repository root and isolated Windows Temp build context |
| Command or tool surface | Source edit, Docker build/run/exec/restart, Node HTTP probe, Python ledger validation and pytest, Vitest |
| Target paths | Three engine source files, two engine test files, NCR roadmap and this review |
| Allowed scope source | Operator instruction to resolve the known Q001 Docker findings |
| Before status evidence | `c8ca57360` with clean starting worktree; D017 contradictions open |
| After status evidence | Source/tests and review pending material commit; 152/152 engine tests, 27/27 web tests and local HTTP/ledger checks passed |
| Diff evidence | Working-tree Git diff and Docker image digest above |
| Approval boundary | Synthetic local path only; no provider/live, public write, deployment or pilot acceptance |
| Claim boundary | Bounded ledger-path and decision/action correction only |
| Agent type | Codex (shared-workspace INTERNAL_AGENT) |
| Invocation ID | q001-docker-ledger-enforcement-20260929 |
| Expected manifest | Three engine source files; two engine test files; this review; NCR roadmap |
| Actual changed set | Three engine source files; two engine test files; this review; NCR roadmap |
| Manifest delta | MATCH |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | Q001 local Docker ledger/enforcement correction |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE: real local HTTP and one volume restart |
| receiptEvidence | CVF_RECEIPT_PRESENT: response receipt ID equals the first volume ledger event request ID |
| actionEvidence | ACTION_EVIDENCE_PRESENT: enforcement ALLOW matched decision ALLOW; two ledger blocks and hash links validated after restart |
| invocationBoundary | two isolated Docker containers, development mock login, synthetic request and no external provider |
| interceptionBoundary | no HTTP fetch interception in final Docker probe; focused fixtures are separate |
| claimLanguage | local correction observed; approval, acceptance and live governance unclaimed |
| forbiddenExpansion | no P11, external runtime, Netlify, public sync, production readiness or live-provider inference |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

This private packet records a bounded local correction. An `ALLOW` engine action is not approval of the HTML artifact, which remains draft and unaccepted.
