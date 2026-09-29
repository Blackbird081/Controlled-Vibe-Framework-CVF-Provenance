# CVF Web UX T4 R1 Browser Acceptance Matrix

Memory class: governed-review-evidence

Status: BLOCKED_WITH_REASON

Text Encoding Exception: Vietnamese literal visible text is retained as browser evidence.

## Purpose

Preserve the R1 browser evidence and classify it against the exact work-order
requirements after independent reviewer inspection.

## Target / Source

- Work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_WEB_UX_T4_R1_BROWSER_EVIDENCE_REPAIR_2026-07-19.md`.
- Evidence root: `docs/reviews/evidence/CVF_WEB_UX_T4_R1_LOCALHOST_2026-07-19/`.
- Execution base: `576bc1a18`.

## Scope / Methodology

The reviewer recomputed all twelve PNG hashes, inspected every image at
original resolution, parsed `captures.json`, checked the responsive source
breakpoint and default accent, checked port teardown, and ran governed gates.

## Findings / Position

All twelve PNGs exist and have unique hashes. Ten route/render states provide
useful bounded evidence. R1 does not close T4 because the 820px Home/sidebar
pair cannot prove a drawer interaction: source makes the sidebar persistent at
the `md` breakpoint and hides the drawer toggle. The packet also omits required
`console.json`, does not retain a visible preferences-open state, and does not
trace focus through the required primary Home, Workspace-details, and journey
actions.

## Risk / Corrective Action

Hash uniqueness alone must not be treated as semantic state uniqueness. A
narrow R2 must test the persistent 820px sidebar separately from a 767px
drawer interaction and add the missing preferences, focus, and console proof.

## Decision / Recommendation / Disposition

`BLOCKED_WITH_REASON`: preserve R1 as partial evidence and dispatch T4-R2.

## Claim Boundary

This matrix establishes partial current-source localhost rendering only. It
does not establish full interaction acceptance or roadmap closure.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_machine_closure_package.py` |
| literalTokensReviewed | status; claim boundary; blocked disposition; closure rows |
| gateRunPurpose | preserve truthful R1 evidence classification |
| claimBoundary | checker compliance cannot convert missing interaction proof into acceptance |

## Epistemic Process Block

### Expected Result / Prediction

Every required state should show the semantic state claimed by its trace, not
merely produce a distinct image hash.

### Evidence Comparison

The 820px pair has distinct hashes but both images visibly show the persistent
sidebar. Source confirms that drawer controls apply only below `md`.

### Contradiction Or Gap Disposition

The worker's 12/12 PASS classification is rejected; useful evidence remains
retained and R2 is required.

### Claim Update

R1 is partial, terminal blocked evidence.

## Closure Diff Gate

| Requirement | Evidence | Disposition |
|---|---|---|
| twelve fresh PNGs | twelve files; twelve unique recomputed hashes | PASS |
| exact URL and literal anchor | present in `captures.json` | PASS_BOUNDED |
| image path and hash binding | present and recomputed | PASS |
| 820px sidebar interaction | both images visibly show persistent sidebar; source hides toggle at `md` | BLOCKED_PACKET_BREAKPOINT |
| preferences open/selection/closed | only a summary action; no retained open-state image | BLOCKED |
| required keyboard path | traces stop mostly at header/menu controls | BLOCKED |
| console evidence | required `console.json` absent | BLOCKED |
| teardown | no listener on ports 3000/3001 at review | PASS |
| exact scope and unchanged HEAD | only three allowed untracked output groups; HEAD `576bc1a18` | PASS |
| worker-fast and pre-closure | worker return failed required packet gates | BLOCKED |

## Matrix Data

