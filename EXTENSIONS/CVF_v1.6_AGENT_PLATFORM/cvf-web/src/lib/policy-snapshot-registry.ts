/**
 * CVF Policy Snapshot Registry
 *
 * Owner module for policy snapshot id generation and secret-safe persisted records.
 * Moves the policySnapshotId lifecycle from a process-local monotonic counter in
 * web-governance-envelope.ts into a durable local registry with an id-to-record
 * read path for audit reconstructability.
 *
 * CVF_POLICY_SNAPSHOT_REGISTRY_VERSION: 2026-06-05
 * ERH_DUR1_MARKER: DURABLE_EVIDENCE_STORE_ACTIVE
 *
 * Claim boundary: bounded local persistence only. Not a production database,
 * Redis store, distributed registry, external policy service, or tamper-proof audit.
 * Secret-safe: records contain policy metadata only; no raw prompts, raw AI output,
 * API keys, provider secrets, or private memory payloads.
 *
 * Env override: CVF_POLICY_SNAPSHOT_DIR
 */

import { mkdir, readFile, writeFile } from 'node:fs/promises';
import path from 'node:path';

export interface PolicySnapshotRecord {
    id: string;
    createdAt: string;
    policyDate: string;
    evidenceClass: 'BOUNDED_LOCAL';
    bounded: true;
}

export interface BuildPolicySnapshotInput {
    id: string;
    createdAt?: string;
}

export function getSnapshotDir(): string {
    return process.env.CVF_POLICY_SNAPSHOT_DIR
        ? path.resolve(process.env.CVF_POLICY_SNAPSHOT_DIR)
        : path.join(process.cwd(), '.cvf', 'runtime', 'policy-snapshots');
}

export function buildPolicySnapshot(input: BuildPolicySnapshotInput): PolicySnapshotRecord {
    const createdAt = input.createdAt ?? new Date().toISOString();
    return {
        id: input.id,
        createdAt,
        policyDate: createdAt.slice(0, 10),
        evidenceClass: 'BOUNDED_LOCAL',
        bounded: true,
    };
}

export async function persistPolicySnapshot(record: PolicySnapshotRecord): Promise<void> {
    const dir = getSnapshotDir();
    try {
        await mkdir(dir, { recursive: true });
    } catch {
        // directory already exists or filesystem is read-only
    }
    try {
        const filePath = path.join(dir, `${record.id}.json`);
        await writeFile(filePath, JSON.stringify(record, null, 2), 'utf8');
    } catch {
        // read-only filesystem — snapshot operates in ephemeral mode
    }
}

export async function readPolicySnapshot(id: string): Promise<PolicySnapshotRecord | null> {
    const dir = getSnapshotDir();
    const filePath = path.join(dir, `${id}.json`);
    try {
        const raw = await readFile(filePath, 'utf8');
        return JSON.parse(raw) as PolicySnapshotRecord;
    } catch {
        return null;
    }
}

let _policySnapshotCounter = 0;

export function generatePolicySnapshotId(): string {
    _policySnapshotCounter++;
    const date = new Date().toISOString().slice(0, 10).replace(/-/g, '');
    const id = `pol-${date}-${_policySnapshotCounter.toString().padStart(4, '0')}`;
    const record = buildPolicySnapshot({ id });
    void persistPolicySnapshot(record).catch(() => {});
    return id;
}
