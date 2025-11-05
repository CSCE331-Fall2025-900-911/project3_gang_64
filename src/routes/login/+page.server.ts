import { redirect } from '@sveltejs/kit';

import type { RequestEvent } from './$types';

export async function load(event: RequestEvent) {
  const session = await event.locals.auth();

  if (session !== null && session.user !== null) {
    return redirect(302, '/');
  }
  return {};
}
