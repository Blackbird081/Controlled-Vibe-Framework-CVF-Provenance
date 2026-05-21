# Work Order - Canonical CLI Runtime Gateway

Memory class: FULL_RECORD

Status: READY_FOR_IMPLEMENTATION
Date: 2026-05-22
docType: work_order

## Purpose
Deliver a bounded package-level canonical `cvf` CLI runtime gateway so the prior Review CVF CLI concern is no longer merely closed by read-only wrappers.

The target command surface is:

- `cvf run`
- `cvf audit`
- `cvf execute`
- `cvf skill`
- `cvf receipt`
- `cvf trace`
- `cvf provider`

## Scope / Target / Owner Boundary
Write ownership:

- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/tests/`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/package.json`
- `docs/reviews/CVF_CANONICAL_CLI_RUNTIME_GATEWAY_COMPLETION_2026-05-22.md`
- `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V11_2026-05-21.md`

Forbidden:

- route changes;
- provider adapter changes;
- new receipt-envelope fields;
- durable memory or database work;
- public-sync updates;
- hosted/product readiness claims;
- live provider proof claims beyond existing CDH-C evidence;
- freeze release.

## Authority Chain
This work order is authorized by:

- `docs/baselines/CVF_GC018_CANONICAL_CLI_RUNTIME_GATEWAY_2026-05-22.md`
- `docs/audits/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_GAP_AUDIT_2026-05-22.md`
- `docs/reviews/CVF_CDH_C_CLI_LIVE_PROOF_COMPLETION_2026-05-21.md`
- operator request 2026-05-22

## Agent Roles
- Orchestrator: file GC-018 and keep the scope package-level.
- Reviewer: confirm no route/provider/receipt-envelope/public-sync expansion.
- Implementer: add the canonical gateway, audit JSONL support, and tests.
- Auditor: run tests, TypeScript check, governance guards, and update session continuity.

## Required First Reads
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `docs/audits/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_GAP_AUDIT_2026-05-22.md`
- `docs/reviews/CVF_CDH_C_CLI_LIVE_PROOF_COMPLETION_2026-05-21.md`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/tests/`

## Pre-Flight Checks
- Confirm `cvf execute` already exists before implementation.
- Confirm this tranche does not require route/provider adapter changes.
- Confirm this tranche does not require new receipt-envelope fields.
- Confirm public-sync update is out of scope.

## Write Ownership
Allowed writes are limited to the files listed in Scope / Target / Owner Boundary plus the completion/session update files.

## Target / Source Under Review
Authority:

- GC-018: `docs/baselines/CVF_GC018_CANONICAL_CLI_RUNTIME_GATEWAY_2026-05-22.md`
- Audit gap: `docs/audits/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_GAP_AUDIT_2026-05-22.md`
- Existing CLI live proof: `docs/reviews/CVF_CDH_C_CLI_LIVE_PROOF_COMPLETION_2026-05-21.md`

## Scope / Methodology
Implementation steps:

1. Add a canonical gateway module for `cvf` that wraps the existing `GovernanceCLI`.
2. Preserve legacy `cvf-guard` compatibility as an accepted prefix/alias.
3. Normalize CLI usage strings toward `cvf`.
4. Keep `cvf run` as an alias to the existing execute handler.
5. Keep `cvf skill`, `cvf receipt`, `cvf trace`, and `cvf provider` read-only.
6. Make `cvf audit` part of the canonical surface and support optional JSONL input filtering/counting without creating a new audit store.
7. Add tests proving the seven-command canonical surface and dry-run execution path.
8. Run package tests, TypeScript check, and governance hook chain.
9. File completion review and update active queue/state/handoff.

## Execution Plan
1. Add canonical gateway module and export surface.
2. Normalize CLI config/usage toward `cvf`.
3. Preserve legacy prefix compatibility.
4. Add JSONL input support for `cvf audit`.
5. Add targeted tests.
6. Run package tests/check.
7. File completion and update session state.
8. Run governance guards and commit.

## Evidence Trace Block
The completion packet must record:

- targeted gateway tests;
- full Governance CLI tests;
- TypeScript check;
- governance hook-chain result;
- explicit no route/provider/receipt-envelope diff;
- claim boundary.

## Findings / Position
Expected closure status: `CLOSED_CANONICAL_CLI_RUNTIME_GATEWAY`.

## Risk / Corrective Action
Risk: a package-level gateway could be mistaken for hosted runtime readiness.

Corrective action: all completion language must say this is the canonical local CLI gateway abstraction over existing behavior, not a new hosted runtime or provider semantics expansion.

## Decision / Recommendation / Disposition
Disposition: implement now under the accepted GC-018.

## Verification
Acceptance criteria:

- `cvf` is the canonical CLI name in the gateway config.
- The gateway can accept both `cvf ...` and legacy `cvf-guard ...` prefixed argv.
- The canonical command list includes exactly the seven requested runtime gateway verbs.
- `cvf run <template> --role <role> --dry-run` succeeds through the async gateway without HTTP I/O.
- `cvf execute --help` succeeds.
- `cvf audit --input <jsonl> --count` can count a supplied audit JSONL.
- Existing read-only command tests remain green.
- No route/provider/receipt-envelope changes occur.

## Review Gate
Before closure, confirm:

- no `cvf-web/src/app/api/execute/route.ts` diff;
- no provider adapter diff;
- no `GovernanceEvidenceReceipt` or web receipt-envelope diff;
- `npm test` and `npm run check` pass in the Governance CLI package;
- completion review states the distribution/public claim boundary.

## Closure Checklist
- [ ] GC-018 filed.
- [ ] Canonical gateway implemented.
- [ ] Legacy prefix compatibility tested.
- [ ] Seven-command canonical surface tested.
- [ ] `cvf run --dry-run` tested without HTTP I/O.
- [ ] `cvf audit --input` tested.
- [ ] Full package tests pass.
- [ ] TypeScript check passes.
- [ ] Governance guards pass.
- [ ] Session queue/state/handoff updated.
- [ ] Completion review filed.

## Operator Checkpoint
Operator selected this tranche explicitly on 2026-05-22 by requesting that CVF be made to have a unified canonical CLI runtime gateway. No additional blocked-work override is required because this tranche does not change provider semantics, route semantics, receipt envelopes, or memory tiers.

## Return-to-Orchestrator Conditions
Return to operator instead of closing if implementation requires route changes, provider adapter changes, new receipt envelopes, npm/global distribution, public-sync update, or a live provider proof beyond existing CDH-C evidence.

## Claim Boundary
This work order closes the package-level canonical CLI gateway gap only. It does not claim broad CLI stability, all-provider parity, public distribution readiness, hosted readiness, or replacement of the web execute route as the runtime source of truth.
