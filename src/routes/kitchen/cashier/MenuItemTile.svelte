<script lang="ts">
  import { getIngredients, getIngredientsForMenuItem } from '$lib/api/ingredient.remote';
  import type { MenuItem } from '$lib/db/types';
  import { orderManager } from '$lib/managers/order_manager.svelte';
  import { Button, Heading } from '@immich/ui';
  import { t } from '$lib/utils/utils';

  interface Props {
    item: MenuItem;
  }

  let { item }: Props = $props();
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
  }
</script>

<div class="flex flex-col justify-between rounded-lg border p-4">
  <Heading size="medium" class="mb-2">{item.name}</Heading>
  <div class="mt-4 flex justify-between flex-col">
    <Heading size="medium" fontWeight="normal" class="mb-2">${item.price.toFixed(2)}</Heading>
    <Button onclick={handleAddToOrder} {loading} disabled={outOfStock} size="large">
      {#if outOfStock}
        {t('orderItem_outOfStock')}
      {:else}
        {t('orderItem_addToOrder')}
      {/if}
    </Button>
  </div>
</div>
