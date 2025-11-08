<script lang="ts">
  import { getEmployees } from '$lib/api/employee.remote';
  import type { Employee } from '$lib/db/types';
  import { Heading, IconButton, Input, LoadingSpinner, modalManager } from '@immich/ui';
  import { mdiMagnify, mdiPencil, mdiPlus, mdiTrashCan } from '@mdi/js';
  import { cubicInOut } from 'svelte/easing';
  import { fade } from 'svelte/transition';
  import EmployeeModal from './EmployeeModal.svelte';

  let employees = getEmployees();
  let searchTerm = $state('');
  let searchedEmployees = $derived(
    employees.current?.filter(
      (employee) =>
        employee.email.toUpperCase().includes(searchTerm.toUpperCase()) ||
        employee.name.toUpperCase().includes(searchTerm.toUpperCase()),
    ) || [],
  );

  function showCreateModal() {
    modalManager.show(EmployeeModal, { mode: { type: 'new' } });
  }

  function showEditModal(employee: Employee) {
    modalManager.show(EmployeeModal, { mode: { type: 'edit', item: employee } });
  }

  async function showDeleteModal(employee: Employee) {
    const confirm = await modalManager.showDialog({
      title: 'Delete Employee',
      prompt: `Are you sure you want to delete ${employee.name}?`,
      confirmText: 'Delete',
      confirmColor: 'danger',
    });

    if (confirm) {
      // TODO: Handle deletion logic here
    }
  }
</script>

<div class="mb-6 flex items-center justify-between">
  <Heading size="large">Employees</Heading>
  <div class="flex w-1/3 items-center gap-2">
    <IconButton icon={mdiPlus} variant="filled" aria-label="Add Employee" style="p-4" onclick={showCreateModal} />
    <Input placeholder="Search" leadingIcon={mdiMagnify} bind:value={searchTerm} />
  </div>
</div>

{#if employees.loading}
  <div class="flex justify-center">
    <LoadingSpinner size="large" />
  </div>
{:else if employees.error}
  <p class="text-danger">Error loading employees: {employees.error.message}</p>
{:else}
  <table class="mt-4 w-full text-start">
    <thead class="mb-4 flex h-12 w-full rounded-md border bg-subtle">
      <tr class="flex w-full place-items-center text-center text-sm font-medium">
        <th class="w-3/12">Name</th>
        <th class="w-4/12 text-left">Email</th>
        <th class="w-3/12">Role</th>
        <th class="w-2/12">Actions</th>
      </tr>
    </thead>
    <tbody class="dark:border-immich-dark-gray block w-full overflow-y-auto rounded-md border">
      {#each searchedEmployees as employee}
        <tr
          transition:fade={{ duration: 400, easing: cubicInOut }}
          class="dark:text-immich-dark-fg flex w-full cursor-pointer place-items-center py-2 text-center odd:bg-subtle/80 even:bg-subtle/20 hover:bg-primary/10"
        >
          <td class="w-3/12">{employee.name}</td>
          <td class="w-4/12 text-left">{employee.email}</td>
          <td class="w-3/12">{employee.role}</td>
          <td class="flex w-2/12 justify-center gap-2">
            <IconButton icon={mdiPencil} aria-label="Edit Employee" onclick={() => showEditModal(employee)} />
            <IconButton
              icon={mdiTrashCan}
              aria-label="Delete Employee"
              color="danger"
              onclick={() => showDeleteModal(employee)}
            />
          </td>
        </tr>
      {/each}
    </tbody>
  </table>
{/if}
