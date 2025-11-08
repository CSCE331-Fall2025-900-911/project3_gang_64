import { query } from '$app/server';
import { order } from '$lib/db/schema';
import { gt, sql } from 'drizzle-orm';
import * as v from 'valibot';
import { getDB } from '../db';

export const getDayOrderCount = query(v.date(), async (day) => {
  const db = getDB();

  return await db
    .select({
      count: sql<number>`COUNT(${order.id})`,
    })
    .from(order)
    .where(gt(order.date, day.toISOString()))
    .then((res) => res[0].count);
});

export const getDayRevenue = query(v.date(), async (day) => {
  const db = getDB();

  return await db
    .select({
      total: sql<number>`SUM(${order.total})`,
    })
    .from(order)
    .where(gt(order.date, day.toISOString()))
    .then((res) => res[0].total ?? 0);
});
