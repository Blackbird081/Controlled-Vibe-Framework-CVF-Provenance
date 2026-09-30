#!/usr/bin/env python3
"""Q001 SQLite target-publication correction probe: disposable synthetic data only.

Measures staged-verify-then-no-clobber publication for import, backup and restore. Faults use the
owner's private seam (restored afterwards) or a real child process that exits at a barrier. Every
state is read with a raw sqlite3/hashlib oracle on a byte copy; the owner reader is not the oracle.
Never edits the owner and never touches the current ledger, providers or the network.
"""
import argparse, gc, hashlib, json, os, shutil, sqlite3, subprocess, sys, time, uuid
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
ENGINE_DIR = REPO_ROOT / "EXTENSIONS" / "CVF_v1.6.1_GOVERNANCE_ENGINE" / "ai_governance_core"
OWNER_FILE = ENGINE_DIR / "ledger_layer" / "sqlite_ledger.py"
PEER = ENGINE_DIR / "tests" / "q001_sqlite_ledger_peer.py"
RUNTIME = REPO_ROOT / ".cvf" / "runtime"
DEFAULT_OUT = REPO_ROOT / "docs" / "reviews" / "evidence" / "cvf-ncr-q001-sqlite-target-publication-worker-2026-09-30.json"
sys.path.insert(0, str(ENGINE_DIR))
from ledger_layer import sqlite_ledger as SL  # noqa: E402
from ledger_layer.block_builder import BlockBuilder  # noqa: E402

SCHEMA_ID = "cvf.ncr.q001.sqliteTargetPublication.workerObservation@1"
N, PAD, MID_INSERT = 12, 4000, 7
SIDECARS = ("-wal", "-shm", "-journal")
FILES = ("source.json", "live.sqlite", "backup.sqlite", "final.sqlite")
COMPETITOR = b"COMPETING-CREATOR-SYNTHETIC"


class Injected(RuntimeError):
    pass


def sha(data):
    return hashlib.sha256(data).hexdigest()


def synthetic_chain(count):
    builder, chain, prior = BlockBuilder(), [], "GENESIS"
    for i in range(count):
        block = builder.build_block(prior, {"request_id": f"r{i:02d}", "artifact_id": "synthetic"})
        chain.append(block)
        prior = block["hash"]
    return chain


class Root:
    """New disposable root under ignored .cvf/runtime; only this exact path is ever removed."""

    def __enter__(self):
        RUNTIME.mkdir(parents=True, exist_ok=True)
        if subprocess.run(["git", "check-ignore", "-q", ".cvf/runtime/x"], cwd=REPO_ROOT).returncode != 0:
            raise RuntimeError("runtime area is not git-ignored")
        self.path = (RUNTIME / f"q001-sqlite-publication-{uuid.uuid4().hex[:10]}").resolve()
        if self.path.parent != RUNTIME.resolve():
            raise RuntimeError("disposable root escaped runtime")
        self.path.mkdir()
        self.n, self.cleanup = 0, {"outcome": "NOT_RUN"}
        return self

    def case_dir(self, name):
        self.n += 1
        d = self.path / f"{name}-{self.n:02d}"
        d.mkdir()
        return d

    def redact(self, text):
        for raw, label in ((str(self.path), "<ROOT>"), (self.path.as_posix(), "<ROOT>"),
                           (str(REPO_ROOT), "<REPO>"), (REPO_ROOT.as_posix(), "<REPO>")):
            text = text.replace(raw, label)
        return text[:240]

    def __exit__(self, *exc):
        gc.collect()
        try:
            shutil.rmtree(self.path)
            self.cleanup = {"outcome": "REMOVED_EXACT_ROOT"}
        except OSError as err:
            self.cleanup = {"outcome": "RESIDUE", "error": type(err).__name__}


