import { createInsertSchema, createSelectSchema, createUpdateSchema } from 'drizzle-valibot';
import { customer, employee, ingredient, menu, order, orderContent, paymethod, recipe } from './schema';

export const employeeSelectSchema = createSelectSchema(employee);
export const employeeUpdateSchema = createUpdateSchema(employee);
export const employeeInsertSchema = createInsertSchema(employee);
export type Employee = typeof employee.$inferSelect;
export type NewEmployee = typeof employee.$inferInsert;

export const BlankEmployee: NewEmployee = {
  name: '',
  email: '',
  role: 'staff',
  archived: false,
};

export const menuItemSelectSchema = createSelectSchema(menu);
export const menuItemUpdateSchema = createUpdateSchema(menu);
export const menuItemInsertSchema = createInsertSchema(menu);
export type MenuItem = typeof menu.$inferSelect;
export type NewMenuItem = typeof menu.$inferInsert;

export const recipeSelectSchema = createSelectSchema(recipe);
export const recipeUpdateSchema = createUpdateSchema(recipe);
export const recipeInsertSchema = createInsertSchema(recipe);
export type Recipe = typeof recipe.$inferSelect;
export type NewRecipe = typeof recipe.$inferInsert;

export const ingredientSelectSchema = createSelectSchema(ingredient);
export const ingredientUpdateSchema = createUpdateSchema(ingredient);
export const ingredientInsertSchema = createInsertSchema(ingredient);
export type Ingredient = typeof ingredient.$inferSelect;
export type NewIngredient = typeof ingredient.$inferInsert;

export const BlankIngredient: NewIngredient = {
  name: '',
  currentStock: 0,
  orderStock: 0,
  category: '',
  unitPrice: 0,
};

export const customerSelectSchema = createSelectSchema(customer);
export const customerUpdateSchema = createUpdateSchema(customer);
export const customerInsertSchema = createInsertSchema(customer);
export type Customer = typeof customer.$inferSelect;
export type NewCustomer = typeof customer.$inferInsert;

export const orderContentSelectSchema = createSelectSchema(orderContent);
export const orderContentUpdateSchema = createUpdateSchema(orderContent);
export const orderContentInsertSchema = createInsertSchema(orderContent);
export type OrderContent = typeof orderContent.$inferSelect;
export type NewOrderContent = typeof orderContent.$inferInsert;

export const orderSelectSchema = createSelectSchema(order);
export const orderUpdateSchema = createUpdateSchema(order);
export const orderInsertSchema = createInsertSchema(order);
export type Order = typeof order.$inferSelect;
export type NewOrder = typeof order.$inferInsert;

export type PaymentMethod = (typeof paymethod.enumValues)[number];

export type CreateOrUpdate<T> = { type: 'new' } | { type: 'edit'; item: T };
