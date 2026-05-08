<!-- Memory class: FULL_RECORD -->
# CVF CI2 Hosted Live Gate Failure Mode

**Date:** 2026-05-08
**Status:** KNOWN-LIMIT DEFERRAL REQUIRED
**Track:** CI2-H1a - Hosted Run Failure Path

## Failure Mode

| Dimension | Classification |
|---|---|
| Failure class | local_tooling_unavailable |
| Local branch state | ahead of `origin/main` |
| GitHub CLI | unavailable |
| Hosted run | not dispatched |
| Secret metadata | not verified |
| Fail-closed posture | PASS - no hosted PASS claim made |

## Details

- `git fetch origin` completed.
- `git status --short --branch` reported `main...origin/main [ahead 4]`.
- `gh` commands failed with "The term 'gh' is not recognized".
- Because current implementation/evidence commits are not on `origin/main` and
  `gh` is unavailable, the protected GitHub hosted workflow cannot be verified
  from this local session.

## Required Follow-Up

One of the following must happen before claiming CI2-H hosted proof:

1. Push the local commits, install/authenticate GitHub CLI, run CI2-H0a
   metadata sanity, then dispatch the protected workflow.
2. Operator explicitly keeps CI2-H as a GA known limit and uses
   `GA_LOCAL_FIRST_APPROVED_WITH_LIMITS` at most.

## Boundary

CI2 is implemented, but CI2-H hosted PASS is not proven in this artifact.