# ------------------------------------------------------------------ raw oracle
def raw_classify(path, expected_ids=None, scratch=None):
    """Independent read-only classification on a byte copy using sqlite3 + hashlib only."""
    path = str(path)
    side = [s for s in SIDECARS if os.path.lexists(path + s)]
    out = {"state": None, "sidecars": side, "count": None, "ids": None, "tip": None, "safeToRetry": False}
    if not os.path.lexists(path):
        out["state"] = "SIDECAR_ONLY" if side else "CLEAN_ABSENT"
        return out
    tmp = Path(scratch or Path(path).parent) / f"oracle-{uuid.uuid4().hex[:8]}"
    tmp.mkdir()
    try:
        copy = tmp / "c.sqlite"
        shutil.copyfile(path, copy)
        for s in side:
            shutil.copyfile(path + s, str(copy) + s)
        try:
            conn = sqlite3.connect(copy)
            try:
                if not conn.execute("SELECT count(*) FROM sqlite_master").fetchone()[0]:
                    out["state"] = "PARTIAL_OPENABLE_INCOMPLETE"
                    return out
                rows = conn.execute("SELECT ordinal, request_id, block_json, block_hash FROM blocks ORDER BY ordinal").fetchall()
            finally:
                conn.close()
        except sqlite3.DatabaseError:
            out["state"] = "PARTIAL_UNOPENABLE"
            return out
        prior, ids, ok = "GENESIS", [], True
        for want, (ordinal, rid, raw, bhash) in enumerate(rows, 1):
            block = json.loads(raw)
            body = {k: block[k] for k in ("timestamp", "previous_hash", "event")}
            digest = hashlib.sha256(json.dumps(body, sort_keys=True).encode()).hexdigest()
            ok &= ordinal == want and block["event"]["request_id"] == rid and block["previous_hash"] == prior
            ok &= digest == bhash == block["hash"]
            prior = bhash
            ids.append(rid)
        out.update(count=len(rows), ids=ids, tip=prior)
        if not ok:
            out["state"] = "PARTIAL_OPENABLE_INCOMPLETE"
        elif expected_ids is None:
            out["state"] = "UNKNOWN_PREEXISTING_ORIGIN"
        else:
            out["state"] = "USABLE_COMPLETE" if ids == expected_ids else "PARTIAL_OPENABLE_INCOMPLETE"
        return out
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def file_state(path):
    path = str(path)
    if not os.path.lexists(path):
        return {"exists": False}
    data = Path(path).read_bytes()
    return {"exists": True, "size": len(data), "sha256": sha(data)}


def dir_state(d, root):
    d = Path(d)
    names = sorted(os.listdir(d))
    return {"names": [n if ".stage-" not in n else "<STAGE>" + n[n.index(".sqlite") if ".sqlite" in n else 0:] for n in names],
            "stageResidue": [n for n in names if ".stage-" in n],
            "sidecars": [n for n in names if n.endswith(SIDECARS)],
            "files": {n: file_state(d / n) for n in names if n in FILES}}


def logical_digest(path):
    """Logical digest of a ledger DB read through a byte copy (row content only)."""
    c = raw_classify(path, None, Path(path).parent)
    return sha(json.dumps([c["state"], c["ids"], c["tip"]]).encode()) if c["count"] is not None else None


# ------------------------------------------------------------------ fixtures + operations
def build_inputs(d):
    chain = synthetic_chain(N)
    (d / "source.json").write_text(json.dumps(chain), encoding="utf-8")
    live = SL.SqliteLedger(d / "live.sqlite")
    for i in range(N):
        live.append_event({"request_id": f"r{i:02d}", "artifact_id": "synthetic", "pad": "x" * PAD})
    live.backup_to(d / "backup.sqlite")
    del live
    gc.collect()
    return [f"r{i:02d}" for i in range(N)]


def operate(op, d):
    target = d / "final.sqlite"
    if op == "import":
        return SL.SqliteLedger.import_json(d / "source.json", target)
    if op == "backup":
        return SL.SqliteLedger(d / "live.sqlite").backup_to(target)
    return SL.SqliteLedger.restore_backup(d / "backup.sqlite", target)


