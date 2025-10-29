<script lang="ts">
  import { page } from '$app/state';
  import { getMenu } from '$lib/api/menu.remote';
  import { cashierManager } from '$lib/managers/cashier.svelte';
  import { AppShellSidebar, Button, Heading, HStack, NavbarItem, Text } from '@immich/ui';
  import MenuGroup from './MenuGroup.svelte';

  let menu = await getMenu();
  let currentCategory = $derived.by(() => {
    const hash = decodeURI(page.url.hash);
    return hash ? hash.substring(1) : Object.keys(menu)[0];
  });
  let currentCategoryItems = $derived(menu[currentCategory]);
</script>

<div class="flex h-full overflow-hidden">
  <AppShellSidebar class="gap-2 pt-2 pr-4">
    {#each Object.keys(menu) as category}
      <NavbarItem href={`/kitchen/cashier#${category}`} title={category ?? ''} active={category === currentCategory} />
    {/each}
  </AppShellSidebar>

  <div class="flex h-full w-full pb-2">
    <!-- Item View -->
    <div class="w-2/3 overflow-y-auto p-4">
      {#if currentCategoryItems}
        <MenuGroup items={currentCategoryItems} title={currentCategory} />
      {/if}
    </div>

    <!-- Order Summary -->
    <div class="m-6 flex w-1/3 flex-col">
      <div class="bg-level-1 mb-4 flex flex-1 flex-col overflow-y-auto rounded-xl p-3">
        {#if cashierManager.currentOrder.length == 0}
          <Text class="pt-6 text-center">No items in order</Text>
        {/if}

        {#each cashierManager.currentOrder as entry, i}
          <div class="mb-2 flex justify-between border-b pb-2">
            <div>
              <Heading size="small">{entry.menuItem.name}</Heading>
              <div class="gap-3 pl-4">
                {#each entry.ingredients as ingredient}
                  <Text size="small" class="text-muted-foreground">
                    {ingredient.name}
                  </Text>
                {/each}
              </div>
            </div>
            <div class="flex flex-col items-end">
              <Text size="small">${Number.parseFloat(entry.menuItem.price).toFixed(2)}</Text>
            </div>
          </div>
        {/each}
      </div>

      <!-- Order Summary -->
      <div class="shrink-0 gap-2">
        <HStack class="flex justify-between">
          <Heading size="tiny" fontWeight="normal">Subtotal</Heading>
          <p>${cashierManager.subtotal.toFixed(2)}</p>
        </HStack>
        <HStack class="flex justify-between">
          <Heading size="tiny" fontWeight="normal">Tax</Heading>
          <p>${cashierManager.tax.toFixed(2)}</p>
        </HStack>
        <HStack class="mt-2 flex justify-between">
          <Heading size="small">Total</Heading>
          <p>${cashierManager.total.toFixed(2)}</p>
        </HStack>
        <Button class="mt-4 w-full" color="success">Submit Order</Button>
      </div>
    </div>
  </div>
</div>
