/** Explicit-root private immutable artifact adapter; no default directory or runtime activation.
 * Trusted single host/root owner only. Mode bits are not Windows ACL enforcement.
 * File flush and no-replace publication do not promise directory/power-loss durability.
 */
import * as fs from 'node:fs/promises';
import { createHash, randomUUID } from 'node:crypto';
import path from 'node:path';
import { assertCurrentIntentSpecActor, type IntentSpecActor } from './intent-spec-actor';
import { prepareIntentSpecAcceptance, type IntentSpecAcceptanceStorePort } from './intent-spec-acceptance';
import { MAX_CONFIRMATION_BYTES } from './intent-spec-confirmation';

const MAX_RECORD_BYTES = MAX_CONFIRMATION_BYTES * 3 + 8192;
const HASH = /^[a-f0-9]{64}$/;
const sha = (bytes: Uint8Array) => createHash('sha256').update(bytes).digest('hex');
const samePath = (left: string, right: string) => path.relative(left, right) === '';
const codeOf = (error: unknown) => (error as NodeJS.ErrnoException)?.code;

/** Create only for an existing, explicitly selected private root; no implicit .data store. */
export class FileIntentSpecAcceptanceStore implements IntentSpecAcceptanceStorePort {
    readonly namespace: string;
    private readonly root: string;

    constructor(root: string, private readonly actor: IntentSpecActor, private readonly clock: () => number = Date.now) {
        assertCurrentIntentSpecActor(actor, clock());
        if (!path.isAbsolute(root) || root.startsWith('\\\\') || samePath(path.resolve(root), path.parse(root).root)) {
            throw new Error('EXPLICIT_PRIVATE_ROOT_REQUIRED');
        }
        this.root = path.resolve(root);
        this.namespace = sha(new TextEncoder().encode(JSON.stringify({
            userId: actor.userId, orgId: actor.orgId, teamId: actor.teamId,
        })));
        Object.freeze(this);
    }

    private async directory(create: boolean): Promise<string | null> {
        assertCurrentIntentSpecActor(this.actor, this.clock());
        const rootStat = await fs.lstat(this.root);
        if (!rootStat.isDirectory() || rootStat.isSymbolicLink() || !samePath(await fs.realpath(this.root), this.root)) {
            throw new Error('UNSAFE_PRIVATE_ROOT');
        }
        const directory = path.join(this.root, this.namespace);
        if (create) {
            try { await fs.mkdir(directory, { mode: 0o700 }); }
            catch (error) { if (codeOf(error) !== 'EEXIST') throw error; }
        }
        let stat;
        try { stat = await fs.lstat(directory); }
        catch (error) { if (!create && codeOf(error) === 'ENOENT') return null; throw error; }
        if (!stat.isDirectory() || stat.isSymbolicLink() || !samePath(await fs.realpath(directory), directory)) {
            throw new Error('UNSAFE_ACTOR_NAMESPACE');
        }
        return directory;
    }

