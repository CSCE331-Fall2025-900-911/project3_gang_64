<script lang="ts">
  import { getIngredients } from '$lib/api/ingredient.remote';
  import { Heading, IconButton, Input, LoadingSpinner, modalManager } from '@immich/ui';
  import { mdiMagnify, mdiPlus } from '@mdi/js';
  import { cubicInOut } from 'svelte/easing';
  import { fade } from 'svelte/transition';
  import CreateInventoryItem from './CreateInventoryItem.svelte';

  let ingredients = getIngredients();
  let searchTerm = $state('');
  let searchedIngredients = $derived(
    ingredients.current?.filter((ingredient) => ingredient.name.toUpperCase().includes(searchTerm.toUpperCase())) || [],
  );

  function showCreateModal() {
    modalManager.show(CreateInventoryItem);
  }
</script>

<div class="mb-6 flex items-center justify-between px-2">
  <Heading size="large">Inventory</Heading>
  <div class="flex w-1/3 items-center gap-2">
    <IconButton icon={mdiPlus} variant="filled" aria-label="Add Employee" style="p-4" onclick={showCreateModal} />
    <Input placeholder="Search" leadingIcon={mdiMagnify} bind:value={searchTerm} />
  </div>
</div>

{#if ingredients.loading}
  <div class="flex justify-center">
    <LoadingSpinner size="large" />
  </div>
{:else if ingredients.error}
  <p class="text-danger">Error loading ingredients: {ingredients.error.message}</p>
{:else}
  <table class="mt-4 w-full text-start">
    <thead class="mb-4 flex h-12 w-full rounded-md border bg-subtle">
      <tr class="flex w-full place-items-center text-center text-sm font-medium">
        <th class="w-6/12">Name</th>
        <th class="w-3/12">Category</th>
        <th class="w-2/12">Current Stock</th>
        <th class="w-2/12">Order Stock</th>
        <th class="w-2/12">Unit Price</th>
      </tr>
    </thead>
    <tbody class="dark:border-immich-dark-gray block w-full overflow-y-auto rounded-md border">
      {#each searchedIngredients as ingredient}
        <tr
          transition:fade={{ duration: 400, easing: cubicInOut }}
          class="dark:text-immich-dark-fg flex w-full place-items-center py-2 text-center odd:bg-subtle/80 even:bg-subtle/20"
        >
          <td class="w-6/12 pl-6 text-left">{ingredient.name}</td>
          <td class="w-3/12">{ingredient.category}</td>
          <td class="w-2/12">{ingredient.currentStock}</td>
          <td class="w-2/12">{ingredient.orderStock}</td>
          <td class="w-2/12">${ingredient.unitPrice.toFixed(2)}</td>
        </tr>
      {/each}
    </tbody>
  </table>
{/if}
