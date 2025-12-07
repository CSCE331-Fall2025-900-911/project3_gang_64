import { ingredientSelectSchema, menuItemSelectSchema } from '$lib/db/types';
import * as v from 'valibot';

export const OrderEntrySchema = v.object({
  menuItem: menuItemSelectSchema,
  ingredients: v.array(ingredientSelectSchema),
  lessList: v.array(v.string()),
  quantity: v.number(),
  subtotal: v.number(),
  iceLevel: v.optional(v.picklist(['None', 'Less', 'Normal', 'Extra']), 'Normal'),
  sugarLevel: v.optional(v.picklist(['None', 'Less', 'Normal', 'Extra']), 'Normal'),
  isCashier: v.boolean(),
});
export type OrderEntry = v.InferInput<typeof OrderEntrySchema>;
