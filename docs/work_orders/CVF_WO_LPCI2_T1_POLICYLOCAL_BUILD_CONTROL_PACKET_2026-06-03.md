# CVF Work Order - LPCI2-T1 PolicyLocal Build Control Packet

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-03

dispatchBaseHead: `3ff90651`

executionBaseHead: `3ff90651`

closureBaseHead: `3ff90651`

Commit mode: SELF_EXECUTION_OPERATOR_AUTHORIZED

## Purpose

Create a bounded PolicyLocal build control packet that merges the existing
PolicyLocal frontend build handoff with the closed LPCI1 T1-T7 governance
contracts. This work order is self-executed by Codex under the operator's
instruction to hold orchestrator, worker, and reviewer roles temporarily.

The output is documentation/control only. No external worker is dispatched.

## Authority Chain

| Authority | Path |
| --- | --- |
| Operator instruction | 2026-06-03 chat instruction: Codex holds multiple roles and finishes without external worker handoff |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` |
| Active handoff | `AGENT_HANDOFF_V15_2026-05-29.md` |
| LPCI2 roadmap | `docs/roadmaps/CVF_LPCI2_POLICYLOCAL_PRODUCTIZATION_ROADMAP_2026-06-03.md` |
| LPCI1-T7 spec | `docs/reference/CVF_LPCI1_T7_TEMPLATE_PACKAGING_SPEC_2026-06-03.md` |
| PolicyLocal external handoff | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\PolicyLocal\CLAUDE_BUILD_HANDOFF.md` |

## Agent Roles

| Role | Responsibility | Boundary |
| --- | --- | --- |
| Orchestrator | choose the next bounded post-LPCI1 move and authorize T1 | no broad product/runtime scope |
| Worker | author repo packet and workspace copy | no app code, corpus import, provider call, or public-sync |
| Reviewer | verify scope, boundary, source inheritance, and gates | reject any implementation or legal-answer overclaim |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap path | Roadmap tranche | Work order tranche | Mapped output | Verification |
| --- | --- | --- | --- | --- |
| `docs/roadmaps/CVF_LPCI2_POLICYLOCAL_PRODUCTIZATION_ROADMAP_2026-06-03.md` | LPCI2-T1 PolicyLocal build control packet | `CVF_WO_LPCI2_T1_POLICYLOCAL_BUILD_CONTROL_PACKET_2026-06-03.md` | `docs/reference/CVF_LPCI2_POLICYLOCAL_BUILD_CONTROL_PACKET_2026-06-03.md` and workspace copy | closure review and final gates |

## Source Verification

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| `EXISTS: LPCI1-T7 downstream guide` | `docs/reference/CVF_LPCI1_T7_TEMPLATE_PACKAGING_SPEC_2026-06-03.md` | `## Downstream Workspace Adoption Guide` | `Downstream Workspace Adoption Guide` | LPCI1-T7 template packaging | ACCEPT |
| `EXISTS: Vietnamese NFC normalization` | `docs/reference/CVF_LPCI1_T7_TEMPLATE_PACKAGING_SPEC_2026-06-03.md` | `## Vietnamese Corpus Stage 3 Diacritic Normalization` | `Unicode NFC` | LPCI1-T7 template packaging | ACCEPT |
| `EXISTS: C4/C5 test corpus design` | `docs/reference/CVF_LPCI1_T7_TEMPLATE_PACKAGING_SPEC_2026-06-03.md` | `## C4/C5 Test Corpus Design` | `freshness_flag`, `conflict_flag` | LPCI1-T7 template packaging | ACCEPT |

## External Workspace Input Verification

These inputs are outside the provenance repo and are therefore recorded outside
the Source Verification table.

| External input | Verification |
| --- | --- |
| `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\PolicyLocal\CLAUDE_BUILD_HANDOFF.md` | file exists; read before T1 packet authoring |
| `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\PolicyLocal\CODEX_POLICYLOCAL_SPEC_REVIEW_2026-06-02.md` | file exists; read before T1 packet authoring |

## Write Ownership

| Path | Action | Notes |
| --- | --- | --- |
| `docs/roadmaps/CVF_LPCI2_POLICYLOCAL_PRODUCTIZATION_ROADMAP_2026-06-03.md` | CREATE | T1 closed, later tranches proposed |
| `docs/work_orders/CVF_WO_LPCI2_T1_POLICYLOCAL_BUILD_CONTROL_PACKET_2026-06-03.md` | CREATE | this self-execution work order |
| `docs/reference/CVF_LPCI2_POLICYLOCAL_BUILD_CONTROL_PACKET_2026-06-03.md` | CREATE | canonical repo copy |
| `docs/reviews/CVF_LPCI2_T1_POLICYLOCAL_BUILD_CONTROL_PACKET_COMPLETION_2026-06-03.md` | CREATE | closure review |
| `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\PolicyLocal\CVF_POLICYLOCAL_BUILD_CONTROL_PACKET_2026-06-03.md` | CREATE | external workspace copy, not committed in this repo |

