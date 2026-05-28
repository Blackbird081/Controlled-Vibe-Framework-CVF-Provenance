# CVF GC-018 B/C Product Outcome Runtime and CLI Distribution

Memory class: SUMMARY_RECORD

Status: ACCEPTED

Date: 2026-05-22

## Purpose

Authorize one bounded continuation tranche to close the remaining clean-closure
gap for Review CVF Problem B and Problem C.

Problem B is already closed at the static pack and workflow-composition layer,
but still needs a concrete runtime binding that makes each certified pack an
outcome-oriented executable plan.

Problem C is already closed at the package-level canonical gateway layer, but
still needs an installable CLI binary contract and stable command output
contract.

## Scope / Target / Owner Boundary

In scope:

- define a product-outcome runtime plan for certified skill packs;
- map certified packs to existing web execute templates, receipt schema paths,
  and failure recovery paths;
- allow `cvf skill plan <pack-or-outcome>` to inspect the executable plan;
- allow `cvf run <certified-pack-or-outcome> --role <role>` to resolve through
  the product-outcome runtime plan before delegating to the existing execute
  client;
- add package-level `bin` and build/smoke scripts for the canonical CLI;
- add JSON output mode at the CLI binary boundary;
- add focused tests and governance closure records.

Out of scope:

- no new `cvf-web` route behavior;
- no provider adapter or provider registry migration;
- no receipt-envelope schema change;
- no durable storage or database;
- no public-sync update;
- no hosted SaaS readiness claim;
- no broad all-provider stability claim;
- no global freeze release.

Owner boundary remains:

- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI` for CLI runtime and distribution
  semantics;
- existing certified skill-pack registry for pack inventory;
- existing `cvf-web /api/execute` route as the execution owner.

## Target / Source Under Review

Source driver: operator request on 2026-05-22 to finish both B and C so they no
longer remain residual pain points.

## Source / Predecessor Evidence

Predecessor evidence:

- `docs/reviews/CVF_T2_PRODUCT_SKILL_PACK_MVP_COMPLETION_2026-05-22.md`
- `docs/reviews/CVF_T3_WORKFLOW_COMPOSITION_OUTCOME_SURFACE_COMPLETION_2026-05-22.md`
- `docs/reviews/CVF_CANONICAL_CLI_RUNTIME_GATEWAY_COMPLETION_2026-05-22.md`
- `.private_reference/legacy/CVF 17.05/Review CVF.md`

## Scope / Methodology

This tranche must close the remaining practical gaps without redefining the
existing runtime truth:

- certified packs become executable plans, not a new execution engine;
- `cvf` becomes installable/buildable at the package boundary, not a public
  distribution claim;
- `cvf run` delegates to the existing execute client after plan resolution;
- receipt and provider ownership remain unchanged.

## Evidence Trace Block

Required evidence:

| Claim | Required evidence |
| --- | --- |
| Certified packs have executable plans | unit tests over all certified pack IDs |
| `cvf skill plan` exposes runtime binding | command tests with text and JSON output |
| `cvf run <pack>` resolves to existing template | dry-run gateway test verifying template mapping |
| CLI is installable/buildable | TypeScript build and bin smoke test |
| Existing CLI behavior preserved | full Governance CLI test suite |
| Governance boundaries preserved | local governance hook chain |

## Findings / Position

Position: approved.

The operator selected this tranche explicitly. The tranche is allowed because it
does not change provider semantics, route semantics, receipt envelopes, or
memory tiers. It turns prior static capability surfaces into inspectable,
delegated runtime plans.

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| Product runtime plan is mistaken for a new execution engine | Bind every plan to existing `cvf-web /api/execute` ownership |
| CLI binary is mistaken for public npm publication | Completion must state package-level build/bin proof only |
| Runtime plan is mistaken for live provider proof | Completion must distinguish dry-run/plan proof from live governance proof |
| Receipt schema paths are mistaken for receipt-envelope mutation | No `GovernanceEvidenceReceipt` schema changes are authorized |

## Decision / Recommendation / Disposition

Decision: proceed with a bounded B/C clean-closure implementation.

Recommendation: close Problem B as product-outcome runtime plans over certified
packs, and close Problem C as installable package-level CLI with stable command
semantics.

## Verification

Minimum verification before closure:

- targeted runtime-plan and CLI-bin tests pass;
- `npm run check` passes for the Governance CLI package;
- `npm test` passes for the Governance CLI package;
- bin smoke script passes;
- markdown structural completeness passes;
- local governance hook chain passes.

## Claim Boundary

This GC-018 authorizes only product-outcome runtime planning and package-level
CLI distribution semantics. It does not authorize public npm release, hosted
readiness, route changes, provider runtime changes, receipt-envelope changes,
durable persistence, public-sync edits, Maika proof, or a global freeze
release.