| captureId | viewport | appearance | literal visible anchor | screenshotPath | SHA-256 | reviewer status |
|---|---|---|---|---|---|---|
| `desktop-dark-home` | 1440x900 | dark | `Kết quả cần tạo` | `docs/reviews/evidence/CVF_WEB_UX_T4_R1_LOCALHOST_2026-07-19/desktop-dark-home.png` | `63FEC5ED16F323A5BD112C7C1FDAF1462DB9C18D589EB89369CCBBAECC0119F9` | PASS_BOUNDED |
| `desktop-dark-workspace` | 1440x900 | dark | `Source Authority` | `docs/reviews/evidence/CVF_WEB_UX_T4_R1_LOCALHOST_2026-07-19/desktop-dark-workspace.png` | `FC0E1E66D9F94B6C81E16A648A01BED438F766B1E067A1354E9702A47E1F5067` | PASS_BOUNDED |
| `desktop-dark-workspace-advanced` | 1440x900 | dark | `Chi tiết kỹ thuật nâng cao (mode, handoff, dispatch, lanes, nguồn)` | `docs/reviews/evidence/CVF_WEB_UX_T4_R1_LOCALHOST_2026-07-19/desktop-dark-workspace-advanced.png` | `69429A51E9C6C3E94B25BA9DF5367A35B2FFFF6C5276C0541EB9F5CB79798830` | PASS_BOUNDED |
| `tablet-light-home` | 820x1180 | light | `Kết quả cần tạo` | `docs/reviews/evidence/CVF_WEB_UX_T4_R1_LOCALHOST_2026-07-19/tablet-light-home.png` | `AF42F119E70FA872CC4F2E46BFDCE11929808FF4E513051C0B56B0C706904FB6` | PASS_PERSISTENT_SIDEBAR |
| `tablet-light-sidebar` | 820x1180 | light | navigation text | `docs/reviews/evidence/CVF_WEB_UX_T4_R1_LOCALHOST_2026-07-19/tablet-light-sidebar.png` | `8D2E255771F05914676734C5BBA5C3B8D9A3CA62F9286EC00B36AFDF05CFDD85` | BLOCKED_NOT_A_DRAWER_DELTA |
| `tablet-light-journey` | 820x1180 | light | `Kiểm duyệt` | `docs/reviews/evidence/CVF_WEB_UX_T4_R1_LOCALHOST_2026-07-19/tablet-light-journey.png` | `6F9AF5AEE3B19219B358DF2CE9F623D1ECC9827C5871E70AACCEBFD84F06FC50` | PASS_BOUNDED |
| `mobile-accent-home` | 390x844 | violet | `Kết quả cần tạo` | `docs/reviews/evidence/CVF_WEB_UX_T4_R1_LOCALHOST_2026-07-19/mobile-accent-home.png` | `BF32E0AF2E1671543192EBD00993B6D8C9BC7FB4B8998190758F2C51676AEF7B` | PASS_BOUNDED |
| `mobile-accent-sidebar` | 390x844 | violet | navigation text | `docs/reviews/evidence/CVF_WEB_UX_T4_R1_LOCALHOST_2026-07-19/mobile-accent-sidebar.png` | `62632E26E91A799A042A5537C67A2A781C177B5D84EF267EB23D373CBE00E42E` | PASS_BOUNDED |
| `mobile-accent-help` | 390x844 | violet | `Trung tâm trợ giúp` | `docs/reviews/evidence/CVF_WEB_UX_T4_R1_LOCALHOST_2026-07-19/mobile-accent-help.png` | `8F6D1FC3BA5A7468EA3084E50C161CED1FEDC5EAC2E3C9E8586208F979E63A3B` | PASS_BOUNDED |
| `mobile-accent-intake` | 390x844 | violet | `Đưa kiến thức mới vào hệ thống` | `docs/reviews/evidence/CVF_WEB_UX_T4_R1_LOCALHOST_2026-07-19/mobile-accent-intake.png` | `DFE24106CB2068D9C6FD006645B9B127E5BB4FBBC7C385DA937C72D55347D56D` | PASS_BOUNDED |
| `mobile-accent-artifacts` | 390x844 | violet | `Biến phần đã duyệt thành gói HTML để rà soát` | `docs/reviews/evidence/CVF_WEB_UX_T4_R1_LOCALHOST_2026-07-19/mobile-accent-artifacts.png` | `AE4B8448D599F6EF200AB2A469F4ABDA2C1E840F6B5D1EFFB8AC691C5825CB86` | PASS_BOUNDED |
| `mobile-accent-transfer` | 390x844 | violet | `Bàn giao công việc cho bước tiếp theo` | `docs/reviews/evidence/CVF_WEB_UX_T4_R1_LOCALHOST_2026-07-19/mobile-accent-transfer.png` | `4FD5D191C1B1A5E1BA148AB4EC1B18AA22C66B95D75D687DF807999CBCC3A6F7` | PASS_BOUNDED |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | delegated worker; independent reviewer correction |
| Provider or surface | current-source localhost images and source repository |
| Agent type | browser-evidence worker returned to reviewer |
| Session or invocation | T4-R1 evidence session |
| Invocation ID | N/A with reason: matrix did not retain a distinct identifier |
| Working directory | repository root and cvf-web package |
| Command or tool surface | Next, Playwright fallback, hashing, image inspection, source search |
| Intent | classify the R1 browser matrix truthfully |
| Inputs | R1 work order, images, captures JSON, responsive source |
| Target paths | R1 matrix and evidence root |
| Allowed scope source | R1 work order plus reviewer closure conversion |
| Expected manifest | twelve PNGs, captures JSON, console JSON, matrix, return |
| Before status evidence | clean execution base `576bc1a18` |
| Actions | capture, hash, inspect, source-compare, classify |
| Outputs | blocked R1 matrix and retained evidence |
| Evidence | twelve image hashes, original-resolution images, source breakpoint |
| After status evidence | exact R1 output groups only; no 3000/3001 listener at review |
| Actual changed set | R1 matrix, return, and evidence root |
| Manifest delta | `console.json` missing |
| Deletion or rename disposition | N/A with reason: no deletion or rename |
| Approval boundary | evidence classification only |
| Diff evidence | git status and hash listing |
| Claim boundary | partial localhost evidence; no T4 closure |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| R1 matrix | this file | reviewer classification | PASS |
| R1 evidence | R1 evidence root | hashes and images retained | PASS_BOUNDED |
| T4 acceptance | completion review | not created | BLOCKED |
| Roadmap closure | active UX roadmap | remains active | BLOCKED |
| Next action | T4-R2 work order | supplemental proof required | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: browser acceptance remains incomplete.
