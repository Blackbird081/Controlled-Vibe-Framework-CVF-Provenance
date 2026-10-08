#!/usr/bin/env python3
"""CVF video preparation preflight: inspect and validate only.

Reads an explicit manifest and an explicit owned resource root, then emits a
deterministic JSON readiness report. It never installs, downloads, infers,
renders, starts a process, opens a socket or writes anything except the optional
exclusive report file. runtimeAdmission is always NO_GO: a complete manifest is
structural evidence for review, not runtime admission or OS containment.
Standard library only; no VieNeu, HyperFrames or provider client is imported.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import stat
import sys
import unicodedata

MANIFEST_SCHEMA = "cvf.videoPreparationManifest@1"
REPORT_SCHEMA = "cvf.videoPreflightReport@1"
MAX_MANIFEST_BYTES = 4 * 1024 * 1024
MAX_DESIGN_BYTES = 1024 * 1024
MAX_ARTIFACT_BYTES = 16 * 1024 ** 3
MAX_ARTIFACTS = 2048
HASH_CHUNK = 1 << 20
FRESHNESS = "DATED_HISTORICAL_NOT_CURRENT_UPSTREAM"
CEILING_STATUS = "PROPOSED_NOT_ENFORCED"
CLASS_ORDER = {"INVALID": 0, "INCOMPLETE": 1, "STANDING_NO_GO": 2}

_V = ("pnnbao97/VieNeu-TTS", "85344322b7258b4e25479b692e8e3396baf9db34")
_H = ("heygen-com/hyperframes", "5c52f72399e21f8dcf3ede2bf2d24978c6522a94")
# Frozen Git-blob pins from docs/reviews/evidence/cvf-ncr-video-production-preparation-inputs-2026-10-08.json.
# (component, pin, path, sha256, bytes)
ACCEPTED_SOURCE_PINS = (
    ("vieneu", _V[1], "pyproject.toml", "b36fc3303dceff0dddbe9f49067d0c82f3c11802e0dd82a2b58208f375d8df63", 5991),
    ("vieneu", _V[1], "uv.lock", "0921052a578f63d82305eb4a19be2579751edfb579eab0c9d65d977652481e2e", 998772),
    ("vieneu", _V[1], "LICENSE", "c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4", 11357),
    ("vieneu", _V[1], "src/vieneu/_v3_turbo_engine/onnx_runtime_lite.py",
     "7747ac18fb5b660a810a434461bd8386ba40b0b46d559c07907db0c19414084e", 32607),
    ("vieneu", _V[1], "src/vieneu/v3turbo.py", "10757905d3f6454e17c834ec32c73d33b5b9d322d05397295c0bbeb5f3ffb3ad", 38604),
    ("hyperframes", _H[1], "packages/cli/package.json",
     "cb61f0ce2902e34791583d6eb5c80e70f6910e8663c1dc3f802c6409bbaef7b2", 2467),
    ("hyperframes", _H[1], "packages/engine/package.json",
     "5d3aa6d8381c547fa93ddd57ca201857e62c54ed6e69771fb9a460cb8f508be7", 2361),
    ("hyperframes", _H[1], "bun.lock", "5993fbbfd6a3affcc0e07f8789711fb69ddb36e7bf8cf716f9383c87b10b067e", 264395),
    ("hyperframes", _H[1], "LICENSE", "4259155fb06f127687ee7b0a8a3682d45132db0f2da26cbc0b7a2d1e796436b8", 10763),
)
LOCK_PIN_PATHS = {"vieneu": "uv.lock", "hyperframes": "bun.lock"}
# Accepted S05 identity from the composition readiness design evidence (s05TextIdentity).
S05_ACCEPTED = {
    "designRawSha256": "3ce5e2363c3e29997fcbf42cb4cec59af7447cca38409d4d970e8aa71e5777e0",
    "narrationSha256": "f6c1cd46a00b535e07dc634bcb53d75dc80ed521a58432de8c5b449cf4017fb8",
    "onScreenSha256": "0846e61c1a38e8468152a6df998e58b07e143a91f5d8d821ffb5c1ba77c2eede",
    "statusCardSha256": "ec3a424cb9b37d3ba630771347c60547b95275ce50900ab73bd8bb17463d3c25",
}
S05_CLAIMS = ["C09", "C10"]
S05_ESTIMATE_SECONDS = 20
S05_PAD_LIMIT_SECONDS = 19.5  # TOL-05
RETIMING = ("NONE_NOT_MEASURED", "NONE_PAD_WITHIN_SCENE", "PROPOSED_RETIMING_PENDING_APPROVAL", "APPROVED_RETIMING")
CORE_DISTRIBUTIONS = ("vieneu", "sea-g2p", "onnxruntime", "numpy", "soundfile", "soxr", "kaldi-native-fbank",
                      "tokenizers", "huggingface-hub", "pyyaml", "gradio", "librosa")
# File sets named by the pinned onnx_runtime_lite.py:42-51 constants.
FILE_SETS = {
    "model_graph": ("vieneu_prefill.onnx", "vieneu_decode_step.onnx", "vieneu_acoustic_cached.onnx",
                    "vieneu_backbone_shared.data", "vieneu_v3_heads.npz"),
    "model_config": ("config.json",),
    "tokenizer": ("tokenizer.json",),
    "codec": ("moss_audio_tokenizer_decode_full.onnx", "moss_audio_tokenizer_decode_shared.data",
              "moss_audio_tokenizer_decode_step.onnx", "codec_browser_onnx_meta.json",
              "moss_audio_tokenizer_encode.onnx", "moss_audio_tokenizer_encode.data"),
    "preset": ("voices_v3_turbo.json",),
}
REQUIRED_CATEGORIES = ("python_wheel", "source_lock", "model_graph", "model_config", "tokenizer", "codec",
                       "phonemizer", "preset", "browser", "ffmpeg", "font", "rights_attribution",
                       "enforcement_evidence")
CATEGORIES = set(REQUIRED_CATEGORIES) | {"denoiser"}
RIGHTS_SCOPE = {"python_wheel": "SOURCE_CODE", "source_lock": "SOURCE_CODE", "phonemizer": "SOURCE_CODE",
                "model_graph": "WEIGHTS", "model_config": "WEIGHTS", "tokenizer": "WEIGHTS", "denoiser": "WEIGHTS",
                "codec": "CODEC", "preset": "VOICE", "font": "FONT", "browser": "BINARY", "ffmpeg": "BINARY"}
PLACEMENTS = ("CACHE", "FINAL", "DUPLICATE")
ORIGIN_KINDS = ("git_blob", "hf_revision", "pypi_file", "npm_file", "vendor_binary", "operator_supplied")
REVISION_KINDS = ("git_blob", "hf_revision")
CODEC_RESOLUTIONS = ("ENGINE_DIRECT_CODEC_DIR", "HF_CACHE_PREPOPULATED_OFFLINE")  # public V3Turbo constructor cannot forward codec_dir
PRESET_SOURCES = ("PACKAGED_BUILTIN_ASSET", "MODEL_ROOT_OVERRIDE_FILE")
ENFORCEMENT_CONTROLS = ("egress_block", "filesystem_quota", "memory_cap", "process_cap", "walltime_cap")
CEILINGS = {  # key -> (unit, integer required)
    "download_install_cache_bytes": ("bytes", True), "final_artifact_bytes": ("bytes", True),
    "duplicated_storage_bytes": ("bytes", True), "log_evidence_bytes": ("bytes", True),
    "aggregate_disk_bytes": ("bytes", True), "peak_committed_ram_bytes": ("bytes", True),
    "process_count": ("count", True), "walltime_seconds": ("seconds", False),
    "cancellation_grace_seconds": ("seconds", False), "retries": ("attempts_per_stage", True),
}
SHARED_CACHE_PARTS = {".cache", ".huggingface", "huggingface", ".npm", "_cacache", "puppeteer", ".nuget"}
STANDING_NO_GO = (
    ("RUNTIME_ADMISSION_NOT_GRANTABLE_BY_VALIDATOR", "a complete manifest is never runtime admission"),
    ("OS_CONTAINMENT_NOT_ESTABLISHED_BY_VALIDATOR", "egress, disk, RAM, process and time controls are metadata only"),
    ("RIGHTS_ASSERTIONS_UNREVIEWED_BY_VALIDATOR", "cleared dispositions are manifest claims awaiting Local review"),
    ("OFFLINE_OPERATION_NOT_PROVEN", "no execution-time network absence was observed"),
    ("WHEEL_CLOSURE_COMPLETENESS_NOT_PROVEN_BY_VALIDATOR", "transitive closure needs review against the pinned uv.lock"),
    ("FONT_VIETNAMESE_GLYPH_COVERAGE_NOT_VERIFIED_BY_VALIDATOR", "glyph coverage needs a rendered check"),
    ("OPERATOR_RUNTIME_ENVELOPE_NOT_ADMITTED", "ceilings are PROPOSED_NOT_ENFORCED until the operator admits an envelope"),
    ("C1_STOP_RETAINED", "stopped C1 metadata and source-relay identities are not reset by this preflight"),
)
SHA_RE = re.compile(r"^[0-9a-f]{64}$")
REV_RE = re.compile(r"^[0-9a-f]{40}$")
ID_RE = re.compile(r"^[A-Za-z0-9_.:-]{1,80}$")
WHEEL_RE = re.compile(r"^[A-Za-z0-9_.]+-[A-Za-z0-9_.!+]+(-\d[A-Za-z0-9_.]*)?-[A-Za-z0-9_.]+-[A-Za-z0-9_.]+-([A-Za-z0-9_.]+)\.whl$")


class Findings:
    def __init__(self):
        self.rows = []

    def add(self, code, cls, subject, detail=""):
        self.rows.append({"code": code, "class": cls, "subject": str(subject), "detail": str(detail)})

    def invalid(self, code, subject, detail=""):
        self.add(code, "INVALID", subject, detail)

    def incomplete(self, code, subject, detail=""):
        self.add(code, "INCOMPLETE", subject, detail)


def _reject_constant(name):
    raise ValueError("non-finite JSON constant " + name)


def _no_dup_keys(pairs):
    out = {}
    for k, v in pairs:
        if k in out:
            raise ValueError("duplicate JSON key " + k)
        out[k] = v
    return out


def read_bounded(path, limit):
    st = os.lstat(path)
    if is_link_like(st) or not stat.S_ISREG(st.st_mode):
        raise ValueError("not a regular non-link file")
    if st.st_size > limit:
        raise ValueError("file exceeds bound %d" % limit)
    with open(path, "rb") as fh:
        data = fh.read(limit + 1)
    if len(data) > limit:
        raise ValueError("file exceeds bound %d" % limit)
    return data


def load_manifest(path):
    data = read_bounded(path, MAX_MANIFEST_BYTES)
    manifest = json.loads(data.decode("utf-8"), parse_constant=_reject_constant, object_pairs_hook=_no_dup_keys)
    if not isinstance(manifest, dict):
        raise ValueError("manifest root must be an object")
    return manifest


def is_link_like(st):
    return stat.S_ISLNK(st.st_mode) or bool(getattr(st, "st_file_attributes", 0) & 0x400)


def check_rel_path(value):
    """Return a rejection reason for an unsafe manifest path, or None."""
    if not isinstance(value, str) or not value:
        return "path must be a non-empty string"
    if "\x00" in value or "\\" in value or ":" in value:
        return "path contains NUL, backslash or colon"
    if value.startswith("/") or value.startswith("//"):
        return "absolute path"
    parts = value.split("/")
    if any(p in ("", ".", "..") for p in parts):
        return "empty, dot or traversal component"
    if any(p != p.rstrip(" .") for p in parts):
        return "component ends with space or dot"
    return None


def locate(root, rel):
    cur = root
    parts = rel.split("/")
    st = None
    for idx, part in enumerate(parts):
        cur = os.path.join(cur, part)
        try:
            st = os.lstat(cur)
        except FileNotFoundError:
            return "MISSING", None
        except OSError:
            return "UNREADABLE", None
        if is_link_like(st):
            return "LINK", None
        if idx < len(parts) - 1 and not stat.S_ISDIR(st.st_mode):
            return "NOT_DIR", None
    return "OK", (cur, st)


def hash_stream(path, limit):
    digest, total = hashlib.sha256(), 0
    with open(path, "rb") as fh:
        while True:
            chunk = fh.read(HASH_CHUNK)
            if not chunk:
                break
            total += len(chunk)
            if total > limit:
                raise ValueError("file grew beyond bound")
            digest.update(chunk)
    return digest.hexdigest(), total


def _is_int(v):
    return isinstance(v, int) and not isinstance(v, bool)


def _finite_number(value):
    try:
        return math.isfinite(value)
    except (TypeError, OverflowError):
        return False


def _valid_origin(origin):
    if not isinstance(origin, dict) or origin.get("kind") not in ORIGIN_KINDS:
        return False
    if not isinstance(origin.get("identity"), str) or not origin["identity"].strip() or origin.get("immutable") is not True:
        return False
    return origin["kind"] not in REVISION_KINDS or bool(REV_RE.match(str(origin.get("revision", ""))))


def check_root(root, f):
    try:
        st = os.lstat(root)
    except OSError:
        f.invalid("ROOT_UNREADABLE", "root", "owned root does not exist")
        return False
    if is_link_like(st) or not stat.S_ISDIR(st.st_mode):
        f.invalid("ROOT_NOT_PLAIN_DIRECTORY", "root", "owned root must be a plain directory, not a link")
        return False
    parts = {p.casefold() for p in os.path.abspath(root).replace("\\", "/").split("/")}
    if parts & SHARED_CACHE_PARTS:
        f.invalid("ROOT_IS_SHARED_CACHE", "root", "owned root sits inside a shared cache or user-data location")
        return False
    return True


def validate_artifact(root, i, a, f, state):
    if not isinstance(a, dict):
        f.invalid("ARTIFACT_MALFORMED", "artifacts[%d]" % i, "entry is not an object")
        return None
    aid = a.get("id")
    if not isinstance(aid, str) or not ID_RE.match(aid):
        f.invalid("ARTIFACT_ID_INVALID", "artifacts[%d]" % i)
        return None
    if aid in state["ids"]:
        f.invalid("DUPLICATE_ARTIFACT_ID", aid)
        return None
    state["ids"][aid] = a
    row = {"id": aid, "category": a.get("category"), "placement": a.get("placement"), "path": a.get("path"),
           "declaredBytes": a.get("bytes"), "measuredBytes": None, "hashVerified": False}
    ok = True
    if a.get("category") not in CATEGORIES:
        f.invalid("ARTIFACT_CATEGORY_UNKNOWN", aid, str(a.get("category")))
        ok = False
    if a.get("placement") not in PLACEMENTS:
        f.invalid("ARTIFACT_PLACEMENT_INVALID", aid, str(a.get("placement")))
        ok = False
    if not isinstance(a.get("sha256"), str) or not SHA_RE.match(a["sha256"]):
        f.invalid("HASH_MALFORMED", aid, "sha256 must be 64 lowercase hex")
        ok = False
    if not _is_int(a.get("bytes")) or a["bytes"] < 0:
        f.invalid("BYTES_MALFORMED", aid, "bytes must be a non-negative integer")
        ok = False
    if not _valid_origin(a.get("origin")):
        f.invalid("ORIGIN_NOT_IMMUTABLE", aid, "origin needs kind, identity, immutable=true and a 40-hex revision for git/hf")
        ok = False
    reason = check_rel_path(a.get("path"))
    if reason:
        f.invalid("PATH_REJECTED", aid, reason)
        return row
    key = unicodedata.normalize("NFC", a["path"]).casefold()
    if key in state["targets"]:
        f.invalid("DUPLICATE_TARGET", aid, "same canonical target as " + state["targets"][key])
        return row
    state["targets"][key] = aid
    status, found = locate(root, a["path"])
    if status == "MISSING":
        f.incomplete("ARTIFACT_MISSING", aid, a["path"])
        return row
    if status != "OK":
        f.invalid("LINK_OR_UNSAFE_PATH_REJECTED" if status == "LINK" else "PATH_UNREADABLE", aid, status)
        return row
    abspath, st = found
    if not stat.S_ISREG(st.st_mode):
        f.invalid("NOT_REGULAR_FILE", aid)
        return row
    row["measuredBytes"] = st.st_size
    if st.st_size > MAX_ARTIFACT_BYTES:
        f.invalid("SIZE_OVER_BOUND", aid, "measured %d bytes" % st.st_size)
        return row
    if ok and st.st_size != a["bytes"]:
        f.invalid("SIZE_MISMATCH", aid, "declared %d measured %d" % (a["bytes"], st.st_size))
        return row
    if ok:
        try:
            digest, total = hash_stream(abspath, MAX_ARTIFACT_BYTES)
        except (OSError, ValueError) as exc:
            f.invalid("HASH_UNREADABLE", aid, str(exc))
            return row
        if digest != a["sha256"] or total != a["bytes"]:
            f.invalid("HASH_MISMATCH", aid, "declared sha256 differs from measured bytes")
        else:
            row["hashVerified"] = True
    return row


def validate_rights(state, f):
    ids = state["ids"]
    for aid, a in ids.items():
        cat, rights = a.get("category"), a.get("rights")
        if cat == "rights_attribution":
            scopes = a.get("rightsScopes")
            if not isinstance(scopes, list) or not scopes or not all(isinstance(s, str) for s in scopes):
                f.invalid("RIGHTS_SCOPES_MALFORMED", aid, "rights evidence needs rightsScopes")
            continue
        if cat not in RIGHTS_SCOPE:
            continue
        disp = rights.get("disposition") if isinstance(rights, dict) else None
        if disp is None or disp == "UNKNOWN":
            f.incomplete("RIGHTS_UNKNOWN", aid, "no rights disposition" if disp is None else "disposition UNKNOWN")
        elif disp == "PUBLISHER_DECLARED_UNVERIFIED":
            f.incomplete("RIGHTS_NOT_CLEARED", aid, "publisher declaration is not independent clearance")
        elif disp == "CLEARED_PINNED_EVIDENCE":
            ev = ids.get(rights.get("evidenceArtifactId"))
            if not ev or ev.get("category") != "rights_attribution":
                f.invalid("RIGHTS_EVIDENCE_UNRESOLVED", aid, "evidenceArtifactId must name a rights_attribution artifact")
            elif RIGHTS_SCOPE[cat] not in (ev.get("rightsScopes") or []):
                f.incomplete("RIGHTS_SCOPE_INSUFFICIENT", aid, "evidence lacks scope " + RIGHTS_SCOPE[cat])
        else:
            f.invalid("RIGHTS_DISPOSITION_INVALID", aid, str(disp))


def validate_inventory(state, f):
    by_cat = {}
    for aid, a in state["ids"].items():
        by_cat.setdefault(a.get("category"), []).append(a)
    for cat in REQUIRED_CATEGORIES:
        if not by_cat.get(cat):
            f.incomplete("CATEGORY_MISSING", cat, "mandatory category has no artifact")
    for cat, names in FILE_SETS.items():
        have = {os.path.basename(str(a.get("path"))).casefold() for a in by_cat.get(cat, [])}
        missing = sorted(n for n in names if n.casefold() not in have)
        if missing and by_cat.get(cat):
            f.incomplete("PRESET_MISSING" if cat == "preset" else "CODEC_MISSING" if cat == "codec" else
                         "SOURCE_FILE_SET_INCOMPLETE", cat, ",".join(missing))
    dists = set()
    for a in by_cat.get("python_wheel", []):
        m = WHEEL_RE.match(os.path.basename(str(a.get("path"))))
        if not m:
            f.invalid("WHEEL_FILENAME_INVALID", a["id"], "python_wheel must be a .whl file")
        elif m.group(2) not in ("win_amd64", "any"):
            f.invalid("WHEEL_PLATFORM_MISMATCH", a["id"], "platform tag " + m.group(2))
        dists.add(re.sub(r"[-_.]+", "-", str(a.get("distribution", ""))).lower())
    missing = sorted(d for d in CORE_DISTRIBUTIONS if d not in dists)
    if missing and by_cat.get("python_wheel"):
        f.incomplete("PYTHON_CLOSURE_INCOMPLETE", "python_wheel", ",".join(missing))
    return by_cat


def validate_pins(manifest, pins, by_cat, f):
    listed = manifest.get("sourcePins")
    if not isinstance(listed, list):
        f.incomplete("SOURCE_PIN_MISSING", "sourcePins", "manifest has no sourcePins list")
        listed = []
    seen = {}
    for entry in listed:
        if isinstance(entry, dict):
            seen[(entry.get("component"), entry.get("path"))] = entry
    for comp, pin, path, sha, size in pins:
        entry = seen.get((comp, path))
        if entry is None:
            f.incomplete("SOURCE_PIN_MISSING", "%s:%s" % (comp, path))
        elif (entry.get("pin"), entry.get("sha256"), entry.get("bytes")) != (pin, sha, size) or entry.get("freshness") != FRESHNESS:
            f.invalid("SOURCE_PIN_DRIFT", "%s:%s" % (comp, path), "pin, sha256, bytes or freshness label differs from frozen input")
    locks = {(a.get("sha256"), a.get("bytes")) for a in by_cat.get("source_lock", [])}
    for comp, pin, path, sha, size in pins:
        if path == LOCK_PIN_PATHS[comp] and by_cat.get("source_lock") and (sha, size) not in locks:
            f.invalid("SOURCE_LOCK_DRIFT", "%s:%s" % (comp, path), "no source_lock artifact matches the pinned blob")


def validate_ceilings(manifest, rows, f):
    ceilings, summary = manifest.get("ceilings"), {}
    if not isinstance(ceilings, dict):
        f.incomplete("CEILINGS_MISSING", "ceilings", "all proposed ceilings are mandatory")
        ceilings = {}
    for key, (unit, integer) in CEILINGS.items():
        c = ceilings.get(key)
        if not isinstance(c, dict):
            f.incomplete("CEILING_MISSING", key)
            continue
        v = c.get("value")
        if isinstance(v, bool) or not isinstance(v, (int, float)) or not _finite_number(v) or v <= 0 or (integer and not _is_int(v)):
            f.invalid("CEILING_INVALID", key, "value must be a positive finite %s" % ("integer" if integer else "number"))
            continue
        if c.get("unit") != unit:
            f.invalid("CEILING_UNIT_INVALID", key, "expected " + unit)
        if c.get("status") != CEILING_STATUS:
            f.invalid("CEILING_ENFORCEMENT_CLAIM_REJECTED", key, "status must be exactly " + CEILING_STATUS)
        summary[key] = v
    sums = {p: sum(r["measuredBytes"] or 0 for r in rows if r["placement"] == p) for p in PLACEMENTS}
    log_ceiling = summary.get("log_evidence_bytes", 0)
    projected = sum(sums.values()) + log_ceiling
    for place, key in (("CACHE", "download_install_cache_bytes"), ("FINAL", "final_artifact_bytes"),
                       ("DUPLICATE", "duplicated_storage_bytes")):
        if key in summary and sums[place] > summary[key]:
            f.invalid("CEILING_EXCEEDED", key, "measured %d exceeds proposed %s" % (sums[place], summary[key]))
    if "aggregate_disk_bytes" in summary and projected > summary["aggregate_disk_bytes"]:
        f.invalid("AGGREGATE_DISK_OVERFLOW", "aggregate_disk_bytes", "projected %d exceeds %s" % (projected, summary["aggregate_disk_bytes"]))
    if "walltime_seconds" in summary and summary.get("cancellation_grace_seconds", 0) >= summary["walltime_seconds"]:
        f.invalid("CEILING_INCONSISTENT", "cancellation_grace_seconds", "grace must be below walltime")
    return {"measuredBytesByPlacement": sums, "logEvidenceCeilingBytes": log_ceiling, "projectedAggregateDiskBytes": projected,
            "proposedCeilings": {k: summary[k] for k in sorted(summary)}, "ceilingStatus": CEILING_STATUS}


def validate_enforcement(manifest, ids, f):
    enforcement = manifest.get("enforcement")
    enforcement = enforcement if isinstance(enforcement, dict) else {}
    for control in ENFORCEMENT_CONTROLS:
        entry = enforcement.get(control)
        ev = ids.get(entry.get("evidenceArtifactId")) if isinstance(entry, dict) else None
        if not ev or ev.get("category") != "enforcement_evidence":
            f.incomplete("ENFORCEMENT_EVIDENCE_MISSING", control, "no enforcement_evidence artifact joined")


def validate_voice(manifest, ids, f):
    voice = manifest.get("voice")
    if not isinstance(voice, dict):
        f.incomplete("VOICE_IDENTITY_MISSING", "voice")
        return
    fixed = (("backend", "onnx"), ("device", "cpu"), ("precision", "fp32"), ("cloning", False), ("paidOrHostedVoice", False))
    for key, want in fixed:
        if voice.get(key) != want or type(voice.get(key)) is not type(want):
            f.invalid("LANE_SUBSTITUTION_REJECTED", key, "C1 requires %s=%r" % (key, want))
    preset = ids.get(voice.get("presetArtifactId"))
    if not voice.get("presetId") or not preset or preset.get("category") != "preset":
        f.incomplete("PRESET_MISSING", "voice.presetArtifactId", "fixed preset must name a verified preset artifact")
    if voice.get("presetSource") not in PRESET_SOURCES:
        f.incomplete("PRESET_SOURCE_MISSING", "voice.presetSource", "name the preset file actually loaded: " + ",".join(PRESET_SOURCES))
    codec = voice.get("codec")
    res = codec.get("resolution") if isinstance(codec, dict) else None
    if res in CODEC_RESOLUTIONS:
        if not (isinstance(codec.get("decisionRef"), str) and codec["decisionRef"].strip()):
            f.incomplete("CODEC_DISPOSITION_MISSING", "voice.codec", "resolution needs an operator decisionRef")
    elif res in (None, "OPERATOR_DISPOSITION_PENDING"):
        f.incomplete("CODEC_DISPOSITION_MISSING", "voice.codec", "no codec resolution path has been dispositioned")
    else:
        f.invalid("CODEC_DISPOSITION_INVALID", "voice.codec", str(res))
    consent = ids.get(voice.get("consentArtifactId"))
    if not consent or consent.get("category") != "rights_attribution" or "VOICE" not in (consent.get("rightsScopes") or []):
        f.incomplete("VOICE_CONSENT_MISSING", "voice.consentArtifactId", "fixed preset needs VOICE-scoped consent evidence")
    den = voice.get("denoiser")
    disp = den.get("disposition") if isinstance(den, dict) else None
    if disp == "PRESENT_ARTIFACT":
        if (ids.get(den.get("artifactId")) or {}).get("category") != "denoiser":
            f.incomplete("DENOISER_DISPOSITION_MISSING", "voice.denoiser", "PRESENT_ARTIFACT needs a denoiser artifact")
    elif disp == "ABSENT_ACCEPTED_PRESET_ONLY":
        if not isinstance(den.get("decisionRef"), str) or not den["decisionRef"].strip():
            f.incomplete("DENOISER_DISPOSITION_MISSING", "voice.denoiser", "absence needs a decisionRef")
    else:
        f.incomplete("DENOISER_DISPOSITION_MISSING", "voice.denoiser", "disposition must be PRESENT_ARTIFACT or ABSENT_ACCEPTED_PRESET_ONLY")


def extract_s05(design_bytes):
    text = design_bytes.decode("utf-8").replace("\r\n", "\n")
    m = re.search(r"^### S05 \|[^\n]*\n(.*?)(?=^### |^## )", text, re.S | re.M)
    if not m:
        raise ValueError("S05 section not found")

    def value(label):
        hit = re.search(r"^- " + label + r": (.*)$", m.group(1), re.M)
        if not hit:
            raise ValueError("S05 label missing: " + label)
        return hit.group(1)

    narration, on_screen, claims = value("Narration"), value("On-screen"), value("Claims")
    card = on_screen.split(". ")[0]
    segments = on_screen.split(". ")[1:]

    def ident(s):
        return {"sha256": hashlib.sha256(s.encode("utf-8")).hexdigest(), "utf8Bytes": len(s.encode("utf-8")),
                "nfc": unicodedata.is_normalized("NFC", s)}
    return {"designRawSha256": hashlib.sha256(design_bytes).hexdigest(), "narration": ident(narration),
            "onScreen": ident(on_screen), "statusCard": ident(card), "statusCardText": card,
            "claimIds": [c.strip() for c in claims.split(",")], "segments": [ident(s) for s in segments]}


def validate_s05(manifest, design_path, f):
    s05 = manifest.get("s05")
    if design_path is None:
        f.incomplete("S05_SOURCE_NOT_PROVIDED", "s05", "pass --design with the accepted storyboard path")
        return None
    try:
        got = extract_s05(read_bounded(design_path, MAX_DESIGN_BYTES))
    except (OSError, ValueError) as exc:
        f.invalid("S05_SOURCE_UNREADABLE", "s05", str(exc))
        return None
    for key, acc in (("designRawSha256", got["designRawSha256"]), ("narrationSha256", got["narration"]["sha256"]),
                     ("onScreenSha256", got["onScreen"]["sha256"]), ("statusCardSha256", got["statusCard"]["sha256"])):
        if acc != S05_ACCEPTED[key]:
            f.invalid("S05_SOURCE_DRIFT", key, "accepted design bytes differ from the frozen identity")
    if got["claimIds"] != S05_CLAIMS or not (got["narration"]["nfc"] and got["onScreen"]["nfc"]):
        f.invalid("S05_SOURCE_DRIFT", "claims/nfc", "claim IDs or NFC property differ from the frozen identity")
    if not isinstance(s05, dict):
        f.incomplete("S05_BINDING_MISSING", "s05")
        return got
    for key in ("designRawSha256", "narrationSha256", "onScreenSha256", "statusCardSha256"):
        if s05.get(key) != S05_ACCEPTED[key]:
            f.invalid("S05_MANIFEST_DRIFT", key, "manifest binding differs from accepted bytes")
    if s05.get("claimIds") != S05_CLAIMS:
        f.invalid("S05_CLAIMS_MISMATCH", "claimIds", "expected C09 and C10")
    est, meas, ret = s05.get("originalEstimateSeconds"), s05.get("measuredNarrationSeconds"), s05.get("retiming")
    if est != S05_ESTIMATE_SECONDS or isinstance(est, bool):
        f.invalid("S05_ESTIMATE_ALTERED", "originalEstimateSeconds", "the 20 second planning estimate stays distinct")
    if meas is not None and (isinstance(meas, bool) or not isinstance(meas, (int, float)) or not _finite_number(meas) or meas <= 0):
        f.invalid("S05_MEASUREMENT_INVALID", "measuredNarrationSeconds")
        meas = None
    disp = ret.get("disposition") if isinstance(ret, dict) else None
    if disp not in RETIMING:
        f.invalid("RETIMING_DISPOSITION_INVALID", "retiming", str(disp))
    elif meas is not None and meas > S05_PAD_LIMIT_SECONDS and disp.startswith("NONE"):
        f.invalid("RETIMING_DISPOSITION_REQUIRED", "retiming", "measured narration exceeds the pad limit")
    elif disp == "APPROVED_RETIMING" and not (isinstance(ret.get("approvalRef"), str) and ret["approvalRef"].strip()):
        f.invalid("RETIMING_APPROVAL_UNBOUND", "retiming", "approved retiming needs approvalRef")
    elif disp == "PROPOSED_RETIMING_PENDING_APPROVAL":
        f.incomplete("RETIMING_APPROVAL_PENDING", "retiming", "operator disposition required")
    frames = s05.get("plannedFrames")
    if not isinstance(frames, list) or not frames:
        f.incomplete("S05_FRAMES_MISSING", "plannedFrames")
        return got
    for i, fr in enumerate(frames):
        good = (isinstance(fr, dict) and fr.get("statusCardText") == got["statusCardText"]
                and fr.get("statusCardSha256") == S05_ACCEPTED["statusCardSha256"] and fr.get("claimIds") == S05_CLAIMS)
        if not good:
            f.invalid("S05_FRAME_STATUS_CARD_MISSING", "plannedFrames[%d]" % i, "each frame needs the full status card and claims C09,C10")
    return got


def run_preflight(manifest_path, root, design_path=None, pins=None):
    pins = ACCEPTED_SOURCE_PINS if pins is None else pins
    f, report = Findings(), {"schema": REPORT_SCHEMA, "mode": "INSPECT_VALIDATE_ONLY", "runtimeAdmission": "NO_GO",
                             "osContainment": "NOT_ESTABLISHED", "pinFreshness": FRESHNESS,
                             "effectsInvoked": "NONE_BY_DESIGN", "artifacts": [], "resourceArithmetic": None}
    try:
        manifest = load_manifest(manifest_path)
    except (OSError, ValueError, UnicodeDecodeError) as exc:
        f.invalid("MANIFEST_MALFORMED", "manifest", str(exc))
        manifest = None
    if manifest is not None and manifest.get("schemaVersion") != MANIFEST_SCHEMA:
        f.invalid("MANIFEST_SCHEMA_UNSUPPORTED", "schemaVersion", str(manifest.get("schemaVersion")))
        manifest = None
    if manifest is not None and check_root(root, f):
        arts = manifest.get("artifacts")
        state = {"ids": {}, "targets": {}}
        if not isinstance(arts, list) or not arts or len(arts) > MAX_ARTIFACTS:
            f.invalid("ARTIFACTS_MALFORMED", "artifacts", "expected 1..%d entries" % MAX_ARTIFACTS)
            arts = []
        try:
            rows = [r for r in (validate_artifact(os.path.abspath(root), i, a, f, state) for i, a in enumerate(arts)) if r]
            validate_rights(state, f)
            by_cat = validate_inventory(state, f)
            validate_pins(manifest, pins, by_cat, f)
            report["resourceArithmetic"] = validate_ceilings(manifest, rows, f)
            validate_enforcement(manifest, state["ids"], f)
            validate_voice(manifest, state["ids"], f)
            got = validate_s05(manifest, design_path, f)
            report["artifacts"] = sorted(rows, key=lambda r: r["id"])
            if got:
                report["s05Extraction"] = {"recipe": "design bytes UTF-8, CRLF->LF, S05 section, value after '- <Label>: ', UTF-8, no newline",
                                           "designRawSha256": got["designRawSha256"], "narrationSha256": got["narration"]["sha256"],
                                           "onScreenSha256": got["onScreen"]["sha256"], "statusCardSha256": got["statusCard"]["sha256"]}
        except (TypeError, OverflowError, RecursionError) as exc:
            # JSON values of incompatible shape cannot escape the NO_GO report.
            # Keep only the exception class, never a raw manifest/request body.
            f.invalid("MANIFEST_SHAPE_INVALID", "manifest", type(exc).__name__)
    for code, detail in STANDING_NO_GO:
        f.add(code, "STANDING_NO_GO", "runtime", detail)
    matrix = sorted(f.rows, key=lambda r: (CLASS_ORDER[r["class"]], r["code"], r["subject"], r["detail"]))
    classes = {r["class"] for r in matrix}
    status = ("INVALID_NO_GO" if "INVALID" in classes else "INCOMPLETE_NO_GO" if "INCOMPLETE" in classes
              else "STRUCTURALLY_COMPLETE_NO_GO")
    report.update({"validationStatus": status, "reasonCodes": sorted({r["code"] for r in matrix}), "noGoMatrix": matrix})
    return report


def canonical(report):
    return json.dumps(report, sort_keys=True, indent=2, ensure_ascii=True) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description="CVF video preparation preflight (inspect/validate only)")
    ap.add_argument("--manifest")
    ap.add_argument("--root", help="explicit owned resource root")
    ap.add_argument("--design", help="accepted storyboard path for the S05 digest check")
    ap.add_argument("--report", help="optional new report file (created exclusively)")
    ap.add_argument("--extract-s05", action="store_true", help="print S05 identity from --design and exit")
    args = ap.parse_args(argv)
    if args.extract_s05:
        if not args.design:
            ap.error("--extract-s05 needs --design")
        got = extract_s05(read_bounded(args.design, MAX_DESIGN_BYTES))
        sys.stdout.write(canonical(got))
        return 0
    if not args.manifest or not args.root:
        ap.error("--manifest and --root are required")
    report = run_preflight(args.manifest, args.root, args.design)
    text = canonical(report)
    if args.report:
        target = os.path.abspath(args.report)
        if os.path.normcase(target).startswith(os.path.normcase(os.path.abspath(args.root)) + os.sep):
            ap.error("--report must not be written inside the owned root")
        with open(target, "x", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
    else:
        sys.stdout.write(text)
    return 0 if report["validationStatus"] == "STRUCTURALLY_COMPLETE_NO_GO" else 1


if __name__ == "__main__":
    sys.exit(main())
