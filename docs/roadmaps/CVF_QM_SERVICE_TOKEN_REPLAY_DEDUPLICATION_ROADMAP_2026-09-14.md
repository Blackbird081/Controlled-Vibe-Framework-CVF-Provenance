# CVF QM Service-Token Replay Deduplication Roadmap

Memory class: governed-roadmap

docType: roadmap

Status: T1_DISPATCH_READY

Date: 2026-09-14

Roadmap ID: QM-SERVICE-TOKEN-REPLAY-DEDUPE

## Authorization And Decision

The operator assigned Local as orchestrator/reviewer and will relay the bounded implementation packet to an internal Claude worker. Local selects QM R1 M5 after OUTPUT-REDACTION-T1 closure because M5 has a named current CVF verifier and five current route call sites. M4 token rotation/claims remains separate and demand-gated.

## Purpose

Prevent an exact valid signed service-token request from being accepted more than once inside one cvf-web process during the existing five-minute signature window. Preserve the first valid request, invalid-request behavior and current HMAC/timestamp checks. Make the process-local boundary explicit; do not claim cross-process, serverless-isolate or distributed replay protection.

## Scope

T1 is one bounded implementation/review tranche. It may add a bounded process-local replay ledger to the existing service-token verifier, focused unit and QBS route integration tests, a local synthetic benchmark and a worker return. The implementation must use CVF-native code and existing dependencies only.

## Non-Goals

- No M4 key rotation, `kid`, audience, actor-scope or multi-token work.
- No database, Redis, Upstash, durable store, new dependency or cross-instance claim.
- No signature-protocol migration, path/method binding change or auth-stack rewrite.
- No real token, ambient credential, provider/live call, network request, public sync or deployment.
- No upstream QM execution or source copying.

## Evidence Baseline

| Evidence | Current fact | Disposition |
| --- | --- | --- |
| `docs/audits/CVF_QM_RUNTIME_VALUE_R1_2026-09-14.json` | M5 is `ADAPT_CANDIDATE`; Local may authorize bounded replay dedupe | ACCEPT |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.ts` | verifier accepts a valid signature solely by token, timestamp window, body and signature | ACCEPT |
| current route source | five API routes call `verifyServiceTokenRequest` | ACCEPT |
| `docs/reviews/CVF_OUTPUT-REDACTION-T1_COMPLETION_2026-09-14.md` | next capability must have a named current consumer | ACCEPT |

## Design Control Gate

| Control | Binding decision |
| --- | --- |
| Replay identity | non-secret digest derived from the already-validated token identity plus timestamp and signature; never store raw token/body |
| Consume order | validate token, timestamp and HMAC first; only a cryptographically valid request may consume a replay key |
| Duplicate outcome | first valid request passes; an exact duplicate inside the active window fails closed |
| Capacity | fixed positive maximum; expired entries pruned; capacity exhaustion fails closed and is tested |
| Time | injected `now` remains authoritative in tests; no timer/daemon/background task |
| Isolation | process-local only; reset/test seam must not weaken production default |
| Compatibility | invalid/missing/stale requests retain false result; different valid signed requests remain independent |
| Performance | measure baseline and changed verifier with fixed synthetic inputs; report median/p95 and sample count |

## Work Plan

| Tranche | Action | Owner | Terminal output |
| --- | --- | --- | --- |
| T1 | implement bounded process-local replay dedupe and proof | INTERNAL_AGENT worker | `COMPLETE_PENDING_REVIEW` worker return |
| T1 review | evaluate returned evidence, repair only in-scope defects, commit material then continuity | Local reviewer/closer | bounded acceptance or blocking findings |

## Invocation And Review Budget

One initial worker return and at most one consolidated repair generation. Reviewer consumes returned evidence and samples only security boundary, M5 behavior, capacity, latency and changed-set integrity. No broad cvf-web rerun unless a named dependency contradiction requires it. Provider/live invocation ceiling is zero.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| INTERNAL_AGENT | work order plus five worker-owned paths | local reversible code/test work; worker must not commit | exact manifest, tests, benchmark, return | same workspace; no adapter | CONTRACT_ONLY |
| EXTERNAL_AGENT_CLI_MCP | none | no external execution or provider authority | N/A | no adapter | N/A_WITH_REASON |

## Acceptance Criteria

1. The same valid signed tuple is accepted once and rejected on immediate replay through `verifyServiceTokenRequest`.
2. The QBS route returns success on first use and 401 on the exact replay without running a real server.
3. Invalid token/signature, stale timestamp and malformed timestamp do not reserve a replay key.
4. Different body, timestamp, token or signature identity does not collide when otherwise valid.
5. Raw tokens and request bodies are not stored or emitted; only bounded non-secret identity material is retained.
6. Expiry pruning and fixed-capacity fail-closed behavior are deterministic and tested.
7. Existing focused service-token and QBS tests plus TypeScript pass.
8. Added verifier median is at most 0.10 ms and p95 at most 0.25 ms for the bounded synthetic fixture; no universal SLA claim.
9. Worker changes exactly five owned paths and makes zero commits.

## Verification And Evidence Plan

Run focused Vitest files and `npm run check` from cvf-web. Run the synthetic benchmark with installed tooling only. Run pre-implementation and worker-return fast gates from repository root. Preserve failed-run history and exact exit codes. No release bundle is required because the tranche makes no provider/live governance claim.

## Stop Conditions

Stop and return `BLOCKED_WITH_REASON` if a correct solution requires durable/shared storage, signature protocol migration, route production edits, new dependencies, credentials, network/provider calls, or any path outside the five-path manifest. Do not silently downgrade replay protection or widen to M4.

## Epistemic Process Block

### Expected Result / Prediction

A bounded process-local replay ledger after successful HMAC validation should reject an exact duplicate without changing first-use or invalid-request behavior and with negligible local latency.

### Evidence Comparison

Current source contains a five-minute freshness check but no nonce or consumed-signature ledger. M5 is already classified as an adaptation candidate and the verifier has five named current route consumers.

### Contradiction Or Gap Disposition

Distributed replay protection remains unresolved by design. T1 must state that limitation rather than treating a process-local map as deployment-wide protection.

### Claim Update

Roadmap selection authorizes bounded local implementation only; it proves no completed behavior, deployment or cross-instance protection.

## Checker Source Read-Ahead Block

| Field | Evidence |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_agent_operation_trace.py` |
| literalTokensReviewed | dispatch prompt placement, exact paths, closeability graph, INITIAL convergence, returned evidence review boundary |
| gateRunPurpose | confirm already-inspected roadmap-derived dispatch evidence before worker handoff |
| claimBoundary | roadmap and dispatch evidence only |

