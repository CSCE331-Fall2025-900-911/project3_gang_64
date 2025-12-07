// +layout.server.ts
import { redirect } from '@sveltejs/kit';
import { localizeHref } from '$lib/i18n/runtime';
import type { LayoutServerLoad } from './$types';

export const load: LayoutServerLoad = async (event) => {
  if (!event.locals.employee) {
    redirect(302, localizeHref('/auth/login'));
  }

  return { employee: event.locals.employee };
};
