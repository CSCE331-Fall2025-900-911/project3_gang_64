<script lang="ts">
  import type { MenuItem } from '$lib/db/types';
  import { kioskManager } from '$lib/managers/kiosk.svelte';
  import { Button, Heading, IconButton } from '@immich/ui';
  import { mdiPlus } from '@mdi/js';
  import banana from '$lib/assets/banana.jpeg';

  interface Props {
    item: MenuItem;
  }

  let { item }: Props = $props();
  let loading = $state(false);

  async function handleAddToOrder() {
    loading = true;
    await kioskManager.addToOrder(item);
    loading = false;
  }
</script>

<div class="flex flex-col justify-between rounded-lg border-2 p-4">
  <img src={item.imageUrl ?? banana} alt={item.name} class="mb-3 h-50 w-full rounded-md border object-cover" />
  <Heading size="medium" class="mb-2">{item.name}</Heading>
  <div class="mt-4 flex items-center justify-between">
    <Heading size="small" fontWeight="normal">${Number.parseFloat(item.price).toFixed(2)}</Heading>
    <IconButton
      icon={mdiPlus}
      size="small"
      color="info"
      onclick={handleAddToOrder}
      disabled={loading}
      aria-label="Add to Order"
    />
  </div>
</div>
