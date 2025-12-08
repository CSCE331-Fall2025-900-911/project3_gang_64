import { command, query } from '$app/server';
import { customer, ingredient, menu, order, orderContent } from '$lib/db/schema';
import {
  orderInsertSchema,
  orderSelectSchema,
  type IceLevel,
  type NewOrder,
  type SizeLevel,
  type SugarLevel,
} from '$lib/db/types';
import { OrderEntrySchema } from '$lib/managers/order_manager.types';
import { itemHash, luxonDatetime } from '$lib/utils/utils';
import { desc, eq, sql } from 'drizzle-orm';
import { DateTime } from 'luxon';
import { v4 as uuidv4 } from 'uuid';
import * as v from 'valibot';
import { getDB } from '../db';

const getOrdersSchema = v.object({
  page: v.optional(v.number(), 1),
  limit: v.optional(v.number(), 50),
  date: v.optional(luxonDatetime),
});

export const getOrders = query(getOrdersSchema, async ({ page = 0, limit = 25, date }) => {
  const db = getDB();

  const filter = date ? eq(sql<string>`DATE(${order.date})`, date) : undefined;

  // Get total count for pagination
  const [totalCount] = await db
    .select({
      count: sql<number>`COUNT(${order.id})`,
    })
    .from(order)
    .where(filter);

  // Get paginated orders
  const orders = await db
    .select({
      id: order.id,
      total: order.total,
      date: order.date,
      customer: customer.name,
      paymethod: order.paymentMethod,
    })
    .from(order)
    .where(filter)
    .innerJoin(customer, eq(order.customerId, customer.id))
    .orderBy(desc(order.date))
    .limit(limit)
    .offset(page * limit);

  const totalPages = Math.ceil(totalCount.count / limit);

  return {
    orders,
    totalPages,
    totalCount: totalCount.count,
  };
});

export const createOrder = command(orderInsertSchema, async (newOrder: NewOrder) => {
  const db = getDB();

  const created = await db.insert(order).values(newOrder).returning();
  return created[0];
});

export const deleteOrder = command(orderSelectSchema.entries.id, async (id) => {
  const db = getDB();
  await db.delete(order).where(eq(order.id, id));
});

const submitOrderSchema = v.object({
  customerId: v.string(),
  paymentMethod: v.picklist(['cash', 'credit'] as const),
  order: v.array(OrderEntrySchema),
  employeeId: v.nullable(v.string()),
});

export const submitOrder = command(
  submitOrderSchema,
  async ({ customerId, paymentMethod, order: submittedOrder, employeeId }) => {
    const db = getDB();

    const subtotal = submittedOrder.reduce((sum, entry) => sum + entry.subtotal * entry.quantity, 0);
    const tax = subtotal * 0.07;
    const total = subtotal + tax;

    const newOrder: NewOrder = {
      customerId,
      subtotal,
      tax,
      total,
      paymentMethod,
      employeeId,
      date: DateTime.now(),
      itemQuantity: submittedOrder.length,
    };

    const createdOrder = await db.insert(order).values(newOrder).returning();

    // Collect all order content entries and ingredient decrements
    const orderContentValues: {
      orderId: string;
      menuItemId: string;
      ingredientId: string;
      orderEntryId: string;
      itemSubtotal: number;
      iceLevel: (typeof submittedOrder)[number]['iceLevel'];
      sugarLevel: (typeof submittedOrder)[number]['sugarLevel'];
      sizeLevel: (typeof submittedOrder)[number]['sizeLevel'];
    }[] = [];
    const ingredientDecrements = new Map<string, number>();

    for (const entry of submittedOrder) {
      for (let i = 0; i < entry.quantity; i++) {
        const entryId = uuidv4();

        for (const entryIngredient of entry.ingredients) {
          orderContentValues.push({
            orderId: createdOrder[0].id,
            menuItemId: entry.menuItem.id,
            ingredientId: entryIngredient.id,
            orderEntryId: entryId,
            itemSubtotal: entry.subtotal,
            iceLevel: entry.iceLevel,
            sugarLevel: entry.sugarLevel,
            sizeLevel: entry.sizeLevel,
          });

          // Track ingredient decrements
          ingredientDecrements.set(entryIngredient.id, (ingredientDecrements.get(entryIngredient.id) || 0) + 1);
        }
      }
    }

    // Bulk insert all order content entries
    if (orderContentValues.length > 0) {
      await db.insert(orderContent).values(orderContentValues);
    }

    // Bulk update ingredient stock levels
    for (const [ingredientId, decrementAmount] of ingredientDecrements) {
      await db
        .update(ingredient)
        .set({ currentStock: sql`${ingredient.currentStock} - ${decrementAmount}` })
        .where(eq(ingredient.id, ingredientId));
    }

    return createdOrder[0];
  },
);

