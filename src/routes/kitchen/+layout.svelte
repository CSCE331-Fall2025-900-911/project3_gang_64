<script lang="ts">
  import { page } from '$app/state';
  import favicon from '$lib/assets/favicon.svg';
  import logo from '$lib/assets/logo.png';
  import { currentEmployee } from '$lib/auth/employee.svelte';
  import UserModal from '$lib/components/UserModal.svelte';
  import { t } from '$lib/utils/utils';
  import {
    AppShell,
    AppShellHeader,
    Avatar,
    Heading,
    HStack,
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
    { label: t('manager'), value: 'manager' },
    { label: t('cashier'), value: 'cashier' },
  ];

  let mode = $derived(modes.find((item) => item.value === page.url.pathname.split('/')[2]) ?? modes[0]);

  function handleModeChange(selected: SelectItem) {
    window.location.href = `/kitchen/${selected.value}/`;
  }

  function openUserProfile() {
    modalManager.show(UserModal);
  }

  let employee = currentEmployee();
</script>

<svelte:head>
  <link rel="icon" href={favicon} />
  <title>{t('title')} | {mode.label}</title>
</svelte:head>

<AppShell>
  <AppShellHeader>
    <div class="flex w-full items-center justify-between p-4">
      <img src={logo} alt={t('logoAlt')} class="h-6" />
      <div class="flex items-center gap-4">
        {#if employee?.role == 'manager'}
          <HStack gap={4}>
            <Heading size="tiny">{t('mode_label')}</Heading>
            <Select data={modes} onChange={handleModeChange} bind:value={mode} />
          </HStack>
        {/if}
        <ThemeSwitcher size="large"/>
        <button onclick={openUserProfile}>
          <Avatar name={employee?.name ?? t('avatar_defaultName')} />
        </button>
      </div>
    </div>
  </AppShellHeader>

  {@render children?.()}
</AppShell>
