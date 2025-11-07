<script lang="ts">
  import { goto } from '$app/navigation';
  import { page } from '$app/state';
  import favicon from '$lib/assets/favicon.svg';
  import logo from '$lib/assets/logo.png';
  import { kioskManager } from '$lib/managers/kiosk.svelte';
  import { AppShell, AppShellHeader, Avatar, IconButton, initializeTheme, ThemeSwitcher } from '@immich/ui';
  import { mdiCartOutline } from '@mdi/js';
  import '../../app.css';

  let { children } = $props();

  initializeTheme();

  function openCart() {
    goto('/kiosk/cart');
  }

  function closeCart() {
    goto('/kiosk/order');
  }

  function handleCartClick() {
    if (page.url.pathname === '/kiosk/cart') {
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
            icon={mdiCartOutline}
            shape="round"
            size="medium"
            color="primary"
            onclick={handleCartClick}
            aria-label="Cart"
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
