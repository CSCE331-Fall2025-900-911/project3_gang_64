import { redirect } from '@sveltejs/kit';
import { localizeHref } from '$lib/i18n/runtime';
import type { LayoutServerLoad } from '../$types';

export const load: LayoutServerLoad = async (event) => {
  if (!event.locals.employee) {
    throw redirect(302, localizeHref('/auth/login'));
  }

  if (event.locals.employee.role !== 'manager') {
    throw redirect(302, localizeHref('/kitchen/cashier'));
  }

  return { employee: event.locals.employee };
};
