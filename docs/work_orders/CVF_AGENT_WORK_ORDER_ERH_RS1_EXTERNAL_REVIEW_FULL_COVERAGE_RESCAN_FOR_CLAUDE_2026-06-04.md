# CVF Agent Work Order - ERH-RS1 External Review Full Coverage Rescan For Claude

Memory class: POINTER_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-04

dispatchBaseHead: `b442085e`

executionBaseHead: `b442085e`

closureBaseHead: `b442085e`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Dispatch Claude to perform a source-backed ERH rescan under the newer corpus
completeness and smart-scan controls.

## 1. Mission

Claude must rescan the archived external public-repo review Word document from
source and produce a full-coverage ledger. Success means CVF has a fresh,
source-backed map of every review section/finding to current disposition, with
special attention to section 4.4 architectural weaknesses and the safety-layer
gap that was previously only claim-calibrated.

## 2. Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-04: rescan the external review and inspect why safety was not elevated beyond regex/pattern claim calibration | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V15_2026-05-29.md` | ACCEPT |
| Fresh GC-018 | `docs/baselines/CVF_GC018_ERH_RS1_EXTERNAL_REVIEW_FULL_COVERAGE_RESCAN_2026-06-04.md` | ACCEPT |
| Predecessor ERH roadmap | `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | ACCEPT_AS_PREDECESSOR |
| External review source | `docs/assessments/archive/CVF_EXTERNAL_PUBLIC_REPO_REVIEW_SOURCE_2026-06-03.docx` | ACCEPT_AS_SOURCE |

Authority boundary:

- This work order does not reopen closed ERH tranches.
- This work order does not authorize runtime implementation.
- If source extraction fails, stop with a blocked rescan diagnostic instead of
  summarizing from the old intake.

## Scope

Allowed scope:

- create or update
  `docs/baselines/CVF_GC018_ERH_RS1_EXTERNAL_REVIEW_FULL_COVERAGE_RESCAN_2026-06-04.md`;
- read and extract text from
  `docs/assessments/archive/CVF_EXTERNAL_PUBLIC_REPO_REVIEW_SOURCE_2026-06-03.docx`;
- create or update
  `docs/assessments/CVF_ERH_RS1_EXTERNAL_REVIEW_FULL_COVERAGE_RESCAN_2026-06-04.md`;
- create or update
  `docs/reviews/CVF_ERH_RS1_EXTERNAL_REVIEW_FULL_COVERAGE_RESCAN_COMPLETION_2026-06-04.md`;
- optionally create a docs-only follow-up candidate section inside the RS1
  assessment for ERH-SAF1 and other runtime-adjacent gaps;
- run local non-provider checks needed to support the rescan artifact.

Forbidden scope:

- edit runtime/source files;
- edit package manifests or lockfiles;
- implement safety, DLP, Redis, database, provider-risk, policySnapshotId, or
  audit durability changes;
- public-sync, push, hosted testing, live provider/API proof, or production
  readiness claims;
- copy secrets, print API keys, or move `.env.local`.

Risk ceiling: R0 docs-only rescan.

## Agent Roles

| Role | Assignee | Boundary |
| --- | --- | --- |
| Orchestrator / dispatcher | Codex | author dispatch packet and review Claude output |
| Implementer | Claude | docs-only source rescan under `WORKER_MUST_NOT_COMMIT` |
| Reviewer / closer | Codex after Claude handoff | verify coverage, gates, and claim boundary |
| Operator checkpoint owner | Operator | required only for runtime, public-sync, live proof, or scope expansion |

## 4. Required First Reads

| Path | Why it matters |
| --- | --- |
| `docs/baselines/CVF_GC018_ERH_RS1_EXTERNAL_REVIEW_FULL_COVERAGE_RESCAN_2026-06-04.md` | dispatch authority |
| `docs/reference/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_STANDARD_2026-06-01.md` | rescan completeness rules |
| `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md` | blind-spot discipline for reopened review knowledge |
| `docs/assessments/archive/CVF_EXTERNAL_PUBLIC_REPO_REVIEW_INTAKE_2026-06-03.md` | predecessor intake, not a substitute for source scan |
| `docs/reference/CVF_ERH_T3_EVIDENCE_DURABILITY_BOUNDARY_2026-06-04.md` | prior docs-only boundary and deferred runtime candidates |

## 5. Source Verification Block

| Claimed item | Verification class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| External review DOCX source path is recorded by predecessor intake | EXISTS | `docs/assessments/archive/CVF_EXTERNAL_PUBLIC_REPO_REVIEW_INTAKE_2026-06-03.md` | lines 13-15 | `CVF_EXTERNAL_PUBLIC_REPO_REVIEW_SOURCE_2026-06-03.docx` | archived external review source pointer | ACCEPT |
| Existing route runs DLP before safety | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 240-261 | `applyDLPFilter` then `applySafetyFilters` | `/api/execute` POST route | ACCEPT |
| DLP policy entry point uses active policy patterns | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/dlp-filter.ts` | lines 6-8 | `applyDLPFilter` | web DLP filter | ACCEPT |
| DLP preset and custom pattern engine exists | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/dlp-filter-core.ts` | lines 24-190 | `PRESET_PATTERNS`, `applyDLPPatterns` | DLP pattern engine | ACCEPT |
| Current safety filter is regex/pattern based | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/safety.ts` | lines 1-35 | `INJECTION_PATTERNS`, `PII_PATTERNS`, `applySafetyFilters` | web safety filter | ACCEPT |
| Richer safety-status logic exists but is not the execute-route safety chain | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/safety-status.ts` | lines 115-167 | `sanitizePrompt`, `isInputDangerous` | web safety status helper | ACCEPT |
| WEB_PROVIDER_DEFINITIONS declares static maxRiskLevel values: openai R2, claude R2, gemini R2, alibaba R1, openrouter R1, deepseek R1 | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/provider-router-adapter.ts` | lines 70-119 | `WEB_PROVIDER_DEFINITIONS` | provider router adapter | ACCEPT |

