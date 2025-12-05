<script lang="ts">
  import home from '$lib/assets/home.webp';
  import {goto} from '$app/navigation';

  const orderUrl: string = '/kiosk/order';
</script>

<div class="max-h-screen" on:click={()=> goto(orderUrl)}>
  <img src={home} alt="boba gallery" class="absolute object-cover size-full"/>
  <div class="w-full bg-black/50 text-5xl flex justify-center py-10 absolute top-175">
    Click Anywhere to Begin
  </div>
</div>

