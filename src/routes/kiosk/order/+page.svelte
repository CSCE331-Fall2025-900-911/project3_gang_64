<script lang="ts">
  import { page } from '$app/state';
  import { getCategorizedMenu } from '$lib/api/menu.remote';
  import favicon from '$lib/assets/favicon.svg';
  import { AppShell, AppShellSidebar, NavbarItem, toastManager } from '@immich/ui';
  import CartToast from './CartToast.svelte';
  import MenuGroup from './MenuGroup.svelte';
  import { t } from '$lib/utils/utils';

  const orderUrl: string = '/kiosk/order';
  const timeout = $state(5000);
  const closable = $state(true);

  let menu = await getCategorizedMenu();

  let isFirstItemAdded = $state(false);

  let currentCategory = $derived.by(() => {
    const hash = decodeURI(page.url.hash);
    const title = hash ? hash.substring(1) : Object.keys(menu)[0];
    return {
      title,
      items: menu[title] ?? [],
    };
  });

  const handleCartPopup = () => {
    toastManager.custom({ component: CartToast, props: {} }, { timeout, closable });
  };

  function firstAddAction() {
    if (!isFirstItemAdded) {
      handleCartPopup();
      isFirstItemAdded = true;
    }
  }
</script>

<svelte:head>
  <link rel="icon" href={favicon} />
  <title>{t('kiosk_order_title')}</title>
</svelte:head>

<AppShell>
  <AppShellSidebar class="gap-2 pt-2 pr-4">
    {#each Object.keys(menu) as category}
      <NavbarItem href={`${orderUrl}#${category}`} title={category ?? ''} active={category === currentCategory.title} />
    {/each}
  </AppShellSidebar>

  <div class="flex h-full w-full pb-2">
    <div class="w-full overflow-y-auto p-4">
      {#if currentCategory.items}
        <MenuGroup title={currentCategory.title} items={currentCategory.items} {firstAddAction} />
      {/if}
    </div>
  </div>
</AppShell>
