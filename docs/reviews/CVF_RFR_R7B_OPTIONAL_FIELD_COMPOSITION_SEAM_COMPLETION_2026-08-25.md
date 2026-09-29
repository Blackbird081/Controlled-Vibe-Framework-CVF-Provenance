# CVF RFR-R7B Optional Field Composition Seam Completion Review

Memory class: governed-completion-review

Status: CLOSED_PASS_BOUNDED

docType: review

Date: 2026-08-25

Batch ID: RFR-R7B-OPTIONAL-FIELD-COMPOSITION-SEAM

Reviewer verdict: `CLOSED_PASS_BOUNDED`

Review base head: `6b12ad9790a8e385adef8657871ebc4e18601e9f`

Commit mode: reviewer/closer owns material commit; worker made no commit

## Purpose

Independently review the worker's `BLOCKED_WITH_REASON` return, determine
whether the optional-field repair is correct, classify the remaining MCP
failure against accepted R7A authority semantics, and close or reject R7B
without weakening canonical admission.

## Scope / Methodology

The reviewer inspected every changed line, verified the exact three-path
worker manifest and unchanged MCP proof hash, reran focused and full tests in
both packages, reran both TypeScript/build commands, compared the real-engine
role result with the canonical authority matrix and R7A closure, and ran the
worker-return fast governance gate.

## Findings / Position

| ID | Finding | Evidence | Disposition |
| --- | --- | --- | --- |
| R7B-F1 | Optional own data properties with value `undefined` were incorrectly treated as present. | pre-change `readDataField`; reproduced baseline | CLOSED |
| R7B-F2 | The worker's normalization is minimal and preserves required/accessor/prototype rejection. | source diff plus 13 new adversarial tests | ACCEPT |
| R7B-F3 | Two mocked-ALLOW composition failures were caused by the optional-field seam and now pass without MCP edits. | unchanged composition proof; focused rerun | CLOSED |
| R7B-F4 | The remaining real-engine positive test uses `AI_AGENT` but expects ALLOW. | test `VALID_INPUT`; canonical matrix; focused 31/32 | ROUTE_R7C_TEST_ONLY |
| R7B-F5 | Adding `execute` to AI-agent BUILD authority would contradict accepted R7A semantics. | R7A-F3; canonical role/action tests 25/25 | REJECT_AUTHORITY_WIDENING |

Final decision: R7B is `CLOSED_PASS_BOUNDED`. Its actual validator defect is
fully repaired with no regression. The original dispatch incorrectly grouped
one stale role-fixture failure with the optional-field seam; that orchestration
attribution error is disclosed and routed to R7C. It does not invalidate the
two-file Model Gateway implementation.

## Risk / Corrective Action

The critical risk is "repairing" the final test by making AI-agent execution
permissive or relabeling `execute` as a build verb. Both are forbidden because
R7A independently established that truthful AI-agent/orchestrator execution
blocks and OPERATOR execution may allow. R7C must be test-only and must use an
already authorized positive-path role or revise the stale expectation while
retaining separate AI-agent BLOCK evidence.

## Independent Command Evidence

| Command | Result | Disposition |
| --- | --- | --- |
| Model Gateway focused manifest plus bridge | 2 files; 71/71 PASS | PASS |
| Model Gateway `npm test -- --run` | 33 files; 301/301 PASS | PASS |
| Model Gateway `npm run check` | TypeScript PASS | PASS |
| MCP composition plus execute focused | execute 25/25; composition 6/7; total 31/32 | exact one R7C fixture residual |
| MCP `npm test -- --run` | 34/35 files; 779/780 PASS | exact one R7C fixture residual |
| MCP `npm run build` | TypeScript build PASS | PASS |
| MCP composition proof SHA-256 | `52b00ddf27b0879cd523fe826eb0914482a374f65a7b6e92b3839dde98f7d994` | MATCH, byte-identical |
| worker-return fast gate | 65/65 reviewer-fast plus all wrapper checks PASS | PASS |
| staging and HEAD | staging empty; HEAD unchanged from worker base | PASS |

## Acceptance Criteria

1. Optional `systemPrompt`, `metadata`, and `routing` own-`undefined` values
   normalize to explicit absence.
2. Omitted and own-`undefined` forms yield identical adapter-input and manifest
   digests when other material is identical.
3. Required fields, accessors, hostile prototypes, invalid non-`undefined`
   values and secret/trace/canonicalization guards remain fail-closed.
4. Both truly related MCP composition failures close with the MCP proof
   byte-identical.
5. The remaining failure is explicitly excluded from the R7B implementation
   claim and receives fresh R7C authority before any edit.

All five bounded criteria pass.

## Roadmap-To-Work-Order Trace Matrix

