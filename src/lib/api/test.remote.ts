import { query } from '$app/server';
import { getDB } from '$lib/database';
import { Role, type Employee } from '$lib/types';
import { authenticate } from './utils';

export const getEmployees = query<Employee[]>(async () => {
  const db = getDB();
  authenticate(Role.USER);
  const employees = await db.selectFrom('employee').selectAll().execute();

  return employees;
});
