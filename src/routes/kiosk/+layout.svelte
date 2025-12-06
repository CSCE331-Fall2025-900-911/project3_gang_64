<script lang="ts">
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
    initializeTheme,
    Modal,
    ModalBody,
    ModalHeader,
    modalManager,
  } from '@immich/ui';
  import { mdiCartOutline, mdiTranslate, mdiWheelchair } from '@mdi/js';
  import { onMount } from 'svelte';
  import '../../app.css';
  import CartModal from './order/CartModal.svelte';
  import { onNavigate, goto } from '$app/navigation';

  let { children } = $props();

  initializeTheme();

  const timeOutLength = 12;
  let timer = $derived(timeOutLength);
  let showModal = $derived(false);

  function openCart() {
    modalManager.show(CartModal);
  }

  //timeout logic and set up
  const resetTimer = () => {
    timer = timeOutLength;
    showModal = false;
  };

  const resetTimerEvent = () => {
    if (!showModal) {
      resetTimer();
    }
  };

  const listenerSetup = () => {
    const events = ['mousemove', 'keydown', 'click', 'touchstart'];
    events.forEach((ev) => window.addEventListener(ev, resetTimerEvent));

    return () => events.forEach((ev) => window.removeEventListener(ev, resetTimerEvent));
  };

  function countD() {
    const listeners = listenerSetup();
    timer = timeOutLength;

    let countDown = setInterval(() => {
      --timer;
      if (!showModal && timer <= 10){
        showModal = true;
      }
      if (timer <= 0) {
        clearInterval(countDown);
        listeners();
        orderManager.clearOrder();
        showModal = false;
        window.location.href='/kiosk/home'

      }
    }, 1000);

    return () => {
      listeners();
      clearInterval(countDown);
    };
  }

  function timeOut() {
    if (window.location.pathname !== '/kiosk/home') {
      const runTimer = countD();

      return () => {
        runTimer();
      };
    } else return null;
  }

  onMount(() => {
    //timeout
    const time = timeOut();

    return time;
  });

  onNavigate(() => timeOut);


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
    <Modal class="w-90 text-center">
      <ModalHeader>
        <div class="my-3 text-4xl">Are you still there?</div>
      </ModalHeader>
      <ModalBody>
        <div class="flex flex-col justify-center text-3xl">
          Your order will be cleared in {timer} seconds
          <Button onclick={resetTimer} class="my-5">I'm still here!</Button>
        </div>
      </ModalBody>
    </Modal>
  {/if}

  {@render children?.()}
</AppShell>
