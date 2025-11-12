<script lang="ts">
  import type { MenuItem } from '$lib/db/types';
  import { kioskManager } from '$lib/managers/kiosk.svelte';
  import { Heading, IconButton , LoadingSpinner } from '@immich/ui';
  import { mdiPlus } from '@mdi/js';
  import {getIngredients , getIngredientsForMenuItem} from '$lib/api/ingredient.remote';
  import {onMount} from 'svelte';
  import { boolean } from 'drizzle-orm/gel-core';

  interface Props {
    item: MenuItem;
    firstAddAction?: () => void;
  }

  let { item, firstAddAction }: Props = $props();
  let loading = $state(false);

  let inventory = getIngredients();
  let recipe = $derived(getIngredientsForMenuItem(item.id));
  let outOfStock = $state(false);
  let isOut:boolean;
  
  //cycle through ingredients in recipe see if we have inventory, set stock appropriately
  $effect(() => {
    let isOut = false;
    recipe.current?.forEach(function(ingredient) {
      inventory.current?.forEach(function (stockItem) {
        if (ingredient.id == stockItem.id && stockItem.currentStock == 0) {
          isOut = true;
        }
      });
    });

    if (isOut !== outOfStock) outOfStock = isOut;

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


<div class="flex flex-col justify-between rounded-lg border-2 p-4">
  <img
    src={item.imageUrl ?? '/kioskImages/boba.jpeg'}
    alt={item.name}
    class="mb-3 h-50 w-full rounded-md border object-cover"
  />
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
