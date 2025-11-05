// +layout.server.ts
import { redirect } from '@sveltejs/kit';
import type { LayoutServerLoad } from './$types';

export const load: LayoutServerLoad = async (event) => {
  if (!event.locals.employee) {
    redirect(302, '/auth/login');
  }

  return { employee: event.locals.employee };
};