def run_inproc(root, op, point, hook, expect, label=None):
    d = root.case_dir(f"{op}-{label or point}")
    ids = build_inputs(d)
    watch = {"source.json": d / "source.json", "backup.sqlite": d / "backup.sqlite", "live.sqlite": d / "live.sqlite"}
    before = {k: file_state(v) for k, v in watch.items()}
    before["liveLogical"] = logical_digest(d / "live.sqlite")
    events = []
    if expect == "preexisting":
        Path(d / "final.sqlite").write_bytes(COMPETITOR)
    if expect == "sidecar_only":
        Path(str(d / "final.sqlite") + "-wal").write_bytes(COMPETITOR)
    pre_final = file_state(d / "final.sqlite")
    if hook:
        SL._FAULTS[point] = hook(d, events)
    result, outcome = None, {}
    try:
        try:
            result = operate(op, d)
            outcome = {"returnedOrRaised": "returned", "returnKeys": sorted(result)}
        except BaseException as exc:  # measured, never swallowed silently
            outcome = {"returnedOrRaised": "raised", "exceptionClass": type(exc).__name__, "message": root.redact(str(exc)),
                       "stageResidueAttr": getattr(exc, "stage_residue", None)}
    finally:
        SL._FAULTS.clear()
    after = {k: file_state(v) for k, v in watch.items()}
    after["liveLogical"] = logical_digest(d / "live.sqlite")
    cls = raw_classify(d / "final.sqlite", ids, root.path)
    owner_cls = SL.classify_target(d / "final.sqlite", None)
    retry = {}
    try:
        operate(op, d)
        retry = {"observation": "returned", "note": "observation only; not retry permission"}
    except BaseException as exc:
        retry = {"observation": "raised", "exceptionClass": type(exc).__name__, "note": "observation only; not retry permission"}
    if expect in ("clean", "clean_source_mutated"):
        verdict = (outcome["returnedOrRaised"] == "raised" and cls["state"] == "CLEAN_ABSENT" and not dir_state(d, root)["stageResidue"]
                   and before["backup.sqlite"] == after["backup.sqlite"])
        # A mutated source is the injected fault itself: it must differ, and be detected rather than published.
        verdict &= (before["source.json"] != after["source.json"]) if expect == "clean_source_mutated"             else before["source.json"] == after["source.json"]
    elif expect in ("preexisting", "sidecar_only", "competing"):
        verdict = (outcome["returnedOrRaised"] == "raised" and outcome.get("exceptionClass") == "FileExistsError"
                   and not dir_state(d, root)["stageResidue"])
        if expect == "competing":
            verdict &= file_state(d / "final.sqlite").get("sha256") == sha(COMPETITOR)
        else:
            verdict &= file_state(d / "final.sqlite") == pre_final
    else:  # success expected
        verdict = outcome["returnedOrRaised"] == "returned" and cls["state"] == "USABLE_COMPLETE" and not cls["sidecars"]
    return {"case": f"{op}:{label or point or 'none'}", "operation": op, "expectation": expect, "faultPoint": point, **outcome,
            "sourceAndInputBefore": before, "sourceAndInputAfter": after, "preExistingFinal": pre_final,
            "finalRawState": cls, "ownerClassifierState": owner_cls["state"], "finalFile": file_state(d / "final.sqlite"),
            "directory": dir_state(d, root), "sameSourceRetryObservation": retry, "barrierEvents": events,
            "safeToRetry": False, "verdict": "PASS" if verdict else "FAIL"}


def child_main(op, point, d):
    """Child process: run the owner op and exit hard when the fault point is reached."""
    d = Path(d)

    def barrier(*_a):
        print(f"BARRIER:{point}", flush=True)
        os._exit(9)

    SL._FAULTS[point] = barrier
    operate(op, d)
    print("CHILD_COMPLETED", flush=True)


