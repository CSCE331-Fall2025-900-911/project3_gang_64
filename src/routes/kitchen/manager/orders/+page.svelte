<script lang="ts">
  import { Table, TableBody, TableBodyCell, TableBodyRow, TableHead, TableHeadCell, Checkbox, TableSearch } from "flowbite-svelte"; 
  import {getOrders} from "$lib/api/orders.remote"
  import { type OrderRow} from "$lib/db/types";
  import { number } from "valibot";
  import { Button } from "@immich/ui";

  async function loadOrders() {
    try {
      let orders = await getOrders();
      console.log(orders);
    }
    catch (err) {
      console.error("fuck", err);
    }
  }

  loadOrders()
</script>

<Table>
  <TableHead>
    <TableHeadCell>Order #</TableHeadCell>
    <TableHeadCell>Amount</TableHeadCell>
    <TableHeadCell>Time</TableHeadCell>
    <TableHeadCell>Name</TableHeadCell>
    <TableHeadCell>Customer Contact</TableHeadCell>
    <TableHeadCell>Payment Method</TableHeadCell>
  </TableHead>
</Table>

<Button on:click={loadOrders}>Click to load order rows to console</Button>