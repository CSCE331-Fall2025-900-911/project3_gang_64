<script lang="ts">
  import favicon from '$lib/assets/favicon.svg';
  import logo from '$lib/assets/logo.png';
  import ColorblindFilter from '$lib/components/ColorblindFilter.svelte';
  import { orderManager } from '$lib/managers/order_manager.svelte';
  import { t } from '$lib/utils/utils';
  import {
    AppShell,
    AppShellHeader,
    Avatar,
    IconButton,
    initializeTheme,
    modalManager,
    ThemeSwitcher,
    HStack,
    Select,
    type SelectItem,
  } from '@immich/ui';
  import { mdiCartOutline, mdiTranslate } from '@mdi/js';
  import '../../app.css';
  import CartModal from './order/CartModal.svelte';
  import { locales, setLocale, getLocale, localizeHref, type Locale } from '$lib/i18n/runtime';

  let { children } = $props();

  initializeTheme();

  const languages: SelectItem[] = locales.map((locale) => {
    try {
      const displayNames = new Intl.DisplayNames([locale], { type: 'language' });
      const label = displayNames.of(locale) || locale;
      return { label: label.charAt(0).toUpperCase() + label.slice(1), value: locale };
    } catch {
      return { label: locale.toUpperCase(), value: locale };
    }
  });

  let selectedLanguage = $state<SelectItem>(languages.find((lang) => lang.value === getLocale()) ?? languages[0]);

  function openCart() {
    modalManager.show(CartModal);
  }

  function handleLanguageChange(selected: SelectItem) {
    selectedLanguage = selected;
    setLocale(selected.value as Locale);
    showLanguageSelect = false;
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
</script>

<ColorblindFilter />

<svelte:head>
  <link rel="icon" href={favicon} />
  <title>{t('title')}</title>
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
        <ThemeSwitcher size="large" />
        <div class="relative inline-block">
          <IconButton
            icon={mdiCartOutline}
            shape="round"
            size="medium"
            color="primary"
            onclick={openCart}
            aria-label={t('kiosk_cart')}
          />
          <div class="absolute -top-1 -right-1">
            <Avatar
              size="tiny"
              name={orderManager.getCurrentCartAmount() > 9 ? '9 +' : orderManager.getCurrentCartAmount().toString()}
              color="red"
            />
          </div>
        </div>
      </div>
    </div>
  </AppShellHeader>

  {@render children?.()}
</AppShell>
