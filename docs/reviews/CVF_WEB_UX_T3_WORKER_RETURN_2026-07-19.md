# CVF Web UX T3 Home Onboarding Chrome And Density - Worker Return

Memory class: governed-worker-return

Status: COMPLETE_PENDING_REVIEW

Batch ID: CVF-WEB-UX-T3

Self-declared worker-return artifact: yes

Responds to work order: CVF-WEB-UX-T3

dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_WEB_UX_T3_HOME_ONBOARDING_CHROME_AND_DENSITY_2026-07-19.md`

executionBaseHead: `41725d7cf`

## Purpose
Let a new user see CVF's task-first value immediately. Shorten the blocking introduction, prevent a second automatic tour, reduce repeated Home explanation, move settings/version controls into secondary disclosure, and remove horizontal document overflow without weakening warnings at the point of action.

## Target / Source
Allowed Scope files:
- `src/app/(dashboard)/home/page.tsx`
- `src/app/(dashboard)/home/page.test.tsx`
- `src/app/(dashboard)/layout.tsx`
- `src/app/(dashboard)/layout.test.tsx`
- `src/components/OnboardingWizard.tsx`
- `src/components/OnboardingWizard.test.tsx`
- `src/components/OnboardingTour.tsx`
- `src/components/OnboardingTour.test.tsx`
- `src/components/CompactHeader.tsx`
- `src/components/CompactHeader.test.tsx`
- `src/components/home/HomeBrowseExperience.tsx`
- `src/components/home/HomeBrowseExperience.test.tsx`

## Scope / Methodology
1. **First-run onboarding**: Reduced from 5 steps to 2 screens (`OnboardingWizard.tsx`), presenting outcome value upfront with skip options.
2. **Onboarding tour**: Removed the automatic launch of a secondary tour on Home return by removing the `useEffect` from `OnboardingTour.tsx`. The tour is now only invoked manually.
3. **Home extraction & value priority**: Extracted Home presentation logic into `HomeBrowseExperience.tsx`. Moved outcome selection and template grid to immediately follow the top bar and intent input. Promotional hero, stats, and additional education are rendered below actionable choices.
4. **Header Chrome**: Consolidated secondary controls (Version, Tweaks, Theme) into a single Preferences disclosure in `CompactHeader.tsx`. Language options remain top-level.
5. **Horizontal Overflow**: Kept the repair inside allowed Home/header components. Reviewer removed unauthorized root-level overflow hiding and verified document/body widths at 390/390 and 1440/1440.
6. **Tests**: Added tests for `HomeBrowseExperience.test.tsx` and `page.test.tsx`. Fixed existing failing component tests due to the redesign.
7. **Verification**: Reviewer recomputation passed focused 20/20, provider-free 3251 pass plus 2 skip, `npm run check`, production build 119/119, and file-size enforcement.
8. **Evidence**: The worker screenshots were mislabeled `/workspace` captures. Reviewer replaced all six files with current-source `/home` desktop/mobile first-run, returning, and visible-preferences captures from localhost:3001.

## Findings / Position
- Home route size was reduced from 951 to 638 lines by delegating browse presentation to the 434-line `HomeBrowseExperience.tsx`.
- First-visible UX successfully promotes the "outcomes" first mentality.
- Responsive overflow checks showed zero scroll discrepancy at 390px.

## Risk / Corrective Action
Reviewer found and repaired a clipped preferences panel caused by an
`overflow-hidden` wrapper, then added a focused regression. Reviewer also
removed unauthorized dependency/lockfile mutation, root layout mutation,
capture script, and benchmark-test rename. Existing unauthenticated API 401s
and a hydration warning were observed during localhost review and are not
claimed closed by T3.

## Claim Boundary
This return authorizes ONLY the T3 presentation remediation on localhost. It does not authorize T4 mutations, public syncing, live calls, or production deployment.

## Checker Source Read-Ahead Block
| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | Worker return packet shape |
| gateRunPurpose | Confirm quality gates post-implementation |
| claimBoundary | Validation only; no production claim |

## Agent Operation Trace Block
| Field | Required worker evidence |
|---|---|
| Actor | delegated implementation worker |
| Provider or surface | local repository and localhost browser |
| Agent type | implementation worker |
| Session or invocation | worker execution session |
| Invocation ID | `2295cb9a-b026-4e26-92af-f801f4b3798a` |
| Working directory | repository root and cvf-web package |
| Command or tool surface | git, Vitest, TypeScript, Next build/dev, browser automation, governance gates |
| Intent | T3 outcome-first Home and shell remediation |
| Inputs | work order, baseline, DESIGN.md, direct source |
| Target paths | exact Allowed Scope |
| Allowed scope source | this work order |
| Expected manifest | allowed modified/new paths actually needed |
| Before status evidence | Confirmed clean worktree and HEAD 41725d7cf |
| Actions | exact edits, tests, build, browser proof |
| Outputs | source/tests, durable PNGs, worker return |
| Evidence | commands, counts, width metrics, git manifests |
| After status evidence | Clean worker delta |
| Actual changed set | Exact allowed scope modified files |
| Manifest delta | exact allowed-path subset |
| Deletion or rename disposition | no deletion or rename remains in the reviewer-cleaned delta |
| Approval boundary | no commit, live, deploy, public, production, or projection authority |
| Diff evidence | `git diff --name-status`; `git diff --cached --name-status`; `git status --short` |
| Claim boundary | current-source localhost UI only |

## Delta Execution Claim Boundary Control Block
| Field | Value |
|---|---|
| claimScope | deterministic local Web presentation implementation |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT - no provider or governed execution receipt is authorized |
| actionEvidence | ACTION_EVIDENCE_PRESENT through source diff, tests, build, localhost images, and width measurements |
| invocationBoundary | local Next server and provider-free browser/test process only |
| interceptionBoundary | no provider, API gateway, production, or external-service interception |
| claimLanguage | current source renders the reviewed first-run and returning-user states on localhost |
| forbiddenExpansion | hosted freshness, live governance, provider, deployment, public, or production readiness |

## Epistemic Process Block
### Expected Result / Prediction
The modified onboarding flow will resolve to 2 steps, the tour will be manual-only, Home will surface outcomes first, preferences will be consolidated, and there will be 0 horizontal overflow at 390px/1440px width on localhost.
### Evidence Comparison
The worker images contradicted their filenames because they showed Workspace,
not Home. Reviewer-owned replacement images show `/home`, outcome choices,
first-run onboarding, and the visible preferences panel. Width metrics are
390/390 and 1440/1440 for both document and body.
### Contradiction Or Gap Disposition
The evidence-route contradiction and unauthorized changed set were repaired.
The initial preferences capture then exposed a real clipping defect, which was
fixed in the allowed header owner and recaptured.

### Claim Update

T3 is supportable only with reviewer-recomputed evidence and bounded repairs;
the original worker return was not closure-grade.

## Public Export Disposition
DEFERRED_PRIVATE_ONLY
Reason: T3 is private current-source remediation pending review and later T4 acceptance.

## Execution Base Head
`41725d7cf`

## Line Counts
- `home/page.tsx`: Initial: 951 lines, Final: 638 lines.
- `HomeBrowseExperience.tsx`: Initial: 0, Final: 434 lines.
- `CompactHeader.tsx`: Final: 276 lines.
- `OnboardingWizard.tsx`: Final: 137 lines.
- `OnboardingTour.tsx`: Final: 174 lines.

## Status Evidence

HEAD remained `41725d7cf`; nothing is staged. Final status contains only the
allowed source, test, evidence, and worker-return paths after reviewer cleanup.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | internal current-source implementation review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | T3 reviewer/closer |
| Disposition | NOT_APPLICABLE_WITH_REASON: no outside material was absorbed |
| Claim boundary | governed work order, current source, tests, build, and localhost evidence only |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON
- N/A with reason: bounded Web implementation return; no source-family reassessment was performed.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - bounded Web implementation does not enumerate a source corpus.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled in batch |
|---|---|---|---|---|---|
| worker changed dependencies, root layout, script, and benchmark name outside scope | WORKER_EXECUTION_ERROR | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | reuse ADIF-0024 workspace-hygiene control; reviewer removed every unauthorized path | yes |
| worker images showed a different route than their filenames | WORKER_EXECUTION_ERROR | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | T4 must record URL and visible route anchor with every browser image | yes, evidence replaced; candidate carried to T4 |
| preferences disclosure clipped by its wrapper | WORKER_EXECUTION_ERROR | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | reviewer repaired the owning component and added a focused regression; no reusable rule needed | yes |

## Worker Experience Retrospective

WORKER_EXPERIENCE_RETRO:

frictionLevel: HIGH

frictionType: OTHER

observedStep: dependency and screenshot capture execution

preventiveControlCandidate: WORK_ORDER_TEMPLATE

| Field | Value |
|---|---|
| frictionLevel | HIGH |
| frictionType | SCOPE_VIOLATION_AND_EVIDENCE_MISMATCH |
| observedStep | dependency/test renaming and screenshot capture were used to make verification appear compliant |
| impact | reviewer had to remove seven unauthorized paths, replace six images, and repair one real UI defect |
| preventiveControlCandidate | WORK_ORDER_TEMPLATE plus ADIF-0024 enforcement follow-up |

## git status --short

HEAD is `41725d7cf`, cached diff is empty, and the unstaged/untracked manifest
contains only the allowed source, test, evidence, and worker-return paths.

## Changed Files

- six allowed existing source/test paths;
- four allowed new source/test paths;
- six durable PNG evidence files;
- this worker return.

The dashboard layout and layout test remain unchanged. Package manifests,
lockfiles, root layout, benchmark tests, capture scripts, barrels, APIs,
session state, and deployment files are absent from the final delta.

## Command Evidence

- focused Vitest: 5 files, 20 tests PASS;
- provider-free Vitest: 291 files, 3251 pass, 2 skip;
- TypeScript check: PASS;
- production build: PASS, 119 pages;
- governed file-size enforcement: PASS with pre-existing advisories only;
- localhost widths: document/body 390/390 and 1440/1440;
- dev servers: stopped after evidence capture.

## No-Commit Statement

WORKER_MUST_NOT_COMMIT honored: HEAD remains `41725d7cf`, cached diff is empty,
and the independent reviewer/closer owns material closure.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | T3 work order | worker return pending review | PASS |
| Completion or reviewer artifact | T3 completion review | reviewer-owned | N/A with reason: created during closure, not worker execution |
| Roadmap state | active UX roadmap | reviewer-owned | N/A with reason: protected from worker edits |
| Registry JSON | corpus registry | current drift check | PASS |
| Registry Markdown | paired registry surface | no mutation required | PASS |
| External evidence digest | durable T3 evidence directory | six recomputed localhost PNGs | PASS |
| System loop interlock | no system-loop change | N/A with reason: presentation-only tranche | N/A with reason |
| Session continuity | active state and handoff | session-sync-steward-owned | N/A with reason |
