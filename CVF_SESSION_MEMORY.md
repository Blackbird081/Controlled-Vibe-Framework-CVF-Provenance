# ACTIVE SESSION FRONT DOOR

Memory class: active-session-front-door

Status: ACTIVE

Last compacted: 2026-07-10

## Startup Order

Read before governed material work:

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
3. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
4. `AGENT_HANDOFF_V40_2026-07-10.md`
5. `docs/reference/guard_orientation/README.md`
6. `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`

Read `DESIGN.md` only when touching Web, UI, or dashboard work.

## Active Pointers

| Field | Path |
|---|---|
| Bootstrap read model | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Canonical state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` |
| Active handoff | `AGENT_HANDOFF_V40_2026-07-10.md` |
| Active review queue | `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` |
| Pain-point closure direction | `docs/reviews/archive/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_DIRECTION_CODEX_2026-05-20.md` |
| Historical handoffs | `CVF_SESSION/handoffs/archive/` |
| Latest front-door archive | `CVF_SESSION/handoffs/archive/CVF_SESSION_MEMORY_COMPACTION_ARCHIVE_2026-07-10.md` |
| Freeze posture | `governance_kernel_freeze_recommended` |

## Startup Acknowledgment

Startup acknowledged: current mode=`msea_r92_worker_return_scaffold_hardening_dispatched`; active handoff=AGENT_HANDOFF_V40_2026-07-10.md; next allowed move=delegated worker executes MSEA-R92 without committing; parked checkpoint=Gop y CVF legacy cleanup follows R92 and R73F remains blocked.

## Current Mode

Current mode marker: `msea_r92_worker_return_scaffold_hardening_dispatched`

Current mode: `msea_r92_worker_return_scaffold_hardening_dispatched`

`msea_r92_worker_return_scaffold_hardening_dispatched`

Previous mode:

`msea_r91_system_chain_map_and_freshness_control_closed`

## Latest Material Work

| Work | Commit | Disposition |
|---|---|---|
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

Mode: `msea_r92_worker_return_scaffold_hardening_dispatched`

Next allowed move: delegated worker executes
`docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R92_WORKER_RETURN_SCAFFOLD_LAST_MILE_HARDENING_2026-07-10.md`
under `WORKER_MUST_NOT_COMMIT`, then returns exactly five paths for reviewer
closure. `Gop y CVF/` legacy cleanup remains next after R92; do not move it in
this tranche. Latest closed numbered LHW wave remains `LHW24`.

`Policy_Local` remains a closed workspace enforcement proof target, not the
next implementation task.

The parked R73F checker-retirement candidate must not reopen until its active
conformance and evidence-pack references are removed or reattached under a
separate source-verified packet.

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
