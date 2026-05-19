# CVF Agent Work Order — C3: Execute Route Step Sequence Guard

Memory class: SUMMARY_RECORD

Status: OPEN — awaiting second Reviewer rebuttal acceptance of V2 roadmap,
GC-018 filing, AND C2 + C4 acceptance criteria passing before implementation.
C3 is the last candidate; do not start until C2 and C4 are closed.

GC-018 required: Yes — new enforcement surface on critical runtime path.
GC-018 path: `docs/baselines/CVF_GC018_C3_EXECUTE_ROUTE_STEP_SEQUENCE_GUARD_2026-05-19.md`

## Purpose

Create `check_execute_route_step_sequence.py` to verify the 8 canonical call
sites in `route.ts` appear in strictly increasing line-number order. Prevents
silent step-order drift on the critical `/api/execute` path without modifying
the route file itself.

## Authority Chain

V2 roadmap (`CVF_WORKFLOW_CHAIN_GOVERNANCE_ROADMAP_V2_2026-05-19.md`) — C3
section. C3 is last; GC-018 must be filed AND C2 + C4 acceptance criteria must
pass before implementation begins. Second Reviewer rebuttal must be no-blocking.

## Agent Roles

- **Orchestrator** — confirms C2 and C4 closed; files GC-018; dispatches work order.
- **Worker** — re-verifies step line numbers against current `route.ts` before writing
  any code; implements all tasks; files completion review upon closure.

## Scope

**Allowed scope:** Governance/provenance repo — step registry JSON, guard script,
policy file (with maintenance note), test file, hook-chain wiring for 8-step
sequence enforcement only.

**Forbidden scope:** Modifying `route.ts`, adding new steps, covering other route
files, semantic validation of what each step does.

## Required First Reads

1. `docs/roadmaps/CVF_WORKFLOW_CHAIN_GOVERNANCE_ROADMAP_V2_2026-05-19.md` — C3
2. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` (current)
3. Completion reviews for C2 and C4 (must be CLOSED before starting)
4. `docs/baselines/CVF_GC018_C3_EXECUTE_ROUTE_STEP_SEQUENCE_GUARD_2026-05-19.md` (after filing)

## Write Ownership

Worker role owns all file creation. Must NOT modify `route.ts`. Pre-flight
line-number verification is mandatory before writing the registry JSON.

## Execution Plan

Pre-flight grep → Task 1 (registry JSON with verified line numbers) → Task 2
(guard script) → Task 3 (policy file) → Task 4 (test file, must pass) →
GC-018 maintenance note → hook-chain wiring. Do not wire before tests pass.

## Evidence Requirements

Evidence trace in completion review: `test_current_route_passes` result,
guard run against actual `route.ts`, and performance timing (< 2 seconds).

## Review Gate

Orchestrator confirms C2 and C4 are CLOSED before accepting C3 completion
packet. Evidence must include 0 violations on actual `route.ts`.

## Closure Checklist

- [ ] Pre-flight line numbers verified and registry updated if drifted
- [ ] All 4 test cases pass with evidence
- [ ] Guard runs in < 2 seconds (verified in evidence)
- [ ] Maintenance note present in GC-018 and policy file
- [ ] GC-020 handoff HEAD SHA updated after commit

## Return-To-Orchestrator Conditions

Return immediately if:

- C2 or C4 is not yet CLOSED (do not start implementation)
- Pre-flight grep finds any step pattern missing from current `route.ts`
- Guard takes > 2 seconds on `route.ts` (investigate before wiring)

## Target repo

`Controlled-Vibe-Framework-CVF` (governance/provenance repo).

## Source / Predecessor Evidence

- `docs/roadmaps/CVF_WORKFLOW_CHAIN_GOVERNANCE_ROADMAP_V2_2026-05-19.md` — C3 section
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` (1001 lines, 2026-05-19)
- Adjacent: no existing guard reads `route.ts` for step ordering

## Canonical step registry (source-fidelity — confirmed 2026-05-19)

Worker must re-verify each line number against current `route.ts` BEFORE
writing the registry JSON. Line numbers may drift if the file was edited
after this work order was filed.

| Order | Step name | Call site pattern | Reference line |
| --- | --- | --- | --- |
| 1 | `resolveExecutionCVFRole` | `resolveExecutionCVFRole(` | 336 |
| 2 | `evaluateExecutionActorRoleGate` | `evaluateExecutionActorRoleGate(` | 348 |
| 3 | `checkRoleOutputPermission` | `checkRoleOutputPermission(` | 350 |
| 4 | `evaluateEnforcement` | `evaluateEnforcement(` | 375 |
| 5 | `routeWebProvider` | `routeWebProvider(` | 564 |
| 6 | `buildEvidenceReceipt` | `buildEvidenceReceipt(` | 858 |
| 7 | `buildRouteAuditMemoryCapture` | `buildRouteAuditMemoryCapture(` | 927 |
| 8 | `appendAuditEvent` (final) | `appendAuditEvent(` | 944 |

Detection: first occurrence of pattern (excluding import lines and comment
lines) must appear at a strictly increasing line number in order 1–8.

## Source-fidelity pre-flight (Worker role must run before writing any code)

