import type { NextRequest } from 'next/server';
import { draftRouteHandlers } from '@/lib/server/html-draft-recovery-api';

export async function POST(request: NextRequest) { return draftRouteHandlers().POST(request); }
export async function GET(request: NextRequest) { return draftRouteHandlers().GET(request); }
