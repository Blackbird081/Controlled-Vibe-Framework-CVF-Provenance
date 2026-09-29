# CVF Web UX Clarity T0 Live And Source Audit

Memory class: review-packet

Status: COMPLETE_PENDING_REVIEW

Date: 2026-07-18

Text Encoding Exception: Vietnamese UI text is retained as direct visual
evidence and as user-facing terminology recommendations.

## Purpose

Audit why the current CVF Web is difficult for a non-technical operator to
understand. Separate hosted deployment observations from current-source local
rendering, then produce a source-backed information-architecture and language
backlog without changing product code.

## Target / Source

- Hosted target: `https://cvfcoding.vn`, observed through operator screenshots
  supplied on 2026-07-18.
- Current-source target: `http://localhost:3000`, captured by browser subagent
  on 2026-07-19 at HEAD `817170d7e` and viewport `1440x900`.
- Canonical presentation contract: `DESIGN.md`.
- Screenshot root:
  `docs/reviews/evidence/CVF_WEB_UX_T0_R3_LOCALHOST_2026-07-19/`.
- Source owners are recorded with full current paths in the route matrix.

## Scope / Methodology

1. Retained operator screenshots as hosted-deployment observations only.
2. Started current source on localhost and used a graphical browser subagent.
3. Captured `/home` before and after onboarding plus all six remaining routes.
4. Recomputed visible headings, actions, warnings, overlays, and state directly
   from screenshots instead of inferring them from source.
5. Mapped each observation to current route and supporting source owners.
6. Applied exact `DESIGN.md` section names and classified later remediation.
7. Performed no form submission, provider call, production mutation, source
   edit, deployment, or public-sync action.

## Findings / Position

### Hypothesis-Verdict Matrix

| Hypothesis | Verdict | Route evidence | Source evidence |
|---|---|---|---|
| Sidebar exposes too many peer concepts and mixed language | CONFIRMED | all eight local captures show the same dense sidebar | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/Sidebar.tsx` |
| `/workspace` exposes internal continuity and dispatch vocabulary | CONFIRMED | hosted V19/MISSING state and local V48/current state both expose internal fields | workspace page plus server read model |
| Help explains implementation names rather than user outcomes | CONFIRMED | `Agent Chat`, `Self-UAT`, `Multi-Agent Workflow`, `SOT3`, and `MAO` are peer cards | help page plus `help-content.ts` |
| Knowledge, review export, and transfer lack one understandable chain | CONFIRMED | separate sidebar routes and disconnected page narratives | route pages plus `Sidebar.tsx` |
| Large cards and repeated prose raise scanning cost | CONFIRMED | help and artifacts captures use large cards and repeated boundary prose | help page and artifact page/panel |
| Version, Tweaks, admin, and language controls dominate global chrome | CONFIRMED | all post-onboarding captures show these controls before task actions | `CompactHeader.tsx` and `Sidebar.tsx` |

### Route Observation And Evidence Comparison Matrix

Browser timestamp: `2026-07-19T01:03:00+07:00`.

| Route / state | Hosted observation | Local browser evidence | Comparison | Current source owner | Exact DESIGN section | UX finding and disposition |
|---|---|---|---|---|---|---|
| `/home`, first run | No hosted overlay evidence supplied | `home_onboarding.png`; overlay heading `Chọn task từ thư viện template`; action `Tiếp ->`; page content obscured | LOCAL_SOURCE_UX_DEFECT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/home/page.tsx`; onboarding component resolved from that route | `## 4. Layout & Navigation`; `## 5. Component Styling`; `## 8. Accessibility & Language` | First-run explanation competes with the outcome-first home page. Retain onboarding only if it becomes shorter, outcome-led, and state-aware. P2. |
| `/home`, dismissed | Hosted heading `Kết quả cần tạo`; actions `Xem outcomes`, `Duyệt template`; no overlay | `home.png`; same heading and actions; no overlay | SOURCE_AND_HOSTED_MATCH | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/home/page.tsx` | `### Page Rhythm`; `### Cards & Panels`; `### Buttons`; `## 8. Accessibility & Language` | Outcome cards are understandable, but mixed Vietnamese/English and repeated card metadata weaken clarity. P2. |
| `/workspace` | `Operator Dashboard`; V19 handoff and multiple `MISSING`/`UNKNOWN` states | `workspace.png`; V48 handoff is active and current lanes are present; no overlay; no primary mutation action | HOSTED_DEPLOYMENT_STALE | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/workspace/page.tsx`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/cvf-workspace-read-model.ts` | `### App Shell`; `### Tables & Dense Data`; `### Empty / Loading / Error`; `## 8. Accessibility & Language` | Data truth differs across hosted/local packaging, while both expose internal handoff and dispatch language to ordinary users. P1: separate data truth, packaging, and presentation remediation. |
| `/help` | `Trung tâm trợ giúp`; large feature cards including SOT3 and MAO | `help.png`; same structure; primary action `Mở docs`; no overlay | SOURCE_AND_HOSTED_MATCH | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/help/page.tsx`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/data/help-content.ts` | `### Page Rhythm`; `### Cards & Panels`; `## 8. Accessibility & Language` | Internal product names dominate user jobs. Rewrite around outcomes and progressively disclose technical names. P2. |
| `/governance/knowledge` | `Knowledge Governance`; four-stage lifecycle and technical form labels | `governance_knowledge.png`; same structure; primary action `Compile`; no overlay | SOURCE_AND_HOSTED_MATCH | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/governance/knowledge/page.tsx` | `### Page Rhythm`; `### Buttons`; `### Filters & Search`; `## 8. Accessibility & Language` | This is an expert/admin tool presented beside ordinary workflows. Route to an advanced surface and localize or explain fields. P2. |
| `/knowledge/intake` | `Đưa kiến thức mới vào CVF mà không làm mất dấu vết`; action `Gửi để nạp` | `knowledge_intake.png`; same heading and action; no overlay | SOURCE_AND_HOSTED_MATCH | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/knowledge/intake/page.tsx` | `### Page Rhythm`; `### Buttons`; `## 8. Accessibility & Language` | The intent is clearer than the governance form, but English `Preview packet review` and reviewer vocabulary remain. P2. |
| `/artifacts` | `Biến phần đã duyệt thành gói HTML để rà soát`; repeated HTML/evidence boundaries | `artifacts.png`; same structure; export controls are below the captured fold; no overlay | SOURCE_AND_HOSTED_MATCH | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/artifacts/page.tsx`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | `### Page Rhythm`; `### Cards & Panels`; `### Buttons`; `## 8. Accessibility & Language` | Explanatory cards precede the primary export task and repeat limitations. Compress explanation and surface the action earlier. P2. |
| `/work-transfer` | `Chuyển phần đã rà soát sang bước tiếp theo với ít phỏng đoán hơn`; mixed English summary/state values | `work_transfer.png`; same structure; selectors drive validation; no standalone primary button is visible; no overlay | SOURCE_AND_HOSTED_MATCH | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/work-transfer/page.tsx` | `### Page Rhythm`; `### Filters & Search`; `### Empty / Loading / Error`; `## 8. Accessibility & Language` | The page exposes workflow mechanics and mixed-language sample content before explaining the user outcome. P2. |

