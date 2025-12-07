<script lang="ts">
  import { onNavigate } from '$app/navigation';
  import favicon from '$lib/assets/favicon.svg';
  import logo from '$lib/assets/logo.png';
  import AccessibiltyModal from '$lib/components/AccessibiltyModal.svelte';
  import ColorblindFilter from '$lib/components/ColorblindFilter.svelte';
  import LanguageSelectModal from '$lib/components/LanguageSelectModal.svelte';
  import { orderManager } from '$lib/managers/order_manager.svelte';
  import { t } from '$lib/utils/utils';
  import {
    AppShell,
    AppShellHeader,
    Avatar,
    Button,
    IconButton,
    Modal,
    ModalBody,
    ModalFooter,
    modalManager,
  } from '@immich/ui';
  import { mdiCartOutline, mdiChatQuestion, mdiTranslate, mdiWheelchair } from '@mdi/js';
  import { onMount } from 'svelte';
  import CartModal from './CartModal.svelte';

  let { children } = $props();

  const TIMEOUT_SECONDS = 30;
  const SHOW_MODAL_AT = 10;

  let timer = $state(TIMEOUT_SECONDS);
  let showModal = $state(false);
  let intervalId: ReturnType<typeof setInterval> | null = null;
  let isTimerActive = false;

  function openCart() {
    modalManager.show(CartModal);
  }

  function stopTimer() {
    if (intervalId) {
      clearInterval(intervalId);
      intervalId = null;
    }
    isTimerActive = false;
  }

  function startTimer() {
    stopTimer();
    timer = TIMEOUT_SECONDS;
    showModal = false;
    isTimerActive = true;

    intervalId = setInterval(() => {
      timer--;
      console.log('Timer:', timer);

      if (timer <= SHOW_MODAL_AT && !showModal) {
        showModal = true;
      }

      if (timer <= 0) {
        stopTimer();
        orderManager.clearOrder();
        showModal = false;
        window.location.href = '/kiosk/home';
      }
    }, 1000);
  }

  function handleUserActivity() {
    // Only reset timer if modal is NOT showing
    if (isTimerActive && !showModal) {
      timer = TIMEOUT_SECONDS;
    }
  }

  function handleStillHere() {
    // User clicked "I'm still here" - restart the whole timer
    timer = TIMEOUT_SECONDS;
    showModal = false;
  }

  function setupActivityListeners() {
    const events = ['mousemove', 'keydown', 'click', 'touchstart'];
    events.forEach((ev) => window.addEventListener(ev, handleUserActivity));
    return () => events.forEach((ev) => window.removeEventListener(ev, handleUserActivity));
  }

  onMount(() => {
    let cleanupListeners: (() => void) | null = null;

    cleanupListeners = setupActivityListeners();
    startTimer();

    return () => {
      stopTimer();
      cleanupListeners?.();
    };
  });

  onNavigate(() => {
    // Clean up and restart timer on navigation (if not going to home)
    stopTimer();

    // Use setTimeout to check pathname after navigation completes
    setTimeout(() => {
      if (window.location.pathname !== '/kiosk/home') {
        startTimer();
      }
    }, 0);
  });
</script>

<ColorblindFilter />

<svelte:head>
  <link rel="icon" href={favicon} />
  <title>{t('title')}</title>
</svelte:head>

<AppShell>
  <AppShellHeader>
    <div class="flex w-full items-center justify-between p-4" role="navigation">
      <img src={logo} alt={t('logoAlt')} class="h-6" />
      <div class="flex items-center gap-4">
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
  {#if showModal}
    <Modal title={t('stillthere_modal_title')} icon={mdiChatQuestion}>
      <ModalBody>
        <p class="mt-2">{t('stillthere_modal_message', { seconds: timer })}</p>
      </ModalBody>
      <ModalFooter>
        <Button onclick={handleStillHere} fullWidth>{t('stillthere_modal_button')}</Button>
      </ModalFooter>
    </Modal>
  {/if}

  {@render children?.()}
</AppShell>
