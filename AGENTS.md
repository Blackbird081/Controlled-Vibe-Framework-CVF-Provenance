# CVF Agent Instructions

## Session Memory Front Door

The active session front door for new or resumed agents is:

`CVF_SESSION_MEMORY.md`

Resolve the machine-readable state registry before treating any root handoff as
current:

`CVF_SESSION/ACTIVE_SESSION_STATE.json`

The current active handoff in that registry is:

`AGENT_HANDOFF_V13_2026-05-25.md`

Historical handoffs are archived under:

`CVF_SESSION/handoffs/archive/`

This includes `AGENT_HANDOFF.md`, V2-V12, and side-channel handoff files. Do not
append new status to archived handoffs; update the active handoff named by
`CVF_SESSION/ACTIVE_SESSION_STATE.json` or open a later versioned handoff when
the active handoff approaches the limit.

## Mandatory Startup Acknowledgment - 2026-05-26

Before material governed work in any new or resumed session, the agent must read
`CVF_SESSION_MEMORY.md`, resolve `CVF_SESSION/ACTIVE_SESSION_STATE.json`, and
identify the active handoff named by that registry.

The agent must then state to the operator or record in the active handoff/session
state one concise acknowledgment naming:

- current mode;
- active handoff;
- next allowed move;
- any parked operator checkpoint.

Suggested format:

`Startup acknowledged: current mode=<mode>; active handoff=<handoff>; next allowed move=<summary>; parked checkpoint=<none|summary>.`

This is a soft-accountability requirement, not proof of runtime auto-load,
universal tool support, MCP availability, or hidden cross-agent memory transfer.
Trivial direct answers may keep the confirmation internal, but any roadmap,
implementation, review, live run, commit, handoff, or public-sync work must
satisfy this acknowledgment first.

## Mandatory F-1 Diminishing Returns Stop Rule - 2026-05-15

This rule is agent-enforced. Future agents must obey it without waiting for a
human reminder.

Canonical stop-rule packet:

`docs/reviews/CVF_F1_DIMINISHING_RETURNS_STOP_RULE_2026-05-15.md`

F-1 output-quality parity work must not continue as open-ended prompt,
template, model, or token-budget tuning. The current evidence already proves a
useful product boundary: CVF preserves governance evidence and safety on the
EVT-4 corpus, but still carries measurable output-quality tax for some
non-coder deliverables.

Binding instructions:

- Do not continue broad prompt/template/model/token-budget tuning for F-1.
- Do not increase the trusted non-coder DeepSeek `deepseek-v4-pro` token cap
  above the retained stable `3072` setting.
- Do not reintroduce runtime two-pass expansion for F-1.
- Do not rerun full EVT-4 merely hoping reviewer variance closes the gap.
- Do not repeat broad family-contract reshaping; R2 is rejected evidence.
- Retain the lean governed system prompt, DeepSeek `3072` cap, and bounded
  CFG-A direct-empty retry unless a later explicit roadmap supersedes them.

The one bounded continuation was completed on 2026-05-15. Closure packet:

`docs/reviews/CVF_F1_OUTPUT_QUALITY_PARITY_CLOSURE_NOT_MET_2026-05-15.md`

Final F-1 status is `closed: not met, evidence-backed`. Do not claim
output-quality parity and do not continue F-1 micro-tuning.

Carry this bounded claim forward:

`docs/reviews/CVF_EVT4_BOUNDED_VALUE_CLAIM_2026-05-15.md`

The next product roadmap is:

`docs/roadmaps/CVF_NONCODER_OUTPUT_QUALITY_HARDENING_ROADMAP_2026-05-15.md`

Future output-quality work must proceed through that roadmap as product-level
non-coder deliverable hardening, not as F-1 parity tuning. EVT-4 may be used as
a regression benchmark only after meaningful product changes.

Any later attempt to reopen broad F-1 tuning requires fresh explicit human
authorization and a new review/roadmap packet explaining why the stop rule no
longer applies.

## Critical Repository Boundary - 2026-05-09

This workspace is the private provenance/archive repository:

`https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF-Provenance.git`

It contains full historical development material, evidence records, handoffs,
reviews, and internal continuity files. Treat it as locked for private audit and
deep review. Do not use this workspace as the public CVF product front door.

