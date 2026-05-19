# CVF Agent Work Order — C1: Workflow Orchestration Guard Hardening

Memory class: SUMMARY_RECORD

Status: CLOSED — C1 public-sync workflow guard hardening implemented and verified.

GC-018 required: No — R0 hardening of existing guard.

## Purpose

Harden `check_workflow_orchestration_guard.py` in the public-sync repo with a
test suite, token-presence fragment matching, an externalized JSON registry, and
receipt emission on `--enforce`. Closes the rebuttal-accepted gap in C1 without
modifying the governance/provenance repo.

## Authority Chain

V2 roadmap (`CVF_WORKFLOW_CHAIN_GOVERNANCE_ROADMAP_V2_2026-05-19.md`) —
authorized after second Reviewer rebuttal returns no-blocking verdict on C1.
No GC-018 required (R0 hardening of existing guard).

## Agent Roles

- **Orchestrator** — dispatches work order; accepts completion packet.
- **Worker** — implements all tasks in public-sync only; runs pre-flight checks
  before writing any code; files completion review upon closure.

## Scope

**Allowed scope:** Public-sync repo (`Controlled-Vibe-Framework-CVF-public-sync`)
only — test file, token-presence replacement, JSON registry, receipt emission.

**Forbidden scope:** Governance/provenance repo edits, policy file modification,
C2/C3/C4 implementation, new guard surfaces not listed in Task 3 registry.

## Required First Reads

1. Public-sync `governance/compat/check_workflow_orchestration_guard.py` (current)
2. `docs/roadmaps/CVF_WORKFLOW_CHAIN_GOVERNANCE_ROADMAP_V2_2026-05-19.md` — C1 section
3. `docs/roadmaps/CVF_WORKFLOW_CHAIN_GOVERNANCE_PROPOSAL_2026-05-19.md` — rebuttal

## Write Ownership

Worker role owns all file creation and modification under this work order.
Only the public-sync repo is writable. Governance repo is read-only for this WO.

## Execution Plan

Tasks 1–4 in sequence: test file → token-presence → JSON registry → receipt.
Each task depends on the guard file read in Required First Reads. Task order
is not flexible — tests (Task 1) must exist before the guard is modified (Task 2).

## Evidence Requirements

Evidence trace block in completion review must cover all 5 acceptance criteria
with: command issued → stdout result → pass/fail verdict.

## Review Gate

Orchestrator reviews completion packet before marking work order CLOSED.
No closure without all acceptance criteria verified with evidence.

## Closure Checklist

- [x] All 5 acceptance criteria verified with evidence trace
- [x] No C1 implementation file created or modified in governance/provenance repo
- [x] Completion review filed in public-sync `docs/reviews/`
- [ ] GC-020 handoff HEAD SHA updated after commit

## Return-To-Orchestrator Conditions

Return immediately if:

- `check_workflow_orchestration_guard.py` does not exist in public-sync
- Token-presence replacement breaks existing COMPLIANT exit
- JSON registry load raises any error

## Target repo

`Controlled-Vibe-Framework-CVF-public-sync` only.

The guard `governance/compat/check_workflow_orchestration_guard.py`
does NOT exist in the governance/provenance repo. All implementation
targets the public-sync sibling repo. Do not create or modify any file
in the governance repo under this work order.

## Source / Predecessor Evidence

- `docs/roadmaps/CVF_WORKFLOW_CHAIN_GOVERNANCE_ROADMAP_V2_2026-05-19.md` — C1 section
- `docs/roadmaps/CVF_WORKFLOW_CHAIN_GOVERNANCE_PROPOSAL_2026-05-19.md` — original proposal + rebuttal
- Public-sync: `governance/compat/check_workflow_orchestration_guard.py` (commit `111daaab`)
- Public-sync: `governance/toolkit/05_OPERATION/CVF_WORKFLOW_ORCHESTRATION_GUARD.md`

## Source-fidelity pre-flight (Worker role must run before writing any code)

```text
1. Confirm check_workflow_orchestration_guard.py exists in public-sync at
   governance/compat/check_workflow_orchestration_guard.py
2. Read its REQUIRED_COMMANDS dict — record exact surface paths and fragments
3. Confirm no test file exists at governance/compat/test_check_workflow_orchestration_guard.py
4. Confirm CVF_WORKFLOW_ORCHESTRATION_REGISTRY.json does NOT exist yet
5. Confirm docs/evidence/workflow-orchestration-guard.jsonl does NOT exist yet
```

## Implementation tasks

### Task 1 — Test file

Create `governance/compat/test_check_workflow_orchestration_guard.py`
in public-sync repo.

Required test cases (pytest):

- `test_compliant_fixture` — all REQUIRED_COMMANDS present → `compliant == True`
- `test_missing_workflow_file` — required file absent → 1 violation, `path` key set
- `test_missing_fragment` — file present but command fragment missing → 1 violation
- `test_fragmented_static_marker` — marker string in workflow YAML → 1 violation
- `test_path_normalization` — backslash in fixture path → no false positive
- `test_json_output_mode` — `--json` flag → valid JSON with `compliant` boolean

