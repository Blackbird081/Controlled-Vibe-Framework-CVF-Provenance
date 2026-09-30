#!/usr/bin/env python3
"""Q001 SQLite migration/recovery rehearsal: observe and classify on disposable synthetic data only.

Never edits the ledger owner file. Faults are injected inside this process (patched calls, restored
afterwards) or through real OS effects; every state is measured with a raw sqlite3/hashlib oracle
that does not call the product reader.
"""
import argparse, contextlib, gc, hashlib, json, os, queue, shutil, sqlite3, subprocess, sys, threading, time, uuid
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
ENGINE_DIR = REPO_ROOT / "EXTENSIONS" / "CVF_v1.6.1_GOVERNANCE_ENGINE" / "ai_governance_core"
PEER = ENGINE_DIR / "tests" / "q001_sqlite_ledger_peer.py"
RUNTIME = REPO_ROOT / ".cvf" / "runtime"
sys.path.insert(0, str(ENGINE_DIR))
from ledger_layer import sqlite_ledger as SL  # noqa: E402
from ledger_layer.block_builder import BlockBuilder  # noqa: E402

LEDGER, REAL_CONNECT, REAL_PATH = SL.SqliteLedger, sqlite3.connect, SL.Path
SCHEMA_ID = "cvf.ncr.q001.sqliteMigrationRecoveryRehearsal.workerObservation@1"
N, MID_INSERT_AFTER, KILL_TRIALS, LARGE_N = 12, 6, 5, 3000
SIDECARS = ("-wal", "-shm", "-journal")
OWNER_DDL = ("CREATE TABLE blocks (ordinal INTEGER PRIMARY KEY, request_id TEXT NOT NULL UNIQUE, "
             "block_json TEXT NOT NULL, block_hash TEXT NOT NULL)")
NOT_INDUCIBLE = "NOT_INDUCIBLE_WITHOUT_OWNER_HOOK"

class Injected(RuntimeError):
    pass


# ---------------------------------------------------------------- disposable root
class DisposableRoot:
    def __enter__(self):
        RUNTIME.mkdir(parents=True, exist_ok=True)
        if subprocess.run(["git", "check-ignore", "-q", ".cvf/runtime/x"], cwd=REPO_ROOT).returncode != 0:
            raise RuntimeError("runtime scratch area is not git-ignored")
        self.path = RUNTIME / f"q001-sqlite-rehearsal-{uuid.uuid4().hex[:10]}"
        self.path.mkdir()
        self.scratch = self.path / "oracle"
        self.scratch.mkdir()
        self.n, self.cleanup = 0, {"outcome": "NOT_RUN"}
        return self

    def fresh(self, name):
        self.n += 1
        d = self.path / f"{name}-{self.n:02d}"
        d.mkdir()
        return d

    def redact(self, text):
        for raw, label in ((str(self.path), "<DISPOSABLE_ROOT>"), (self.path.as_posix(), "<DISPOSABLE_ROOT>"),
                           (str(REPO_ROOT), "<REPO_ROOT>"), (REPO_ROOT.as_posix(), "<REPO_ROOT>")):
            text = text.replace(raw, label)
        return text[:300]

    def __exit__(self, *exc):
        gc.collect()
        try:
            if self.path.parent != RUNTIME or not self.path.name.startswith("q001-sqlite-rehearsal-"):
                raise RuntimeError("refusing to remove an unexpected path")
            shutil.rmtree(self.path)
            self.cleanup = {"outcome": "REMOVED_BY_PROBE"}
        except Exception as error:  # residue is disclosed, never retried with shell recursion
            self.cleanup = {"outcome": "RESIDUE_LEFT", "category": type(error).__name__}
        return False


# ---------------------------------------------------------------- fixtures
def build_chain(n, tag="rehearsal", ids=None):
    builder, prev, chain = BlockBuilder(), "GENESIS", []
    for i in range(1, n + 1):
        rid = ids[i - 1] if ids else f"{tag}-req-{i:04d}"
        blk = builder.build_block(prev, {"request_id": rid, "artifact_id": "synthetic", "n": i})
        chain.append(blk)
        prev = blk["hash"]
    return chain

def write_json(path, chain):
    Path(path).write_text(json.dumps(chain), encoding="utf-8")

def raw_build(path, chain, wal=False):
    """Oracle-side fixture writer: plain sqlite3, no product code."""
    conn = REAL_CONNECT(path)
    try:
        if wal:
            conn.execute("PRAGMA journal_mode=WAL")
        conn.execute(OWNER_DDL)
        conn.execute("PRAGMA user_version=1")
        for i, blk in enumerate(chain, 1):
            conn.execute("INSERT INTO blocks VALUES (?,?,?,?)",
                         (i, blk["event"]["request_id"], json.dumps(blk, sort_keys=True), blk["hash"]))
        conn.commit()
    finally:
        conn.close()

def product_sqlite(d, name, chain):
    src, led = d / f"{name}.json", d / f"{name}.sqlite"
    write_json(src, chain)
    LEDGER.import_json(src, led)
    return led


# ---------------------------------------------------------------- independent oracle
def sidecars_of(path):
    return sorted(s for s in SIDECARS if Path(str(path) + s).exists())

def _block_hash(block):
    body = {k: block[k] for k in ("timestamp", "previous_hash", "event")}
    return hashlib.sha256(json.dumps(body, sort_keys=True).encode()).hexdigest()

