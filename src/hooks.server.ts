import { redirect, type Handle } from '@sveltejs/kit';
import { handle as authenticationHandle } from './lib/auth/auth';
import { getDB } from './lib/db';
import { sequence } from '@sveltejs/kit/hooks';
import { employee } from '$lib/db/schema';
import { eq } from 'drizzle-orm';

async function authorizationHandle({ event, resolve }: Parameters<Handle>[0]) {
  // Protect any routes under /authenticated
  if (event.url.pathname.startsWith('/kitchen')) {
    const session = await event.locals.auth();
    if (!session || !session.user || !session.user.email) {
      // Redirect to the signin page
      throw redirect(303, '/login');
    }

    const db = getDB();
    try {
      const result = await db.select().from(employee).where(eq(employee.email, session.user.email)).limit(1);

      const isEmployee = result.length > 0;

      if (!isEmployee) {
        console.warn(`Attempted access by non-provisioned user: ${session.user.email}`);
        throw redirect(303, '/auth/unauthorized'); // Redirect to a dedicated unauthorized page
      }
    } catch (e) {
      console.error('Database query failed during authorization check:', e);
      if (e && typeof e === 'object' && 'status' in e && e.status === 303) {
        throw e;
      }
      throw redirect(303, 'auth/unauthorized');
    }
  }
  return resolve(event);
}

export const handle: Handle = sequence(authenticationHandle, authorizationHandle);
