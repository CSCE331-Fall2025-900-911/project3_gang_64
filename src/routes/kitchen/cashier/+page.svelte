<script lang="ts">
  import { page } from '$app/state';
  import { getMenuCategories } from '$lib/api/menu.remote';
  import { AppShellSidebar, Button, Heading, HStack, NavbarItem, Text } from '@immich/ui';
  import MenuGroup from './MenuGroup.svelte';

  let categories = await getMenuCategories();
  console.log(page.url.hash.replace('#', ''));
  let currentCategory = $derived(
    categories.find((cat) => cat === decodeURI(page.url.hash).replace('#', '')) ?? categories[0],
  );
</script>

<div class="flex h-full overflow-hidden">
  <AppShellSidebar class="gap-2 pt-2 pr-4">
    {#each categories as category}
      <NavbarItem href={`/kitchen/cashier#${category}`} title={category ?? ''} active={category === currentCategory} />
    {/each}
  </AppShellSidebar>

  <div class="flex h-full w-full pb-2">
    <!-- Item View -->
    <div class="w-2/3 overflow-y-auto p-4">
      {#if currentCategory}
        <MenuGroup categoryTitle={currentCategory} />
      {/if}
    </div>
    <!-- Order Summary -->

    <div class="m-6 flex w-1/3 flex-col">
      <div class="bg-level-1 mb-4 flex flex-1 flex-col justify-center overflow-y-auto rounded-xl p-3">
        <Text class="text-center">No items in order</Text>
      </div>

      <div class="shrink-0 gap-2">
        <HStack class="flex justify-between">
          <Heading size="tiny" fontWeight="normal">Subtotal</Heading>
          <p>$0.00</p>
        </HStack>
        <HStack class="flex justify-between">
          <Heading size="tiny" fontWeight="normal">Tax</Heading>
          <p>$0.00</p>
        </HStack>
        <HStack class="mt-2 flex justify-between">
          <Heading size="small">Total</Heading>
          <p>$0.00</p>
        </HStack>
        <Button class="mt-4 w-full" color="success">Submit Order</Button>
      </div>
    </div>
  </div>
</div>
