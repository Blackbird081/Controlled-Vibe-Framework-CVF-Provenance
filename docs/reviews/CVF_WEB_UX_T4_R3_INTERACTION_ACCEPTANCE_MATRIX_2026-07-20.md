<!-- Text Encoding Exception: Vietnamese UI labels in interaction evidence -->
# CVF Web UX T4 R3 Interaction Acceptance Matrix

Memory class: governed-review-evidence
Status: BLOCKED_WITH_REASON

## Purpose

Interaction acceptance matrix for T4 R3 supplemental evidence: five semantic
keyboard scenarios with real DOM state deltas.

## Target / Source

- Work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_WEB_UX_T4_R3_INTERACTION_TRACE_REPAIR_2026-07-20.md`
- Evidence: `docs/reviews/evidence/CVF_WEB_UX_T4_R3_LOCALHOST_2026-07-20/`

## Scope/Target/Owner Boundary

Evidence-only; no source mutation. All R1/R2 evidence preserved and immutable.

## Scope / Methodology

Five keyboard interaction scenarios captured via Playwright against `localhost:3000`.
State deltas observed via DOM evaluation (`aria-label`, `details.open`, CSS transform
class, `getComputedStyle`, form visibility). Each scenario records before/after state
and literal result anchor.

## Findings / Position

Preferences and drawer have useful state evidence. Home changes to a form but
uses the onboarding heading as its result anchor. Workspace retains only the
open transition. Knowledge targets the step tab rather than the compile action.

## Risk / Corrective Action

R4 must repair only Home result identity, Workspace full open/close, Knowledge
action/result identity, and terminal command evidence.

## Decision/Recommendation/Disposition

BLOCKED_WITH_REASON - bounded R3 evidence retained; R4 required.

## Claim Boundary

Claim: 5 keyboard scenarios with verified state deltas. Predecessor R1/R2 hashes unchanged.
Server stopped; no active listener on :3000.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | worker-return full fields; handoff route; closure conversion; matrix row schema |
| gateRunPurpose | confirm R3 source fidelity and dispatch shape before submission |
| claimBoundary | gate PASS authorizes submission to independent reviewer only |

## Epistemic Process Block

EPISTEMIC_PROCESS_NA_WITH_REASON: Matrix data only; epistemic process recorded in Worker Return.

## Interaction Scenario Matrix

| scenario | route | viewport | targetAccessibleName | targetTagRole | stableSelector | focusedBefore | beforeState | activationKey | focusedAfter | afterState | resultAnchor | terminalVerdict |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| preferences open/select violet/close | /home | 1440x900 | violet | button | `button[aria-label="violet"]` | Cài đặt | panel-closed | Enter | violet | panel-open_violet-selected | violet | PASS |
| 767px drawer open/focus close/close | /home | 767x1024 | Close sidebar | button | `button[aria-label="Close sidebar"]` | Open sidebar | CLOSED_translate-x-full | Enter | Close sidebar | CLOSED_translate-x-full | sidebar transition: CLOSED_translate-x-full -> OPEN_translate-x-0 -> CLOSED_translate-x-full | PASS |
| Home Tao PRD action to form | /home | 1440x900 | Tạo PRD | button | `button:has-text("Tạo PRD")` | Tạo PRD | quick_actions_visible | Enter | form-field | form_visible | onboarding heading, not form-specific | BLOCKED |
| Workspace advanced details open/close | /workspace | 1440x900 | Chi tiết kỹ thuật nâng cao | summary | `details[data-testid="advanced-detail"] > summary` | Chi tiết kỹ thuật nâng cao | details.open=false | Enter | Chi tiết kỹ thuật nâng cao | details.open=true only | closing transition absent | BLOCKED |
| Knowledge Bien soan action to result or terminal local diagnostic | /governance/knowledge | 1440x900 | 1. Biên soạn và duyệt | step-tab button | broad contains-text selector | step tab | ready | Enter | step tab | script label only | no visible result/error anchor | BLOCKED |

## Preferences Capture Record

| captureId | viewport | route | visibleAnchorText | computedAccentRgb | verdict |
|---|---|---|---|---|---|
| desktop-dark-preferences-violet-open | 1440x900 | http://localhost:3000/home | violet | 139 92 246 | PASS |