def run_kill(root, op, point):
    d = root.case_dir(f"{op}-kill-{point}")
    ids = build_inputs(d)
    before = {k: file_state(d / k) for k in ("source.json", "backup.sqlite")}
    proc = subprocess.run([sys.executable, str(Path(__file__).resolve()), "--child", op, point, str(d)],
                          capture_output=True, text=True, timeout=60, cwd=str(REPO_ROOT))
    barrier_seen = f"BARRIER:{point}" in proc.stdout
    cls = raw_classify(d / "final.sqlite", ids, root.path)
    stages = [n for n in os.listdir(d) if ".stage-" in n]
    published = point == "after_publication"
    retry = {}
    try:
        operate(op, d)
        retry = {"observation": "returned", "note": "observation only; not retry permission"}
    except BaseException as exc:
        retry = {"observation": "raised", "exceptionClass": type(exc).__name__, "note": "observation only; not retry permission"}
    ok = barrier_seen and proc.returncode == 9 and (cls["state"] == ("USABLE_COMPLETE" if published else "CLEAN_ABSENT"))
    return {"case": f"{op}:kill@{point}", "operation": op, "faultPoint": point, "killExitCode": proc.returncode,
            "barrierEvents": ["BARRIER:" + point] if barrier_seen else [], "finalRawState": cls,
            "stageResidueAfterKill": len(stages), "sourceUnchanged": before == {k: file_state(d / k) for k in before},
            "sameSourceRetryObservation": retry, "ambiguousOutcome": published, "safeToRetry": False,
            "classification": "AMBIGUOUS_COMPLETE_TARGET_NO_AUTOMATIC_RETRY" if published and ok else
                              ("CLEAN_ABSENT_NO_TARGET" if ok else "UNEXPECTED"),
            "verdict": "PASS" if ok else "FAIL"}


def run_reject(root, op, kind):
    """Invalid target suffix or empty import source: rejected before any stage or target exists."""
    d = root.case_dir(f"{op}-reject-{kind}")
    build_inputs(d)
    target = d / ("final" + {"db": ".db", "noext": "", "sqlite3": ".sqlite3", "empty": ".sqlite"}[kind])
    if kind == "empty":
        (d / "source.json").write_text("[]", encoding="utf-8")
    before = {n: file_state(d / n) for n in sorted(os.listdir(d))}
    reached = []
    SL._FAULTS["before_publication"] = lambda *a: reached.append(1)
    try:
        try:
            SL.SqliteLedger.import_json(d / "source.json", target) if op == "import" else (
                SL.SqliteLedger(d / "live.sqlite").backup_to(target) if op == "backup"
                else SL.SqliteLedger.restore_backup(d / "backup.sqlite", target))
            outcome = {"returnedOrRaised": "returned"}
        except ValueError as exc:
            outcome = {"returnedOrRaised": "raised", "exceptionClass": "ValueError", "message": root.redact(str(exc))}
    finally:
        SL._FAULTS.clear()
    after = {n: file_state(d / n) for n in sorted(os.listdir(d))}
    unchanged = {n: after.get(n) for n in before if not n.startswith("live.sqlite-")} == {n: v for n, v in before.items() if not n.startswith("live.sqlite-")}
    extra = sorted(set(after) - set(before))
    ok = outcome["returnedOrRaised"] == "raised" and not reached and not os.path.lexists(target) and unchanged and not [n for n in extra if ".stage-" in n or n.startswith("final")]
    return {"case": f"{op}:reject-{kind}", "operation": op, "expectation": "rejected_before_stage", **outcome,
            "publicationReached": bool(reached), "targetExists": os.path.lexists(target), "inputsUnchanged": unchanged,
            "newNamesAfter": extra, "safeToRetry": False, "verdict": "PASS" if ok else "FAIL"}


