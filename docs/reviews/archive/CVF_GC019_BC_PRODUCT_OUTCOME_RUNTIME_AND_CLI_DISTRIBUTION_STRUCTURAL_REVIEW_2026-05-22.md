# CVF GC019 B/C Product Outcome Runtime and CLI Distribution Structural Review

Memory class: FULL_RECORD

Status: APPROVED_BOUNDED_BC_STRUCTURE

docType: review

Reviewer: Codex

Date: 2026-05-22

## Purpose

Record the GC-019 structural-change review for adding product-outcome runtime
planning and package-level CLI binary semantics to close Review CVF Problem B
and Problem C.

## Scope / Target / Owner Boundary

Target change:

- new `product-outcome.runtime.ts` helper inside the existing Governance CLI
  package;
- new `src/bin/cvf.ts` package binary entrypoint;
- package `bin`, build, and bin smoke declarations;
- `cvf skill plan` and `cvf skill list --certified` command behavior;
- `cvf run <certified-pack>` resolution before existing execute-client
  delegation;
- focused tests.

Owner remains `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI`.

## Target / Source Under Review

Governance packet:

- `docs/baselines/CVF_GC018_BC_PRODUCT_OUTCOME_RUNTIME_AND_CLI_DISTRIBUTION_2026-05-22.md`
- `docs/work_orders/CVF_WO_BC_PRODUCT_OUTCOME_RUNTIME_AND_CLI_DISTRIBUTION_2026-05-22.md`
- `docs/reviews/CVF_BC_PRODUCT_OUTCOME_RUNTIME_AND_CLI_DISTRIBUTION_COMPLETION_2026-05-22.md`

Implementation surfaces:

- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/product-outcome.runtime.ts`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/bin/cvf.ts`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/execute.client.ts`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/package.json`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/tsconfig.json`

## Scope / Methodology

This review classifies whether the tranche creates a new extension root,
changes route/provider/receipt ownership, commits generated distribution
artifacts, creates durable state, or updates public-sync materials.

## Evidence Trace Block

| Claim | Evidence | Result |
| --- | --- | --- |
| No new extension root introduced | all source changes remain under existing Governance CLI package | closed |
| Product runtime does not replace execution route | each runtime plan names `cvf-web /api/execute` as route owner | closed |
| CLI bin is package-level only | `bin` points to build output, no public-sync or npm publish artifact | closed |
| No receipt-envelope mutation | no `GovernanceEvidenceReceipt` type or route receipt diff | closed |
| No provider adapter mutation | provider command remains read-only listing | closed |
| No generated dist committed | build smoke output removed before commit | closed |

## Findings / Position

Position: APPROVE.

Findings:

- The new product-outcome runtime helper is an additive package-local binding
  layer.
- Certified packs are mapped to existing templates and existing pack artifact
  paths.
- `cvf run` still delegates through the existing execute client.
- The binary entrypoint formats output and exits with the command exit code; it
  does not introduce a separate runtime engine.
- No web route, provider adapter, receipt envelope, durable store, public-sync
  tree, or hosted surface is changed.

## Risk / Defect / Corrective Action

| Risk | Corrective action |
| --- | --- |
| Runtime plan is mistaken for route ownership change | Plans explicitly record `cvf-web /api/execute` |
| Package bin is mistaken for public release | Completion limits claim to package-level build/bin proof |
| CommonJS build change affects package consumers | Full CLI tests, typecheck, and bin smoke passed |
| Pack expansion is mistaken for new certified packs | No new certified pack directories or registry entries were added |

## Decision / Recommendation / Disposition

Decision: approve the B/C product-outcome runtime and CLI distribution
structure as a bounded additive change inside the existing Governance CLI
package.

Recommendation: future public npm publication or hosted CLI distribution must
use a separate GC-018 and public-sync authorization.

Disposition: APPROVED_BOUNDED_BC_STRUCTURE.

## Verification

Supporting verification:

- targeted B/C tests PASS 4 files / 16 tests;
- Governance CLI `npm run check` PASS;
- Governance CLI `npm test` PASS 13 files / 110 tests;
- Governance CLI `npm run smoke:bin` PASS;
- no route/provider/receipt-envelope/public-sync diff.

## Claim Boundary

This review approves only the bounded package-level structural change. It does
not approve public npm publication, hosted readiness, provider semantics,
receipt-envelope changes, route changes, durable state, public-sync updates,
Maika proof, or freeze release.
