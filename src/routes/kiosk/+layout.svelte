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
  import { mdiCartOutline } from '@mdi/js';
  import '../../app.css';
  import CartModal from './order/CartModal.svelte';

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