export const getOrderDetails = query(orderSelectSchema.entries.id, async (orderId) => {
  const db = getDB();

  // Get order info with customer
  const [orderInfo] = await db
    .select({
      id: order.id,
      subtotal: order.subtotal,
      tax: order.tax,
      total: order.total,
      date: order.date,
      paymentMethod: order.paymentMethod,
      customerName: customer.name,
      customerEmail: customer.email,
    })
    .from(order)
    .innerJoin(customer, eq(order.customerId, customer.id))
    .where(eq(order.id, orderId));

  if (!orderInfo) {
    throw new Error('Order not found');
  }

  // Get order contents grouped by orderEntryId
  const contents = await db
    .select({
      orderEntryId: orderContent.orderEntryId,
      menuItemId: orderContent.menuItemId,
      menuItemName: menu.name,
      menuItemPrice: menu.price,
      ingredientId: orderContent.ingredientId,
      ingredientName: ingredient.name,
      iceLevel: orderContent.iceLevel,
      sugarLevel: orderContent.sugarLevel,
      sizeLevel: orderContent.sizeLevel,
    })
    .from(orderContent)
    .innerJoin(menu, eq(orderContent.menuItemId, menu.id))
    .innerJoin(ingredient, eq(orderContent.ingredientId, ingredient.id))
    .where(eq(orderContent.orderId, orderId));

  // Group contents by orderEntryId to reconstruct order entries
  const entriesMap = new Map<
    string,
    {
      menuItem: { id: string; name: string; price: number };
      ingredients: { id: string; name: string }[];
      iceLevel: IceLevel;
      sugarLevel: SugarLevel;
      sizeLevel: SizeLevel;
    }
  >();

  for (const content of contents) {
    if (!entriesMap.has(content.orderEntryId)) {
      entriesMap.set(content.orderEntryId, {
        menuItem: {
          id: content.menuItemId,
          name: content.menuItemName,
          price: content.menuItemPrice,
        },
        ingredients: [],
        iceLevel: content.iceLevel,
        sugarLevel: content.sugarLevel,
        sizeLevel: content.sizeLevel,
      });
    }
    entriesMap.get(content.orderEntryId)!.ingredients.push({
      id: content.ingredientId,
      name: content.ingredientName,
    });
  }

  // Count quantity of identical entries (same menu item + same ingredients)
  const itemQuantities = new Map<string, number>();
  for (const entry of entriesMap.values()) {
    const key = itemHash(entry.menuItem, entry.ingredients, entry.iceLevel, entry.sugarLevel, entry.sizeLevel);
    itemQuantities.set(key, (itemQuantities.get(key) || 0) + 1);
  }

  // Create final entries with quantities (deduplicated by menu item + ingredients)
  const seenEntries = new Set<string>();
  const entries = [];
  for (const entry of entriesMap.values()) {
    const hash = itemHash(entry.menuItem, entry.ingredients);
    if (!seenEntries.has(hash)) {
      seenEntries.add(hash);
      entries.push({
        menuItem: entry.menuItem,
        ingredients: entry.ingredients,
        quantity: itemQuantities.get(hash) || 1,
      });
    }
  }

  return {
    ...orderInfo,
    entries,
  };
});
