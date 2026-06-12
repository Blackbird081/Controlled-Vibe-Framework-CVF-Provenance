# CVF Agent Work Order: MEOR-T1 Metadata Evidence Resolution Contract

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: work_order

Date: 2026-06-12

Worker: Codex

Reviewer: Codex in separated reviewer pass

Commit mode: WORKER_MAY_COMMIT

dispatchBaseHead: `eb4ad235`

executionBaseHead: WORKER_MUST_CAPTURE_AT_START

closureBaseHead: REVIEWER_CAPTURE

GC-018: `docs/baselines/CVF_GC018_MEOR_T1_METADATA_EVIDENCE_RESOLUTION_CONTRACT_2026-06-12.md`

## Purpose

Author and verify the specification-only MEOR-T1 contract and machine
semantics before any runtime implementation.

## Authority Chain

| Authority | Path | Status |
| --- | --- | --- |
| Operator direction | 2026-06-12 foundation-first execution | ACCEPT |
| Roadmap | `docs/roadmaps/CVF_METADATA_EVIDENCE_AND_OPERATOR_RESOLUTION_FOUNDATION_ROADMAP_2026-06-12.md` | MEOR-T1 `SPEC_PENDING` |
| GC-018 | `docs/baselines/CVF_GC018_MEOR_T1_METADATA_EVIDENCE_RESOLUTION_CONTRACT_2026-06-12.md` | DISPATCH_READY |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order requirement | Output | Verification |
| --- | --- | --- | --- |
| Canonical contract before implementation | create Markdown contract | `docs/reference/CVF_METADATA_EVIDENCE_AND_OPERATOR_RESOLUTION_CONTRACT_2026-06-12.md` | structural and semantic review |
| Machine-readable semantics | create JSON artifact | `docs/reference/CVF_METADATA_EVIDENCE_AND_OPERATOR_RESOLUTION_SEMANTICS_2026-06-12.json` | JSON parse and value alignment |
| Cross-domain examples | include legal-policy and technical-project examples | both artifacts | no domain-field bleed |
| No runtime implementation | lock source paths | changed-path check | no `EXTENSIONS/` change |

## Intake Role Routing Decision

- Intake summary: execute the specification-only MEOR-T1 tranche under the
  operator-authorized foundation-first roadmap.
- Risk sensitivity: low-risk private control-plane documentation; no runtime,
  provider, secret, legal-quality, public-sync, or readiness claim.
- routeMode: `SINGLE_AGENT_MULTI_ROLE`;
- reason: bounded specification-only tranche with artifact-separated author
  and reviewer passes;
- independence control: authoring, semantic recomputation, and closure review
  must be separate steps with command-backed evidence.
- Escalation condition: stop for operator or an external reviewer if scope
  expands to runtime, Policy_Local mutation, provider/live proof, secrets,
  destructive action, public-sync, or a wider claim boundary.

## Agent Roles

| Role | Actor | Responsibility |
| --- | --- | --- |
| Spec author | Codex author pass | create contract and JSON |
| Adversarial reviewer | Codex reviewer pass | recompute matrix and inspect non-bleed |
| Closer | Codex closure pass | gates, status, commit, continuity |

## Single-Agent Multi-Role Control Block

- Role separation ledger: spec author, adversarial reviewer, closer, and
  committer duties are performed as separate recorded passes.
- Evidence basis: review uses source paths, JSON parse, recomputed transition
  checks, git diff, and machine gates rather than memory-only claims.
- Self-review boundary: independent review is not claimed; this bounded
  single-agent pass is not represented as external validation.
- Escalation conditions: stop for operator or external review if scope, risk,
  public-sync, provider/live proof, secrets, destructive action, or claim
  boundary changes.
- Gate sequence: pre-dispatch before execution, pre-implementation before
  authoring, reviewer-fast before commit, and pre-closure on a real committed
  range before closure.

## Worker Autonomy / No-Question Rule

Allowed-scope remediation is mandatory. Codex proceeds without asking the
operator for routine document corrections, JSON repairs, or gate reruns inside
this work order. Escalate only for a Return-To-Orchestrator condition.

## Required First Reads

1. `docs/roadmaps/CVF_METADATA_EVIDENCE_AND_OPERATOR_RESOLUTION_FOUNDATION_ROADMAP_2026-06-12.md`
2. `docs/baselines/CVF_GC018_MEOR_T1_METADATA_EVIDENCE_RESOLUTION_CONTRACT_2026-06-12.md`
3. `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py`
4. `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts`
5. `docs/reference/CVF_EC02_GATE_SEMANTICS_2026-06-11.json`

