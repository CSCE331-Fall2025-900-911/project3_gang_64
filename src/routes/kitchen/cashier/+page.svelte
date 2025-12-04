<script lang="ts">
  import { page } from '$app/state';
  import { getCategorizedMenu } from '$lib/api/menu.remote';
  import OrderSummary from '$lib/components/OrderSummary.svelte';
  import { localizeHref } from '$lib/i18n/runtime';
  import { orderManager } from '$lib/managers/order_manager.svelte';
  import { AppShellSidebar, modalManager, NavbarItem } from '@immich/ui';
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
    modalManager.show(OrderSubmitDialog, { isCashier: true });
  }
</script>

<div class="flex h-full overflow-hidden">
  <AppShellSidebar class="gap-2 pt-2 pr-4">
    {#each Object.keys(menu) as category}
      <NavbarItem
        href={localizeHref(`/kitchen/cashier#${category}`)}
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

    <div class="flex w-1/3 border-l p-4">
      <OrderSummary
        entries={orderManager.currentOrder}
        subtotal={orderManager.subtotal}
        tax={orderManager.tax}
        total={orderManager.total}
        editable={true}
        {showSubmitDialog}
        onUpdateQuantity={(i, value) => orderManager.updateQuantity(i, value)}
        onRemoveEntry={(i) => orderManager.removeFromOrder(i)}
      />
    </div>
  </div>
</div>
