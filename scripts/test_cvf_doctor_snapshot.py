#!/usr/bin/env python3
"""Hermetic tests for the cvf_doctor.py capability-snapshot mode and the
run_cvf_release_gate_bundle.py capability environment preflight consumer.

Zero real network calls. Zero real subprocess-to-real-tools where avoidable
-- every command discovery/version-probe call site and every clock read is
injected via a fake callable. The release-bundle wiring tests monkeypatch
`cvf_doctor.run_capability_snapshot_cli` (or the underlying probe call
sites) so no real environment observation is required for those cases.

Authorization: docs/work_orders/CVF_AGENT_WORK_ORDER_RSPB_AI_T2_CAPABILITY_ENVIRONMENT_SNAPSHOT_DOCTOR_ENRICHMENT_AND_PRE_DISPATCH_CONSUMER_IMPLEMENTATION_2026-08-16.md
"""

from __future__ import annotations

import json
import sys
import unittest
from datetime import datetime, timezone
from pathlib import Path
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import cvf_doctor as doctor  # noqa: E402
import run_cvf_release_gate_bundle as bundle  # noqa: E402


FIXED_NOW = datetime(2026, 8, 16, 12, 0, 0, tzinfo=timezone.utc)


def _fixed_now_fn(moment: datetime = FIXED_NOW):
    return lambda: moment


def _fake_which_all_present(name: str) -> str | None:
    return f"/usr/bin/{name}"


def _fake_which_none(name: str) -> str | None:
    return None


def _fake_version_probe_ok(resolved_path: str) -> str:
    return "1.2.3\n"


def _fake_version_probe_raises(resolved_path: str) -> str:
    raise RuntimeError("boom")


def _fake_version_probe_empty(resolved_path: str) -> str:
    return "   \n"


class ObserveCommandTests(unittest.TestCase):
    """One row per Focused Test Matrix availability case, exercised across
    all five allow-listed commands."""

    def test_all_five_commands_successful_probe_are_available_with_bounded_version_and_redacted_path(self):
        for name in doctor.SNAPSHOT_COMMANDS:
            with self.subTest(command=name):
                obs = doctor.observe_command(
                    name,
                    which_fn=_fake_which_all_present,
                    version_probe_fn=_fake_version_probe_ok,
                )
                self.assertEqual(obs.availability, doctor.AVAILABILITY_AVAILABLE)
                self.assertEqual(obs.version, "1.2.3")
                self.assertNotEqual(obs.pathClass, "")
                # Redacted: never the raw resolved path itself.
                self.assertNotIn("/usr/bin", obs.pathClass)
                self.assertIn(
                    obs.pathClass,
                    {
                        doctor.PATH_CLASS_SYSTEM_PATH,
                        doctor.PATH_CLASS_PROJECT_LOCAL,
                        doctor.PATH_CLASS_USER_PATH,
                        doctor.PATH_CLASS_UNKNOWN_PATH_CLASS,
                    },
                )

    def test_command_not_discovered_is_missing_not_unknown(self):
        obs = doctor.observe_command(
            "git", which_fn=_fake_which_none, version_probe_fn=_fake_version_probe_ok
        )
        self.assertEqual(obs.availability, doctor.AVAILABILITY_MISSING)
        self.assertNotEqual(obs.availability, doctor.AVAILABILITY_UNKNOWN)
        self.assertEqual(obs.pathClass, doctor.PATH_CLASS_NOT_DISCOVERED)

    def test_discovered_command_that_raises_is_unknown_not_available(self):
        obs = doctor.observe_command(
            "npm", which_fn=_fake_which_all_present, version_probe_fn=_fake_version_probe_raises
        )
        self.assertEqual(obs.availability, doctor.AVAILABILITY_UNKNOWN)
        self.assertNotEqual(obs.availability, doctor.AVAILABILITY_AVAILABLE)

    def test_discovered_command_with_unusable_output_is_unknown(self):
        obs = doctor.observe_command(
            "npx", which_fn=_fake_which_all_present, version_probe_fn=_fake_version_probe_empty
        )
        self.assertEqual(obs.availability, doctor.AVAILABILITY_UNKNOWN)

    def test_discovered_command_that_times_out_is_unknown(self):
        import subprocess as _subprocess

        def timeout_probe(resolved_path: str) -> str:
            raise _subprocess.TimeoutExpired(cmd=[resolved_path, "--version"], timeout=10)

        obs = doctor.observe_command(
            "node", which_fn=_fake_which_all_present, version_probe_fn=timeout_probe
        )
        self.assertEqual(obs.availability, doctor.AVAILABILITY_UNKNOWN)

    def test_discovered_command_non_zero_return_is_unknown(self):
        def non_zero_probe(resolved_path: str) -> str:
            raise RuntimeError("version probe returned non-zero: 1")

        obs = doctor.observe_command(
            "python", which_fn=_fake_which_all_present, version_probe_fn=non_zero_probe
        )
        self.assertEqual(obs.availability, doctor.AVAILABILITY_UNKNOWN)