| Requirement | Reviewer result | Disposition |
| --- | --- | --- |
| repair optional-field seam | implementation and direct tests pass | PASS |
| preserve strict validation | negative matrix plus 301/301 package | PASS |
| unchanged MCP proof closes related failures | two of two causally related cases pass | PASS_BOUNDED |
| original 7/7 aggregate criterion | one independently unrelated stale role fixture remains | R7C_REQUIRED |
| independent acceptance | all decisive evidence rerun | PASS |

## Dependency Closure Matrix

| Review dimension | Result | Evidence / next action |
| --- | --- | --- |
| semantic owner | PASS | Model Gateway `readDataField` remains sole production edit |
| fail-closed behavior | PASS | required/accessor/prototype/invalid cases reject |
| cross-owner composition | PARTIAL_BOUNDED | 6/7; R7C test-only reconciliation |
| authority integrity | PASS | no Guard Contract or action-label change |
| path boundary | PASS | exact two edits plus return; completion/closure docs reviewer-owned |
| external effects | PASS | zero provider/live/network/deploy/public effect |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| optional own undefined is normalized only after accessor rejection | `EXTENSIONS/CVF_MODEL_GATEWAY/src/material-context-manifest.ts` | `readDataField` | `readDataField` | material-context manifest | RUNTIME_SOURCE | ACCEPT |
| required values do not take normalization branch | `EXTENSIONS/CVF_MODEL_GATEWAY/src/material-context-manifest.ts` | `readDataField` | `readDataField` | material-context manifest | RUNTIME_SOURCE | ACCEPT |
| direct adversarial coverage exists | `EXTENSIONS/CVF_MODEL_GATEWAY/tests/material-context-manifest.test.ts` | 13 new cases | omission/equality/negative matrix | Model Gateway tests | TEST_SOURCE | ACCEPT |
| stale positive fixture uses AI_AGENT | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/model-gateway-composition-proof.test.ts` | `VALID_INPUT` and real-engine ALLOW case | `VALID_INPUT` | MCP composition proof | TEST_SOURCE | ACCEPT |
| canonical AI-agent BUILD lacks execute | `EXTENSIONS/CVF_GUARD_CONTRACT/src/guards/authority-gate.guard.ts` | `AUTHORITY_MATRIX` | `AUTHORITY_MATRIX` | Guard Contract | CONTRACT_SOURCE | ACCEPT |
| OPERATOR execute ALLOW and AI-agent execute BLOCK are accepted behavior | `docs/reviews/CVF_RFR_R7A_CANONICAL_MCP_GUARD_ENGINE_ADOPTION_COMPLETION_2026-08-24.md` | R7A-F3 and acceptance matrix | truthful Model Gateway action | R7A reviewer authority | GOVERNANCE_EVIDENCE | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_machine_closure_package.py`; `governance/compat/check_roadmap_closure_freshness.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_corpus_scan_registry.py` |
| literalTokensReviewed | `CLOSED_PASS_BOUNDED`; Source Verification columns; Machine Closure Package; Public Export Disposition; Agent Operation Trace Block |
| gateRunPurpose | confirm closure artifact shape after independent semantic review |
| claimBoundary | checker conformance does not substitute for test or source evidence |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
| --- | --- | --- | --- | --- | --- |
| Dispatch attributed three failing cases to one cause without tracing each guard stop. | ORCHESTRATOR_PACKET_GAP | RUNTIME_BEHAVIOR_LEARNING | DESIGN_REVIEW_REQUIRED | R7C packet must pin each test's role/action/blockedBy intent and forbid authority widening | handled in R7C dispatch design; implementation deferred |

## Epistemic Process Block

- Epistemic Process Applicability: BOUNDED_GOVERNANCE_IMPLEMENTATION_REVIEW
- Expected result / prediction: one validator change would close three failures.
- Evidence Comparison: it closes exactly two; the third stops earlier at
  canonical `authority_gate` because the positive fixture uses `AI_AGENT`.
- Contradiction or gap disposition: narrow R7B to its verified causal scope
  and route the stale test contract to R7C.
- Claim update: optional-field repair accepted; full composition proof remains
  pending one test-only reconciliation.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | independent orchestrator/reviewer/closer |
