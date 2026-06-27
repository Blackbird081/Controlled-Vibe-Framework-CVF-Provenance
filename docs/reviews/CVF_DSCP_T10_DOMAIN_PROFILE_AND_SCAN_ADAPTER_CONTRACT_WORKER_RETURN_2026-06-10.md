# DSCP-T10 Domain Profile And Scan Adapter Contract - Worker Return

Memory class: FULL_RECORD

Status: WORKER_RETURN_PENDING_REVIEW

docType: worker_return

Date: 2026-06-10

Worker: Claude

Reviewer: Codex

Commit mode: WORKER_MUST_NOT_COMMIT

---

## Purpose

Return Claude's bounded DSCP-T10 implementation packet for Codex review,
including source/test artifacts, registry coverage, command evidence, and claim
boundary.

## Scope / Target / Owner Boundary

Target:

- DSCP-T10 domain-profile contract source;
- focused deterministic CPF tests;
- GC-051 source/test/export registry coverage;
- worker evidence packet for Codex review.

Owner boundary:

- Worker owns only the implementation packet and evidence listed in the
  DSCP-T10 work order.
- Codex owns closure review, roadmap/work-order status conversion, final gates,
  commit, and session continuity.
- External `Policy_Local`, provider calls, corpus ingestion, T12, public-sync,
  hosted readiness, production readiness, and public readiness remain out of
  scope.

## Target / Source

| Target | Source or evidence |
|---|---|
| Work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_DSCP_T10_DOMAIN_PROFILE_AND_SCAN_ADAPTER_CONTRACT_FOR_CLAUDE_2026-06-10.md` |
| Source contract | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` |
| Export barrel | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/control.plane.context.barrel.ts` |
| Focused tests | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.domain.profile.contract.test.ts` |
| Registry | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` and `.md` |

## Scope / Methodology

Method:

- implement local deterministic TypeScript contract;
- preserve DSCP descriptor compatibility;
- test legal-policy, company-docs, technical-project, and gate isolation
  behavior;
- update GC-051 registry for changed source/test/export surfaces;
- return uncommitted artifacts for Codex review.

## Findings / Position

Position: RETURNED_PASS_BOUNDED_PENDING_CODEX_REVIEW.

| Finding | Position |
|---|---|
| Contract/test implementation completed within allowed scope | ACCEPT |
| Initial worker packet lacked structural review sections | RESOLVED_BY_CODEX_REVIEWER_AMENDMENT |
| Initial GC-051 coverage omitted the CPF export barrel mentioned in this packet | RESOLVED_BY_CODEX_REVIEWER_AMENDMENT |
| Missing-value domain gate diagnostics needed stronger test coverage | RESOLVED_BY_CODEX_REVIEWER_AMENDMENT |

## Risk / Corrective Action

| Risk | Corrective action |
|---|---|
| A domain gate key with no source value could be silently injected as `UNKNOWN` | Add deterministic diagnostic and focused test coverage |
| Review packet could fail structural completeness gate | Add required review structure sections |
| Registry could miss the export barrel touched by this tranche | Include export barrel under DSCP-T10 source/export registry coverage |

## Finding-To-Governance Learning Disposition

Defect class: `WORKER_EXECUTION_ERROR`

Learning lane: `GOVERNANCE_CONTROL_PLANE`

Disposition: `RULE_EXISTS`

Next action: no new rule required. Existing reviewer-fast structural checks and
GC-051 registry checks caught the worker-return packet gaps before closure.
Codex reviewer amended the packet and registry within allowed scope, and added
focused test coverage for missing-value domain gate diagnostics.

Runtime/provider/cost learning: `N/A_WITH_REASON`

Reason: DSCP-T10 is a deterministic local CPF source contract with no provider
call, live runtime route, cost event, corpus ingestion, or external product
workspace edit.

## Pre-Flight Evidence

| Check | Command | Result |
| --- | --- | --- |
| Clean working tree before edits | `git status --short` (before edits) | Clean - only dispatch files present |
| executionBaseHead captured | `git rev-parse --short HEAD` | `6c6964e0` |
| New source absent before implementation | `Test-Path dscp.domain.profile.contract.ts` | False |
| New test absent before implementation | `Test-Path dscp.domain.profile.contract.test.ts` | False |

executionBaseHead: `6c6964e0`

## Changed File List

`git diff --name-status` result (unstaged new files shown separately):

| Status | Path |
| --- | --- |
| M | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/control.plane.context.barrel.ts` |
| M | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` |
| M | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` |
| ?? (new) | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` |
| ?? (new) | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.domain.profile.contract.test.ts` |
| ?? (new) | `docs/reviews/CVF_DSCP_T10_DOMAIN_PROFILE_AND_SCAN_ADAPTER_CONTRACT_WORKER_RETURN_2026-06-10.md` |