class SnapshotBuildTests(unittest.TestCase):
    def test_snapshot_generated_at_injected_time_has_exact_observed_and_expires(self):
        snap = doctor.build_capability_snapshot(
            now_fn=_fixed_now_fn(),
            which_fn=_fake_which_all_present,
            version_probe_fn=_fake_version_probe_ok,
            id_fn=lambda: "fixed-id-0001",
        )
        self.assertEqual(snap.observedAt, FIXED_NOW.isoformat())
        expected_expiry = FIXED_NOW.isoformat().replace("12:00:00", "12:05:00")
        self.assertEqual(snap.expiresAt, expected_expiry)
        self.assertEqual(snap.snapshotId, "fixed-id-0001")
        self.assertEqual(snap.schemaVersion, doctor.SNAPSHOT_SCHEMA_VERSION)
        self.assertEqual(snap.scope, "WORKSPACE_LOCAL")
        self.assertEqual(snap.ttlSeconds, 300)

    def test_snapshot_id_is_unique_across_builds(self):
        snap1 = doctor.build_capability_snapshot(
            now_fn=_fixed_now_fn(), which_fn=_fake_which_all_present,
            version_probe_fn=_fake_version_probe_ok,
        )
        snap2 = doctor.build_capability_snapshot(
            now_fn=_fixed_now_fn(), which_fn=_fake_which_all_present,
            version_probe_fn=_fake_version_probe_ok,
        )
        self.assertNotEqual(snap1.snapshotId, snap2.snapshotId)

    def test_fresh_complete_snapshot_is_ready_pass(self):
        snap = doctor.build_capability_snapshot(
            now_fn=_fixed_now_fn(), which_fn=_fake_which_all_present,
            version_probe_fn=_fake_version_probe_ok,
        )
        self.assertEqual(snap.verificationStatus, doctor.VERIFICATION_PASS)
        ready, reason = doctor.snapshot_is_ready(snap, now_fn=_fixed_now_fn())
        self.assertTrue(ready)
        self.assertEqual(reason, "")

    def test_expired_snapshot_is_non_ready_fail_closed_with_reason(self):
        snap = doctor.build_capability_snapshot(
            now_fn=_fixed_now_fn(), which_fn=_fake_which_all_present,
            version_probe_fn=_fake_version_probe_ok,
        )
        later = datetime(2026, 8, 16, 12, 10, 0, tzinfo=timezone.utc)  # 10 min later > 5 min TTL
        ready, reason = doctor.snapshot_is_ready(snap, now_fn=lambda: later)
        self.assertFalse(ready)
        self.assertTrue(reason)
        self.assertIn("expired", reason)

    def test_malformed_expires_at_is_non_ready_fail_closed_with_reason(self):
        snap = doctor.build_capability_snapshot(
            now_fn=_fixed_now_fn(), which_fn=_fake_which_all_present,
            version_probe_fn=_fake_version_probe_ok,
        )
        snap.expiresAt = "not-a-timestamp"
        ready, reason = doctor.snapshot_is_ready(snap, now_fn=_fixed_now_fn())
        self.assertFalse(ready)
        self.assertTrue(reason)
        self.assertIn("malformed", reason)

    def test_malformed_observed_at_is_non_ready_fail_closed_with_reason(self):
        snap = doctor.build_capability_snapshot(
            now_fn=_fixed_now_fn(), which_fn=_fake_which_all_present,
            version_probe_fn=_fake_version_probe_ok,
        )
        snap.observedAt = ""
        ready, reason = doctor.snapshot_is_ready(snap, now_fn=_fixed_now_fn())
        self.assertFalse(ready)
        self.assertTrue(reason)

    def test_timezone_naive_timestamp_is_non_ready(self):
        snap = doctor.build_capability_snapshot(
            now_fn=_fixed_now_fn(), which_fn=_fake_which_all_present,
            version_probe_fn=_fake_version_probe_ok,
        )
        snap.observedAt = "2026-08-16T12:00:00"
        ready, reason = doctor.snapshot_is_ready(snap, now_fn=_fixed_now_fn())
        self.assertFalse(ready)
        self.assertIn("malformed", reason)

    def test_future_observation_is_non_ready(self):
        snap = doctor.build_capability_snapshot(
            now_fn=_fixed_now_fn(), which_fn=_fake_which_all_present,
            version_probe_fn=_fake_version_probe_ok,
        )
        earlier = datetime(2026, 8, 16, 11, 59, 0, tzinfo=timezone.utc)
        ready, reason = doctor.snapshot_is_ready(snap, now_fn=lambda: earlier)
        self.assertFalse(ready)
        self.assertIn("future", reason)

    def test_tampered_ttl_is_non_ready(self):
        snap = doctor.build_capability_snapshot(
            now_fn=_fixed_now_fn(), which_fn=_fake_which_all_present,
            version_probe_fn=_fake_version_probe_ok,
        )
        snap.ttlSeconds = 600
        ready, reason = doctor.snapshot_is_ready(snap, now_fn=_fixed_now_fn())
        self.assertFalse(ready)
        self.assertIn("ttl", reason)

    def test_wrong_command_set_is_non_ready(self):
        snap = doctor.build_capability_snapshot(
            commands=("git",), now_fn=_fixed_now_fn(),
            which_fn=_fake_which_all_present, version_probe_fn=_fake_version_probe_ok,
        )
        ready, reason = doctor.snapshot_is_ready(snap, now_fn=_fixed_now_fn())
        self.assertFalse(ready)
        self.assertIn("command_set", reason)

    def test_missing_command_makes_snapshot_not_ready(self):
        snap = doctor.build_capability_snapshot(
            now_fn=_fixed_now_fn(), which_fn=_fake_which_none,
            version_probe_fn=_fake_version_probe_ok,
        )
        self.assertEqual(snap.verificationStatus, doctor.VERIFICATION_FAIL)
        ready, reason = doctor.snapshot_is_ready(snap, now_fn=_fixed_now_fn())
        self.assertFalse(ready)
        self.assertIn("not AVAILABLE", reason)

    def test_unknown_command_makes_snapshot_not_ready(self):
        snap = doctor.build_capability_snapshot(
            now_fn=_fixed_now_fn(), which_fn=_fake_which_all_present,
            version_probe_fn=_fake_version_probe_raises,
        )
        self.assertEqual(snap.verificationStatus, doctor.VERIFICATION_WARN)
        ready, reason = doctor.snapshot_is_ready(snap, now_fn=_fixed_now_fn())
        self.assertFalse(ready)


