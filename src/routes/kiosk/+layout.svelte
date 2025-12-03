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
  } from '@immich/ui';
  import { mdiCartOutline, mdiTranslate, mdiWheelchair } from '@mdi/js';
  import '../../app.css';
  import CartModal from './order/CartModal.svelte';
  import LanguageSelectModal from '$lib/components/LanguageSelectModal.svelte';
  import AccessibiltyModal from '$lib/components/AccessibiltyModal.svelte';

  let { children } = $props();

  initializeTheme();

  function openCart() {
    modalManager.show(CartModal);
  }
</script>

<ColorblindFilter />

<svelte:head>
  <link rel="icon" href={favicon} />
  <title>{t('title')}</title>
</svelte:head>

<AppShell>
  <AppShellHeader>
    <div class="flex w-full items-center justify-between p-4">
      <img src={logo} alt={t('logoAlt')} class="h-6" />
      <div class="flex items-center gap-4">
        <ThemeSwitcher size="large" />
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