    private validate(id: string, input: Uint8Array, write: boolean): void {
        if (!HASH.test(id) || !input.byteLength || input.byteLength > MAX_RECORD_BYTES || sha(input) !== id) {
            throw new Error('INVALID_STORED_SPEC_RECORD');
        }
        const text = new TextDecoder('utf-8', { fatal: true, ignoreBOM: true }).decode(input);
        const record = JSON.parse(text);
        const keys = ['schema', 'state', 'scope', 'actor', 'preparedAt', 'sourceFileSha256', 'sourceFile'];
        if (!record || typeof record !== 'object' || Array.isArray(record)
            || Object.keys(record).length !== keys.length || !keys.every(key => Object.hasOwn(record, key))
            || JSON.stringify(record) + '\n' !== text
            || record.schema !== 'cvf.intentSpecAcceptanceCandidate.v1' || record.state !== 'PENDING_STORE_COMMIT'
            || record.scope !== 'SPEC_REVIEW_ONLY_NO_BUILD_AUTHORITY'
            || typeof record.preparedAt !== 'string' || !Number.isFinite(Date.parse(record.preparedAt))
            || new Date(record.preparedAt).toISOString() !== record.preparedAt
            || typeof record.sourceFile !== 'string') throw new Error('INVALID_STORED_SPEC_RECORD');
        const actor = record.actor;
        const actorKeys = ['userId', 'orgId', 'teamId', 'role', 'assurance'];
        if (!actor || typeof actor !== 'object' || Array.isArray(actor)
            || Object.keys(actor).length !== actorKeys.length || !actorKeys.every(key => Object.hasOwn(actor, key))
            || actor.userId !== this.actor.userId || actor.orgId !== this.actor.orgId || actor.teamId !== this.actor.teamId
            || !['owner', 'admin', 'developer', 'reviewer'].includes(actor.role)
            || !['LOCAL_TEST_SESSION', 'EXISTING_AUTH_JS_OWNER'].includes(actor.assurance)
            || (write && JSON.stringify(actor) !== JSON.stringify(this.actor))) {
            throw new Error('STORED_SPEC_ACTOR_MISMATCH');
        }
        // Reuse existing source admission; a renamed/tampered file cannot bypass its parser.
        prepareIntentSpecAcceptance(this.actor, new TextEncoder().encode(record.sourceFile), record.sourceFileSha256, this.clock());
    }

    async read(id: string): Promise<Uint8Array | null> {
        if (!HASH.test(id)) throw new Error('INVALID_STORED_SPEC_RECORD');
        const directory = await this.directory(false);
        if (!directory) return null;
        const file = path.join(directory, `${id}.json`);
        let stat;
        try { stat = await fs.lstat(file); }
        catch (error) { if (codeOf(error) === 'ENOENT') return null; throw error; }
        if (!stat.isFile() || stat.isSymbolicLink() || stat.size > MAX_RECORD_BYTES) throw new Error('UNSAFE_SPEC_RECORD');
        const handle = await fs.open(file, 'r');
        let bytes: Uint8Array;
        try {
            const opened = await handle.stat();
            if (!opened.isFile() || opened.size > MAX_RECORD_BYTES) throw new Error('UNSAFE_SPEC_RECORD');
            bytes = new Uint8Array(await handle.readFile());
        } finally { await handle.close(); }
        this.validate(id, bytes, false);
        assertCurrentIntentSpecActor(this.actor, this.clock());
        return bytes;
    }

    async createIfAbsent(id: string, input: Uint8Array): Promise<void> {
        if (!ArrayBuffer.isView(input) || input.byteLength > MAX_RECORD_BYTES) throw new Error('INVALID_STORED_SPEC_RECORD');
        const bytes = new Uint8Array(input);
        this.validate(id, bytes, true);
        const directory = (await this.directory(true))!;
        const existing = await this.read(id);
        if (existing) {
            if (!existing.every((byte, index) => byte === bytes[index]) || existing.length !== bytes.length) throw new Error('SPEC_RECORD_CONFLICT');
            return;
        }
        const temporary = path.join(directory, `.pending-${randomUUID()}`);
        const final = path.join(directory, `${id}.json`);
        let handle: Awaited<ReturnType<typeof fs.open>> | undefined;
        let owned = false;
        try {
            handle = await fs.open(temporary, 'wx', 0o600); owned = true;
            await handle.writeFile(bytes); await handle.sync(); await handle.close(); handle = undefined;
            assertCurrentIntentSpecActor(this.actor, this.clock());
            try { await fs.link(temporary, final); }
            catch (error) { if (codeOf(error) !== 'EEXIST') throw error; }
            const stored = await this.read(id);
            if (!stored || stored.length !== bytes.length || !stored.every((byte, index) => byte === bytes[index])) {
                throw new Error('SPEC_RECORD_CONFLICT');
            }
        } finally {
            try { await handle?.close(); }
            finally { if (owned) await fs.unlink(temporary); }
        }
    }
}