class SerializationRedactionTests(unittest.TestCase):
    def test_output_serialization_has_no_raw_path_or_secret_fields(self):
        snap = doctor.build_capability_snapshot(
            now_fn=_fixed_now_fn(),
            which_fn=lambda name: f"/usr/bin/{name}-real-executable",
            version_probe_fn=_fake_version_probe_ok,
        )
        payload = doctor.snapshot_to_payload(snap, now_fn=_fixed_now_fn())
        serialized = json.dumps(payload)

        # No raw absolute executable path.
        self.assertNotIn("/usr/bin/git-real-executable", serialized)
        self.assertNotIn("real-executable", serialized)
        # No raw repository absolute path.
        self.assertNotIn(str(REPO_ROOT), serialized)
        # No PATH listing, env var, credential, or token field names. (Note:
        # "PATH" itself is not checked as a bare substring because the
        # legitimate redacted `pathClass` field name contains it; the real
        # negative assertions are the raw-path checks above plus these.)
        for forbidden in ("environ", "credential", "token", "secret", "API_KEY", "PATH="):
            self.assertNotIn(forbidden, serialized)

    def test_serialization_contains_only_bounded_version_text(self):
        long_output = "v9.9.9 " + ("x" * 500)

        def long_probe(resolved_path: str) -> str:
            return long_output

        snap = doctor.build_capability_snapshot(
            now_fn=_fixed_now_fn(), which_fn=_fake_which_all_present,
            version_probe_fn=long_probe,
        )
        for command in snap.commands:
            self.assertLessEqual(len(command.version), doctor.VERSION_TEXT_MAX_LENGTH)

    def test_unsafe_version_line_is_redacted(self):
        for unsafe in (
            "tool token=super-secret-value",
            "tool loaded C:/Users/example/private/config",
            "tool loaded /home/example/private/config",
        ):
            with self.subTest(unsafe=unsafe):
                self.assertEqual(
                    doctor.bound_version_text(unsafe),
                    "[REDACTED_UNSAFE_VERSION_OUTPUT]",
                )


