import { ingredientSelectSchema, menuItemSelectSchema } from '$lib/db/types';
import * as v from 'valibot';

export const OrderEntrySchema = v.object({
  menuItem: menuItemSelectSchema,
  ingredients: v.array(ingredientSelectSchema),
  quantity: v.number(),
  subtotal: v.number(),
  iceLevel: v.optional(v.picklist(['None', 'Less', 'Normal', 'Extra']), 'Normal'),
  sugarLevel: v.optional(v.picklist(['None', 'Less', 'Normal', 'Extra']), 'Normal'),
  sizeLevel: v.optional(v.picklist(['Small', 'Medium', 'Large', 'Extra Large']), 'Small'),
  isCashier: v.optional(v.boolean(), false),
  isHot: v.optional(v.boolean(), false),
});
export type OrderEntry = v.InferInput<typeof OrderEntrySchema>;