## Source Verification Table

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Fact class | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Generic finding extension point | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py` | lines 131-144 | `additional_findings` | `build_scan_outcome_report` | EXISTS | ACCEPT |
| Finding evidence map | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py` | lines 32-39 | `ScanOutcomeFinding` | dataclass | EXISTS | ACCEPT |
| Domain-scoped metadata maps | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | lines 23-53 | `DscpDomainProfile` | interface | EXISTS | ACCEPT |
| LPCI lifecycle enum | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts` | line 20 | `DocumentStatus` | type alias | VALUE_SET | ACCEPT |
| EC-02 matrix | `docs/reference/CVF_EC02_GATE_SEMANTICS_2026-06-11.json` | `queryClassMatrix` | `queryClassMatrix` | JSON schema | VALUE_SET | ACCEPT |

## New Doc-Only Fields

| New item | Intended owner | T1 disposition |
| --- | --- | --- |
| `requirementId` | generic metadata requirement contract | DOC_ONLY_NEW |
| `ownerProfileId` | generic metadata requirement contract | DOC_ONLY_NEW |
| `observedState` | generic metadata evidence record | DOC_ONLY_NEW |
| `evidenceBasis` | generic metadata evidence record | DOC_ONLY_NEW |
| `resolutionState` | generic operator resolution record | DOC_ONLY_NEW |
| `downstreamDisposition` | generic downstream decision record | DOC_ONLY_NEW |
| `requiredAction` | generic operator action record | DOC_ONLY_NEW |
| failure tokens | machine semantics | DOC_ONLY_NEW |

## Allowed Scope

- the two T1 reference artifacts;
- this GC-018/work order, roadmap status, completion review, and continuity;
- local JSON/semantic verification scripts executed without new dependencies.

## Forbidden Scope

- all `EXTENSIONS/` source and tests;
- external Policy_Local;
- corpus mutation, OCR, EC activation, retrieval, provider/API-key use;
- public-sync and readiness claims.

## Write Ownership

| Path | Action |
| --- | --- |
| `docs/reference/CVF_METADATA_EVIDENCE_AND_OPERATOR_RESOLUTION_CONTRACT_2026-06-12.md` | CREATE |
| `docs/reference/CVF_METADATA_EVIDENCE_AND_OPERATOR_RESOLUTION_SEMANTICS_2026-06-12.json` | CREATE |
| T1 baseline/work order/completion and parent roadmap | REVIEWER CLOSURE |
| `EXTENSIONS/**` | FORBIDDEN |

## Forbidden Filesystem State At Dispatch

- no uncommitted `EXTENSIONS/` changes;
- neither T1 reference artifact exists;
- no Policy_Local workspace change is included.

## Pre-Flight Checks

1. Confirm HEAD descends from `eb4ad235`.
2. Confirm roadmap and GC-018 exist.
3. Confirm both target reference paths are absent.
4. Run pre-dispatch autorun with a real changed range.
5. Capture execution base after dispatch commit.

## Execution Plan

1. Author the Markdown contract with exact semantics and invalid combinations.
2. Author equivalent JSON machine semantics.
3. Include one legal-policy example and one technical-project example without
   promoting their fields into the generic vocabulary.
4. Parse JSON and independently recompute allowed transitions.
5. Confirm no raw-content field and no mutation authorization exists.
6. Close artifacts only after reviewer-fast and pre-closure evidence.

## Evidence Requirements

- valid JSON;
- exact enum/value alignment;
- deterministic rule matrix;
- changed-path proof excluding `EXTENSIONS/`;
- reviewer-fast PASS;
- pre-closure autorun PASS after material commit.

## Acceptance Criteria

1. Exact generic values are locked.
2. Invalid combinations and failure tokens are explicit.
3. Source and operator evidence remain distinct.
4. Hints never release downstream work.
5. Report generation is non-mutating.
6. Legal-policy and technical-project examples remain profile-scoped.
7. No runtime/source file changes.

## Review Gate

The reviewer must compare Markdown and JSON independently, test every rule
matrix row, inspect examples for domain bleed, and reject any implicit
activation or autonomous correction language.

## Closure Checklist

- [ ] Contract exists and is structurally complete.
- [ ] JSON parses and matches contract values.
- [ ] Examples show no cross-domain bleed.
- [ ] No runtime/source path changed.
- [ ] Reviewer-fast passes.
- [ ] Completion review and roadmap status are updated.
- [ ] Session continuity is synchronized after material commit.

## Return-To-Orchestrator Conditions

Return to orchestrator if generic semantics require legal-specific fields,
runtime code, external files, a new dependency, provider proof, or a wider
claim boundary.

## Operator Checkpoint

operator.checkpoint.waiver: operator explicitly instructed Codex to execute the
roadmap. No additional checkpoint is required inside T1 allowed scope.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | this file | closed-equivalent status after review | OPEN |
| Completion review | `docs/reviews/CVF_MEOR_T1_METADATA_EVIDENCE_RESOLUTION_CONTRACT_COMPLETION_2026-06-12.md` | final disposition | OPEN |
| Roadmap state | foundation roadmap | MEOR-T1 row | OPEN |
| Contract | T1 Markdown reference | contract version | OPEN |
| Semantics | T1 JSON reference | schema version and JSON parse | OPEN |
| Session continuity | active state/memory/handoff | MEOR-T2 release requires the T1 completion artifact and its closure commit | OPEN |

## Claim Boundary

This work order authorizes specification only. It does not authorize runtime
implementation, metadata correction, domain activation, retrieval, or
readiness claims.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private specification work; no public-sync authorized.
