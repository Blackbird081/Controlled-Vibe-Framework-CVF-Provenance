# CVF P3 Hosted Protected Workflow Proof Blocker Review

Memory class: FULL_RECORD

Status: RETURNED_BLOCKED_CLARIFY

docType: review

Reviewer: Codex

Date: 2026-05-23

---

## Purpose

Record the result of the GC-018-authorized P3 hosted protected workflow proof.

The hosted endpoint was reached with signed service-token authentication and
returned live governance evidence, but the proof does not close as pass because
the route returned a clarification gate instead of `success=true`.

---

## Scope / Target / Owner Boundary

Target:

- hosted endpoint: `https://vibcode.netlify.app/api/execute`;
- protected workflow: signed service-token `/api/execute`;
- proof count: one live hosted call;
- provider lane requested: Alibaba `qwen-turbo`.

Owner boundary:

- evidence review only;
- no source-code changes;
- no deployment changes;
- no provider/runtime changes;
- no public-sync.

---

## Authority Chain

- GC-018:
  `docs/baselines/CVF_GC018_P3_HOSTED_PROTECTED_WORKFLOW_PROOF_2026-05-23.md`
- Work order:
  `docs/work_orders/CVF_WO_P3_HOSTED_PROTECTED_WORKFLOW_PROOF_2026-05-23.md`
- P3 roadmap:
  `docs/roadmaps/CVF_P3_HOSTED_TARGET_PREFLIGHT_DECISION_ROADMAP_2026-05-23.md`

---

## Target / Source Under Review

Source under review:

- one signed service-token POST to
  `https://vibcode.netlify.app/api/execute`;
- sanitized command output only;
- no raw API key, service token, NextAuth secret, or signed headers were copied
  into this review.

---

## Scope / Methodology

Method:

1. Loaded `CVF_SERVICE_TOKEN` from the ignored local operator env file into
   process memory only.
2. Built one low-risk `/api/execute` payload.
3. Computed `x-cvf-service-signature` as HMAC-SHA256 over
   `<timestamp>.<body>`.
4. Posted the signed request to the hosted endpoint.
5. Captured only sanitized response facts.

One earlier PowerShell attempt did not yield evidence because the local error
handler used the wrong response-object API. It did not print raw secrets. The
Node retry produced the evidence below and is the evidence-bearing call for this
review.

---

## Evidence

Sanitized hosted response facts:

| Field | Value |
| --- | --- |
| Proof | `P3_HOSTED_PROTECTED_WORKFLOW_PROOF` |
| Target | `https://vibcode.netlify.app/api/execute` |
| HTTP status | `422` |
| Duration | `1169ms` |
| `success` | `false` |
| Error | `Spec needs clarification before execution.` |
| Enforcement status | `CLARIFY` |
| Evidence mode | `live` |
| Provider | `alibaba` |
| Model | `clarify` |
| Receipt id | `rcpt-env-mpi3w54q-p5p7bj` |
| Trace id | `env-mpi3w54q-p5p7bj` |
| Policy snapshot id | `pol-20260523-0001` |
| Raw secret printed | `false` |

Interpretation:

- hosted target is reachable;
- signed service-token auth did not fail as `401`;
- live governance envelope/receipt was emitted;
- execution did not reach the required `ALLOW`/provider completion path because
  the hosted route classified the request as needing clarification.

---

## Findings / Position

Position: `RETURNED_BLOCKED_CLARIFY`.

Findings:

- The protected hosted route is alive and reachable.
- The signed service-token request reached CVF governance evaluation.
- The route returned live evidence with receipt and trace identifiers.
- The proof cannot close as pass because acceptance required HTTP `200`,
  `success=true`, decision `ALLOW`, and live completion evidence.
- The blocker is a hosted clarification gate for the submitted proof payload,
  not a network outage and not a service-token authorization failure.

---

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| Overclaiming P3 as closed | Keep status `RETURNED_BLOCKED_CLARIFY`; do not claim hosted protected workflow pass. |
| Treating clarification as provider failure | Record exact status: governance returned `CLARIFY` with live evidence before provider completion. |
| Rerunning repeatedly under a one-call work order | Stop after the evidence-bearing call; open a narrow follow-up if a more concrete payload should be tested. |
| Secret leakage | Evidence records only sanitized facts and `rawSecretPrinted=false`; ignored env files were not staged. |

---

## Decision

Decision: return P3 direct hosted proof as blocked at the clarification gate.

Recommended next move:

- open a tiny follow-up GC-018/work order for one revised hosted payload that
  supplies enough concrete execution fields to avoid the clarification gate; or
- use an existing concrete trusted-form/template payload known to pass local
  governed `/api/execute` and rerun hosted proof once authorized.

Do not treat this review as hosted proof closure.

---

## Evidence Trace Block

Claim: the hosted protected route was reachable and emitted live governance
evidence, but P3 direct proof did not pass.

Evidence:

- signed service-token POST to `https://vibcode.netlify.app/api/execute`;
- HTTP `422`;
- `success=false`;
- `enforcementStatus=CLARIFY`;
- `evidenceMode=live`;
- receipt `rcpt-env-mpi3w54q-p5p7bj`;
- trace `env-mpi3w54q-p5p7bj`;
- `rawSecretPrinted=false`.

Verdict:

- hosted reachability/auth/governance-evidence path is partially proven;
- hosted protected workflow pass remains open because acceptance criteria were
  not met.

---

## Claim Boundary

This review does not close P3 direct hosted proof as pass. It does not claim
hosted readiness, production readiness, broad provider stability, auth model
completeness, deployment correctness, public-sync readiness, runtime/provider
semantic change, or freeze release.
