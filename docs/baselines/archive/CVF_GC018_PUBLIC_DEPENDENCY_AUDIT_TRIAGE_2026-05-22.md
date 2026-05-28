# CVF GC-018 Public Dependency Audit Triage

Memory class: SUMMARY_RECORD

Status: CLOSED_PUBLIC_DEPENDENCY_AUDIT_RESIDUAL

Date: 2026-05-22

## Purpose

Record the operator-authorized dependency-audit triage opened after the P1
public developer onboarding proof reported npm audit residuals in public
`cvf-web`.

## Scope

In scope:

- public-sync `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json`;
- public-sync `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package-lock.json`;
- public evidence for npm audit closure;
- non-live static CI proof after dependency updates.

Out of scope:

- live provider behavior;
- hosted workflow freshness;
- broad dependency modernization across every extension;
- Next canary adoption;
- `next-auth` API migration;
- runtime/governance semantics.

## Source / Predecessor Evidence

Predecessors:

- `docs/baselines/CVF_GC018_POST_A2_PUBLIC_READINESS_AND_NEXT_VALUE_SCREENING_2026-05-22.md`
- public-sync `docs/evidence/public-developer-onboarding-proof-2026-05-22.md`
- public-sync commit `30976e49 docs: prove public developer onboarding path`

Operator authorization:

```text
User: "đồng ý"
Interpreted tranche: PUBLIC_DEPENDENCY_AUDIT_TRIAGE
```

## GC-018 Candidate Screening

| Candidate | Class | Score | Decision | Rationale |
|---|---:|---:|---|---|
| Public `cvf-web` dependency-audit residual closure | VALIDATION_TEST / MAINTENANCE | 9/10 | CONTINUE_AND_CLOSE | Directly improves public onboarding trust; bounded to package/lock/evidence; machine-verifiable through npm audit and static gate. |
| Forced npm audit downgrade path | RISKY_MAINTENANCE | 2/10 | REJECTED | `npm audit fix --force` proposed downgrading Next/next-auth across major/API boundaries; not compatible with current app-router/next-auth v5 usage. |
| Broad dependency modernization | BROAD_REFACTOR | 4/10 | DEFER | Higher risk and outside the onboarding residual scope. |

## Change Summary

Public-sync commit:

```text
27e0ee63 fix(web): close public dependency audit residual
```

Public changes:

- `next`: `16.1.6` -> `16.2.6`
- `eslint-config-next`: `16.1.6` -> `16.2.6`
- lockfile audit fixes for `jspdf`, `ajv`, `brace-expansion`, `dompurify`,
  `flatted`, `minimatch`, `picomatch`, `rollup`, `undici`, `vite`, and
  related optional packages
- npm override: `postcss` -> `8.5.15`
- new public evidence:
  `docs/evidence/public-dependency-audit-triage-2026-05-22.md`
- P1 onboarding evidence updated to point at the residual closure
- public evidence index, changelog, and technical catalog updated

## Verification

Commands run in public-sync:

```text
npm audit --json
npm ls postcss next next-auth --depth=2
npm run check
python scripts/run_cvf_static_ci_gate.py --json
```

Results:

- `npm audit --json`: PASS, 0 vulnerabilities
- `npm ls postcss next next-auth --depth=2`: PASS
  - `next@16.2.6`
  - `next-auth@5.0.0-beta.30`
  - `postcss@8.5.15` deduped/overridden
- `npm run check`: PASS
- `python scripts/run_cvf_static_ci_gate.py --json`: PASS 7/7
  - Public surface guard: PASS
  - Workflow orchestration guard: PASS
  - Web build: PASS
  - Web TypeScript check: PASS
  - Secrets scan: PASS
  - Docs governance compatibility: PASS
  - Static governance/unit tests: PASS, 44/44

## Decision

Decision: CLOSED.

The public `cvf-web` dependency-audit residual from P1 onboarding is resolved
without `npm audit fix --force`.

## Claim Boundary

This packet records clean npm audit posture for the current public web package
after bounded dependency updates. It does not claim live governance behavior,
hosted release readiness, full extension-stack security certification, or
broader dependency freshness outside the public `cvf-web` package.
