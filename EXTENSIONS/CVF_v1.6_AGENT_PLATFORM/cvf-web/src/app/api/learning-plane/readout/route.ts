import { NextRequest, NextResponse } from 'next/server';
import {
  buildFindingToLearningRecord,
  FINDING_TO_LEARNING_BRIDGE_VERSION,
  type FindingToLearningInput,
} from '@/lib/finding-to-learning-bridge';
import { verifyServiceTokenRequest } from '@/lib/service-token-auth';
import { verifySessionCookie } from '@/lib/middleware-auth';

export const LEARNING_PLANE_READOUT_ROUTE_VERSION =
  "cvf.learningPlaneReadoutRoute.rt3.v1";

function extractBody(raw: unknown): FindingToLearningInput | null {
  if (!raw || typeof raw !== 'object') return null;
  const b = raw as Record<string, unknown>;
  if (
    typeof b.sourceId !== 'string' ||
    typeof b.sourceArtifact !== 'string' ||
    typeof b.sourceSummary !== 'string' ||
    typeof b.lane !== 'string' ||
    typeof b.defectClass !== 'string' ||
    typeof b.severity !== 'string' ||
    typeof b.disposition !== 'string' ||
    typeof b.nextControlAction !== 'string' ||
    typeof b.evidenceBasis !== 'string'
  ) return null;
  return b as unknown as FindingToLearningInput;
}

export async function POST(request: NextRequest) {
  // Auth: service token or session
  const serviceToken = request.headers.get('x-cvf-service-token');
  const signature = request.headers.get('x-cvf-service-signature');
  const timestamp = request.headers.get('x-cvf-service-timestamp');

  let bodyText: string;
  try {
    bodyText = await request.text();
  } catch {
    return NextResponse.json({ success: false, error: 'Invalid request body.' }, { status: 400 });
  }

  const configuredToken = process.env.CVF_SERVICE_TOKEN;
  const isServiceAllowed = verifyServiceTokenRequest({
    configuredToken,
    presentedToken: serviceToken,
    signature,
    timestamp,
    body: bodyText,
  });

  const session = await verifySessionCookie(request);

  if (!session && !isServiceAllowed) {
    return NextResponse.json(
      { success: false, error: 'Unauthorized: please login or provide a valid service token.' },
      { status: 401 },
    );
  }

  let raw: unknown;
  try {
    raw = JSON.parse(bodyText);
  } catch {
    return NextResponse.json({ success: false, error: 'Invalid JSON body.' }, { status: 400 });
  }

  const input = extractBody(raw);
  if (!input) {
    return NextResponse.json(
      {
        success: false,
        error: 'Missing required fields: sourceId, sourceArtifact, sourceSummary, lane, defectClass, severity, disposition, nextControlAction, evidenceBasis.',
      },
      { status: 400 },
    );
  }

  const record = buildFindingToLearningRecord(input);

  return NextResponse.json({
    success: true,
    routeVersion: LEARNING_PLANE_READOUT_ROUTE_VERSION,
    bridgeVersion: FINDING_TO_LEARNING_BRIDGE_VERSION,
    findingToLearningReadout: record,
  });
}
