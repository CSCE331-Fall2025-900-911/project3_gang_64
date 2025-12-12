import { signIn } from '$lib/auth/auth';
import { localizeHref } from '$lib/i18n/runtime';
import { redirect } from '@sveltejs/kit';
import type { Actions, RequestEvent } from './$types';

export async function load(event: RequestEvent) {
  const session = await event.locals.auth();

  // If the user is already logged in, redirect to kitchen main page
  if (session?.user) {
    throw redirect(302, localizeHref('/kitchen'));
  }

  return {};
}

export const actions: Actions = { default: signIn };
