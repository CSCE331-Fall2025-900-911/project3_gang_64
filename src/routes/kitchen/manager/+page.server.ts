import { redirect } from '@sveltejs/kit';
import { localizeHref } from '$lib/i18n/runtime';

export const load = () => {
  throw redirect(307, localizeHref('/kitchen/manager/dashboard'));
};
