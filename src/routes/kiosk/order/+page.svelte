<script lang="ts">
  import favicon from '$lib/assets/favicon.svg';
  import { page } from '$app/state';
  import { getMenu } from '$lib/api/menu.remote';
  import MenuGroup from './MenuGroup.svelte';
  import { AppShell, AppShellSidebar, initializeTheme, NavbarItem } from '@immich/ui';

  let menu = await getMenu();

  let currentCategory = $derived.by(() => {
    const hash = decodeURI(page.url.hash);
    const title = hash ? hash.substring(1) : Object.keys(menu)[0];
    return {
      title,
      items: menu[title] ?? [],
    };
  });
</script>

<svelte:head>
  <link rel="icon" href={favicon} />
  <title>ShareTea</title>
</svelte:head>

<AppShell>
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
</AppShell>
