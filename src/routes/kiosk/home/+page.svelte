<script lang="ts">
  import home from '$lib/assets/home.webp';
  import { t } from '$lib/utils/utils'
  import {goto} from '$app/navigation'
</script>

<div class="fix inset-0 z-50 overflow-hidden" on:click={() => goto('/kiosk/order')}>
  <img src={home} alt="boba gallery" class="absolute z-30 size-full object-cover" />
  <div class="absolute top-150 z-35 flex w-full justify-center bg-black/50 py-10 text-5xl">{t('kiosk_timeOut')}</div>
</div>
asdfas