def run_postpublication_validator_fault(root, op):
    """A validator made faulty after publication cannot change a completed call to failure."""
    d = root.case_dir(f"{op}-postpublication-validator")
    ids = build_inputs(d)
    inputs = {name: file_state(d / name) for name in ("source.json", "backup.sqlite", "live.sqlite")}
    original = SL._validate_chain
    reached = []

    def after_publication(_stage):
        reached.append("PUBLISHED")

        def fail_validation(_chain):
            raise Injected("POST_PUBLICATION_VALIDATOR_FAULT")

        SL._validate_chain = fail_validation

    SL._FAULTS["after_publication"] = after_publication
    try:
        try:
            result = operate(op, d)
            outcome = {"returnedOrRaised": "returned", "returnKeys": sorted(result), "count": result["count"]}
        except BaseException as exc:
            outcome = {"returnedOrRaised": "raised", "exceptionClass": type(exc).__name__, "message": root.redact(str(exc))}
    finally:
        SL._FAULTS.clear()
        SL._validate_chain = original
    final = raw_classify(d / "final.sqlite", ids, root.path)
    unchanged = inputs == {name: file_state(d / name) for name in inputs}
    residue = dir_state(d, root)["stageResidue"]
    ok = reached == ["PUBLISHED"] and outcome["returnedOrRaised"] == "returned" and outcome["count"] == N
    ok &= final["state"] == "USABLE_COMPLETE" and unchanged and not residue
    return {"case": f"{op}:postpublication-validator-fault", "operation": op, "expectation": "complete_not_reported_failed",
            **outcome, "barrierEvents": reached, "finalRawState": final, "inputsUnchanged": unchanged,
            "stageResidue": residue, "safeToRetry": False, "verdict": "PASS" if ok else "FAIL"}


# ------------------------------------------------------------------ peer + mutants
def peer_barrier(path, request_id, early=False):
    parent = sqlite3.connect(path)
    parent.execute("BEGIN IMMEDIATE")
    events, times = [], {}
    cmd = [sys.executable, str(PEER), str(path), request_id] + (["--early-entered-mutant"] if early else [])
    child = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1,
                             cwd=str(ENGINE_DIR), env={**os.environ, "PYTHONPATH": str(ENGINE_DIR)})
    try:
        assert child.stdout.readline().strip() == "READY"; events.append("READY")
        child.stdin.write("START_ATTEMPT\n"); child.stdin.flush(); events.append("START_ATTEMPT")
        assert child.stdout.readline().strip() == "ATTEMPTING"; events.append("ATTEMPTING")
        times["release"] = time.perf_counter_ns()
        parent.commit(); events.append("PARENT_RELEASE")
        line = child.stdout.readline().strip()
        assert line.startswith("ENTERED:")
        times["entered"] = int(line.split(":", 1)[1]); events.append("ENTERED")
        assert child.stdout.readline().strip() == "COMPLETE"; events.append("COMPLETE")
        assert child.wait(timeout=20) == 0
    finally:
        parent.rollback(); parent.close()
        if child.poll() is None:
            child.kill(); child.wait(timeout=10)
    return events, times


def order_verdict(events, times):
    if times["entered"] < times["release"]:
        return "REJECT_ENTRY_BEFORE_PARENT_RELEASE"
    ok = (events.index("READY") < events.index("START_ATTEMPT") < events.index("ATTEMPTING")
          < events.index("PARENT_RELEASE") < events.index("ENTERED") < events.index("COMPLETE"))
    return "ORDER_OK" if ok else "ORDER_INVALID"


