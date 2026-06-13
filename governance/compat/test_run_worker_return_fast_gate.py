from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().with_name("run_worker_return_fast_gate.py")
SPEC = importlib.util.spec_from_file_location("run_worker_return_fast_gate", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class WorkerReturnFastGateTests(unittest.TestCase):
    def test_default_commands_include_reviewer_fast_and_registry_drift(self) -> None:
        labels = [command.name for command in MODULE.build_commands()]

        self.assertEqual(
            labels,
            [
                "corpus scan registry aggregate drift",
                "reviewer-fast governance gate",
                "git diff whitespace check",
            ],
        )

    def test_pytest_targets_run_before_governance_gates(self) -> None:
        commands = MODULE.build_commands(("tests/example_test.py",))

        self.assertEqual(commands[0].name, "focused pytest targets")
        self.assertEqual(
            commands[0].command,
            ("python", "-m", "pytest", "tests/example_test.py", "-q"),
        )


if __name__ == "__main__":
    unittest.main()
