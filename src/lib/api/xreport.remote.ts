import { query } from '$app/server';
import { getDB } from '$lib/db';
import { order, zReport } from '$lib/db/schema';
import { and, desc, gte, lte, sql } from 'drizzle-orm';
import { DateTime } from 'luxon';
import * as v from 'valibot';

/**
 * Retrieves hourly sales data for the X-Report.
 * Returns data grouped by hour of the day with sales metrics.
 * @param clientTimezone - The IANA timezone of the client (e.g., 'America/Chicago')
 */
export const getXReportData = query(v.string(), async (clientTimezone: string) => {
  const db = getDB();

  const today = DateTime.now().setZone(clientTimezone).startOf('day');
  const todayEnd = DateTime.now().setZone(clientTimezone).endOf('day');

  // Generate hours from 11 AM to 11 PM and LEFT JOIN with order data
  // Use AT TIME ZONE to convert database timestamps to client timezone
  const hourlyData = await db.execute(sql`
    WITH hours AS (
      SELECT generate_series(11, 23) AS hour
    )
    SELECT 
      h.hour,
      COALESCE(SUM(o.total), 0) AS sales,
      COUNT(CASE WHEN o.payment_method = 'cash' THEN 1 END) AS cash_count,
      COUNT(CASE WHEN o.payment_method = 'credit' THEN 1 END) AS credit_count,
      COALESCE(SUM(o.tax), 0) AS tax_collected,
      COALESCE(SUM(o.item_quantity), 0) AS total_items,
      COUNT(DISTINCT o.id) AS total_orders
    FROM hours h
    LEFT JOIN "order" o ON EXTRACT(HOUR FROM (o.date AT TIME ZONE ${clientTimezone})) = h.hour
      AND o.date >= ${today}
      AND o.date <= ${todayEnd}
    GROUP BY h.hour
    ORDER BY h.hour
  `);

  // Format the data for display
  return hourlyData.rows.map((row: any) => ({
    hour: Number(row.hour),
    sales: Number(row.sales),
    cashCount: Number(row.cash_count),
    creditCount: Number(row.credit_count),
    taxCollected: Number(row.tax_collected),
    avgItemsPerOrder: row.total_orders > 0 ? Number(row.total_items) / Number(row.total_orders) : 0,
    avgOrderTotal: row.total_orders > 0 ? Number(row.sales) / Number(row.total_orders) : 0,
  }));
});
