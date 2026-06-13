from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().with_name("check_agent_operation_trace.py")
SPEC = importlib.util.spec_from_file_location("check_agent_operation_trace", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


VALID_TRACE = """
## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Codex |
| Provider or surface | Codex CLI |
| Session or invocation | current session |
| Working directory | repo root |
| Command or tool surface | apply_patch |
| Target paths | docs/work_orders/example.md |
| Allowed scope source | operator instruction |
| Before status evidence | git status --short |
| After status evidence | git status --short |
| Diff evidence | git diff --name-status |
| Approval boundary | operator approved |
| Claim boundary | repo-local evidence only |
"""


class AgentOperationTraceTests(unittest.TestCase):
    def test_changed_work_order_without_trace_is_violation(self) -> None:
        changed = {"docs/work_orders/CVF_AGENT_WORK_ORDER_EXAMPLE.md": {"A"}}
        texts = {"docs/work_orders/CVF_AGENT_WORK_ORDER_EXAMPLE.md": "Status: DISPATCHED\n"}

        violations = MODULE.find_trace_violations(changed, texts)

        self.assertEqual(len(violations), 1)
        self.assertIn("missing or incomplete", violations[0])

    def test_changed_work_order_with_complete_trace_passes(self) -> None:
        changed = {"docs/work_orders/CVF_AGENT_WORK_ORDER_EXAMPLE.md": {"M"}}
        texts = {"docs/work_orders/CVF_AGENT_WORK_ORDER_EXAMPLE.md": VALID_TRACE}

        self.assertEqual(MODULE.find_trace_violations(changed, texts), [])

    def test_completion_review_with_worker_trigger_requires_trace(self) -> None:
        changed = {"docs/reviews/CVF_EXAMPLE_COMPLETION_2026-06-13.md": {"A"}}
        texts = {
            "docs/reviews/CVF_EXAMPLE_COMPLETION_2026-06-13.md": (
                "docType: completion_review\nWorker: Claude\n"
            )
        }

        violations = MODULE.find_trace_violations(changed, texts)

        self.assertEqual(len(violations), 1)

    def test_non_execution_review_is_ignored(self) -> None:
        changed = {"docs/reviews/CVF_NOTE_2026-06-13.md": {"A"}}
        texts = {"docs/reviews/CVF_NOTE_2026-06-13.md": "Status: NOTE\n"}

        self.assertEqual(MODULE.find_trace_violations(changed, texts), [])

    def test_protected_delete_requires_delete_or_rename_disposition(self) -> None:
        changed = {
            "docs/roadmaps/CVF_OLD.md": {"D"},
            "docs/reviews/CVF_EXAMPLE_COMPLETION_2026-06-13.md": {"A"},
        }
        texts = {"docs/reviews/CVF_EXAMPLE_COMPLETION_2026-06-13.md": VALID_TRACE}

        violations = MODULE.find_trace_violations(changed, texts)

        self.assertEqual(len(violations), 1)
        self.assertIn("protected delete/rename", violations[0])

    def test_protected_delete_with_disposition_passes(self) -> None:
        changed = {
            "docs/roadmaps/CVF_OLD.md": {"D"},
            "docs/reviews/CVF_EXAMPLE_COMPLETION_2026-06-13.md": {"A"},
        }
        texts = {
            "docs/reviews/CVF_EXAMPLE_COMPLETION_2026-06-13.md": (
                VALID_TRACE
                + "| Deletion or rename disposition | authorized archive rotation |\n"
            )
        }

        self.assertEqual(MODULE.find_trace_violations(changed, texts), [])


if __name__ == "__main__":
    unittest.main()
