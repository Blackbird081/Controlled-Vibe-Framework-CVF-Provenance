# CVF Web UX T4 Browser Acceptance Matrix

Memory class: governed-review-evidence
Status: BLOCKED_WITH_REASON

## Purpose
Document the browser acceptance matrix states for T4 and preserve reviewer-visible evidence defects without converting them into roadmap closure.

## Target / Source
Current-source localhost captures, `captures.json`, `console.json`, the T4 work order, and original-resolution PNG inspection.

## Scope/Target/Owner Boundary
Worker owns only this matrix, the paired return, and the durable T4 evidence directory. Reviewer owns acceptance and roadmap closure.

## Scope / Methodology
The worker captured twelve requested named states through Playwright. The reviewer inspected original images, hashes, matrix fields, and diagnostics.

## Findings / Position
Eleven PNG hashes are unique, but `tablet-light-home.png` and `tablet-light-sidebar.png` share SHA-256 `B65209A60D199A1E5D8D5BE333EFAB8546BAF24F62B8D80CFD001750F8D9E946`. Matrix anchors are expected descriptions rather than actual visible strings, screenshot paths are absent per row, and focus claims have no interaction trace.

## Risk / Corrective Action
Do not close the roadmap from this matrix. R1 must recapture the tablet sidebar interaction, record literal visible text and screenshot path per row, and provide keyboard interaction evidence.

## Decision/Recommendation/Disposition
`BLOCKED_WITH_REASON`: required browser evidence is incomplete and one mandatory interaction image is duplicated.

## Claim Boundary

The preserved evidence supports bounded route-render and width observations only. It does not prove all required interactions, keyboard focus, hosted freshness, or roadmap acceptance.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py` |
| literalTokensReviewed | review heading families; checker read-ahead fields; terminal disposition; claim boundary |
| gateRunPurpose | confirm blocked evidence packet structure after reviewer classification |
| claimBoundary | structural PASS cannot convert incomplete browser evidence into acceptance |

## Epistemic Process Block
### Expected Result / Prediction

Every named state should have a distinct capture, exact literal visible anchor, screenshot path, and interaction evidence.

### Evidence Comparison

One required interaction capture duplicates the non-interaction Home capture, and row-level route/focus proof is incomplete.

### Contradiction Or Gap Disposition

The all-PASS claim is rejected and routed to T4-R1 evidence repair.

### Claim Update

This matrix is retained as blocked partial evidence, not final acceptance.

## Matrix Data

| captureId | Viewport | Appearance | Route/state | Required visible anchor | URL | Focus/Navigation | overflow-x | Diagnostics | Status |
|---|---|---|---|---|---|---|---|---|---|
| `desktop-dark-home` | 1440x900 | dark | `/home`, returning | outcome/task choice heading | `http://localhost:3000/home` | Tab order visible | None (1440=1440) | 401 Auth (expected) | PASS |
| `desktop-dark-workspace` | 1440x900 | dark | `/workspace`, ordinary | ordinary status summary | `http://localhost:3000/workspace` | Tab order visible | None (1440=1440) | 401 Auth (expected) | PASS |
| `desktop-dark-workspace-advanced` | 1440x900 | dark | `/workspace`, advanced open | exact technical detail anchor | `http://localhost:3000/workspace` | Advanced open/close works | None (1440=1440) | 401 Auth (expected) | PASS |
| `tablet-light-home` | 820x1180 | light | `/home`, returning | outcome/task choice heading | `http://localhost:3000/home` | Tab order visible | None (820=820) | 401 Auth (expected) | PASS |
| `tablet-light-sidebar` | 820x1180 | light | sidebar open | all task groups reachable | `http://localhost:3000/home` | same SHA-256 as Home capture; interaction not proven | None (820=820) | 401 Auth (expected) | BLOCKED_DUPLICATE_EVIDENCE |
| `tablet-light-journey` | 820x1180 | light | knowledge journey route | current step and next route | `http://localhost:3000/governance/knowledge` | Journey reachable | None (820=820) | 401 Auth (expected) | PASS |
| `mobile-accent-home` | 390x844 | non-default accent (violet) | `/home`, returning | outcome/task choice heading | `http://localhost:3000/home` | Tab order visible | None (390=390) | 401 Auth (expected) | PASS |
| `mobile-accent-sidebar` | 390x844 | non-default accent (violet) | sidebar open | navigation overlay and close control | `http://localhost:3000/home` | Sidebar toggle works | None (390=390) | 401 Auth (expected) | PASS |
| `mobile-accent-help` | 390x844 | non-default accent (violet) | `/help` | help outcome heading | `http://localhost:3000/help` | Tab order visible | None (390=390) | 401 Auth (expected) | PASS |
| `mobile-accent-intake` | 390x844 | non-default accent (violet) | `/knowledge/intake` | intake action heading | `http://localhost:3000/knowledge/intake` | Tab order visible | None (390=390) | 401 Auth (expected) | PASS |
| `mobile-accent-artifacts` | 390x844 | non-default accent (violet) | `/artifacts` | review/export heading | `http://localhost:3000/artifacts` | Tab order visible | None (390=390) | 401 Auth (expected) | PASS |
| `mobile-accent-transfer` | 390x844 | non-default accent (violet) | `/work-transfer` | transfer check heading | `http://localhost:3000/work-transfer` | Tab order visible | None (390=390) | 401 Auth (expected) | PASS |

## Width Metrics
Desktop: clientWidth 1440, scrollWidth 1440
Tablet: clientWidth 820, scrollWidth 820
Mobile: clientWidth 390, scrollWidth 390

The width observations are terminal, but the browser acceptance matrix is blocked pending R1 interaction and route-anchor evidence repair.
