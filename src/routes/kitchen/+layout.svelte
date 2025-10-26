<script lang="ts">
  import { page } from '$app/state';
  import favicon from '$lib/assets/favicon.svg';
  import {
    AppShell,
    AppShellHeader,
    Avatar,
    Heading,
    initializeTheme,
    Select,
    ThemeSwitcher,
    type SelectItem,
  } from '@immich/ui';
  import '../../app.css';

  let { children } = $props();

  initializeTheme();

  const modes: SelectItem[] = [
    { label: 'Manager', value: 'manager' },
    { label: 'Cashier', value: 'cashier' },
  ];

  let mode = $derived(modes.find((item) => item.value === page.url.pathname.split('/')[2]) ?? modes[0]);

  function handleModeChange(selected: SelectItem) {
    window.location.href = `/kitchen/${selected.value}/`;
  }
</script>

<svelte:head>
  <link rel="icon" href={favicon} />
  <title>ShareTea | {mode.label}</title>
</svelte:head>

<AppShell>
  <AppShellHeader>
    <div class="flex w-full items-center justify-between p-4">
      <Heading size="medium">ShareTea</Heading>
      <div class="flex items-center gap-4">
        <Select data={modes} onChange={handleModeChange} bind:value={mode} />
        <ThemeSwitcher />
        <div>
          <Avatar name="Share Tea" />
        </div>
      </div>
    </div>
  </AppShellHeader>

  {@render children?.()}
</AppShell>
