<script lang="ts">
  import { page } from '$app/state';
  import favicon from '$lib/assets/favicon.svg';
  import logo from '$lib/assets/logo.png';
  import UserModal from '$lib/shared/UserModal.svelte';
  import {
    AppShell,
    AppShellHeader,
    Avatar,
    initializeTheme,
    modalManager,
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

  function openUserProfile() {
    modalManager.show(UserModal);
  }
</script>

<svelte:head>
  <link rel="icon" href={favicon} />
  <title>ShareTea | {mode.label}</title>
</svelte:head>

<AppShell>

  {@render children?.()}
</AppShell>
