# CVF Workflow Chain Governance Roadmap — V2 (Post-Rebuttal)

Memory class: SUMMARY_RECORD

Status: READY_FOR_REBUTTAL — revised after first Reviewer-role rebuttal.
Filed by: Orchestrator role. C1/C2/C3/C4 work orders may be pre-filed
as non-executable packets, but no Worker implementation may begin before
the second Reviewer-role pass returns no-blocking findings and each
accepted GC-018-required candidate has its GC-018 filed.

Predecessor: `docs/roadmaps/CVF_WORKFLOW_CHAIN_GOVERNANCE_PROPOSAL_2026-05-19.md`
(Status: REBUTTED — Reviewer disposition recorded there)

---

## Scope / Target / Owner Boundary

In scope: C1 hardening (public-sync repo), C2 pack contract guard
(governance repo), C3 execute route sequence guard (governance repo),
C4 continuation chain guard (governance repo).

Out of scope: replacing existing guards, modifying canonical role taxonomy,
introducing persona-named workflow rules, any implementation before a
second Reviewer rebuttal is recorded and accepted candidates have GC-018.

Owner: Orchestrator role files GC-018 and work orders; Worker role
implements per work order; Reviewer role rebuts each candidate
independently.

---

## Purpose

Close workflow-chain integrity gaps in CVF across four bounded layers:

1. CI/Release YAML ↔ canonical runner (guard hardening — public-sync)
2. Governed pack 3-file contract validation (new guard — governance repo)
3. Execute route step sequence enforcement (new guard — governance repo)
4. Continuation chain: work-order → review → GC-018 → handoff sync

All four candidates are independently reviewable. Each candidate that
survives rebuttal gets its own GC-018 where required before implementation.

---

## What changed from V1

| Candidate | V1 problem | V2 fix |
| --- | --- | --- |
| C1 | Assumed guard lived in governance repo | Explicitly scoped to public-sync repo only |
| C2 | Required `## Steps` (wrong), step-name keys in JSON (not in current packs) | Now requires `## Workflow`, validates section exists + has numbered items only |
| C3 | Step list named non-existent functions | Replaced with actual `route.ts` call sites from source read; selector mode handles repeated `buildEvidenceReceipt` / `appendAuditEvent` calls |
| C4 | Checked `Status: DELIVERED/COMPLETE`, `*_WORK_ORDER_COMPLETION_REVIEW_*`; assumed every work order needs GC-018 | Now checks `Status: CLOSED`, `*_COMPLETION_*.md`; drops "next 5 commits" for HEAD SHA check; Rule A applies only to work orders that declare `GC-018 required: Yes` |

---

## Role vocabulary

Same as V1. Not persona names — role names:

- `OPERATOR` — session/repo owner (final authority)
- `Orchestrator` — files GC-018, dispatches work orders
- `Reviewer` — rebuts proposals, audits deliveries
- `Worker` — implements per work order
- `Auditor` — signs evidence

---

## Candidate 1 — Harden existing workflow orchestration guard (public-sync)

**Target repo:** `Controlled-Vibe-Framework-CVF-public-sync` only.

The guard `governance/compat/check_workflow_orchestration_guard.py` does
not exist in the governance (provenance) repo. It lives only in public-sync
at commit `111daaab`. This candidate hardens the guard where it exists.

**Type:** Improvement to existing guard. No new guard file.
**Risk:** R0
**GC-018 required:** No — R0 hardening of existing guard under META_GUARD policy.

### Hardening tasks

#### Task 1 — Test file

Path: `governance/compat/test_check_workflow_orchestration_guard.py`
(in public-sync repo)

Required test cases:

- Compliant fixture (all `REQUIRED_COMMANDS` present) → `compliant == True`
- Missing required workflow file → 1 violation, `path` field set
- Command fragment missing in a present file → 1 violation
- Fragmented static marker present in workflow YAML → 1 violation
- Path normalization (backslash vs forward-slash on Windows) → no false positive
- JSON output mode (`--json`) → valid JSON with `compliant` boolean key

#### Task 2 — Token-presence matching

Replace current `_normalize()` collapse-whitespace with token-presence check:

- Split required fragment by whitespace into tokens
- Assert each token appears anywhere in the target file text
- This catches `"scripts/foo.py"` vs `scripts/foo.py` quoting drift

#### Task 3 — Externalize REQUIRED_COMMANDS

Move hardcoded dict to:
`governance/compat/CVF_WORKFLOW_ORCHESTRATION_REGISTRY.json`

Schema per entry:

```json
{
  "surface": ".github/workflows/cvf-static-ci.yml",
  "requiredFragments": ["python scripts/run_cvf_static_ci_gate.py --json"],
  "addedAt": "2026-05-19",
  "addedBy": "Worker"
}
```

Guard reads JSON, validates schema, then applies token-presence logic.

#### Task 4 — Receipt emission

When `--enforce` flag is set, append one-line JSONL to
`docs/evidence/workflow-orchestration-guard.jsonl`:

```json
{"timestamp": "...", "compliant": true, "violationCount": 0}
```

### C1 acceptance criteria

- `python governance/compat/check_workflow_orchestration_guard.py` → COMPLIANT
- `pytest governance/compat/test_check_workflow_orchestration_guard.py` → all pass
- `CVF_WORKFLOW_ORCHESTRATION_REGISTRY.json` validates against schema
- `--enforce` run appends a JSONL line to evidence file

---

## Candidate 2 — Governed Pack Contract Guard (governance repo)

**Target repo:** `Controlled-Vibe-Framework-CVF` (governance/provenance).

**File:** `governance/compat/check_governed_pack_contract.py`
**Policy:** `governance/toolkit/05_OPERATION/CVF_GOVERNED_PACK_CONTRACT_GUARD.md`
**Risk:** R0 — read-only validation; does not modify packs.
**GC-018 required:** Yes — new enforcement surface.

### C2 adjacent guards (must cite, do not duplicate)

- `check_template_skill_standard_guard_compat.py` — validates template/skill
  companion docs (markdown standards). Does NOT validate pack folder 3-file
  contract or pack-id ↔ template-id binding. This candidate fills that gap.
- `check_guard_contract_compat.py` — validates guard contract SDK compat.
  Does NOT read governed pack folders.

### Rules (source-fidelity verified against existing packs)

#### Rule A — 3-file presence

Pack folder under
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/`
MUST contain:

- `workflow.spec.md`
- `execution.policy.json`
- `receipt.schema.json`

Other files allowed. Confirmed present in all 3 existing packs
(`app_builder_complete`, `documentation`, `strategy_analysis`).

#### Rule B — templateId binding

`execution.policy.json` MUST be valid JSON with a `templateId` field.
That `templateId` value MUST appear as an `id:` string in at least one
file under
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates/*.ts`
(grep check, not full TS parse).

#### Rule C — Workflow section (revised from V1)

`workflow.spec.md` MUST contain a `## Workflow` section (not `## Steps` —
V1 was wrong; all existing packs use `## Workflow` confirmed at
`app_builder_complete/workflow.spec.md` line 39) with at least one
numbered list item (`1.` or `1)`).

No requirement that step names appear as keys in `execution.policy.json`
— that binding does not exist in current packs and is deferred to a
separate pack-contract evolution tranche.

#### Rule D — Receipt schema (revised from V1)

`receipt.schema.json` MUST be valid JSON Schema (draft-07 or later)
with a `stepTraces` property present anywhere in the schema object tree.
No per-step count assertion — current packs use a flat `stepTraces`
array, not per-step entries.

### C2 acceptance criteria

- All 3 existing packs PASS Rule A–D
- Synthetic broken pack (missing `workflow.spec.md`) → Rule A violation
- Synthetic broken pack (`templateId` not in templates) → Rule B violation
- Synthetic broken pack (no `## Workflow` section) → Rule C violation
- Synthetic broken pack (no `stepTraces` in receipt schema) → Rule D violation
- Guard wired into `governance/compat/run_local_governance_hook_chain.py`
- Guard wired into `scripts/run_cvf_static_ci_gate.py`

---

## Candidate 3 — Execute Route Step Sequence Guard (governance repo)

**Target repo:** `Controlled-Vibe-Framework-CVF` (governance/provenance).

**File:** `governance/compat/check_execute_route_step_sequence.py`
**Policy:** `governance/toolkit/05_OPERATION/CVF_EXECUTE_ROUTE_STEP_SEQUENCE_GUARD.md`
**Risk:** R1 — reads live source file; brittle to refactor; high value.
**GC-018 required:** Yes — new enforcement surface on critical runtime path.

### C3 adjacent guards

None reads `route.ts` for step ordering. This is a new surface.

### Canonical step registry (source-fidelity — read from route.ts 2026-05-19)

All line numbers from
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
(1001 lines total):