The only GitHub repository intended for public/external CVF information is:

`https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git`

Public-facing architecture, README, contributor, setup, governance, provider,
cost, or evidence-summary changes must be prepared and pushed from the sibling
public-sync clone:

`d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync`

Before any push that is meant for the public repository, run `git remote -v`.
If the current working directory is this provenance workspace or `origin`
contains `Controlled-Vibe-Framework-CVF-Provenance`, stop and switch to the
public-sync clone. Do not push the full provenance tree into the public repo.

## UI / Web Design Contract

For any UI, frontend, web app, redesign, dashboard, landing page, or visual
handoff work, read the root `DESIGN.md` before implementation. Treat
`DESIGN.md` as the canonical CVF visual contract.

Use external design repos, Claude Design prototypes, screenshots, and copied
HTML only as reference material. Absorb patterns into CVF language; do not
copy a third-party brand identity or override CVF's design contract.

## Mandatory Live Governance Proof

Any test, roadmap closure, release gate, demo proof, or public claim that asserts CVF governance behavior must use a real provider API call.

This includes claims about risk classification, approval flow, phase gates, DLP filtering, bypass detection, output validation, provider routing, audit trail updates, or CVF controlling AI/agent behavior for non-coders.

Mock mode is allowed only for pure UI structure checks such as navigation, routing, static badges, layout, and RBAC pages that do not assert AI governance behavior.

Required command for release-quality proof:

```bash
python scripts/run_cvf_release_gate_bundle.py --json
```

This command must include live governance E2E and must fail if no DashScope-compatible live key is available. `DASHSCOPE_API_KEY` is accepted directly; `ALIBABA_API_KEY`, `CVF_ALIBABA_API_KEY`, and `CVF_BENCHMARK_ALIBABA_KEY` are accepted aliases. `--e2e` is a targeted UI-only mock check and is not a substitute for governance proof.

Never commit or print raw API key values. Use operator-supplied environment variables such as `DASHSCOPE_API_KEY`, `ALIBABA_API_KEY`, and `DEEPSEEK_API_KEY`.

