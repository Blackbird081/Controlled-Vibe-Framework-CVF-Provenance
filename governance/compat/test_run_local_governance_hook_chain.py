from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().with_name("run_local_governance_hook_chain.py")
SPEC = importlib.util.spec_from_file_location("run_local_governance_hook_chain", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class LocalGovernanceHookChainTests(unittest.TestCase):
    def test_reviewer_fast_chain_contains_early_reviewer_checks(self) -> None:
        labels = [label for label, _ in MODULE.HOOK_CHAINS["reviewer-fast"]]

        self.assertIn("closure packaging preflight", labels)
        self.assertIn("agent packet authority and encoding", labels)
        self.assertIn("machine closure package", labels)
        self.assertIn("public export disposition quality", labels)
        self.assertIn("rescan intelligence hardening", labels)
        self.assertIn("corpus scan registry", labels)
        self.assertIn("active session state compatibility", labels)

    def test_latency_sensitive_hooks_default_to_parallel(self) -> None:
        self.assertIn("reviewer-fast", MODULE.PARALLEL_BY_DEFAULT_HOOKS)
        self.assertIn("pre-commit", MODULE.PARALLEL_BY_DEFAULT_HOOKS)
        self.assertIn("pre-push", MODULE.PARALLEL_BY_DEFAULT_HOOKS)


if __name__ == "__main__":
    unittest.main()
