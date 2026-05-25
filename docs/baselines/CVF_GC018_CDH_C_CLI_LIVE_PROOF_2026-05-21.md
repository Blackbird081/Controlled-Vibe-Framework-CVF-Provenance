# CVF GC-018 CDH-C CLI Live Proof

Memory class: FULL_RECORD

Status: GC018_ACCEPTED_FOR_BOUNDED_IMPLEMENTATION

docType: baseline

Date: 2026-05-21

---

## Source / Predecessor Evidence

- `docs/reviews/archive/CVF_CDH_C_DELTA_CODEX_REBUTTAL_2026-05-20.md`
- `docs/roadmaps/CVF_CDH_C_CLI_LIVE_PROOF_ROADMAP_2026-05-21.md`
- `docs/work_orders/CVF_WO_CDH_C_CLI_LIVE_PROOF_2026-05-21.md`
- `docs/reviews/archive/CVF_C2_CLI_EXECUTE_HARDENING_COMPLETION_2026-05-19.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`

---

## Purpose / Decision / Baseline

Decision: ACCEPTED.

The operator confirmed API keys may be used for testing on 2026-05-21. Codex
confirmed the local CVF web endpoint was running at `http://127.0.0.1:3000`
before live step C-02.

This GC-018 authorizes only a bounded live proof of the existing `cvf execute`
CLI path, JSONL receipt persistence evidence, and one diagnostic error path.

---

## Decision / Baseline / Proposed Tranche

Proposed tranche: CDH-C CLI live proof.

Accepted implementation/proof:

- run the existing async `cvf execute` command path through
  `GovernanceCLI.runAsync()`;
- call the local CVF `/api/execute` endpoint with live provider credentials;
- persist a CLI JSONL receipt metadata line;
- trigger one operator-visible diagnostic failure.

Rejected expansion:

- new CLI command or flag;
- provider/runtime semantics changes;
- SSE streaming;
- multi-agent orchestration;
- packaging/installability work;
- public-sync update.

---

## Scope / Proposed Tranche

In scope:

- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts` readout
  evidence for existing registration;
- `docs/evidence/cdh-c-cli-live-proof-2026-05-21.jsonl` generated receipt
  metadata evidence;
- completion review and continuity sync.

Out of scope:

- code changes to command registration;
- provider adapter changes;
- route implementation changes;
- public catalog or public README claims.

---

## Evidence / Required Evidence / Verification

Required verification:

- live CLI invocation returns success with `decision=ALLOW`;
- receipt includes `evidenceMode=live`, provider, model, receipt id, and trace
  id/envelope id;
- JSONL receipt metadata exists on disk;
- diagnostic error path returns a clear operator error;
- CLI tests and TypeScript check pass;
- governance docs checks pass.

---

## Claim Boundary

This GC-018 authorizes and records only one bounded live proof of the existing
CLI execute path. It does not prove broad CLI stability, all-provider CLI
parity, SSE streaming, multi-agent orchestration, provider runtime expansion,
or any public product capability.