No forbidden paths modified. Confirmed: no `Policy_Local`, `cvf-web`, `ECO_v1.4_RAG_PIPELINE/src`, or `LEARNING_PLANE_FOUNDATION/src` files changed.

## Package Check Result

Command: `npm run check` in `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION`

```
> cvf-control-plane-foundation@0.1.0 check
> tsc -p tsconfig.json --noEmit
```

Result: PASS - zero TypeScript errors.

## Focused Test Result

Command: `npm run test -- tests/dscp.domain.profile.contract.test.ts`

```
 [pass] tests/dscp.domain.profile.contract.test.ts (18 tests) 10ms

 Test Files  1 passed (1)
       Tests  17 passed (17)
   Start at  15:48:34
   Duration  744ms
```

Result: PASS - 18/18 tests passing after Codex reviewer amendment.

Test coverage:

| Describe block | Tests | Profile fixture |
| --- | --- | --- |
| legal_policy (PolicyLocal / Vietnamese) | 7 | `policylocal-vi-legal-policy-v1` - languageCodes `["vi","en"]` |
| company_docs | 4 | `company-docs-internal-v1` - businessUnit/policyOwner metadata |
| technical_project | 4 | `technical-project-docs-v1` - moduleId/runtimeVersion/interfaceLayer |
| unknown gate key diagnostics | 3 | cross-profile gate isolation and missing-value diagnostics |

## Reviewer-Fast Gate Result

Command: `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast --serial`

```
[CVF hook] All reviewer-fast governance checks passed.
```

Result: PASS - 10/10 reviewer-fast checks passed.

## GC-051 Registry Update Summary

JSON registry (`docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`):

- Added entry `dscp-t10-domain-profile-contract-source`: status=SCANNED, findings=[], negativeSearchTerms=[], nextScanRecommendation=NONE_REQUIRED
  covering the new source contract and CPF export barrel.
- Added entry `dscp-t10-domain-profile-contract-test`: status=SCANNED, findings=[], negativeSearchTerms=[], nextScanRecommendation=NONE_REQUIRED
- Total corpora: 37 (was 35)

Markdown registry (`docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md`):

- Added 2 Quick Lookup rows for DSCP-T10 source and test paths.

## Implementation Notes

Source fidelity: implementation uses exact names from the work order contract
(`DomainProfileId`, `DscpDomainFamily`, `DscpDomainProfile`,
`applyDomainProfileToDescriptorInput`, `DomainProfileApplyOptions`,
`DomainProfileApplyResult`). No naming deviations.

Export path: new types and function exported via
`EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/control.plane.context.barrel.ts`
(12 lines added at end). This barrel is already re-exported from `src/index.ts`
through `control.plane.context.barrel`.

Boundary rule check: the function rejects any boundary rule value starting with
`BLOCKED` or equal to `PROHIBITED`. The `legalPolicyProfile` test fixture
explicitly tests this via a mutated profile with
`ec02Gate: "BLOCKED_UNTIL_2026-07-01"` - blocked=true result confirmed.

PolicyLocal isolation: the `policylocal-vi-legal-policy-v1` fixture's
`jurisdiction`, `authorityLevel`, and `legalFramework` fields exist only in that
profile instance. They are not injected into `GovernedArtifactDescriptorInput`
unless `applyDomainProfileToDescriptorInput()` is explicitly called with that
profile. No global DSCP defaults were modified.

Gate isolation test: the cross-profile test confirms that `ec02Gate` appears only
in the legal_policy customGates, `internalGate` only in company_docs, and
`stabilityGate` only in technical_project - gate keys do not bleed between
profiles.

## Claim Boundary

This worker return covers a local deterministic source contract and focused
vitest. It does not claim provider behavior, live governance proof, retrieval
quality, semantic correctness, corpus ingestion, OCR, vector search, PolicyLocal
T12 readiness, legal advice quality, current-law status, public readiness, hosted
readiness, production readiness, public-sync, memory reinjection, high-risk
promotion, or autonomous mutation.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: worker return packet for internal provenance tranche; not public-synced.
