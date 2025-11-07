import { command, query } from '$app/server';
import { employee } from '$lib/db/schema';
import { employeeInsertSchema, employeeSelectSchema, employeeUpdateSchema } from '$lib/db/types';
import { eq } from 'drizzle-orm';
import { getDB } from '../db';

export const getEmployees = query(async () => {
  const db = getDB();
  return await db.select().from(employee);
});

export const createEmployee = command(employeeInsertSchema, async (newEmployee) => {
  const db = getDB();

  const created = await db.insert(employee).values(newEmployee).returning();
  await getEmployees().refresh();

  return created[0];
});

export const updateEmployee = command(employeeUpdateSchema, async (updatedEmployee) => {
  const db = getDB();
  const updated = await db
    .update(employee)
    .set(updatedEmployee)
    .where(eq(employee.id, updatedEmployee.id!))
    .returning();

  await getEmployees().refresh();

  return updated[0];
});

export const deleteEmployee = command(employeeSelectSchema.entries.id, async (id) => {
  const db = getDB();
  await db.delete(employee).where(eq(employee.id, id));

  await getEmployees().refresh();
});