## Pre-Flight Checks

| Command | Required result |
| --- | --- |
| `git rev-parse --short HEAD` | capture Claude base anchor |
| `git status --short` | record start-state changes |
| `Get-FileHash -Path docs/assessments/archive/CVF_EXTERNAL_PUBLIC_REPO_REVIEW_SOURCE_2026-06-03.docx -Algorithm SHA256` | hash matches GC-018 digest or return to orchestrator |
| `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base b442085e --head HEAD` | PASS before source rescan implementation |

## Write Ownership

| Owned path | Mode |
| --- | --- |
| `docs/baselines/CVF_GC018_ERH_RS1_EXTERNAL_REVIEW_FULL_COVERAGE_RESCAN_2026-06-04.md` | create/update |
| `docs/assessments/CVF_ERH_RS1_EXTERNAL_REVIEW_FULL_COVERAGE_RESCAN_2026-06-04.md` | create/update |
| `docs/reviews/CVF_ERH_RS1_EXTERNAL_REVIEW_FULL_COVERAGE_RESCAN_COMPLETION_2026-06-04.md` | create/update |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_RS1_EXTERNAL_REVIEW_FULL_COVERAGE_RESCAN_FOR_CLAUDE_2026-06-04.md` | update only for Claude execution notes if needed |

Forbidden paths: runtime/source files, tests, package manifests, lockfiles,
public-sync clone, workflow files, environment files.

## 6. Execution Plan

| Step | Input | Output | Stop condition |
| --- | --- | --- | --- |
| 1 | DOCX source file | extraction method, hash, section inventory | DOCX unreadable or unsupported |
| 2 | extracted text | section/page-label coverage ledger | any section unprocessed without declared exclusion |
| 3 | predecessor ERH intake and current source paths | finding disposition table | old intake used as source substitute |
| 4 | section 4.4 architectural weaknesses | focused runtime-adjacent gap table | missing row for any 4.4 bullet |
| 5 | safety and DLP source facts | ERH-SAF1 readiness recommendation | runtime implementation attempted |
| 6 | authored RS1 assessment | gates and handoff summary | required gate failure inside allowed scope left unresolved |

## 7. Required Output Structure

The RS1 assessment must include these sections:

| Required section | Minimum content |
| --- | --- |
| `Source Corpus` | DOCX path, SHA256, extraction tool/method, extraction timestamp, extracted text artifact status |
| `Corpus Completeness And Report Integrity` | GC-047-style manifest, processing ledger, reconciliation, exclusions, unreadable/unsupported accounting, drift check, traceability, adversarial verification, verdict |
| `Section Coverage Ledger` | one row per review section or page-labeled section, with `captured`, `missed`, `superseded`, `deferred`, or `not_applicable` disposition |
| `Finding Disposition Ledger` | each finding mapped to current artifact, runtime source, follow-up candidate, or rejection reason |
| `Section 4.4 Architectural Weaknesses` | explicit rows for ephemeral audit, in-memory rate limiter, thin safety/jailbreak layer, policySnapshotId reconstructability, provider risk ceiling hardcoding |
| `Safety Layer Reassessment` | why prior ERH only calibrated claims, current DLP/safety foundations, whether ERH-SAF1 is ready, blocked, or should remain deferred |
| `Workflow Chain Candidates` | prioritized follow-up candidates, with ERH-SAF1 first if safety foundation is sufficient |
| `Claim Boundary` | no ML DLP, no full remediation, no production/public readiness unless later proven |
| `Finding-To-Governance Learning Disposition` | required finding-learning table |
| `Public Export Disposition` | `DEFERRED_PRIVATE_ONLY` unless a separate public-sync work order is authorized |

Allowed GC-047 verdicts for the RS1 assessment:

- `COMPLETE_VERIFIED`
- `COMPLETE_WITH_DECLARED_EXCLUSIONS`
- `PARTIAL`
- `BLOCKED`
- `STALE_SNAPSHOT`

`COMPLETE_VERIFIED` requires zero unresolved sections and zero unresolved
source extraction gaps.

## 8. Section 4.4 Mandatory Rows

The RS1 assessment must include this minimum mapping, updated with source
evidence after Claude extracts the DOCX:

| External-review concern | Required disposition choices |
| --- | --- |
| ephemeral audit JSON/tmp evidence | fixed, bounded, deferred runtime roadmap, or still open |
| in-memory rate limiter without Redis/distributed adapter | fixed, bounded, deferred runtime roadmap, or still open |
| safety layer too thin / lacks advanced jailbreak detection | fixed, ERH-SAF1 ready, ERH-SAF1 blocked, or still open |
| policySnapshotId cannot reconstruct policy at request time | fixed, bounded, deferred runtime roadmap, or still open |
| provider risk ceilings hardcoded in code | fixed, bounded, deferred runtime roadmap, or still open |

## 9. ERH-SAF1 Readiness Rules

Claude must recommend `ERH-SAF1_READY` only if all are true:

- current source confirms `/api/execute` has a safety entry point;
- current source confirms DLP/safety artifacts exist that can be chained without
  introducing ML/classifier claims;
- proposed SAF1 scope can be deterministic and testable without live provider
  proof unless it asserts live governance behavior;
- proposed SAF1 can include audit/readout evidence for safety block or
  escalation;
- runtime file-size and route-size constraints can be respected.

Claude must recommend `ERH-SAF1_HOLD` if source extraction, route ownership,
audit event taxonomy, or file-size constraints are unclear.

Claude must recommend `ERH-SAF1_NOT_READY` only with concrete source-backed
reasons.

## 10. Roadmap-To-Work-Order Trace Matrix

| Roadmap or operator requirement | Work order output | Verification | Status |
| --- | --- | --- | --- |
| Rescan external review because old roadmap predates smart-scan hardening | RS1 assessment with GC-047-style block | source corpus and section ledger | REQUIRED |
| Check section 4.4 architectural weaknesses | Section 4.4 focused table | five mandatory rows | REQUIRED |
| Reassess safety beyond regex claim calibration | Safety Layer Reassessment | ERH-SAF1 readiness rule | REQUIRED |
| Avoid runtime overreach | forbidden scope and git diff evidence | no runtime/source changes | REQUIRED |

## Evidence Requirements

| Evidence | Path or command | Required |
| --- | --- | --- |
| Base anchor | `git rev-parse --short HEAD` | Yes |
| Worktree start state | `git status --short` | Yes |
| DOCX hash | `Get-FileHash ... -Algorithm SHA256` or equivalent | Yes |
| DOCX extraction method | command/tool transcript or script note | Yes |
| Section coverage ledger | RS1 assessment | Yes |
| Finding disposition ledger | RS1 assessment | Yes |
| Runtime no-edit proof | `git diff --name-status <base> HEAD` | Yes |
| Closure worktree state | `git status --short` | Yes |

## 12. Worker Autonomy / No-Question Rule

Claude proceeds autonomously for source extraction, docs-only assessment
authoring, and gate remediation inside Allowed scope. Escalation is required
only for runtime/source edits, live/API proof, public-sync, dependency changes,
secrets, destructive actions, or a claim-boundary change.

## Review Gate

| Gate | Requirement |
| --- | --- |
| Source extraction | DOCX extracted from archived source path, not inferred from old intake |
| Corpus completeness | RS1 includes required GC-047-style block and honest verdict |
| Section 4.4 coverage | five mandatory architectural rows present |
| Runtime boundary | no runtime/source diff |
| Claim boundary | no ML DLP, production readiness, public readiness, or complete remediation claim |

## Closure Checklist

| Item | Required resolution |
| --- | --- |
| RS1 assessment created | checked, blocked, or N/A with reason |
| DOCX hash recorded | checked, blocked, or N/A with reason |
| Section coverage ledger complete | checked, blocked, or N/A with reason |
| Safety reassessment completed | checked, blocked, or N/A with reason |
| Gates rerun | checked, blocked, or N/A with reason |
| Worktree state reported | checked, blocked, or N/A with reason |

## 13. Required Gates

Before implementation:

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base b442085e --head HEAD
```

