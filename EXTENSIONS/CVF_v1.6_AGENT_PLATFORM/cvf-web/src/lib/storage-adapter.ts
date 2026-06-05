/**
 * CVF Storage Adapter
 *
 * Pluggable storage adapter interface for CVF durable evidence and snapshot stores.
 * DUR2 extends DUR1 by making the I/O backend selectable via CVF_STORAGE_ADAPTER_TYPE:
 *   - FileEventListAdapter / FileKeyValueAdapter: wraps DUR1 file-backed I/O (default)
 *   - RedisEventListAdapter / RedisKeyValueAdapter: stubs for future Redis backend
 *
 * ERH_DUR2_MARKER: EXTERNAL_STORAGE_ADAPTER_ACTIVE
 * CVF_STORAGE_ADAPTER_VERSION: 2026-06-05
 *
 * Claim boundary: adapter interface contract and file-backed implementation only.
 * Redis stubs throw CVF_NOT_IMPLEMENTED. No live Redis connection, production
 * database, distributed durability, or tamper-proof audit is claimed.
 *
 * Env: CVF_STORAGE_ADAPTER_TYPE — 'file' (default) | 'redis' (stub only)
 * Secret-safe: adapters carry structured governance records only; raw prompts,
 * raw AI output, API keys, provider secrets, and private memory payloads are
 * forbidden from adapter records.
 */

import { mkdir, readFile, writeFile } from 'node:fs/promises';
import path from 'node:path';

// ─── Interfaces ────────────────────────────────────────────────────────────────

/**
 * Adapter for list-backed stores (e.g. control-plane event store).
 * All operations target a single named store key (file path or Redis key prefix).
 */
export interface EventListAdapter<T = unknown> {
  readonly adapterType: string;
  /** Ensure the store exists and is initialized. */
  init(storeKey: string): Promise<void>;
  /** Read all items. Returns [] if store is empty or unreadable. */
  readAll(storeKey: string): Promise<T[]>;
  /** Replace all items in the store. */
  writeAll(storeKey: string, items: T[]): Promise<void>;
  /** Write raw string content (used internally for corruption repair). */
  writeRaw(storeKey: string, content: string): Promise<void>;
}

/**
 * Adapter for key-value stores (e.g. policy snapshot registry).
 * Items are addressed by (dir, id) pair.
 */
export interface KeyValueAdapter<T = unknown> {
  readonly adapterType: string;
  /** Write an item by ID within a named directory/namespace. */
  write(dir: string, id: string, item: T): Promise<void>;
  /** Read an item by ID. Returns null if not found. */
  read(dir: string, id: string): Promise<T | null>;
}

// ─── File Implementations ──────────────────────────────────────────────────────

function findTopLevelArrayEnd(raw: string): number | null {
  let depth = 0;
  let inString = false;
  let escaped = false;

  for (let index = 0; index < raw.length; index += 1) {
    const char = raw[index];

    if (inString) {
      if (escaped) { escaped = false; continue; }
      if (char === '\\') { escaped = true; continue; }
      if (char === '"') { inString = false; }
      continue;
    }

    if (char === '"') { inString = true; continue; }
    if (char === '[') { depth += 1; continue; }
    if (char === ']') {
      depth -= 1;
      if (depth === 0) return index;
    }
  }

  return null;
}

export class FileEventListAdapter<T = unknown> implements EventListAdapter<T> {
  readonly adapterType = 'file';

  async init(storeKey: string): Promise<void> {
    try {
      await mkdir(path.dirname(storeKey), { recursive: true });
    } catch {
      // directory already exists or filesystem is read-only
    }
    try {
      await readFile(storeKey, 'utf8');
    } catch {
      try {
        await writeFile(storeKey, '[]', 'utf8');
      } catch {
        // read-only filesystem — store operates in ephemeral mode
      }
    }
  }

  async readAll(storeKey: string): Promise<T[]> {
    await this.init(storeKey);
    let raw: string;
    try {
      raw = await readFile(storeKey, 'utf8');
    } catch {
      return [];
    }
    try {
      return JSON.parse(raw) as T[];
    } catch {
      return this._repair(raw, storeKey);
    }
  }

  async writeAll(storeKey: string, items: T[]): Promise<void> {
    await this.init(storeKey);
    await writeFile(storeKey, JSON.stringify(items, null, 2), 'utf8');
  }

