// +layout.server.ts
import { localizeHref } from '$lib/i18n/runtime';
import { redirect } from '@sveltejs/kit';
import type { LayoutServerLoad } from './$types';

export const load: LayoutServerLoad = async (event) => {
  if (!event.locals.employee) {
    throw redirect(302, localizeHref('/auth/login'));
  }

  return { employee: event.locals.employee };
};