def raw_rows(path, scratch):
    """Read a byte copy so the oracle cannot alter the observed target."""
    cp = Path(scratch) / f"o-{uuid.uuid4().hex[:8]}.sqlite"
    shutil.copyfile(path, cp)
    if Path(str(path) + "-wal").exists():
        shutil.copyfile(str(path) + "-wal", str(cp) + "-wal")
    conn = None
    try:
        conn = REAL_CONNECT(cp)
        if conn.execute("PRAGMA user_version").fetchone()[0] != 1:
            return "UNOPENABLE", "NO_LEDGER_SCHEMA_VERSION"
        return "OK", conn.execute("SELECT ordinal, request_id, block_json, block_hash FROM blocks ORDER BY ordinal").fetchall()
    except sqlite3.Error as error:
        return "UNOPENABLE", type(error).__name__
    finally:
        if conn is not None:
            conn.close()
        for suffix in ("", "-wal", "-shm"):
            with contextlib.suppress(OSError):
                os.remove(str(cp) + suffix)

def check_rows(rows):
    prior, chain = "GENESIS", []
    for i, (ordinal, rid, raw, bhash) in enumerate(rows, 1):
        if ordinal != i:
            return None, "ORDINAL_GAP"
        try:
            blk = json.loads(raw)
        except ValueError:
            return None, "BLOCK_JSON_INVALID"
        if not isinstance(blk, dict) or set(blk) != {"timestamp", "previous_hash", "event", "hash"}:
            return None, "BLOCK_SHAPE"
        if not isinstance(blk["event"], dict) or blk["event"].get("request_id") != rid:
            return None, "REQUEST_ID_MISMATCH"
        if blk["hash"] != bhash or _block_hash(blk) != bhash:
            return None, "HASH_MISMATCH"
        if blk["previous_hash"] != prior:
            return None, "PREDECESSOR_MISMATCH"
        prior = bhash
        chain.append(blk)
    return chain, "OK"

def classify(path, expected, scratch):
    sc = sidecars_of(path)
    if not Path(path).exists():
        return {"state": "SIDECAR_ONLY" if sc else "CLEAN_ABSENT", "sidecars": sc, "reason": "", "blocks": 0}
    status, payload = raw_rows(path, scratch)
    if status != "OK":
        return {"state": "PARTIAL_UNOPENABLE", "sidecars": sc, "reason": payload, "blocks": None}
    chain, reason = check_rows(payload)
    if chain is None:
        return {"state": "PARTIAL_OPENABLE_INCOMPLETE", "sidecars": sc, "reason": reason, "blocks": len(payload)}
    if chain == expected:
        return {"state": "USABLE_COMPLETE", "sidecars": sc, "reason": "", "blocks": len(chain)}
    why = ("EMPTY_CHAIN" if not chain else "SHORT_CHAIN" if expected[:len(chain)] == chain else "DIFFERENT_CHAIN")
    return {"state": "PARTIAL_OPENABLE_INCOMPLETE", "sidecars": sc, "reason": why, "blocks": len(chain)}

def snap(path, scratch):
    p = Path(path)
    if not p.exists():
        return {"raw": None, "logical": None, "sidecars": sidecars_of(p)}
    raw = hashlib.sha256(p.read_bytes()).hexdigest()
    if p.suffix == ".json":
        return {"raw": raw, "logical": raw, "sidecars": []}
    status, payload = raw_rows(p, scratch)
    logical = (hashlib.sha256("\n".join(f"{o}|{r}|{h}" for o, r, _, h in payload).encode()).hexdigest()
               if status == "OK" else None)
    return {"raw": raw, "logical": logical, "sidecars": sidecars_of(p)}

def compare_snap(before, after):
    if before["logical"] != after["logical"]:
        verdict = "LOGICAL_DIGEST_CHANGED"
    elif before["raw"] != after["raw"]:
        verdict = "RAW_CHANGED_LOGICAL_EQUAL"
    else:
        verdict = "UNCHANGED"
    return {"verdict": verdict, "sidecarsBefore": before["sidecars"], "sidecarsAfter": after["sidecars"]}

def tag_outcome(raised, state, verdicts):
    if raised:
        tag = {"CLEAN_ABSENT": "CLEAN_ABSENT_AFTER_RAISE", "SIDECAR_ONLY": "SIDECAR_RESIDUE_FINDING",
               "USABLE_COMPLETE": "COMPLETE_BUT_REPORTED_FAILED_FINDING"}.get(state, "PARTIAL_TARGET_FINDING")
    else:
        tag = "SUCCESS_CORRECT_STATE" if state == "USABLE_COMPLETE" else "SUCCESS_WRONG_STATE_FINDING"
    changed = any(v["verdict"] == "LOGICAL_DIGEST_CHANGED" for v in verdicts.values())
    return tag, (["INPUT_CHANGED_FINDING"] if changed else [])

def tag_preexisting(raised, unchanged):
    return "PREEXISTING_TARGET_UNCHANGED_AFTER_RAISE" if raised and unchanged else "PREEXISTING_TARGET_CHANGED_FINDING"


# ---------------------------------------------------------------- fault injection (probe process only)
class InsertFault(sqlite3.Connection):
    def execute(self, sql, *args):
        if sql.lstrip().upper().startswith("INSERT INTO BLOCKS"):
            done = getattr(self, "inserted", 0)
            if done >= MID_INSERT_AFTER:
                raise Injected("INJECTED_INSERT_FAULT_AFTER_SIXTH_INSERT")
            self.inserted = done + 1
        return super().execute(sql, *args)

@contextlib.contextmanager
def fault_connect(target, k, mode, record):
    """On the k-th SqliteLedger._connect to `target`: raise, or hand back a connection failing mid-insert."""
    original, key, count = LEDGER._connect, os.path.normcase(os.path.abspath(target)), [0]

    def wrapped(self):
        if os.path.normcase(os.path.abspath(self.ledger_path)) == key:
            count[0] += 1
            if count[0] == k:
                size = os.path.getsize(target) if os.path.exists(target) else None
                record.update({"connectIndex": k, "targetExistedAtFault": os.path.exists(target), "targetSizeAtFault": size})
                if mode == "raise":
                    raise Injected("INJECTED_CONNECT_FAULT")
                conn = REAL_CONNECT(self.ledger_path, timeout=self.timeout, factory=InsertFault)
                conn.execute("PRAGMA journal_mode=WAL")
                conn.execute("PRAGMA synchronous=FULL")
                return conn
        return original(self)

    LEDGER._connect = wrapped
    try:
        yield
    finally:
        LEDGER._connect = original

