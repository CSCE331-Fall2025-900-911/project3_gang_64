<script lang="ts">
  import { page } from '$app/state';
  import { getCategorizedMenu } from '$lib/api/menu.remote';
  import { orderManager } from '$lib/managers/order_manager.svelte';
  import { AppShellSidebar, Button, Heading, HStack, modalManager, NavbarItem, Text } from '@immich/ui';
  import MenuGroup from './MenuGroup.svelte';
  import OrderSubmitDialog from './OrderSubmitDialog.svelte';

  let menu = await getCategorizedMenu();
  let currentCategory = $derived.by(() => {
    const hash = decodeURI(page.url.hash);
    const title = hash ? hash.substring(1) : Object.keys(menu)[0];

    return {
      title,
      items: menu[title] ?? [],
    };
  });

  function showSubmitDialog() {
    modalManager.show(OrderSubmitDialog);
  }
</script>

<div class="flex h-full overflow-hidden">
  <AppShellSidebar class="gap-2 pt-2 pr-4">
    {#each Object.keys(menu) as category}
      <NavbarItem
        href={`/kitchen/cashier#${category}`}
        title={category ?? ''}
        active={category === currentCategory.title}
      />
    {/each}
  </AppShellSidebar>

  <div class="flex h-full w-full pb-2">
    <!-- Item View -->
    <div class="w-2/3 overflow-y-auto p-4">
      {#if currentCategory.items}
        <MenuGroup {...currentCategory} />
      {/if}
    </div>

    <!-- Order Summary -->
    <div class="m-6 flex w-1/3 flex-col">
      <div class="bg-level-1 mb-4 flex flex-1 flex-col overflow-y-auto rounded-xl p-3">
        {#if orderManager.currentOrder.length == 0}
          <Text class="pt-6 text-center">No items in order</Text>
        {/if}

        {#each orderManager.currentOrder as entry, i}
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
              <Text size="small">${entry.menuItem.price.toFixed(2)}</Text>
            </div>
          </div>
        {/each}
      </div>

      <!-- Order Summary -->
      <div class="shrink-0 gap-2">
        <HStack class="flex justify-between">
          <Heading size="tiny" fontWeight="normal">Subtotal</Heading>
          <p>${orderManager.subtotal.toFixed(2)}</p>
        </HStack>
        <HStack class="flex justify-between">
          <Heading size="tiny" fontWeight="normal">Tax</Heading>
          <p>${orderManager.tax.toFixed(2)}</p>
        </HStack>
        <HStack class="mt-2 flex justify-between">
          <Heading size="small">Total</Heading>
          <p>${orderManager.total.toFixed(2)}</p>
        </HStack>
        <Button class="mt-4 w-full" color="success" onclick={showSubmitDialog} disabled={!orderManager.isValidOrder}
          >Submit Order</Button
        >
      </div>
    </div>
  </div>
</div>
