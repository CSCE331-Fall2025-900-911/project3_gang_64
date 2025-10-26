import { relations } from 'drizzle-orm/relations';
import { customer, employee, ingredient, menu, order, orderContent, recipe } from './schema';

export const orderRelations = relations(order, ({ one, many }) => ({
  customer: one(customer, {
    fields: [order.customerId],
    references: [customer.id],
  }),
  employee: one(employee, {
    fields: [order.employeeId],
    references: [employee.id],
  }),
  orderContents: many(orderContent),
}));

export const customerRelations = relations(customer, ({ many }) => ({
  orders: many(order),
}));

export const employeeRelations = relations(employee, ({ many }) => ({
  orders: many(order),
}));

export const orderContentRelations = relations(orderContent, ({ one }) => ({
  order: one(order, {
    fields: [orderContent.orderId],
    references: [order.id],
  }),
  menu: one(menu, {
    fields: [orderContent.menuItemId],
    references: [menu.id],
  }),
  ingredient: one(ingredient, {
    fields: [orderContent.ingredientId],
    references: [ingredient.id],
  }),
}));

export const menuRelations = relations(menu, ({ many }) => ({
  orderContents: many(orderContent),
  recipes: many(recipe),
}));

export const ingredientRelations = relations(ingredient, ({ many }) => ({
  orderContents: many(orderContent),
  recipes: many(recipe),
}));

export const recipeRelations = relations(recipe, ({ one }) => ({
  menu: one(menu, {
    fields: [recipe.menuItemId],
    references: [menu.id],
  }),
  ingredient: one(ingredient, {
    fields: [recipe.ingredientId],
    references: [ingredient.id],
  }),
}));
