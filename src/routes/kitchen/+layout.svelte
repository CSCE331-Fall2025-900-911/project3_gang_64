<script lang="ts">
  import { page } from '$app/state';
  import favicon from '$lib/assets/favicon.svg';
  import logo from '$lib/assets/logo.png';
  import { currentEmployee } from '$lib/auth/employee.svelte';
  import { localizeHref } from '$lib/i18n/runtime';
  import ColorblindFilter from '$lib/components/ColorblindFilter.svelte';
  import UserModal from '$lib/components/UserModal.svelte';
  import AccessibiltyModal from '$lib/components/AccessibiltyModal.svelte';
  import LanguageSelectModal from '$lib/components/LanguageSelectModal.svelte';
  import { t } from '$lib/utils/utils';
  import {
    AppShell,
    AppShellHeader,
    Avatar,
    Heading,
    HStack,
    IconButton,
    initializeTheme,
    modalManager,
    Select,
    type SelectItem,
  } from '@immich/ui';
  import { locales } from '$lib/i18n/runtime';
  import { mdiTranslate, mdiWheelchair } from '@mdi/js';
  import '../../app.css';

  let { children } = $props();

  initializeTheme();

  const modes: SelectItem[] = [
    { label: t('manager'), value: 'manager' },
    { label: t('cashier'), value: 'cashier' },
  ];

  let mode = $derived(
    modes.find(
      (item) =>
        item.value ===
        page.url.pathname.split('/').filter((segment) => !locales.includes(segment as (typeof locales)[0]))[2],
    ) ?? modes[0],
  );

  function handleModeChange(selected: SelectItem) {
    window.location.href = localizeHref(`/kitchen/${selected.value}/`);
  }

  function openUserProfile() {
    modalManager.show(UserModal);
  }

  let employee = currentEmployee();
</script>

<ColorblindFilter />

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
        <IconButton
          icon={mdiWheelchair}
          size="large"
          variant="outline"
          shape="round"
          onclick={() => modalManager.show(AccessibiltyModal)}
          aria-label={t('accessibility_options_label')}
        />
        <IconButton
          icon={mdiTranslate}
          size="large"
          variant="outline"
          shape="round"
          onclick={() => modalManager.show(LanguageSelectModal)}
          aria-label={t('change_language_label')}
        />
        <button onclick={openUserProfile}>
          <Avatar name={employee?.name ?? t('avatar_defaultName')} />
        </button>
      </div>
    </div>
  </AppShellHeader>

  {@render children?.()}
</AppShell>