Before closure, using Claude's captured base anchor:

```powershell
python governance/compat/check_markdown_structural_completeness.py --base <baseHead> --head HEAD --all-changed --enforce
python governance/compat/check_finding_to_governance_learning.py --base <baseHead> --head HEAD --enforce
python governance/compat/check_public_export_disposition.py --base <baseHead> --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base <baseHead> --head HEAD
```

No pre-push gate is required for Claude because `WORKER_MUST_NOT_COMMIT` and
`WORKER_MUST_NOT_PUSH` are implied by this packet.

## 14. Acceptance Criteria

| Criterion | Evidence | Status |
| --- | --- | --- |
| DOCX source was read from the archived source path | source corpus block | REQUIRED |
| Every extracted review section has a disposition | section coverage ledger | REQUIRED |
| Section 4.4 has all five mandatory architectural rows | focused table | REQUIRED |
| Safety gap is classified with ERH-SAF1 readiness | safety reassessment | REQUIRED |
| No runtime/source files changed | diff evidence | REQUIRED |
| Public export remains private-only | Public Export Disposition | REQUIRED |

## 15. Fail Conditions

| Condition | Disposition |
| --- | --- |
| Claude summarizes from prior intake without extracting the DOCX | BLOCKS_CLOSURE |
| Any extracted section has no disposition and no declared exclusion | BLOCKS_CLOSURE |
| Section 4.4 safety row is missing or only repeats old claim calibration | BLOCKS_CLOSURE |
| Runtime/source files are edited | BLOCKS_CLOSURE |
| Assessment claims ML DLP, production readiness, or complete remediation | BLOCKS_CLOSURE |
| Public-sync or push is attempted | BLOCKS_CLOSURE |

