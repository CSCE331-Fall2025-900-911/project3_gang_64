<script lang="ts">
  import type { MenuItem } from '$lib/db/types';
  import { cashierManager } from '$lib/managers/cashier.svelte';
  import { Button, Heading } from '@immich/ui';

  interface Props {
    item: MenuItem;
  }

  let { item }: Props = $props();
  let loading = $state(false);

  async function handleAddToOrder(item: MenuItem) {
    loading = true;

    await cashierManager.addToOrder(item);
    loading = false;
  }
</script>

<div class="flex flex-col justify-between rounded-lg border p-4">
  <Heading size="medium" class="mb-2">{item.name}</Heading>
  <div class="mt-4 flex items-center justify-between">
    <Heading size="small" fontWeight="normal">${Number.parseFloat(item.price).toFixed(2)}</Heading>
    <Button onclick={() => handleAddToOrder(item)} {loading}>Add to Order</Button>
  </div>
</div>
