<script lang="ts">
  import { td } from '$lib/contexts/translations.svelte';
  import type { MenuItem } from '$lib/db/types';
  import OrderItemTile from './OrderItemTile.svelte';

  interface Props {
    items: MenuItem[];
    id: string;
  }

  let { items, id }: Props = $props();
</script>

<div>
  <h1 class="mb-4 text-3xl font-bold">{td(id)}</h1>

  <div class="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3">
    {#each items as item (item.id)}
      <OrderItemTile {item} />
    {/each}
  </div>
</div>