## External Repository Absorption Entry Control

NOT_APPLICABLE_WITH_REASON: this roadmap reuses the already accepted and pinned QM R1 M5 record; it performs no new repository intake or corpus scan.

## Mandatory Blind-Spot Control Block

NOT_APPLICABLE_WITH_REASON: one accepted mechanism and named current CVF consumer are used; no completeness or rescan claim is made.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | QM R1 M5 -> Local current-consumer verification -> bounded CVF-native implementation |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.ts` |
| Disposition | ADAPT one mechanism without source copy |
| Claim boundary | no new source acquisition or repository-complete claim |

## External/Local Coordination Binding

```json
{
  "contractId": "cvf.external-local-absorption-coordination@1",
  "invariants": {
    "externalRole": "ADVISORY_RESEARCH_AND_PATTERN_MAPPING",
    "externalContext": "PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ",
    "localRole": "SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION",
    "finalDecisionOwner": "LOCAL",
    "localCoverageBasis": "SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST",
    "externalEvidenceAuthority": "INPUT_NOT_PRIVATE_CVF_PROOF"
  },
  "contractSha256": "92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c",
  "parentArtifact": "docs/reviews/CVF_EXTERNAL_LOCAL_ABSORPTION_PROGRAM_CONTINUITY_HARDENING_2026-09-13.md"
}
```

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Local orchestrator/reviewer |
| Provider or surface | internal workspace |
| Session or invocation | QM-SERVICE-TOKEN-REPLAY-DEDUPE dispatch authoring |
| Working directory | repository root |
| Command or tool surface | startup reads, current source/consumer inspection, governed artifact authoring, pre-dispatch gates |
| Target paths | this roadmap; paired baseline; paired work order |
| Allowed scope source | operator instruction on 2026-09-14 |
| Before status evidence | clean worktree at HEAD `79927acaa1ecf6525bef92ab32a41145077bfe56` |
| After status evidence | three dispatch artifacts pending before dispatch validation |
| Diff evidence | `git status --short`; `git diff --name-status` |
| Approval boundary | dispatch authoring only; worker implementation remains pending |
| Claim boundary | no implementation result |
| Agent type | dispatcher |
| Invocation ID | QM-SERVICE-TOKEN-REPLAY-DEDUPE-dispatch |
| Expected manifest | this roadmap; paired baseline; paired work order |
| Actual changed set | this roadmap; paired baseline; paired work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Next Allowed Move

After pre-dispatch PASS and dispatch/continuity commits, the internal worker executes only the paired T1 work order and returns uncommitted evidence to Local.

## Claim Boundary

This roadmap selects process-local replay deduplication for one existing verifier. It does not claim completion, distributed protection, live deployment, provider behavior, public export or completion of QM or the three-repository program.
