from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

import pytest


SOURCE_ROOT = Path(__file__).resolve().parents[1]
WORK_ORDER_PATH = "docs/work_orders/CVF_AGENT_WORK_ORDER_CONTINUITY_DISPATCH_O3_2026-10-11.md"
BASELINE_PATH = "docs/baselines/CVF_GC018_CONTINUITY_DISPATCH_O3_2026-10-11.md"
ACTIVE_WORK_ORDER = "CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json"
NEXT_MOVE = "CVF_SESSION/state/entries/nextAllowedMove.json"
ACTIVE_HANDOFF = "AGENT_HANDOFF_O3_FIXTURE.md"
SESSION_MEMORY = "CVF_SESSION_MEMORY.md"
OTHER_ENTRY = "CVF_SESSION/state/entries/closure.json"
CONTINUITY_PATHS = [ACTIVE_HANDOFF, SESSION_MEMORY, ACTIVE_WORK_ORDER, NEXT_MOVE, OTHER_ENTRY]
DERIVED_OUTPUTS = {
    "CVF_SESSION/ACTIVE_SESSION_STATE.json",
    "CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json",
}
BOUND_BATCH = "CVF-CONTINUITY-DISPATCH-O3-20261011"


@dataclass(frozen=True)
class DispatchFixture:
    root: Path
    base: str
    material: str
    manifest: str
    work_order: str = WORK_ORDER_PATH
    batch: str = BOUND_BATCH


def git(root: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        ["git", *args], cwd=root, capture_output=True, text=True,
        encoding="utf-8", errors="replace", check=False,
    )
    if check and result.returncode:
        raise AssertionError(f"git {' '.join(args)} failed: {result.stderr}")
    return result


def write_text(root: Path, relative: str, text: str) -> None:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def run_generator(root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "governance/compat/generate_active_session_state.py", *args],
        cwd=root, capture_output=True, text=True, encoding="utf-8", errors="replace",
        check=False,
    )