```text
1. Grep route.ts for each callPattern above; record actual first occurrence
   line (excluding import/comment lines); update registry if any line changed
2. Confirm check_execute_route_step_sequence.py does NOT exist yet
3. Confirm CVF_EXECUTE_ROUTE_STEP_SEQUENCE_REGISTRY.json does NOT exist yet
4. Confirm route.ts is still 1001 lines (if changed, update registry)
```

## Implementation tasks

### Task 1 — Step registry JSON

Create `governance/compat/CVF_EXECUTE_ROUTE_STEP_SEQUENCE_REGISTRY.json`:

```json
[
  {
    "order": 1,
    "stepName": "resolveExecutionCVFRole",
    "callPattern": "resolveExecutionCVFRole(",
    "confirmedLine": 336,
    "addedAt": "2026-05-19",
    "addedBy": "Worker"
  },
  {
    "order": 2,
    "stepName": "evaluateExecutionActorRoleGate",
    "callPattern": "evaluateExecutionActorRoleGate(",
    "confirmedLine": 348,
    "addedAt": "2026-05-19",
    "addedBy": "Worker"
  },
  {
    "order": 3,
    "stepName": "checkRoleOutputPermission",
    "callPattern": "checkRoleOutputPermission(",
    "confirmedLine": 350,
    "addedAt": "2026-05-19",
    "addedBy": "Worker"
  },
  {
    "order": 4,
    "stepName": "evaluateEnforcement",
    "callPattern": "evaluateEnforcement(",
    "confirmedLine": 375,
    "addedAt": "2026-05-19",
    "addedBy": "Worker"
  },
  {
    "order": 5,
    "stepName": "routeWebProvider",
    "callPattern": "routeWebProvider(",
    "confirmedLine": 564,
    "addedAt": "2026-05-19",
    "addedBy": "Worker"
  },
  {
    "order": 6,
    "stepName": "buildEvidenceReceipt",
    "callPattern": "buildEvidenceReceipt(",
    "confirmedLine": 858,
    "addedAt": "2026-05-19",
    "addedBy": "Worker"
  },
  {
    "order": 7,
    "stepName": "buildRouteAuditMemoryCapture",
    "callPattern": "buildRouteAuditMemoryCapture(",
    "confirmedLine": 927,
    "addedAt": "2026-05-19",
    "addedBy": "Worker"
  },
  {
    "order": 8,
    "stepName": "appendAuditEvent_final",
    "callPattern": "appendAuditEvent(",
    "confirmedLine": 944,
    "addedAt": "2026-05-19",
    "addedBy": "Worker"
  }
]
```

Update `confirmedLine` values if pre-flight grep finds different lines.

### Task 2 — Guard script

Create `governance/compat/check_execute_route_step_sequence.py`.

Detection logic:

```python
def _find_first_call_line(lines: list[str], pattern: str) -> int | None:
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith("import ") or stripped.startswith("//"):
            continue
        if pattern in line:
            return i
    return None
```

For each step in registry order:
- Find first occurrence line
- If not found: violation (missing step)
- If found line <= previous step line: violation (order broken)

Two modes: `--check` (default, exit 0 even on violation), `--enforce`
(exit 2 on violation). `--json` emits JSON report.

### Task 3 — Policy file

Create `governance/toolkit/05_OPERATION/CVF_EXECUTE_ROUTE_STEP_SEQUENCE_GUARD.md`.

Required sections: Purpose, Rule (8 canonical steps + detection method),
Enforcement Surface, Registry file path, Maintenance note (update registry
when route.ts step order changes), Related Artifacts, Final Clause.

### Task 4 — Test file

Create `governance/compat/test_check_execute_route_step_sequence.py`.

Required test cases:

- `test_current_route_passes` — run guard against actual `route.ts` → 0 violations
- `test_missing_step` — synthetic route with one pattern removed → 1 missing-step violation
- `test_swapped_steps` — synthetic route with steps 3 and 4 swapped → 1 order violation
- `test_first_occurrence_used` — pattern appears on import line earlier; guard uses first
  non-import occurrence → no false positive, correct line detected

Use `route.ts` content loaded as string for test_current_route_passes.
Use inline string fixtures for broken cases (do not modify real route.ts).

### Task 5 — Maintenance note in GC-018

The GC-018 for C3 MUST include this maintenance obligation:

> Any future refactor that changes the call order, renames a function, or
> adds a mandatory step to `route.ts` MUST update
> `CVF_EXECUTE_ROUTE_STEP_SEQUENCE_REGISTRY.json` in the same commit.
> Failure to do so will cause the guard to fail on the next CI run.

## Acceptance criteria

- [ ] Current `route.ts` → 0 violations on guard run
- [ ] `test_missing_step` → missing-step violation detected
- [ ] `test_swapped_steps` → order violation detected
- [ ] `test_first_occurrence_used` → no false positive on import-line pattern
- [ ] Guard runs in < 2 seconds
- [ ] Policy file present with all required sections including maintenance note
- [ ] Registry JSON validates (no JSON parse error)

## Completion packet

File `docs/reviews/CVF_C3_EXECUTE_ROUTE_STEP_SEQUENCE_GUARD_COMPLETION_2026-05-19.md`
with evidence trace (command → result → verdict per criterion).

Update V10 handoff HEAD SHA per GC-020 after commit.

## Claim boundary

This work order covers only step-order enforcement for the 8 canonical
call sites in `route.ts`. It does not modify `route.ts`, does not add
new steps, does not cover other route files, and does not claim semantic
validation of what each step does.