| Order | Step name | Call site pattern | Selector | Confirmed line |
| --- | --- | --- | --- | --- |
| 1 | `resolveExecutionCVFRole` | `resolveExecutionCVFRole(` | first non-import/comment occurrence | 336 |
| 2 | `evaluateExecutionActorRoleGate` | `evaluateExecutionActorRoleGate(` | first non-import/comment occurrence | 348 |
| 3 | `checkRoleOutputPermission` | `checkRoleOutputPermission(` | first non-import/comment occurrence | 350 |
| 4 | `evaluateEnforcement` | `evaluateEnforcement(` | first non-import/comment occurrence | 375 |
| 5 | `routeWebProvider` | `routeWebProvider(` | first non-import/comment occurrence | 564 |
| 6 | `buildEvidenceReceipt` (success path) | `buildEvidenceReceipt(` | last non-import/comment occurrence | 858 |
| 7 | `buildRouteAuditMemoryCapture` | `buildRouteAuditMemoryCapture(` | first non-import/comment occurrence | 927 |
| 8 | `appendAuditEvent` (final audit memory event) | `appendAuditEvent(` | last non-import/comment occurrence | 944 |

Steps 1-4 are the governance gate sequence (role → actor gate → permission →
enforcement). Steps 5-8 are the execution and evidence sequence. The guard
asserts that the selected occurrence of each pattern appears at a strictly
increasing line number in the canonical order. Selector mode is required
because `route.ts` has earlier error-path `buildEvidenceReceipt(` and
`appendAuditEvent(` calls before the final success/evidence path.

Branches (early-exit 403 at step 2 if actor gate rejects) are permitted as
long as the calls that DO execute maintain order.

### Externalize to registry

`governance/compat/CVF_EXECUTE_ROUTE_STEP_SEQUENCE_REGISTRY.json`

Schema per entry:

```json
{
  "order": 1,
  "stepName": "resolveExecutionCVFRole",
  "callPattern": "resolveExecutionCVFRole(",
  "selector": "first",
  "confirmedLine": 336,
  "addedAt": "2026-05-19",
  "addedBy": "Worker"
}
```

### Detection method

1. Read registry JSON.
2. Read `route.ts` as text; for each step entry, find the line number
   selected by `selector` (`first` or `last`) among non-import and
   non-comment occurrences of `callPattern`.
3. Assert line numbers are strictly increasing in `order` sequence.
4. Report each out-of-order or missing step as a violation.

### C3 test fixtures

- **Passing:** snapshot of current `route.ts` → 0 violations
- **Broken 1:** step removed (delete pattern) → 1 missing-step violation
- **Broken 2:** two steps swapped → 1 order violation
- **Broken 3:** repeated success-path pattern earlier in file → assert
  `selector: last` still resolves the final success/evidence occurrence
  and does not create a false positive

### C3 acceptance criteria

- Current `route.ts` snapshot → 0 violations
- All 3 broken fixtures → correct violation per fixture
- Guard runs in < 2 seconds on `route.ts`
- Registry JSON validates against schema
- Covered by test file `test_check_execute_route_step_sequence.py`

---

## Candidate 4 — Continuation Chain Guard (governance repo)

**Target repo:** `Controlled-Vibe-Framework-CVF` (governance/provenance).

**File:** `governance/compat/check_continuation_chain.py`
**Policy:** `governance/toolkit/05_OPERATION/CVF_CONTINUATION_CHAIN_GUARD.md`
**Risk:** R0 — process guard; reads file existence and grep patterns only.
**GC-018 required:** Yes — new enforcement surface, R0.

### C4 adjacent guards (must cite, do not duplicate)

- `check_agent_handoff_guard_compat.py` — handoff template chain. Does NOT
  check work-order → review packet binding.
- `check_depth_audit_continuation_compat.py` — GC-018 reopen logic. Does NOT
  check work-order → review binding.
- `check_active_session_state.py` — front-door pointer alignment. Does NOT
  check work-order → review binding.

This guard fills the upstream gap: work-order closed → review packet exists
→ handoff HEAD SHA current.

### Chain rules (source-fidelity — verified against current conventions)

#### C4 Rule A — GC-018 reference in work order

For every file matching `docs/work_orders/CVF_AGENT_WORK_ORDER_*.md`
that declares `GC-018 required: Yes`, body MUST contain a reference to a
`docs/baselines/CVF_GC018_*.md` path (regex:
`docs/baselines/CVF_GC018_[^\s]+\.md`).

Work orders that declare `GC-018 required: No` are explicitly out of
Rule A scope. Legacy/prerequisite work orders that do not declare the
field are recorded as `not_applicable` unless a later cleanup tranche
requires universal declaration.

#### C4 Rule B — Closed work order → completion review exists (revised from V1)