@contextlib.contextmanager
def source_read_fault(source, mode):
    calls = [0]

    class FaultPath(type(REAL_PATH())):
        def read_bytes(self):
            data = super().read_bytes()
            if os.path.normcase(str(self)) == os.path.normcase(str(source)):
                calls[0] += 1
                if mode == "raise":
                    raise OSError("INJECTED_SOURCE_READ_FAULT")
                if mode == "second_read_differs" and calls[0] == 2:
                    return data + b"\n"
            return data

    SL.Path = FaultPath
    try:
        yield calls
    finally:
        SL.Path = REAL_PATH


# ---------------------------------------------------------------- case runner
def attempt(call, redact=lambda s: s):
    try:
        call()
        return {"returnedOrRaised": "RETURNED", "exceptionClass": None}
    except BaseException as error:  # observation: every failure mode is recorded
        return {"returnedOrRaised": "RAISED", "exceptionClass": type(error).__name__, "exceptionMessage": redact(str(error))}

def add_retry(ctx, rec, call, target, expected):
    gc.collect()
    rec["retry"] = attempt(call, ctx.redact)
    rec["retry"]["targetStateAfterRetry"] = classify(target, expected, ctx.scratch)

def run_case(ctx, scenario_id, sub, fault_point, call, target, expected, inputs, retry=None, injection=None, preexisting=False):
    gc.collect()
    before = {n: snap(p, ctx.scratch) for n, p in inputs.items()}
    outcome = attempt(call, ctx.redact)
    gc.collect()
    after = {n: snap(p, ctx.scratch) for n, p in inputs.items()}
    verdicts = {n: compare_snap(before[n], after[n]) for n in inputs}
    state = classify(target, expected, ctx.scratch)
    raised = outcome["returnedOrRaised"] == "RAISED"
    if preexisting:
        unchanged = all(v["verdict"] != "LOGICAL_DIGEST_CHANGED" and v["sidecarsBefore"] == v["sidecarsAfter"]
                        and before[n]["raw"] == after[n]["raw"] for n, v in verdicts.items())
        tag, flags = tag_preexisting(raised, unchanged), []
    else:
        tag, flags = tag_outcome(raised, state["state"], verdicts)
    rec = {"scenarioId": scenario_id, "subCase": sub, "faultPoint": fault_point, "injection": injection or {},
           "outcome": outcome, "targetState": state, "digests": {"before": before, "after": after, "verdicts": verdicts},
           "tag": tag, "flags": flags}
    if retry is not None:
        add_retry(ctx, rec, retry, target, expected)
    return rec


# ---------------------------------------------------------------- peer processes
class LineReader:
    def __init__(self, stream):
        self.q = queue.Queue()
        threading.Thread(target=lambda: [self.q.put(line.rstrip("\r\n")) for line in stream], daemon=True).start()

    def get(self, timeout=30):  # DEADLOCK_SAFETY_ONLY: expiry is a failure, never evidence
        try:
            return self.q.get(timeout=timeout)
        except queue.Empty:
            raise RuntimeError("DEADLOCK_SAFETY_TIMEOUT waiting for peer output")

def peer_env():
    return {**os.environ, "PYTHONPATH": str(ENGINE_DIR)}

def order_verdict(events, release_ns, entered_ns):
    if entered_ns < release_ns:
        return "REJECT_ENTRY_BEFORE_PARENT_RELEASE"
    names = [n for n, _ in events]
    ordered = (names.index("READY") < names.index("START_ATTEMPT") < names.index("ATTEMPTING")
               and names.index("PARENT_RELEASE") < names.index("ENTERED") < names.index("COMPLETE"))
    return "ORDER_OK" if ordered else "REJECT_EVENT_ORDER"

def run_barrier_peer(path, request_id, early=False, during=None):
    parent = REAL_CONNECT(path)
    parent.execute("BEGIN IMMEDIATE")
    cmd = [sys.executable, str(PEER), str(path), request_id] + (["--early-entered-mutant"] if early else [])
    child = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
                             bufsize=1, cwd=str(ENGINE_DIR), env=peer_env())
    reader, events, dur = LineReader(child.stdout), [], None
    try:
        if reader.get() != "READY":
            raise RuntimeError("peer did not report READY")
        events.append(("READY", time.perf_counter_ns()))
        child.stdin.write("START_ATTEMPT\n")
        child.stdin.flush()
        events.append(("START_ATTEMPT", time.perf_counter_ns()))
        if reader.get() != "ATTEMPTING":
            raise RuntimeError("peer did not report ATTEMPTING")
        events.append(("ATTEMPTING", time.perf_counter_ns()))
        dur = during() if during else None
        release_ns = time.perf_counter_ns()
        parent.rollback()
        events.append(("PARENT_RELEASE", release_ns))
        line = reader.get()
        if not line.startswith("ENTERED:"):
            raise RuntimeError("peer did not report ENTERED")
        entered_ns = int(line.split(":", 1)[1])
        events.append(("ENTERED", time.perf_counter_ns()))
        if reader.get() != "COMPLETE":
            raise RuntimeError("peer did not report COMPLETE")
        events.append(("COMPLETE", time.perf_counter_ns()))
        code = child.wait(timeout=30)
    finally:
        parent.close()
        if child.poll() is None:
            child.kill()
            child.wait(timeout=30)
    return {"events": events, "releaseNs": release_ns, "enteredNs": entered_ns, "peerExit": code,
            "orderVerdict": order_verdict(events, release_ns, entered_ns), "during": dur}

