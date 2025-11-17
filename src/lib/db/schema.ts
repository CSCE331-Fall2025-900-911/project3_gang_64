import { sql } from 'drizzle-orm';
import {
  boolean,
  doublePrecision,
  foreignKey,
  integer,
  pgEnum,
  pgTable,
  timestamp,
  uuid,
  varchar,
} from 'drizzle-orm/pg-core';
import { v4 as uuidv4 } from 'uuid';

export const paymethod = pgEnum('paymethod', ['cash', 'credit']);
export const role = pgEnum('role', ['manager', 'staff']);

export const menu = pgTable('menu', {
  id: uuid('id').$defaultFn(uuidv4).primaryKey().notNull(),
  name: varchar({ length: 100 }).notNull(),
  category: varchar({ length: 100 }).notNull(),
  price: doublePrecision().notNull(),
  imageUrl: varchar({ length: 255 }),
  archived: boolean().default(false).notNull(),
});

export const customer = pgTable('customer', {
  id: uuid('id').$defaultFn(uuidv4).primaryKey().notNull(),
  name: varchar({ length: 100 }).notNull(),
  email: varchar({ length: 100 }).notNull().unique(),
});

export const order = pgTable(
  'order',
  {
    id: uuid('id').$defaultFn(uuidv4).primaryKey().notNull(),
    customerId: uuid('customer_id').notNull(),
    employeeId: uuid('employee_id'),
    subtotal: doublePrecision().notNull(),
    tax: doublePrecision().notNull(),
    total: doublePrecision().notNull(),
    date: timestamp({ mode: 'string' })
      .default(sql`CURRENT_TIMESTAMP`)
      .notNull(),
    paymentMethod: paymethod('payment_method').notNull(),
    itemQuantity: integer('item_quantity').default(0).notNull(),
  },
  (table) => [
    foreignKey({
      columns: [table.customerId],
      foreignColumns: [customer.id],
      name: 'order_customer_id_fkey',
    }),
    foreignKey({
      columns: [table.employeeId],
      foreignColumns: [employee.id],
      name: 'order_employee_id_fkey',
    }),
  ],
);

export const employee = pgTable('employee', {
  id: uuid('id').$defaultFn(uuidv4).primaryKey().notNull(),
  name: varchar({ length: 100 }).notNull(),
  email: varchar({ length: 100 }).unique().notNull(),
  role: role().notNull().default('staff'),
  archived: boolean().default(false).notNull(),
});

export const orderContent = pgTable(
  'order_content',
  {
    orderId: uuid('order_id').notNull(),
    menuItemId: uuid('menu_item_id').notNull(),
    ingredientId: uuid('ingredient_id').notNull(),
    orderEntryId: uuid('order_entry_id').notNull(),
  },
  (table) => [
    foreignKey({
      columns: [table.orderId],
      foreignColumns: [order.id],
      name: 'order_content_order_id_fkey',
    }),
    foreignKey({
      columns: [table.menuItemId],
      foreignColumns: [menu.id],
      name: 'order_content_menu_item_id_fkey',
    }),
    foreignKey({
      columns: [table.ingredientId],
      foreignColumns: [ingredient.id],
      name: 'order_content_ingredient_id_fkey',
    }),
  ],
);

export const ingredient = pgTable('ingredient', {
  id: uuid('id').$defaultFn(uuidv4).primaryKey().notNull(),
  name: varchar({ length: 100 }).notNull(),
  category: varchar({ length: 100 }).notNull(),
  currentStock: integer('current_stock').notNull(),
  orderStock: integer('order_stock').notNull(),
  unitPrice: doublePrecision('unit_price').notNull(),
});

export const recipe = pgTable(
  'recipe',
  {
    menuItemId: uuid('menu_item_id').notNull(),
    ingredientId: uuid('ingredient_id').notNull(),
    quantity: integer().notNull(),
  },
  (table) => [
    foreignKey({
      columns: [table.menuItemId],
      foreignColumns: [menu.id],
      name: 'recipe_menu_item_id_fkey',
    }),
    foreignKey({
      columns: [table.ingredientId],
      foreignColumns: [ingredient.id],
      name: 'recipe_ingredient_id_fkey',
    }),
  ],
);

export const zReport = pgTable('z_report', {
  timestamp: timestamp({ mode: 'string' })
    .default(sql`(CURRENT_TIMESTAMP - '1 day'::interval)`)
    .notNull(),
});

export const nutrition_info = pgTable(
  'nutrition_info',
  {
    ingredientId: uuid('ingredient_id').notNull(),
    calories: integer().notNull(),
    fat_g: integer().notNull(),
    sodium_g: integer().notNull(),
    carbs_g: integer().notNull(),
    sugar_g: integer().notNull(),
    caffiene_mg: integer().notNull(),
  },
  (table) => [
    foreignKey({
      columns: [table.ingredientId],
      foreignColumns: [ingredient.id],
      name: 'recipe_ingredient_id_fkey',
    }),
  ],
);

export const allergens = pgTable(
  'allergens',
  {
    ingredientId: uuid('ingredient_id').notNull(),
    allergen: varchar({ length: 255 }).notNull(),
  },
  (table) => [
    foreignKey({
      columns: [table.ingredientId],
      foreignColumns: [ingredient.id],
      name: 'recipe_ingredient_id_fkey',
    }),
  ],
);
