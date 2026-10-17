# ACTIVE SESSION FRONT DOOR
Memory class: active-session-front-door
Status: ACTIVE
Last compacted: 2026-08-11
## Startup Order
Read progressively, stopping once current facts are resolved; the full
history/state aggregate is a targeted lookup, not a default startup step:
1. `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` (compact current
   facts: current mode, active handoff, next allowed move)
2. this front door
3. `AGENT_HANDOFF_V63_2026-09-18.md`
4. only the current-authority paths those two surfaces name for the task
5. `CVF_SESSION/ACTIVE_SESSION_STATE.json` only as a targeted lookup, when a
   current fact above is missing, contradictory, or the task explicitly
   requires historical evidence
Canonical read-budget standard:
`docs/reference/CVF_ACTIVE_CONTINUITY_READ_BUDGET_STANDARD_2026-08-10.md`.
Machine guard: `governance/compat/check_active_session_state.py`.
Read `DESIGN.md` only when touching Web, UI, or dashboard work. Read
`docs/reference/guard_orientation/README.md` before authoring a governed
artifact.
## Active Pointers
| Field | Path |
|---|---|
| Bootstrap read model | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Canonical state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` |
| Active handoff | `AGENT_HANDOFF_V63_2026-09-18.md` |
| Active review queue | `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` |
| Pain-point closure direction | `docs/reviews/archive/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_DIRECTION_CODEX_2026-05-20.md` |
| Historical handoffs | `CVF_SESSION/handoffs/archive/` |
| Prior handoff (archive-qualified) | `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V62_2026-09-17.md` |
| Latest front-door archive | `CVF_SESSION/handoffs/archive/CVF_SESSION_MEMORY_COMPACTION_ARCHIVE_2026-08-11.md` |
| Current authority evidence | `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json` `currentAuthority` |
| Parent maintenance | S12 blocked/source18 restored; S13 fixture-only phase1 pending; S11/Q04/R1E accepted old source; R02 spent |
| Freeze posture | `governance_kernel_freeze_recommended` |
## Startup Acknowledgment

Startup acknowledged: current mode=`cvf_ncr_html_login_fixture_control_dispatched`; active handoff=`AGENT_HANDOFF_V63_2026-09-18.md`; next allowed move=bound phase1 fixture-only worker2 after committed release; role=INTERNAL_AGENT Local dispatcher/reviewer; phase=CONTINUITY; decision owner=LOCAL; parked checkpoint=source18 mutations and all product/runtime/provider/native/HTTP/Docker/real-data/deletion/public/deploy effects.

## Current Mode

Current mode marker: `cvf_ncr_html_login_fixture_control_dispatched`
Current mode: `cvf_ncr_html_login_fixture_control_dispatched`; previous mode marker: `cvf_ncr_html_login_readiness_source_blocked`

## Next Allowed Move

Mode: `cvf_ncr_html_login_fixture_control_dispatched`

Actual fixture dispatch material SHA 53054f56470adfa415c83d521733f55856830495. PROGRAM_ID=CVF-NCR; NEXT_ACTION_CLASS=EXECUTE; BATCH_ID=CVF-NCR-HTML-LOGIN-FIXTURE-CONTROL-20261017. Under `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_HTML_LOGIN_FIXTURE_CONTROL_2026-10-17.md` and `docs/baselines/CVF_GC018_NCR_HTML_LOGIN_FIXTURE_CONTROL_2026-10-17.md`, release one INTERNAL_AGENT fixture worker only after actual exact10/6 dispatch and bound pre-dispatch/pre-implementation PASS on current B/W hashes. Worker exact2 WR/WE plus one fresh ignored actual LoginPageClient SSR/hydrate/controlled-submit harness; all18 sources frozen. Node worker max2 <=60s each, optional one named fixture-only repair/repeat preserving first failure; Python semantic0; Root distinct private six-case Node1 once<=60 after valid return. Preparation anchor04:00Z includes prior diagnosis, workerhard06:15Z, Localhard07:00Z, no reset. Same-problem SCEC ordinal1 with three unresolved blockers, ROOT_CONTRACT_REQUIRED/INTEGRATED_ROOT_CONTRACT. S12 failed accepted=false, no retry; S11/Q04/R1E old-source acceptance; R02 spent. gen9/SCECordinal2/counters2,0,2,0/blockers2/freeze/prior7 exclusions/LHW24; R1/R2 partial, R3/R4 open, R5/R6 deferred unchanged. No journey.run, browser/product runtime, real auth/backend, network/provider, native utility/socket, HTTP, Docker, real data, deletion, public/deploy.

## Parked Checkpoints

NCR-R0 limited pilot selection is retained; real-data writer/custody, business acceptance and effect-specific cost decisions remain action-specific checkpoints. U1 code import/runtime use, out-of-manifest production TypeScript edits, unrelated existing-guard edits, hook/autorun/CI wiring, provider/live, credential access, quota mutation, CLI/MCP invocation, public sync, deployment, production, trusted-evidence readiness and cross-runtime determinism claims remain parked.
T4 closed as standalone static checker work with no hook wiring or production-source mutation.
Prior unrelated checkpoints remain historical.

The `broad external knowledge absorption` lane remains outside the current release; blocked work classes remain G1-G6 continuation, G7 implementation/experiment work, Party B/C, credential handling, Group 4 source/T3E, provider/runtime/deployment, and any new absorption tranche without fresh operator authority.

External absorption preparation closed at `b4fb661bb`, path correction `100d6bd8b`: public `main` is `132371c3`; protocol-1.3 packet `D:\UNG DUNG AI\EXTERNAL_AGENT_READ` is live-refreshed with 5/5 hashes matching. Each new repo still needs its own immutable pin, license evidence, and new task capsule.

## Targeted Lookup Rules

- For complete canonical state, read `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- For prior T2A closure narrative, read `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V58_2026-08-11.md`; do not restate it here.
- For pre-2026-08-11 front-door history, read the front-door archive above.
- For guard/task orientation, read `docs/reference/guard_orientation/README.md`.

## Claim Boundary
This compact current-only pointer carries no closed-tranche narrative; historical evidence lives in the dated archives listed above.

## Dispatch Eligibility Learning Discovery
Read `docs/reviews/learnings/README.md` before fresh-context/blind-review dispatch. T1H blocked1 retained; generic pre-transfer rule added at 8c0904c53; machine binding candidate only. R1 authority and parked lanes unchanged.