class SnapshotCliIsolationTests(unittest.TestCase):
    """Snapshot CLI branch must not invoke env bootstrap, port/socket probe,
    write probe, or full build_checks()."""

    def test_run_capability_snapshot_cli_does_not_call_bootstrap_env(self):
        with mock.patch.object(doctor, "bootstrap_repo_env") as bootstrap_mock:
            doctor.run_capability_snapshot_cli(
                now_fn=_fixed_now_fn(), which_fn=_fake_which_all_present,
                version_probe_fn=_fake_version_probe_ok,
            )
        bootstrap_mock.assert_not_called()

    def test_run_capability_snapshot_cli_does_not_call_build_checks(self):
        with mock.patch.object(doctor, "build_checks") as build_checks_mock:
            doctor.run_capability_snapshot_cli(
                now_fn=_fixed_now_fn(), which_fn=_fake_which_all_present,
                version_probe_fn=_fake_version_probe_ok,
            )
        build_checks_mock.assert_not_called()

    def test_run_capability_snapshot_cli_does_not_call_port_probe(self):
        with mock.patch.object(doctor, "is_port_listening") as port_mock:
            doctor.run_capability_snapshot_cli(
                now_fn=_fixed_now_fn(), which_fn=_fake_which_all_present,
                version_probe_fn=_fake_version_probe_ok,
            )
        port_mock.assert_not_called()

    def test_run_capability_snapshot_cli_does_not_call_write_probe(self):
        with mock.patch.object(doctor, "path_writable") as write_mock:
            doctor.run_capability_snapshot_cli(
                now_fn=_fixed_now_fn(), which_fn=_fake_which_all_present,
                version_probe_fn=_fake_version_probe_ok,
            )
        write_mock.assert_not_called()

    def test_run_capability_snapshot_cli_exit_zero_when_all_available_and_fresh(self):
        payload, exit_code = doctor.run_capability_snapshot_cli(
            now_fn=_fixed_now_fn(), which_fn=_fake_which_all_present,
            version_probe_fn=_fake_version_probe_ok,
        )
        self.assertEqual(exit_code, 0)
        self.assertTrue(payload["ready"])

    def test_run_capability_snapshot_cli_exit_nonzero_when_missing(self):
        payload, exit_code = doctor.run_capability_snapshot_cli(
            now_fn=_fixed_now_fn(), which_fn=_fake_which_none,
            version_probe_fn=_fake_version_probe_ok,
        )
        self.assertNotEqual(exit_code, 0)
        self.assertFalse(payload["ready"])

    def test_run_capability_snapshot_cli_exit_nonzero_when_unknown(self):
        payload, exit_code = doctor.run_capability_snapshot_cli(
            now_fn=_fixed_now_fn(), which_fn=_fake_which_all_present,
            version_probe_fn=_fake_version_probe_raises,
        )
        self.assertNotEqual(exit_code, 0)
        self.assertFalse(payload["ready"])


class LegacyDoctorCompatibilityTests(unittest.TestCase):
    """Existing non-snapshot doctor behavior (JSON shape, exit codes,
    build_checks) stays compatible."""

    def test_build_checks_returns_doctor_check_list(self):
        checks = doctor.build_checks()
        self.assertIsInstance(checks, list)
        self.assertGreater(len(checks), 0)
        ids = {c.id for c in checks}
        self.assertIn("node_available", ids)
        self.assertIn("npm_available", ids)
        self.assertIn("python_available", ids)

    def test_summarize_blocked_on_blocker_fail(self):
        checks = [
            doctor.DoctorCheck("x", "FAIL", "BLOCKER", "blocked thing"),
        ]
        self.assertEqual(doctor.summarize(checks), "BLOCKED")

    def test_summarize_warn_when_only_warnings(self):
        checks = [doctor.DoctorCheck("x", "WARN", "WARNING", "warn thing")]
        self.assertEqual(doctor.summarize(checks), "WARN")

    def test_summarize_pass_when_clean(self):
        checks = [doctor.DoctorCheck("x", "PASS", "OPTIONAL", "ok")]
        self.assertEqual(doctor.summarize(checks), "PASS")

    def test_main_source_still_calls_bootstrap_and_build_checks_outside_snapshot_mode(self):
        import inspect
        source = inspect.getsource(doctor.main)
        self.assertIn("bootstrap_repo_env()", source)
        self.assertIn("build_checks()", source)
        self.assertIn("--capability-snapshot", source)


