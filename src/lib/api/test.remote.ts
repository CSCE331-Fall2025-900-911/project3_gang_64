import { query } from '$app/server';
import { getDB } from '$lib/database';
import { type Employee } from '$lib/types';

export const getEmployees = query<Employee[]>(async () => {
  const db = getDB();
  const employees = await db.selectFrom('employee').selectAll().execute();

  return employees;
});
