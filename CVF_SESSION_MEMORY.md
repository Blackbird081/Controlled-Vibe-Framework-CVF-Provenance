# ACTIVE SESSION FRONT DOOR

Memory class: active-session-front-door

Status: ACTIVE

Last compacted: 2026-07-11

## Startup Order

Read before governed material work:

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
3. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
4. `AGENT_HANDOFF_V41_2026-07-11.md`
5. `docs/reference/guard_orientation/README.md`
6. `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`

Read `DESIGN.md` only when touching Web, UI, or dashboard work.

## Active Pointers

| Field | Path |
|---|---|
| Bootstrap read model | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Canonical state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` |
| Active handoff | `AGENT_HANDOFF_V41_2026-07-11.md` |
| Active review queue | `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` |
| Pain-point closure direction | `docs/reviews/archive/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_DIRECTION_CODEX_2026-05-20.md` |
| Historical handoffs | `CVF_SESSION/handoffs/archive/` |
| Latest front-door archive | `CVF_SESSION/handoffs/archive/CVF_SESSION_MEMORY_COMPACTION_ARCHIVE_2026-07-10.md` |
| Freeze posture | `governance_kernel_freeze_recommended` |

## Startup Acknowledgment

Startup acknowledged: current mode=`mao_t5_dispatched`; active handoff=AGENT_HANDOFF_V41_2026-07-11.md; next allowed move=release T5 packet status then one MAO-T5 WORKER_MUST_NOT_COMMIT execution; parked checkpoint=MAO-T6-T9 dependencies, provider/network, broader runtime and public work.

## Current Mode

Current mode marker: `mao_t5_dispatched`

Current mode: `mao_t5_dispatched`

`mao_t5_dispatched`

Previous mode:

`mao_t4_closed`

## Latest Material Work

| Work | Commit | Disposition |
|---|---|---|
| MAO-T5-T9 packet chain | `5a5dc0364` | T5 released for status flip/execution; T6-T9 source-complete but dependency-held. |
| MAO-T4 reviewer isolation/dissent/revision closure | `f71ba01f6` | REVIEWER_ACCEPTED_BOUNDED after independent evidence and semantic repair; 78/78 tests, typecheck, worker-return/reviewer-fast and pre-commit pass. |
| MAO-T4 reviewer isolation/dissent/revision dispatch | `68cc94572` | DISPATCH_READY; five exact outputs; worker must not commit. |
| MAO-T3 adapter closure | `052845fa1` | REVIEWER_ACCEPTED_BOUNDED; 21/21 tests, typecheck, reviewer-fast and 82/82 pre-commit pass. |
| MAO-T3 provider-neutral delegation adapter dispatch | `1738d9263` | DISPATCH_READY; fake/local only; four outputs; worker must not commit. |
| MAO-T2 risk-based role resolver closure | `854bb3a92` | REVIEWER_ACCEPTED_BOUNDED after semantic repairs; 22/22 tests, typecheck, GC-051 and 82/82 pre-commit pass. |
| MAO-T2 risk-based role resolver dispatch | `570cd6452` | DISPATCH_READY; four exact outputs; worker must not commit; no provider invocation. |
| MAO-T1 task graph/state foundation closure | `01618e9dc` | REVIEWER_ACCEPTED_BOUNDED; 39/39 focused tests, typecheck, GC-051 coverage, and 82/82 pre-commit checks pass. |
| MAO-T1 task graph/state foundation dispatch | `6383e8180` | DISPATCH_READY; six exact worker outputs; worker must not commit. |
| MAO-T0 contract/schema foundation closure | `dbe963b03` | REVIEWER_ACCEPTED_BOUNDED; four reference/schema artifacts plus accepted return/review. |
| MAO-T0 contract foundation dispatch | `f42195d20` | DISPATCH_READY; delegated worker must not commit; five exact outputs. |
| MAO roadmap critique reconciliation | `d61c3c92c` | REVIEWER_ACCEPTED_BOUNDED; T0 packet authoring released with three caveats. |
| MAO runtime foundation roadmap | `6a08a041e` | PROPOSED after R94/R95 reopen audit; external critique is next; implementation remains parked. |
| MSEA-ASC architecture catalog closure | `6273f3413` | REVIEWER_ACCEPTED_BOUNDED; 22 entities, 3 gaps, deterministic local/CI/weekly freshness. |
| MSEA-ASC-RW integrated remaining wave dispatch | `fa4838c57` | DISPATCH_READY; one no-commit T1-T5 execution, exact T5 wiring owners, one final independent review. |
| MSEA-ASC-T0 source schema and reconciliation contract closure | `9f8815fb7` | REVIEWER_ACCEPTED_BOUNDED after Round 2 JSON Schema invariant correction and independent negative validation. |
| MSEA-ASC-T0 source schema and reconciliation contract dispatch | `cbc5348bf` | DISPATCH_READY; WORKER_MUST_NOT_COMMIT; exactly four reference/schema outputs plus one worker return. |
| MSEA-ASC external critique classification and fold | `6485fc7ad` | REVIEWER_ACCEPTED_BOUNDED. Ten findings accepted/calibrated; roadmap ready for ASC-T0 packet authoring only. |
| MSEA-ASC as-built architecture and system catalog roadmap | `027ead038` | PROPOSED. Machine catalog, proof-class edge graph, indexed gap README/JSON, human front door, freshness/admission controls, and independent critique sequence. |
| MSEA-R99 L1 system-definition owner design closure | `ea57cc634` | REVIEWER_ACCEPTED_BOUNDED. Compact pointer owner created; L1 path/authority/freeze boundaries retained; freshness CURRENT. |
| MSEA-R99 L1 system-definition owner design dispatch | `31ed30db8` | DISPATCH_READY. Create one compact pointer owner and reconcile L1 route/freshness; no doctrine or legacy mutation. |
| MSEA-R98 L2 build-protocol owner ratification closure | `21aeae180` | REVIEWER_ACCEPTED_BOUNDED under single-agent self-review boundary. L2 is NAMED_DIFFERENTLY_ACTIVE_OWNER_WITH_BOUNDARY; freshness CURRENT. |
| MSEA-R98 L2 build-protocol owner ratification dispatch | `cd58b0211` | DISPATCH_READY. Decide whether `AGENTS.md` is the bounded active L2 owner; no doctrine, AGENTS, runtime, checker, or public mutation. |
| MSEA-R97 L6 examples inventory alignment closure | `8295f5534` | REVIEWER_ACCEPTED_BOUNDED under single-agent self-review boundary. One active-reference row added; L6 remains PARTIAL_OWNER_WITH_GAP; freshness CURRENT. |
| MSEA-R97 L6 examples inventory alignment dispatch | `6eea64bf5` | DISPATCH_READY. Single-agent multi-role, five material paths, no consolidation or doctrine change. |
| MSEA-R96 doctrine route gap reconciliation closure | `d733abd70` | REVIEWER_ACCEPTED_BOUNDED. L1/L4 unresolved with search evidence; L2 adaptation candidate pending ratification; L6 partial distributed owner; R91 freshness CURRENT. |
| MSEA-R96 doctrine route gap reconciliation dispatch | `54666a41d` | DISPATCH_READY. Four-layer L1/L2/L4/L6 source decision pass; exact four outputs; no legacy promotion, doctrine/runtime mutation, or worker commit. |
| MSEA-R95 external repository absorption entry hardening closure | `8c5755051` | REVIEWER_ACCEPTED_BOUNDED. Existing ADIF-0014 owner extended; 44/44 tests, reviewer-fast 60/60, closure pre-commit 81/81. |
| MSEA-R95 external repository absorption entry hardening dispatch | `dd92fa6d6` | DISPATCH_READY. Extend ADIF-0014 entry detection and guidance with source-mirror and explicit intake triggers, an R85-style terminal-ledger control block, focused compatibility tests, and no new checker or hook. Worker must not commit. |
| MSEA-R94-T1B gateway helper ownership disposition closure | `3c5e87d7b` | REVIEWER_ACCEPTED_BOUNDED. GC-009/010 CLAIM_DOWNGRADED_WITH_REASON; focused tests 54/54; system-chain freshness CURRENT. |
| MSEA-R94-T1A contract-guard matrix evidence correction closure | `ee39d8e62` | REVIEWER_ACCEPTED_BOUNDED. Six rows FIXED_AND_PROVEN, focused tests 34/34, system-chain freshness CURRENT. |
| MSEA-R94-T1A contract-guard matrix evidence correction dispatch | `f32175bdc` | DISPATCH_READY. Correct exactly six mismatched evidence cells using existing direct contract tests; no test/runtime mutation. |
| MSEA-R94-T0 Contract-to-Runtime 50-row inventory closure | `db4e2369a` | REVIEWER_ACCEPTED_BOUNDED. 50/50 terminal rows, 82-file reproducible manifest, catalog invocation evidence, 50/50 operator evidence, and full pre-commit 81/81 pass. |
| MSEA-R94-T0 Contract-to-Runtime 50-row inventory dispatch | `a58b61ae8` | DISPATCH_READY. No-commit read-only audit with per-row implementation, invocation, test-pairing, and operator/evidence-route proof. |
| MSEA-R94 System Chain Gap Closure roadmap | `383a273c8` | PROPOSED. Prioritizes a 50-row contract-to-runtime audit, then targeted repairs and doctrine reconciliation; operator-surface implementation remains value-gated. |
| MSEA-R93 Gop y CVF storage cleanup | `0f05b7942` | REVIEWER_ACCEPTED_BOUNDED. Preserved 16 active advisory files under external reviews, 27 older files in private legacy, and removed the visible root. |
| MSEA-R92 worker-return scaffold last-mile hardening closure | `4284a5acd` | REVIEWER_ACCEPTED_BOUNDED. FULL and COMPACT share checker-required markers/headings; compact keeps its exact three-section conditional delta; 13 focused tests and reviewer-fast 60/60 pass. |
| MSEA-R92 worker-return scaffold last-mile hardening dispatch | `115dd8d16` | DISPATCH_READY. Profile-neutral five-path helper/test/guidance hardening; no checker, compact eligibility, hook, session, cleanup, or roadmap mutation. |
| MSEA-R91 system-chain map and freshness control closure | `017ae9718` | REVIEWER_ACCEPTED_BOUNDED. Five-lane human/machine map, 28 required fingerprints, 30-day freshness ceiling, 17 tests, local/CI/weekly enforcement, corrected evidence paths, and GC-051 registration closed. |
| MSEA-R91 system-chain map and freshness control dispatch | `4b5b02f7c` | DISPATCH_READY. Claude builds Deliverable B from accepted R90 evidence, adds deterministic freshness detection, local/CI/weekly reminder wiring, corrects confirmed stale paths, and returns without committing. |
| MSEA-R90 system-chain Audit A closure | `645df8b83` | REVIEWER_ACCEPTED_BOUNDED. Five bounded lanes closed; registry-driven invocation proven; 31-record manifest and GC-051 registry entry reconciled; B and freshness implementation require a fresh packet. |
| MSEA-R90 system-chain Audit A completion dispatch | `1398098cf` | DISPATCH_READY after initial packet commit `2abdb8857`. Complete and revalidate all five chain rows; worker produces governed audit, JSON evidence, and worker return without committing. Deliverable B, maintenance automation, legacy relocation, runtime/checker changes, governance-lane changes, and session mutation remain excluded. |
| MSEA-R88 double-click workspace setup wizard | `b7d0e818d` | CLOSED_PASS_BOUNDED. Added a one-file double-click launcher and three-step Windows GUI over the shared R87 setup engine; GUI and launcher smoke proofs passed. |
| MSEA-R87 interactive operator workspace initializer | `b3004069d` | CLOSED_PASS_BOUNDED_AND_PUBLIC_SYNCED. Added one options-driven provenance entrypoint and agent autorun routing; fresh and existing workspace proofs passed; public root-rules fix exported at `a78b35c9d`. |
| MSEA-R86 workspace classification guide | `c5b1fddd1` | CLOSED_PASS_BOUNDED_AND_PUBLIC_SYNCED. Added the detailed classification guide, exported public commit `4c0d06cf2`, refreshed the actual operator workspace, retained `operator-local`, and passed workspace enforcement. |
| MSEA-R85 residual value absorption closure | `6872dbc94` | REVIEWER_ACCEPTED_BOUNDED. Reconciled 27/27 source files, created bounded BUILD-loop and public-trust owners, exported public commit `c2663b1ee`, and closed the historical R64-R70 roadmap. |
| MSEA-R85 residual value absorption dispatch | `f350d506d` | DISPATCH_READY for terminal 27-file reconciliation, bounded BUILD-loop and public-trust owner surfaces, five-minute demo, public-safe projection, and closure. |
| MSEA-R84 Lean Governance Follow-Through closure | `a4b504b53` | CLOSED_PASS_BOUNDED. Dispatch-authenticated compact profile; full compatibility; protected controls remain blocking; 175 focused tests pass. |
| MSEA-R84 Lean Governance Follow-Through dispatch | `dc91b6807` | DISPATCH_READY for one compact docs-only worker-return profile and one bounded checker lifecycle disposition; no public-sync or global demotion. |
| MSEA-R83 Workspace Health Repair And Upgrade Experience | `213c6ab4f` | RC_PASS_BOUNDED_AND_PUBLIC_SYNCED after product `202d7dd92`, compatibility fix `38672f496`, and public commits `3d6a85008` plus `fbb6c4d49`. Four verdicts, repair, deterministic build, migration, rollback, and static CI 8/8 passed. |
| MSEA-R82 Workspace Distribution And Update Release | `4bd363a81` | RC_PASS_BOUNDED_AND_PUBLIC_SYNCED after implementation `4939e59d0` and public commit `a4d5dba915`. Windows PowerShell 5.1 and PowerShell 7 clean installs, update, rollback, deterministic build, profile boundary, leakage scans, and public static CI 8/8 passed for version `0.1.0-rc1`. |
| MSEA-R81 Workspace Productization Release Candidate | `c067328d5` | RC_PASS_BOUNDED. Fresh bootstrap and existing-project adoption each passed doctor and enforcement 17/17. Workspace update passed. Public-free and paid-user-safe profile boundary scans passed. Operator-local failed without explicit continuity allowance and passed with it. No `Policy_Local`, public-sync, provider/live, runtime, checker, hook, or Fast Lane mutation occurred. |
| MSEA-R81B integrated dispatch | `810ace2ee` | Fulfilled by the R81 material closure commit. |
| MSEA-R81A source map | `60dfb0495` | REVIEWER_ACCEPTED_BOUNDED and consumed by R81 checklist/closure. |

Latest closed numbered LHW wave remains `LHW24`.

## Next Allowed Move

Mode: `mao_t5_dispatched`

MAO-T4 is dispatch-ready at `68cc94572`. Next allowed move is one delegated
local worker execution from clean post-sync HEAD with exactly five outputs and no commit.
L4 remains `VALUE_PARKED_WITH_REOPEN_CONDITIONS`. Latest closed numbered LHW
wave remains `LHW24`.

`Policy_Local` remains a closed workspace enforcement proof target, not the
next implementation task.

The parked R73F checker-retirement candidate must not reopen until its active
conformance and evidence-pack references are removed or reattached under a
separate source-verified packet.

R84 effectiveness follow-up is `DEFERRED_AND_REVISIT_ON_EVIDENCE`. R84 proved
shape reduction, not end-to-end token or latency savings. Collect at least five
post-R92 compact-eligible worker returns across at least two task classes. A
bounded improvement may reopen only if two returns each need at least two
repairs attributable to the same ceremony/scaffold issue, comparable evidence
from at least three runs shows less than 20 percent token or elapsed-time
improvement versus full-profile evidence, or a reviewer cites a real missed
defect caused by insufficient compact context. Do not re-propose a governance
refactor before one condition is met.

## Boundaries

- `broad external knowledge absorption` remains a separately authorized work
  class; it is not an automatic next move.
- `blocked work classes` remain blocked until their recorded source condition or
  operator checkpoint is satisfied.
- Provenance remains the full private source of truth.
- Public-facing changes go only through the sibling public-sync clone after
  fresh remote verification and explicit authorization.
- Local workspace may consume curated profiles; private continuity requires
  `operator-local` plus explicit allowance.
- Do not infer hosted, paid-user production, cross-platform, provider/live,
  Memory/RAG, retrieval, vectorization, or legal-workflow readiness from R82.

## History

Detailed pre-R81 continuity is preserved in:

- `CVF_SESSION/handoffs/archive/CVF_SESSION_MEMORY_COMPACTION_ARCHIVE_2026-07-10.md`
- `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V39_2026-07-08.md`

Use the generated active state for canonical machine-readable history; do not
expand this front door back into a chronological log.
