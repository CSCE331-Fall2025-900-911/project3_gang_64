<script lang="ts">
  import favicon from '$lib/assets/favicon.svg';
  import { mdiCartOutline } from '@mdi/js';
  import logo from '$lib/assets/logo.png';
  import { page } from '$app/state';
  import { getMenu } from '$lib/api/menu.remote';
  import { goto } from '$app/navigation';
  import MenuGroup from './MenuGroup.svelte';
  import {
    AppShell,
    AppShellHeader,
    AppShellSidebar,
    Avatar,
    IconButton,
    initializeTheme,
    NavbarItem,
    type SelectItem,
    ThemeSwitcher,
  } from '@immich/ui';
  import '../../../app.css';
  import { kioskManager } from '$lib/managers/kiosk.svelte';

  let { children } = $props();

  let menu = await getMenu();

  let currentCategory = $derived.by(() => {
    const hash = decodeURI(page.url.hash);
    const title = hash ? hash.substring(1) : Object.keys(menu)[0];
    return {
      title,
      items: menu[title] ?? [],
    };
  });

  initializeTheme();

  function openCart() {
    goto('/kiosk/cart');
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
            onclick={openCart}
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

  <AppShellSidebar class="gap-2 pt-2 pr-4">
    {#each Object.keys(menu) as category}
      <NavbarItem
        href={`/kiosk/order#${category}`}
        title={category ?? ''}
        active={category === currentCategory.title}
      />
    {/each}
  </AppShellSidebar>

  <div class="flex h-full w-full pb-2">
    <div class="w-full overflow-y-auto p-4">
      {#if currentCategory.items}
        <MenuGroup {...currentCategory} />
      {/if}
    </div>
  </div>

  {@render children?.()}
</AppShell>