def run_peer(root):
    d = root.case_dir("peer")
    ledger = SL.SqliteLedger(d / "peer.sqlite")
    ledger.append_event({"request_id": "one"})
    events, times = peer_barrier(d / "peer.sqlite", "two")
    good = order_verdict(events, times)
    SL.SqliteLedger(d / "mut.sqlite")
    m_events, m_times = peer_barrier(d / "mut.sqlite", "mut", early=True)
    mutant = order_verdict(m_events, m_times)

    def fail():
        raise Injected("AFTER_ACQUIRE_BEFORE_MUTATION")

    before = raw_classify(d / "peer.sqlite", None, root.path)["ids"]
    try:
        ledger.append_event({"request_id": "fault"}, after_acquire=fail)
        raised = False
    except Injected:
        raised = True
    mid = raw_classify(d / "peer.sqlite", None, root.path)["ids"]
    sub = subprocess.run([sys.executable, str(PEER), str(d / "peer.sqlite"), "three"], input="START_ATTEMPT\n", capture_output=True,
                         text=True, timeout=30, cwd=str(ENGINE_DIR), env={**os.environ, "PYTHONPATH": str(ENGINE_DIR)})
    after = raw_classify(d / "peer.sqlite", None, root.path)["ids"]
    lines = sub.stdout.splitlines()
    return {"realSecondProcess": True, "events": events, "orderVerdict": good, "earlyEntryMutantVerdict": mutant,
            "postAcquireFaultRaised": raised, "idsBeforeFault": before, "idsAfterFault": mid, "idsAfterSubsequentPeer": after,
            "subsequentPeerExit": sub.returncode, "subsequentPeerEvents": [l.split(":")[0] for l in lines],
            "markers": ["SUBSEQUENT_PEER_ACQUIRES"] if sub.returncode == 0 and after[-1] == "three" and mid == before else [],
            "verdict": "PASS" if good == "ORDER_OK" and mutant == "REJECT_ENTRY_BEFORE_PARENT_RELEASE" and raised and mid == before
            and sub.returncode == 0 and after == before + ["three"] else "FAIL"}


def run_mutants(root):
    out = {}
    orig_publish, orig_seal = SL._publish, SL._seal
    # 1. partial-final mutant
    d = root.case_dir("mutant-partial")
    ids = build_inputs(d)

    def partial(stage, final):
        Path(final).write_bytes(Path(stage).read_bytes()[:2048]); raise Injected("mutant")
    SL._publish = partial
    try:
        try:
            operate("import", d)
        except Injected:
            pass
    finally:
        SL._publish = orig_publish
    st = raw_classify(d / "final.sqlite", ids, root.path)["state"]
    out["partialFinalMutant"] = {"finalState": st, "oracleVerdict": "REJECTED" if st != "CLEAN_ABSENT" else "ACCEPTED_WEAK_ORACLE"}
    # 2. overwrite-capable publication mutant
    d = root.case_dir("mutant-overwrite")
    build_inputs(d)

    def overwrite(stage, final):
        SL._fault("before_publication", stage, final); os.replace(stage, final)
    SL._FAULTS["before_publication"] = lambda s, f: Path(f).write_bytes(COMPETITOR)
    SL._publish = overwrite
    try:
        operate("import", d)
    finally:
        SL._publish = orig_publish; SL._FAULTS.clear()
    changed = file_state(d / "final.sqlite").get("sha256") != sha(COMPETITOR)
    out["overwriteCapableMutant"] = {"competitorOverwritten": changed, "oracleVerdict": "REJECTED" if changed else "ACCEPTED_WEAK_ORACLE"}
    # 3. success-with-short-chain mutant (owner verification must refuse to publish it)
    d = root.case_dir("mutant-short")
    ids = build_inputs(d)

    def short(stage):
        c = sqlite3.connect(stage); c.execute("DELETE FROM blocks WHERE ordinal=(SELECT max(ordinal) FROM blocks)"); c.commit(); c.close()
        return orig_seal(stage)
    SL._seal = short
    try:
        try:
            operate("import", d); raised = False
        except ValueError:
            raised = True
    finally:
        SL._seal = orig_seal
    out["shortChainMutant"] = {"ownerRefusedToPublish": raised, "finalState": raw_classify(d / "final.sqlite", ids, root.path)["state"]}
    # oracle control: a short target is classified incomplete, a full one usable
    d = root.case_dir("oracle-control")
    ids = build_inputs(d)
    operate("import", d)
    full = raw_classify(d / "final.sqlite", ids, root.path)["state"]
    short_state = raw_classify(d / "final.sqlite", ids + ["r99"], root.path)["state"]
    out["oracleControl"] = {"positive": full, "shortExpected": short_state,
                            "verdict": "PASS" if full == "USABLE_COMPLETE" and short_state == "PARTIAL_OPENABLE_INCOMPLETE" else "FAIL"}
    out["earlyPeerEntryMutant"] = "see peer.earlyEntryMutantVerdict"
    out["verdict"] = "PASS" if (out["partialFinalMutant"]["oracleVerdict"] == "REJECTED" and out["overwriteCapableMutant"]["oracleVerdict"] == "REJECTED"
                                and raised and out["shortChainMutant"]["finalState"] == "CLEAN_ABSENT" and out["oracleControl"]["verdict"] == "PASS") else "FAIL"
    return out


