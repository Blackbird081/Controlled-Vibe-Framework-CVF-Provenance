import { NextRequest, NextResponse } from 'next/server';
import { createHash } from 'node:crypto';
import { existsSync, readFileSync } from 'node:fs';
import { join, normalize } from 'node:path';
import type { CorpusManifest, IntakeReport } from '@/lib/lpci/types';

const REGISTRY_PATH = join(process.cwd(), '..', '..', '..', 'docs', 'corpus-intelligence', 'CVF_CORPUS_SCAN_REGISTRY.json');

const ALLOWED_DOCTYPE_ENUM = new Set([
  'law', 'decree', 'circular', 'policy', 'notice', 'decision', 'sop', 'contract', 'other',
]);

// NR-05: normalize path — root-relative, forward-slash, lowercase, no trailing/leading separator
function normalizePath(relativePath: string): string {
  return relativePath
    .replace(/\\/g, '/')
    .replace(/^\/+|\/+$/g, '')
    .toLowerCase();
}

function isCorpusRegistered(corpusId: string): boolean {
  try {
    const raw = readFileSync(REGISTRY_PATH, 'utf-8');
    const registry = JSON.parse(raw) as { corpora: Array<{ id: string }> };
    return registry.corpora.some((c) => c.id === corpusId);
  } catch {
    return false;
  }
}

export async function POST(request: NextRequest) {
  let body: unknown;
  try {
    body = await request.json();
  } catch {
    return NextResponse.json({ error: 'Invalid JSON body' }, { status: 400 });
  }

  const { corpusRoot, manifestPath } = body as { corpusRoot?: string; manifestPath?: string };

  if (!corpusRoot || !manifestPath) {
    return NextResponse.json({ error: 'corpusRoot and manifestPath are required' }, { status: 400 });
  }

  // GC-051: verify corpus is registered
  const manifestAbs = normalize(manifestPath);
  if (!existsSync(manifestAbs)) {
    return NextResponse.json({ error: 'manifestPath not found', receiptType: 'MANIFEST_NOT_FOUND' }, { status: 400 });
  }

  let manifest: CorpusManifest;
  try {
    manifest = JSON.parse(readFileSync(manifestAbs, 'utf-8')) as CorpusManifest;
  } catch {
    return NextResponse.json({ error: 'Failed to parse manifest JSON' }, { status: 400 });
  }

  if (!isCorpusRegistered(manifest.corpusId)) {
    return NextResponse.json({
      error: 'Corpus not registered in GC-051 registry',
      receiptType: 'NOT_REGISTERED',
      corpusId: manifest.corpusId,
    }, { status: 403 });
  }

  const gaps: string[] = [];
  let hashMode = 'per-file';

  if (manifest.manifestHashProxy) {
    hashMode = `manifest-proxy: ${manifest.manifestProxyException ?? 'no exception documented'}`;
    if (!manifest.manifestProxyException) {
      gaps.push('NR-04: manifestHashProxy=true but manifestProxyException not documented');
    }
  }

  const intakeRows: Array<{ normalizedPath: string; sourceHash: string; documentType: string; gap?: string }> = [];

  for (const entry of manifest.files ?? []) {
    const normalizedPath = normalizePath(entry.relativePath);
    const absPath = join(corpusRoot, entry.relativePath);

    // NR-04: compute hash or accept proxy
    let sourceHash: string;
    if (manifest.manifestHashProxy && manifest.manifestProxyException) {
      sourceHash = entry.hash ?? 'PROXY';
    } else {
      if (existsSync(absPath)) {
        const bytes = readFileSync(absPath);
        sourceHash = createHash('sha256').update(bytes).digest('hex');
      } else {
        sourceHash = 'FILE_NOT_FOUND';
        gaps.push(`NR-04: file not found at ${absPath}`);
      }
    }

    // documentType validation
    const docType = (entry.documentType ?? '').toLowerCase();
    if (!ALLOWED_DOCTYPE_ENUM.has(docType)) {
      gaps.push(`documentType '${entry.documentType}' not in allowed enum for ${normalizedPath}`);
    }

    intakeRows.push({ normalizedPath, sourceHash, documentType: entry.documentType });
  }

  const report: IntakeReport = {
    rowCount: intakeRows.length,
    gaps,
    sourceHashSummary: hashMode,
  };

  return NextResponse.json(report);
}
