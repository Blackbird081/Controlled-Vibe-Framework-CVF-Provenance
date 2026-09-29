# CVF GC-018 - QM Service-Token Replay Deduplication T1

Memory class: governed-authorization-baseline

docType: baseline

Status: APPROVED_FOR_EXECUTION

Date: 2026-09-14

Batch ID: QM-SERVICE-TOKEN-REPLAY-DEDUPE-T1

dispatchBaseHead: 79927acaa1ecf6525bef92ab32a41145077bfe56

providerExecutionAuthority: FORBIDDEN

## Purpose

Authorize one bounded local implementation tranche that makes an exact valid service-token signature single-use inside one cvf-web process during the existing freshness window. Paired roadmap: `docs/roadmaps/CVF_QM_SERVICE_TOKEN_REPLAY_DEDUPLICATION_ROADMAP_2026-09-14.md`. Paired work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_QM_SERVICE_TOKEN_REPLAY_DEDUPE_T1_2026-09-14.md`.

## Scope / Target / Owner Boundary

The worker owns exactly five paths named by the work order and must not commit. Local owns review, repair within the same scope, commit and continuity. Risk ceiling is MEDIUM/R2. No durable/shared store, route production edit, dependency, provider/live call, credential use, public sync or deployment.

## Decision / Baseline

APPROVED_FOR_EXECUTION after the paired pre-dispatch gate passes. The binding baseline is the current synchronous verifier and five named current route call sites at dispatch HEAD `79927acaa1ecf6525bef92ab32a41145077bfe56`; process-local replay deduplication is the only authorized behavior delta.

## Source Verification Block

| Fact | Source file | Verified section | Disposition |
| --- | --- | --- | --- |
| M5 selection | `docs/audits/CVF_QM_RUNTIME_VALUE_R1_2026-09-14.json` | M5 and terminalValueDisposition | ACCEPT |
| Current verifier | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.ts` | `verifyServiceTokenRequest` | ACCEPT |
| Unit owner | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.test.ts` | `service-token-auth` suite | ACCEPT |
| Route consumer | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/qbs/front-door-clarification/route.ts` | `POST` verifier call | ACCEPT |
| Route test owner | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/qbs/front-door-clarification/route.test.ts` | QBS route suite | ACCEPT |

## Acceptance Criteria

First valid request passes; exact second use fails within the active window; invalid requests cannot poison the replay ledger; entries expire and capacity fails closed; no raw secret/body storage; focused tests, TypeScript and bounded benchmark pass; worker delta is exactly five paths and uncommitted.

## Checker Source Read-Ahead Block

| Field | Evidence |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | source verification, worker no-commit, return packet and closeability requirements |
| gateRunPurpose | confirm previously inspected source and contract evidence before dispatch |
| claimBoundary | authorization only; no runtime completion claim |

## Evidence / Verification

The dispatcher verified the cited source symbols, five route call sites and exact file hashes before authoring. Execution evidence must come from the worker's focused tests, TypeScript result, benchmark and fast-gate receipt; this baseline supplies no implementation proof.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`runtime-hardening`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class runtime-hardening --role dispatcher --lifecycle-phase pre-dispatch --risk-ceiling MEDIUM --json`. Returned defects: NONE_RETURNED; items=[], totalCandidates=0, truncated=false.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Local dispatcher |
| Provider or surface | internal workspace |
| Session or invocation | QM-SERVICE-TOKEN-REPLAY-DEDUPE-T1 baseline |
| Working directory | repository root |
| Command or tool surface | source reads, packet authoring and pre-dispatch gate |
| Target paths | roadmap, this baseline and paired work order |
| Allowed scope source | operator instruction on 2026-09-14 |
| Before status evidence | clean HEAD `79927acaa1ecf6525bef92ab32a41145077bfe56` |
| After status evidence | three dispatch artifacts pending |
| Diff evidence | `git status --short`; `git diff --name-status` |
| Approval boundary | bounded internal implementation only |
| Claim boundary | no implementation or deployment evidence |
| Agent type | dispatcher |
| Invocation ID | QM-SERVICE-TOKEN-REPLAY-DEDUPE-T1-baseline |
| Expected manifest | roadmap; this baseline; paired work order |
| Actual changed set | roadmap; this baseline; paired work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

GC-018 authorizes only bounded process-local replay deduplication and synthetic/local proof. It makes no distributed, live, provider, deployment, public or program-completion claim.
