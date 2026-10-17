"""Cooperative invocation fences around immutable owned-profile implementations."""
from __future__ import annotations

import copy
import hashlib
import json
import os
import re
import subprocess
import threading
from contextlib import contextmanager
from pathlib import Path

try:
    from . import cvf_ncr_html_owned_profile as owned
except ImportError:
    import cvf_ncr_html_owned_profile as owned

ROOT = owned.P.ROOT
SOURCES = ("scripts/cvf_ncr_html_effect_fence.py", "scripts/run_cvf_ncr_html_effect_driver.py",
           "scripts/test_cvf_ncr_html_effect_driver.py", "scripts/cvf_ncr_html_browser_fence.cjs",
           "scripts/cvf_ncr_html_browser_fence.test.cjs")
RELEASE = 'docs/reviews/evidence/ncr-html-body-heading-source-release-20261017.json'
RELEASE_SHA = 'c68427b2466c56b1a36a18017fccec352704d0c484b532c030bd29917ec3652a'
CHROME = {"path": r"C:\Users\DELL\AppData\Local\ms-playwright\chromium-1208\chrome-win64\chrome.exe",
          "sha256": "ff0c99fc5bb2301cad77930aa76e5354cf2a5fefb7efdcf3b3bc10ba0550c015"}
DOCKER = {"context": "desktop-linux", "endpoint": "npipe:////./pipe/dockerDesktopLinuxEngine",
          "image": "sha256:a0725d62d5cfa8fc47b5e30be04bc08ea714a9cdd72c259595526f691db95294",
          "os": "linux", "architecture": "amd64"}
KEYS = ("CVF_NCR_BROWSER_BINDING_PATH", "CVF_NCR_BROWSER_BINDING_SHA256")
_guard, _frames = threading.Lock(), threading.local()


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def require(ok, reason):
    if not ok:
        raise ValueError(reason)


def closed(value, keys):
    require(isinstance(value, dict) and set(value) == set(keys.split()), "closed object shape")


def hexhash(value):
    require(type(value) is str and re.fullmatch("[0-9a-f]{64}", value), "invalid digest")


def safe_path(value, *, relative=False):
    require(type(value) is str and value and "\x00" not in value, "invalid path")
    p = Path(value)
    require(".." not in p.parts and "." not in p.parts, "path traversal")
    if relative:
        require(not p.is_absolute() and "\\" not in value and ":" not in value, "repo path required")
        require(p.as_posix() == value, "noncanonical repo path")
        p = ROOT / p
    else:
        require(p.is_absolute() and str(p) == value, "canonical absolute path required")
    return p


class Disk:
    """Small synchronous IO seam; tests supply an entirely in-memory implementation."""
    def read(self, path):
        self.check(path)
        p = Path(path)
        require(p.is_file() and p.stat().st_size <= 512 * 1024 * 1024, "bounded regular file required")
        return p.read_bytes()

    def check(self, path):
        p = Path(path).absolute()
        for part in (p, *p.parents):
            owned.no_reparse(part)

    def exists(self, path):
        self.check(path)
        return Path(path).exists()

    def is_dir(self, path):
        self.check(path)
        return Path(path).is_dir()

    def write(self, path, raw):
        self.check(path)
        Path(path).write_bytes(raw)

    def exclusive(self, path, raw):
        self.check(path)
        with Path(path).open("xb") as target:
            target.write(raw)
            target.flush()

    def sources(self, release):
        return owned.P.admit_sources(release["path"], release["sha256"])

    def controls(self, receipt, cap, expected):
        return owned.P.admit_controls(receipt, cap, expected)


def reject_environment(env):
    for name in env:
        key = name.upper()
        for prefix in ("NPM_CONFIG_", "NPM_PACKAGE_CONFIG_"):
            if key.startswith(prefix):
                key = key[len(prefix):]
        require(key not in {"NODE_OPTIONS", "NODE_PATH", "PWDEBUG", "DOCKER_HOST", "DOCKER_CONTEXT", *KEYS}
                and not key.startswith("PLAYWRIGHT_"), "ambient execution override refused")


class StartLedger:
    def __init__(self, persist_attempt=lambda snapshot: None):
        self.lock, self.persist = threading.RLock(), persist_attempt
        self.work, self.cleanup, self.attempts = 0, 0, []

    def snapshot(self):
        with self.lock:
            return copy.deepcopy({"workUsed": self.work, "cleanupUsed": self.cleanup, "attempts": self.attempts})

    def charge(self, op, *, native, collector, frame):
        with self.lock:
            require(frame is getattr(_frames, "active", None) and frame is not None, "inactive spawn frame")
            require(frame["native"] is native and native.c is collector and frame["collector"] is collector,
                    "foreign native/collector")
            proto = collector.proto
            require(frame["proto"] is proto and frame["op"] is op and not frame["charged"], "foreign/reused frame")
            require(any(x is op for x in proto.ops) and op.state == owned.PR.DISPATCHED, "unregistered operation")
            require(type(op.cleanup) is bool, "invalid operation classification")
            if frame["admitted"]:
                require(collector.current_op() is op, "foreign utility operation")
            else:
                require(op.kind == "launch", "foreign direct operation")
            used, limit = (self.cleanup, 8) if op.cleanup else (self.work, 56)
            require(used < limit, "controlled root capacity exhausted")
            frame["charged"] = True
            if op.cleanup:
                self.cleanup += 1
            else:
                self.work += 1
            self.attempts.append({"seq": len(self.attempts) + 1, "opId": op.id, "kind": op.kind,
                                  "cleanup": op.cleanup, "partition": "cleanup" if op.cleanup else "work", "ordinal": used + 1})
            self.persist(self.snapshot())
        proto.check(op)


