<script lang="ts">
  import { page } from '$app/state';
  import favicon from '$lib/assets/favicon.svg';
  import logo from '$lib/assets/logo.png';
  import { currentEmployee } from '$lib/auth/employee.svelte';
  import AccessibiltyModal from '$lib/components/AccessibiltyModal.svelte';
  import ColorblindFilter from '$lib/components/ColorblindFilter.svelte';
  import UserModal from '$lib/components/UserModal.svelte';
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
  import { mdiTranslate, mdiWheelchair } from '@mdi/js';
  import '../../app.css';
  import { locales, setLocale, getLocale, localizeHref, type Locale } from '$lib/i18n/runtime';

  let { children } = $props();

  initializeTheme();

  const modes: SelectItem[] = [
    { label: t('manager'), value: 'manager' },
    { label: t('cashier'), value: 'cashier' },
  ];

  const languages: SelectItem[] = locales.map((locale) => {
    try {
      const displayNames = new Intl.DisplayNames([locale], { type: 'language' });
      const label = displayNames.of(locale) || locale;
      return { label: label.charAt(0).toUpperCase() + label.slice(1), value: locale };
    } catch {
      return { label: locale.toUpperCase(), value: locale };
    }
  });

  let mode = $derived(modes.find((item) => item.value === page.url.pathname.split('/')[2]) ?? modes[0]);
  let selectedLanguage = $state<SelectItem>(languages.find((lang) => lang.value === getLocale()) ?? languages[0]);

  function handleModeChange(selected: SelectItem) {
    window.location.href = localizeHref(`/kitchen/${selected.value}/`);
  }

  function handleLanguageChange(selected: SelectItem) {
    selectedLanguage = selected;
    setLocale(selected.value as Locale);
    showLanguageSelect = false;
  }

  function openUserProfile() {
    modalManager.show(UserModal);
  }

  let showLanguageSelect = $state(false);
  let languageSelectRef: HTMLDivElement | undefined = $state();
  let selectElement: HTMLElement | undefined = $state();

  function toggleLanguageSelect() {
    showLanguageSelect = !showLanguageSelect;
  }

  function handleClickOutside(event: MouseEvent) {
    if (showLanguageSelect && languageSelectRef && !languageSelectRef.contains(event.target as Node)) {
      showLanguageSelect = false;
    }
  }

  let employee = currentEmployee();
</script>

<ColorblindFilter />

<svelte:head>
  <link rel="icon" href={favicon} />
  <title>{t('title')} | {mode.label}</title>
</svelte:head>

<svelte:document onclick={handleClickOutside} />

<AppShell>
  <AppShellHeader>
    <div class="flex w-full items-center justify-between p-4">
      <img src={logo} alt={t('logoAlt')} class="h-6" />
      <div class="flex items-center gap-4">
        <div bind:this={languageSelectRef}>
          <HStack gap={4}>
            <IconButton
              icon={mdiTranslate}
              size="large"
              variant="outline"
              shape="round"
              onclick={toggleLanguageSelect}
              aria-label={t('change_language_label')}
            />
            {#if showLanguageSelect}
              <div bind:this={selectElement}>
                <Select data={languages} onChange={handleLanguageChange} bind:value={selectedLanguage} />
              </div>
            {/if}
          </HStack>
        </div>
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
        <button onclick={openUserProfile}>
          <Avatar name={employee?.name ?? t('avatar_defaultName')} />
        </button>
      </div>
    </div>
  </AppShellHeader>

  {@render children?.()}
</AppShell>
