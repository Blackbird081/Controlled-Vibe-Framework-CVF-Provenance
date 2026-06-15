from pathlib import Path

import governance.compat.run_agent_commit_steward_preflight as steward


def test_protected_session_path_classification() -> None:
    assert steward._is_protected_session_path("CVF_SESSION_MEMORY.md")
    assert steward._is_protected_session_path("CVF_SESSION/ACTIVE_SESSION_STATE.json")
    assert steward._is_protected_session_path("AGENT_HANDOFF_V18_2026-06-12.md")
    assert not steward._is_protected_session_path("docs/reference/example.md")


def test_agent_operation_trace_detection(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setattr(steward, "REPO_ROOT", tmp_path)
    traced = tmp_path / "docs" / "reviews" / "trace.md"
    traced.parent.mkdir(parents=True)
    traced.write_text(
        "# Trace\n\n## Agent Operation Trace Block\n\n| Actual changed set | x |\n",
        encoding="utf-8",
    )
    plain = tmp_path / "docs" / "reviews" / "plain.md"
    plain.write_text("# Plain\n", encoding="utf-8")

    assert steward._has_agent_operation_trace("docs/reviews/trace.md")
    assert not steward._has_agent_operation_trace("docs/reviews/plain.md")


def test_path_plan_collision_risk(monkeypatch) -> None:
    monkeypatch.setattr(
        steward,
        "_range_paths",
        lambda base, head: (
            "docs/work_orders/example.md",
            "AGENT_HANDOFF_V18_2026-06-12.md",
        ),
    )
    monkeypatch.setattr(steward, "_status_paths", lambda: ())
    monkeypatch.setattr(
        steward,
        "_has_agent_operation_trace",
        lambda path: path == "docs/work_orders/example.md",
    )

    plan = steward.build_path_plan("base", "head")

    assert plan.mixed_material_and_session
    assert plan.exact_manifest_collision_risk
    assert plan.material_paths == ("docs/work_orders/example.md",)
    assert plan.protected_session_paths == ("AGENT_HANDOFF_V18_2026-06-12.md",)


def test_status_paths_handles_trimmed_git_status(monkeypatch) -> None:
    monkeypatch.setattr(
        steward,
        "_git_output",
        lambda *args, **kwargs: "M AGENTS.md\n?? docs/reference/new.md\n",
    )

    assert steward._status_paths() == (
        "AGENTS.md",
        "docs/reference/new.md",
    )