def no_clobber_primitive(root):
    d = root.case_dir("primitive")
    a, b = d / "a.bin", d / "b.bin"
    a.write_bytes(b"CANDIDATE"); b.write_bytes(COMPETITOR)
    try:
        os.link(a, b); res = "LINK_OVERWROTE"
    except FileExistsError:
        res = "FileExistsError"
    except OSError as e:
        res = type(e).__name__
    return {"primitive": "os.link(candidate, target) then unlink(candidate)", "platform": sys.platform,
            "competitorSurvived": b.read_bytes() == COMPETITOR, "raised": res,
            "sidecarRaceBoundary": "UNPROVEN: sidecar creation outside cooperative access is not covered by target-file no-clobber"}


# ------------------------------------------------------------------ main
def hooks():
    def fault(*_a):
        raise Injected("INJECTED_FAULT")
    def at_insert(d, ev):
        def h(ordinal):
            ev.append(f"insert:{ordinal}")
            if ordinal == MID_INSERT:
                raise Injected("INJECTED_FAULT")
        return h
    def const(f):
        return lambda d, ev: f
    def race(d, ev):
        def h(stage, final):
            ev.append("PUBLICATION_RACE_CREATOR")
            Path(final).write_bytes(COMPETITOR)
        return h
    def verified(d, ev):
        def h(stage, final):
            c = raw_classify(stage, None, d)
            ev.append(f"VERIFIED_BEFORE_PUBLICATION:{c['state']}:{c['count']}:target_absent={not os.path.lexists(final)}")
        return h
    def mutate_source(d, ev):
        def h(path):
            path.write_bytes(path.read_bytes() + b" "); ev.append("SOURCE_MUTATED_BEFORE_REVERIFY")
        return h
    return fault, at_insert, const, race, verified, mutate_source


