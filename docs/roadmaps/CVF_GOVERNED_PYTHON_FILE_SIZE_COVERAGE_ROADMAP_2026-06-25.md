# CVF Governed Python File Size Coverage Roadmap (GFS-PY)

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: roadmap

Date: 2026-06-25

Index classification: GOVERNED_DOC (not an INDEX_ARTIFACT). This roadmap plans
a bounded upgrade of the existing governed Python size guard and a sequenced
split of one oversized checker monolith. It is not a registry, generated
aggregate, resolver, or runtime readout.

## Purpose

Close the governance blind spot that governed Python automation
(`governance/compat/*.py`, `scripts/*.py`) is size-checked only in CI by a
flat-threshold guard that does not distinguish a checker from a test, a helper,
or a CLI orchestrator, and is not wired into the local pre-commit hook chain or
the autorun phase gates.

The roadmap also sequences the eventual decomposition of
`governance/compat/check_work_order_dispatch_quality.py` (the dispatch-quality
"central nervous system") so it is split with order and evidence rather than in
one risky regression-prone rewrite.

## Authorization / Decision

The operator requested a Governed Python Checker File-Size Coverage tranche
after observing that the file-size guard excluded `.py` and that the
dispatch-quality monolith had grown to 3056 lines with no class-aware ceiling.
The operator confirmed scope decisions on 2026-06-25:

- upgrade the existing `check_python_automation_size.py` rather than fold `.py`
  into `check_governed_file_size.py` or create a third guard;
- per-class thresholds for `python_checker`, `python_test`,
  `python_library_helper`, and `python_cli_orchestrator`;
- a touch rule where an already-excepted file may be read freely but, when
  modified in a batch, must not grow (net line delta `<= 0` versus `HEAD`);
- wire the guard into the local hook chain and the autorun `pre-implementation`
  phase (no new gate phase) for no-bottleneck early enforcement;
- defer non-governance Python (`EXTENSIONS/`, `tools/`, `governance/skill-library/`)
  to a later tranche, recorded but not enforced now;
- split `check_work_order_dispatch_quality.py` only through the ordered T1-T4
  sequence below, never as a same-tranche side effect of T0.

## Scope

In scope: governed Python under `scripts/` and `governance/compat/`; the
class-aware threshold model; the touch rule; the seedAuthorization model; the
local and autorun wiring of the existing guard; and the ordered T1-T4 split of
the dispatch-quality monolith.

## Non-Goals

Out of scope: any non-governance Python (`EXTENSIONS/`, `tools/`,
`governance/skill-library/`); any duplicate guard; any change to the flat
baseline thresholds; any monolith split inside T0; any network/provider/LLM
behavior; any runtime, public, or provider-readiness claim.

## Design Control Gate

Each tranche opens only through a fresh operator selection, a fresh GC-018, and
a source-verified work order. T1-T4 are held until their predecessor passes.
Splits must be behavior-preserving and proven by the existing dispatch-quality
test suite plus any added focused tests. No tranche may raise a seeded
exception above its frozen line count.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Source fact type | Disposition |
| --- | --- | --- | --- | --- | --- |
| A governed Python size guard already exists and scans scripts and governance/compat | `governance/compat/check_python_automation_size.py` | `SCOPES = ("scripts", "governance/compat")` | `SCOPES` | EXISTS | ACCEPT |
| The existing guard uses a single flat soft/hard threshold, not per-class | `governance/compat/check_python_automation_size.py` | `soft_threshold = int(registry.get("softThresholdLines", 600))`; `hard_threshold = int(registry.get("hardThresholdLines", 1200))` | `softThresholdLines`; `hardThresholdLines` | RUNTIME_BEHAVIOR | ACCEPT |
| The existing guard protects its registry baseline against self-authored exceptions and threshold drift | `governance/compat/check_python_automation_size.py` | `new_exception_requires_manual_review`; `threshold_changed_from_baseline` | `load_json_policy_baseline` | RUNTIME_BEHAVIOR | ACCEPT |
| The Python guard runs only in CI, not in the local hook chain or autorun gate | `.github/workflows/documentation-testing.yml` | `python governance/compat/check_python_automation_size.py --enforce` | `check_python_automation_size` | EXISTS | ACCEPT |
| check_governed_file_size.py excludes governance/compat and scripts and does not classify .py | `governance/compat/check_governed_file_size.py` | `EXCLUDED_PREFIXES`; `CODE_EXTENSIONS = {".ts", ".tsx", ".js", ".jsx"}` | `EXCLUDED_PREFIXES`; `CODE_EXTENSIONS` | RUNTIME_BEHAVIOR | ACCEPT |
| The dispatch-quality monolith is the oversized split target | `governance/compat/check_work_order_dispatch_quality.py` | file length 3056 lines | `check_work_order_dispatch_quality` | EXISTS | ACCEPT |
| The Python guard registry currently holds no exceptions | `governance/compat/CVF_PYTHON_AUTOMATION_SIZE_EXCEPTION_REGISTRY.json` | `"exceptions": []` | `exceptions` | EXISTS | ACCEPT |