  async writeRaw(storeKey: string, content: string): Promise<void> {
    try {
      await mkdir(path.dirname(storeKey), { recursive: true });
    } catch {
      // directory exists or read-only
    }
    await writeFile(storeKey, content, 'utf8');
  }

  private async _repair(raw: string, storeKey: string): Promise<T[]> {
    const arrayEnd = findTopLevelArrayEnd(raw);
    if (arrayEnd === null) {
      await this.writeRaw(storeKey, '[]');
      return [];
    }
    const recoveredRaw = raw.slice(0, arrayEnd + 1);
    try {
      const recovered = JSON.parse(recoveredRaw) as T[];
      const backupPath = `${storeKey}.corrupt-${Date.now()}.json`;
      await this.writeRaw(backupPath, raw);
      await this.writeRaw(storeKey, JSON.stringify(recovered, null, 2));
      return recovered;
    } catch {
      await this.writeRaw(storeKey, '[]');
      return [];
    }
  }
}

export class FileKeyValueAdapter<T = unknown> implements KeyValueAdapter<T> {
  readonly adapterType = 'file';

  async write(dir: string, id: string, item: T): Promise<void> {
    try {
      await mkdir(dir, { recursive: true });
    } catch {
      // directory already exists or filesystem is read-only
    }
    try {
      await writeFile(path.join(dir, `${id}.json`), JSON.stringify(item, null, 2), 'utf8');
    } catch {
      // read-only filesystem — snapshot operates in ephemeral mode
    }
  }

  async read(dir: string, id: string): Promise<T | null> {
    try {
      const raw = await readFile(path.join(dir, `${id}.json`), 'utf8');
      return JSON.parse(raw) as T;
    } catch {
      return null;
    }
  }
}

// ─── Redis Stubs ───────────────────────────────────────────────────────────────

const CVF_NOT_IMPLEMENTED =
  'CVF_NOT_IMPLEMENTED: RedisStorageAdapter is a stub only. ' +
  'Set CVF_STORAGE_ADAPTER_TYPE=file or leave unset to use the file-backed adapter.';

export class RedisEventListAdapter<T = unknown> implements EventListAdapter<T> {
  readonly adapterType = 'redis';

  async init(_storeKey: string): Promise<void> {
    throw new Error(CVF_NOT_IMPLEMENTED);
  }

  async readAll(_storeKey: string): Promise<T[]> {
    throw new Error(CVF_NOT_IMPLEMENTED);
  }

  async writeAll(_storeKey: string, _items: T[]): Promise<void> {
    throw new Error(CVF_NOT_IMPLEMENTED);
  }

  async writeRaw(_storeKey: string, _content: string): Promise<void> {
    throw new Error(CVF_NOT_IMPLEMENTED);
  }
}

export class RedisKeyValueAdapter<T = unknown> implements KeyValueAdapter<T> {
  readonly adapterType = 'redis';

  async write(_dir: string, _id: string, _item: T): Promise<void> {
    throw new Error(CVF_NOT_IMPLEMENTED);
  }

  async read(_dir: string, _id: string): Promise<T | null> {
    throw new Error(CVF_NOT_IMPLEMENTED);
  }
}

// ─── Factories ─────────────────────────────────────────────────────────────────

export function buildEventListAdapter<T = unknown>(type?: string): EventListAdapter<T> {
  const resolved = type ?? process.env.CVF_STORAGE_ADAPTER_TYPE ?? 'file';
  if (resolved === 'file') return new FileEventListAdapter<T>();
  if (resolved === 'redis') return new RedisEventListAdapter<T>();
  throw new Error(
    `CVF_CONFIGURATION_ERROR: unknown CVF_STORAGE_ADAPTER_TYPE "${resolved}". ` +
    'Supported values: file, redis.',
  );
}

export function buildKeyValueAdapter<T = unknown>(type?: string): KeyValueAdapter<T> {
  const resolved = type ?? process.env.CVF_STORAGE_ADAPTER_TYPE ?? 'file';
  if (resolved === 'file') return new FileKeyValueAdapter<T>();
  if (resolved === 'redis') return new RedisKeyValueAdapter<T>();
  throw new Error(
    `CVF_CONFIGURATION_ERROR: unknown CVF_STORAGE_ADAPTER_TYPE "${resolved}". ` +
    'Supported values: file, redis.',
  );
}
