<script lang="ts">
  import home from '$lib/assets/home.webp';
  import {goto} from '$app/navigation';

  const orderUrl: string = '/kiosk/order';
</script>

<div class="z-50 fix inset-0 overflow-hidden" on:click={()=> goto(orderUrl)}>
  <img src={home} alt="boba gallery" class="absolute object-cover size-full z-30"/>
  <div class="w-full bg-black/50 text-5xl flex justify-center py-10 absolute top-150 z-35">
    Click Anywhere to Begin
  </div>
</div>