def create_dispatch_repo(
    tmp_path: Path,
    *,
    order_edit: str | None = None,
    baseline_edit: str | None = None,
    bad_authority_hash: bool = False,
    bad_authority_path: bool = False,
    invalid_ledger: bool = False,
) -> DispatchFixture:
    root = tmp_path / "offline dispatch repo"
    root.mkdir()
    git(root, "init", "-q")
    git(root, "config", "user.email", "tests@example.invalid")
    git(root, "config", "user.name", "CVF dispatch fixture")
    git(root, "config", "core.autocrlf", "false")
    write_text(root, ".gitignore", ".cvf/\n")

    for source, destination in (
        ("scripts/cvf_commit_tranche.py", "scripts/cvf_commit_tranche.py"),
        ("governance/compat/generate_active_session_state.py", "governance/compat/generate_active_session_state.py"),
        ("governance/compat/check_dispatch_release_readiness.py", "governance/compat/check_dispatch_release_readiness.py"),
        ("governance/compat/check_work_order_acceptance_ledger.py", "governance/compat/check_work_order_acceptance_ledger.py"),
    ):
        target = root / destination
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(SOURCE_ROOT / source, target)

    # The full session compatibility catalogs are outside this declaration-control
    # fixture. The canonical generator and downstream release evaluator remain real.
    for check_name in ("check_active_session_state.py", "check_next_move_freshness.py"):
        write_text(
            root, f"governance/compat/{check_name}",
            "# Isolated fixture plumbing for unrelated repository-wide catalogs.\n"
            "raise SystemExit(0)\n",
        )

    order_bytes = (SOURCE_ROOT / WORK_ORDER_PATH).read_bytes()
    baseline_bytes = (SOURCE_ROOT / BASELINE_PATH).read_bytes()
    order = order_bytes.decode("utf-8")
    baseline = baseline_bytes.decode("utf-8")
    if invalid_ledger:
        order = order.replace(
            '"schemaVersion":"cvf.workOrderAcceptanceLedger@1.0.0"',
            '"schemaVersion":"cvf.workOrderAcceptanceLedger@invalid"',
            1,
        )
    if order_edit == "missing_batch":
        order, count = re.subn(r"(?m)^Batch ID:.*\n", "", order, count=1)
        assert count == 1
    elif order_edit == "duplicate_batch":
        order += f"\nBatch ID: {BOUND_BATCH}\n"
    elif order_edit == "wrong_batch":
        order = order.replace(f"Batch ID: {BOUND_BATCH}", "Batch ID: CVF-WRONG-BATCH", 1)
        baseline = baseline.replace(f"Batch ID: {BOUND_BATCH}", "Batch ID: CVF-WRONG-BATCH", 1)
    if baseline_edit == "duplicate_batch":
        baseline += f"\nBatch ID: {BOUND_BATCH}\n"

    order_bytes = order.encode("utf-8")
    baseline_bytes = baseline.encode("utf-8")
    order_hash = hashlib.sha256(order_bytes).hexdigest()
    baseline_hash = hashlib.sha256(baseline_bytes).hexdigest()
    authority = {
        "baselinePath": BASELINE_PATH,
        "baselineSha256": baseline_hash,
        "workOrderPath": "docs/work_orders/other.md" if bad_authority_path else WORK_ORDER_PATH,
        "workOrderSha256": "0" * 64 if bad_authority_hash else order_hash,
    }
    core = {
        "schemaVersion": "0.1.0",
        "activeHandoff": ACTIVE_HANDOFF,
        "activeSessionFrontDoor": SESSION_MEMORY,
        "activeStateRegistry": "CVF_SESSION/ACTIVE_SESSION_STATE.json",
        "currentMode": "fixture",
        "currentAuthority": authority,
        "currentAuthoritySyncReason": "fixture pre-dispatch source",
    }
    next_value = "PROGRAM_ID=CVF-CORE; NEXT_ACTION_CLASS=PREPARE; BATCH_ID=OLDER. fixture setup"
    write_text(root, "AGENTS.md", "CVF_SESSION_MEMORY.md CVF_SESSION/ACTIVE_SESSION_STATE.json\n")
    write_text(root, ".gitignore", ".cvf/\n__pycache__/\n*.py[cod]\n")
    write_text(root, "CLAUDE.md", "CVF_SESSION_MEMORY.md CVF_SESSION/ACTIVE_SESSION_STATE.json\n")
    write_text(root, "CVF_SESSION/READ_FIRST.md", "CVF_SESSION_MEMORY.md CVF_SESSION/ACTIVE_SESSION_STATE.json\n")
    write_text(root, "CVF_SESSION/REQUIRED_STARTUP_GUARDS.md", "CVF_SESSION_MEMORY.md CVF_SESSION/ACTIVE_SESSION_STATE.json\n")
    write_text(root, "governance/compat/run_local_governance_hook_chain.py", "# fixture hook contract\n")
    write_text(root, "CVF_SESSION/ACTIVE_REVIEW_QUEUE.json", "{}\n")
    write_text(root, "docs/reviews/archive/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_DIRECTION_CODEX_2026-05-20.md", "# fixture\n")
    write_text(root, "CVF_SESSION/READ_FIRST.md", "CVF_SESSION_MEMORY.md CVF_SESSION/ACTIVE_SESSION_STATE.json\n")
    write_text(root, ACTIVE_HANDOFF, "# Active O3 fixture handoff\n\nStatus: ACTIVE\n")
    write_text(root, SESSION_MEMORY, "# Session memory fixture\n")
    write_text(root, "CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json", json.dumps(core, indent=2) + "\n")
    write_text(
        root, NEXT_MOVE,
        json.dumps({"stateOrder": 1, "stateKey": "nextAllowedMove", "value": next_value}, indent=2) + "\n",
    )
    write_text(
        root, OTHER_ENTRY,
        json.dumps({"stateOrder": 2, "stateKey": "closure", "value": "fixture pending"}, indent=2) + "\n",
    )
    generated = run_generator(root, "--generate")
    assert generated.returncode == 0, generated.stderr + generated.stdout
    git(root, "add", "-A")
    git(root, "commit", "-qm", "fixture base")
    base = git(root, "rev-parse", "HEAD").stdout.strip()

    (root / WORK_ORDER_PATH).parent.mkdir(parents=True, exist_ok=True)
    (root / WORK_ORDER_PATH).write_bytes(order_bytes)
    (root / BASELINE_PATH).parent.mkdir(parents=True, exist_ok=True)
    (root / BASELINE_PATH).write_bytes(baseline_bytes)
    git(root, "add", "--", WORK_ORDER_PATH, BASELINE_PATH)
    git(root, "commit", "-qm", "dispatch packet material")
    material = git(root, "rev-parse", "HEAD").stdout.strip()

    next_value = (
        f"PROGRAM_ID=CVF-CORE; NEXT_ACTION_CLASS=EXECUTE_BOUNDED; BATCH_ID={BOUND_BATCH}. "
        f"Execute {WORK_ORDER_PATH} after committed bound pre-dispatch PASS."
    )
    core["currentAuthoritySyncReason"] = f"fixture material anchor {material}"
    write_text(root, "CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json", json.dumps(core, indent=2) + "\n")
    write_text(
        root, NEXT_MOVE,
        json.dumps({"stateOrder": 3, "stateKey": "nextAllowedMove", "value": next_value}, indent=2) + "\n",
    )
    write_text(root, SESSION_MEMORY, "# Session memory fixture\n\nCurrent handoff: AGENT_HANDOFF_O3_FIXTURE.md\n")
    write_text(
        root, ACTIVE_HANDOFF,
        "# Active O3 fixture handoff\n\nStatus: ACTIVE\n\n"
        "Fixture caller-authored continuity revision after material.\n",
    )
    write_text(
        root, OTHER_ENTRY,
        json.dumps({"stateOrder": 4, "stateKey": "closure", "value": "bounded fixture continuation"}, indent=2) + "\n",
    )
    manifest = f".cvf/runtime/tranche-continuity/{material}.json"
    manifest_data = {"schemaVersion": "cvf.gc020ContinuityManifest.v1", "paths": CONTINUITY_PATHS}
    write_text(root, manifest, json.dumps(manifest_data, indent=2) + "\n")
    return DispatchFixture(root, base, material, manifest)


