<script lang="ts">
  import { deleteMenuItem, getMenu } from '$lib/api/menu.remote';
  import { Table, TableBody, TableCell, TableHeader, TableHeaderCell, TableRow } from '$lib/components/Table';
  import type { MenuItem } from '$lib/db/types';
  import { Heading, IconButton, Input, LoadingSpinner, modalManager } from '@immich/ui';
  import { mdiMagnify, mdiTrashCan } from '@mdi/js';

  let menu = getMenu();
  let searchTerm = $state('');
  let searchedMenuItems = $derived(
    menu.current?.filter(
      (item) =>
        item.name.toUpperCase().includes(searchTerm.toUpperCase()) ||
        item.category.toUpperCase().includes(searchTerm.toUpperCase()),
    ) || [],
  );

  async function showDeleteModal(item: MenuItem) {
    const confirm = await modalManager.showDialog({
      title: 'Delete Menu Item',
      prompt: `Are you sure you want to delete ${item.name}?`,
      confirmText: 'Delete',
      confirmColor: 'danger',
      icon: mdiTrashCan,
    });

    if (confirm) {
      await deleteMenuItem(item.id);
    }
  }
</script>

<div class="mb-6 flex items-center justify-between">
  <Heading size="large">Menu Items</Heading>
  <div class="flex w-1/3 items-center gap-2">
    <!-- TODO: Add create menu item -->
    <!-- <IconButton icon={mdiPlus} variant="filled" aria-label="Add Menu Item" style="p-4" /> -->
    <Input placeholder="Search" leadingIcon={mdiMagnify} bind:value={searchTerm} />
  </div>
</div>

{#if menu.loading}
  <div class="flex justify-center">
    <LoadingSpinner size="large" />
  </div>
{:else if menu.error}
  <p class="text-danger">Error loading menu: {menu.error.message}</p>
{:else}
  <Table>
    <TableHeader>
      <TableHeaderCell width="w-5/12">Name</TableHeaderCell>
      <TableHeaderCell width="w-4/12">Category</TableHeaderCell>
      <TableHeaderCell width="w-3/12">Price</TableHeaderCell>
      <TableHeaderCell width="w-2/12">Actions</TableHeaderCell>
    </TableHeader>
    <TableBody>
      {#each searchedMenuItems as item}
        <TableRow>
          <TableCell width="w-5/12">{item.name}</TableCell>
          <TableCell width="w-4/12">{item.category}</TableCell>
          <TableCell width="w-3/12">${item.price.toFixed(2)}</TableCell>
          <!-- TODO: Implement edit functionality -->
          <TableCell width="w-2/12" class="flex justify-center gap-2">
            <!-- <IconButton icon={mdiPencil} aria-label="Edit Menu Item" /> -->
            <IconButton
              icon={mdiTrashCan}
              aria-label="Delete Menu Item"
              color="danger"
              onclick={() => showDeleteModal(item)}
            />
          </TableCell>
        </TableRow>
      {/each}
    </TableBody>
  </Table>
{/if}
