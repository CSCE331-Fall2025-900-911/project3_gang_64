import { query } from '$app/server';
import type { Employee } from '$lib/types';
import { db } from '../database';

export const getEmployees = query<Employee[]>(async () => {
	const employees = await db.selectFrom('employee').selectAll().execute();

	return employees;
});
