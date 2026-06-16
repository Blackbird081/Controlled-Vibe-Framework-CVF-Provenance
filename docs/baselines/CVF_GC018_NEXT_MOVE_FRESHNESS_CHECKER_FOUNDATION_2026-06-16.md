# CVF GC-018 - Next-Move Freshness Checker Foundation

Memory class: POINTER_RECORD

Status: CLOSED_PASS_BOUNDED

docType: baseline

Date: 2026-06-16

Owner: Codex

executionBaseHead: 7a89cccc

rawMemoryReleased: false

## Purpose

Authorize a bounded governance checker that prevents active next-move
surfaces from dispatching or reopening work that the active session state
already records as `CLOSED_PASS` or `CLOSED_PASS_BOUNDED`.

## Source / Predecessor Evidence

| Source | Evidence |
|---|---|
| Operator instruction | 2026-06-16 request to process this error before the next roadmap |
| RSF-T3 completion | machine-check candidate for semantic next-move freshness |
| Active state | `nextAllowedMove` currently blocks C-02 P2 redispatch but no checker enforced that semantics before this batch |
| Existing guard pattern | session-mode checker provides read-only session-surface consistency pattern |

## Decision / Baseline / Proposed Tranche

Decision: authorize one bounded foundation tranche for a read-only
next-move freshness checker.

Baseline: structural session gates can pass while stale semantic next-move text
would still be possible.

Proposed tranche: add checker, tests, hook wiring, autorun wiring, steward
session-sync wiring, and closure evidence.

## Scope

Allowed:

- add a read-only next-move freshness checker under `governance/compat`;
- add focused unit tests for stale active-state, front-door, handoff, and
  startup-acknowledgment next-move text;
- wire the checker into reviewer-fast, pre-commit, pre-push, autorun common
  gates, and the steward `session-sync` lane;
- document the standard, work order, and completion review.

Forbidden:

- runtime product-source mutation outside `governance/compat`;
- provider/API calls, credentials, live proof, public-sync, or network claims;
- Model Gateway C-02 P2 redispatch or Model Gateway P3 authorization;
- session front-door, active state, or active handoff mutation in the material
  commit;
- broad legacy absorption, historical artifact migration, or public readiness
  claim.

## Acceptance Criteria

| ID | Criterion | Evidence |
|---|---|---|
| NMF-AC1 | Checker discovers closed targets from active session state. | focused tests and current-state run |
| NMF-AC2 | Checker scans only current next-move surfaces. | implementation review |
| NMF-AC3 | Checker rejects dispatch/open/worker text for closed targets. | focused tests |
| NMF-AC4 | Safe blocked/closed wording remains allowed. | focused tests and current-state run |
| NMF-AC5 | Checker is wired into early phase gates. | hook and autorun runner diffs |

## Evidence / Verification

Required verification:

- focused unit tests for the checker;
- current-state checker run;
- core guard self-protection;
- work-order dispatch-quality gate;
- reviewer-fast gate;
- material-range pre-closure gate after commit.

## Claim Boundary

This baseline authorizes governance control-plane freshness only. It does not
prove runtime governance behavior, provider routing behavior, public readiness,
production readiness, or any Model Gateway implementation permission.
