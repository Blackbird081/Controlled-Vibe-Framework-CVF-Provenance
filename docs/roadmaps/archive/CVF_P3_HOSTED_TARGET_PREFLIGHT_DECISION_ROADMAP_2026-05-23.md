# CVF P3 Hosted Target Preflight Decision Roadmap

Memory class: SUMMARY_RECORD

Status: SELECTED_P3_PREFLIGHT_DECISION_ROADMAP

docType: roadmap

Date: 2026-05-23

---

## Purpose

Turn P3 hosted protected workflow proof from a conditional hold into an
executable decision packet.

The roadmap exists because direct hosted proof is valuable, but only after CVF
has an exact hosted target, protected workflow, auth/token path, secret posture,
and pass/fail matrix.

---

## Authority Chain

- Selection audit:
  `docs/reviews/CVF_P3_NEXT_ROADMAP_SELECTION_AUDIT_2026-05-23.md`
- P2/HN1 closure:
  `docs/reviews/CVF_P2_HN1_TRANCHE_CLOSURE_REVIEW_2026-05-23.md`
- Active session state:
  `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- Prior local product proof roadmap:
  `docs/roadmaps/archive/CVF_HOSTED_PRODUCT_READINESS_PROOF_ROADMAP_2026-05-21.md`

---

## Authorization / Decision

Decision: select P3 hosted target preflight and decision as the next roadmap.

This roadmap does not authorize direct hosted proof by itself. It authorizes a
bounded preflight that must end in one of two states:

- `P3_DIRECT_PROOF_READY`: concrete target/workflow/auth/secret/pass-fail
  details are named and a fresh GC-018/work order can be opened.
- `NO_HOSTED_TARGET_AVAILABLE`: no executable hosted target is available, and
  P3 remains blocked with cause.

---

## Scope / Target / Owner Boundary

Target:

- one hosted CVF target candidate, if available;
- one protected workflow candidate;
- one auth/token path;
- one secret-handling posture;
- one pass/fail matrix for a later direct proof.

Owner boundary:

- preflight and decision documentation only;
- no source-code implementation;
- no deployment, tunnel, platform configuration, or production rollout;
- no runtime/provider semantics;
- no public-sync.

---

## Non-Goals

- Do not deploy CVF to a new host.
- Do not create a tunnel or public endpoint as part of this roadmap.
- Do not run direct hosted live proof yet.
- Do not change `/api/execute`, provider adapters, receipt envelopes, auth
  semantics, runtime memory, persistence, or UI.
- Do not claim hosted SaaS readiness, public deployment readiness,
  multi-tenant readiness, or production readiness.
- Do not update the public repository unless a later public-safe capability
  delta exists.
- Do not use this roadmap to lift any governance-kernel freeze.

---

## Work Plan

1. P3-0 hosted target inventory:
   record whether an existing hosted CVF URL/platform exists and whether the
   operator controls it.
2. P3-1 protected workflow selection:
   choose exactly one protected workflow, preferably signed service-token
   `/api/execute` unless a more specific protected hosted workflow is named.
3. P3-2 auth/token and secret posture:
   name the auth path, required environment variables, masking rules, and
   secret non-disclosure constraints.
4. P3-3 pass/fail matrix:
   define the minimum later proof facts: reachability, authenticated request,
   HTTP status, `success`, governance decision, evidence mode, provider/model,
   receipt id, trace id, and raw-secret printed flag.
5. P3-4 decision packet:
   file either `P3_DIRECT_PROOF_READY` with a fresh GC-018/work-order request,
   or `NO_HOSTED_TARGET_AVAILABLE` with the blocker recorded.

---

## Verification / Evidence

Evidence must include:

- hosted target URL/platform or explicit no-target finding;
- target ownership and environment boundary;
- protected workflow name and route;
- auth/token path and non-secret variable names;
- secret-handling posture;
- pass/fail matrix for the later direct proof;
- statement that no raw secrets were printed or committed;
- statement that no hosted readiness claim was made during preflight.

---

## Acceptance Criteria

- The preflight names an exact hosted target URL/platform or records
  `NO_HOSTED_TARGET_AVAILABLE`.
- The preflight names exactly one protected workflow for later proof.
- The preflight names the auth/token path without exposing secret values.
- The preflight defines how secrets will be supplied, masked, and excluded from
  commits.
- The preflight defines a pass/fail matrix sufficient for a later direct proof.
- Direct P3 proof remains blocked until a fresh GC-018 and work order authorize
  execution against the named target.

---

## Decision / Exit Criteria

The roadmap exits in one of two states:

| Exit state | Meaning | Next allowed move |
| --- | --- | --- |
| `P3_DIRECT_PROOF_READY` | Target, workflow, auth, secret posture, and pass/fail matrix are concrete. | Open fresh GC-018 and work order for direct hosted protected workflow proof. |
| `NO_HOSTED_TARGET_AVAILABLE` | No controlled hosted target exists. | Keep P3 blocked; choose a different high-value roadmap or separately authorize deployment setup. |

---

## Claim Boundary

This roadmap selects and constrains a P3 preflight only. It does not prove hosted
protected workflow behavior, does not prove hosted readiness, does not perform a
deployment, does not update public-sync, does not change runtime/provider
behavior, and does not authorize a freeze release.
