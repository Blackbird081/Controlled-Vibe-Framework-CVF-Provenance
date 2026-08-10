# CVF LPCI1 Web UC-01 Hosted Smoke Evidence Contract

Memory class: FULL_RECORD

Status: DOC_ONLY_NORMATIVE_ACCEPTED_BOUNDED

Date: 2026-08-10

docType: reference

hostedSmokeReceiptVersion: `cvf.lpci.hostedSmokeReceipt.v1`

## Purpose

Define the minimized, secret-safe receipt, correlation, stop, freshness,
review, and invalidation contract for a future separately authorized LPCI
UC-01 hosted smoke.

This document creates no receipt and grants no execution authority.

rawMemoryReleased=false

## Scope

The contract applies only after the hosted operations ownership contract is
independently accepted and a fresh packet names one logical environment,
opaque target, accountable role ledger, exact action budget, and proof class.

The receipt is evidence about one bounded observation. It is not a release
decision, deployment authorization, health certificate, or reusable authority.

## Source Lineage

| Source | Evidence rule retained | Boundary |
| --- | --- | --- |
| `docs/reference/CVF_LPCI1_WEB_UC01_RELEASE_HARDENING_SPEC_2026-08-10.md` | Immutable artifact/config correlation, static/external-health separation, one provider attempt, zero automatic retry, minimized audit, and fresh lifecycle authority. | Deterministic contract only. |
| `docs/guides/CVF_LPCI1_WEB_UC01_RELEASE_OPERATIONS_RUNBOOK.md` | Hosted/live smoke needs separate authority; rollback/recovery creates a new receipt. | No current hosted action. |
| `docs/reference/CVF_LPCI1_WEB_UC01_HOSTED_OPERATIONS_OWNERSHIP_CONTRACT_2026-08-10.md` | Logical environments, accountable roles, custody, and independent review. | Accepted bounded; does not instantiate owners. |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/release-health.ts` | `STATIC_READY` leaves external status unproven. | Receipt must not convert static metadata into liveness. |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/release-audit.ts` | Finite terminal audit fields and safe correlation pattern. | Hosted smoke receipt is `DOC_ONLY_NEW`, not a runtime event already emitted. |

## Proof Classes

The following values are `DOC_ONLY_NEW`.

| Proof class | Permitted observation | Provider call rule | Claim ceiling |
| --- | --- | --- | --- |
| `HOSTED_CONTROL_PLANE` | One bounded target observation of selected route, distributed quota, durable audit, static metadata, and monitoring paths named by the packet. | `providerCallBudget=0`; provider entry is forbidden. | Selected hosted control evidence only. |
| `HOSTED_PROVIDER_LIVE_COMPOSED` | The selected hosted controls plus one bounded real-provider attempt. | Requires a separate explicit live-provider authority in the same packet; at most one provider entry and zero retry. | One observed route/provider composition, not production readiness. |

A future work order must source-verify an executable, fail-closed method for the
selected proof class. This contract does not claim that a current route can
exercise every control with one invocation or without source changes.

## Receipt Schema

Every field below is `DOC_ONLY_NEW` unless its value is a cited current-source
enum or version. Optional means absent unless the selected proof class actually
observed the field.

### Identity And Correlation Fields

| Field | Requirement |
| --- | --- |
| `hostedSmokeReceiptVersion` | Exact literal `cvf.lpci.hostedSmokeReceipt.v1`. |
| `receiptId` | Server/tool-generated opaque identifier; unique to one attempt. |
| `authorityPacketRef` | Immutable reference to the exact fresh execution packet. |
| `hostedEnvironmentClass` | One accepted logical environment value. |
| `targetDeploymentRef` | Opaque non-secret target identity; no credential-bearing URL or query. |
| `roleAssignmentLedgerRef` | Immutable reference to the accepted environment-specific role ledger. |
| `proofClass` | Exactly one proof class above. |
| `observedAt` | UTC observation time. |
| `freshnessDeadline` | UTC deadline fixed by the fresh packet before execution. |

### Artifact And Configuration Correlation

