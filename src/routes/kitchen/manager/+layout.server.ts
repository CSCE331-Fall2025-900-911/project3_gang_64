import { redirect } from '@sveltejs/kit';
import type { LayoutServerLoad } from '../$types';

export const load: LayoutServerLoad = async (event) => {
  if (!event.locals.employee) {
    throw redirect(302, '/auth/login');
  }

  if (event.locals.employee.role !== 'manager') {
    throw redirect(302, '/kitchen/cashier');
  }

  return { employee: event.locals.employee };
};
