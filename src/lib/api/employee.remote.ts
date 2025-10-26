import { command, query } from '$app/server';
import { employee } from '$lib/db/schema';
import { employeeInsertSchema, employeeSelectSchema, type Employee, type NewEmployee } from '$lib/db/types';
import { eq } from 'drizzle-orm';
import { getDB } from '../db';

export const getEmployees = query<Employee[]>(async () => {
  const db = getDB();
  return await db.select().from(employee);
});

export const createEmployee = command(employeeInsertSchema, async (newEmployee: NewEmployee) => {
  const db = getDB();

  const created = await db.insert(employee).values(newEmployee).returning();
  getEmployees().refresh();

  return created[0];
});

export const deleteEmployee = command(employeeSelectSchema.entries.id, async (id) => {
  const db = getDB();
  await db.delete(employee).where(eq(employee.id, id));

  getEmployees().refresh();
});