## Allowed Scope

- Create documentation/control artifacts only.
- Merge LPCI1 T1-T7 rules with the existing PolicyLocal handoff.
- Define must-pass implementation gates for future app work.
- Update session state and handoff after closure.

## Forbidden Scope

- No Next.js scaffold, UI component, API route, database file, package install,
  provider key handling, live provider call, vector DB, embedding, corpus
  ingestion, or public-sync.
- No legal advice, current-law claim, production readiness claim, or public
  release claim.

## Worker Autonomy / No-Question Rule

Codex may repair any gate failure inside this allowed scope and rerun gates
without asking the operator. Codex must stop only if a repair requires runtime
implementation, destructive file operations, public-sync, live provider proof,
secret access, or a broader product decision.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `AGENT_HANDOFF_V15_2026-05-29.md`
4. `docs/reference/CVF_LPCI1_T7_TEMPLATE_PACKAGING_SPEC_2026-06-03.md`
5. `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\PolicyLocal\CLAUDE_BUILD_HANDOFF.md`
6. `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\PolicyLocal\CODEX_POLICYLOCAL_SPEC_REVIEW_2026-06-02.md`

## Pre-Flight Checks

- Confirm `git status --short` before edits.
- Confirm external PolicyLocal folder exists.
- Confirm LPCI1-T7 is `CLOSED_PASS_BOUNDED`.
- Confirm no runtime files are inside this work order's allowed scope.

## Execution Plan

1. Read session front door and active state.
2. Read PolicyLocal handoff and Codex addendum in the external workspace.
3. Create LPCI2 roadmap, work order, build control packet, completion review,
   and external workspace copy.
4. Update active session continuity.
5. Run governance gates and commit.

## Acceptance Criteria

| Criterion | Requirement |
| --- | --- |
| Repo packet exists | `docs/reference/CVF_LPCI2_POLICYLOCAL_BUILD_CONTROL_PACKET_2026-06-03.md` |
| Workspace packet exists | `CVF-Workspace\PolicyLocal\CVF_POLICYLOCAL_BUILD_CONTROL_PACKET_2026-06-03.md` |
| Closure review exists | completion review records evidence and boundaries |
| Session updated | mode and next allowed move reflect LPCI2-T1 closure |
| Gates pass | markdown, dispatch-quality, F2G, public disposition, active-session, autorun closure |

## Evidence Requirements

| Evidence type | Required artifact |
| --- | --- |
| Roadmap | `docs/roadmaps/CVF_LPCI2_POLICYLOCAL_PRODUCTIZATION_ROADMAP_2026-06-03.md` |
| Work order | `docs/work_orders/CVF_WO_LPCI2_T1_POLICYLOCAL_BUILD_CONTROL_PACKET_2026-06-03.md` |
| Repo packet | `docs/reference/CVF_LPCI2_POLICYLOCAL_BUILD_CONTROL_PACKET_2026-06-03.md` |
| Completion review | `docs/reviews/CVF_LPCI2_T1_POLICYLOCAL_BUILD_CONTROL_PACKET_COMPLETION_2026-06-03.md` |
| External workspace copy | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\PolicyLocal\CVF_POLICYLOCAL_BUILD_CONTROL_PACKET_2026-06-03.md` |

## Review Gate

Reviewer confirms:

- [x] No runtime files are created.
- [x] External workspace copy exists.
- [x] Packet preserves LPCI1 citation, freshness, receipt, abstain, and local
  ownership boundaries.
- [x] Next runtime implementation remains dependency-gated.

## Closure Checklist

- [x] Roadmap created.
- [x] Work order created and closed.
- [x] Repo build control packet created.
- [x] Workspace build control packet created.
- [x] Completion review created.
- [x] No runtime or provider work performed.
- [x] Session continuity updated.
- [x] Gates pass.

## Return-To-Orchestrator Conditions

Return to the operator if:

- product scaffold implementation is requested in this same T1 batch;
- a real production corpus must be processed;
- live provider proof or secret access is required;
- public-sync is required.

## Operator Checkpoint

No operator checkpoint remains open for T1. T2/T3/T4 require fresh operator
direction before implementation.

## Claim Boundary

This work order claims only documentation/control packaging for future
PolicyLocal implementation. It does not claim app implementation or production
readiness.

## Finding-To-Governance Learning Disposition

Defect class: `RULE_GAP` - no single packet forced PolicyLocal implementation
to consume LPCI1 evidence and CVF answer-boundary rules.

Learning lane: `GOVERNANCE_CONTROL_PLANE`

Disposition: `RULE_ADDED`

Next control action: `CLOSED`

Runtime/provider/cost learning: `N/A_WITH_REASON`

Reason: documentation/control only.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: references private local workspace path and internal LPCI chain.
