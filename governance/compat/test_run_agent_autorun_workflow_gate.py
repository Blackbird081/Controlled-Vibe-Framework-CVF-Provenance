import json
from pathlib import Path

import governance.compat.run_agent_autorun_workflow_gate as autorun
import governance.compat.run_agent_commit_steward_preflight as steward


def test_range_shape_preflight_blocks_exact_manifest_session_mix(monkeypatch) -> None:
    plan = steward.PathPlan(
        changed_paths=(
            "docs/reviews/example.md",
            "AGENT_HANDOFF_V19_2026-06-15.md",
        ),
        material_paths=("docs/reviews/example.md",),
        protected_session_paths=("AGENT_HANDOFF_V19_2026-06-15.md",),
        trace_artifact_paths=("docs/reviews/example.md",),
        mixed_material_and_session=True,
        exact_manifest_collision_risk=True,
        handoff_sync_only=False,
    )
    monkeypatch.setattr(autorun.steward, "build_path_plan", lambda base, head: plan)

    assert autorun._range_shape_preflight("pre-closure", "base", "head") == 1


def test_range_shape_preflight_allows_split_material_range(monkeypatch) -> None:
    plan = steward.PathPlan(
        changed_paths=("docs/reviews/example.md",),
        material_paths=("docs/reviews/example.md",),
        protected_session_paths=(),
        trace_artifact_paths=("docs/reviews/example.md",),
        mixed_material_and_session=False,
        exact_manifest_collision_risk=False,
        handoff_sync_only=False,
    )
    monkeypatch.setattr(autorun.steward, "build_path_plan", lambda base, head: plan)

    assert autorun._range_shape_preflight("pre-closure", "base", "head") == 0


def test_range_shape_preflight_ignores_pre_dispatch(monkeypatch) -> None:
    monkeypatch.setattr(
        autorun.steward,
        "build_path_plan",
        lambda base, head: (_ for _ in ()).throw(AssertionError("not called")),
    )

    assert autorun._range_shape_preflight("pre-dispatch", "base", "head") == 0


def test_command_manifest_hash_changes_with_command() -> None:
    first = (autorun.GateCommand("one", ("python", "one.py")),)
    second = (autorun.GateCommand("one", ("python", "two.py")),)

    assert autorun._command_manifest_hash(first) != autorun._command_manifest_hash(second)


def test_valid_receipt_requires_exact_context(tmp_path: Path) -> None:
    path = tmp_path / "receipt.json"
    expected = {
        "phase": "pre-implementation",
        "baseSha": "abc1234",
        "headSha": "def5678",
        "commandManifestHash": "manifest",
        "worktreeFingerprint": "worktree",
    }
    path.write_text(
        json.dumps({"schema": autorun.RECEIPT_SCHEMA, "status": "PASS", **expected}),
        encoding="utf-8",
    )

    assert autorun._load_valid_receipt(path, expected)[0]
    stale = {**expected, "worktreeFingerprint": "changed"}
    valid, reason = autorun._load_valid_receipt(path, stale)
    assert not valid
    assert reason == "receipt worktreeFingerprint mismatch"


def test_malformed_receipt_fails_closed(tmp_path: Path) -> None:
    path = tmp_path / "receipt.json"
    path.write_text("{not-json", encoding="utf-8")

    valid, reason = autorun._load_valid_receipt(path, {"phase": "pre-dispatch"})

    assert not valid
    assert reason.startswith("receipt unreadable:")


def test_parallel_runner_retains_all_results_and_failure(monkeypatch) -> None:
    commands = (
        autorun.GateCommand("pass", ("pass",)),
        autorun.GateCommand("fail", ("fail",)),
    )

    def fake_execute(index: int, command: autorun.GateCommand) -> autorun.GateResult:
        return autorun.GateResult(
            index=index,
            name=command.name,
            command=command.command,
            returncode=1 if command.name == "fail" else 0,
            duration_s=0.01,
            output="",
        )

    monkeypatch.setattr(autorun, "_execute", fake_execute)
    results = autorun._run_commands(commands, parallel=True, max_workers=2)

    assert [result.name for result in results] == ["pass", "fail"]
    assert [result.returncode for result in results] == [0, 1]


def test_serial_runner_preserves_manifest_order(monkeypatch) -> None:
    observed: list[str] = []
    commands = (
        autorun.GateCommand("first", ("first",)),
        autorun.GateCommand("second", ("second",)),
    )

    def fake_execute(index: int, command: autorun.GateCommand) -> autorun.GateResult:
        observed.append(command.name)
        return autorun.GateResult(index, command.name, command.command, 0, 0.01, "")

    monkeypatch.setattr(autorun, "_execute", fake_execute)
    autorun._run_commands(commands, parallel=False, max_workers=1)

    assert observed == ["first", "second"]


def test_worktree_fingerprint_changes_with_file_content(tmp_path: Path, monkeypatch) -> None:
    target = tmp_path / "sample.txt"
    target.write_text("one", encoding="utf-8")
    plan = steward.PathPlan(
        changed_paths=("sample.txt",),
        material_paths=("sample.txt",),
        protected_session_paths=(),
        trace_artifact_paths=(),
        mixed_material_and_session=False,
        exact_manifest_collision_risk=False,
        handoff_sync_only=False,
    )
    monkeypatch.setattr(autorun, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(autorun.steward, "build_path_plan", lambda base, head: plan)

    first = autorun._worktree_fingerprint("base", "head")
    target.write_text("two", encoding="utf-8")
    second = autorun._worktree_fingerprint("base", "head")

    assert first != second
