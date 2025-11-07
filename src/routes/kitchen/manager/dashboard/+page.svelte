<script>
  import { Icon } from "@immich/ui";
  import {mdiWeatherHurricane} from "@mdi/js";
  import {getOrderCountDay} from '$lib/api/orders.remote'
  let temp = 67;
  let tempColor = "primary"


  //weather api calls

  let dailyOrders = getOrderCountDay().current;

  if(temp < 50) {
    tempColor = "cyan-300"
  }
</script>

<div class="flex flex-row justify-around">
  <div class = "min-h-[33dvh] bg-subtle min-w-[20dvw] rounded-md">
    <h1 class="text-primary text-lg text-center">Daily Revenue</h1>
  </div>

  <div class = "min-h-[33dvh] bg-subtle min-w-[20dvw] rounded-md flex flex-col ">
    <h1 class="text-primary text-lg text-center">Orders Today</h1>
    <h1 class = 'text-center text-9xl align-middle mt-10'>{dailyOrders}</h1>
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