def liveness(ctx, ledger_path, scenario_id):
    """RH-CONC-04: post-acquire fault through the production append hook, then an unchanged real peer acquires."""
    before = snap(ledger_path, ctx.scratch)
    status, rows = raw_rows(ledger_path, ctx.scratch)
    chain_before, _ = check_rows(rows) if status == "OK" else (None, "UNREADABLE")
    if chain_before is None:
        proc = subprocess.run([sys.executable, str(PEER), str(ledger_path), f"live-{scenario_id}"], input="START_ATTEMPT\n",
                              capture_output=True, text=True, cwd=str(ENGINE_DIR), env=peer_env(), timeout=60)
        return {"scenarioId": scenario_id, "applicable": False,
                "reason": "source is deliberately unreadable or corrupt; no valid chain to append to",
                "peerRefusedCorruptSource": proc.returncode != 0, "peerExit": proc.returncode}

    def fail():
        raise Injected("AFTER_ACQUIRE_BEFORE_MUTATION")

    fault = "NOT_RAISED"
    try:
        LEDGER(ledger_path).append_event({"request_id": f"fault-{scenario_id}"}, after_acquire=fail)
    except Injected:
        fault = "RAISED_AFTER_ACQUIRE"
    gc.collect()
    mid = compare_snap(before, snap(ledger_path, ctx.scratch))
    rid = f"live-{scenario_id}"
    proc = subprocess.run([sys.executable, str(PEER), str(ledger_path), rid], input="START_ATTEMPT\n", capture_output=True,
                          text=True, cwd=str(ENGINE_DIR), env=peer_env(), timeout=60)
    lines = proc.stdout.splitlines()
    status, rows = raw_rows(ledger_path, ctx.scratch)
    chain_after, _ = check_rows(rows) if status == "OK" else (None, "UNREADABLE")
    acquired = (proc.returncode == 0 and len(lines) == 4 and lines[0] == "READY" and lines[1] == "ATTEMPTING"
                and lines[2].startswith("ENTERED:") and lines[3] == "COMPLETE" and chain_after is not None
                and chain_after[:len(chain_before)] == chain_before and len(chain_after) == len(chain_before) + 1
                and chain_after[-1]["event"]["request_id"] == rid)
    return {"scenarioId": scenario_id, "applicable": True, "postAcquireFault": fault,
            "chainUnchangedAfterFault": mid["verdict"] != "LOGICAL_DIGEST_CHANGED",
            "peerExit": proc.returncode, "expectedSourceChange": f"{len(chain_before)} -> {len(chain_after) if chain_after else None} blocks",
            "SUBSEQUENT_PEER_ACQUIRES": bool(acquired)}


# ---------------------------------------------------------------- oracle self-check (mutants and controls)
def mutant_import_leaves_partial(src, target):
    raw_build(target, json.loads(Path(src).read_text())[:MID_INSERT_AFTER])
    raise Injected("MUTANT_LEFT_PARTIAL_TARGET")

def mutant_import_short_chain(src, target):
    raw_build(target, json.loads(Path(src).read_text())[:-1])
    return {"count": N}

def mutant_backup_mutates_source(source, target):
    shutil.copyfile(source, target)
    conn = REAL_CONNECT(source)
    conn.execute("DELETE FROM blocks WHERE ordinal=(SELECT max(ordinal) FROM blocks)")
    conn.commit()
    conn.close()

def oracle_selfcheck(ctx):
    d, chain = ctx.fresh("selfcheck"), build_chain(N, "selfcheck")
    sc, out = ctx.scratch, {"controls": {}, "mutants": {}}
    absent, sidecar_only, good = d / "absent.sqlite", d / "sidecar.sqlite", d / "good.sqlite"
    Path(str(sidecar_only) + "-wal").write_bytes(b"x")
    raw_build(good, chain)
    empty, tampered, garbage, zero = d / "empty.sqlite", d / "tampered.sqlite", d / "garbage.sqlite", d / "zero.sqlite"
    raw_build(empty, [])
    bad = json.loads(json.dumps(chain))
    bad[5]["hash"] = "0" * 64
    raw_build(tampered, bad)
    garbage.write_bytes(os.urandom(4096))
    zero.write_bytes(b"")
    declared = {"absent": (absent, "CLEAN_ABSENT"), "sidecarOnly": (sidecar_only, "SIDECAR_ONLY"),
                "completeValid": (good, "USABLE_COMPLETE"), "emptySchemaValid": (empty, "PARTIAL_OPENABLE_INCOMPLETE"),
                "tamperedHash": (tampered, "PARTIAL_OPENABLE_INCOMPLETE"), "garbageFile": (garbage, "PARTIAL_UNOPENABLE"),
                "zeroByteFile": (zero, "PARTIAL_UNOPENABLE")}
    for name, (path, want) in declared.items():
        got = classify(path, chain, sc)["state"]
        out["controls"][name] = {"declared": want, "observed": got, "ok": got == want}
    src = d / "mut-source.json"
    write_json(src, chain)
    for name, fn, want_tag, want_state in (("leavesPartialTarget", mutant_import_leaves_partial, "PARTIAL_TARGET_FINDING", "PARTIAL_OPENABLE_INCOMPLETE"),
                                            ("successWithShortChain", mutant_import_short_chain, "SUCCESS_WRONG_STATE_FINDING", "PARTIAL_OPENABLE_INCOMPLETE")):
        target = d / f"mut-{name}.sqlite"
        rec = run_case(ctx, "MUTANT", name, "mutant", lambda f=fn, t=target: f(src, t), target, chain, {"source": src})
        naive_accepts = rec["outcome"]["returnedOrRaised"] in ("RAISED", "RETURNED")
        out["mutants"][name] = {"tag": rec["tag"], "state": rec["targetState"]["state"], "naiveExceptionOnlyOracleAccepts": naive_accepts,
                                "rejected": rec["tag"] == want_tag and rec["targetState"]["state"] == want_state}
    msrc = product_sqlite(d, "mut-backup-source", chain)
    rec = run_case(ctx, "MUTANT", "sourceLogicalDigestAltered", "mutant", lambda: mutant_backup_mutates_source(msrc, d / "mut-backup.sqlite"),
                   d / "mut-backup.sqlite", chain, {"source": msrc})
    out["mutants"]["sourceLogicalDigestAltered"] = {"tag": rec["tag"], "flags": rec["flags"],
                                                    "rejected": "INPUT_CHANGED_FINDING" in rec["flags"]}
    out["allRejectedAndClassified"] = all(c["ok"] for c in out["controls"].values()) and all(m["rejected"] for m in out["mutants"].values())
    return out


