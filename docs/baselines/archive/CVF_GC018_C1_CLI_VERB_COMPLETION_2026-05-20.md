# CVF GC-018 C1 CLI Verb Completion

Memory class: SUMMARY_RECORD

Status: AUTHORIZED

docType: baseline

Date: 2026-05-20

---

## Purpose

Authorize five read-only top-level CLI verbs that close the residual command
surface named by the Review-CVF audit.

---

## Source or Predecessor Evidence

- `docs/work_orders/CVF_WO_RESIDUAL_C1_CLI_VERB_COMPLETION_2026-05-20.md`
- `docs/reviews/archive/CVF_REVIEW_CVF_RESIDUAL_CLOSURE_ROADMAP_CODEX_REBUTTAL_2026-05-19.md`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/execute.client.ts`

---

## Decision / Baseline

Decision: CONTRACT_CLOSURE with read-only wrappers.

| Verb | Backing source | Forbidden behavior |
| --- | --- | --- |
| `cvf run <template>` | Alias to existing `execute` command argument shape | New runtime path |
| `cvf skill list/show` | Existing `cvf-web/public/data/skills-index.json` skill index | Skill mutation or network fetch |
| `cvf receipt show` | Existing execute receipt JSONL path | Receipt mutation |
| `cvf trace dump` | Existing audit JSONL path supplied by trace input/default | Log mutation or creation |
| `cvf provider list` | Existing cvf-web provider lane list contract | Provider mutation, key exposure, network call |

---

## Scope or Proposed Tranche

Authorized:

- Register `run`, `skill`, `receipt`, `trace`, and `provider`.
- Add tests proving read-only behavior and error handling.

Forbidden:

- Provider API calls.
- Auth changes.
- Mutation commands.
- New runtime execution semantics.

---

## Evidence / Required Evidence / Verification

Required verification:

- `npm test` in `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI`
- `npm run check` in `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI`

---

## Claim Boundary

This baseline authorizes read-only CLI wrapper registration only. It does not
authorize new provider execution, auth, or runtime semantics.
