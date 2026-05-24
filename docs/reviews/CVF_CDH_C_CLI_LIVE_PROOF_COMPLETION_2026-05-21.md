# CVF CDH-C CLI Live Proof Completion

Memory class: FULL_RECORD

Status: CLOSED_CLI_LIVE_PROOF

docType: review

Date: 2026-05-21

---

## Purpose

Close the bounded CDH-C CLI live proof work order after proving the existing
`cvf execute` async CLI path against the local CVF web endpoint with live
provider credentials and JSONL receipt persistence.

---

## Scope / Target / Owner Boundary

Target:

- `docs/work_orders/CVF_WO_CDH_C_CLI_LIVE_PROOF_2026-05-21.md`

Evidence surfaces:

- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts`
- `docs/evidence/cdh-c-cli-live-proof-2026-05-21.jsonl`

Owner boundary:

- existing CLI execute path only;
- no new command or flag;
- no provider/runtime semantics change;
- no public-sync update.

---

## Target / Source Under Review

Authority chain:

- `docs/baselines/CVF_GC018_CDH_C_CLI_LIVE_PROOF_2026-05-21.md`
- `docs/reviews/CVF_CDH_C_DELTA_CODEX_REBUTTAL_2026-05-20.md`
- `docs/reviews/archive/CVF_C2_CLI_EXECUTE_HARDENING_COMPLETION_2026-05-19.md`

---

## Scope / Methodology

Codex executed the bounded work order as Orchestrator, Reviewer, Implementer,
and Auditor:

1. Filed GC-018 for CDH-C.
2. Confirmed `cvf execute` registration in `command.registry.ts`.
3. Started the local `cvf-web` dev endpoint at `http://127.0.0.1:3000`.
4. Loaded operator-supplied environment variables from `.env.local` without
   printing raw values.
5. Ran `GovernanceCLI.runAsync(["execute", ...])` against `/api/execute`.
6. Persisted CLI JSONL receipt metadata.
7. Ran a missing-service-token diagnostic path.
8. Ran CLI tests, TypeScript check, and governance checks.

---

## Evidence Trace Block

| Claim | Evidence | Result |
| --- | --- | --- |
| Registration confirmed | `command.registry.ts:114` has `name: "execute"`; `command.registry.ts:116` has `usage: "cvf execute ..."`; `command.registry.ts:131` calls `executeGovernedTemplateCommand(args)` | PASS |
| Live invocation success | `GovernanceCLI.runAsync(["execute", ...])` against `http://127.0.0.1:3000` | PASS, `cliSuccess=true`, `exitCode=0` |
| Live governance receipt | CLI output summary | PASS, receipt `rcpt-env-mpf9zb9y-luu9gq`, trace/envelope `env-mpf9zb9y-luu9gq`, `decision=ALLOW` |
| No mock fallback | receipt field | PASS, `evidenceMode=live` |
| Provider lane | receipt field | PASS, provider `alibaba`, model `qwen-turbo` |
| JSONL receipt metadata | `docs/evidence/cdh-c-cli-live-proof-2026-05-21.jsonl` | PASS, first-line keys `timestamp,templateId,requestedRole,workflowId,receiptBinding` |
| Diagnostic error path | same CLI path with `CVF_SERVICE_TOKEN` removed from process env | PASS, `status=401`, error `Unauthorized: please login.` |
| No new command surface | no source changes to `command.registry.ts`; registration line pre-existed | PASS |
| CLI test suite | `npm test` in `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI` | PASS, 97 tests |
| CLI typecheck | `npm run check` in `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI` | PASS |

---

## Findings / Position

Position: CLOSED_CLI_LIVE_PROOF.

Findings:

- The existing async CLI execute path can call the local CVF web execute route
  with live provider credentials.
- The returned governance receipt is live, allowed, provider-backed, and
  carries a receipt id plus envelope id.
- CLI JSONL receipt metadata is persisted without raw secrets.
- Missing service token produces an operator-visible 401 diagnostic.
- No CLI command, flag, provider runtime, SSE behavior, or route behavior was
  added.

---

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| Live proof is mistaken for broad CLI stability | Claim boundary limits this to one bounded invocation |
| Receipt log is mistaken for full audit receipt store | Completion calls it CLI JSONL metadata only |
| Secret leakage | Evidence records variable names/results only; raw key values were not printed |
| CLI surface drift | No command registry source changes were made |

---

## Decision / Recommendation / Disposition

Disposition: close CDH-C CLI live proof.

Remaining CDH work:

- CDH-D vision runtime still requires the vision-runtime work order and
  vision-capable provider proof before closure.

---

## Claim Boundary

This closure proves one bounded live invocation of the existing `cvf execute`
CLI path plus JSONL metadata persistence and one diagnostic error path. It does
not prove broad CLI stability, all-provider parity, SSE streaming, multi-agent
orchestration, provider runtime expansion, public-sync readiness, or a public
product capability.