# ---------------------------------------------------------------- scenarios
def scen_positive(ctx):
    d, chain = ctx.fresh("pos"), build_chain(N, "pos")
    src, imp, bak, rst = d / "source.json", d / "imported.sqlite", d / "backup.sqlite", d / "restored.sqlite"
    write_json(src, chain)
    r1 = run_case(ctx, "RH-POS-01", "import", "none", lambda: LEDGER.import_json(src, imp), imp, chain, {"source": src})
    r2 = run_case(ctx, "RH-POS-01", "backup", "none", lambda: LEDGER(imp).backup_to(bak), bak, chain, {"source": imp})
    r3 = run_case(ctx, "RH-POS-01", "restore", "none", lambda: LEDGER.restore_backup(bak, rst), rst, chain, {"source": bak})
    logicals = {snap(p, ctx.scratch)["logical"] for p in (imp, bak, rst)}
    equal = (all(r["tag"] == "SUCCESS_CORRECT_STATE" and not r["flags"] for r in (r1, r2, r3)) and len(logicals) == 1
             and json.loads(src.read_text()) == chain)
    return [r1, r2, r3, {"scenarioId": "RH-POS-01", "subCase": "chainEquality", "literal": "ROUNDTRIP_CHAIN_EQUAL", "ok": equal,
                         "blocks": N, "tip": chain[-1]["hash"], "logicalDigest": sorted(logicals)[0],
                         "tag": "ROUNDTRIP_CHAIN_EQUAL" if equal else "ROUNDTRIP_CHAIN_NOT_EQUAL_FINDING"}]

def scen_import(ctx):
    recs, builder = [], BlockBuilder()
    chain = build_chain(N, "imp")
    dup = build_chain(N, "imp", ids=[f"imp-req-{i:04d}" if i != 8 else "imp-req-0003" for i in range(1, N + 1)])
    pred = json.loads(json.dumps(chain))
    pred[5] = builder.build_block("GENESIS", pred[5]["event"])
    corrupt = json.loads(json.dumps(chain))
    corrupt[5]["hash"] = "0" * 64
    for sub, data in (("hashCorruptSource", corrupt), ("duplicateRequestId", dup), ("brokenPredecessor", pred)):
        d = ctx.fresh("imp-f1")
        src, tgt = d / "source.json", d / "target.sqlite"
        write_json(src, data)
        recs.append(run_case(ctx, "RH-IMP-F1", sub, "before target creation (natural rejection)", lambda s=src, t=tgt: LEDGER.import_json(s, t),
                             tgt, chain, {"source": src}, retry=lambda s=src, t=tgt: LEDGER.import_json(s, t)))
    cases = (("RH-IMP-F1", "injectedSourceReadException", "before target creation", ("read", "raise")),
             ("RH-IMP-F2", "afterTargetCreationBeforeFirstInsert", "third connect to target, before any insert", ("connect", "raise")),
             ("RH-IMP-F3", "insideInsertLoopAfterSixth", "seventh insert statement, before commit", ("connect", "insert")),
             ("RH-IMP-F4", "verificationSecondReadDiffers", "after commit, at verification", ("read", "second_read_differs")))
    for sid, sub, point, (kind, mode) in cases:
        d = ctx.fresh(sid.lower())
        src, tgt, rec_inj = d / "source.json", d / "target.sqlite", {}
        write_json(src, chain)
        cm = source_read_fault(src, mode) if kind == "read" else fault_connect(tgt, 3, mode, rec_inj)
        with cm:
            rec = run_case(ctx, sid, sub, point, lambda s=src, t=tgt: LEDGER.import_json(s, t), tgt, chain, {"source": src},
                           injection={"mechanism": kind + "/" + mode})
        rec["injection"].update(rec_inj)
        add_retry(ctx, rec, lambda s=src, t=tgt: LEDGER.import_json(s, t), tgt, chain)
        recs.append(rec)
    return recs

def _preexisting(ctx, sid, op, chain, make_source, sidecar_only):
    d = ctx.fresh(sid.lower())
    src = make_source(d)
    tgt = d / "target.sqlite"
    (Path(str(tgt) + "-wal") if sidecar_only else tgt).write_bytes(b"PREEXISTING-SENTINEL")
    inputs = {"source": src, "preexistingTarget": Path(str(tgt) + "-wal") if sidecar_only else tgt}
    call = (lambda: LEDGER(src).backup_to(tgt)) if op == "backup" else (lambda: LEDGER.restore_backup(src, tgt))
    rec = run_case(ctx, sid, "sidecarOnlyPresent" if sidecar_only else "targetFilePresent", "target or sidecar already present", call,
                   tgt, chain, inputs, retry=call, preexisting=True)
    return rec, src

