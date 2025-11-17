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
  <div class="relative mb-5">
    <img
      src={item.imageUrl ?? '/kioskImages/boba.jpeg'}
      alt={item.name}
      class="h-50 w-full rounded-md border object-cover"
    />
    {#if outOfStock}
      <div class="absolute inset-0 flex items-center justify-center rounded-md bg-black/60">
        <span class="text-lg font-semibold text-white">Out of Stock</span>
      </div>
    {/if}
  </div>
  <Heading size="large" class="mb-2">{item.name}</Heading>
  <div class="mt-2 flex items-center justify-between">
    <Heading size="medium" fontWeight="normal">${item.price.toFixed(2)}</Heading>
    <IconButton
      icon={mdiPlus}
      size="large"
      color="info"
      onclick={handleAddToOrder}
      disabled={outOfStock || loading}
      aria-label="Add to Order"
    />
  </div>
</div>
