<script lang="ts">
  import { page } from '$app/state';
  import { getCategorizedMenu } from '$lib/api/menu.remote';
  import favicon from '$lib/assets/favicon.svg';
  import { td } from '$lib/contexts/translations.svelte';
  import { localizeHref } from '$lib/i18n/runtime';
  import { t } from '$lib/utils/utils';
  import { AppShellSidebar, NavbarItem } from '@immich/ui';
  import MenuGroup from './MenuGroup.svelte';

  let menu = await getCategorizedMenu();

  let currentCategory = $derived.by(() => {
    const hash = decodeURI(page.url.hash);
    const id = hash ? hash.substring(1) : Object.keys(menu)[0];
    return {
      id,
      items: menu[id] ?? [],
    };
  });
</script>

<svelte:head>
  <link rel="icon" href={favicon} />
  <title>{t('kiosk_order_title')}</title>
</svelte:head>

<div class="flex h-full overflow-hidden" role="main">
  <AppShellSidebar class="gap-2 pt-2 pr-4">
    {#each Object.keys(menu) as category}
      <NavbarItem
        href={localizeHref(`/kiosk/order#${category}`)}
        title={td(category) ?? ''}
        active={category === currentCategory.id}
      />
    {/each}
  </AppShellSidebar>

  <div class="h-full w-full overflow-y-auto p-4">
    {#if currentCategory.items}
      <MenuGroup {...currentCategory} />
    {/if}
  </div>
</div>
