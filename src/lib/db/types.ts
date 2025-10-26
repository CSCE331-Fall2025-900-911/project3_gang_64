import { createInsertSchema, createSelectSchema, createUpdateSchema } from 'drizzle-valibot';
import { employee } from './schema';

export const employeeSelectSchema = createSelectSchema(employee);
export const employeeUpdateSchema = createUpdateSchema(employee);
export const employeeInsertSchema = createInsertSchema(employee);
export type Employee = typeof employee.$inferSelect;
export type NewEmployee = typeof employee.$inferInsert;
