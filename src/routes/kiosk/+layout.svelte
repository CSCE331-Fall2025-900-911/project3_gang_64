<script lang="ts">
  import { goto } from '$app/navigation';
  import { page } from '$app/state';
  import favicon from '$lib/assets/favicon.svg';
  import logo from '$lib/assets/logo.png';
  import { orderManager } from '$lib/managers/order_manager.svelte';
  import { AppShell, AppShellHeader, Avatar, IconButton, initializeTheme, ThemeSwitcher } from '@immich/ui';
  import { mdiCartOutline, mdiEye, mdiPartyPopper, mdiShoppingOutline } from '@mdi/js';
  import { onMount } from 'svelte';
  import '../../app.css';
  import { colorblindMode, type ColorblindMode } from './colorBlind';

  let { children } = $props();

  initializeTheme();

  const orderUrl: string = '/kiosk/order';
  const cartUrl: string = '/kiosk/cart';
  const cartLabel: string = 'Cart';
  const orderLabel: string = 'Order';

  const shopModeIcon = $derived.by(() => {
    return page.url.pathname === cartUrl ? mdiShoppingOutline : mdiCartOutline;
  });

  const shopModeLabel = $derived.by(() => {
    return page.url.pathname === cartUrl ? orderLabel : cartLabel;
  });

  const colorBlindModeLabel = $derived.by(() => {
    return currentMode;
  });

  function openCart() {
    goto(cartUrl);
  }

  function closeCart() {
    goto(orderUrl);
  }

  function handleShopModeClick() {
    if (page.url.pathname === cartUrl) {
      closeCart();
    } else {
      openCart();
    }
  }

  //Color blind stuff
  let currentMode: ColorblindMode = $state('normal');
  const modes: ColorblindMode[] = ['normal', 'protanopia', 'deuteranopia', 'tritanopia', 'grayscale'];

  function isColorblindMode(value: string): value is ColorblindMode {
    return modes.includes(value as ColorblindMode);
  }

  onMount(() => {
    const saved = localStorage.getItem('colorblindMode');
    if (saved && isColorblindMode(saved)) {
      colorblindMode.set(saved);
    }
  });

  $effect(() => {
    const unsubscribe = colorblindMode.subscribe((mode) => {
      currentMode = mode;
      document.documentElement.className = '';
      document.documentElement.classList.add(`colorblind-${mode}`);
      localStorage.setItem('colorblindMode', mode);
    });
    return unsubscribe;
  });

  function toggleMode() {
    const nextIndex = (modes.indexOf(currentMode) + 1) % modes.length;
    colorblindMode.set(modes[nextIndex]);
  }

  let intervalId: number | null = null;

  function startStopRepeating(toggleDisco: () => void, delay = 100): void {
    if (intervalId === null) {
      intervalId = window.setInterval(toggleDisco, delay);
    } else {
      clearInterval(intervalId);
      intervalId = null;
    }
  }

  function discoooo() {
    startStopRepeating(toggleMode, 100);
  }
</script>

<!-- Colorblind Stuff -->
<svg width="0" height="0" style="position: absolute">
  <filter id="normal">
    <feColorMatrix
      type="matrix"
      values="1 0 0 0 0
                0 1 0 0 0
                0 0 1 0 0
                0 0 0 1 0"
    />
  </filter>

  <filter id="protanopia">
    <feColorMatrix
      type="matrix"
      values="0.152 1.053 -0.205 0 0
                0.114 0.786 0.100 0 0
                -0.004 0.048 0.956 0 0
                0 0 0 1 0"
    />
  </filter>

  <filter id="deuteranopia">
    <feColorMatrix
      type="matrix"
      values="0.367 0.861 -0.228 0 0
                0.280 0.673 0.047 0 0
                -0.012 0.043 0.969 0 0
                0 0 0 1 0"
    />
  </filter>

  <filter id="tritanopia">
    <feColorMatrix
      type="matrix"
      values="1.255 -0.077 -0.178 0 0
            -0.078 0.930 0.148 0 0
             0.004 0.691 0.305 0 0
             0 0 0 1 0"
    />
  </filter>
</svg>

<svelte:head>
  <link rel="icon" href={favicon} />
  <title>ShareTea</title>
</svelte:head>

<AppShell>
  <AppShellHeader>
    <div class="flex w-full items-center justify-between p-4">
      <img src={logo} alt="ShareTea Logo" class="h-6" />
      <div class="flex items-center gap-4">
        <IconButton
          icon={mdiPartyPopper}
          shape="round"
          size="medium"
          color="primary"
          onclick={discoooo}
          aria-label={colorBlindModeLabel}
        />
        <IconButton
          icon={mdiEye}
          shape="round"
          size="medium"
          color="primary"
          onclick={toggleMode}
          aria-label={colorBlindModeLabel}
        />
        <ThemeSwitcher />
        <div class="relative inline-block">
          <IconButton
            icon={shopModeIcon}
            shape="round"
            size="medium"
            color="primary"
            onclick={handleShopModeClick}
            aria-label={shopModeLabel}
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
