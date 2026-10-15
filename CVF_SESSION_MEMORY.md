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
| Parent maintenance | Native prerequisite PLAN complete; snapshot source/API mismatch blocks native entry; Local prepares bounded source envelope directly |
| Freeze posture | `governance_kernel_freeze_recommended` |
## Startup Acknowledgment

Startup acknowledged: current mode=`cvf_ncr_html_native_prerequisites_complete_source_contract_plan`; active handoff=`AGENT_HANDOFF_V63_2026-09-18.md`; next=Local consolidate bounded native-binding source-correction envelope; role=INTERNAL_AGENT Local planner/implementer/reviewer/steward, one read-only internal adviser; phase=prerequisite PLAN complete/native entry source-blocked; decision owner=Local; parked checkpoint=actual native/B-E/product/browser/container/provider/stage/parent/public/deploy. Direct implementation, no manual relay.

## Current Mode

Current mode marker: `cvf_ncr_html_native_prerequisites_complete_source_contract_plan`
Current mode: `cvf_ncr_html_native_prerequisites_complete_source_contract_plan`; previous mode marker: `cvf_ncr_html_direct_local_source_repair_accepted_native_prerequisite_plan`

## Next Allowed Move

PROGRAM_ID=CVF-NCR; NEXT_ACTION_CLASS=PLAN; BATCH_ID=CVF-NCR-HTML-NATIVE-PREREQUISITES-20261016. Native prerequisite PLAN material=1bd5095079f58cdb148cdfb007f964827b64c6dc; evidence=docs/reviews/evidence/ncr-html-native-prerequisites-local-20261016.json. Local next consolidates one bounded existing-owner native-binding source-correction envelope, including snapshot failure sentinel and directly connected resume/enumeration error contracts before any edit/test. Win32._ok currently rejects zero only while Microsoft documents INVALID_HANDLE_VALUE for CreateToolhelp32Snapshot used by resume. This is a verified source/API mismatch, not an observed native failure or independent critical evidence. Keep lifecycle owner and focused non-native regression scope; bind exact paths/capacity, failure oracles, authority and a fresh prospective budget first. No new checker, product/guard/legacy entrypoint change, broad ABI campaign or manual implementation relay. N1-N4 standalone Windows ABI/owned benign-child/handle-stop/terminal proof is selected for a later separate before-effect release, never full runner as inventory. Current native/test/child/product/browser/container/provider/deletion0; primary documentation reads3. cap1 control admission remains fail-closed; B-E profile/tools/image/host and actual parent cleanup/disposal unproved. No native effect or control slot granted by this plan; old Local8/8 and52/54 window closed, original grants spent. Prior direct Local source acceptance160 Python/13 Node/14 independent retained at94f7793e; prior six receipts consumed read-only, no control rerun. All failures and source pins retained; Local owns direct implementation/disposition/commit and routine documentary steps without micro-confirmation. Schema-required currentAuthority R5 pair remains consumed historical provenance, no executable order. Same root NCR_HTML_CONFIGURED_RECEIPT_CONTROL_PROOF/generation6/SCEC2/counters2,0,2,0/two blockers/freeze, no transition/new independentCriticalEvidence. Prior7 P4 blocked rows/exclusions and exact adjudications preserved; consume normal collector only, no manual rerun/promotion. R1/R2partial,R3/R4open,R5/R6deferred; foundation active/extension NOT_APPLIED/projectOPEN; data/custody/business/send/B2/P11/public/deploy parked; LHW24 retained. Existing outside-temp fixtures retained by Local after prior policy rejection; no new deletion attempt or alternate removal.

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