Every future GFS-PY work order must refresh exact paths, symbols, and
line/section evidence before dispatch.

## Proposed Thresholds (operator-confirmed 2026-06-25)

| File class | Soft | Near-hard | Hard |
| --- | ---: | ---: | ---: |
| `python_checker` | 700 | 900 | 1000 |
| `python_test` | 900 | 1100 | 1200 |
| `python_library_helper` | 600 | 800 | 900 |
| `python_cli_orchestrator` | 500 | 700 | 800 |

Application:

- under soft: OK;
- over soft: advisory, split if adding new logic;
- near-hard and touched: same batch needs shrink/split evidence or an explicit
  exception;
- over hard: no new logic into the file except a small exception-covered
  bugfix; a refactor tranche must be opened.

## Tranches

### T0 - Bring governed Python under class-aware, locally-enforced size coverage

DONE. Upgraded `check_python_automation_size.py` to per-class
thresholds; add the touch rule (excepted file modified in a batch must be net
`<= 0` lines versus `HEAD`); add the near-hard touched-file shrink/split
requirement; wire the guard into `run_local_governance_hook_chain.py` and the
autorun `pre-implementation` phase; seed legacy exceptions for the files already
over their new class hard threshold (at minimum
`check_work_order_dispatch_quality.py` and its test) with `requiredFollowup`
pointing at T1-T4; record the deferral of non-governance Python. No monolith
split happens in T0.

### T1 - Split markdown table parsing / source verification helpers

DONE (closed at completion `docs/reviews/CVF_GFS_PY_T1_DISPATCH_QUALITY_HELPER_SPLIT_COMPLETION_2026-06-25.md`; monolith 3056 -> 2972, cap lowered to 2972, full suite 86/86 unchanged). Extract the pure markdown-table
parsing helpers (`_parse_markdown_tables`, `_parse_any_markdown_tables`,
`_normalize_table_key`, `_row_value`, `_section_tables`, `_truthy_cell`,
`_clean_manifest_path`, with `_extract_section` moved or imported cleanly) from
`check_work_order_dispatch_quality.py` into a dedicated module,
behavior-preserving, with the existing test suite as the regression anchor, and
ratchet the monolith's registry `approvedMaxLines` down to the new line count.
Dispatch packet:
`docs/baselines/CVF_GC018_GFS_PY_T1_DISPATCH_QUALITY_HELPER_SPLIT_2026-06-25.md`
and `docs/work_orders/CVF_AGENT_WORK_ORDER_GFS_PY_T1_DISPATCH_QUALITY_HELPER_SPLIT_2026-06-25.md`.
Source-verification cell readers are deferred to a later split if they prove to
carry validator logic rather than pure parsing.

### T2 - Split work-order lifecycle / status validators

DONE (closed at completion `docs/reviews/CVF_GFS_PY_T2_LIFECYCLE_STATUS_VALIDATOR_SPLIT_COMPLETION_2026-06-26.md`; monolith 2972 -> 2720, cap lowered to 2720, combined dispatch-quality suites 144/144 unchanged). Extracted lifecycle/status validators into
`governance/compat/check_work_order_dispatch_quality_lifecycle.py`,
behavior-preserving, with focused module tests and the unchanged dispatch-quality
suite as regression anchors.

### T3 - Split source-verification / token-collision validators

