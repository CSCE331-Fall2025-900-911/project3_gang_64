<script lang="ts">
  import type { MenuItem } from '$lib/db/types';
  import { cashierManager } from '$lib/managers/cashier.svelte';
  import { Button, Heading } from '@immich/ui';
  import {getIngredients , getIngredientsForMenuItem} from '$lib/api/ingredient.remote';


  interface Props {
    item: MenuItem;
  }

  let { item }: Props = $props();
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

  async function handleAddToOrder(item: MenuItem) {
    loading = true;

    await cashierManager.addToOrder(item);
    loading = false;
  }

</script>

<div class="flex flex-col justify-between rounded-lg border p-4">
  <Heading size="medium" class="mb-2">{item.name}</Heading>
  <div class="mt-4 flex items-center justify-between">
    <Heading size="small" fontWeight="normal">${item.price.toFixed(2)}</Heading>
    <Button onclick={() => handleAddToOrder(item)} {loading} disabled = {outOfStock}>
      {#if (outOfStock)}
        Out of Stock 
      {:else}
        Add to Order  
      {/if}
    </Button>
  </div>
</div>