@contextmanager
def installed_fences(policy, pins, persist_attempt, *, api_factory=None, popen=None):
    require(_guard.acquire(blocking=False), "concurrent/nested invocation")
    old_protocol, old_collector, old_native = owned.PR.Protocol, owned.E.Collector, owned.Native
    ledger, io = StartLedger(persist_attempt), policy.get("io") or Disk()
    try:
        require(pins["docker"] == DOCKER and pins["chrome"] == CHROME, "identity policy drift")

        class Protocol(old_protocol):
            def grant(self, op, requested, unit=None):
                frame = getattr(_frames, "active", None)
                try:
                    wait = super().grant(op, requested, unit)
                except BaseException:
                    if frame is not None:
                        frame["op"] = None
                    raise
                if frame is not None:
                    require(not frame["admitted"] and frame["proto"] is self and frame["op"] is None,
                            "unexpected grant inside spawn")
                    frame["op"] = op
                return wait

        class Collector(old_collector):
            def command(self, kind, argv, **kwargs):
                result = super().command(kind, argv, **kwargs)
                if kind == "docker-context":
                    require(result.strip() == DOCKER["context"], "Docker context mismatch")
                elif kind == "docker-context-inspect":
                    require(result["Endpoints"]["docker"]["Host"] == DOCKER["endpoint"], "Docker endpoint mismatch")
                elif kind == "cached-image":
                    require((result["Id"], result["Os"], result["Architecture"]) ==
                            (DOCKER["image"], "linux", "amd64"), "Docker image mismatch")
                elif kind == "installed-browser-path":
                    require(result.strip() == CHROME["path"] and digest(io.read(result.strip())) == CHROME["sha256"],
                            "browser discovery mismatch")
                return result

        class Native(old_native):
            def __init__(self, collector, docker_prefix, stage, namespace, **kwargs):
                if api_factory is not None:
                    kwargs["api"] = api_factory()
                kwargs["popen"] = self._popen
                super().__init__(collector, docker_prefix, stage, namespace, **kwargs)

            def _popen(self, argv, **kwargs):
                frame = getattr(_frames, "active", None)
                ledger.charge(frame["op"] if frame else None, native=self, collector=self.c, frame=frame)
                tool = Path(argv[0]).name.lower().removesuffix(".exe")
                require(tool in pins["tools"], "unlisted executable")
                target = pins["tools"][tool]["path"]
                require(not Path(argv[0]).is_absolute() or str(Path(argv[0])) == target, "tool path mismatch")
                require(digest(io.read(target)) == pins["tools"][tool]["sha256"], "tool byte drift")
                self.c.proto.check(frame["op"])
                return (popen or subprocess.Popen)([target, *argv[1:]], **kwargs)

            def _spawn(self, argv, *, admitted=False, **kwargs):
                require(getattr(_frames, "active", None) is None, "nested spawn")
                frame = {"native": self, "collector": self.c, "proto": self.c.proto, "admitted": admitted,
                         "op": self.c.current_op() if admitted else None, "charged": False}
                _frames.active = frame
                try:
                    entry = pins["helpers"]["entry"]["path"]
                    if len(argv) > 1 and str(argv[1]) == entry:
                        require(len(argv) == 9 and argv[6] == "owned-profile" and argv[2] == pins["modules"]["path"]
                                and argv[7] == pins["helpers"]["journey"]["path"], "helper argv mismatch")
                        config = io.read(argv[8])
                        cfg = json.loads(config)
                        observation = str(self.c.custody / "browser-fence.json")
                        binding = {"schemaVersion": "cvf.ncrHtmlBrowserBinding@1", "runId": policy["invocation"]["runId"],
                                   "actor": policy["invocation"]["actor"], "cap": policy["invocation"]["cap"],
                                   "entry": pins["helpers"]["entry"], "modulesPath": argv[2], "journey": pins["helpers"]["journey"],
                                   "preload": {"path": str(ROOT / SOURCES[3]), "sha256": pins["adjunctSources"][SOURCES[3]]},
                                   "config": {"path": argv[8], "sha256": digest(config)}, "profilePath": cfg["browserProfile"],
                                   "observationPath": observation, "chrome": pins["chrome"]}
                        require(cfg["cap"] == binding["cap"] and cfg["inputs"] == policy["inputs"], "helper config mismatch")
                        raw, location = canonical(binding), str(self.c.custody / "browser-binding.json")
                        io.write(location, raw)
                        env = dict(kwargs["env"])
                        require(env.get("NODE_OPTIONS") == owned.P.node_preload_options(argv[7]), "existing preload mismatch")
                        env["NODE_OPTIONS"] = owned.P.node_preload_options(argv[7], binding["preload"]["path"])
                        env.update({KEYS[0]: location, KEYS[1]: digest(raw)})
                        kwargs["env"] = env
                        policy["binding"] = binding
                    return super()._spawn(argv, admitted=admitted, **kwargs)
                finally:
                    _frames.active = None

        owned.PR.Protocol, owned.E.Collector, owned.Native = Protocol, Collector, Native
        yield ledger
    finally:
        owned.PR.Protocol, owned.E.Collector, owned.Native = old_protocol, old_collector, old_native
        _guard.release()
