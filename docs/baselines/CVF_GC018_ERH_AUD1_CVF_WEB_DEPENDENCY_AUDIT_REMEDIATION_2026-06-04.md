# CVF GC-018 ERH-AUD1 CVF Web Dependency Audit Remediation

Memory class: FULL_RECORD

Status: ACTIVE_BASELINE

docType: baseline

Date: 2026-06-04

executionBaseHead: `28f76620`

## Purpose

Authorize a bounded Claude work order for `cvf-web` dependency-audit
remediation after ERH-DEP1 classified `next-auth` beta as an API-stability
risk, not a direct CVE.

ERH-AUD1 targets the remaining `npm audit --json` findings in
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web` and turns them into a source-backed
remediation workflow, not an unbounded framework migration.

## Scope / Target / Owner Boundary

Target workspace:

`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web`

Allowed work:

- refresh `npm audit --json` and package metadata;
- update `package.json` and `package-lock.json` only when the fix is
  non-semver-major or explicitly classified as bounded;
- run focused web verification after dependency changes;
- create an audit remediation ledger, checker, tests, and completion review;
- update ERH roadmap and GC-052 registry if a reusable checker/workflow is
  created.

Forbidden work:

- do not change auth runtime behavior;
- do not migrate `next-auth` beta in ERH-AUD1;
- do not public-sync or push public;
- do not claim production, hosted, public, or security readiness;
- do not suppress unresolved audit findings without ledger classification;
- do not perform a destructive package reset or broad dependency refresh.

## Initial Evidence Snapshot

Codex ran `npm audit --json` from `cvf-web` on 2026-06-04 at base
`28f76620`. The command exited non-zero and reported:

| Severity | Count |
| --- | --- |
| critical | 3 |
| high | 7 |
| moderate | 4 |
| total | 14 |

Direct vulnerable packages in the snapshot include:

- `next` at `16.1.6`, with audit fix available at `16.2.7` and
  `isSemVerMajor=false`;
- `jspdf` at `^4.1.0`, affected range `<=4.2.0`;
- `vitest` at `^4.0.18`, affected range `<4.1.0`;
- `@vitest/coverage-v8` at `^4.0.18`, affected through `vitest`.

Claude must rerun audit and metadata checks before editing because dependency
metadata is time-sensitive.

## Source / Predecessor Evidence

| Source | Purpose | Disposition |
| --- | --- | --- |
| `docs/reviews/CVF_ERH_DEP1_DEPENDENCY_RISK_WORKFLOW_CHAIN_COMPLETION_2026-06-04.md` | predecessor classifying `next-auth` beta separately from audit CVEs | ACCEPT |
| `docs/reference/CVF_ERH_DEP1_DEPENDENCY_RISK_LEDGER_2026-06-04.md` | prior audit snapshot and dependency-risk ledger | ACCEPT |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | package manifest and script surface | ACCEPT |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package-lock.json` | lockfile dependency graph | ACCEPT |
| `npm audit --json` from `cvf-web` at base `28f76620` | fresh initial audit snapshot for dispatch | ACCEPT_WITH_REFRESH_REQUIRED |

## Decision

Dispatch ERH-AUD1 to Claude under `WORKER_MUST_NOT_COMMIT`.

The desired result is a committed-candidate worktree with a bounded dependency
audit remediation, evidence ledger, and verification record. Codex/operator
will review and commit if gates pass.

## Evidence / Verification

Dispatch authoring verification:

```powershell
python governance/compat/check_markdown_structural_completeness.py --base 28f76620 --head HEAD --all-changed --enforce
python governance/compat/check_work_order_dispatch_quality.py --base 28f76620 --head HEAD --enforce
python governance/compat/check_public_export_disposition.py --base 28f76620 --head HEAD --enforce
python governance/compat/check_finding_to_governance_learning.py --base 28f76620 --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 28f76620 --head HEAD
```

Live proof requirement: N/A with reason. ERH-AUD1 dispatch authoring makes no
AI/provider governance behavior claim and performs no live provider call.

## Claim Boundary

This baseline authorizes a dependency-audit remediation work order only. It
does not prove production security, hosted readiness, public readiness, stable
auth posture, live governance behavior, or provider behavior.
