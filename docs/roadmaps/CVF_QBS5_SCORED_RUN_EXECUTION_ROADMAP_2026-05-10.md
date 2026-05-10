# CVF QBS-5 Scored Run Execution Roadmap

Memory class: FULL_RECORD
Status: FINAL ROADMAP - EXECUTION FAILED / SCORE CLAIM BLOCKED
Date: 2026-05-10
GC-018:
`docs/reference/CVF_GC018_QBS5_SCORED_RUN_EXECUTION_CANDIDATE_2026-05-10.md`

---

## 0. Purpose

QBS-5 executes the pre-registered QBS powered single-provider lane and produces
sanitized execution artifacts for later scoring/review. It does not publish a
QBS quality score by itself.

## 1. Scope

Authorized:

- implement a public powered single-provider runner;
- verify pre-registration tag before execution;
- use Alibaba/DashScope `qwen-turbo` local ignored credentials;
- execute `CFG-A0`, `CFG-A1`, and `CFG-B` over the frozen 48-task corpus with
  three repeats;
- produce curated public artifacts under the pre-registered artifact root;
- preserve raw outputs/logs outside the public repo;
- update public docs and provenance handoff.

Not authorized:

- public QBS score;
- L4/L5/L6 quality claim;
- family-level quality claim;
- provider parity claim;
- committing raw secrets, raw provider logs, unredacted outputs, or unredacted
  reviewer packets.

## 2. Run Boundary

Run ID:

`qbs1-powered-single-provider-20260510-alibaba`

Pre-registration tag:

`qbs/preregister/qbs1-powered-single-provider-20260510-alibaba`

Tag SHA:

`3f574fd5e5843b577a1e7ec78bfcce7f10fd1053`

Public artifact root:

`docs/benchmark/runs/qbs1-powered-single-provider-20260510-alibaba/`

## 3. Gates

| Gate | Requirement | Status |
|---|---|---|
| G0 | QBS4 pre-registration tag pushed | PASS |
| G1 | Fresh GC-018 authorizes execution | PASS |
| G2 | Runner implemented | PASS |
| G3 | Readiness checker with required tag passes | PASS |
| G4 | Local credentials available without printing raw values | PASS |
| G5 | Live execution completes or stops with classified blocker | FAIL - hard-gate failure classified |
| G6 | Sanitized public artifacts written | PASS |
| G7 | Public-surface scan passes | PASS |
| G8 | No public QBS score claimed | PASS |

## 4. Execution Result

Public status:

`EXECUTION_FAILED_NO_QBS_SCORE`

Public commits:

- `0a6e963 Add QBS powered single-provider runner`
- `9f09db3 Publish QBS powered execution failure`

The pre-registered run completed all 432 planned configuration executions, but
failed hard gates:

- direct configs transport OK: true
- `CFG-B` receipt completeness: false
- `CFG-B` expected-decision matching: false
- secret scan clean: true
- mock fallback detected: false
- severe unsafe false negatives: 12 rows across 4 task IDs
- negative-control false blocks: 0

Primary failure classes:

- safety-filtered secret reconstruction rows did not return receipts;
- R2 expected-approval tasks were allowed;
- ambiguous non-coder tasks were allowed instead of clarified.

## 5. Claim Boundary

Allowed after this execution:

- QBS pre-registered Alibaba single-provider execution completed and failed
  hard gates.
- Public artifacts are no-score.
- Reviewer scoring is blocked until the hard-gate failures are remediated or a
  new pre-registered run-set is created.

Not allowed:

- CVF has a public QBS score.
- QBS5 proves L4/L5/L6.
- QBS5 proves provider parity.
- QBS5 supports family-level claims.

## 6. Next Track

Because execution failed hard gates, the next track should be:

`QBS6-HARD-GATE-REMEDIATION-AND-RERUN-PLANNING`

That future track should address receipt completeness for safety-filter blocks,
approval handling for R2 expected-approval tasks, and clarification behavior for
ambiguous non-coder tasks before any reviewer scoring or quality claim.
