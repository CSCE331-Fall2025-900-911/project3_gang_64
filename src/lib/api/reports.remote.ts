import { query } from '$app/server';
import { order } from '$lib/db/schema';
import { luxonDatetime } from '$lib/utils/utils';
import { gt, sql } from 'drizzle-orm';
import { getDB } from '../db';

export const getDayOrderCount = query(luxonDatetime, async (day) => {
  const db = getDB();

  return await db
    .select({
      count: sql<number>`COUNT(${order.id})`,
    })
    .from(order)
    .where(gt(order.date, day))
    .then((res) => res[0].count);
});

export const getDayRevenue = query(luxonDatetime, async (day) => {
  const db = getDB();

  return await db
    .select({
      total: sql<number>`SUM(${order.total})`,
    })
    .from(order)
    .where(gt(order.date, day))
    .then((res) => res[0].total ?? 0);
});
