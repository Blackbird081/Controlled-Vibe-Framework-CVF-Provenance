# CVF Work Order P3 Hosted Protected Workflow Proof Rerun

Memory class: FULL_RECORD

Status: AUTHORIZED_WORK_ORDER

docType: work_order

Date: 2026-05-23

---

## Purpose

Execute the GC-018-authorized P3 hosted proof rerun with one concrete
trusted-form payload that should avoid the previous `CLARIFY` gate.

---

## Scope / Target / Owner Boundary

Target:

- `https://vibcode.netlify.app/api/execute`

Protected workflow:

- signed service-token `/api/execute`.

Owner boundary:

- proof execution and evidence filing only;
- no application code edits;
- no deployment edits;
- no provider/runtime semantics;
- no public-sync.

---

## Authority Chain

- GC-018:
  `docs/baselines/CVF_GC018_P3_HOSTED_PROTECTED_WORKFLOW_PROOF_RERUN_2026-05-23.md`
- Prior blocker:
  `docs/reviews/CVF_P3_HOSTED_PROTECTED_WORKFLOW_PROOF_BLOCKER_REVIEW_2026-05-23.md`

---

## Agent Roles

Codex performs the bounded workflow roles:

- Orchestrator: keep the proof to one named hosted endpoint, one protected
  workflow, and one concrete payload.
- Implementer: run the signed live request.
- Auditor: record sanitized evidence and no-secret handling.
- Reviewer: reject hosted-readiness, production-readiness, broad provider, or
  freeze-release claims.

---

## Required First Reads

Read before execution:

- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `docs/reviews/CVF_P3_HOSTED_PROTECTED_WORKFLOW_PROOF_BLOCKER_REVIEW_2026-05-23.md`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates/business.ts`

---

## Allowed Scope

Allowed:

- load local env values into process memory without printing them;
- sign one request body with the configured service token;
- POST one concrete `strategy_analysis` payload to hosted `/api/execute`;
- record sanitized response facts;
- file completion or blocker evidence;
- update session continuity after proof.

Forbidden:

- print or commit raw API keys, service tokens, NextAuth secrets, or signed
  request headers;
- copy ignored env files into evidence;
- change source, route behavior, provider adapters, auth semantics, deployment
  config, or public-sync content;
- claim hosted SaaS readiness, production readiness, uptime, or broad hosted
  readiness.

---

## Execution Plan

1. Confirm worktree status.
2. Load `CVF_SERVICE_TOKEN` from ignored local operator env.
3. Build a concrete Alibaba `strategy_analysis` payload with required `topic`
   and `context` fields.
4. Compute `x-cvf-service-signature` as HMAC-SHA256 over
   `<timestamp>.<body>`.
5. Send one POST request to `https://vibcode.netlify.app/api/execute`.
6. Capture sanitized evidence fields only.
7. File completion or blocker review.
8. Run local governance/session checks.

---

## Pre-flight Checks

Before the live call:

- confirm worktree status;
- confirm `https://vibcode.netlify.app/api/execute` is the only target;
- confirm env values are loaded without printing raw values;
- confirm the payload includes required `strategy_analysis` inputs;
- confirm service-token signature headers are generated from the exact request
  body.

---

## Write Ownership

Permitted writes:

- this work order;
- the GC-018 authorization packet;
- one completion/blocker review under `docs/reviews/`;
- session continuity files after completion.

No source-code, deployment, public-sync, provider, or runtime write ownership
is granted.

---

## Evidence Requirements

Evidence must include:

- proof command class, not raw command with secrets;
- HTTP status;
- response `success`;
- route/guard decision;
- routing decision if present;
- enforcement status if present;
- evidence mode;
- provider/model;
- receipt id;
- trace/envelope id;
- raw-secret printed flag.

Evidence Trace Block:

- source: hosted `/api/execute` response;
- method: one signed service-token POST;
- secret handling: raw values loaded only into process memory and not printed;
- expected verdict: pass or narrow blocker.

---

## Acceptance Criteria

Close only if the completion review records:

- HTTP `200`;
- `success=true`;
- decision/routing decision `ALLOW`;
- live evidence/receipt fields;
- provider/model facts;
- raw secret printed `false`;
- no source/runtime/deployment/public-sync change.

Return a blocker if any required fact is absent.

---

## Review Gate

The completion review must explicitly reject claims of:

- hosted SaaS readiness;
- production readiness;
- broad provider stability;
- auth model completeness;
- uptime or operational reliability;
- freeze release.

---

## Closure Checklist

- GC-018 filed.
- Work order filed.
- Live call executed or blocker recorded.
- Completion/blocker review filed.
- Active session state updated.
- Local governance checks pass.
- Push goes only to provenance repo unless a later public-sync work order
  exists.

---

## Return Conditions

Return to operator if:

- hosted endpoint is unreachable;
- service-token auth fails;
- hosted provider key is unavailable;
- response lacks governance evidence;
- a source or deployment change would be required.

## Return-To-Orchestrator Conditions

Return to orchestrator under the same conditions:

- hosted endpoint unreachable;
- service-token authorization failure;
- hosted provider key unavailable;
- missing governance evidence;
- any required source, deployment, provider, or runtime change.

---

## Operator Checkpoint

Operator checkpoint is satisfied by the 2026-05-23 request stating: "tôi cần P3
pass hoàn toàn", after the prior P3 blocker had recommended a tiny fresh
GC-018/work order for one revised concrete hosted payload.

---

## Claim Boundary

This work order authorizes one direct hosted protected workflow rerun only. It
does not authorize source changes, deployment changes, public-sync, hosted
readiness claims, production-readiness claims, provider/runtime semantic
changes, persistence, Maika proof, broad provider stability, or freeze release.
