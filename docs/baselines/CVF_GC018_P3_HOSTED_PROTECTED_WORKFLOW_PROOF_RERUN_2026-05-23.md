# CVF GC-018 P3 Hosted Protected Workflow Proof Rerun

Memory class: SUMMARY_RECORD

Status: AUTHORIZED_P3_HOSTED_PROTECTED_WORKFLOW_PROOF_RERUN

docType: baseline

Date: 2026-05-23

---

## Purpose

Authorize one narrow follow-up P3 hosted proof after the first hosted call
returned live governance evidence but stopped at `CLARIFY`.

This rerun is limited to one revised concrete payload that uses an existing
trusted-form shape previously proven on live governed `/api/execute`.

---

## Scope / Target / Owner Boundary

Target:

- hosted endpoint: `https://vibcode.netlify.app/api/execute`;
- protected workflow: signed service-token `/api/execute`;
- provider lane: Alibaba `qwen-turbo`;
- payload class: concrete `strategy_analysis` trusted-form payload;
- proof count: one live hosted call.

Owner boundary:

- evidence execution only;
- no source-code changes;
- no deployment changes;
- no provider/runtime semantics changes;
- no public-sync changes;
- no hosted readiness, production readiness, or freeze-release claim.

---

## Source / Predecessor Evidence

Predecessor blocker:

- `docs/reviews/CVF_P3_HOSTED_PROTECTED_WORKFLOW_PROOF_BLOCKER_REVIEW_2026-05-23.md`

The predecessor proved hosted reachability, signed service-token auth into the
governance runtime, live evidence emission, and secret-safe handling, but did
not satisfy P3 pass criteria because the proof payload returned HTTP `422` with
`enforcementStatus=CLARIFY`.

Known passing payload source:

- `scripts/run_phase2b_live_governance_receipt_probe.mjs`
- `docs/reviews/archive/CVF_PHASE_2B_LIVE_GOVERNANCE_PROOF_COMPLETION_2026-05-21.md`

---

## Decision / Baseline / Proposed Tranche

Decision: authorize `P3_HOSTED_PROTECTED_WORKFLOW_PROOF_RERUN`.

Allowed workflow:

1. Load `CVF_SERVICE_TOKEN` from ignored local operator env files into process
   memory only.
2. Build one concrete `strategy_analysis` payload with required `topic` and
   `context` inputs plus optional concrete fields.
3. Sign the exact JSON request body with the configured service-token HMAC
   flow.
4. POST once to `https://vibcode.netlify.app/api/execute`.
5. Record only sanitized response facts.
6. File a completion or blocker review.

---

## Acceptance Criteria

This rerun may close as `CLOSED_P3_HOSTED_PROTECTED_WORKFLOW_PROOF_PASS` only if
the hosted call returns:

- HTTP `200`;
- `success=true`;
- decision/routing decision `ALLOW`;
- evidence mode `live`;
- provider `alibaba`;
- model `qwen-turbo` or route-selected Alibaba equivalent;
- receipt id and trace/envelope id;
- raw secret printed `false`.

If any required fact is absent, return a narrow blocker and do not claim P3
pass.

---

## Evidence / Verification

Required evidence:

- HTTP status;
- `success` flag;
- decision/routing decision;
- enforcement status;
- evidence mode;
- provider;
- model;
- receipt id;
- trace/envelope id;
- policy snapshot id if emitted;
- output length;
- raw secret printed flag;
- proof timestamp or duration;
- whether this closes P3 or returns a blocker.

Verification commands:

- one signed hosted service-token POST to
  `https://vibcode.netlify.app/api/execute`;
- `python governance/compat/check_active_session_state.py --enforce`;
- `python governance/compat/run_local_governance_hook_chain.py`.

Mandatory negative evidence boundary:

- no raw API key;
- no raw service token;
- no HMAC signature;
- no raw signed request headers;
- no copied ignored env-file contents.

---

## Claim Boundary

This GC-018 authorizes one revised hosted proof only. It does not authorize
rerun loops, deployment work, source changes, provider/runtime changes,
public-sync, hosted SaaS readiness, production readiness, persistence, Maika
proof, broad provider stability, or freeze release.
