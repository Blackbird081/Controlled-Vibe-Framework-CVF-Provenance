# CVF GC019 Canonical CLI Runtime Gateway Structural Review

Memory class: FULL_RECORD

Status: APPROVED_BOUNDED_CLI_STRUCTURE

docType: review

Reviewer: Codex

Date: 2026-05-22

## Purpose

Record the GC-019 structural-change review for making the CVF governance CLI
package expose a unified canonical `cvf` runtime gateway.

## Scope / Target / Owner Boundary

Target change:

- add `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/canonical.gateway.ts`;
- add `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/index.ts`;
- make the package default runtime name `cvf`;
- retain `cvf-guard` as an accepted legacy argv prefix;
- add bounded JSONL input support for `cvf audit --input ... --count`;
- add targeted canonical gateway tests.

Owner remains `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI`.

## Target / Source Under Review

Governance packet:

- `docs/baselines/CVF_GC018_CANONICAL_CLI_RUNTIME_GATEWAY_2026-05-22.md`
- `docs/work_orders/CVF_WO_CANONICAL_CLI_RUNTIME_GATEWAY_2026-05-22.md`
- `docs/reviews/CVF_CANONICAL_CLI_RUNTIME_GATEWAY_COMPLETION_2026-05-22.md`

Implementation surfaces:

- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/canonical.gateway.ts`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/index.ts`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/types.ts`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/package.json`

## Scope / Methodology

This review classifies the CLI package changes against GC-019 structural-change
classes. The review checks whether the tranche creates a new extension root,
merges packages, moves route ownership, alters provider registries, changes the
receipt envelope, adds persistent memory, or changes public-sync materials.

## Evidence Trace Block

| Claim | Evidence | Result |
| --- | --- | --- |
| No new extension root introduced | changes remain under existing `CVF_ECO_v2.2_GOVERNANCE_CLI` package plus governance docs | closed |
| Canonical command surface is explicit | `CVF_CANONICAL_RUNTIME_COMMANDS` lists `run`, `audit`, `execute`, `skill`, `receipt`, `trace`, `provider` | closed |
| Legacy prefix remains accepted | gateway strips either `cvf` or `cvf-guard` argv prefix before dispatch | closed |
| No route ownership transfer | gateway inspection records execution owner as existing `cvf-web /api/execute` | closed |
| No provider registry change | gateway inspection records provider owner as existing provider registries | closed |
| No receipt-envelope change | gateway inspection records `receiptEnvelopeChanged: false` | closed |
| Audit support is bounded | `cvf audit --input` reads local JSONL and filters/counts entries only | closed |

## Findings / Position

Position: APPROVE.

Findings:

- The canonical gateway is an additive package-level facade over the existing
  `GovernanceCLI` and command registry.
- The package main now exposes a canonical index, but command dispatch remains
  inside the existing CLI package.
- `cvf` becomes the canonical runtime name while `cvf-guard` remains accepted
  for legacy invocation compatibility.
- The `audit --input` implementation reads local JSONL evidence records and
  does not introduce a new audit database, server route, or persistence layer.
- No `cvf-web` execution route, provider adapter, receipt envelope, public-sync
  file, or hosted/runtime deployment surface is modified.

## Risk / Defect / Corrective Action

| Risk | Corrective action |
| --- | --- |
| Canonical gateway is mistaken for global npm distribution | Completion review limits the claim to package-level runtime gateway behavior |
| `cvf audit` is mistaken for a new audit store | Audit input support is local JSONL read/filter/count only |
| `cvf execute` is mistaken for a new execution engine | Gateway inspection binds execution ownership to existing `cvf-web /api/execute` |
| `cvf provider` is mistaken for provider registry migration | Gateway inspection binds provider ownership to existing provider registries |

## Decision / Recommendation / Disposition

Decision: approve the canonical CLI runtime gateway structural change as a
bounded additive structure inside the existing governance CLI package.

Recommendation: future work may wire deeper `cvf execute`, `cvf provider`, or
`cvf receipt` semantics only through a fresh GC-018/work-order packet and a
new structural review if route, provider, or receipt ownership changes.

Disposition: APPROVED_BOUNDED_CLI_STRUCTURE.

## Verification

Verification completed for this tranche:

- `npm run test -- tests/canonical.gateway.test.ts` PASS.
- `npm run check` PASS.
- `npm test` PASS.
- `python governance/compat/check_markdown_structural_completeness.py --base HEAD --head HEAD --enforce` PASS after required document sections were added.
- `python governance/compat/check_governed_file_size.py --enforce` PASS.

Additional boundary check:

- no `cvf-web` `/api/execute` route diff;
- no provider adapter diff;
- no receipt envelope diff;
- no public-sync diff.

## Claim Boundary

This review approves only the bounded package-level `cvf` canonical CLI
runtime gateway. It does not approve hosted CLI distribution, global binary
installation, public npm publication, new route ownership, provider registry
migration, receipt-envelope changes, durable audit storage, public-sync edits,
or live provider governance claims.
