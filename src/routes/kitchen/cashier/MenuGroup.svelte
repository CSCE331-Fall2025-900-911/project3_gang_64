<script lang="ts">
  import type { MenuItem } from '$lib/db/types';
  import { cashierManager } from '$lib/managers/cashier.svelte';
  import { Button, Heading } from '@immich/ui';

  interface Props {
    items: MenuItem[];
    title: string;
  }

  let { items, title }: Props = $props();
</script>

<div>
  <Heading size="large" class="mb-4">{title}</Heading>

  <div class="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3">
    {#each items as item}
      <div class="flex flex-col justify-between rounded-lg border p-4">
        <Heading size="medium" class="mb-2">{item.name}</Heading>
        <div class="mt-4 flex items-center justify-between">
          <Heading size="small" fontWeight="normal">${Number.parseFloat(item.price).toFixed(2)}</Heading>
          <Button onclick={() => cashierManager.addToOrder(item)}>Add to Order</Button>
        </div>
      </div>
    {/each}
  </div>
</div>