def git(*args):
    return subprocess.run(["git", *args], cwd=REPO_ROOT, capture_output=True, text=True).stdout.strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(DEFAULT_OUT))
    ap.add_argument("--child", nargs=3, metavar=("OP", "POINT", "DIR"))
    args = ap.parse_args()
    if args.child:
        return child_main(*args.child)
    out = Path(args.out)
    if out.exists():
        print("refusing to overwrite existing evidence file", file=sys.stderr)
        return 2
    fault, at_insert, const, race, verified, mutate_source = hooks()
    started = time.time()
    with Root() as root:
        cases = []
        cases.append(run_inproc(root, "import", "before_publication", verified, "success", "verified-before-publication"))
        cases.append(run_inproc(root, "import", "import_before_insert", const(fault), "clean"))
        cases.append(run_inproc(root, "import", "import_insert", at_insert, "clean", "insert-7"))
        cases.append(run_inproc(root, "import", "before_source_reverify", mutate_source, "clean_source_mutated", "source-reread-mismatch"))
        cases.append(run_inproc(root, "import", "after_candidate_close", const(fault), "clean"))
        cases.append(run_inproc(root, "import", "before_publication", const(fault), "clean", "fault-before-publication"))
        cases.append(run_inproc(root, "import", "before_publication", race, "competing", "competing-creator"))
        for op in ("backup", "restore"):
            cases.append(run_inproc(root, op, None, None, "success", "clean-success"))
            cases.append(run_inproc(root, op, "backup_progress", const(fault), "clean", "mid-copy"))
            cases.append(run_inproc(root, op, "after_candidate_close", const(fault), "clean"))
            cases.append(run_inproc(root, op, "before_publication", const(fault), "clean", "fault-before-publication"))
            cases.append(run_inproc(root, op, "before_publication", race, "competing", "competing-creator"))
        cases.append(run_inproc(root, "import", None, None, "success", "clean-success"))
        for op in ("import", "backup", "restore"):
            cases.append(run_inproc(root, op, None, None, "preexisting", "preexisting-target"))
            cases.append(run_inproc(root, op, None, None, "sidecar_only", "sidecar-only"))
        for op in ("import", "backup", "restore"):
            cases.append(run_kill(root, op, "before_publication"))
            cases.append(run_kill(root, op, "after_publication"))
        for op in ("import", "backup", "restore"):
            for kind in ("db", "noext", "sqlite3"):
                cases.append(run_reject(root, op, kind))
        cases.append(run_reject(root, "import", "empty"))
        for op in ("backup", "restore"):
            cases.append(run_postpublication_validator_fault(root, op))
        peer = run_peer(root)
        mutants = run_mutants(root)
        primitive = no_clobber_primitive(root)
    owner_bytes, probe_bytes = OWNER_FILE.read_bytes(), Path(__file__).read_bytes()
    failed = [c["case"] for c in cases if c["verdict"] != "PASS"]
    verified_events = [e for c in cases for e in c.get("barrierEvents", []) if e.startswith("VERIFIED_BEFORE_PUBLICATION")]
    markers = ["VERIFIED_BEFORE_PUBLICATION"] if verified_events and all(
        e == f"VERIFIED_BEFORE_PUBLICATION:UNKNOWN_PREEXISTING_ORIGIN:{N}:target_absent=True" for e in verified_events) else []
    if all(c["verdict"] == "PASS" for c in cases if c.get("expectation") == "competing"):
        markers.append("PREEXISTING_TARGET_UNCHANGED_AFTER_RAISE")
    if all(c["safeToRetry"] is False for c in cases):
        markers.append("NO_AUTOMATIC_RETRY")
    markers += peer["markers"]
    evidence = {"schemaVersion": SCHEMA_ID, "executionBaseHead": git("rev-parse", "HEAD"),
                "ownerSha256": sha(owner_bytes), "probeSha256": sha(probe_bytes),
                "syntheticParameters": {"importChainLength": N, "backupPadBytesPerEvent": PAD, "midInsertOrdinal": MID_INSERT,
                                        "backupCopyPagesPerStep": 8, "publication": "hard-link no-clobber"},
                "filesystemNoClobberObservation": primitive, "cases": cases, "peer": peer, "mutants": mutants,
                "markers": markers, "failedCases": failed,
                "notInducible": [], "cleanup": root.cleanup, "providerCallCount": 0, "privateDataAccessed": "NONE",
                "durationSeconds": round(time.time() - started, 1),
                "overallVerdict": "PASS" if not failed and peer["verdict"] == "PASS" and mutants["verdict"] == "PASS"
                and primitive["competitorSurvived"] and root.cleanup["outcome"] == "REMOVED_EXACT_ROOT" else "FAIL",
                "independentProbeDisposition": "PENDING_REVIEWER_EXECUTION",
                "claimBoundary": "synthetic single-host Windows observation; no power-loss, multi-host, retention, RPO/RTO or real-ledger claim"}
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(evidence, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"overall={evidence['overallVerdict']} cases={len(cases)} failed={failed} peer={peer['verdict']} mutants={mutants['verdict']}")
    return 0 if evidence["overallVerdict"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