| Field | Requirement |
| --- | --- |
| `immutableArtifactDigest` | Digest of the exact accepted deployed artifact. |
| `configBundleVersion` | Opaque non-secret atomic bundle version. |
| `configSchemaVersion` | Accepted non-secret schema version. |
| `configDigest` | Digest over schema plus non-secret model/endpoint contract only. |
| `authPolicyVersion` | Accepted authorization policy version. |
| `routeCompositionVersion` | Accepted route-composition version. |
| `staticHealthState` | Exact observed static state; `STATIC_READY` is required before external observation but never proves it. |

### Bounded Action Counts

| Field | Allowed value |
| --- | --- |
| `routeInvocationBudget` / `routeInvocationCount` | Packet-fixed `0` or `1`; actual cannot exceed budget. |
| `rateLimitStoreProbeBudget` / `rateLimitStoreProbeCount` | Packet-fixed `0` or `1`; actual cannot exceed budget. |
| `auditStoreProbeBudget` / `auditStoreProbeCount` | Packet-fixed `0` or `1`; actual cannot exceed budget. |
| `providerCallBudget` / `providerCallCount` | `0` for control-plane proof; packet-fixed `1` only with explicit live-provider authority. |
| `retryBudget` / `retryCount` | Both must be `0`. |
| `rollbackActionCount` | Must be `0`; smoke cannot execute rollback. |

An invocation that enters more than one selected surface must still increment
each applicable actual count. A timeout, partial response, failed append, or
unclear result consumes the attempt and cannot be rerun under the same packet.

### Observation Results

| Field | Allowed minimized value |
| --- | --- |
| `authorizationResult` | `PASS`, `FAIL_CLOSED`, `NOT_SELECTED`, or `NOT_OBSERVED`. |
| `distributedQuotaResult` | `PASS`, `FAIL_CLOSED`, `NOT_SELECTED`, or `NOT_OBSERVED`. |
| `durableAuditResult` | `PASS`, `FAIL_CLOSED`, `NOT_SELECTED`, or `NOT_OBSERVED`. |
| `providerResult` | `PASS`, `FAIL_CLOSED`, `NOT_AUTHORIZED`, or `NOT_OBSERVED`. |
| `monitoringResult` | `PASS`, `FAIL_CLOSED`, `NOT_SELECTED`, or `NOT_OBSERVED`. |
| `diagnosticClass` | One finite secret-safe class source-verified by the fresh packet. |
| `httpStatusClass` | Optional bounded class such as `2XX`, `4XX`, `5XX`, or `NO_HTTP_RESULT`; no body. |
| `latencyBucket` | Optional coarse bucket; no raw timeline or provider telemetry. |
| `terminalDisposition` | `PASS_BOUNDED`, `FAIL_CLOSED`, `BLOCKED_PRECALL`, or `INVALIDATED`. |

`PASS_BOUNDED` is allowed only when every selected observation is `PASS`, every
count is within budget, correlation is exact, and durable evidence append is
confirmed. An unselected dimension remains `NOT_SELECTED`; it is never silently
treated as passing.

## Required Receipt Correlations

The future executor must establish all of these equalities without exposing a
secret:

1. Authority environment class equals receipt environment class.
2. Authority target reference equals receipt target reference.
3. Deployed artifact digest equals the accepted artifact digest.
4. Active opaque config bundle/schema/digest equals the packet correlation.
5. Accepted auth-policy and route-composition versions equal observed static
   metadata.
6. Role ledger authorizes the exact executor and names a distinct reviewer.
7. Actual counts do not exceed packet budgets and retry count is zero.
8. Provider/model result and durable event correlation equal the configured
   exact pair when provider execution was explicitly authorized.
9. The minimized receipt is durably appended before it can be presented for
   independent review.

A mismatch yields `FAIL_CLOSED` or `BLOCKED_PRECALL`, never a partial pass.

## Prohibited Receipt And Diagnostic Content

The receipt, its logs, metrics, screenshots, command output, and review packet
must not include:

- raw or encoded credential values;
- secret length, prefix, suffix, fingerprint, secret-store identifier, secret
  version, or secret-derived rotation metadata;
