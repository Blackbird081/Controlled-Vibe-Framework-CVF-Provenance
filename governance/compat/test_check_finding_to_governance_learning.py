import importlib.util
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().with_name("check_finding_to_governance_learning.py")
SPEC = importlib.util.spec_from_file_location("check_finding_to_governance_learning", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


VALID_DOC = """
# Review

## Quality Findings

| Finding | Evidence |
|---|---|
| Missing guard | log |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
|---|---|---|---|---|
| Missing guard | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | Add guard |
"""


def _messages(issues: list[dict[str, str]]) -> list[str]:
    return [issue["message"] for issue in issues]


def test_valid_finding_doc_passes() -> None:
    assert MODULE._validate_finding_doc("docs/logs/CVF_TEST.md", VALID_DOC) == []


def test_finding_doc_without_disposition_fails() -> None:
    invalid = VALID_DOC.split("## Finding-To-Governance Learning Disposition")[0]
    issues = MODULE._validate_finding_doc("docs/reviews/CVF_TEST.md", invalid)
    assert any("Finding-To-Governance" in message for message in _messages(issues))


def test_runtime_finding_requires_runtime_lane() -> None:
    invalid = VALID_DOC.replace("GOVERNANCE_CONTROL_PLANE", "DOCUMENTATION_ONLY_LEARNING")
    invalid = invalid.replace("Missing guard", "Runtime provider timeout")
    issues = MODULE._validate_finding_doc("docs/logs/CVF_TEST.md", invalid)
    assert any("runtime/provider/cost" in message for message in _messages(issues))


def test_doc_only_runtime_boundary_allows_explicit_na() -> None:
    valid = """
# Review

## Findings

Runtime modification is explicitly out of scope.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next action |
|---|---|---|---|---|
| Runtime/provider/cost learning | RUNTIME_SIGNAL_GAP | DOCUMENTATION_ONLY_LEARNING | N/A_WITH_REASON - doc-only; no runtime signal | N/A |
"""
    assert MODULE._validate_finding_doc("docs/reviews/CVF_TEST.md", valid) == []


def test_binding_check_requires_autorun_reference() -> None:
    issues = MODULE._validate_binding(MODULE.AUTORUN_PATH, "no guard here")
    assert any(MODULE.THIS_SCRIPT_PATH in message for message in _messages(issues))