def _locked(ctx, sid, op, chain, source, d):
    target = d / "locked-target.sqlite"
    ledger = LEDGER(source, timeout=0.3) if op == "backup" else None
    around = {"before": snap(source, ctx.scratch)}
    holder = REAL_CONNECT(source, timeout=0.1)
    holder.execute("PRAGMA locking_mode=EXCLUSIVE")
    holder.execute("BEGIN EXCLUSIVE")
    call = (lambda: ledger.backup_to(target)) if op == "backup" else (lambda: LEDGER.restore_backup(source, target))
    try:
        rec = run_case(ctx, sid, "sourceHeldExclusiveLock", "real source lock before the copy starts (not a mid-copy interruption)", call,
                       target, chain, {})
    finally:
        holder.rollback()
        holder.close()
    add_retry(ctx, rec, call, target, chain)
    gc.collect()
    around["after"] = snap(source, ctx.scratch)
    rec["sourceDigestsAroundLock"] = {**around, "verdict": compare_snap(around["before"], around["after"])["verdict"]}
    return rec

def _child(op, source, target):
    print("STARTED", flush=True)
    if op == "backup":
        LEDGER(source).backup_to(target)
    else:
        LEDGER.restore_backup(source, target)
    print("DONE", flush=True)

def kill_trials(ctx, op, big_chain, seed):
    """Kill the child once the production call has created the target (an event inside the call), then observe."""
    trials, d = [], ctx.fresh(f"kill-{op}")
    for i in range(KILL_TRIALS):
        target = d / f"target-{i}.sqlite"
        child = subprocess.Popen([sys.executable, str(Path(__file__)), "--child-op", op, "--source", str(seed), "--target", str(target)],
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, env=peer_env())
        first = LineReader(child.stdout).get(60)
        deadline = time.monotonic() + 30  # DEADLOCK_SAFETY_ONLY
        while not target.exists() and child.poll() is None and time.monotonic() < deadline:
            pass
        child.kill()
        child.wait(timeout=30)
        gc.collect()
        size = target.stat().st_size if target.exists() else None
        st = classify(target, big_chain, ctx.scratch)
        if st["state"] == "USABLE_COMPLETE":
            kind = "COMPLETE_BEFORE_KILL"
        elif not target.exists():
            kind = "KILLED_BEFORE_TARGET_CREATION"
        elif size == 0:
            kind = "PRE_COPY_ZERO_BYTE_TARGET"
        else:
            kind = "MID_COPY_PARTIAL"
        retry = attempt(lambda: LEDGER(seed).backup_to(target) if op == "backup" else LEDGER.restore_backup(seed, target))
        trials.append({"trial": i + 1, "childReported": first, "kind": kind, "targetState": st["state"], "reason": st["reason"],
                       "targetSizeBytes": size, "sidecars": st["sidecars"], "retryAfterKill": retry})
    return {"trials": trials, "distribution": dict(Counter(t["kind"] for t in trials))}

def _mid_copy_record(ctx, sid, op, locked_rec, kills):
    kinds = {t["kind"] for t in kills["trials"]}
    deterministic = kinds == {"MID_COPY_PARTIAL"} and len({(t["targetState"], t["reason"]) for t in kills["trials"]}) == 1
    extra = ["PARTIAL_TARGET_AFTER_PROCESS_KILL_FINDING"] if kinds & {"PRE_COPY_ZERO_BYTE_TARGET", "MID_COPY_PARTIAL"} else []
    return {"scenarioId": sid, "subCase": "midCopyInterruptionOfProductionCall",
            "disposition": "MID_COPY_OBSERVED_DETERMINISTICALLY" if deterministic else NOT_INDUCIBLE,
            "reason": ("The production call runs one Connection.backup step with no owner-visible hook between pages; no packet-owned "
                       "interruption point exists. A real source lock fails before any copy starts (see sourceHeldExclusiveLock), and "
                       "killing the child after it creates the target lands at a timing-dependent point (see killTrials). No simulation "
                       "is offered as proof."),
            "realLockObservation": {"tag": locked_rec["tag"], "targetState": locked_rec["targetState"]["state"],
                                    "exception": locked_rec["outcome"]["exceptionClass"]},
            "killTrials": kills, "additionalFindingTags": extra,
            "tag": "MID_COPY_OBSERVED_FINDING" if deterministic else "MID_COPY_NOT_INDUCIBLE_FINDING"}

def scen_backup(ctx):
    recs, lives = [], []
    chain = build_chain(N, "bak")
    mk = lambda d: product_sqlite(d, "source", chain)
    for sidecar_only in (False, True):
        rec, src = _preexisting(ctx, "RH-BAK-F1", "backup", chain, mk, sidecar_only)
        recs.append(rec)
        lives.append(liveness(ctx, src, "RH-BAK-F1" + ("s" if sidecar_only else "f")))
    d = ctx.fresh("bak-f2")
    src = mk(d)
    locked = _locked(ctx, "RH-BAK-F2", "backup", chain, src, d)
    recs.append(locked)
    big = build_chain(LARGE_N, "kill")
    kd = ctx.fresh("kill-seed")
    seed = product_sqlite(kd, "seed", big)
    recs.append(_mid_copy_record(ctx, "RH-BAK-F2", "backup", locked, kill_trials(ctx, "backup", big, seed)))
    lives.append(liveness(ctx, src, "RH-BAK-F2"))
    d = ctx.fresh("bak-f3")
    src, tgt, inj = mk(d), d / "target.sqlite", {}
    with fault_connect(tgt, 1, "raise", inj):
        rec = run_case(ctx, "RH-BAK-F3", "afterCopyBeforeVerificationRead", "first ledger connect to the copied target", lambda: LEDGER(src).backup_to(tgt),
                       tgt, chain, {"source": src}, injection={"mechanism": "connect/raise", **inj})
    add_retry(ctx, rec, lambda: LEDGER(src).backup_to(tgt), tgt, chain)
    recs.append(rec)
    lives.append(liveness(ctx, src, "RH-BAK-F3"))
    return recs, lives