- authorization headers, cookies, tokens, signatures, or session identifiers;
- raw query, prompt, answer, evidence projection, matched paths, request body,
  response body, or provider body;
- raw actor identity, raw corpus identity, IP address, stack trace, or internal
  filesystem path;
- endpoint/config values, Redis credentials, cloud account/resource metadata,
  dashboards, or private operator data; or
- a claim of deployment, production health, readiness, or public availability.

## Pre-Call Stop Rules

The future executor records `BLOCKED_PRECALL` and makes zero route, store, and
provider calls when any of these is missing or inconsistent:

- fresh exact operator authority;
- accepted ownership and smoke-evidence contracts;
- one logical environment and opaque target reference;
- complete role ledger with distinct executor and reviewer;
- accepted immutable artifact/config correlation;
- selected proof class and exact nonnegative budgets;
- safe durable receipt destination and independent review route;
- static prerequisites required by the selected packet;
- source-verified invocation method and diagnostic mapping; or
- a secret-safe execution environment whose outputs obey the prohibited-field
  boundary.

Provider entry is additionally blocked unless the packet explicitly grants
live-provider authority and sets `providerCallBudget=1`.

## In-Run Stop Rules

1. Zero automatic retry, hedge, provider fallback, model fallback, or rerun.
2. Stop after the first failed, partial, timed-out, unclear, or budget-consuming
   attempt and write one sanitized terminal diagnostic.
3. Stop before provider entry on failed authorization, quota, config, static
   health, target correlation, or preceding selected control.
4. On durable append failure, withhold any pending answer, classify the receipt
   `FAIL_CLOSED`, and do not retry the provider.
5. On exact provider/model mismatch, classify `FAIL_CLOSED` and retain no raw
   response content.
6. Smoke never executes deploy, promotion, rollback, migration, config rotation,
   secret mutation, or public action.
7. A second attempt requires a new diagnostic-backed authority packet; this
   receipt does not grant it.

## Freshness And Invalidation

A receipt is current only before `freshnessDeadline` and only for the exact
tuple of environment class, target reference, artifact digest, config bundle
version/schema/digest, policy version, route-composition version, role ledger,
proof class, and authority packet.

It becomes historical and `INVALIDATED` immediately when any tuple member
changes, the deadline passes, the target is replaced, an accountable role
assignment changes, a selected dependency reports a later failure, rollback or
recovery begins, the receipt is found incomplete, or the independent reviewer
rejects a correlation.

Evidence from development, preview, or staging cannot satisfy production. A
receipt cannot be refreshed by editing timestamps, copying fields, backfilling
response-local evidence, or attaching a later authority. Recovery requires a
new packet and a new receipt.

## Independent Review Contract

The `INDEPENDENT_EVIDENCE_REVIEWER` must recompute field presence, enum values,
correlation, count budgets, prohibited-field absence, freshness, terminal
diagnostic consistency, and the executor/reviewer separation. Review has one of
three dispositions:

- `ACCEPT_BOUNDED_EVIDENCE`: selected observations are supported, current, and
  within the exact claim ceiling;
- `REJECT_EVIDENCE`: malformed, overbroad, unsafe, contradictory, stale, or
  unsupported evidence; or
- `RETURN_FOR_NEW_AUTHORITY`: a further observation is needed, but no rerun is
  authorized by the existing packet.

Reviewer acceptance does not promote, deploy, rollback, release, publish, or
declare readiness.

## Verification Before Dispatch

A future dispatcher must source-verify the current callable method, target
binding, exact count model, current diagnostics, receipt sink, and every
selected dependency. It must run the required dispatch gate and reject any
packet that uses this schema as a substitute for actual owner assignments or
fresh authority.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this receipt contract is private provenance documentation and no
public-sync authority exists.

## Claim Boundary

This document defines a future minimized evidence shape and its fail-closed
rules only. It does not prove current target existence, owner assignment,
credential presence, store/provider liveness, deployed artifact identity,
hosted smoke, rollback, monitoring operation, production behavior, release
readiness, reviewer acceptance, or public export.
