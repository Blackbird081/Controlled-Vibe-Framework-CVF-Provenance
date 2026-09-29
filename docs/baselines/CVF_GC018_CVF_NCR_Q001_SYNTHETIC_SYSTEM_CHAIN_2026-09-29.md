# CVF GC-018 Baseline - Q001 Synthetic System Chain

Memory class: governed-dispatch-baseline

docType: baseline

Status: DISPATCH_READY

Batch ID: CVF-NCR-Q001-SYNTHETIC-SYSTEM-CHAIN

Dispatch base head: `8f153fd0a`

Commit mode: `WORKER_MUST_NOT_COMMIT`

providerExecutionAuthority: FORBIDDEN

## Purpose

Define the next Q001 proof on a disposable Web-to-engine-to-SQLite path. The accepted local SQLite component is a candidate, while a receipt generated through the actual Web export route and reconciled against one authoritative synthetic store remains unproven.

## Authority And Source

The active next move selects authoring this paired packet, not worker execution. `docs/reviews/CVF_CVF_NCR_Q001_POST_SQLITE_GAP_REVIEW_2026-09-29.md` prioritizes the synthetic chain. Roadmap D020, D026, D029 and Q001 preserve timeout, secret-scan and artifact-acceptance limits. `docs/reviews/CVF_Q001_ACCEPTANCE_LEDGER_PRE_DISPATCH_LEARNING_2026-09-29.md` requires the acceptance ledger before release.

## Source / Predecessor Evidence

The accepted SQLite candidate and independent probe are recorded in `docs/reviews/CVF_CVF_NCR_Q001_LOCAL_TRANSACTION_STORE_COMPLETION_2026-09-29.md`. The post-SQLite gap review separates component acceptance from the remaining Web consumer chain. No existing synthetic SQLite Web receipt is asserted by this baseline.

## Decision / Baseline / Proposed Tranche

Decision: author one proof-only, single-host synthetic integration tranche. Baseline: SQLite append, exact-ID lookup and local restore passed component review; the existing GitHub JSON ledger has not been migrated. Proposed output: an isolated reproducible probe, machine-readable observations and a worker return for independent Local review. `DISPATCH_READY` describes reviewed packet content; worker execution still requires a paired material commit, continuity release and bound pre-dispatch PASS.

## Scope / Target / Owner Boundary

Target: Web `POST /api/artifacts/export` -> Web `POST /api/governance/evaluate` -> engine `POST /api/v1/evaluate` -> SQLite block -> exact-ID and restart reconciliation. Worker may create only the named probe and evidence paths in the paired order. Local reviewer owns an independent HTTP/store probe and acceptance. The operator owns real GitHub-ledger cutover, pilot/live, deployment and cost checkpoints. External Web agents remain advisory; Local owns private source verification.

## Acceptance Invariants

1. Start a fresh engine with `CVF_GOVERNANCE_LEDGER_PATH` set to a new disposable `.sqlite` file and a separate Web process with synthetic auth/service token and explicit engine URL. Stage tracked source into a clean disposable context excluding local env files and the current JSON ledger; never start against the user's `.env.local` or current ledger.
2. A valid export response binds one generated attempt ID to the Web receipt, engine report and one hash-valid committed SQLite block. Record `authMode` and route authorization evidence separately from the governance decision.
3. Restart the engine against the same synthetic SQLite path; exact-ID lookup and chain tip/count remain stable. A limited ledger tail is not an absence oracle.
4. Simulate response loss only inside the disposable environment: route Web's engine URL through a one-shot local proxy that forwards the evaluation, lets SQLite commit, then delays/drops the response beyond the configured Web receipt timeout. Set `GOVERNANCE_ENGINE_TIMEOUT` above `CVF_GOVERNANCE_RECEIPT_TIMEOUT_MS` so the inner client cannot mask the intended boundary. The Web failure response must retain `governanceReceiptAttemptId`; reconcile that exact ID by direct SQLite lookup against the designated store, not the limited `/api/v1/ledger` tail. Record `safeToRetry=false` as the probe disposition for `FOUND`, `UNKNOWN` or failed lookup; no such Web response field is claimed. Do not replay the export automatically.
5. The HTML stays `DRAFT_UNACCEPTED` (or explicit review-required state) even when engine decision/action is `ALLOW`; receipt presence does not establish artifact approval.
6. Sign the synthetic export request using the route's timestamped service-token HMAC contract. Report denied auth, unavailable engine, malformed response and timeout as distinct observations. A Web timeout can follow a committed engine block; report ambiguity without converting it to a safe retry.
7. Local reviewer independently repeats at least one HTTP/SQLite join and one response-loss/absence discrimination without reusing the worker's assertion helper. Worker return remains pending review.

## Forbidden Scope

No real GitHub ledger mutation or migration, operator OAuth credentials, user HTML, provider model call, external runtime, public sync, deployment, pilot/live effect, automatic retry, artifact acceptance, P11 or Q001/R0 exit. No production latency or RPO/RTO claim follows from this synthetic chain.

## Evidence / Verification

The proof record must include process identity, isolated store path category (not private secret path), startup/restart outcome, attempt IDs, exact-ID lookup result, block count and tip hash before/after, hash-chain validation, receipt state, auth mode, timeout classification, retry disposition and artifact governance state. Redact tokens, cookies, OAuth callback codes, request bodies and secrets. `ALLOW` and `DRAFT_UNACCEPTED` are separate fields.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Internal governed input (no external intake) |
| Internal source | `docs/reviews/CVF_CVF_NCR_Q001_POST_SQLITE_GAP_REVIEW_2026-09-29.md` |
| Chain map route | Local system-chain proof under existing Web and engine owners |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/proof.ts`; `EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/api/server.py` |
| Disposition | INTERNAL_ONLY_NO_EXTERNAL_PROMOTION |
| Claim boundary | External advisory is not private-CVF proof. |

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work_order_authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Command: `python governance/compat/run_adif_defect_resolver.py --task-class work_order_authoring --role dispatcher --lifecycle-phase pre-dispatch --json`; result 0 items, `truncated=false`.

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_release_readiness.py`; `governance/compat/check_work_order_acceptance_ledger.py`; `governance/compat/check_high_risk_local_transaction_proof.py` |
| literalTokensReviewed | `Status`; `Batch ID`; `WORKER_MUST_NOT_COMMIT`; `acceptance-ledger-json`; `requiredGate`; `DR-07` |
| gateRunPurpose | Confirmation of source-backed held packet shape; gate output is evidence, not first discovery |
| claimBoundary | Static packet validation is not a synthetic chain receipt or dispatch authorization |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-NCR-Q001-SYNTHETIC-SYSTEM-CHAIN --title "Q001 Synthetic Web Engine SQLite System Chain" --date 2026-09-29 --base 8f153fd0a --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch with no-commit worker profile; previewed only |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | authored compact source-backed baseline and paired work order instead of retaining placeholder skeleton |
| checkerReadAheadConfirmation | read dispatch quality, release readiness, acceptance ledger, structural, review-cost and scaffold provenance checker sources |
| docOnlyNewFields | N/A with reason: no new field contract introduced |
| claimBoundary | Scaffold provenance is authoring evidence only, not runtime or worker-release proof. |

## Claim Boundary

This baseline defines proof requirements. No worker has been released, no synthetic chain has been run from this packet, and no Q001/R0, provider, pilot or public claim is closed.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