Use in-memory fixture strings (no temp files on disk). Each test must
be independent and not depend on repo state.

### Task 2 — Token-presence matching

In `check_workflow_orchestration_guard.py`, replace `_normalize()` with
token-presence matching:

```python
def _fragment_present(text: str, fragment: str) -> bool:
    tokens = fragment.replace("\\", "/").split()
    normalized = text.replace("\\", "/")
    return all(token in normalized for token in tokens)
```

Replace all calls from `_normalize(fragment) not in normalized` to
`not _fragment_present(text, fragment)`.

Keep `_normalize()` for backward-compat if used elsewhere, or remove if
only used in `_check_required_commands`.

### Task 3 — Externalize REQUIRED_COMMANDS

Create `governance/compat/CVF_WORKFLOW_ORCHESTRATION_REGISTRY.json`
in public-sync repo:

```json
[
  {
    "surface": ".github/workflows/public-surface.yml",
    "requiredFragments": ["python scripts/check_public_surface.py"],
    "addedAt": "2026-05-19",
    "addedBy": "Worker"
  },
  {
    "surface": ".github/workflows/cvf-static-ci.yml",
    "requiredFragments": ["python scripts/run_cvf_static_ci_gate.py --json"],
    "addedAt": "2026-05-19",
    "addedBy": "Worker"
  },
  {
    "surface": ".github/workflows/cvf-protected-live-release-gate.yml",
    "requiredFragments": ["python scripts/run_cvf_release_gate_bundle.py --json"],
    "addedAt": "2026-05-19",
    "addedBy": "Worker"
  },
  {
    "surface": ".github/workflows/ci.yml",
    "requiredFragments": [
      "python governance/compat/run_local_governance_hook_chain.py --hook pre-commit",
      "npm run test:run",
      "npm run build"
    ],
    "addedAt": "2026-05-19",
    "addedBy": "Worker"
  },
  {
    "surface": ".github/workflows/cvf-web-ci.yml",
    "requiredFragments": [
      "check_core_compat.py",
      "npm run lint -- --max-warnings=0",
      "npm run build",
      "npm run test:run",
      "npm run test:coverage"
    ],
    "addedAt": "2026-05-19",
    "addedBy": "Worker"
  },
  {
    "surface": "scripts/run_cvf_static_ci_gate.py",
    "requiredFragments": [
      "check_public_surface",
      "check_workflow_orchestration_guard",
      "check_web_build",
      "check_web_typecheck",
      "check_secrets",
      "check_docs_governance_compat",
      "check_static_governance_tests"
    ],
    "addedAt": "2026-05-19",
    "addedBy": "Worker"
  },
  {
    "surface": "governance/compat/run_local_governance_hook_chain.py",
    "requiredFragments": ["check_workflow_orchestration_guard.py"],
    "addedAt": "2026-05-19",
    "addedBy": "Worker"
  }
]
```

Populate from the existing `REQUIRED_COMMANDS` dict — do not invent new
surfaces. Update `check_workflow_orchestration_guard.py` to load this
JSON instead of using the hardcoded dict. Keep exact same validation
logic; only the data source changes.

### Task 4 — Receipt emission

Add to `check_workflow_orchestration_guard.py` in `main()`:

```python
if args.enforce:
    _emit_receipt(report)
```

```python
def _emit_receipt(report: dict) -> None:
    receipt_path = REPO_ROOT / "docs" / "evidence" / "workflow-orchestration-guard.jsonl"
    receipt_path.parent.mkdir(parents=True, exist_ok=True)
    import datetime as dt
    line = json.dumps({
        "timestamp": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "compliant": report["compliant"],
        "violationCount": report["violationCount"],
    }, ensure_ascii=False)
    with receipt_path.open("a", encoding="utf-8") as f:
        f.write(line + "\n")
```

## Acceptance criteria

- [ ] `python governance/compat/check_workflow_orchestration_guard.py` exits 0, prints COMPLIANT
- [ ] `pytest governance/compat/test_check_workflow_orchestration_guard.py` — all 6 tests pass
- [ ] `CVF_WORKFLOW_ORCHESTRATION_REGISTRY.json` is valid JSON; guard loads it without error
- [ ] `python governance/compat/check_workflow_orchestration_guard.py --enforce` appends a line to `docs/evidence/workflow-orchestration-guard.jsonl`
- [ ] No file created or modified in the governance/provenance repo

## Completion packet

File `docs/reviews/CVF_C1_WORKFLOW_GUARD_HARDENING_COMPLETION_2026-05-19.md`
in public-sync repo with evidence trace (command → result → verdict per
acceptance criterion).

## Claim boundary

This work order covers only the four hardening tasks in the public-sync
repo. It does not add C1 to the governance repo hook chain, does not
modify the guard policy file, and does not implement C2/C3/C4.
