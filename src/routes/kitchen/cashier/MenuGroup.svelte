<script lang="ts">
  import { getMenuCategory } from '$lib/api/menu.remote';
  import { Button, Heading, LoadingSpinner } from '@immich/ui';

  interface Props {
    categoryTitle: string;
  }

  let { categoryTitle }: Props = $props();

  const menuItems = $derived(getMenuCategory(categoryTitle));
</script>

<div>
  <Heading size="large" class="mb-4">{categoryTitle}</Heading>

  {#if menuItems.loading}
    <LoadingSpinner class="my-8" />
  {:else if menuItems.error}
    <p class="my-8 text-red-500">Error loading menu items.</p>
  {:else}
    <div class="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3">
      {#each menuItems.current as item}
        <div class="flex flex-col justify-between rounded-lg border p-4">
          <Heading size="medium" class="mb-2">{item.name}</Heading>
          <div class="mt-4 flex items-center justify-between">
            <Heading size="small" fontWeight="normal">${Number.parseFloat(item.price).toFixed(2)}</Heading>
            <Button>Add to Order</Button>
          </div>
        </div>
      {/each}
    </div>
  {/if}
</div>
