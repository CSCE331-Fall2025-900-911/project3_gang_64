<script lang="ts">
  import home from '$lib/assets/home.webp';
  import {goto} from '$app/navigation';

  const orderUrl: string = '/kiosk/order';
</script>

<div class="bg-amber-50 w-full h-full z-50">
  <img src={logo} alt="ShareTea logo" onclick={() => goto(orderUrl)}/>
</div>

