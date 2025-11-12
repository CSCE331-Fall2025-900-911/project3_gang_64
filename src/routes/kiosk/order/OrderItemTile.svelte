<script lang="ts">
  import type { MenuItem } from '$lib/db/types';
  import { kioskManager } from '$lib/managers/kiosk.svelte';
  import { Heading, IconButton} from '@immich/ui';
  import { mdiPlus } from '@mdi/js';
  import {getIngredients , getIngredientsForMenuItem} from '$lib/api/ingredient.remote';

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
    recipe.current?.forEach(ingredient => {
      inventory.current?.forEach(stockItem => {
        if(stockItem.id === ingredient.id && stockItem.currentStock == 0) {
          tempStock = true;
          return;
        }
      });
    })
    return tempStock;
  });

  async function handleAddToOrder() {
    loading = true;
    await kioskManager.addToOrder(item);
    loading = false;
    if (firstAddAction) {
      firstAddAction();
    }
  }
</script>

<div class="flex flex-col justify-between rounded-lg border-2 p-4 relative">
  <img
    src={item.imageUrl ?? '/kioskImages/boba.jpeg'}
    alt={item.name}
    class="mb-3 h-50 w-full rounded-md border object-cover"
  />
  {#if (outOfStock)}
    <div class="bg-black/50 text-white absolute top-25 text-center w-full pr-9">Out of Stock</div>
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