Operator-key continuity note: in this provenance workspace, operator-supplied
live keys may already exist in
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/.env.local`. Future agents must
check/load that file before claiming no live key is available. Do not print raw
values, do not copy that file into the public-sync repository, and only pass the
values through process environment for live proof commands.

## Mandatory Live Run Diagnostics - 2026-05-24

Canonical standard:

`docs/reference/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`

Any AI/agent that runs a live provider/API-key/service-token/CLI/MCP/browser
proof must classify failures before rerunning. A failed, partial, timed-out,
empty-output, or rerun-triggering live run must record a secret-safe diagnostic
with stage, class, retryability, user action, provider/model when known, HTTP
status/latency when available, receipt/trace when available, and a safe
human-readable message.

Do not consume more live quota by repeating the same unclear test until the
previous failure has a diagnostic or an explicit reason why diagnostic capture
was impossible.

Benchmark evidence that emits multiple events per live call must report both
the call-level result and the event-model denominator so readers do not confuse
event ratios with execution pass rate.

## Mandatory Knowledge Absorption Blind-Spot Prevention - 2026-05-24

Canonical standard:

`docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`

Any AI/agent that absorbs, reopens, scopes, or implements knowledge from
`.private_reference/legacy/`, archived absorption packets, external capability
sources, Review-CVF pain points, memory, graph, workflow, CLI/MCP/tool,
provider, benchmark, context, or non-coder outcome surfaces must complete the
Knowledge Absorption Blind-Spot Control Block before implementation.

Every future `GC-018` packet touching memory, graph, or intelligence work must
include that Control Block. A missing block makes the packet incomplete and
implementation must not be dispatched.

Do not scope from active summaries alone. Resolve prior absorption evidence,
read detailed source files when present, normalize accepted value into existing
CVF owner surfaces, record accept/defer/reject dispositions, run adversarial
role review, and close with a blind-spot delta. If the block is `PARTIAL` or
`BLOCKED`, the implementation must stop or explicitly record why the remaining
blind spot is low-risk and out of scope.

## Latest Closed Continuation Roadmap

The latest closed continuation roadmap is `docs/roadmaps/CVF_W132_T1_PROVIDER_RUNTIME_STABILITY_AND_BROWSER_SESSION_HARDENING_ROADMAP_2026-04-30.md`.

The previous closed continuation roadmap is `docs/roadmaps/CVF_W131_T1_NONCODER_POST_W130_REAL_TRAFFIC_STABILITY_AND_CLAIM_HARDENING_ROADMAP_2026-04-30.md`.

The active next runtime-stability tranche is W133, authorized conceptually by the W132 continuation decision but still requiring a fresh GC-018 and roadmap file before implementation. W133 scope: SSE/connection lifecycle fix, inter-journey delay/backoff, `user_persona` routing coverage, and stability re-run.

Treat the W113/W116/W117/W118/W119/W122/W123/W124/W125/W126/W127/W128/W129/W130/W131/W132 boundary language as binding:

- Workspace bootstrap is now agent-enforcement-ready when generated artifacts, workspace-root `WORKSPACE_RULES.md`, and the workspace doctor pass. Canonical workspace topology is `docs/reference/CVF_WORKSPACE_RULES.md`: a non-git parent workspace, hidden `.Controlled-Vibe-Framework-CVF` governance clone, and sibling downstream application folders.
- W113 proved this in one real downstream sample project with live API-backed governance evidence.
- W116 proved the downstream knowledge pipeline: `.md` files in `knowledge/` → ingested chunks → positive retrieval delta confirmed by unit evidence tests (16/16 pass).
- W117 proved the writable knowledge store: `KNOWLEDGE_COLLECTIONS` constant replaced by `InProcessKnowledgeStore`; admin CRUD API and UI delivered; Wave 2 live regression 4/4 pass; D1.4b deferred note retired.
- W118 proved unified persistent knowledge store: `_runtimeCollections` Map eliminated; `InProcessKnowledgeStore` unified with ephemeral path (`registerEphemeral()`); `FileBackedKnowledgeStore` delivers JSON-file persistence for admin-CRUD collections; `KnowledgeStoreAuditEntry` append-only audit trail delivered; `GET /api/admin/knowledge/audit` route delivered; Wave 2 live regression 4/4 pass; CP2 evidence hardening added real file I/O regression coverage (11 CP4 tests + 3 audit route tests in targeted W118 coverage).
- W119 proved the bounded non-coder adoption journey: secret-free first-run readiness; project knowledge ingest into governed `/api/execute`; route-returned `governanceEvidenceReceipt`; ProcessingScreen/ResultViewer evidence visibility and copy/export; live W119 runner 3/3 locked journeys pass on Alibaba lane with raw keys not printed.
- W122 proved the noncoder intent-first front door: `intent-router.ts` as single routing source of truth; `IntentEntry` component extracted and rendered behind `NEXT_PUBLIC_CVF_INTENT_FIRST_FRONT_DOOR` feature flag (default `false`); weak-confidence fallback = no routed target (all target fields null, CTA disabled); wizard-family (9-entry) trusted routing subset enforced; evidence parity between routed and direct handoff paths proven (10/10); live E2E 6 passed / 2 skipped on Alibaba `qwen-turbo`; release gate 7/7 PASS. Feature flag default is `false` — rollout-safe. Known limit: VN `ứng dụng` `\b` boundary requires ASCII keywords for strong routing.
- W123 proved noncoder iteration memory and follow-up continuity: `execution-continuity.ts` helper module with `buildContinuationExecution`, `buildRootExecution`, thread selectors, `buildEvidenceSnapshot`, and `buildContinuityParityObject`; `Execution` type extended with `threadId`, `rootExecutionId`, `parentExecutionId`, `projectLabel`, `knowledgeCollectionId`, `evidenceReceiptSnapshot`, `starterSource`; Zustand store extended with `getThreadExecutions` + `setProjectLabel`; `handleFollowUp` in `home/page.tsx` creates durable continuation chain; `HistoryList` shows thread-label + follow-up badge + continue-work CTA behind `NEXT_PUBLIC_CVF_NONCODER_ITERATION_MEMORY` flag (default `false`); vitest 77/77 targeted; Playwright 6 passed / 1 skipped on Alibaba lane.
- W124 proved noncoder clarification loop and safe routing recovery: `intent-router-clarification.ts` with `startClarification`, `submitClarificationAnswer`, `buildEnrichedInput`, `buildNextQuestion` (max depth=2), `buildClarificationState`, `advanceClarificationState`; eligible cases = `weak_confidence` VN/EN only; browse-only cases = `unsupported_language`, `empty_input`; `IntentEntry` extended with clarification question + option buttons behind `NEXT_PUBLIC_CVF_NONCODER_CLARIFICATION_LOOP` flag (default `false`); 5 analytics event types added; vitest 23/23 clarification + 45/45 targeted; Playwright 2 passed / 2 skipped. Feature flag default `false` — rollout-safe. No parallel detector introduced; enrichment delegates to W122 `intent-router.ts`.
- W125 proved noncoder deliverable packs and handoff productization: `deliverable-pack.ts` typed contract (`DeliverablePack`, `PackType`, `PackGovernanceEvidence`); `inferPackType()` with template-match → category-fallback → `documentation_handoff` default; `generateDeliverablePack(execution, receipt?)` builds all pack fields; `serializePackToMarkdown()` 7-section export; `ResultViewer` upgraded with Result/Pack tab toggle and pack preview panel (6 sections); export menu extended with distinct "Download Deliverable Pack (.md)" option; 28/28 unit tests + 36/36 ResultViewer tests + E2E spec 4 journeys; release gate PASS.
- W126 proved trusted form-template routing expansion: `form-routing.ts` adds the bounded trusted-form subset (`email_template`, `documentation`, `competitor_review`, `risk_assessment`, `user_persona`, `feature_prioritization`, `pricing_strategy`, `strategy_analysis`); `routeIntent()` now enforces wizard -> trusted form -> weak-fallback precedence; form routes return `routeType: 'form'` with `starterKey: null`; Home handoff guard became route-type aware; vitest 28/28 pass. Routing claim remains bounded to the audited trusted subset, not the full template corpus.
- W127 proved noncoder adoption metrics and friction baseline: `noncoder-metrics.ts` computes 6 browser-local metrics (`time_to_first_value`, `route_recovery_rate`, `weak_fallback_rate`, `followup_continuation_rate`, `evidence_export_rate`, `deliverable_pack_export_rate`); `generateMetricReport()` + `summarizeFriction()` provide threshold-based readout; analytics instrumentation now includes `intent_routed`, `followup_started`, `evidence_exported`, and `deliverable_pack_exported`; Day-0 baseline artifact is published with N/A values until real traffic accumulates. Release gate PASS.
- W128 proved noncoder rollout readout and optimization loop: `noncoder-rollout-readout.ts` adds typed lane readouts and bounded `RolloutRecommendation` output across 6 lanes (`entry_routing`, `clarification_recovery`, `trusted_form`, `followup_continuity`, `evidence_export`, `deliverable_pack`); recommendations are feature-flag aware via `readNoncoderFlags()` and deterministic threshold logic; `AnalyticsDashboard` now exposes a `Noncoder Health` readout with low-data caveat, summary strip, flag posture, lane cards, and prioritized next actions. Targeted verification: 56/56 pass; release gate PASS 7/7.
- W129 proved noncoder controlled rollout posture and full Stage A → B → C signal capture: GC-018 issued 2026-04-27 (depth audit 9/10); rollout playbook (flag order + enable/hold/rollback criteria) + Stage A operator-local flag posture (`NEXT_PUBLIC_CVF_INTENT_FIRST_FRONT_DOOR`) + two rollout analytics events (`rollout_flag_enabled`, `rollout_session_start`) + dedicated live signal capture spec (`w129-stage-a-signal-capture.live.spec.ts`) with governed execution `ALLOW`, `intent_routed=5`, `clarification_browse_fallback=0`, and lane readout `entry_routing=healthy`, `trusted_form=healthy`. §7 post-closure addendum: `w129-stage-a-volume-capture.live.spec.ts` — `execution_created=12`, `entry_routing=healthy`, `stageBDecision=STAGE_B_MAY_ENABLE`. §8 Stage B signal capture (2026-04-28): `NEXT_PUBLIC_CVF_NONCODER_CLARIFICATION_LOOP=true` enabled; `w129-stage-b-signal-capture.live.spec.ts` — 8 short-input (≤5 char) journeys, `clarification_question_asked=8`, `clarification_recovery=healthy`, `stageCDecision=STAGE_C_MAY_ENABLE`. §9 Stage C signal capture (2026-04-28): `NEXT_PUBLIC_CVF_NONCODER_ITERATION_MEMORY=true` enabled; `w129-stage-c-signal-capture.live.spec.ts` — 5 browser-driven UI journeys with 3 successful follow-up submissions, plus one final live governed proof call; `followup_started=3`, `followup_continuity=healthy`, `rolloutDecision=W129_ROLLOUT_COMPLETE`. Boundary: the Stage C packet alone may show `clarification_recovery=no_data` because it does not replay weak-confidence prompts; rollout completion relies on aggregate Stage A+B+C evidence, with Stage B already proving `clarification_recovery=healthy`. All 3 noncoder flags now enabled in operator environment. W129 rollout is FULLY COMPLETE. W130 requires fresh GC-018.
- W130 proved noncoder evidence and pack export activation: GC-018 issued 2026-04-28 (depth 9/10); export activation contract published in `docs/reviews/CVF_W130_EXPORT_ACTIVATION_CONTRACT_2026-04-28.md`; `ResultViewer.tsx` now surfaces a noncoder export nudge and defaults to Pack view for noncoder sessions; `ProcessingScreen.tsx` now waits for hydrated local settings before launching live execution, preventing false fallback to default Gemini settings during governed browser runs; `ResultViewer.tsx` now uses a clipboard fallback path so evidence-copy analytics still fire when browser clipboard permissions are limited. Live proof: `w130-evidence-pack-export.live.spec.ts` PASS on Alibaba lane with `evidence_exported=1`, `deliverable_pack_exported=1`, `execution_accepted=1`, `evidence_export=healthy`, and `deliverable_pack=healthy`. Boundary: the W130 evidence packet contains 1 successful governed journey that fired both export events, plus 2 `mock_fallback_no_receipt` journeys retained for transparency; W130 proves both export lanes can exit `no_data`, not uniform live stability for every trusted-form prompt. W131 requires fresh GC-018.
- W131 proved post-W130 claim hardening by finding the current instability boundary: GC-018 issued 2026-04-30 (depth 10/10); W131 evidence packets show Alibaba `qwen-turbo` and DeepSeek `deepseek-chat` both at 1/6 accepted with 2 `api_timeout`, 2 `mock_fallback_no_receipt`, and 1 `route_miss`; Alibaba's long matrix also collapsed browser context after the first 6 real journeys. The continuation decision is data-backed: W132 = provider/runtime stability and browser session hardening. W131 does not prove stable multi-form noncoder operation.
- W132 proved browser-session isolation and diagnostics while classifying the remaining provider/runtime blocker: CP1-CP7 delivered, browser cascade failure eliminated, diagnostic subcodes and navigation hardening confirmed. Persistent blocker is `sequential_journey_failure_server_side_connection`: J1 succeeds, J2+ times out at about 93s across Alibaba and DeepSeek/model variants, indicating server-side SSE/streaming connection lifecycle. Secondary blocker: `user_persona` routing gap. W133 requires fresh GC-018 before implementation.
- CVF ADD doctrine absorption is officially integrated through docs and bounded runtime activation. Canon docs live in `docs/reference/CVF_GOVERNED_CAPABILITY_INTAKE_DOCTRINE_2026-05-07.md`, `docs/reference/CVF_BOUNDARY_FIRST_GOVERNANCE_DOCTRINE_2026-05-07.md`, `docs/reference/CVF_GOVERNED_CONTEXT_PROFILE_METADATA_DOCTRINE_2026-05-07.md`, `docs/reference/CVF_AGENT_CONTINUITY_AND_DELEGATION_DOCTRINE_2026-05-07.md`, and `docs/reference/CVF_SCOPED_KNOWLEDGE_PROVIDER_BOUNDARY_DOCTRINE_2026-05-07.md`. Runtime RT0-RT7 is delivered in `docs/roadmaps/CVF_ADD_RUNTIME_ACTIVATION_ROADMAP_2026-05-07.md`: metadata is runtime-readable, registry-persisted, and visible in External Asset Governance UI, without executing external tools or widening provider behavior.
- Web is governance-inherited on the active governed AI path, not the full CVF runtime.
- Future work must improve enforcement without overstating either claim.