| Provider or surface | repository-local review surface |
| Session or invocation | RFR-R7B independent review, 2026-08-25 |
| Working directory | repository root and two package roots |
| Command or tool surface | diff/source inspection, focused/full Vitest, TypeScript/build, hashes and governance gates |
| Target paths | exact worker manifest plus reviewer-owned return/completion/work-order/roadmap closure surfaces |
| Allowed scope source | standing operator roadmap authority and R7B reviewer closure conversion |
| Before status evidence | HEAD `6b12ad979`; exact worker three-path delta; staging empty |
| After status evidence | exact worker implementation plus reviewer closure documents; staging remains empty before commit |
| Diff evidence | `git diff --name-status`; MCP composition proof hash MATCH |
| Approval boundary | bounded local closure only; no R7C implementation or external effect |
| Claim boundary | no live/provider/deployment/public/production claim |
| Agent type | independent reviewer/closer |
| Invocation ID | `rfr-r7b-independent-review-2026-08-25` |
| Expected manifest | two Model Gateway files, worker return, completion review, work order and roadmap |
| Actual changed set | same exact six paths before material commit |
| Manifest delta | NONE |
| Deletion or rename disposition | N/A with reason: none authorized or performed |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | deterministic local validator and composition-test evidence |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE: R7B validator defect closed; R7C residual explicit |
| receiptEvidence | CVF_RECEIPT_PRESENT: local test/build/governance command evidence recorded above |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no provider/runtime external action |
| invocationBoundary | hermetic repository-local commands |
| interceptionBoundary | no wrapper/interception/live enforcement claim |
| claimLanguage | source-wired and locally tested bounded closure |
| forbiddenExpansion | Guard Contract widening, runtime relabeling, provider/live/network, credentials, deploy, public sync, push and production |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | NOT_APPLICABLE_WITH_REASON: no external knowledge intake |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | first-party Model Gateway and MCP tests |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | repository-governed sources remain authority |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

Reason: this is bounded implementation review, not corpus rescan or intake.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - no complete-corpus claim is made.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance remediation; no public-sync action is authorized.

## Core Guard Self-Protection Authorization

Protected paths:

- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`

Operator authorization: standing dependency-ordered roadmap continuation and
independent reviewer/closer authority for R7B material closure.

Authorized guard-maintenance scope: update only the current R7B work-order
SHA-256 after reviewer closure conversion and regenerate the two derived state
surfaces. Do not change mode, next move, authority paths or state structure in
this material commit.

Rollback boundary: revert the exact atomic material manifest below as one unit.

## Mixed Protected-Path Atomicity Authorization

Disposition: AUTHORIZED_EXACT_MANIFEST

Atomicity reason: the active-session compatibility guard binds
`currentAuthority.workOrderSha256` to the raw closed work-order bytes. The
three generated-state companion paths therefore accompany the material
closure and change only that exact hash projection.

Rollback boundary: revert this exact R7B material-plus-hash-projection commit
as one unit; never retain closed work-order bytes with a stale authority hash.

Exact changed manifest:

- `EXTENSIONS/CVF_MODEL_GATEWAY/src/material-context-manifest.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/tests/material-context-manifest.test.ts`
- `docs/reviews/CVF_RFR_R7B_OPTIONAL_FIELD_COMPOSITION_SEAM_WORKER_RETURN_2026-08-25.md`
- `docs/reviews/CVF_RFR_R7B_OPTIONAL_FIELD_COMPOSITION_SEAM_COMPLETION_2026-08-25.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_RFR_R7B_OPTIONAL_FIELD_COMPOSITION_SEAM_2026-08-25.md`
- `docs/roadmaps/CVF_RUNTIME_FINDINGS_CLOSURE_ROADMAP_2026-08-24.md`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`

Reason: closed work-order bytes and the active authority hash must remain
atomic. The generated state surfaces cannot truthfully retain the dispatch
hash after the work order changes to reviewer-closed status.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | R7B work order | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | this file | reviewer verdict `CLOSED_PASS_BOUNDED` | PASS |
| Worker return | R7B worker return | block reason independently accepted and narrowed | PASS |
| Implementation | exact two Model Gateway files | focused 71/71; package 301/301 | PASS |
| Deterministic proof | both package command receipts | MCP 779/780 with exact R7C residual | PASS |
| Authority integrity | Guard Contract and MCP runtime source | unchanged | PASS |
| Roadmap state | runtime findings roadmap | R7B closed, R7C ready | PASS |
| Registry JSON | corpus registry source owners | no registry mutation authorized or required for existing implementation paths | BLOCKED with reason |
| Registry Markdown | corpus registry source owners | no registry mutation authorized or required for existing implementation paths | BLOCKED with reason |
| External evidence digest | N/A with reason: no external evidence consumed | no digest | N/A with reason |
| System loop interlock | R7B/R7C roadmap dependency | residual routed forward | PASS |
| Session continuity | separately governed sync after commit | excluded from this material commit | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
| --- | --- | --- |
| omission equivalence | identical explicit absence and digests | PASS |
| fail-closed negatives | all direct and package tests pass | PASS |
| cross-owner related cases | both optional-field cases now pass | PASS |
| residual role semantics | AI-agent BLOCK preserved; R7C test-only | PASS_BOUNDED |

## Claim Boundary

R7B is closed only for the optional-own-`undefined` validator repair and its
two causally related composition failures. Full MCP composition proof closure
is not claimed until R7C reconciles the one stale positive-role test. No
authority widening, runtime source edit, live/provider/deploy/public effect or
production-readiness claim follows.
