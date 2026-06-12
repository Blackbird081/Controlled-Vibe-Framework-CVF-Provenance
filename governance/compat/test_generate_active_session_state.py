import json
import tempfile
import unittest
from pathlib import Path

from governance.compat.generate_active_session_state import (
    aggregate_entry,
    build_state,
    entry_filename,
    render_json,
    validate_aggregate_matches_sources,
)


class GenerateActiveSessionStateTests(unittest.TestCase):
    def test_entry_filename_uses_safe_slug(self) -> None:
        self.assertEqual(
            entry_filename("nextAllowedMove"),
            "nextAllowedMove.json",
        )
        self.assertEqual(
            entry_filename("Policy Local / PL-S1"),
            "Policy-Local-PL-S1.json",
        )

    def test_build_state_sorts_by_state_order_and_expands_entries(self) -> None:
        state = build_state(
            {"schemaVersion": "0.1.0"},
            [
                {"stateOrder": 3, "stateKey": "b", "value": "B"},
                {"stateOrder": 2, "stateKey": "a", "value": {"nested": True}},
            ],
        )

        self.assertEqual(list(state.keys()), ["schemaVersion", "a", "b"])
        self.assertEqual(state["a"], {"nested": True})

    def test_aggregate_entry_requires_state_key_and_value(self) -> None:
        self.assertEqual(
            aggregate_entry({"stateOrder": 1, "stateKey": "mode", "value": "x"}),
            ("mode", "x"),
        )
        with self.assertRaises(ValueError):
            aggregate_entry({"stateOrder": 1, "value": "x"})
        with self.assertRaises(ValueError):
            aggregate_entry({"stateOrder": 1, "stateKey": "mode"})

    def test_validate_aggregate_matches_sources_detects_drift(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            core = root / "core.json"
            entries = root / "entries"
            aggregate = root / "aggregate.json"
            entries.mkdir()
            core.write_text(render_json({"schemaVersion": "0.1.0"}), encoding="utf-8")
            (entries / "mode.json").write_text(
                render_json({"stateOrder": 2, "stateKey": "mode", "value": "ready"}),
                encoding="utf-8",
            )
            aggregate.write_text(
                json.dumps({"schemaVersion": "0.1.0", "mode": "stale"}),
                encoding="utf-8",
            )

            violations = validate_aggregate_matches_sources(aggregate, core, entries)

        self.assertEqual(len(violations), 1)
        self.assertIn("ACTIVE_SESSION_STATE.json drifted", violations[0])


if __name__ == "__main__":
    unittest.main()
