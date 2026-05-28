# CVF Work Order P3 Hosted Protected Workflow Proof

Memory class: FULL_RECORD

Status: AUTHORIZED_WORK_ORDER

docType: work_order

Date: 2026-05-23

---

## Purpose

Execute the GC-018-authorized P3 direct hosted protected workflow proof with one
signed live call to the hosted CVF `/api/execute` endpoint.

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
- no public-sync;
- no provider/runtime semantics.

---

## Authority Chain

- GC-018:
  `docs/baselines/CVF_GC018_P3_HOSTED_PROTECTED_WORKFLOW_PROOF_2026-05-23.md`
- P3 roadmap:
  `docs/roadmaps/CVF_P3_HOSTED_TARGET_PREFLIGHT_DECISION_ROADMAP_2026-05-23.md`
- P3 selection audit:
  `docs/reviews/CVF_P3_NEXT_ROADMAP_SELECTION_AUDIT_2026-05-23.md`

---

## Agent Roles

Codex performs the bounded workflow roles:

- Orchestrator: keep the proof to one named hosted endpoint and one protected
  workflow.
- Implementer: run the signed live request.
- Auditor: record sanitized evidence and no-secret handling.
- Reviewer: reject broad hosted-readiness or production-readiness claims.

---

## Required First Reads

Read before execution:

- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `docs/roadmaps/CVF_P3_HOSTED_TARGET_PREFLIGHT_DECISION_ROADMAP_2026-05-23.md`
- `docs/baselines/CVF_GC018_P3_HOSTED_PROTECTED_WORKFLOW_PROOF_2026-05-23.md`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`

---

## Allowed Scope

Allowed:

- read local env variable names and values only into process memory;
- sign one request body with the configured service token;
- POST one low-risk payload to the hosted `/api/execute` endpoint;
- record sanitized response facts;
- file completion or blocker evidence.

Forbidden:

- print or commit raw API keys, service tokens, NextAuth secrets, or signed
  request headers;
- copy `.env.netlify` into evidence;
- change code, route behavior, provider adapters, auth semantics, deployment
  config, or public-sync content;
- claim production, SaaS, multi-tenant, uptime, or broad hosted readiness.

---

## Preflight Checks

Before the live call:

- confirm worktree status;
- confirm `https://vibcode.netlify.app/api/execute` is the only target;
- confirm env values are loaded without printing raw values;
- confirm service-token signature headers are generated from the exact request
  body.

---

## Write Ownership

Permitted writes:

- this work order;
- the GC-018 authorization packet;
- one completion/blocker review under `docs/reviews/`;
- session continuity files after completion.

No source-code write ownership is granted.

---

## Execution Plan

1. Commit GC-018 and this work order.
2. Load `CVF_SERVICE_TOKEN` from local operator env without printing it.
3. Build a low-risk hosted proof payload using provider `alibaba` and model
   `qwen-turbo`.
4. Compute `x-cvf-service-signature` as HMAC-SHA256 over
   `<timestamp>.<body>`.
5. Send one POST request to `https://vibcode.netlify.app/api/execute`.
6. Capture sanitized evidence fields only.
7. File completion or blocker review.
8. Run governance checks and update session continuity.

---

## Evidence Requirements

Evidence must include:

- proof command class, not raw command with secrets;
- HTTP status;
- response `success`;
- route/guard decision;
- evidence mode;
- provider/model;
- receipt id if present;
- trace/envelope id if present;
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
- decision `ALLOW`;
- live evidence/receipt fields;
- provider/model;
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
- Push goes only to provenance repo unless a later public-sync work order exists.

---

## Return-To-Orchestrator Conditions

Return to operator if:

- hosted endpoint is unreachable;
- service-token auth fails;
- provider key is unavailable on hosted target;
- response lacks governance evidence;
- a deployment change would be required.

---

## Operator Checkpoint

Operator checkpoint is satisfied by the 2026-05-23 request stating that Claude
reported `P3_DIRECT_PROOF_READY` and that Codex may open GC-018 plus work order
to run the live call to the named hosted endpoint.

---

## Claim Boundary

This work order authorizes one direct hosted protected workflow proof only. It
does not authorize source changes, deployment changes, public-sync, hosted
readiness claims, production-readiness claims, provider/runtime semantic
changes, or freeze release.
