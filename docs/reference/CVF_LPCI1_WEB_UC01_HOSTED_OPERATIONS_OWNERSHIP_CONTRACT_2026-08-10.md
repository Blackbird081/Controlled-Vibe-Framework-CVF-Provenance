# CVF LPCI1 Web UC-01 Hosted Operations Ownership Contract

Memory class: FULL_RECORD

Status: DOC_ONLY_NORMATIVE_ACCEPTED_BOUNDED

Date: 2026-08-10

docType: reference

Contract version: `cvf.lpci.hostedOperationsOwnership.v1`

## Purpose

Define the logical environment classes, accountable operational roles, custody
boundaries, separation of duties, escalation duties, and authority gates that
must be instantiated before a separately authorized LPCI UC-01 hosted smoke.

This contract names role classes, not people, accounts, cloud resources,
deployments, or current external state.

rawMemoryReleased=false

## Scope

This documentation-only contract applies to future LPCI UC-01 hosted-operation
packets that need to correlate one governed artifact, one atomic non-secret
configuration identity, distributed quota, durable audit, static health,
monitoring, smoke evidence, and rollback custody.

It does not instantiate an environment or role assignment. A future packet must
source-verify its target and record an environment-specific role-assignment
ledger before any hosted action.

## Source Lineage

| Source | Contract fact retained | Boundary |
| --- | --- | --- |
| `docs/reference/CVF_LPCI1_WEB_UC01_RELEASE_HARDENING_SPEC_2026-08-10.md` | Atomic config, distributed quota, durable minimized audit, static-health, promotion, smoke, rollback, recovery, and fresh-authority requirements. | Deterministic normative source, not hosted evidence. |
| `docs/guides/CVF_LPCI1_WEB_UC01_RELEASE_OPERATIONS_RUNBOOK.md` | Generic release-operator, platform-operations, and application-owner sequence. | Guidance only; no environment identity or execution authority. |
| `docs/reviews/CVF_LPCI1_WEB_UC01_HOSTED_RELEASE_READINESS_DISCOVERY_COMPLETION_2026-08-10.md` | Environment-specific ownership and evidence custody must be defined before hosted smoke. | Accepted repository-only gap; no external-state proof. |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/release-policy.ts` | Exact config lifecycle and safe non-secret correlation fields. | Source capability only. |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/release-health.ts` | Static readiness cannot establish external liveness or writability. | Source capability only. |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/rate-limit.ts` | Distributed Redis limiter capability and fail-closed states. | Hosted service custody remains uninstantiated. |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/storage-adapter.ts` | Distributed event-list capability, atomic append, and retention boundary. | Hosted storage custody remains uninstantiated. |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/release-audit.ts` | Minimized terminal audit projection and awaited append. | No current hosted persisted-event claim. |

## Contract Vocabulary

The following values are `DOC_ONLY_NEW` and do not claim runtime fields.

### hostedEnvironmentClass

| Value | Meaning | Authority rule |
| --- | --- | --- |
| `DEVELOPMENT` | Isolated development-class hosted target. | Cannot authorize any higher class. |
| `PREVIEW` | Ephemeral review-class hosted target. | Evidence is target-local and cannot promote itself. |
| `STAGING` | Production-like validation target. | Requires fresh staging authority and exact artifact/config binding. |
| `PRODUCTION` | User-serving production target. | Requires fresh production authority; no lower-class authority or receipt is inherited. |

These are logical classes only. They do not state that a target exists on
Vercel, Netlify, or any other platform.

### hostedOperationsRole

| Value | Accountable duty | Must not claim |
| --- | --- | --- |
| `OPERATOR_AUTHORITY_OWNER` | Issues the exact authority token and bounds target, actions, budgets, and forbidden expansion. | Technical execution or readiness merely because authority exists. |
| `RELEASE_DECISION_OWNER` | Accepts or rejects promotion/rollback decisions within operator authority. | Permission beyond the current environment packet. |
| `PLATFORM_OPERATIONS_OWNER` | Executes only authorized artifact/config promotion or restoration. | Application correctness or evidence acceptance. |
| `APPLICATION_OWNER` | Verifies route composition, static health, exact-pair behavior, and deterministic prerequisites. | Store/provider liveness from static metadata. |
| `CREDENTIAL_CUSTODIAN` | Controls secret placement and atomic rotation outside receipts; exposes only the allowed availability decision to the existing credential boundary. | Raw value, length, fingerprint, secret-store identifier, version, or secret-derived metadata. |
| `RATE_LIMIT_STORE_OWNER` | Owns distributed limiter provisioning, access, liveness, error handling, and alert routing. | Active hosted service from checked-in adapter capability alone. |
| `AUDIT_STORE_OWNER` | Owns durable append, access, retention, restore, and append-failure escalation. | Persistence or writability without separately observed evidence. |
| `MONITORING_INCIDENT_OWNER` | Owns minimized signals, thresholds, alert delivery, triage, and incident correlation. | Request content, identities, secret state, or readiness from signal absence. |
| `HOSTED_SMOKE_EXECUTOR` | Performs only the exact separately authorized smoke and writes the minimized receipt. | Self-approval, retries, or an undispatched provider call. |
| `INDEPENDENT_EVIDENCE_REVIEWER` | Recomputes receipt correlation and accepts, rejects, or invalidates evidence. | Execution authority or production release authority. |

## Environment-Specific Role Assignment Prerequisite

Before any hosted smoke packet can become executable, its reviewer-owned
assignment ledger must contain all of the following `DOC_ONLY_NEW` facts:

| Required assignment fact | Rule |
| --- | --- |
| `hostedEnvironmentClass` | Exactly one logical class. |
| target reference | One opaque, non-secret reference to the intended deployment; no credential-bearing URL or query string. |
| accountable role mapping | Exactly one accountable assignment reference for every role required by the selected smoke class. |
| escalation reference | One opaque, non-secret route for operational escalation. |
| artifact custody reference | Identifies where the immutable accepted artifact is controlled without embedding repository credentials. |
| config custody reference | Identifies the opaque bundle-custody process, never secret value or secret-derived metadata. |
| store custody references | Separately identify rate-limit and audit-store operational ownership. |
| monitoring custody reference | Identifies the owner of minimized observation and alert evidence. |
| independent reviewer | Distinct from the smoke executor. |
| authority packet | Fresh exact authority for the selected environment and action budget. |

An assignment reference may point to an operator-controlled system outside this
repository. Its presence in a future packet is evidence of declared custody,
not proof that the external owner or resource is live.

## Nine-Dimension Accountability Matrix

| Dimension | Accountable role | Responsible role | Required custody evidence before smoke | Fail-closed result |
| --- | --- | --- | --- | --- |
| configuration ownership | `RELEASE_DECISION_OWNER` | `PLATFORM_OPERATIONS_OWNER` | Exact immutable artifact digest plus opaque config bundle version, schema, and non-secret digest for one environment. | Block when correlation is absent, mixed, stale, or targets another environment. |
| credential boundary | `CREDENTIAL_CUSTODIAN` | `APPLICATION_OWNER` verifies metadata-only behavior | Secret-safe availability decision and atomic rotation disposition; no secret metadata. | Block on missing/blank/unavailable metadata or rotation-pending state. |
| rate-limit store | `RATE_LIMIT_STORE_OWNER` | `PLATFORM_OPERATIONS_OWNER` | Declared distributed store assignment and separately authorized liveness/writability evidence. | Block on memory mode, missing/invalid config, store error, or absent owner. |
| durable audit store | `AUDIT_STORE_OWNER` | `PLATFORM_OPERATIONS_OWNER` | Declared durable store assignment, 30-day retention duty, access duty, and append-evidence route. | Withhold pending answer and block on append/custody failure. |
| static and live health | `APPLICATION_OWNER` for static; `MONITORING_INCIDENT_OWNER` for external signals | `HOSTED_SMOKE_EXECUTOR` under fresh authority | `STATIC_READY` receipt plus separate bounded liveness evidence for each selected external dependency. | Never infer external status from static health. |
| artifact/promotion | `RELEASE_DECISION_OWNER` | `PLATFORM_OPERATIONS_OWNER` | Target-local immutable artifact/config correlation and fresh promotion authority. | Block target mismatch, mutable identity, missing prior rollback artifact, or inherited authority. |
| smoke | `RELEASE_DECISION_OWNER` | `HOSTED_SMOKE_EXECUTOR` | Accepted smoke plan, exact budgets, safe receipt sink, stop rules, and independent reviewer assignment. | No invocation until every prerequisite is present. |
| rollback/recovery | `RELEASE_DECISION_OWNER` | `PLATFORM_OPERATIONS_OWNER`; `APPLICATION_OWNER` verifies | Last accepted artifact/config pair, trigger, restoration plan, escalation, and post-restore deterministic verification. | Stop promotion; do not weaken authorization, quota, audit, timeout, exact-pair, or health controls. |
| monitoring | `MONITORING_INCIDENT_OWNER` | Store/application owners emit minimized signals | Named sink/route, finite signal allowlist, threshold policy, alert destination, and evidence retention/access duty. | Treat absent/stale monitoring evidence as unproven, never healthy. |

## Separation Of Duties

1. `HOSTED_SMOKE_EXECUTOR` and `INDEPENDENT_EVIDENCE_REVIEWER` must be distinct
   assignments for every environment class.
2. For `PRODUCTION`, `RELEASE_DECISION_OWNER` and
   `PLATFORM_OPERATIONS_OWNER` must be distinct assignments.
3. `CREDENTIAL_CUSTODIAN` never authors or reviews a field derived from a raw
   secret; only the existing credential boundary may resolve the secret.
4. Store owners may attest operational custody but cannot convert static source
   capability into liveness without authorized observation.
5. `OPERATOR_AUTHORITY_OWNER` may release a bounded action but cannot waive
   immutable artifact/config correlation, minimized evidence, zero automatic
   retry, or independent review.
6. An emergency role-combination request is a new operator checkpoint. It must
   be recorded before action and must not combine executor with evidence
   reviewer.

## Promotion Authority Contract

Each logical environment boundary is independent. A future packet must bind:

- the environment class and opaque target reference;
- one immutable artifact digest;
- one opaque non-secret config bundle version, schema, and digest;
- accepted policy and route-composition versions;
- deterministic test evidence and side-effect-free `STATIC_READY` evidence;
- the complete role-assignment ledger;
- an exact action/call budget and terminal stop rules; and
- a minimized evidence destination plus independent review owner.

No production authority is inherited from development, preview, or staging.
No hosted authority includes provider/live, deploy, rollback execution, public
sync, or readiness unless the exact operator token says so.

## Credential And Configuration Custody

- The three LPCI names are promoted as one atomic bundle.
- Only opaque non-secret bundle/schema/digest correlation enters receipts.
- The raw key and all secret-derived metadata are excluded from repository,
  logs, metrics, UI, smoke receipts, and reviewer evidence.
- Rotation creates and validates a complete candidate bundle, then atomically
  promotes it or retains/restores the complete prior bundle.
- A partial, mixed-version, invalid, or rotation-pending bundle blocks the
  provider lane.
- A credential-presence check is itself outside this documentation tranche and
  requires the authority of the later execution packet.

## Store, Audit, And Monitoring Custody

The rate-limit and audit stores have separate accountable roles even if a
single platform service later implements both. Their evidence and failure
routes remain distinct.

Monitoring may use only counts, bounded status values, coarse latency buckets,
server-generated correlation identifiers, exact provider/model identifiers
when an attempt was authorized, and safe diagnostic codes. It must exclude raw
query, prompt, answer, matched paths, bodies, headers, cookies, raw actor or
corpus identity, endpoint/config values, and every secret or secret-derived
field.

Signal absence, static capability, or checked-in platform configuration cannot
be treated as liveness, writability, successful deployment, or readiness.

## Rollback, Recovery, And Escalation

Rollback triggers remain: non-ready dependency, authorization bypass,
distributed quota bypass/unavailability, durable append failure, exact-pair
mismatch, provider timeout/error threshold breach, or authorized smoke
mismatch.

The `RELEASE_DECISION_OWNER` stops promotion and selects the last accepted
artifact/config pair. `PLATFORM_OPERATIONS_OWNER` restores that pair.
`APPLICATION_OWNER` reruns deterministic verification and static health.
Store owners verify only their separately authorized operational evidence.
`MONITORING_INCIDENT_OWNER` correlates minimized signals and escalates.

Recovery repairs one governed owner, preserves historical receipts, obtains
fresh authority, and creates a new receipt. A failed or invalidated receipt is
never overwritten, upgraded, or reused as current proof.

## Verification Before Hosted-Smoke Dispatch

A future dispatcher must source-verify the target-specific role assignments,
artifact/config correlation, selected external dependencies, evidence sink,
call budgets, freshness window, and stop conditions. Dispatch fails if any role
is unnamed, any assignment is ambiguous, executor and reviewer collide, or the
packet needs a secret value to explain its evidence.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this normative contract is private provenance documentation and no
public-sync authority exists.

## Claim Boundary

This contract defines logical classes and accountable duties only. It does not
claim an actual owner assignment, target, credential, store, monitor, artifact,
deployment, liveness result, hosted smoke, rollback execution, production
operation, release readiness, reviewer acceptance, or public export.
