# CVF Canonical CLI Runtime Gateway Completion

Memory class: FULL_RECORD

Status: CLOSED_CANONICAL_CLI_RUNTIME_GATEWAY
Date: 2026-05-22
Baseline: docs/baselines/CVF_GC018_CANONICAL_CLI_RUNTIME_GATEWAY_2026-05-22.md
Work Order: docs/work_orders/CVF_WO_CANONICAL_CLI_RUNTIME_GATEWAY_2026-05-22.md

## Purpose
Close the operator-selected tranche that makes CVF have a unified package-level canonical `cvf` CLI runtime gateway.

## Scope / Target / Owner Boundary
Delivered:

- `CVFCanonicalGateway` as the canonical `cvf` gateway wrapper around the existing `GovernanceCLI`.
- Canonical command declaration for `cvf run`, `cvf audit`, `cvf execute`, `cvf skill`, `cvf receipt`, `cvf trace`, and `cvf provider`.
- Legacy prefix handling for `cvf-guard`.
- `DEFAULT_CLI_CONFIG.name = "cvf"` with a retained `LEGACY_GUARD_CLI_CONFIG`.
- Package main entry moved to `src/index.ts` to expose the canonical gateway.
- `cvf audit --input <audit.jsonl>` counting/filtering over supplied JSONL without creating a new audit store.
- Tests for the canonical gateway, legacy prefix, dry-run execution delegation, and audit JSONL counting.

Out of scope remained unchanged: no route behavior change, provider adapter change, receipt-envelope change, durable state, public-sync update, live provider claim, hosted readiness, Maika proof, or freeze release.

## Target / Source Under Review
Authority chain:

- GC-018: `docs/baselines/CVF_GC018_CANONICAL_CLI_RUNTIME_GATEWAY_2026-05-22.md`
- Work order: `docs/work_orders/CVF_WO_CANONICAL_CLI_RUNTIME_GATEWAY_2026-05-22.md`
- Original audit gap: `docs/audits/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_GAP_AUDIT_2026-05-22.md`
- Existing CLI live proof boundary: `docs/reviews/archive/CVF_CDH_C_CLI_LIVE_PROOF_COMPLETION_2026-05-21.md`

## Scope / Methodology
Codex executed the bounded tranche as Orchestrator, Reviewer, Implementer, and Auditor:

1. Filed GC-018 and work order before implementation.
2. Added a package-level canonical gateway instead of rewriting route/provider behavior.
3. Normalized command usage toward `cvf`.
4. Preserved the existing execute client and `run` alias behavior.
5. Extended `audit` to read caller-supplied JSONL for count/filter use cases.
6. Added targeted tests and ran the full package suite.

## Evidence Trace Block
Targeted gateway test:

```text
npm run test -- tests/canonical.gateway.test.ts
Test Files: 1 passed
Tests: 6 passed
```

Governance CLI TypeScript check:

```text
npm run check
PASS - tsc --noEmit
```

Governance CLI full test suite:

```text
npm test
Test Files: 11 passed
Tests: 104 passed
```

Boundary checks:

```text
Route files changed: none
Provider adapter files changed: none
Receipt-envelope files changed: none
Public-sync changes: none
```

## Findings / Position
The prior statement "CVF has no `cvf execute`" is not correct anymore. The corrected closure is narrower and now implemented:

- CVF has a canonical package-level `cvf` gateway abstraction.
- The gateway exposes the requested seven-command surface.
- `cvf run` delegates to the existing execute path and is proven in dry-run mode without HTTP I/O.
- `cvf execute` remains the existing governed web execute caller.
- `cvf audit`, `cvf skill`, `cvf receipt`, `cvf trace`, and `cvf provider` are inspection/read-only commands unless a later work order authorizes stronger runtime behavior.

## Risk / Defect / Corrective Action
Residual risk: this is not an npm-distributed binary proof and not a broad live-provider proof.

Corrective action: if the next goal is installed CLI distribution, create a separate package/distribution tranche with build output, `bin`, install smoke test, and public-sync/catalog rules.

## Decision / Recommendation / Disposition
Disposition: `CLOSED_CANONICAL_CLI_RUNTIME_GATEWAY`.

Recommendation: treat the Review CVF CLI runtime gap as closed at the package-level gateway layer. Do not claim public product distribution or all-provider runtime stability from this tranche.

Public catalog update: N/A for this tranche because public-sync updates were out of scope; any public catalog claim should be prepared from the sibling public-sync clone under separate authorization.

## Verification
PASS:

- `cvf` is the canonical gateway name.
- `cvf-guard` remains accepted as a legacy prefix.
- Canonical runtime commands are exactly `run`, `audit`, `execute`, `skill`, `receipt`, `trace`, and `provider`.
- `cvf run documentation --role BUILDER --dry-run` succeeds through the async gateway without HTTP I/O.
- `cvf audit --input <audit.jsonl> --count` counts supplied audit JSONL.
- Existing CLI tests remain green.
- TypeScript check passes.

## Test Depth Classification
T1: direct unit coverage for prefix stripping and canonical command declaration.

T2: command behavior coverage for `run`, `audit`, and help/legacy compatibility.

T3: full package test suite and TypeScript check.

T4: governance hook chain required before commit.

Meaningful Assertion Rate: high for package-level canonical gateway behavior; intentionally no live-provider or package-install distribution claim.

## Claim Boundary
This completion proves a canonical package-level CLI runtime gateway abstraction in the Governance CLI package. It does not prove npm/global installation, hosted runtime readiness, public deployment readiness, all-provider parity, new provider execution semantics, new receipt envelopes, route changes, durable state, public-sync catalog readiness, Maika readiness, or freeze release.
