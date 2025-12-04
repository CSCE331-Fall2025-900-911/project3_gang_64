<script lang="ts">
  import type { MenuItem } from '$lib/db/types';
  import { Heading } from '@immich/ui';
  import { td } from '$lib/contexts/translations.svelte';
  import OrderItemTile from './OrderItemTile.svelte';

  interface Props {
    items: MenuItem[];
    id: string;
  }

  let { items, id }: Props = $props();
</script>

<div>
  <Heading size="large" class="mb-4">{td(id)}</Heading>

  <div class="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3">
    {#each items as item}
      <OrderItemTile {item} />
    {/each}
  </div>
</div>