When work order body contains `Status: CLOSED` (prefix match, not exact —
covers `CLOSED`, `CLOSED_WITH_*`, `CLOSED — ...`):
a matching completion review MUST exist under `docs/reviews/` with a
filename matching `CVF_*_COMPLETION_*.md` (not the V1 pattern
`*_WORK_ORDER_COMPLETION_REVIEW_*` which missed all Lane-style reviews
like `CVF_LANE_G_RUNTIME_ACTOR_ENFORCEMENT_COMPLETION_2026-05-19.md`
and `CVF_LANE_B_WORKFLOW_PACKAGING_COMPLETION_2026-05-19.md`).

Matching: review file body MUST contain the work order filename
(basename without path) OR the work order's declared `templateId` /
lane identifier.

#### C4 Rule C — Handoff HEAD SHA current (revised from V1)

Drop "next 5 commits" lookahead — it is brittle and undefined for
non-linear histories.

Instead: read active handoff path from
`CVF_SESSION/ACTIVE_SESSION_STATE.json` → `activeHandoff`. Read that
handoff file. Assert that the handoff body contains the string of
`git rev-parse HEAD`. If not found, emit a GC-020 drift violation
(informational, not blocking by default; `--enforce` makes it blocking).

### Exemption registry

`governance/compat/CVF_CONTINUATION_CHAIN_EXEMPTION_REGISTRY.json`

Records legacy work orders that close differently (e.g., pre-GC-018
closures, multi-lane bundle work orders). Exempted work orders skip
Rule B only.

### C4 acceptance criteria

- Scan of current `docs/work_orders/` → 0 applicable Rule A violations,
  0 Rule B orphans (or all orphans are in exemption registry), 0 Rule C drift
- Synthetic Rule A violation (work order declares `GC-018 required: Yes`
  without GC-018 reference) → caught
- Synthetic Rule B violation (closed work order with no matching review) → caught
- Rule C: force HEAD mismatch in fixture → GC-020 drift violation emitted
- Exemption registry prevents false positives on legacy work orders

---

## Ordering and dependencies

```text
C1 (public-sync, R0, no GC-018)    ←  independent, can start immediately
C2 (governance, R0, needs GC-018)  ←  independent of C1
C4 (governance, R0, needs GC-018)  ←  independent of C1 and C2
C3 (governance, R1, needs GC-018)  ←  after C2 and C4 are stable
```

C1 does not block C2/C3/C4 — different repos. C2 and C4 can be
dispatched in parallel after their GC-018s are filed. C3 is last because
it touches the most-changed file (`route.ts`).

---

## Non-goals

- Do not replace any of the 94 existing guards.
- Do not modify the canonical role taxonomy.
- Do not use persona-named roles or vendor-specific workflow rules.
- Do not claim full workflow-chain enforcement until all accepted
  candidates have GC-018 packets, tests, and hook-chain evidence.

## Work plan

1. Orchestrator files this roadmap for second Reviewer-role rebuttal.
2. Reviewer accepts, rejects, or narrows each candidate independently.
3. For each accepted candidate: Orchestrator files GC-018, then dispatches
   work order to Worker role.
4. Worker implements, runs acceptance criteria, files completion packet.
5. Orchestrator reviews completion packet, closes candidate.

## Acceptance criteria (proposal level)

- Second Reviewer rebuttal returns no blocking findings.
- Each accepted candidate has its own GC-018 before any implementation.
- Each GC-018 cites adjacent guards and states why it is not a duplicate.
- Each implementation includes passing positive and negative tests.
- Hook-chain wiring present only after local evidence passes.

## Verification/Evidence

- `python governance/compat/check_markdown_structural_completeness.py`
  passes for this roadmap file.
- `python governance/compat/run_local_governance_hook_chain.py --hook
  pre-commit` passes before commit.
- No public claim may cite this roadmap as implementation proof.

## Risk

| Risk | Mitigation |
| --- | --- |
| C3 brittle to `route.ts` refactor | Externalized registry; Worker must update registry on any route refactor |
| C2 guard breaks future valid pack | Acceptance test uses all 3 existing packs as positive fixtures |
| C4 exemption registry grows unbounded | Policy file caps exemptions at 10; beyond 10 triggers a separate tranche |
| Guard sprawl (94 → 97) | Each guard cites duplication-audit table in its policy file |

## Decision / Recommendation / Disposition

READY_FOR_REBUTTAL. Second Reviewer-role rebuttal required before
Orchestrator files any GC-018 or dispatches any work order.

## Claim Boundary

This roadmap does not authorize implementation. It does not modify any
existing guard. It does not change role taxonomy. It is the corrected
design artifact that supersedes the V1 proposal per Reviewer-role
rebuttal disposition.
