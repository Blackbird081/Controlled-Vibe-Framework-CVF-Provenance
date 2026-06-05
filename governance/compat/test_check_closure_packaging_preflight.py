from __future__ import annotations

import importlib.util
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().with_name("check_closure_packaging_preflight.py")
SPEC = importlib.util.spec_from_file_location("check_closure_packaging_preflight", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


def test_closed_doc_rejects_stale_dispatch_language() -> None:
    text = """
# Example

Status: CLOSED_PASS_BOUNDED

This does not dispatch worker execution.
"""
    issues = MODULE.validate_doc("docs/work_orders/CVF_WO_EXAMPLE.md", text, {"docs/work_orders/CVF_WO_EXAMPLE.md"})
    assert any("stale dispatch/hold/pre-closure" in issue for issue in issues)


def test_corpus_enumeration_rejects_git_listing() -> None:
    text = """
# Example

Status: CLOSED_PASS_BOUNDED

## Corpus Completeness And Report Integrity

- Enumeration command: `git ls-files docs/reviews`
"""
    issues = MODULE.validate_doc("docs/reviews/CVF_EXAMPLE.md", text, {"docs/reviews/CVF_EXAMPLE.md"})
    assert any("git-derived file listing" in issue for issue in issues)


def test_corpus_enumeration_rejects_bare_rg_files() -> None:
    text = """
# Example

Status: CLOSED_PASS_BOUNDED

## Corpus Completeness And Report Integrity

- Enumeration command: `rg --files docs/reviews`
"""
    issues = MODULE.validate_doc("docs/reviews/CVF_EXAMPLE.md", text, {"docs/reviews/CVF_EXAMPLE.md"})
    assert any("--hidden" in issue and "--no-ignore" in issue for issue in issues)


def test_closure_diff_gate_rejects_path_not_in_changed_range() -> None:
    text = """
# Example

Status: CLOSED_PASS_BOUNDED

## Closure Diff Gate

| Requirement | Final artifact | Disposition |
| --- | --- | --- |
| Runtime route | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | SATISFIED |
"""
    issues = MODULE.validate_doc("docs/reviews/CVF_EXAMPLE.md", text, {"docs/reviews/CVF_EXAMPLE.md"})
    assert any("not present in the changed range" in issue for issue in issues)


def test_valid_closed_doc_passes_preflight() -> None:
    text = """
# Example

Status: CLOSED_PASS_BOUNDED

## Closure Diff Gate

| Requirement | Final artifact | Disposition |
| --- | --- | --- |
| Completion | `docs/reviews/CVF_EXAMPLE.md` | SATISFIED |

## Corpus Completeness And Report Integrity

- Enumeration command: `rg --files --hidden --no-ignore docs/reviews/CVF_EXAMPLE.md`
"""
    issues = MODULE.validate_doc("docs/reviews/CVF_EXAMPLE.md", text, {"docs/reviews/CVF_EXAMPLE.md"})
    assert issues == []