class ReleasePreflightConsumerTests(unittest.TestCase):
    """release-gate bundle capability environment preflight consumer."""

    def test_check_capability_preflight_message_contains_required_literal(self):
        result = bundle.check_capability_preflight(dry_run=True)
        self.assertIn("Capability environment preflight", result.name)

    def test_dry_run_preflight_is_skip_and_executes_nothing(self):
        with mock.patch.object(doctor, "run_capability_snapshot_cli") as cli_mock:
            result = bundle.check_capability_preflight(dry_run=True)
        cli_mock.assert_not_called()
        self.assertEqual(result.status, "SKIP")

    def test_preflight_pass_uses_snapshot_cli(self):
        fake_payload = {
            "ready": True,
            "commands": [{"name": "git", "availability": "AVAILABLE"}],
        }
        with mock.patch.object(
            bundle.cvf_doctor, "run_capability_snapshot_cli", return_value=(fake_payload, 0)
        ):
            result = bundle.check_capability_preflight(dry_run=False)
        self.assertEqual(result.status, "PASS")

    def test_preflight_fail_uses_snapshot_cli(self):
        fake_payload = {
            "ready": False,
            "readinessReason": "command(s) not AVAILABLE: git",
            "commands": [{"name": "git", "availability": "MISSING"}],
        }
        with mock.patch.object(
            bundle.cvf_doctor, "run_capability_snapshot_cli", return_value=(fake_payload, 1)
        ):
            result = bundle.check_capability_preflight(dry_run=False)
        self.assertEqual(result.status, "FAIL")
        self.assertIn("Capability environment preflight", result.message)

    def test_release_preflight_fail_short_circuits_all_expensive_checks(self):
        fail_payload = {
            "ready": False,
            "readinessReason": "command(s) not AVAILABLE: git",
            "commands": [],
        }
        argv = ["run_cvf_release_gate_bundle.py", "--json"]
        with mock.patch.object(sys, "argv", argv), \
             mock.patch.object(
                 bundle.cvf_doctor, "run_capability_snapshot_cli",
                 return_value=(fail_payload, 1),
             ) as snapshot_mock, \
             mock.patch.object(bundle, "check_web_build") as web_build_mock, \
             mock.patch.object(bundle, "check_ts_typecheck") as typecheck_mock, \
             mock.patch.object(bundle, "check_provider_readiness") as provider_mock, \
             mock.patch.object(bundle, "check_secrets") as secrets_mock, \
             mock.patch.object(bundle, "check_e2e") as e2e_mock, \
             mock.patch.object(bundle, "check_sot3") as sot3_mock:
            with self.assertRaises(SystemExit) as ctx:
                bundle.main()

        snapshot_mock.assert_called_once()
        web_build_mock.assert_not_called()
        typecheck_mock.assert_not_called()
        provider_mock.assert_not_called()
        secrets_mock.assert_not_called()
        e2e_mock.assert_not_called()
        sot3_mock.assert_not_called()
        self.assertNotEqual(ctx.exception.code, 0)

    def test_release_preflight_fail_result_is_secret_safe_fail(self):
        fail_payload = {
            "ready": False,
            "readinessReason": "command(s) not AVAILABLE: git",
            "commands": [],
        }
        argv = ["run_cvf_release_gate_bundle.py", "--json", "--output", "unused-output.json"]
        with mock.patch.object(sys, "argv", ["run_cvf_release_gate_bundle.py", "--json"]), \
             mock.patch.object(
                 bundle.cvf_doctor, "run_capability_snapshot_cli",
                 return_value=(fail_payload, 1),
             ), \
             mock.patch.object(bundle, "check_web_build"), \
             mock.patch.object(bundle, "check_ts_typecheck"), \
             mock.patch.object(bundle, "check_provider_readiness"), \
             mock.patch.object(bundle, "check_secrets"), \
             mock.patch.object(bundle, "check_e2e"), \
             mock.patch.object(bundle, "check_sot3"), \
             mock.patch("builtins.print") as print_mock:
            with self.assertRaises(SystemExit):
                bundle.main()

        printed = "".join(str(call.args[0]) for call in print_mock.call_args_list if call.args)
        payload = json.loads(printed)
        self.assertEqual(payload["gate_result"], "FAIL")
        names = [c["name"] for c in payload["checks"]]
        self.assertIn("Capability environment preflight", names)
        # Secret-safe: no raw path/secret content leaked into the emitted payload.
        self.assertNotIn(str(REPO_ROOT), printed)

    def test_release_preflight_fail_preserves_requested_result_and_manifest_outputs(self):
        fail_payload = {
            "ready": False,
            "readinessReason": "command(s) not AVAILABLE: git",
            "commands": [],
        }
        argv = [
            "run_cvf_release_gate_bundle.py", "--json",
            "--output", "result.json", "--manifest-output", "manifest.json",
        ]
        with mock.patch.object(sys, "argv", argv), \
             mock.patch.object(
                 bundle.cvf_doctor, "run_capability_snapshot_cli",
                 return_value=(fail_payload, 1),
             ), \
             mock.patch.object(bundle, "write_json_payload") as write_result, \
             mock.patch.object(bundle, "write_live_evidence_manifest") as write_manifest:
            with self.assertRaises(SystemExit) as ctx:
                bundle.main()

        self.assertNotEqual(ctx.exception.code, 0)
        write_result.assert_called_once()
        write_manifest.assert_called_once()

    def test_release_preflight_pass_preserves_existing_check_order_and_sot3(self):
        pass_payload = {
            "ready": True,
            "commands": [{"name": "git", "availability": "AVAILABLE"}],
        }
        call_order: list[str] = []

        def record(name, *_args, **_kwargs):
            call_order.append(name)
            return bundle.CheckResult(name, "PASS", "stub")

        with mock.patch.object(sys, "argv", ["run_cvf_release_gate_bundle.py", "--json", "--e2e"]), \
             mock.patch.object(
                 bundle.cvf_doctor, "run_capability_snapshot_cli",
                 return_value=(pass_payload, 0),
             ) as snapshot_mock, \
             mock.patch.object(bundle, "check_web_build", side_effect=lambda *a, **k: record("web_build")), \
             mock.patch.object(bundle, "check_ts_typecheck", side_effect=lambda *a, **k: record("typecheck")), \
             mock.patch.object(bundle, "check_provider_readiness", side_effect=lambda *a, **k: record("provider")), \
             mock.patch.object(bundle, "check_secrets", side_effect=lambda *a, **k: record("secrets")), \
             mock.patch.object(bundle, "check_docs_governance", side_effect=lambda *a, **k: record("docs")), \
             mock.patch.object(bundle, "check_e2e", side_effect=lambda *a, **k: record("e2e")), \
             mock.patch.object(bundle, "check_sot3", side_effect=lambda *a, **k: record("sot3")), \
             mock.patch.object(bundle, "_LAST_SOT3_PAYLOAD", {"overall": "PASS"}):
            with self.assertRaises(SystemExit) as ctx:
                bundle.main()

        self.assertEqual(ctx.exception.code, 0)
        snapshot_mock.assert_called_once()
        self.assertEqual(call_order[0], "web_build")
        self.assertEqual(call_order[-1], "sot3")
        self.assertIn("typecheck", call_order)
        self.assertIn("provider", call_order)
        self.assertIn("secrets", call_order)


class ReleaseDryRunTests(unittest.TestCase):
    def test_release_dry_run_preflight_is_skip_and_no_real_execution(self):
        # Pre-existing dry-run contract (unchanged by this tranche): SOT3 is
        # always SKIP in dry-run, and result_payload() treats a SKIP SOT3
        # payload as not-PASS-supporting, so gate_result is FAIL even though
        # every individual check is SKIP/PASS and nothing real executed. The
        # assertions here only cover what this tranche must guarantee: the
        # preflight snapshot CLI and any real subprocess call are never
        # invoked in dry-run mode.
        with mock.patch.object(sys, "argv", ["run_cvf_release_gate_bundle.py", "--dry-run", "--json"]), \
             mock.patch.object(bundle.cvf_doctor, "run_capability_snapshot_cli") as snapshot_mock, \
             mock.patch.object(bundle, "run_cmd") as run_cmd_mock:
            with self.assertRaises(SystemExit):
                bundle.main()

        snapshot_mock.assert_not_called()
        run_cmd_mock.assert_not_called()


if __name__ == "__main__":
    unittest.main()