DONE (closed at completion `docs/reviews/CVF_GFS_PY_T3_SOURCE_VERIFICATION_TOKEN_COLLISION_SPLIT_COMPLETION_2026-06-26.md`; monolith 2720 -> 2213, cap lowered to 2213, combined dispatch-quality suites 150/150 unchanged). Extracted source-verification and token-collision validators into
`governance/compat/check_work_order_dispatch_quality_source.py`,
behavior-preserving, with focused module tests and the unchanged dispatch-quality
suite as regression anchors.

### T4 - Leave check_work_order_dispatch_quality.py as an orchestrator shell

DONE (closed at completion `docs/reviews/CVF_GFS_PY_T4_ORCHESTRATOR_SHELL_REDUCTION_COMPLETION_2026-06-26.md`; monolith 2213 -> 313, exception ratcheted to 313, combined dispatch-quality suites 150/150 pass). Reduced the file to an
orchestrator shell that loads split implementation modules:
`governance/compat/check_work_order_dispatch_quality_core.py`,
`governance/compat/check_work_order_dispatch_quality_artifacts.py`, and
`governance/compat/check_work_order_dispatch_quality_range.py`.

Each child tranche requires a fresh operator selection, a fresh GC-018, and a
source-verified work order. Splits must be behavior-preserving and proven by the
existing dispatch-quality test suite plus any added focused tests.

## Work Plan

| Tranche | Work | State |
| --- | --- | --- |
| T0 | upgrade the guard to per-class thresholds, add the touch rule, wire it locally and in autorun, seed legacy exceptions | DONE |
| T1 | split markdown table-parsing helpers out of the monolith | DONE |
| T2 | split work-order lifecycle / status validators | DONE |
| T3 | split source-verification / token-collision validators | DONE |
| T4 | reduce the monolith to an orchestrator shell | DONE |

## Acceptance Criteria

- T0: the guard is class-aware, locally and autorun-enforced, COMPLIANT
  repo-wide, with seeded exceptions for all over-hard governance Python and no
  monolith split.
- T1-T4: each split is behavior-preserving, proven by the dispatch-quality test
  suite, and shrinks the monolith toward removal of its exception.

## Verification / Evidence

T0 verification is the read-only guard run before and after seeding, the
15-test focused suite, and the live local hook-chain run. T1-T4 verification is
the unchanged dispatch-quality test suite plus added focused tests for each
extracted module.

## Deferred (recorded, not enforced in this roadmap)

Non-governance Python under `EXTENSIONS/`, `tools/`, and
`governance/skill-library/` is out of scope for GFS-PY. When a future tranche
touches those surfaces, a separate coverage decision is required before
enforcing size thresholds there. This is a `DEFERRED_RECORDED` scope boundary,
not a value-declined lane.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: internal governance checker refactor; no public-sync authorized.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_GFS_PY_T4_ORCHESTRATOR_SHELL_REDUCTION_FOR_CODEX_2026-06-26.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_GFS_PY_T4_ORCHESTRATOR_SHELL_REDUCTION_COMPLETION_2026-06-26.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | this roadmap | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | `governance/compat/CVF_PYTHON_AUTOMATION_SIZE_EXCEPTION_REGISTRY.json` | monolith exception ratcheted to 313 | PASS |
| Registry Markdown | N/A with reason | Python size guard has no companion markdown registry | BLOCKED with reason |
| External evidence digest | N/A | no external evidence digest | N/A with reason |
| System loop interlock | this roadmap | GFS-PY T0-T4 closed | PASS |
| Public export | this roadmap | `DEFERRED_PRIVATE_ONLY` | PASS |
| Session continuity | active session state/front door/handoff | update separately after material commit | PASS |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
| --- | --- | --- |
| T0 status | DONE | PASS |
| T1 status | DONE | PASS |
| T2 status | DONE | PASS |
| T3 status | DONE | PASS |
| T4 status | DONE | PASS |
| Final roadmap status | CLOSED_PASS_BOUNDED | PASS |
| Dispatch-quality monolith exception | ratcheted to 313 | PASS |
| Python size guard | COMPLIANT | PASS |

## Claim Boundary

This roadmap completed an authoring-time size-governance upgrade and an ordered
monolith split. It does not prove runtime behavior of any checker beyond the
size guard, does not change any dispatch-quality validation semantics, and does
not claim production, public, or provider readiness. GFS-PY T0-T4 are closed;
future governed Python size work requires fresh operator authorization and a
fresh source-verified work order.
