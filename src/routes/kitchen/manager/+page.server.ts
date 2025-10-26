import { redirect } from '@sveltejs/kit';

export const load = () => {
  throw redirect(307, '/kitchen/manager/dashboard');
};
