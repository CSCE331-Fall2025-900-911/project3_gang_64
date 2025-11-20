<script lang="ts">
  import type { MenuItem } from '$lib/db/types';
  import { Heading } from '@immich/ui';
  import OrderItemTile from './OrderItemTile.svelte';

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
      <OrderItemTile {item} />
    {/each}
  </div>
</div>