def _make_backup(d, chain):
    led = product_sqlite(d, "seed", chain)
    bak = d / "backup.sqlite"
    LEDGER(led).backup_to(bak)
    return bak

def _corrupt(bak, kind):
    conn = REAL_CONNECT(bak)
    try:
        if kind == "mutatedBlockHash":
            conn.execute("UPDATE blocks SET block_hash=? WHERE ordinal=6", ("0" * 64,))
        elif kind == "mutatedBlockBody":
            raw = conn.execute("SELECT block_json FROM blocks WHERE ordinal=6").fetchone()[0]
            blk = json.loads(raw)
            blk["event"]["n"] = 999
            conn.execute("UPDATE blocks SET block_json=? WHERE ordinal=6", (json.dumps(blk, sort_keys=True),))
        else:
            conn.execute("ALTER TABLE blocks RENAME COLUMN block_hash TO block_hash_x")
        conn.commit()
    finally:
        conn.close()

def scen_restore(ctx):
    recs, lives = [], []
    chain = build_chain(N, "res")
    d = ctx.fresh("res-f1")
    absent, tgt = d / "absent.sqlite", d / "target.sqlite"
    recs.append(run_case(ctx, "RH-RES-F1", "backupAbsent", "backup path does not exist", lambda: LEDGER.restore_backup(absent, tgt), tgt, chain, {},
                         retry=lambda: LEDGER.restore_backup(absent, tgt)))
    lives.append({"scenarioId": "RH-RES-F1", "applicable": False, "reason": "no source ledger exists in this scenario"})
    for kind in ("mutatedBlockHash", "mutatedBlockBody", "mutatedSchema"):
        d = ctx.fresh("res-f2")
        bak, tgt = _make_backup(d, chain), d / "target.sqlite"
        _corrupt(bak, kind)
        recs.append(run_case(ctx, "RH-RES-F2", kind, "corrupted backup passed to restore", lambda b=bak, t=tgt: LEDGER.restore_backup(b, t), tgt, chain,
                             {"backup": bak}, retry=lambda b=bak, t=tgt: LEDGER.restore_backup(b, t)))
        lives.append(liveness(ctx, bak, "RH-RES-F2-" + kind))
    d = ctx.fresh("res-f3")
    bak = _make_backup(d, chain)
    locked = _locked(ctx, "RH-RES-F3", "restore", chain, bak, d)
    recs.append(locked)
    big = build_chain(LARGE_N, "kill")
    seed_dir = ctx.fresh("kill-seed")
    recs.append(_mid_copy_record(ctx, "RH-RES-F3", "restore", locked, kill_trials(ctx, "restore", big, _make_backup(seed_dir, big))))
    lives.append(liveness(ctx, bak, "RH-RES-F3"))
    d = ctx.fresh("res-f4")
    bak, tgt, inj = _make_backup(d, chain), d / "target.sqlite", {}
    with fault_connect(tgt, 1, "raise", inj):
        rec = run_case(ctx, "RH-RES-F4", "afterCopyBeforeChainComparison", "first ledger connect to the restored target",
                       lambda: LEDGER.restore_backup(bak, tgt), tgt, chain, {"backup": bak}, injection={"mechanism": "connect/raise", **inj})
    add_retry(ctx, rec, lambda: LEDGER.restore_backup(bak, tgt), tgt, chain)
    recs.append(rec)
    lives.append(liveness(ctx, bak, "RH-RES-F4"))
    for sidecar_only in (False, True):
        rec, bak = _preexisting(ctx, "RH-RES-F5", "restore", chain, lambda d: _make_backup(d, chain), sidecar_only)
        recs.append(rec)
        lives.append(liveness(ctx, bak, "RH-RES-F5" + ("s" if sidecar_only else "f")))
    return recs, lives