### Workspace Three-Layer Split

| Layer | Evidence | Disposition |
|---|---|---|
| Data truth | hosted V19/MISSING differs from local V48/ACTIVE | preserve exact state but label deployment freshness |
| Deployment packaging | hosted artifact set is stale relative to current source/session | separate deployment repair; do not treat as styling |
| Presentation | internal mode, handoff, dispatch, and next-move vocabulary is the default view | move to reviewer/admin detail; give ordinary users task and outcome summaries |

### Proposed Navigation Tree

1. `Trang chu` - outcomes, active work, and one clear next action.
2. `Lam viec voi AI` - chat, templates, skills, and bounded automation.
3. `Kien thuc va ra soat` - intake, review packet, evidence, and handoff as one
   understandable chain.
4. `Van hanh nang cao` - workspace state, governance forms, MAO runs, history,
   analytics, and runtime modules for reviewer/admin users.
5. `Tai khoan va cai dat` - language, theme, provider settings, and identity.

### Terminology Map

| Current label | Problem | Recommended Vietnamese | English equivalent | Decision |
|---|---|---|---|---|
| Agent Handoff | internal mechanism | Ban giao cong viec | Work Handoff | translate; advanced detail |
| SOT3 Evidence | unexplained abbreviation | Bang chung kien thuc | Knowledge Evidence | translate; show SOT3 secondarily |
| MAO Durable Runs | internal runtime term | Lich su phoi hop AI | AI Coordination History | reviewer/admin |
| Operator Dashboard | role ambiguity | Trang thai van hanh | Operations Status | reviewer/admin |
| activeHandoff | raw state key | Ban giao dang hoat dong | Active Handoff | hide from ordinary view |
| materialCommit | Git/internal term | Phien ban da chap nhan | Accepted Version | reviewer/admin |
| Preview packet review | mixed-language label | Xem truoc goi ra soat | Review Packet Preview | translate |

### Prioritized Backlog And Tranche Map

| Priority | Remediation | Target tranche | Destination |
|---|---|---|---|
| P1 | Correct hosted `/workspace` packaging freshness and separate ordinary-user state from reviewer/admin detail | T1 | deployment plus workspace owners |
| P1 | Rebuild navigation around user jobs and move diagnostic/governance machinery under advanced operations | T1 | sidebar and app shell |
| P2 | Rewrite help, knowledge, artifact, and transfer copy with Vietnamese-first progressive disclosure | T2 | ordinary user plus reviewer |
| P2 | Shorten first-run onboarding and ensure it does not hide the outcome-first value proposition unnecessarily | T2 | new user |
| P3 | Reduce global chrome dominance and repeated cards/boundary prose | T3 | all users |

## Risk / Corrective Action

| Risk | Corrective action |
|---|---|
| Hosted and local observations are conflated | keep separate evidence columns and explicit drift disposition |
| Internal truth is hidden without a replacement route | retain exact details under reviewer/admin advanced operations |
| Vietnamese becomes literal translation | test labels as user jobs; retain English equivalents in the terminology contract |
| Redesign becomes runtime mutation | require fresh GC-018 and source-verified work order before implementation |

## Decision / Disposition

The audit supports a bounded UX remediation roadmap. T1 should own navigation,
workspace audience separation, and hosted freshness. Later tranches should own
language, onboarding, card density, and global chrome. No implementation is
authorized by this audit.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_agent_packet_authority_and_encoding.py` |
| literalTokensReviewed | required audit headings; Text Encoding Exception; evidence and decision sections |
| gateRunPurpose | confirm the already-recomputed audit structure and encoding evidence before reviewer closure |
| claimBoundary | checker compliance confirms packet shape only; reviewer screenshot/source recomputation supports substantive findings |

## Epistemic Process Block

EPISTEMIC_PROCESS_NA_WITH_REASON: bounded visual/source audit with explicit
route matrix and direct screenshot evidence; no corpus-wide completeness or
runtime-governance behavior claim.

## Claim Boundary

This packet records hosted observations, local current-source screenshots,
source ownership, and a remediation backlog. It does not claim production
readiness, complete responsive coverage, provider behavior, implementation,
deployment repair, or public release.
