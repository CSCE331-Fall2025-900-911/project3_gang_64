import type { LayoutServerLoad } from './$types';

export const ssr = false;
export const load: LayoutServerLoad = async (event) => {
  return {
    employee: event.locals.employee,
    translations: event.locals.translations,
  };
};
