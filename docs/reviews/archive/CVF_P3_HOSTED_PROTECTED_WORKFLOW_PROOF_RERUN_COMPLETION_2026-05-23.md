# CVF P3 Hosted Protected Workflow Proof Rerun Completion

Memory class: FULL_RECORD

Status: CLOSED_P3_HOSTED_PROTECTED_WORKFLOW_PROOF_PASS

docType: review

Reviewer: Codex

Date: 2026-05-23

---

## Purpose

Record the successful follow-up P3 hosted protected workflow proof after the
prior hosted call returned a live `CLARIFY` blocker.

The rerun used one concrete `strategy_analysis` trusted-form payload and closed
the narrow P3 pass criteria.

---

## Scope / Target / Owner Boundary

Target:

- hosted endpoint: `https://vibcode.netlify.app/api/execute`;
- protected workflow: signed service-token `/api/execute`;
- payload class: concrete `strategy_analysis` trusted-form payload;
- provider lane requested: Alibaba `qwen-turbo`;
- proof count: one live hosted call.

Owner boundary:

- evidence review only;
- no source-code changes;
- no deployment changes;
- no provider/runtime changes;
- no public-sync.

---

## Authority Chain

- GC-018:
  `docs/baselines/CVF_GC018_P3_HOSTED_PROTECTED_WORKFLOW_PROOF_RERUN_2026-05-23.md`
- Work order:
  `docs/work_orders/CVF_WO_P3_HOSTED_PROTECTED_WORKFLOW_PROOF_RERUN_2026-05-23.md`
- Prior blocker:
  `docs/reviews/CVF_P3_HOSTED_PROTECTED_WORKFLOW_PROOF_BLOCKER_REVIEW_2026-05-23.md`

---

## Target / Source Under Review

Source under review:

- one signed service-token POST to
  `https://vibcode.netlify.app/api/execute`;
- sanitized command output only;
- no raw API key, service token, NextAuth secret, HMAC signature, or signed
  request headers were copied into this review.

---

## Scope / Methodology

Method:

1. Loaded `CVF_SERVICE_TOKEN` from ignored local operator env files into process
   memory only.
2. Built one concrete `strategy_analysis` payload with required `topic` and
   `context` values plus optional `options`, `constraints`, and `priority`.
3. Computed `x-cvf-service-signature` as HMAC-SHA256 over
   `<timestamp>.<body>`.
4. Posted the signed request to the hosted endpoint.
5. Captured only sanitized response facts.

No rerun loop was performed.

---

## Evidence

Sanitized hosted response facts:

| Field | Value |
| --- | --- |
| Proof | `P3_HOSTED_PROTECTED_WORKFLOW_PROOF_RERUN` |
| Target | `https://vibcode.netlify.app/api/execute` |
| HTTP status | `200` |
| Duration | `15504ms` |
| `success` | `true` |
| Decision | `ALLOW` |
| Routing decision | `ALLOW` |
| Enforcement status | `ALLOW` |
| Evidence mode | `live` |
| Provider | `alibaba` |
| Model | `qwen-turbo` |
| Receipt id | `rcpt-env-mpi55je6-hiddxq` |
| Trace id | `env-mpi55je6-hiddxq` |
| Policy snapshot id | `pol-20260523-0001` |
| Output length | `3917` |
| Raw secret printed | `false` |

Assertions:

- HTTP `200`: pass;
- `success=true`: pass;
- `ALLOW` decision: pass;
- live evidence: pass;
- receipt present: pass;
- trace/envelope present: pass;
- Alibaba provider: pass;
- raw secret printed: pass.

---

## Findings / Position

Position: `CLOSED_P3_HOSTED_PROTECTED_WORKFLOW_PROOF_PASS`.

Findings:

- The hosted target is reachable.
- Signed service-token auth reached the hosted governance runtime.
- The route returned live governance evidence.
- The revised concrete trusted-form payload avoided the prior clarification
  gate.
- The hosted route completed with HTTP `200`, `success=true`, and `ALLOW`.

---

## Decision

Decision: close P3 direct hosted protected workflow proof as pass for the
bounded one-call evidence scope.

The prior blocker remains accurate historical evidence for the earlier minimal
payload. This completion supersedes it only for P3 pass status after the
authorized concrete-payload rerun.

---

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| Overclaiming one hosted proof as hosted SaaS readiness | Keep the claim boundary to one signed hosted `/api/execute` proof only. |
| Treating the prior `CLARIFY` result as invalid | Retain it as historical evidence for the earlier minimal payload. |
| Secret leakage into evidence | Record only sanitized response facts and `rawSecretPrinted=false`; do not copy env files or request headers. |
| Rerun loops under a narrow proof | Stop after the single authorized concrete-payload proof. |

---

## Evidence Trace Block

Claim: the hosted protected route can accept a signed service-token request and
return live governed `ALLOW` evidence for one concrete trusted-form payload.

Evidence:

- signed service-token POST to `https://vibcode.netlify.app/api/execute`;
- HTTP `200`;
- `success=true`;
- `decision=ALLOW`;
- `routingDecision=ALLOW`;
- `enforcementStatus=ALLOW`;
- `evidenceMode=live`;
- provider `alibaba`;
- model `qwen-turbo`;
- receipt `rcpt-env-mpi55je6-hiddxq`;
- trace `env-mpi55je6-hiddxq`;
- `rawSecretPrinted=false`.

Verdict:

- P3 hosted protected workflow proof passes for this bounded proof scope.

---

## Claim Boundary

This review closes one narrow P3 hosted protected workflow proof only. It does
not claim hosted SaaS readiness, production readiness, broad provider
stability, auth model completeness, uptime, deployment correctness, public-sync
readiness, persistence/database readiness, Maika proof, runtime/provider
semantic change, or freeze release.