def scen_concurrency(ctx):
    recs = []
    chain = build_chain(N, "conc")
    d = ctx.fresh("conc01")
    led, bak, rst = product_sqlite(d, "source", chain), d / "backup.sqlite", d / "restored.sqlite"
    ledger = LEDGER(led)
    res = run_barrier_peer(led, "peer-conc01", during=lambda: ledger.backup_to(bak))
    status, rows = raw_rows(led, ctx.scratch)
    final, _ = check_rows(rows) if status == "OK" else (None, "UNREADABLE")
    restored = run_case(ctx, "RH-CONC-01", "restoreOfBackup", "restore of the backup taken during the peer attempt", lambda: LEDGER.restore_backup(bak, rst), rst, chain,
                        {"backup": bak})
    ok = (res["orderVerdict"] == "ORDER_OK" and res["peerExit"] == 0 and classify(bak, chain, ctx.scratch)["state"] == "USABLE_COMPLETE"
          and final is not None and final[:N] == chain and len(final) == N + 1 and final[-1]["event"]["request_id"] == "peer-conc01"
          and restored["targetState"]["state"] == "USABLE_COMPLETE")
    recs.append({"scenarioId": "RH-CONC-01", "subCase": "backupWhileParentHoldsWriteGuardAndPeerAttempting", "orderVerdict": res["orderVerdict"],
                 "events": [{"event": n, "observedNs": t} for n, t in res["events"]], "peerEnteredNs": res["enteredNs"], "parentReleaseNs": res["releaseNs"],
                 "backupState": classify(bak, chain, ctx.scratch), "backupEqualsPreAppendChain": classify(bak, chain, ctx.scratch)["state"] == "USABLE_COMPLETE",
                 "finalSourceIsPreAppendChainPlusPeerBlock": bool(final and final[:N] == chain and len(final) == N + 1),
                 "restoreOfBackup": restored["targetState"]["state"], "ok": ok,
                 "tag": "PEER_DURING_BACKUP_OBSERVED_CONSISTENT" if ok else "PEER_DURING_BACKUP_INCONSISTENT_FINDING"})
    kd = ctx.fresh("conc02")
    trials = []
    for i in range(KILL_TRIALS):
        l2 = product_sqlite(kd, f"race{i}", chain)
        b2, lg = kd / f"race-backup-{i}.sqlite", LEDGER(l2)
        child = subprocess.Popen([sys.executable, str(PEER), str(l2), f"race-{i}"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True,
                                 cwd=str(ENGINE_DIR), env=peer_env())
        rd = LineReader(child.stdout)
        rd.get()
        child.stdin.write("START_ATTEMPT\n")
        child.stdin.flush()
        err = attempt(lambda: lg.backup_to(b2))["exceptionClass"]
        child.wait(timeout=60)
        st, rows = raw_rows(b2, ctx.scratch) if Path(b2).exists() else ("ABSENT", [])
        ch, _ = check_rows(rows) if st == "OK" else (None, st)
        trials.append({"trial": i + 1, "backupError": err, "backupBlocks": len(ch) if ch else None, "validChain": ch is not None, "consistentWithPeerOrder": bool(ch is not None and ch[:N] == chain[:len(ch)])})
    recs.append({"scenarioId": "RH-CONC-02", "subCase": "peerCommitBetweenBackupSteps", "disposition": NOT_INDUCIBLE,
                 "reason": "backup_to performs one Connection.backup step with no owner hook between steps, so a peer commit cannot be placed inside the copy "
                           "deterministically; the unordered race trials below are observation only.",
                 "raceTrials": trials, "tag": "PEER_COMMIT_BETWEEN_STEPS_NOT_INDUCIBLE_FINDING"})
    d = ctx.fresh("conc03")
    led3 = product_sqlite(d, "source", chain)
    mres = run_barrier_peer(led3, "peer-mutant", early=True)
    recs.append({"scenarioId": "RH-CONC-03", "subCase": "earlyEntryMutantThroughRealPeer", "orderVerdict": mres["orderVerdict"],
                 "oracleRejectedMutant": mres["orderVerdict"] == "REJECT_ENTRY_BEFORE_PARENT_RELEASE", "tag": "ORDERING_MUTANT_REJECTED"
                 if mres["orderVerdict"] == "REJECT_ENTRY_BEFORE_PARENT_RELEASE" else "ORDERING_MUTANT_ACCEPTED_FINDING"})
    return recs


# ---------------------------------------------------------------- driver
def collect_findings(items):
    found = []
    for r in items:
        for extra in r.get("additionalFindingTags", []):
            found.append({"scenarioId": r.get("scenarioId"), "subCase": r.get("subCase"), "tag": extra, "disposition": None, "flags": []})
        tag = r.get("tag", "")
        if tag.endswith("FINDING") or r.get("flags") or r.get("disposition") == NOT_INDUCIBLE:
            found.append({"scenarioId": r.get("scenarioId"), "subCase": r.get("subCase"), "tag": tag or r.get("disposition"),
                          "disposition": r.get("disposition"), "flags": r.get("flags", [])})
    return found

def run_all(execution_base):
    with DisposableRoot() as ctx:
        selfcheck = oracle_selfcheck(ctx)
        evidence = {"schemaVersion": SCHEMA_ID, "executionBaseHead": execution_base,
                    "probeSha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                    "parameters": {"N": N, "midInsertAfter": MID_INSERT_AFTER, "killTrials": KILL_TRIALS, "largeChainBlocks": LARGE_N},
                    "oracleSelfCheck": selfcheck}
        if selfcheck["allRejectedAndClassified"]:
            scenarios = scen_positive(ctx) + scen_import(ctx)
            b_recs, b_live = scen_backup(ctx)
            r_recs, r_live = scen_restore(ctx)
            scenarios += b_recs + r_recs + scen_concurrency(ctx)
            evidence.update({"scenarios": scenarios, "livenessAfterFaults": b_live + r_live, "findings": collect_findings(scenarios)})
        else:
            evidence.update({"scenarios": [], "blocked": "ORACLE_CANNOT_REJECT_A_MUTANT"})
    evidence.update({"disposableRoot": {"category": "IGNORED_RUNTIME_SCRATCH", "cleanup": ctx.cleanup},
                     "privateDataAccessed": "NONE", "providerCallCount": 0, "ownerFileEdited": False,
                     "claimBoundary": "Observations of induced synthetic cases only; no safety, durability or cutover claim."})
    return evidence

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output")
    ap.add_argument("--execution-base-head")
    ap.add_argument("--child-op", choices=("backup", "restore"))
    ap.add_argument("--source")
    ap.add_argument("--target")
    args = ap.parse_args()
    if args.child_op:
        _child(args.child_op, args.source, args.target)
        return 0
    base = args.execution_base_head or subprocess.run(["git", "rev-parse", "--short=9", "HEAD"], cwd=REPO_ROOT, capture_output=True,
                                                      text=True).stdout.strip()
    evidence = run_all(base)
    text = json.dumps(evidence, indent=2) + "\n"
    if args.output:
        Path(args.output).write_text(text, encoding="utf-8", newline="\n")
    tags = Counter(r.get("tag") or r.get("disposition") for r in evidence["scenarios"])
    print(json.dumps({"scenarios": len(evidence["scenarios"]), "tags": dict(tags), "findings": len(evidence.get("findings", [])),
                      "selfCheck": evidence["oracleSelfCheck"]["allRejectedAndClassified"], "cleanup": evidence["disposableRoot"]["cleanup"]}))
    return 0 if evidence["oracleSelfCheck"]["allRejectedAndClassified"] else 3


if __name__ == "__main__":
    raise SystemExit(main())
