# CVF 17.05 Consolidated Live Proof Plan - 2026-05-18

Memory class: FULL_RECORD

Status: LIVE PROOF BUNDLE - PHASE 2.C / 3.E EXECUTED

## Purpose

Define one consolidated live/API-key proof tranche for the 17.05 roadmap so
Phase 2.C, Phase 3.E, and any demand-gated provider-method proof can share the
same operator-key setup and evidence run instead of repeatedly touching live
provider credentials.

## Scope / Target / Owner Boundary

Target: live-proof-dependent phases after bounded Phase 2.B.

Owner: CVF session-continuity, noncoder runtime governance, and release-proof
surfaces.

In scope:

- identifying phases that require live provider proof;
- grouping live proof into one future tranche;
- defining key-loading and no-secret-printing rules;
- defining the minimum evidence bundle to collect.

Out of scope:

- printing or copying API keys;
- changing `.env.local`;
- implementing Phase 4.T1/T2 runtime behavior;
- changing public claims.

## Target / Source Under Review

Sources:

- `AGENTS.md` Mandatory Live Governance Proof
- `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_REVIEW_CVF_FINAL_CONVERGED_REMEDIATION_ROADMAP_2026-05-17.md`
- `docs/reviews/CVF_17_05_PHASE_2C_VERTICAL_SLICE_PREFLIGHT_2026-05-18.md`
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/operational-metrics.schema.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/.env.local` (operator-key
  location; values must not be printed)

## Scope / Methodology

Method:

1. Identify roadmap phases that require live provider proof.
2. Separate non-live preparation from live execution.
3. Define a single shared live run that can produce evidence for multiple
   phases without repeating key handling.

## Findings / Position

The live/API-key phases should be grouped where they share a source.

Phase 2.C needs live proof before any public/noncoder governance claim.
Phase 3.E needs runtime sources; the best first source is the Phase 2.C
vertical-slice run. Provider method extension should only join the live bundle
if a concrete consumer or vertical slice requires a method.

Addendum 2026-05-18: the Phase 2.C / Phase 3.E shared live bundle has now
run once on the Alibaba lane after the operator confirmed live keys are
available in `.env.local`. Raw key values were not printed. Phase 4 remains
demand-gated and was not included because the selected vertical slice did not
need `stream()`, `tool_call()`, `json_mode()`, `vision()`, `embedding()`, or
`reasoning()`.

## Live Bundle Membership

| Phase | Live dependency | Bundle disposition |
|---|---|---|
| Phase 2.C vertical slice | Real provider governance proof for `Create Product Brief` before claim | Executed: `route.phase2c-product-brief.alibaba.live.test.ts` |
| Phase 3.E emission pilot | Runtime source for policy violation rate, receipt integrity, task completion rate | Executed from same Phase 2.C live response |
| Phase 4.T1 stream/tool_call/json_mode | Provider capability proof only if a selected vertical slice consumes the method | Conditional include |
| Phase 4.T2 vision/embedding/reasoning | Requires named runtime need and separate GC-018 | Exclude until named |

## Live Run Requirements

For this bundle and any later live run:

- load operator keys from
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/.env.local` or process
  environment;
- never print raw key values;
- prefer `DASHSCOPE_API_KEY`; aliases `ALIBABA_API_KEY`,
  `CVF_ALIBABA_API_KEY`, and `CVF_BENCHMARK_ALIBABA_KEY` are acceptable;
- ensure any public governance behavior proof includes a real provider API
  call.

Required release-quality command:

```bash
python scripts/run_cvf_release_gate_bundle.py --json
```

The consolidated live tranche used a targeted Phase 2.C / 3.E proof command.
This targeted command does not replace the release gate bundle for
release-quality governance claims.

Executed targeted command:

```powershell
# .env.local loaded into process without printing values
npx vitest run src/app/api/execute/route.phase2c-product-brief.alibaba.live.test.ts
```

## Evidence To Capture

The executed live bundle captured:

- one successful governed `Create Product Brief` vertical-slice journey;
- provider/model lane used, without raw key values;
- policy/risk/guard decision trace;
- deliverable pack generated;
- receipt envelope / evidence receipt adapter result;
- Phase 3.E metric emissions for 2-3 metrics only;
- explicit skipped metrics and why they remain planned-but-not-emitted;
- pass/fail summary suitable for handoff and claim-boundary docs.

## Risk / Corrective Action

Risk:

- Running live proof repeatedly increases key-handling risk and produces
  scattered evidence that is hard to interpret.

Corrective action:

- Batch related live proof into one tranche after non-live GC-018/preflight work
  is complete.
- Keep live proof evidence in one completion packet.
- Defer Phase 4 live execution until a selected method and consuming runtime
  need are fully defined.

## Decision / Recommendation / Disposition

Decision: group live/API-key-dependent proof where phases share a runtime
source. Phase 2.C and Phase 3.E have been executed together.

Recommendation: use the recorded Phase 2.C / Phase 3.E evidence for bounded
roadmap closure. Keep Phase 4 outside live proof until demand-gated.

Disposition: `phase_2c_3e_live_bundle_executed_phase_4_deferred`.

## Claim Boundary

This plan records the bounded Phase 2.C / Phase 3.E live proof. It does not
claim full release-quality governance proof, does not authorize Phase 4.T1/T2
implementation, does not print or copy API keys, and does not change public
claims.
