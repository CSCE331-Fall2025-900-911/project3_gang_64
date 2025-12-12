<script lang="ts">
  import home from '$lib/assets/home.webp';
  import logo from '$lib/assets/logo.png';
  import LanguageSelectModal from '$lib/components/LanguageSelectModal.svelte';
  import { localizeHref } from '$lib/i18n/runtime';
  import { t } from '$lib/utils/utils';
  import { Button, IconButton, modalManager } from '@immich/ui';
  import { mdiTranslate } from '@mdi/js';
</script>

<div class="fixed inset-0 z-50 flex flex-col overflow-hidden">
  <!-- Background image -->
  <img src={home} alt="boba gallery" class="absolute inset-0 z-0 size-full object-cover" />

  <!-- Dark overlay for better contrast -->
  <div class="absolute inset-0 z-10 bg-black/30"></div>

  <!-- Translation button - bottom right -->
  <div class="absolute right-6 bottom-6 z-30">
    <IconButton
      icon={mdiTranslate}
      size="giant"
      variant="outline"
      shape="round"
      onclick={() => modalManager.show(LanguageSelectModal)}
      aria-label={t('change_language_label')}
    />
  </div>

  <!-- Main content area - grows to fill space -->
  <div class="relative z-20 flex flex-1 flex-col items-center justify-center"></div>

  <!-- Bottom ribbon -->
  <div
    class="relative z-20 flex flex-col items-center gap-6 bg-linear-to-t from-black/80 to-black/60 px-8 py-10 backdrop-blur-sm"
  >
    <Button size="giant" onclick={() => (window.location.href = localizeHref('/kiosk/order'))} color="success"
      >{t('kiosk_tapToBegin')}</Button
    >

    <img src={logo} alt="Logo" class="h-16 object-contain opacity-90" />
  </div>
</div>
