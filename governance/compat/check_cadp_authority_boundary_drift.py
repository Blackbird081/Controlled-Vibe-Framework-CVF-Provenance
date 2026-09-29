#!/usr/bin/env python3
"""
CADP-AI-T4 authority boundary drift checker.

Hermetic, read-only, dependency-free static checker. It validates a strict
JSON fixture describing the accepted CADP T1/T3A/T3B authority-boundary
surfaces, then lexically inspects the fixture-named contract and package-root
files for contract-version drift, authorization-field widening, forbidden
execution seams, and package-export drift.

Claim boundary: this checker performs bounded comment/string-tolerant lexical
matching, not TypeScript AST parsing or compiler-equivalent semantic
verification. A PASS shows only that the named source literals and
export-block text match the strict fixture under the implemented checks; it
does not prove full TypeScript semantics, runtime enforcement, or provider
safety. This checker performs no writes, no TypeScript import/execution, no
network call, no subprocess call, and no credential or provider access.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_FIXTURE = REPO_ROOT / "governance" / "compat" / "fixtures" / "cadp_authority_boundary_contract.v1.json"
CHECKER_PATH = "governance/compat/check_cadp_authority_boundary_drift.py"
SCHEMA_VERSION = "cadp-authority-boundary-contract.v1"

VIOLATION_CODES = (
    "FIXTURE_SCHEMA_INVALID",
    "SURFACE_MISSING",
    "CONTRACT_VERSION_DRIFT",
    "AUTHORITY_TYPE_WIDENED",
    "AUTHORITY_VALUE_WIDENED",
    "FORBIDDEN_EXECUTION_SEAM",
    "PACKAGE_EXPORT_DRIFT",
)

_SURFACE_REQUIRED_KEYS = {
    "surfaceId",
    "contractPath",
    "packageRootPath",
    "versionSymbol",
    "versionValue",
    "falseAuthorityFields",
    "requiredExportSymbols",
    "requiredExportModule",
    "forbiddenSeamTokens",
}

_STRING_LIST_KEYS = ("falseAuthorityFields", "requiredExportSymbols", "forbiddenSeamTokens")


class Violation:
    __slots__ = ("code", "surface_id", "path", "message")

    def __init__(self, code: str, surface_id: str, path: str, message: str) -> None:
        self.code = code
        self.surface_id = surface_id
        self.path = path
        self.message = message

    def to_dict(self) -> dict[str, str]:
        return {
            "code": self.code,
            "surfaceId": self.surface_id,
            "path": self.path,
            "message": self.message,
        }

    def sort_key(self) -> tuple[str, str, str, str]:
        return (self.code, self.surface_id, self.path, self.message)


def _is_safe_repo_relative_path(value: Any) -> bool:
    if not isinstance(value, str) or not value.strip():
        return False
    normalized = value.replace("\\", "/")
    if normalized.startswith("/") or normalized.startswith("~"):
        return False
    if re.match(r"^[A-Za-z]:", normalized):
        return False
    parts = normalized.split("/")
    if any(part == ".." for part in parts):
        return False
    if any(part == "" for part in parts):
        return False
    return True


def _validate_surface_schema(raw: Any, index: int, violations: list[Violation]) -> dict[str, Any] | None:
    prefix = f"$.surfaces[{index}]"
    if not isinstance(raw, dict):
        violations.append(Violation("FIXTURE_SCHEMA_INVALID", "UNKNOWN", prefix, "Surface entry must be a JSON object."))
        return None

    keys = set(raw.keys())
    unknown = keys - _SURFACE_REQUIRED_KEYS
    missing = _SURFACE_REQUIRED_KEYS - keys
    surface_id = raw.get("surfaceId") if isinstance(raw.get("surfaceId"), str) else "UNKNOWN"

    if unknown:
        violations.append(Violation(
            "FIXTURE_SCHEMA_INVALID", surface_id, prefix,
            f"Surface has unknown key(s): {sorted(unknown)}.",
        ))
    if missing:
        violations.append(Violation(
            "FIXTURE_SCHEMA_INVALID", surface_id, prefix,
            f"Surface is missing required key(s): {sorted(missing)}.",
        ))
    if unknown or missing:
        return None

    ok = True
    if not isinstance(raw["surfaceId"], str) or not raw["surfaceId"].strip():
        violations.append(Violation("FIXTURE_SCHEMA_INVALID", surface_id, f"{prefix}.surfaceId", "surfaceId must be a non-empty string."))
        ok = False
    if not _is_safe_repo_relative_path(raw["contractPath"]):
        violations.append(Violation("FIXTURE_SCHEMA_INVALID", surface_id, f"{prefix}.contractPath", "contractPath must be a safe repo-relative path."))
        ok = False
    if raw["packageRootPath"] is not None and not _is_safe_repo_relative_path(raw["packageRootPath"]):
        violations.append(Violation("FIXTURE_SCHEMA_INVALID", surface_id, f"{prefix}.packageRootPath", "packageRootPath must be null or a safe repo-relative path."))
        ok = False
    if not isinstance(raw["versionSymbol"], str) or not raw["versionSymbol"].strip():
        violations.append(Violation("FIXTURE_SCHEMA_INVALID", surface_id, f"{prefix}.versionSymbol", "versionSymbol must be a non-empty string."))
        ok = False
    if not isinstance(raw["versionValue"], str) or not raw["versionValue"].strip():
        violations.append(Violation("FIXTURE_SCHEMA_INVALID", surface_id, f"{prefix}.versionValue", "versionValue must be a non-empty string."))
        ok = False

    for key in _STRING_LIST_KEYS:
        value = raw[key]
        if not isinstance(value, list) or any(not isinstance(item, str) or not item.strip() for item in value):
            violations.append(Violation("FIXTURE_SCHEMA_INVALID", surface_id, f"{prefix}.{key}", f"{key} must be a list of non-empty strings."))
            ok = False
            continue
        if len(set(value)) != len(value):
            violations.append(Violation("FIXTURE_SCHEMA_INVALID", surface_id, f"{prefix}.{key}", f"{key} must not contain duplicate entries."))
            ok = False

    if key_empty_required(raw, "falseAuthorityFields"):
        violations.append(Violation("FIXTURE_SCHEMA_INVALID", surface_id, f"{prefix}.falseAuthorityFields", "falseAuthorityFields must not be empty."))
        ok = False
    if key_empty_required(raw, "forbiddenSeamTokens"):
        violations.append(Violation("FIXTURE_SCHEMA_INVALID", surface_id, f"{prefix}.forbiddenSeamTokens", "forbiddenSeamTokens must not be empty."))
        ok = False

    if raw["requiredExportModule"] is not None and (not isinstance(raw["requiredExportModule"], str) or not raw["requiredExportModule"].strip()):
        violations.append(Violation("FIXTURE_SCHEMA_INVALID", surface_id, f"{prefix}.requiredExportModule", "requiredExportModule must be null or a non-empty string."))
        ok = False
    if (raw["packageRootPath"] is None) != (raw["requiredExportModule"] is None):
        violations.append(Violation(
            "FIXTURE_SCHEMA_INVALID", surface_id, f"{prefix}.requiredExportModule",
            "packageRootPath and requiredExportModule must both be null or both be set.",
        ))
        ok = False
    if raw["packageRootPath"] is None and raw["requiredExportSymbols"]:
        violations.append(Violation(
            "FIXTURE_SCHEMA_INVALID", surface_id, f"{prefix}.requiredExportSymbols",
            "requiredExportSymbols must be empty when packageRootPath is null.",
        ))
        ok = False
    if raw["packageRootPath"] is not None and not raw["requiredExportSymbols"]:
        violations.append(Violation(
            "FIXTURE_SCHEMA_INVALID", surface_id, f"{prefix}.requiredExportSymbols",
            "requiredExportSymbols must not be empty when packageRootPath is set.",
        ))
        ok = False

    return raw if ok else None


def key_empty_required(raw: dict[str, Any], key: str) -> bool:
    value = raw.get(key)
    return isinstance(value, list) and len(value) == 0


def load_fixture(fixture_path: Path) -> tuple[dict[str, Any] | None, list[Violation]]:
    violations: list[Violation] = []
    try:
        text = fixture_path.read_text(encoding="utf-8")
    except OSError as exc:
        violations.append(Violation("FIXTURE_SCHEMA_INVALID", "UNKNOWN", str(fixture_path), f"Fixture could not be read: {exc}."))
        return None, violations

    try:
        raw = json.loads(text)
    except json.JSONDecodeError as exc:
        violations.append(Violation("FIXTURE_SCHEMA_INVALID", "UNKNOWN", str(fixture_path), f"Fixture is not valid JSON: {exc}."))
        return None, violations

    if not isinstance(raw, dict):
        violations.append(Violation("FIXTURE_SCHEMA_INVALID", "UNKNOWN", "$", "Fixture root must be a JSON object."))
        return None, violations

    top_keys = set(raw.keys())
    expected_top_keys = {"schemaVersion", "surfaces"}
    if top_keys != expected_top_keys:
        unknown = top_keys - expected_top_keys
        missing = expected_top_keys - top_keys
        detail = []
        if unknown:
            detail.append(f"unknown key(s) {sorted(unknown)}")
        if missing:
            detail.append(f"missing key(s) {sorted(missing)}")
        violations.append(Violation("FIXTURE_SCHEMA_INVALID", "UNKNOWN", "$", f"Fixture root has {'; '.join(detail)}."))
        return None, violations

    if raw.get("schemaVersion") != SCHEMA_VERSION:
        violations.append(Violation(
            "FIXTURE_SCHEMA_INVALID", "UNKNOWN", "$.schemaVersion",
            f"Fixture schemaVersion must be exactly {SCHEMA_VERSION!r}.",
        ))
        return None, violations

    surfaces_raw = raw.get("surfaces")
    if not isinstance(surfaces_raw, list) or len(surfaces_raw) == 0:
        violations.append(Violation("FIXTURE_SCHEMA_INVALID", "UNKNOWN", "$.surfaces", "Fixture surfaces must be a non-empty list."))
        return None, violations

    validated_surfaces: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    seen_contract_paths: set[str] = set()
    seen_version_symbols: set[str] = set()
    schema_ok = True

    for index, raw_surface in enumerate(surfaces_raw):
        validated = _validate_surface_schema(raw_surface, index, violations)
        if validated is None:
            schema_ok = False
            continue
        surface_id = validated["surfaceId"]
        contract_path = validated["contractPath"].replace("\\", "/")
        version_symbol = validated["versionSymbol"]
        if surface_id in seen_ids:
            violations.append(Violation("FIXTURE_SCHEMA_INVALID", surface_id, f"$.surfaces[{index}].surfaceId", f"Duplicate surfaceId: {surface_id}."))
            schema_ok = False
            continue
        # contractPath ownership must stay unique per surface: two surfaces
        # cannot share the same authority-owned contract-source file.
        # packageRootPath is a discoverability reference, not an ownership
        # claim, so distinct surfaces may cite the same shared package-root
        # file; each surface's own export block is still checked
        # independently by check_surface's module-qualified export lookup.
        if contract_path in seen_contract_paths:
            violations.append(Violation("FIXTURE_SCHEMA_INVALID", surface_id, f"$.surfaces[{index}].contractPath", f"Duplicate contractPath: {contract_path}."))
            schema_ok = False
            continue
        if version_symbol in seen_version_symbols:
            violations.append(Violation("FIXTURE_SCHEMA_INVALID", surface_id, f"$.surfaces[{index}].versionSymbol", f"Duplicate versionSymbol: {version_symbol}."))
            schema_ok = False
            continue
        seen_ids.add(surface_id)
        seen_contract_paths.add(contract_path)
        seen_version_symbols.add(version_symbol)
        validated_surfaces.append(validated)

    if not schema_ok:
        return None, violations

    return {"schemaVersion": raw["schemaVersion"], "surfaces": validated_surfaces}, violations


def _read_text(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None


def _lexical_mask(source: str, *, mask_strings: bool) -> str:
    """Mask comments and optionally string/template bodies while preserving offsets.

    This is a bounded TypeScript lexical pass, not a parser. Keeping offsets
    stable lets structured regex matches be required to start in code rather
    than in a comment or decoy string. Template expressions are conservatively
    masked with the template body; they cannot satisfy authority invariants.
    """
    chars = list(source)
    out = list(source)
    index = 0
    state = "code"
    quote = ""
    while index < len(chars):
        char = chars[index]
        nxt = chars[index + 1] if index + 1 < len(chars) else ""
        if state == "code":
            if char == "/" and nxt == "/":
                out[index] = out[index + 1] = " "
                index += 2
                state = "line_comment"
                continue
            if char == "/" and nxt == "*":
                out[index] = out[index + 1] = " "
                index += 2
                state = "block_comment"
                continue
            if char in ("'", '"', "`"):
                quote = char
                if mask_strings:
                    out[index] = " "
                index += 1
                state = "string"
                continue
            index += 1
            continue
        if state == "line_comment":
            if char == "\n":
                state = "code"
            else:
                out[index] = " "
            index += 1
            continue
        if state == "block_comment":
            if char == "*" and nxt == "/":
                out[index] = out[index + 1] = " "
                index += 2
                state = "code"
            else:
                if char != "\n":
                    out[index] = " "
                index += 1
            continue
        if state == "string":
            if mask_strings and char != "\n":
                out[index] = " "
            if char == "\\":
                if index + 1 < len(chars):
                    if mask_strings and chars[index + 1] != "\n":
                        out[index + 1] = " "
                    index += 2
                else:
                    index += 1
                continue
            if char == quote:
                state = "code"
            index += 1
    return "".join(out)


def _strip_comments(source: str) -> str:
    return _lexical_mask(source, mask_strings=False)


def _code_only(source: str) -> str:
    return _lexical_mask(source, mask_strings=True)


def _find_export_block(source: str, module_specifier: str) -> str | None:
    """Return the text of an `export ... from "<module_specifier>";` block, if present."""
    escaped_module = re.escape(module_specifier)
    pattern = re.compile(
        r"export\s+(?:type\s+)?\{(?P<body>[^}]*)\}\s*from\s*[\"']" + escaped_module + r"[\"']",
        re.DOTALL,
    )
    code = _code_only(source)
    matches = [match for match in pattern.finditer(source) if code[match.start():match.start() + 6] == "export"]
    if not matches:
        return None
    return "\n".join(match.group("body") for match in matches)


def _symbol_present_in_block(block: str, symbol: str) -> bool:
    pattern = re.compile(r"(?<![A-Za-z0-9_$])" + re.escape(symbol) + r"(?![A-Za-z0-9_$])")
    return pattern.search(block) is not None


def _version_declared(source: str, symbol: str, value: str) -> bool:
    pattern = re.compile(
        r"export\s+const\s+" + re.escape(symbol) + r"(?![A-Za-z0-9_$])\s*=\s*[\"']"
        + re.escape(value) + r"[\"']\s+as\s+const\b",
    )
    code = _code_only(source)
    return any(code[match.start():match.start() + 6] == "export" for match in pattern.finditer(source))


def _type_position_declared_false(source: str, field_name: str) -> bool:
    """True if `readonly <field>: false;`-shaped interface/type member is present.

    The `readonly` keyword immediately before the field name is this
    repository's literal marker for a type-position (interface/type member)
    declaration, distinct from an object-literal value assignment of the same
    field, which never carries a preceding `readonly`.
    """
    pattern = re.compile(
        r"readonly\s+" + re.escape(field_name) + r"(?![A-Za-z0-9_$])\s*:\s*false\b",
    )
    return bool(pattern.search(_code_only(source)))


def _type_position_widened(source: str, field_name: str) -> bool:
    """True if the type-position declaration widens to a non-false type."""
    pattern = re.compile(
        r"readonly\s+" + re.escape(field_name) + r"(?![A-Za-z0-9_$])\s*:\s*(boolean|true)\b",
    )
    return bool(pattern.search(_code_only(source)))


def _value_position_declared_false(source: str, field_name: str) -> bool:
    """True if the field's false-output enforcement is present in either of the
    two literal shapes this repository's CADP contracts use:

      - a non-readonly object-literal value assignment `<field>: false`
        (e.g. inside a returned `data: {...}` or `Object.freeze({...})`); or
      - a `requireExactFalse(<owner>, '<field>', ...)` runtime-validator
        invocation, which is this codebase's enforcement idiom for
        caller-input fields that are never re-emitted as an output literal.

    Either shape independently satisfies the value-position requirement; a
    field with neither shape present has no output enforcement at all.
    """
    code = _code_only(source)
    literal_pattern = re.compile(
        r"(?<![A-Za-z0-9_$])" + re.escape(field_name) + r"(?![A-Za-z0-9_$])\s*:\s*false\b",
    )
    for match in literal_pattern.finditer(code):
        prefix = source[max(0, match.start() - 9):match.start()]
        if prefix.rstrip().endswith("readonly"):
            continue
        return True
    validator_pattern = re.compile(
        r"requireExactFalse\s*\([^)]*?[\"']" + re.escape(field_name) + r"[\"']",
        re.DOTALL,
    )
    return any(code[match.start():match.start() + len("requireExactFalse")].strip() == "requireExactFalse" for match in validator_pattern.finditer(source))


def _value_position_widened(source: str, field_name: str) -> bool:
    """True if any non-readonly value assignment is not the literal `false`."""
    code = _code_only(source)
    pattern = re.compile(
        r"(?<![A-Za-z0-9_$])" + re.escape(field_name)
        + r"(?![A-Za-z0-9_$])\s*:\s*(?P<value>[^,;}\n]+)",
    )
    for match in pattern.finditer(code):
        prefix = code[max(0, match.start() - 9):match.start()]
        if prefix.rstrip().endswith("readonly"):
            continue
        if match.group("value").strip() != "false":
            return True
    return False


def _forbidden_seam_present(source: str, seam_token: str) -> bool:
    code = _code_only(source)
    if seam_token in code:
        return True
    # Module specifiers are string literals by syntax, so recognize them only
    # when attached to an import/require construct whose start is real code.
    module_pattern = re.compile(
        r"(?:\bfrom\s*|\bimport\s*(?:\(|(?=[\"']))|\brequire\s*\()"
        r"[\"'][^\"']*" + re.escape(seam_token) + r"[^\"']*[\"']",
    )
    for match in module_pattern.finditer(_strip_comments(source)):
        start_text = match.group(0).lstrip()
        keyword = "from" if start_text.startswith("from") else ("import" if start_text.startswith("import") else "require")
        offset = match.start() + len(match.group(0)) - len(start_text)
        if code[offset:offset + len(keyword)] == keyword:
            return True
    return False


def _computed_property_assignment_present(source: str) -> bool:
    """Reject computed object/type properties in an authority-owned contract.

    A dynamic key cannot be proven distinct from a protected authority field
    by this bounded lexical checker. Exact quoted and template keys are also
    rejected so they cannot bypass the direct `<field>: false` invariant.
    """
    comments_removed = _strip_comments(source)
    code = _code_only(source)
    pattern = re.compile(r"\[[^\]\n]+\]\s*:\s*[^,;}\n]+")
    return any(code[match.start()] == "[" for match in pattern.finditer(comments_removed))


def check_surface(surface: dict[str, Any], repo_root: Path) -> list[Violation]:
    violations: list[Violation] = []
    surface_id = surface["surfaceId"]
    contract_path = surface["contractPath"]
    contract_file = repo_root / contract_path

    if not contract_file.is_file():
        violations.append(Violation("SURFACE_MISSING", surface_id, contract_path, "Fixture-owned contract path does not exist."))
        return violations

    raw_source = _read_text(contract_file)
    if raw_source is None:
        violations.append(Violation("SURFACE_MISSING", surface_id, contract_path, "Fixture-owned contract path could not be read."))
        return violations

    source = _strip_comments(raw_source)

    if not _version_declared(source, surface["versionSymbol"], surface["versionValue"]):
        violations.append(Violation(
            "CONTRACT_VERSION_DRIFT", surface_id, contract_path,
            f"Version symbol {surface['versionSymbol']!r} with value {surface['versionValue']!r} was not found.",
        ))

    for field_name in surface["falseAuthorityFields"]:
        type_declared_false = _type_position_declared_false(source, field_name)
        type_widened = _type_position_widened(source, field_name)
        if type_widened or not type_declared_false:
            violations.append(Violation(
                "AUTHORITY_TYPE_WIDENED", surface_id, contract_path,
                f"Authorization field {field_name!r} is not declared as a literal false type.",
            ))
        value_declared_false = _value_position_declared_false(source, field_name)
        value_widened = _value_position_widened(source, field_name)
        if value_widened or not value_declared_false:
            violations.append(Violation(
                "AUTHORITY_VALUE_WIDENED", surface_id, contract_path,
                f"Authorization field {field_name!r} output assignment is missing or not literal false.",
            ))

    if _computed_property_assignment_present(raw_source):
        violations.append(Violation(
            "AUTHORITY_VALUE_WIDENED", surface_id, contract_path,
            "Computed property assignment prevents proof that authority fields remain literal false.",
        ))

    for seam_token in surface["forbiddenSeamTokens"]:
        if _forbidden_seam_present(raw_source, seam_token):
            violations.append(Violation(
                "FORBIDDEN_EXECUTION_SEAM", surface_id, contract_path,
                f"Forbidden execution seam token found in owned contract: {seam_token!r}.",
            ))

    package_root_path = surface["packageRootPath"]
    if package_root_path is not None:
        package_root_file = repo_root / package_root_path
        if not package_root_file.is_file():
            violations.append(Violation("SURFACE_MISSING", surface_id, package_root_path, "Fixture-owned package-root path does not exist."))
        else:
            package_raw_source = _read_text(package_root_file)
            if package_raw_source is None:
                violations.append(Violation("SURFACE_MISSING", surface_id, package_root_path, "Fixture-owned package-root path could not be read."))
            else:
                package_source = _strip_comments(package_raw_source)
                block = _find_export_block(package_source, surface["requiredExportModule"])
                if block is None:
                    violations.append(Violation(
                        "PACKAGE_EXPORT_DRIFT", surface_id, package_root_path,
                        f"No export block found for module {surface['requiredExportModule']!r}.",
                    ))
                else:
                    for symbol in surface["requiredExportSymbols"]:
                        if not _symbol_present_in_block(block, symbol):
                            violations.append(Violation(
                                "PACKAGE_EXPORT_DRIFT", surface_id, package_root_path,
                                f"Required export symbol {symbol!r} is not present in the {surface['requiredExportModule']!r} export block.",
                            ))

    return violations


def run_checks(repo_root: Path, fixture_path: Path) -> tuple[dict[str, Any], list[Violation]]:
    fixture, fixture_violations = load_fixture(fixture_path)
    all_violations: list[Violation] = list(fixture_violations)
    checked_surface_count = 0

    if fixture is not None:
        checked_surface_count = len(fixture["surfaces"])
        for surface in fixture["surfaces"]:
            all_violations.extend(check_surface(surface, repo_root))

    all_violations.sort(key=lambda v: v.sort_key())

    report = {
        "checkerPath": CHECKER_PATH,
        "schemaVersion": SCHEMA_VERSION,
        "checkedSurfaceCount": checked_surface_count,
        "violationCount": len(all_violations),
        "violations": [v.to_dict() for v in all_violations],
        "claimBoundary": (
            "Bounded comment/string-tolerant lexical static check only; not a "
            "TypeScript compiler or AST-equivalence proof, and not a runtime, "
            "provider, or production-readiness claim."
        ),
    }
    return report, all_violations


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="CADP-AI-T4 authority boundary drift checker.")
    parser.add_argument("--json", action="store_true", help="Emit the report as JSON to stdout.")
    parser.add_argument("--enforce", action="store_true", help="Exit nonzero if any violation is found.")
    parser.add_argument("--repo-root", type=Path, default=REPO_ROOT, help="Override repository root (for hermetic tests).")
    parser.add_argument("--fixture", type=Path, default=None, help="Override fixture path (for hermetic tests).")
    args = parser.parse_args(argv)

    repo_root = args.repo_root.resolve()
    fixture_path = (args.fixture if args.fixture is not None else (repo_root / "governance" / "compat" / "fixtures" / "cadp_authority_boundary_contract.v1.json")).resolve()

    report, violations = run_checks(repo_root, fixture_path)

    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print(f"CADP authority boundary drift checker: {report['checkedSurfaceCount']} surface(s) checked, {report['violationCount']} violation(s).")
        for violation in violations:
            print(f"  [{violation.code}] {violation.surface_id} {violation.path}: {violation.message}")

    if args.enforce and violations:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
