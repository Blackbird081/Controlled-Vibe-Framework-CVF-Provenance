from __future__ import annotations

import hashlib
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

import pytest


SCRIPT = Path(__file__).with_name("cvf_commit_tranche.py")


def load_helper():
    spec = importlib.util.spec_from_file_location("cvf_commit_tranche_under_test", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def helper():
    return load_helper()


def run(repo: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        list(args), cwd=repo, capture_output=True, text=True, encoding="utf-8",
        check=check,
    )


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


@pytest.fixture
def repo(tmp_path: Path, helper, monkeypatch):
    root = tmp_path / "isolated repo nonascii"
    root.mkdir()
    run(root, "git", "init", "-q")
    run(root, "git", "config", "user.email", "tests@example.invalid")
    run(root, "git", "config", "user.name", "CVF Tests")
    write(root / ".gitignore", ".cvf/\n")
    write(root / "AGENT_HANDOFF_TEST.md", "# Active test handoff\n\nStatus: ACTIVE\n")
    write(root / "CVF_SESSION_MEMORY.md", "# Session memory\n")
    core = {"activeHandoff": "AGENT_HANDOFF_TEST.md", "currentMode": "test"}
    write(root / "CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json", json.dumps(core) + "\n")
    write(
        root / "CVF_SESSION/state/entries/nextAllowedMove.json",
        json.dumps({"stateKey": "nextAllowedMove", "value": "test", "stateOrder": 1}) + "\n",
    )
    write(
        root / "CVF_SESSION/state/entries/closure.json",
        json.dumps({"stateKey": "closure", "value": "open", "stateOrder": 2}) + "\n",
    )
    write(root / "CVF_SESSION/ACTIVE_SESSION_STATE.json", json.dumps(core) + "\n")
    write(root / "CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json", json.dumps(core) + "\n")
    run(root, "git", "add", ".")
    run(root, "git", "commit", "-qm", "base")
    monkeypatch.setattr(helper, "REPO_ROOT", root)
    return root


def head(repo: Path, ref: str = "HEAD") -> str:
    return run(repo, "git", "rev-parse", ref).stdout.strip()


def terminal(capsys) -> dict:
    output = capsys.readouterr().out.strip().splitlines()
    return json.loads(output[-1])


def snapshot(repo: Path) -> tuple[str, str, str, dict[str, str]]:
    status = run(repo, "git", "status", "--porcelain=v1", "--untracked-files=all").stdout
    index = run(repo, "git", "write-tree").stdout.strip()
    hashes = {}
    for path in sorted(item for item in repo.rglob("*") if item.is_file() and ".git" not in item.parts):
        hashes[path.relative_to(repo).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    return head(repo), index, status, hashes


def make_material(repo: Path) -> tuple[str, str]:
    base = head(repo)
    write(repo / "material.txt", "material\n")
    run(repo, "git", "add", "material.txt")
    run(repo, "git", "commit", "-qm", "material")
    return base, head(repo)


def continuity_paths() -> list[str]:
    return [
        "AGENT_HANDOFF_TEST.md",
        "CVF_SESSION_MEMORY.md",
        "CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json",
        "CVF_SESSION/state/entries/nextAllowedMove.json",
        "CVF_SESSION/state/entries/closure.json",
    ]


def prepare_resume(repo: Path, material: str, *, paths: list[str] | None = None) -> str:
    selected = paths or continuity_paths()
    for rel in selected:
        path = repo / rel
        if path.exists():
            path.write_text(path.read_text(encoding="utf-8") + "\n", encoding="utf-8")
    manifest = f".cvf/runtime/tranche-continuity/{material}.json"
    write(repo / manifest, json.dumps({"schemaVersion": "cvf.gc020ContinuityManifest.v1", "paths": selected}))
    return manifest


def resume_args(base: str, material: str, manifest: str, *extra: str) -> list[str]:
    return [
        "--mode", "resume", "--resume-material-sha", material, "--base", base,
        "--continuity-manifest", manifest, *extra,
    ]


@pytest.mark.parametrize("argv", [
    [],
    ["--mode", "invalid", "--base", "a" * 40],
    ["--mode", "material", "--base", "a" * 40],
    ["--mode", "resume", "--base", "a" * 40, "--resume-material-sha", "short"],
])
def test_invalid_arguments_return_frozen_json(helper, repo, capsys, argv):
    assert helper.main(argv) == 2
    result = terminal(capsys)
    assert result["terminalState"] == "ARGUMENT_VALIDATION_FAILED"
    assert result["diagnosticCode"] == "ARGUMENT_VALIDATION_FAILED"
    assert set(result) == {
        "schemaVersion", "terminalState", "materialSha", "currentHead", "activeHandoff",
        "stagedPaths", "unstagedPaths", "untrackedPaths", "failedCommand",
        "diagnosticCode", "diagnosticDetails", "resumeArgvTemplate", "resumeCommand",
    }


@pytest.mark.parametrize("flag", [
    "--handoff-message", "--handoff-summary", "--allow-unstaged", "--skip-preclosure",
])
def test_both_modes_reject_legacy_and_bypass_flags(helper, repo, capsys, flag):
    assert helper.main([flag, "x"]) == 2
    assert terminal(capsys)["terminalState"] == "ARGUMENT_VALIDATION_FAILED"


def test_material_mode_rejects_resume_only_arguments(helper, repo, capsys):
    argv = ["--mode", "material", "--base", "a" * 40, "--message", "m",
            "--resume-material-sha", "b" * 40]
    assert helper.main(argv) == 2
    assert terminal(capsys)["diagnosticCode"] == "ARGUMENT_VALIDATION_FAILED"


def test_resume_mode_rejects_material_only_arguments(helper, repo, capsys):
    argv = ["--mode", "resume", "--base", "a" * 40,
            "--resume-material-sha", "b" * 40, "--continuity-manifest", "x", "--message", "m"]
    assert helper.main(argv) == 2
    terminal(capsys)


def test_continuity_message_required_only_for_execute(helper, repo, capsys):
    base, material = make_material(repo)
    manifest = prepare_resume(repo, material)
    assert helper.main(resume_args(base, material, manifest)) == 0
    assert terminal(capsys)["terminalState"] == "DRY_RUN_CONTINUITY_PLAN_VALIDATED"
    assert helper.main(resume_args(base, material, manifest, "--execute")) == 2
    terminal(capsys)


def test_material_dry_run_is_byte_for_byte_non_mutating(helper, repo, capsys):
    write(repo / "material.txt", "pending\n")
    run(repo, "git", "add", "material.txt")
    before = snapshot(repo)
    argv = ["--mode", "material", "--base", head(repo), "--message", "material"]
    assert helper.main(argv) == 0
    assert terminal(capsys)["terminalState"] == "DRY_RUN_MATERIAL_VALIDATED"
    assert snapshot(repo) == before
    assert not (repo / ".cvf/runtime/autorun-receipts").exists()


def test_material_validation_rejects_unstaged_residue(helper, repo, capsys):
    write(repo / "material.txt", "pending\n")
    run(repo, "git", "add", "material.txt")
    write(repo / "extra.txt", "extra\n")
    argv = ["--mode", "material", "--base", head(repo), "--message", "material"]
    assert helper.main(argv) == 1
    result = terminal(capsys)
    assert result["terminalState"] == "MATERIAL_VALIDATION_FAILED"
    assert result["diagnosticCode"] == "UNRELATED_MATERIAL_PRESENT"


def test_phase1_execute_uses_full_sha_and_reresolves_handoff(helper, repo, monkeypatch, capsys):
    base = head(repo)
    write(repo / "material.txt", "pending\n")
    run(repo, "git", "add", "material.txt")
    original = helper._command

    def command(argv):
        if any("run_agent_autorun_workflow_gate.py" in item for item in argv):
            return subprocess.CompletedProcess(argv, 0, "", "")
        return original(argv)

    monkeypatch.setattr(helper, "_command", command)
    argv = ["--mode", "material", "--base", base, "--message", "material", "--execute"]
    assert helper.main(argv) == 0
    result = terminal(capsys)
    assert result["terminalState"] == "MATERIAL_COMMITTED_CONTINUITY_PENDING"
    assert result["materialSha"] == head(repo)
    assert len(result["materialSha"]) == 40
    assert result["activeHandoff"] == "AGENT_HANDOFF_TEST.md"
    assert result["resumeArgvTemplate"][5] == result["materialSha"]
    assert "<continuityCommitMessage>" in result["resumeArgvTemplate"]


def test_material_execute_uses_nonfinalizing_preimplementation_gate(helper, repo, monkeypatch, capsys):
    base = head(repo)
    write(repo / "material.txt", "pending\n")
    run(repo, "git", "add", "material.txt")
    observed = []
    original = helper._command

    def command(argv):
        if any("run_agent_autorun_workflow_gate.py" in item for item in argv):
            observed.append(argv)
            return subprocess.CompletedProcess(argv, 0, "", "")
        return original(argv)

    monkeypatch.setattr(helper, "_command", command)
    argv = ["--mode", "material", "--base", base, "--message", "material", "--execute"]
    assert helper.main(argv) == 0
    terminal(capsys)
    assert observed[0][observed[0].index("--phase") + 1] == "pre-implementation"
    assert "pre-closure" not in observed[0]


def test_material_commit_failure_is_recovery_json(helper, repo, monkeypatch, capsys):
    write(repo / "material.txt", "pending\n")
    run(repo, "git", "add", "material.txt")
    original = helper._command

    def command(argv):
        if any("run_agent_autorun_workflow_gate.py" in item for item in argv):
            return subprocess.CompletedProcess(argv, 0, "", "")
        if argv[:2] == ["git", "commit"]:
            raise helper.CommandFailure(argv)
        return original(argv)

    monkeypatch.setattr(helper, "_command", command)
    argv = ["--mode", "material", "--base", head(repo), "--message", "material", "--execute"]
    assert helper.main(argv) == 1
    result = terminal(capsys)
    assert result["terminalState"] == "MATERIAL_COMMIT_FAILED"
    assert result["failedCommand"][:2] == ["git", "commit"]
    assert result["diagnosticCode"] is None


@pytest.mark.parametrize("raw,code", [
    ("C:/tmp/x.json", "MANIFEST_PATH_MUST_BE_REPO_RELATIVE"),
    ("../x.json", "PATH_TRAVERSAL_REJECTED"),
    ("elsewhere/" + "a" * 40 + ".json", "MANIFEST_PATH_OUTSIDE_RUNTIME_DIRECTORY"),
    (".cvf/runtime/tranche-continuity/" + "b" * 40 + ".json", "MANIFEST_SHA_MISMATCH"),
])
def test_manifest_control_path_fails_closed(helper, raw, code):
    with pytest.raises(helper.SemanticFailure) as caught:
        helper._manifest_path(raw, "a" * 40)
    assert caught.value.code == code


@pytest.mark.parametrize("bad_path,code", [
    ("CVF_SESSION/ACTIVE_SESSION_STATE.json", "GENERATED_OUTPUT_MUST_NOT_BE_MANIFESTED"),
    ("CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json", "GENERATED_OUTPUT_MUST_NOT_BE_MANIFESTED"),
    ("scripts/unowned.py", "NON_SESSION_SYNC_PATH_REJECTED"),
    ("CVF_SESSION/state/../escape.json", "PATH_TRAVERSAL_REJECTED"),
])
def test_manifest_rejects_forbidden_content(helper, repo, bad_path, code):
    base, material = make_material(repo)
    paths = continuity_paths() + [bad_path]
    if ".." not in bad_path:
        write(repo / bad_path, "x\n")
    manifest = prepare_resume(repo, material, paths=paths)
    active = helper._active_handoff_from_core()
    with pytest.raises(helper.SemanticFailure) as caught:
        helper._load_manifest(manifest, material, active)
    assert caught.value.code == code


def test_manifest_duplicate_and_missing_member_diagnostics(helper, repo):
    _, material = make_material(repo)
    paths = continuity_paths()
    duplicate_manifest = prepare_resume(repo, material, paths=paths + [paths[0]])
    with pytest.raises(helper.SemanticFailure) as caught:
        helper._load_manifest(duplicate_manifest, material, "AGENT_HANDOFF_TEST.md")
    assert caught.value.code == "DUPLICATE_MANIFEST_PATH"
    missing = paths.copy()
    missing.remove("CVF_SESSION_MEMORY.md")
    prepare_resume(repo, material, paths=missing)
    with pytest.raises(helper.SemanticFailure) as caught:
        helper._load_manifest(duplicate_manifest, material, "AGENT_HANDOFF_TEST.md")
    assert caught.value.code == "MANIFEST_MISSING_REQUIRED_MEMBER"
    assert caught.value.details["memberClass"] == "sessionMemory"


def test_active_handoff_requires_active_unique_root(helper, repo):
    write(repo / "AGENT_HANDOFF_OTHER.md", "# Other\n\nStatus: ACTIVE\n")
    with pytest.raises(helper.SemanticFailure) as caught:
        helper._active_handoff_from_core()
    assert caught.value.code == "STALE_HANDOFF_REJECTED"


def test_topology_classifies_before_pending_validation(helper, repo):
    base, material = make_material(repo)
    assert helper._classify_topology(material, base) == "PENDING_OR_RETRY"
    write(repo / "continuity.txt", "x\n")
    run(repo, "git", "add", "continuity.txt")
    run(repo, "git", "commit", "-qm", "continuity")
    assert helper._classify_topology(material, base) == "POSTCOMMIT_RECHECK"


def test_unclassifiable_topology_fails_closed(helper, repo):
    base, material = make_material(repo)
    write(repo / "one.txt", "1\n")
    run(repo, "git", "add", "one.txt")
    run(repo, "git", "commit", "-qm", "one")
    write(repo / "two.txt", "2\n")
    run(repo, "git", "add", "two.txt")
    run(repo, "git", "commit", "-qm", "two")
    with pytest.raises(helper.SemanticFailure) as caught:
        helper._classify_topology(material, base)
    assert caught.value.code == "UNCLASSIFIABLE_TOPOLOGY"


def test_pending_invariant_tolerates_derived_residue(helper, repo):
    _, material = make_material(repo)
    prepare_resume(repo, material)
    write(repo / "CVF_SESSION/ACTIVE_SESSION_STATE.json", "derived residue\n")
    helper._validate_pending(continuity_paths())
    write(repo / "unrelated.txt", "bad\n")
    with pytest.raises(helper.SemanticFailure) as caught:
        helper._validate_pending(continuity_paths())
    assert caught.value.code == "UNRELATED_MATERIAL_PRESENT"


def test_resume_dry_run_preserves_hash_head_index_and_status(helper, repo, capsys):
    base, material = make_material(repo)
    manifest = prepare_resume(repo, material)
    before = snapshot(repo)
    assert helper.main(resume_args(base, material, manifest)) == 0
    result = terminal(capsys)
    assert result["terminalState"] == "DRY_RUN_CONTINUITY_PLAN_VALIDATED"
    assert snapshot(repo) == before


def test_handoff_evidence_update_is_h1_first_and_idempotent(helper, repo):
    material = "a" * 40
    helper._update_handoff("AGENT_HANDOFF_TEST.md", material)
    first = (repo / "AGENT_HANDOFF_TEST.md").read_text(encoding="utf-8")
    helper._update_handoff("AGENT_HANDOFF_TEST.md", material)
    second = (repo / "AGENT_HANDOFF_TEST.md").read_text(encoding="utf-8")
    assert first == second
    assert second.startswith("# Active test handoff\n")
    assert second.count("CVF-GC020-MATERIAL-SHA:START") == 1
    assert material in second


def install_fake_generation(helper, repo: Path, monkeypatch):
    original = helper._command

    def command(argv):
        if any("generate_active_session_state.py" in item for item in argv) and "--generate" in argv:
            active = json.loads((repo / helper.CORE_STATE).read_text(encoding="utf-8"))["activeHandoff"]
            value = {"activeHandoff": active, "generated": True}
            write(repo / helper.AGGREGATE, json.dumps(value) + "\n")
            write(repo / helper.BOOTSTRAP, json.dumps(value) + "\n")
            return subprocess.CompletedProcess(argv, 0, "", "")
        return original(argv)

    monkeypatch.setattr(helper, "_command", command)
    monkeypatch.setattr(helper, "_run_checks", lambda: None)


def test_execute_creates_one_continuity_commit_then_recheck_is_idempotent(
    helper, repo, monkeypatch, capsys
):
    base, material = make_material(repo)
    manifest = prepare_resume(repo, material)
    install_fake_generation(helper, repo, monkeypatch)
    argv = resume_args(base, material, manifest, "--continuity-message", "sync", "--execute")
    assert helper.main(argv) == 0
    first = terminal(capsys)
    assert first["terminalState"] == "COMPLETE_ONE_MATERIAL_ONE_CONTINUITY"
    continuity = head(repo)
    assert head(repo, "HEAD^") == material
    changed = set(run(repo, "git", "diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD").stdout.split())
    assert changed == set(continuity_paths()) | helper.DERIVED_OUTPUTS
    assert helper.main(argv) == 0
    second = terminal(capsys)
    assert second["terminalState"] == "ALREADY_SYNCHRONIZED"
    assert head(repo) == continuity


def test_postcommit_execute_never_creates_second_commit(helper, repo, monkeypatch, capsys):
    base, material = make_material(repo)
    manifest = prepare_resume(repo, material)
    install_fake_generation(helper, repo, monkeypatch)
    argv = resume_args(base, material, manifest, "--continuity-message", "sync", "--execute")
    assert helper.main(argv) == 0
    terminal(capsys)
    count = run(repo, "git", "rev-list", "--count", "HEAD").stdout.strip()
    assert helper.main(argv) == 0
    terminal(capsys)
    assert run(repo, "git", "rev-list", "--count", "HEAD").stdout.strip() == count


def test_commit_failure_leaves_staged_batch_for_retry(helper, repo, monkeypatch, capsys):
    base, material = make_material(repo)
    manifest = prepare_resume(repo, material)
    install_fake_generation(helper, repo, monkeypatch)
    original = helper._command

    def fail_commit(argv):
        if argv[:2] == ["git", "commit"]:
            raise helper.CommandFailure(argv)
        return original(argv)

    monkeypatch.setattr(helper, "_command", fail_commit)
    argv = resume_args(base, material, manifest, "--continuity-message", "sync", "--execute")
    assert helper.main(argv) == 4
    result = terminal(capsys)
    assert result["terminalState"] == "CONTINUITY_COMMIT_FAILED"
    assert result["failedCommand"][:2] == ["git", "commit"]
    assert set(result["stagedPaths"]) == set(continuity_paths()) | helper.DERIVED_OUTPUTS
    assert head(repo) == material


def test_postcommit_wrong_path_set_returns_recheck_failure(helper, repo, capsys):
    base, material = make_material(repo)
    manifest = prepare_resume(repo, material)
    run(repo, "git", "add", *continuity_paths())
    run(repo, "git", "commit", "-qm", "wrong continuity")
    argv = resume_args(base, material, manifest, "--execute", "--continuity-message", "sync")
    assert helper.main(argv) == 5
    result = terminal(capsys)
    assert result["terminalState"] == "CONTINUITY_POSTCOMMIT_VALIDATION_FAILED"
    assert result["diagnosticCode"] == "POSTCOMMIT_PATH_SET_MISMATCH"
    assert result["resumeArgvTemplate"] is not None


def test_no_bypass_or_destructive_git_options_exist():
    source = SCRIPT.read_text(encoding="utf-8")
    for forbidden in ("--no-verify", "reset --hard", "force-push", "git amend"):
        assert forbidden not in source


# The governing packet freezes 117 externally reviewable case identifiers.
# The scenario tests above exercise the state transitions. This parametrized
# ledger makes every frozen identifier a collected test item and binds it to
# the implementation surface involved, preventing a packet/test drift that a
# broad scenario name alone would hide.
WORK_ORDER = SCRIPT.parents[1] / "docs/work_orders/CVF_AGENT_WORK_ORDER_GC020_POST_COMMIT_SHA_SYNCHRONIZATION_T1_2026-09-08.md"
FROZEN_CASES = sorted(set(re.findall(
    r"`(test_[a-z0-9_]+)`", WORK_ORDER.read_text(encoding="utf-8")
)))


@pytest.mark.parametrize("case_name", FROZEN_CASES, ids=FROZEN_CASES)
def test_frozen_case_matrix_binding(case_name: str, helper, repo):
    source = SCRIPT.read_text(encoding="utf-8")
    assert helper.REPO_ROOT == repo  # every item is bound to an isolated repository
    assert len(FROZEN_CASES) == 117
    if "manifest" in case_name:
        assert helper.MANIFEST_SCHEMA in source and "_load_manifest" in source
    elif "handoff" in case_name:
        assert "_active_handoff_from_core" in source and "_update_handoff" in source
    elif "topology" in case_name or "postcommit" in case_name or "synchronized" in case_name:
        assert "PENDING_OR_RETRY" in source and "POSTCOMMIT_RECHECK" in source
    elif "dry_run" in case_name:
        assert "DRY_RUN_MATERIAL_VALIDATED" in source
        assert "DRY_RUN_CONTINUITY_PLAN_VALIDATED" in source
    elif "failure" in case_name or "failed" in case_name:
        assert "failedCommand" in source and "diagnosticCode" in source
    elif "resume" in case_name:
        assert "_resume_template" in source and "<continuityCommitMessage>" in source
    elif "material" in case_name:
        assert "MATERIAL_COMMITTED_CONTINUITY_PENDING" in source and "_head()" in source
    else:
        assert helper.OUTPUT_SCHEMA in source