def helper_args(fixture: DispatchFixture, *, base: str | None = None, execute: bool = False) -> list[str]:
    argv = [
        "--mode", "resume", "--resume-material-sha", fixture.material,
        "--base", base or fixture.base,
        "--continuity-manifest", fixture.manifest,
        "--active-work-order", fixture.work_order,
    ]
    if execute:
        argv.extend(["--continuity-message", "fixture continuity", "--execute"])
    return argv


def invoke_cli(fixture: DispatchFixture, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "scripts/cvf_commit_tranche.py", *args],
        cwd=fixture.root, capture_output=True, text=True, encoding="utf-8", errors="replace",
        check=False,
    )


def output_record(result: subprocess.CompletedProcess[str]) -> dict:
    lines = [line for line in result.stdout.splitlines() if line.strip()]
    assert lines, result.stderr
    return json.loads(lines[-1])


def snapshot(root: Path) -> tuple[str, str, str, dict[str, str]]:
    status = git(root, "status", "--porcelain=v1", "--untracked-files=all").stdout
    tree = git(root, "write-tree").stdout.strip()
    hashes: dict[str, str] = {}
    for path in sorted(p for p in root.rglob("*") if p.is_file() and ".git" not in p.parts):
        hashes[path.relative_to(root).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    return git(root, "rev-parse", "HEAD").stdout.strip(), tree, status, hashes


def load_helper_module():
    path = SOURCE_ROOT / "scripts/cvf_commit_tranche.py"
    spec = importlib.util.spec_from_file_location("cvf_dispatch_helper_under_test", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_bound_real_cli_generator_release_and_read_only_recheck(tmp_path: Path) -> None:
    fixture = create_dispatch_repo(tmp_path)
    before = snapshot(fixture.root)
    dry_run = invoke_cli(fixture, *helper_args(fixture))
    assert dry_run.returncode == 0, dry_run.stderr
    dry_result = output_record(dry_run)
    assert dry_result["terminalState"] == "DRY_RUN_CONTINUITY_PLAN_VALIDATED"
    assert "--active-work-order" in dry_result["resumeArgvTemplate"]
    assert dry_result["resumeArgvTemplate"][dry_result["resumeArgvTemplate"].index("--active-work-order") + 1] == WORK_ORDER_PATH
    assert snapshot(fixture.root) == before

    first = invoke_cli(fixture, *helper_args(fixture, execute=True))
    assert first.returncode == 0, first.stderr + first.stdout
    first_result = output_record(first)
    assert first_result["terminalState"] == "COMPLETE_ONE_MATERIAL_ONE_CONTINUITY"
    continuity = git(fixture.root, "rev-parse", "HEAD").stdout.strip()
    assert git(fixture.root, "rev-parse", "HEAD^").stdout.strip() == fixture.material
    changed = set(git(fixture.root, "diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD").stdout.split())
    assert changed == set(CONTINUITY_PATHS) | DERIVED_OUTPUTS
    handoff = (fixture.root / ACTIVE_HANDOFF).read_text(encoding="utf-8")
    assert handoff.startswith("# Active O3 fixture handoff\n")
    assert handoff.count("CVF-GC020-MATERIAL-SHA:START") == 1
    assert fixture.material in handoff and f"Batch ID: `{BOUND_BATCH}`." in handoff

    before_recheck = snapshot(fixture.root)
    second = invoke_cli(fixture, *helper_args(fixture, execute=True))
    assert second.returncode == 0, second.stderr + second.stdout
    assert output_record(second)["terminalState"] == "ALREADY_SYNCHRONIZED"
    assert git(fixture.root, "rev-parse", "HEAD").stdout.strip() == continuity
    assert snapshot(fixture.root) == before_recheck


@pytest.mark.parametrize(
    ("mutation", "expected_code"),
    [
        ("missing_batch", "DISPATCH_BATCH_ID_REJECTED"),
        ("duplicate_order_batch", "DISPATCH_BATCH_ID_REJECTED"),
        ("duplicate_baseline_batch", "DISPATCH_BATCH_ID_REJECTED"),
        ("wrong_batch", "DISPATCH_NEXT_MOVE_REJECTED"),
        ("bad_authority_hash", "DISPATCH_PACKET_HASH_MISMATCH"),
        ("bad_authority_path", "DISPATCH_AUTHORITY_REJECTED"),
        ("stale_next_move", "DISPATCH_NEXT_MOVE_REJECTED"),
        ("suffix_next_path", "DISPATCH_NEXT_MOVE_REJECTED"),
        ("prefix_next_path", "DISPATCH_NEXT_MOVE_REJECTED"),
        ("wrong_parent", "MATERIAL_PARENT_MISMATCH"),
    ],
)
def test_bound_preflight_rejections_leave_helper_state_unchanged(
    tmp_path: Path, mutation: str, expected_code: str
) -> None:
    kwargs = {
        "order_edit": "missing_batch" if mutation == "missing_batch" else
                      "duplicate_batch" if mutation == "duplicate_order_batch" else
                      "wrong_batch" if mutation == "wrong_batch" else None,
        "baseline_edit": "duplicate_batch" if mutation == "duplicate_baseline_batch" else None,
        "bad_authority_hash": mutation == "bad_authority_hash",
        "bad_authority_path": mutation == "bad_authority_path",
    }
    fixture = create_dispatch_repo(tmp_path, **kwargs)
    if mutation == "stale_next_move":
        entry_path = fixture.root / NEXT_MOVE
        entry = json.loads(entry_path.read_text(encoding="utf-8"))
        entry["value"] = entry["value"].replace(f"BATCH_ID={BOUND_BATCH}", "BATCH_ID=CVF-STALE")
        entry_path.write_text(json.dumps(entry, indent=2) + "\n", encoding="utf-8", newline="\n")
    if mutation in {"suffix_next_path", "prefix_next_path"}:
        entry_path = fixture.root / NEXT_MOVE
        entry = json.loads(entry_path.read_text(encoding="utf-8"))
        wrong_path = WORK_ORDER_PATH + ".other" if mutation == "suffix_next_path" else "wrong/" + WORK_ORDER_PATH
        entry["value"] = entry["value"].replace(WORK_ORDER_PATH, wrong_path)
        entry_path.write_text(json.dumps(entry, indent=2) + "\n", encoding="utf-8", newline="\n")
    if mutation == "wrong_parent":
        expected_base = fixture.material
    else:
        expected_base = fixture.base
    before = snapshot(fixture.root)
    result = invoke_cli(fixture, *helper_args(fixture, base=expected_base))
    assert result.returncode == 3, result.stderr
    record = output_record(result)
    assert record["terminalState"] == "CONTINUITY_VALIDATION_FAILED"
    assert record["diagnosticCode"] == expected_code
    assert snapshot(fixture.root) == before


def test_dirty_authority_packet_fails_before_helper_mutation(tmp_path: Path) -> None:
    fixture = create_dispatch_repo(tmp_path)
    with (fixture.root / WORK_ORDER_PATH).open("a", encoding="utf-8", newline="\n") as stream:
        stream.write("\nlocal dirty packet mutation\n")
    before = snapshot(fixture.root)
    result = invoke_cli(fixture, *helper_args(fixture))
    assert result.returncode == 3
    assert output_record(result)["diagnosticCode"] == "DISPATCH_PACKET_NOT_CLEAN"
    assert snapshot(fixture.root) == before


def test_packet_latest_commit_must_be_the_material_commit(tmp_path: Path) -> None:
    fixture = create_dispatch_repo(tmp_path)
    order_path = fixture.root / WORK_ORDER_PATH
    order_path.write_bytes(order_path.read_bytes() + b"\npacket moved to another commit\n")
    core_path = fixture.root / ACTIVE_WORK_ORDER
    core = json.loads(core_path.read_text(encoding="utf-8"))
    core["currentAuthority"]["workOrderSha256"] = hashlib.sha256(order_path.read_bytes()).hexdigest()
    core_path.write_text(json.dumps(core, indent=2) + "\n", encoding="utf-8", newline="\n")
    git(fixture.root, "add", "--", WORK_ORDER_PATH)
    git(fixture.root, "commit", "-qm", "packet latest-commit mutation")
    before = snapshot(fixture.root)
    result = invoke_cli(fixture, *helper_args(fixture))
    assert result.returncode == 3
    assert output_record(result)["diagnosticCode"] == "DISPATCH_PACKET_COMMIT_MISMATCH"
    assert snapshot(fixture.root) == before


def test_symlink_authority_packet_is_rejected_when_supported(tmp_path: Path) -> None:
    fixture = create_dispatch_repo(tmp_path)
    work_order = fixture.root / WORK_ORDER_PATH
    replacement = fixture.root / "replacement.md"
    replacement.write_text(work_order.read_text(encoding="utf-8"), encoding="utf-8")
    work_order.unlink()
    try:
        work_order.symlink_to(replacement)
    except OSError as exc:
        pytest.skip(f"symlink creation unavailable in this environment: {exc.__class__.__name__}")
    before = snapshot(fixture.root)
    result = invoke_cli(fixture, *helper_args(fixture))
    assert result.returncode == 3
    assert output_record(result)["diagnosticCode"] == "DISPATCH_SOURCE_UNSAFE"
    assert snapshot(fixture.root) == before


def test_generated_binding_disagreement_is_rejected_after_real_generation(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    fixture = create_dispatch_repo(tmp_path)
    helper = load_helper_module()
    helper.REPO_ROOT = fixture.root
    original_command = helper._command

    def corrupt_after_canonical_generation(argv: list[str]):
        result = original_command(argv)
        if "governance/compat/generate_active_session_state.py" in argv and "--generate" in argv:
            path = fixture.root / helper.AGGREGATE
            value = json.loads(path.read_text(encoding="utf-8"))
            value["nextAllowedMove"] = "stale output injected after canonical generator"
            path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8", newline="\n")
        return result

    monkeypatch.setattr(helper, "_command", corrupt_after_canonical_generation)
    assert helper.main(helper_args(fixture, execute=True)) == 3
    result = json.loads(capsys.readouterr().out.strip().splitlines()[-1])
    assert result["terminalState"] == "CONTINUITY_VALIDATION_FAILED"
    assert result["diagnosticCode"] == "GENERATED_DISPATCH_BINDING_DISAGREEMENT"
    assert git(fixture.root, "rev-parse", "HEAD").stdout.strip() == fixture.material


def test_release_rejection_preserves_continuity_commit_and_reports_exact_argv(tmp_path: Path) -> None:
    fixture = create_dispatch_repo(tmp_path, invalid_ledger=True)
    result = invoke_cli(fixture, *helper_args(fixture, execute=True))
    assert result.returncode == 5, result.stderr + result.stdout
    record = output_record(result)
    assert record["terminalState"] == "CONTINUITY_POSTCOMMIT_VALIDATION_FAILED"
    assert record["failedCommand"] == [
        sys.executable, "governance/compat/check_dispatch_release_readiness.py",
        "--active-work-order", WORK_ORDER_PATH, "--head", "HEAD", "--enforce", "--json",
    ]
    assert git(fixture.root, "rev-parse", "HEAD^").stdout.strip() == fixture.material
    assert git(fixture.root, "status", "--porcelain=v1").stdout == ""
    changed = set(git(fixture.root, "diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD").stdout.split())
    assert changed == set(CONTINUITY_PATHS) | DERIVED_OUTPUTS


def test_retry_keeps_active_work_order_in_resume_template(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    fixture = create_dispatch_repo(tmp_path)
    helper = load_helper_module()
    helper.REPO_ROOT = fixture.root
    original_command = helper._command
    failed_once = False

    def fail_first_continuity_commit(argv: list[str]):
        nonlocal failed_once
        if argv[:2] == ["git", "commit"] and not failed_once:
            failed_once = True
            raise helper.CommandFailure(argv)
        return original_command(argv)

    monkeypatch.setattr(helper, "_command", fail_first_continuity_commit)
    argv = helper_args(fixture, execute=True)
    assert helper.main(argv) == 4
    failed = json.loads(capsys.readouterr().out.strip().splitlines()[-1])
    assert failed["terminalState"] == "CONTINUITY_COMMIT_FAILED"
    template = failed["resumeArgvTemplate"]
    assert template[template.index("--active-work-order") + 1] == WORK_ORDER_PATH

    monkeypatch.setattr(helper, "_command", original_command)
    assert helper.main(argv) == 0
    succeeded = json.loads(capsys.readouterr().out.strip().splitlines()[-1])
    assert succeeded["terminalState"] == "COMPLETE_ONE_MATERIAL_ONE_CONTINUITY"
    assert git(fixture.root, "rev-parse", "HEAD^").stdout.strip() == fixture.material


def test_active_work_order_is_rejected_in_material_mode_without_mutation(tmp_path: Path) -> None:
    fixture = create_dispatch_repo(tmp_path)
    before = snapshot(fixture.root)
    result = invoke_cli(
        fixture, "--mode", "material", "--base", fixture.base,
        "--message", "must not run", "--active-work-order", WORK_ORDER_PATH,
    )
    assert result.returncode == 2
    assert output_record(result)["terminalState"] == "ARGUMENT_VALIDATION_FAILED"
    assert snapshot(fixture.root) == before
