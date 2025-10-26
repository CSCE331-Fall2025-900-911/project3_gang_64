import { Role } from '$lib/types';
import { error } from '@sveltejs/kit';

export function authenticate(role: Role) {
  // const { cookies } = getRequestEvent();

  if (role != Role.ADMIN) error(403, 'Forbidden');
}
