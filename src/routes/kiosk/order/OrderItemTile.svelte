<script lang="ts">
  import { getIngredients, getIngredientsForMenuItem } from '$lib/api/ingredient.remote';
  import type { MenuItem } from '$lib/db/types';
  import { orderManager } from '$lib/managers/order_manager.svelte';
  import { Heading, IconButton } from '@immich/ui';
  import { mdiPlus } from '@mdi/js';

  interface Props {
    item: MenuItem;
    firstAddAction?: () => void;
  }

  let { item, firstAddAction }: Props = $props();
  let loading = $state(false);

  let inventory = getIngredients();
  let recipe = $derived(getIngredientsForMenuItem(item.id));
  let outOfStock = $derived.by(() => {
    let tempStock = false;
    recipe.current?.forEach((ingredient) => {
      inventory.current?.forEach((stockItem) => {
        if (stockItem.id === ingredient.id && stockItem.currentStock == 0) {
          tempStock = true;
          return;
        }
      });
    });
    return tempStock;
  });

  async function handleAddToOrder() {
    loading = true;
    await orderManager.addToOrder(item);
    loading = false;
    if (firstAddAction) {
      firstAddAction();
    }
  }
</script>

<div class="relative flex flex-col justify-between rounded-lg border-2 p-4">
  <img
    src={item.imageUrl ?? '/kioskImages/boba.jpeg'}
    alt={item.name}
    class="mb-3 h-50 w-full rounded-md border object-cover"
  />
  {#if outOfStock}
    <div class="absolute top-25 w-full bg-black/50 pr-9 text-center text-white">Out of Stock</div>
  {/if}
  <Heading size="medium" class="mb-2">{item.name}</Heading>
  <div class="mt-4 flex items-center justify-between">
    <Heading size="small" fontWeight="normal">${item.price.toFixed(2)}</Heading>
    <IconButton
      icon={mdiPlus}
      size="small"
      color="info"
      onclick={handleAddToOrder}
      disabled={outOfStock || loading}
      aria-label="Add to Order"
    />
  </div>
</div>
