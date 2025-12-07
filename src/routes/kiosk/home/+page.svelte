<script lang="ts">
  import home from '$lib/assets/home.webp';
</script>

<div class="fix inset-0 z-50 overflow-hidden" on:click={() => (window.location.href = '/kiosk/order')}>
  <img src={home} alt="boba gallery" class="absolute z-30 size-full object-cover" />
  <div class="absolute top-150 z-35 flex w-full justify-center bg-black/50 py-10 text-5xl">Click Anywhere to Begin</div>
</div>
