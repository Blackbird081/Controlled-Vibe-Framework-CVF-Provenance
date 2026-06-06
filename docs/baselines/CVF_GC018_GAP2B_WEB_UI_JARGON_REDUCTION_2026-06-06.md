# GC-018 Continuation Candidate — GAP 2B Web UI Noncoder Jargon Reduction

Memory class: FULL_RECORD

Status: AUTHORIZED

Date: 2026-06-06

dispatchBaseHead: `29a85511`

## Purpose

Authorize the bounded implementation of GAP 2B: reduce proprietary CVF jargon
on the Web UI noncoder surface by placing plain-language outcome labels as
primary headings and demoting technical governance terms to small muted
subtitles, so new operators and noncoders see what a section does before seeing
its CVF term.

## Operator Authorization

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator direct instruction | 2026-06-06 session: "xử lý 2B luôn" | ACCEPT |
| GAP 2B diagnosis | `docs/audits/CVF_EXTERNAL_REVIEW_GAP_ANALYSIS_AND_PROPOSED_SOLUTIONS_2026-06-05.md` GAP 2B section | ACCEPT |

## Scope

In scope — wizard component heading labels only:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/AppBuilderWizard.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/BusinessStrategyWizard.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ContentStrategyWizard.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/DataAnalysisWizard.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/MarketingCampaignWizard.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ProductDesignWizard.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ResearchProjectWizard.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/SecurityAssessmentWizard.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/SystemDesignWizard.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/home/page.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/landing/page.tsx`

Out of scope:

- Internal governance documents, work orders, handoffs, CLAUDE.md — jargon
  precision there is a feature, not a defect
- AgentChat governance mode labels (developer surface, not noncoder surface)
- Test file assertions (tests check for jargon text as subtitles, still present)
- Any route, API, auth, session, memory, public-sync surface

## Source Verification Block

| Claimed item | Verification class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| `Freeze receipt` heading rendered in wizard noncoder surface | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/AppBuilderWizard.tsx` | line 521, 740 — `Freeze receipt` as visible h4/div heading text | `AppBuilderWizard` | `AppBuilderWizard` component | ACCEPT |
| `Approval checkpoints` heading rendered in wizard noncoder surface | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/AppBuilderWizard.tsx` | line 719 — `Approval checkpoints` as visible h4 heading text | `AppBuilderWizard` | `AppBuilderWizard` component | ACCEPT |
| `Execution handoff` heading rendered in wizard noncoder surface | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/AppBuilderWizard.tsx` | line 753 — `Execution handoff` as visible h4 heading text | `AppBuilderWizard` | `AppBuilderWizard` component | ACCEPT |
| `language` prop controls bilingual rendering | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/AppBuilderWizard.tsx` | line 1 imports — `language` prop used throughout for `'vi' \| 'en'` switching | `language` | `AppBuilderWizard` component | ACCEPT |

## Decisions

| Item | Decision | Boundary |
| --- | --- | --- |
| Heading replacement strategy | Add plain-language label as primary heading; demote CVF term to `<p className="text-xs text-gray-400">` subtitle | Technical term stays visible below — not removed |
| Label mapping | `Freeze receipt` → `What gets locked` / `Kết quả được khóa`; `Approval checkpoints` → `Who needs to approve` / `Ai cần phê duyệt`; `Execution handoff` → `How the AI continues` / `AI tiếp tục như thế nào` | Same mapping across all 8 wizard files |
| `governance receipt` in descriptive text | Replace with `audit record` in home/page.tsx and landing/page.tsx | One occurrence each |
| Test files | No change required — tests use `getAllByText(/Freeze receipt/i)` etc., which still match the subtitle text | Tests remain green |
| Internal docs | Not touched — CLAUDE.md, work orders, governance docs retain exact CVF terminology | Boundary: UI-only |

## Evidence

| Evidence | Result |
| --- | --- |
| TypeScript type check (`tsc --noEmit`) | PASS — no errors |
| Full cvf-web test suite | PASS — all tests green |
| Backward compatibility | PASS — governance terms preserved as subtitles; no functionality changed |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
| --- | --- | --- | --- | --- |
| CVF technical terms (`Freeze receipt`, `Approval checkpoints`, `Execution handoff`) used as primary headings on noncoder wizard surface without plain-language context | RULE_GAP | DOCUMENTATION_ONLY_LEARNING | DESIGN_REVIEW_REQUIRED | Outcome labels now primary; governance terms demoted to subtitle — noncoder entry barrier reduced |

## Claim Boundary

This GC-018 authorizes only:

- replacing primary heading text in wizard `h3`/`h4`/`div` elements with
  plain-language outcome labels;
- adding a muted `<p>` subtitle retaining the CVF technical term;
- replacing `governance receipt` in two descriptive strings with `audit record`.

This does NOT authorize: changes to CVF governance documents, API routes,
authentication, session, memory, public-sync, provider routing, internal
governance logic, test logic, role-based access control, or any other surface.
