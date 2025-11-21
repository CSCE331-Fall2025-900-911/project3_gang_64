<script lang="ts">
  import { getIngredients, getIngredientsForMenuItem } from '$lib/api/ingredient.remote';
  import type { MenuItem } from '$lib/db/types';
  import { t } from '$lib/utils/utils';
  import { Heading, Icon, IconButton, modalManager, toastManager } from '@immich/ui';
  import { mdiImageOff, mdiPlus } from '@mdi/js';
  import CartToast from './CartToast.svelte';
  import ItemModificationModal from './ItemModificationModal.svelte';

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

  async function showSubmitDialog() {
    const states = { isAdded: false };
    await modalManager.show(ItemModificationModal, { item, states });

    if (states.isAdded) {
      toastManager.custom({ component: CartToast, props: { itemName: item.name } }, { timeout: 5000, closable: true });
    }
  }
</script>

<div class="relative flex flex-col justify-between rounded-lg border-2 p-4">
  <div class="relative mb-5">
    <div class="bg-level-2 flex h-50 w-full items-center justify-center rounded-md border object-cover">
      {#if item.imageUrl}
        <img src={item.imageUrl} alt={item.name} />
      {:else}
        <Icon icon={mdiImageOff} size="96" class="" />
      {/if}
    </div>

    {#if outOfStock}
      <div class="absolute inset-0 flex items-center justify-center rounded-md bg-black/60">
        <span class="text-lg font-semibold text-white">{t('orderItem_outOfStock')}</span>
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
      onclick={showSubmitDialog}
      disabled={outOfStock || loading}
      aria-label={t('orderItem_addToOrder')}
    />
  </div>
</div>
