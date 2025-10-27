import { createInsertSchema, createSelectSchema, createUpdateSchema } from 'drizzle-valibot';
import { employee, menu } from './schema';

export const employeeSelectSchema = createSelectSchema(employee);
export const employeeUpdateSchema = createUpdateSchema(employee);
export const employeeInsertSchema = createInsertSchema(employee);
export type Employee = typeof employee.$inferSelect;
export type NewEmployee = typeof employee.$inferInsert;

export const menuItemSelectSchema = createSelectSchema(menu);
export const menuItemUpdateSchema = createUpdateSchema(menu);
export const menuItemInsertSchema = createInsertSchema(menu);
export type MenuItem = typeof menu.$inferSelect;
export type NewMenuItem = typeof menu.$inferInsert;
