<script lang="ts">
  import { goto } from '$app/navigation';
  import { page } from '$app/state';
  import favicon from '$lib/assets/favicon.svg';
  import logo from '$lib/assets/logo.png';
  import { kioskManager } from '$lib/managers/kiosk.svelte';
  import { AppShell, AppShellHeader, Avatar, IconButton, initializeTheme, ThemeSwitcher } from '@immich/ui';
  import { mdiCartOutline, mdiShoppingOutline } from '@mdi/js';
  import '../../app.css';

  let { children } = $props();

  initializeTheme();

  const orderUrl: string = '/kiosk/order';
  const cartUrl: string = '/kiosk/cart';
  const cartLabel: string = 'Cart';
  const orderLabel: string = 'Order';

  const shopModeIcon = $derived.by(() => {
    return page.url.pathname === cartUrl ? mdiShoppingOutline : mdiCartOutline;
  });

  const shopModeLabel = $derived.by(() => {
    return page.url.pathname === cartUrl ? orderLabel : cartLabel;
  });

  function openCart() {
    goto(cartUrl);
  }

  function closeCart() {
    goto(orderUrl);
  }

  function handleShopModeClick() {
    if (page.url.pathname === cartUrl) {
      closeCart();
    } else {
      openCart();
    }
  }
</script>

<svelte:head>
  <link rel="icon" href={favicon} />
  <title>ShareTea</title>
</svelte:head>

<AppShell>
  <AppShellHeader>
    <div class="flex w-full items-center justify-between p-4">
      <img src={logo} alt="ShareTea Logo" class="h-6" />
      <div class="flex items-center gap-4">
        <ThemeSwitcher />
        <div class="relative inline-block">
          <IconButton
            icon={shopModeIcon}
            shape="round"
            size="medium"
            color="primary"
            onclick={handleShopModeClick}
            aria-label={shopModeLabel}
          />
          <div class="absolute -top-1 -right-1">
            <Avatar
              size="tiny"
              name={kioskManager.getCurrentCartAmount() > 9 ? '9 +' : kioskManager.getCurrentCartAmount().toString()}
              color="red"
            />
          </div>
        </div>
      </div>
    </div>
  </AppShellHeader>

  {@render children?.()}
</AppShell>
