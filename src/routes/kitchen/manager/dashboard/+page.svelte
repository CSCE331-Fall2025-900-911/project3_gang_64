<script lang='ts'>
  import { Icon, LoadingSpinner } from "@immich/ui";
  import {mdiWeatherHurricane} from "@mdi/js";
  import {getOrderCountDay , getDailyRevenue} from '$lib/api/orders.remote'
  
  let dailyOrders = getOrderCountDay();
  let dailyRevenue = getDailyRevenue();
  
  const debug = () => {
    console.log(dailyRevenue.current);
  };

  //weather place holders
  let temp = 67;
  let tempColor = "primary"

  if(temp < 50) {
    tempColor = "cyan-300"
  }
</script>

<div class="flex flex-row justify-around">
  <div class = "min-h-[33dvh] bg-subtle min-w-[20dvw] rounded-md p-1">
    <h1 class="text-primary text-lg text-center" onclick={debug}>Daily Revenue</h1>
    {#if dailyRevenue.loading}
      <LoadingSpinner/>
    {:else}
          <h1 class = 'text-center text-6xl align-middle mt-19 mx-2'>${dailyRevenue.current?.toFixed(2)}</h1>
    {/if}
  </div>

  <div class = "min-h-[33dvh] bg-subtle min-w-[20dvw] rounded-md flex flex-col p-1">
    <h1 class="text-primary text-lg text-center">Orders Today</h1>
    <h1 class = 'text-center text-9xl align-middle mt-10'>{dailyOrders.current}</h1>
  </div>

  <div class = "min-h-[33dvh] bg-subtle min-w-[20dvw] rounded-md flex flex-col items-center justify-evenly">
    <h1 class="text-primary text-lg">Weather</h1>
    <Icon icon={mdiWeatherHurricane} size='200'/>
    <div class="flex justify-between w-full">
      <h2 class="text-{tempColor} mx-2">{temp} &degF</h2>
      <h2 class="text-primary mx-2">Hurricane</h2>
    </div>
  </div>
</div>