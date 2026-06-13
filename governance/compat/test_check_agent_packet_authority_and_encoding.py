from __future__ import annotations

import importlib.util
import sys
import tempfile
from pathlib import Path
from unittest.mock import patch


MODULE_PATH = Path(__file__).resolve().with_name("check_agent_packet_authority_and_encoding.py")
SPEC = importlib.util.spec_from_file_location("check_agent_packet_authority_and_encoding", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def test_review_packet_rejects_missing_authority_artifact() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        repo_root = Path(tmp)
        text = (
            "Worker return references "
            "`docs/work_orders/CVF_AGENT_WORK_ORDER_MISSING_FOR_CLAUDE_2026-06-10.md`.\n"
        )
        with patch.object(MODULE, "REPO_ROOT", repo_root):
            issues = MODULE.find_authority_reference_violations(
                "docs/reviews/CVF_EXAMPLE_WORKER_RETURN_2026-06-10.md",
                text,
            )
    assert any("missing authority artifact" in issue for issue in issues)


def test_review_packet_accepts_existing_authority_artifact() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        repo_root = Path(tmp)
        authority = repo_root / "docs" / "work_orders" / "CVF_AGENT_WORK_ORDER_PRESENT_2026-06-10.md"
        authority.parent.mkdir(parents=True, exist_ok=True)
        authority.write_text("Status: DISPATCHED\n", encoding="utf-8")
        text = (
            "Worker return references "
            "`docs/work_orders/CVF_AGENT_WORK_ORDER_PRESENT_2026-06-10.md`.\n"
        )
        with patch.object(MODULE, "REPO_ROOT", repo_root):
            issues = MODULE.find_authority_reference_violations(
                "docs/reviews/CVF_EXAMPLE_WORKER_RETURN_2026-06-10.md",
                text,
            )
    assert issues == []


def test_added_non_ascii_line_requires_exception_marker() -> None:
    issues = MODULE.find_non_ascii_line_violations(
        "docs/reviews/CVF_EXAMPLE_WORKER_RETURN_2026-06-10.md",
        [MODULE.AddedLine(7, "Result - contains smart dash \u2014 here")],
        has_exception=False,
    )
    assert any("non-ASCII" in issue for issue in issues)


def test_added_non_ascii_line_allows_recorded_exception_marker() -> None:
    issues = MODULE.find_non_ascii_line_violations(
        "docs/reviews/CVF_EXAMPLE_WORKER_RETURN_2026-06-10.md",
        [MODULE.AddedLine(7, "Quoted filename: T\u00e0i li\u1ec7u.pdf")],
        has_exception=True,
    )
    assert issues == []


def test_provider_specific_agent_file_rejected_as_source_authority() -> None:
    text = (
        "## Source Authority\n\n"
        "| Source | Path | Role |\n"
        "| --- | --- | --- |\n"
        "| Repository agent guidance | `CLAUDE.md` | canonical routing evidence |\n"
    )
    issues = MODULE.find_provider_specific_authority_violations(
        "docs/reference/CVF_EXAMPLE_MATRIX_2026-06-13.md",
        text,
    )
    assert any("provider-specific" in issue for issue in issues)


def test_provider_specific_agent_file_allowed_when_marked_not_cvf_source() -> None:
    text = (
        "## Finding-To-Governance Learning Disposition\n\n"
        "| Finding | Disposition |\n"
        "| --- | --- |\n"
        "| Provider-specific `CLAUDE.md` guidance cited by worker | NOT_CVF_SOURCE |\n"
    )
    issues = MODULE.find_provider_specific_authority_violations(
        "docs/reviews/CVF_EXAMPLE_COMPLETION_2026-06-13.md",
        text,
    )
    assert issues == []


def test_cvf_session_memory_front_door_not_confused_with_provider_memory() -> None:
    text = (
        "## Source Authority\n\n"
        "| Source | Path | Role |\n"
        "| --- | --- | --- |\n"
        "| Active front door | `CVF_SESSION_MEMORY.md` | session continuity |\n"
    )
    issues = MODULE.find_provider_specific_authority_violations(
        "docs/reviews/CVF_EXAMPLE_COMPLETION_2026-06-13.md",
        text,
    )
    assert issues == []
