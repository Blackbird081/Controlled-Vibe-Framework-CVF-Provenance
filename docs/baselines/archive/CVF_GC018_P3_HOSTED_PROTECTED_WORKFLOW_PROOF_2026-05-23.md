# CVF GC-018 P3 Hosted Protected Workflow Proof

Memory class: FULL_RECORD

Status: AUTHORIZED_P3_HOSTED_PROTECTED_WORKFLOW_PROOF

docType: baseline

Date: 2026-05-23

---

## Purpose

Authorize one bounded direct hosted protected workflow proof after the P3
preflight exited as `P3_DIRECT_PROOF_READY`.

The proof asks whether the controlled hosted CVF target can accept one signed
service-token `/api/execute` request and return live governance evidence.

---

## Scope / Target / Owner Boundary

Target:

- hosted endpoint: `https://vibcode.netlify.app/api/execute`;
- protected workflow: signed service-token `/api/execute`;
- provider lane: Alibaba via the hosted environment;
- proof count: one live call.

Owner boundary:

- evidence execution only;
- no source-code changes;
- no Netlify deployment changes;
- no provider adapter changes;
- no public-sync changes.

---

## Source / Predecessor Evidence

Predecessor evidence:

- P3 roadmap:
  `docs/roadmaps/CVF_P3_HOSTED_TARGET_PREFLIGHT_DECISION_ROADMAP_2026-05-23.md`
- P3 selection audit:
  `docs/reviews/CVF_P3_NEXT_ROADMAP_SELECTION_AUDIT_2026-05-23.md`
- P2/HN1 closure:
  `docs/reviews/CVF_P2_HN1_TRANCHE_CLOSURE_REVIEW_2026-05-23.md`
- operator/Claude preflight report on 2026-05-23:
  `P3_DIRECT_PROOF_READY`

Concrete preflight values supplied:

| Required value | Selected value |
| --- | --- |
| Hosted target | `https://vibcode.netlify.app` |
| Protected route | `/api/execute` |
| Auth path | signed service token using `x-cvf-service-token`, `x-cvf-service-timestamp`, and `x-cvf-service-signature` |
| Secret posture | operator-supplied local env file only; raw values must not be printed, committed, or copied into evidence |
| Pass/fail matrix | HTTP status, `success`, governance decision, evidence mode, provider/model, receipt id, trace/envelope id, raw-secret printed flag |

---

## Decision / Baseline / Proposed Tranche

Decision: authorize `P3_HOSTED_PROTECTED_WORKFLOW_PROOF`.

This tranche may run exactly one hosted signed service-token call against:

```text
https://vibcode.netlify.app/api/execute
```

Allowed workflow:

1. Load only the non-secret variable names needed for the request from the local
   operator env file.
2. Build a minimal low-risk `/api/execute` payload.
3. Sign the exact request body with the service-token HMAC flow already used by
   the route.
4. POST to the hosted endpoint.
5. Record only sanitized evidence fields.
6. File completion or blocker evidence.

---

## Evidence / Verification

Required evidence:

- HTTP status;
- `success` flag;
- route decision or guard final decision;
- evidence mode;
- provider;
- model;
- receipt id if present;
- trace/envelope id if present;
- service-token auth mode if visible;
- raw secret printed flag;
- proof timestamp;
- whether the result closes direct P3 proof or returns a blocker.

Mandatory negative evidence boundary:

- no raw API key;
- no raw service token;
- no raw NextAuth secret;
- no copied `.env.netlify` contents;
- no request headers containing secrets in committed evidence.

---

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| Hosted proof is overread as production readiness | Claim only one hosted protected workflow call, not SaaS, multi-tenant, uptime, or broad hosted readiness. |
| Secrets leak into evidence | Use local env only, do not print raw values, and record `rawSecretPrinted=false` only if command output is sanitized. |
| Provider failure is confused with auth failure | Record HTTP status, response error, and whether governance evidence fields are absent or present. |
| Endpoint accepts unsigned traffic by mistake | Use signed service-token headers for the positive proof; do not infer broader auth posture from one positive call. |

---

## Acceptance Criteria

The tranche may close as `CLOSED_P3_HOSTED_PROTECTED_WORKFLOW_PROOF_PASS` only if
the hosted call returns:

- HTTP `200`;
- `success=true`;
- live governance evidence or equivalent receipt/envelope fields;
- routing/guard decision `ALLOW`;
- provider/model facts;
- receipt id and trace/envelope id, if emitted by the hosted route;
- raw secret printed `false`.

If any required field is missing, close or return as a blocker with the narrow
cause recorded.

---

## Claim Boundary

This GC-018 authorizes only one hosted protected workflow proof against the
named target. It does not authorize deployment changes, source changes,
provider/runtime semantics, public-sync, hosted SaaS readiness, production
readiness, broad provider stability, persistence, Maika proof, or freeze
release.
