import { ingredientSelectSchema, menuItemSelectSchema } from '$lib/db/types';
import * as v from 'valibot';

export const OrderEntrySchema = v.object({
  menuItem: menuItemSelectSchema,
  ingredients: v.array(ingredientSelectSchema),
  quantity: v.number(),
  subtotal: v.number(),
  iceLevel: v.optional(v.picklist(['None', 'Low', 'Normal', 'High']), 'Normal'),
  sugarLevel: v.optional(v.picklist(['None', 'Low', 'Normal', 'High']), 'Normal'),
});
export type OrderEntry = v.InferInput<typeof OrderEntrySchema>;