## Return-To-Orchestrator Conditions

Return to Codex/orchestrator if:

- the DOCX cannot be extracted with available tools;
- the source file hash differs from the authorized hash without an operator
  explanation;
- RS1 discovers a high-risk runtime/security issue that should not be handled
  as docs-only planning;
- ERH-SAF1 requires live proof, provider calls, secrets, route refactor, or
  package changes.

## Operator Checkpoint

N/A with reason: Claude may complete the docs-only rescan without operator
input. Operator approval is required only for runtime/source edits, live/API
proof, public-sync, dependency changes, secrets, destructive actions, or claim
boundary expansion.

## 17. Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_RS1_EXTERNAL_REVIEW_FULL_COVERAGE_RESCAN_FOR_CLAUDE_2026-06-04.md` | `CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ERH_RS1_EXTERNAL_REVIEW_FULL_COVERAGE_RESCAN_COMPLETION_2026-06-04.md` | `CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `N/A with reason` | RS1 is a fresh rescan follow-up, not a row in the closed original ERH roadmap | N/A with reason |
| Registry JSON | `BLOCKED with reason` | RS1 source is a private archived external-review assessment, not a GC-051 product/search corpus; return action: register only if a later corpus-intelligence reuse work order authorizes it | BLOCKED with reason |
| Registry Markdown | `BLOCKED with reason` | no matching Markdown registry owner exists for this private ERH rescan; return action: add one only if RS1 becomes a reusable corpus-intelligence source | BLOCKED with reason |
| External evidence digest | `docs/assessments/CVF_ERH_RS1_EXTERNAL_REVIEW_FULL_COVERAGE_RESCAN_2026-06-04.md` | DOCX SHA256 `1C52C011A2D11922C5A5712FF785435474AB772B6F9C0A42563D177B1F255A10` | PASS |
| System loop interlock | `N/A with reason` | RS1 authorizes no runtime workflow-chain implementation; SAF1 interlock belongs to a later work order | N/A with reason |
| RS1 assessment | `docs/assessments/CVF_ERH_RS1_EXTERNAL_REVIEW_FULL_COVERAGE_RESCAN_2026-06-04.md` | `CLOSED_PASS_BOUNDED` | PASS |
| Runtime no-edit proof | `git status --short` before reviewer commit showed docs-only RS1 artifacts | PASS |
| Public export | RS1 `Public Export Disposition` | `DEFERRED_PRIVATE_ONLY` | PASS |
| Session continuity | active handoff update by Codex after review | follow-up sync after closure commit | N/A with reason |

## 18. Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Escalation state | Next control action |
| --- | --- | --- | --- | --- |
| Prior ERH intake did not prove full external-review coverage under newer scan controls | CORPUS_COMPLETENESS_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | RS1 coverage ledger |
| Prior safety treatment was claim calibration rather than workflow-chain hardening | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | ROADMAP_REQUIRED | RS1 ERH-SAF1 readiness decision |

## 19. Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this work order and its RS1 assessment are private provenance review
artifacts.

Next action: if RS1 produces public-facing corrections, Codex must author a
separate public-sync work order and switch to the public-sync clone before any
public push.

## Claim Boundary

This work order authorizes only a source-backed rescan and follow-up readiness
assessment. It does not implement runtime safety, DLP, provider-risk,
policySnapshotId, Redis, audit-database, public repository, hosted, production,
or live governance proof changes.
